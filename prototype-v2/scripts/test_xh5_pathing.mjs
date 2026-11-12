#!/usr/bin/env node
/* =====================================================================
   test_xh5_pathing.mjs — Kiểm chứng XH-5 (12/11): TỰ ĐI HÀNH TRÌNH
   CHẶNG 1 (spawn -206,5.6 -> Vòng xoay Hòa Bình -30,-6, check r13).
   Lỗi thật 03:57 12/11: tự đi dừng hẳn ở ~46m trước đích, không đi tiếp.
   Harness lái animate() THẬT (rAF + performance.now giả lập 16,7ms/frame)
   trong môi trường diag, cho autoWalk chạy từ spawn và ghi vết vị trí;
   FAIL nếu kẹt >240 frame (4s) khi chưa tới hoặc không tới trong 3600 frame.
   Cách dùng: DIAG_NODE_MODULES=/tmp/diag/node_modules node scripts/test_xh5_pathing.mjs
   ===================================================================== */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = process.env.GAME_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const WORK = '/tmp/diag-runtime-work-xh5';

const diagSrc = fs.readFileSync(path.join(ROOT, 'scripts/diag_runtime.mjs'), 'utf8');
const stubEnd = diagSrc.indexOf('// ---------- chuẩn bị bản game đã vá import');
if (stubEnd < 0) { console.error('[xh5p] không tìm thấy marker vá import trong diag_runtime.mjs'); process.exit(9); }
fs.mkdirSync(WORK, { recursive: true });
const NM = process.env.DIAG_NODE_MODULES || '/tmp/diag/node_modules';
try { fs.symlinkSync(NM, path.join(WORK, 'node_modules')); } catch(e) {}
const stubsPath = path.join(WORK, 'diag_stubs.mjs');
let stubSrc = diagSrc.slice(0, stubEnd);
stubSrc = stubSrc.replace(
  "const ROOT = process.env.GAME_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');",
  `const ROOT = ${JSON.stringify(ROOT)};`);
fs.writeFileSync(stubsPath, stubSrc);
await import(stubsPath);

// --- giả lập thời gian + rAF riêng + modal đã đóng (như người chơi thật đã chọn chế độ) ---
let fakeNow = 1000;
performance.now = () => fakeNow;
const myQ = [];
globalThis.requestAnimationFrame = cb => { myQ.push(cb); return myQ.length; };
const _qs = document.querySelector.bind(document);
document.querySelector = sel => (sel === '.modal.open' ? null : _qs(sel));
{ // stub xuPops: firstChild không có trong stub — vá để spawnXuPop không vấp khi dồn >5 pop
  const pops = document.getElementById('xuPops');
  pops.appendChild = x => { pops.children.push(x); if (pops.children.length > 5) pops.children.shift(); return x; };
  Object.defineProperty(pops, 'firstChild', { get() { return pops.children[0] ? { remove() { pops.children.shift(); } } : null; } });
}

const raw = fs.readFileSync(path.join(ROOT, process.env.SRC_FILE || 'index.html'), 'utf8');
const mStart = raw.indexOf('<script type="module">');
const mEnd = raw.indexOf('</script>', mStart);
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
;globalThis.__xh5p = {
  start(tx, tz){
    playerState.x = -206; playerState.z = 5.6; playerState.y = groundH(-206, 5.6);
    camYaw = -Math.PI / 2;
    autoWalkTo(tx, tz);
    return autoWalk.path.map(p => [Math.round(p.x * 10) / 10, Math.round(p.z * 10) / 10]);
  },
  snap(tx, tz){
    return { x: Math.round(playerState.x * 100) / 100, z: Math.round(playerState.z * 100) / 100, y: Math.round(playerState.y * 100) / 100,
      i: autoWalk.i, active: autoWalk.active, tutStep: state.tutStep, guideStage: state.guide ? state.guide.stage : -1,
      ci: currentInteract ? currentInteract.type : null,
      arrived: Math.hypot(playerState.x - tx, playerState.z - tz) < (Math.abs(tx + 30) < 0.01 ? 13.0 : 14.0) || (playerState.x > -32 && playerState.z < 6 && playerState.z > -8),
      wp: autoWalk.path[autoWalk.i] ? [autoWalk.path[autoWalk.i].x, autoWalk.path[autoWalk.i].z] : null,
      dist: Math.round(Math.hypot(playerState.x - tx, playerState.z - tz) * 10) / 10 };
  },
  sweep(){
    const rows = [];
    for (let x = -100; x <= -40; x += 0.5) {
      const r = collide(x, 5.6);
      if (Math.abs(r[0] - x) > 0.001 || Math.abs(r[1] - 5.6) > 0.001) rows.push([x, Math.round(r[0] * 100) / 100, Math.round(r[1] * 100) / 100]);
    }
    const strip = colliders.filter(c => c.maxX > -110 && c.minX < -30 && c.maxZ > 2 && c.minZ < 9.5)
      .map(c => ({ minX: Math.round(c.minX * 100) / 100, maxX: Math.round(c.maxX * 100) / 100, minZ: Math.round(c.minZ * 100) / 100, maxZ: Math.round(c.maxZ * 100) / 100, nightOnly: !!c.nightOnly }));
    // mô phỏng "đẩy đông liên tục" từ -90: mỗi bước +0,117u rồi collide — điểm hội tụ = tường
    let px = -90; for (let i = 0; i < 2000; i++) { const r = collide(px + 0.117, 5.6); if (Math.abs(r[0] - px) < 0.001) break; px = r[0]; }
    // XH-5: độ ổn định collide của MỌI đích hành trình (tut + guide) — đích nào bị collide
    // đẩy đi sẽ được awProjectTarget chiếu khi findAwPath chạy; in ra để đối chiếu chủ đích.
    const targets = {};
    for (const [nm, t] of Object.entries({ tut1: [-28, 0], guide1: [-30, -6], guide3: [-27, 10.15], guide4: [-53.2, -19.2], guide5: [26.8, -52], tut2: [-56, -33], tut3: [-19, -48] })) {
      const c = collide(t[0], t[1]);
      targets[nm] = { t, collideTo: [Math.round(c[0] * 100) / 100, Math.round(c[1] * 100) / 100], stable: Math.abs(c[0] - t[0]) < 0.01 && Math.abs(c[1] - t[1]) < 0.01, ground: groundH(t[0], t[1]) };
    }
    for (const [nm, t] of Object.entries({ endWalk: [-31.64, 5.39], ax40: [-40, 5.6], ax50: [-50, 5.6], ax62: [-62, 5.6], ax76: [-76, 5.6] })) targets[nm] = { t, ground: groundH(t[0], t[1]) };
    return { rows, strip, convergeX: Math.round(px * 100) / 100, targets };
  },
  boatTo(x, z){ boatOn = true; boatAuto = false; boating = 300; boatState.x = x; boatState.z = z; boatState.v = 0; boatState.h = 0; },
  pressE(){ interact(); },
  photoHas(id){ return !!G.photos[id]; },
  features(){
    const out = { fails: [], info: {} };
    const fail = m => out.fails.push(m);
    // 1) photo spot 'lake'
    const def = PHOTO_SPOTS.find(p => p.id === 'lake');
    if (!def) fail('photo: thiếu spot lake'); else { out.info.lakeDef = [def.x, def.z, !!def.boat]; if (!def.boat) fail('photo: spot lake phải có boat:true'); }
    const pp = photoPts.find(p => p.def.id === 'lake');
    if (!pp) fail('photo: thiếu photoPt lake'); else if (Math.abs(pp.grp.position.y - 4.95) > 0.01) fail('photo: vòng lake phải nổi ở y 4,95, thấy ' + pp.grp.position.y);
    out.info.photoTotal = PHOTO_SPOTS.length;
    // 2) ambience khu hồ
    playerState.x = -300; playerState.z = 100; const azLake = ambZone();
    playerState.x = -100; playerState.z = 5.6; const azStreet = ambZone();
    out.info.ambLake = [azLake.w, azLake.m]; out.info.ambStreet = [azStreet.w, azStreet.m];
    if (!(azLake.w > azStreet.w * 2)) fail('ambience: tiếng nước khu hồ phải trội hơn phố (lake w=' + azLake.w + ' vs street w=' + azStreet.w + ')');
    if (!(azLake.m < azStreet.m)) fail('ambience: rì rầm khu hồ phải nhỏ hơn phố');
    // 3) nhiệm vụ vòng hồ: chèo qua 4 mốc -> +30 Xu đúng 1 lần
    const xu0 = state.xu;
    boatOn = true; boatAuto = false;
    for (const [lx, lz] of XH5_LAP_PTS) { boatState.x = lx; boatState.z = lz; tickWater(200 + lx); }
    out.info.lapSeen = xh5Lap.seen.size;
    if (xh5Lap.seen.size !== 4) fail('lap: qua 4 mốc phải đủ seen=4, thấy ' + xh5Lap.seen.size);
    if (state.xu - xu0 !== 30) fail('lap: thưởng vòng hồ phải +30 Xu đúng 1 lần, thực tế +' + (state.xu - xu0));
    for (const [lx, lz] of XH5_LAP_PTS) { boatState.x = lx; boatState.z = lz; tickWater(300 + lx); }
    if (state.xu - xu0 !== 30) fail('lap: đi lại vòng 2 trong cùng phiên chèo không được thưởng nữa, Xu +' + (state.xu - xu0));
    // 4) autopilot không tính mốc
    boatOn = false; tickWater(400); // rời thuyền -> reset
    boatOn = true; boatAuto = true;
    for (const [lx, lz] of XH5_LAP_PTS) { boatState.x = lx; boatState.z = lz; tickWater(500 + lx); }
    if (xh5Lap.seen.size !== 0) fail('lap: autopilot tự về bến không được tính mốc, seen=' + xh5Lap.seen.size);
    boatAuto = false; boatOn = false; tickWater(600);
    return out;
  },
  probe(x, z){
    const cols = colliders.filter(c => x > c.minX - 3.5 && x < c.maxX + 3.5 && z > c.minZ - 3.5 && z < c.maxZ + 3.5)
      .map(c => ({ minX: Math.round(c.minX * 100) / 100, maxX: Math.round(c.maxX * 100) / 100, minZ: Math.round(c.minZ * 100) / 100, maxZ: Math.round(c.maxZ * 100) / 100, nightOnly: !!c.nightOnly }));
    const npcs = [];
    for (const s of statics){ if (s.g && Math.hypot(s.g.position.x - x, s.g.position.z - z) < 3.5) npcs.push(['static', Math.round(s.g.position.x * 100) / 100, Math.round(s.g.position.z * 100) / 100]); }
    for (const w of wanderers){ if (w.g && w.active && Math.hypot(w.g.position.x - x, w.g.position.z - z) < 3.5) npcs.push(['wand', Math.round(w.g.position.x * 100) / 100, Math.round(w.g.position.z * 100) / 100, w.mode || '']); }
    return { cols, npcs, ground: groundH(x, z), collidersTotal: colliders.length };
  }
};
`;

const patchedPath = path.join(WORK, 'game_xh5p.mjs');
fs.writeFileSync(patchedPath, header + code);
const t0 = Date.now();
try {
  await import(patchedPath);
  console.log('[xh5p] MODULE INIT OK sau', Date.now() - t0, 'ms');
} catch (e) {
  console.error('[xh5p] *** NGOẠI LỆ TRONG INIT ***');
  console.error(e && e.stack || e);
  process.exit(2);
}
await new Promise(r => setTimeout(r, 1500)); // chờ GLB nạp (statics/wanderers có mesh)

if (process.env.FEATURES === '1') {
  const H = globalThis.__xh5p;
  const r = H.features();
  console.log('[xh5p] FEATURES', JSON.stringify(r, null, 1));
  if (r.fails.length) { console.error('[xh5p] FEATURES FAIL:', r.fails.length); process.exit(1); }
  // E2E: đang trên thuyền giữa hồ -> prompt phải là 'photo' (không phải 'boatride'), bấm E chụp được
  H.boatTo(-390, 115);
  for (let f = 0; f < 40; f++) {
    const cbs = myQ.splice(0, myQ.length);
    if (!cbs.length) break;
    fakeNow += 16.7;
    try { for (const cb of cbs) cb(fakeNow); } catch (e) { console.error('[xh5p] *** NGOẠI LỆ E2E frame', f, '***'); console.error(e && e.stack || e); process.exit(3); }
  }
  const s = H.snap(-390, 115);
  console.log('[xh5p] E2E snap', JSON.stringify(s));
  if (s.ci !== 'photo') { console.error('[xh5p] FEATURES FAIL: trên thuyền giữa hồ prompt phải là photo, thấy', s.ci); process.exit(1); }
  H.pressE();
  if (!H.photoHas('lake')) { console.error('[xh5p] FEATURES FAIL: bấm E trên thuyền không chụp được spot lake'); process.exit(1); }
  console.log('[xh5p] FEATURES PASS (gồm E2E chụp ảnh lake trên thuyền)');
  process.exit(0);
}
if (process.env.PROBE === '1') {
  console.log('[xh5p] SWEEP', JSON.stringify(globalThis.__xh5p.sweep(), null, 1));
  process.exit(0);
}
// --- LIVE-LIKE: pre-run thế giới cho đám đông/xe tản ra rồi mới bấm tự đi ---
const PRERUN = parseInt(process.env.PRERUN || '0', 10);
if (PRERUN > 0) {
  for (let f = 0; f < PRERUN; f++) {
    const cbs = myQ.splice(0, myQ.length);
    if (!cbs.length) break;
    fakeNow += 16.7;
    try { for (const cb of cbs) cb(fakeNow); } catch (e) { console.error('[xh5p] *** NGOẠI LỆ PRERUN frame', f, '***'); console.error(e && e.stack || e); process.exit(3); }
  }
  console.log('[xh5p] prerun xong', PRERUN, 'frame');
}
const TX = parseFloat(process.env.TX || '-28'), TZ = parseFloat(process.env.TZ || '0'), MAXF = 3600, STALLF = 240;
const pathPts = globalThis.__xh5p.start(TX, TZ);
console.log('[xh5p] path', JSON.stringify(pathPts));
let lastX = null, lastZ = null, stallRun = 0, stallInfo = null, reached = -1;
for (let f = 0; f < MAXF; f++) {
  const cbs = myQ.splice(0, myQ.length);
  if (!cbs.length) { console.log('[xh5p] rAF cạn ở frame', f); break; }
  fakeNow += 16.7;
  try { for (const cb of cbs) cb(fakeNow); }
  catch (e) { console.error('[xh5p] *** NGOẠI LỆ ANIMATE frame', f, '***'); console.error(e && e.stack || e); console.log('[xh5p] SNAP@exc', JSON.stringify(globalThis.__xh5p.snap(TX, TZ))); process.exit(3); }
  const s = globalThis.__xh5p.snap(TX, TZ);
  if (f % 120 === 0) console.log('[xh5p] trace', f, s.x, s.z, 'wp' + s.i, 'dist' + s.dist, 'tut' + s.tutStep);
  if (s.arrived && reached < 0) reached = f;
  if (reached >= 0 && !s.active) break; // XH-5: tới nơi VÀ tự đi tự kết thúc mới là xong
  if (process.env.OBSERVE && reached > 0 && f > reached + parseInt(process.env.OBSERVE, 10)) break;
  if (lastX !== null) {
    const moved = Math.hypot(s.x - lastX, s.z - lastZ);
    if (s.active && moved < 0.02) { stallRun++; if (stallRun >= STALLF && !stallInfo) { stallInfo = { frame: f, ...s }; } }
    else stallRun = 0;
  }
  lastX = s.x; lastZ = s.z;
  if (stallInfo) break;
}
const end = globalThis.__xh5p.snap(TX, TZ);
console.log('[xh5p] END', JSON.stringify(end), 'reachedFrame =', reached);
if (stallInfo) {
  console.log('[xh5p] STALL', JSON.stringify(stallInfo));
  console.log('[xh5p] PROBE@player', JSON.stringify(globalThis.__xh5p.probe(stallInfo.x, stallInfo.z)));
  if (stallInfo.wp) console.log('[xh5p] PROBE@waypoint', JSON.stringify(globalThis.__xh5p.probe(stallInfo.wp[0], stallInfo.wp[1])));
  console.error('[xh5p] FAIL: tự đi kẹt tại frame', stallInfo.frame);
  process.exit(1);
}
if (reached < 0) { console.error('[xh5p] FAIL: không tới được vùng check bước 1 trong', MAXF, 'frame'); process.exit(1); }
if (end.active) { console.error('[xh5p] FAIL: đã tới vùng check nhưng tự đi KHÔNG tự kết thúc (active vẫn true) — vị trí', end.x, end.z); process.exit(1); }
console.log('[xh5p] PASS: tự đi bước 1 tới vùng check ở frame', reached, 'và TỰ KẾT THÚC (active=false) — vị trí cuối', end.x, end.z);
process.exit(0);
