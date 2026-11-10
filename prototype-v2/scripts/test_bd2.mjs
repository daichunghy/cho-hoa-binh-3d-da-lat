#!/usr/bin/env node
/* =====================================================================
   test_bd2.mjs — Kiểm chứng BLENDER-DEEP-2 (09/11): mục 7 nước chảy,
   mục 8 âm thanh theo khoảng cách, mục 9 coi bói 3 kiểu, mục 10 chu kỳ
   nhà lồng đóng/mở, mục 12-14 hàng hóa + tiệm lớn + quần áo, mục 15-17
   3 chế độ chơi. Chạy trên index.html THẬT trong harness diag (như
   check_sweep3). Thoát 0 = đạt hết; 1 = có kiểm hỏng.
   Cách dùng: node scripts/test_bd2.mjs
   ===================================================================== */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = process.env.GAME_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const WORK = '/tmp/diag-runtime-work';

const diagSrc = fs.readFileSync(path.join(ROOT, 'scripts/diag_runtime.mjs'), 'utf8');
const stubEnd = diagSrc.indexOf('// ---------- chuẩn bị bản game đã vá import');
if (stubEnd < 0) { console.error('[bd2] không tìm thấy marker vá import trong diag_runtime.mjs'); process.exit(9); }
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
;globalThis.__bd2 = () => {
  const out = { fails: [], info: {} };
  const fail = (m) => out.fails.push(m);
  const M = window.__MODES;
  try {
    // ---------- mục 7: NƯỚC CHẢY (thay đổi theo frame) ----------
    out.info.water = { surfs: WATER_FX.surfs.length, jets: WATER_FX.jets.length, rings: WATER_FX.rings.length };
    if (WATER_FX.surfs.length < 1) fail('water: khong co mat nuoc dang ky');
    if (WATER_FX.jets.length < 7) fail('water: tia phun < 7: ' + WATER_FX.jets.length);
    if (WATER_FX.rings.length < 2) fail('water: vong gon < 2');
    tickWater(0);
    const sf = WATER_FX.surfs[0], jt = WATER_FX.jets[0], rg = WATER_FX.rings[0];
    const a = { y: sf.m.position.y, o: sf.m.material.opacity, js: jt.scale.y, rs: rg.m.scale.x };
    tickWater(1.3);
    const b = { y: sf.m.position.y, o: sf.m.material.opacity, js: jt.scale.y, rs: rg.m.scale.x };
    out.info.waterDelta = { dy: +(b.y - a.y).toFixed(4), do: +(b.o - a.o).toFixed(4), dJet: +(b.js - a.js).toFixed(4), dRing: +(b.rs - a.rs).toFixed(3) };
    if (Math.abs(b.y - a.y) < 0.005) fail('water: mat bon khong gon theo frame');
    if (Math.abs(b.js - a.js) < 0.01) fail('water: tia phun khong nhap nho theo frame');
    if (Math.abs(b.rs - a.rs) < 0.05) fail('water: vong gon khong lan theo frame');

    // ---------- mục 8: ÂM THANH THEO KHOẢNG CÁCH ----------
    const at = (x, z) => { playerState.x = x; playerState.z = z; return ambSpatial(); };
    const sNear = at(33, -50).stage, sMid = at(0, -20).stage, sFar = at(101, -42).stage;
    out.info.stage = { near: sNear, mid: sMid, far: sFar };
    if (!(sNear.g > sMid.g && sMid.g > sFar.g)) fail('spatial stage gain khong giam theo khoang cach: ' + [sNear.g, sMid.g, sFar.g].join('/'));
    if (!(sNear.f > sMid.f && sMid.f > sFar.f)) fail('spatial stage filter khong mo dan theo khoang cach: ' + [sNear.f, sMid.f, sFar.f].join('/'));
    if (sNear.g < 0.9) fail('spatial stage: dung gan phai gan nhu ro het: g=' + sNear.g);
    const fNear = at(28, 6).fnt, fFar = at(-100, 5).fnt;
    out.info.fnt = { near: fNear, far: fFar };
    if (!(fNear.g > fFar.g && fNear.f > fFar.f)) fail('spatial dai phun khong giam theo khoang cach');

    // ---------- mục 9: COI BÓI 3 KIỆU ----------
    const runs = {};
    for (const tp of ['bai', 'mat', 'tay']) {
      const seen = new Set();
      for (let i = 0; i < 40; i++) seen.add(fortuneResultFor(tp).x);
      runs[tp] = seen.size;
      if (seen.size < 10) fail('fortune ' + tp + ': chi ' + seen.size + ' ket qua phan biet sau 40 luot (can >=10)');
    }
    out.info.fortuneDistinct = runs;
    const oneBai = fortuneResultFor('bai').x, oneMat = fortuneResultFor('mat').x, oneTay = fortuneResultFor('tay').x;
    if (!CARD_DECK.some(c => oneBai.includes(c.n))) fail('fortune bai: ket qua khong chua ten la trong CARD_DECK');
    if (!oneMat.includes('Trán')) fail('fortune mat: thieu luan net Trang');
    if (!oneTay.includes('Sinh Đạo')) fail('fortune tay: thieu duong Sinh Dao');
    if (!oneBai.includes('Chú Ba') && !oneBai.includes('chú')) fail('fortune: thieu giong Chu Ba (xung chu)');
    state.xu = 500; const fc0 = state.fortuneCount || 0; fortuneType = 'tay';
    drawFortune();
    if (state.xu !== 480) fail('drawFortune: khong tru dung 20 Xu (con ' + state.xu + ')');
    if ((state.fortuneCount || 0) !== fc0 + 1) fail('drawFortune: fortuneCount khong tang');

    // ---------- mục 10+13: CHU KỲ NHÀ LỒNG + TIỆM LỚN ĐÓNG 22H ----------
    const stById = id => stalls.find(x => x.id === id);
    const rau = stById('rau'), dac = stById('dacsan'), lon = stById('dacsanlon'), ngoai = stById('banhtrang');
    if (!rau || !dac || !lon || !ngoai) fail('hall: thieu sap kiem tra');
    const atHour = (h) => { gameHourF = h; hallTick(); };
    atHour(12);
    out.info.hall12 = { rauClosed: rau.closed, dacClosed: dac.closed, lonClosed: lon.closed, rauShutter: rau.shutter.visible };
    if (rau.closed) fail('hall 12h: quay trong nha long phai MO');
    if (rau.shutter.visible) fail('hall 12h: cua cuon phai an');
    atHour(18.75);
    out.info.hall1875 = { pShutterY: rau.shutter.position.y, vis: rau.shutter.visible };
    if (!rau.shutter.visible) fail('hall 18:45: cua cuon phai dang ha (visible)');
    if (Math.abs(rau.shutter.position.y - 2.5) < 0.05 || Math.abs(rau.shutter.position.y - 1.32) < 0.05) fail('hall 18:45: cua cuon phai o giua chung (mo mot nua), y=' + rau.shutter.position.y);
    atHour(20);
    out.info.hall20 = { rauClosed: rau.closed, rauVendor: rau.vendor.visible, dacClosed: dac.closed, lonClosed: lon.closed, ngoaiClosed: ngoai.closed };
    if (!rau.closed) fail('hall 20h: quay thuong trong nha long phai DONG');
    if (rau.vendor.visible) fail('hall 20h: tieu thuong trong nha phai roi vi tri');
    if (dac.closed) fail('hall 20h: quay dac san phai con mo toi 22h');
    if (lon.closed) fail('hall 20h: tiem lon dac san phai con mo toi 22h');
    if (ngoai.closed) fail('hall 20h: sap ngoai troi khong duoc dong');
    atHour(23);
    out.info.hall23 = { dacClosed: dac.closed, lonClosed: lon.closed };
    if (!dac.closed) fail('hall 23h: quay dac san phai DONG sau 22h');
    if (!lon.closed) fail('hall 23h: tiem lon phai DONG sau 22h');
    atHour(12); // dua ve ngay de cac kiem sau khong bi anh huong

    // ---------- mục 12-14: HÀNG HÓA + TIỆM + QUẦN ÁO ----------
    out.info.stallCount = STALL_DEFS.length;
    if (STALL_DEFS.length !== 45) fail('goods: STALL_DEFS phai = 45 (44 cua BD2 + 1 sap V6 Antigravity, id phan biet du — V7-IMPROVE-1 doi chuan), thay ' + STALL_DEFS.length);
    const dauIds = STALL_DEFS.filter(d => ['dau', 'dau2', 'dau3', 'dau4'].includes(d.id)).length;
    if (dauIds !== 4) fail('goods: phai co 4 quay dau, thay ' + dauIds);
    for (const id of ['mut', 'hong', 'tra2', 'hoa2', 'luuniem2', 'dosi', 'len3', 'dacsanlon'])
      if (!stById(id)) fail('goods: thieu sap runtime ' + id);
    if (Math.abs(groundH(51.5, 20)) > 0.01) fail('shop: groundH tai tiem lon phai = 0, thay ' + groundH(51.5, 20));
    const ak = STALL_DEFS.find(d => d.id === 'aokhoac');
    if (ak.name.includes('\\uFFFD')) fail('quanao: ten aokhoac con ky tu loi U+FFFD');
    out.info.aokhoacName = ak.name;

    // ---------- mục 18: PHỐ ĐÊM (loa chợ / bước chân / cửa cuốn phố) ----------
    const S = window.__BD2_STREET;
    if (!S) fail('street: window.__BD2_STREET khong ton tai');
    else {
      const lgN = S.loaGainAt(-131, 2), lgM = S.loaGainAt(-60, 2), lgF = S.loaGainAt(60, -52);
      out.info.loa = { near: +lgN.toFixed(3), mid: +lgM.toFixed(3), far: +lgF.toFixed(3), fNear: Math.round(S.loaFreqAt(-131, 2)), fFar: Math.round(S.loaFreqAt(60, -52)) };
      if (!(lgN > lgM && lgM > lgF)) fail('loa: gain khong giam dan theo khoang cach: ' + [lgN, lgM, lgF].join('/'));
      if (!(lgF > 0 && lgF < 0.1)) fail('loa: o xa phai con nghe rat nho (floor > 0), thay ' + lgF);
      if (!(S.loaFreqAt(-131, 2) > S.loaFreqAt(60, -52))) fail('loa: tan so loc phai thap dan khi xa (mo tieng)');
      const sf1 = S.surfaceAt(-100, 5), sf2 = S.surfaceAt(-100, -17), sf3 = S.surfaceAt(-56, -15), sf4 = S.surfaceAt(0, 20); // LAYOUT-FIX-1: diem mau 'thang' theo tam thang moi -56
      out.info.surfaces = { road: sf1, sidewalk: sf2, stairs: sf3, hall: sf4 };
      if (new Set([sf1, sf2, sf3, sf4]).size !== 4) fail('buoc chan: 4 mat duong phai khac nhau, thay ' + [sf1, sf2, sf3, sf4].join('/'));
      const sc0 = S.stepCount(); S.playStep('nhua');
      if (S.stepCount() !== sc0 + 1 || S.lastSurface() !== 'nhua') fail('buoc chan: playStep nhua khong ghi nhan');
      S.playStep('thang');
      if (S.lastSurface() !== 'thang') fail('buoc chan: doi mat duong khong doi mau buoc chan');
      gameHourF = 12; hallTick();
      const visDay = S.shutters.filter(m => m.visible).length;
      gameHourF = 20; hallTick();
      const visNight = S.shutters.filter(m => m.visible).length;
      out.info.shopShutters = { total: S.shutters.length, visDay, visNight };
      if (S.shutters.length !== 14) fail('street: phai co 14 cua cuon mat tien pho, thay ' + S.shutters.length);
      if (visDay !== 0) fail('street: ban ngay cua cuon pho phai mo het (an), thay ' + visDay + ' cai ha');
      if (visNight < 10) fail('street: ban dem da so cua cuon phai ha, thay ' + visNight + '/14');
      gameHourF = 12; hallTick();
    }

    // ---------- mục 15-17: CHẾ ĐỘ CHƠI ----------
    if (!M) fail('modes: window.__MODES khong ton tai');
    else {
      const sim = (t0, secs) => { let tt = t0; const steps = Math.ceil(secs / 0.08); for (let i = 0; i < steps; i++) { tt += 0.08; M.tickModes(tt); } return tt; };
      let T = 100;
      // Couple: 1 nguoi di theo
      M.setMode('couple');
      if (M.companions.length !== 1) fail('couple: phai spawn dung 1 nguoi thuong, thay ' + M.companions.length);
      player.position.set(0, 0, 20); T = sim(T, 0.5);
      player.position.set(30, 0, 20); T = sim(T, 6);
      const pd = Math.hypot(M.companions[0].g.position.x - 30, M.companions[0].g.position.z - 20);
      out.info.coupleFollowDist = +pd.toFixed(2);
      if (pd > 3.2) fail('couple: nguoi thuong khong bam kip sau 6s mo phong, lech ' + pd.toFixed(2) + 'u');
      // mua dau -> tich viec
      state.xu = 900; cooking = null;
      const d2 = stById('dau2'); buyItem(d2, d2.menu[0]); cooking = null;
      if (!M.mProg('couple').t.dau) fail('couple: mua dau o dau2 khong tich viec dau');
      // Gia dinh: 3 nguoi... (4 thanh vien tinh ca Be)
      M.setMode('family');
      if (M.companions.length !== 4) fail('family: phai spawn 4 thanh vien (Ba/Bo/Me/Be), thay ' + M.companions.length);
      player.position.set(-60, 0, 0); T = sim(T, 0.5);
      player.position.set(-20, 0, 0); T = sim(T, 7);
      const worst = Math.max(...M.companions.map(c => Math.hypot(c.g.position.x + 20, c.g.position.z)));
      out.info.familyWorstDist = +worst.toFixed(2);
      if (worst > 7) fail('family: thanh vien cham nhat lech ' + worst.toFixed(2) + 'u sau 7s');
      const t2 = stById('tra2'); cooking = null; buyItem(t2, t2.menu[0]); cooking = null;
      if (!M.mProg('family').t.ba) fail('family: mua Tra atiso khong tich mong muon cua Ba');
      // Theo doan: xe chay vao -> doan xuong xe -> check-in diem 1
      M.setMode('tour');
      if (!M.tourState || M.tourState.phase !== 'drive') fail('tour: phai bat dau bang su kien doan xe');
      T = sim(T, 16);
      if (!M.tourState || M.tourState.phase !== 'walk') fail('tour: doan xe khong vao xong / doan chua xuong xe');
      const members = M.companions.filter(c => c.leader).length;
      out.info.tourMembers = members;
      if (members !== 10) fail('tour: phai co 10 doan vien ao doan, thay ' + members);
      player.position.set(-146, groundH(-146, 8), 8); T = sim(T, 7);
      out.info.tourCp = M.mProg('tour').cp;
      if (M.mProg('tour').cp < 1) fail('tour: dung o diem tap ket 5s khong check-in duoc');
      // save/load giu tien do
      save();
      const sv = JSON.parse(localStorage.getItem('chohb3d-v1'));
      if (!sv.modeProg || !sv.modeProg.couple.t.dau || !sv.modeProg.family.t.ba || sv.modeProg.tour.cp < 1) fail('modes: save khong giu tien do tung che do');
      if (sv.mode !== 'tour') fail('modes: save khong giu che do hien tai');
      M.setMode('solo');
      if (M.companions.length !== 0) fail('solo: phai don ban dong hanh cu');
      out.info.modes = 'ok';
    }
  } catch (e) { out.fails.push('BD2 EXCEPTION: ' + (e && e.stack || e)); }
  return out;
};
`;

const patchedPath = path.join(WORK, 'game_bd2.mjs');
fs.writeFileSync(patchedPath, header + code);
const t0 = Date.now();
try {
  await import(patchedPath);
  console.log('[bd2] MODULE INIT OK sau', Date.now() - t0, 'ms');
} catch (e) {
  console.error('[bd2] *** NGOẠI LỆ TRONG INIT ***');
  console.error(e && e.stack || e);
  process.exit(2);
}
await new Promise(r => setTimeout(r, 800));
const res = globalThis.__bd2();
console.log(JSON.stringify(res, null, 1));
if (res.fails && res.fails.length) {
  console.error('[bd2] FAILS:', res.fails.length);
  for (const f of res.fails) console.error(' -', f);
  process.exit(1);
}
console.log('[bd2] ALL CHECKS PASS');
process.exit(0);
