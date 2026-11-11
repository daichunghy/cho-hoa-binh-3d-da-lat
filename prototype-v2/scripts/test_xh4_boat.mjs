#!/usr/bin/env node
/* =====================================================================
   test_xh4_boat.mjs — Kiểm chứng XH-4 (12/11): ĐẠP VỊT THIÊN NGA + LUẬT
   MẶT NƯỚC. Chạy trên index.html THẬT trong harness diag (như test_bd2):
   thuê (trừ đúng 30 Xu, thiếu Xu từ chối) -> chèo đụng biên bắc/đảo/đập/
   đông/nam + cầu Y + thuyền tĩnh -> trả thuyền -> Xu khớp; đi bộ bị chặn
   ở mép nước; hết giờ autopilot tự về bến; save không chứa trạng thái thuê.
   Cách dùng: DIAG_NODE_MODULES=/tmp/diag/node_modules node scripts/test_xh4_boat.mjs
   ===================================================================== */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = process.env.GAME_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const WORK = '/tmp/diag-runtime-work-xh4';

const diagSrc = fs.readFileSync(path.join(ROOT, 'scripts/diag_runtime.mjs'), 'utf8');
const stubEnd = diagSrc.indexOf('// ---------- chuẩn bị bản game đã vá import');
if (stubEnd < 0) { console.error('[xh4] không tìm thấy marker vá import trong diag_runtime.mjs'); process.exit(9); }
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
;globalThis.__xh4 = () => {
  const out = { fails: [], info: {} };
  const fail = (m) => out.fails.push(m);
  const drive = (steps, ix, iy) => { let tt = 100; for(let i = 0; i < steps; i++){ tt += 0.05; tickBoat(0.05, tt, ix, iy); if(!boatOn) break; } };
  try {
    // ---------- 1: registry + luật mặt nước (hàm thuần) ----------
    if (!LAKE_PLAYER_BOAT) fail('registry: thiếu LAKE_PLAYER_BOAT');
    out.info.boats = LAKE_BOATS.length;
    if (LAKE_BOATS.length !== 10) fail('registry: LAKE_BOATS phải = 10 (9 tĩnh + 1 người chơi), thấy ' + LAKE_BOATS.length);
    if (xh4OnWater(-300, 100) !== true) fail('nước: giữa hồ (−300,100) phải là mặt nước');
    if (xh4OnWater(-250, 58) !== false) fail('nước: đảo (−250,58) không được là nước');
    if (xh4OnWater(-259, 40) !== true) fail('nước: slip (−259,40) phải là nước');
    if (xh4OnWater(-259, 36.6) !== false) fail('nước: lối nối bờ (−259,36,6) không được là nước');
    if (xh4OnWater(-282, 39) !== false) fail('nước: thân cầu Y (−282,39) phải đi bộ được');
    { const wx = -282 + Math.sin(0.62) * 1.3, wz = 41 + Math.cos(0.62) * 1.3;
      if (!(groundH(wx, wz) === 5.5 && xh4OnWater(wx, wz) === false)) fail('nước: cánh cầu Y phải solid (groundH 5,5)'); }
    playerState.x = -259; playerState.z = 36.9;
    { const r = xh4WaterGuard(-259, 38.5);
      if (!(Math.abs(r[1] - 36.9) < 1e-9 && Math.abs(r[0] + 259) < 1e-9)) fail('guard: bước từ cầu bến xuống nước phải bị chặn ở mép, nhận ' + r.join(',')); }
    playerState.x = -270; playerState.z = 35.5;
    { const r = xh4WaterGuard(-270.5, 36.3);
      if (!(Math.abs(r[0] + 270.5) < 1e-9 && Math.abs(r[1] - 35.5) < 1e-9)) fail('guard: bước chéo ở mép bờ bắc phải trượt dọc mép (x đi, z giữ), nhận ' + r.join(',')); }
    playerState.x = -240; playerState.z = 40;
    { const r = xh4WaterGuard(-239.4, 40.6);
      if (!(Math.abs(r[0] + 240) < 1e-9 && Math.abs(r[1] - 40) < 1e-9)) fail('guard: cả 2 trục đều ướt phải đứng yên, nhận ' + r.join(',')); }

    // ---------- 2: thuê / trả / thiếu Xu ----------
    state.xu = 100; playerState.x = -259; playerState.z = 33.6;
    toggleBoat();
    if (!(boatOn === true && boating === 300)) fail('thuê: boatOn/boating sai (boating=' + boating + ')');
    if (state.xu !== 70) fail('thuê: phải trừ đúng 30 Xu (100→70), thấy ' + state.xu);
    { const d = Math.hypot(playerState.x - boatState.x, playerState.z - boatState.z);
      if (d > 0.6) fail('thuê: người chơi phải ở ghế thuyền, lệch ' + d.toFixed(2)); }
    if (boatNearSlip() !== true) fail('thuê: thuyền neo trong slip phải nearSlip');
    tryReturnBoat();
    if (!(boatOn === false && boatParkT > 0)) fail('trả: tại slip phải xuống được + thuyền lướt về neo');
    if (!(Math.abs(playerState.z - 34.9) < 1e-9 && groundH(playerState.x, playerState.z) === 5.5)) fail('trả: người chơi phải đứng trên bờ (groundH 5,5)');
    state.xu = 10; toggleBoat();
    if (!(boatOn === false && state.xu === 10)) fail('thiếu Xu: phải từ chối và giữ nguyên Xu');

    // ---------- 3: chèo đụng biên bằng vật lý thật ----------
    state.xu = 100; toggleBoat();
    if (!(boatOn === true && state.xu === 70)) fail('thuê lần 2 lỗi');
    drive(100, 0, -1);
    out.info.slipExit = { x: +boatState.x.toFixed(1), z: +boatState.z.toFixed(1) };
    // Làn slip x=-259: vòng r17 của đảo cắt ngang ở z=58-sqrt(17^2-9^2)=43,58 -> lùi thẳng chỉ tới ~43,6
    // (hành lang giữa vòng đảo và kè bắc z=38 là làn đi thật, như hồ thật: đảo Thủy Tạ sát bờ bắc).
    if (!(boatState.z > 43.1 && boatState.z < 43.9)) fail('slip: lùi S ra khỏi kênh ngón cầu + chạm vòng đảo r17 (z≈43,6), thấy z=' + boatState.z.toFixed(2));
    if (!(Math.abs(boatState.x + 259) < 3)) fail('slip: ra khỏi slip không được xuyên ngón cầu, x=' + boatState.x.toFixed(1));
    boatState.h = -Math.PI / 2; boatState.v = 0; drive(240, 0, 1); // bẻ lái tây, đi vòng qua hành lang phía tây đảo
    { const d = Math.hypot(boatState.x + 250, boatState.z - 58); out.info.slipWest = { x: +boatState.x.toFixed(1), z: +boatState.z.toFixed(1), r: +d.toFixed(2) };
      if (!(boatState.x < -270 && d > 17.2)) fail('slip: vòng qua phía tây đảo không thoát được (x=' + boatState.x.toFixed(1) + ', r=' + d.toFixed(2) + ')'); }
    const run = (x, z, h, steps, ix, iy) => { boatState.x = x; boatState.z = z; boatState.h = h; boatState.v = 0; drive(steps, ix, iy); return boatState; };
    let B = run(-340, 60, Math.PI, 400, 0, 1);
    out.info.edgeN = +B.z.toFixed(2);
    if (!(B.z >= 37.99 && B.z <= 40)) fail('BIÊN BẮC: z phải dừng ≥38, thấy ' + B.z.toFixed(2));
    B = run(-310, 58, Math.PI / 2, 500, 0, 1); // làn tây z=58 trống thuyền tĩnh (cung tĩnh ở phía nam đảo)
    { const d = Math.hypot(B.x + 250, B.z - 58); out.info.isleR = +d.toFixed(2);
      if (!(d >= 16.95 && d <= 18.5)) fail('BIÊN ĐẢO: r phải ≥17, thấy ' + d.toFixed(2)); }
    B = run(-250, 84, Math.PI, 400, 0, 1); // hướng nam: vòng thuyền tĩnh cung nam (r 18,6 + tránh 2,35) chắn trước vòng đảo
    { const d = Math.hypot(B.x + 250, B.z - 58); out.info.isleRS = +d.toFixed(2);
      if (!(d >= 20.8 && d <= 21.2)) fail('CUNG THUYỀN TĨNH NAM ĐẢO: phải dừng ở r≈20,95 (18,6+2,35), thấy ' + d.toFixed(2)); }
    B = run(-400, 160, -Math.PI / 2, 1600, 0, 1);
    out.info.edgeW = +B.x.toFixed(2);
    if (!(B.x >= -556.01 && B.x <= -549)) fail('BIÊN TÂY: x phải dừng ≥−556, thấy ' + B.x.toFixed(2));
    B = run(-450, 95, -Math.PI / 2, 1200, 0, 1);
    out.info.damX = +B.x.toFixed(2);
    if (!(B.x >= -551.8 && B.x <= -544)) fail('ĐẬP ÔNG ĐẠO: x phải dừng ≥−551,75 ở hàng z=95, thấy ' + B.x.toFixed(2));
    B = run(-300, 100, Math.PI / 2, 900, 0, 1);
    out.info.edgeE = +B.x.toFixed(2);
    if (!(B.x <= -227.99 && B.x >= -236)) fail('BIÊN ĐÔNG: x phải dừng ≤−228, thấy ' + B.x.toFixed(2));
    B = run(-400, 150, 0, 700, 0, 1);
    out.info.edgeS = +B.z.toFixed(2);
    if (!(B.z <= 192.01 && B.z >= 184)) fail('BIÊN NAM: z phải dừng ≤192, thấy ' + B.z.toFixed(2));
    B = run(-282, 52, Math.PI, 500, 0, 1);
    out.info.pierZ = +B.z.toFixed(2);
    if (!(B.z >= 41.9 && B.z <= 48)) fail('CẦU Y: không được xuyên thân/cánh cầu, dừng trước cầu, thấy z=' + B.z.toFixed(2));
    B = run(-272, 47, Math.PI, 400, 0, 1);
    { const d = Math.hypot(B.x + 272, B.z - 39.5); out.info.staticD = +d.toFixed(2);
      if (!(d >= 2.3)) fail('THUYỀN TĨNH: vòng tránh r ≥2,35, thấy d=' + d.toFixed(2)); }
    B = run(-259, 47, Math.PI, 300, 0, 1);
    if (boatNearSlip() !== true) fail('về slip: kênh giữa 2 ngón cầu phải thông để quay về');
    tryReturnBoat();
    if (!(boatOn === false && state.xu === 70)) fail('trả thuyền: không được trừ thêm Xu, thấy ' + state.xu);

    // ---------- 4: hết giờ — autopilot tự về bến ----------
    toggleBoat();
    if (!(boatOn === true && state.xu === 40)) fail('thuê lần 3 lỗi (xu=' + state.xu + ')');
    boatState.x = -320; boatState.z = 120; boatState.h = 0.4; boatState.v = 0;
    startBoatAuto();
    if (boatAuto !== true) fail('autopilot: startBoatAuto không bật');
    { let steps = 0, tt = 500; while(boatOn && steps < 5800){ tt += 0.05; tickBoat(0.05, tt, 0, 0); steps++; }
      out.info.autoSteps = steps;
      if (boatOn !== false) fail('autopilot: thuyền không tự về bến được sau ' + steps + ' bước');
      if (!(groundH(playerState.x, playerState.z) === 5.5)) fail('autopilot: sau khi về, người chơi phải đứng trên bờ'); }

    // ---------- 5: save không chứa trạng thái thuê ----------
    { const s = JSON.parse(localStorage.getItem('chohb3d-v1') || '{}');
      if ('boating' in s || 'boatOn' in s || 'boatState' in s) fail('save: trạng thái thuê lọt vào save'); }
  } catch (e) { out.fails.push('XH4 EXCEPTION: ' + (e && e.stack || e)); }
  return out;
};
`;

const patchedPath = path.join(WORK, 'game_xh4.mjs');
fs.writeFileSync(patchedPath, header + code);
const t0 = Date.now();
try {
  await import(patchedPath);
  console.log('[xh4] MODULE INIT OK sau', Date.now() - t0, 'ms');
} catch (e) {
  console.error('[xh4] *** NGOẠI LỆ TRONG INIT ***');
  console.error(e && e.stack || e);
  process.exit(2);
}
await new Promise(r => setTimeout(r, 800));
const res = globalThis.__xh4();
console.log(JSON.stringify(res, null, 1));
if (res.fails && res.fails.length) {
  console.error('[xh4] FAILS:', res.fails.length);
  for (const f of res.fails) console.error(' -', f);
  process.exit(1);
}
console.log('[xh4] ALL CHECKS PASS');
process.exit(0);
