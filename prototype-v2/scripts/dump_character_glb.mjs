#!/usr/bin/env node
/* dump_character_glb.mjs — Dump baseline/kiểm chứng character.glb (CROWD-OPT-1).
   Dùng: node scripts/dump_character_glb.mjs [path/to/character.glb]
   In: cây node (tên object, vị trí origin) + tri gộp theo node cha gần nhất
   có tên trong danh sách neo + tổng tri/verts.
   Cần three r160 tại /tmp/diag/node_modules (như diag_runtime). */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const glbPath = process.argv[2] || path.join(ROOT, 'assets/character.glb');
const buf = fs.readFileSync(glbPath);
const loader = new GLTFLoader();
const gltf = await loader.parseAsync(buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength), '');
const root = gltf.scene;
const ANCHORS = ['LegL','LegR','ArmL','ArmR','Torso','Head','HatNonLa','HatBeanie','HatCap','Scarf','tmpCollar'];
let totalTri = 0, totalVert = 0, meshCount = 0;
const agg = {};
function addAgg(name, tri, verts) {
  if (!agg[name]) agg[name] = { tri: 0, verts: 0, meshes: 0 };
  agg[name].tri += tri; agg[name].verts += verts; agg[name].meshes++;
}
function walk(o, depth, anchor) {
  const isAnchor = ANCHORS.includes(o.name);
  const cur = isAnchor ? o.name : anchor;
  const pad = '  '.repeat(depth);
  if (o.isMesh) {
    meshCount++;
    const g = o.geometry;
    const pos = g.attributes.position;
    const idx = g.index;
    const tri = idx ? idx.count / 3 : pos.count / 3;
    totalTri += tri; totalVert += pos.count;
    addAgg(cur || '(root)', tri, pos.count);
    g.computeBoundingBox();
    const bb = g.boundingBox;
    console.log(`${pad}MESH ${o.name} tri=${Math.round(tri)} verts=${pos.count} mats=${Array.isArray(o.material) ? o.material.map(m=>m.name).join('+') : o.material.name} bbY=[${bb.min.y.toFixed(2)},${bb.max.y.toFixed(2)}]`);
  } else {
    console.log(`${pad}${o.type} ${o.name || '(unnamed)'} pos=(${o.position.x.toFixed(2)},${o.position.y.toFixed(2)},${o.position.z.toFixed(2)})`);
  }
  for (const c of o.children) walk(c, depth + 1, cur);
}
console.log('GLB:', glbPath, 'size:', fs.statSync(glbPath).size, 'bytes');
walk(root, 0, null);
console.log('--- AGGREGATE per anchor ---');
for (const [k, v] of Object.entries(agg)) console.log(k, 'meshes=', v.meshes, 'verts=', v.verts, 'tris=', Math.round(v.tri));
console.log('TOTAL meshes:', meshCount, 'verts:', totalVert, 'tris:', Math.round(totalTri));
console.log('--- ANCHOR CHECK ---');
for (const n of ANCHORS) {
  const o = root.getObjectByName(n);
  if (o) {
    const bb = new THREE.Box3().setFromObject(o);
    console.log('NODE', n, 'FOUND pos=', o.position.toArray().map(v=>+v.toFixed(3)).join(','), 'worldBB_Y=[', bb.min.y.toFixed(3), ',', bb.max.y.toFixed(3), '] size=', [bb.max.x-bb.min.x, bb.max.y-bb.min.y, bb.max.z-bb.min.z].map(v=>+v.toFixed(3)).join('x'));
  } else console.log('NODE', n, 'MISSING');
}
