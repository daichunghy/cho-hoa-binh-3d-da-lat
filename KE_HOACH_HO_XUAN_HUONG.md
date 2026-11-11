# KẾ HOẠCH — HỒ XUÂN HƯƠNG (khu đi dạo + đạp vịt thiên nga)

> Lệnh: Chung Hy 19:41 11/11/2026 — "build hồ Xuân Hương, tỉ lệ thích hợp với quảng trường
> Hòa Bình, có băng ghế đá, các kiểu, có đạp vịt… task lớn: lấy hình ảnh trước rồi plan
> thật kỹ trước khi làm". File này = vòng NGHIÊN CỨU + KẾ HOẠCH, chưa thi công.
> Ảnh tham chiếu: `theme/xuan-huong/` (17 ảnh thật đã kiểm chứng + `SOURCES.md`).
> Mọi con số game đều ĐỌC TỪ CODE `prototype-v2/index.html` (ghi kèm dòng), số thật đo
> PIL từ ảnh tải về hoặc spec nguồn web — đúng luật ĐO, KHÔNG ĐOÁN.

---

## 1. MẪU SỐ TỈ LỆ — QUẢNG TRƯỜNG HÒA BÌNH TRONG GAME (đo từ code)

| Khối | Số đo trong game | Nguồn |
|---|---|---|
| Mặt tiền chợ | rộng **68u** (marketHW 34 × 2), front z = **12** | index.html:918 |
| Tấm nền quảng trường (plaza) | plane **170 × 130u** tại (0, 0, 18) → x −85..85, z −47..83 | index.html:720 |
| Đảo bùng binh | tâm **(−30, −6)**, vành đường **R11.8 → Ø 23,6u**, solid 10,4 | index.html:1033, 1062, 1071 |
| Dải sân mở trước mặt tiền | sâu ~**30u** (z −17,8 mép vành đảo → 12 mặt tiền), ngang ~**94u** (x −48..46) | suy từ 2 dòng trên |
| Đài phun (mặt nước duy nhất hiện nay) | đĩa Ø **4,9u** tại (27, 5.2) | research/27 §0 |
| Ghế đá (idiom sẵn) | **1,8 × 0,5u**, cao ngồi 0,42 + tựa 0,62, tại x −15,5 quảng trường đệm | index.html:1083–1086 |
| Điểm spawn người chơi | **(−206, 5.6)**, cao độ 5,5 = entryRampY(−206), mặt hướng đông | index.html:2179 |
| Biên bản đồ hiện tại | nhựa tới x **−216**; minimap khung x **−212..92**, z **−88..40** (mmX/mmY) | index.html:1502, 6814 |
| Cao độ trục tây | entryRampY(x) = min(5,5; (−52−x)·0,07) — thềm phẳng **5,5** từ x ≤ −131 tới bùng binh đầu chợ | index.html (groundH) |

**Hệ số tỉ lệ của game (neo để quy đổi):** vật dụng 1u ≈ 1m (sạp 4,2u = sạp thật ~4,2m;
thuyền giữ nguyên mét thật). Kiến trúc nén ~0,75–0,8 (đảo thật Ø ~30m → 23,6u; mặt tiền
chợ thật ~90m → 68u). → Đoạn hồ dựng mới lấy **~0,5–0,6 tỉ lệ thật của một đoạn bờ bắc
điển hình**, neo tuyệt đối vào mẫu số quảng trường ở trên (không neo vào km thật).

**Suy ra kích thước khu hồ (chốt):**
- Bờ hồ (đường dạo) dài **100u** ≈ 1,06× chiều ngang dải sân quảng trường (94u) ≈ 1,5× mặt tiền chợ (68u) — đứng ở quảng trường nhìn sang thấy hồ "cùng cỡ thế giới", không lấn át chợ.
- Mặt nước rộng (bờ dạo → bờ xa) **80u** ≈ 2,7× chiều sâu dải sân (30u) — đủ xa để thuyền thành điểm nhỏ giữa hồ như ảnh 07/10, đủ gần để bờ xa không rỗng.
- Tổng mặt nước 128 × 80u ≈ 10.200u² ≈ 135× diện tích đĩa đài phun — đúng cảm giác "hồ" so với "bồn".

## 2. VỊ TRÍ — 2 PHƯƠNG ÁN, CHỐT 1

Địa lý thật: hồ nằm **tây-nam** chợ (~5–7 phút đi bộ), bờ **bắc** là đường Trần Quốc Toản,
bến đạp vịt + Thủy Tạ ở đầu tây-bắc hồ — tức đầu gần chợ nhất.

- **Phương án A — thẳng tây:** hồ chiếm x < −216, bờ chạy bắc–nam, đường dạo là bờ đông
  nhìn sang tây. *Ưu:* nối thẳng trục spawn. *Nhược:* sai địa lý (hồ thành "phía tây"),
  đường dạo quay lưng về chợ, bờ xa phải dựng cả skyline tây, và thềm 5,5 ở biên tây hiện
  là vành đồi khép kín — đặt nước lọt thỏm sau vành, nhìn từ chợ không thấy hồ.
- **Phương án B — tây-nam (CHỐT):** hồ ở góc tây-nam, đường dạo chạy dọc **bờ bắc** hồ
  theo hướng đông-bắc → tây-nam, nối từ bùng binh đầu chợ (spawn −206, 5.6) bằng lối
  vòng ~30u. *Lý do chốt:* đúng địa lý thật (bờ bắc Trần Quốc Toản, bến gần đầu chợ),
  thềm phẳng 5,5 sẵn có của trục tây thành cao độ bờ hồ tự nhiên (nước thấp hơn 0,6u —
  khớp cao kè đo từ ảnh), và từ quảng trường/chợ đi ra hồ đúng trình tự thật:
  chợ → bùng binh đầu chợ → bờ hồ.

**Khung tọa độ chốt (khóa ở Vòng 0, mọi vòng sau không tự dời):**
- Lối nối: từ (−206, 8) vòng xuống (−232, 26), rộng 6u, lát đá như đường dạo.
- Đường dạo bờ bắc: trục z ≈ 30, x từ **−238 → −338** (dài 100u). Tiết diện (từ nước lên):
  kè đứng tại z = 36 → lát đi bộ 5u (z 31..36) → dải ghế + cỏ 2,5u (z 28,5..31) →
  hàng đèn + thông tại z ≈ 28 → cỏ dốc nhẹ lên phía bắc.
- Mặt nước: x **−352..−224**, z **36..116**, mặt nước y = **4,9** (đường dạo y 5,5; kè 0,6u).
- Bến thuyền: x **−266..−252** ở bờ bắc đoạn đông (gần lối nối nhất); cầu bến gỗ vươn
  z 36 → 42; ki-ốt thuê thuyền tại (−259, 29).
- Thủy Tạ (điểm nhấn): bán đảo nhỏ ở góc đông-bắc mặt hồ tại (−240, 46) — gần bến,
  nhìn được từ đường dạo; đúng vị trí tương đối thật (đầu hồ phía chợ).
- Bờ xa (nam): taluy cỏ z 116..132 dốc lên 5,5 → 9 + hàng thông silhouette + 2–3 khối
  villa mờ; phao giới hạn vòng thuyền z ≈ 100.
- Cao độ toàn khu: 5,5 (khớp thềm trục tây, không bậc cấp từ spawn tới bến).

⚠️ **Bẫy kỹ thuật đã rà:** `groundH` với x < −208 và z > 34 hiện rơi vào nhánh mặc định
`z >= -2 → 0` — tức có "vách giả" ở biên tây-nam. Vòng 0 phải thêm nhánh groundH cho
toàn khu hồ TRƯỚC mọi nhánh mặc định, trước khi đặt bất kỳ vật nào.

## 3. SỐ ĐO THẬT → SỐ GAME (bảng quy đổi từng khối)

| Khối | Thật (đo/nguồn) | Trong game | Cách đo |
|---|---|---|---|
| Đường dạo ven hồ | vỉa hè Trần Quốc Toản ~5–6m (tỉ lệ ảnh 03 so lòng đường 2 làn ~7,5m) | lát **5u** + dải ghế/cỏ 2,5u | tỉ lệ pixel ảnh 03 |
| Cao kè | mặt dạo cao hơn mặt nước 0,4–0,6m (ảnh 03 mép đá; ảnh 05 taluy đoạn bờ cỏ) | **0,6u** (dạo 5,5 / nước 4,9) | nhìn + đối chiếu 2 ảnh |
| Màu nước ngày | #12669d (gần thuyền) · #649abb (giữa hồ) · #4d8393 (ven bờ) | base **0x276a8a** + texture gợn canvas — dùng đúng bộ thông số WATER-1 (research/27) | PIL median 4 vùng/3 ảnh |
| Lát đường dạo | #dde2e2 xám sáng, ô điểm hồng đỏ nhạt | slab 0xdde2e2 + ô accent #b98a7a thưa | PIL ảnh 03 |
| Ghế đá | ghế bê tông ven hồ, nhịp thật thưa 15–25m | ghế idiom game 1,8u, nhịp **12u** → 8 ghế, mặt hướng nước | ảnh 03/05 + idiom index.html:1083 |
| Đèn bờ hồ | cột đèn ven hồ nhịp ~25–30m | colonialLamp idiom, nhịp **18u** → 6 đèn | ảnh 14/17 (đêm) + nén tỉ lệ game |
| Thuyền thiên nga 2 chỗ | **2,1 × 1,6m**, thân sâu 0,6m, khoang 2 người, mái che phẳng (spec FRP PF-72) | **2,2 × 1,6u**, cao tổng ~1,6u (nước → mào), draft 0,25u | spec hãng + tỉ lệ ảnh 10 |
| Thiên nga 4 chỗ (dự phòng trang trí) | 3,25 × 1,62m (PF-71) | 1 chiếc neo bờ làm điểm nhấn, không lái được ở bản đầu | spec hãng |
| Màu thiên nga | thân trắng #e0dfe2, mỏ vàng cam, mào đỏ, mái che trắng/xanh sọc | đúng 4 mã này trong build_models | PIL ảnh 06 + nhìn ảnh 10 |
| Hàng thông bờ | thông 3 lá cao 15–25m | pine.glb clone scale 1,0–1,3 nhịp ~14u + 3–4 cây mai anh đào (tán hồng) gần bến | ảnh 18/16 |
| Hồ thật (tham chiếu cảm giác) | 25 ha, vòng hồ ~5km, hình lưỡi liềm | chỉ dựng 1 đoạn bờ bắc 100u — ghi rõ trong biển chỉ dẫn in-game là "đoạn bờ bắc" | reatimes/vinwonders |

## 4. BỐ CỤC KHU HỒ THEO KHỐI

1. **Mặt nước:** plane 128 × 80u tại y 4,9; vật liệu + texture gợn canvas 256² trôi
   offset (đúng idiom WATER-1 research/27 §3: base teal, vệt sáng #bfe6f5, đêm
   emissive qua list như `uplightMats`). Thêm vệt phản chiếu giả dưới hàng đèn bờ bắc
   khi đêm (plane mờ kéo dài trên nước — kỹ thuật rẻ kiểu chibi, xem ảnh đêm 15).
2. **Kè + đường dạo:** kè đứng đá xám dọc z = 36 (trừ đoạn bến), mặt lát #dde2e2,
   bó vỉa sáng như vành bồn WATER-1 (0xd8d2c2) để "bờ" đọc được mọi hướng nhìn.
   Đoạn tây xa (x < −320) chuyển taluy cỏ như ảnh 05 cho đỡ đơn điệu.
3. **Ghế đá:** 8 ghế idiom game (1,8u) hướng ra hồ, nhịp 12u; 2 ghế đăng ký điểm
   `sit` cho người chơi (idiom `startSit` sẵn có), 4 ghế đặt NPC ngồi tĩnh.
4. **Đèn + thông + mai anh đào:** 6 colonialLamp vào `applyDayNight`; thông pine.glb
   hàng sau z ≈ 27; 3 cây mai anh đào gần bến (tán cầu hồng — dựng trong lake.glb).
5. **Bến thuyền:** sàn gỗ (box code) 14 × 6u nhô ra nước, lan can 2 đầu, ki-ốt thuê
   (dựng code theo idiom sạp: khung + mái bạt + biển "THUÊ THUYỀN THIÊN NGA"),
   biển chỉ dẫn "BẾN THUYỀN HỒ XUÂN HƯƠNG" + biển đường "Đ. TRẦN QUỐC TOẢN"
   (signMesh/vSign idiom như biển NTMK tại −160).
6. **Thuyền:** 5 thiên nga 2 chỗ (3 neo dọc cầu bến, 1 neo bờ cỏ phía tây, 1 NPC chèo
   vòng chậm giữa hồ) + 1 thiên nga 4 chỗ neo bờ trang trí. Model Blender thật
   (lake.glb, §6) — cấm hộp trơn.
7. **Thủy Tạ:** pavilion trắng mái cong trên bán đảo (−240, 46), đèn ấm ban đêm,
   1 photo spot ngắm từ đường dạo. Không vào trong (giữ chi phí vòng đầu).
8. **Người:** 2 tuyến wander NPC dọc đường dạo (route khép kín 2 chiều), 4–6 NPC
   ngồi ghế/cặp đôi đứng ngắm hồ (static + sit idiom), 1 NPC trực ki-ốt (chat idiom).

## 5. CƠ CHẾ ĐẠP VỊT (bám idiom thuê xe V5.2 — không chế hệ mới)

Game đã có thuê xe máy: `interact` type `rent → toggleRide()`, `ride → parkBike()`
(xuống xe, xe đỗ tại chỗ), `remount` (cưỡi tiếp trong giờ thuê) — index.html:7278–7295.
Đạp vịt sao chép đúng khung này:

- **Thuê:** tới ki-ốt/cầu bến → ctxPrompt "🛶 Thuê thuyền thiên nga (30 Xu · 5 phút)"
  → E: trừ Xu, người chơi (và companion nếu đang đi Couple — ngồi ghế sau, dùng lại
  cơ chế companion sẵn có) hiện trên thuyền tại đầu cầu bến; HUD hiện giờ thuê như xe.
- **Lái:** W/↑ hoặc joystick đẩy tới = đạp (tốc độ tối đa ~2,2u/s, tăng tốc mềm),
  A/D hoặc joystick ngang = lái (tốc độ quay ~35°/s, chỉ quay khi đang có đà — đúng
  cảm giác đạp vịt); thả phím = trôi theo quán tính, ma sát nước. Bọt sóng: vòng gợn
  expanding ở đuôi thuyền (tái dùng hệ `rings` của đài phun) + vệt wake mờ.
- **Phạm vi:** toàn mặt nước, giữ biên mềm: cách bờ xa ≥ 6u, cách bờ bắc ≥ 3u ngoài
  vùng bến; chạm phao z ≈ 100 hoặc biên → thuyền tự lướt dừng + rung nhẹ + tiếng
  "cộc" (sfx sẵn), không kẹt góc. Va thiên nga NPC: đẩy nhẹ nhau ra (không vật lý cứng).
- **Xuống thuyền:** E khi ở trong vùng trả (bán kính 7u quanh đầu cầu bến) → thuyền
  neo lại, người chơi hiện trên cầu bến. E giữa hồ → ctxPrompt nhắc "Về bến để xuống
  thuyền". Hết giờ thuê giữa hồ: thuyền tự trôi chậm về hướng bến (autopilot như
  autoWalk) rồi mới cho xuống — tránh kẹt giữa hồ.
- **Phần thưởng móc vào hệ sẵn:** đạp đủ 1 vòng hồ (đi qua 4 điểm neo ảo quanh hồ,
  cơ chế đếm kiểu guideAngle của Theo đoàn) → +30 Xu + tính vào photo/quest nếu có;
  chụp ảnh trên thuyền tính photo spot 'lake' khi ở vùng giữa hồ.

## 6. MODEL BLENDER (pipeline chuẩn dự án, không ngoại lệ)

- Thêm vào `prototype-v2/scripts/build_models.py`: `build_lake()` → xuất **lake.glb**
  gồm: **SwanBoat** (thân vỏ cong bằng lathe/loft từ profile, cổ cong ống bezier
  thuôn, đầu + mỏ vàng + mào đỏ, khoang 2 ghế, khung + mái che phẳng, phao cứu sinh
  cam bên hông — đối chiếu ảnh 10/06 từng chi tiết), **ThuyTa** (khối trắng, cột,
  mái cong 2 lớp), **CherryTree** (thân + tán cầu hồng 2 tông). Ghế/kè/cầu bến =
  code box (đúng idiom game, ghế đã là box trong bản hiện tại).
- Sau build: chạy `scripts/quantize_glbs.sh` (luật GLB-QUANTIZE-1) → mới nạp assets.
- Ước lượng: swan ~6–9k tri/bản master (clone 6 chiếc, 1 geometry), tổng lake.glb
  quantized ~80–150KB → standalone +~0,2MB (headroom 5,6MB — thoáng).

## 7. HỆ THỐNG PHẢI NỐI (checklist cho từng vòng thi công)

| Hệ thống | Việc | Vị trí code |
|---|---|---|
| `groundH()` | thêm nhánh khu hồ (dạo 5,5 / bờ cỏ 5,5 / taluy nam / bán đảo) TRƯỚC nhánh mặc định; nước không phải mặt đi bộ | index.html:605 |
| `solid()` | kè z = 36 (chừa đoạn bến x −266..−252), ki-ốt, cột đèn, trụ cầu bến, bán đảo Thủy Tạ | index.html:672 |
| `detectZone()` | thêm zone "Bờ hồ Xuân Hương — Đ. Trần Quốc Toản" (chỉ label) + cân nhắc stamp mới (§8) | index.html:5000 |
| NPC wander | 2 route mới dọc đường dạo + route thuyền NPC trên nước (không qua đồ thị đường bộ) | addWanderer:3195 |
| ROUTE xe | **không đổi** — đường dạo là phố đi bộ; xe vẫn chạy NTMK như cũ | ROUTE_ROAD_E/W:3971 |
| Minimap | nới khung mmX/mmY: x −360..92 (452u), z −88..132 (220u) + vẽ thêm polygon hồ & đường dạo trong hàm vẽ bản đồ; rà mọi rect vẽ tay theo khung cũ | index.html:6814 + khối vẽ ~6835 |
| `applyDayNight()` | 6 đèn bờ + đèn Thủy Tạ + emissive nước vào list như `uplightMats`; vệt phản chiếu đêm | index.html:6460 |
| Photo spot | thêm `lake` (giữa hồ, chỉ chụp được khi trên thuyền) + `thuyta` (từ đường dạo) | PHOTO_SPOTS:5733 |
| Hộ chiếu | đề xuất thêm dấu thứ 10 { id:'lake' } — xem điểm khóa §8 | STAMPS:4989 |
| Âm thanh | ambience khu hồ: gió + nước vỗ bờ nhẹ (theo hệ ambience theo khu sẵn có) | khối ambience |
| Save | state.stamps là dict theo id → thêm dấu an toàn; vị trí thuyền thuê reset khi load (như xe thuê) | save/load |

## 8. ĐIỂM PHẢI KHÓA TRƯỚC KHI LÀM (ghi rõ để vòng thi công không tự quyết lại)

1. **Vị trí + khung tọa độ §2 (phương án B)** — khóa. Đổi vị trí sau Vòng 0 = làm lại groundH/minimap/solid.
2. **Biên bản đồ mới:** x tới −360, z tới +132 — khóa kèm công thức minimap mới.
3. **Dấu hộ chiếu:** kế hoạch đề xuất THÊM dấu 'lake' (9 → 10 dấu; save cũ an toàn vì dict theo id, UI tự đếm STAMPS.length). Đây là thay đổi spec "9 dấu" đã khóa từ đầu dự án — vòng thi công chỉ thêm khi triển khai Vòng 5, và ghi rõ vào V4-CHECKLIST như một thay đổi spec có chủ đích.
4. **Cao độ:** bờ 5,5 / nước 4,9 — khóa (ăn theo thềm trục tây, không tạo dốc mới).
5. **Thủy Tạ chỉ ngắm, không vào trong** ở bản đầu — khóa phạm vi.

## 9. LỘ TRÌNH THI CÔNG — 6 VÒNG NHỎ

Mỗi vòng: qua **bộ 8 cổng chuẩn** (diag 900 · SEED_SAVE 300 · standalone diag 300 ·
traffic 26/26 · audit_ground 0 lỗi cứng/0 nhảy lưới · test_bd2 · check_sweep3 ·
test_real1) + render Blender đối chiếu ảnh thật tương ứng, đạt mới sang vòng sau,
xong vòng nào đẩy GitHub vòng đó (nhịp làm việc đã khóa 19:05 11/11).

| Vòng | Việc | File đụng | Đối chiếu ảnh | Byte dự tính |
|---|---|---|---|---|
| **XH-0 KHUNG** | groundH khu hồ + solid kè + zone label + minimap khung mới + mặt đất trống (cỏ/nền đường dạo phẳng, chưa nước) | index.html | top-down render vs sơ đồ §2 | +3–5KB code |
| **XH-1 NƯỚC & BỜ** | mặt nước + gợn (idiom WATER-1) + kè + lát dạo + bó vỉa + taluy bờ xa + hàng thông silhouette | index.html | ảnh 03 (dạo), 05 (bờ xa), ngày + chạng vạng | +4–6KB |
| **XH-2 MODEL** | build_lake(): SwanBoat + ThuyTa + CherryTree → lake.glb → quantize → đặt 6 thuyền + pavilion | build_models.py, assets/lake.glb, index.html | ảnh 10 (cận thuyền), 06 (dãy neo), 12 (Thủy Tạ) | +0,2MB standalone |
| **XH-3 TRANG TRÍ BỜ** | ghế đá + sit spots, đèn + applyDayNight, ki-ốt + cầu bến + biển, NPC wander/ngồi, mai anh đào | index.html | ảnh 06 (bến), 17 (đêm bến) | +6–9KB |
| **XH-4 ĐẠP VỊT** | cơ chế thuê/lái/trả thuyền (bám rent/ride xe), HUD giờ, wake, biên hồ, NPC thuyền, thưởng vòng hồ | index.html | quay/chụp khi chơi thử; diag + traffic phải xanh | +8–12KB |
| **XH-5 TÍCH HỢP** | stamp 'lake', 2 photo spot, phản chiếu đêm, ambience, minimap icon, rà save cũ, bộ render cuối (ngày/đêm/top-down/trên thuyền) | index.html | toàn bộ set ảnh theme/xuan-huong | +3–5KB |

Tổng dự tính: standalone 4,89MB → ~5,2MB, vẫn dưới trần 10,48MB ~5,3MB.

## 10. RỦI RO

- **Minimap vẽ tay:** ngoài công thức mmX/mmY, khối vẽ bản đồ có thể chứa rect tọa độ
  cứng theo khung cũ → Vòng 0 phải rà toàn bộ hàm vẽ, không chỉ đổi 2 hàm map.
- **groundH thứ tự nhánh:** nhánh hồ phải đứng trước nhánh hành lang trục tây
  (x −208..−58, z −25..34) ở đoạn giao (lối nối) — sai thứ tự = cao độ nhảy 5,5 ↔ ramp.
- **Hiệu năng:** thêm ~40 prop + 1 mặt nước lớn — nhẹ; rủi ro chính là số NPC + thuyền
  NPC dùng chung vòng tick, giữ ≤ ngân sách hiện tại.
- **Cảm giác tỉ lệ:** bờ xa 80u với silhouette thấp có thể vẫn "gần"; nếu render XH-1
  cho thấy hồ nông, phương án dự phòng là hạ silhouette bờ xa + thêm lớp sương mù xa
  (fog sẵn có) thay vì nới bản đồ thêm.
- **Đồng hồ thuê thuyền + save:** không lưu trạng thái đang-thuê vào save (như xe) —
  load game luôn bắt đầu trên bờ.

## 11. NGHIÊN CỨU BỔ SUNG (vòng 2 — 11/11/2026)

Vòng 2 đào sâu theo lệnh "còn ít lắm, nghiên cứu thêm": **+22 ảnh thật (19–40), bộ ảnh = 39 ảnh**,
đo PIL có định vị visual grounding, số liệu web có URL từng số. Chi tiết ảnh + URL: `theme/xuan-huong/SOURCES.md`.
Các khóa vòng 1 (vị trí tây-nam B, khung nước, cao độ, 6 vòng XH-0→XH-5, cơ chế đạp vịt bám thuê xe)
**giữ nguyên** trừ các điểm sửa ở §11.4.

### 11.1 Ảnh mới theo mảng

| Mảng | Ảnh | Kết luận dùng thi công |
|---|---|---|
| Thủy Tạ cận + toàn cảnh | 19, 20, 21, 22, 36, 37, 38 | Khối trắng 2 tầng dáng "du thuyền": boong sát nước + lan can trắng, thang/mái dốc lên thượng, cột biển cao; nhà nằm trên **đảo tròn** (xem S1) |
| Thủy Tạ bình minh/khung hoa | 35 | Phượng tím là loài ký tên đoạn bờ Thủy Tạ (thêm vào danh sách cây) |
| Bến + neo thuyền | 23, 24 | Neo **mũi vào bờ** trên sàn bến thấp sát nước; mật độ trên mặt hồ giờ cao điểm ~15 chiếc/khung hình |
| Ghế bờ hồ | 25, 26, 27 | Mẫu chuẩn = **ghế bê tông 2 tấm** (xem S3); ghế thanh trắng là loại phụ trên bãi cỏ |
| Đèn + vỉa hè | 28 | **Đèn bướm** là đèn thật của Trần Quốc Toản (xem S2); vỉa hè tấm be + dải tactile |
| Đêm bờ bắc | 31, 32, 33, 39 | Ký tên đêm = **hàng cây uplight vàng + vệt phản chiếu dài**; cầu chữ Y lên đèn trắng; bollard thấp trong công viên bờ |
| Flycam tỉ lệ | 29, 30, 38, 20, 22 | Đảo Ø ≈ 0,30–0,37 bề ngang vịnh; dải bờ/mặt nước thật 0,06–0,10 → khóa game 8u/80u = 0,10 đúng |
| Cầu Ông Đạo | 40 (1955) | Đập thấp + đường trên mặt đập + lan can cọc 2 thanh — đủ hình khối để dựng khối nền (xem S4) |

### 11.2 Số liệu thật + nguồn

| Số liệu | Giá trị | Nguồn |
|---|---|---|
| Diện tích hồ | ~25 ha (phạm vi khai thác đạp vịt tính theo công trình thuỷ lợi: 38 ha — khác định nghĩa) | reatimes (ảnh 01); Tiền Phong/24h 11/2024 |
| Chu vi hồ | ~5 km (một nguồn 5,1 km) | đa nguồn du lịch; dalat24h |
| Đội thuyền toàn hồ | **95 thuyền đạp vịt + 3 ca nô cứu hộ**, 3 đơn vị khai thác; dịch vụ ~30 năm | Dân Trí + Tiền Phong 14/11/2024: https://dtinews.dantri.com.vn/vietnam-today/da-lat-suspends-duck-pedal-boat-service-on-xuan-huong-lake-20241114122948964.htm |
| Trạng thái dịch vụ | Tạm dừng 10–11/2024 (chưa cấp phép thuỷ lợi) → **hoạt động trở lại từ 13/08/2025** | baotintuc 21/08/2025: https://baotintuc.vn/du-lich/cho-phep-xe-dap-nuoc-tren-ho-xuan-huong-da-lat-hoat-dong-tro-lai-20250821103224181.htm |
| Giá thuê hiện hành | ~**60.000–120.000đ/giờ** theo loại thuyền (30.000đ/giờ là giá cũ còn lặp lại) | Mytour; Gofarvietnam bảng giá 2026; Vinpearl cập nhật 06/11/2026 |
| Bến chính | Giao **Đinh Tiên Hoàng × Trần Quốc Toản** + vòng neo quanh đảo Thủy Tạ | đa nguồn + ảnh 20/38 |
| Đường Trần Quốc Toản (bờ bắc) | Đoạn Đinh Tiên Hoàng → Trần Nhân Tông dài **~1.500m**; **lộ giới 12m** (lòng đường 2 làn ~7m, vỉa hè phía hồ ~3–4m) | Tiền Phong 02/06/2023; NLĐ 13/09/2023 (quy hoạch mở rộng) |
| Cao độ mặt hồ | ~1.477m so với mực nước biển (thuyết minh du lịch) | mytour |
| Cầu Ông Đạo | = **chính con đập đá** chắn suối Cam Ly, đầu tây-nam hồ; KS Trần Đăng Khoa xây **1934–1935** sau bão 03/1932 vỡ 2 đập cũ; tên gọi vì đập nằm trước Dinh Quản Đạo Phạm Khắc Hòe. Hồ đào 1919 (Cunhac/Labbé), đập 2 năm 1923, tên "Xuân Hương" từ 1953 | chuyenxua.net; dalatservices (ảnh 40 + chú thích) |
| Giờ hoạt động bến | **Chưa có nguồn** chính thức | — |
| Cao trình kè tuyệt đối | **Chưa có nguồn** (game giữ cao độ tương đối đã khóa: bờ 5,5 / nước 4,9) | — |

### 11.3 Đo từ ảnh vòng 2 (PIL, hộp mẫu định vị bằng visual grounding — chi tiết ở SOURCES.md)

- Thủy Tạ: sơn trắng (nắng đọc #bacad8 do ánh ngày; game **#f2f0eb**), mái phẳng **#afc1cc**, tấm biển cột **#0268d0**.
- Ghế bê tông: mặt kem trắng (nắng #ffffff → game **#e8e2d4**), chân tối **#5d534a** (game #4a423a).
- Thuyền: mái che xanh nhạt **#7edcfc**, ghế hồng **#fc508f**, thân trắng #ffffff + sơn hoa văn nhiều màu, phao cam #e8a33d.
- Đèn bướm: kim loại xanh tối (#364434 vùng bóng → game cột #1e4d2e); vỉa hè be **#e1d3bd**.
- Đêm: uplight cây vàng ấm (vệt phản chiếu #855916 → game vệt ~#a8742a, họ sáng #ffb45e); nước đêm #12121b.
- Tỉ lệ: đảo Thủy Tạ Ø ≈ 0,30–0,37 bề ngang vịnh ⇒ thật ≈ Ø120m; vòng neo quanh đảo 25–30 chiếc giờ cao điểm;
  thuyền/người khớp spec vòng 1 (thân 2,1m, mái che cao ~1,55m ≈ tầm mắt người ngồi) — giữ spec Blender vòng 1.

### 11.4 ĐIỂM SỬA PLAN VÒNG 1 (chỉ các điểm này thay khóa cũ)

- **S1 — Thủy Tạ: bán đảo → ĐẢO TRÒN có cầu nối (sửa lớn nhất).** Ảnh 20/22/38 cho thấy Thủy Tạ là đảo gần tròn
  Ø≈120m tách hẳn bờ, nối bằng cầu thẳng hẹp, nhà trắng ở mép tây đảo nhô ra nước, thuyền neo vòng bờ nam/tây đảo.
  → Game: đĩa đảo **Ø30u, tâm (−250, 58)** (x −265..−235, z 43..73 — vừa khung nước đã khóa; kênh đảo–bờ 7u ≈ tỉ lệ thật 0,08);
  cầu đi bộ dài 7u rộng 2,5u tại x=−250 (z 36→43); nhà Thủy Tạ đặt mép tây đảo (−262, 58) hướng mặt ra hồ (vẫn khóa: không vào trong nhà);
  **bến neo chính chuyển quanh bờ nam đảo** (cung z≈73, x −262..−238), bến bờ bắc x −266..−252 giữ làm bến phụ/NPC;
  **ki-ốt vé dời về đầu cầu phía bờ (−250, 31)**. Hệ quả thi công: XH-0 groundH thêm đĩa đảo (cao 5,5) + dải cầu;
  XH-1 thêm đĩa cỏ đảo + vòng đường quanh đảo; solid thuyền = vòng đảo; vùng nước loại trừ đĩa đảo.
  Đảo là công viên công cộng thật → người chơi **đi bộ lên đảo được** (mở rộng vùng đi bộ, không mở nội thất nhà).
- **S2 — Đèn đường dạo: colonialLamp → ĐÈN BƯỚM.** Ảnh 28: cột xanh đậm ~5–6m + cánh bướm kim loại xanh/panel mờ
  + huy hiệu tròn. 6 đèn giữ nhịp 18u nhưng dựng mesh đèn bướm (cột + 2 ellipse cánh + đĩa tròn), đêm cánh phát sáng mờ;
  colonialLamp chỉ còn dùng khu chợ.
- **S3 — Ghế: đổi vật liệu + vị trí đặt.** Mẫu thật = ghế bê tông 2 tấm kem #e8e2d4, chân thang tối #4a423a,
  đặt **trên dải cỏ sát mép nước** (không trên lát) mặt hướng hồ. → 8 ghế giữ số lượng/nhịp, chuyển z về dải cỏ
  (z≈37,5 phía hồ của đường dạo — cập nhật toạ độ khi XH-3 theo tiết diện cuối), ghế tài trợ để tấm trắng trơn (không in logo ngân hàng thật).
- **S4 — Thêm cầu Ông Đạo (khối nền, vòng 1 thiếu hẳn).** Đập đá thấp + mặt đường + lan can cọc 2 thanh ngang
  tại **mép tây xa của mặt nước (x −356..−348, z 60..96)**, ngoài vùng đi bộ/thuyền — điểm nhìn nền khi nhìn về tây;
  dựng ở XH-1 cùng khối bờ xa. Không đổi ROUTE xe, không tương tác.
- **S5 — Tiết diện đường dạo: GIỮ NGUYÊN khóa vòng 1** (lát 5u + dải ghế/cỏ 2,5u). Số liệu thật (lộ giới 12m gồm
  lòng đường xe ~7m, vỉa hè đi bộ thật chỉ ~3–4m) cho thấy game đã **phố đi bộ hoá** cả tiết diện — ghi rõ đây là
  chủ đích thiết kế (lõi trải nghiệm là đi dạo), không thu hẹp.
- **S6 — Thuyền neo phải có sơn hoa văn.** Ảnh 23/08/09: đội thuyền neo phần lớn sơn hoa/chấm/sọc nhiều màu, mái che
  xanh nhạt hoặc sọc hồng-trắng, ghế hồng/xanh. → XH-2 thêm 2 biến thể texture canvas hoa văn cho thuyền neo
  (ít nhất 2/5 chiếc), thuyền người chơi giữ trắng sạch để nhận diện; màu mái/ghế theo §11.3.
- **S7 — Thêm 3 chi tiết bờ có ảnh thật:** (a) **cầu ngắm chữ Y** lan can trắng vươn 5u ra hồ tại x=−282 và x=−318 (ảnh 33);
  (b) **đèn bollard thấp** dọc lối công viên bờ đoạn gần cầu đảo (ảnh 39); (c) **phượng tím** 2 cây gần đầu cầu đảo +
  bụi hoa loa kèn cạnh đèn bướm (ảnh 35/28). Đưa vào phạm vi XH-3.
- **Giá/giờ thật không đổi cơ chế game:** thuê vẫn 30 Xu/5 phút (tiền game); số liệu 60–120k/giờ chỉ là tư liệu đối chiếu.

### 11.5 Danh sách chi tiết trang trí bờ — CHỐT DỰNG NGAY (mỗi dòng 1 vật)

- **Ghế:** hộp mặt 1,8×0,5×0,08 + tấm lưng nghiêng nhẹ, bê tông kem #e8e2d4; 2 chân thang bê tông tối #4a423a; đặt trên cỏ sát mép nước, hướng mặt ra hồ.
- **Lan can kè:** cọc sắt hộp 0,06 cách 1,2u + 2 thanh ngang, sơn trắng (đoạn cầu chữ Y + đầu cầu đảo); đoạn kè thường giữ bó vỉa đá như vòng 1 (bờ bắc thật không lan can liên tục).
- **Đèn bướm:** cột trụ xanh #1e4d2e cao 3,2u (nén từ 5–6m thật), 2 cánh ellipse xanh + panel mờ, đĩa huy hiệu Ø0,5 treo dưới cánh; đêm: panel + đĩa phát sáng ấm, uplight họ #ffb45e.
- **Đèn bollard:** trụ hộp 0,12×0,5 tối + đầu phát sáng trắng ấm, dọc lối đá công viên bờ, nhịp 6u đoạn gần cầu đảo.
- **Thùng rác:** trụ Ø0,45×0,7 xanh lá đậm có nắp vòm, đặt cạnh ghế/đèn (chưa có ảnh cận đạt — dựng theo mẫu công viên phổ thông, ghi rõ).
- **Biển chỉ dẫn:** cột 2,2u + biển chữ nhật xanh/trắng "BẾN THUYỀN THIÊN NGA" ở đầu cầu đảo và đầu lối nối (chưa có ảnh cận đạt — theo quy ước biển công viên).
- **Ki-ốt vé:** quầy 2,2×1,6×2,4 mái dốc tại đầu cầu đảo (−250, 31), mặt trước treo áo phao cam + bảng "THUÊ THUYỀN — 30 XU/5 PHÚT".
- **Cầu bến:** sàn gỗ/thép thấp 0,25 trên mặt nước dọc cung bờ nam đảo, thuyền neo mũi vào bờ cách nhau 2,6u, phao cam treo khung mái mỗi thuyền neo.
- **Cầu chữ Y:** sàn gỗ 5×1,8 vươn ra hồ, lan can trắng 2 bên, đầu cầu tẽ 2 nhánh ngắn hình Y, tại x=−282 và x=−318.
- **Cầu đảo:** sàn lát 7×2,5 thẳng tại x=−250, lan can trắng thấp 2 bên, đầu cầu phía đảo mở vào vòng đường cỏ.
- **Đảo Thủy Tạ:** đĩa cỏ Ø30 viền kè đá thấp, vòng đường lát quanh cỏ tròn tâm, nhà trắng 10×6×5,5 + boong lan can trắng nhô ra nước ở mép tây, cột biển xanh #0268d0 cao 3u trên mái, 2 liễu rũ + 1 thông cao trên đảo.
- **Cầu Ông Đạo (nền xa):** thân đập đá xám rộng 8u chạy z 60..96 ở x≈−352, mặt đường nhựa trên đỉnh + lan can cọc trắng phía hồ, không tương tác.
- **Cây bờ:** thông pine nhịp ~14u (gốc quét vôi trắng 0,8u — chi tiết thật ảnh 25), liễu rũ sát mép nước đoạn gần đảo, mai anh đào cụm gần bến, phượng tím 2 cây đầu cầu đảo, bụi hoa loa kèn trắng/vàng cạnh đèn bướm.

### 11.6 Còn thiếu (ghi trung thực, không đoán)

- Chưa có ảnh đạt: cận ki-ốt bán vé/bảng giá thật (giá đã có từ web), cận thùng rác, cận biển chỉ dẫn, ảnh hiện trạng cầu Ông Đạo (chỉ có ảnh 1955).
- Chưa có nguồn: giờ hoạt động chính thức của bến; cao trình kè tuyệt đối.
- Ảnh 27 có watermark blog ở góc, ảnh 29 có watermark báo — chỉ dùng đối chiếu, không dùng làm texture.
