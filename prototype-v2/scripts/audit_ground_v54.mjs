#!/usr/bin/env node
/* =====================================================================
   audit_ground_v54.mjs — Kiểm toán NGƯỜI + MẶT ĐẤT cho Chợ Hòa Bình 3D (V5.4).
   Ra đời sau phản hồi chơi thử 08/11/2026: "người hoạt động không đúng,
   người đi vào đất, lỗi tùm lum".

   Cách làm: TRÍCH NGUYÊN VĂN groundH/stairH/innerStairH/laneZE/laneZW/
   vehBumpE/AW_NODES/AW_EDGES/STALL_DEFS + mọi tuyến addWanderer từ
   index.html rồi chạy kiểm tra hình học thuần trên dữ liệu đó:
   A) quét lưới groundH tìm NHẢY CAO ĐỘ bất ngờ (vách đứng không có
      trong thiết kế: bậc thang/đai thềm/hành lang là vùng trắng);
   B) lấy mẫu dọc mọi tuyến người (wanderer + AW) mỗi 0.4u: nhảy cao độ
      > 1.0, CHÌM ĐẢO (trong đĩa R10.5 mà groundH < 0.85), LẤN LÀN XE
      (cách tâm làn < 0.65 = VA CHẠM thật: nửa thân xe 0.35 + bán kính
      người 0.3 — cùng tiêu chí clearance của harness giao thông; chạy dọc
      >= 2.4u mới là lỗi cứng, ngắn hơn là băng qua; < 0.95 = sát làn),
      CHUI THÂN SẠP.
   Thoát mã 0 = sạch (chỉ còn cảnh báo sát làn đã biết); 1 = có lỗi cứng.
   ===================================================================== */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const src = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');

function extractFn(name) {
  const i = src.indexOf('function ' + name + '(');
  if (i < 0) throw new Error('không thấy hàm ' + name);
  let d = 0, j = src.indexOf('{', i);
  const start = j;
  for (; j < src.length; j++) { if (src[j] === '{') d++; else if (src[j] === '}') { d--; if (!d) break; } }
  return src.slice(i, j + 1);
}
function extractConst(name) {
  const i = src.indexOf('const ' + name + ' =');
  if (i < 0) throw new Error('không thấy const ' + name);
  // quét cân bằng [] {} () tới hết biểu thức (comment trong mảng có thể chứa ';')
  let d = 0, j = src.indexOf('=', i);
  for (j = j + 1; j < src.length; j++) {
    const c = src[j];
    if (c === '[' || c === '{' || c === '(') d++;
    else if (c === ']' || c === '}' || c === ')') { d--; if (d === 0) { j++; break; } }
    else if (c === ';' && d === 0) break;
  }
  while (j < src.length && src[j] !== ';') j++;
  return src.slice(i, j + 1);
}
const sandbox = {};
const code = [
  extractFn('stairH'), extractFn('innerStairH'), extractFn('groundH'),
  extractFn('entryRampY'), extractFn('islandBump'),
  extractFn('vehBumpE'), extractFn('laneZE'), extractFn('laneZW'),
  extractConst('AW_NODES'),
  'const AW_EDGES=[]; for(let i=0;i<15;i++){ if(i===7) continue; AW_EDGES.push([i,i+1]); } AW_EDGES.push([7,16],[16,17],[17,18],[7,19],[19,20],[20,21],[14,22],[22,23],[23,24],[24,25],[25,26],[26,27],[27,28],[28,29],[10,30],[30,31],[11,32],[32,33],[13,34],[34,35],[36,0],[37,36],[38,37],[39,38],[27,41],[41,40],[42,39],[43,42],[44,43],[45,44],[46,45],[47,46],[8,48],[48,2]); // GEOMETRY-2 + LAYOUT-FIX-1: snapshot khop index.html (+ chuoi truc toi bung binh dau cho 42-47; + canh noi chan thang tay qua nut dem 48)',
  extractConst('RB_ARC'),
  'const RB = RB_ARC.concat(RB_ARC.slice(0,-1).reverse());',
  extractConst('LOOP'),
].join('\n');
const api = new Function(code + '\nreturn { stairH, innerStairH, groundH, entryRampY, laneZE, laneZW, AW_NODES, AW_EDGES, RB, LOOP };')();
Object.assign(sandbox, api);
const { groundH, laneZE, laneZW, AW_NODES, AW_EDGES, LOOP, RB } = sandbox;

// --- tuyến wanderer: quét mọi addWanderer( và trích đối số đầu theo cân bằng ngoặc ---
const routes = [];
{
  let idx = 0;
  while (true) {
    const i = src.indexOf('addWanderer(', idx);
    if (i < 0) break;
    idx = i + 12;
    // bỏ qua chính định nghĩa hàm
    if (src.slice(Math.max(0, i - 10), i).includes('function')) continue;
    let j = i + 'addWanderer('.length, d = 0, start = j;
    for (; j < src.length; j++) {
      const c = src[j];
      if (c === '[' || c === '(' || c === '{') d++;
      else if (c === ']' || c === ')' || c === '}') { if (d === 0) break; d--; }
      else if (c === ',' && d === 0) break;
    }
    const arg = src.slice(start, j).trim();
    let pts = null;
    try {
      pts = new Function('RB', 'LOOP', 'return (' + arg + ');')(RB, LOOP);
    } catch (e) { pts = null; }
    if (Array.isArray(pts) && pts.length && Array.isArray(pts[0])) routes.push({ name: 'wanderer#' + routes.length + '@' + src.slice(0, i).split('\n').length, pts, isRB: arg.includes('RB'), elevated: /(^|\[)LOOP/.test(arg.replace(/\s/g, '')) || arg.includes('LOOP') });
    else console.log('[audit] BỎ QUA addWanderer không parse được:', arg.slice(0, 60));
  }
}
routes.push({ name: 'LOOP', pts: LOOP, open: false, elevated: true });
const awRoute = { name: 'AW-graph', edges: AW_EDGES, nodes: AW_NODES };

// --- STALL_DEFS rút gọn ---
const stalls = [];
for (const m of src.matchAll(/\{\s*id:'([a-z0-9]+)'[^}]*?x:(-?[\d.]+),\s*z:(-?[\d.]+),\s*rotY:(-?[\d.]+|-?Math\.PI(?:\s*\/\s*2)?)/g)) { // V5.5: rotY am (sap quan ao -PI/2) — truoc day bi bo qua khoi danh sach sap
  stalls.push({ id: m[1], x: +m[2], z: +m[3], hx: 1.65, hz: 1.0 });
}
// --- lưới quầy trang trí nhà lồng (cùng quy tắc sinh + bỏ qua như code thật) ---
const gridStalls = [];
{
  const inner = stalls.filter(s => s.x >= -34 && s.x <= 34 && s.z >= 12 && s.z <= 28);
  const rows = [];
  for (let i = 0; i < 12; i++) { const cx = -28.6 + i * 5.2; rows.push({ x: cx, z: 14.55 }); rows.push({ x: cx, z: 26.7 }); }
  for (let i = 0; i < 12; i++) { const cx = -28.6 + i * 5.2; rows.push({ x: cx, z: 19.35 }); rows.push({ x: cx, z: 20.65 }); }
  for (const r of rows) {
    if (r.x > 25 && r.z > 14) continue;
    if (inner.some(s => Math.abs(r.x - s.x) < 4.6 && Math.abs(r.z - s.z) < 2.7)) continue;
    gridStalls.push({ id: 'quay@' + r.x.toFixed(1) + ',' + r.z, x: r.x, z: r.z, hx: 2.15, hz: 0.7 }); // thân thật box(4.3, _, 1.4)
  }
}
const allObstacles = stalls.concat(gridStalls);
const INDOOR_RT = new Function(extractConst('INDOOR_RT') + '\nreturn INDOOR_RT;')();
routes.push({ name: 'INDOOR_RT', pts: INDOOR_RT, flatY: 0.5 });
// guard dưới công trình: người ở mặt đất (y<8) trong footprint cầu/hành lang -> ground hiệu dụng 0
const inFootprint = (x, z) => (x >= 14.5 && x <= 20.5 && z >= -30 && z <= 9) || (x >= 14 && x <= 33 && z >= 7 && z <= 12.2);
const effG = (x, z, elevated) => (!elevated && inFootprint(x, z)) ? 0 : groundH(x, z);
const ISLAND = { x: -30, z: -6, R: 10.5 }; // GEOMETRY-2: tâm đảo mới

// ---------- A) quét lưới nhảy cao độ ----------
const inStairs = (x, z) => x >= -67.5 && x <= -44.5 && z >= -30.5 && z <= -1.5;         // bậc quantize 0.567 — thiết kế (LAYOUT-FIX-1: thang tam -56)
const inBands = (x, z) => ((x >= -71.6 && x <= -66.4) || (x >= -46.6 && x <= -40.4)) && z >= -30.5 && z <= -1.5; // tường thềm đứng 2 bên thang — thiết kế (LAYOUT-FIX-1: them dong thu hep -45..-43.5 nen dai dong mo rong toi -46.6 de bao o seam canh sap dau hu)
const inIsleCut = (x, z) => x >= -53.6 && x <= -51.4 && z >= -28 && z <= -11.5;            // GEOMETRY-2: vách cắt thềm đảo phía tây theo tâm mới (mép x -52)
const inIsleCutE = (x, z) => x >= -15.6 && x <= -13.4 && z >= -28 && z <= -1.5;           // mép đông thềm đảo nối liền sát thềm tây (-14.5)
const inShelfWall = (x, z) => x >= -58.5 && x <= -44.5 && z >= -12.5 && z <= -10.4;        // V5.4: tường chắn đất thềm bắc — thiết kế
const inInner = (x, z) => x >= 28.4 && x <= 33.6 && z >= 11.4 && z <= 27.4;              // thang trong nhà quantize — thiết kế
const inDeckEdge = (x, z) => x >= 13.9 && x <= 21.1 && z >= -30.5 && z <= 12.6;          // mép deck/hành lang — phân tầng đứng
const inRampCut = (x, z) => x <= -51 && ((z >= -11.2 && z <= -8.4) || (z >= 12.9 && z <= 14.6)); // V5.4: mép cắt/đắp của đường dốc vào
const inCorrWall = (x, z) => (x >= 12.8 && x <= 14.6 && z >= 6 && z <= 13.4) || (x >= 32.8 && x <= 34.6 && z >= 6 && z <= 13.4) || (z >= 5.8 && z <= 7.6 && x >= 13 && x <= 34) || (z >= 11.6 && z <= 13.4 && x >= 13 && x <= 34); // vách khối hành lang tầng 2 — thiết kế
const inStairWall = (x, z) => x >= 27.8 && x <= 29.6 && z >= 12 && z <= 27.5;               // vách tây thang trong nhà — thiết kế
const inCorrNorth55 = (x, z) => x >= -86.5 && x <= -51.5 && z >= -26.5 && z <= -24.0;       // BLENDER-DEEP-2: mép cắt bắc của hành lang kéo dài theo line thềm mới z -25
const inTerrNorth55 = (x, z) => x >= -57.5 && x <= -34.5 && z >= -22.6 && z <= -17.5;       // BLENDER-DEEP-2 + V6: mép thềm bắc (z -21.5, x -52..-35) — có tường chắn 2 bậc chắn mặt cắt
let gridBad = [];
for (let x = -86; x <= 86; x += 1) for (let z = -70; z <= 30; z += 1) {
  if (inStairs(x, z) || inBands(x, z) || inInner(x, z) || inDeckEdge(x, z) || inRampCut(x, z) || inIsleCut(x, z) || inIsleCutE(x, z) || inShelfWall(x, z) || inCorrWall(x, z) || inStairWall(x, z) || inCorrNorth55(x, z) || inTerrNorth55(x, z)) continue;
  const g = groundH(x, z);
  for (const [dx, dz] of [[1, 0], [0, 1]]) {
    const g2 = groundH(x + dx, z + dz);
    if (Math.abs(g2 - g) > 1.35) gridBad.push(`(${x},${z}) ${g.toFixed(2)} -> (${x + dx},${z + dz}) ${g2.toFixed(2)}`);
  }
}
// gộp liên tiếp cho gọn
console.log('=== A) NHẢY CAO ĐỘ TRÊN LƯỚI (ngoài vùng thiết kế) ===');
console.log(gridBad.length ? gridBad.slice(0, 40).join('\n') : 'sạch');

// ---------- B) lấy mẫu tuyến người ----------
function laneDist(x, z) {
  // khoảng cách tới 2 làn (chỉ có nghĩa ở dải đường z -8..13, x -86..86)
  return Math.min(Math.abs(z - laneZE(x)), Math.abs(z - laneZW(x)));
}
function sampleRoute(pts, closed = true) {
  const out = [];
  const segs = [];
  const n = pts.length;
  const m = closed ? n : n - 1;
  for (let i = 0; i < m; i++) segs.push([pts[i], pts[(i + 1) % n]]);
  for (const [a, b] of segs) {
    const L = Math.hypot(b[0] - a[0], b[1] - a[1]);
    const steps = Math.max(1, Math.round(L / 0.4));
    for (let s = 0; s <= steps; s++) out.push([a[0] + (b[0] - a[0]) * s / steps, a[1] + (b[1] - a[1]) * s / steps]);
  }
  return out;
}
let hardErr = [], warns = [];
// gộp các mẫu liên tiếp cùng loại lỗi thành 1 dòng (điểm đầu + số mẫu)
function reportRuns(label, kind, flags, fmt) {
  let run = 0, first = null, lastHit = null;
  const flush = () => { if (run > 0) { const s = fmt(first, run, lastHit); if (s) (kind === 'hard' ? hardErr : warns).push(s); } run = 0; first = null; };
  for (const f of flags) {
    if (f.hit) { if (!run) first = f; run++; lastHit = f; }
    else if (run) flush();
  }
  if (run) flush();
}
function auditPts(label, pts, closed = true, opts = {}) {
  const samples = sampleRoute(pts, closed);
  let prev = null;
  const laneFlags = [], islFlags = [], stallFlags = [];
  for (const [x, z] of samples) {
    // cao độ hiệu dụng: flatY (INDOOR_RT) / guard dưới cầu-hành lang cho tuyến mặt đất / groundH cho tuyến trên cao (LOOP)
    const g = opts.flatY !== undefined ? opts.flatY : effG(x, z, opts.elevated);
    if (prev !== null && Math.abs(g - prev.g) > 1.0 && !inStairs(x, z) && !inStairs(prev.x, prev.z))
      hardErr.push(`${label}: nhảy cao độ ${prev.g.toFixed(2)}->${g.toFixed(2)} tại (${x.toFixed(1)},${z.toFixed(1)})`);
    const dIsl = Math.hypot(x - ISLAND.x, z - ISLAND.z);
    islFlags.push({ x, z, hit: dIsl < ISLAND.R - 0.2 && g < 0.85, g });
    let laneHit = false, laneD = 9;
    // tuyến vành đảo (RB): đi trên vành apron CHIA SẺ với làn vòng đảo (xe có vùng chậm + yield) — miễn kiểm làn, vẫn kiểm chìm đảo/nhảy cao độ
    // vành apron NAM ĐẢO (bán kính < 13.5 quanh tâm đảo, z > 0): làn E ôm sát mép đảo R11.55 —
    // về hình học KHÔNG thể tách người khỏi làn tại đây; đây là không gian chia sẻ có sẵn
    // SLOW_ZONE vành nam (xe 0.45) + yield R-11 trong game — miễn kiểm làn như RB.
    const inApron = Math.hypot(x - ISLAND.x, z - ISLAND.z) < 13.5 && z > 0;
    if (!opts.apron && !inApron && g <= 2.5 && z >= -8 && z <= 13 && x >= -86 && x <= 86) { laneD = laneDist(x, z); laneHit = laneD < 0.65; }
    laneFlags.push({ x, z, hit: laneHit, d: laneD });
    let stHit = null;
    // chỉ tính xuyên sạp ở CAO ĐỘ MẶT ĐẤT: tuyến hành lang/cầu (g >= 4) đi TRÊN nóc sạp tầng trệt
    if (g < 4) for (const st of allObstacles) if (Math.abs(x - st.x) < st.hx && Math.abs(z - st.z) < st.hz) stHit = st.id;
    stallFlags.push({ x, z, hit: !!stHit, id: stHit });
    prev = { x, z, g };
  }
  // trong làn: chạy DỌC >= 6 mẫu (2.4u) mới là lỗi cứng; ngắn hơn = băng qua (cảnh báo)
  (function () {
    let run = 0, first = null, last = null;
    const flush = () => {
      if (run >= 6) hardErr.push(`${label}: ĐI DỌC LÀN XE từ (${first.x.toFixed(1)},${first.z.toFixed(1)}) dài ~${(run * 0.4).toFixed(1)}u`);
      else if (run > 0) warns.push(`${label}: băng qua làn tại (${first.x.toFixed(1)},${first.z.toFixed(1)}) (~${(run * 0.4).toFixed(1)}u)`);
      run = 0; first = null;
    };
    for (const f of laneFlags) { if (f.hit) { if (!run) first = f; run++; last = f; } else if (run) flush(); }
    if (run) flush();
  })();
  reportRuns(label, 'hard', islFlags, (f, n) => `${label}: CHÌM ĐẢO từ (${f.x.toFixed(1)},${f.z.toFixed(1)}) groundH=${f.g.toFixed(2)} (mặt đảo 0.93), ~${(n * 0.4).toFixed(1)}u`);
  reportRuns(label, 'hard', stallFlags, (f, n) => `${label}: XUYÊN THÂN SẠP ${f.id} tại (${f.x.toFixed(1)},${f.z.toFixed(1)})`);
}
for (const r of routes) auditPts(r.name, r.pts, true, { apron: !!r.isRB, elevated: !!r.elevated, flatY: r.flatY });
// AW: duyệt theo cạnh đồ thị (cùng quy tắc chạy dọc/băng qua như wanderer)
// chuỗi cạnh 14->22->...->29 là đường TRÊN CAO (đồi -> cầu -> hành lang -> thang trong):
// người chơi đi các cạnh này với y cao nên guard mặt đất không áp dụng (elevated).
const AW_ELEV = new Set(['14-22', '22-23', '23-24', '24-25', '25-26', '26-27', '27-28', '28-29']);
{
  for (const [a, b] of AW_EDGES) {
    const A = AW_NODES[a], B = AW_NODES[b], tag = a + '-' + b;
    const awElev = AW_ELEV.has(tag);
    const L = Math.hypot(B[0] - A[0], B[1] - A[1]), steps = Math.max(1, Math.round(L / 0.4));
    let prev = null, run = 0, runFirst = null;
    const flushRun = () => {
      if (run >= 6) hardErr.push(`AW cạnh ${tag}: ĐI DỌC LÀN XE từ (${runFirst[0].toFixed(1)},${runFirst[1].toFixed(1)}) dài ~${(run * 0.4).toFixed(1)}u`);
      else if (run > 0) warns.push(`AW cạnh ${tag}: băng qua làn tại (${runFirst[0].toFixed(1)},${runFirst[1].toFixed(1)})`);
      run = 0; runFirst = null;
    };
    for (let s = 0; s <= steps; s++) {
      const x = A[0] + (B[0] - A[0]) * s / steps, z = A[1] + (B[1] - A[1]) * s / steps;
      const g = effG(x, z, awElev); // mặt đất: guard dưới cầu/hành lang; chuỗi cầu: cao độ deck thật
      if (prev && Math.abs(g - prev.g) > 1.0 && !inStairs(x, z))
        hardErr.push(`AW cạnh ${tag}: nhảy cao độ ${prev.g.toFixed(2)}->${g.toFixed(2)} tại (${x.toFixed(1)},${z.toFixed(1)})`);
      const dIsl = Math.hypot(x - ISLAND.x, z - ISLAND.z);
      if (dIsl < ISLAND.R - 0.2 && g < 0.85) hardErr.push(`AW cạnh ${tag}: CHÌM ĐẢO tại (${x.toFixed(1)},${z.toFixed(1)})`);
      let inLane = false;
      const inApronAW = Math.hypot(x - ISLAND.x, z - ISLAND.z) < 13.5 && z > 0; // vành apron nam đảo — như wanderer
      if (!inApronAW && g <= 2.5 && z >= -8 && z <= 13) inLane = laneDist(x, z) < 0.65;
      if (inLane) { if (!run) runFirst = [x, z]; run++; } else if (run) flushRun();
      if (g < 4) for (const st of allObstacles) if (Math.abs(x - st.x) < st.hx && Math.abs(z - st.z) < st.hz)
        hardErr.push(`AW cạnh ${tag}: XUYÊN THÂN SẠP ${st.id} tại (${x.toFixed(1)},${z.toFixed(1)})`);
      prev = { x, z, g };
    }
    if (run) flushRun();
  }
}
hardErr = [...new Set(hardErr)]; warns = [...new Set(warns)];
console.log('=== B) LỖI CỨNG TRÊN TUYẾN NGƯỜI ===');
console.log(hardErr.length ? hardErr.slice(0, 60).join('\n') : 'sạch');
console.log('=== C) CẢNH BÁO SÁT LÀN (chấp nhận được nếu có vùng chậm/yield) ===');
console.log(warns.length ? warns.slice(0, 25).join('\n') : 'không có');
console.log(`\nTỔNG: ${routes.length} tuyến wanderer + AW (${AW_NODES.length} nút), ${stalls.length} sạp | lỗi cứng: ${hardErr.length} | nhảy lưới: ${gridBad.length}`);
process.exit(hardErr.length || gridBad.length ? 1 : 0);
