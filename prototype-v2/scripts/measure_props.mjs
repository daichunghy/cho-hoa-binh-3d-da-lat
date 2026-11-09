#!/usr/bin/env node
/* =====================================================================
   measure_props.mjs — ĐO VẬT PHẨM theo nhóm (PROPS-OPT-1).
   Tái dùng stub DOM/WebGL/fetch của diag_runtime.mjs bằng cách cắt phần
   stub ra file tạm rồi import (nó tự dựng node_modules/three symlink).
   Sau đó vá import của index.html như diag, chèn __propsDump vào cuối
   module game: duyệt scene thật sau init, gom mesh theo
   (container, loại geometry, vật liệu, cỡ) + theo từng sạp.
   Container: crowd / stall:<id> / glb (geometry.type==='BufferGeometry')
   / world (còn lại). Đếm cả số geometry KHÁC NHAU mỗi bucket (shared?).
   Cách dùng: node scripts/measure_props.mjs [outfile.json]
   ===================================================================== */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = process.env.GAME_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const OUT = process.argv[2] || '/tmp/props_measure.json';
const WORK = '/tmp/diag-runtime-work';

// 1) cắt phần stub của diag_runtime.mjs (từ đầu tới marker vá import) -> import để dựng globals
const diagSrc = fs.readFileSync(path.join(ROOT, 'scripts/diag_runtime.mjs'), 'utf8');
const stubEnd = diagSrc.indexOf('// ---------- chuẩn bị bản game đã vá import');
if (stubEnd < 0) { console.error('[measure] không tìm thấy marker vá import trong diag_runtime.mjs'); process.exit(9); }
fs.mkdirSync(WORK, { recursive: true });
const stubsPath = path.join(WORK, 'diag_stubs.mjs');
let stubSrc = diagSrc.slice(0, stubEnd);
// stubs tính ROOT từ vị trí file của nó — file này nằm ở /tmp nên phải ghim ROOT về thư mục game
stubSrc = stubSrc.replace(
  "const ROOT = process.env.GAME_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');",
  `const ROOT = ${JSON.stringify(ROOT)};`);
fs.writeFileSync(stubsPath, stubSrc);
await import(stubsPath);

// 2) vá import của index.html (y hệt diag)
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

// 3) epilogue đo (cùng scope module game: scene/wanderers/statics/stalls)
code += `
;globalThis.__stallCheck = () => {
  const rows = [];
  for (const s of stalls) {
    let merged = 0, mergedTris = 0, normal = 0, textured = 0, lanterns = 0, vendorMeshes = 0, inGraph = true;
    s.group.traverse(o => {
      if (!o.isMesh) return;
      if (o.name === 'merged') { merged++; const g = o.geometry; mergedTris += (g.index ? g.index.count : g.attributes.position.count) / 3; return; }
      normal++;
      if (o.material && o.material.map) textured++;
      if (o.name && o.name.indexOf('Lantern') === 0) lanterns++;
      let a = o; while (a) { if (a === s.vendor) { vendorMeshes++; break; } a = a.parent; }
    });
    let pourOk = null;
    if (s.pourStream) { let a = s.pourStream, ok = false; while (a) { if (a === s.group) { ok = true; break; } a = a.parent; } pourOk = ok; }
    rows.push({ id: s.id, merged, mergedTris: Math.round(mergedTris), normal, textured, lanterns, vendorMeshes, pourOk, groupVisible: s.group.visible });
  }
  return rows;
};
;globalThis.__propsDump = () => {
  scene.updateMatrixWorld(true);
  const crowdSet = new Set();
  for (const p of wanderers) if (p.g) crowdSet.add(p.g);
  for (const p of statics) if (p.g) crowdSet.add(p.g);
  const stallOf = new Map();
  for (const s of stalls) if (s.group) stallOf.set(s.group, s.id);
  const buckets = new Map();
  const perStall = {};
  const _v = new THREE.Vector3();
  scene.traverse(o => {
    if (!o.isMesh) return;
    const g = o.geometry; if (!g || !g.attributes || !g.attributes.position) return;
    const n = g.index ? g.index.count : g.attributes.position.count;
    const mt = n / 3;
    if (!g.boundingSphere) g.computeBoundingSphere();
    o.getWorldScale(_v);
    const r = (g.boundingSphere ? g.boundingSphere.radius : 0) * Math.max(_v.x, _v.y, _v.z);
    const rCls = r < 0.15 ? 'tiny' : r < 0.45 ? 'small' : r < 1.2 ? 'mid' : 'big';
    let container = 'world';
    let a = o, stallId = null;
    while (a) {
      if (crowdSet.has(a)) { container = 'crowd'; break; }
      if (stallOf.has(a)) { container = 'stall'; stallId = stallOf.get(a); break; }
      a = a.parent;
    }
    if (container === 'world' && g.type === 'BufferGeometry') container = 'glb';
    let matKey = '?';
    const m = o.material;
    if (m) {
      if (Array.isArray(m)) matKey = 'multi[' + m.length + ']';
      else if (m.map) matKey = 'tex:' + (m.name || 'unnamed');
      else if (m.color) matKey = '#' + m.color.getHexString();
      else matKey = m.type || '?';
    }
    const k = (stallId ? 'stall:' + stallId : container) + '|' + g.type + '|' + matKey + '|' + rCls;
    let b = buckets.get(k);
    if (!b) { b = { key: k, container: stallId ? 'stall:' + stallId : container, gtype: g.type, mat: matKey, rCls, meshes: 0, tris: 0, casters: 0, visMeshes: 0, visTris: 0, geos: new Set() }; buckets.set(k, b); }
    b.meshes++; b.tris += mt; if (o.castShadow) b.casters++; b.geos.add(g);
    // hiệu lực hiển thị: mesh chỉ vẽ khi chính nó + mọi tổ tiên đều visible
    let vis = o.visible; let p = o.parent; while (vis && p) { vis = p.visible !== false; p = p.parent; }
    if (vis) { b.visMeshes++; b.visTris += mt; }
    if (stallId) {
      const ps = perStall[stallId] || (perStall[stallId] = { meshes: 0, tris: 0 });
      ps.meshes++; ps.tris += mt;
    }
  });
  const arr = [...buckets.values()].map(b => ({ key: b.key, container: b.container, gtype: b.gtype, mat: b.mat, rCls: b.rCls, meshes: b.meshes, tris: Math.round(b.tris), casters: b.casters, visMeshes: b.visMeshes, visTris: Math.round(b.visTris), distinctGeos: b.geos.size }));
  arr.sort((x, y) => y.tris - x.tris);
  const byMesh = [...arr].sort((x, y) => y.meshes - x.meshes);
  let totalMeshes = 0, totalTris = 0, visMeshes = 0, visTris = 0;
  const byContainer = {};
  for (const b of arr) {
    totalMeshes += b.meshes; totalTris += b.tris; visMeshes += b.visMeshes; visTris += b.visTris;
    const c = b.container.split(':')[0];
    const cc = byContainer[c] || (byContainer[c] = { meshes: 0, tris: 0, visMeshes: 0, visTris: 0, casters: 0 });
    cc.meshes += b.meshes; cc.tris += b.tris; cc.visMeshes += b.visMeshes; cc.visTris += b.visTris; cc.casters += b.casters;
  }
  const rollup = {};
  for (const b of arr) {
    const rk = b.container.split(':')[0] + '|' + b.gtype + '|' + b.rCls;
    const r = rollup[rk] || (rollup[rk] = { meshes: 0, tris: 0, visMeshes: 0, visTris: 0 });
    r.meshes += b.meshes; r.tris += b.tris; r.visMeshes += b.visMeshes; r.visTris += b.visTris;
  }
  return { totalMeshes, totalTris, visMeshes, visTris, byContainer, rollup, byTris: arr.slice(0, 60), byMesh: byMesh.slice(0, 60), perStall };
};
`;
const patchedPath = path.join(WORK, 'game_measure.mjs');
fs.writeFileSync(patchedPath, header + code);
console.log('[measure] game_measure.mjs bytes =', (header + code).length);
const t0 = Date.now();
try {
  await import(patchedPath);
  console.log('[measure] MODULE INIT OK sau', Date.now() - t0, 'ms');
} catch (e) {
  console.error('[measure] *** NGOẠI LỆ TRONG INIT ***');
  console.error(e && e.stack || e);
  process.exit(2);
}
let prev = -1, stable = 0;
for (let i = 0; i < 120 && stable < 3; i++) {
  await new Promise(r => setTimeout(r, 30));
  const d = globalThis.__propsDump();
  const c = d.totalMeshes;
  if (c === prev) stable++; else stable = 0;
  prev = c;
}
const res = globalThis.__propsDump();
fs.writeFileSync(OUT, JSON.stringify(res, null, 1));
console.log('--- stallCheck (merged/normal/textured/lanterns/vendorMeshes/pourOk/visible) ---');
const sc = globalThis.__stallCheck();
let bad = 0;
for (const r of sc) {
  const ok = r.vendorMeshes > 0 && r.textured >= 2 && (r.pourOk === null || r.pourOk === true);
  if (!ok) bad++;
  console.log(`${r.id.padEnd(12)} merged=${r.merged} mTri=${r.mergedTris} normal=${r.normal} tex=${r.textured} lant=${r.lanterns} vendor=${r.vendorMeshes} pour=${r.pourOk} vis=${r.groupVisible}${ok ? '' : '  <-- KIỂM TRA'}`);
}
console.log('stallCheck bad =', bad, '| stalls =', sc.length);
console.log('[measure] totalMeshes =', res.totalMeshes, '| totalTris =', res.totalTris, '| VISIBLE meshes =', res.visMeshes, '| VISIBLE tris =', res.visTris, '| ->', OUT);
console.log('--- byContainer ---');
for (const [c, v] of Object.entries(res.byContainer)) console.log(`${c}: meshes ${v.meshes} (vis ${v.visMeshes}) | tris ${Math.round(v.tris)} (vis ${Math.round(v.visTris)}) | casters ${v.casters}`);
console.log('--- TOP 15 by tris ---');
for (const b of res.byTris.slice(0, 15)) console.log(`${b.tris} tri | ${b.meshes} mesh | ${b.distinctGeos} geo | ${b.key}`);
console.log('--- TOP 15 by mesh count ---');
for (const b of res.byMesh.slice(0, 15)) console.log(`${b.meshes} mesh | ${b.tris} tri | ${b.distinctGeos} geo | ${b.key}`);
console.log('--- perStall (tris desc, top 12) ---');
const ps = Object.entries(res.perStall).map(([id, v]) => ({ id, ...v })).sort((a, b) => b.tris - a.tris);
for (const s of ps.slice(0, 12)) console.log(`${s.id}: ${s.meshes} mesh, ${Math.round(s.tris)} tri`);
let sm = 0, st = 0; for (const s of ps) { sm += s.meshes; st += s.tris; }
console.log(`--- perStall total: ${ps.length} stalls | ${sm} meshes | ${Math.round(st)} tris ---`);
process.exit(0);
