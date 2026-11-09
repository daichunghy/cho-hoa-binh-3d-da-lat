#!/usr/bin/env node
/* =====================================================================
   test_real1.mjs — Kiểm chứng REALISM-1 (09/11): texture mặt đất hậu xử
   lý + facade, cửa sổ đêm ngẫu nhiên, đa dạng tóc/áo người.
   Kỹ thuật như test_bd2.mjs: cắt stub từ diag_runtime.mjs, nạp game
   thật, khẳng định trong cùng scope module.
   Cách dùng: node scripts/test_real1.mjs  (SRC_FILE=index-standalone.html cũng được)
   Thoát 0 = đạt hết; 1 = có kiểm hỏng.
   ===================================================================== */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = process.env.GAME_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const WORK = '/tmp/diag-runtime-work';

const diagSrc = fs.readFileSync(path.join(ROOT, 'scripts/diag_runtime.mjs'), 'utf8');
const stubEnd = diagSrc.indexOf('// ---------- chuẩn bị bản game đã vá import');
if (stubEnd < 0) { console.error('[real1] không tìm thấy marker vá import trong diag_runtime.mjs'); process.exit(9); }
fs.mkdirSync(WORK, { recursive: true });
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
;globalThis.__real1 = () => {
  const out = { fails: [], info: {} };
  const fail = (m) => out.fails.push(m);
  try {
    // ---------- (a) texture mặt đất + facade ----------
    const R = window.__REAL1;
    if (!R) fail('real1: window.__REAL1 khong ton tai');
    else {
      out.info.texMeshes = R.texMeshes;
      out.info.facadeTex = R.facadeTex;
      if (R.texMeshes < 20) fail('real1: texMeshes < 20: ' + R.texMeshes);
      if (R.facadeTex < 8) fail('real1: facadeTex < 8: ' + R.facadeTex);
    }

    // ---------- (b) cửa sổ đêm ngẫu nhiên qua applyDayNight ----------
    out.info.winMats = winMats.length;
    isNight = true; applyDayNight();
    const nightVals = winMats.map(w => +w.emissiveIntensity.toFixed(3));
    const distinct = new Set(nightVals);
    const zeroRatio = nightVals.filter(v => v === 0).length / Math.max(1, nightVals.length);
    out.info.nightWin = { distinct: distinct.size, zeroRatio: +zeroRatio.toFixed(3), sample: nightVals.slice(0, 8) };
    if (distinct.size < 3) fail('real1: cua so dem phai co >= 3 muc sang phan biet, thay ' + distinct.size);
    if (zeroRatio < 0.15 || zeroRatio > 0.45) fail('real1: ti le cua so tat dem phai trong [0.15,0.45], thay ' + zeroRatio.toFixed(3));
    isNight = false; applyDayNight();
    const dayVals = winMats.map(w => w.emissiveIntensity);
    if (!dayVals.every(v => v === 0)) fail('real1: ban ngay tat ca cua so phai = 0');
    isNight = true; applyDayNight(); // tra ve dem (mac dinh game)

    // ---------- (e) người: màu tóc + họa tiết áo ----------
    const hairCols = new Set();
    let mappedTorso = 0, hairMissing = 0;
    for (let i = 0; i < 40; i++) {
      const look = rollLook('crowd');
      const g = makePerson(look.shirt, look.pants, look.hat, look.skin, look.hatColor);
      // Tóc trong GLB đã gộp vào node Head: mesh con dùng material 'HairDark'
      // (không còn node 'tmpHair') — giữ tham chiếu mesh tóc TRƯỚC applyLook,
      // sau applyLook đọc màu material đã recolor trên chính mesh đó.
      let hairMesh = g.getObjectByName('tmpHair') || null;
      if (!hairMesh) g.traverse(o => { if (!hairMesh && o.isMesh && o.material && !Array.isArray(o.material) && o.material.name === 'HairDark') hairMesh = o; });
      applyLook(g, look, 'crowd');
      if (hairMesh && hairMesh.material && hairMesh.material.color) hairCols.add(hairMesh.material.color.getHex());
      else hairMissing++;
      const torso = g.getObjectByName('Torso');
      if (torso && torso.material && torso.material.map) mappedTorso++;
    }
    if (hairMissing) fail('real1: ' + hairMissing + '/40 nguoi khong tim thay mesh toc (material HairDark)');
    out.info.people = { hairDistinct: hairCols.size, hairHexes: [...hairCols].map(h => '0x' + h.toString(16)), mappedTorso };
    if (hairCols.size < 3) fail('real1: phai co >= 3 mau toc phan biet sau 40 nguoi, thay ' + hairCols.size);
    if (mappedTorso < 5) fail('real1: phai co >= 5/40 nguoi ao co hoa tiet (map), thay ' + mappedTorso);
  } catch (e) { out.fails.push('REAL1 EXCEPTION: ' + (e && e.stack || e)); }
  return out;
};
`;

const patchedPath = path.join(WORK, 'game_real1.mjs');
fs.writeFileSync(patchedPath, header + code);
const t0 = Date.now();
try {
  await import(patchedPath);
  console.log('[real1] MODULE INIT OK sau', Date.now() - t0, 'ms');
} catch (e) {
  console.error('[real1] *** NGOẠI LỆ TRONG INIT ***');
  console.error(e && e.stack || e);
  process.exit(2);
}
await new Promise(r => setTimeout(r, 800));
const res = globalThis.__real1();
console.log(JSON.stringify(res, null, 1));
if (res.fails && res.fails.length) {
  console.error('[real1] FAILS:', res.fails.length);
  for (const f of res.fails) console.error(' -', f);
  process.exit(1);
}
console.log('REAL1 TEST PASS');
process.exit(0);
