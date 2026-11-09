#!/usr/bin/env python3
# BLENDER-DEEP-2 mục 18 (tham khảo reel Phúc Trần — học NGUYÊN TẮC thiết kế
# đường xá/không khí/âm thanh phố Việt Nam ban đêm, KHÔNG sao chép pixel/asset):
# 18A mặt tiền có nghề có biển + cửa cuốn theo giờ + bốt giữ xe + dây điện nối dài
# 18B phố phụ thưa người sau 22:00 (trục chợ đêm vẫn đông sáng)
# 18C loa chợ (falloff như mục 8) + bước chân theo mặt đường + côn trùng đêm khuya
import sys
P = 'index.html'
s = open(P, encoding='utf-8').read()
orig = len(s.encode('utf-8'))

def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    assert c == n, f'{tag}: tim thay {c} (can {n}) :: {old[:70]!r}'
    s = s.replace(old, new)
    print('OK', tag)

JS = r"""
{ // BLENDER-DEEP-2 (mục 18): PHỐ VIỆT NAM BAN ĐÊM — học nguyên tắc từ reel tham khảo (đường xá cụ thể / tương phản sáng / loa + bước chân), giữ nguyên chibi 3D
  // ---------- 18A: cửa cuốn mặt tiền phố theo giờ (nối mục 10) ----------
  const SHOP_SHUTTERS = [];
  const SH_TOWNS = [
    [-62, -25.55], [-52, -25.55], [-42, -25.55], [-80, -25.55], [-96, -25.55], [-112, -25.55], [-126, -25.55], // dãy bắc (mặt tiền z -25.7)
    [-60.5, 32.55], [-53, 32.55], [-38.5, 32.55], [-80, 32.55], [-95, 32.55], [-110, 32.55], [-124, 32.55]  // dãy nam (mặt tiền z 32.7)
  ];
  for(const [tx, tz] of SH_TOWNS){
    const by = groundH(tx, tz < 0 ? -28.5 : 35.5);
    const sh = box(4.8, 2.5, 0.1, 0x707880, tx, by + 1.25, tz, worldGroup, false);
    sh.visible = false; SHOP_SHUTTERS.push(sh);
  }
  const _hallTickF = hallTick; // bọc tiếp sau bọc của tiệm lớn (mục 13)
  hallTick = function(){
    _hallTickF();
    const h = gameHour(); const closed = (h >= 18.8 || h < 6);
    SHOP_SHUTTERS.forEach((m, i) => { m.visible = closed && (i % 4 !== 3); }); // 3/4 mặt tiền cuốn hạ ban đêm, 1/4 (tạp hóa khuya) còn mở — đúng hình ảnh reel
  };
  // ---------- 18A: biển DỌC có nghề dọc phố (đọc được khi đi dọc đường) ----------
  function vSign(x, z, txt, bg){
    const by = groundH(x, z < 0 ? -28.5 : 35.5);
    box(0.08, 2.6, 0.08, 0x4a4038, x, by + 1.3, z, worldGroup, false);
    const sg = signMesh(txt, 2.3, 0.55, bg, '#ffe9b0');
    sg.position.set(x, by + 2.75, z); sg.rotation.y = Math.PI / 2; worldGroup.add(sg);
  }
  vSign(-96, -25.3, 'NHÀ THUỐC', '#1f6b3a');
  vSign(-62, -25.3, 'HỚT TÓC', '#35507a');
  vSign(-126, -25.3, 'GIỮ XE', '#c8372d');
  vSign(-105, 32.3, 'TẠP HÓA', '#8c5a2e');
  vSign(-70, 32.3, 'SỬA XE', '#5d2f24');
  vSign(-140, 32.3, 'QUÁN NƯỚC', '#2e6da4');
  // ---------- 18A: bốt giữ xe ở điểm giữ xe (gần cổng, phía Hoa Sữa) ----------
  {
    const bx = -118, bz = 24.5, by = groundH(bx, bz);
    box(1.7, 2.2, 1.7, 0xd8c8ae, bx, by + 1.1, bz, worldGroup, false);
    box(2.1, 0.14, 2.1, 0x9c4034, bx, by + 2.3, bz, worldGroup, false);
    box(0.9, 1.0, 0.06, 0xa8cfe0, bx, by + 1.25, bz - 0.86, worldGroup, false); // cửa kính bốt nhìn ra đường
    const sg = signMesh('GIỮ XE', 2.2, 0.6, '#c8372d', '#ffe9b0', '5K / LƯỢT');
    sg.position.set(bx, by + 2.75, bz - 0.4); sg.rotation.y = Math.PI; worldGroup.add(sg);
    solid(bx, bz, 0.95, 0.95);
    colonialLamp(-115.5, 22.3, true); // đèn chốt giữ xe — vũng sáng ấm ban đêm (lampGlows tự sáng về đêm)
  }
  // ---------- 18A: dây điện nối dài dọc phố bắc về phía cổng (cột sẵn có ở -72/-58/-44) ----------
  {
    const tops = [];
    for(const px of [-160, -132, -104]){
      const y = entryRampY(px);
      cyl(0.09, 0.12, 7.6, 0x4a4640, px, y + 3.8, -8.6, worldGroup, 8);
      box(1.7, 0.09, 0.09, 0x4a4640, px, y + 7.05, -8.6, worldGroup, false);
      tops.push([px, y + 7.05]);
    }
    tops.push([-72, entryRampY(-72) + 7.05]);
    for(let k = 0; k + 1 < tops.length; k++){
      const [x0, y0] = tops[k], [x1, y1] = tops[k + 1];
      for(let sg2 = 0; sg2 < 5; sg2++){
        const t0 = sg2 / 5, t1 = (sg2 + 1) / 5;
        const ax = x0 + (x1 - x0) * t0, bx2 = x0 + (x1 - x0) * t1;
        const ay = y0 + (y1 - y0) * t0 - Math.sin(t0 * Math.PI) * 0.55;
        const byy = y0 + (y1 - y0) * t1 - Math.sin(t1 * Math.PI) * 0.55;
        const len = Math.hypot(bx2 - ax, byy - ay);
        const w = box(len, 0.035, 0.035, 0x1c1a18, (ax + bx2) / 2, (ay + byy) / 2, -8.6, worldGroup, false);
        w.rotation.z = Math.atan2(byy - ay, bx2 - ax);
      }
    }
  }
  // ---------- 18B: sau 22:00 phố PHỤ thưa người thêm (trục chợ đêm giữ nguyên) ----------
  const _ucdF = updateCrowdDensity;
  updateCrowdDensity = function(){
    _ucdF();
    const h = gameHour(); if(!(h >= 22 || h < 5)) return;
    const side = (x, z) => (z > 34 || z < -26 || x < -150);
    for(const st of statics){ if(st.g && side(st.g.position.x, st.g.position.z) && st.rank < 0.35) st.g.visible = false; }
    for(const w of wanderers){ if(w.g && side(w.g.position.x, w.g.position.z) && w.rank < 0.35) w.g.visible = false; }
  };
  // ---------- 18C: LOA CHỢ ở cổng chào (-131) — falloff như mục 8, nghe khắp map nhỏ dần ----------
  const LOA_POS = { x: -131, z: 2 };
  function loaGainAt(x, z){ const d = Math.hypot(x - LOA_POS.x, z - LOA_POS.z); return 0.04 + 0.85 * spatFall(d, 8, 170); }
  function loaFreqAt(x, z){ return 500 + 2400 * Math.pow(loaGainAt(x, z), 1.3); }
  const LOA_TEXTS = [
    '📢 Loa chợ: Chợ đêm Âm Phủ mở tới khuya — mời bà con giữ gìn vệ sinh chung nghen!',
    '📢 Loa chợ: Ai nhặt được chùm chìa khóa, xin mang tới bốt giữ xe ở cổng chợ.',
    '📢 Loa chợ: Nhắc nhẹ — 22 giờ nhà lồng đóng cửa, bà con tranh thủ mua đặc sản nghen!',
    '📢 Loa chợ: Chúc bà con một buổi tối đi chợ vui vẻ, ấm áp giữa sương Đà Lạt!',
    '📢 Loa chợ: Xe ôm, taxi đậu đúng điểm đón ở bùng binh đầu chợ, tránh ùn tắc nghen!'
  ];
  let loaIdx = 0, loaTimer = 45; // phát lần đầu sau ~45s, rồi mỗi ~80-110s
  function playLoa(){
    const g = loaGainAt(playerState.x, playerState.z);
    if(g > 0.15) toast(LOA_TEXTS[loaIdx % LOA_TEXTS.length]);
    loaIdx++;
    if(!actx || state.muted) return;
    try {
      const t0 = actx.currentTime + 0.03;
      const bp = actx.createBiquadFilter(); bp.type = 'bandpass'; bp.frequency.value = loaFreqAt(playerState.x, playerState.z); bp.Q.value = 0.9;
      const gn = actx.createGain(); gn.gain.value = 0;
      const dl = actx.createDelay(0.5); dl.delayTime.value = 0.16;
      const fb = actx.createGain(); fb.gain.value = 0.22;
      bp.connect(gn); gn.connect(masterGain || actx.destination); gn.connect(dl); dl.connect(fb); fb.connect(dl); dl.connect(masterGain || actx.destination);
      gn.gain.setValueAtTime(0.0001, t0);
      gn.gain.exponentialRampToValueAtTime(0.16 * g + 0.001, t0 + 0.15);
      gn.gain.setValueAtTime(0.16 * g + 0.001, t0 + 2.1);
      gn.gain.exponentialRampToValueAtTime(0.0001, t0 + 2.5);
      const osc = actx.createOscillator(); osc.type = 'sawtooth';
      let tt = t0, f = 150;
      while(tt < t0 + 2.2){ f = 130 + Math.random() * 110; osc.frequency.setValueAtTime(f, tt); tt += 0.08 + Math.random() * 0.07; } // nhịp "giọng nói" qua bandpass = tiế́ng loa
      osc.connect(bp); osc.start(t0); osc.stop(t0 + 2.6);
    } catch(e) {}
  }
  // ---------- 18C: BƯỚC CHÂN theo mặt đường + côn trùng đêm khuya ----------
  function surfaceAt(x, z){
    if(x >= -34 && x <= 34 && z >= 12 && z <= 28) return 'san';       // sàn nhà lồng
    if(x >= -11 && x <= 11 && z > -30 && z <= -2) return 'thang';     // bậc tam cấp
    if(x >= 14.5 && x <= 20.5 && z >= -30 && z <= 9) return 'thang';  // deck dốc trên cao
    if(x < -52 && Math.abs(groundH(x, z) - entryRampY(x)) > 0.05) return 'gach'; // vỉa hè/thềm cao hơn mặt đường
    if(z >= -2 && x > -34) return 'gach';                             // sân chợ lát gạch
    return 'nhua';
  }
  const STEP_FREQ = { nhua: 240, gach: 950, thang: 520, san: 680 };
  let stepAcc = 0, lastPX = player.position.x, lastPZ = player.position.z, stepCount = 0, lastStepSurface = '';
  function playStep(surf){
    stepCount++; lastStepSurface = surf;
    if(!actx || state.muted) return;
    try {
      const src = actx.createBufferSource(); src.buffer = ambNoiseBuf(actx);
      const f = actx.createBiquadFilter(); f.type = 'bandpass'; f.frequency.value = STEP_FREQ[surf] || 400; f.Q.value = 1.1;
      const g = actx.createGain(); const t0 = actx.currentTime;
      g.gain.setValueAtTime(0.055, t0); g.gain.exponentialRampToValueAtTime(0.0001, t0 + 0.075);
      src.connect(f); f.connect(g); g.connect(masterGain || actx.destination);
      src.start(t0, Math.random() * 1.5, 0.09); src.stop(t0 + 0.1);
    } catch(e) {}
  }
  let insectT = 0;
  const _tickWaterF = tickWater; // bọc tiếp sau bọc chế độ chơi (mục 15-17)
  tickWater = function(t){
    _tickWaterF(t);
    const dtF = Math.min(0.1, Math.max(0, t - (tickWater._lt || t))); tickWater._lt = t;
    // bước chân: cộng quãng đường người chơi đã đi
    const dx = player.position.x - lastPX, dz = player.position.z - lastPZ;
    const dd = Math.hypot(dx, dz);
    if(dd < 3){ stepAcc += dd; if(stepAcc > 2.1){ stepAcc = 0; playStep(surfaceAt(player.position.x, player.position.z)); } }
    lastPX = player.position.x; lastPZ = player.position.z;
    // loa chợ theo đồng hồ tích lũy
    loaTimer -= dtF;
    if(loaTimer <= 0){ loaTimer = 80 + Math.random() * 30; playLoa(); }
    // côn trùng đêm khuya: rất nhỏ, thỉnh thoảng
    const h = gameHour();
    if(actx && !state.muted && (h >= 21.5 || h < 5)){
      insectT -= dtF;
      if(insectT <= 0){ insectT = 5 + Math.random() * 6;
        try { const o = actx.createOscillator(); o.type = 'sine'; o.frequency.setValueAtTime(4300, actx.currentTime); o.frequency.exponentialRampToValueAtTime(4050, actx.currentTime + 0.09);
          const g = actx.createGain(); g.gain.setValueAtTime(0.012, actx.currentTime); g.gain.exponentialRampToValueAtTime(0.0001, actx.currentTime + 0.1);
          o.connect(g); g.connect(masterGain || actx.destination); o.start(); o.stop(actx.currentTime + 0.11); } catch(e) {}
      }
    }
  };
  window.__BD2_STREET = { shutters: SHOP_SHUTTERS, surfaceAt, loaGainAt, loaFreqAt, playLoa,
    stepCount: () => stepCount, lastSurface: () => lastStepSurface, playStep };
}
"""
rep("animate();\nsetTimeout(() => toast('👋 Chào mừng",
    JS + "\nanimate();\nsetTimeout(() => toast('👋 Chào mừng",
    tag='js muc 18 block')

open(P, 'w', encoding='utf-8').write(s)
print('PATCH F DONE, bytes =', len(s.encode('utf-8')), '(delta %+d)' % (len(s.encode('utf-8')) - orig))
