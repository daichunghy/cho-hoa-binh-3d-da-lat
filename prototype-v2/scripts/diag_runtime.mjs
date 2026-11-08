#!/usr/bin/env node
/* =====================================================================
   diag_runtime.mjs — Harness CHẨN ĐOÁN RUNTIME cho Chợ Hòa Bình 3D.
   Ra đời sau sự cố MÀN HÌNH ĐEN 08/11/2026: bản chốt v5.1+v5.2+v5.3 chết
   ngay khi nạp trên máy thật dù node --check đạt, vì node --check chỉ
   kiểm CÚ PHÁP — không chạy code.

   Harness này THỰC THI nguyên văn module script của index.html trong
   Node: stub DOM/canvas/localStorage/rAF tối thiểu, WebGLRenderer giả,
   GLTFLoader THẬT nạp GLB thật từ assets/ qua fetch-đọc-đĩa, three
   r160 thật. Nó chạy hết init top-level rồi bơm N frame animate, bắt
   ngoại lệ đầu tiên kèm stack đầy đủ.

   Cách dùng:
     node scripts/diag_runtime.mjs [so_frame]     (mặc định 60)
     SEED_SAVE=1 node scripts/diag_runtime.mjs    (seed save cũ chohb3d-v1)
   Cần gói three r160: đặt tại /tmp/diag/node_modules/three
   (build/three.module.js + examples/jsm/loaders/GLTFLoader.js +
   examples/jsm/utils/BufferGeometryUtils.js + package.json exports),
   hoặc trỏ DIAG_NODE_MODULES=<thư mục chứa node_modules có three>.
   Thoát mã: 0 sạch · 2 lỗi init · 3 lỗi animate.
   ===================================================================== */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = process.env.GAME_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const FRAMES = parseInt(process.argv[2] || process.env.FRAMES || '60', 10);
const WORK = '/tmp/diag-runtime-work';

// --- chuẩn bị thư mục làm việc có node_modules/three ---
const nmSrc = process.env.DIAG_NODE_MODULES
  || (fs.existsSync('/tmp/diag/node_modules/three') ? '/tmp/diag/node_modules' : null)
  || (fs.existsSync(path.join(ROOT, 'node_modules/three')) ? path.join(ROOT, 'node_modules') : null);
if (!nmSrc) { console.error('[diag] KHÔNG tìm thấy gói three — xem hướng dẫn đầu file.'); process.exit(9); }
fs.mkdirSync(WORK, { recursive: true });
const nmDst = path.join(WORK, 'node_modules');
try { fs.rmSync(nmDst, { recursive: true, force: true }); } catch (e) {}
fs.symlinkSync(nmSrc, nmDst, 'dir');

process.on('unhandledRejection', e => { console.error('[unhandledRejection]', e && e.stack || e); });

// ---------- canvas 2d stub ----------
function makeCtx2d(canvas) {
  const base = {
    canvas,
    measureText: () => ({ width: 42 }),
    getImageData: (x, y, w, h) => ({ data: new Uint8ClampedArray(Math.max(0, w * h * 4)), width: w, height: h }),
    createLinearGradient: () => ({ addColorStop() {} }),
    createRadialGradient: () => ({ addColorStop() {} }),
    createPattern: () => ({}),
  };
  return new Proxy(base, {
    get(t, k) { if (k in t) return t[k]; if (typeof k === 'string') return () => {}; return undefined; },
    set() { return true; },
  });
}
function makeCanvas() {
  const c = {
    width: 300, height: 150, style: {}, dataset: {},
    classList: { add() {}, remove() {}, toggle() {}, contains: () => false },
    getContext(kind) { if (kind === '2d') return makeCtx2d(c); return null; },
    addEventListener() {}, removeEventListener() {},
    setPointerCapture() {}, releasePointerCapture() {},
    getBoundingClientRect: () => ({ left: 0, top: 0, right: 0, bottom: 0, width: 0, height: 0 }),
    appendChild(x) { return x; },
    toDataURL: () => 'data:,',
  };
  return c;
}

// ---------- DOM element stub ----------
function makeEl(tag = 'div') {
  if (tag === 'canvas') return makeCanvas();
  const el = {
    tagName: String(tag).toUpperCase(),
    children: [], style: {}, dataset: {}, className: '', id: '',
    textContent: '', innerHTML: '', value: '', disabled: false, checked: false,
    classList: { add() {}, remove() {}, toggle() {}, contains: () => false },
    appendChild(x) { el.children.push(x); return x; },
    removeChild(x) { return x; },
    remove() {},
    addEventListener() {}, removeEventListener() {},
    setAttribute() {}, getAttribute: () => null,
    querySelector: () => makeEl(),
    querySelectorAll: () => [],
    getContext(kind) { if (kind === '2d') return makeCtx2d(el); return null; },
    width: 300, height: 150,
    closest: () => null,
    getBoundingClientRect: () => ({ left: 0, top: 0, right: 0, bottom: 0, width: 0, height: 0 }),
    setPointerCapture() {}, releasePointerCapture() {},
    focus() {}, blur() {}, click() {},
  };
  Object.defineProperty(el, 'parentElement', { get() { if (!el._pe) el._pe = makeEl(); return el._pe; } });
  return el;
}
const elCache = new Map();
const documentStub = {
  getElementById(id) { if (!elCache.has(id)) { const e = makeEl(); e.id = id; elCache.set(id, e); } return elCache.get(id); },
  createElement: tag => makeEl(tag),
  createElementNS: (ns, tag) => makeEl(tag),
  querySelector: () => makeEl(),
  querySelectorAll: () => [],
  addEventListener() {}, removeEventListener() {},
  body: makeEl('body'),
  documentElement: makeEl('html'),
  hidden: false,
  visibilityState: 'visible',
};

// ---------- global window/browser stubs ----------
const rafQueue = [];
const storage = new Map();
globalThis.window = globalThis;
globalThis.document = documentStub;
globalThis.innerWidth = 1280;
globalThis.innerHeight = 800;
globalThis.devicePixelRatio = 1;
if (process.env.SEED_SAVE === '1') {
  storage.set('chohb3d-v1', JSON.stringify({ xu: 1250, bag: [{ id: 'xoi', n: 1 }], stamps: { 'bung-binh': true }, eaten: {}, questDone: true, xp: 640 }));
  console.log('[diag] đã seed save cũ chohb3d-v1');
}
globalThis.localStorage = {
  getItem: k => (storage.has(k) ? storage.get(k) : null),
  setItem: (k, v) => storage.set(k, String(v)),
  removeItem: k => storage.delete(k),
};
globalThis.requestAnimationFrame = cb => { rafQueue.push(cb); return rafQueue.length; };
globalThis.cancelAnimationFrame = () => {};
globalThis.addEventListener = () => {};
globalThis.removeEventListener = () => {};
globalThis.location = { href: 'file:///diag/', protocol: 'file:' };
globalThis.ProgressEvent = class ProgressEvent {
  constructor(type, init = {}) { this.type = type; this.loaded = init.loaded || 0; this.total = init.total || 0; this.lengthComputable = !!init.lengthComputable; }
};
try { Object.defineProperty(globalThis, 'navigator', { value: { userAgent: 'diag-node', maxTouchPoints: 0 }, configurable: true }); } catch (e) {}

// fetch: phục vụ assets/*.glb từ đĩa cho GLTFLoader; URL http -> lỗi như offline
const RealRequest = globalThis.Request;
globalThis.Request = class extends RealRequest {
  constructor(input, init) {
    if (typeof input === 'string' && !/^[a-z][a-z0-9+.-]*:/i.test(input)) input = 'filediag://' + input.replace(/^\.?\//, '');
    super(input, init);
  }
};
globalThis.fetch = async (input) => {
  const u = typeof input === 'string' ? input : input.url;
  if (u.startsWith('data:')) { // bản standalone: GLB nhúng data-URI — giải mã như fetch của trình duyệt
    const b64 = u.slice(u.indexOf(',') + 1);
    return new Response(Buffer.from(b64, 'base64'), { status: 200 });
  }
  if (/^https?:\/\//i.test(u)) throw new Error('diag: network disabled for ' + u);
  const rel = u.replace(/^filediag:\/\//, '').replace(/^\.?\//, '');
  const buf = fs.readFileSync(path.join(ROOT, rel));
  return new Response(buf, { status: 200, headers: { 'Content-Type': 'model/gltf-binary' } });
};

// ---------- chuẩn bị bản game đã vá import (WebGLRenderer giả) ----------
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
  setPixelRatio() {} setSize() {} setViewport() {} setScissor() {}
  render() { this.info.render.calls++; }
  dispose() {} setAnimationLoop() {}
  getContext() { return null; }
  forceContextLoss() {}
}
const THREE = { ..._THREE, WebGLRenderer: FakeWebGLRenderer };
`;
const patchedPath = path.join(WORK, 'game_patched.mjs');
fs.writeFileSync(patchedPath, header + code);
console.log('[diag] game_patched.mjs bytes =', (header + code).length, '| frames =', FRAMES);

// ---------- chạy ----------
const t0 = Date.now();
try {
  await import(patchedPath);
  console.log('[diag] MODULE INIT OK sau', Date.now() - t0, 'ms — rafQueue =', rafQueue.length);
} catch (e) {
  console.error('[diag] *** NGOẠI LỆ TRONG INIT ***');
  console.error(e && e.stack || e);
  process.exit(2);
}
let ts = 0;
for (let f = 0; f < FRAMES; f++) {
  const cbs = rafQueue.splice(0, rafQueue.length);
  if (!cbs.length) { console.log('[diag] frame', f, ': không còn callback rAF — animate đã dừng'); break; }
  ts += 16.7;
  try { for (const cb of cbs) cb(ts); }
  catch (e) {
    console.error('[diag] *** NGOẠI LỆ TRONG ANIMATE frame', f, '***');
    console.error(e && e.stack || e);
    process.exit(3);
  }
}
console.log('[diag] ANIMATE', FRAMES, 'frames SẠCH — không ngoại lệ.');
process.exit(0);
