#!/usr/bin/env node
/* =====================================================================
   check_sweep3.mjs — Kiểm chứng cuối SWEEP-3 (09/11):
   NPC (phom/mũ/khăn/màu áo/tông da) + TỦ ĐỒ 60 món (neo AR/ARMS/LEGS)
   trên index.html THẬT, chạy trong harness diag (stub DOM/WebGL/GLB).
   Tái dùng pattern của scripts/measure_props.mjs (cắt stub diag_runtime).
   Cách dùng: node scripts/check_sweep3.mjs
   Thoát 0 = mọi kiểm đạt; 1 = có kiểm hỏng.
   ===================================================================== */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = process.env.GAME_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const WORK = '/tmp/diag-runtime-work';

const diagSrc = fs.readFileSync(path.join(ROOT, 'scripts/diag_runtime.mjs'), 'utf8');
const stubEnd = diagSrc.indexOf('// ---------- chuẩn bị bản game đã vá import');
if (stubEnd < 0) { console.error('[sw3] không tìm thấy marker vá import trong diag_runtime.mjs'); process.exit(9); }
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
;globalThis.__sw3 = () => {
  const out = { fails: [] };
  const fail = (m) => out.fails.push(m);
  try {
    // ---- 1. NPC census: wanderers + statics ----
    const NPC_SKINS_SET = new Set(NPC_SKINS.map(c => '#' + c.toString(16).padStart(6, '0')));
    const persons = [];
    for (const p of wanderers) if (p.g) persons.push(p.g);
    for (const p of statics) if (p.g) persons.push(p.g);
    out.persons = persons.length;
    const forms = { puffer: 0, coat: 0, hoodie: 0, other: 0 };
    const shirts = {}, skins = {}, hats = { beanie: 0, nonla: 0, cap: 0, none: 0 };
    let scarvesVis = 0, heldCup = 0, heldBag = 0;
    for (const g of persons) {
      const t = g.getObjectByName('Torso');
      let f = 'other';
      if (t && t.scale.x > 1.2) f = 'puffer';
      else {
        let coat = false, hood = false;
        g.traverse(o => {
          if (o.isMesh && o.geometry === GEO_COATSKIRT) coat = true;
          if (o.isMesh && o.geometry === GEO_NECKTUBE) hood = true;
        });
        if (coat) f = 'coat'; else if (hood) f = 'hoodie';
      }
      forms[f]++;
      if (t && t.material && t.material.color) {
        const hx = '#' + t.material.color.getHexString();
        shirts[hx] = (shirts[hx] || 0) + 1;
      }
      const head = g.getObjectByName('Head');
      if (head) head.traverse(o => {
        // SWEEP-3: recolor() thay material Skin bằng repMat() KHÔNG tên — nhận diện
        // tông da bằng MÀU (NPC_SKINS), không bằng tên material.
        if (o.isMesh && o.material && o.material.color) {
          const hx = '#' + o.material.color.getHexString();
          if (NPC_SKINS_SET.has(hx)) skins[hx] = (skins[hx] || 0) + 1;
        }
      });
      const hb = g.getObjectByName('HatBeanie'), hn = g.getObjectByName('HatNonLa'), hc = g.getObjectByName('HatCap');
      if (hb && hb.visible) hats.beanie++;
      else if (hn && hn.visible) hats.nonla++;
      else if (hc && hc.visible) hats.cap++;
      else hats.none++;
      const sc = g.getObjectByName('Scarf');
      if (sc && sc.visible) scarvesVis++;
      if (g.userData.heldR) heldCup++;
      if (g.userData.heldBag) heldBag++;
    }
    out.forms = forms; out.shirts = shirts; out.skins = skins; out.hats = hats;
    out.scarvesVis = scarvesVis; out.heldCup = heldCup; out.heldBag = heldBag;
    if (persons.length < 300) fail('persons < 300: ' + persons.length);
    if (forms.puffer < 20 || forms.coat < 10 || forms.hoodie < 10) fail('phom thiếu: ' + JSON.stringify(forms));
    if (Object.keys(shirts).length < 10) fail('màu áo distinct < 10: ' + Object.keys(shirts).length);
    if (Object.keys(skins).length < 3) fail('tông da distinct < 3: ' + Object.keys(skins).length);
    if (hats.beanie < 20 || hats.cap < 5) fail('mũ ít: ' + JSON.stringify(hats));

    // ---- 2. Player nodes + limbs ----
    out.playerLimbs = {
      lLeg: !!player.userData.limbs.lLeg, rLeg: !!player.userData.limbs.rLeg,
      lArm: !!player.userData.limbs.lArm, rArm: !!player.userData.limbs.rArm,
    };
    out.playerNodes = {
      Head: !!player.getObjectByName('Head'),
      HatBeanie: !!player.getObjectByName('HatBeanie'),
      HatNonLa: !!player.getObjectByName('HatNonLa'),
      HatCap: !!player.getObjectByName('HatCap'),
      Scarf: !!player.getObjectByName('Scarf'),
    };
    for (const [k, v] of Object.entries(out.playerLimbs)) if (!v) fail('limb thiếu: ' + k);
    for (const [k, v] of Object.entries(out.playerNodes)) if (!v) fail('node player thiếu: ' + k);

    // ---- 3. Tủ đồ: 60 món + neo gắn ----
    out.wdTotal = WARDROBE_DEFS.length;
    const bySlot = {};
    for (const d of WARDROBE_DEFS) bySlot[d.slot] = (bySlot[d.slot] || 0) + 1;
    out.wdBySlot = bySlot;
    if (WARDROBE_DEFS.length !== 63) fail('WARDROBE_DEFS != 63 (60 goc + AO-DOI/NON-DOAN/AO-DOAN cua BLENDER-DEEP-2 muc 15-17): ' + WARDROBE_DEFS.length);
    const visGroups = (id) => {
      const d = WARDROBE_DEFS.find(x => x.id === id);
      if (!d) return -1;
      return d._groups.filter(g => g.visible).length + '/' + d._groups.length;
    };
    const eq0 = JSON.parse(JSON.stringify(state.equipped));
    // equip đủ 1 món mỗi slot + extra AR/ARMS/LEGS
    state.equipped = { hat: 'M1', scarf: 'K1', coat: 'A2', hand: 'T1', shoes: 'G2', extra: ['P1', 'P5'] };
    applyWardrobe();
    const _beanieMesh = (() => { let m = null; const hb = player.getObjectByName('HatBeanie'); if (hb) hb.traverse(o => { if (!m && o.isMesh) m = o; }); return m; })();
    out.wdEquip = {
      hatBeanieVis: player.getObjectByName('HatBeanie').visible,
      hatNonLaVis: player.getObjectByName('HatNonLa').visible,
      scarfVis: player.getObjectByName('Scarf').visible,
      shirtColor: '#' + wdMats.Shirt.color.getHexString(),
      beanieColor: _beanieMesh && _beanieMesh.material.color ? '#' + _beanieMesh.material.color.getHexString() : 'n/a',
      T1_AR: visGroups('T1'), P1_ARMS: visGroups('P1'), P5_LEGS: visGroups('P5'), G2_LEGS: visGroups('G2'),
    };
    if (!out.wdEquip.hatBeanieVis) fail('M1 beanie không hiện');
    if (out.wdEquip.hatNonLaVis) fail('M1 mà HatNonLa vẫn hiện');
    if (!out.wdEquip.scarfVis) fail('K1 scarf không hiện');
    if (out.wdEquip.shirtColor !== '#35507a') fail('A2 shirt color sai: ' + out.wdEquip.shirtColor);
    if (out.wdEquip.beanieColor !== '#a62b25') fail('M1 beanie color sai: ' + out.wdEquip.beanieColor);
    // đổi mũ sang M8 (teal + sọc) — kiểm màu + pattern của mũ
    state.equipped.hat = 'M8';
    applyWardrobe();
    const _beanieMesh2 = (() => { let m = null; const hb = player.getObjectByName('HatBeanie'); if (hb) hb.traverse(o => { if (!m && o.isMesh) m = o; }); return m; })();
    out.wdEquipM8 = {
      beanieColor: _beanieMesh2 && _beanieMesh2.material.color ? '#' + _beanieMesh2.material.color.getHexString() : 'n/a',
      beanieMap: !!(_beanieMesh2 && _beanieMesh2.material.map),
    };
    if (out.wdEquipM8.beanieColor !== '#2f8f83') fail('M8 beanie color sai: ' + out.wdEquipM8.beanieColor);
    if (!out.wdEquipM8.beanieMap) fail('M8 beanie không có map sọc');
    state.equipped.hat = 'M1';
    applyWardrobe();
    for (const k of ['T1_AR', 'P1_ARMS', 'P5_LEGS', 'G2_LEGS']) {
      const v = out.wdEquip[k];
      if (!v || v.startsWith('0/')) fail(k + ' không hiện nhóm nào: ' + v);
    }
    // đổi mũ sang nón lá
    state.equipped.hat = 'M6';
    applyWardrobe();
    out.wdNonLa = {
      hatBeanieVis: player.getObjectByName('HatBeanie').visible,
      hatNonLaVis: player.getObjectByName('HatNonLa').visible,
    };
    if (!out.wdNonLa.hatNonLaVis) fail('M6 nonla không hiện');
    if (out.wdNonLa.hatBeanieVis) fail('M6 mà HatBeanie vẫn hiện');
    // tháo hết
    state.equipped = { hat: null, scarf: null, coat: null, hand: null, shoes: null, extra: [] };
    applyWardrobe();
    out.wdClear = {
      hatBeanieVis: player.getObjectByName('HatBeanie').visible,
      hatNonLaVis: player.getObjectByName('HatNonLa').visible,
      scarfVis: player.getObjectByName('Scarf').visible,
      T1_AR: visGroups('T1'), P1_ARMS: visGroups('P1'),
    };
    if (out.wdClear.hatBeanieVis || out.wdClear.hatNonLaVis || out.wdClear.scarfVis) fail('tháo mũ/khăn mà node vẫn hiện');
    // khôi phục trạng thái ban đầu
    state.equipped = eq0;
    applyWardrobe();
  } catch (e) {
    out.fails.push('EXCEPTION: ' + (e && e.stack || e));
  }
  return out;
};
`;
code += `
;{ // NPC-SPECIAL-1 (09/11): boc __sw3 — kiem them nhan vat dac biet sau khi kiem goc chay xong
  const _origSw3 = globalThis.__sw3;
  globalThis.__sw3 = () => {
    const out = _origSw3();
    const fail = (m) => out.fails.push(m);
    try {
      const hex = (m) => (m && m.material && m.material.color) ? '#' + m.material.color.getHexString() : null;
      const findGeo = (g, geo) => { let f = null; g.traverse(o => { if (!f && o.isMesh && o.geometry === geo) f = o; }); return f; };
      const headMeshesByColor = (g, hx) => { const H = g.getObjectByName('Head'); let n = 0; if (H) H.traverse(o => { if (o.isMesh && hex(o) === hx) n++; }); return n; };
      // ---- 4a. Tieu thuong dac biet (7 sap) ----
      const SV_EXP = {
        banhtrang: { shirt:'#7a4a2e', apron:'#4a6741', hat:'HatBeanie' },
        banhcan:   { shirt:'#6b8f3e', apron:'#5c4633', hat:'HatNonLa' },
        supcua:    { shirt:'#35507a', apron:'#a62b25', hat:'HatCap', cap:'#e8e2d4' },
        sua:       { shirt:'#e8c87e', apron:'#2e6b46', hat:'HatNonLa' },
        caphe:     { shirt:'#96683f', apron:'#8c2f39', hat:'HatBeanie' },
        dau:       { shirt:'#c95d7e', apron:'#d9a62e', hat:'HatBeanie' },
        hoasua:    { shirt:'#e8c87e', apron:'#2e7d6b', hat:'HatBeanie', beanie:'#f0ead8' },
      };
      out.svVendors = {};
      for (const [id, exp] of Object.entries(SV_EXP)) {
        const s = stalls.find(x => x.id === id);
        if (!s) { fail('SV thieu sap ' + id); continue; }
        const v = s.vendor;
        const tor = v.getObjectByName('Torso');
        const ap = findGeo(v, GEO_APRON);
        const r = { shirt: hex(tor), apron: ap ? hex(ap) : null,
          hatVis: ['HatBeanie','HatNonLa','HatCap'].filter(h => { const n = v.getObjectByName(h); return n && n.visible; }) };
        if (exp.cap) { const hc = v.getObjectByName('HatCap'); let cm = null; if (hc) hc.traverse(o => { if (!cm && o.isMesh) cm = o; }); r.cap = hex(cm); }
        if (exp.beanie) { const hb = v.getObjectByName('HatBeanie'); let bm = null; if (hb) hb.traverse(o => { if (!bm && o.isMesh) bm = o; }); r.beanie = hex(bm); }
        out.svVendors[id] = r;
        if (r.shirt !== exp.shirt) fail('SV ' + id + ' shirt ' + r.shirt + ' != ' + exp.shirt);
        if (r.apron !== exp.apron) fail('SV ' + id + ' apron ' + r.apron + ' != ' + exp.apron);
        if (r.hatVis.length !== 1 || r.hatVis[0] !== exp.hat) fail('SV ' + id + ' hat ' + JSON.stringify(r.hatVis) + ' != ' + exp.hat);
        if (exp.cap && r.cap !== exp.cap) fail('SV ' + id + ' cap ' + r.cap + ' != ' + exp.cap);
        if (exp.beanie && r.beanie !== exp.beanie) fail('SV ' + id + ' beanie ' + r.beanie + ' != ' + exp.beanie);
      }
      // ---- 4b. NPC dac biet tinh ----
      out.specials = {};
      const SP_EXP = { chuba:[5.6,-19.6], guard:[37.6,9.6], sweeper:[10.4,10.8], xeom:[-181,17.5] }; // GEOMETRY-2: xeom neo lai o via he nam canh bung binh dau cho (spawn moi)
      if (!Array.isArray(SPECIAL_NPCS)) fail('SPECIAL_NPCS khong ton tai');
      else {
        if (SPECIAL_NPCS.length !== 4) fail('SPECIAL_NPCS != 4: ' + SPECIAL_NPCS.length);
        for (const sp of SPECIAL_NPCS) {
          const e = SP_EXP[sp.id];
          const d = e ? Math.hypot(sp.g.position.x - e[0], sp.g.position.z - e[1]) : -1;
          out.specials[sp.id] = { d: +d.toFixed(2), rank: sp.st.rank, kind: sp.st.kind };
          if (!e) { fail('special la: ' + sp.id); continue; }
          if (d > 0.6) fail('special ' + sp.id + ' lech vi tri d=' + d);
          if (sp.st.rank !== 0) fail('special ' + sp.id + ' rank != 0');
          if (sp.st.kind !== 'special') fail('special ' + sp.id + ' kind != special');
          if (typeof sp.st.spIdle !== 'function') fail('special ' + sp.id + ' thieu spIdle');
        }
        const byId = (id) => { const s = SPECIAL_NPCS.find(x => x.id === id); return s && s.g; };
        const cb = byId('chuba');
        if (cb) {
          if (headMeshesByColor(cb, '#23272e') < 3) fail('chuba thieu kinh (dark meshes < 3)');
          if (headMeshesByColor(cb, '#b8b0a2') < 1) fail('chuba thieu rau bac');
          if (headMeshesByColor(cb, '#27324e') < 2) fail('chuba thieu khan xep');
          const tor = cb.getObjectByName('Torso');
          if (hex(tor) !== '#37455e') fail('chuba ao dai sai mau: ' + hex(tor));
        }
        const gd2 = byId('guard');
        if (gd2) {
          let stripes = 0, ticket = false;
          gd2.traverse(o => { if (o.isMesh && hex(o) === '#d8dde2') stripes++; if (o.isMesh && hex(o) === '#f5f2e8') ticket = true; });
          if (stripes < 2) fail('guard thieu soc phan quang: ' + stripes);
          if (!ticket) fail('guard thieu ve cam tay');
          const tor = gd2.getObjectByName('Torso');
          if (hex(tor) !== '#c8d93c') fail('guard ao da quang sai: ' + hex(tor));
        }
        const wk2 = byId('sweeper');
        if (wk2) {
          if (!wk2.userData.broom) fail('sweeper thieu choi (userData.broom)');
          let gloves = 0; wk2.traverse(o => { if (o.isMesh && o.geometry === GEO_GLOVE) gloves++; });
          if (gloves < 2) fail('sweeper thieu gang: ' + gloves);
        }
        const xo2 = byId('xeom');
        if (xo2) {
          if (headMeshesByColor(xo2, '#35a04f') < 1) fail('xeom thieu mu bao hiem xanh');
          if (!xo2.userData.heldR) fail('xeom thieu dien thoai cam tay');
        }
      }
      // ---- 4c. Ca si san khau ----
      {
        const tor = singer.getObjectByName('Torso');
        if (hex(tor) !== '#2f4d6e') fail('singer ao sai: ' + hex(tor));
        const hc = singer.getObjectByName('HatCap');
        if (!hc || !hc.visible) fail('singer cap khong hien');
        let cm = null; if (hc) hc.traverse(o => { if (!cm && o.isMesh) cm = o; });
        if (hex(cm) !== '#8c2f39') fail('singer cap sai mau: ' + hex(cm));
        if (headMeshesByColor(singer, '#23272e') < 3) fail('singer thieu kinh mat');
        let guitar = false;
        for (const c of singer.children) c.traverse(o => { if (o.isMesh && o.geometry && o.geometry.parameters && o.geometry.parameters.radiusTop === 0.26) guitar = true; });
        out.singer = { shirt: hex(tor), cap: hex(cm), guitar };
        if (!guitar) fail('singer thieu dan guitar');
      }
      // ---- 4c. GEOMETRY-2: moi wanderer phai co y huu han (loi routeY cu: rt thua phan tu thu 3 lam 55/59 wanderer y=NaN vinh vien -> vo hinh tren trinh duyet) ----
      let yBad = 0;
      for (const w of wanderers) { if (!w.g || !Number.isFinite(w.g.position.y)) yBad++; }
      out.wandererYBad = yBad;
      if (yBad) fail('GEOMETRY-2: ' + yBad + ' wanderer co y khong huu han');
    } catch (e) { out.fails.push('SP1 EXCEPTION: ' + (e && e.stack || e)); }
    return out;
  };
}
`;
const patchedPath = path.join(WORK, 'game_sw3.mjs');
fs.writeFileSync(patchedPath, header + code);
const t0 = Date.now();
try {
  await import(patchedPath);
  console.log('[sw3] MODULE INIT OK sau', Date.now() - t0, 'ms');
} catch (e) {
  console.error('[sw3] *** NGOẠI LỆ TRONG INIT ***');
  console.error(e && e.stack || e);
  process.exit(2);
}
await new Promise(r => setTimeout(r, 800));
const res = globalThis.__sw3();
console.log(JSON.stringify(res, null, 1));
if (res.fails && res.fails.length) {
  console.error('[sw3] FAILS:', res.fails.length);
  process.exit(1);
}
console.log('[sw3] ALL CHECKS PASS');
process.exit(0);
