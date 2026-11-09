#!/usr/bin/env node
/* =====================================================================
   audit_crowd_geo2.mjs — ĐO CHỒNG LẤN ĐÁM ĐÔNG cho Chợ Hòa Bình 3D
   *** SỐ ĐO **TRƯỚC** ĐỢT SỬA GEOMETRY-2 (baseline, chưa sửa gì) ***
   KHÔNG sửa index.html — chỉ nạp game vào harness Node (stub
   DOM/WebGL như scripts/diag_runtime.mjs, theo mẫu scripts/
   check_sweep3.mjs) rồi:
     1. Chạy mô phỏng FRAMES frame (mặc định 1800) với dt CỐ ĐỊNH 1/30
        (vá clock.getDelta trong epilogue cùng scope module game +
        performance.now giả tiến theo frame) và save sạch
        (localStorage trống -> seed save mặc định của game).
        Math.random được gieo hạt cố định (mulberry32) để lần đo
        lặp lại ra cùng một thực tại. Chế độ giữ nguyên mặc định
        của game: CHỢ ĐÊM (isNight=true, crowdLevel=1.0 — đông nhất).
     2. Thu thập: statics (kind + g.position, chụp 1 lần — người tĩnh
        không di chuyển) và wanderers (vị trí + mode, lấy mẫu mỗi
        SAMPLE_EVERY frame, chỉ người active + visible).
     3. Tính:
        - Mọi cặp statics có khoảng cách XZ < 0.6u (kèm kind, tọa độ
          làm tròn 1 số lẻ, nhóm theo khu bằng phân khu npcZoneOf —
          bản sao thuần không có tác dụng phụ đếm; NPC_ZONE_COUNT
          gốc của game cũng được in kèm).
        - Wanderer chồng nhau: theo từng mẫu, số cặp XZ < 0.5u;
          mẫu tệ nhất + điểm nóng (trung điểm cặp làm tròn về lưới
          2u, đếm tần suất cặp-mẫu tại ô).
        - Wanderer browse: tại cùng 1 mẫu, số wanderer cùng browse
          tại cùng 1 sạp (theo browsePt sx/sz) — liệt kê sạp có
          > 2 người cùng ngắm.
        - Wanderer–statics: số cặp XZ < 0.45u trong các mẫu (người
          đi bộ đứng lọt vào người tĩnh).
        Mọi khoảng cách chính là XZ (mặt đất, như các audit trước);
        mỗi cặp còn ghi dy + khoảng cách 3D và cờ "cùng cao độ"
        (|dy| <= 1.5) để phân biệt chồng thật với chồng hình chiếu
        khác tầng (cầu/sân thượng).
   Cách dùng: node scripts/audit_crowd_geo2.mjs
   Biến môi trường: AUDIT_FRAMES (1800), AUDIT_SAMPLE_EVERY (30),
   AUDIT_SEED (20261109), GAME_ROOT, SRC_FILE như các harness khác.
   Đầu ra: JSON tóm tắt ra stdout + bản đầy đủ ghi vào
   scripts/audit_crowd_geo2_result.json. Thoát 0 = đo xong;
   2 = lỗi init; 3 = lỗi khi chạy frame; 9 = thiếu harness/hook.
   ===================================================================== */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = process.env.GAME_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const WORK = '/tmp/diag-runtime-work';
const FRAMES = parseInt(process.env.AUDIT_FRAMES || '1800', 10);
const SAMPLE_EVERY = parseInt(process.env.AUDIT_SAMPLE_EVERY || '30', 10);
const FIXED_DT = 1 / 30;
const SEED = parseInt(process.env.AUDIT_SEED || '20261109', 10) >>> 0;
const OUT_PATH = path.join(ROOT, 'scripts', 'audit_crowd_geo2_result.json');
const log = (...a) => console.error('[crowd2]', ...a);

// ---------- 1) stub DOM/WebGL/fetch: cắt từ diag_runtime.mjs như check_sweep3 ----------
const diagSrc = fs.readFileSync(path.join(ROOT, 'scripts/diag_runtime.mjs'), 'utf8');
const stubEnd = diagSrc.indexOf('// ---------- chuẩn bị bản game đã vá import');
if (stubEnd < 0) { log('không tìm thấy marker vá import trong diag_runtime.mjs'); process.exit(9); }
fs.mkdirSync(WORK, { recursive: true });
const stubsPath = path.join(WORK, 'diag_stubs.mjs');
let stubSrc = diagSrc.slice(0, stubEnd);
stubSrc = stubSrc.replace(
  "const ROOT = process.env.GAME_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');",
  `const ROOT = ${JSON.stringify(ROOT)};`);
fs.writeFileSync(stubsPath, stubSrc);
await import(stubsPath);

// ---------- 2) môi trường đo xác định: save sạch + RNG gieo hạt + rAF/now giả ----------
try { globalThis.localStorage.removeItem('chohb3d-v1'); } catch (e) {} // save sạch bất kể SEED_SAVE bên ngoài
{ // mulberry32 — thay Math.random TRƯỚC khi nạp game để mọi tung hứng reproducible
  let s = SEED >>> 0;
  Math.random = () => {
    s = (s + 0x6D2B79F5) | 0;
    let t = Math.imul(s ^ (s >>> 15), 1 | s);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const myRaf = [];
globalThis.requestAnimationFrame = cb => { myRaf.push(cb); return myRaf.length; };
globalThis.cancelAnimationFrame = () => {};
let fakeNowMs = 100000; // performance.now giả: tiến đúng 1000/30 ms mỗi frame bơm
try { performance.now = () => fakeNowMs; } catch (e) { log('không vá được performance.now:', e && e.message); }

// ---------- 3) vá import của index.html (y hệt diag/check_sweep3) + epilogue đo ----------
const raw = fs.readFileSync(path.join(ROOT, process.env.SRC_FILE || 'index.html'), 'utf8');
const mStart = raw.indexOf('<script type="module">');
const mEnd = raw.indexOf('</script>', mStart);
if (mStart < 0 || mEnd < 0) { log('không trích được module script từ index.html'); process.exit(9); }
let code = raw.slice(mStart + '<script type="module">'.length, mEnd);
code = code.replace(/import \* as THREE from 'three';/, '');
code = code.replace(/import \{ GLTFLoader \} from 'three\/addons\/loaders\/GLTFLoader\.js';/, '');
const header = `
import * as _THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
class FakeWebGLRenderer {
  constructor(opts = {}) {
    this.domElement = document.createElement('canvas');
    this.shadowMap = { enabled: false, type: 0 };
    this.outputColorSpace = 0; this.toneMapping = 0; this.toneMappingExposure = 1;
    this.info = { render: { calls: 0, triangles: 0 }, memory: { geometries: 0, textures: 0 } };
    this.capabilities = { isWebGL2: true };
  }
  setPixelRatio(v) { this._pr = v; } setSize() {} setViewport() {} setScissor() {}
  render() { this.info.render.calls++; }
  dispose() {} setAnimationLoop() {}
  getContext() { return null; }
  forceContextLoss() {}
}
const THREE = { ..._THREE, WebGLRenderer: FakeWebGLRenderer };
`;
code += `
;{ // ===== EPILOGUE AUDIT CROWD GEO-2 (chỉ-đo, không đổi hành vi game ngoài đồng hồ) =====
  try { clock.getDelta = () => { clock.elapsedTime += ${FIXED_DT}; return ${FIXED_DT}; }; } catch (e) {}
  // npcZoneOf bản sao THUẦN (nguyên văn logic phân khu, bỏ dòng tăng NPC_ZONE_COUNT)
  const __zonePure = (x, z) => {
    let zn;
    if (z >= 12 && z <= 28 && x >= -34 && x <= 34) zn = 'nha-long';
    else if (x < -36 && z > -14 && z < 18) zn = 'duong-vao';
    else if (Math.hypot(x + 24, z + 6) < 15) zn = 'bung-binh';
    else if (Math.abs(x) <= 20 && z <= -2 && z >= -31) zn = 'thang';
    else if (z < -31) zn = 'doi';
    else if (z >= 28 || (z > 6 && (x > 34 || x < -34))) zn = 'ven-cho';
    else zn = 'pho-cho-dem';
    return zn;
  };
  globalThis.__crowd = {
    zoneOf: __zonePure,
    meta: () => ({
      isNight, crowdLevel: (typeof crowdLevelNow === 'function' ? crowdLevelNow() : null),
      npcZoneCount: Object.assign({}, NPC_ZONE_COUNT),
      npcStats: (typeof window !== 'undefined' && window.NPC_STATS) ? Object.assign({}, window.NPC_STATS) : null,
      counts: { wanderers: wanderers.length, statics: statics.length, stalls: stalls.length },
    }),
    statics: () => statics.map((st, i) => ({
      i, kind: st.kind, sched: st.sched, active: !!st.active, visible: !!(st.g && st.g.visible),
      x: st.g ? st.g.position.x : null, y: st.g ? st.g.position.y : null, z: st.g ? st.g.position.z : null,
    })),
    stalls: () => stalls.map(s => ({ id: s.id, x: s.x, z: s.z, fx: s.front.x, fz: s.front.z, nightOnly: !!s.nightOnly })),
    wanderers: () => wanderers.map((w, i) => ({
      i, sched: w.sched, active: !!w.active, visible: !!(w.g && w.g.visible), mode: w.mode,
      x: w.g ? w.g.position.x : null, y: w.g ? w.g.position.y : null, z: w.g ? w.g.position.z : null,
      browse: (w.mode === 'browse' && w.browsePt) ? { x: w.browsePt.x, z: w.browsePt.z, sx: w.browsePt.sx, sz: w.browsePt.sz } : null,
    })),
  };
}
`;
const patchedPath = path.join(WORK, 'game_crowd2.mjs');
fs.writeFileSync(patchedPath, header + code);
const t0 = Date.now();
try {
  await import(patchedPath);
  log('MODULE INIT OK sau', Date.now() - t0, 'ms — raf chờ:', myRaf.length);
} catch (e) {
  console.error('[crowd2] *** NGOẠI LỆ TRONG INIT ***');
  console.error(e && e.stack || e);
  process.exit(2);
}
if (!globalThis.__crowd) { log('thiếu hook __crowd sau init'); process.exit(9); }
const C = globalThis.__crowd;
// chờ GLB/tài sản bất đồng bộ lắng xuống như check_sweep3 (800ms) + nới thêm cho xe/tuyến phụ
await new Promise(r => setTimeout(r, 1200));

// ---------- 4) chụp statics + mô phỏng 1800 frame, lấy mẫu wanderers mỗi 30 frame ----------
const r1 = v => Math.round(v * 10) / 10, r2 = v => Math.round(v * 100) / 100, r3 = v => Math.round(v * 1000) / 1000;
const meta0 = C.meta();
const staticsSnap = C.statics();
const stallsSnap = C.stalls();
const stallIdByFrontPt = new Map(); // browsePt sx/sz chính là s.x/s.z của sạp
for (const s of stallsSnap) stallIdByFrontPt.set(s.x.toFixed(2) + ',' + s.z.toFixed(2), s.id);
log('statics =', staticsSnap.length, '| wanderers =', meta0.counts.wanderers, '| stalls =', stallsSnap.length,
  '| isNight =', meta0.isNight, '| crowdLevel =', meta0.crowdLevel);

const samples = [];
function takeSample(frame) {
  const ws = C.wanderers().filter(w => w.active && w.visible && w.x !== null);
  samples.push({
    frame, tSim: r2(frame * FIXED_DT),
    wanderers: ws.map(w => ({
      i: w.i, mode: w.mode, x: w.x, y: w.y, z: w.z,
      stallId: w.browse ? (stallIdByFrontPt.get(w.browse.sx.toFixed(2) + ',' + w.browse.sz.toFixed(2)) || ('@' + w.browse.sx + ',' + w.browse.sz)) : null,
      sx: w.browse ? w.browse.sx : null, sz: w.browse ? w.browse.sz : null,
    })),
  });
}
takeSample(0);
let simError = null;
for (let f = 1; f <= FRAMES; f++) {
  fakeNowMs += 1000 * FIXED_DT;
  const cbs = myRaf.splice(0, myRaf.length);
  if (!cbs.length) { simError = 'hết callback rAF tại frame ' + f + ' — animate đã dừng'; break; }
  try { for (const cb of cbs) cb(fakeNowMs); }
  catch (e) { simError = 'NGOẠI LỆ ANIMATE frame ' + f + ': ' + (e && e.stack || e); break; }
  if (f % SAMPLE_EVERY === 0) takeSample(f);
  if (f % 150 === 0) await new Promise(r => setTimeout(r, 0)); // nhường event loop cho nạp GLB bất đồng bộ
}
if (simError) { console.error('[crowd2] ***', simError); }
const metaEnd = C.meta();
log('mô phỏng xong:', samples.length, 'mẫu | wanderers cuối =', metaEnd.counts.wanderers,
  '| statics cuối =', metaEnd.counts.statics, simError ? '| LỖI: ' + simError : '');

// ---------- 5a) cặp statics < 0.6u ----------
// dy/sameLevel là phân loại 3 trạng thái: y của statics luôn hữu hạn, nhưng
// y của wanderer thì KHÔNG (xem meta.wandererY — lỗi routeY/rt của game:
// điểm tuyến sau map luôn có length 3 nên routeY trả pt[2]=undefined cho
// tuyến không ghi y; y thành NaN sau nhịp lerp đầu). dy=null/sameLevel=null
// nghĩa là KHÔNG BIẾT cao độ — không được đọc thành "khác tầng".
const lvlOf = (ya, yb) => {
  if (!Number.isFinite(ya) || !Number.isFinite(yb)) return { dy: null, d3: null, sameLevel: null };
  const dy = Math.abs(ya - yb);
  return { dy: r2(dy), d3: null, sameLevel: dy <= 1.5 };
};
const actStatics = staticsSnap.filter(s => s.active && s.visible && s.x !== null);
const stPairs = [];
for (let a = 0; a < actStatics.length; a++) for (let b = a + 1; b < actStatics.length; b++) {
  const A = actStatics[a], B = actStatics[b];
  const d = Math.hypot(A.x - B.x, A.z - B.z);
  if (d < 0.6) {
    const mx = (A.x + B.x) / 2, mz = (A.z + B.z) / 2, lv = lvlOf(A.y, B.y);
    stPairs.push({
      a: A.i, b: B.i, kindA: A.kind, kindB: B.kind, d: r3(d),
      d3: lv.dy === null ? null : r3(Math.hypot(A.x - B.x, A.y - B.y, A.z - B.z)), dy: lv.dy, sameLevel: lv.sameLevel,
      ax: r1(A.x), az: r1(A.z), bx: r1(B.x), bz: r1(B.z),
      zone: C.zoneOf(mx, mz), zoneA: C.zoneOf(A.x, A.z), zoneB: C.zoneOf(B.x, B.z),
    });
  }
}
stPairs.sort((p, q) => p.d - q.d);
const stPairsByZone = {};
for (const p of stPairs) stPairsByZone[p.zone] = (stPairsByZone[p.zone] || 0) + 1;

// ---------- 5b/c/d) theo mẫu: wanderer–wanderer, browse chung sạp, wanderer–statics ----------
const cellOf = (x, z) => ({ cx: Math.round(x / 2) * 2, cz: Math.round(z / 2) * 2 });
const wwPerSample = [], browseEvents = [], wsPerSample = [];
const browseCtx = { browseWandererSamples: 0, maxSimultaneousAny: 0, groupsOf2: 0 };
const wwCells = new Map(), wsCells = new Map(); // key "cx,cz" -> {cx,cz,pairSamples,sampleSet}
const wwZonePairs = {}, wsZonePairs = {};
const zoneWandererSum = {}; let zoneSampleN = 0;
function bumpCell(map, mx, mz, frame) {
  const { cx, cz } = cellOf(mx, mz), k = cx + ',' + cz;
  let c = map.get(k); if (!c) { c = { cx, cz, pairSamples: 0, frames: new Set(), zone: C.zoneOf(cx, cz) }; map.set(k, c); }
  c.pairSamples++; c.frames.add(frame);
}
for (const sm of samples) {
  const ws = sm.wanderers;
  zoneSampleN++;
  for (const w of ws) { const zn = C.zoneOf(w.x, w.z); zoneWandererSum[zn] = (zoneWandererSum[zn] || 0) + 1; }
  // wanderer–wanderer < 0.5
  const pairs = [];
  for (let a = 0; a < ws.length; a++) for (let b = a + 1; b < ws.length; b++) {
    const A = ws[a], B = ws[b], d = Math.hypot(A.x - B.x, A.z - B.z);
    if (d < 0.5) {
      const mx = (A.x + B.x) / 2, mz = (A.z + B.z) / 2, lv = lvlOf(A.y, B.y);
      pairs.push({ a: A.i, b: B.i, d: r3(d), dy: lv.dy, sameLevel: lv.sameLevel, ax: r1(A.x), az: r1(A.z), bx: r1(B.x), bz: r1(B.z), modeA: A.mode, modeB: B.mode });
      bumpCell(wwCells, mx, mz, sm.frame);
      const zn = C.zoneOf(mx, mz); wwZonePairs[zn] = (wwZonePairs[zn] || 0) + 1;
    }
  }
  const lvlCount = arr => ({
    sameLevelPairs: arr.filter(p => p.sameLevel === true).length,
    diffLevelPairs: arr.filter(p => p.sameLevel === false).length,
    unknownLevelPairs: arr.filter(p => p.sameLevel === null).length,
  });
  wwPerSample.push({ frame: sm.frame, tSim: sm.tSim, wanderers: ws.length, pairCount: pairs.length, ...lvlCount(pairs), pairs });
  // browse chung sạp (cùng sx/sz tại cùng mẫu) + thống kê ngữ cảnh browse
  const byStall = new Map();
  for (const w of ws) if (w.mode === 'browse' && w.sx !== null) {
    browseCtx.browseWandererSamples++;
    const k = w.sx.toFixed(2) + ',' + w.sz.toFixed(2);
    if (!byStall.has(k)) byStall.set(k, { stallId: w.stallId, sx: w.sx, sz: w.sz, idxs: [] });
    byStall.get(k).idxs.push(w.i);
  }
  for (const g of byStall.values()) {
    if (g.idxs.length > browseCtx.maxSimultaneousAny) browseCtx.maxSimultaneousAny = g.idxs.length;
    if (g.idxs.length === 2) browseCtx.groupsOf2++;
    if (g.idxs.length > 2)
      browseEvents.push({ frame: sm.frame, tSim: sm.tSim, stallId: g.stallId, sx: g.sx, sz: g.sz, count: g.idxs.length, wandererIdxs: g.idxs });
  }
  // wanderer–statics < 0.45
  const wsp = [];
  for (const w of ws) for (const st of actStatics) {
    const d = Math.hypot(w.x - st.x, w.z - st.z);
    if (d < 0.45) {
      const mx = (w.x + st.x) / 2, mz = (w.z + st.z) / 2, lv = lvlOf(w.y, st.y);
      wsp.push({ w: w.i, st: st.i, kind: st.kind, d: r3(d), dy: lv.dy, sameLevel: lv.sameLevel, wx: r1(w.x), wz: r1(w.z), sx: r1(st.x), sz: r1(st.z), mode: w.mode });
      bumpCell(wsCells, mx, mz, sm.frame);
      const zn = C.zoneOf(mx, mz); wsZonePairs[zn] = (wsZonePairs[zn] || 0) + 1;
    }
  }
  wsPerSample.push({ frame: sm.frame, tSim: sm.tSim, pairCount: wsp.length, ...lvlCount(wsp), pairs: wsp });
}
const worstWW = wwPerSample.reduce((m, s) => (s.pairCount > (m ? m.pairCount : -1) ? s : m), null);
const worstWS = wsPerSample.reduce((m, s) => (s.pairCount > (m ? m.pairCount : -1) ? s : m), null);
const cellsSorted = map => [...map.values()].map(c => ({ cell: '(' + c.cx + ',' + c.cz + ')', cx: c.cx, cz: c.cz, zone: c.zone, pairSamples: c.pairSamples, distinctSamples: c.frames.size }))
  .sort((a, b) => b.pairSamples - a.pairSamples || b.distinctSamples - a.distinctSamples);
const wwHot = cellsSorted(wwCells), wsHot = cellsSorted(wsCells);
// gộp browse theo sạp
const browseByStall = new Map();
for (const e of browseEvents) {
  let g = browseByStall.get(e.stallId);
  if (!g) { g = { stallId: e.stallId, sx: e.sx, sz: e.sz, zone: C.zoneOf(e.sx, e.sz), maxSimultaneous: 0, samplesOver2: 0, worstFrame: null, worstIdxs: [] }; browseByStall.set(e.stallId, g); }
  g.samplesOver2++;
  if (e.count > g.maxSimultaneous) { g.maxSimultaneous = e.count; g.worstFrame = e.frame; g.worstIdxs = e.wandererIdxs; }
}
const browseAgg = [...browseByStall.values()].sort((a, b) => b.maxSimultaneous - a.maxSimultaneous || b.samplesOver2 - a.samplesOver2);
// tổng hợp theo khu để nhận định chen chúc
const zones = {};
{
  const all = new Set([...Object.keys(stPairsByZone), ...Object.keys(wwZonePairs), ...Object.keys(wsZonePairs), ...Object.keys(zoneWandererSum)]);
  const stByZone = {};
  for (const s of actStatics) { const zn = C.zoneOf(s.x, s.z); stByZone[zn] = (stByZone[zn] || 0) + 1; }
  for (const zn of all) zones[zn] = {
    statics: stByZone[zn] || 0,
    staticPairsUnder06: stPairsByZone[zn] || 0,
    wanderersAvgPerSample: r2((zoneWandererSum[zn] || 0) / Math.max(1, zoneSampleN)),
    wandererOverlapPairSamples: wwZonePairs[zn] || 0,
    wandererStaticPairSamples: wsZonePairs[zn] || 0,
  };
}

// ---------- 6) JSON đầy đủ -> file; JSON tóm tắt -> stdout ----------
// Kiểm toán cao độ y (phát hiện phụ, đo trực tiếp từ state cuối mô phỏng):
// statics luôn có y hữu hạn; wanderer thì phần lớn KHÔNG (lỗi routeY/rt —
// xem lvlOf). Số cặp XZ của báo cáo không bị ảnh hưởng vì chuyển động XZ
// của game không phụ thuộc y.
const yAudit = (() => {
  const wsEnd = C.wanderers(), ssEnd = C.statics();
  const fin = a => a.filter(p => Number.isFinite(p.y)).length;
  return {
    wanderersFiniteY: fin(wsEnd), wanderersNonFiniteY: wsEnd.length - fin(wsEnd), wanderersTotal: wsEnd.length,
    staticsFiniteY: fin(ssEnd), staticsNonFiniteY: ssEnd.length - fin(ssEnd), staticsTotal: ssEnd.length,
    finiteYWandererIdxs: wsEnd.filter(p => Number.isFinite(p.y)).map(p => p.i),
    finding: 'Wanderer spawn với y=undefined (routeY đọc pt[2] của điểm tuyến ĐÃ map qua rt — mảng luôn dài 3 nên nhánh groundH không bao giờ chạy cho tuyến 2 tọa độ), rồi thành NaN sau nhịp lerp y đầu tiên trong animate; chỉ wanderer có y tường minh trong tuyến (INDOOR_RT, y=0.5) giữ y hữu hạn. Đo trong harness three r160 thật — cần kiểm chứng thêm trên trình duyệt thật trước khi kết luận bản chạy thật cũng dính.',
  };
})();
const lvlTotals = arr => ({
  totalSameLevel: arr.reduce((s, x) => s + (x.sameLevelPairs || 0), 0),
  totalDiffLevel: arr.reduce((s, x) => s + (x.diffLevelPairs || 0), 0),
  totalUnknownLevel: arr.reduce((s, x) => s + (x.unknownLevelPairs || 0), 0),
});
const result = {
  meta: {
    label: 'audit_crowd_geo2 — lượt chạy gần nhất (nhãn cũ ghi cứng BEFORE là của baseline 09/11; số liệu trong file luôn là của lượt chạy mới nhất)',
    generatedAt: new Date().toISOString(),
    gameRoot: ROOT, sourceFile: process.env.SRC_FILE || 'index.html',
    framesSimulated: FRAMES, fixedDt: FIXED_DT, sampleEvery: SAMPLE_EVERY, samplesTaken: samples.length,
    randomSeed: SEED, saveState: 'sạch (localStorage trống)',
    isNight: meta0.isNight, crowdLevel: meta0.crowdLevel,
    countsInit: meta0.counts, countsEnd: metaEnd.counts,
    npcZoneCountGame: meta0.npcZoneCount, npcStatsGame: meta0.npcStats,
    staticsTotal: staticsSnap.length, staticsActiveVisible: actStatics.length,
    simError, wandererY: yAudit,
    note: 'Khoảng cách chính = XZ; dy/sameLevel 3 trạng thái (true=cùng cao độ |dy|<=1.5, false=khác cao độ thật, null=y không hữu hạn nên không phân loại được — xem wandererY). NPC_ZONE_COUNT của game đếm cả sạp + điểm xuất phát wanderer nên chỉ để tham chiếu.',
  },
  staticsPairsUnder06: { count: stPairs.length, sameLevelCount: stPairs.filter(p => p.sameLevel === true).length, diffLevelCount: stPairs.filter(p => p.sameLevel === false).length, unknownLevelCount: stPairs.filter(p => p.sameLevel === null).length, byZone: stPairsByZone, pairs: stPairs },
  wandererOverlapUnder05: {
    threshold: 0.5,
    totalPairSamples: wwPerSample.reduce((s, x) => s + x.pairCount, 0),
    ...lvlTotals(wwPerSample),
    samplesWithOverlap: wwPerSample.filter(x => x.pairCount > 0).length,
    avgPairsPerSample: r2(wwPerSample.reduce((s, x) => s + x.pairCount, 0) / Math.max(1, wwPerSample.length)),
    worstSample: worstWW ? { frame: worstWW.frame, tSim: worstWW.tSim, wanderers: worstWW.wanderers, pairCount: worstWW.pairCount, sameLevelPairs: worstWW.sameLevelPairs, diffLevelPairs: worstWW.diffLevelPairs, unknownLevelPairs: worstWW.unknownLevelPairs, pairs: worstWW.pairs.slice(0, 40) } : null,
    perSample: wwPerSample.map(x => ({ frame: x.frame, tSim: x.tSim, wanderers: x.wanderers, pairCount: x.pairCount, sameLevelPairs: x.sameLevelPairs, diffLevelPairs: x.diffLevelPairs, unknownLevelPairs: x.unknownLevelPairs })),
    hotspots: wwHot,
  },
  wandererBrowseSharing: { rule: 'cùng mẫu, cùng browsePt sx/sz, số người > 2', context: browseCtx, events: browseEvents, byStall: browseAgg },
  wandererStaticUnder045: {
    threshold: 0.45,
    totalPairSamples: wsPerSample.reduce((s, x) => s + x.pairCount, 0),
    ...lvlTotals(wsPerSample),
    samplesWithOverlap: wsPerSample.filter(x => x.pairCount > 0).length,
    avgPairsPerSample: r2(wsPerSample.reduce((s, x) => s + x.pairCount, 0) / Math.max(1, wsPerSample.length)),
    worstSample: worstWS ? { frame: worstWS.frame, tSim: worstWS.tSim, pairCount: worstWS.pairCount, sameLevelPairs: worstWS.sameLevelPairs, diffLevelPairs: worstWS.diffLevelPairs, unknownLevelPairs: worstWS.unknownLevelPairs, pairs: worstWS.pairs.slice(0, 60) } : null,
    perSample: wsPerSample.map(x => ({ frame: x.frame, tSim: x.tSim, pairCount: x.pairCount, sameLevelPairs: x.sameLevelPairs, diffLevelPairs: x.diffLevelPairs, unknownLevelPairs: x.unknownLevelPairs })),
    hotspots: wsHot.slice(0, 20),
  },
  zones,
};
fs.writeFileSync(OUT_PATH, JSON.stringify(result, null, 1));
log('đã ghi', OUT_PATH);
const summary = {
  label: result.meta.label,
  meta: { frames: FRAMES, dt: FIXED_DT, samples: samples.length, isNight: meta0.isNight, crowdLevel: meta0.crowdLevel, staticsActiveVisible: actStatics.length, wanderersInit: meta0.counts.wanderers, simError },
  npcZoneCountGame: meta0.npcZoneCount,
  staticsPairsUnder06: { count: stPairs.length, sameLevelCount: result.staticsPairsUnder06.sameLevelCount, byZone: stPairsByZone, worst15: stPairs.slice(0, 15) },
  wandererOverlapUnder05: { totalPairSamples: result.wandererOverlapUnder05.totalPairSamples, avgPairsPerSample: result.wandererOverlapUnder05.avgPairsPerSample, worstSample: result.wandererOverlapUnder05.worstSample, hotspotsTop8: wwHot.slice(0, 8) },
  wandererBrowseSharing: { events: browseEvents.length, context: browseCtx, byStall: browseAgg },
  wandererY: { finite: yAudit.wanderersFiniteY, nonFinite: yAudit.wanderersNonFiniteY, total: yAudit.wanderersTotal, finiteIdxs: yAudit.finiteYWandererIdxs },
  wandererStaticUnder045: { totalPairSamples: result.wandererStaticUnder045.totalPairSamples, avgPairsPerSample: result.wandererStaticUnder045.avgPairsPerSample, worstSample: result.wandererStaticUnder045.worstSample && { frame: result.wandererStaticUnder045.worstSample.frame, pairCount: result.wandererStaticUnder045.worstSample.pairCount, sameLevelPairs: result.wandererStaticUnder045.worstSample.sameLevelPairs }, hotspotsTop8: wsHot.slice(0, 8) },
  zones,
  resultFile: OUT_PATH,
};
console.log(JSON.stringify(summary, null, 1));
process.exit(simError ? 3 : 0);
