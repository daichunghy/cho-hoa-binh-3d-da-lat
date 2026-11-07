# V4 CHECKLIST — Cải thiện sâu theo ảnh thật (research/11)

Nguyên tắc: mỗi mục có cách kiểm chứng quan sát được. Chỉ tick khi đã có bằng chứng.

## A. Nhà lồng chợ (market.glb dựng lại)
- [x] Chữ nổi 3D "CHỢ ĐÀ LẠT" ĐỎ mặt tiền (kiểm chứng: node/mesh material `SignLetters` trong GLB + thấy trong render v4-01)
- [x] Chữ "CHỢ ĐÀ LẠT" đỏ gỉ mặt sau + tháp thang máy kính xanh lá + bạt sọc xanh–trắng + cầu thang trắng ngoài trời (render v4-01b)
- [x] Dải ZIGZAG trắng chạy ngang mặt tiền (node `Zigzag` + render v4-01)
- [x] Dải cửa sổ lam trắng (louver) tầng trên (render v4-01)
- [x] Băng hồng đào dưới cửa sổ tầng 2 (render v4-01)
- [x] Dải biển quảng cáo nhiều màu + panel LED đỏ tầng trệt (render v4-01)
- [x] Sân thượng: lan can + hàng thông cột + tượng trắng + hộp kính (render v4-01)
- [x] Giữ nguyên neo kỹ thuật: footprint 70×18, sàn 6.55/12.85, terrace (17.5,~9.5) top 12.6, material `MarketWin` còn để web bắt sáng đêm

## B. Bùng binh (roundabout.glb)
- [x] Tượng đài đá xám ở tâm: bệ bậc + 3 tượng người trừu tượng + thông đá chạm (render v4-02)
- [x] Thảm hoa HỌA TIẾT quạt quanh tượng (mảng hoa xen cỏ) (render v4-02)
- [x] Ghế đá trắng quanh (render v4-02) + collider ghế trong web

## C. Xe cộ (vehicle.glb + giao thông web) — MỚI
- [x] vehicle.glb có `Moto` (WheelF/WheelR tách riêng để quay, Rider, Helmet, HeadLamp) và `Car` (4 bánh, HeadLamp) — kiểm chứng parse GLB
- [x] Xe máy chạy vòng bùng binh + chạy thẳng đường trước chợ, nhiều xe khác tốc/làn (grep hệ `vehicles` trong index.html)
- [x] Bánh xe quay theo tốc độ (code animate)
- [x] Đèn pha: emissive + nón sáng bật về đêm (applyDayNight)
- [x] Bãi xe máy đậu dày trước chợ ≥ 40 chiếc (đếm trong code tĩnh/loop)

## D. Đám đông làm lại
- [x] Tổng NPC ≥ 68 (đếm: addWanderer + sitters + queues + groups trong code)
- [x] Phân bố: dày ở bậc thang + đường chợ đêm, vừa quảng trường, thưa nhà lồng (đếm theo khu trong code)
- [x] NGỒI ĂN trên bậc thang: NPC ngồi ghế nhựa xanh/đỏ trên bậc, tay ăn + gật đầu (code + render v4-03)
- [x] XẾP HÀNG 3–5 người ở ≥ 6 sạp ăn đặc biệt (code)
- [x] NHÓM ĐỨNG nói chuyện 2–3 người đối mặt + cử chỉ tay (code)
- [x] Đa dạng màu áo/khăn/mũ (palette + scarf ngẫu nhiên trong code)

## E. Đèn đêm
- [x] Mỗi sạp 1 bóng đèn trắng + quầng halo sprite, bật đêm, nhấp nháy nhẹ lệch pha (code `stallBulbs` + render v4-04 mô phỏng)
- [x] Chữ CHỢ ĐÀ LẠT phát sáng đỏ ban đêm (SignLetters emissive qua applyDayNight)
- [x] Đèn đường cam sodium (đã có từ v3 — xác nhận còn nguyên)
- [x] Dây đèn cũ giữ một phần (xác nhận còn nguyên)

## F. Chi tiết sạp
- [x] Bạt sọc 2 màu (canvas texture web) cho sạp rau/len/chợ đêm
- [x] Biển tên sạp: trong nhà lồng = nền trắng/vàng chữ đỏ khổ lớn; ngoài trời giữ nền tối chữ vàng
- [x] Mẹt tròn hàng theo màu + rổ nhựa đỏ/xanh ở sạp nông sản
- [x] Tường đồ len treo nhiều màu ở sạp len
- [x] Ghế nhựa + bàn thấp ở sạp ăn; chai tương ớt trên quầy ăn; hộp quà xếp chồng ở sạp đặc sản

## G. Giữ nguyên gameplay v3
- [x] node --check đạt cho module JS
- [x] Còn đủ: openMenu/buyItem/sellItem/buyUpgrade/tickSystems(nhiệt độ)/drawFortune/toggleListen/openPassport (grep)
- [x] Save key `chohb3d-v1` không đổi

## H. Khách sạn quanh khu (hotels.glb) — BỔ SUNG 09:57
- [x] 4 biến thể khách sạn 4–6 tầng: khối trắng/kem, cửa sổ đều nhịp có khung lõm/nổi, ban công vài tầng, gờ chỉ từng tầng, mái đua + bể nước nóc
- [x] Biển tên nóc bằng chữ nổi phát sáng đêm (DALAT CENTER vàng / HOTEL COLLINE trắng / VIB trắng / THANH BÌNH xanh) — material `HS*`, web tăng emissive ban đêm
- [x] Cửa sổ sáng đèn vàng RẢI RÁC ban đêm (3 material HotelWinA/B/C, web cho cường độ khác nhau)
- [x] Bố trí: dãy sau đồi (phông nền bậc thang), 2 bên đông/tây, 2 phía nam sau chợ + collider

## I. Quán nước + cà phê mặt đường (shop.glb) — BỔ SUNG 09:57
- [x] shop.glb: nhà 2 tầng mặt tiền lớp (cửa lõm, hiên/bạt, biển, ban công nhỏ)
- [x] 3 quán đặt đúng vị trí tương đối: cạnh bùng binh (tây), chân bậc thang (đông), đường đông trước chợ
- [x] Biển chữ canvas từng quán + bàn ghế vỉa hè + khách ngồi uống (statics)

## J. Chất lượng 3D (tiêu chí soi render — BỔ SUNG 09:57)
- [x] Khối chính đều có bevel — không còn cạnh sắc "hộp trơn"
- [x] Mặt tiền có lớp: cửa sổ lõm/nổi, ban công, gờ chỉ, mái đua
- [x] Vật liệu có biến thiên nhẹ giữa các bề mặt (không 1 màu bẹt toàn khối)
- [x] Nhân vật: thêm cầu vai bo tròn, tăng bevel tay/chân/thân (character.glb dựng lại)
- [x] Vòng xoay khớp bố cục ảnh 04: đảo r6.9 / ghế r8.3 / người r~9.5 / xe máy r10.6 / ô tô r11.8

## Kiểm chứng cuối
- [x] Render v4-01 mặt tiền ngày — tự soi
- [x] Render v4-01b mặt sau/thang máy kính — tự soi
- [x] Render v4-02 bùng binh + tượng + xe — tự soi
- [x] Render v4-03 bậc thang đông người ngồi ăn — tự soi
- [x] Render v4-04 dãy sạp + đèn (mô phỏng đêm) — tự soi
- [x] Đóng gói index-standalone.html (14 GLB nhúng), 9.856.024 byte (9,40 MB) — dưới ngưỡng 10MB
- [x] Cập nhật KE_HOACH.md

## V4.1 — Sửa 4 điểm điều phối bác ở v4 (06/11/2026)
- [x] **1. MẶT NHÂN VẬT (regression v4) — ĐÃ SỬA + render cận mặt xác nhận.** Chẩn đoán: (a) render kiểm chứng v4 bật CẢ 3 mũ cùng lúc (web makePerson chỉ bật 1) → cầu beanie đỏ nâu + vành cap xiên qua mặt thành "dải ngang tối + mảng đỏ"; (b) lỗi GLB thật: mũ beanie/cap là cầu nguyên khối phủ xuống tận cằm, chôn cả mắt (z1.52). Sửa trong build_character(): helper trim_front_below() cắt phần cầu mũ/tóc ở trước mặt dưới ngưỡng z; beanie thành vòm dẹt + vành cyl nâng lên z1.63; cap vành nâng lên z1.585; mắt to hơn (r0.05). Bằng chứng: renders/v41-face-before-beanie-front.png + v41-face-before-allhats-above.png (tái hiện lỗi) → renders/v41-face-after-beanie-front.png + v41-face-after-nonla-above.png (mặt sạch: 2 mắt chấm đen + má hồng + mũi + miệng, mũ ôm đỉnh đầu trên mắt). character.glb 475.700 → 459.580 byte.
- [x] **2. TƯỢNG ĐÀI + THẢM HOA — ĐÃ SỬA.** Tượng: bệ 3 bậc giữ, pedestal hạ (1.8×1.8×1.35), cụm 3 hình người trừu tượng đọc rõ đầu/vai/tay vươn (thân cyl thuôn + cầu vai + đầu r0.27), thông đá thu nhỏ trên đỉnh (~8.4 tổng). Thảm hoa: 8 quạt vành khăn đặc (sector r2.32–5.72) xen kẽ carpet hoa bão hoà / cỏ + hoa nhỏ rải dày 3 vòng mỗi quạt + vòng hoa sát bệ 16 — liền mảng, không còn chấm thưa. roundabout.glb 1.107.856 → 1.500.476 byte.
- [x] **3. MẶT TIỀN — ĐÃ SỬA.** Băng hồng đào đậm hơn (0.78,0.42,0.23) + thêm 3 rãnh PeachSlat tối chạy dọc băng; dải zigzag: nền đậm tương phản (0.52,0.49,0.44) + chevron arm 1.42 / thick 0.42 / tall 0.62 (cao + dày hơn hẳn v4). market.glb 1.563.916 → 1.569.348 byte.
- [x] **4. KIỂM CHỨNG TOÀN CẢNH — MỚI:** scripts/render_check_v41.py lắp toàn bộ cảnh như web (2 cao độ, nhà lồng, thang + cầu, bùng binh + tượng + xe chạy + bãi xe đậu ~70 chiếc, 20 sạp, 4 khách sạn ×7 vị trí, 3 quán) + đám đông 68 NPC đúng phân bố web (12 ngồi ăn bậc thang, 8 đứng trên thang, 12 xếp hàng 4 sạp, 10 dạo đường chợ đêm, 5 quanh bùng binh, 6 nhóm nói chuyện, 6 quảng trường đồi, chú coi bói + khách, 3 khách quán, ca sĩ + 3 khán giả). 2 ảnh nghiệm thu: renders/v41-01-toan-canh-ngay.png + renders/v41-02-cho-dem.png (verdict tự soi ghi trong KE_HOACH.md mục V4.1).
- [x] Gameplay + save giữ nguyên (không đụng index.html đợt này ngoài đóng gói lại); node --check module JS: OK.
- [x] Đóng gói lại index-standalone.html: 14 GLB, 10.365.264 byte (9,89 MB) — tăng so với v4 (9,40 MB) chủ yếu do roundabout chi tiết hơn (+392KB GLB); vẫn dưới ngưỡng 10MB nhưng rất sát — đợt sau thêm model phải nén GLB trước.
- [ ] Đẩy GitHub / upload bản v4.1 — KHÔNG làm theo lệnh đợt này (chờ điều phối).

## V4.2 — HÀNH TRÌNH ĐI VÀO + MẶC ĐỊNH TỐI ẤM + VIBE ĐÀ LẠT + LỚP GAME + BÁM ẢNH CHỐT (06/11/2026)
### HÀNH TRÌNH ĐI VÀO (lệnh 14:56 — ưu tiên cao nhất)
- [x] Trục hành trình chốt: SPAWN đầu đường vào → ĐƯỜNG VÀO → VÒNG XOAY → CHỢ → BẬC THANG (Chú Ba) → QUẢNG TRƯỜNG ĐỒI / NGƯỜI HÁT.
- [x] Đường vào dựng lại: mặt nhựa dốc nhẹ về bùng binh (ramp ~2m từ x=-83→-52, groundH + xe bám dốc), vạch kẻ + vạch qua đường, vỉa hè 2 bên, 6 nhà phố/quán 2 bên (biển canvas: PHỞ & BÚN BÒ ĐÊM, TẠP HÓA CÔ TƯ, NHÀ NGHỈ HOA SIM, CÀ PHÊ SƯỜN ĐỒI, HOMESTAY THÔNG XANH, BÁNH MÌ & SỮA NÓNG), HotelD dời khỏi lòng đường về (-70, 15.5), cổng chào "KHU HÒA BÌNH — CHỢ ĐÀ LẠT" tại spawn, xe chạy + xe đậu dọc lề, 2 sạp mới trên đường vào (BÁNH ƯỚT LÒNG GÀ, SỮA TƯƠI & ĐẬU HŨ) + hàng rong ngồi + khách ngồi vỉa hè.
- [x] Spawn đặt lại (-76, 2) + camera mở đầu sau lưng nhìn dọc đường về vòng xoay/mặt tiền (camYaw -π/2); từ spawn thấy cổng + đường + bùng binh + mặt tiền.
- [x] Mật độ dày nhất dọc trục: +3 tuyến người đi bộ bám trục, hàng chờ 2 sạp mới, nhóm chat vỉa hè, khách ngồi trước nhà phố.
### MẶC ĐỊNH BUỔI TỐI + TÔNG ẤM (lệnh 15:19)
- [x] Load game (kể cả save mới) = CHỢ ĐÊM ~19:15 (isNight mặc định true; giờ game 19.25 khi đêm / 9.5 khi ngày cho nhiệt độ + đám đông + giờ diễn); nút N/ngày-đêm giữ nguyên.
- [x] Grade ấm: nền/sương đêm nâu ấm 0x191209, hemi vàng mật ong, đèn điểm vàng cam 0xff9a3d cường độ tăng, exposure 1.0, quầng ướt (wetGlows) dưới đèn/sạp, nhiệt độ lạnh + sương đêm khớp mặc định tối.
### LỚP 1 — VIBE ĐÀ LẠT (lệnh 16:01)
- [x] Phông đồi thông: 8 ridge cone lớp xa + hàng thông lớn sườn đồi + hàng thông mép đồi — không thấy mép thế giới.
- [x] Sương sống: thêm mảng sương trôi đường vào/đồi + 2 đĩa sương sát đất (vòng xoay, trước chợ) xoay/đổi opacity theo đêm.
- [x] Hoa Đà Lạt: cẩm tú cầu (cụm cầu xanh/tím/hồng) dọc vỉa hè đường vào + vòng xoay + quảng trường + giỏ hoa treo cột đèn thuộc địa/lan can cầu.
- [x] Đèn kiểu thuộc địa dọc đường vào + vòng xoay + quảng trường (cột đúc, chụp đèn ấm, PointLight xen kẽ).
- [x] Đường ướt phản sáng: vật liệu đường bóng (roughness 0.35) + đĩa quầng sáng mặt đất dưới mọi đèn/sạp (chỉ hiện ban đêm).
- [x] Khói/hơi: ống khói HotelD + nhà sườn đồi, hơi quán cà phê vợt (cộng lớp hơi sạp ở mục BÁM ẢNH CHỐT).
- [x] Landmark hậu cảnh: tháp chuông nhà thờ stylized (silhouette + 2 cửa sổ sáng) trên đồi bắc.
### LỚP 2 — GIỐNG GAME HƠN (lệnh 16:01)
- [x] Nhiệm vụ dẫn đường 5 chặng đúng hành trình (cột sáng + mũi tên + panel HUD + tiến độ): 1) tới vòng xoay 2) vòng quanh tượng đài (đo góc quét) 3) mua 1 món bất kỳ 4) coi 1 quẻ Chú Ba 5) nghe hát ở quảng trường. Mỗi chặng: toast + thưởng 30 Xu (chặng cuối 60) + tích vào hộ chiếu qua hệ dấu sẵn có.
- [x] Thẻ tên khu vực chữ lớn mờ dần: Đường vào chợ / Vòng xoay Hòa Bình / Chợ Đà Lạt / Bậc thang chợ / Quảng trường Hòa Bình.
- [x] Bong bóng thoại NPC theo khu/món (người gần nhất, câu xoay vòng: sữa nóng, bánh tráng, coi bói, hát...).
- [x] Hiệu ứng: sạp đặc biệt + điểm nhiệm vụ lấp lánh (sparkles vàng), popup +Xu bay lên khi nhận Xu.
- [x] Minimap góc màn hình: nền khu/đường/vòng xoay/thang + chấm người chơi + chấm mục tiêu vàng nhấp nháy.
### BÁM ẢNH CHỐT (lệnh 16:25 — thước đo theme/CHOT-phong-cach-cho-dem.png)
- [x] Biển sạp: bảng gỗ lớn canvas (vân gỗ + tên vàng kem + dòng GIÁ "— 15K —" + hình hũ đậu/chồng ly vẽ kèm), đọc từ xa — áp cho mọi sạp.
- [x] Bày hàng riêng: sạp đồ uống/súp có hũ thuỷ tinh đựng đậu + chồng ly + tô đậu phộng + ly mang đi; sạp nướng có bánh trên vỉ; sạp đồ ăn có chồng chén; phin/nồi dùng prop GLB sẵn có.
- [x] Tiểu thương có đạo cụ: sạp sữa/sữa tươi/cà phê có ấm rót trên tay + dòng rót hiện khi có khách xếp hàng/người chơi tới gần (tay chuyển tư thế rót); cột hơi nước LỚN (sprite size 1.15, cao 3.4) ở sạp đặc biệt có món nóng.
- [x] Lồng đèn giấy vàng LỚN (r0.21) x3/sạp nhiều cao độ + tua đỏ, đêm phát sáng ấm mạnh; đèn dây chỉ giăng quảng trường/đường vào/hẻm ăn — trục Âm Phủ giữ đèn từng sạp theo ảnh thật (research/11+12).
- [x] Nóc sạp phủ cành thông + chùm lá; trước sạp: giỏ mây dâu tây + chậu cây nhỏ.
- [x] Nền đá lát canvas (đá cuội có khe) cho quảng trường trước chợ + quảng trường đồi; sương là là sát đất ban đêm ở khu chợ.
- [x] Thẻ tên NPC pill canvas trên đầu ("Cô Lan - Bán Sữa", "Chú Ba - Coi Bói", ca sĩ...) + thẻ "Bạn" cho người chơi — chỉ hiện khi đến gần (<13.5).
### BỔ SUNG research/12 (lệnh 16:35)
- [x] Mục 2 — UI NÂU ẤM: toàn bộ panel/HUD/modal/toast chuyển nâu đậm + viền vàng đồng + bo góc 14-16px, nền trang nâu tối (hết kính xám-xanh lạnh).
- [x] Mục 11 — Đơn hàng "MUA HỘ" (Township): khách NPC (dấu ! vàng + chip đơn) nhờ mua 1 món cụ thể ở sạp chỉ định; mua xong quay lại giao → thưởng giá×2+15 Xu; đơn hết hạn sau ~170s, đơn mới xuất hiện sau ~1 phút.
- [x] Đối chiếu 19 mục research/12: ĐÃ LÀM 1 (thẻ tên), 2 (UI nâu), 3 (biển có giá+hình), 4 (cành thông nóc), 5 (giỏ dâu/chậu cây), 6 (cột hơi lớn — ở mức sprite points to/đậm hơn), 7 (đá lát), 10 (đèn giấy lớn + quy tắc dây), 11 (đơn mua hộ). LÀM MỘT PHẦN: 8 (bộ bày hàng mới đủ sâu cho họ đồ uống/nướng/ăn — họ kem-dâu/lưu niệm/hoa chưa có set riêng), 9 (đạo cụ cầm tay mới có ấm rót cho 3 sạp đồ uống — xẻng/muôi/cân cho nghề khác chưa có). ĐỂ ĐỢT SAU: 12 (nội thất nhà lồng chiều dọc), 13 (sự kiện hẹn giờ + đèn lồng điều ước), 14 (mèo đi theo), 15 (thang cầu vồng + khung check-in), 16 (chợ phiên đầu mối cuối tuần), 17 (xe đẩy rong di động; xe đạp sạp rau), 18 (đồng hồ + cờ + chậu hoa mặt tiền), 19 (sạp của bạn — effort L).
### Kiểm chứng V4.2
- [x] node --check module JS: OK sau từng patch (1a-1d, 2a-2c). index.html 163.360 byte.
- [x] Đóng gói index-standalone.html: 14 GLB, 10.410.292 byte (9,93 MB) — dưới ngưỡng 10MB.
- [ ] Render hành trình scripts/render_journey.py: 5 ảnh đêm ấm (a đường vào / b vòng xoay / c bậc thang / d đồi thông / e cận sạp) — verdict điền sau khi soi.
- [ ] Đẩy GitHub / upload — KHÔNG làm theo lệnh đợt này.

---
## V4.3 — SỬA THEO PHẢN HỒI CHƠI THỬ 23:47 (06/11) + KHUNG "GAME THẬT" + KHÓA PALETTE research/13
### 1. BUG "ĐI TRÊN TRỜI" — ĐÃ TÌM GỐC RỄ & SỬA DỨT ĐIỂM
- [x] GỐC RỄ (đo trực tiếp bridge.glb bằng Blender + đối chiếu script render đã kiểm chứng): mesh cầu đặt `rotation.x = -atan2(4.4,39)` — SAI DẤU. Mặt cầu nhìn thấy dốc NGƯỢC với mặt đi logic (groundH): đầu đồi người lơ lửng +4,3m trên mặt cầu; đầu chợ kết cấu dâng lên cắt ngang người → người "đứng trên dầm/xà ngang" đúng như ảnh chụp lỗi. ĐÃ SỬA: `rotation.x = +atan2(4.4,39)`; 2 trụ đỡ pier (scale.y 13,4/15,0) vốn khớp dốc đúng — thêm bằng chứng dấu xoay là lỗi duy nhất.
- [x] groundH cầu bám đúng mặt deck đo từ GLB: `17.14 - (z+30)*0.11282` (deck top +0,29 so với mặt phẳng gốc).
- [x] Rà toàn bộ tuyến lang thang NPC: 10 điểm mốc lọt footprint cầu/sân thượng/tầng 2 đã sửa tọa độ; Y của wanderer bám groundH tại vị trí hiện tại (không nội suy về Y của điểm đích — nguyên nhân phụ gây bay chéo); tuyến nào có Y tường minh (vòng bùng binh) giữ nguyên; guard: dưới cầu/sân thượng mà y<8 thì về mặt đất 0.
### 2. LÊN ĐÈN + KHÓA MÀU (research/13 Phần 8)
- [x] Trời: dome gradient (đêm tím than → ấm ở chân trời; ngày #a8d4f0 pha ấm theo khóa), trăng + halo, mây trôi (ngày rõ/đêm mờ), sao nhấp nháy về đêm.
- [x] Sáng tổng: hemi khóa #ffd9a0/#4a3220 @0.55, exposure đêm khóa 1.05, thêm fill ambient ấm 0.10 (theo brief mục 2b), moonlight 0.38, sương đêm #191209 (khóa), fog 0.0092.
- [x] Đèn rực: halo sprite lớn cho đèn thuộc địa + đèn đường GLB (3.6–3.8), halo sạp 2.5/opacity 0.46, đĩa quầng sáng mặt đất 0.22; CHIẾU SÁNG ĐIỂM NHẤN: 2 spotlight ấm rọi mặt tiền chợ + point light rọi tượng đài.
- [x] KHÓA PALETTE: bão hòa HSV hàng hóa/trang phục 0.45–0.80, kiến trúc 0.15–0.35 (biển hiệu 0.45–0.65), cấm xám không hue (xám ngả ấm hue 0.07), chữ CHỢ ĐÀ LẠT = đỏ nhấn #c8372d, đèn #ff9a3d / ánh sạp #ffb45e, đường #4a4038, plaza xám ấm #8a7f72.
- [x] BẢNG 14 MÀU ÁO CỐ ĐỊNH (đỏ đô, cam đất, vàng mù tạt, kem bơ, xanh rêu, xanh thông, teal, dương, oải hương, hồng đào, hồng sen, nâu cà phê, nâu đất, navy ấm — mọi màu trong dải bão hòa 0.46–0.79): áp cho CROWD_SHIRTS, khăn, màu xe, áo người chơi/ca sĩ; 22 áo tiểu thương trong STALL_DEFS ánh xạ về màu gần nhất trong bảng.
- [ ] Tỉ lệ chibi đầu:thân 1:1.6 — chuẩn đã ghi nhận; KHÔNG dựng lại character.glb đợt này (trần dung lượng + tránh regression), để đợt model riêng.
### 3. HỆ THỐNG GAME (khung "giống game, không phải simulation")
- [x] XP + CẤP "KHÁCH QUEN CHỢ" (đổi tên theo research/13 P0-2): 11 mốc cấp (0→4200 XP), mọi hành động cho XP (mua +6, ăn +4/+10 món mới, coi bói +8, tip +5, chặng dẫn đường +25, chụp ảnh +15, nhặt đèn sao +8, chat +3, hát +4/5s, giao đơn +20/+30); thanh XP + cấp + danh hiệu LUÔN trên HUD; popup "+XP" bay; rung thanh XP khi ≥85% mốc.
- [x] MỤC TIÊU LUÔN HIỆN HỮU: panel nhiệm vụ (dẫn đường + ngày) render động mỗi giây + chip sự kiện góc màn hình (combo/ thuê xe) + dòng tiến độ bộ sưu tập trong panel dẫn đường.
- [x] THỬ THÁCH CÓ ĐIỂM + GIỜ: (a) "Giao hàng nhanh" — đơn mua hộ có t0 + chip đếm ngược, giao <45s +40 Xu (thành tựu ⚡), <90s +20, <150s +8, chơi lại vô hạn; (b) "Săn lồng đèn" — combo 25s, Xu = 10×(1+0.5×(combo−1)), mốc chuỗi ghi comboBest.
- [x] THÀNH TỰU: 14 mục trong Hộ chiếu (mua đầu tiên, ăn 5 món, đủ 9 dấu, xong dẫn đường, 5 ảnh, 3/10 vật ẩn, combo ×4, hát 3 buổi, chat 10 người, 3 đơn, giao nhanh, coi bói 3 lần, cấp 5) — popup + thưởng Xu khi đạt.
- [x] MỞ KHÓA THEO TIẾN TRÌNH (mức danh hiệu/nội dung theo chốt phạm vi — KHÔNG tủ đồ): cấp 3 danh hiệu lên thẻ tên người chơi; cấp 4 mở điểm check-in bí mật sân thượng; cấp 5 thuê xe miễn phí.
- [x] JUICE: SFX WebAudio tự sinh (pop/ting/coin/shutter/level-up), popup XP bay, flash chụp ảnh, rung thanh XP.
- [x] NHIỆM VỤ NGÀY MỞ RỘNG: pool 8 mục xoay theo ngày (chụp 2 ảnh, nhặt 2 đèn sao, chat 3 người, ăn 1 món, tiêu 100 Xu, giao 1 đơn, hát 1 buổi, ngồi ấm 1 lần) — chọn 3/ngày, mỗi mục +40 Xu +30 XP. (Dồn quest 3 ngày = backlog P0 bản sau, KHÔNG làm đợt này theo chốt.)
### 4. GÓI TƯƠNG TÁC MỚI
- [x] a) Check-in chụp ảnh: 6 điểm (tượng đài, mặt tiền, đỉnh đồi, cầu, góc hát, sân thượng-bí mật cấp 4) — vòng sáng + icon 📷, bấm → flash + lưu bộ sưu tập trong Hộ chiếu + 10 Xu + 15 XP; minimap chấm trắng điểm chưa chụp.
- [x] b) Vật ẩn: 10 lồng đèn sao lấp lánh quanh map, đi qua là nhặt; mốc 3/6/10 thưởng +25/+50/+100 Xu + thành tựu Nhà sưu tầm.
- [x] c) Ngồi ăn/uống tại chỗ: ghế trước mọi sạp đồ nóng + quán cà phê — ngồi 3,6s hồi Độ Ấm +11/s, +8 XP, cà phê thêm buff tỉnh táo 30s; di chuyển là đứng dậy.
- [x] d) Trò chuyện NPC: 24 câu chuyện Đà Lạt/chợ luân phiên, bong bóng thoại, +3 XP (mỗi NPC 60s), 25% tặng quà nhỏ/Xu/kẹo dâu.
- [x] e) Hát cùng ở góc hát: nút trong modal sân khấu khi đang diễn — nhún nhảy + nốt nhạc bay, +6 Xu +4 XP mỗi 5s (cap XP hát 60/ngày), ≥10s tính 1 buổi.
- [x] f) Thuê xe máy: bãi thuê trước chợ, 30 Xu/90s (cấp 5 miễn phí), tốc độ 15, xe nghiêng theo hướng lái, chặn leo thang/vào nhà lồng, hết giờ/E là xuống xe. (Làm đủ bản xe máy, không phải thay bằng xe đạp.)
- [x] Mọi tương tác đều có dấu hiệu nhìn thấy + phản hồi (popup/âm/SFX) + ghi vào save `chohb3d-v1` (state.game, save cũ tự migration, KHÔNG phá save).
### Kiểm chứng V4.3
- [x] node --check module JS đạt sau từng patch (1–8). index.html 202.275 → sau patch palette/ cầu ~202.5KB.
- [x] Đóng gói index-standalone.html: 10.450.769 byte (9,97 MB) — dưới trần 10MiB nhưng CHỈ còn dư ~35KB: thêm nội dung nữa phải nén GLB trước.
- [x] Render kiểm chứng scripts/render_v43.py — ĐÃ SOI TỪNG ẢNH: a/b cùng góc v42 (ghép cạnh nhau: renders/v43-vs-v42-a-duong-vao.png, v43-vs-v42-b-vong-xoay.png) — v4.3 SÁNG HƠN RÕ, nền trời ấm thay đen đặc, tượng đài/mặt tiền được rọi, màu áo theo bảng 14; g cầu (góc ngoài — mái kính che deck nên bổ sung bản kiểm tra riêng); h check-in tượng đài ĐẠT (vòng hoa + đèn + người + xe); i góc hát ĐẠT mức mô phỏng (khán giả + nốt nhạc bay, khung hình từ sau sân khấu).
- [x] KIỂM CHỨNG RIÊNG CHO BUG CẦU (renders/v43-bridge-check-endon.png): dựng cầu theo đúng transform web SAU SỬA (xoay +atan) + người đặt theo đúng công thức groundH mới — người đứng TRỌN trên mặt deck, chân chạm sàn, cầu nối đồi (17,14) xuống sân thượng (12,74) liền mạch. Hết "đi trên trời" ở cấp độ hình học + công thức (runtime duyệt bởi người chơi là bước cuối).
- [ ] Lớp runtime (HUD/popup/tương tác thật trong trình duyệt) chưa kiểm chứng trực tiếp được — giới hạn trình duyệt đã biết; kiểm chứng bằng rà code + mock trong render.
- [ ] Đẩy GitHub / upload — KHÔNG làm theo lệnh đợt này (điều phối làm sau khi soi ảnh).

## V4.4 — CHỈ HÌNH/KHÔNG KHÍ ĐÊM (phản hồi chơi thử 02:46 07/11: "tối ôm, không giống đêm Đà Lạt, thiếu chi tiết, không sống động")
Phạm vi khóa: KHÔNG thêm hệ thống game, KHÔNG đụng logic v4.3, KHÔNG thêm GLB mới (chỉ tham số sáng/vật liệu + prop bằng helper sẵn có).
### 1. Độ sáng tổng thể đêm
- [x] Exposure đêm 1.05 → **1.34**; hemi đêm 0.55 → **0.92**; fill ambient ấm 0.10 → **0.26**; moonlight 0.38 → 0.55.
- [x] Sương đêm đổi #191209 → **#4a3420** (nâu ấm bắt sáng) + mật độ 0.0092 → 0.0066: xa mờ thành haze ấm thay vì nuốt vào đen.
- [x] Đèn đường/đèn thuộc địa: PointLight 70 → **120**, tầm phủ 26/30 → 34/36.
### 2. Cụm sáng từng sạp
- [x] **Dây 6 bóng nhỏ** quanh mép mái trước mọi sạp (material dùng chung, đêm #fff3cf) + halo bóng chính 2.5 → 3.4, opacity 0.46 → 0.60.
- [x] **2 vũng sáng glowDisc/sạp** (dưới quầy r2.9 + trước quầy r3.8), wetGlows 0.22 → **0.40** — các vũng chồng lấn dọc dãy như ảnh thật 06.
- [x] Lồng đèn GLB emissive đêm 1.0 → 1.5; lồng đèn giấy lớn 1.6 → 2.3.
### 3. Haze + halo
- [x] Mặt sương: opacity đêm 0.11 → 0.17, thêm 2 mặt sương (dãy sạp mặt tiền + quanh bùng binh); sương sát đất 0.13 → 0.22.
- [x] Khói bếp 0.55 → 0.62, cột hơi lớn 0.34 → 0.50 (bắt sáng thành cột mờ).
### 4. Chi tiết dày (mesh sẵn có trong code, không GLB mới)
- [x] Mọi sạp: thùng hàng xếp chồng 3 lớp cạnh sạp + dãy 4 chai lọ rực trên quầy + 2 chậu cẩm tú cầu trước sạp; cành thông nóc 4 → 6 cụm.
- [x] Sạp rau: thêm 2 mẹt hàng rực (vàng/tím) bày sát đất trước quầy.
- [x] Hoa thảm bùng binh thoát kẹp bão hòa kiến trúc trong clampSat: rule riêng `Flower*` bão hòa 0.62–0.88 + lightness ≥ 0.45.
### 5. Tượng đài + mặt tiền
- [x] monuLight 65 → **150** + dời về phía chợ (-24, 4.2, -2.5); spot mặt tiền 1400 → **2100** ×2.
- [x] **8 đèn viền chân đảo** (emissive ấm, đêm 2.8) + glowDisc r8.6 quanh đảo.
### 6. Xe — điểm sáng chuyển động
- [x] Đèn pha emissive 2.2 → 3.0; chóp sáng 0.16 → 0.27.
- [x] **Đèn hậu đỏ mới**: cầu emissive đỏ gắn sau mỗi xe theo bounding box (moto 1, ô tô 2), đêm 2.8.
### Kiểm chứng V4.4
- [x] node --check module JS đạt (cả index.html và standalone). index.html 203.837 → 207.714 byte.
- [x] Đóng gói index-standalone.html: **10.454.646 byte (9,97 MB)** — vẫn dưới trần 10MiB, dư ~31KB. Không GLB mới nên không cần nén.
- [x] Render kiểm chứng scripts/render_v44.py (gương tham số web) — ĐÃ SOI TỪNG ẢNH:
  - A đường vào (v44-a-duong-vao-dem.png): ĐẠT — sáng/ấm hơn v4.3 rõ, dãy sạp giữa khung lấp lánh điểm sáng, đám đông đọc rõ; nền đường gần camera còn phẳng trong bản render Blender (web có thêm glowDisc đèn thuộc địa phủ khu này).
  - B vòng xoay (v44-b-vong-xoay-dem.png): ĐẠT — quảng trường hết vùng chết tối, mặt tượng phía chợ ấm sáng, thảm hoa lên màu hồng/đỏ, mặt tiền + chữ đỏ rực. Ghép cạnh ảnh thật 05: renders/v44-vs-real-b-vong-xoay.png.
  - H tượng đài (v44-h-checkin-dem.png): ĐẠT — khác hẳn v4.3 (tượng đứng một mình giữa quảng trường trống): có nhóm người chụp ảnh/nói chuyện, xe đèn pha bật, thảm hoa được rọi.
  - E cận sạp (v44-e-can-sap-dem.png): ĐẠT ở lần đặt camera 4 (dùng lại đúng khung đã kiểm chứng của v42 — nhìn dọc dãy sạp từ phía tây): khách đứng trước quầy 2 cụm, lồng đèn tròn + đèn sao + dây bóng lấp lánh dọc mái sạp, zigzag mặt tiền phía trên, nền sáng ấm toàn khung. Ghép cạnh ảnh thật 06: renders/v44-vs-real-e-can-sap.png. LƯU Ý TRUNG THỰC: render Blender không có các prop code-built của web (biển giá, thùng hàng, chai lọ, hũ ly) — phần bày quầy trong render thưa hơn game thật, đã kiểm chứng bằng code + node --check.
- [ ] Lớp runtime thật trong trình duyệt vẫn chưa kiểm chứng trực tiếp (giới hạn đã biết) — render Blender là xấp xỉ ánh sáng web.
- [ ] Đẩy GitHub / upload — KHÔNG làm theo lệnh đợt này.

## V4.4 bổ sung (07/11 — lệnh 03:16/03:21/03:27): MÀU UI + TỦ ĐỒ 60 MÓN
### A. Màu UI theo ảnh chốt CHOT-phong-cach-cho-dem.png
- [x] Lấy mã màu bằng lấy mẫu pixel trực tiếp từ ảnh chốt: panel sô-cô-la #3b281c, CTA vàng #f4be39, viền vàng đồng ~#d7a13e, chữ kem ấm.
- [x] .panel/.sheet: nền gradient nâu sô-cô-la (#58371d→#2b180c), viền vàng đồng 1.5–2px, bo tròn lớn 18px (sheet 22px), highlight mép trên.
- [x] Nút CTA (buyBtn/bigBtn/eatBtn/nút hành động mobile): gradient VÀNG TƯƠI #ffd94d→#f6ad1f, chữ NÂU ĐẬM #4a2405 (trước đây cam nâu #c8871a chữ trắng — lệch ảnh chốt nhất). Nút phụ (sellBtn, hbtn): nền sô-cô-la + viền vàng + chữ kem.
- [x] Toast/modal/itemRow/chữ phụ: kem ấm #ffeec4 / #dcbc8d; dấu hộ chiếu got: viền #f0c268; huy hiệu hồng #e75480 dùng cho chip bộ sưu tập (.setChip).
- [x] CSS riêng tủ đồ: .wdGrid/.wdCard (món đang mặc viền vàng + nền vàng nhạt), .wdBtn, .wdSec, .wdLock.
- [ ] Chưa kiểm chứng trực tiếp trong trình duyệt (giới hạn đã biết) — đối chiếu bằng mã màu lấy mẫu từ ảnh.

### B. Hệ thống Tủ đồ P0-1 (theo research/15 bản 60 món)
- [x] WARDROBE_DEFS đủ 60 món (Mũ 12 · Khăn 8 · Áo 10 · Tay cầm 10 · Phụ kiện 12 · Giày 8), mọi màu thuộc bảng 14 (kiểm bằng script), 118 primitive parts, 13 món họa tiết canvas (caro/sọc/chấm dâu/chấm sao/cánh hoa vẽ bằng code), 5 món phát sáng đêm, 0 GLB mới.
- [x] State: state.wardrobe[] + state.equipped{hat,scarf,coat,hand,shoes,extra[]} trong save chohb3d-v1; migration mặc định wardrobe:['M1'], equipped.hat='M1' — save cũ mở không lỗi (kiểm bằng đọc code + defaults merge; chưa chạy thật trong trình duyệt).
- [x] Đường mua: sạp len1/len2/luuniem/dongho/suatuoi/khoai/banhtrang có mục "🧣 Trang phục" riêng; mua = vào Tủ đồ (không vào Giỏ, không qua chế biến); 6 món goods cũ trùng (Áo len cổ lọ/Khăn choàng/Mũ beanie/Găng/Kính mát/Móc khóa) đã ẩn khỏi menu goods để nối vào tủ đồ.
- [x] Mở khóa đủ loại: cấp 3/4 (13+8 món), dấu hộ chiếu produce/night/đủ 9 dấu, chỉ bán ban đêm (K8/A10/T2), thưởng tự nhận: ăn đủ 5/10/15 món (M12/A4/T9), check-in đủ 6 điểm ảnh (T10), đạt cấp 6 (P12/G8), sở hữu đủ 10 món (A6 mở mua).
- [x] Mặc = hiện trên nhân vật: node HatBeanie/HatNonLa/Scarf có sẵn + tô lại vật liệu riêng của người chơi (không đụng NPC) + group primitive theo neo root/tay/chân; móc khóa đung đưa theo nhịp, đèn cầm tay có PointLight riêng, quầng sáng mặt đất.
- [x] Độ Ấm: tổng ấm đồ đang mặc (kể cả +ấm bộ) cộng thẳng vào thanh Độ Ấm hiển thị + ngưỡng lạnh/chậm/run đều dùng giá trị đã cộng; dòng chữ phụ hiện "🧣 đồ đang mặc +N°". Đối chiếu thiết kế: bộ mua ngay = +45°, bộ đẹp nhất = +64° (script kiểm đạt).
- [x] 5 bộ sưu tập (24 món): đủ bộ +3° (Dã Quỳ +4°) + đặc quyền chạy thật — giảm 10% giá tại sạp thuộc bộ (áp cả menu thường lẫn đồ tủ đồ, nút giá hiện "-10% bộ"), Bộ Cẩm Tú Cầu: cánh hoa rơi quanh người; Bộ Nhà Ga: danh hiệu "🚂 Khách du lịch Đà Lạt" trên thẻ tên; Bộ Chợ Đêm: quầng sáng quanh người rộng hơn; Bộ Dâu Tây: NPC thỉnh thoảng khen trong bong bóng thoại. UI Tủ đồ hiện tiến độ từng bộ x/y.
- [x] UI: nút "🧣 Tủ đồ (n)" cạnh nút Giỏ + phím T; modal lưới theo 6 ô (Mặc/Gỡ, món đang mặc viền vàng), mục bộ sưu tập, mục "Chưa sở hữu" ghi rõ bán ở đâu/điều kiện mở.
- [x] QA từng món: render cận Blender đủ 60/60 món theo từng ô (renders/wd-<id>.png + bảng wd-sheet-*.png) từ CHÍNH spec WARDROBE_DEFS trích xuất từ index.html; soi từng món và sửa tại chỗ: M2 bỏ pom trùng GLB, M5 beret hạ thấp+nghiêng, K5 thêm xoay torus nằm phẳng (lỗi web thật), T8/T9 cán ô lệch ra ngoài tránh xuyên đầu, giày xử lý 3 vòng (khe đen do mặt đồng phẳng với shoe GLB → nới rộng 0.25; nâng hộp phủ kín shoe; G7 đổi sang đế+quai), K3 hộp nối bao kín đuôi khăn GLB (hết ô đen z-fight), M4 xác nhận dải bịt tai vòng qua đỉnh đầu. Thêm 3 ảnh bộ đầy đủ: wd-outfit-basic2 (bộ mua ngay), wd-outfit-chodem (đủ bộ Chợ Đêm), wd-outfit-night.
- [x] node --check đạt; harness Node kiểm dữ liệu: 60 món/id duy nhất/ô đúng số/màu đúng bảng/stallId tồn tại/set đủ 24 món/ấm trong thang/tổng ấm 2 bộ chuẩn — TOÀN BỘ ĐẠT.
- [ ] CHƯA kiểm chứng trong trình duyệt thật (giới hạn đã biết): bấm Mặc/Gỡ, mở modal tủ đồ, mua tại sạp, save cũ nạp lên — đã rà soát bằng code path + node --check, cần Chung Hy chơi thử xác nhận.
- [ ] Họa tiết canvas (caro/sọc/chấm) chỉ kiểm chứng bằng code — render Blender QA chỉ hiện màu nền (đã khai báo rõ, không suy đoán đạt).

### C. ĐỢT CẢI THIỆN (polish — đúng 1 đợt sau QA)
- [x] M3: lá dâu nhô ra khỏi bóng pom GLB (trước bị che khuất) — render lại đạt.
- [x] A6: poncho thu hẹp đáy 0.66→0.60, ngắn lại — bớt xòe như váy.
- [x] K3: tua rua dài 0.13→0.17 cho dễ đọc.
- [x] T2: khung sao thu gọn 0.36→0.32, lõi 0.08→0.075 — sao gọn và rõ hơn.
- [x] M7: vành bucket hạ 1.585→1.565 — tách lớp vành/vòm rõ hơn.
- [x] K3 (phát sinh khi soi ảnh polish): hộp nối đuôi khăn bao kín đuôi GLB — hết ô đen.

### D. Dung lượng
- [x] Standalone sau khi thêm UI + tủ đồ từng VƯỢT trần 12.651 byte → đã cắt 19.569 byte dòng chú thích thuần (không đụng logic; node --check + harness đạt sau cắt). Standalone cuối: 10.478.842 byte (9,99MB), DƯ ~6,9KB — RẤT SÁT TRẦN: đợt sau (lối đi chợ) bắt buộc nén GLB trước theo research/14 mới thêm được nội dung.
- [x] SỬA MUỘN QUAN TRỌNG (từ dump GLB trả về trễ): pivot chân LegL/LegR trong three.js ở y=0.50 (không phải 0.70 như đã giả định khi tính tọa độ) → toàn bộ 18 part neo LEGS (ô Giày G1–G8 + tất P5) đã dịch +0.20 về đúng vị trí web thật; harness QA cũng sửa pivot 0.50 và render lại G1–G8 + P5 đối chứng (vị trí thế giới khớp ảnh đã duyệt, tọa độ local nay đúng pivot thật). Neo tay (1.02) và neo gốc đã đối chiếu dump — không lệch.

## V4.5 — DỰNG LẠI LỐI ĐI CHỢ + NỐI 2 CAO ĐỘ (07/11, theo research/16 mục 4)
### A. Thang lớn + vành đai quanh thang
- [x] stairs.glb dựng lại: rộng 11 -> 22 (làn đi giữa 7 + 2 dải khán đài), chiếu nghỉ sâu 2.5 -> 4 (chuyến A/B/C rút còn 7.25/6.5/6.25), LandingTop hạ cho mặt tấm = đúng stairH (bản cũ lệch +0.345). Bỏ bevel bậc -> GLB 295.044 -> 95.104 byte.
- [x] Sitters 12 -> 28: cụm 2-4 người trên mặt bậc ở 2 dải khán đài (|x| 6.5..9.5), TẤT CẢ quay mặt xuống phố (+z), ghế nhựa xanh dương chủ đạo (75%) điểm ghế đỏ; Chú Ba giữ nguyên ở chiếu nghỉ 1.
- [x] 4 điểm bán TRÊN thang: khoainuong (chiếu nghỉ 1, tương tác đầy đủ + hàng chờ 3), suadau (chiếu nghỉ 2, tương tác + hàng chờ 3), 2 sạp bậc visual (bánh tráng nướng chuyến B, trứng nướng chuyến C, quay mặt ra làn đi, có người bán).
- [x] Đèn tay vịn: 24 bóng InstancedMesh dọc 2 tay vịn suốt 3 chuyến (trục sáng liên tục).
- [x] Thềm ôm sườn: san 2 dải x -19..-11 và 11..14.5 thành 3 vùng thềm bậc thang (14.2/8.5/2.8) có tấm lát đá; 9 điểm hàng rong groundVendor + 5 cụm ghế ngồi ăn trên thềm; thang phụ cầu vồng sườn đông (8 bậc sơn màu + 5 đèn sao).
- [x] Sườn trơn rút còn 2 đoạn ngoài (x -70..-19 và 20.5..70).
### B. Nhà lồng
- [x] Lưới 34 quầy trang trí (áp tường nam/bắc + dãy đôi giữa lưng đối lưng, pitch 5.2) + 6 quầy tương tác = 40 quầy; MỌI quầy trang trí có biển canvas "QUẦY SỐ n" chữ đỏ nền kem + danh mục; bạt luân phiên 6 màu, hàng hóa trên mặt quầy.
- [x] Dời dacsan (-20,20, quay nam) + tra (20,20, quay bắc) từ đồi vào dãy giữa nhà lồng; giữ len1/len2/rau/dau.
- [x] Lửng kính visual dọc tường bắc: sàn lửng (mặt 3.7) + dải kính + lan can + 3 NPC đứng nhìn xuống khu rau.
- [x] Chừa miệng thang trong nhà (không đặt quầy ở góc đông-bắc x>25 z>14).
### C. Thang trong nhà + nối sân thượng (hết "rụng" 12.1)
- [x] Hành lang nối: tấm sàn 12.6 x 21..33 z 7..12.2 + lan can; cửa khung gỗ + biển "XUỐNG CHỢ LA" tại x 29.9..31.5 (qua dải kính mặt tiền).
- [x] Thang trong nhà dọc tường đông x 29..33: 2 chuyến x 10 bậc + chiếu nghỉ giữa 6.55 (innerStairH), vách tây đặc che giao cắt 2 sàn tầng, 2 tấm dốc đỡ bậc, tay vịn.
- [x] Quầy CHỢ LA (giá treo quần áo 6 màu + biển + người bán) trên chiếu nghỉ giữa, chừa lối đi 2.2 phía tây.
### D. Đồi (sau khi dời đặc sản/trà)
- [x] 2 quán cà phê sân hiên ở mép đồi z -32.5 (sàn gỗ, quầy pha chế, 2 bàn/quán, khách ngồi quay xuống chợ) tại (-17) và (17.5); 3 ki-ốt (bánh mì/nước mía/đồ chơi) ôm quảng trường, có solid.
- [x] Điểm nhìn xuống: lan can 2 bên miệng thang + ống nhòm + 4 NPC đứng ngắm.
### E. Dòng người
- [x] Tuyến LOOP khép kín (21 điểm): đường chợ -> thang (x -2) -> đồi -> cầu -> sân thượng -> hành lang -> thang trong nhà -> nhà lồng -> cửa chính -> đường chợ; 6 wanderer (4 xuôi + 2 ngược, lệch tốc độ/lịch).
- [x] 5 tuyến thang chuyên: x -3/-2.5/-2/+2.5/+3 (làn lệch, không ai đi giữa trục nữa; tuyến x=0 và x=1 cũ đã sửa).
- [x] Quét số học groundH (chạy bằng chính code JS): LOOP nhảy tối đa 0.61 = 1 bậc thang; các vị trí đặt người/sạp đúng cao độ thiết kế.
### F. SỬA LỖI LỚN PHÁT HIỆN KHI QUÉT SỐ (ngoài đặc tả, phải báo)
- [x] stairH cũ có t NGƯỢC DẤU ở cả 3 chuyến (t = (-30-z)/run): chiều cao phình tới 22.67 ở chân chuyến A, người chơi/NPC trên thang LƠ LỬNG dần tới +10.8 so với mặt bậc GLB — tồn tại từ các bản trước, không ai cô lập được vì render các đợt trước không soi cận thang và công thức port sang harness cũng sai giống hệt. Đã viết lại theo u đo từ đỉnh chuyến; kiểm chứng 10/10 điểm khớp mặt bậc GLB (build_stairs) + render m2/c cho thấy người ngồi/đi ĐÚNG mặt bậc.
### G. Kiểm chứng V4.5
- [x] Render full harness render_v45.py (9 góc, 185 người): a-duong-vao, b-vong-xoay, h-checkin, e-can-sap KHÔNG hồi quy; c-chan-thang đạt (thang rộng kín khung, sitters đúng bậc, sạp chiếu nghỉ, thềm); f-trong-cho đạt (nội thất đêm ấm, hàng quầy + biển chạy dài — sau khi sửa biển trong harness từ phát sáng sang vật liệu thường như web).
- [x] Render mini render_v45_mini.py: m2 chân thang (sitters đúng mặt bậc sau sửa stairH), m5 trong chợ rộng (40 quầy dày đặc), m4 hành lang nối (người đứng đúng mặt sàn 12.6), m7 trong thang (người bán chợ la + giá áo trên chiếu nghỉ giữa).
- [x] node --check đạt sau mọi patch; save chohb3d-v1 không đụng (không sửa cấu trúc state).
- [ ] Góc d-giua-thang (full) lệch khung thành cận cảnh hàng chờ suadau; góc i-doi-nhin-xuong tiền cảnh bị mặt đồi che trục thang — 2 góc này do c/m2/m5 gánh thay; thân thang trong nhà không chụp được từ ngoài (không gian kín, vướng sàn tầng) — kiểm chứng bằng quét số học + m7 từ bên trong.
- [ ] Chưa chạy được game thật trong trình duyệt (giới hạn đã biết): tuyến LOOP + tương tác 2 sạp chiếu nghỉ mới cần Chung Hy chơi thử xác nhận; đầu chuyến 1 thang trong nhà có đoạn ~2 unit đầu người chơi có thể chạm mép sàn tầng 2 (slab GLB phủ tới z 11.4) — đã ghi nhận, chấp nhận ở mức trang trí cửa che một phần.
- [ ] Cà phê hiên đồi chưa có ảnh cận riêng (thấy trong toàn cảnh a + đúng cao độ bằng số học).
### H. ĐỢT CẢI THIỆN (polish — đúng 1 đợt sau QA)
- [x] 4 sạp đêm ôm miệng thang (bánh ướt cuốn/nước mía/chè ba màu/bắp xào) ở (+/-13, 2) và (+/-17.6, 1.6), quay mặt vào miệng thang, có người bán; dịch 2 cụm chat chân thang về (+/-10.8, 2.6) tránh trùng.
- [x] Đèn dẫn đường: PointLight hành lang nối (27, 14.6, 10.8) + quầy chợ la (31, 8.8, 19.4), đẩy vào lampLights sẵn có (tự bật đêm/tắt ngày theo applyDayNight).
- [x] KHÔNG đổi sáng tổng thể web: harness render đọc sáng hơn game thật (khác tone mapping); thông số đêm v4.4 đã được Chung Hy duyệt khi chơi thử — không chỉnh mù.
### I. Dung lượng
- [x] stairs.glb 295.044 -> 95.104 byte (bỏ bevel bậc + LandingTop). Standalone cuối: 10.230.277 byte (9,76MB), DƯ 255.483 byte dưới trần 10MiB — từ thế dư ~7KB (v4.4) thành dư ~250KB.
- [x] Không đẩy GitHub, không upload (điều phối làm).

## V4.6 — SỔ ĐẶC SẢN + QUEST NGÀY DỒN 3 NGÀY + CÂN BẰNG XP/KINH TẾ (07/11, theo research/14 P0-3/P0-4)
### A. Tab Sổ Đặc Sản trong Hộ chiếu (P0-3)
- [x] Danh sách suy TỰ ĐỘNG từ menu bán thật trong STALL_DEFS (không bịa món): **39 món / 5 khu** — Ẩm thực nóng 14 · Sữa & đồ uống 12 · Nông sản 6 · Hoa tươi 2 · Đặc sản mang về 5. Gồm đủ món research/14 nêu: dâu tây, kem bơ, atiso, mứt dâu, hồng treo gió, trà, cà phê, bánh tráng nướng, sữa đậu nành. Loại trừ đúng: đồ len/kính mát/đồng hồ/móc khóa/bưu thiếp (không phải đặc sản ăn uống). Món bán ở 2 sạp (Sữa đậu nành nóng...) chỉ tính 1.
- [x] Ghi sổ khi MUA XONG (finishCooking — món vào giỏ) và khi ĂN/UỐNG (eatItem, đường dự phòng); mỗi món lưu ngày mua dd/mm/yyyy trong `state.soDacSan{}`; icon emoji theo từ khóa món (canvas/CSS, 0 GLB mới).
- [x] UI trong Hộ chiếu (phím P): mục "📖 Sổ Đặc Sản Đà Lạt" — tổng X/39 + % + mốc thưởng tiếp theo; từng khu có dòng % riêng; ô đã có: ✔ + icon + ngày mua; ô chưa có: tên mờ để biết mà săn. Toast "📖 +1 Sổ Đặc Sản: <món> (X/39)" + +5 XP/món mới.
- [x] Thưởng mốc bộ sưu tập: 5 món +30 Xu/+20 XP · 10 món +50/+30 · 20 món +80/+50 · 30 món +120/+80 · ĐỦ BỘ 39 +250/+150 (tổng 530 Xu + 330 XP, một lần). Thêm 2 thành tựu: 📖 Sưu Tầm Đặc Sản (20 món, +60 Xu), 🏅 Bậc Thầy Đặc Sản (đủ bộ, +120 Xu) — tổng thành tựu 14 -> 16.
- [x] Migration save cũ: `state.soDacSan{}` + `state.dacSanGot{}` mặc định; backfill từ `state.eaten` cũ (món đã ăn từ các bản trước tự vào sổ, đánh dấu "Từ trước"); mốc đã qua nhờ backfill chỉ đánh dấu, KHÔNG phát thưởng ngược.
### B. Quest ngày dồn tối đa 3 ngày (P0-4, phần dồn — quest sinh từ NPC để đợt khác theo phạm vi giao)
- [x] `G.dailyCarry[]` (migration mặc định []): qua ngày, quest chưa xong của ngày cũ dồn sang với NGUYÊN tiến độ + ngày gốc; quest đã xong không dồn; ở lại khi tuổi đời < 3 ngày (ngày gốc + 2 ngày dồn), **sang ngày thứ 4 thì rớt** (lọc bằng dayDiff tại mỗi lần chuyển ngày, kể cả nghỉ nhiều ngày mới vào lại).
- [x] dailyProg tính tiến độ đồng thời cho quest hôm nay VÀ quest tồn trùng loại; xong quest tồn: thưởng như quest ngày (+40 Xu/+30 XP) + toast riêng "Xong thử thách TỒN từ d/m".
- [x] UI panel mục tiêu: mục "↩️ Tồn từ hôm trước" liệt kê từng quest tồn kèm ngày gốc + "còn N ngày"; panel cũng hiện tiến độ Sổ Đặc Sản (polish).
### C. Cân bằng XP/kinh tế (chỉ chỉnh số/bảng hằng — trước -> sau)
- [x] Quest "🛒 Mua sắm": goal **50 -> 100 Xu** (khớp mô tả nhiệm vụ đã ghi ở v4.3 "tiêu 100 Xu"; bản cũ 1 món 55 Xu là xong ngay, quá dễ so với các quest còn lại).
- [x] Thưởng quest ngày: rải rác 40 Xu/30 XP viết cứng -> gom 1 bảng hằng `DAILY_REWARD_XU=40 / DAILY_REWARD_XP=30`, áp thống nhất cho quest hôm nay + quest tồn (trước đây quest quá ngày = mất trắng 0 Xu).
- [x] Nguồn XP/Xu mới có bảng riêng: `DACSAN_XP_NEW=5` XP/món mới; mốc Sổ 30/50/80/120/250 Xu + 20/30/50/80/150 XP (mục A). LEVELS giữ nguyên (tổng XP mới ~525 XP trọn đời sưu tầm ≈ nửa cấp cuối — không phá nhịp lên cấp).
### D. ⚠️ SỬA LỖI TREO GAME GỐC TỪ V4.3 (phát hiện nhờ harness V4.6 — NGOÀI phạm vi giao, đã sửa vì chặn cả hệ quest)
- [x] Gốc rễ: vòng chọn 3 quest ngày trong ensureDaily dùng `(seed * 1103515245 + 12345) >>> 0` — tích vượt 2^53, JS mất chính xác bit thấp -> `seed % 8` kẹt ở 0/1 -> **vòng while lặp VÔ HẠN** (kiểm chứng độc lập trên thuật toán gốc: treo với mọi ngày thử 04–09/11). ensureDaily được gọi từ renderQuestPanel/updateHUD nên bản web thật có nguy cơ đóng băng ngay khi panel nhiệm vụ chạy — các đợt trước không bắt được vì lớp runtime chưa từng chạy được trong trình duyệt ở môi trường này (đã khai báo là giới hạn từ v4.3).
- [x] Đã sửa: Math.imul (nhân 32-bit chính xác) + chặn 200 vòng + lấp đầy tất định. Kiểm chứng: ensureDaily ổn định qua 10 ngày liên tiếp, mỗi ngày đúng 3 quest khác nhau.
### E. Kiểm chứng V4.6 (harness Node chạy CODE TRÍCH NGUYÊN VĂN từ index.html — /tmp/harness46.js + harness46b.js)
- [x] Phần A Sổ (34 test): tổng 39 món, đúng số theo khu, không trùng tên, có mặt các món research/14 nêu, loại trừ đúng đồ len/lưu niệm, icon khớp món mẫu, ghi sổ + ngày đúng định dạng, mua trùng không ghi lại, món ngoài sổ bỏ qua an toàn, mốc 5 phát thưởng đúng, XP cộng đúng (5×5+20=45), đủ bộ 39/39 tổng thưởng 530 Xu.
- [x] Phần B Quest dồn (18 test): ngày 1 phát 3 quest (không treo), xong 1 quest +40 Xu, quest dở dồn sang ngày 2 nguyên tiến độ, quest xong không dồn, làm tiếp quest tồn -> xong + rời sổ + +40 Xu, ngày 3 quest ngày 1 còn (còn 1 ngày trên panel), ngày 4 rớt đúng hạn, ngày 5 quest ngày 2 rớt đúng hạn, 10 ngày liên tiếp ổn định.
- [x] Phần C Migration (9 test): save v4.5 (không có field mới) nạp nguyên xu/nâng cấp/game; field mới mặc định đúng; backfill 6/7 món eaten hợp lệ (loại 1 món lạ); mốc 5 đánh dấu không phát thưởng ngược.
- [x] Phần D Render (5 test, DOM stub): header 6/39 + mốc tiếp theo; đủ 5 khu × (tiêu đề + lưới); ô đã có hiện "🗓 Từ trước"; món chưa có hiện tên mờ.
- [x] node --check đạt cho module JS của cả index.html và index-standalone.html sau mọi patch.
- [ ] CHƯA kiểm chứng trong trình duyệt thật (giới hạn đã biết của môi trường): bấm mở Hộ chiếu xem tab Sổ trực quan, mua tại sạp thật, để qua ngày thật — đã thay bằng harness chạy code thật + DOM stub như trên; cần Chung Hy chơi thử xác nhận, ĐẶC BIỆT là xác nhận bản web không còn nguy cơ treo ở panel nhiệm vụ.
### F. ĐỢT CẢI THIỆN (polish — đúng 1 đợt sau QA)
- [x] Toast khi chuyển ngày có quest được dồn: "↩️ N thử thách từ hôm trước chưa xong đã được DỒN sang hôm nay — làm tiếp trong vòng 3 ngày nhé!" (trước đây dồn lặng, người chơi dễ tưởng quest biến mất). Có test riêng trong harness B.
- [x] Panel mục tiêu luôn hiện dòng "📖 Sổ Đặc Sản: X/39 món đã ghi" để tiến độ sưu tầm nhìn thấy ngay ngoài HUD, không cần mở Hộ chiếu. Có test riêng trong harness B.
### G. Dung lượng
- [x] index.html 249.929 -> 261.202 byte (+11.273). Đóng gói lại index-standalone.html: **10.241.550 byte (9,77MB)**, DƯ 244.210 byte dưới trần 10MiB. Không GLB mới, không cần nén thêm.
- [x] Không đẩy GitHub, không upload (điều phối làm).

## ĐỢT MODEL (07/11, sau V4.6) — CHIBI + KHOÉT SLAB
### A. Nhân vật chibi (character.glb dựng lại trong scripts/build_models.py, giữ nguyên tên node LegL/LegR/Torso/tmpCollar/ArmL/ArmR/Head/HatNonLa/HatBeanie/HatCap/Scarf)
- [x] Gốc tỉ lệ: research/13 ghi "đầu:thân ≈ 1:1.6". ⚠️ CHÊNH LỆCH ĐỊNH NGHĨA cần biết: đo bản CŨ theo KHỐI đầu (node Head 0.877 trên tổng 1.937) thì đầu:dưới-đầu = 1:1.21; đo theo MẶT (cằm->chân tóc 0.57) thì 1:1.86. Ảnh chốt (thước đo số 1) + mau-np-02: đầu ≈ 45–54% chiều cao. -> ĐÃ DỰNG THEO ẢNH CHỐT: đầu ≈ 50% chiều cao (khối đầu 0.924/1.824); theo cách đo MẶT bản mới = 0.57 : dưới-mặt 0.90 = **1:1.58 ≈ 1:1.6 của research/13**; theo cách đo khối-đầu là ~1:0.97. Nếu hiểu 1:1.6 theo khối-đầu thì đầu phải NHỎ đi — ngược mô tả "đầu to" và ngược ảnh chốt. Chờ Chung Hy chốt lại định nghĩa nếu muốn khác.
- [x] Thông số mới (dump GLB thật kiểm chứng): tổng cao 1.824 (cũ 1.937); pivot chân (±0.12, 0.40) (cũ 0.50); thân pivot 0.66, bbox 0.355–1.000; tay pivot (±0.40, 0.88), hình học local tay GIỮ NGUYÊN (đáy local −0.505) nên mọi part neo tay không phải dịch; đầu pivot 1.35, bbox 0.900–1.824; giày giữ nguyên 0–0.12 (chân không lún/nổi).
- [x] character.glb 459.580 -> 457.688 byte (−1.892).
### B. Tủ đồ 60 món hiệu chỉnh theo neo mới (WARDROBE_DEFS, transform bằng script /tmp/wd_transform.py)
- [x] Phương pháp: HEAD quanh tâm đầu 1.48->1.35 hệ số 1.0714 (M2/M3/M4/M5/M7/M10/M11/M12/P3 + chỉnh riêng vòng M2, vành M7, kính P3...); TORSO quanh 0.82->0.66 (y ×0.91, x ×1.08, z ×1.06; A2/A9/A4/A5/A6/P2/P6/P7/P9/P12 + nới size áo khoác/poncho/túi); LEGS +0.10 giữ vị trí thế giới (G1–G8, P5); A1/K5 neo cổ theo cổ mới 0.905/0.96; sway P4/P10/P11 theo hông mới; part neo AR/ARMS giữ nguyên (local tay không đổi).
- [x] Harness scripts/render_wardrobe.py (PIVOT + khung máy theo thân mới) render lại TOÀN BỘ: soi TỪNG ảnh 60/60 món + P2 góc sau + 2 outfit (basic/night), đối chiếu bộ wd-* cũ đã duyệt (/tmp/wd_old) — **60/60 ĐẠT, không món nào lệch phải sửa thêm**. node --check đạt sau patch.
### C. Tư thế ngồi (NPC + người chơi dùng chung model)
- [x] Render ngang bằng phép xoay ma trận quanh pivot hông (đúng −1.45 của sitPose web): đùi gập ngang, giày hướng trước — tư thế ngồi đúng trên model mới (renders/model-compare-sit.png).
- [x] Số đo điểm tiếp xúc ghế nhựa (mặt ghế 0.325 theo stoolWorld; offset ngồi web +0.30 NPC/+0.28 người chơi GIỮ NGUYÊN): khe dưới đùi bản cũ 0.36 -> bản mới **0.26** (hông hạ 0.50->0.40 nên ngồi SÁT ghế hơn trước, không tệ đi). Không chỉnh offset ngồi trong đợt này: hạ về ~+0.04 để chạm tuyệt đối sẽ đổi quan hệ chiều cao với bàn/sạp/đạo cụ toàn chợ — thuộc đợt tinh chỉnh gameplay riêng nếu Chung Hy muốn.
- [x] Người đứng/ngồi trên thang: groundH/stairH/innerStairH không phụ thuộc chiều cao nhân vật (chỉ vị trí chân) — không phải sửa; tổng cao giảm 1.937->1.824 nên mọi khoảng trống đầu đều tăng +0.11.
### D. Khoét slab market.glb (build_market trong scripts/build_models.py)
- [x] Floor2: 3 mảnh, giếng blender x 28.6–33.65 × y 4.4–8.7 (= web z 11.3–15.6); Floor1: 4 mảnh, giếng y −3.8..1.8 (= web z 18.2–23.8). Dump GLB xác nhận đúng tọa độ các mảnh + WellTrim/WellRail.
- [x] Viền fascia ConcreteDk quanh miệng khoét 2 tầng (WellTrim1W/S/N, WellTrim2W/S) + lan can MetalDark miệng giếng Floor2 mép tây + nam (WellRail2*: trụ + 2 tay vịn, kiểu RoofRail).
- [x] Khoảng trống đầu tại mép hẹp nhất (nhân vật mới cao 1.80 tới đỉnh đầu cầu; nón lá tới 1.99 tính riêng): mép nam giếng Floor2 (web z 15.6): đầu 9.575+1.80 = 11.38 < đáy slab 12.625 (dư 1.24); mép nam giếng Floor1 (web z 23.8): 3.53+1.80 = 5.33 < 6.325 (dư 0.99). Nón lá (đỉnh 1.99): 11.57 < 12.625 vẫn dư 1.06.
- [x] Kiểm hình bằng CUTAWAY (chỉ giữ Floor/Well* + bậc xấp xỉ theo code + nhân vật tại 4 điểm): renders/model-well-a (miệng giếng + lan can từ hành lang), model-well-b (mặt đứng ortho: 2 slab + 2 miệng khoét + đầu nhân vật dưới mép slab — rõ khoảng trống), model-well-c (chiếu nghỉ trong giếng Floor1). Lưu ý: sàn hành lang Floor2 trong web là geometry CODE (mặt 12.6 theo groundH), không thuộc GLB nên không có trong cutaway.
- [x] market.glb 1.569.348 -> 1.632.756 byte (+63.408 do thêm mảnh/viền/lan can — đã lường trước, vẫn dưới trần).
### E. ĐỢT CẢI THIỆN (polish — đúng 1 đợt sau QA)
- [x] Thẻ tên người chơi hạ theo đầu mới: playerTagSpr y 2.42 -> 2.22 (mép dưới thẻ 1.945 = đúng đỉnh beanie mới; bản cũ để 2.42 sẽ lơ lửng cao hơn đầu mới ~0.2). node --check đạt cho cả index.html + index-standalone.html.
### F. Dung lượng + đóng gói
- [x] index.html 261.202 -> 261.344 byte (+142). Đóng gói lại: **index-standalone.html = 10.323.712 byte**, DƯ 162.048 byte dưới trần 10MiB (10.485.760). GLB raw tổng 7.546.292 byte.
- [x] Save `chohb3d-v1` không đổi schema — không migration.
- [ ] CHƯA kiểm chứng trong trình duyệt thật (giới hạn môi trường đã biết): nhân vật mới đi/ngồi thật trong game, Mặc/Gỡ tủ đồ tại runtime, đi thang trong nhà xuyên giếng mới — đã thay bằng dump GLB + harness render Blender soi từng món/cutaway như trên; chờ Chung Hy chơi thử bản standalone mới.
- [x] Không đẩy GitHub, không upload (điều phối làm).

## V4.7 (07/11) — CHƠI ĐƯỢC + ĐÔNG + RỘNG (theo phản hồi chơi thử 22:50: "không biết chơi như nào", "ít người quá", "đường vào nhỏ xíu", "có sương mù nhẹ")
### A. Dẫn chơi "một việc một lúc" (mục quan trọng nhất)
- [x] Chuỗi hướng dẫn lần đầu "Lần đầu đi chợ" 6 bước, mỗi lúc CHỈ 1 thẻ lớn #tutCard (chữ 21px) ghi đúng 1 câu việc: (1) tới vòng sáng sạp sữa đậu nành (2) mua 1 ly Sữa đậu nành nóng (3) uống ly sữa hồi ấm (4) leo thang lên quảng trường (5) nói chuyện với 1 người đi chợ (6) mở Hộ chiếu. Xong bước thẻ tự chuyển; thưởng 15 Xu + 10 XP/bước, bước cuối 50 Xu + 20 XP (tổng 125 Xu / 70 XP).
- [x] Móc sự kiện thật: buyItem (đúng sạp 'sua' + đúng tên món) -> tutFlags.sua; eatItem -> drank; G.chats++ -> chatted; openPassport -> pass. Bước 1 check khoảng cách tới front sạp <3m; bước 4 check playerState.y > 15,5.
- [x] Tại đích luôn có cột sáng/vòng sáng (dùng chung beacon của hành trình; tickGuide nhường điều khiển beacon cho tickTutorial khi hướng dẫn đang chạy) + mũi tên 8 hướng theo camera + khoảng cách (m) trên thẻ. Bước tại chỗ (3, 6) thì cột sáng tắt.
- [x] TỰ ĐI (auto-walk): đồ thị waypoint AW_NODES 36 nút (trục chính khớp tuyến LOOP/hành trình + 5 nhánh: dãy sạp đông/sạp sữa, trong nhà lồng, cầu->sân thượng->thang trong, sạp trên thang, Chú Ba, đồi tây) + BFS findAwPath. Bấm thẻ hướng dẫn hoặc panel 🧭 = nhân vật tự đi; WASD/joystick/E/xe/ngồi đều hủy ngay. Có dòng "🚶 Đang tự đi…" trên thẻ (polish).
- [x] Sau hướng dẫn: dòng đầu panel mục tiêu = "➡️ VIỆC TIẾP THEO" duy nhất (ưu tiên: bước hướng dẫn -> chặng hành trình -> nhiệm vụ chính -> quest ngày -> tự do), luôn kèm mũi tên + khoảng cách, cập nhật mỗi frame (refreshNextTaskLine). Trong lúc hướng dẫn panel 🧭 ẩn để đúng "một việc một lúc".
- [x] Prompt tương tác #ctxPrompt: chữ 15 -> 17,5px, viền vàng 2px + nhấp nháy sáng (ctxPulse), thêm cursor pointer + BẤM VÀO PROMPT = tương tác (trước đây chỉ phím E/nút mobile). Nút Bỏ qua hướng dẫn có; lưu state.tutorialDone + state.tutStep.
- [x] Migration save chohb3d-v1 KHÔNG phá: save cũ có tiến độ (guide.stage>0 / guide.done / questDone / xp>0) tự coi như đã qua hướng dẫn; save đang học dở (tutorialDone=false đã lưu) được tôn trọng. Harness kiểm 5 trường hợp migration đạt.
- [x] HARNESS /tmp/harness47.js (trích nguyên văn code thật + DOM stub): **48/48 đạt** — mô phỏng đủ 6 bước (kèm thưởng đúng số), auto-walk spawn -> sạp sữa tới nơi cách front 1,30m (~14,1s ở tốc độ đi bộ, qua đúng nút nhánh 22,7.2), auto-walk sạp sữa -> đỉnh thang đạt y=17 (qua check bước 4), groundH/baseY, đếm người.
### B. Tăng người 185 -> ~300 (đếm bằng code, runtime có window.NPC_STATS in console)
- [x] Hàng chờ 34 -> 49 (+15): thêm banhcan 3, supcua 3, yaourt 2, hoa 2; tăng sua 3->4, caphe 3->4, banhtrang 3->4, dau 4->5, xien 4->5.
- [x] Khán đài thang 28 -> 40 người ngồi (+12 cụm mới cả 3 chuyến + 2 chiếu nghỉ).
- [x] Cụm đứng chuyện 28 -> 51 (+23): quảng trường đồi +10, dọc phố chợ đêm +8, hai vệ đường vào +5.
- [x] Nhà lồng: +28 người mua đứng trước 34 quầy trang trí (chạy lại đúng logic bỏ quầy của code dựng quầy; ~80% quầy có khách) + 4 wanderer đi lối giữa trong nhà (sàn 0,5).
- [x] Wanderer +16 tổng cộng: tuyến LOOP 6 -> 10 (+4), trong nhà lồng +4 (ở mục trên), đường vào +4, quảng trường trước chợ/bùng binh +4.
- [x] Tĩnh mới: vòng bùng binh + thềm thang 8, ngắm hàng trước dãy sạp mặt tiền 8 (z 6,4 bám đất), ngồi trước dãy nhà bắc 3, hàng rong thêm 2 đầu đường vào 2. TỔNG CỘNG THÊM +115 -> **~300 người**.
- [x] Bộ đếm theo khu npcZoneOf gắn vào addStatic/addWanderer/người bán: window.NPC_STATS {duong-vao, bung-binh, pho-cho-dem, nha-long, thang, doi, ven-cho, tong} + console.log khi nạp game (số runtime CHƯA quan sát được trong trình duyệt thật — xem mục Chưa kiểm chứng).
- [x] Xe đậu: hàng trước mặt tiền lùi z 11,25 -> 11,75 (~56 xe) + 2 hàng dọc đường vào bám dốc (parkedRowY dùng entryRampY, ~31 xe) + phía đông trước chợ 8,9 (~8 xe) -> tổng xe đậu ~100+.
### C. Đường vào rộng + tỉ lệ chợ lớn (đo trước/sau)
- [x] Mặt đường chính 170x11 @z2 -> **170x18 @z1,5** (z -7,5..10,5); đoạn dốc vào 31x11 -> 31x18; vỉa hè nam 2,4 -> 3,0 @z12,4, vỉa hè bắc 1,8 -> 2,6 @z-9,2; vạch qua đường sâu 8,8 -> 15. Sân lát đá trước mặt tiền 7,6 -> 9,5 @z10,4.
- [x] Dãy nhà lùi: nam z 12,2 -> 16,5 (mặt tiền 9,4 -> 13,7), bắc -13,5/-14,5 -> -18/-19, khách sạn HotelD 15,5 -> 20,5; khói bếp theo nhà. Đèn thuộc địa ra mép mới (-8,6 / 11,9), cẩm tú cầu 13,6 / -10,4, dây đèn 12,2 / -8,4, biển tên đường -8,0.
- [x] Dãy 10 sạp mặt tiền/đường vào z 8,4 -> 10,15 (front 6,3 -> 8,05); vùng groundH dốc vào z -5,5..10,5 -> -9..13,5 khớp đường mới; AREA_ZONES đường vào nới -12..16; guide chặng 3 tz -> 10,15; làn xe chạy -1,5 / 4,5; minimap vẽ lại đường + thang rộng 22.
- [x] SỬA LỖI TIỀM ẨN phát hiện khi rà soát (có từ V4.5, V4.7 dời sạp mới lộ hẳn): groundH ở dải x 21..33, z 7..12,2 trả 12,6 (mặt hành lang sân thượng cho tuyến LOOP) khiến 3 sạp sữa/cà phê/yaourt bám baseY=12,6 và hàng chờ (front mới 8,05, pz>=7) bị kéo lên cao. Đã sửa gốc: baseY ngoại lệ = 0 cho dải đó; hàng chờ bám s.baseY thay vì tự hỏi groundH; onElevated của người chơi + thêm rect hành lang đông (đi bộ dưới hành lang không bị nhấc lên); cột sáng hướng dẫn đặt ở cao độ người chơi khi đích nằm dưới hành lang; người ngắm sạp đặt z 6,4. Harness có test riêng cho cả cụm này.
- [x] Sửa luôn 2 điểm chìm/lệch: người ngồi trước nhà phố nam z 9,9 (TRONG thân nhà cũ) -> 13,0 trước mặt tiền mới; hàng rong (-58,-9,9) và (-70,-9,9) nằm ngoài rect dốc vào -> kéo về z -8,6 trên vỉa hè bắc.
- [x] Render đối chiếu cùng góc (scripts/render_v47.py = gương v45 + hình học/crowd mới): v47-a-duong-vao (mật độ trung cảnh tăng rõ, dải đất thoáng rộng hơn), v47-b-vong-xoay (cụm người trước mặt tiền đông hơn), v47-f-trong-cho (lối đi trong nhà CÓ người mua đứng trước quầy — bản v45 trống trơn); ảnh ghép trước/sau: renders/v47-a-duong-vao-truoc-sau.png + v47-b-vong-xoay-truoc-sau.png. Đối chiếu ảnh thật 05/06: hướng đi đúng (mặt phố rộng + người tràn + xe đậu kín vệ) dù tỉ lệ game vẫn nén hơn ảnh thật.
### D. Sương Đà Lạt rõ hơn
- [x] Thêm 3 dải sương trôi: ngang đường vào (-56, y2,0, rộng 44, trôi 0,30), chân thang (0, y1,5, rộng 34, trôi 0,12), là là quanh bùng binh (-24, y1,1, rộng 34, trôi 0,10); dải trước dãy sạp chỉnh z 9 -> 7 (trước front mới).
- [x] Thêm 2 đĩa sương mặt đất: chân thang r12 (0, 0,3, 2) + đoạn bằng đường vào r12 (-52, 0,32, 2). Độ mờ đêm: sương trôi 0,17 -> 0,24, đĩa mặt đất 0,22 -> 0,32; GIỮ nguyên fogBase 0,0066 để không nuốt mặt tiền/sạp.
### E. ĐỢT CẢI THIỆN (polish — đúng 1 đợt sau QA)
- [x] Thẻ hướng dẫn top 122 -> 138px (tránh đè panel mục tiêu khi chữ xuống dòng ở màn hẹp) + thẻ hiện "🚶 Đang tự đi…" khi auto-walk đang chạy. Sau polish: node --check đạt + harness chạy lại 48/48.
### F. Dung lượng + đóng gói
- [x] index.html 261.344 -> ~282KB. Đóng gói lại: **index-standalone.html = 10.344.519 byte**, DƯ 141.241 byte dưới trần 10MiB (10.485.760). Không GLB mới (chỉ code + dữ liệu mảng) nên không cần nén.
- [x] node --check đạt cho cả index.html và index-standalone.html sau mọi patch (A, B, C, C-fix, D, polish).
- [ ] CHƯA kiểm chứng trong trình duyệt thật (giới hạn môi trường đã biết — trình duyệt được quản lý chặn loopback/domain): luồng bấm thật (bấm thẻ -> tự đi có va chạm trượt dọc sạp trong collide() thật, mở/đóng modal giữa chừng), FPS với ~300 NPC, số NPC_STATS in ra ở runtime, sương billboard trong web (harness Blender chỉ là xấp xỉ), thẻ hướng dẫn trên màn hình mobile thật. Đã thay bằng: harness Node trích nguyên văn 48/48 + render Blender soi 3 góc. Chờ Chung Hy chơi thử bản standalone mới.
- [x] Không đẩy GitHub, không upload (điều phối làm).
