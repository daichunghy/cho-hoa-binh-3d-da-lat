# -*- coding: utf-8 -*-
"""REALISM-1 patcher: texture mặt đất + cửa sổ đêm ngẫu nhiên + phụ kiện
shophouse/sạp + dây điện ngang + xe đậu cụm + đa dạng người.
Chạy 1 lần, assert từng thay đúng 1 lần — không thấy thì DỪNG, không đoán."""
import sys
P = '/home/hatch/workspace/cho-hoa-binh-3d/prototype-v2/index.html'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    assert c == n, f'[{tag}] tim thay {c} (can {n}): {old[:80]!r}'
    s = s.replace(old, new)
    print('OK', tag)

# ================= PATCH 1a: khối texture canvas ngay sau mat() =================
REAL1_TEX = r"""
// ================= REALISM-1: TEXTURE CANVAS MẶT ĐẤT (runtime, 0 byte asset) =================
function makeGroundTex(drawFn){
  const c = document.createElement('canvas'); c.width = 256; c.height = 256;
  drawFn(c.getContext('2d'));
  const t = new THREE.CanvasTexture(c);
  t.wrapS = t.wrapT = THREE.RepeatWrapping; t.colorSpace = THREE.SRGBColorSpace;
  return t;
}
let _r1Seed = 987654321;
function _r1Rnd(){ _r1Seed = (_r1Seed * 1103515245 + 12345) % 2147483648; return _r1Seed / 2147483648; }
const TEX_ASPHALT = makeGroundTex(x2 => {
  x2.fillStyle = '#ffffff'; x2.fillRect(0, 0, 256, 256);
  for(let i = 0; i < 2600; i++){
    x2.fillStyle = _r1Rnd() < 0.5 ? '#3a3a3a' : '#ffffff';
    x2.globalAlpha = 0.05 + _r1Rnd() * 0.11;
    x2.fillRect(_r1Rnd() * 256, _r1Rnd() * 256, 1 + _r1Rnd() * 2, 1 + _r1Rnd() * 2);
  }
  x2.globalAlpha = 1;
  for(let i = 0; i < 5; i++){
    x2.fillStyle = 'rgba(60,58,55,' + (0.10 + _r1Rnd() * 0.06).toFixed(3) + ')';
    const w = 30 + _r1Rnd() * 70, h = 20 + _r1Rnd() * 50;
    x2.beginPath(); x2.roundRect(_r1Rnd() * (256 - w), _r1Rnd() * (256 - h), w, h, 6); x2.fill();
  }
  x2.strokeStyle = 'rgba(40,38,36,0.18)'; x2.lineWidth = 1;
  for(let i = 0; i < 3; i++){
    x2.beginPath(); let px = _r1Rnd() * 256, py = _r1Rnd() * 256; x2.moveTo(px, py);
    for(let k = 0; k < 5; k++){ px += (_r1Rnd() - 0.5) * 36; py += (_r1Rnd() - 0.5) * 36; x2.lineTo(px, py); }
    x2.stroke();
  }
});
const TEX_TILE = makeGroundTex(x2 => {
  x2.fillStyle = '#ffffff'; x2.fillRect(0, 0, 256, 256);
  for(let i = 0; i < 900; i++){
    x2.fillStyle = _r1Rnd() < 0.5 ? '#3a3a3a' : '#ffffff';
    x2.globalAlpha = 0.04 + _r1Rnd() * 0.08;
    x2.fillRect(_r1Rnd() * 256, _r1Rnd() * 256, 1 + _r1Rnd() * 2, 1 + _r1Rnd() * 2);
  }
  x2.globalAlpha = 1;
  for(let i = 0; i < 7; i++){ x2.fillStyle = 'rgba(90,80,70,0.10)'; x2.fillRect(Math.floor(_r1Rnd() * 4) * 64, Math.floor(_r1Rnd() * 4) * 64, 64, 64); }
  x2.strokeStyle = 'rgba(70,64,58,0.55)'; x2.lineWidth = 2;
  for(let p = 0; p <= 256; p += 64){
    x2.beginPath(); x2.moveTo(p, 0); x2.lineTo(p, 256); x2.stroke();
    x2.beginPath(); x2.moveTo(0, p); x2.lineTo(256, p); x2.stroke();
  }
});
const TEX_GRASS = makeGroundTex(x2 => {
  x2.fillStyle = '#ffffff'; x2.fillRect(0, 0, 256, 256);
  for(let i = 0; i < 40; i++){
    x2.fillStyle = i % 2 ? 'rgba(100,110,80,0.12)' : 'rgba(70,80,55,0.12)';
    x2.beginPath(); x2.ellipse(_r1Rnd() * 256, _r1Rnd() * 256, 12 + _r1Rnd() * 30, 8 + _r1Rnd() * 20, _r1Rnd() * 3.14, 0, 6.29); x2.fill();
  }
  for(let i = 0; i < 1200; i++){
    x2.fillStyle = _r1Rnd() < 0.5 ? '#3a3a3a' : '#ffffff';
    x2.globalAlpha = 0.04 + _r1Rnd() * 0.08;
    x2.fillRect(_r1Rnd() * 256, _r1Rnd() * 256, 1 + _r1Rnd() * 2, 1 + _r1Rnd() * 2);
  }
  x2.globalAlpha = 1;
});
const TEX_GRIME = makeGroundTex(x2 => {
  x2.fillStyle = '#ffffff'; x2.fillRect(0, 0, 256, 256);
  for(let i = 0; i < 26; i++){
    x2.fillStyle = 'rgba(105,95,85,' + (0.05 + _r1Rnd() * 0.05).toFixed(3) + ')';
    x2.fillRect(_r1Rnd() * 256, 0, 3 + _r1Rnd() * 9, 90 + _r1Rnd() * 166);
  }
  for(let i = 0; i < 10; i++){
    x2.fillStyle = 'rgba(105,95,85,' + (0.06 + _r1Rnd() * 0.05).toFixed(3) + ')';
    x2.beginPath(); x2.ellipse(_r1Rnd() * 256, 226 + _r1Rnd() * 30, 10 + _r1Rnd() * 22, 5 + _r1Rnd() * 9, 0, 0, 6.29); x2.fill();
  }
});
window.__REAL1 = { texMeshes: 0, facadeTex: 0 };
"""
rep("""function mat(color, rough=0.9, metal=0.0){
  const k = color+'_'+rough+'_'+metal;
  if(!MAT[k]) MAT[k] = new THREE.MeshStandardMaterial({ color, roughness:rough, metalness:metal });
  return MAT[k];
}
const worldGroup""",
"""function mat(color, rough=0.9, metal=0.0){
  const k = color+'_'+rough+'_'+metal;
  if(!MAT[k]) MAT[k] = new THREE.MeshStandardMaterial({ color, roughness:rough, metalness:metal });
  return MAT[k];
}""" + REAL1_TEX + """const worldGroup""", tag='1a-tex-block')

# ================= PATCH 1a2: cache áo caro (cạnh cache sọc) =================
rep("const _npcStripeMats = {};",
    "const _npcStripeMats = {};\nconst _npcCheckMats = {}; // REALISM-1: cache material áo caro",
    tag='1a2-check-cache')

# ================= PATCH 1a2b: rampMat + road.material =================
rep("  const rampMat = new THREE.MeshStandardMaterial({ color:0x453f3a, roughness:0.35, metalness:0.08 });",
    "  const rampMat = new THREE.MeshStandardMaterial({ color:0x453f3a, map:TEX_ASPHALT, bumpMap:TEX_ASPHALT, bumpScale:0.02, roughness:0.62, metalness:0.08 }); // REALISM-1: nhựa có hạt/vá",
    tag='1a2-rampMat')
rep("  road.material = new THREE.MeshStandardMaterial({ color:0x4a4038, roughness:0.35, metalness:0.08 }); // khóa #4a4038",
    "  road.material = new THREE.MeshStandardMaterial({ color:0x4a4038, map:TEX_ASPHALT, bumpMap:TEX_ASPHALT, bumpScale:0.02, roughness:0.62, metalness:0.08 }); // khóa #4a4038 // REALISM-1: nhựa có hạt/vá",
    tag='1a2-roadMat')

# ================= PATCH 1a4: facade chợ =================
rep("  solid(-34, 20, 0.8, 8.4); solid(34, 20, 0.8, 8.4); solid(0, 27.8, 34, 0.8);",
    """  mk.traverse(o => { // REALISM-1 (a4): vệt bẩn facade nhà lồng chợ
    if(o.isMesh && o.material && !Array.isArray(o.material) && o.material.isMeshStandardMaterial && !o.material.map && o.material.color){
      const _hsl = {}; o.material.color.getHSL(_hsl);
      if(_hsl.l > 0.55){ o.material = o.material.clone(); o.material.map = TEX_GRIME; window.__REAL1.facadeTex++; }
    }
  });
  solid(-34, 20, 0.8, 8.4); solid(34, 20, 0.8, 8.4); solid(0, 27.8, 34, 0.8);""",
    tag='1a4-market-facade')

# ================= PATCH 1a4: facade khách sạn (trong placeHotel) =================
rep("    solid(x, z, hw, hd);",
    """    g.traverse(o => { // REALISM-1 (a4): vệt bẩn facade khách sạn
      if(o.isMesh && o.material && !Array.isArray(o.material) && o.material.isMeshStandardMaterial && !o.material.map && o.material.color){
        const _hsl = {}; o.material.color.getHSL(_hsl);
        if(_hsl.l > 0.55){ o.material = o.material.clone(); o.material.map = TEX_GRIME; window.__REAL1.facadeTex++; }
      }
    });
    solid(x, z, hw, hd);""",
    tag='1a4-hotel-facade')

# ================= PATCH 3: phụ kiện shophouse =================
rep("  solid(x, z, w / 2, 2.9);",
    """  { // REALISM-1: phụ kiện mặt tiền/nóc theo hash tất định từ (x,z)
    const _sv = Math.sin(x * 12.9898 + z * 78.233) * 43758.5453; const hf = _sv - Math.floor(_sv);
    if(hf < 0.55){ // máy lạnh mặt tiền (-z cục bộ, tường ở z=-2.8)
      box(0.78, 0.55, 0.28, 0xb9bcbe, w * 0.28, (floors > 2 ? 5.15 : 2.1), -2.96, g, false);
      box(0.6, 0.38, 0.04, 0x83878c, w * 0.28, (floors > 2 ? 5.15 : 2.1), -3.11, g, false);
    }
    if(hf >= 0.3 && hf < 0.82){ // bồn nước nóc + ăng-ten
      cyl(0.42, 0.42, 0.85, 0x3f4a52, -w * 0.3, hgt + 0.68, 0.8, g, 10);
      cyl(0.02, 0.02, 1.7, 0x777777, w * 0.32, hgt + 1.1, -0.6, g, 6);
      box(0.72, 0.035, 0.035, 0x777777, w * 0.32, hgt + 1.55, -0.6, g, false);
      box(0.5, 0.035, 0.035, 0x777777, w * 0.32, hgt + 1.3, -0.6, g, false);
    }
  }
  solid(x, z, w / 2, 2.9);""",
    tag='3-shophouse-props')

# ================= PATCH 7a: npcCheckShirt cạnh npcStripeShirt =================
CHECK_FN = r"""function npcCheckShirt(g, baseHex){ // REALISM-1: áo CARO cho khách (ô 16px trên canvas 64)
  if(!_npcCheckMats[baseHex]){
    const c = document.createElement('canvas'); c.width = 64; c.height = 64;
    const x2 = c.getContext('2d');
    x2.fillStyle = '#' + baseHex.toString(16).padStart(6, '0'); x2.fillRect(0, 0, 64, 64);
    x2.fillStyle = 'rgba(240,234,216,0.5)';
    for(let p = 0; p < 64; p += 16){ x2.fillRect(p, 0, 8, 64); x2.fillRect(0, p, 64, 8); }
    x2.fillStyle = 'rgba(30,26,22,0.35)';
    for(let p = 0; p < 64; p += 16){ x2.fillRect(p, 0, 2, 64); x2.fillRect(0, p, 64, 2); }
    const t = new THREE.CanvasTexture(c); t.wrapS = t.wrapT = THREE.RepeatWrapping; t.colorSpace = THREE.SRGBColorSpace;
    _npcCheckMats[baseHex] = new THREE.MeshStandardMaterial({ map:t, roughness:0.95 });
  }
  for(const nm of ['Torso', 'tmpCollar']){ const n = g.getObjectByName(nm); if(n) n.material = _npcCheckMats[baseHex]; }
}
function npcStripeShirt(g, baseHex){"""
rep("function npcStripeShirt(g, baseHex){", CHECK_FN, tag='7a-check-shirt')

# ================= PATCH 7b+7c: đầu applyLook =================
rep("function applyLook(g, look, role){",
    """function applyLook(g, look, role){
  if(role !== 'vendor'){ // REALISM-1: họa tiết áo cho khách — sọc 30% / caro 14% (vendor giữ sọc riêng ở thân hàm)
    const r = Math.random();
    if(r < 0.30) npcStripeShirt(g, look.shirt); else if(r < 0.44) npcCheckShirt(g, look.shirt);
  }
  { // REALISM-1: đa dạng màu tóc qua material 'HairDark' (recolor theo TÊN material)
    const r2 = Math.random();
    if(r2 < 0.26) recolor(g, 'HairDark', 0x241c16); else if(r2 < 0.40) recolor(g, 'HairDark', 0x4a3220);
    else if(r2 < 0.50) recolor(g, 'HairDark', 0x6e5136); else if(r2 < 0.56) recolor(g, 'HairDark', 0x8a8a86);
  }""",
    tag='7bc-applyLook-head')

# ================= PATCH 6: xe máy đậu cụm (sau gm1/gm2) =================
rep("  const gm2 = makeMoto(0x2e4a6e, false).g; gm2.position.set(-17.6, 0, 9.8); gm2.rotation.y = 0.45;",
    """  const gm2 = makeMoto(0x2e4a6e, false).g; gm2.position.set(-17.6, 0, 9.8); gm2.rotation.y = 0.45;
  { // REALISM-1: xe máy đậu cụm hai vệ đường vào (nam z 24.6 / bắc z -14.6) — ngoài làn traffic
    const _parkCols = [0x8c2f26, 0x2e4a6e, 0x3a3a3c, 0xd8d4c4];
    const _parkHash = v => { const sv = Math.sin(v * 12.9898) * 43758.5453; return sv - Math.floor(sv); };
    [-118, -110, -96, -88, -74, -66].forEach((px, i) => {
      const pz = 24.6 + (_parkHash(px) - 0.5) * 0.6;
      const pm = makeMoto(_parkCols[i % 4], false).g;
      pm.position.set(px, groundH(px, pz), pz);
      pm.rotation.y = Math.PI / 2 + (_parkHash(px + 7) - 0.5) * 0.3;
      pm.traverse(o => { if(o.isMesh) o.castShadow = false; });
    });
    [-96, -84, -70].forEach((px, i) => {
      const pz = -14.6 + (_parkHash(px) - 0.5) * 0.6;
      const pm = makeMoto(_parkCols[(i + 2) % 4], false).g;
      pm.position.set(px, groundH(px, pz), pz);
      pm.rotation.y = -Math.PI / 2 + (_parkHash(px + 7) - 0.5) * 0.4;
      pm.traverse(o => { if(o.isMesh) o.castShadow = false; });
    });
  }""",
    tag='6-parked-motos')

# ================= PATCH 5: rác chân sạp (vòng V5.3 STALL_DEFS) =================
rep("""  for(const def of STALL_DEFS){
    const h = def.id.split('').reduce((a, c) => a + c.charCodeAt(0), 0);
    const baseY = groundH(def.x, def.z);""",
    """  for(const def of STALL_DEFS){
    const h = def.id.split('').reduce((a, c) => a + c.charCodeAt(0), 0);
    const baseY = groundH(def.x, def.z);
    if(h % 3 === 0){ // REALISM-1: chồng ghế nhựa ở góc phải sạp (local 2.35, 0.55)
      const _chairCols = [0x2e6da4, 0xc8372d, 0x2e8b47];
      const [cwx, cwz] = stallLocalXZ(def, 2.35, 0.55);
      for(let ci = 0; ci < 4; ci++){
        const cm = box(0.44, 0.055, 0.44, _chairCols[ci % 3], cwx, baseY + 0.1 + ci * 0.11, cwz, worldGroup, false);
        cm.rotation.y = (def.rotY || 0) + ci * 0.12;
      }
      const [bwx, bwz] = stallLocalXZ(def, 2.35, 0.35);
      const bm = box(0.44, 0.4, 0.05, _chairCols[3 % 3], bwx, baseY + 0.62, bwz, worldGroup, false);
      bm.rotation.y = (def.rotY || 0);
    }
    if(h % 4 === 1){ // REALISM-1: thùng xốp + nắp + sọt ở lưng sạp (local -1.95/-1.3, -0.85)
      const [fwx, fwz] = stallLocalXZ(def, -1.95, -0.85);
      const fm = box(0.58, 0.36, 0.42, 0xe9e7e0, fwx, baseY + 0.18, fwz, worldGroup, false); fm.rotation.y = (def.rotY || 0);
      const lm = box(0.62, 0.06, 0.46, 0xdfdcd2, fwx, baseY + 0.39, fwz, worldGroup, false); lm.rotation.y = (def.rotY || 0);
      const [swx, swz] = stallLocalXZ(def, -1.3, -0.85);
      const sm = box(0.46, 0.38, 0.46, 0xd97a30, swx, baseY + 0.19, swz, worldGroup, false); sm.rotation.y = (def.rotY || 0);
    }""",
    tag='5-stall-clutter')

# ================= PATCH 1a3: hậu xử lý mặt đất ngay trước applyDayNight =================
GROUND_POST = r"""// ================= REALISM-1 (a3): HẬU XỬ LÝ TEXTURE MẶT ĐẤT =================
// Chỉ thay material/geometry TRÊN mesh mặt đất có màu thuộc bảng — KHÔNG sửa MAT cache dùng chung.
{
  const _r1Map = { 0x978a78: TEX_TILE, 0x84796a: TEX_TILE, 0x5f8547: TEX_GRASS, 0x9e9078: TEX_GRASS };
  const _r1Mats = {};
  const _r1Targets = [];
  worldGroup.traverse(o => {
    if(o.isMesh && o.material && !Array.isArray(o.material) && o.material.color && _r1Map[o.material.color.getHex()])
      _r1Targets.push([o, o.material.color.getHex()]);
  });
  for(const [o, hx] of _r1Targets){
    const geo = o.geometry; if(!geo || !geo.attributes || !geo.attributes.uv || !geo.parameters) continue;
    let sx, sy;
    if(geo.type === 'PlaneGeometry'){ sx = geo.parameters.width; sy = geo.parameters.height; }
    else if(geo.type === 'BoxGeometry'){ sx = geo.parameters.width; sy = geo.parameters.depth; }
    else continue;
    const ng = geo.clone();
    const uv = ng.attributes.uv;
    for(let i = 0; i < uv.count; i++) uv.setXY(i, uv.getX(i) * sx / 3.2, uv.getY(i) * sy / 3.2);
    uv.needsUpdate = true;
    if(!_r1Mats[hx]) _r1Mats[hx] = new THREE.MeshStandardMaterial({ color:hx, map:_r1Map[hx], bumpMap:_r1Map[hx], bumpScale:0.02, roughness:0.95 });
    o.geometry = ng; o.material = _r1Mats[hx];
    window.__REAL1.texMeshes++;
  }
}
function applyDayNight(){"""
rep("function applyDayNight(){", GROUND_POST, tag='1a3-ground-post')

# ================= PATCH 2: cửa sổ đêm ngẫu nhiên =================
rep("    for(const w of winMats) w.emissiveIntensity = 1.9;",
    """    const _rfTab = [0.65, 0, 0.3, 1, 0.45, 0, 0.85, 0.2]; // REALISM-1: cửa sổ đêm sáng/tắt ngẫu nhiên tất định theo chỉ số
    for(let wi = 0; wi < winMats.length; wi++){ const w = winMats[wi]; if(w.userData.rf === undefined) w.userData.rf = _rfTab[wi % 8]; w.emissiveIntensity = 1.9 * w.userData.rf; }""",
    tag='2-night-windows')

# ================= PATCH 4: dây điện NGANG qua đường (sau khối 18A nối dài) =================
rep("""    }
  }
  // ---------- 18B: sau 22:00""",
    """    }
  }
  // ---------- REALISM-1: dây điện NGANG qua đường (2 cột nam mới + nhịp tại x -101/-61) ----------
  {
    for(const cx of [-101, -61]){
      const gy = groundH(cx, 25.8);
      cyl(0.09, 0.12, 7.6, 0x4a4640, cx, gy + 3.8, 25.8, worldGroup, 8); // cột nam như cột bắc, KHÔNG solid()
      box(1.7, 0.09, 0.09, 0x4a4640, cx, gy + 7.05, 25.8, worldGroup, false);
      for(const off of [-0.55, 0.55]){
        const yN = entryRampY(cx) + 7.05, yS = gy + 7.05;
        const curve = new THREE.QuadraticBezierCurve3(
          new THREE.Vector3(cx + off, yN, -8.6),
          new THREE.Vector3(cx + off, Math.min(yN, yS) - 1.1, (-8.6 + 25.8) / 2),
          new THREE.Vector3(cx + off, yS, 25.8));
        worldGroup.add(new THREE.Mesh(new THREE.TubeGeometry(curve, 20, 0.025, 5), mat(0x1c1a18)));
      }
    }
  }
  // ---------- 18B: sau 22:00""",
    tag='4-cross-wires')

open(P, 'w', encoding='utf-8').write(s)
print('PATCH REAL1 DONE, bytes =', len(s.encode('utf-8')))
