# -*- coding: utf-8 -*-
"""BLENDER-DEEP-2 patch C: mục 10 (chu kỳ nhà lồng ngày/đêm) + mục 11 (sương theo giờ) + đồng bộ harness."""
P = '/home/hatch/workspace/cho-hoa-binh-3d/prototype-v2/index.html'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    assert c == n, f'[{tag}] tim thay {c} (can {n}): {old[:80]!r}'
    s = s.replace(old, new)
    print('OK', tag)

# ---------- dong ho game chay + sương theo giờ ----------
rep("function gameHour(){ return isNight ? 19.25 : 9.5; } // V4.2: giờ game theo chế độ",
    "let gameHourF = 19.0; // BLENDER-DEEP-2 (mục 10): đồng hồ game CHẢY (1 giờ game = 60 giây thật), mặc định 19:00 chợ đêm\n"
    "function gameHour(){ return gameHourF; }\n"
    "function fogHourBonus(){ const h = gameHourF; if(h >= 5 && h < 9) return 0.005 * Math.sin((h - 5) / 4 * Math.PI); if(h >= 21 || h < 4) return 0.006; if(h >= 19) return 0.0025; return 0; } // BLENDER-DEEP-2 (mục 11): sương dày sáng sớm + sau 21h, ngày tan", tag='clock')
rep("  scene.fog.density = fogBase + Math.max(0, 15.5 - curTemp) * 0.0008; // V5.4",
    "  scene.fog.density = fogBase + Math.max(0, 15.5 - curTemp) * 0.0008 + fogHourBonus(); // BLENDER-DEEP-2 (mục 11): + sương theo giờ (tối đa ~0.016 khuya lạnh — tầm nhìn 25u còn ~85%)", tag='fog tick')

# ---------- cua cuon cho sap trong nha long (buildStall) ----------
rep("  solid(def.x, def.z, 1.9, 1.25, !!def.nightOnly);",
    "  let shutter = null; // BLENDER-DEEP-2 (mục 10): sạp TRONG nhà lồng có cửa cuốn — đóng theo giờ thật của chợ (research/23)\n"
    "  if(def.x >= -34 && def.x <= 34 && def.z >= 12 && def.z <= 28){ shutter = box(4.5, 2.3, 0.09, 0x707880, 0, 2.5, 1.08, g, false); shutter.visible = false; }\n"
    "  solid(def.x, def.z, 1.9, 1.25, !!def.nightOnly);", tag='stall shutter')
rep("    bigLanternMat: chotFx.bigLanternMat, pourStream: chotFx.pourStream, hasQueue:false,",
    "    bigLanternMat: chotFx.bigLanternMat, pourStream: chotFx.pourStream, hasQueue:false, shutter, closed:false,", tag='stall obj')

# ---------- quay trang tri trong nha long: cua cuon + thu thap ----------
rep("const INDOOR_COUNTERS", "const INDOOR_COUNTERS", n=0, tag='noop') if False else None
anchor = "{ // V4.5: lưới quầy nhà lồng"
assert anchor in s
s = s.replace(anchor, "const INDOOR_COUNTERS = { shutters: [], people: [] }; // BLENDER-DEEP-2 (mục 10): quầy + khách trong nhà lồng (đóng theo giờ)\n" + anchor, 1)
print('OK INDOOR_COUNTERS def')
rep("    const sg = signMesh('QUẦY SỐ ' + qn, 3.6, 0.95, '#f3e3c2', '#b02020', CATS[qn % CATS.length]);\n    sg.position.set(0, 2.55, 0.62); g.add(sg);\n  }",
    "    const sg = signMesh('QUẦY SỐ ' + qn, 3.6, 0.95, '#f3e3c2', '#b02020', CATS[qn % CATS.length]);\n    sg.position.set(0, 2.55, 0.62); g.add(sg);\n"
    "    const shu = box(4.4, 2.05, 0.08, 0x707880, 0, 2.42, 0.98, g, false); shu.visible = false; INDOOR_COUNTERS.shutters.push(shu); // BLENDER-DEEP-2: cửa cuốn quầy\n  }", tag='counter shutter')
rep("    const p = crowdPerson(0.45);\n    p.position.set(r.x + (qn2 % 3 - 1) * 0.9, 0.5, r.z + r.f * 1.8);\n    p.rotation.y = r.f > 0 ? Math.PI : 0;\n    addStatic(p, 'all', 'stand');",
    "    const p = crowdPerson(0.45);\n    p.position.set(r.x + (qn2 % 3 - 1) * 0.9, 0.5, r.z + r.f * 1.8);\n    p.rotation.y = r.f > 0 ? Math.PI : 0;\n"
    "    const _cst = addStatic(p, 'all', 'stand'); _cst.hallSched = 'all'; INDOOR_COUNTERS.people.push(_cst); // BLENDER-DEEP-2: khách trong nhà lồng — về khi đóng cửa", tag='counter people')

# ---------- hang cho sap trong nha long ----------
rep("const QUEUES = [ // V4.7: hàng chờ dày hơn (34 -> 49 người)",
    "const QUEUE_STATICS = {}; // BLENDER-DEEP-2 (mục 10): hàng chờ theo sạp — sạp trong nhà đóng thì hàng chờ tan\nconst QUEUES = [ // V4.7: hàng chờ dày hơn (34 -> 49 người)", tag='queue statics def')
rep("    addStatic(p, s.nightOnly ? 'night' : 'all', 'queue');",
    "    const _qst = addStatic(p, s.nightOnly ? 'night' : 'all', 'queue'); _qst.hallSched = _qst.sched;\n"
    "    if(s.x >= -34 && s.x <= 34 && s.z >= 12 && s.z <= 28){ (QUEUE_STATICS[s.id] = QUEUE_STATICS[s.id] || []).push(_qst); } // BLENDER-DEEP-2: hàng chờ sạp trong nhà", tag='queue capture')

# ---------- may trang thai nha long ----------
HALL = r'''
// ================= BLENDER-DEEP-2 (mục 10): CHU KỲ NHÀ LỒNG THEO GIỜ THẬT (research/23) =================
// Nhà lồng Chợ Đà Lạt KHÔNG bán tối: quầy trong nhà đóng ~18:30–19:00; khu đặc sản mở tới 22:00.
// Ngoài trời (chợ đêm Âm Phủ) là trung tâm mua bán ban đêm — sạp ngoài trời không bị máy này chạm.
const HALL_LATE_IDS = new Set(['dacsan', 'tra']); // khu đặc sản trong nhà — mở tới 22:00
let hallPhase = '', hallP = 0;
function hallPhaseAt(h){
  if(h >= 6.5 && h < 18.5) return ['open', 0];
  if(h >= 18.5 && h < 19) return ['closing', (h - 18.5) * 2];
  if(h >= 19 && h < 22) return ['night', 1];
  if(h >= 22 || h < 6) return ['late', 1];
  return ['opening', 1 - (h - 6) * 2];
}
function applyHallState(){
  const [phase, p] = hallPhaseAt(gameHourF);
  hallPhase = phase; hallP = p;
  for(const st of stalls){
    if(!(st.x >= -34 && st.x <= 34 && st.z >= 12 && st.z <= 28)) continue;
    const cp = HALL_LATE_IDS.has(st.id) ? (phase === 'late' ? 1 : 0) : p;
    st.closed = cp > 0.5;
    if(st.shutter){ st.shutter.visible = cp > 0.02; st.shutter.position.y = 2.5 - cp * 1.18; }
    if(st.vendor) st.vendor.visible = cp < 0.5;
    const qs = QUEUE_STATICS[st.id];
    if(qs) for(const q of qs) q.sched = st.closed ? 'day' : q.hallSched;
  }
  for(const shu of INDOOR_COUNTERS.shutters){ shu.visible = p > 0.02; shu.position.y = 2.42 - p * 1.14; }
  for(const pe of INDOOR_COUNTERS.people) pe.sched = p > 0.5 ? 'day' : pe.hallSched;
}
let hallToastPhase = '';
function hallTick(){
  applyHallState();
  if(hallPhase !== hallToastPhase){
    if(hallToastPhase !== ''){ // không báo ở nhịp đầu (vào game đã là đêm)
      if(hallPhase === 'night') toast('🌙 Nhà lồng đóng cửa — chợ đêm Âm Phủ mở đèn ngoài trời!');
      else if(hallPhase === 'late') toast('🌃 Khu đặc sản trong nhà lồng cũng đóng — chợ đêm còn ngoài đường nhé!');
      else if(hallPhase === 'open') toast('🌅 Nhà lồng mở cửa — 40 quầy trong nhà bán lại rồi!');
      else if(hallPhase === 'closing') toast('🔔 Nhà lồng sắp đóng cửa — tiểu thương trong nhà đang sập quầy…');
    }
    hallToastPhase = hallPhase;
  }
}
'''
anchor2 = "const FORTUNE_PT = { x:2.8, z:-19.2 };"
assert anchor2 in s
s = s.replace(anchor2, HALL + "\n" + anchor2, 1)
print('OK hall machine')

# ---------- chan tuong tac sap da dong ----------
rep("    if(s.nightOnly && !isNight) continue;\n    const d = Math.hypot(playerState.x - s.front.x, playerState.z - s.front.z);",
    "    if(s.nightOnly && !isNight) continue;\n    if(s.closed) continue; // BLENDER-DEEP-2 (mục 10): quầy trong nhà đã đóng — không tương tác mua bán\n    const d = Math.hypot(playerState.x - s.front.x, playerState.z - s.front.z);", tag='nearest closed')
rep("function openMenu(stall){\n  if(!stall) return;",
    "function openMenu(stall){\n  if(!stall) return;\n  if(stall.closed){ toast('🚪 Quầy đã đóng cửa — nhà lồng nghỉ buổi tối, ra chợ đêm Âm Phủ ngoài trời nhé!'); return; } // BLENDER-DEEP-2 (mục 10)", tag='openMenu guard')
rep("      s.bulb.haloMat.opacity = isNight ? (0.5 + 0.16 * (0.5 + 0.5 * Math.sin(s.bulb.ph * 3.7))) + 0.06 * Math.sin(t * 6.3 + s.bulb.ph) * Math.sin(t * 2.9 + s.bulb.ph * 1.7) : 0;",
    "      s.bulb.haloMat.opacity = s.closed ? 0 : (isNight ? (0.5 + 0.16 * (0.5 + 0.5 * Math.sin(s.bulb.ph * 3.7))) + 0.06 * Math.sin(t * 6.3 + s.bulb.ph) * Math.sin(t * 2.9 + s.bulb.ph * 1.7) : 0); // BLENDER-DEEP-2: quầy đóng = tắt đèn", tag='bulb closed')

# ---------- nut ngay/dem + khoi tao + animate ----------
rep("document.getElementById('btnDayNight').addEventListener('click', () => {\n  isNight = !isNight; applyDayNight();",
    "document.getElementById('btnDayNight').addEventListener('click', () => {\n  isNight = !isNight; gameHourF = isNight ? 19.0 : 9.5; applyDayNight(); applyHallState(); // BLENDER-DEEP-2: nút nhảy đồng hồ tới 19:00 / 9:30", tag='btn clock')
rep("{ // V4.2: MẶC ĐỊNH LÀ CHỢ ĐÊM (giờ game ~19:00) — linh hồn của chợ là chợ đêm.\n  isNight = true;\n  applyDayNight();\n}",
    "{ // V4.2: MẶC ĐỊNH LÀ CHỢ ĐÊM (giờ game ~19:00) — linh hồn của chợ là chợ đêm.\n  isNight = true;\n  applyDayNight();\n  applyHallState(); // BLENDER-DEEP-2: spawn 19:00 = nhà lồng đã đóng, chợ đêm ngoài trời mở (đúng thật)\n}", tag='init hall')
rep("  crowdTimer += dt;\n  if(crowdTimer >= 1){ crowdTimer = 0; updateCrowdDensity(); }",
    "  crowdTimer += dt;\n  if(crowdTimer >= 1){ crowdTimer = 0; updateCrowdDensity(); }\n"
    "  // BLENDER-DEEP-2 (mục 10): đồng hồ chảy + tự chuyển ngày/đêm + máy nhà lồng\n"
    "  gameHourF = (gameHourF + dt / 60) % 24;\n"
    "  const wantNight = gameHourF >= 17.6 || gameHourF < 5.6;\n"
    "  if(wantNight !== isNight){ isNight = wantNight; applyDayNight(); }\n"
    "  hallTick();", tag='animate clock')

open(P, 'w', encoding='utf-8').write(s)
print('PATCH C DONE, bytes =', len(s.encode('utf-8')))

# ---------- dong bo harness STALLS ----------
H = '/home/hatch/workspace/cho-hoa-binh-3d/prototype-v2/scripts/v52_traffic_harness.mjs'
h = open(H, encoding='utf-8').read()
for old, new in [("['banhtrang',-36,26,Math.PI]", "['banhtrang',-36,30,Math.PI]"),
                 ("['banhuot',-56,26,Math.PI]", "['banhuot',-56,30,Math.PI]"),
                 ("['suatuoi',-49.5,26,Math.PI]", "['suatuoi',-49.5,30,Math.PI]"),
                 ("['banhflan',-95,26,Math.PI]", "['banhflan',-95,30,Math.PI]"),
                 ("['banhmi',-56,-15.7,0]", "['banhmi',-56,-19.7,0]"),
                 ("['hutieu',-51,-15.7,0]", "['hutieu',-51,-19.7,0]"),
                 ("['traicay',-46,-15.7,0]", "['traicay',-46,-19.7,0]"),
                 ("['dauhu',-41,-15.7,0]", "['dauhu',-41,-19.7,0]"),
                 ("['chao',-37,-15.7,0]", "['chao',-37,-19.7,0]"),
                 ("['haisan',-100,-15.7,0]", "['haisan',-100,-19.7,0]")]:
    assert h.count(old) == 1, f'harness: {old}'
    h = h.replace(old, new)
open(H, 'w', encoding='utf-8').write(h)
print('HARNESS SYNC DONE')
