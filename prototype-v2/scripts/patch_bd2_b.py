# -*- coding: utf-8 -*-
"""BLENDER-DEEP-2 patch B: mục 8 (âm theo khoảng cách) + mục 9 (coi bói 3 kiểu)."""
P = '/home/hatch/workspace/cho-hoa-binh-3d/prototype-v2/index.html'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    assert c == n, f'[{tag}] tim thay {c} (can {n}): {old[:80]!r}'
    s = s.replace(old, new)
    print('OK', tag)

# ================= MUC 8: AM THEO KHOANG CACH =================
rep("let ambNodes = null, ambLastT = 0, bikeCool = 0;",
    "let ambNodes = null, ambLastT = 0, bikeCool = 0;\nconst ambFilts = {}; // BLENDER-DEEP-2 (mục 8): filter từng lớp để chỉnh theo khoảng cách\nlet stageBus = null; // BLENDER-DEEP-2 (mục 8): bus riêng cho nhạc góc hát (gain + lowpass theo khoảng cách)", tag='amb decl')
rep("function ambLayer(ac, type, freq, q){ const src = ac.createBufferSource(); src.buffer = ambNoiseBuf(ac); src.loop = true; const f = ac.createBiquadFilter(); f.type = type; f.frequency.value = freq; f.Q.value = q; const g = ac.createGain(); g.gain.value = 0; src.connect(f); f.connect(g); g.connect(masterGain); src.start(); return g; }",
    "function ambLayer(ac, type, freq, q, key){ const src = ac.createBufferSource(); src.buffer = ambNoiseBuf(ac); src.loop = true; const f = ac.createBiquadFilter(); f.type = type; f.frequency.value = freq; f.Q.value = q; const g = ac.createGain(); g.gain.value = 0; src.connect(f); f.connect(g); g.connect(masterGain); src.start(); if(key) ambFilts[key] = f; return g; }\n"
    "function spatFall(d, near, far){ if(d <= near) return 1; if(d >= far) return 0; const t = (d - near) / (far - near); return 1 - t * t * (3 - 2 * t); } // BLENDER-DEEP-2 (mục 8): falloff trơn\n"
    "function ambSpatial(){\n"
    "  const px = playerState.x, pz = playerState.z;\n"
    "  const dStage = Math.hypot(px - 31, pz + 52);\n"
    "  const dFnt = Math.hypot(px - 27, pz - 5.2);\n"
    "  let dFood = 1e9; for(const a of [[-41,-19.7],[-95,-19.7],[-150,-19.7],[-56,30],[-110,30],[-21,11],[22,11],[6,-15]]) dFood = Math.min(dFood, Math.hypot(px - a[0], pz - a[1]));\n"
    "  const dHall = Math.hypot(px, pz - 20);\n"
    "  return {\n"
    "    stage: { g: spatFall(dStage, 5, 75), f: 500 + 8500 * Math.pow(spatFall(dStage, 5, 75), 1.5), d: dStage },\n"
    "    fnt: { g: spatFall(dFnt, 2, 30), f: 700 + 1600 * spatFall(dFnt, 2, 30), d: dFnt },\n"
    "    food: { g: spatFall(dFood, 2, 26), f: 900 + 5600 * spatFall(dFood, 2, 26), d: dFood },\n"
    "    hall: { g: spatFall(dHall, 4, 42), d: dHall }\n"
    "  };\n"
    "}\n"
    "function ensureStageBus(){ if(!actx) return null; if(!stageBus){ const f = actx.createBiquadFilter(); f.type = 'lowpass'; f.frequency.value = 9000; const g = actx.createGain(); g.gain.value = 0; f.connect(g); g.connect(masterGain || actx.destination); stageBus = { f, g }; } return stageBus; }\n"
    "function updateStageBus(sp){ const sb = ensureStageBus(); if(!sb) return; const on = (typeof listening !== 'undefined' && listening) || (typeof melodyTimer !== 'undefined' && !!melodyTimer); const tg = on ? 0.9 * (0.06 + 0.94 * sp.stage.g) : 0; sb.g.gain.setTargetAtTime(tg, actx.currentTime, 0.4); sb.f.frequency.setTargetAtTime(sp.stage.f, actx.currentTime, 0.4); }", tag='ambLayer+spatial')
rep("    mur: ambLayer(ac, 'bandpass', 500, 0.6),   // rì rầm 250–800Hz\n    low: ambLayer(ac, 'lowpass', 160, 0.5),    // trầm <250Hz — thân đám đông + động cơ xa\n    siz: ambLayer(ac, 'highpass', 4200, 0.7),  // xì xèo 2,5–6kHz — chỉ gần sạp ăn\n    wat: ambLayer(ac, 'bandpass', 1100, 0.8),  // nước đài phun\n    wnd: ambLayer(ac, 'lowpass', 280, 0.4)     // gió chỗ cao/vắng",
    "    mur: ambLayer(ac, 'bandpass', 500, 0.6, 'mur'),   // rì rầm 250–800Hz\n    low: ambLayer(ac, 'lowpass', 160, 0.5, 'low'),    // trầm <250Hz — thân đám đông + động cơ xa\n    siz: ambLayer(ac, 'highpass', 4200, 0.7, 'siz'),  // xì xèo 2,5–6kHz — chỉ gần sạp ăn\n    wat: ambLayer(ac, 'bandpass', 1100, 0.8, 'wat'),  // nước đài phun\n    wnd: ambLayer(ac, 'lowpass', 280, 0.4, 'wnd')     // gió chỗ cao/vắng", tag='amb keys')
rep("else if(x >= -200 && x <= 43 && z >= -20 && z <= 29){ m = 1; l = 0.5; g = 0.1; if(Math.abs(z + 15.7) < 5 || Math.abs(z - 26) < 5) s = 1; } // GEOMETRY-2: phố ăn phủ toàn trục kéo dài, xì xèo theo 2 hàng sạp mới (-15.7 / 26)",
    "else if(x >= -200 && x <= 43 && z >= -24 && z <= 34){ m = 1; l = 0.5; g = 0.1; if(Math.abs(z + 19.7) < 5 || Math.abs(z - 30) < 5) s = 1; } // BLENDER-DEEP-2: phố ăn theo 2 hàng sạp mới (-19.7 / 30)", tag='ambzone bands')
rep("  ambNodes.wnd.gain.setTargetAtTime(z.g, ac.currentTime, 0.6);",
    "  ambNodes.wnd.gain.setTargetAtTime(z.g, ac.currentTime, 0.6);\n"
    "  // BLENDER-DEEP-2 (mục 8): nhân hệ số khoảng cách thật + lọc theo khoảng cách cho nguồn điểm\n"
    "  const sp = ambSpatial();\n"
    "  ambNodes.wat.gain.setTargetAtTime(z.w * (0.25 + 0.75 * sp.fnt.g), ac.currentTime, 0.6);\n"
    "  if(ambFilts.wat) ambFilts.wat.frequency.setTargetAtTime(sp.fnt.f, ac.currentTime, 0.6);\n"
    "  ambNodes.siz.gain.setTargetAtTime(z.s * (0.15 + 0.85 * sp.food.g), ac.currentTime, 0.6);\n"
    "  if(ambFilts.siz) ambFilts.siz.frequency.setTargetAtTime(sp.food.f, ac.currentTime, 0.6);\n"
    "  ambNodes.mur.gain.setTargetAtTime(z.m * (0.7 + 0.3 * sp.hall.g), ac.currentTime, 0.6);\n"
    "  updateStageBus(sp);", tag='tick spatial')
rep("  o.connect(g); g.connect(masterGain || actx.destination);\n  o.start(); o.stop(actx.currentTime + 0.42);",
    "  o.connect(g); g.connect(stageBus ? stageBus.f : (masterGain || actx.destination)); // BLENDER-DEEP-2 (mục 8): nốt nhạc đi qua bus góc hát (xa = nhỏ + lờ mờ)\n  o.start(); o.stop(actx.currentTime + 0.42);", tag='playNote bus')
# startMusic phai tao stageBus truoc not dau
rep("function startMusic(){\n  if(melodyTimer) return;",
    "function startMusic(){\n  if(melodyTimer) return;\n  ensureStageBus(); // BLENDER-DEEP-2 (mục 8)", tag='startMusic bus')

# ================= MUC 9: COI BOI 3 KIEU =================
rep("  #fortuneResult { margin:10px 0; }",
    "  #fortuneResult { margin:10px 0; }\n  .ftype.sel { outline:2px solid #ffd98a; background:#5a3a1a; }", tag='ftype css')
rep('  <div class="btnRow"><button class="bigBtn" id="btnDrawFortune">🔮 Rút quẻ — 20 Xu</button></div>',
    '  <div class="btnRow" id="fortuneTypes">\n'
    '    <button class="bigBtn ftype" data-ft="bai">🃏 Xem Bài</button>\n'
    '    <button class="bigBtn ftype" data-ft="mat">👁️ Xem Mặt</button>\n'
    '    <button class="bigBtn ftype" data-ft="tay">✋ Xem Chỉ Tay</button>\n'
    '  </div>\n'
    '  <div class="btnRow"><button class="bigBtn" id="btnDrawFortune">🔮 Gieo quẻ kiểu đã chọn — 20 Xu</button></div>', tag='fortune modal html')
rep("  document.getElementById('btnDrawFortune').disabled = state.xu < 20;\n  openModal('fortuneModal');",
    "  document.getElementById('btnDrawFortune').disabled = state.xu < 20;\n"
    "  document.querySelectorAll('.ftype').forEach(x => { x.classList.toggle('sel', x.dataset.ft === fortuneType); x.disabled = state.xu < 20; });\n"
    "  openModal('fortuneModal');", tag='openFortune types')

NEW_DRAW = r'''let fortuneType = 'bai'; // BLENDER-DEEP-2 (mục 9): 3 kiểu coi bói riêng kho — bai (bài) / mat (nhân tướng) / tay (chỉ tay)
const CARD_DECK = [ // 12 lá bài của Chú Ba — mỗi lá tên + nghĩa + điểm vận
  { n:'Lá Sữa Nóng', m:'ấm bụng, có người thương mời ăn uống', v:2 },
  { n:'Lá Thông Reo', m:'tin vui từ phương xa, việc làm hanh thông', v:3 },
  { n:'Lá Sương Mù', m:'việc chưa rõ ràng, chớ vội quyết', v:-1 },
  { n:'Lá Bánh Tráng', m:'việc khó giòn tan, cứ mạnh dạn mà làm', v:2 },
  { n:'Lá Hồng Treo', m:'phải chờ mới ngọt, kiên nhẫn là chìa khóa', v:1 },
  { n:'Lá Cẩm Tú Cầu', m:'duyên lành nở rộ, gặp người hợp ý', v:3 },
  { n:'Lá Mưa Phùn', m:'hơi trắc trở, tiền bạc dễ hao hụt nhỏ', v:-2 },
  { n:'Lá Đèn Lồng', m:'đường đi sáng rõ, quý nhân dẫn lối', v:2 },
  { n:'Lá Cà Phê Phin', m:'chậm mà chắc, giọt nào cũng đáng giá', v:1 },
  { n:'Lá Dâu Tây', m:'tình cảm ngọt ngào, có lộc ăn uống', v:2 },
  { n:'Lá Gió Đồi', m:'thay đổi bất ngờ, nên linh hoạt theo thời', v:0 },
  { n:'Lá Trăng Rằm', m:'đại cát — vận đỏ hiếm có, làm gì cũng thông', v:3 },
];
const FACE_TRAITS = [ // [nét, [[câu luận, điểm vận], ...]] — luận nhân tướng
  ['Trán', [['cao rộng, sáng sủa — trí tuệ mở mang, học hành tấn tới', 2], ['đầy đặn — phúc khí dày, được người trên thương mến', 2], ['hơi hẹp — phải tự lực cánh sinh, càng lớn càng vững vàng', 0]]],
  ['Mắt', [['sáng, lòng đen trắng phân minh — nhìn người nhìn việc đều tinh tường', 2], ['hay cười — duyên ăn nói, đi đâu cũng có bạn bè', 1], ['sâu trầm — nghĩ nhiều, việc gì cũng cân nhắc kỹ càng', 0]]],
  ['Mũi', [['thẳng, cánh mũi đầy — tài lộc giữ được, tiền vào đều đều', 2], ['cao — chí lớn, không chịu ngồi yên một chỗ', 1], ['đầu mũi tròn — hiền lành, lộc ăn uống không bao giờ thiếu', 1]]],
  ['Miệng và cằm', [['miệng cười tươi, cằm đầy — hậu vận an nhàn, con cháu đề huề', 3], ['cằm hơi nhọn — nhanh nhẹn, hợp nghề buôn bán chợ búa', 1], ['miệng mím chắc — giữ chữ tín, hứa là làm', 1]]],
];
const PALM_LINES = [ // [đường chỉ/gò, [[biến thể + luận, điểm vận], ...]]
  ['Đường Sinh Đạo', [['dài và rõ nét — sức khỏe dồi dào, càng sống càng khỏe', 2], ['hơi ngắn — phải biết giữ sức, đừng thức khuya như đi chợ đêm hoài', 0], ['đứt đoạn giữa chừng — từng có phen mệt mỏi, nhưng qua được là vận đổi chiều', 1]]],
  ['Đường Trí Đạo', [['thẳng và dài — đầu óc mạch lạc, tính toán đâu ra đó', 2], ['hơi cong xuống — giàu tưởng tượng, hợp việc làm đẹp, làm nghệ', 1], ['chia nhánh ở cuối — nhiều nghề tay trái, lộc đến từ nhiều đường', 2]]],
  ['Đường Tâm Đạo', [['cong nhẹ hướng lên — tình cảm chân thành, yêu là hết lòng', 2], ['thẳng — lý trí trong chuyện tình cảm, chọn người rất kỹ', 1], ['nhiều nhánh nhỏ — đào hoa, đi chợ cũng có người để ý đó nghen', 1]]],
  ['Gò tay', [['gò Kim Tinh đầy — sức sống mạnh, tình cảm nồng nhiệt', 1], ['gò Thái Dương nổi — có duyên với tiền bạc và may mắn bất ngờ', 2], ['gò Mộc Tinh cao — có uy, sau này làm chủ được việc lớn', 2]]],
];
const FORTUNE_ADVICE = ['Lời khuyên của chú: ghé sạp sữa đậu nành làm ly nóng trước khi quyết việc lớn nghen con.', 'Lời khuyên của chú: mua một bó hoa Đà Lạt về chưng, nhà thơm thì vận cũng thông.', 'Lời khuyên của chú: leo lên đỉnh đồi Hòa Bình ngắm chợ một vòng, đầu óc sáng ra liền.', 'Lời khuyên của chú: ăn gì nóng rồi hãy tính tiếp — bụng no thì quẻ nào cũng hóa lành.', 'Lời khuyên của chú: hôm nay nên ghé góc hát nghe một bài, tâm an thì lộc tự tới.', 'Lời khuyên của chú: giữ ấm cổ bằng cái khăn len mới, sương Đà Lạt không đùa được đâu.'];
const FORTUNE_LUCKY = ['Điểm may mắn: ly sữa nóng đầu tiên trong ngày.', 'Điểm may mắn: bậc thang thứ 9 từ dưới đếm lên.', 'Điểm may mắn: một bó cẩm tú cầu tím.', 'Điểm may mắn: chiếc đèn lồng đỏ ở sạp đầu chợ.', 'Điểm may mắn: mùi bánh tráng nướng bay ngang qua.', 'Điểm may mắn: tiếng thông reo lúc chiều xuống.'];
function fortuneFx(score){
  if(score >= 5){ giveBuff('luck', 300); gainXu(20); }
  else if(score >= 2){ giveBuff('luck', 240); }
  else if(score >= 0){ giveBuff('warm', 90); warmth = Math.min(100, warmth + 20); }
  else { giveBuff('alert', 90); }
}
function pickW(arr){ return arr[Math.floor(Math.random() * arr.length)]; }
function fortuneResultFor(type){
  let title; const lines = []; let score = 0;
  if(type === 'mat'){
    title = '👁️ Xem Mặt — Nhân Tướng';
    for(const [feat, vars] of FACE_TRAITS){ const v = pickW(vars); lines.push(feat + ' ' + v[0] + '.'); score += v[1]; }
    lines.push(score >= 6 ? 'Tổng luận: tướng này là dạng phúc hậu, càng về sau càng phát đó con.' : score >= 3 ? 'Tổng luận: vận đang lên đều, cứ chăm chỉ là tới nơi.' : 'Tổng luận: vận bình hòa — giữ sức khỏe và chữ tín là lộc tự về.');
  } else if(type === 'tay'){
    title = '✋ Xem Chỉ Tay';
    for(const [line, vars] of PALM_LINES){ const v = pickW(vars); lines.push(line + ' ' + v[0] + '.'); score += v[1]; }
    lines.push(score >= 6 ? 'Tổng luận: bàn tay này là tay có lộc, càng làm càng ra tiền đó con.' : score >= 3 ? 'Tổng luận: chỉ tay khá lành, việc đang tính cứ thế mà tiến.' : 'Tổng luận: vận bình hòa — chậm mà chắc, đừng vay mượn liều nghen.');
  } else {
    title = '🃏 Xem Bài — Rút 3 Lá';
    const pool = [...CARD_DECK]; const drawn = [];
    for(let i = 0; i < 3; i++){ const c = pool.splice(Math.floor(Math.random() * pool.length), 1)[0]; drawn.push(c); score += c.v; }
    for(const c of drawn) lines.push('• ' + c.n + ' — ' + c.m + '.');
    lines.push(score >= 5 ? 'Ba lá cùng chiều tốt: quẻ này ĐẠI CÁT đó con.' : score >= 2 ? 'Tổ hợp này khá lành: việc đang tính làm được.' : score >= 0 ? 'Tổ hợp trung bình: cứ từ từ, đừng nóng vội.' : 'Tổ hợp hơi xấu: hôm nay nên thủ hơn công, giữ tiền kỹ nghen con.');
  }
  lines.push(pickW(FORTUNE_ADVICE));
  lines.push(pickW(FORTUNE_LUCKY));
  return { t: title, x: lines.join('\n'), score };
}
const FORTUNE_RITUAL = { bai:'🃏 Chú Ba xào bộ bài cũ sờn gáy… con rút được 3 lá:', mat:'👁️ Chú Ba nheo mắt, nhìn con một lượt từ trán tới cằm, gật gù…', tay:'✋ Chú Ba cầm tay con, săm soi từng đường chỉ dưới ánh đèn vàng…' };
let fortuneTimer = null;
function drawFortune(){
  if(state.xu < 20) return;
  state.xu -= 20; state.fortuneCount++; questFlags.fortune = true; // V4.2: móc chặng 4
  gainXP(8); save(); updateHUD(); fortuneShown = true;
  const type = fortuneType;
  const rs = document.getElementById('fortuneResult'); rs.innerHTML = '';
  const rp = document.createElement('div'); rp.className = 'ftext'; rp.textContent = FORTUNE_RITUAL[type]; rs.appendChild(rp);
  document.getElementById('btnDrawFortune').disabled = true;
  if(fortuneTimer) clearTimeout(fortuneTimer);
  fortuneTimer = setTimeout(() => { // nghi thức ngắn 0,9s rồi mới ra quẻ (bỏ qua bằng cách đóng modal)
    const f = fortuneResultFor(type);
    fortuneFx(f.score);
    rs.innerHTML = '';
    const h = document.createElement('div'); h.className = 'fname'; h.textContent = '🔮 ' + f.t;
    const p = document.createElement('div'); p.className = 'ftext'; p.style.whiteSpace = 'pre-line'; p.textContent = f.x;
    rs.appendChild(h); rs.appendChild(p);
    document.getElementById('fortuneSub').textContent = 'Chú Ba gật gù: “Quẻ này ứng nghiệm lắm nghen…” • Còn ' + state.xu + ' Xu • Đã coi ' + state.fortuneCount + ' lần';
    document.getElementById('btnDrawFortune').disabled = state.xu < 20;
    toast('🔮 Chú Ba: ' + f.t);
  }, 900);
}
document.querySelectorAll('.ftype').forEach(b => b.addEventListener('click', () => {
  fortuneType = b.dataset.ft;
  document.querySelectorAll('.ftype').forEach(x => x.classList.toggle('sel', x === b));
  document.getElementById('fortuneResult').innerHTML = '<i>' + FORTUNE_RITUAL[fortuneType] + ' Bấm Gieo quẻ là chú coi cho nghen.</i>';
}));'''

import re as _re
m = _re.search(r"function drawFortune\(\)\{.*?\n\}\ndocument\.getElementById\('btnDrawFortune'\)\.addEventListener\('click', drawFortune\);", s, _re.S)
assert m, 'khong tim thay khoi drawFortune cu'
s = s[:m.start()] + NEW_DRAW + "\ndocument.getElementById('btnDrawFortune').addEventListener('click', drawFortune);" + s[m.end():]
print('OK drawFortune 3 kieu')

open(P, 'w', encoding='utf-8').write(s)
print('PATCH B DONE, bytes =', len(s.encode('utf-8')))
