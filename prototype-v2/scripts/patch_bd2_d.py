#!/usr/bin/env python3
# BLENDER-DEEP-2 mục 12-14: hàng hóa toàn chợ theo hàng thật (research/24) +
# khu phải bậc tam cấp (tiem lon DAC SAN - LUU NIEM vao duoc ben trong) +
# quan ao nhin thay ro. Chay 1 lan, assert tung diem neo.
import re, sys
P = 'index.html'
s = open(P, encoding='utf-8').read()
orig = len(s.encode('utf-8'))

def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    assert c == n, f'{tag}: tim thay {c} (can {n}) :: {old[:70]!r}'
    s = s.replace(old, new)
    print('OK', tag)

# --- 1. Go 6 o decor o 2 hang duong vao, thay bang sap tuong tac that ---
rep("const DECOR_N_XS = [-188,-181.3,-174.6,-167.9,-161.2,-154.5,-147.8,-141.1,-121,-114.5,-108,-93,-80,-73.5,-67,-61.5];",
    "const DECOR_N_XS = [-188,-181.3,-174.6,-167.9,-161.2,-154.5,-147.8,-141.1,-121,-108,-73.5,-67,-61.5]; // BLENDER-DEEP-2 (muc 12): bo -114.5/-93/-80 — da thay bang sap tuong tac tra2/hong/dau2",
    tag='decor N')
rep("const DECOR_S_XS = [-188,-181.3,-174.6,-167.9,-161.2,-154.5,-147.8,-141.1,-113,-106.5,-88,-81.5,-75,-68.5,-62,-44];",
    "const DECOR_S_XS = [-188,-181.3,-174.6,-167.9,-161.2,-154.5,-147.8,-141.1,-113,-88,-75,-62,-44]; // BLENDER-DEEP-2 (muc 12): bo -106.5/-81.5/-68.5 — da thay bang sap tuong tac hoa2/dau3/mut",
    tag='decor S')

# --- 2. Sua ten sap aokhoac bi loi encoding (ky tu thay the U+FFFD tren bien) ---
m = re.search(r"ÁO KHOÁC [^']*?À LẠT", s)
assert m, 'khong tim thay ten aokhoac loi'
s = s.replace(m.group(0), 'ÁO KHOÁC ĐÀ LẠT')
print('OK aokhoac name fix:', m.group(0)[:20], '-> ÁO KHOÁC ĐÀ LẠT')

# --- 3. SPECIAL_VENDOR: chu tiem lon ---
rep("\n};\nfunction dressSpecialVendor",
    "\n  dacsanlon: { shirt:0x2e6b46, pants:0x3a3f4a, hat:'cap', hatColor:0xc8372d, skin:0xc68a5e, apron:0x8c2f39 }, // BLENDER-DEEP-2 (muc 13): chu tiem DAC SAN - LUU NIEM — tap de do do + mu do rieng\n};\nfunction dressSpecialVendor",
    tag='special vendor dacsanlon')

# --- 4. ANIM_BY_ID cho sap moi ---
rep("const ANIM_BY_ID = {",
    "const ANIM_BY_ID = { dacsanlon:'pack', mut:'pack', tra2:'pack', dau2:'weigh', dau3:'pack', dau4:'weigh', hong:'weigh', hoa2:'bouquet', luuniem2:'pack', dosi:'arrange', len3:'arrange', // BLENDER-DEEP-2 (muc 12-13)\n",
    tag='anim by id')

# --- 5. STALL_DEFS moi (chen truoc ]; sau sap aolen) ---
NEW_DEFS = """  { id:'dau2', name:'DÂU TÂY ĐÀ LẠT', district:P, x:-80, z:-19.7, rotY:0, special:true, shirt:0xc95d7e, menu:[
    { name:'Dâu tây tươi (hộp)', price:55, buff:'alert', sec:45, type:'goods', desc:'Dâu vườn hái sáng nay — đỏ mọng' },
    { name:'Dâu lắc muối tôm', price:25, buff:'alert', sec:40, type:'food', desc:'Chua cay mặn ngọt' },
    { name:'Nước ép dâu', price:20, buff:'alert', sec:40, type:'drink', desc:'Ép nguyên quả, không pha' } ] },
  { id:'dau3', name:'DÂU TÂY & MỨT DÂU', district:P, x:-81.5, z:30, rotY:Math.PI, shirt:0xc95d7e, menu:[
    { name:'Mứt dâu tây', price:45, buff:null, sec:0, type:'goods', desc:'Hũ mứt dâu nấu thủ công' },
    { name:'Dâu sấy dẻo', price:48, buff:null, sec:0, type:'goods', desc:'Sấy dẻo giữ vị chua ngọt' },
    { name:'Dâu tươi (hộp lớn)', price:75, buff:null, sec:0, type:'goods', desc:'Hộp lớn mang về làm quà' } ] },
  { id:'dau4', name:'DÂU TÂY TƯƠI', district:P, x:12, z:11.0, rotY:Math.PI, special:true, shirt:0xc95d7e, menu:[
    { name:'Dâu tây tươi (hộp)', price:55, buff:'alert', sec:45, type:'goods', desc:'Ngay mặt tiền chợ — hộp dâu đỏ xếp tháp' },
    { name:'Kem dâu tây', price:22, buff:'alert', sec:45, type:'food', desc:'Kem mát vị dâu thật' } ] },
  { id:'mut', name:'MỨT & TRÁI CÂY SẤY', district:S, x:-68.5, z:30, rotY:Math.PI, shirt:0x96683f, menu:[
    { name:'Mứt dâu', price:45, buff:null, sec:0, type:'goods', desc:'Mứt dâu tằm & dâu tây' },
    { name:'Mứt hồng', price:42, buff:null, sec:0, type:'goods', desc:'Hồng Đà Lạt nấu mứt' },
    { name:'Khoai lang sấy', price:35, buff:null, sec:0, type:'goods', desc:'Sấy giòn, ngọt tự nhiên' },
    { name:'Mận sấy & me sấy', price:38, buff:null, sec:0, type:'goods', desc:'Chua ngọt ăn vặt dọc đường' },
    { name:'Phúc bồn tử sấy', price:55, buff:null, sec:0, type:'goods', desc:'Đặc sản hiếm của cao nguyên' } ] },
  { id:'hong', name:'HỒNG TREO GIÓ & BƠ SÁP', district:P, x:-93, z:-19.7, rotY:0, shirt:0xd97c2e, menu:[
    { name:'Hồng treo gió', price:50, buff:null, sec:0, type:'goods', desc:'Treo gió dẻo ngọt kiểu Nhật' },
    { name:'Hồng giòn (1kg)', price:35, buff:null, sec:0, type:'goods', desc:'Giòn tan, ngọt thanh' },
    { name:'Bơ sáp 034 (1kg)', price:48, buff:null, sec:0, type:'goods', desc:'Bơ sáp dẻo béo trứ danh' } ] },
  { id:'tra2', name:'TRÀ ATISO & CÀ PHÊ', district:S, x:-114.5, z:-19.7, rotY:0, shirt:0x96683f, menu:[
    { name:'Trà atiso túi lọc', price:40, buff:null, sec:0, type:'goods', desc:'Atiso Đà Lạt phơi sấy' },
    { name:'Hoa atiso khô', price:55, buff:null, sec:0, type:'goods', desc:'Nấu nước mát gan' },
    { name:'Cà phê Cầu Đất', price:65, buff:null, sec:0, type:'goods', desc:'Arabica rang vừa' } ] },
  { id:'hoa2', name:'HOA TƯƠI CẨM TÚ CẦU', district:P, x:-106.5, z:30, rotY:Math.PI, shirt:0x8668c4, menu:[
    { name:'Bó cẩm tú cầu', price:40, buff:null, sec:0, type:'goods', desc:'Hoa cắt sáng nay ở vườn' },
    { name:'Bó hồng Đà Lạt', price:45, buff:null, sec:0, type:'goods', desc:'Hồng nhung đỏ thắm' },
    { name:'Bó hoa baby', price:30, buff:null, sec:0, type:'goods', desc:'Nhẹ nhàng tinh khôi' },
    { name:'Bó cúc họa mi', price:35, buff:null, sec:0, type:'goods', desc:'Trắng nhỏ xinh' } ] },
  { id:'luuniem2', name:'LƯU NIỆM ĐÀ LẠT', district:S, x:45, z:17.5, rotY:Math.PI/2, shirt:0x8668c4, menu:[
    { name:'Móc khóa Đà Lạt', price:15, buff:null, sec:0, type:'goods', desc:'Móc khóa nhà thờ con gà' },
    { name:'Tranh gỗ chợ đêm', price:60, buff:null, sec:0, type:'goods', desc:'Tranh gỗ khắc tay' },
    { name:'Búp bê len', price:45, buff:null, sec:0, type:'goods', desc:'Búp bê móc len thủ công' },
    { name:'Chuông gió tre', price:38, buff:null, sec:0, type:'goods', desc:'Kêu leng keng trong sương' } ] },
  { id:'dosi', name:'ĐỒ SI SECONDHAND', district:W, x:45, z:22.5, rotY:Math.PI/2, shirt:0x51624a, menu:[
    { name:'Áo khoác si', price:65, buff:null, sec:0, type:'goods', desc:'Hàng si tuyển — đúng chất chợ đêm' },
    { name:'Áo len si', price:45, buff:null, sec:0, type:'goods', desc:'Len ngoại nhập giá rẻ' },
    { name:'Quần jean si', price:55, buff:null, sec:0, type:'goods', desc:'Jean cũ form đẹp' },
    { name:'Khăn si', price:20, buff:null, sec:0, type:'goods', desc:'Khăn lạ độc bản' } ] },
  { id:'len3', name:'ĐỒ LEN GIÁ RẺ', district:W, x:40, z:27.5, rotY:-Math.PI/2, shirt:0x74566b, menu:[
    { name:'Áo len trơn', price:70, buff:null, sec:0, type:'goods', desc:'Len trơn đủ màu, giá rẻ' },
    { name:'Mũ len', price:35, buff:null, sec:0, type:'goods', desc:'Đội ấm đầu đêm sương' },
    { name:'Găng tay len', price:25, buff:null, sec:0, type:'goods', desc:'Ấm tay chạy xe' } ] },
  { id:'dacsanlon', name:'ĐẶC SẢN – LƯU NIỆM', district:S, x:51.5, z:20, rotY:-Math.PI/2, roof:'tin', special:true, shirt:0x2e6b46, menu:[
    { name:'Hộp quà đặc sản', price:90, buff:null, sec:0, type:'goods', desc:'Hộp quà tổng hợp của tiệm — mang về biếu' },
    { name:'Mứt tổng hợp', price:60, buff:null, sec:0, type:'goods', desc:'5 loại mứt trong 1 hộp' },
    { name:'Trà atiso (hộp lớn)', price:75, buff:null, sec:0, type:'goods', desc:'Hộp lớn pha cả tháng' },
    { name:'Búp bê len lớn', price:65, buff:null, sec:0, type:'goods', desc:'Búp bê len khổ lớn của tiệm' },
    { name:'Tranh gỗ lớn', price:85, buff:null, sec:0, type:'goods', desc:'Tranh gỗ chợ Đà Lạt khổ lớn' } ] },
"""
rep("desc:'Quàng là ấm cổ' } ] },\n];",
    "desc:'Quàng là ấm cổ' } ] },\n" + NEW_DEFS + "];",
    tag='stall defs moi x11')

# --- 6. So dac san: cong sap moi ---
rep("const DACSAN_GOODS_STALLS = ['rau','dau','hoa','dacsan','tra'];",
    "const DACSAN_GOODS_STALLS = ['rau','dau','hoa','dacsan','tra','dau2','dau3','dau4','mut','tra2','hong','dacsanlon']; // BLENDER-DEEP-2 (muc 12)",
    tag='dacsan goods stalls')

# --- 7. Khoi sau build: decor rieng + tiem lon + quan ao ro + dong tiem 22h ---
POST = """
{ // BLENDER-DEEP-2 (mục 12-14): decor riêng cho sạp mới + TIỆM LỚN khu phải bậc + quần áo nhìn rõ
  const byId = id => stalls.find(x => x.id === id);
  function berryPyramid(st){ // hộp dâu xếp tháp trên quầy (mặt tiền đọc ra DÂU ngay)
    if(!st) return; const g = st.group;
    const lv = [[-0.5,0],[0.05,0],[0.6,0],[-0.22,1],[0.33,1],[0.05,2]];
    for(const [dx, l] of lv){
      box(0.46, 0.17, 0.4, 0xf0ead8, dx, 1.24 + l * 0.18, 0.92, g, false);
      for(let i = 0; i < 3; i++) ball(0.075, 0xd63c2a, dx - 0.13 + i * 0.13, 1.36 + l * 0.18, 0.92, g, 0.9);
    }
  }
  berryPyramid(byId('dau2')); berryPyramid(byId('dau3')); berryPyramid(byId('dau4'));
  { const st = byId('hong'); if(st){ // dây hồng treo gió trước sạp
    for(let k = 0; k < 3; k++){
      const sx = -0.9 + k * 0.9;
      cyl(0.012, 0.012, 0.75, 0x6a5136, sx, 2.15, 1.15, st.group, 4);
      for(let i = 0; i < 4; i++) ball(0.085, 0xe07b2a, sx, 2.32 - i * 0.17, 1.15, st.group, 0.9);
    } } }
  { const st = byId('hoa2'); if(st){ hydrangeaBasket(st.group, -1.5, 1.02, 1.1); hydrangeaBasket(st.group, 1.5, 1.02, 1.1); } }
  // --- mục 14: QUẦN ÁO NHÌN THẤY RÕ từ bậc tam cấp + đài phun ---
  { const post1 = box(0.09, 3.1, 0.09, 0x4a4038, 36.9, 1.55, 14.6, worldGroup, false);
    const post2 = box(0.09, 3.1, 0.09, 0x4a4038, 36.9, 1.55, 25.4, worldGroup, false);
    const sg = signMesh('QUẦN ÁO – ĐỒ LEN', 7.2, 1.05, '#7a2e22', '#ffe9b0', 'ÁO KHOÁC • ÁO LEN • ĐỒ SI • GIÁ RẺ');
    sg.position.set(36.85, 2.95, 20); sg.rotation.y = -Math.PI / 2; worldGroup.add(sg);
    solid(36.9, 14.6, 0.25, 0.25); solid(36.9, 25.4, 0.25, 0.25);
    function rack(x, z){ // giá treo NGOÀI mặt sạp
      const g = new THREE.Group(); g.position.set(x, 0, z); worldGroup.add(g);
      for(const dz of [-0.85, 0.85]) box(0.07, 1.55, 0.07, 0x3a3f4a, 0, 0.78, dz, g, false);
      const bar = cyl(0.03, 0.03, 1.8, 0x8a9298, 0, 1.5, 0, g, 6); bar.rotation.x = Math.PI / 2;
      const cols = [0xb03a30, 0xe07b2a, 0xe8c33c, 0x3f7a44, 0x2e6da4];
      for(let i = 0; i < 5; i++) box(0.05, 0.62, 0.3, cols[i], 0, 1.14, -0.68 + i * 0.34, g, false);
    }
    rack(36.7, 17.5); rack(36.7, 22.5);
    function mannequin(x, z, col){ // ma-nơ-canh mặc đồ len
      const g = new THREE.Group(); g.position.set(x, 0, z); g.rotation.y = -Math.PI / 2; worldGroup.add(g);
      cyl(0.3, 0.36, 0.14, 0x5a4632, 0, 0.07, 0, g, 10);
      box(0.2, 0.5, 0.24, 0x3a3f4a, 0, 0.4, 0, g, false);
      cyl(0.17, 0.21, 0.55, col, 0, 0.92, 0, g, 10);
      ball(0.135, 0xd9a37e, 0, 1.36, 0, g, 0.95);
      const bn = ball(0.14, col, 0, 1.44, 0, g, 0.55);
    }
    mannequin(37.2, 20, 0xc95d7e); mannequin(37.2, 25.0, 0x2e6da4);
  }
  // --- mục 13: TIỆM LỚN ĐẶC SẢN – LƯU NIỆM (vào được bên trong), mặt tiền x=49 nhìn về bậc/đài phun ---
  const SHOP = { x0: 49, x1: 59.5, z0: 14.2, z1: 25.8 };
  box(11, 0.12, 12, 0x9a8a76, 54.25, 0.06, 20, worldGroup, false); // sàn
  box(0.25, 3.4, 2.2, 0xe6d9bd, 49, 1.7, 15.3, worldGroup, false); // tường mặt tiền A
  box(0.25, 3.4, 2.2, 0xe6d9bd, 49, 1.7, 24.7, worldGroup, false); // tường mặt tiền B
  box(0.06, 2.3, 2.6, 0xa8cfe0, 49, 1.55, 17.7, worldGroup, false); // kính 1
  box(0.06, 2.3, 2.6, 0xa8cfe0, 49, 1.55, 22.3, worldGroup, false); // kính 2
  box(0.25, 0.7, 11.6, 0xe6d9bd, 49, 3.05, 20, worldGroup, false); // dầm biển
  box(0.25, 3.4, 12, 0xe6d9bd, 59.5, 1.7, 20, worldGroup, false); // tường sau
  box(10.5, 3.4, 0.25, 0xdfd0ae, 54.25, 1.7, 14.2, worldGroup, false); // tường hông bắc
  box(10.5, 3.4, 0.25, 0xdfd0ae, 54.25, 1.7, 25.8, worldGroup, false); // tường hông nam
  box(11.5, 0.18, 12.5, 0x51624a, 54.25, 3.55, 20, worldGroup, false); // mái
  { const sg = signMesh('ĐẶC SẢN – LƯU NIỆM', 8.6, 1.0, '#1f4d2e', '#ffe9b0', 'TRÁI CÂY SẤY • MỨT • TRÀ ATISO • QUÀ TẶNG');
    sg.position.set(48.82, 3.05, 20); sg.rotation.y = -Math.PI / 2; worldGroup.add(sg);
    const sg2 = signMesh('GIÁ RẺ', 2.0, 0.85, '#c8372d', '#ffe94d');
    sg2.position.set(48.85, 1.9, 17.7); sg2.rotation.y = -Math.PI / 2; worldGroup.add(sg2); }
  const GOODS_COLS = [0xc23b2e, 0xe07b2a, 0xe8c832, 0x6a9a4a, 0xf0ead8, 0x9a4a7a, 0xc9a227, 0x8c5a2e];
  function shelf(x, z, ry){ // kệ song song có hàng đóng gói đủ màu
    const g = new THREE.Group(); g.position.set(x, 0, z); g.rotation.y = ry; worldGroup.add(g);
    for(const dx of [-1.7, 1.7]) box(0.08, 1.7, 0.45, 0x6a5136, dx, 0.85, 0, g, false);
    for(let b = 0; b < 3; b++){
      box(3.6, 0.06, 0.5, 0x8a6a42, 0, 0.45 + b * 0.5, 0, g, false);
      for(let i = 0; i < 6; i++){
        const c = GOODS_COLS[(b * 6 + i + ((x * 7 + z) | 0)) % GOODS_COLS.length];
        if((i + b) % 3 === 2) cyl(0.07, 0.07, 0.22, c, -1.45 + i * 0.58, 0.6 + b * 0.5, 0, g, 8);
        else box(0.3, 0.24, 0.3, c, -1.45 + i * 0.58, 0.6 + b * 0.5, 0, g, false);
      }
    }
  }
  shelf(54, 15.1, 0); shelf(54, 24.9, Math.PI); shelf(58.5, 20, -Math.PI / 2);
  box(3.2, 1.35, 0.8, 0x74522f, 55.5, 0.68, 20, worldGroup, false); // đảo kệ giữa
  for(let i = 0; i < 6; i++){ box(0.3, 0.24, 0.3, GOODS_COLS[i % 8], 54.2 + (i % 3) * 1.1, 1.48, 19.8 + Math.floor(i / 3) * 0.4, worldGroup, false); }
  hydrangeaBasket(worldGroup, 48.2, 0.12, 16.2); hydrangeaBasket(worldGroup, 48.2, 0.12, 23.8);
  solid(49, 15.3, 0.3, 1.1); solid(49, 17.7, 0.3, 1.3); solid(49, 22.3, 0.3, 1.3); solid(49, 24.7, 0.3, 1.1);
  solid(59.5, 20, 0.3, 5.8); solid(54.25, 14.2, 5.25, 0.3); solid(54.25, 25.8, 5.25, 0.3);
  solid(55.5, 20, 1.6, 0.5); solid(54, 15.1, 1.8, 0.4); solid(54, 24.9, 1.8, 0.4); solid(58.5, 20, 0.4, 1.8);
  const shopShutter = box(0.12, 2.6, 2.2, 0x707880, 49, 1.3, 20, worldGroup, false); shopShutter.visible = false;
  const _hallTickShop = hallTick; // mục 13+10: tiệm thuộc nhóm đặc sản — mở tới 22:00 rồi đóng
  hallTick = function(){
    _hallTickShop();
    const st = byId('dacsanlon'); if(!st) return;
    const h = gameHour(); const closed = (h >= 22 || h < 6);
    if(st.closed !== closed){ st.closed = closed; if(st.vendor) st.vendor.visible = !closed; shopShutter.visible = closed; }
  };
}
"""
rep("for(const def of STALL_DEFS) buildStall(def);\nmergeStallStatics();",
    "for(const def of STALL_DEFS) buildStall(def);\nmergeStallStatics();" + POST,
    tag='post-build D (shop/quan ao/decor)')

open(P, 'w', encoding='utf-8').write(s)
print('PATCH D DONE, bytes =', len(s.encode('utf-8')), '(delta %+d)' % (len(s.encode('utf-8')) - orig))
