# -*- coding: utf-8 -*-
"""BLENDER-DEEP-2 patch A: hình học mục 1-5 + đài phun (mục 4/7 nền). Chạy 1 lần, assert từng thay."""
import re, sys
P = '/home/hatch/workspace/cho-hoa-binh-3d/prototype-v2/index.html'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    assert c == n, f'[{tag}] tim thay {c} (can {n}): {old[:80]!r}'
    s = s.replace(old, new)
    print('OK', tag)

# ---------- MUC 1: groundH ----------
rep('z >= -16.5 && z <= -2) return x < -52 ? entryRampY(x) + 0.11 : 0;',
    'z >= -21.5 && z <= -2) return x < -52 ? entryRampY(x) + 0.11 : 0; // BLENDER-DEEP-2: them bac noi toi -21.5 cho hang sap bac moi -19.7', tag='gh-shelfN')
rep('if(x >= -131 && x <= -59 && z >= -13.9 && z <= -11.1) return entryRampY(x) + 0.11;',
    'if(x >= -208 && x <= -59 && z >= -18.4 && z <= -15.6) return entryRampY(x) + 0.11; // BLENDER-DEEP-2: via he bac theo line moi z -17.0, dai toi bung binh dau cho', tag='gh-swN')
rep('if(x >= -208 && x < -58 && z >= -21 && z <= 30){ const r = entryRampY(x); return (z < -16 || (z > 16.5 && z <= 24)) ? r + 0.11 : r; }',
    'if(x >= -208 && x < -58 && z >= -25 && z <= 34){ const r = entryRampY(x); return (z < -18 || (z > 25.5 && z <= 32)) ? r + 0.11 : r; } // BLENDER-DEEP-2: hanh lang theo hang sap moi (bac -19.7 / nam 30)', tag='gh-corridor')
rep('if(x >= -208 && x < -52 && z > 24) return entryRampY(x);',
    'if(x >= -208 && x < -52 && z > 32) return entryRampY(x); // BLENDER-DEEP-2: nen day nha nam moi z 35.5', tag='gh-foundS')
rep('if(x >= -84 && x <= -34 && z > 13.5 && z <= 25.5) return entryRampY(x) + 0.05;',
    'if(x >= -84 && x <= -34 && z > 13.5 && z <= 33.5) return entryRampY(x) + 0.05; // BLENDER-DEEP-2: them sap nam toi sap z 30', tag='gh-shelfS')
rep('if(x < -52 && z >= -21 && z <= 30) return entryRampY(x);',
    'if(x < -52 && z >= -25 && z <= 34) return entryRampY(x); // BLENDER-DEEP-2: mat duong mo rong theo nhua 49u', tag='gh-catch')

# ---------- MUC 1: STALL_DEFS ----------
for sid, old, new in [('banhtrang','z:26','z:30'), ('banhuot','z:26','z:30'), ('suatuoi','z:26','z:30'), ('banhflan','z:26','z:30'),
                      ('dauhu','z:-15.7','z:-19.7'), ('banhmi','z:-15.7','z:-19.7'), ('hutieu','z:-15.7','z:-19.7'),
                      ('traicay','z:-15.7','z:-19.7'), ('chao','z:-15.7','z:-19.7'), ('haisan','z:-15.7','z:-19.7')]:
    pat = re.compile(r"(id:'" + sid + r"'[^}]*?)z:" + re.escape(old.replace('z:', '')))
    s2, cnt = pat.subn(lambda m: m.group(1) + 'z:' + new.replace('z:', ''), s, count=1)
    assert cnt == 1, f'stall {sid}: {cnt}'
    s = s2
    print('OK stall', sid, '->', new)

# ---------- MUC 1: decor ----------
rep('DECOR_N_XS.forEach((x, i) => buildDecorStall(x, -15.7, 0, i));',
    'DECOR_N_XS.forEach((x, i) => buildDecorStall(x, -19.7, 0, i)); // BLENDER-DEEP-2: hang bac lui -19.7', tag='decorN')
rep('DECOR_S_XS.forEach((x, i) => buildDecorStall(x, 26, Math.PI, i + 5));',
    'DECOR_S_XS.forEach((x, i) => buildDecorStall(x, 30, Math.PI, i + 5)); // BLENDER-DEEP-2: hang nam lui 30', tag='decorS')

# ---------- MUC 1: mat nhua ----------
rep('new THREE.BoxGeometry(82, 0.07, 41), rampMat); // GEOMETRY-2: nhua RONG x -134..-52, sau z -13.5..27.5 (mat sap bac -13.6 / nam 23.9)',
    'new THREE.BoxGeometry(82, 0.07, 49), rampMat); // BLENDER-DEEP-2: nhua RONG 49u z -17.5..31.5 (mat sap bac -17.6 / nam 27.9)', tag='seg')
rep('new THREE.BoxGeometry(22, 0.05, 45), rampMat); // GEOMETRY-2: doan phang x -52..-30, sau z -17.5..27.5',
    'new THREE.BoxGeometry(22, 0.05, 49), rampMat); // BLENDER-DEEP-2: doan phang x -52..-30, rong 49u nhu toan truc', tag='seg2')
rep('seg2.position.set(-41, 0.0, 5);', 'seg2.position.set(-41, 0.0, 7); // BLENDER-DEEP-2: tam z 7 khop nhua 49u', tag='seg2pos')
rep('new THREE.BoxGeometry(76, 0.07, 41), rampMat); // GEOMETRY-2: doan PHANG keo dai x -206..-130 toi bung binh dau cho (entryRampY da cham nap 5.5)',
    'new THREE.BoxGeometry(76, 0.07, 49), rampMat); // BLENDER-DEEP-2: doan keo dai rong 49u nhu toan truc', tag='seg3')

# ---------- MUC 1: le dat + via he + them ----------
rep('const _sh = box(82, 0.06, 9, 0x978a78, -93, entryRampY(-93) + 0.03, -16.5, worldGroup, false);',
    'const _sh = box(82, 0.06, 13, 0x978a78, -93, entryRampY(-93) + 0.03, -18.5, worldGroup, false); // BLENDER-DEEP-2: le bac sau toi -25..-12', tag='sh1')
rep('box(76, 0.06, 9, 0x978a78, -168, 5.53, -16.5, worldGroup, false);',
    'box(76, 0.06, 13, 0x978a78, -168, 5.53, -18.5, worldGroup, false); // BLENDER-DEEP-2: le bac doan keo dai', tag='sh2')
rep('const swS = box(79, 0.1, 2.7, 0x84796a, -91.5, entryRampY(-91.5) + 0.06, 22.9);',
    'const swS = box(79, 0.1, 2.7, 0x84796a, -91.5, entryRampY(-91.5) + 0.06, 26.4); // BLENDER-DEEP-2: via he nam truoc mat sap 27.9', tag='swS')
rep('box(17, 0.1, 2.7, 0x84796a, -43.5, 0.0, 22.9, worldGroup, false);',
    'box(17, 0.1, 2.7, 0x84796a, -43.5, 0.0, 26.4, worldGroup, false); // BLENDER-DEEP-2', tag='swS2')
rep('box(76, 0.1, 2.7, 0x84796a, -168, 5.56, 22.9, worldGroup, false);',
    'box(76, 0.1, 2.7, 0x84796a, -168, 5.56, 26.4, worldGroup, false); // BLENDER-DEEP-2', tag='swS3')
rep('box(76, 0.1, 2.8, 0x84796a, -168, 5.56, -12.5, worldGroup, false);',
    'box(76, 0.1, 2.8, 0x84796a, -168, 5.56, -17.0, worldGroup, false); // BLENDER-DEEP-2: via he bac doan keo dai z -17.0', tag='swN3')
rep('const swN = box(72, 0.1, 2.8, 0x84796a, -95, entryRampY(-95) + 0.06, -12.5);',
    'const swN = box(72, 0.1, 2.8, 0x84796a, -95, entryRampY(-95) + 0.06, -17.0); // BLENDER-DEEP-2: via he bac z -17.0', tag='swN')
rep('const shelfW = box(8, 0.1, 17, 0x978a78, -54, entryRampY(-54) + 0.06, -10.25);',
    'const shelfW = box(8, 0.1, 22, 0x978a78, -54, entryRampY(-54) + 0.06, -12.25); // BLENDER-DEEP-2: them bac sau toi -23.25', tag='shelfW')
rep('box(15, 0.1, 17, 0x978a78, -42.5, 0.0, -10.25, worldGroup, false);',
    'box(15, 0.1, 22, 0x978a78, -42.5, 0.0, -12.25, worldGroup, false); // BLENDER-DEEP-2', tag='shelfW2')
rep('const shelfS = box(31, 0.1, 15, 0x978a78, -67, entryRampY(-67) + 0.06, 21);',
    'const shelfS = box(31, 0.1, 20, 0x978a78, -67, entryRampY(-67) + 0.06, 23.5); // BLENDER-DEEP-2: them nam toi 33.5', tag='shelfS')
rep('box(24, 0.1, 15, 0x978a78, -46, 0.0, 21, worldGroup, false);',
    'box(24, 0.1, 20, 0x978a78, -46, 0.0, 23.5, worldGroup, false); // BLENDER-DEEP-2', tag='shelfS2')

# ---------- MUC 1: day nha lui ----------
s2, cnt = re.subn(r'(shophouse\(-[\d.]+, )30\.5', r'\g<1>35.5', s)
assert cnt == 7, f'nha nam: {cnt}'
s = s2; print('OK nha nam 30.5->35.5 x7')
for x, z in [('-62', '-24'), ('-52', '-24.5'), ('-42', '-23'), ('-80', '-24'), ('-96', '-24.5'), ('-112', '-25'), ('-126', '-25')]:
    rep(f'shophouse({x}, {z},', f'shophouse({x}, -28.5,', tag=f'nha bac {x}')

# ---------- MUC 1: den duong theo via moi (chi khoi den truc vao) ----------
i0 = s.index('colonialLamp(-74, -12.5, true)')
i1 = s.index('colonialLamp(-33.5, -13.5, false)')
blk = s[i0:i1].replace('-12.5', '-17.0').replace('22.9', '26.4')
s = s[:i0] + blk + s[i1:]
print('OK lamps entry -> -17.0 / 26.4')

# ---------- MUC 2: brandShop ----------
BRAND = r'''
function brandShop(x, z, rotY, kind){ // BLENDER-DEEP-2 (mục 2): 2 thương hiệu dựng THẬT bằng code geometry + biển canvas — thay shophouse gợi mốc của GEOMETRY-2. Mặt tiền = local -z.
  const y = groundH(x, z);
  const g = new THREE.Group(); g.position.set(x, y, z); g.rotation.y = rotY; worldGroup.add(g);
  const J = kind === 'jollibee';
  const wall = J ? 0xc23527 : 0xefe3c2, trim = J ? 0xffc72c : 0x3f7a44;
  box(9.6, 6.4, 6.0, wall, 0, 3.2, 0, g);                        // khối chính 2 tầng
  box(10.2, 0.3, 6.8, J ? 0x8f1d12 : 0x8a4a38, 0, 6.55, 0, g);   // viền mái
  box(9.8, 0.45, 6.2, trim, 0, 3.18, 0, g, false);               // dải màu ngang (vàng Jollibee / xanh L'angfarm)
  box(7.6, 2.2, 0.12, 0x2e3438, 0, 1.35, -3.02, g, false);       // kính mặt tiền
  box(1.5, 2.2, 0.16, J ? 0x7a1408 : 0x33502e, 2.2, 1.35, -3.04, g, false); // cửa vào
  for(const wx of [-2.6, 0, 2.6]) box(1.7, 1.05, 0.1, 0x3a3f45, wx, 4.35, -3.02, g, false); // cửa sổ tầng 2
  if(J){ for(let i = 0; i < 6; i++){ const aw = box(1.55, 0.09, 1.9, i % 2 ? 0xf5f0e6 : 0xc8102e, -3.9 + i * 1.56, 2.82, -3.8, g, false); aw.rotation.x = 0.3; } } // hiên sọc đỏ/trắng
  else { const aw = box(9.4, 0.09, 1.9, 0x3f7a44, 0, 2.82, -3.8, g, false); aw.rotation.x = 0.3; } // hiên xanh lá
  const main = signMesh(J ? 'JOLLIBEE' : "L'ANGFARM", 8.4, 1.15, J ? '#c8102e' : '#2e5b2e', '#ffffff',
    J ? 'GÀ RÁN GIÒN • KHOAI TÂY CHIÊN' : 'ĐẶC SẢN ĐÀ LẠT • TRÀ • MỨT • HOA KHÔ');
  main.position.set(0, 5.72, -3.3); main.rotation.y = Math.PI; g.add(main);
  if(J){
    cyl(0.30, 0.36, 0.78, 0xc8102e, 4.35, 7.3, -2.0, g, 10);      // mascot ONG trên mái: thân đỏ
    ball(0.25, 0xffc72c, 4.35, 7.85, -2.0, g, 0.95);              // đầu ong vàng
    box(0.5, 0.06, 0.3, 0xf5f0e6, 4.0, 7.62, -2.25, g, false);    // cánh ong
    box(0.5, 0.06, 0.3, 0xf5f0e6, 4.7, 7.62, -2.25, g, false);
    const mb = signMesh('COMBO GÀ GIÒN 39K', 1.7, 1.05, '#ffffff', '#c8102e', 'MÌ Ý • BURGER • KEM');
    mb.position.set(-3.6, 1.5, -4.4); mb.rotation.y = Math.PI; g.add(mb);
    box(0.07, 1.5, 0.07, 0x555049, -3.6, 0.75, -4.4, g, false);
    for(const tx of [-1.2, 2.4]){                                  // bàn ngoài trời trước quán
      cyl(0.42, 0.42, 0.05, 0xf5f0e6, tx, 0.72, -4.9, g, 12);
      cyl(0.05, 0.05, 0.7, 0x555049, tx, 0.36, -4.9, g, 8);
      cyl(0.19, 0.19, 0.42, 0xc8102e, tx - 0.62, 0.21, -4.9, g, 10);
      cyl(0.19, 0.19, 0.42, 0xffc72c, tx + 0.62, 0.21, -4.9, g, 10);
    }
  } else {
    box(6.6, 0.09, 0.85, 0x74522f, 0, 1.02, -3.55, g, false);      // kệ gỗ trưng bày trước cửa
    box(6.6, 0.09, 0.85, 0x74522f, 0, 1.62, -3.55, g, false);
    const jarCols = [0xd8542e, 0xe8c33c, 0x9a4a7a, 0x3f7a44, 0xe07b2a, 0xb03a30];
    for(let i = 0; i < 6; i++){ cyl(0.15, 0.15, 0.36, jarCols[i], -2.75 + i * 1.1, 1.25, -3.55, g, 8); cyl(0.16, 0.16, 0.05, 0x8a6a42, -2.75 + i * 1.1, 1.45, -3.55, g, 8); } // lọ mứt đủ màu + nắp
    for(let i = 0; i < 5; i++) box(0.52, 0.4, 0.5, i % 2 ? 0xefe3c2 : 0x3f7a44, -2.4 + i * 1.2, 1.86, -3.55, g, false); // hộp trà/quà tầng trên
    const sub2 = signMesh("L'ANGFARM STORE", 3.2, 0.62, '#efe3c2', '#2e5b2e');
    sub2.position.set(3.1, 2.6, -3.3); sub2.rotation.y = Math.PI; g.add(sub2);
    hydrangeaBasket(g, -4.35, 0.2, -3.9); hydrangeaBasket(g, 4.35, 0.2, -3.9); // giỏ hoa 2 góc cửa
  }
  solid(x, z, 4.9, 3.1);
  return g;
}
'''
anchor = "{ // GEOMETRY-2: BÙNG BINH ĐẦU CHỢ"
assert anchor in s
s = s.replace(anchor, BRAND + anchor, 1)
print('OK brandShop def')
rep("  shophouse(-183, -20, 8, 2, 0xc8372d, 'JOLLIBEE — GÀ RÁN', '#c8102e', 0xffc72c, Math.PI);\n  shophouse(-183, 31.5, 8.5, 2, 0xe8dcc4, \"L'ANGFARM — ĐẶC SẢN ĐÀ LẠT\", '#33502e', 0x68804f);",
    "  brandShop(-183, -20, Math.PI, 'jollibee'); // BLENDER-DEEP-2: dựng THẬT (research/23 — nhận diện đỏ/vàng + ong)\n  brandShop(-183, 31.5, 0, 'langfarm'); // BLENDER-DEEP-2: dựng THẬT (research/23 — 6 Nguyễn Thị Minh Khai: kính + kệ đặc sản)", tag='brand calls')

# ---------- MUC 5: danh tinh Da Lat (chen sau bien Tang Bat Ho) ----------
IDENT = '''
  // BLENDER-DEEP-2 (mục 5): danh tính Đà Lạt dọc trục — biển tên đường + thông + chậu hoa góc vỉa
  function streetSign(txt, x, z, ry){
    const y = groundH(x, z);
    box(0.09, 2.9, 0.09, 0x3a4a3a, x, y + 1.45, z, worldGroup, false);
    const sgn = signMesh(txt, 3.6, 0.62, '#1f4d2e', '#eaf5d8');
    sgn.position.set(x, y + 2.75, z); sgn.rotation.y = ry; worldGroup.add(sgn);
    solid(x, z, 0.25, 0.25);
  }
  streetSign('Đ. NGUYỄN THỊ MINH KHAI', -160, -17.6, 0);
  streetSign('Đ. NGUYỄN THỊ MINH KHAI', -70, 27.4, Math.PI);
  streetSign('Đ. TĂNG BẠT HỔ', -176, 27.4, Math.PI);
  pine(-150, -23.5, 1.25); pine(-120, -24, 1.4); pine(-90, -23.5, 1.15); pine(-70, -24.5, 1.3);
  pine(-150, 36, 1.2); pine(-105, 36.5, 1.35);
  hydrangea(-138, -18.6, 0.9); hydrangea(-104, -18.6, 0.9); hydrangea(-146, 27.6, 0.9); hydrangea(-110, 27.6, 0.9);'''
rep("  box(0.09, 2.9, 0.09, 0x5a4632, -130.6, gy + 1.45, 16.9, worldGroup, false);",
    "  box(0.09, 2.9, 0.09, 0x5a4632, -130.6, gy + 1.45, 16.9, worldGroup, false);" + IDENT, tag='identity')

# ---------- MUC 4 + 7-nen: dai phun cao hon + dang ky WATER_FX ----------
rep("{ // ================= V5.5: ĐÀI PHUN NƯỚC + KHU QUẦN ÁO + BÀN GHẾ HOA SỮA =================",
    "const WATER_FX = { surfs: [], jets: [], rings: [] }; // BLENDER-DEEP-2 (mục 7): đăng ký mặt nước + tia để animate gợn/chảy nhẹ trong tickWater\n"
    "function tickWater(t){\n"
    "  for(const sf of WATER_FX.surfs){ sf.m.position.y = sf.y + Math.sin(t * 1.7) * 0.02; sf.m.material.opacity = 0.84 + Math.sin(t * 2.3) * 0.06; }\n"
    "  for(const rg of WATER_FX.rings){ const f = (t * 0.32 + rg.ph) % 1; const sc = 0.7 + f * 1.7; rg.m.scale.set(sc, sc, 1); rg.m.material.opacity = 0.38 * (1 - f); }\n"
    "  for(const jt of WATER_FX.jets){ const pu = 1 + Math.sin(t * 5.2 + jt.userData.ph) * 0.07; jt.scale.set(1, pu, 1); jt.material.opacity = 0.5 + Math.sin(t * 5.2 + jt.userData.ph) * 0.08; }\n"
    "}\n"
    "{ // ================= V5.5: ĐÀI PHUN NƯỚC + KHU QUẦN ÁO + BÀN GHẾ HOA SỮA =================", tag='waterfx def')
rep("  fwater.rotation.x = -Math.PI/2; fwater.position.set(FNT.x, 0.5, FNT.z); worldGroup.add(fwater);",
    "  fwater.rotation.x = -Math.PI/2; fwater.position.set(FNT.x, 0.5, FNT.z); worldGroup.add(fwater);\n"
    "  WATER_FX.surfs.push({ m: fwater, y: 0.5 }); // BLENDER-DEEP-2 (mục 7): mặt bồn gợn nhẹ\n"
    "  for(let ri = 0; ri < 2; ri++){\n"
    "    const ring = new THREE.Mesh(new THREE.RingGeometry(0.5 + ri * 0.8, 0.62 + ri * 0.8, 24), new THREE.MeshBasicMaterial({ color:0xeaf6fc, transparent:true, opacity:0.35, depthWrite:false }));\n"
    "    ring.rotation.x = -Math.PI/2; ring.position.set(FNT.x, 0.53 + ri * 0.012, FNT.z); worldGroup.add(ring);\n"
    "    WATER_FX.rings.push({ m: ring, ph: ri * 0.5 });\n"
    "  }", tag='water surf')
rep("cyl(0.28, 0.42, 1.5, 0x8a8074, FNT.x, 1.05, FNT.z, worldGroup, 10); // cột giữa",
    "cyl(0.26, 0.44, 2.3, 0x8a8074, FNT.x, 1.42, FNT.z, worldGroup, 10); // BLENDER-DEEP-2 (mục 4): cột giữa CAO 1.5 -> 2.3 — đài phun bớt bẹt", tag='fnt col')
rep("cyl(0.85, 0.5, 0.25, 0x8a8074, FNT.x, 1.85, FNT.z, worldGroup, 12); // bát trên",
    "cyl(0.95, 0.52, 0.25, 0x8a8074, FNT.x, 2.62, FNT.z, worldGroup, 12); // BLENDER-DEEP-2 (mục 4): bát chính theo cột mới\n"
    "  cyl(0.5, 0.3, 0.18, 0x8a8074, FNT.x, 3.12, FNT.z, worldGroup, 10); // BLENDER-DEEP-2: bát tầng 2\n"
    "  ball(0.16, 0x8a8074, FNT.x, 3.34, FNT.z, worldGroup, 0.9); // BLENDER-DEEP-2: chóp cầu", tag='fnt bowl')
rep("  const fup = new THREE.MeshStandardMaterial({ color:0x3a3f45, emissive:0xffc98a, emissiveIntensity:0, roughness:0.5 });",
    "  const cjet = new THREE.Mesh(new THREE.CylinderGeometry(0.035, 0.05, 1.1, 6), jetMat.clone());\n"
    "  cjet.position.set(FNT.x, 3.85, FNT.z); cjet.userData.ph = 0.5; worldGroup.add(cjet); WATER_FX.jets.push(cjet); // BLENDER-DEEP-2: tia đứng giữa từ bát tầng 2\n"
    "  const fup = new THREE.MeshStandardMaterial({ color:0x3a3f45, emissive:0xffc98a, emissiveIntensity:0, roughness:0.5 });", tag='cjet')
rep("const jet = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 1.15, 5), jetMat);",
    "const jet = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 1.5, 5), jetMat.clone()); // BLENDER-DEEP-2: tia dài 1.15 -> 1.5 + material riêng để nhấp nhô", tag='jet len')
rep("jet.position.set(FNT.x + Math.cos(a) * 0.42, 2.2, FNT.z + Math.sin(a) * 0.42);",
    "jet.position.set(FNT.x + Math.cos(a) * 0.5, 2.95, FNT.z + Math.sin(a) * 0.5); jet.userData.ph = i * 1.05; WATER_FX.jets.push(jet); // BLENDER-DEEP-2: tia từ bát mới (đầu tia r ~0.92 < bồn 2.45)", tag='jet pos')

# ---------- MUC 3: dem dao <-> bac ----------
rep("box(58, 0.08, 13, 0x978a78, 9, 0.01, 3, worldGroup, false); // GEOMETRY-2: tấm sân quảng trường dưới bậc — nới từ x -20 tới 38 (bản cũ chỉ quanh đài phun x 12..36)",
    "box(58, 0.08, 13, 0xa79a84, 9, 0.01, 3, worldGroup, false); // BLENDER-DEEP-2 (mục 3): tấm sân sáng hơn — tách tông khỏi thềm/đường (GEOMETRY-2: nới x -20..38)\n"
    "  box(0.7, 0.1, 13, 0x6e6257, -19.6, 0.02, 3, worldGroup, false); // BLENDER-DEEP-2: dải viền sẫm mép tây sân\n"
    "  for(const hz of [0.5, 3.5, 6.5, 9.5]) hydrangea(-13.2, hz, 0.9); // BLENDER-DEEP-2: dải chậu hoa phân cách vành đảo <-> sân bậc (dải đất y0 duy nhất: z -2..10)\n"
    "  for(const zx of [-16.8, -15.6, -14.4, -13.2]) box(0.55, 0.03, 2.6, 0xe8e4da, zx, 0.07, 1.0, worldGroup, false); // BLENDER-DEEP-2: zebra qua vành đường đảo về bậc\n"
    "  const bsign = signMesh('BẬC TAM CẤP →', 2.2, 0.55, '#7a1f1a', '#ffd98a');\n"
    "  bsign.position.set(-12.8, 2.5, 8.6); bsign.rotation.y = Math.PI / 2; worldGroup.add(bsign);\n"
    "  box(0.08, 2.5, 0.08, 0x4a3b2c, -12.8, 1.25, 8.6, worldGroup, false);", tag='buffer')

# ---------- MUC 7: goi tickWater trong animate ----------
rep("  tickAmbience(t); // SOUND-COLOR-1: ambience theo khu (throttle 0,3s trong hàm)",
    "  tickAmbience(t); // SOUND-COLOR-1: ambience theo khu (throttle 0,3s trong hàm)\n  tickWater(t); // BLENDER-DEEP-2 (mục 7): nước gợn/chảy nhẹ", tag='tickwater call')

open(P, 'w', encoding='utf-8').write(s)
print('PATCH A DONE, bytes =', len(s.encode('utf-8')))
