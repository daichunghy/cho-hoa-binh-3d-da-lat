#!/usr/bin/env node
/* dump_glb_general.mjs — Dump tổng quát mọi GLB (BLENDER-DEEP-1).
   Dùng: node scripts/dump_glb_general.mjs <glb> [glb2 ...]
   In mỗi GLB: cây node (tên, world pos), mỗi mesh: tri, material + màu,
   tâm bbox geometry theo local node (đo lệch tâm pivot), cỡ bbox.
   Cần three r160 resolve được (symlink node_modules -> /tmp/diag/node_modules). */
import fs from 'node:fs';
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

for (const glbPath of process.argv.slice(2)) {
  const buf = fs.readFileSync(glbPath);
  const loader = new GLTFLoader();
  const gltf = await loader.parseAsync(buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength), '');
  const root = gltf.scene;
  root.updateMatrixWorld(true);
  let totalTri = 0, totalVert = 0, meshCount = 0;
  const matColors = {};
  console.log(`\n===== ${glbPath.split('/').pop()} size=${buf.length} =====`);
  function walk(o, depth) {
    const pad = '  '.repeat(depth);
    const wp = new THREE.Vector3(); o.getWorldPosition(wp);
    if (o.isMesh) {
      meshCount++;
      const g = o.geometry; const pos = g.attributes.position;
      const tri = g.index ? g.index.count / 3 : pos.count / 3;
      totalTri += tri; totalVert += pos.count;
      g.computeBoundingBox(); const bb = g.boundingBox;
      const c = new THREE.Vector3(); bb.getCenter(c);
      const s = new THREE.Vector3(); bb.getSize(s);
      const wb = new THREE.Box3().setFromObject(o);
      const wc = new THREE.Vector3(); wb.getCenter(wc);
      const ws = new THREE.Vector3(); wb.getSize(ws);
      const mats = (Array.isArray(o.material) ? o.material : [o.material]).map(m => {
        const col = m && m.color ? '#' + m.color.getHexString() : '?';
        if (m) matColors[m.name] = col;
        return `${m ? m.name : '?'}:${col}`;
      }).join('+');
      const normals = g.attributes.normal ? 'N' : 'NO-NORMAL';
      console.log(`${pad}MESH ${o.name} tri=${Math.round(tri)} v=${pos.count} [${mats}] lctr=(${c.x.toFixed(2)},${c.y.toFixed(2)},${c.z.toFixed(2)}) wpos=(${wp.x.toFixed(2)},${wp.y.toFixed(2)},${wp.z.toFixed(2)}) wctr=(${wc.x.toFixed(2)},${wc.y.toFixed(2)},${wc.z.toFixed(2)}) wsize=(${ws.x.toFixed(2)},${ws.y.toFixed(2)},${ws.z.toFixed(2)}) ${normals}`);
    } else {
      console.log(`${pad}${o.type} "${o.name}" wpos=(${wp.x.toFixed(2)},${wp.y.toFixed(2)},${wp.z.toFixed(2)})`);
    }
    for (const ch of o.children) walk(ch, depth + 1);
  }
  walk(root, 0);
  console.log(`--- TOTAL meshes=${meshCount} verts=${totalVert} tris=${Math.round(totalTri)}`);
  console.log(`--- MATERIALS: ${Object.entries(matColors).map(([k, v]) => `${k}=${v}`).join(' ')}`);
}
