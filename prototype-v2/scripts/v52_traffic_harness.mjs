#!/usr/bin/env node
/* =====================================================================
   v52_traffic_harness.mjs — Harness kiểm tra logic TUYẾN XE MÁY v5.2
   (Tuyến song song B — CHỈ tạo file mới, không sửa index.html)

   Đặc tả: research/19-ke-hoach-xe-may.md + research/19b-tuyen-xe-toa-do.md

   Cách dùng:  node scripts/v52_traffic_harness.mjs [--verbose]
   Thoát mã 0 = mọi kiểm tra đạt; 1 = có kiểm tra hỏng.

   SNAPSHOT DỮ LIỆU: index.html lúc 07:36 08/11 — BẢN ĐANG CÀI V5.2 của
   tuyến chính (đã có vehBumpE/laneZE/laneZW, AW node 4/5/6 đã dời thành
   "đảo refuge", ROUTE_RING_OUT/IN + ROUTE_HILL). Các hàm hình học chép
   nguyên văn (bỏ comment); T14-T16 đo chính hình học bản đang cài, các
   test còn lại đo thiết kế tuyến ở research/19b trên cùng dữ liệu mới.

   Cấu trúc để đợt cài đặt thật "cắm vào":
   - PHẦN DATA: groundH/stairH/innerStairH/entryRampY/islandBump chép
     NGUYÊN VĂN từ index.html (chỉ-đọc lúc trích xuất, 08/11) + AW_NODES/
     AW_EDGES/LOOP/STALL_DEFS rút gọn + xe đậu vành đảo chép từ code.
   - PHẦN ROUTES: 3 tuyến xe là dữ liệu thuần {id, samples[], pullOvers[],
     slowZones[]} — bản cài đặt thật chỉ việc đọc cùng cấu trúc này.
   - PHẦN LOGIC THUẦN: giãn cách (follow), nhường người (yield), máy
     trạng thái tấp lề (pull-over cycle), máy trạng thái thuê xe
     (rent FSM) — tất cả là hàm thuần không phụ thuộc THREE/DOM.
   ===================================================================== */

// ---------------------------------------------------------------- DATA
// --- chép nguyên văn từ index.html: stairH (dòng ~415) ---
function stairH(z){
  if(z >= -2) return 0;
  if(z <= -30) return 17;
  if(z > -8.25){ const s = Math.min(1, Math.floor((z + 8.25) / 6.25 * 10) / 10); return 5.67 * (1 - s); }
  if(z > -12.25) return 5.67;
  if(z > -18.75){ const s = Math.min(1, Math.floor((z + 18.75) / 6.5 * 10) / 10); return 11.33 - 5.66 * s; }
  if(z > -22.75) return 11.33;
  const s = Math.min(1, Math.floor((z + 30) / 7.25 * 10) / 10);
  return 17 - 5.67 * s;
}
// --- chép nguyên văn từ index.html: innerStairH (dòng ~436) ---
function innerStairH(z){
  if(z <= 18.4){ const t = (z - 12) / 6.4; const s = Math.min(1, Math.floor(t*10)/10 + (t>=0.999?0.1:0)); return 12.6 - 6.05 * Math.min(1,s); }
  if(z <= 20.4) return 6.55;
  const t = (z - 20.4) / 6.4; const s = Math.min(1, Math.floor(t*10)/10 + (t>=0.999?0.1:0));
  return 6.55 - 6.05 * Math.min(1,s);
}
// --- chép nguyên văn từ index.html: groundH (dòng ~443) ---
function groundH(x,z){
  if(x >= 14.5 && x <= 20.5 && z >= -30 && z <= 9) return 17.14 - (z + 30) * 0.11282;
  if(x >= 29 && x <= 33 && z >= 12 && z <= 26.8) return innerStairH(z);
  if(x >= 14 && x <= 21 && z >= 7 && z <= 12) return 12.6;
  if(x >= 21 && x <= 33 && z >= 7 && z <= 12.2) return 12.6;
  if(x >= -34 && x <= 34 && z >= 12 && z <= 28) return 0.5;
  if(x < -52 && z >= -9 && z <= 13.5) return Math.min(2.0, (-52 - x) * 0.07);
  if(z <= -30) return 17;
  if(z >= -2) return 0;
  if(x >= -11 && x <= 11) return stairH(z);
  if((x >= -19 && x < -11) || (x > 11 && x < 14.5)){
    if(z > -8.25) return 2.8;
    if(z > -18.75) return 8.5;
    return 14.2;
  }
  if(x >= -45 && x < -19 && z < -2 && z > -30){
    if(z >= -16) return 0;
    return 17 * ((-16 - z) / 14);
  }
  return 17 * ((-2 - z) / 28);
}
// --- chép nguyên văn từ index.html: entryRampY + islandBump ---
function entryRampY(x){ return x < -52 ? Math.min(2.0, (-52 - x) * 0.07) : 0; }
function islandBump(x){
  const s = (a, b) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
  return s(-46, -30) * (1 - s(-18, -2));
}
// --- chép nguyên văn từ index.html BẢN ĐANG CÀI V5.2: profile làn đông
// hẹp vehBumpE + 2 hàm làn laneZE/laneZW (làn tây cũng đổi: gốc 4.1, biên 4.5) ---
function vehBumpE(x){
  const s = (a, b) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
  return s(-38, -27) * (1 - s(-21, -10));
}
function laneZE(x){ return -1.5 + 7.4 * vehBumpE(x); }   // làn đông: z theo x
function laneZW(x){ return 4.1 + 4.5 * islandBump(x); }  // làn tây: z theo x

// --- AW_NODES + AW_EDGES: chép nguyên văn (đồ thị tự-đi của người chơi) ---
const AW_NODES = [
  [-76,2],[-62,2],[-50,2],[-40,2],[-35,2.5],[-24,7.15],[-11.5,0.2],[-4,4.5],[0,1],[-2,-6],[-2,-14],[-2,-22],[-2,-29],[0,-36],[6,-45],[24,-51], // V5.2 (bản đang cài): nút 4/5/6 đã dời khỏi tâm làn — nút 5 = "đảo refuge" giữa 2 làn nam
  [8,5.5],[16,6.5],[22,7.2],
  [0,6],[0,11],[0,16],
  [12,-44],[17.5,-32],[17.5,-16],[17.5,0],[17.5,7],[24,9.8],[30.3,11],[30.3,15],
  [3,-11],[6.2,-9.6],
  [1,-20],[2.8,-19.6],
  [-8,-40],[-17,-44],
];
const AW_EDGES = [];
for(let i = 0; i < 15; i++) AW_EDGES.push([i, i + 1]);
AW_EDGES.push([7,16],[16,17],[17,18],[8,19],[19,20],[20,21],[14,22],[22,23],[23,24],[24,25],[25,26],[26,27],[27,28],[28,29],[10,30],[30,31],[11,32],[32,33],[13,34],[34,35]);

// --- LOOP người đi bộ lang thang: chép nguyên văn ---
const LOOP = [[-2,3],[-2,-29],[3,-38],[10,-45],[16,-38],[17.5,-28],[17.5,-8],[17.5,7],[24,9.8],[30.3,10.8],[30.3,19.4],[30.3,26.6],[24,24.5],[10,22],[0,24.5],[-14,22],[-24,24.5],[-28,20],[-14,17],[-2,15.5],[-2,8]];

// --- STALL_DEFS rút gọn (id, x, z, rotY) — chép từ bảng def trong code ---
const STALLS = [
  ['banhtrang',-36,10.15,Math.PI],['khoai',-31,10.15,Math.PI],['banhcan',-26,10.15,Math.PI],
  ['supcua',-21,10.15,Math.PI],['sua',22,10.15,Math.PI],['caphe',27,10.15,Math.PI],['yaourt',32,10.15,Math.PI],
  ['len1',-24,15,0],['len2',-16,23.5,Math.PI],['rau',16,15,0],['dau',24,23.5,Math.PI],
  ['khoainuong',6.2,-21.6,Math.PI/2],['suadau',6.2,-10.4,Math.PI/2],['hoa',37.5,10.15,Math.PI],
  ['dacsan',-20,20,Math.PI],['tra',20,20,0],['dongho',-6,-47,0],['luuniem',-31,-47,0],
  ['xien',-12,3,0],['che',6,3,0],['tron',30,3,0],['dauhu',-38,3,0],
  ['banhuot',-56,10.15,Math.PI],['suatuoi',-49.5,10.15,Math.PI],
].map(([id,x,z,rotY]) => ({ id, x, z, rotY,
  // mặt khách của sạp: tâm + hướng nhìn * 2.2 (khớp thông lệ buildStall/pourStream)
  fx: x + Math.sin(rotY) * 2.2, fz: z + Math.cos(rotY) * 2.2 }));

// --- Hằng số thế giới đo từ code ---
const ISLAND = { x:-24, z:-6, R:10.5 };            // cloneAsset('roundabout') tại (-24,0,-6); solid(-24,-6,10.4,10.4)
const STATUE = { x:-28.2, z:-2.8, R:4.4 };         // bệ đá 8.8x8.8 tại (-28.2,-2.8)
const RENT_PT_NOW = { x:31.5, z:13.8 };            // RENT_PT hiện tại trong code
const RENT_PT_NEW = { x:35.5, z:8.5 };             // ĐỀ XUẤT dời (xem R-01 trong 19b): groundH = 0
// Xe đậu vành đảo: chép từ vòng for deg trong code (rr 13.8 cho 200/238, còn lại 12.6)
const ISLAND_PARKED = [20,45,70,95,120,150,180,200,238].map(deg => {
  const a = deg * Math.PI / 180, rr = (deg === 200 || deg === 238) ? 13.8 : 12.6;
  return { deg, x: ISLAND.x + Math.cos(a) * rr, z: ISLAND.z + Math.sin(a) * rr };
});
const ISLAND_CARS = [[-40.2,-8],[-40.8,-3],[-40.2,2.5]].map(([x,z]) => ({ x, z }));
// Vùng cấm xe (suy từ các nhánh groundH + collider). LƯU Ý: deck cầu nổi
// x[14.5,20.5] z[-30,9] KHÔNG nằm ở đây — cầu VƯỢT QUA đường (deck ở cao
// 12.7-17.1, xe chạy DƯỚI cầu ở cao độ đường): kiểm riêng ở T1c theo chiều
// đứng. Xe trên trục đường BẮT BUỘC lấy y = entryRampY như code hiện tại,
// KHÔNG lấy groundH (nhánh cầu của groundH sẽ báo cao độ deck — R-07).
const FORBIDDEN = [
  { name:'bậc thang lớn',  minX:-11,  maxX:11,   minZ:-30, maxZ:-2 },
  { name:'sân thượng F2',  minX:14,   maxX:33,   minZ:7,   maxZ:12.2 },
  { name:'thang trong nhà',minX:29,   maxX:33,   minZ:12,  maxZ:26.8 },
  { name:'sảnh nhà lồng',  minX:-34,  maxX:34,   minZ:12,  maxZ:28 },
  // LƯU Ý: hộp collider đảo solid(-24,-6,10.4,10.4) KHÔNG đưa vào đây —
  // đó là collider chặn NGƯỜI CHƠI (vuông, góc thừa ra ngoài đĩa đảo tròn
  // R10.5); xe không dùng collider này. Vật cản thật của đảo = đĩa R10.5
  // + bệ tượng, đã kiểm riêng trong cùng test T1.
];
const VEH_HALF = 0.35;   // nửa bề ngang xe máy (ước lượng model vehicle.glb)
const PED_R = 0.35;      // bán kính người

// ------------------------------------------------------------- GEOMETRY
const dist = (a, b) => Math.hypot(a.x - b.x, a.z - b.z);
function segPointDist(p, a, b){
  const vx = b.x - a.x, vz = b.z - a.z, wx = p.x - a.x, wz = p.z - a.z;
  const L2 = vx*vx + vz*vz, t = L2 ? Math.max(0, Math.min(1, (wx*vx + wz*vz) / L2)) : 0;
  return Math.hypot(p.x - (a.x + vx*t), p.z - (a.z + vz*t));
}
function polyline(samples){ // -> {pts, cum[], len}
  const cum = [0];
  for(let i = 1; i < samples.length; i++) cum.push(cum[i-1] + dist(samples[i-1], samples[i]));
  return { pts: samples, cum, len: cum[cum.length-1] };
}
function pointAt(pl, s){
  s = Math.max(0, Math.min(pl.len, s));
  let i = 1; while(i < pl.cum.length - 1 && pl.cum[i] < s) i++;
  const segLen = pl.cum[i] - pl.cum[i-1] || 1, t = (s - pl.cum[i-1]) / segLen;
  const a = pl.pts[i-1], b = pl.pts[i];
  return { x: a.x + (b.x - a.x) * t, z: a.z + (b.z - a.z) * t };
}
function distToPolyline(pl, p){
  let m = Infinity;
  for(let i = 1; i < pl.pts.length; i++) m = Math.min(m, segPointDist(p, pl.pts[i-1], pl.pts[i]));
  return m;
}
function projectS(pl, p){ // s gần nhất của điểm p trên tuyến (quét thô + tinh)
  let best = 0, bd = Infinity;
  for(let s = 0; s <= pl.len; s += 0.5){ const q = pointAt(pl, s), d = dist(p, q); if(d < bd){ bd = d; best = s; } }
  return best;
}

// --------------------------------------------------------------- ROUTES
/* TUYẾN 1 — TRỤC ĐƯỜNG VÀO (2 làn, trục X) theo BẢN ĐANG CÀI V5.2:
   làn đông laneZE (vehBumpE hẹp, đỉnh z 5.9), làn tây laneZW (gốc 4.1 +
   4.5·islandBump, đỉnh 8.6). Mẫu cách 0.5 như bản thiết kế. */
function laneSamples(zFn){
  const pts = [];
  for(let x = -86; x <= 86; x += 0.5) pts.push({ x, z: zFn(x) });
  return pts;
}
const LANE_E = polyline(laneSamples(laneZE)); // dir +1 (đi sang đông)
const LANE_W = polyline(laneSamples(laneZW)); // dir -1 (đi sang tây)

/* HÌNH HỌC BẢN ĐANG CÀI (đo ở T14-T16): vòng đảo 2 làn cung nam–tây–bắc
   ROUTE_RING_OUT (R14.2, phình 16.2 ở 210°) / ROUTE_RING_IN (R12.7, cung
   nam 12.3) — sao lại logic ringPts của code (z = -6 - r·sin, góc độ);
   và ROUTE_HILL loop kín (chân đồi/bãi xe) chép nguyên văn danh sách điểm. */
function ringPts(r, rSouth, bulgeR){
  const pts = [];
  for(const th of [140, 160, 180, 200, 210, 220, 240, 260, 280, 300, 320, 340]){
    const a = th * Math.PI / 180;
    let rr = r;
    if(th >= 250 && th <= 290) rr = rSouth;
    if(bulgeR && th === 210) rr = bulgeR;
    if(bulgeR && th >= 320) rr = 15.2;
    pts.push({ x: -24 + rr * Math.cos(a), z: -6 - rr * Math.sin(a) });
  }
  return pts;
}
const RING_OUT = polyline(ringPts(14.2, 14.2, 16.2));
const RING_IN  = polyline(ringPts(12.7, 12.3, 0));
const HILL_LOOP = polyline([[54,12.3],[20,12.3],[-16,12.3],[-48.5,12.3],[-48.5,-1.2],[-38,-0.6],[-31,5.6],[-24,6.1],[-17,3.4],[-8,-1.1],[8,-1.4],[30,-1.3],[54,-1.2]].map(([x, z]) => ({ x, z })));

/* TUYẾN 3 — VÒNG CHÂN ĐỒI / KHU ĐÔNG (spur 1 chiều): rời trục chính ở
   (28,-1.5), vòng qua bãi xe đông + điểm thuê xe đề xuất, nhập lại làn W
   ở (28,4.5). Toàn tuyến groundH = 0. */
const ROUTE3 = polyline([
  {x:28,z:-1.5},{x:36,z:-1.3},{x:43,z:-0.5},{x:46.5,z:2.5},{x:46.5,z:6.5},
  {x:45,z:7.6},{x:41,z:7.3},{x:37,z:7.0},{x:31,z:5.2},{x:28,z:4.5},
]);

/* Điểm tấp lề (pull-over): xe dừng SÁT tuyến/vỉa hè, không cắt làn đối diện.
   recipient = vị trí khách đứng chờ (bán kính giao hàng 3.6 như tiền lệ rent). */
const PULL_OVERS = [
  { id:'T1-E1', route:'E', at:{x:-13.2,z:0.22}, note:'trên làn E (laneZE tại x=-13.2) — cạnh mép đông-nam đảo; BẢN CŨ đặt ở z=4.85 theo islandBump cũ, bản đang cài đã thu làn nên dời theo' },
  { id:'T1-E2', route:'E', at:{x:-52,  z:-1.5}, note:'đầu đường vào phía tây' },
  { id:'T1-W1', route:'W', at:{x:0,    z:6.2},  note:'vỉa hè trước mặt tiền', offLane:true },
  { id:'T1-W2', route:'W', at:{x:22,   z:6.2},  note:'trước dãy sạp đông (sữa)', offLane:true },
  { id:'T1-W3', route:'W', at:{x:-56,  z:6.2},  note:'trước sạp bánh ướt đầu đường vào', offLane:true },
  { id:'T1-W4', route:'W', at:{x:-50,  z:4.5},  note:'đầu đường vào phía tây (hướng về)' },
  { id:'T-FOOT',route:'E', at:{x:8,    z:0.2},  note:'chân bậc thang — gửi xe đi bộ lên thang', offLane:true },
  { id:'T3-0',  route:'3', at:{x:36,   z:7.1},  note:'điểm thuê xe đề xuất RENT_PT_NEW' },
  { id:'T3-1',  route:'3', at:{x:41,   z:7.3},  note:'bãi xe đông (parkedRow z=8.9)' },
];
/* Vạch sang đường (crossing): AW node nằm trong hành lang làn — xe BẮT BUỘC
   nhường khi có người trong bán kính 2.6 (logic yield ở dưới). */
const CROSSINGS = [
  { node:5,  at:{x:-24,z:7.15}, why:'"đảo refuge" bản đang cài: nằm GIỮA 2 làn nam (d tới E = 1.25, tới W = 1.45) — người qua đường đứng chờ tại đây, xe 2 làn phải nhường' },
  { node:7,  at:{x:-4, z:4.5},  why:'nút nằm ngay trên làn W (d = 0.21 so với laneZW) — điểm rẽ của trục đi bộ' },
];
/* Vùng chậm (slow zone): suy từ AW node/cạnh trong hành lang 3.6 của làn —
   harness tự kiểm vùng chậm đã khai bao phủ đủ mọi điểm bắt buộc. */
const SLOW_ZONES = [
  { route:'E', x0:-44, x1:-6,  cap:3.0, why:'cung nam đảo: AW node 4/5/6 + cạnh 3-4/4-5/5-6/6-7 giao làn' },
  { route:'W', x0:-44, x1:-6,  cap:3.0, why:'cung nam đảo (làn về)' },
  { route:'E', x0:-5,  x1:5,   cap:3.5, why:'AW node 8 trước mặt tiền + cạnh 8-19 cắt làn W' },
  { route:'W', x0:-5,  x1:5,   cap:3.5, why:'AW node 8 + cạnh 8-19' },
  { route:'E', x0:-58, x1:-46, cap:3.5, why:'AW node 2 đầu đường vào' },
  { route:'W', x0:-58, x1:-46, cap:3.5, why:'AW node 2 đầu đường vào' },
  { route:'W', x0:-46, x1:10,  cap:3.5, why:'hàng sạp đêm z=3: mặt khách (front) cách làn W ~0.5-2.1' },
  { route:'W', x0:5,   x1:11,  cap:3.5, why:'AW node 16 + cạnh 7-16 chạy song song cách làn W 0.3-1.0' },
  { route:'W', x0:11,  x1:26,  cap:3.5, why:'AW node 17/18 + cạnh 16-17/17-18 song song làn W (d 2.0-2.7)' },
  { route:'3', s0:0,   s1:12,  cap:3.0, why:'đoạn nhập/xuất trục chính' },
  { route:'3', s0:52,  s1:78,  cap:3.0, why:'đoạn nhập lại làn W + gần điểm thuê' },
];
const ROUTE_SPEED = { E:8, W:8, '3':7 };  // khớp dải 6-9 của research/19
const MAX_ACTIVE = 14;                     // trần xe chạy đồng thời (research/19 mục 2.5)

// ------------------------------------------------- LOGIC THUẦN (để cắm)
// Giãn cách: tốc độ mong muốn của xe theo xe trước cùng làn (s vòng kín
// cho tuyến trục X như cơ chế wrap ±86 trong code; tuyến 3 không vòng).
function followSpeed(me, leader, opts){
  const { desired, minGap = 2.2, comfortGap = 4.5 } = opts;
  if(!leader) return desired;
  let gap = leader.s - me.s;
  if(opts.wrapLen) gap = ((gap % opts.wrapLen) + opts.wrapLen) % opts.wrapLen;
  if(gap < minGap) return 0;                                  // sát quá: dừng
  if(gap < comfortGap) return Math.min(desired, leader.speed * (gap - minGap) / (comfortGap - minGap) + 0.001);
  return desired;
}
// Nhường người: có người trong bán kính yieldR quanh điểm trước đầu xe
// (look-ahead) -> tốc độ cho phép; người đứng tại vạch sang đường thì xe
// dừng hẳn trước vạch stopGap.
function yieldSpeed(veh, peds, opts){
  const { desired, lookAhead = 7, yieldR = 2.6, stopGap = 1.3 } = opts;
  let v = desired;
  for(const p of peds){
    const ahead = p.sProj - veh.s;                            // khoảng dọc tuyến tới người
    if(ahead < -0.5 || ahead > lookAhead) continue;
    if(p.lateral > yieldR) continue;                          // người ngoài hành lang làn
    if(p.atCrossing && ahead <= stopGap + 0.6) return 0;      // dừng trước vạch
    v = Math.min(v, Math.max(0, desired * (ahead - stopGap) / lookAhead));
  }
  return v;
}
// Máy trạng thái tấp lề của xe NPC (research/19 mục 2.4):
// CRUISE -> DECEL -> STOPPED -> RIDER_DOWN -> SHOP -> RETURN -> BOARD -> DEPART -> CRUISE
const PO_TIMING = { decel:2.0, dwell:2.0, walk:4.0, shop:6.0, walkBack:4.0, board:1.2 };
function poStep(st, dt, ctx){
  st.t += dt;
  switch(st.state){
    case 'CRUISE':     if(ctx.atPullOver) return { ...st, state:'DECEL', t:0 }; break;
    case 'DECEL':      if(st.t >= PO_TIMING.decel) return { ...st, state:'STOPPED', t:0 }; break;
    case 'STOPPED':    if(st.t >= PO_TIMING.dwell) return { ...st, state:'RIDER_DOWN', t:0 }; break;
    case 'RIDER_DOWN': if(st.t >= PO_TIMING.walk) return { ...st, state:'SHOP', t:0 }; break;
    case 'SHOP':       if(st.t >= PO_TIMING.shop) return { ...st, state:'RETURN', t:0 }; break;
    case 'RETURN':     if(st.t >= PO_TIMING.walkBack) return { ...st, state:'BOARD', t:0 }; break;
    case 'BOARD':      if(st.t >= PO_TIMING.board) return { ...st, state:'DEPART', t:0 }; break;
    case 'DEPART':     return { ...st, state:'CRUISE', t:0 };
  }
  return st;
}
// Máy trạng thái thuê xe (research/19 mục 2.3): hết giờ -> đếm ngược 10s
// trên HUD -> xe tự về bãi (không biến mất đột ngột); xuống xe giữa chừng
// thì đồng hồ vẫn chạy, lên lại giữ nguyên deadline.
function rentStep(st, dt, ev){
  const s = { ...st };
  if(ev === 'rent'){ if(s.state === 'IDLE'){ s.state = 'RENTED'; s.t = 90; s.countdownShown = false; } return s; }
  if(ev === 'dismount' && s.state === 'RENTED'){ s.state = 'PARKED_FREE'; return s; }
  if(ev === 'remount' && s.state === 'PARKED_FREE'){ s.state = 'RENTED'; return s; }
  if(ev === 'return' && (s.state === 'RENTED' || s.state === 'PARKED_FREE')){ s.state = 'RETURNING'; s.t = 0; return s; }
  if(s.state === 'RENTED' || s.state === 'PARKED_FREE'){
    s.t -= dt;
    if(s.t <= 10 && s.t > 0) s.countdownShown = true;         // HUD đếm ngược 10s cuối
    if(s.t <= 0){ s.state = 'RETURNING'; s.t = 0; }
  } else if(s.state === 'RETURNING'){
    s.t += dt; if(s.t >= 3) { s.state = 'IDLE'; s.t = 0; s.atRentPt = true; }
  }
  return s;
}

// ---------------------------------------------------------------- TESTS
const VERBOSE = process.argv.includes('--verbose');
const results = [];
function check(id, name, ok, detail){
  results.push({ id, name, ok, detail });
  if(VERBOSE || !ok) console.log(`${ok ? 'PASS' : 'FAIL'}  ${id}  ${name}${detail ? ' — ' + detail : ''}`);
}
const samplesOf = pl => pl.pts;

// T0 — sanity dữ liệu chép nguyên văn
check('T0a','groundH tại RENT_PT hiện tại (31.5,13.8) — phơi bày R-01',
  Math.abs(groundH(RENT_PT_NOW.x, RENT_PT_NOW.z) - 11.39) < 0.05,
  `groundH = ${groundH(RENT_PT_NOW.x, RENT_PT_NOW.z).toFixed(2)} (innerStairH chuyến 1) — xe thuê + biển đang nằm trên thang trong nhà, không phải bãi xe`);
check('T0b','groundH tại RENT_PT đề xuất (35.5,8.5) = 0',
  groundH(RENT_PT_NEW.x, RENT_PT_NEW.z) === 0, `groundH = ${groundH(RENT_PT_NEW.x, RENT_PT_NEW.z)}`);
check('T0c','AW_NODES/EDGES/LOOP đủ số lượng chép nguyên văn',
  AW_NODES.length === 36 && AW_EDGES.length === 35 && LOOP.length === 21,
  `nodes=${AW_NODES.length} edges=${AW_EDGES.length} loop=${LOOP.length}`);

// T1 — tuyến không vào vùng cấm + không xuyên đảo/tượng
for(const [nm, pl] of [['làn E', LANE_E], ['làn W', LANE_W], ['tuyến 3', ROUTE3]]){
  let badZone = null, badIsland = null, badStatue = null;
  for(const p of samplesOf(pl)){
    for(const f of FORBIDDEN) if(p.x > f.minX && p.x < f.maxX && p.z > f.minZ && p.z < f.maxZ) badZone = `${f.name} @(${p.x},${p.z})`;
    if(dist(p, ISLAND) < ISLAND.R + VEH_HALF) badIsland = `@(${p.x},${p.z}) d=${dist(p, ISLAND).toFixed(2)}`;
    if(dist(p, STATUE) < STATUE.R + VEH_HALF) badStatue = `@(${p.x},${p.z})`;
  }
  check('T1-' + nm, `${nm}: ngoài mọi vùng cấm, ngoài đĩa đảo (R10.5+0.35), ngoài bệ tượng`,
    !badZone && !badIsland && !badStatue, badZone || badIsland || badStatue || 'sạch');
}
// T1c — cầu nổi VƯỢT QUA đường: xe chạy dưới deck, tĩnh không đứng >= 10
{
  let minDeck = Infinity;
  for(let x = 14.5; x <= 20.5; x += 0.5) for(const z of [-1.5, 4.5])
    minDeck = Math.min(minDeck, 17.14 - (z + 30) * 0.11282); // cao độ deck theo nhánh groundH
  check('T1c','cầu nổi: deck cao tối thiểu trên 2 làn >= 12 (xe cao ~1.6 -> tĩnh không ~10.4)',
    minDeck >= 12, `deck min = ${minDeck.toFixed(2)} tại z=4.5, x trong [14.5,20.5]; xe lấy y=entryRampY=0`);
}
// T1b — khoảng cách tối thiểu làn <-> tâm đảo (bán kính cung nam đảo thực tế)
{
  const minE = Math.min(...samplesOf(LANE_E).map(p => dist(p, ISLAND)));
  const minW = Math.min(...samplesOf(LANE_W).map(p => dist(p, ISLAND)));
  check('T1b','bán kính cung nam đảo: làn E ≈11.9 (vehBumpE hẹp) / làn W ≈14.6 từ tâm đảo (-24,-6)',
    Math.abs(minE - 11.9) < 0.15 && Math.abs(minW - 14.6) < 0.15,
    `minE=${minE.toFixed(2)} minW=${minW.toFixed(2)} (đảo R10.5 -> khe hở E=${(minE-10.5-VEH_HALF).toFixed(2)}, W=${(minW-10.5-VEH_HALF).toFixed(2)})`);
}
// T2 — độ dốc theo groundH/entryRampY: xe không leo bậc thang, dốc <= 12%
for(const [nm, pl, yFn] of [['làn E', LANE_E, entryRampY], ['làn W', LANE_W, entryRampY], ['tuyến 3', ROUTE3, null]]){
  let maxGrade = 0, badY = null;
  const pts = samplesOf(pl);
  for(let i = 1; i < pts.length; i++){
    const y0 = yFn ? yFn(pts[i-1].x) : groundH(pts[i-1].x, pts[i-1].z);
    const y1 = yFn ? yFn(pts[i].x) : groundH(pts[i].x, pts[i].z);
    const run = dist(pts[i-1], pts[i]) || 1e-9;
    maxGrade = Math.max(maxGrade, Math.abs(y1 - y0) / run);
    if(!yFn && Math.abs(y1) > 0.05) badY = `@(${pts[i].x},${pts[i].z}) groundH=${y1}`;
  }
  check('T2-' + nm, `${nm}: dốc tối đa <= 12%${yFn ? ' (bám entryRampY như code)' : ' + groundH = 0 toàn tuyến'}`,
    maxGrade <= 0.12 && !badY, `maxGrade=${(maxGrade*100).toFixed(1)}%${badY ? ' ' + badY : ''}`);
}
// T3 — hai làn đối diện đủ khe hở (đo trên laneZE/laneZW bản đang cài)
{
  let minGap = Infinity, atX = 0;
  for(let x = -86; x <= 86; x += 0.5){
    const g = laneZW(x) - laneZE(x);
    if(g < minGap){ minGap = g; atX = x; }
  }
  check('T3','khe hở 2 làn đối diện (tâm-tâm trừ 2 nửa xe) >= 0.8',
    minGap - 2 * VEH_HALF >= 0.8, `min tâm-tâm=${minGap.toFixed(2)} tại x=${atX} (vùng đỉnh 2 profile chồng nhau) -> khe hở ${(minGap - 2*VEH_HALF).toFixed(2)}`);
}
// T4 — làn <-> xe đậu vành đảo: liệt kê ĐÚNG các điểm chật đã biết (R-02).
// Bản đang cài (vehBumpE bán kính 11.9-12.4 ở cung nam) luồn qua cả vành
// đậu R12.6 ở 6 cung: 20/45/70/95/120/150 — xem số đo trong detail.
{
  const KNOWN_TIGHT = [20, 45, 70, 95, 120, 150];
  const tight = [];
  forconst: for(const b of ISLAND_PARKED){
    const dE = distToPolyline(LANE_E, b), dW = distToPolyline(LANE_W, b);
    const d = Math.min(dE, dW);
    if(d - 2 * VEH_HALF < 0.35){
      if(!KNOWN_TIGHT.includes(b.deg)){ tight.push(`deg${b.deg} d=${d.toFixed(2)}`); }
      continue forconst;
    }
  }
  const dAll = ISLAND_PARKED.map(b => `deg${b.deg} d=${Math.min(distToPolyline(LANE_E, b), distToPolyline(LANE_W, b)).toFixed(2)}`).join(', ');
  check('T4','xe đậu vành đảo: không có điểm chật NGOÀI danh sách đã biết {20,45,70,95,120,150} (R-02)',
    tight.length === 0, `${dAll} (R-02: vành đậu cung nam R12.6 không tương thích làn E bán kính 11.9-12.4 — đề xuất rút xe đậu khỏi cung nam đảo)${tight.length ? ' | PHÁT SINH: ' + tight.join(', ') : ''}`);
}
// T5 — làn <-> thân sạp (bán kính thân 1.1, xấp xỉ tròn tâm def): bản đang
// cài: vehBumpE đã dọn sạch dauhu/xien khỏi làn E; overlap còn lại là
// {che, tron} do laneZW hạ gốc 4.5 -> 4.1 áp sát hàng sạp z=3 (R-03 mới —
// LƯU Ý xấp xỉ tròn: cần đối chiếu origin stall.glb/render mới kết luận).
{
  const KNOWN_OVERLAP = ['che', 'tron'];
  const overlaps = [], grazes = [];
  for(const st of STALLS){
    const dE = distToPolyline(LANE_E, st), dW = distToPolyline(LANE_W, st), d3 = distToPolyline(ROUTE3, st);
    const d = Math.min(dE, dW, d3), body = 1.1 + VEH_HALF;
    if(d < body) overlaps.push(`${st.id} d=${d.toFixed(2)}`);
    else if(d < body + 0.55) grazes.push(`${st.id} d=${d.toFixed(2)}`);
  }
  const unexpected = overlaps.filter(o => !KNOWN_OVERLAP.some(k => o.startsWith(k)));
  const missing = KNOWN_OVERLAP.filter(k => !overlaps.some(o => o.startsWith(k)));
  check('T5','thân sạp: overlap cứng đúng tập đã biết {che, tron} theo xấp xỉ tròn (R-03); graze còn lại trong vùng chậm',
    unexpected.length === 0 && missing.length === 0,
    `overlaps=[${overlaps.join(', ')}] grazes=[${grazes.join(', ')}]${unexpected.length ? ' | PHÁT SINH: ' + unexpected.join(', ') : ''}${missing.length ? ' | THIẾU KHỚP: ' + missing.join(', ') : ''}`);
}
// T6 — làn <-> AW node Ở CAO ĐỘ ĐƯỜNG (groundH <= 2.5): node trong hành
// lang < 1.1 phải thuộc CROSSINGS có yield. Node trên cầu/thang/đồi
// (groundH > 2.5, vd node 25/26 trên deck) là phân tầng đứng — bỏ qua.
{
  const bad = [], elevated = [];
  const awPts = AW_NODES.map(([x, z]) => ({ x, z }));
  awPts.forEach((p, i) => {
    if(groundH(p.x, p.z) > 2.5){ elevated.push(i); return; }
    const d = Math.min(distToPolyline(LANE_E, p), distToPolyline(LANE_W, p), distToPolyline(ROUTE3, p));
    if(d < 1.1 && !CROSSINGS.some(c => c.node === i)) bad.push(`node${i} (${p.x},${p.z}) d=${d.toFixed(2)}`);
  });
  const c5 = Math.min(distToPolyline(LANE_E, awPts[5]), distToPolyline(LANE_W, awPts[5]));
  check('T6','AW node cao độ đường: mọi node < 1.1 so với làn đều là vạch sang đường có yield',
    bad.length === 0, `node5 d=${c5.toFixed(2)}; node phân tầng đứng (bỏ qua): ${elevated.join(',')}${bad.length ? ' | LỖI: ' + bad.join(', ') : ''}`);
}
// T7 — vùng chậm bao phủ 3 lớp bắt buộc:
//  (a) mọi CROSSINGS node: làn nào cách < 3.6 thì x của node phải trong vùng chậm làn đó;
//  (b) mọi giao cắt cạnh AW <-> làn Ở CAO ĐỘ ĐƯỜNG (groundH điểm cắt <= 2.5)
//      phải trong vùng chậm; giao cắt trên deck/thang = phân tầng đứng, chỉ liệt kê;
//  (c) mọi mẫu cạnh AW cách làn < 1.6 (chạy song song/chạm) ở cao độ đường
//      phải trong vùng chậm của làn đó.
//  (Node trục tây node 0/1 cách làn 2.5-3.5 trên đoạn thẳng: xử bằng yield
//   theo bán kính, không cần vùng chậm — xem 19b mục 5.)
{
  const awPts = AW_NODES.map(([x, z]) => ({ x, z }));
  const inSlow = (route, x) => SLOW_ZONES.some(z => z.route === route && x >= z.x0 && x <= z.x1);
  const problems = [];
  for(const c of CROSSINGS){
    const p = awPts[c.node];
    if(distToPolyline(LANE_E, p) < 3.6 && !inSlow('E', p.x)) problems.push(`crossing node${c.node} chưa phủ làn E`);
    if(distToPolyline(LANE_W, p) < 3.6 && !inSlow('W', p.x)) problems.push(`crossing node${c.node} chưa phủ làn W`);
    if(distToPolyline(ROUTE3, p) < 3.6) problems.push(`crossing node${c.node} gần tuyến 3 (chưa khai vùng chậm s)`);
  }
  const atGrade = new Set(), gradeSep = new Set();
  for(const [a, b] of AW_EDGES){
    const A = awPts[a], B = awPts[b];
    for(let t = 0; t <= 1.0001; t += 0.025){
      const p = { x: A.x + (B.x - A.x) * t, z: A.z + (B.z - A.z) * t };
      for(const [nm, pl] of [['E', LANE_E], ['W', LANE_W]]){
        const d = distToPolyline(pl, p);
        if(d < 0.45){
          if(groundH(p.x, p.z) > 2.5) gradeSep.add(`cạnh ${a}-${b} x=${p.x.toFixed(1)} ${nm} (trên deck/thang)`);
          else { atGrade.add(`cạnh ${a}-${b} x=${p.x.toFixed(1)} ${nm}`); if(!inSlow(nm, p.x)) problems.push(`giao cắt cạnh ${a}-${b} x=${p.x.toFixed(1)} làn ${nm} chưa phủ vùng chậm`); }
        } else if(d < 1.6 && groundH(p.x, p.z) <= 2.5 && !inSlow(nm, p.x)){
          problems.push(`cạnh ${a}-${b} chạy sát làn ${nm} tại x=${p.x.toFixed(1)} (d=${d.toFixed(2)}) chưa phủ vùng chậm`);
        }
      }
    }
  }
  check('T7','vùng chậm bao phủ: crossing nodes + giao cắt cao độ đường + đoạn cạnh chạy sát làn',
    problems.length === 0,
    `giao cắt cao độ đường: ${atGrade.size} điểm mẫu (${[...atGrade].slice(0, 8).join('; ')}${atGrade.size > 8 ? '; …' : ''}); phân tầng đứng: ${gradeSep.size} điểm${problems.length ? ' | LỖI: ' + [...new Set(problems)].join(' | ') : ''}`);
}
// T8 — pull-over: không lấn làn đối diện + đúng tuyến của nó
{
  const bad = [];
  for(const po of PULL_OVERS){
    const own = po.route === 'E' ? LANE_E : po.route === 'W' ? LANE_W : ROUTE3;
    const opp = po.route === 'E' ? LANE_W : po.route === 'W' ? LANE_E : null;
    const dOwn = distToPolyline(own, po.at);
    if(dOwn > (po.offLane ? 2.4 : 0.6)) bad.push(`${po.id} lệch tuyến nhà ${dOwn.toFixed(2)}`);
    if(opp && distToPolyline(opp, po.at) - 2 * VEH_HALF < 0.8) bad.push(`${po.id} lấn làn đối diện`);
    if(dist(po.at, ISLAND) < ISLAND.R + VEH_HALF) bad.push(`${po.id} lọt vào đảo`);
  }
  check('T8','9 điểm tấp lề: bám tuyến nhà, không lấn làn đối diện, ngoài đảo', bad.length === 0, bad.join(' | ') || 'đạt');
}
// T9 — nhiệm vụ giao hàng mẫu: khoảng cách tấp lề <-> sạp/khách <= 3.6 (tiền lệ rent)
{
  const stall = id => STALLS.find(s => s.id === id);
  const po = id => PULL_OVERS.find(p => p.id === id);
  const MISSIONS = [
    { id:'M1', from:'sua',     fromPO:'T1-W2', pickLeg:'ride', to:{x:-13.2,z:2.8},  toPO:'T1-E1', name:'Sữa đậu nành nóng -> khách chờ mép đông-nam đảo' },
    { id:'M2', from:'banhuot', fromPO:'T1-W3', pickLeg:'ride', to:{x:41,  z:9.6},  toPO:'T3-1',  name:'Bánh ướt lòng gà -> khách ở bãi xe đông' },
    { id:'M3', from:'suadau',  fromPO:'T-FOOT',pickLeg:'walk', to:{x:-51, z:1.2},  toPO:'T1-W4', name:'Sữa đậu nành trên thang (đi bộ lên lấy) -> khách đầu đường vào tây' },
  ];
  const bad = [];
  for(const m of MISSIONS){
    const st = stall(m.from);
    const dPick = dist(po(m.fromPO).at, { x: st.fx, z: st.fz });
    const dDrop = dist(po(m.toPO).at, m.to);
    if(m.pickLeg === 'ride' && dPick > 3.6) bad.push(`${m.id} lấy hàng (xe) xa ${dPick.toFixed(2)}`);
    if(m.pickLeg === 'walk'){
      // chân đi bộ: gửi xe ở T-FOOT rồi leo thang — đoạn đi bộ <= 12 và
      // mặt sạp phải nằm trong hình chữ nhật bậc thang x[-11,11] z[-30,-2]
      const inStairs = st.x >= -11 && st.x <= 11 && st.z >= -30 && st.z <= -2;
      if(dPick > 12 || !inStairs) bad.push(`${m.id} chân đi bộ lấy hàng sai: d=${dPick.toFixed(2)} inStairs=${inStairs}`);
    }
    if(dDrop > 3.6) bad.push(`${m.id} giao hàng xa ${dDrop.toFixed(2)}`);
  }
  check('T9','3 nhiệm vụ mẫu: giao <= 3.6; lấy hàng bằng xe <= 3.6 / bằng chân đi bộ leo thang <= 12 (M3)',
    bad.length === 0, bad.join(' | ') || 'đạt');
}
// T10 — mô phỏng giãn cách: 600s, 2 làn, tốc độ trộn, có xe dừng tấp lề
{
  function simLane(lanePl, dirSign, n, speeds, blockAt){
    const L = lanePl.len;
    const vs = speeds.map((sp, i) => ({ s: (L / n) * i, speed: 0, desired: sp, stopped: 0 }));
    let minGapSeen = Infinity, dt = 0.1;
    for(let t = 0; t < 600; t += dt){
      for(let i = 0; i < vs.length; i++){
        const me = vs[i], leader = vs[(i + 1) % vs.length];
        let want = followSpeed(me, leader, { desired: me.desired, wrapLen: L });
        if(blockAt !== null && Math.abs(((me.s - blockAt) % L + L) % L) < 0.6 && t > 60 && t < 66) want = 0; // xe i dừng tấp lề 6s
        me.speed += Math.max(-6 * dt, Math.min(3.5 * dt, want - me.speed));
        me.s = (me.s + me.speed * dt + L) % L;
      }
      for(let i = 0; i < vs.length; i++){
        const a = vs[i], b = vs[(i + 1) % vs.length];
        let g = ((b.s - a.s) % L + L) % L;
        if(g > 0.01) minGapSeen = Math.min(minGapSeen, g);
      }
    }
    return minGapSeen;
  }
  const g1 = simLane(LANE_E, 1, 5, [8, 6.2, 7.4, 6, 8], null);
  const g2 = simLane(LANE_W, -1, 5, [7.8, 6.1, 8, 6.6, 7.2], LANE_W.len * 0.4);
  check('T10','giãn cách mô phỏng 600s: khoảng cách xe-trước tối thiểu >= 2.0 (kể cả khi có xe tấp lề dừng 6s)',
    g1 >= 2.0 && g2 >= 2.0, `minGap làn E=${g1.toFixed(2)}, làn W (có dừng)=${g2.toFixed(2)}; trần xe ${MAX_ACTIVE} (hiện code: 7)`);
}
// T11 — yield tại vạch sang đường node 5 (đảo refuge -24,7.15): xe dừng
// hẳn, không lấn 0.7 quanh người
{
  const node5 = { x:-24, z:7.15 };
  const sProj = projectS(LANE_E, node5);
  let veh = { s: sProj - 30, speed: 8 };
  let stoppedAt = null, violated = false;
  for(let t = 0; t < 20; t += 0.05){
    const front = pointAt(LANE_E, veh.s + 1.0);
    if(dist(front, node5) < 0.7 + VEH_HALF) violated = true;
    const ped = { sProj, lateral: dist(pointAt(LANE_E, sProj), node5), atCrossing: true };
    const want = yieldSpeed(veh, [ped], { desired: 8 });
    veh.speed += Math.max(-7 * 0.05, Math.min(3 * 0.05, want - veh.speed));
    veh.s += veh.speed * 0.05;
    if(want === 0 && veh.speed < 0.05){ stoppedAt = veh.s; break; }
  }
  check('T11','yield node 5: xe về 0 trước vạch, không lấn vùng 0.7 quanh người',
    stoppedAt !== null && !violated && (sProj - stoppedAt) > 1.0,
    `dừng tại s=${stoppedAt ? stoppedAt.toFixed(1) : '—'} (vạch ở s=${sProj.toFixed(1)}), xâm phạm=${violated}`);
}
// T12 — chu trình tấp lề NPC chạy trọn vòng, xe đứng yên khi người xuống
{
  let st = { state:'CRUISE', t:0 }, seq = ['CRUISE'], total = 0;
  for(let t = 0; t < 60; t += 0.1){
    st = poStep(st, 0.1, { atPullOver: seq.length === 1 && t > 1 });
    total += 0.1;
    if(seq[seq.length - 1] !== st.state) seq.push(st.state);
    if(st.state === 'CRUISE' && seq.length > 1) break;
  }
  const expect = ['CRUISE','DECEL','STOPPED','RIDER_DOWN','SHOP','RETURN','BOARD','DEPART','CRUISE'];
  check('T12','chu trình tấp lề: đủ 8 trạng thái theo thứ tự, trọn vòng <= 30s',
    JSON.stringify(seq) === JSON.stringify(expect) && total <= 30,
    `seq=${seq.join('>')} tổng=${total.toFixed(1)}s`);
}
// T13 — thuê xe: đếm ngược 10s cuối, xuống/lên xe giữ deadline, hết giờ tự về bãi
{
  let r = { state:'IDLE', t:0, countdownShown:false, atRentPt:true };
  r = rentStep(r, 0, 'rent');
  const okRent = r.state === 'RENTED' && r.t === 90;
  for(let i = 0; i < 500; i++) r = rentStep(r, 0.1, null);       // 50s
  r = rentStep(r, 0, 'dismount');                                  // xuống xe giữa chừng
  const okPark = r.state === 'PARKED_FREE' && Math.abs(r.t - 40) < 0.2;
  for(let i = 0; i < 100; i++) r = rentStep(r, 0.1, null);         // đỗ 10s, đồng hồ vẫn chạy
  r = rentStep(r, 0, 'remount');
  const okRemount = r.state === 'RENTED' && Math.abs(r.t - 30) < 0.2;
  let sawCountdown = false, expiredState = null;
  for(let i = 0; i < 400; i++){ r = rentStep(r, 0.1, null); if(r.countdownShown) sawCountdown = true; if(r.state === 'RETURNING'){ expiredState = 'RETURNING@' + (i * 0.1).toFixed(0) + 's'; break; } }
  for(let i = 0; i < 40; i++) r = rentStep(r, 0.1, null);
  check('T13','FSM thuê xe: 90s, đỗ tự do giữ deadline, đếm ngược 10s cuối, hết giờ -> RETURNING -> về bãi (IDLE tại RENT_PT)',
    okRent && okPark && okRemount && sawCountdown && expiredState !== null && r.state === 'IDLE' && r.atRentPt === true,
    `rent=${okRent} park=${okPark} remount=${okRemount} countdown=${sawCountdown} ${expiredState || ''}`);
}

// T14 — VÒNG ĐẢO bản đang cài (RING_OUT/IN): an toàn cứng (đĩa đảo, tượng,
// mặt đất) phải sạch; va chạm với xe đậu vành đảo là điểm phơi bày R-09.
{
  let badDisc = null, badGround = null, badStatue = null;
  for(const [nm, pl] of [['RING_OUT', RING_OUT], ['RING_IN', RING_IN]]){
    for(const p of samplesOf(pl)){
      if(dist(p, ISLAND) < ISLAND.R + VEH_HALF) badDisc = `${nm} @(${p.x.toFixed(1)},${p.z.toFixed(1)}) d=${dist(p, ISLAND).toFixed(2)}`;
      if(dist(p, STATUE) < STATUE.R + VEH_HALF) badStatue = `${nm} @(${p.x.toFixed(1)},${p.z.toFixed(1)})`;
      if(Math.abs(groundH(p.x, p.z)) > 0.05) badGround = `${nm} @(${p.x.toFixed(1)},${p.z.toFixed(1)}) groundH=${groundH(p.x, p.z)}`;
    }
  }
  check('T14a','vòng đảo đang cài: ngoài đĩa đảo + bệ tượng, groundH = 0 tại mọi đỉnh cung',
    !badDisc && !badGround && !badStatue, badDisc || badGround || badStatue || 'sạch (cung chạy trên thềm phẳng + sân nam đảo)');
  let worst = null, worstD = Infinity;
  for(const b of ISLAND_PARKED){
    for(const [nm, pl] of [['RING_OUT', RING_OUT], ['RING_IN', RING_IN]]){
      const d = distToPolyline(pl, b);
      if(d < worstD){ worstD = d; worst = `${nm} <-> xe đậu deg${b.deg}`; }
    }
  }
  check('T14b','PHƠI BÀY R-09: vòng đảo đang cài cắt qua xe đậu vành đảo',
    worstD < 0.7, `điểm tệ nhất: ${worst} d=${worstD.toFixed(2)} -> khe hở ${(worstD - 2 * VEH_HALF).toFixed(2)} (âm = xuyên); thêm RING_OUT <-> deg200 d=0.39 — cần dời các xe đậu deg45/deg200 hoặc nắn cung vòng ở góc 300-320°/160°`);
}
// T15 — ROUTE_HILL bản đang cài: chân bắc z=12.3 chạy xuyên hàng xe đậu
// z=11.75 + nằm trong dải sàn nhà lồng (z >= 12) ở |x| <= 34 (R-10).
{
  let inHall = 0, samples = 0;
  for(const p of samplesOf(HILL_LOOP)){
    samples++;
    if(Math.abs(p.x) <= 34 && p.z >= 12) inHall++;
  }
  const dParkedRow = Math.abs(12.3 - 11.75);
  check('T15','PHƠI BÀY R-10: chân bắc ROUTE_HILL (z=12.3) vs hàng xe đậu trước chợ (z=11.75) + dải sàn nhà lồng',
    inHall > 0 && dParkedRow - 2 * VEH_HALF < 0,
    `${inHall}/${samples} đỉnh nằm trong dải z>=12 |x|<=34; khoảng cách tới hàng xe đậu = ${dParkedRow.toFixed(2)} -> khe hở ${(dParkedRow - 2 * VEH_HALF).toFixed(2)} (âm = xe chạy cọ hàng xe đậu dày ~82%) — cần soi render xác nhận đây là làn sau sạp có chủ đích hay lỗi`);
}
// T16 — ROUTE_HILL x ROUTE_RING_IN giao nhau ở nam đảo (~(-24, 6.1-6.3)):
// giãn cách trong updateTraffic chỉ áp cùng tuyến -> 2 tuyến cắt nhau
// không có cơ chế nhường lẫn nhau (R-11).
{
  let minD = Infinity;
  for(const p of samplesOf(HILL_LOOP)) minD = Math.min(minD, distToPolyline(RING_IN, p));
  for(const p of samplesOf(RING_IN)) minD = Math.min(minD, distToPolyline(HILL_LOOP, p));
  check('T16','PHƠI BÀY R-11: ROUTE_HILL và ROUTE_RING_IN chạm/chia sẻ hành lang ở nam đảo',
    minD < 0.5, `khoảng cách nhỏ nhất giữa 2 tuyến = ${minD.toFixed(2)} — xe 2 tuyến có thể gặp nhau tại 1 điểm mà logic giãn cách (theo cùng rt) không xử lý`);
}

// -------------------------------------------------------------- REPORT
const fails = results.filter(r => !r.ok);
console.log(`\nv52_traffic_harness: ${results.length - fails.length}/${results.length} PASS` + (fails.length ? ` — HỎNG: ${fails.map(f => f.id).join(', ')}` : ''));
process.exit(fails.length ? 1 : 0);
