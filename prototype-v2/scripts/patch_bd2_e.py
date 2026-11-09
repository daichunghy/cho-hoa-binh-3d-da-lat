#!/usr/bin/env python3
# BLENDER-DEEP-2 mục 15-17: 3 chế độ chơi Couple / Gia đình / Theo đoàn + cửa vào chế độ.
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

# --- CSS ---
CSS = """
/* BLENDER-DEEP-2 (mục 15-17): chế độ chơi */
#modePanel{ position:fixed; left:10px; top:158px; width:248px; z-index:30; padding:10px 12px; font-size:13px; }
#modePanelTitle{ font-weight:bold; color:#ffd94d; margin-bottom:6px; }
#modeTasks .tk{ margin:3px 0; color:#e8e2d4; }
#modeTasks .tk.done{ color:#9fd48a; text-decoration:line-through; }
.modeBarWrap{ height:8px; background:#3a2c1c; border-radius:4px; margin-top:8px; overflow:hidden; }
#modeBar{ height:100%; width:0%; background:linear-gradient(90deg,#c95d7e,#ffd94d); border-radius:4px; transition:width .6s ease; }
.modeCards{ display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:10px; }
.modeCard{ background:#2e2118; border:2px solid #6a5136; border-radius:12px; padding:12px; cursor:pointer; text-align:left; color:#f0ead8; font-family:inherit; }
.modeCard:hover{ border-color:#ffd94d; }
.modeCard.sel{ border-color:#ffd94d; background:#453217; }
.modeCard .ic{ font-size:30px; }
.modeCard .nm{ font-weight:bold; font-size:16px; margin:4px 0; color:#ffe9b0; }
.modeCard .ds{ font-size:12px; color:#bdb5a2; line-height:1.45; }
#photoFlash{ position:fixed; inset:0; background:#fff8ea; opacity:0; pointer-events:none; z-index:80; display:flex; align-items:center; justify-content:center; transition:opacity .5s; }
#photoFlash .fr{ border:6px solid #7a4a2e; border-radius:10px; padding:26px 44px; color:#7a2e22; font-size:26px; font-weight:bold; background:rgba(255,248,234,.92); }
"""
rep("</style>", CSS + "</style>", tag='css modes')

# --- HTML: nút HUD + panel + 2 modal + flash ---
rep('<button class="hbtn" id="btnPassport">📖 Hộ chiếu</button>',
    '<button class="hbtn" id="btnPassport">📖 Hộ chiếu</button>\n  <button class="hbtn" id="btnMode">🎭 Chế độ</button>',
    tag='hud btn mode')
HTML = """
<div id="modePanel" class="panel" style="display:none"><div id="modePanelTitle"></div><div id="modeTasks"></div><div class="modeBarWrap"><div id="modeBar"></div></div></div>
<div id="photoFlash"><div class="fr" id="photoFlashTxt">📸 Đà Lạt</div></div>
<div class="modal" id="modeModal"><div class="sheet">
  <button class="closeX" data-close="modeModal">✕</button>
  <h2>🎭 Chọn cách đi chợ</h2><div class="sub">Đi một mình hay đi cùng ai? Mỗi cách đi có bảng việc riêng, làm đủ là có thưởng + danh hiệu trong Hộ chiếu. Đổi chế độ lúc nào cũng được (nút 🎭 Chế độ), Xu / túi đồ / hộ chiếu giữ nguyên.</div>
  <div class="modeCards">
    <button class="modeCard" id="mcSolo"><div class="ic">🚶</div><div class="nm">Đi một mình</div><div class="ds">Thong thả dạo chợ theo cách quen thuộc.<br>🎁 Tự do khám phá, không bảng việc.</div></button>
    <button class="modeCard" id="mcCouple"><div class="ic">💕</div><div class="nm">Couple</div><div class="ds">Đi cùng người thương: chụp hình, mua dâu, coi bói đôi, nghe hát, uống sữa đậu nành, mua áo đôi.<br>🎁 Đủ 100% TIM: +150 Xu + danh hiệu “Cặp đôi Hòa Bình”.</div></button>
    <button class="modeCard" id="mcFamily"><div class="ic">👨‍👩‍👧</div><div class="nm">Gia đình</div><div class="ds">Cả nhà đi chợ: Bà, Bố/Mẹ và Bé cùng theo, mỗi người một mong muốn riêng.<br>🎁 Đủ “Ấm no”: +200 Xu + danh hiệu “Gia đình”.</div></button>
    <button class="modeCard" id="mcTour"><div class="ic">🚩</div><div class="nm">Theo đoàn</div><div class="ds">Theo cờ đoàn Hòa Bình: đoàn xe đón ở bùng binh đầu chợ, check-in 6 điểm cùng hướng dẫn viên.<br>🎁 +250 Xu + Nón đoàn & Áo đoàn trong Tủ đồ.</div></button>
  </div>
  <button class="buyBtn" id="modeClose">Đóng</button>
</div></div>
<div class="modal" id="modeDoneModal"><div class="sheet">
  <button class="closeX" data-close="modeDoneModal">✕</button>
  <h2 id="modeDoneTitle">🎉</h2><div class="sub" id="modeDoneTxt"></div>
  <button class="buyBtn" id="modeDoneClose">Tuyệt vời!</button>
</div></div>
"""
rep('<div class="modal" id="passModal">', HTML + '<div class="modal" id="passModal">', tag='html modes')

# --- Hộ chiếu: gắn danh hiệu chế độ vào passSub ---
rep("+ (state.fortuneCount ? ' • 🔮 Đã coi bói ' + state.fortuneCount + ' lần với Chú Ba ở bậc thang' : '');",
    "+ (state.fortuneCount ? ' • 🔮 Đã coi bói ' + state.fortuneCount + ' lần với Chú Ba ở bậc thang' : '') + (state.modeTitles && state.modeTitles.length ? ' • 🎖 Danh hiệu: ' + state.modeTitles.join(' • ') : '');",
    tag='passport titles')

# --- WARDROBE_DEFS: áo đôi + đồ đoàn (price 0, cấp qua hoàn thành chế độ) ---
rep('const WD_SETS = {',
    """WARDROBE_DEFS.push(
  { id:'AO-DOI', name:'Áo đôi Hòa Bình', slot:'coat', warm:12, price:0, stall:null, mat:'Shirt', color:'#c95d7e', parts:[{ g:'cyl', s:[0.215,0.235,0.15], p:[0,0.909,0], c:'#c95d7e', a:'R' }] },
  { id:'NON-DOAN', name:'Nón đoàn Hòa Bình', slot:'hat', warm:5, price:0, stall:null, node:'beanie', mat:'Beanie', color:'#2e8f83', parts:[] },
  { id:'AO-DOAN', name:'Áo đoàn Hòa Bình', slot:'coat', warm:10, price:0, stall:null, mat:'Shirt', color:'#2e8f83', parts:[{ g:'cyl', s:[0.215,0.235,0.15], p:[0,0.909,0], c:'#2e8f83', a:'R' }] }
); // BLENDER-DEEP-2 (mục 16-17): đồ mở khóa bằng chế độ chơi
const WD_SETS = {""",
    tag='wardrobe mode items')

# --- JS hệ chế độ (chen truoc animate() cuoi file, SAU khoi dong bang tinh) ---
JS = r"""
{ // BLENDER-DEEP-2 (mục 15-17): 3 CHẾ ĐỘ CHƠI — Couple / Gia đình / Theo đoàn
  if(typeof state.mode !== 'string') state.mode = 'solo';
  if(typeof state.modeSeen !== 'boolean') state.modeSeen = false;
  if(!state.modeProg || typeof state.modeProg !== 'object') state.modeProg = {};
  if(!Array.isArray(state.modeTitles)) state.modeTitles = [];
  function mProg(m){ if(!state.modeProg[m] || typeof state.modeProg[m] !== 'object') state.modeProg[m] = { t:{}, done:false, cp:0 }; const p = state.modeProg[m]; if(!p.t) p.t = {}; if(typeof p.cp !== 'number') p.cp = 0; return p; }
  const companions = []; // { g, off:{x,z}, maxSp, ph, role, leader }
  let tourState = null;   // { vehicles:[], guide:{g,heading}, phase, waitT, farT }
  let modesBooted = false, lastTickT = -1, panelT = 0, heartT = 0, lastFortuneSeen = state.fortuneCount || 0;
  const heartFx = [];
  function tagSprite(txt, bg){
    const c = document.createElement('canvas'); c.width = 256; c.height = 72;
    const x = c.getContext('2d'); x.fillStyle = bg || 'rgba(46,32,20,0.85)';
    x.beginPath(); x.roundRect(6, 6, 244, 60, 16); x.fill();
    x.fillStyle = '#ffe9b0'; x.font = 'bold 34px Arial'; x.textAlign = 'center'; x.textBaseline = 'middle'; x.fillText(txt, 128, 38);
    const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: new THREE.CanvasTexture(c), transparent: true, depthWrite: false }));
    sp.scale.set(1.7, 0.48, 1); sp.position.y = 2.0; return sp;
  }
  function spawnCompanion(shirt, pants, hat, skin, hatColor, opt){
    const g = makePerson(shirt, pants, hat, skin, hatColor);
    if(opt.scale) g.scale.setScalar(opt.scale);
    if(opt.scarf){ const sc = g.getObjectByName('Scarf'); if(sc){ sc.visible = true; recolor(g, 'Scarf', opt.scarf); } }
    if(opt.tag) g.add(tagSprite(opt.tag, opt.tagBg));
    g.position.set(player.position.x + (opt.off.x || 0), player.position.y, player.position.z + (opt.off.z || 0));
    worldGroup.add(g);
    const c = { g, off: opt.off, maxSp: opt.maxSp || 7.5, ph: Math.random() * 6.28, role: opt.role || '', leader: !!opt.leader };
    companions.push(c); return c;
  }
  function clearCompanions(){
    for(const c of companions) worldGroup.remove(c.g);
    companions.length = 0;
    if(tourState){ for(const v of tourState.vehicles) worldGroup.remove(v); if(tourState.guide) worldGroup.remove(tourState.guide.g); tourState = null; }
  }
  function rotOff(f, ox, oz){ return { x: ox * Math.cos(f) + oz * Math.sin(f), z: -ox * Math.sin(f) + oz * Math.cos(f) }; }
  function moveToward(c, tx, tz, dt, t){
    const g = c.g, dx = tx - g.position.x, dz = tz - g.position.z, d = Math.hypot(dx, dz);
    if(d > 25){ g.position.x = tx; g.position.z = tz; }
    else if(d > 0.08){
      const sp = Math.min(c.maxSp, Math.max(1.2, d * 2.4));
      const st = Math.min(d, sp * dt);
      g.position.x += dx / d * st; g.position.z += dz / d * st;
      g.rotation.y = Math.atan2(dx, dz);
    }
    g.position.y = groundH(g.position.x, g.position.z) + (d > 0.35 ? Math.abs(Math.sin(t * 8 + c.ph)) * 0.045 : 0);
    return d;
  }
  // ---------- định nghĩa việc ----------
  const COUPLE_TASKS = [
    { id:'photo', name:'📸 Chụp hình chung ở bùng binh hoa' },
    { id:'dau', name:'🍓 Mua dâu tặng nhau ở quầy dâu' },
    { id:'boi', name:'🔮 Coi bói đôi với Chú Ba' },
    { id:'hat', name:'🎶 Nghe hát cùng ở quảng trường' },
    { id:'sua', name:'🥛 Uống sữa đậu nành ở Hoa Sữa' },
    { id:'aodoi', name:'🧥 Mua áo đôi ở khu quần áo' } ];
  const FAMILY_WISHES = [
    { id:'ba', who:'Bà', name:'🍵 Bà: mua trà atiso' },
    { id:'me', who:'Mẹ', name:'🍓 Mẹ: mua mứt về làm quà' },
    { id:'bo', who:'Bố', name:'🔥 Bố: ăn bánh tráng nướng' },
    { id:'be', who:'Bé', name:'🧸 Bé: mua búp bê len' },
    { id:'an', who:'Cả nhà', name:'🍽 Cả nhà ăn cùng ở phố ăn' },
    { id:'anh', who:'Cả nhà', name:'📸 Chụp hình gia đình ở đài phun' } ];
  const TOUR_CPS = [
    { x:-146, z:8, name:'Điểm tập kết đoàn xe' },
    { x:-30, z:5, name:'Bùng binh hoa' },
    { x:-20, z:18.2, name:'Nhà lồng — mua đặc sản' },
    { x:2.8, z:-19.2, name:'Bậc tam cấp' },
    { x:26.8, z:-52, name:'Quảng trường — nghe hát' },
    { x:47, z:20, name:'Tiệm lưu niệm — mua quà' } ];
  const MODE_TITLES = { couple:'Cặp đôi Hòa Bình', family:'Gia đình Hòa Bình', tour:'Đoàn viên Hòa Bình' };
  // ---------- spawn theo chế độ ----------
  function spawnForMode(m){
    clearCompanions();
    if(m === 'couple'){
      spawnCompanion(0xe8e2d4, 0x74566b, 'beanie', 0xe8b98f, 0xc95d7e, { off:{ x:1.15, z:0.15 }, maxSp:8, role:'partner', tag:'💕 Người thương', tagBg:'rgba(140,40,80,0.88)', scarf:0xc8372d });
    } else if(m === 'family'){
      spawnCompanion(0x8668c4, 0x4a4640, 'beanie', 0xc68a5e, 0x8668c4, { off:{ x:0, z:-1.7 }, maxSp:5.6, role:'ba', tag:'Bà' });
      spawnCompanion(0x35507a, 0x2e2a26, 'cap', 0xa96f42, 0x35507a, { off:{ x:-1.15, z:-2.5 }, maxSp:7.2, role:'bo', tag:'Bố' });
      spawnCompanion(0x2e6b46, 0x5c4633, 'beanie', 0xe8b98f, 0xd9a62e, { off:{ x:1.15, z:-2.5 }, maxSp:7.2, role:'me', tag:'Mẹ' });
      const be = spawnCompanion(0xe8c33c, 0x2e6da4, 'beanie', 0xe8b98f, 0xc8372d, { off:{ x:0.55, z:-0.95 }, maxSp:8.5, role:'be', tag:'Bé', scale:0.7 });
      ball(0.17, 0xc8372d, 0.38, 1.62, 0.05, be.g, 0.95); // bóng bay của Bé
      cyl(0.008, 0.008, 0.34, 0xf0ead8, 0.38, 1.42, 0.05, be.g, 4);
    } else if(m === 'tour'){
      tourState = { vehicles: [], guide: null, phase: 'drive', waitT: 0, farT: 0, flag: null };
      const busCols = [0x2e8f83, 0xd97c2e];
      for(let i = 0; i < 2; i++){
        const b = new THREE.Group();
        box(2.3, 1.5, 5.6, busCols[i], 0, 1.35, 0, b, false);
        box(2.34, 0.62, 5.0, 0xbfe0ea, 0, 1.72, 0, b, false);
        box(2.3, 0.5, 5.6, 0xf0ead8, 0, 0.55, 0, b, false);
        for(const [wx, wz] of [[-1.05, 1.9], [1.05, 1.9], [-1.05, -1.9], [1.05, -1.9]]){
          const w = cyl(0.34, 0.34, 0.18, 0x22201e, wx, 0.34, wz, b, 10); w.rotation.z = Math.PI / 2;
        }
        const sg = signMesh(i ? 'ĐOÀN HÒA BÌNH 2' : 'ĐOÀN HÒA BÌNH', 3.4, 0.6, '#f3e3c2', '#7a2e22');
        sg.position.set(0, 2.35, 0); b.add(sg);
        b.position.set(-212 - i * 9, groundH(-212 - i * 9, 14), 14); b.rotation.y = Math.PI / 2;
        worldGroup.add(b); tourState.vehicles.push(b);
      }
    }
    renderModePanel();
  }
  function spawnTourGroup(){
    const gt = makePerson(0x2e8f83, 0x3a3f4a, 'cap', 0xc68a5e, 0xc8372d);
    gt.position.set(-146, groundH(-146, 8), 8); worldGroup.add(gt);
    gt.add(tagSprite('🚩 Hướng dẫn viên', 'rgba(20,90,80,0.9)'));
    const pole = cyl(0.025, 0.025, 1.7, 0x8a6a42, 0.42, 1.9, 0, gt, 6);
    const flag = signMesh('ĐOÀN HÒA BÌNH', 1.5, 0.42, '#c8372d', '#ffe9b0');
    flag.position.set(0.42, 2.62, 0.4); gt.add(flag);
    tourState.guide = { g: gt, heading: Math.PI / 2 };
    tourState.flag = flag;
    for(let i = 0; i < 10; i++){
      const row = Math.floor(i / 2), side = i % 2 ? 0.85 : -0.85;
      spawnCompanion(0x2e8f83, 0x4a4640, 'cap', [0xd9a37e, 0xc68a5e, 0xa96f42, 0xe8b98f][i % 4], 0x2e8f83,
        { off:{ x: side, z: -1.3 - row * 1.15 }, maxSp:7.6, role:'member', leader: true });
    }
    for(const c of companions) if(c.leader){ c.g.position.set(-146 + c.off.x, groundH(-146, 8), 8 + c.off.z); }
    tourState.phase = 'walk';
    toast('🚩 Đoàn Hòa Bình đã tới điểm tập kết — đi theo cờ đoàn nhé!');
  }
  // ---------- việc: đánh dấu + hoàn thành ----------
  function modeTaskDone(mode, id, label){
    const p = mProg(mode); if(p.t[id] || p.done) return;
    p.t[id] = true; save(); renderModePanel();
    toast('✔ ' + label, 'stamp');
    checkModeComplete(mode);
  }
  function modePct(mode){
    const p = mProg(mode);
    if(mode === 'couple') return COUPLE_TASKS.filter(x => p.t[x.id]).length / COUPLE_TASKS.length;
    if(mode === 'family') return FAMILY_WISHES.filter(x => p.t[x.id]).length / FAMILY_WISHES.length;
    if(mode === 'tour') return Math.min(1, p.cp / TOUR_CPS.length);
    return 0;
  }
  function checkModeComplete(mode){
    const p = mProg(mode); if(p.done) return;
    if(modePct(mode) < 1) return;
    p.done = true;
    const reward = mode === 'couple' ? 150 : mode === 'family' ? 200 : 250;
    gainXu(reward);
    const title = MODE_TITLES[mode];
    if(title && !state.modeTitles.includes(title)) state.modeTitles.push(title);
    if(mode === 'tour') for(const id of ['NON-DOAN', 'AO-DOAN']) if(!state.wardrobe.includes(id)) state.wardrobe.push(id);
    save();
    document.getElementById('modeDoneTitle').textContent = mode === 'couple' ? '💕 Cặp đôi Hòa Bình!' : mode === 'family' ? '🎉 Cả nhà ấm no!' : '🚩 Hoàn thành tour Hòa Bình!';
    document.getElementById('modeDoneTxt').textContent = 'Hoàn thành 100% bảng việc ' + (mode === 'couple' ? 'Couple' : mode === 'family' ? 'Gia đình' : 'Theo đoàn') + ' — thưởng +' + reward + ' Xu' + (title ? ' + danh hiệu “' + title + '” gắn trong Hộ chiếu' : '') + (mode === 'tour' ? ' + Nón đoàn & Áo đoàn đã vào Tủ đồ (phím T)' : '') + '!';
    openModal('modeDoneModal');
    if(mode === 'couple') heartBurst();
  }
  function heartBurst(){
    for(let i = 0; i < 7; i++){
      const sp = tagSprite('💕', 'rgba(0,0,0,0)');
      sp.position.set(player.position.x + (Math.random() - 0.5) * 2, player.position.y + 1.4, player.position.z + (Math.random() - 0.5) * 2);
      worldGroup.add(sp); heartFx.push({ sp, ttl: 1.8, ph: Math.random() * 6.28 });
    }
  }
  function photoFlash(txt){
    const f = document.getElementById('photoFlash');
    document.getElementById('photoFlashTxt').textContent = txt;
    f.style.opacity = '1'; setTimeout(() => { f.style.opacity = '0'; }, 900);
  }
  // ---------- panel + modal ----------
  function renderModePanel(){
    const panel = document.getElementById('modePanel');
    const badge = document.getElementById('modeBadge');
    const m = state.mode;
    if(badge) badge.textContent = m === 'couple' ? '💕 Couple' : m === 'family' ? '👨‍👩‍👧 Gia đình' : m === 'tour' ? '🚩 Theo đoàn' : '';
    if(m === 'solo'){ panel.style.display = 'none'; return; }
    panel.style.display = 'block';
    const p = mProg(m);
    let rows = '', title = '';
    if(m === 'couple'){ title = '💕 Hẹn hò Đà Lạt — TIM ' + Math.round(modePct(m) * 100) + '%'; rows = COUPLE_TASKS.map(x => '<div class="tk' + (p.t[x.id] ? ' done' : '') + '">' + (p.t[x.id] ? '✔ ' : '○ ') + x.name + '</div>').join(''); }
    else if(m === 'family'){ title = '👨‍👩‍👧 Gia đình đi chợ — Ấm no ' + Math.round(modePct(m) * 100) + '%'; rows = FAMILY_WISHES.map(x => '<div class="tk' + (p.t[x.id] ? ' done' : '') + '">' + (p.t[x.id] ? '✔ ' : '○ ') + x.name + '</div>').join(''); }
    else if(m === 'tour'){ title = '🚩 Đoàn Hòa Bình — ' + Math.min(p.cp, TOUR_CPS.length) + '/' + TOUR_CPS.length + ' điểm • Đoàn 12 người — ' + (companions.filter(c => c.leader).length + 2) + ' đủ'; rows = TOUR_CPS.map((x, i) => '<div class="tk' + (i < p.cp ? ' done' : '') + '">' + (i < p.cp ? '✔ ' : i === p.cp ? '➤ ' : '○ ') + x.name + '</div>').join(''); }
    if(p.done) rows += '<div class="tk done">🏆 ĐÃ HOÀN THÀNH — danh hiệu trong Hộ chiếu!</div>';
    document.getElementById('modePanelTitle').textContent = title;
    document.getElementById('modeTasks').innerHTML = rows;
    document.getElementById('modeBar').style.width = Math.round(modePct(m) * 100) + '%';
    for(const id of ['mcSolo', 'mcCouple', 'mcFamily', 'mcTour']){
      const el = document.getElementById(id); if(el) el.classList.toggle('sel', id === 'mc' + m.charAt(0).toUpperCase() + m.slice(1));
    }
  }
  function setMode(m){
    state.mode = m; state.modeSeen = true; save();
    spawnForMode(m); renderModePanel();
    toast(m === 'solo' ? '🚶 Đi một mình — thong thả dạo chợ' : m === 'couple' ? '💕 Chế độ Couple — người thương đi cạnh bạn!' : m === 'family' ? '👨‍👩‍👧 Chế độ Gia đình — cả nhà theo sau!' : '🚩 Chế độ Theo đoàn — đoàn xe đang vào chợ…');
  }
  document.getElementById('btnMode').addEventListener('click', () => openModal('modeModal'));
  document.getElementById('modeClose').addEventListener('click', () => closeModal('modeModal'));
  document.getElementById('modeDoneClose').addEventListener('click', () => closeModal('modeDoneModal'));
  document.getElementById('mcSolo').addEventListener('click', () => { setMode('solo'); closeModal('modeModal'); });
  document.getElementById('mcCouple').addEventListener('click', () => { setMode('couple'); closeModal('modeModal'); });
  document.getElementById('mcFamily').addEventListener('click', () => { setMode('family'); closeModal('modeModal'); });
  document.getElementById('mcTour').addEventListener('click', () => { setMode('tour'); closeModal('modeModal'); });
  // ---------- móc mua hàng ----------
  function modeOnBuy(stall, item){
    const m = state.mode; if(m === 'solo') return;
    const nm = item.name || '';
    if(m === 'couple'){
      if(['dau', 'dau2', 'dau3', 'dau4'].includes(stall.id)) modeTaskDone('couple', 'dau', 'Mua dâu tặng nhau 🍓');
      if(stall.id === 'hoasua') modeTaskDone('couple', 'sua', 'Uống sữa đậu nành ở Hoa Sữa 🥛');
      if(['aokhoac', 'aolen', 'len3', 'dosi'].includes(stall.id)) coupleAoDoi();
    } else if(m === 'family'){
      if(nm.includes('Trà atiso')) modeTaskDone('family', 'ba', 'Bà có trà atiso 🍵');
      if(nm.includes('Mứt')) modeTaskDone('family', 'me', 'Mẹ có mứt làm quà 🍓');
      if(stall.id === 'banhtrang') modeTaskDone('family', 'bo', 'Bố ăn bánh tráng nướng 🔥');
      if(nm.includes('Búp bê len')) modeTaskDone('family', 'be', 'Bé có búp bê len 🧸');
    } else if(m === 'tour'){
      const p = mProg('tour');
      if(tourState && tourState.phase === 'walk' && p.cp === 2 && ['dacsan', 'tra', 'dacsanlon', 'mut', 'tra2'].includes(stall.id)) tourCheckDone();
    }
  }
  function coupleAoDoi(){
    if(!state.wardrobe.includes('AO-DOI')) state.wardrobe.push('AO-DOI');
    const partner = companions.find(c => c.role === 'partner');
    if(partner) recolor(partner.g, 'Shirt', 0xc95d7e);
    modeTaskDone('couple', 'aodoi', 'Áo đôi — cả hai cùng mặc 🧥 (xem Tủ đồ, phím T)');
  }
  const _buyItemMode = buyItem;
  buyItem = function(stall, item){ const x0 = state.xu; _buyItemMode(stall, item); if(state.xu !== x0) modeOnBuy(stall, item); };
  const _buyWdMode = buyWardrobe;
  buyWardrobe = function(stall, d){ const x0 = state.xu; _buyWdMode(stall, d); if(state.xu !== x0 && state.mode === 'couple' && ['aokhoac', 'aolen', 'len3', 'dosi', 'len1', 'len2'].includes(stall.id)) coupleAoDoi(); };
  // ---------- tour ----------
  function tourCheckDone(){
    const p = mProg('tour'); if(p.cp >= TOUR_CPS.length) return;
    const cp = TOUR_CPS[p.cp]; p.cp++; if(tourState) tourState.waitT = 0;
    save(); renderModePanel();
    toast('🚩 Check-in ✔ ' + cp.name + ' (' + p.cp + '/' + TOUR_CPS.length + ')', 'stamp');
    checkModeComplete('tour');
  }
  // ---------- tick chính (móc vào tickWater chạy mỗi frame) ----------
  let couplePhotoT = 0, coupleHatT = 0, famAnT = 0, famAnhT = 0;
  function near(x, z, px, pz, r){ return Math.hypot(px - x, pz - z) <= r; }
  function tickModes(t){
    const dt = lastTickT < 0 ? 0 : Math.min(0.1, t - lastTickT); lastTickT = t;
    if(!modesBooted){ modesBooted = true; if(state.mode !== 'solo') spawnForMode(state.mode); renderModePanel(); }
    if(!companions.length && !tourState) return;
    const px = player.position.x, pz = player.position.z, f = playerState.face;
    // đoàn xe chạy vào
    if(tourState && tourState.phase === 'drive'){
      let arrived = true;
      tourState.vehicles.forEach((b, i) => {
        const target = -152 - i * 8;
        if(b.position.x < target){ b.position.x = Math.min(target, b.position.x + 7 * dt); arrived = false; }
        b.position.y = groundH(b.position.x, 14);
      });
      if(arrived) spawnTourGroup();
    }
    // bạn đồng hành đi theo
    for(const c of companions){
      let tx, tz;
      if(c.leader && tourState && tourState.guide){
        const o = rotOff(tourState.guide.heading, c.off.x, c.off.z);
        tx = tourState.guide.g.position.x + o.x; tz = tourState.guide.g.position.z + o.z;
      } else {
        let off = c.off;
        if(c.role === 'be' && state.mode === 'family'){ // Bé thỉnh thoảng chạy trước rồi quay lại
          const cyc = t % 9; if(cyc < 2.4) off = { x: 0.6, z: 2.6 };
        }
        const o = rotOff(f, off.x, off.z);
        tx = px + o.x; tz = pz + o.z;
      }
      moveToward(c, tx, tz, dt, t);
    }
    // hướng dẫn viên dẫn đoàn
    if(tourState && tourState.phase === 'walk' && tourState.guide){
      const p = mProg('tour'), g = tourState.guide;
      if(p.cp < TOUR_CPS.length){
        const cp = TOUR_CPS[p.cp];
        const gd = Math.hypot(cp.x - g.g.position.x, cp.z - g.g.position.z);
        const pd = Math.hypot(cp.x - px, cp.z - pz);
        if(gd > 1.4){
          if(pd < 38){ const dx = cp.x - g.g.position.x, dz = cp.z - g.g.position.z; g.heading = Math.atan2(dx, dz); g.g.rotation.y = g.heading; g.g.position.x += dx / gd * Math.min(gd, 2.3 * dt); g.g.position.z += dz / gd * Math.min(gd, 2.3 * dt); g.g.position.y = groundH(g.g.position.x, g.g.position.z); }
        } else if(pd <= 3.6){
          tourState.waitT += dt;
          if(tourState.waitT >= 5) tourCheckDone();
        } else tourState.waitT = 0;
        if(pd > 30){ // đi quá xa đoàn
          tourState.farT += dt;
          if(tourState.flag) tourState.flag.scale.setScalar(1 + Math.sin(t * 10) * 0.18);
          if(tourState.farT > 10){ tourState.farT = 0; toast('🚩 Về đoàn nào! Cờ đoàn đang chờ bạn ở ' + cp.name); }
        } else { tourState.farT = 0; if(tourState.flag) tourState.flag.scale.setScalar(1); }
      }
    }
    // việc theo vị trí
    if(state.mode === 'couple'){
      const partner = companions.find(c => c.role === 'partner');
      if(partner){
        const pg = partner.g.position;
        if(near(-30, 5, px, pz, 3.5) && near(-30, 5, pg.x, pg.z, 3.5)){ couplePhotoT += dt; if(couplePhotoT >= 2 && !mProg('couple').t.photo){ photoFlash('📸 Đà Lạt — Cặp đôi Hòa Bình'); modeTaskDone('couple', 'photo', 'Chụp hình chung ở bùng binh hoa 📸'); } }
        else couplePhotoT = 0;
        if(near(31, -52, px, pz, 7) && near(31, -52, pg.x, pg.z, 7)){ coupleHatT += dt; if(coupleHatT >= 5) modeTaskDone('couple', 'hat', 'Nghe hát cùng nhau 🎶'); }
        heartT += dt;
        if(heartT > 4){ heartT = 0; if(Math.hypot(pg.x - px, pg.z - pz) < 2.3){ const sp = tagSprite('💕', 'rgba(0,0,0,0)'); sp.position.set(px + 0.5, player.position.y + 1.6, pz); worldGroup.add(sp); heartFx.push({ sp, ttl: 1.6, ph: 0 }); } }
      }
      if((state.fortuneCount || 0) > lastFortuneSeen){ lastFortuneSeen = state.fortuneCount; modeTaskDone('couple', 'boi', 'Coi bói đôi với Chú Ba 🔮'); }
    }
    if(state.mode === 'family'){
      const allNear = (x, z, r) => companions.length === 4 && companions.every(c => near(x, z, c.g.position.x, c.g.position.z, r + 2.5));
      if(near(-36, 27.9, px, pz, 5) && allNear(-36, 27.9, 6)){ famAnT += dt; if(famAnT >= 3) modeTaskDone('family', 'an', 'Cả nhà ăn cùng ở phố ăn 🍽'); } else famAnT = 0;
      if(near(27, 5.2, px, pz, 5) && allNear(27, 5.2, 6)){ famAnhT += dt; if(famAnhT >= 2 && !mProg('family').t.anh){ photoFlash('📸 Gia đình ở đài phun nước Đà Lạt'); modeTaskDone('family', 'anh', 'Chụp hình gia đình ở đài phun 📸'); } } else famAnhT = 0;
    }
    // tim bay
    for(let i = heartFx.length - 1; i >= 0; i--){
      const h = heartFx[i]; h.ttl -= dt; h.sp.position.y += dt * 0.7; h.sp.material.opacity = Math.max(0, h.ttl / 1.6);
      if(h.ttl <= 0){ worldGroup.remove(h.sp); heartFx.splice(i, 1); }
    }
    panelT += dt; if(panelT > 1){ panelT = 0; if(state.mode !== 'solo') renderModePanel(); }
  }
  const _tickWaterMode = tickWater;
  tickWater = function(t){ _tickWaterMode(t); tickModes(t); };
  if(!state.modeSeen){ try { setTimeout(() => { if(!anyModalOpen()) openModal('modeModal'); }, 1500); } catch(e) {} }
  window.__MODES = { setMode, mProg, companions, tickModes, modeTaskDone, tourCheckDone, TOUR_CPS, COUPLE_TASKS, FAMILY_WISHES, get tourState(){ return tourState; } };
}
"""
rep("animate();\nsetTimeout(() => toast('👋 Chào mừng",
    JS + "\nanimate();\nsetTimeout(() => toast('👋 Chào mừng",
    tag='js modes block')

# --- HUD badge ---
rep('<div id="hudMain" class="panel">',
    '<div id="hudMain" class="panel">',
    tag='hudMain anchor check')
s = s.replace('id="xuVal"', 'id="xuVal"', 1)  # no-op giu nguyen
# chen badge vao hudMain: tim dong chua hudMain roi them span sau the mo panel dau tien co id hudMain — dung cach chen truoc nut btnMode da them o hudBtns thi don gian hon: badge dat trong modePanelTitle da co. Them badge nho canh nut Che do:
rep('<button class="hbtn" id="btnMode">🎭 Chế độ</button>',
    '<button class="hbtn" id="btnMode">🎭 Chế độ</button> <span id="modeBadge" style="color:#ffd94d;font-weight:bold"></span>',
    tag='mode badge')

open(P, 'w', encoding='utf-8').write(s)
print('PATCH E DONE, bytes =', len(s.encode('utf-8')), '(delta %+d)' % (len(s.encode('utf-8')) - orig))
