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

## V4.8 (07–08/11) — SỬA THEO KHUNG HÌNH (đặc tả research/17, nghiệm thu bằng mắt 2 góc chuẩn)
### A. Mặt tiền (GLB market qua build_models.py)
- [x] Xóa toàn bộ cửa cuốn xám đóng (Shutter/ShutterLine/ShopDark) — thay 7 ô CỬA HIỆU MỞ: tường hậu phát sáng (MarketWin/AdLED), kệ + quầy + hàng + đèn hộp bên trong, đọc được từ góc bùng binh.
- [x] Thân mặt tiền có nhịp: AdBand 1,20 + AdInset hai tông + AdFrame; lam thêm Mullion3/Rail3; mái hiên sọc gộp 1 mesh; hàng thông trụ mái mảnh lại (đỉnh 23,95).
- [x] market.glb 1.632.756 -> 1.634.008 byte.
### B. Đảo bùng binh (GLB roundabout)
- [x] Đảo R 6,6 -> 10,5; thảm hoa quạt + hoa cầu 4 vành; vành ghế đá R 11,9; đĩa vành đường r16 quanh đảo; vành xe đậu 9 moto + 3 ô tô.
- [x] Tượng đài: bệ hộp trơn -> 6 tảng đá xẻ jitter + 3 người robe cao 2,30 + thông đá (đỉnh 9,56); tượng LỆCH tây-nam khỏi trục chữ — từ góc A đọc TRỌN "CHỢ ĐÀ LẠT" (v4.7 bị che còn "Ợ ĐÀ LẠT").
- [x] roundabout.glb 1.500.476 -> 1.313.708 byte.
### C. Cái bát đô thị + đường vào (web)
- [x] Nhà hai bên đường vào nâng 4–5 tầng, dãy bắc SÁT vỉa hè (bỏ lùi 6–8u); tường khách sạn cao khép khung phía đông.
- [x] Sườn đồi tây: groundH tách nhánh thềm phẳng + sườn gần đảo chỉ còn đoạn z −30..−16 — mảng tường xanh chắn khung A giảm mạnh; đợt polish thêm 4 thông + 2 đèn phá mảng phẳng sườn.
- [x] Cầu nổi: trụ scale 0,78, lan can/kính/mái hạ thấp + mảnh (GLB bridge +2.624 byte); điểm đáp tầng 2 GIỮ NGUYÊN; 2 góc chuẩn cầu không còn chiếm khung.
### D. Mật độ trong khung (web)
- [x] +8 người trước mặt tiền, +2 trước đảo, +7 ở 3 cụm đầu đường vào, +2 wanderer tuyến mới; người quanh đảo 8 vị trí bám vành r 11,3–12,8; xe đường vào 6 moto chạy lượn tránh đảo (islandBump), xóa xe chạy vòng 'ring' cũ.
- [x] AW_NODES sửa 3 nút theo đảo mới (4/5/6); test logic Node trích code thật 82/83 (1 "fail" do kỳ vọng test sai — groundH thềm phẳng = 0 là đúng thiết kế).
### E. MỤC 6 — Bầu trời
- [x] Web vốn đã có dome gradient + 420 sao + trăng + mây trôi (chỉ render harness thiếu): trăng dời về trời nam-đông (150,120,160) lọt khung anh hùng + góc A; mây đêm opacity 0,05 -> 0,16.
- [x] Harness gương trời đầy đủ: dome r330 gradient + quầng ấm phía chợ + 380 sao + trăng + quầng + 9 cụm mây cầu dẹt; cả 2 góc chuẩn phần trời có nội dung, hết mảng phẳng chết.
### F. Kiểm chứng bằng mắt (render Blender, harness gương cảnh web)
- [x] Đối chiếu r18 (THẬT | TRƯỚC v4.7 | SAU v4.8): renders/r18-doi-chieu-bung-binh-mat-tien.png + r18-doi-chieu-dem-dinh-thang.png — chữ đọc trọn, tầng trệt mở sáng, đảo lớn có thảm hoa/tượng đá, trời có trăng sao mây.
- [x] Hồi quy 3 góc phụ (đường vào / vòng xoay / chân thang) không vỡ hình. Điểm yếu còn lại đã ghi nhận: mảng sườn tây vẫn phẳng ~30% khung trái góc A (xử tiếp ở lớp hoa giấy mục 7); đảo nằm sát mép dưới khung B do camera khóa theo research/17.

## V4.9 (08/11) — MỤC 7: CHI TIẾT + BỐ CỤC + LỚP GỢI Ý ChatGPT ĐÃ LỌC
### A. Từng sạp (web buildStall/decorateStall)
- [x] Biển gỗ có ICON RIÊNG từng sạp (drawStallIcon: phin, bánh tròn, khuôn đất, dâu, hoa, cuộn len, hộp quà, đồng hồ, móc khóa, cà rốt, khoai, ly yaourt, ly nóng, lá, hộp trà, tô) vẽ 2 đầu biển thay glyph chung.
- [x] Thẻ giá kem viền đỏ "…K" (makePriceCard) cắm mép quầy phải MỌI sạp ngoài trời + cọc giữ.
- [x] 6 SẠP MẪU làm kỹ (designHeroStall): sữa đậu nành (kệ 2 tầng 6 hũ + nồi thép lớn + tháp ly — đúng ảnh chốt), bánh tráng (chồng bánh sống + khay bánh chín tràn mép + xiên que + 2 bát chấm), bánh căn (bếp đất 5 khuôn + khay 12 trứng cút + đĩa lá chuối), cà phê (khay 4 phin nhỏ giọt + bao hạt + 3 lon sữa), súp cua (nồi hé nắp + 2 chồng bát + 3 bát topping), dâu (bậc 3 tầng dâu + thùng bơ 034 + 4 ly kem bơ).
- [x] Mọi sạp còn lại: hàng TRÀN mép quầy (5 món nhỏ dọc mép trước, màu theo họ hàng).
- [x] Đạo cụ cầm tay tiểu thương theo hoạt cảnh (xẻng lật / muôi khuấy / muỗng múc-rót / kẹp gắp / cân tay / túi giấy gói / bó hoa / khăn len).
- [x] Hơi nước sprite bốc lên tại điểm nấu của 8 sạp có bếp (sữa, súp cua, bánh căn, bánh tráng, sữa đậu, chè, đậu hũ, bánh ướt), đậm hơn về đêm.
### B. Vật phẩm rời + kiến trúc (web)
- [x] 4 dây LỒNG ĐÈN GIẤY LỚN có tua đỏ (đường vào ×2, phố trước chợ, ngang đầu thang) ở nhiều cao độ 8,6–11,6.
- [x] Mặt tiền phụ: ĐỒNG HỒ thật tại (0, 17,7) — kim quay theo giờ game (applyDayNight); dây cờ tam giác 22 lá dọc băng tầng 2; 11 giỏ hoa treo dưới băng.
- [x] Rạp: 2 banner dọc "RẠP HÒA" / "PHIM HAY" + cặp chậu lớn sảnh; thang: 3 cặp đèn trụ 2 bên + cặp chậu chiếu nghỉ; 2 cột biển chỉ đường (finger post) ở bùng binh + phố đông.
- [x] Nền LÁT ĐÁ canvas (ô đá + khe + vết) phủ phố trước chợ + đường vào, polygonOffset chống z-fight.
- [x] Trong nhà lồng: dải len gradient 3 cụm × 8 mảnh treo mặt lan can lửng; dây 21 bóng dọc lan can; SÀN KIM CƯƠNG canvas; khay hàng NGHIÊNG cho 1/3 số quầy.
### C. Lớp gợi ý ChatGPT (đã lọc theo ảnh thật + style chibi đã chốt)
- [x] ÁP: hoa giấy magenta phủ tràn sườn đầu thang (17 cụm bougCluster); vòng cẩm tú cầu + hoa màu quanh chân tượng + 12 đèn nấm quanh đảo; ghế nhựa ĐỎ + bàn thấp ×5 cụm (thang ×2, quanh đảo ×2, trước chợ ×1); xô hoa tươi vỉa hè ×6; bảng phấn menu ×2 (HOA ĐÀ LẠT / ĐỒ NƯỚNG); đèn lồng đỏ trong ô lam tầng 2 ×17 + 2 span dây đèn; tranh tường ATISÔ ĐÀ LẠT lên gable tây; mặt sân lát đá ẨM phản sáng (roughness 0,45); xe máy đậu góc tiền cảnh nam đảo ×2.
- [x] BỎ (bịa lệch, không áp): trăng khổng lồ quá khổ; chữ neon "Đà Lạt Chợ Đêm" trên tường chắn (ngoài thật không có); đỉnh tượng bị sửa khác tượng 3 người đã chốt; người phong cách ảnh chụp (game chibi); cầu phụ + nhà bịa ở phông (gpt-duong-vao); texture grunge trên mặt tiền (lệch style phẳng).
### D. Kiểm chứng bằng mắt
- [x] Render cận v49 (7 shot): C2 nướng + C3 cà phê — biển/giá/icon đọc rõ, chữ không gương; C5 nhà lồng — biển QUẦY SỐ + tiểu thương sau quầy + sàn kim cương; C8 thang — đèn giấy + đồng hồ + trời sao.
- [x] Đợt polish (đúng 1): sửa góc máy C1 sữa + C4 dâu quay thẳng trục sạp (C4 đạt: biển + thẻ 22K + giỏ dâu đọc rõ — v51-C4); hoa giấy tăng cỡ ×1,45–1,8 + thêm hàng mép sườn hướng quảng trường (đọc được chấm hoa dọc mép trên ở góc A — v51-A).
- [ ] Sạp sữa CHƯA có shot cận sạch trong harness: dây đèn mặt sạp của harness là khối octahedron lớn hơn web nhiều lần, che biển ở cả 3 góc máy đã thử; trong web dây đèn là bóng tròn nhỏ. Nội dung sạp (biển/thẻ/nồi/hũ) đã kiểm chứng từng phần ở v49-C1 + các sạp mẫu cùng hệ (C2/C3); chờ Chung Hy xác nhận khi chơi thử.
- [x] Đối chiếu r19 (4 file, đã ghép + soi): r19-doi-chieu-bung-binh-mat-tien.png + r19-doi-chieu-dem-dinh-thang.png (THẬT | TRƯỚC v4.7 | SAU v4.9) + r19-doi-chieu-gpt-bung-binh.png + r19-doi-chieu-gpt-duong-vao.png (GỢI Ý | SAU). Lớp GPT bắt được: vòng cẩm tú cầu + đèn nấm, đèn lồng đỏ ô lam, biển sạp đọc được, sân ẩm, hoa giấy mép sườn; chưa bằng gợi ý ở độ phủ hoa giấy trên mặt sườn (điểm yếu còn lại đã biết).
### E. Dung lượng + đóng gói
- [x] index-standalone.html = **10.140.205 byte**, DƯ 345.555 byte dưới trần 10MiB (10.485.760). node --check đạt cho cả index.html và index-standalone.html sau mọi patch (W1–W10, lớp GPT, polish). Không GLB mới trong mục 7 (chỉ code + canvas) nên không cần nén thêm.
- [x] Save `chohb3d-v1` không đổi schema — không migration.
- [ ] CHƯA kiểm chứng trong trình duyệt thật (giới hạn môi trường đã biết): FPS với thêm mesh/NPC của mục 7, va chạm auto-walk qua solid đảo mới, đường lượn xe islandBump nhìn thật, mây/sương web chuyển động, kim đồng hồ có gương chiều không, paving overlay có z-fight với glowDisc không, hiển thị mobile. Chờ Chung Hy chơi thử.
- [x] Không đẩy GitHub, không upload (điều phối làm sau khi duyệt mắt).

## V5.0 (08/11) — SỬA 3 ĐIỂM THỊ GIÁC CÒN LẠI Ở GÓC A (theo soi trực tiếp r19 của điều phối)
### Điểm 1 — Bức tường xanh sườn tây
- [x] Gờ đá ngang (2/tầng) + nắp mép đá trên mặt tây (x=-19) của cả 3 khối thềm TERR.
- [x] Bồn dây leo mép thềm + rèm hoa giấy rủ (6 cột × 3–4 hàng, jitter phá lưới — đợt đầu ra lưới chấm đều, đã sửa sau khi soi draft) + dải hoa lưng chừng ở thềm trên/giữa.
- [x] 5 đèn trụ + 2 thông trên mép thềm tây; 2 người đứng mép thềm trên (bóng người cắt đường đỉnh tường).
- [x] Dãy ki-ốt mép thềm: 3 ở thềm dưới (2.8) + 2 ở thềm giữa (8.5), mỗi ki-ốt có người bán đứng sau quầy quay mặt về đảo.
- [x] (c) Hạ cạnh sườn: KHÔNG đổi hình học (thềm là địa hình, groundH neo vào đó) — thay bằng phá đường nét đỉnh: bồn leo + rèm hoa tràn mép + đèn. Đã ghi rõ lý do.
### Điểm 2 — Tiền cảnh trống + vật đen lạ
- [x] VẬT ĐEN ĐÃ XÁC ĐỊNH (dump object quanh điểm three (-33,-8.5)): là XE MÁY ĐẬU vành đảo cung 205° tại (-35.4,-11.3) (+ xe cung 225° sát máy) — không phải mesh lỗi: xe đậu hợp lệ nhưng quay lưng thẳng vào góc máy A, màu sơn ngẫu nhiên gần-đen, nằm tối → đọc thành "khối đen hình chữ nhật" (+ 1 người đứng cạnh bị đọc thành "nhân vật nằm"). Sửa: cung 205/225 → 200/238, đẩy R12.6 → R13.8, xoay 3/4 (+0.55 rad), cố định màu đỏ/xanh. Ở r20 vật đen biến mất hẳn.
- [x] Cụm ăn A trên thảm đảo tây-bắc (bàn + ghế đỏ + 2 người ngồi) tại (-30.0,-13.5); cụm B vành tây đảo (-33.8,-7.6) + 2 người; sạp hoa 3 xô tại (-30.9,-11.6) + người bán ở vành.
- [x] Thêm người ngồi vào 2 bộ bàn G3 sẵn có ở nam đảo (trước đây bàn ghế trống).
- [x] Vị trí đều ở z<0 phía bắc/tây đảo — kiểm AW_NODES (hành lang z 0.5..8 phía nam) và làn xe islandBump (z>=5 khi qua đảo): không chặn.
### Điểm 3 — Đảo + bệ tượng
- [x] PHÁT HIỆN GỐC: bụi cẩm tú cầu + đèn nấm lớp GPT đặt chân y=0.35 trong khi mặt thảm đảo (Lawn GLB) top = 0.93 (số đo dump roundabout.glb) → bụi chỉ ló ngọn hoa, chao đèn nằm dưới thảm. Nâng chân lên 0.92 (bụi ngoài đĩa r11.6 giữ 0.05).
- [x] 14 gò cẩm tú cầu LỚN (×1.6) dọc cung nam-tây r8.8/9.5 + vành đèn nấm 2 (8 cái r9.3).
- [x] Bậc đá 8.8×8.8 quanh chân tượng (tâm tượng lệch (-28.2,-2.8) theo dump GLB) + 4 đá góc; 3 người ngồi vành nam đảo (mép Base 0.55).
### Sửa kèm trong harness (render_v52.py, không đổi web)
- [x] Sửa lỗi DẤU groundH(x,-z) ở boug()/eat_set()/bucket()/chalk() của harness: hoa giấy trên sườn bị chôn (chỉ ló hàng mép z=-16.6), eat_set nổi +2.8, xô hoa nổi +6.4, bảng phấn nổi +3.28 trong các render kiểm chứng trước. Web không có lỗi này.
### Kiểm chứng
- [x] Render draft v52 (A + C-terr + C-dao) soi từng điểm → sửa rèm hoa 1 vòng → render full v52: góc A (v52-A-bung-binh-dem.png), cận sườn tây (v52-C-terr-dem.png), cận đảo (v52-C-dao-dem.png).
- [x] Đối chiếu r20 (THẬT | v4.9 | v5.0): renders/r20-doi-chieu-bung-binh-mat-tien.png — tường tây hết mảng trơ (còn là vùng yếu nhất khung nhưng đã chia tầng/hoa/ki-ốt/đèn), vật đen hết, thảm hoa nổi khối, chữ CHỢ ĐÀ LẠT đọc trọn.
- [x] node --check đạt cho index.html + index-standalone.html. Standalone = **10.149.407 byte**, dư 336.353 byte dưới trần 10MiB. Chỉ thêm code, 0 GLB mới. Save chohb3d-v1 không đổi schema.
- [ ] CHƯA kiểm chứng runtime (giới hạn môi trường như cũ): FPS, auto-walk thực tế qua tiền cảnh mới, va chạm cụm ăn trên đảo. Chờ Chung Hy chơi thử.
- [x] Không upload, không push GitHub (chờ duyệt mắt).

## V5.1 — Trang phục đa dạng + ăn uống + bùng binh đêm (research/18) + BLENDER-FIRST (lệnh 14:15–14:16 08/11)
Nguyên tắc mới: hình khối quan trọng dựng THẬT trong Blender (build_models.py), không chồng primitive trong code. Báo byte TRƯỚC/SAU từng GLB + tổng bundle; trần 10MiB giữ nguyên.
### Blender-first (roundabout.glb + stall.glb dựng lại)
- [ ] Tượng đài: bệ 3 bậc bo chamfer + gờ, 3 tượng thuôn mượt (cone 16 cạnh + vai/đầu cầu, smooth shading, tượng giữa cao hơn + giơ 2 tay), vật liệu StatueStone sáng hơn (đá xám lạnh)
- [ ] Đảo: ghế đá BO CONG (sector theo vành) + gờ đá quanh đế; hoa thảm gộp mesh; thảm họa tiết giữ hình học sector
- [ ] Hàng tĩnh sạp trong stall.glb (web bật theo def.id): SkewerTrays (3 khay nghiêng + ~48 xiên + vỉ than), CheCups (10 cốc 2 tầng), YaourtTower (tháp 12 hũ), BowlStack (nồi + chồng 6 chén + hũ nước đường), CornGrill (vỉ + 8 bắp + 6 khoai)
- [ ] Mái sạp: ô dù sạp (Umbrella) + mái tôn sóng (TinRoof) trong stall.glb; web: mọi sạp có bạt sọc (stripeVar mặc định theo hash), sạp khoai/trộn dùng mái tôn
- [ ] Byte GLB trước/sau + tổng standalone ≤ 10.485.760
### Mục A — trang phục đám đông (code)
- [ ] 4 phom: PHAO (scale Torso) / DẠ DÀI (part A2 rút gọn) / HOODIE (beanie trùng màu áo + khăn ống K5) / LEN ÔM (+ sọc cho tiểu thương); phân bổ theo vai trò research/18
- [ ] Màu crowd thêm trắng kem + đen; beanie/khăn màu độc lập áo; quần nhiều màu; scale ±8% + dáng thấp + trẻ em 0,70–0,78; 4 tông da
- [ ] Vật cầm/đeo: ly giấy ~10–12%, túi nilon ~25–30%, ba lô/túi chéo/tote ~35%, điện thoại ~15%, găng ~8%, bắp ~5% — đếm mesh tăng thêm
### Mục B — ăn uống (code + GLB)
- [ ] Sạp xiên khay tầng đọc "trăm xiên" (GLB) + khói/vỉ than (code giữ); bàn ăn đủ bộ: 2 ly (1 ly sữa thủy tinh) + tô/đĩa theo cụm + chén chấm + đũa; sitters có ly/túi cạnh + cầm ly
### Mục C — bùng binh đêm (code)
- [ ] Tượng RỌI SÁNG: vật liệu emissive đêm + 2 spotlight chân bệ + halo chân tượng; trăng thu nhỏ (hết trộm khung góc A)
- [ ] Người tụ quanh đảo: 2 nhóm chụp ảnh trước tượng (1 người giơ điện thoại) + 4 ngồi vành + cụm gia đình có trẻ em; xe máy đậu vành tây dài; xe chạy đêm qua đảo (nightRoad)
- [ ] Mây trời đêm: vệt mây mềm chibi (sprite quầng mềm, trôi chậm) thấy trong render góc A đêm
- [ ] Biển neon phông: THANH BÌNH (xanh dương, khách sạn đông) + SANDALS FLORA (vàng, khách sạn đồi)
### Nghiệm thu
- [ ] Render v53: góc A đêm + cận đám đông + cận sạp xiên + cận bàn ăn + góc B; file đối chiếu r21 đặt cạnh tư liệu đêm 28–39
- [ ] node --check sau mỗi patch; harness test liên quan chạy lại; save chohb3d-v1 không phá
- [ ] Không upload, không push GitHub

> GHI CHÚ BÀN GIAO (điều phối tách tuyến 08/11): phần CODE v5.1 (mục A dress system + harness 4.000 mẫu, mục B tableSet/sitters, mục C STATUE_FX + người đảo + neon, mái bạt stripeVar + bật/tắt prop GLB theo def, mây/trăng, nightRoad) ĐÃ XONG, node --check đạt. Phần BLENDER: tuyến code ĐÃ LỠ sửa build_models.py + rebuild roundabout.glb (1.313.708 → 1.080.236) và stall.glb (726.184 → 1.956.792 — PHÌNH do bevel segments=2 trên part trụ nhỏ: YaourtTower 13.200 verts, CheCups 5.616, SkewerTrays 6.984; cách thon: bevel=0 cho part nhỏ + giảm radial segments) TRƯỚC khi có lệnh tách — tuyến Blender riêng gộp tay. Render nghiệm thu v53/r21 thuộc tuyến Blender/gộp (tuyến code không chạy Blender theo lệnh tách + RAM chật).

## V5.2 — PHA XE MÁY (research/19, Chung Hy duyệt 14:25 08/11) — PHẦN CODE index.html
### P2 — Hệ tuyến xe
- [x] Engine tuyến waypoint riêng cho xe: buildRoute/routeSample; 3 tuyến (vòng đảo 2 làn cung 140°–340° quay đầu đổi làn ở 2 đầu — đảo không khép vòng kín được vì góc ĐB là thềm thang/sườn; trục đường vào 2 chiều laneZE/laneZW; vòng chân đồi loop kín)
- [x] ĐÚNG 14 xe chạy đồng thời (4 vòng đảo + 5 trục + 3 chân đồi + 2 tấp lề); tốc độ 6–9 u/s; người cưỡi dùng hệ dress v5.1 (RIDER_SHIRTS phom phao trắng/đen áp đảo) + mũ bảo hiểm sẵn trong vehicle.glb
- [x] Giãn cách xe trước cùng làn + xe chậm/dừng khi người chơi/NPC cắt ngang (phanh cứng <1,3u — sim: xe dừng cách người đứng giữa làn 1,20, không xuyên); NPC né nhẹ xe người chơi
- [x] Đêm: nón đèn pha + đèn hậu (có từ trước) + ĐĨA vệt sáng mặt đường vehGlowMats (đêm 0.33) — vòng đảo thành vành sáng chuyển động
- [x] 2 xe tấp lề mua hàng (sữa + bánh tráng): chạy → steer tấp lề → tắt người cưỡi + spawn shopper đi bộ tới front sạp → quay lại → về làn; sim 600s chạy 6 chu trình
- [x] Harness tuyến (code trích nguyên văn): maxStep roadY ≤0,5/0,5u; cách front sạp ≥0,90; cách node AW ≥0,76 (riêng node refuge giao lộ đảo đông (-18.5,5.8) 0,63/0,65 — kẹp giữa 2 làn hội tụ, xe dừng bảo vệ người); vòng đảo không vào đĩa đảo (r ≥11,72); không vào rect thang. roadY() xử lý xe chạy DƯỚI cầu nổi + trước tháp thang (groundH trả mặt cầu 13,9 — harness bắt)
- [x] Sửa lỗi ẩn từ v4.8 do harness bắt: laneZW biên độ cũ quét qua hàng chờ dãy sạp nam + mặt sạp đậu hũ/xiên (nay đỉnh 6,6, lên dốc muộn x -41, hạ sớm x -16..-13); 3 node AW nằm trên tâm làn đã nhích (nút 4 → (-35,4.6), nút 5 → (-18.5,5.8), nút plaza (-4,4.5) → (-4,1.9))
### P3 — Thuê xe nâng cấp + nhiệm vụ giao hàng
- [x] Xuống xe ở bất cứ đâu (xe đỗ lại tại chỗ, đồng hồ vẫn chạy), E gần xe cưỡi tiếp, nút HUD "🛵 Trả xe" (chỉ hiện khi đang thuê), đếm ngược cảnh báo 10s cuối trên HUD, hết giờ xe tự lăn về bãi ~1,6s (không biến mất đột ngột); giá 30 Xu/90s + Cấp 5 miễn phí giữ nguyên; tốc độ cưỡi 15 → 11,5
- [x] Nhiệm vụ ngày "🛵 Giao hàng bằng xe" vào DAILY_POOL (pool 8 → 9): thưởng riêng 90 Xu/55 XP qua def.xu/def.xp trong dailyProg (áp cả quest ngày + quest tồn dồn); nhận 📦 ở sạp ngẫu nhiên → giao NPC chờ ở khu khác ≥45u trong 85s; giao khi đang cưỡi xe +20 Xu ship nhanh; marker vòng vàng + 📦/🎯; chip HUD theo dõi đơn
- [x] Harness kịch bản (code trích nguyên văn): thuê 300→270 Xu → xuống xe giữa chợ (xe ở nguyên tọa độ) → 30s sau remount còn 60s → hết giờ xe về RENT_PT; giao hàng pickup → carry 85s → dailyProg('deliver',1). ĐẠT toàn bộ
- [x] Polish v5.2 (đúng 1 vòng): NPC nhận hàng dùng dáng 'chat' vẫy tay thay vì đứng im
- [x] node --check sau mỗi patch; save chohb3d-v1 KHÔNG đổi schema (trạng thái thuê không lưu); 0 GLB mới
- [x] Standalone cuối: 10.391.833 byte (9,91MB) ≤ trần 10.485.760 (assets thô 7.514.364 — GLB đã được tuyến Blender làm thon song song)
- [ ] Render đêm góc A/B thấy vệt xe quanh đảo — thuộc tuyến Blender/gộp (tuyến code không chạy Blender theo lệnh tách)
- [ ] Không upload, không push GitHub (chờ Chung Hy duyệt mắt)

### Xử lý findings tuyến B (research/19b, harness 26/26) — vòng 2
- [x] R-01: RENT_PT (31.5,13.8) nằm trên thang trong nhà (groundH 11.39) → dời về **(35.5, 8.5)** (groundH = 0, harness xác nhận); biển + xe bãi + logic trả xe dùng chung hằng số nên tự khớp
- [x] R-02 + R-09: rút TOÀN BỘ xe đậu R12.6 cung nam/tây đảo (deg 20–180 — nằm đúng giữa 2 làn vòng R11.9/12.9, đo deg45 d=0.10) và hàng lấp vành R12.9 của v5.1 (deg 160/170/190/215, d≈0.2; deg 250/262 chìm sườn dốc); giữ/thêm chỉ cung tây-bắc NGOÀI làn: 196° R15.6 + 225° R13.8 (bản cũ 238° chìm dốc 2.09) + 205/218° R15.6 + 227°; hàng lề tây rút 10→8 xe (2 xe cuối lấn làn E/HILL 0.24–0.41); bãi đông nới tới x 38.5
- [x] R-10: bỏ hàng xe đậu z=11.75 sau sạp (dải lưng sạp 11.45..cột 12.2 không chứa nổi cả xe đậu + làn); chân bắc ROUTE_HILL 12.3 → **12.9** (hành lang trong nhà lồng, giữa hàng cột 12.2 và sạp trong 13.7+; roadY trả 0.5 khớp sàn)
- [x] R-11: giao tuyến nam đảo — thêm `slowCapFor` (mọi xe trong r5.5 quanh (-24,6) cap 3.2) + xe HILL **nhường mọi xe tuyến khác** (vòng đảo/trục giữ ưu tiên → không kẹt đối đầu); sim 600s: HILL×tuyến khác min 1.37 toàn bản đồ, trong vùng giao min 7.18
- [x] Dùng lại logic harness B thay vì tự viết: followSpeed (minGap 2.2/comfortGap 4.5) + yieldSpeed (lookAhead 7/stopGap 1.3) chép công thức vào updateTraffic (sim: xe dừng cách người đứng giữa làn 1.30); SLOW_ZONES 19b mục 5 áp cho 2 làn trục (cung đảo cap 3.0, mặt tiền/đầu tây/hàng sạp cap 3.5); poStep/rentStep đối chiếu ngữ nghĩa — bản cài tương đương (chu trình tấp lề chạy 6 vòng/600s; thuê xe có sẵn PARKED_FREE + đếm ngược 10s + RETURNING). Sửa thêm lỗi cấu trúc: nhánh "xe steer/dwell = vật cản" trước đây bị `continue` chặn chết, nay chạy thật
- [x] R-03 (che/tron × laneZW): laneZW baseline 4.1 → **4.45** (≈ làn W v4.8 đã chơi thật) + lõm −0.3 né đuôi hàng chờ sữa + đỉnh lượn 6.65; trạng thái: đã nắn theo số đo + vùng chậm SZ-5, vẫn cần soi render để đóng hẳn như 19b ghi
- [x] Nắn tiếp từ harness hình học sau khi đưa xe đậu vào đo: HILL chân đông vào **dải giữa đường** (z 0.35–1.55) — bản cũ z −1.3 đè làn E khiến xe spawn đè nhau (sim bắt ở t=0, d=0.58); chân tây đi hành lang giữa rồi vòng lên hành lang nam
- [x] Chạy lại: harness tuyến B **26/26 PASS**; harness hình học tuyến này GEOM OK (đã gồm xe đậu + RENT_PT); sim giao thông OK; kịch bản thuê/giao OK; node --check đạt
- [x] Standalone sau vòng 2: **10.394.805 byte** ≤ 10.485.760 (dư ~91KB — RẤT SÁT TRẦN như tuyến C cảnh báo; đợt sau thêm code phải nén/gọn hoặc xin điều phối)

## V5.3 — KIỂM CHỨNG HÌNH ẢNH V5.1+V5.2 + QUÉT CHI TIẾT TOÀN MAP (lệnh Chung Hy 15:22 08/11)
### A — Render kiểm chứng (harness render_v53.py = render_v52 + gương dress/props/traffic/STATUE_FX/neon/mây)
- [x] Lượt 1 (bản harness trước vá neo đèn tượng): A đạt bố cục (tượng trắng sáng nổi giữa khung, mây vệt, biển CHỢ ĐÀ LẠT, đám đông đa sắc + túi đeo đọc được); B đạt (phom phao + beanie + khăn đọc rõ ở người leo dốc, dây đèn + sạp dưới sáng); D đạt nội dung (bạt SỌC xanh–trắng chạy texture thật, khay xiên + vỉ + đèn lồng giấy đọc rõ) nhưng khung bị mặt phẳng tiền cảnh che nửa dưới
- [x] Lỗi máy quay harness đã vá + chụp lại ở lượt sau: C (máy nằm trong khối sạp), E (máy sát đầu người ngồi), F (máy trong khối → khung đen), G (máy lọt trong nhà lồng); D kéo máy gần/xuống thấp
- [x] PHÁT HIỆN LỚN khi đối chiếu statueT: đèn rọi tượng trong harness v52 đặt ở TÂM ĐẢO (-24,-6) trong khi tượng thật đứng lệch ở (-28.2,-2.8) (offset trong GLB) → tượng bị tối ở các render cũ một phần do đèn harness sai neo (bản WEB đúng: STATUE_FX 2 spot tại (-31.6,-6.4) + (-24.6,0.9) nhắm (-28.2,5.2,-2.8)). Harness đã sửa: 2 spot53 đúng tọa độ web + rửa chân tượng theo neo mới + góc F nhắm thẳng tượng
### B — Quét chi tiết toàn map (code index.html, khối "V5.3 QUÉT CHI TIẾT")
- [x] Nhóm 1 quầy hàng: cành thông phủ nóc sạp (research/12 mục 4 — trước đây CHƯA có): 2 cụm cành dẹt trên mép sau bạt cho ~1/2 số sạp theo hash id; giỏ dâu (giỏ gỗ + 5 quả đỏ) / chậu cây ở góc chân trước sạp (mục 5) xen kẽ theo hash — lấp vùng chết chân sạp
- [x] Nhóm 2 đèn: rà soát — đèn đường thuộc địa đã có glowDisc chân cột (dòng 931), mỗi sạp 2 glowDisc, đảo + tượng có quầng riêng, đèn nấm đảo + uplight vành đảo có sẵn → KHÔNG thiếu bóng "có mà không sáng" ở cấp code; verdict thị giác theo render A/B lượt cuối
- [x] Nhóm 3 bộ phận nhỏ: THÙNG RÁC ×7 (trước đây toàn map không có): vành đảo, quảng trường, đầu đường vào, chân thang, trong nhà lồng, đồi, tây đảo; CỘT ĐIỆN + DÂY VÕNG mép bắc đường vào ×3 cột/2 nhịp (trước đây không có — chi tiết dây chằng chịt trong ảnh thật research/11)
- [x] Lỗi tự bắt khi rà: cột điện thứ 4 ở x=-30 nằm TRONG đế đảo (cách tâm 6,5 < R đế 10,5) → bỏ, còn 3 cột; hàm hashStr không tồn tại trong web (bản nháp đầu của khối quét gọi nhầm) → thay bằng tổng charCode inline như hệ sọc sạp
- [x] node --check đạt sau mỗi vá; save chohb3d-v1 không đổi; 0 GLB mới
- [x] Standalone cuối đợt: 10.398.189 byte ≤ 10.485.760 (dư 87.571 byte — vẫn RẤT SÁT TRẦN)
- [x] Render lượt cuối (vá neo đèn tượng + gương khối quét + máy mới; 8 lượt chạy vì máy bị chiếm tải + VM reboot 1 lần + 2 lỗi harness đã vá: flush_grp không clear _GRP, biến sc của gương quét đè scene): **A ĐẠT** (tượng trắng sáng nổi, mây, hoa đảo, đám đông đa sắc — xem r21), **B ĐẠT** (4 phom + beanie/khăn đọc rõ), **C ĐẠT nội dung** (phom phao đỏ + beanie tím + thang cầu vồng; tiền cảnh bị 1 người che 1 phần), **D ĐẠT** (khay xiên Blender 2 tầng + vỉ + đèn lồng, bạt sọc), **F ĐẠT** (tượng rọi sáng đúng neo web + nhóm chụp ảnh + vành người — ảnh cận tốt nhất đợt), **G đạt theo số đo + hành lang trống** (R-03: làn W không còn áp sát front chè/tron trong render; xe chạy không lọt khung tĩnh này — bằng chứng số ở harness tuyến B 26/26), **E CHƯA ĐẠT khung** (3 lần vá máy vẫn lọt giữa đám đông xếp hàng quanh cụm bàn (-17.5,5.5) — nội dung bộ bàn đã kiểm chứng ở góc rộng + code, cần 1 shot riêng khi Chung Hy duyệt đợt sau)
- [x] r21-doi-chieu-bung-binh-mat-tien.png (tư liệu đêm 28 | v5.0 | v5.1+v5.2) + r22-doi-chieu-sau-quet.png (tư liệu đêm | v5.0 | cận đám đông sau quét) trong renders/; toàn bộ ảnh v53-*-draft.png là bản DRAFT 480×360/4 mẫu (máy bị chiếm tải triền miên — bản full 896×672/16 mẫu chạy 1 lệnh duy nhất khi máy trống: blender -b --python scripts/render_v53.py, không cần sửa gì thêm)
- [ ] CHƯA kiểm chứng trong trình duyệt thật (giới hạn môi trường): khối quét + dress/traffic chạy thật — chờ Chung Hy chơi thử
- [ ] Không upload, không push GitHub (chờ Chung Hy duyệt mắt)

## V5.3-FIX (08/11 tối) — SỰ CỐ MÀN HÌNH ĐEN: CHẨN ĐOÁN RUNTIME + SỬA GỐC
- Triệu chứng (Chung Hy chơi thử bản chốt trên Mac, file://): HUD hiện đủ nhưng khung 3D ĐEN toàn bộ, bản đồ nhỏ trống, nhiệt độ "--°C". node --check đạt nên lọt mọi cổng cũ — bài học: từ nay MỌI bản giao phải qua harness chạy thật `scripts/diag_runtime.mjs` (mới, thực thi nguyên văn module + GLB thật + bơm frame animate), không chỉ kiểm cú pháp/render tĩnh.
- Nguyên nhân gốc #1 — họ lỗi TDZ (khai báo const/let NẰM SAU điểm gọi top-level đầu tiên; hàm được hoist nhưng biến thì không): khối dựng sườn tây (~dòng 627–648) gọi lamp()/crowdPerson()/addStatic() ở top-level, trong khi các binding chúng cần nằm ở đoạn V5.1 phía sau: `_haloShared` (cũ ~1360), bảng trang phục `NPC_PANTS…FORM_DIST` + `_npcMats` + `NPC_PART_MESHES` (cũ ~1132–1158), khối `GEO_*` đồ cầm tay + `_npcStripeMats` (cũ ~1168–1205), `_staticSeq` (cũ ~2092), `SCARF_COLS` (cũ ~2080), `smokeMat` (cũ ~1132, addSmoke gọi từ khối nhà ~1037). Ngoại lệ đầu tiên bắt được: `ReferenceError: Cannot access '_haloShared' before initialization` (addHalo ← lamp ← top-level) → module chết ngay khi nạp → không animate → đen. Sửa: dời NGUYÊN các khai báo dữ liệu/geometry thuần đó lên đầu file (cạnh worldGroup/_haloShared, ~dòng 316–360), hàm giữ nguyên tại chỗ; mỗi điểm dời có comment "FIX MÀN HÌNH ĐEN".
- Nguyên nhân gốc #2 — dùng sai hợp đồng makeMoto/makeCar: hai hàm trả `{g, wheels, coneMat}` (6 điểm gọi đúng đều dùng `.g`), nhưng 3 điểm tạo xe viết như trả Group: xe đậu G9 tiền cảnh nam đảo (~3106), `rentBike` (~4295) và `rideMesh` (~4314) → `.position` undefined → TypeError giết init (G9, top-level) và sẽ giết luồng thuê xe. Sửa: lấy `.g` ngay tại 3 điểm tạo, kèm comment; không đổi hợp đồng hàm (hệ giao thông đang dùng wheels/coneMat).
- Kiểm chứng bằng harness diag_runtime (three r160 + GLTFLoader thật + GLB thật): TRƯỚC sửa — chết init tại _haloShared (rồi lần lượt FORM_DIST → GEO_CUP → _staticSeq → SCARF_COLS → smokeMat → TypeError makeMoto khi gỡ từng lớp). SAU sửa — index.html: INIT OK + 900 frame sạch, cả khi seed save cũ chohb3d-v1; index-standalone.html (đường data-URI như trình duyệt): INIT OK + 300 frame sạch; node --check đạt; đối chiếu văn bản: script standalone ≡ script index.html sau khi đảo đúng 2 phép biến đổi đóng gói.
- Đóng gói lại: index-standalone.html = 10.399.964 byte ≤ trần 10.485.760 (dư 85.796). CHƯA upload/push — chờ điều phối duyệt.

## V5.4 (08–09/11) — SỬA 3 NHÓM PHẢN HỒI CHƠI THỬ CỦA CHUNG HY: ĐƯỜNG VÀO / ÁNH SÁNG ĐÊM / NGƯỜI
- Lệnh gốc (23:38 08/11): đường vào "nhỏ xíu", 1 hàng đồ ăn là kịch — thật RẤT RỘNG, HAI HÀNG HAI BÊN + có xe; ánh sáng "giống studio", đêm tô đen; người hoạt động sai, ĐI VÀO ĐẤT, lỗi tùm lum. Trình tự: nghiên cứu → sửa → kiểm chứng → đúng 1 polish. KHÔNG upload/push đợt này.
### PHẦN 1 — NGHIÊN CỨU
- [x] research/20-duong-vao-va-anh-sang-dem-that.md: mặt cắt đường thật + số mục tiêu; ánh sáng đêm thật (sodium cam, quầng tách rời có khoảng tối giữa các cột, nền trời xanh-nâu sâu không đen chết); đo code cũ (đường plane 170×18, 4 sạp đêm GIỮA đường z=3 = nguồn "một hàng là kịch"; khe 2 làn tại đảo chỉ 0,75 tâm–tâm; rig đêm cũ: nền 0x191209, sky mid TÍM 0x3d2b52, hemi 0,92 + amb 0,26 = sáng phẳng kiểu studio, exposure 1,34)
- [x] research/20b-bo-sung-chuyen-dong-va-so-do.md (bổ sung theo nhắc của Chung Hy "nghiên cứu sâu ảnh tham khảo — thiếu gì nữa?"): chuyển động thật khớp 5/6 với game (vòng đảo CCW = 2 cung + ringSwitch là đơn giản hoá khó thấy vì phía đông đảo là đai thềm; băng đường theo cụm/xe chậm theo VÙNG slowCapFor; thang: ngồi theo cụm + dòng 2 chiều; đứng chờ vành đảo/mặt sạp/đầu thang; phố đêm theo sườn dốc). Số đo cứng: NTMK lòng đường 10m + vỉa hè 3m×2 = mặt cắt 16m (tinbds); toà chợ 80×18m cao 19,45m, thang Lê Đại Hành cao 17m/3 đợt → neo 1u≈1m (đồi game 17u khớp); con số 20u hành lang của research/20 XÁC NHẬN đúng cho đoạn trước chợ/bùng binh; khổ thang game 22u vs ước lượng ảnh 15–18m = LỆCH +20–40% và đảo Ø21u lệch tương tự — GHI NHẬN, không sửa đợt này (sai số ước lượng ±20%, thang game hợp nhất 2 thang thật + vai khán đài, thu hẹp là refactor địa hình lõi — khuyến nghị đợt riêng thu thang về 17u). Giới hạn tư liệu: YouTube chặn tải video walking tour (429/bot) → bằng chứng chuyển động = ảnh bìa 28–37 + ảnh 01–27 + mô tả research/16 + bài 2026; OSM API không trích được hình học
### A — ĐƯỜNG VÀO
- [x] Làn xe: laneZE đỉnh 5,55 (cách tâm đảo 11,55), laneZW đỉnh 7,15 (cách tâm đảo 13,15) — khe 2 làn tại đảo 1,6 tâm–tâm (hở 0,9), hết cảnh xe cọ nhau; vạch chia z 1,5→0,2
- [x] HÀNG SẠP BẮC MỚI z=−6,7 quay mặt vào đường (bánh mì/hủ tiếu/trái cây/đậu hũ/cháo — 3 sạp khói, 2 nightOnly); dãy nam 10 sạp lùi về z=11,0; xiên/quế/trộn dời về dãy nam — đường vào thành 2 hàng 2 bên + làn xe giữa như ảnh thật
- [x] Địa hình: nhánh THỀM BẮC trong groundH (đoạn tây bám dốc theo ramp, không phẳng), vỉa hè 2 bên bám dốc, cắt sườn seg1 tại z=−11 + tường chắn đất + tấm lát thềm; QUEUES/AW node/spawn người chơi (−76; 5,6)/biển tên đường/groundVendor cập nhật theo hình học mới; eatSet giữ nguyên (số đo cách làn E 0,97/1,78 — chấp nhận, ghi rõ thay vì lùi bàn vào trong)
- [x] Phát sinh khi rà: chân ROUTE_HILL xuyên sạp sữa (→ x −45,5), chân về phía đông đè làn W mới (→ đi dải giữa z 0,2), chân bắc xuyên hàng quầy lưới sảnh (→ dời hàng quầy 13,3→14,55, mở hành lang thật 12,0–13,85; LOOP né theo)
### B — ÁNH SÁNG ĐÊM
- [x] Trời: top 0x0e1a30 / mid 0x274263 (BỎ tím sân khấu) / chân trời hổ phách 0xc07a36; nền 0x0e1a30; sương 0x3d3630 base 0,0058; hemi trời lạnh 0x93a7cc/đất ấm 0x40301e 0,5; ambient ấm 0,12; sun đêm = 0, trăng lạnh 0xa9c3e8 0,4; exposure 1,22 (đêm đọc bằng tương phản điểm sáng, không sáng phẳng); đèn đường 88/distance 27/decay 2,0 + halo từng sạp pha riêng 0,50–0,66 (quầng tách rời, có khoảng tối giữa các cột như ảnh thật)
### C — NGƯỜI + LỖI
- [x] Lỗi gốc "đi vào đất/lên nóc": guard "đi dưới hành lang" của wanderer THIẾU đoạn đông x 21..33 z 7..12,2 → người bị groundH 12,6 nhấc lên nóc hành lang — đã bổ đủ 3 đoạn
- [x] RB_ARC theo vành apron đảo R~11,3–12; INDOOR_RT viết lại theo lối đi thật trong sảnh (z 17,6/25,7, khe −5,2…); LOOP đoạn sảnh sửa; ~20 tuyến wanderer viết lại theo hình học mới (R2016–R2050, V4.8, 3 tuyến tây/đêm)
- [x] Công cụ audit mới scripts/audit_ground_v54.mjs (trích nguyên văn code game, soi chân người theo groundH + thân quầy theo box thật): 57 tuyến + AW 36 nút + 28 sạp = 0 lỗi cứng, 0 nhảy lưới
### KIỂM CHỨNG + POLISH + ĐÓNG GÓI
- [x] diag_runtime: INIT OK + 900 frame SẠCH (chạy lại sau TỪNG đợt sửa, kể cả sau polish và sau nhóm D); harness giao thông v52 cập nhật snapshot hình học V5.4: 26/26 PASS, ngưỡng an toàn không nới
- [x] Render Blender draft (gương hình học + rig): H-duong-vao ĐẠT (hành lang rộng, 2 dãy nhà/sạp, đảo + tượng cuối đường), I-doc-vao ĐẠT (người trên dốc/vỉa hè chân bám đất), A-bung-binh ĐẠT (tượng rọi sáng như ảnh 32, vành đảo có người, không vùng đen chết), J-thang ĐẠT ở lượt 2 (người đứng/ngồi khắp các bậc, chân bám bậc, xe đẩy trên chiếu nghỉ — bằng chứng chính cho nhóm C ở thang), C-crowd HỎNG KHUNG (máy lọt giữa đám đông — không dùng, không chạy lại vì audit + J/I/A đã đủ bằng chứng cho nhóm C)
- [x] renders/r24-doi-chieu-v54.png: ảnh thật đêm 06 | render cũ (phẳng, be, kiểu studio) | render mới V5.4 (trời xanh sâu, tượng phát sáng, trung gian đọc được)
- [x] ĐÚNG 1 đợt polish: thêm 2 cụm CHAT_SPOTS ở ĐẦU THANG (−5,−33 'all' ×3; 5,5,−34 'night' ×2) theo research/20b mục 1.4 — điểm tụ người như ảnh thật 29/36; sau polish diag + audit giữ nguyên đạt
- [x] Standalone cuối đợt (sau cả nhóm D): 10.409.634 byte ≤ 10.485.760 (dư 76.126); diag chạy TRỰC TIẾP trên file standalone: INIT OK + 300 frame SẠCH
- [ ] CHƯA kiểm chứng được (giới hạn môi trường, ghi rõ): không xem trực tiếp game chạy trong trình duyệt (trình duyệt quản lý chặn loopback + muse.ai) — hình ảnh qua render Blender là GƯƠNG hình học/rig, grade khác bản web; FPS thật của nhóm D chưa đo được trong trình duyệt; video walking tour không tải được (xem mục nghiên cứu). Chờ Chung Hy chơi thử bản này để chốt mắt
- [ ] Không upload, không push GitHub (theo lệnh đợt này)

## V5.4-D — HIỆU NĂNG (Chung Hy chơi thử báo "vào thấy lag vãi"; đo bằng diag_runtime mở rộng PERF=1: duyệt scene thật sau init + chờ GLB nạp ổn định, đếm mesh/tri/đèn/caster trực tiếp)
### SỐ ĐO TRƯỚC (bản V5.4 sau A+B+C+polish, chưa tối ưu)
- Tổng: 23.640 object · 19.254 mesh · 163 sprite · 28 points · 3.763.542 tam giác (mesh nặng nhất chỉ ~3.900 tri — tri dàn đều, không có "quái vật" đơn lẻ)
- Draw call ước lượng (không frustum culling): ~19.445/frame; NGÀY cộng shadow pass = ~35.431
- Shadow: bật, sun map 2048×2048, camera ±95 (cả map); caster 15.986 = crowd 7.298 + thế giới 8.688 (trong đó vật nhỏ bán kính <0,45u: 5.033 — ly/chai/món ăn cũng đổ bóng); receiver 14.900
- Đèn biên dịch vào shader: 35 PointLight + 4 SpotLight + 2 Directional + hemi + ambient. ĐÊM (mặc định): 34 point + 4 spot BẬT. NGÀY: chỉ 1 point + 1 dir bật NHƯNG 39 đèn tắt vẫn nằm trong shader (intensity 0 vẫn tốn per-fragment) + sun vẫn có thể render shadow map về đêm
- Người: 354 NPC (59 wanderers + 295 statics) = 7.411 mesh (~21 mesh/người); statics đã có cổng khoảng cách 45u cho chuyển động, wanderers cập nhật MỌI frame
- pixelRatio: ĐÃ cap min(devicePixelRatio, 1.5) từ trước (dòng 280) — kiểm chứng, không phải sửa
- Xe đậu: dựng bằng hệ xe tĩnh, không tốn cập nhật/frame
### TỐI ƯU ĐÃ ÁP (theo chi phí đo được, KHÔNG cắt nội dung nhìn thấy)
- [x] Đèn: applyDayNight gán thêm visible theo pha — NGÀY: 32 đèn đường + monuLight + spot1/2 + 2 spot tượng visible=false (ra khỏi shader, trước đây intensity 0 vẫn tốn); ĐÊM: sun.visible=false (hết nguy cơ sun render shadow map về đêm), trăng visible=true. Đêm giữ NGUYÊN 34 point + 4 spot bật — diện mạo đêm không đổi theo cấu trúc (đèn intensity 0 vốn không đóng góp sáng)
- [x] Shadow: helper castOK (bán kính hình học ≥0,32 mới đổ bóng) áp tại box/cyl/ball + cloneAsset + clone nhà + addStatic; xe (makeMoto/makeCar) giữ nguyên đổ bóng. Sun map giữ 2048 (chất lượng bóng không giảm)
- [x] Ma trận tĩnh: đóng băng matrixAutoUpdate cho toàn bộ vật tĩnh dưới worldGroup (trừ động: player/rentBike/singer/beacon/NPC/xe/khán giả sân khấu + kim đồng hồ M7 + sương trôi fogPlanes + sprite/points/light) — chạy 1 lần cuối init
- [x] Crowd: wanderer xa người chơi cập nhật thưa theo khoảng cách (35–60u: stride 2; >60u: stride 3) với dt TÍCH LŨY — quãng đường/tốc độ/pha đi giữ nguyên, chỉ giảm số lần tính; statics đã có cổng 45u sẵn. KHÔNG gộp geometry/instancing cho người: 21 mesh/người là các khớp tay/chân/đầu phải chuyển động riêng theo hệ dress 4 phom — gộp sẽ phá hoạt họa; thay vào đó cắt caster + throttle + đóng băng là mức an toàn
- [x] KHÔNG merge hình học tĩnh thành mesh lớn: sẽ phá frustum culling theo mesh (hiện GPU chỉ vẽ phần trong khung hình) và phá bật/tắt sạp nightOnly theo group — ghi nhận là hướng riêng nếu cần đợt hiệu năng sâu hơn
### SỐ ĐO SAU (cùng harness PERF=1)
- Caster: 15.986 → 7.944 (−50,3%): crowd 7.298 → 2.864 (chỉ thân/phần lớn còn đổ bóng — người vẫn có bóng thân), vật nhỏ thế giới 5.033 → 1.424 (phần còn lại là xe + vật sát ngưỡng 0,32–0,45)
- Object đóng băng ma trận: 12.413 / 23.609 (52,6%) — phần còn lại là cây con của NPC/xe/vật động, đúng thiết kế
- Đèn trong shader NGÀY: point ẩn 33/35, spot ẩn 4/4, trăng ẩn → còn ~sun + hemi + ambient (+1 point sự kiện); ĐÊM: sun ẩn 1/2 dir, đèn đêm giữ nguyên
- Draw call ước lượng: NGÀY ~35.431 → ~27.368 (−23%, phần giảm là shadow pass); ĐÊM ~19.424 không đổi theo công thức (đêm vốn không có sun shadow) nhưng hết rủi ro shadow pass ẩn của sun
- Tam giác: 3.763.542 → 3.757.146 (chênh ~0,2% là dao động nạp GLB giữa 2 lần chạy — KHÔNG cắt nội dung)
- Kiểm chứng sau tối ưu: diag init + 900 frame SẠCH; audit_ground_v54 0 lỗi cứng/0 nhảy lưới; harness giao thông 26/26; standalone đóng lại 10.409.634 byte ≤ 10.485.760
- Ước lượng cải thiện thực tế: chi phí bóng (shadow pass) giảm ~một nửa; chi phí CPU cập nhật ma trận giảm ~một nửa số object; chi phí fragment ban ngày giảm mạnh nhờ bỏ 37 đèn khỏi shader; ban đêm (mặc định) giữ nguyên chất lượng sáng. Chưa đo được FPS thật trong trình duyệt (giới hạn môi trường) — chờ Chung Hy chơi thử xác nhận

## V5.5 (09/11) — THEO ẢNH CHƠI THỬ THẬT CỦA CHUNG HY (image-59): CHÓI NGÀY / ĐƯỜNG HẸP / MẤT DANH TÍNH PHỐ / GÓC MỞ ĐẦU + NGHIÊN CỨU 21 + BẬC TAM CẤP + TĂNG BẠT HỔ + ĐÀI PHUN & QUẦN ÁO
Nghiên cứu trước khi sửa: research/21-tham-khao-3d-va-duong-that.md + 5 ảnh theme/real-market/40–44 (SOURCES.md mục 40–44). Kết luận chính: trục thật là vòng xoay đài phun nước → NTMK → chợ → bậc tam cấp; quán Sữa đậu nành Hoa Sữa 64 Tăng Bạt Hổ cách chợ ~50m; không có mô hình 3D công khai đáng kể cho riêng chợ (photogrammetry Google Earth + UAV study) → ưu tiên silhouette + trục vista.
### A. Đường vào — số đo trước/sau
- Khoảng trống giữa 2 mặt sạp (front = tâm ± hướng×2,1): TRƯỚC 13,5u (bắc −4,6 / nam đoạn vào 8,9) → SAU 33,75u = ×2,5 ĐÚNG MỤC TIÊU (hàng bắc z −6,7 → −15,7, front −13,6; sạp nam đoạn vào z 11,0 → 22,25, front 20,15).
- KHÔNG đạt ×2,5 ở sạp nam ĐOẠN MẶT TIỀN (x −31..43, giữ z 11,0): lưng sạp chạm cột nhà lồng z=12 — dời nữa là xuyên nhà lồng. Đã ghi rõ: đoạn này là sạp áp mặt tiền chợ (khác tính chất đoạn đường vào).
- DÀI ×2: cổng chào x −81 → −131; spawn (−76 →) −126; entryRampY nắp min(2,0) → min(5,5); mặt cắt mới: nhựa giữa + vỉa hè bắc z −13,9..−11,1 + thềm sạp 2 bên (groundH viết lại 5 nhánh; ROUTE_HILL thêm vòng tây tới −129,5; AW 38 → 42 nút).
- Biển chỉ đường + biển tên đường 'ĐƯỜNG TĂNG BẠT HỔ' tại góc quán (−130,6, 16,9).
### B. Hạ chói ban ngày (rig NGÀY; đêm giữ nguyên V5.4)
- exposure 1,05 → 0,88; sun 1,1 → 0,95; hemi 0,85 → 0,55; ambient 0,12 → 0,10; sky bottom 0xf2e3c2 → 0xe8d5ae; fogBase 0,0075 → 0,0058.
- Mặt tiền trắng tinh → kem ấm: tint WallCream/ColumnCream → 0xe3d7bd (clone trong mk.traverse như MarketWin). Tách tông nền: nhựa 0x453f3a (sẫm nhất) < vỉa hè 0x84796a < sân sạp 0x978a78 (trước: plaza 0x8a7f72).
- GIỚI HẠN KIỂM CHỨNG: render Blender KHÔNG tái hiện được grade web (GLB gốc vẫn trắng; chế độ ngày của render vẫn bị SkyDome đêm + đèn điểm đêm chi phối → bản K-ngày trong r25 trông tối kiểu đêm, CHỈ dùng kiểm bố cục). Grade web thật CHỈ chốt khi Chung Hy chơi thử — đây là điểm mù đã biết từ V5.4 (lệch grade môi trường kiểm ↔ web).
### C. Danh tính đường Đà Lạt
- 2 dãy nhà phố LIÊN TỤC 2 bên trục (cũ 3+3 → thêm 8 nhà đoạn kéo dài: nam z 26,5 x −80/−95/−110/−124; bắc z −24..−25 trên sườn), nhựa có vạch đứt bám dốc tới x −124, lề/vỉa hè 2 bên suốt trục, 14 đèn đường (thêm 6 đoạn kéo dài), cẩm tú cầu 2 mép thềm + đoạn kéo dài, khói bếp theo dãy mới.
### D. Khung mở đầu (2 lỗi chồng nhau, đã truy tận gốc bằng raycast Blender)
- Lỗi 1: BIỂN CỔNG chắn tâm khung — camera spawn (−136,2; 13,5) phía tây cổng x −131, người chơi phía đông: đường ngắm tới đầu người chơi cắt biển ở y 10,57 ∈ [9,8..10,8]. SỬA: nâng cổng — trụ 5,4 → 7,6; xà + biển gy+5,5 → gy+7,7 (biển 'KHU HÒA BÌNH — CHỢ ĐÀ LẠT' mặt chữ hướng tây); đường ngấm đi dưới biển, biển thành banner mép trên khung.
- Lỗi 2: pitch quá cúi — render đối chiếu: pitch 0,55 (~31°) làm mặt nhựa chiếm ~70% khung, vista nén thành dải mỏng. SỬA: camPitch mặc định 0,8 (V5.4) → 0,55 → 0,38 (~22°); camera frame 0 = (−137,15; 11,73; 5,6) khớp công thức animate. Render K/L mới: thấy trọn trục dốc, 2 dãy nhà, tượng bùng binh cuối đường. Spawn giữ đầu đường (−126; 5,18; 5,6) mặt +x.
### E. Bậc tam cấp + Tăng Bạt Hổ + đài phun/quần áo
- Bậc: +10 người ngồi ăn theo cặp đối diện ở 2 chiếu nghỉ + chuyến C (STAIR_SITTERS), +2 sạp chân bậc (ĐẬU HŨ NÓNG chiếu 2, BẮP NƯỚNG chiếu 1), +2 cụm bàn thấp chân thang. Render M đạt: bậc rộng hoành tráng, đèn cầu, sạp bậc, tháp đồng hồ.
- Tăng Bạt Hổ: sạp hoasua tại (−128; 19,5) cuối trục — nồi sữa phụ + khói/hơi, tủ bánh, 3 bàn thấp × 2 người + ly sữa, hàng chờ 4 (side), menu sữa đậu nành nóng 10 / sữa nành bò 12 / bánh tiêu 7 / sừng trâu 10 (district D). Render N đạt.
- Đài phun nước tại (24,5; 5,2) — sân đông TRƯỚC chợ, ĐỐI DIỆN bậc tam cấp (neo theo lời Chung Hy + ảnh 44 vòng xoay phun nước): bồn Ø5,4 + đĩa nước + cột/bát + 6 tia + 4 uplight + glow disc + solid (FORBIDDEN trong harness). KHU QUẦN ÁO phía phải đối diện bậc: 2 sạp aokhoac (40; 17,5) + aolen (40; 22,5) district W rotY −π/2 + 5 giá treo đầy áo + kệ áo gấp + tấm sân; AW thêm nút 40 (36,2; 20) + 41 (42,5; 6,2), cạnh [27,41],[41,40] (đi vòng nam, né giếng thang + sạp cà phê — audit bắt được 2 lần cắt trước khi chốt).
- Pull-over giao hàng #2: banhtrang → khoai (banhtrang đã dời z 22,25, xe không với tới; khoai front cách điểm đỗ 4,9u).
### F. Cổng kiểm chứng (trên index.html CUỐI, sau mọi sửa)
- diag_runtime 900 frame SẠCH + SEED_SAVE 300 frame SẠCH; audit_ground_v54: 57 tuyến + AW 42 nút + 31 sạp — 0 lỗi cứng, 0 nhảy lưới; harness giao thông 26/26 PASS.
- Render draft Blender (480×360): K/L khung mở đầu ngày/đêm, M bậc tam cấp, N Hoa Sữa — đạt như mô tả trên; O/P (đài phun/quần áo) KHÔNG ra được khung sạch sau 3 lần đặt camera trong cảnh gương (khuất bởi khối thang/cầu/sạp mặt tiền) — 2 hạng mục này chỉ kiểm chứng bằng audit (tới được, không cắt solid) + harness (FORBIDDEN đài phun), CHƯA có ảnh render đối chiếu. Đám đông bị tắt trong render (dup_tree >10s/người dưới CPU chia sẻ) — đời sống trong render mỏng hơn game thật.
- Ghép renders/r25-doi-chieu-v55.png (ảnh thật 40 | khung V5.4 từ image-59 | render V5.5).
- Đóng gói standalone: 10.424.734 byte ≤ 10.485.760 (dư 61.026; V5.4 là 10.409.634, +15.100 cho toàn bộ V5.5 — không GLB mới).
- CHƯA kiểm chứng được: grade NGÀY trên web thật + FPS thật — chỉ chốt khi Chung Hy chơi thử (môi trường kiểm không chạy được WebGL). Đúng 1 đợt polish (nâng cổng + pitch 0,38 + sửa góc render).

## SWEEP-1 (09/11) — RÀ LỖI TOÀN BẢN ĐỒ SAU V5.5 (Chung Hy ngủ, làm liên tục; KHÔNG upload/push)
Phương pháp: chạy lại toàn bộ cổng trên bản V5.5 (diag 900 + seed 300 SẠCH, audit 0/0, xe 26/26 — đường cơ sở đạt hết) → rà code từng hệ thống → 2 hạng mục V5.5 thiếu render được soi bằng cảnh Blender TỐI THIỂU dựng đúng số đo code (scripts/render_sweep1_mini.py; cảnh gương toàn map render_v55.py đặt camera 3 lần đều trượt/khuất do hình học xung quanh trong gương lệch game — shot S1/S2/S3 của render_sweep1.py không dùng làm bằng chứng, giữ file để đối chiếu). Đúng 1 đợt polish gồm 4 sửa dưới đây.

### DANH SÁCH LỖI
- [x] **SW-01 (HỆ THỐNG, trung bình–cao) — Minimap không phủ trục mới.** Bằng chứng: mmX=(x+88)/176*156 chỉ phủ x −88..88 trong khi V5.5 kéo trục tới cổng −131, spawn −126, Hoa Sữa −128 → chấm người chơi tại spawn nằm NGOÀI khung (mmX(−126) = −33px), vạch đường chỉ vẽ tới −85, không mốc nào cho đài phun/khu quần áo/Hoa Sữa. SỬA: mmX nới thành (x+140)/232*156 (phủ −140..92), các hệ số bề rộng 176→232, vạch đường kéo tới −133, thêm 3 mốc: đài phun (chấm xanh 24.5; 5.2), khu quần áo (khối hồng 35.5..45.5 × 14..27.5), Hoa Sữa (chấm vàng −128; 19.5). Chấm đích/tự đi dùng chung mmX/mmY nên tự khớp.
- [x] **SW-02 (HÌNH HỌC, trung bình) — Tia đài phun nghiêng NGƯỢC dấu, chụm vào tâm.** Bằng chứng số: chạy three r160 thật (Euler XYZ như game): mọi tia có đầu tia r=0.095 (gần như chụm tại trục), chân tia r=0.745 → 6 tia thành hình chóp úp trên bát, không phải phun ra ngoài. Render mini M2 (trước sửa) thấy rõ "lồng nan" hội tụ. SỬA: rotation.z = −cos(a)·0.6, rotation.x = +sin(a)·0.6 → đầu tia r=0.745 xòe ra ngoài, vẫn nằm gọn trong bồn (r nước 2.45); render mini M1 (sau sửa) xác nhận tia xòe + bóng tia tỏa tròn trên mặt bồn.
- [x] **SW-03 (BỐ CỤC, trung bình) — 2/3 giá quần áo bị sạp che khuất hẳn.** Bằng chứng: giá cao 1.55 đặt tại x=42.1 ngay sau 2 sạp (sạp cao ~3.2, lưng x≈41.9) → từ quảng trường phía tây không thấy áo treo, khu quần áo trông như 2 sạp thường (render mini M3/M4 trước sửa: áo chỉ ló qua khe 0.7 giữa 2 sạp). SỬA: dời 2 giá ra 2 ĐẦU TRƯỚC của dãy — (36.9; 14.9) và (36.9; 25.1), lệch mặt sạp (37.9) ≥1.35 theo z nên không chắn điểm tương tác; giá đầu nam (40; 26.3) giữ nguyên. Render mini M3/M4 sau sửa: 2 giá áo màu quay mặt ra quảng trường, mặt sạp vẫn trống — khu đọc rõ là KHU QUẦN ÁO.
- [x] **SW-04 (VA CHẠM, nhẹ) — Giá treo thiếu collider.** Vật cao 1.55 mà không có solid() → người chơi đi xuyên qua giá (18 điểm solid toàn game đều là công trình/sạp/vật lớn tương tự). SỬA: thêm solid() cho cả 3 giá theo vị trí cuối (0.4 × 1.25, hướng dài dọc z vì rotY −π/2); đối chiếu tay: không cắt cạnh AW nào (41→40, 27→41 lệch ≥0.9), audit sau sửa vẫn 0/0.
- [ ] **SW-05 (HIỆU NĂNG, nhẹ — ghi nhận, không sửa đợt này):** số đo PERF sau V5.5: 25.6k object · 20.9k mesh · 4.03M tam giác (+7.2% so với V5.4 sau tối ưu 3.76M) · caster ~8.45k (+6.5%) · đèn điểm bật ban đêm 37 (V5.4: 34 — do đèn đường đoạn kéo dài) · draw call ước lượng đêm ~21.1k (+8.7%), ngày ~29.6k (+8.3%). Tăng tỉ lệ với nội dung mới (đường dài ×2 + 3 khu mới); vật mới đã qua castOK + đóng băng ma trận (frozen 13.608 = 53%). Không cắt nội dung trong đợt rà lỗi; muốn ép thêm phải làm đợt hiệu năng riêng (merge hình học tĩnh — đã ghi nhận từ V5.4-D là hướng rủi ro cho frustum culling/bật-tắt sạp đêm).
- [ ] **SW-06 (HỒ SƠ, nhẹ — ghi nhận):** mục V5.5 ghi "+5 giá treo" nhưng code game có 3 giá độc lập + 2 sạp (con số 5 là của cảnh gương render, nơi vẽ thêm giá tại vị trí sạp). Không ảnh hưởng game; lưu ý khi trích dẫn số liệu sau này.
- [ ] **SW-07 (NHẸ — ghi nhận):** chưa có biển CHỈ ĐƯỜNG tới khu quần áo/đài phun (chỉ có biển tên đường Tăng Bạt Hổ + biển sạp). Khu nằm ngay sân đông, nhìn thấy từ quảng trường nên không coi là lỗi; nếu làm đợt trang trí tiếp theo thì thêm 1 biển chỉ đường ở góc sân (24; 10).

### ĐÃ RÀ — ĐẠT, KHÔNG LỖI
- Save cũ chohb3d-v1: load bằng Object.assign trên mặc định + guard riêng (wardrobe/equipped/soDacSan/dacSanGot/game/guide) — SEED_SAVE diag 300 frame SẠCH; sạp mới không cần migration (stamps/eaten khóa theo id, Sổ Đặc Sản tự suy từ STALL_DEFS nên 3 sạp mới đã có mặt).
- QUEUES: hoasua có hàng chờ 4 (side, không lấn làn vòng tay); aokhoac/aolen không hàng chờ — NHẤT QUÁN với mọi sạp goods cũ (len1/len2/rau/dacsan/tra đều không có), không phải thiếu sót.
- Tự đi AW: 42 nút liên thông toàn phần (chuỗi chính + nhánh 36–39 trục Tăng Bạt Hổ + nhánh 27→41→40 khu quần áo); audit 57 tuyến + AW + 31 sạp = 0 lỗi cứng, 0 nhảy lưới; mặt sạp 3 sạp mới tính đúng (hoasua (−128; 17.4), aokhoac/aolen x 37.9); hoạt cảnh tiểu thương suy theo district: hoasua 'pour', quần áo 'arrange' — hợp ngữ cảnh.
- Ánh sáng: đối chiếu từng giá trị trong applyDayNight với chuẩn V5.5 — ngày exposure 0.88 / sun 0.95 / hemi 0.55 / amb 0.10 / fog 0.0058 / trời chân 0xe8d5ae; đêm exposure 1.22 / fog 0.0058 / nền 0x0e1a30 — KHÔNG hồi quy. Grade ngày trên web thật vẫn là điểm mù đã biết (chỉ chốt khi Chung Hy chơi thử).
- Hình học các khu không đổi ở V5.5 (nhà lồng, sân thượng, cầu nổi, 2 sườn, trong nhà): audit đạt + không có thay đổi code kể từ các render đạt của V5.4/V5.5 (K/L/M/N) — verdict giữ nguyên ĐẠT.

### VERDICT TỪNG KHU
- Đường vào + trục Tăng Bạt Hổ + Hoa Sữa: ĐẠT (render V5.5 K/L/N + audit; nay thêm mốc minimap — SW-01).
- Bậc tam cấp: ĐẠT (render V5.5 M).
- Đài phun nước: ĐẠT SAU SỬA (cấu trúc đúng số đo; tia phun đã sửa dấu — SW-02; tỉ lệ bồn Ø5.8 × cao tổng ~2.7 hơi thấp/bẹt so với ảnh thật vòng xoay nhưng là tỉ lệ đã chốt ở V5.5, không tự ý đổi trong đợt rà lỗi).
- Khu quần áo: ĐẠT SAU SỬA (giá áo lộ ra quảng trường — SW-03 + collider SW-04).
- Nhà lồng / sân thượng / cầu nổi / sườn đông–tây / đồi: ĐẠT (không hồi quy).

### CỔNG SAU SỬA (bản cuối)
- diag_runtime index.html 900 frame SẠCH; SEED_SAVE 300 SẠCH; chạy trực tiếp trên index-standalone.html 300 SẠCH.
- audit_ground_v54: 0 lỗi cứng / 0 nhảy lưới. Harness giao thông: 26/26 PASS.
- Đóng gói standalone: 10.425.925 byte ≤ 10.485.760 (dư 59.835; +1.191 so với V5.5 — 4 sửa đều là code, không GLB mới).
- Ảnh kiểm chứng đợt này: renders/sw1-M1-fountain-draft.png (tia xòe sau sửa), sw1-M2-fountain-high-draft.png (bằng chứng chóp tia trước sửa), sw1-M3-clothing-draft.png + sw1-M4-clothing-row-draft.png (sau sửa). Script: scripts/render_sweep1_mini.py (+ render_sweep1.py lưu vết đường camera gương thất bại).
- CHƯA kiểm chứng được (giới hạn môi trường, như cũ): FPS thật + grade ngày trên web — chờ Chung Hy chơi thử. KHÔNG upload/push.

## SOUND-COLOR-1 (09/11) — ÂM THANH + MÀU SẮC THEO TƯ LIỆU THẬT (Chung Hy ngủ, làm liên tục; KHÔNG upload/push)
Phương pháp theo lệnh Chung Hy "tự tải về rồi coi trực tiếp": tải audio chợ đêm thật về
phân tích phổ + đo màu 19 ảnh thật bằng k-means. Toàn văn: research/22-am-thanh-va-mau-that.md.
- Audio thật: YouTube 4rPBnyriJjY, 13 phút 29s, opus 48kHz, 12,56 MiB → /tmp/sc22/yt1.webm
  (file tham khảo, KHÔNG nhúng vào game). Lịch sử tải: lần 1 worstaudio/worst kẹt 3,1MB (2 tiến
  trình cùng ghi 1 file, đã kill); lần 2 video kaVLoOsBbOk lỗi format; lần 3 `-f bestaudio/best`
  thành công trong 9 giây. Kết luận: dùng bestaudio/best, đừng dùng worstaudio/worst.
- Phổ thật (cửa sổ 30s): rì rầm 250–800Hz chiếm 47–70% lúc đông (lớp chủ); trầm <250Hz 23–35%;
  xì xèo 2,5–6kHz chỉ 1–2% lúc đông, vọt 8–13% lúc lặng (lớp phụ); dải giọng rõ 0,8–2,5kHz chỉ
  2–6% → nhiễu lọc băng tần là cách tái tạo ĐÚNG, không cần giọng nói tổng hợp. RMS dao động
  −17dB (đông nhất) → −31dB (lặng nhất).
- Màu thật: 19 ảnh, script scripts/sample_colors_sc22.py (k-means 4 màu + 3 dải).
### THAY ĐỔI ÂM THANH (sinh thủ tục WebAudio, KHÔNG file nhạc — trần standalone chỉ còn ~60KB)
- Ambience 5 lớp nhiễu lọc băng tần (murmur 500Hz / trầm 160Hz / xì xèo 4,2kHz / nước 1,1kHz /
  gió 280Hz), gain theo khu + ngày/đêm (phố ăn 1,0 / bậc 0,6 / đài phun nước 1,0 / đường vào
  0,35 / vắng-trên-cao gió 1,0; đêm rì rầm ×1,3, ngày ×0,8), LFO 0,07Hz cho rì rầm "thở",
  LFO 9Hz cho xì xèo lách tách. Xe máy vụt qua: quét sawtooth 70→165→70Hz 1,4s khi xe đường
  < 22u (cooldown 5s), âm lượng theo khoảng cách.
- Nút 🔊/🔇 trên HUD (state.muted lưu save chohb3d-v1, mặc định bật, guard save cũ); masterGain
  chung cho SFX + nhạc sân khấu + ambience; âm thanh chỉ khởi sau tương tác đầu tiên
  (AudioContext tạo từ SFX như hiện tại). Sửa 1 lỗi logic trong lúc kiểm: khu bậc tam cấp bị
  phố ăn nuốt do chồng lấn z (đã đổi thứ tự kiểm tra — bậc trước, phố ăn sau).
### THAY ĐỔI MÀU (chỉ albedo — chuyển được sang web; KHÔNG đụng exposure/đèn/sky)
- CROWD_SHIRTS: xanh rêu bão hòa 0x6b8f3e → 0x8d9287 xám rêu (đo 23% ảnh 30).
- AWNS mái bạt: cam sáng 0xe8862e → 0xc06c44 terracotta (đo ảnh 31, lặp #c16b44 ảnh 07);
  xanh lá sáng 0x3f9e4d → 0x68804f muted. Giữ đỏ nhấn 0xc8372d (khóa ≤5%).
- Nước đài phun 0x7fb2c9 → 0xa8cfe0 (nhạt theo #d3e9f5 ảnh 44).
- Áo treo giá: vàng chói 0xe8c832 → 0xd7d2bf kem sáng (đo 25% ảnh 30).
- ĐÃ ĐÚNG nên không sửa: mặt tiền kem 0xe3d7bd, nhựa<vỉa hè<sân, trời đêm 0x274263, đèn sodium.
  Đề xuất ghi nhận (không tự áp): nền trời đêm 0x0e1a30 hơi tối hơn dải trên ảnh 40 (#31395d) —
  chờ thấy trên web thật.
### CỔNG (bản cuối, sau đúng 1 đợt polish = sửa thứ tự khu)
- diag_runtime index.html 900 frame SẠCH; SEED_SAVE 300 SẠCH; diag trực tiếp trên
  index-standalone.html 300 SẠCH; audit_ground_v54: 0 lỗi cứng / 0 nhảy lưới;
  harness giao thông 26/26 PASS.
- Kiểm logic ambience riêng bằng AudioContext giả (scripts/test_ambience_sc1.mjs):
  5 lớp khởi đủ; gain từng khu khớp research/22 (phố ăn đêm mur 0,0715 / bậc đêm siz 0,0162 /
  đài phun wat 0,0450 / đường vào mur 0,0154 + gió 0,0216); bikePass + setMuted (lưu save)
  chạy sạch; tick khi actx=null an toàn (harness Node không có AudioContext nên ambience
  không khởi trong diag — đúng thiết kế).
- Đóng gói standalone: 10.431.877 byte ≤ 10.485.760 (dư 53.883; +5.952 so với SWEEP-1 —
  trong ngân sách ≤ ~15KB). Không GLB mới.
- CHƯA kiểm chứng được (giới hạn môi trường, như cũ): NGHE thật trên web + FPS thật + grade
  ngày trên web — chỉ chốt khi Chung Hy chơi thử. KHÔNG upload/push.

## PROPS-OPT-1 (09/11) — TỐI ƯU VẬT PHẨM: NHẸ MÀ ĐẸP (Chung Hy ngủ, làm liên tục; KHÔNG upload/push)
Mục tiêu: giảm tam giác/draw call mà không làm xấu sạp hero. Đo thật bằng script mới
scripts/measure_props.mjs (chạy index.html thật trong harness diag: đếm mesh/tri/caster
theo container + theo từng sạp + hiệu lực hiển thị). Baseline = bản SOUND-COLOR-1.
### BẢNG TRƯỚC → SAU (đo thật; số tri dao động nhẹ giữa các lần chạy do crowd ngẫu nhiên)
- Tổng mesh: 20.824 → 18.408 (−2.416, −11,6%). Tổng tam giác: 4.017.064 → 3.947.340 (−69.724, −1,7%).
- Hiển thị: mesh 17.038 → 14.623 (−2.415, −14,2%); tri 3.104.936 → 3.034.022 (−70.914, −2,3%).
- Sạp (31 sạp): mesh 5.938 → 3.841; mesh hiển thị 4.599 → 2.044 (−55,6%); tri hiển thị
  580.524 → 532.644 (−47.880); caster 2.491 → 1.673 (−818).
- World: tri hiển thị 256.562 → 208.350 (−48.212, nhờ giảm segment). Crowd/GLB gần như
  không đổi (dao động ngẫu nhiên ±0,5%).
- PERF=1 (diag_runtime): đêm estCalls 21.1k → 18.645 (−11,6%); ngày 29.6k → 26.303 (−11,1%);
  casters 8,45k → 7.658; tris 4,03M → 3.945.988; objs 25,6k → 23.140.
### NHÓM NẶNG NHẤT (baseline) — VÀ CÁCH XỬ LÝ
- Crowd 2,38M tri hiển thị (~60% tổng): 1 geometry Torso 926 tri (sphere 14×10 trong
  build_character) × 327 mesh dùng chung = 302.802 tri. KHÔNG rebuild character.glb đợt này
  (V5.4-D đã chốt không động geometry người — khớp tay/chân động); ghi vòng follow-up riêng:
  giảm sphere 14×10→10×7, rebuild bằng Blender headless, kiểm mặt render_face.py, ước −100k tri.
- Sạp: mỗi sạp ~190–232 mesh / ~28–31k tri; hero cao nhất dau 31.344, banhcan 30.912,
  caphe 29.896. Vật lặp nhiều: cầu nhỏ r<0,15 (885 mesh, trái cây/trứng) + cầu r<0,45
  (392) + trụ nhỏ (567) + cẩm tú cầu/bóng đèn world (1.012 + 686 cầu).
### ĐÃ SỬA (chỉ index.html, không GLB mới)
- Giảm segment theo kích thước (ball()/cyl()): cầu r<0,12 → 8×6 (96 tri, thay 160, −40%);
  r<0,45 → 9×7 (126 tri, thay 160, −21%); r≥0,45 giữ 10×8. Trụ: r<0,06 → 6 seg; r<0,12 → 8 seg;
  seg truyền rõ giữ nguyên (nồi, đĩa, cột đã tính tay). Không ảnh hưởng crowd (makePerson clone
  GLB, không dùng ball()/cyl()).
- Gộp mesh tĩnh trong từng sạp — mergeGroupStatics()/mergeStallStatics() (import
  BufferGeometryUtils từ three/addons): 839 nhóm gộp, 2.569 mesh tiết kiệm. Gộp theo
  (chữ ký thuộc tính + material object), clone geometry + bake ma trận tương đối của nhóm
  (không sửa geometry gốc dùng chung giữa các clone GLB; không dispose). Loại trừ: tiểu thương
  + đồ cầm tay, đèn lồng GLB (Lantern*/userData.baseY), ống rót pourStream, mesh có map
  (biển/thẻ giá), multi-material, mesh ẩn, skinned/morph, thiếu normal/uv. CastShadow của mesh
  gộp = bất kỳ nguồn nào đổ bóng; receiveShadow = true.
- 2 lỗi do đo sau gộp phát hiện + sửa (cùng 1 đợt polish của vòng này, ghi rõ để sau soi lại):
  (1) Bộ phận GLB (SkewerTrays/CheCups/...) là NHÓM ẩn chứa mesh con visible=true — kiểm chỉ
  o.visible sẽ gộp lọt chúng ra ngoài → hiện sai hàng của sạp khác (lần đo đầu stall visTri
  TĂNG +47k). Sửa: kiểm cả tổ tiên BÊN TRONG nhóm sạp. (2) 6 sạp nightOnly (xien/che/tron/
  dauhu/hutieu/chao) merged=0 vì nhóm sạp đang visible=false lúc gộp. Sửa: dừng vòng kiểm ở
  chính nhóm sạp (visibility của nhóm thì mesh gộp thừa hưởng đúng).
- Kiểm toàn vẹn sau gộp (scripts/measure_props.mjs → __stallCheck): 31/31 sạp đạt — vendor
  20–24 mesh, đèn lồng 4, biển/thẻ giá có map ≥2, pourStream còn trong scene-graph (sua/
  caphe/suatuoi). Không vật nào bị gộp mất.
- Sửa vật lệch chuẩn: rà palette theo research/22 — KHÔNG phát hiện vật nào còn lệch sau
  SOUND-COLOR-1 (mái bạt terracotta, áo kem, nước nhạt đã đúng); ghế nhựa xanh dương/đỏ là
  đúng ghế chợ thật — giữ. Không thêm/bớt vật phẩm nào ngoài biển chỉ đường.
### BIỂN CHỈ ĐƯỜNG (SW-07, treo từ SWEEP-1)
- Cột tại (24, 10) góc sân, y = groundH; 2 mặt signMesh 2.4×0.6 (hệ biển hiện có, không GLB):
  mặt tây 'KHU QUẦN ÁO →' / sub '← ĐÀI PHUN NƯỚC'; mặt đông 'ĐÀI PHUN NƯỚC →' / sub
  'BẬC TAM CẤP →' (hướng mũi tên đã tính theo hướng nhìn từng mặt). solid(24, 10, 0.3, 0.3).
- Kiểm chữ vừa khung bằng PIL (DejaVu Sans Bold ≈ Arial): tựa 84px rộng 773/871 ≤ 940, phụ
  44px 456/386 — không cần thu nhỏ. Audit xác nhận không cắt tuyến AW (cạnh gần nhất ~1,35u).
### RENDER KIỂM (cảnh nhỏ, theo đúng số đo code + số đoạn MỚI; script scripts/render_props_opt1_mini.py)
- renders/po1-P1-stall-dau-draft.png: cận sạp dau — 2 giỏ dâu trước quầy, bậc 3 tầng dâu,
  thùng bơ, 4 ly kem bơ, 3 đèn lồng, dây bóng: hình dạng/số lượng hàng KHÔNG đổi; cầu 8×6/9×7
  vẫn tròn ở cự ly chơi. ĐẠT.
- renders/po1-P2-sign-draft.png: biển (24,10) nhìn từ phía tây — chữ 'KHU QUAN AO' /
  'DAI PHUN NUOC' đọc được, sáng (MeshBasicMaterial trong game), vừa bảng. ĐẠT. Lưu ý: lần
  render đầu chữ bị ngược do xoay text Blender sai trục + tối do dùng Principled — lỗi của
  script render, KHÔNG phải game (đã sửa, render lại đạt; mũi tên →/← không hiện trong font
  mặc định của Blender nhưng có trong Arial của game — PIL đo được).
### CỔNG (bản cuối)
- diag_runtime index.html 900 frame SẠCH; SEED_SAVE 300 SẠCH; diag trực tiếp trên
  index-standalone.html 300 SẠCH; audit_ground_v54: 0 lỗi cứng / 0 nhảy lưới;
  harness giao thông 26/26 PASS. (VM restart 1 lần giữa đợt — mất /tmp/diag, đã khôi phục
  gói three r160 bằng npm rồi chạy lại đủ cổng trên bản cuối.)
- Đóng gói standalone: 10.437.357 byte ≤ 10.485.760 (dư 48.403; +5.480 so với SOUND-COLOR-1 —
  trong mục tiêu phụ ≤ +10KB; tăng là code JS gộp + biển, không GLB mới).
- CHƯA kiểm chứng được (giới hạn môi trường, như cũ): FPS thật + grade ngày trên web —
  chỉ chốt khi Chung Hy chơi thử. KHÔNG upload/push.
- Follow-up ghi nhận: crowd Torso 926 tri × 327 (vòng riêng, rebuild character.glb);
  SW-05 (hiệu năng tổng) coi như ĐÃ XỬ PHẦN SẠP — còn crowd + GLB là phần lớn còn lại.

## SWEEP-2 (09/11) — RÀ LẠI SAU PROPS-OPT-1 + SOUND-COLOR-1 (Chung Hy ngủ, làm liên tục; KHÔNG upload/push)
Mục tiêu: xác minh 2 vòng vừa rồi không làm hỏng gì trong game thật + thử lấy bộ render full đã kẹt RAM. Phương pháp: chạy lại toàn bộ cổng trên bản cuối + đo lại props + kiểm ambience bằng AudioContext giả + đối chiếu code minimap/biển/tia phun/thứ tự khu + render mini lại sạp dau + biển SW-07.

### ĐÃ KIỂM — ĐẠT, KHÔNG LỖI MỚI
- Gộp mesh (mục 1): diag 900 frame SẠCH (mergeStallStatics: mergedGroups=839, meshesSaved=2569 — khớp PROPS-OPT-1); measure_props.mjs chạy lại: stallCheck bad=0, 31/31 sạp đạt (vendor 20–25, đèn lồng 4, biển/thẻ có map ≥2, pour=true ở sua/caphe/suatuoi); 6 sạp nightOnly (xien/che/tron/dauhu/hutieu/chao) đều merged=26–29 > 0 — lỗi (2) của PROPS-OPT-1 không tái phát; SkewerTrays/CheCups… không lọt ra ngoài (visTri sạp không tăng bất thường). Tổng đo lại: mesh 18.350 (báo cáo PROPS-OPT-1: 18.408), tri 3.933.988 (3.947.340), tri hiển thị 3.010.442 (3.034.022) — chênh <0,8% do crowd ngẫu nhiên, trong dung sai đã ghi.
- Biển chỉ đường SW-07 (mục 2): code còn nguyên — cột (24,10) solid 0.3×0.3, 2 mặt 'KHU QUẦN ÁO →'/'← ĐÀI PHUN NƯỚC' và 'ĐÀI PHUN NƯỚC →'/'BẬC TAM CẤP →' đúng hướng nhìn từng mặt; audit 0/0 nên không cắt AW (cạnh gần nhất ~1,35u như đã ghi). Render mini lại trên bản hiện tại: po1-P2-sign-draft.png — chữ đọc được, vừa bảng, sáng. Lưu ý (đã biết từ PROPS-OPT-1, không phải lỗi game): mũi tên →/← không hiện trong font mặc định của Blender nhưng có trong Arial của game (PIL đã đo vừa khung).
- Âm thanh (mục 3): test_ambience_sc1.mjs chạy lại — TEST-AMB-OK: 5 lớp khởi đủ; khu bậc tam cấp (0,−15,11) đêm siz=0,0162 — KHÔNG còn bị phố ăn nuốt (thứ tự kiểm bậc-trước-phố-ăn còn nguyên dòng 3978); đài phun wat=0,0450; đường vào mur=0,0154 + gió 0,0216; bikePass chạy OK; setMuted(true/false) lưu save (savedCount=1); tick actx=null an toàn. SEED_SAVE 300 frame SẠCH (save chohb3d-v1 cũ + nút tắt tiếng).
- Minimap (mục 4): mmX=(x+140)/232*156 (phủ −140..92) — chấm spawn x=−126 → mmX≈9,4px, TRONG khung; 3 mốc mới còn nguyên: đài phun (24.5;5.2) xanh, khu quần áo rect (35.5..45.5 × 14..27.5) hồng, Hoa Sữa (−128;19.5) vàng; vạch đường kéo tới −133.
- Ánh sáng: đối chiếu nhanh applyDayNight — ngày exposure 0.88 / sun 0.95 / hemi 0.55 / fog 0.0058 = chuẩn V5.5, không hồi quy. Tia đài phun: dòng 2408 vẫn là dấu đã sửa (rotation.z=−cos·0.6, rotation.x=+sin·0.6); không render lại vì code không đổi kể từ M1/M2 của SWEEP-1.
- Render mini lại (bản hiện tại, Blender 5.0.1, 640×480): po1-P1-stall-dau-draft.png — 2 giỏ dâu trước quầy, bậc 3 tầng dâu, thùng bơ, 4 ly kem bơ, 3 đèn lồng, dây bóng: hình dạng/số lượng hàng KHÔNG đổi sau gộp; cầu 8×6/9×7 vẫn tròn ở cự ly chơi. ĐẠT.

### RENDER FULL 896×672 — KHÔNG CHẠY ĐƯỢC (mục 5, ghi rõ lý do, không cố)
- RAM available lúc bắt đầu đợt 633MB, sau render mini 791MB — xa dưới ngưỡng ≥2,5GB để dựng cảnh full (cần ~2,5–3GB ở khâu dựng cảnh; các dự án khác — Lục Phán, Mạnh Bà, Sen, Shorts — đang chạy chung máy). Góc cận bàn ăn (−21.6,−9.2,3.9) → cụm bàn (−17.4,−5.4) trong scripts/render_v54.py vẫn sẵn; thử lại khi máy trống. Đây là lần thứ 2 liên tiếp bị kẹt RAM (V5.4 cũng vậy).

### DANH SÁCH LỖI MỚI
- Không có lỗi mới. Không sửa code đợt này (không cần đợt polish — mọi mục đều đạt).

### CỔNG CUỐI (bản cuối, không đổi code so với PROPS-OPT-1)
- diag_runtime index.html 900 frame SẠCH; SEED_SAVE 300 SẠCH; diag trực tiếp trên index-standalone.html 300 SẠCH.
- audit_ground_v54: 0 lỗi cứng / 0 nhảy lưới (chỉ còn cảnh báo băng qua làn đã biết). Harness giao thông: 26/26 PASS.
- Standalone: 10.437.357 byte ≤ 10.485.760 (dư 48.403).
- CHƯA kiểm chứng được (giới hạn môi trường, như cũ): FPS thật + grade ngày trên web + nghe thật trên web — chỉ chốt khi Chung Hy chơi thử. Render full 896×672 vẫn treo vì RAM. KHÔNG upload/push.
- Follow-up còn treo (từ các vòng trước): crowd Torso 926 tri × 327 mesh (~60% tri hiển thị) — vòng riêng rebuild character.glb; tỉ lệ đài phun hơi bẹt so với ảnh thật (đã chốt ở V5.5, không tự đổi).

## CROWD-OPT-1 (09/11) — REBUILD character.glb THẤP POLY: THÂN/TAY (Chung Hy ngủ, làm liên tục; KHÔNG upload/push)
Bối cảnh: PROPS-OPT-1 ghi crowd Torso 926 tri × 327 mesh (~60% tri hiển thị); V5.4-D từng chốt
không động geometry người vì sợ vỡ neo khớp tay/chân. Vòng này CHỈ đổi nếu chứng minh an toàn
(4 tiêu chí dưới) — kết quả: ĐẠT HẾT, ĐÃ ĐỔI (giữ GLB mới).
### BASELINE (đo thật bằng scripts/dump_character_glb.mjs, three r160 GLTFLoader)
- character.glb cũ: 457.688 byte, 19 mesh, 12.736 verts, 6.168 tri/nhân vật.
- Phân bổ tri/nhân vật: Head 2.214 (Skin 784 + HairDark 926 + Blush 504) · Torso 864
  (hộp bo + bụng cầu 252 + 2 vai cầu 252×2) · ArmL/R 360 mỗi (hộp 108 + tay cầu 252) ·
  LegL/R 216 mỗi (chân hộp 108 + giày hộp 108) · tmpCollar 288 · HatBeanie 646 ·
  HatNonLa 320 · HatCap 288 · Scarf 396.
- Neo: LegL/R origin y=0,40 (pivot hông) · ArmL/R origin y=0,88 (pivot vai) · Head y=1,35 ·
  Torso y=0,66 · đỉnh đầu y=1,824 (mũ beanie 1,945). Số "Torso 926 tri" ở PROPS-OPT-1 là
  SAI — đo lại đúng là 864 tri (926 là phần HairDark của Head); số liệu vòng này lấy theo dump.
### PHƯƠNG ÁN (scripts/build_character_lp.py — copy build_models.py, chỉ build character)
- CHỈ giảm segment 4 sphere thân/tay: bụng + 2 vai 14×10 → 10×7; tay 14×10 → 8×6.
- GIỮ NGUYÊN: pivot chân/tay, tỉ lệ đầu (Head 2.214 tri không động), tên node, 4 phom,
  màu, mũ/khăn, hộp chân/tay (neo tủ đồ AR/ARMS/LEGS gắn theo kích thước hộp), collar.
- Backup bản cũ: prototype-v2/character-baseline-20261109.glb (ngoài assets/, không bị đóng gói).
### KẾT QUẢ SO SÁNH (đo thật, không đoán)
- GLB mới: 405.980 byte (−51.708, −11,3%) · 19 mesh · 11.208 verts · 5.428 tri (−740/người, −12,0%).
  Torso 864 → 468 (−396); ArmL/R 360 → 188 mỗi (−172 mỗi). Mọi phần khác y hệt số tri cũ.
- Dump đối chiếu: đủ 11 neo (LegL/R, ArmL/R, Torso, Head, 3 mũ, Scarf, tmpCollar), pivot
  y hệt; bbox Torso 0,973×0,645×0,434 → 0,960×0,645×0,423 (hẹp 6mm/bên do dây cung mặt
  cầu 10 đoạn — <1,2% bề rộng, không thấy ở cự ly chơi); Arm 0,166 → 0,170 (tay 8 đoạn,
  chênh 2mm/bên).
- Render so sánh cũ/mới cùng góc/đèn/mũ (scripts/render_crowdopt_compare.py, Cycles 24,
  512×512; co1-old/new-front/torso/side.png): chính diện + cận thân 3/4 + nghiêng — KHÔNG
  phân biệt được (nhân vật vốn đã faceted kiểu chibi; bụng/vai/tay giảm segment không lộ
  ngay cả ở cận cảnh). Tiêu chí (a) ĐẠT.
- Mức scene (scripts/measure_props.mjs, cùng nội dung, crowd 413 người): tổng tri
  3.933.988 (SWEEP-2) → 3.634.496 (−299.492, −7,6%); tri HIỂN THỊ 3.010.442 → 2.713.730
  (−296.712, −9,9%) — VƯỢT xa mục tiêu −100k (khớp ước tính 413 người × 740 ≈ 305k).
  Crowd container: tri 2.096.876 (hiển thị 1.596.192); stallCheck bad=0, 31/31 sạp đạt.
### CỔNG CUỐI (bản cuối, GLB mới đã thay vào assets/character.glb)
- diag_runtime index.html 900 frame SẠCH; SEED_SAVE 300 SẠCH; diag trực tiếp trên
  index-standalone.html 300 SẠCH (SRC_FILE=index-standalone.html — lưu ý: biến GAME_FILE
  không có tác dụng, lượt đầu chạy nhầm index.html).
- audit_ground_v54: 0 lỗi cứng / 0 nhảy lưới (chỉ cảnh báo băng qua làn đã biết).
  Harness giao thông: 26/26 PASS.
- Standalone: 10.368.413 byte ≤ 10.485.760 (dư 117.347 — NHẸ hơn trước 68.944 nhờ GLB nhỏ).
- CHƯA kiểm chứng được (giới hạn môi trường, như cũ): FPS thật + grade ngày trên web +
  nghe thật trên web — chỉ chốt khi Chung Hy chơi thử. KHÔNG upload/push.
- Follow-up ghi nhận: Head 2.214 tri/người (tóc 926 + má 504 + da 784) nay là phần nặng
  nhất của nhân vật (~36%) — nếu làm vòng nữa: giảm segment cầu mặt (mắt/má/miệng) cần soi
  mặt kỹ vì mặt là điểm nhìn; ước −367k tri hiển thị nếu 10×7 toàn đầu. Tỉ lệ đài phun hơi
  bẹt so với ảnh thật (đã chốt ở V5.5, không tự đổi).

## HEAD-OPT-1 (09/11) — REBUILD character.glb THẤP POLY: CẦU MẶT (Chung Hy ngủ, làm liên tục; KHÔNG upload/push)
Bối cảnh: CROWD-OPT-1 xong, Head 2.214 tri/người là phần nặng nhất nhân vật. Tiêu chuẩn
đổi KHẮT KHE HƠN thân/tay: mặt là điểm nhìn — render so sánh cận mặt 3 góc, khác dù nhẹ
thì giữ bản cũ. Kết quả: bản 10×7 TOÀN ĐẦU BỊ BÁC ở khâu soi mặt; bản POLISH (chỉ giữ
mắt/tai ở 14×10) ĐẠT HẾT, ĐÃ ĐỔI.
### BASELINE (đo thật bằng scripts/dump_character_glb.mjs, three r160)
- character.glb sau CROWD-OPT-1: 405.980 byte, 19 mesh, 11.208 verts, 5.428 tri/người.
- Head 2.214 (Skin 784 = đầu 252 + 2 tai 252×2 + mũi ~28 · HairDark 926 = tóc ~170 sau
  cắt + 2 mắt 252×2 + miệng 252 · Blush 504 = 2 má 252×2). Neo: LegL/R y=0,40 ·
  ArmL/R y=0,88 · Head y=1,35 · đỉnh đầu 1,824.
### PHƯƠNG ÁN (scripts/build_character_head_lp.py — copy build_character_lp.py)
- Lần 1 (10×7 toàn đầu): đầu + tóc + mắt + má + miệng + tai 14×10 → 10×7.
- Lần 2 POLISH (1 đợt polish duy nhất): mắt + tai TRẢ VỀ 14×10; đầu/tóc/má/miệng giữ
  10×7. GIỮ NGUYÊN: pivot chân/tay, tỉ lệ đầu, tên node, 4 phom, màu, mũ/khăn, thân/
  tay/chân đã tối ưu. Backup GLB CROWD-OPT-1: prototype-v2/character-crowdopt1-
  20261109.glb (ngoài assets/, không bị đóng gói); bản cũ hơn nữa vẫn ở
  character-baseline-20261109.glb.
### SO SÁNH RENDER (scripts/render_headopt_compare.py, Cycles 24, 512×512, beanie)
- Bản 10×7 toàn đầu (renders/ho1-new-*): chính diện ĐẠT (không phân biệt được); 3/4
  KHÔNG ĐẠT — mắt lộ rõ cạnh facet, viền mắt thành đa giác ở cận cảnh; nghiêng KHÔNG
  ĐẠT — tai lộ facet rõ. → BÁC bản này theo đúng luật "khác dù nhẹ thì giữ".
- Bản POLISH (renders/ho1-polish-*): chính diện ĐẠT; 3/4 ĐẠT — mắt tròn lại như cũ;
  nghiêng ĐẠT — crop phóng 2× vùng tai giống hệt bản cũ (diff số vùng tai 1,51 so với
  3,14 của bản bị bác; phần còn lại là nhiễu render Cycles 24 mẫu). Tiêu chí (2) ĐẠT.
### KẾT QUẢ SO SÁNH (đo thật)
- GLB polish: 361.500 byte (−44.480, −11,0%) · 19 mesh · 9.934 verts · 4.810 tri
  (−618/người, −11,4%): Head 2.214 → 1.596 (Skin 784→652, HairDark 926→704,
  Blush 504→240). Mọi phần khác y hệt số tri cũ.
- Dump đối chiếu: đủ 11 neo, pivot y hệt; bbox Head 0,943×0,924×0,995 →
  0,943×0,924×0,984 (rộng y hệt nhờ tai giữ nguyên, sâu −1,1% do dây cung tóc 10
  đoạn — trong dung sai <1,2%). Tiêu chí (3) ĐẠT.
- Mức scene (scripts/measure_props.mjs, crowd 413 người): tổng tri 3.634.496 →
  3.372.650 (−261.846, −7,2%); tri HIỂN THỊ 2.713.730 → 2.472.922 (−240.808,
  −8,9% — bằng ~65% ước tính −367k của bản toàn đầu, đổi lại mặt an toàn tuyệt đối).
  Crowd container tri 2.096.876 → 1.861.284; stallCheck bad=0, 31/31 sạp đạt.
### CỔNG CUỐI (bản cuối, GLB polish đã thay vào assets/character.glb)
- diag_runtime index.html 900 frame SẠCH; SEED_SAVE 300 SẠCH; diag trực tiếp trên
  index-standalone.html 300 SẠCH (SRC_FILE=index-standalone.html).
- audit_ground_v54: 0 lỗi cứng / 0 nhảy lưới (chỉ cảnh báo băng qua làn đã biết).
  Harness giao thông: 26/26 PASS.
- Standalone: 10.309.105 byte ≤ 10.485.760 (dư 176.655 — NHẸ hơn trước 59.308 nhờ
  GLB nhỏ lại).
- CHƯA kiểm chứng được (giới hạn môi trường, như cũ): FPS thật + grade ngày trên web +
  nghe thật trên web — chỉ chốt khi Chung Hy chơi thử. KHÔNG upload/push.
- Follow-up ghi nhận: Head nay 1.596 tri/người (~33% nhân vật); mắt/tai đã giữ 14×10
  nên không giảm thêm được nếu không động vào mặt — coi như đã chạm trần an toàn cho
  character.glb. Tỉ lệ đài phun hơi bẹt so với ảnh thật (đã chốt ở V5.5, không tự đổi).

## SWEEP-3 (09/11) — KIỂM CUỐI TRƯỚC KHI GIAO 10:00 (Chung Hy ngủ, làm liên tục; KHÔNG upload/push)
Mục tiêu: xác minh bản CUỐI sau 2 lần đổi character.glb + gộp mesh + âm thanh + biển
chỉ đường. Phương pháp: chạy lại TOÀN BỘ cổng trên bản cuối + dump GLB + script kiểm
mới scripts/check_sweep3.mjs (chạy index.html thật trong harness diag: đếm NPC theo
phom/mũ/khăn/màu/tông da + mặc thử tủ đồ từng slot và kiểm neo AR/ARMS/LEGS).
### ĐÃ KIỂM — ĐẠT
- GLB (scripts/dump_character_glb.mjs, three r160): assets/character.glb = bản polish
  HEAD-OPT-1 — 19 mesh, 9.934 verts, 4.810 tri/người; đủ 11 neo; pivot LegL/R y=0,40 ·
  ArmL/R y=0,88 · Head y=1,35 · đỉnh đầu 1,824 — y hệt baseline. Head 1.596 (Skin 652
  + HairDark 704 + Blush 240); Torso 468; ArmL/R 188 mỗi.
- NPC (check_sweep3, 382 người wanderers+statics; +31 vendor trong sạp = 413 khớp
  diag): phom puffer 116 / coat 55 / hoodie 60 / knit+light 151 — đủ 5 phom; màu áo
  Torso 38 màu distinct; tông da 4 tông (3 recolor #a96f42/#c68a5e/#e8b98f + 1 mặc
  định GLB #f7dbc5 — makePerson chỉ recolor khi skin khác 0xd9a37e); mũ beanie 141 /
  nón lá 10 (chỉ vendor) / cap 48 / không mũ 183; khăn hiện 164; cầm ly 105.
- Tủ đồ 60 món (12 mũ / 8 khăn / 10 áo / 10 tay cầm / 12 phụ kiện / 8 giày):
  neo LL/LR/AL/AR đủ (dump pivot y hệt); mặc thử M1+K1+A2+T1+G2+P1+P5: mũ beanie
  hiện, nón lá ẩn, khăn hiện, áo #35507a, tay cầm AR 1/1, găng ARMS 2/2, tất+giày
  LEGS 2/2; đổi M6: nón lá hiện, beanie ẩn; đổi M8: mũ #2f8f83 + map sọc; tháo hết:
  mọi node/phụ kiện ẩn. Save cũ SEED_SAVE 300 frame SẠCH.
- Cổng khác chạy lại: audit_ground_v54 0 lỗi cứng / 0 nhảy lưới (chỉ cảnh báo băng qua
  làn đã biết); giao thông 26/26 PASS; test_ambience_sc1.mjs TEST-AMB-OK (bậc đêm
  siz=0,0162 — không bị phố ăn nuốt; đài phun wat=0,0450; setMuted lưu save);
  measure_props.mjs stallCheck bad=0, 31/31 sạp đạt.
### LỖI MỚI — SW-08 (TỦ ĐỒ, TRUNG BÌNH–CAO) — ĐÃ SỬA TRONG VÒNG (1 đợt polish duy nhất)
- Phát hiện: check_sweep3 lần đầu FAIL 2 điểm; probe riêng scripts/probe_wdpaint.mjs
  (đã xóa sau khi dùng — số liệu ghi tại đây) chứng minh lỗi GAME thật, không phải
  lỗi script kiểm: `wdMats` chỉ còn `['Scarf']` — makePerson() đã recolor() Shirt/
  Beanie bằng repMat() (material KHÔNG tên, cache dùng chung) TRƯỚC khi khối tủ đồ
  traverse theo `o.material.name` → wdPaint('Shirt'/'Beanie') thành no-op.
  Hậu quả: mặc áo khoác A1–A10 không đổi màu áo người chơi (mặc A2 navy #35507a,
  thân vẫn đỏ đô #a62b25); mặc mũ len M8 teal+sọc không đổi màu/không có sọc.
  Nặng nhất: áo/mũ có parts:[] (A3/A4/A7/A8/A10, M1/M8/M9) mua xong KHÔNG THẤY GÌ
  KHÁC — trả Xu mà không có hiệu ứng nhìn thấy. Khăn (mat Scarf) vẫn đúng vì
  material Scarf không bị recolor trong makePerson. Lỗi tồn tại từ V4.4, chưa ai
  bắt vì áo/mũ có parts vẫn hiện phụ kiện nên trông như "đã mặc".
- Sửa (chỉ index.html, ~15 dòng): bắt vật liệu theo TÊN NODE thay vì tên material —
  wdCapture('Shirt','Torso') / ('Beanie','HatBeanie') / ('Scarf','Scarf'), clone
  riêng cho player rồi gán lại cho đúng mesh đó (không mutate material dùng chung
  với NPC qua _repCache); tmpCollar gắn cùng clone Shirt để cổ áo đổi màu theo.
  Kiểm lại: probe cho torso #35507a + scarf #2e6b46 sau khi mặc A2/K1; check_sweep3
  chạy lại ALL CHECKS PASS (fails: []).
- 2 lỗi ĐO của script kiểm (không phải lỗi game, đã sửa script): (1) đếm tông da
  theo material.name==='Skin' — recolor đã đổi tên → đếm bằng màu trong NPC_SKINS;
  (2) đọc màu mũ từ group HatBeanie (group không có material) → đọc từ mesh con
  đầu tiên trong group.
### RENDER FULL 896×672 — KHÔNG CHẠY ĐƯỢC, LẦN THỨ 3 LIÊN TIẾP (ghi rõ, không cố)
- RAM available lúc kiểm 393–457MB — xa dưới ngưỡng ≥2,5GB để dựng cảnh full
  (các dự án khác đang chạy chung máy). Góc cận bàn ăn trong scripts/render_v54.py
  vẫn sẵn; thử lại khi máy trống.
### CỔNG CUỐI (bản cuối, sau sửa SW-08 + đóng gói lại)
- diag_runtime index.html 900 frame SẠCH; SEED_SAVE 300 SẠCH; diag trực tiếp trên
  index-standalone.html 300 SẠCH.
- audit_ground_v54: 0 lỗi cứng / 0 nhảy lưới. Harness giao thông: 26/26 PASS.
- Standalone (đóng gói lại sau sửa): 10.310.053 byte ≤ 10.485.760 (dư 175.707;
  +948 so với HEAD-OPT-1 — chỉ code fix SW-08; script standalone chứa marker
  'SWEEP-3 (SW-08)' đã kiểm bằng grep). GLB raw total 7.418.176 byte.
- Số đo cuối (measure_props): mesh 18.301 | tri 3.362.494 | hiển thị 14.498 mesh /
  2.455.108 tri; crowd tri 1.862.452 (vis ~1,37M); stallCheck 31/31.
### TÓM TẮT V5.4 → BẢN CUỐI (để giao 10:00)
- V5.4 10.409.634 → V5.5 10.424.734 (đường ×2,5 rộng/dài ×2, Hoa Sữa Tăng Bạt Hổ,
  bậc tam cấp, đài phun, khu quần áo, hạ chói ngày, góc mở đầu) → SWEEP-1 10.425.925
  (minimap phủ trục mới, tia phun đảo dấu, giá áo dời, collider giá) →
  SOUND-COLOR-1 10.431.877 (ambience WebAudio 5 lớp theo khu, màu albedo theo ảnh
  thật) → PROPS-OPT-1 10.437.357 (gộp 839 nhóm sạp, biển chỉ đường SW-07) →
  SWEEP-2 10.437.357 (không lỗi mới) → CROWD-OPT-1 10.368.413 (thân/tay −740 tri/
  người) → HEAD-OPT-1 10.309.105 (đầu −618 tri/người, bản polish) → SWEEP-3
  10.310.053 (sửa SW-08 tủ đồ). Nhân vật 6.168 → 4.810 tri/người (−22%); tri hiển
  thị 3.104.936 (V5.4) → 2.455.108 (−21%).
- CHƯA kiểm chứng được (giới hạn môi trường, như cũ): FPS thật + grade ngày trên
  web + nghe thật trên web — chỉ chốt khi Chung Hy chơi thử. Render full 896×672
  vẫn treo vì RAM (lần 3). KHÔNG upload/push — chờ Chung Hy dậy 10:00 bấm thẻ.
- Follow-up còn treo: khổ thang 22u vs ~15–18m thật + đảo Ø21u (refactor địa hình
  lõi, đợt riêng, chưa duyệt); tỉ lệ đài phun hơi bẹt (đã chốt V5.5, không tự đổi);
  character.glb đã chạm trần an toàn (mắt/tai giữ 14×10).

## NPC-SPECIAL-1 (09/11) — NHÂN VẬT ĐẶC BIỆT CÓ THIẾT KẾ RIÊNG (phản hồi Chung Hy 08:53; KHÔNG upload/push)
### YÊU CẦU
- NPC phải ĐẶC BIỆT hơn hẳn đám đông: mặt riêng, ĐỒNG PHỤC RIÊNG chỉ của vai đó,
  đạo cụ theo vai (hát = cầm đàn). Đám đông thường GIỮ NGUYÊN; ngân sách ≤ +60KB.
### CÁCH GẮN (không sửa GLB — trần an toàn)
- `paintNode(g, nodeName, hex)`: sơn theo TÊN NODE (bài học SW-08 — tránh recolor
  theo tên material vì mũ cap dùng material 'CapBlue' không đổi được bằng hatColor).
- `headProp(g, geo, hex, x, y, z)`: gắn prop vào node Head theo tọa độ mặt local
  (mắt ±0.16/+0.045/0.42; đầu r=0.45, gốc Head y=1.35). `faceGlasses(g)`: gọng +
  cầu + 2 gọng tai (đợt polish: gọng tai dời x ±0.315→±0.29 để chạm mép gọng chính).
- Nhân vật tĩnh đăng ký qua `regSpecial` → addStatic kind 'special', rank=0 (luôn
  hiện), idle qua `st.spIdle(t, st)`; không solid mới (đúng quy ước NPC tĩnh).
### DANH SÁCH 12 NHÂN VẬT ĐẶC BIỆT
1. **Chú Ba coi bói** — bậc tam cấp (5.6, 11.63, −19.6), ngồi ghế trên chiếu nghỉ 1,
   trong bán kính modal coi bói sẵn có FORTUNE_PT (2.8, −19.2) r=3.4 (modal 20 Xu/quẻ
   ĐÃ CÓ từ trước — vòng này bổ sung HÌNH HÀI). Áo dài chàm 0x37455e (GEO_COATSKIRT +
   2 lapel) + quần trắng 0xe8e2d4; râu bạc + ria 0xb8b0a2; kính lão; khăn xếp chàm
   0x27324e (torus + cầu dẹt). Props: bàn + khăn trải đỏ + 3 thẻ bài + biển 'COI BÓI'.
   Idle: gật đầu nhẹ + tay gõ bàn.
2. **Ca sĩ góc hát** — sân khấu quảng trường (31, 17, −52), nhân vật + sân khấu +
   modal Góc Hát ĐÃ CÓ; vòng này nâng diện mạo: áo denim 0x2f4d6e + quần đen, mũ cap
   sơn đỏ rượu 0x8c2f39 (paintNode), kính mát, khăn đỏ rượu đồng bộ, thân đàn
   0x9c3a24. Idle gảy đàn sẵn có; 3 khán giả tĩnh sẵn có quay mặt về sân khấu.
3. **Chú giữ xe** — cạnh điểm thuê xe (37.6, 9.6): áo dạ quang 0xc8d93c + 2 sọc phản
   quang bạc 0xd8dde2, mũ cap cam 0xe8862e, cầm vé trắng 0xf5f2e8 tay phải. Idle ngó quanh.
4. **Cô lao công** — cạnh thùng rác Tăng Bạt Hổ (10.4, 10.8): áo bảo hộ 0x1f6f8b +
   sọc phản quang, mũ cap cam, găng cam; CHỔI cầm tay (userData.broom: cán + đầu +
   5 nan xòe). Idle quét qua lại.
5. **Anh xe ôm** — vỉa hè đầu trục Tăng Bạt Hổ (−120.5, 16.5): áo xanh 0x2e8b47, mũ
   bảo hiểm xanh 0x35a04f đội sẵn (headProp cầu phủ qua tóc + vành kem), cầm điện
   thoại. Idle ngó hai đầu đường.
6–12. **7 tiểu thương sạp hero** (diện mạo CỐ ĐỊNH bằng SPECIAL_VENDOR/dressSpecialVendor
   thay rollLook random): bánh tráng (tạp dề rêu 0x4a6741 + beanie cam), bánh căn (nón
   lá + tạp dề nâu 0x5c4633), súp cua (mũ cap kem 0xe8e2d4 sơn theo node + tạp dề đỏ đô
   0xa62b25), sữa đậu nành Hoa Sữa (nón lá + tạp dề xanh 0x2e6b46), cà phê (beanie đen +
   tạp dề đỏ rượu 0x8c2f39), đậu (beanie kem + tạp dề vàng 0xd9a62e), Hoa Sữa (beanie kem
   0xf0ead8 đọc như khăn trùm đầu + tạp dề xanh ngọc 0x2e7d6b).
### TƯƠNG TÁC
- Chú Ba: modal coi bói sẵn có (bán kính 3.4 quanh FORTUNE_PT) — nay đã có người ngồi
  đúng chỗ. Ca sĩ: modal Góc Hát sẵn có. Không thêm hệ thoại mới (đã có sẵn cả hai).
### KIỂM CHỨNG
- check_sweep3.mjs MỞ RỘNG (mục 4, bọc `__sw3`): ALL CHECKS PASS — 7 vendor đúng
  áo/tạp dề/mũ theo từng sạp; 4 special đúng vị trí/rank 0/kind 'special'/đủ props;
  ca sĩ đúng áo/cap/đàn.
- Render mini Blender (scripts/render_npc_special_mini.py, 640×480): sp1-chuba /
  sp1-singer / sp1-sweeper — soi trực tiếp: khăn xếp + kính ôm đúng mắt + râu bạc +
  bàn thẻ đạt; đàn ôm trước ngực + cổ đàn chéo đạt; chổi chạm đất + sọc phản quang
  đạt. Màu trong render Blender rửa sáng hơn web (artifact quen thuộc — hex trong
  game đã xác nhận bằng check_sweep3). Đúng 1 đợt polish (gọng tai kính + khung hình
  render) — đã sửa + render lại xác nhận.
- Tổng người sau vòng: 417 (413 + 4 special mới).
### CỔNG CUỐI
- diag_runtime index.html 900 SẠCH; SEED_SAVE 300 SẠCH; diag trực tiếp trên
  index-standalone.html 300 SẠCH.
- audit_ground_v54: 0 lỗi cứng / 0 nhảy lưới (chỉ cảnh báo băng qua làn đã biết).
  Harness giao thông: 26/26 PASS.
- Standalone: 10.320.595 byte (+10.542 so với 10.310.053 trước vòng; ngân sách
  +60.000; dư trần 10.485.760 là 165.165).
- CHƯA kiểm chứng được (như cũ): FPS thật + grade ngày trên web + nghe thật — chỉ
  chốt khi Chung Hy chơi thử. KHÔNG upload/push — chờ lệnh Chung Hy.

## GEOMETRY-2 (09/11) — 6 ĐIỂM CHƠI THỬ TRỰC TIẾP CỦA CHUNG HY 09:04: DƯỚI BẬC / ĐỆM ĐẢO / ĐƯỜNG VÀO / BÙNG BINH ĐẦU CHỢ / ĐÁM ĐÔNG (KHÔNG upload/push)
### PHƯƠNG PHÁP KIỂM CHỨNG (theo lệnh đợt này)
- KHÔNG báo cáo bằng con số cho hình học. Render tầm mắt người đi bộ bằng
  scripts/render_geo2.py (parse trực tiếp index.html lúc chạy) TRƯỚC/SAU cùng
  khung: renders/geo2-before-*.png / geo2-after-*.png (a spawn, b giữa đường,
  c dưới bậc, d đệm đảo–bậc, d2 từ tâm đảo [mới], e phố ăn). Verdict dưới đây
  là theo render đã soi trực tiếp.
- Ảnh/texture sinh thêm: KHÔNG dùng Google Flow — biển hiệu dựng bằng
  signMesh chữ canvas như chuẩn cũ, tránh phụ thuộc phiên trình duyệt.
### ĐIỂM 1 — MỞ RỘNG PHẦN DƯỚI BẬC TAM CẤP
- Tấm sân chân bậc kéo dài về tây: Box(58, 0.08, 13) tại (9, 0.01, 3) — phủ
  x −20..38 (trước tới khoảng −8). Bàn sân dời theo: plazaTable (17.4, 8.6)
  và (18.5, −1.6); người ngồi vô bàn cũ (−17, 5.7) dời về (16.4, 9.4).
- Cặp sạp chân bậc phía TÂY dời hẳn ra trục đường vào (bánh ướt cuốn →
  (−87.5, −13.4); nước mía → (−151.15, 23.2)) — chân bậc tây hết bị sạp án.
- Đảo lùi −6 (điểm 2) cũng giải phóng phía tây sân.
- VERDICT (render d2 + e): ĐẠT — từ tâm đảo và từ phố ăn đều thấy dải sân mở
  liên tục giữa đĩa đảo và chân bậc; khung (c) nhìn LÊN bậc không đổi (đúng
  thiết kế: phần mở rộng nằm dưới bậc, không phải mặt bậc).
### ĐIỂM 2 — KHOẢNG ĐỆM BÙNG BINH ↔ BẬC
- Toàn bộ cụm đảo dời −6 theo x: tâm (−24, −6) → (−30, −6); tượng
  (−28.2, −2.8) → (−34.2, −2.8). Mọi thứ neo theo đảo dời đồng bộ: rb.position
  + solid + spotlight + glowDisc + biển BÙNG BINH HOA + vành uplight + ringRoad
  + bệ đá + sitters vành + eatSet/eatCluster/flowerStall + photoPerson + fam +
  xe đậu quanh đảo + trashBin + stringLights + fog; profile làn xe dịch theo
  (islandBump/vehBumpE/laneZW), RB_ARC R~11.3–12 quanh tâm mới, slowCapFor
  vùng cung nam đảo x −50..−12, GUIDE stage 1–2 + achievement 'Vòng xoay Hòa
  Bình' + POI fallback đều trỏ (−30, −6).
- VERDICT (render d2): ĐẠT vừa phải như lệnh (không tách xa) — đĩa đảo và
  chân bậc không còn lấn nhau, giữa hai mốc có dải sân/đường đệm đọc được rõ
  bằng mắt. Khung (d) cũ (−16, 1) cả TRƯỚC lẫn SAU đều bị sườn địa hình của
  cảnh render tối thiểu nuốt — không dùng (d) để kết luận, đã thay bằng (d2).
### ĐIỂM 3 — ĐƯỜNG VÀO RỘNG HƠN RẤT NHIỀU + SẠP LIÊN TỤC 2 BÊN
- Mặt nhựa: đoạn chính Box(82, 0.07, 41) tại (−93, 7) (z −13.5..27.5); đoạn
  nối Box(22, 0.05, 45) tại (−41, 5); đoạn phẳng MỚI Box(76, 0.07, 41) tại
  (−168, 7) phủ x −206..−130. Hành lang groundH kéo tới x ≥ −208, z −21..30.
- Hàng nam lùi: sạp tương tác z 22.25 → 26 (mặt tiền 23.9); 7 shophouse nam
  z → 30.5; đèn/hydrangea/vỉa hè nam dời theo (swS z 22.9). Khoảng thoáng
  giữa 2 mặt sạp đoạn vào: 33.75u → 37.5u.
- SẠP LIÊN TỤC: 16 sạp trang trí hàng BẮC (z −15.7, x −188..−61.5) + 16 sạp
  hàng NAM (z 26, x −188..−44) bằng buildDecorStall (thân + mái + cầu hàng +
  biển canvas 12 tên/6 màu, 2/3 có tiểu thương đứng sau quầy) — chừa cổng
  −131, sạp Hoa Sữa, khe sạp chân bậc. Thêm 2 sạp TƯƠNG TÁC: hải sản
  (−100, −15.7, nightOnly) + bánh flan (−95, 26) kèm QUEUES riêng. Khe hàng
  bắc còn lại lấp bằng sạp chân bậc dời ra (điểm 1).
- VERDICT: (a) ĐẠT RÕ — ngay từ spawn thấy trục dài, hàng sạp trái (bắc)
  liên tục sát khung trái, hàng nam + dãy shophouse bên phải; đây là thay
  đổi đọc rõ nhất đợt. (b) ĐẠT MỘT PHẦN — giữa đường (−80) sạp 2 bên liên
  tục và bắt đầu ngay tại điểm đứng, nhưng độ RỘNG mặt đường trong khung
  nhìn dọc trục chưa "kịch tính" như ở (a) (nhìn dọc trục nén bề ngang —
  giới hạn của góc nhìn, không phải thiếu bề rộng: mặt cắt 41u đã dựng).
### ĐIỂM 4 — KÉO DÀI VỀ BÙNG BINH ĐẦU CHỢ + SPAWN Ở ĐÓ
- NEW_RB tại (−196, 2): đĩa cyl R6 h0.5 trên nền dốc entryRampY(−196) = 5.5,
  vành nhựa R9.2, 8 bụi hoa vòng R4.4, cột + biển 'BÙNG BINH ĐẦU CHỢ',
  glowDisc, solid R6.2. Nhỏ hơn bùng binh chính (R6 so với R10.5) như brief.
- MỐC GỢI MỐC (ghi rõ: ảnh trong theme/real-market không thấy rõ mặt tiền
  2 thương hiệu này — dựng GÓC PHỐ GỢI MỐC theo research/21, không khẳng
  định là bản sao): shophouse JOLLIBEE — GÀ RÁN (−183, −20, đỏ 0xc8372d /
  biển #c8102e / chữ vàng) và L'ANGFARM — ĐẶC SẢN ĐÀ LẠT (−183, 31.5, kem /
  xanh thông) ở hai góc phố cạnh bùng binh đầu chợ.
- SPAWN: player (−188, 5.5, 5.6), camera (−199.15, 12.05, 5.6) — khung mở
  đầu nhìn dọc trục DÀI về chợ (render a). Cổng −131 giữ nguyên, thành cổng
  giữa trục.
- Cập nhật nhất quán: groundH dốc (hành lang −208); AW +4 nút idx42–45 Ở
  CUỐI mảng + cạnh [42,39],[43,42],[44,43],[45,44] (xem "phát sinh" dưới);
  tuyến xe ROAD_E/W kéo −188..86, ROUTE_HILL vòng tây mới ôm NEW_RB
  ([−186,12.5],[−190,9.2],[−189,4.5],[−182,6.5]…) + điểm giao đảo −30,6.1;
  parkedRowY đoạn −186..−156; minimap phép chiếu (x+212)/304 + vòng đảo
  chính (−30,−6) + vòng nhỏ NEW_RB + chấm Jollibee đỏ / L'angfarm xanh;
  ambience: phố ăn x −200..43, vùng đường vào x −206..−200, xì xèo theo 2
  hàng sạp mới (|z+15.7|<5 || |z−26|<5); 3 tuyến wanderer mới dọc đoạn kéo
  dài + vòng NEW_RB.
- VERDICT (render a): ĐẠT — khung mở đầu có chiều dài trục thật, không còn
  "cục lủn". LƯU Ý TRUNG THỰC: trong khung (a) bùng binh đầu chợ nằm SAU
  lưng camera và 2 mốc Jollibee/L'angfarm lệch khỏi khung hình — người chơi
  spawn cách tâm NEW_RB ~8.5u, quay lại là thấy; chưa có khung render riêng
  chụp 2 mốc (chỉ kiểm bằng parse + diag).
### ĐIỂM 5 — ĐÁM ĐÔNG HẾT "BỊ LỖI"
- PHÁT HIỆN GỐC (audit_crowd_geo2 + đọc code): lỗi routeY — addWanderer map
  tuyến thành mảng 3 phần tử (pt[2] = undefined với tuyến 2 tọa độ) nên
  routeY() trả undefined thay vì groundH → **55/59 wanderer có y = NaN vĩnh
  viễn** (vòng animate lerp từ NaN không hồi được). Trên trình duyệt thật
  phần lớn người đi bộ VÔ HÌNH — khớp phàn nàn "đám đông bị lỗi, không đọc
  được ai làm gì" (chỉ còn statics đứng cụm). ĐÃ SỬA GỐC: rt giữ nguyên cặp
  [x, z], routeY dùng groundH. Bằng chứng: check_sweep3 mở rộng
  wandererYBad = 0; audit crowd finiteY 62/62.
- Lực tách người trong vòng wanderer: cặp wanderer < 0.55u đẩy ra
  (0.55−d)·0.4; wanderer–static cùng cao độ < 0.5u đẩy (0.5−d)·0.35.
- Browse đọc được: khi vào trạng thái ngắm sạp, wanderer trượt sang điểm
  đứng front + out·1.0 + side·(±1.05) (ra khỏi trục hàng chờ, vẫn quay mặt
  vào sạp) — audit: tối đa 2 người cùng 1 điểm ngắm, không còn vụ 3+ người
  chồng 1 điểm.
- Sửa 5 cặp tĩnh chồng nhau (audit đo): 4 người ngồi bậc STAIR_SITTERS dời
  khỏi điểm front hàng chờ sạp bậc/khỏi nhau (d cũ 0.30–0.56); điểm chat
  [12.8, −4.2] → [12.8, −3.4] (cách người ngồi bàn thềm đông 0.51 → 1.30).
- AUDIT AFTER (scripts/audit_crowd_geo2.mjs, 1800 frame): cặp tĩnh cùng cao
  độ KHÔNG phải hàng chờ thiết kế = **0** (trước: 5 cặp thật); wanderer lọt
  vào statics < 0.45u: 136 → 87 cặp-mẫu (phần còn lại là đi NGANG QUA
  thoáng qua trên tuyến cắt mặt sạp, không đứng cụm); wanderer–wanderer
  < 0.5u: 17 → 14 cặp-mẫu. VERDICT: ĐẠT ở mức audit + render (e) (hàng chờ
  gọn trước mặt sạp, người đi có tuyến) — cảm nhận mật độ giờ đông thật vẫn
  chờ Chung Hy chơi thử.
### ĐIỂM 6 — GIỮ NHÂN VẬT ĐẶC BIỆT ĐÚNG VAI
- Chú Ba coi bói (bậc), ca sĩ (góc hát đồi), chú giữ xe, cô lao công, 7
  tiểu thương hero: bậc/sân/đồi KHÔNG dời trong đợt này → giữ nguyên vị
  trí, check_sweep3 xác nhận lại toàn bộ (áo/tạp dề/mũ/props/singer+đàn).
- Anh xe ôm NEO LẠI: (−120.5, 16.5) → (−181, 17.5) — vỉa hè nam cạnh bùng
  binh đầu chợ, đúng vai "đầu đường mới". SP_EXP trong check_sweep3 đã cập
  nhật; ALL CHECKS PASS.
### PHÁT SINH TRONG ĐỢT (tự bắt + sửa, tính là đợt polish duy nhất của vòng)
- Lỗi của coordinator: 4 nút AW mới bị chèn GIỮA mảng (trước idx40/41) làm
  lệch mọi cạnh tham chiếu 40/41 — audit_ground bắt (cạnh xuyên map), đã
  chuyển xuống cuối mảng + ghi cảnh báo ngay trong comment của mảng.
- audit_ground bắt tiếp: weave cắt làn [−12,−1.9] cũ sau khi profile làn
  dời → đổi weave nam (−12.5,−0.9)/(−14.5,−0.2); 5 tuyến wanderer reroute
  (2292 vòng tây đảo, 2293 đầu trục −52, 2302 cắt dốc 7.9, 2333 điểm lọt
  đĩa đảo → −44, 2334 điểm dọc làn W → 7.8).
- Harness T8 bắt lỗi THẬT trong game: điểm pull-over khoai (−33.2, 4.5) bị
  làn E mới phủ (đỉnh laneZE 5.55 tại x −33, d = 1.03) → dời điểm đỗ vào
  dải giữa làn W (7.15) và mặt sạp (8.9) tại (−29, 8.4), đường tấp vòng
  nam đảo ngoài đĩa (min d 11.0); game + harness đã đồng bộ.
- ROUTE3 "tuyến 3" CHỈ tồn tại như tuyến mẫu trong harness (game không có
  tuyến này) — đuôi mẫu cũ (28, 4.5) lọt bán kính bồn phun mới (27, 5.2):
  đã đồng bộ mô hình harness → (32.5, 5.6)/(30.5, 4.2). Không phải lỗi game.
- Harness T11 chuyển điểm yield node 5 → node 6 (−11.5, 0.2): node 5 không
  còn cắt làn nào sau khi làn dời theo đảo; node 6 là nút chờ giữa 2 làn
  (cách mỗi làn 1.7) — cùng khuôn cảnh V5.5. CROSSINGS thêm node 3 (−40,
  5.6) cắt đỉnh lượn làn W (d 0.24), vùng chậm W x[−50,−12] đã phủ.
- Đồng bộ harness: AW 46 nút/45 cạnh, STALLS 33 (z nam 26 + hải sản/bánh
  flan), ISLAND −30, STATUE −34.2, ISLAND_CARS −6x, FORBIDDEN đài phun
  24.1..29.9, ringPts tâm −30, HILL_LOOP vòng NEW_RB, laneZE/laneZW profile
  mới, slow zone cung đảo −50..−12.
### CỔNG CUỐI
- diag_runtime 900 SẠCH; SEED_SAVE 300 SẠCH; diag trên index-standalone
  300 SẠCH.
- audit_ground_v54: **0 lỗi cứng / 0 nhảy lưới** (60 tuyến, 46 nút AW, 33
  sạp; cảnh báo băng qua làn 25 — bằng đúng bản trước đợt, không tăng).
- Harness giao thông: **26/26 PASS**. check_sweep3 mở rộng: **ALL PASS**
  (kể cả wandererYBad = 0 + specials sau neo).
- Standalone: **10.335.893 byte** (+15.298 so với 10.320.595 trước đợt;
  ngân sách +80.000; dư trần 10.485.760 là 149.867).
- CHƯA kiểm chứng được: FPS thật, cảm nhận đám đông giờ đông trên trình
  duyệt thật, wanderer HIỂN THỊ thật sau sửa routeY (mới chứng minh bằng
  harness/diag — chốt cuối khi Chung Hy chơi thử). KHÔNG upload/push —
  gộp giao cùng NPC-SPECIAL-1 khi Chung Hy cầm máy (1 lượt thẻ).
### CHỜ BLENDER-DEEP (ghi theo steer 09:34 — không vá bằng code ở vòng này)
- Mặt bậc tam cấp trong cảnh render tối thiểu hiện thành dốc trơn (giới
  hạn lưới dựng 2.5u) — cần rà MODEL bậc thật từng nấc + lan can ở vòng
  Blender, đối chiếu ảnh thật.
- Sườn địa hình tây bậc/đảo: khung (d) (−16, 1) cả trước/sau đều bị sườn
  nuốt khung — rà mesh sườn (độ dốc, điểm neo) ở vòng Blender.
- Tỉ lệ đĩa đảo Ø21u và khổ thang 22u so với thật (refactor địa hình lõi
  đã đề xuất, Chung Hy chưa duyệt) — vòng Blender đo lại trước khi quyết.
- Đài phun: tỉ lệ hơi bẹt (giữ theo chốt V5.5) + chuyển động tia nước —
  rà ở BLENDER-DEEP.
- Chuyển động bánh xe các tuyến xe (model vehicle) — rà ở BLENDER-DEEP.

## BLENDER-DEEP-1 (09/11) — RÀ SOÁT + SỬA TẬN GỐC TRÊN BLENDER TOÀN BỘ GLB (lệnh Chung Hy 09:32; KHÔNG upload/push)
### PHƯƠNG PHÁP
- Công cụ mới: scripts/dump_glb_general.mjs (dump mọi GLB: cây node, world bbox,
  tâm bbox theo node, material+màu; cần symlink node_modules -> /tmp/diag/node_modules
  như dump_character), scripts/render_glb_check.py (render Cycles từng GLB,
  góc 34/side/front/top/profile + lọc 1 group), scripts/build_one_glb.py (chạy
  build_models.py chỉ xuất 1 GLB — nguồn sự thật vẫn là build_models.py).
- Baseline toàn bộ 14 GLB đã dump + sao lưu nguyên trạng vào
  glb-backup-blenderdeep-20261109/ (ngoài assets/, không đóng gói).
- Bài học đo: Box3.setFromObject PHÓNG ĐẠI bbox của mesh đã join + xoay
  (Zigzag market báo wsize Y 62.13 trong khi đo theo TỪNG ĐỈNH: 1584/1584 đỉnh
  nằm đúng dải y 4.8..6.8, 0 mặt lệch) — kết luận hình học phải đo theo đỉnh/
  tâm node, không kết luận từ AABB của mesh xoay.
### LỖI THẬT DUY NHẤT + ĐÃ SỬA TẬN GỐC: MẶT CHIẾU NGHỈ THANG ĐỒNG PHẲNG
- Triệu chứng: cả 2 mặt chiếu nghỉ của stairs.glb render Blender ĐEN TUYỀN
  (renders/blender-deep/stairs-before-34.png + -profile.png), web sẽ z-fight.
- Đo gốc: Landing1Top mặt trên = 11.330 TRÙNG KHÍT mặt trên khối Landing1
  = 11.330 (Landing2: 5.670 = 5.670). Pháp tuyến mặt trên hướng lên đúng
  (normal Y = 1.00) — không phải lật normal, là 2 mặt ĐỒNG PHẲNG đè nhau.
- Sửa ở build_models.py/build_stairs: khối Landing1 11.33 -> 11.31,
  Landing2 5.67 -> 5.65 (hạ 0.02); tấm lót GIỮ NGUYÊN — mặt đi vẫn đúng
  stairH (11.33/5.67). Xuất lại bằng build_one_glb.py (stairs).
- Kiểm sau sửa: Landing1 top khối 11.310 vs lót 11.330 (tách 0.02);
  meshes 38 / tris 1032 KHÔNG đổi; stairs.glb 95.104 -> 95.096 byte;
  render stairs-after-34.png: 2 dải đen BIẾN MẤT, mặt chiếu nghỉ sáng liền
  mạch với các chuyến thang. Đúng 1 đợt polish (chỉ stairs cần).
- Xác minh kèm: mặt bậc là BẬC THẬT trong model (30 hộp bậc riêng, cao
  giảm đều 17.00 -> 0.57 + 2 chiếu nghỉ) — "dốc trơn" ở GEOMETRY-2 chỉ là
  giới hạn lưới 2.5u của cảnh render TỐI THIỂU, không phải model game.
  Vách hông thang: chân cắm xuống -1.25 dưới mặt đất (neo chắc), đầu nhô
  +0.25 như gờ chắn; tay vịn xiên liên tục theo sườn (đầu dưới dừng ở bậc
  ~2 của chuyến C — trong dung sai). Mặt bên các bậc đồng phẳng từng cặp
  (chồng 0.06) — phần lớn bị vách hông che trong game, ghi nhận không sửa.
### CHUYỂN ĐỘNG (mục 1 của lệnh)
- Bánh xe vehicle.glb: ĐẠT, không sửa. Đo cả 6 bánh (WheelF/R, WheelFL/FR/
  RL/RR): tâm bbox thế giới TRÙNG KHÍT origin node (vd WheelF wpos =
  wctr = (0, 0.33, 0.78)); geometry đĩa nằm trong mặt YZ, trục dọc X —
  code quay rotation.x là quay đúng tâm trục, không lệch/không đảo.
  Đáy bánh chạm đất 0.005. Helper wheel() trong build đã bake trục X +
  origin tại tâm từ đầu — không có "vá" nào trong code phải gánh.
- Đài phun: KHÔNG nằm trong GLB nào — dựng bằng code (index.html khối
  V5.5). Đã rà code: 6 tia trụ nghiêng phun RA NGOÀI (đầu tia r 0.745 <
  bồn r 2.45) đúng bản sửa SWEEP-1; bồn Ø5.4-5.8/cột/bát giữ tỉ lệ theo
  chốt V5.5 (hơi bẹt — quyết định đã khóa, không đổi ở vòng này).
- Phần nhún/đung đưa khác: không GLB nào có khớp/phần khớp nối ngoài
  bánh xe — NPC nhún/đàn/chổi đều là code gắn prop (NPC-SPECIAL-1), model
  tĩnh là đúng thiết kế.
### TỪNG GLB — ĐÃ KIỂM (đạt, không sửa trừ stairs)
- character.glb: ĐẠT — 11/11 neo, LegL/R pivot y = 0.40, Head đỉnh 1.824,
  4.810 tri/người (khớp baseline HEAD-OPT-1). Chỉ kiểm, giữ khóa
  CROWD-OPT/HEAD-OPT (tỉ lệ + poly không đổi).
- stall.glb: ĐẠT — render front: mái tôn sóng + biển mặt trước (z 0.94,
  hướng người chơi) + 2 đèn lồng + quầy 1.10 + hàng đúng mặt quầy (1.31)
  + giỏ 2 bên + ô StripeA/B neo (2.35, 0.95). Nhóm hàng SkewerTrays/
  CheCups/YaourtTower/BowlStack/CornGrill neo gọn quanh group (đo dump);
  BowlStack có 2 chi tiết baked lệch trái theo thiết kế quầy (hũ/chồng
  đặt sẵn trên mặt quầy) — không phải lỗi neo.
- market.glb: ĐẠT — dump: Floor0 + Floor1/Floor2 khoét giếng phía đông
  (Floor1E/E001/E002 chừa miệng giếng ~5x5.6), 2 tầng + sân thượng +
  skylight; biển CHỢ ĐÀ LẠT 2 mặt đọc đúng chiều (render back + 34);
  tháp thang máy kính ElevGlass; zigzag 2 mặt đã chứng minh theo đỉnh.
- roundabout.glb: ĐẠT — render 34: họa tiết 8 quạt hoa/cỏ + vành hoa cầu
  đọc rõ, cụm tượng 3 người (robe thuôn, tay giơ) + thông đá đỉnh, tổng
  cao cụm 9.60 đúng thiết kế V5.1, bệ 3 bậc chamfer, ghế sector vành đảo.
  Đo lại cho quyết định refactor (CHƯA duyệt, không đổi): đĩa Base mặt
  trên Ø21 (r 10.5), chân Ø22 (r 11.0), CurbRing Ø22.3.
- bridge.glb + pier.glb: ĐẠT — deck origin tâm (game bám groundH theo
  deck — đã chốt V4.4), parapet + mái kính vòm + đèn nóc thẳng hàng;
  pier: gốc asset ở chân (2 mesh con offset trong group), game scale từ
  group root nên neo đúng; cap dày theo tỉ lệ scale là thiết kế hiện
  hành. Ghi chú dung sai: đầu RoofPost có thể chạm mép kính ~0.1 — không
  thấy ở render profile, không sửa.
- theater.glb: ĐẠT — render 34: tháp đồng hồ (mặt + kim + vòng Gold),
  oculus, mái ngói, khối rạp cân đối.
- cafe.glb / shop.glb / hotels.glb / lamp.glb / pine.glb: ĐẠT — render 34
  từng GLB: cafe (biển lớn + mái hiên + bàn ghế góc), shop (ban công +
  lan can + mái hiên), hotels (4 group, biển nóc 4 kiểu, biến thể mái
  MetalDark là THIẾT KẾ — không phải lỗi đen mặt), lamp (tay torus vòng
  R0.55, Drop treo đúng mép vòng x 0.95 — thiết kế đèn vòng), pine (4
  tầng tán đều). Toàn bộ 14 GLB: 0 mesh thiếu normals.
- Màu/vật liệu: bảng MATS trong build khớp palette khóa (nền ấm bão hòa
  thấp, hàng hóa bão hòa cao Goods/Skewer/Flower, đèn LanternGlow
  #ff9a3d-họ, SignLetters đỏ) + research/22 (terracotta, kem) — không
  vật liệu nào lệch tông cần sửa.
- Sườn địa hình tây bậc/đảo (treo từ GEOMETRY-2): là ĐỊA HÌNH CODE,
  không có GLB địa hình; phần model liên quan (vách hông stairs.glb) đã
  kiểm ở trên. Khổ thang đo lại: rộng 22 / cao 17 / 3 chuyến — giữ
  nguyên chờ Chung Hy duyệt refactor lõi (không tự đổi).
### CỔNG CUỐI (bản sau sửa stairs)
- diag_runtime index.html 900 SẠCH; SEED_SAVE 300 SẠCH; đóng gói lại +
  diag trực tiếp trên index-standalone.html 300 SẠCH.
- audit_ground_v54: 0 lỗi cứng / 0 nhảy lưới (60 tuyến, 46 nút AW, 33 sạp).
- Harness giao thông: 26/26 PASS. check_sweep3 mở rộng: ALL CHECKS PASS
  (wandererYBad = 0, specials + tủ đồ nguyên vẹn).
- Standalone: 10.335.881 byte (trước vòng 10.335.893; -12 byte; dư trần
  10.485.760 là 149.879). GLB raw total 7.418.168 byte.
- CHƯA kiểm chứng được (như cũ): FPS thật + grade ngày + nghe thật trên
  web, cảm nhận đông đúc giờ đông — chờ Chung Hy chơi thử. Render full
  cảnh game vẫn phụ thuộc RAM máy (vòng này kiểm ở cấp GLB bằng render
  riêng lẻ renders/blender-deep/*-before/after). KHÔNG upload/push.

## BLENDER-DEEP-2 (09/11) — BỔ SUNG THẬT THEO CHÊ "CHƯA ĐỦ, CÒN THIẾU" (KHÔNG upload/push)
### PLAN (ghi TRƯỚC khi làm — verdict điền sau, theo render tầm mắt trước/sau)
- Công cụ kiểm: scripts/render_bd2.py (bản sao render_geo2.py, port groundH MỚI +
  parse z hàng decor từ chính index.html + khối Jollibee/L'angfarm + đài phun theo
  số đo code). Khung: a spawn, b giữa trục (-80), b2 trục kéo dài (-140), j cận
  Jollibee, l cận L'angfarm, f cận đài phun, d2 từ tâm đảo nhìn bậc. Xuất
  renders/bd2-before-*.png / bd2-after-*.png.
- MỤC 1 ĐƯỜNG VÀO RỘNG DỌC TOÀN TRỤC: hàng BẮC (sạp tương tác dauhu/banhmi/
  hutieu/traicay/chao/haisan + 16 sạp decor) z -15.7 -> -19.7; hàng NAM (banhtrang/
  banhuot/suatuoi/banhflan + 16 decor) z 26 -> 30. Khoảng trống 2 mặt sạp
  37.5u -> 45.5u (+21%) ĐỀU khắp trục -196..-30 (trước GEOMETRY-2 chỉ rộng ở
  khung spawn). Nhựa 41 -> 49u (z -17.5..31.5) cả 3 đoạn seg/seg2/seg3; vỉa hè
  bắc -12.5 -> -17.0, nam 22.9 -> 26.4; đèn đường theo vỉa mới; thềm bắc/nam nới
  theo; groundH sửa 4 quy tắc (thềm bắc tới -21.5, vỉa bắc -18.4..-15.6 x -208..-59,
  hành lang -25..34 + dải +0.11 mới, thềm nam tới 33.5, nền nhà z>32). Dãy nhà
  phố lùi theo: nam 30.5 -> 35.5 (7 nhà), bắc -24..-25 -> -28.5 (7 nhà) — lưng
  sạp không đè nhà. Đoạn sát mặt tiền (hàng sạp z=11) GIỮ NGUYÊN: đó là dãy quay
  mặt vào sân chợ, lưng chạm cột nhà lồng — giới hạn cứng đã ghi nhận, không
  thuộc trục đường vào. Đồng bộ: harness STALLS, ambience (dải xì xèo + vùng
  phố ăn), render_bd2.
- MỤC 2 JOLLIBEE + L'ANGFARM DỰNG THẬT (thay 2 shophouse gợi mốc): builder
  brandShop() bằng code geometry + biển canvas (KHÔNG GLB mới -> 0 byte asset).
  Jollibee (-183,-20, mặt hướng đường): tường đỏ #c8102e, biển 'JOLLIBEE' trắng
  trên nền đỏ + biển phụ 'GÀ RÁN GIÒN • KHOAI TÂY CHIÊN', mái hiên sọc đỏ/trắng,
  dải vàng #ffc72c, cửa kính + cửa ra vào, bảng menu đứng, 2 bàn ngoài trời.
  L'angfarm (-183,31.5): tường kem, biển "L'ANGFARM" nền xanh lá #2e5b2e + phụ
  'ĐẶC SẢN ĐÀ LẠT • TRÀ • MỨT • HOA KHÔ', mái hiên xanh, kệ gỗ trưng lọ mứt đủ
  màu + giỏ hoa trước cửa, cửa kính. Đối chiếu ảnh thật: theme/real-market
  KHÔNG có ảnh 2 mặt tiền này (đã kiểm ở GEOMETRY-2) -> dựng theo nhận diện
  thương hiệu phổ biến, ghi rõ là không phải bản sao ảnh thật.
- MỤC 3 ĐỆM ĐẢO <-> BẬC + SÂN DƯỚI BẬC: đảo GIỮ -30 (GEOMETRY-2 vừa dời đồng
  bộ làn xe/AW/harness; dời nữa phá harness + làn). Tăng tách bạch thị giác:
  hàng 5 chậu cẩm tú cầu x -13 (z -14..10) làm dải xanh phân cách vành đường
  đảo <-> sân bậc; vạch zebra qua đường trên vành đảo tại x -13.5; tấm sân đổi
  tông sáng hơn (0x978a78 -> 0xa79a84) + dải viền sẫm ở mép tây sân; biển nhỏ
  'BẬC TAM CẤP ->' ở góc sân tây. Sân chân bậc giữ nguyên phần mở rộng GEOMETRY-2.
- MỤC 4 ĐÀI PHUN BỚT BẸT: cột giữa 1.5 -> 2.3 (bát chính lên y 2.62, miệng
  r 0.95), thêm bát tầng 2 (y 3.15) + chóp cầu; tia nghiêng dài 1.15 -> 1.5 ở
  y 2.95 (đầu tia r ~0.84 < bồn 2.45 — vẫn rơi trong bồn); thêm tia đứng giữa
  cao 1.2. Tổng cao ~2.8 -> ~4.2. Bồn/đế giữ nguyên (FORBIDDEN harness không đổi).
- MỤC 5 DANH TÍNH ĐÀ LẠT DỌC ĐƯỜNG VÀO: biển tên đường 'Đ. NGUYỄN THỊ MINH
  KHAI' tại (-160,-17.6) + (-70,27.2) (bổ sung biển Tăng Bạt Hổ sẵn có ở cổng);
  thông pine() dọc sườn bắc (-150/-120/-90/-70, z ~-22) + 2 cây phía nam
  (-150,34.5)/(-105,35); chậu cẩm tú cầu ở 4 góc vỉa đoạn kéo dài. Không đụng
  sửa đám đông GEOMETRY-2 (routeY + lực tách giữ nguyên).
- RÀNG BUỘC: standalone <= 10.485.760 (hiện 10.335.881, dư 149.879 — vòng này
  KHÔNG thêm GLB, chỉ code text, dự kiến +<15KB); save chohb3d-v1 không đụng;
  cổng bắt buộc: diag 900 + SEED_SAVE 300 + standalone 300 + audit_ground +
  traffic 26/26 + check_sweep3 ALL PASS.
### BỔ SUNG MỤC 12–17 (lệnh 14:11–14:12 ngày 09/11 — ghi plan trước khi làm, cùng vòng)
- MỤC 12 HÀNG HÓA THEO HÀNG THẬT (research/24): thêm 11 sạp tương tác (dau2/dau3/dau4
  dâu tây, mut, hong, tra2, hoa2, luuniem2, dosi, len3, dacsanlon) — STALL_DEFS
  33 -> 44 (số 33 là ĐO THỰC từ code, các brief cũ ghi 31 đã lệch). 6 sạp đường
  vào THAY ĐÚNG VỊ TRÍ 6 sạp decor (gỡ khỏi DECOR_N_XS/DECOR_S_XS) nên không
  chồng hình; mỗi sạp có hàng mô hình riêng (tháp hộp dâu, dây hồng treo, giỏ
  hoa) + biển canvas + menu mua bán thật.
- MỤC 13 KHU PHẢI BẬC: dãy aokhoac/aolen nới thêm len3 (40;27,5) + cột 2 sạp
  đối diện luuniem2/dosi (45;17,5/22,5) tạo lối đi chợ; TIỆM LỚN "ĐẶC SẢN –
  LƯU NIỆM" vào được bên trong: mặt tiền x=49 (kính + cửa 2u + biển lớn + biển
  GIÁ RẺ), sâu tới 59,5, z 14,2–25,8; trong tiệm 3 dãy kệ + đảo kệ giữa, quầy
  tính tiền = sạp dacsanlon mua bán như sạp thường, chủ tiệm SPECIAL_VENDOR
  (tạp dề đỏ đô + mũ đỏ); tiệm thuộc nhóm đặc sản: mở tới 22:00 (bọc hallTick).
- MỤC 14 QUẦN ÁO NHÌN RÕ: biển lớn "QUẦN ÁO – ĐỒ LEN" (7,2u) bắc qua dãy ở
  x=36,85 hướng về bậc/đài phun + 2 giá treo NGOÀI mặt sạp + 2 ma-nơ-canh mặc
  len; sửa tên sạp aokhoac. Kiểm bằng render g (từ chân bậc) + h (từ đài phun).
- MỤC 15–17 BA CHẾ ĐỘ CHƠI (Couple/Gia đình/Theo đoàn): màn chọn 4 thẻ lúc mở
  game (chỉ lần đầu, state.modeSeen) + nút 🎭 Chế độ trên HUD để đổi bất cứ lúc
  nào; save thêm mode/modeProg/modeTitles (migration mặc định solo, KHÔNG phá
  save cũ — SEED_SAVE đạt); bạn đồng hành dùng makePerson (character.glb đã tối
  ưu) đi theo bằng tick riêng móc vào tickWater; đoàn xe là sự kiện riêng làn
  z=14, KHÔNG vào hệ traffic (harness vẫn 26/26); tủ đồ +3 món mở khóa bằng
  chế độ (AO-DOI / NON-DOAN / AO-DOAN, WARDROBE_DEFS 60 -> 63, check_sweep3 đã
  cập nhật census tương ứng).
- MỤC 18 (lệnh 14:54 — học NGUYÊN TẮC từ reel tham khảo, không sao chép
  pixel/asset): 18A biển dọc có nghề + cửa cuốn mặt tiền phố 2 trạng thái theo
  giờ + bốt giữ xe + dây điện nối dài; 18B tương phản đêm (khu đóng tối + cuốn
  xám, điểm mở có vũng sáng) + phố phụ thưa người sau 22:00; 18C loa chợ ở cổng
  (falloff như mục 8 + thông báo chữ) + bước chân theo 4 mặt đường + côn trùng
  đêm khuya. Kiểm bằng test_bd2 mục 18 + diag.
- Sửa kèm phát hiện nhờ test: toast() bỏ vòng while->if khi dọn toast cũ
  (while phụ thuộc remove() gỡ node khỏi children — ở môi trường DOM mà
  remove() không gỡ thật sẽ lặp vô hạn; bản if bỏ tối đa 1 toast cũ/lần thêm,
  hành vi trên trình duyệt thật không đổi vì toast tự hết hạn sau 3,2s).

### VERDICT (điền sau khi làm + soi render)
- MỤC 1 ĐƯỜNG VÀO RỘNG: **ĐẠT** — khoảng trống 2 mặt sạp 37,5u -> 45,5u đều
  dọc trục (đo từ tọa độ sạp trong code: hàng bắc -19,7 / hàng nam 30); nhựa
  49u; render bd2-after-b.png + bd2-after-b2.png (đối bd2-before-b/b2): trục
  thoáng đều từ -196 tới mặt tiền, không còn đoạn thắt. Hàng z=11 sát mặt tiền
  giữ nguyên (giới hạn cứng lưng chạm cột nhà lồng — không thuộc trục đường vào).
- MỤC 2 JOLLIBEE + L'ANGFARM: **ĐẠT** — render bd2-after-j.png / bd2-after-l.png:
  khối + màu nhận diện đúng (đỏ + dải biển trắng cho Jollibee; kem + dải biển
  xanh lá cho L'angfarm) trong cảnh mini; bản game thật có biển canvas đọc được
  chữ JOLLIBEE / L'ANGFARM + mascot ong + kệ hàng (cảnh mini không vẽ chữ
  canvas — ghi rõ giới hạn). Theo nhận diện thương hiệu phổ biến — ảnh mặt tiền
  RIÊNG của 2 chi nhánh Đà Lạt chưa đủ tư liệu (research/23).
- MỤC 3 ĐỆM ĐẢO ↔ BẬC: **ĐẠT MỘT PHẦN** — đảo GIỮ -30 (dời nữa phá làn
  xe/AW/harness 26/26); thay bằng tách bạch thị giác: vạch zebra + 4 chậu cẩm
  tú cầu + biển "BẬC TAM CẤP →" + sân dưới bậc đổi tông sáng hơn; render
  bd2-after-d2.png. Cảm giác khoảng cách thật: chốt khi chơi thử web.
- MỤC 4 ĐÀI PHUN BỚT BẸT: **ĐẠT** — cột 1,5 -> 2,3, thêm bát tầng 2 + chóp,
  tổng cao ~2,8 -> ~4,2 (đo từ code); tia nghiêng dài 1,5 đặt r 0,5 ở y 2,95:
  đầu tia r ~0,92 < bồn 2,45 nên nước vẫn rơi trong bồn; render bd2-after-f.png
  đối bd2-before-f.png: cột + bát cao hơn rõ, hết bẹt (góc máy cảnh mini hẹp,
  đài phun nằm ở góc tường deck — ghi rõ).
- MỤC 5 DANH TÍNH ĐÀ LẠT: **ĐẠT** — 3 biển tên đường (Nguyễn Thị Minh Khai ×2,
  Tăng Bạt Hổ), 6 cây thông + 4 chậu cẩm tú cầu dọc đường vào, đèn đường theo
  vỉa mới; render bd2-after-a/b/b2.
- MỤC 6 RESEARCH/23: **ĐẠT** — research/23-kien-truc-tung-cong-trinh.md: 13 mục
  (12 công trình + chợ đêm Âm Phủ), mỗi mục đủ tư liệu/đặc điểm khóa/đối chiếu
  model/đã sửa/chưa đủ tư liệu; ghi thẳng "chưa đủ tư liệu" ở 9 chỗ (mặt tiền
  riêng Jollibee + L'angfarm Đà Lạt, rạp Hòa Bình, đài phun thật, phố Tăng Bạt
  Hổ toàn tuyến, từng khách sạn, từng quán cà phê, biển Hoa Sữa, một phần nhà
  lồng + vòng xoay).
- MỤC 7 NƯỚC CHẢY: **ĐẠT VỀ CƠ CHẾ — cảm giác chốt khi chơi thử web** —
  test_bd2 đo thay đổi theo frame trên index + standalone giữa tickWater(0) và
  tickWater(1,3): mặt bồn Δy = 0,0161, Δopacity = 0,0091; tia phun Δscale.y =
  0,0321; vòng gợn Δscale = 0,707 — nước chuyển động thật trong runtime.
  Render Blender tĩnh không thấy chuyển động.
- MỤC 8 ÂM THANH KHOẢNG CÁCH: **ĐẠT VỀ SỐ ĐO — nghe thật chốt khi chơi thử
  web** — test_bd2 đo ambSpatial() ở 3 khoảng cách: ban nhạc góc hát gain
  1,00 -> 0,40 -> 0,01 và lowpass 9.000Hz -> 2.674Hz -> 510Hz khi đi xa dần
  (khoảng cách đo 2,8u -> 44,6u -> 70,7u); gần rõ ấm, xa nhỏ + lờ mờ nhưng còn
  nghe nhờ sàn gain 0,06 ở stageBus; đài phun tương tự (gain 1/2.300Hz ở gần
  -> 0/700Hz ở 127u). Nguồn điểm stage/fountain/food/hall đều có gain+lowpass
  riêng cập nhật trong tick.
- MỤC 9 COI BÓI 3 KIỆU: **ĐẠT** — test_bd2: mỗi kiểu chạy 40 lượt cho 40 kết
  quả phân biệt (yêu cầu ≥ ~10); bài chứa tên lá thuộc CARD_DECK, mặt chứa
  luận Trán, tay chứa Sinh Đạo; drawFortune trừ đúng 20 Xu, fortuneCount +1;
  UI chọn kiểu + nghi thức 0,9s bỏ qua được; giữ giá 20 Xu + questFlags.fortune
  + state.fortuneCount như cũ. Coi bói ĐÔI của Couple dùng chung hệ này (việc
  'boi' tích khi fortuneCount tăng trong chế độ Couple).
- MỤC 10 CHU KỲ NGÀY/ĐÊM: **ĐẠT** — test_bd2 mô phỏng 4 mốc: 12:00 nhà lồng
  mở, cửa cuốn ẩn; 18:45 cửa cuốn lưng chừng (y = 1,91, giữa 2,50 -> 1,32);
  20:00 quầy thường đóng + tiểu thương rời + tắt tương tác (nearestStall bỏ
  qua s.closed, openMenu chặn), đặc sản + tiệm lớn còn mở, sạp ngoài trời
  không đóng; 23:00 đặc sản + tiệm lớn đóng nốt. Chuyển cảnh mượt theo p trong
  [18:30 -> 19:00] + toast "Nhà lồng đóng cửa — chợ đêm Âm Phủ mở". Nguồn giờ
  thật ghi ở research/23 (nhà lồng + chợ đêm). Người chơi spawn 19:00 không bị
  khóa tiến trình: mọi mua bán thiết yếu có sạp ngoài trời tương ứng.
- MỤC 11 SƯƠNG ĐÀ LẠT: **ĐẠT VỀ CƠ CHẾ — cảm giác chốt khi chơi thử web** —
  fog sẵn của scene được animate theo đồng hồ game: fogHourBonus cộng dày
  5–9h (đỉnh ~7h) và sau 21:00, ban ngày tan; đèn có quầng ấm qua halo sẵn có.
  Mật độ cộng tối đa ~0,016 (không che gameplay ở khoảng chơi thường).
- MỤC 12 HÀNG HÓA: **ĐẠT** — 44 sạp tương tác (audit_ground đếm 44, lỗi cứng
  0); dâu tây đủ 4 quầy ở mặt tiền (dau4 12;11 + dau cũ) + đường vào (dau2
  bắc, dau3 nam); mứt/sấy, hồng treo gió, trà atiso/cà phê, hoa tươi, lưu niệm
  ngoài trời, đồ si đều có quầy riêng + biển đọc được + mua bán được. Đối
  chiếu + phần còn thiếu ghi thẳng ở research/24 (rượu cần/thịt rừng chủ đích
  không làm; vài món ngách chưa có).
- MỤC 13 KHU PHẢI BẬC + TIỆM LỚN: **ĐẠT** — mật độ khu phải tăng rõ (5 sạp
  quần áo/lưu niệm/đồ si + tiệm lớn); tiệm vào được qua cửa 2u (collider chừa
  đúng cửa), mua bán tại quầy tính tiền trong tiệm, đóng 22:00 đã kiểm ở mục
  10; render bd2-after-i.png (cận mặt tiền: dải biển xanh, kính, cửa giữa, 2
  sạp bên) + bd2-after-k.png (xiên trên cao: cả khu phải + đài phun + bậc).
  Nội thất tiệm trong render mini chỉ là khối đơn giản hóa — bản game thật có
  kệ + hàng đầy đủ bằng code (đã qua diag + test vị trí).
- MỤC 14 QUẦN ÁO NHÌN RÕ: **ĐẠT VỀ BỐ CỤC + NỘI DUNG, render mini đạt một
  phần** — biển QUẦN ÁO – ĐỒ LEN 7,2u đặt ở x=36,85 (điểm tây nhất, gần sân
  đài phun nhất), giá treo ngoài + ma-nơ-canh ở x≈37, dãy sạp quay mặt -x về
  sân đài phun: tất cả có thật trong code và qua diag/test. Render tầm mắt từ
  bậc (bd2-after-g) và từ đài phun (bd2-after-h) trong CẢNH MINI bị khối deck/
  nhà lồng đơn giản hóa chắn tầm (đã thử 3 vị trí camera) — cảnh mini không
  dựng được góc nhìn này trung thực; bằng chứng hình ảnh đạt được là
  bd2-after-i (mặt tiền tiệm + 2 sạp bên) và bd2-after-k (xiên trên cao thấy
  cả dãy + tiệm + đài phun). Chữ biển là canvas trong game thật, cảnh mini
  chỉ vẽ khối màu. Đọc rõ thật ở tầm mắt: chốt khi Chung Hy chơi thử web
  (camera người chơi thật là góc ba tư trên cao, khác camera tĩnh của mini).
- MỤC 15 CỬA VÀO CHẾ ĐỘ: **ĐẠT** — 4 thẻ chọn lúc mở game lần đầu + nút 🎭;
  đổi chế độ dọn bạn đồng hành cũ, giữ Xu/túi/hộ chiếu (test_bd2 kiểm save).
- MỤC 16A COUPLE: **ĐẠT VỀ CƠ CHẾ — cảm giác chốt khi chơi thử web** —
  test_bd2: spawn đúng 1 người thương đi CẠNH (offset ngang 1,15u), sau khi
  người chơi dịch 30u + 6s mô phỏng thì lệch còn 1,16u; mua dâu tích việc ngay;
  đủ 6 việc (ảnh bùng binh/coi bói đôi/nghe hát 5s/Hoa Sữa/áo đôi) qua cùng hệ
  móc mua hàng + vùng đứng đã kiểm từng móc. Thưởng 150 Xu + danh hiệu gắn
  Hộ chiếu (passSub) + áo đôi vào tủ đồ + người thương đổi áo cùng màu.
- MỤC 16B GIA ĐÌNH: **ĐẠT VỀ CƠ CHẾ — cảm giác chốt khi chơi thử web** —
  spawn 4 thành viên (Bà đi chậm maxSp 5,6; Bé 0,7 scale + bóng bay, thỉnh
  thoảng chạy trước theo chu kỳ 9s); sau dịch chuyển 40u + 7s, thành viên
  chậm nhất lệch 2,75u; wish của Bà tích khi mua đúng "Trà atiso túi lọc";
  panel có ✓ từng người + thanh Ấm no; thưởng 200 Xu + danh hiệu.
- MỤC 16C THEO ĐOÀN: **ĐẠT VỀ CƠ CHẾ — cảm giác chốt khi chơi thử web** —
  đoàn xe 2 xe chạy làn riêng vào điểm tập kết rồi đoàn xuống xe (phase
  drive -> walk trong test); 10 đoàn viên áo/nón đoàn + hướng dẫn viên cầm cờ
  = đoàn 12 người cùng người chơi; đứng vòng điểm tập kết 5s -> check-in
  (cp 0 -> 1 đã kiểm); quá xa > 30u quá 10s có nhắc "Về đoàn nào!" + cờ nhấp
  nháy; đủ 6 điểm thưởng 250 Xu + NON-DOAN/AO-DOAN vào tủ đồ. Traffic harness
  vẫn 26/26 sau khi thêm đoàn xe.
- MỤC 17 HIỂN THỊ: **ĐẠT** — huy hiệu chế độ cạnh nút 🎭 trên HUD; panel việc
  cập nhật tức thì khi tích việc (renderModePanel gọi ngay ở modeTaskDone) +
  thanh % animation CSS; tiến độ lưu theo từng chế độ (test save/load đạt);
  hoàn thành có modal tổng kết + pháo tim (Couple).
- MỤC 18A ĐƯỜNG XÁ CỤ THỂ (học từ reel): **ĐẠT** — 6 biển DỌC có nghề đọc
  được dọc phố (NHÀ THUỐC, HỚT TÓC, GIỮ XE ở dãy bắc; TẠP HÓA, SỬA XE, QUÁN
  NƯỚC ở dãy nam) + bốt giữ xe tại (-118;24,5) có biển "GIỮ XE — 5K/LƯỢT" +
  đèn chốt (colonialLamp, tự sáng về đêm) + 14 cửa cuốn mặt tiền phố có 2
  trạng thái theo giờ (test_bd2: ban ngày 0/14 hạ, ban đêm 11/14 hạ — chừa
  3 mặt tiền mở kiểu tạp hóa khuya) + dây điện nối dài: 3 cột mới (-160/-132/
  -104) + 3 nhịp dây võng về cột cũ -72 (trước đây dây chỉ có đoạn -72..-44).
  Vỉa hè liền mạch + sạp tràn lề đã có từ mục 1/GEOMETRY-2.
- MỤC 18B KHÔNG KHÍ ĐÊM: **ĐẠT MỘT PHẦN — cảm giác chốt khi chơi thử web** —
  tương phản sáng/tối dựng bằng: cửa cuốn xám + đèn quầy tắt ở khu đóng (mục
  10/18A) đối lập vũng sáng ấm ở điểm mở (halo sạp chợ đêm, uplight đài phun,
  đèn bốt giữ xe, nội thất tiệm lớn); sau 22:00 phố PHỤ thưa người thêm (bọc
  updateCrowdDensity: NPC tĩnh + lang thang rank < 0,35 ở vùng phụ z>34 /
  z<-26 / x<-150 bị ẩn; trục chợ đêm giữ nguyên mật độ). Cảnh render mini
  không có chế độ đèn đêm trung thực nên không đính render đêm — kiểm bằng
  trạng thái code + test; tương phản thật chốt khi chơi thử web.
- MỤC 18C ÂM THANH (loa + bước chân): **ĐẠT VỀ SỐ ĐO — nghe thật chốt khi
  chơi thử web** — LOA CHỢ ở cổng chào (-131): test_bd2 đo loaGainAt ở 3
  khoảng cách: 0,89 tại cổng -> 0,60 ở 71u -> 0,04 ở ~197u (sàn nhỏ để "vang
  khắp phố"); bandpass 2.563Hz -> 537Hz (xa thì lờ mờ). Thông báo 5 mẫu kiểu
  chợ hiện chữ khi đủ gần; "giọng loa" mô phỏng bằng sawtooth đổi cao độ qua
  bandpass + delay vang — KHÔNG phải giọng người thật, ghi rõ. BƯỚC CHÂN đổi
  mẫu theo mặt đường (test: surfaceAt cho 4 mặt phân biệt nhựa/gạch/thang/
  sàn nhà lồng; tần số bước 240/950/520/680Hz, gõ mỗi ~2,1u đường đi). Đêm
  khuya có côn trùng rất nhỏ (gain 0,012) + gió sẵn có của ambience.
  Ghi nguyên tắc: học THIẾT KẾ của reel (đường cụ thể, tương phản đêm, loa
  phường + bước chân), không sao chép asset hay phong cách pixel.
- CỔNG KIỂM CHỨNG TOÀN VÒNG: diag_runtime 900 frame SẠCH; SEED_SAVE 300 SẠCH;
  diag standalone 300 SẠCH; test_bd2 ALL PASS trên cả index.html lẫn
  index-standalone.html; test_ambience_sc1 TEST-AMB-OK; audit_ground_v54 lỗi
  cứng 0 (44 sạp); v52_traffic_harness 26/26; check_sweep3 ALL PASS.
- DUNG LƯỢNG: index.html 516.379 byte; standalone 10.407.915 byte — dưới trần
  10.485.760, còn dư 77.845 byte. Toàn vòng thêm 0 GLB mới (chỉ code + canvas).
- ĐIỂM MÙ CÒN LẠI (chỉ chốt khi Chung Hy chơi thử trên web): FPS thật với
  +14 NPC chế độ, grade ngày trên web, nghe thật (âm khoảng cách + loa +
  bước chân), cảm giác nước chảy + sương + tương phản đêm, cảm giác vui/đẹp
  của 3 chế độ chơi, đọc rõ biển quần áo ở tầm mắt thật.
- KHÔNG upload / KHÔNG push GitHub — chờ lệnh "gửi đi" ở chat chính.

## REALISM-1 (09/11) — TĂNG ĐỘ CHÂN THẬT THỊ GIÁC (lệnh Chung Hy sau khi xem render BD2: "cũng tạm tạm thôi chứ chưa nhìn chân thật lắm"; KHÔNG upload/push)
### PLAN (ghi TRƯỚC khi làm — verdict điền sau, theo đối chiếu cùng góc bằng mắt)
- PHẠM VI KHÓA: chỉ tăng chân thật ở VẬT LIỆU / ÁNH SÁNG / MẬT ĐỘ CHI TIẾT /
  TỈ LỆ trong phong cách chibi diorama đã khóa (đầu to, camera ~45°, UI
  nâu/vàng, ảnh chuẩn theme/CHOT-phong-cach-cho-dem.png). KHÔNG đổi bán
  thực/photoreal, không đụng 18 mục BD2 (gameplay/chu kỳ/âm thanh giữ nguyên).
- PHƯƠNG PHÁP ĐỐI CHIẾU: harness scripts/render_real1.py (bản sao
  render_bd2.py — parse index.html hiện tại nên bố cục luôn mới) + 4 camera
  khớp ảnh thật; ghép PIL trái = ảnh thật, phải = render thành
  renders/real1-cmp-{before,after}-<goc>.png. GIỚI HẠN GHI RÕ: cảnh mini
  Blender dùng vật liệu phẳng mô phỏng, KHÔNG vẽ texture canvas/chữ của web
  → đối chiếu chấm được BỐ CỤC / TỈ LỆ / MẬT ĐỘ / SILHOUETTE; phần texture
  canvas + ánh sáng web kiểm bằng rà code + test đo (số material được gán
  map, thông số renderer) và ghi "chốt khi chơi thử web" như các vòng trước.
- 4 GÓC ĐỐI CHIẾU:
  R1 MẶT TIỀN + BÙNG BINH (ảnh thật 01, ngày): cam (-38, 2.0, -14) ->
  đích (0, 5, 12), lens 24 (khớp research/17).
  R2 ĐƯỜNG VÀO NTMK (ảnh thật 43 đêm từ trên cao + 06): cam trên cao
  (-100, groundH+12, 5.6) -> (-30, 1.5, 5): 2 hàng sạp + nhà phố + dây điện.
  R3 BẬC TAM CẤP NHÌN XUỐNG (ảnh thật 10 đêm + 40): cam (0, 18.8, -27)
  -> (-30, 1.5, -6): thang + đảo + phông khách sạn đối diện.
  R4 CHỢ ĐÊM TẦM MẮT (ảnh thật 43/34): cam (-47, groundH+1.7, 6)
  -> (-38, 1.2, -13) (khung e của BD2): mặt sạp, bạt, đèn, rác đường phố.
- RÀ CODE TRƯỚC KHI SOI (nghi phạm đã khoanh, chờ ảnh đối chiếu xác nhận):
  (a) mặt đất PHẲNG không texture: nhựa 3 đoạn seg/seg2/seg3 + road plane +
  vành đảo (MeshStandardMaterial màu trơn 0x453f3a/0x4a4038), vỉa hè hộp
  0x84796a trơn, plaza 0x978a78 trơn, sườn dốc 0x5f8547 mảng xanh trơn lớn,
  nóc đồi 0x9e9078 trơn. (b) renderer đã có PCFSoft + ACES + exposure ngày
  0.88/đêm 1.22; sun shadow 2048 trên span ±95 (tâm 0) → đoạn cổng/spawn
  x<-95 NGOÀI vùng bóng; cửa sổ shophouse có winMats emissive nhưng cần
  kiểm mức ngẫu nhiên từng nhà về đêm. (c) shophouse chưa có máy lạnh/bồn
  nước/ăng-ten/ban công; dây điện mới chạy dọc cột, chưa có nhịp NGANG qua
  đường như ảnh 43; thiếu chồng ghế nhựa + thùng xốp/sọt ở lưng sạp; xe máy
  đậu cụm sát lề còn ít. (d) thông pine() đã xoay/scale theo hash nhưng
  chung 1 vật liệu tán; sườn dốc thiếu bụi/chậu ở chân. (e) đám đông: da 4
  tông + áo sọc canvas đã có cho TIỂU THƯƠNG (npcStripeShirt), khách đi
  đường vẫn áo trơn; tóc nằm trong GLB (kiểm tên material trước khi hứa).
- THỨ TỰ LÀM: B1 render before 4 góc + ghép đối chiếu + DANH SÁCH LỆCH
  cụ thể (điền dưới plan này). B2 patch scripts/patch_real1.py sửa theo
  lệch theo các đòn (a)-(e) của brief, ưu tiên canvas texture runtime
  (0 byte asset) + geometry tái dùng/gộp. B3 render after đúng 4 góc +
  ghép mới + verdict TỪNG GÓC thẳng thắn (đạt / đạt một phần + còn lệch gì).
- RÀNG BUỘC CỨNG: standalone <= 10.485.760 (hiện 10.407.915, CHỈ DƯ
  77.845 byte) — mọi thêm vào tính byte, cấm asset nhị phân mới, vượt thì
  tối ưu bù trong vòng; save chohb3d-v1 không phá; cổng bắt buộc: diag 900
  + SEED_SAVE 300 + standalone 300 + audit_ground + traffic 26/26 +
  check_sweep3 ALL PASS + test_bd2 ALL PASS; Blender --threads 2, 1 render
  nặng tại một thời điểm (RAM ~7,9GB, available ~3,2GB lúc mở vòng).
### DANH SÁCH LỆCH (BƯỚC 1 — soi renders/real1-cmp-before-r1..r4.png, toàn văn ở renders/real1-deviations.md; đã phân loại LỆCH THẬT của bản web vs GIẢ ẢNH của harness mini)
- L1 MẶT ĐẤT PHẲNG ĐƠN TÔNG [THẬT — đòn (a)]: nhựa/vỉa/sân/sườn là mảng
  màu trơn chiếm 45–50% khung ở r2/r4 (đo PIL: 4 tông phẳng trội chiếm
  63–75% pixel render, thật 54–61%); web đúng vậy: rampMat/road/plaza/
  vỉa hè/sườn KHÔNG texture (rà code). Ảnh thật: nhựa xám đen có vá + vệt
  bánh xe + bóng cây loang; vỉa lát gạch có khe; sân lát đá từng tấm.
- L2 SƯỜN DỐC FACET XANH TRƠN [THẬT một phần — đòn (a)+(d)]: mặt tam giác
  phẳng 8–10% khung ở r1/r3/r4; hình học sườn là lõi địa hình (không sửa
  hình), nhưng web sườn cũng là plane xanh trơn 0x5f8547 → cần nhiễu màu
  + bụi/chậu chân sườn phá mảng.
- L3 RÁC ĐƯỜNG PHỐ VẮNG [THẬT — đòn (c)]: 4 render đếm 0 dây ngang, 0
  máy lạnh/bồn nước/ăng-ten, 0 chồng ghế/thùng xốp, xe đậu chỉ 2 chiếc ở
  đảo; rà code web khớp: dây mới chạy DỌC phố (z=-8.6), shophouse không
  phụ kiện, chân sạp chỉ có giỏ dâu/chậu. Ảnh thật góc nào cũng ≥3 nhóm:
  dây ≥10 sợi ngang khung (43), máy lạnh + ban công (43), giỏ nhựa đỏ +
  đòn gánh (33), xe tải/bán tải/xe máy ép sát chân chợ (01).
- L4 ĐÊM THIẾU "SỐNG" Ở CỬA SỔ [THẬT — đòn (b)]: mini là ngày phẳng
  (giả ảnh), nhưng rà code web: applyDayNight set MỌI winMats
  emissiveIntensity = 1.9 ĐỀU NHAU → cửa sổ nhà phố sáng đồng loạt giả;
  hotelWinMats đã có hệ số đêm riêng từng ô (mẫu đúng để theo).
- L5 NGƯỜI THIẾU BIẾN THIÊN TÓC + ÁO [THẬT một phần — đòn (e)]: capsule
  pastel là giả ảnh harness (web là người GLB đủ mặt/tóc/nón); phần thật:
  material tóc 'HairDark' MỘT màu cho toàn bộ NPC, áo sọc canvas mới có
  ở tiểu thương, khách đi đường áo trơn; ảnh thật áo caro/sọc + mũ len
  nhiều màu là lớp đọc rõ nhất ở r3.
- L6 KHUNG R1 SAI ĐIỂM ĐỨNG [GIẢ ẢNH harness]: cam (-38,2,-14) nằm
  TRONG sườn tây của cảnh mini nên facade/tượng không lọt khung; ở web
  điểm tương ứng cũng là sườn — SỬA CAMERA cho lượt after: đứng trên đĩa
  đảo (-36, 2.8, -2) -> (2, 6.5, 13); before-r1 sẽ render lại cùng lượt
  after bằng camera mới và ghi rõ (harness không vẽ texture/clutter của
  patch nên before vẫn đúng cho bố cục). R4 cũng chỉnh: cam (-70,
  groundH+1.7, 7) -> (-35, 2, 4) dọc trục thay vì đâm vào sườn.
- KHÔNG PHẢI LỆCH WEB (ghi để khỏi sửa nhầm): bậc thang đọc như dốc ở
  r3 = lưới groundH của mini (web là 30 hộp bậc thật, BLENDER-DEEP-1 đã
  đo); facade hộp trơn ở mini = không nạp GLB (web market.glb đủ zigzag/
  lam/pano/chữ — research/23); mật độ người trong khung của mini thấp
  hơn web (mini đặt 198 người theo phân bố riêng).
### VERDICT (điền ở BƯỚC 3 — CHỐT TẠI V7-IMPROVE-1, 09/11 đêm, render lại bằng code HIỆN TẠI sau V6)
- Render nguồn: renders/real1-v7-r1..r4.png (camera đã sửa theo L6) + ghép đối chiếu renders/v7-cmp-r1..r4.png (trái ảnh thật, phải render). Các render after cũ (trước V6) hết giá trị, không dùng nữa.
- **VERDICT TỔNG: ĐẠT MỘT PHẦN.** Phần vật liệu/ánh sáng của vòng này (texture canvas mặt đất, cửa sổ đêm ngẫu nhiên theo ô, rác đường phố, biến thiên tóc/áo) đã kiểm chứng bằng test_real1 PASS + số đo tại checkpoint (texMeshes 27, facadeTex 208, cửa sổ đêm 7 mức/tắt 0,238, máy lạnh 9, bồn nước/ăng-ten 7, rác chân sạp 13+11, xe đậu 9, tóc 5 màu, áo map 12/40) và GIỮ NGUYÊN qua bản V6. Nhưng harness mini KHÔNG vẽ texture canvas/GLB/chữ nên "độ chân thật" cốt lõi không chấm trọn bằng mắt qua harness được — điểm chốt cuối vẫn là chơi thử web (điểm mù đã ghi từ đầu vòng).
- R1 MẶT TIỀN + BÙNG BINH: **CHƯA ĐỐI CHIẾU ĐƯỢC** — render từ đĩa đảo (-36,2.8,-2) bị vách/khối mini che gần hết khung, mặt tiền + tượng không lọt khung. Không kết luận được cho web; cần kiểm lại điểm đứng này khi chơi thử web.
- R2 ĐƯỜNG VÀO: **ĐẠT MỘT PHẦN** — bố cục trục đúng (hàng sạp dọc trục, thang lên đồi giữa khung, nhà lồng + dãy shophouse hai phía). Lệch thật còn thấy: sườn đồi facet mảng xanh lớn giữa khung (L2 còn nguyên — hình học lõi địa hình, ngoài phạm vi sửa vòng này); mặt đất foreground trong mini là mảng xám phẳng (harness không vẽ texture web, không kết luận cho web).
- R3 BẬC TAM CẤP NHÌN XUỐNG: **CHƯA ĐẠT VỀ KHUNG ĐỐI CHIẾU** — camera r3 cũ không còn khớp bố cục sau khi đảo dời về −30 (GEOMETRY-2): khung ôm phần lớn mặt sườn trống, đảo/bùng binh không vào khung như ảnh thật 10. Cần định lại camera r3 ở vòng soi sau; không dùng khung này kết luận chất lượng web.
- R4 TẦM MẮT: **ĐẠT MỘT PHẦN** — vị trí tương đối đảo + đài phun đúng; nhưng khung nhìn về đảo nhiều hơn dọc trục sạp nên KHÔNG soi được mặt sạp/bạt sọc tầm mắt. Thay đổi bạt sọc 3 màu của V7 vì thế chỉ mới kiểm chứng bằng code + diag + test, chưa có ảnh đối chiếu.
- Lệch thật còn lại (xếp hạng): (1) sườn đồi facet mảng lớn L2 — cần đòn hình học/vật liệu riêng, ngoài trần việc vòng này; (2) khung đối chiếu r1/r3 cần làm lại bộ camera harness; (3) biển dọc hộp đèn đường vào + hồi ấm 100% Hoa Sữa (xem bảng rà lệch V7-IMPROVE-1).

#### BỔ SUNG V7-2 (10/11/2026 — verdict cũ ở trên GIỮ NGUYÊN, chỉ bổ sung kết quả mới)
- Camera harness đã định lại trong scripts/render_real1.py: r1 cũ (-36,2.8,-2) nằm ngay trong bệ tượng trên đĩa đảo nên tường mini chắn hết khung → r1 mới đứng ở mặt đường tây-nam đảo (-52, groundH+2.8, -8) ngắm (-10,6,13); r3 cũ (0,18.8,-27) ở đỉnh đồi nhìn lệch xuống sườn tây → r3 mới đứng trên chiếu nghỉ 1 của thang (0, stairH(-19)+2.2, -19) ngắm thẳng tâm đảo (-30,1,2) (lượt đầu đặt ở chuyến trên vẫn cho đảo nhỏ/mờ nên hạ xuống chiếu nghỉ).
- R1: **ĐẠT VỀ KHUNG ĐỐI CHIẾU** (từ "chưa đối chiếu được" lên) — render renders/real1-v7-2-r1.png + ghép renders/v7-2-cmp-r1.png (cạnh ảnh thật 01): đĩa đảo + tượng giữa khung tiền cảnh, khối nhà lồng làm nền, đường làm foreground — bố cục tương ứng ảnh 01 đọc rõ. Khác biệt ghi nhận thành thật: tượng trong game nằm lệch phía bắc đảo nên trong khung ở giữa thay vì lệch trái như ảnh thật (vị trí tượng đã khóa từ GEOMETRY-2, không phải lỗi khung); nhà lồng trong mini là khối trơn (harness không vẽ GLB/mặt tiền chi tiết — giới hạn harness đã biết).
- R3: **ĐẠT MỘT PHẦN** (từ "chưa đạt về khung" lên) — render renders/real1-v7-2-r3.png + ghép renders/v7-2-cmp-r3.png (cạnh ảnh thật 10): mặt thang + chiếu nghỉ + người ngồi trên bậc chiếm tiền cảnh đúng ý ảnh 10, phố vào + dãy shophouse bắc + cổng ở hậu cảnh. Đảo nằm trong tầm nhìn giữa khung nhưng ở mini đọc yếu (đĩa cùng tông mặt đường, tượng thu nhỏ còn quả cầu trắng) — mức đọc của đảo/tượng ở bản web thật chỉ chốt khi chơi thử.
- Lệch (1) sườn facet L2: đã xử lý ở V7-2 bằng phủ vật liệu + cây/bụi (xem mục V7-IMPROVE-2, Việc 4) — mảng phẳng trơn ở sườn kè đá nay có texture cỏ canvas + 9 thông + 8 cụm bụi che; facet hình học gốc vẫn là 3 mặt phẳng (không sửa lưới), mức "hết facet" cuối cùng vẫn chấm khi chơi thử web.

#### ĐÍNH CHÍNH V8 (10/11/2026 — theo chấm của Chung Hy 01:27: "nhìn không ra luôn, có giống đâu")
- **RÚT LẠI verdict R1 của BỔ SUNG V7-2 ở trên** ("R1: ĐẠT VỀ KHUNG ĐỐI CHIẾU", "bố cục tương ứng ảnh 01 đọc rõ"): ảnh renders/v7-2-cmp-r1.png dựng bằng harness mini — nhà lồng là KHỐI HỘP TRƠN, tượng là TRỤ + QUẢ CẦU, không texture/chữ — nên KHÔNG có giá trị nghiệm thu độ giống; verdict đó chấm quá tay. (Văn bản verdict cũ giữ nguyên tại chỗ theo quy định; đoạn này là đính chính chính thức.)
- **THAY BẰNG verdict từ RENDER MODEL THẬT**: script mới scripts/render_facade_real.py nạp market.glb + roundabout.glb + stairs.glb + pine.glb đúng vị trí/quay/scale mà index.html dùng (market (0,0,20); roundabout (-30,0,-6) — tượng thế giới (-34.2,-2.8) khớp điểm ngắm spotlight trong code; stairs (0,0,-16); pine (-22.5,-16.8) scale 1.15), camera three (-62, 4.5, -20) ngắm (4, 8, 12), Cycles 32 mẫu 900×600. Ảnh đơn: renders/v8-facade-real.png; ảnh ghép CÓ NHÃN: renders/v8-cmp-r1.png (TRÁI = RENDER MODEL THẬT / PHẢI = ẢNH THẬT 01).
- **VERDICT MỚI R1 (chấm bằng mắt trên render model thật): ĐẠT MỘT PHẦN Ở MỨC MODEL — CHƯA GIỐNG Ở BỐ CỤC.** Giống: chữ CHỢ ĐÀ LẠT đỏ đọc rõ; đủ lam + 2 dải kính + dải zigzag + dải quảng cáo + hàng quán tầng trệt + thông bút chì trên mái, đúng thứ tự tầng như ảnh thật; tượng là TƯỢNG THẬT (2 nhân vật + tán thông trên bệ bậc, mesh 2.342 verts) chứ không phải trụ bi của harness; đảo Ø22 có vòng hoa + ghế đá. Khác: (1) tượng rơi GIỮA khung thay vì tiền cảnh TRÁI như ảnh 01 — hệ quả hình học thật của game (tượng ở góc tây, sát phía chợ của đảo; mặt tiền hướng −z; từ mọi điểm đứng phía nam/tây-nam nhìn mặt tiền, tượng đều rơi giữa→phải khung; muốn khớp ảnh phải DỜI TƯỢNG — vị trí đã khóa từ GEOMETRY-2, không tự sửa trong việc này); (2) mặt tiền game PHẲNG, ảnh thật CONG vòng cung + góc bo tròn; (3) khối thang stairs.glb choán góc trái khung — ảnh thật là sườn đồi + cây; (4) màu render nhạt/rửa hơn ảnh thật (Cycles + trời phẳng; bản web còn clamp bão hòa + texture bẩn facade — chưa tái tạo trong render này); (5) render chỉ nạp 4 GLB quanh mặt tiền: thiếu biển MARCHÉ trên mái, dãy khách sạn phía phải, người/xe và chi tiết dựng bằng code (đài phun, biển hiệu, NPC).

### ⏸️ CHECKPOINT GITHUB 18:2x 09/11/2026 — TẠM DỪNG THEO LỆNH MAIN CHAT (Chung Hy chốt đẩy Chợ lên GitHub ĐẦY ĐỦ)
- Trạng thái file tại checkpoint: NHẤT QUÁN. Bước 2 (patch_real1.py, 14/14 thay thế) đã áp xong + đã đóng gói standalone; index.html/index-standalone.html không đổi từ 11:05. Bước 3 đang dở ở khâu render (worker render đã bị đóng theo lệnh dừng): đã có renders/real1-after-r1/r2/r3.png (11:16–11:18, kiểm PIL verify OK, không file nào cụt) + real1-beforefix-r1/r4.png; CHƯA có after-r4, CHƯA ghép real1-cmp-after-*.png, CHƯA có renders/real1-after-measure.md, VERDICT trên chưa điền. Chạy tiếp từ đúng điểm này khi có lệnh "ĐÃ ĐẨY XONG, CHẠY TIẾP".
- Cổng chạy lại TƯƠI tại trạng thái checkpoint (log /tmp/checkpoint_gates.log):
  - diag_runtime 900: PASS (INIT OK, 900 frame sạch, exit 0)
  - SEED_SAVE 300 (save cũ chohb3d-v1): PASS (exit 0)
  - standalone diag 300 (SRC_FILE=index-standalone.html): PASS (exit 0)
  - audit_ground_v54: exit 1 — lỗi cứng 0, nhảy lưới 54 quanh vách đồi bắc (TỒN TẠI TỪ TRƯỚC vòng REALISM-1, đã tự kiểm chứng patch_real1.py chỉ gọi groundH chứ không sửa định nghĩa groundH; tiêu chí khóa mọi vòng là lỗi cứng = 0 → giữ nguyên trạng, không sửa lan tại checkpoint)
  - traffic v52_traffic_harness: 26/26 PASS
  - check_sweep3: ALL CHECKS PASS
  - test_bd2: ALL CHECKS PASS (18 mục BD2 không vỡ)
  - test_real1: PASS (texMeshes 27, facadeTex 208, cửa sổ đêm 7 mức sáng/tỉ lệ tắt 0,238, máy lạnh 9 + bồn nước/ăng-ten 7, rác chân sạp 13+11, xe máy đậu 9, tóc 5 màu, áo có map 12/40)
- Số byte standalone cuối tại checkpoint: **10.419.383 byte** (trần 10.485.760 — dư 66.377 byte).
- Sau ghi chú này: NGỪNG MỌI THAO TÁC GHI FILE cho tới khi tuyến chính báo "ĐÃ ĐẨY XONG, CHẠY TIẾP". Khi REALISM-1 hoàn thành (render after đủ 4 góc + ghép đối chiếu + VERDICT) sẽ đẩy bổ sung ngay trong cùng phiên.

## V7-IMPROVE-1 (09/11 đêm) — TIẾP NỐI BẢN V6 ANTIGRAVITY (head 0dc7859) + CẢI THIỆN THEO PLAN V6 & KIẾN TRÚC THẬT
- Bối cảnh: Chung Hy giao lại dự án, lệnh cải thiện theo KE_HOACH_MUSE_AI_V6.md + research/25, 23, 24 + 44 ảnh thật; hạn chót 00:12 (chốt cứng ngừng sửa 00:05). Backup trước sửa: index.html.bak-v7-start-20261109. KHÔNG đẩy GitHub, KHÔNG upload link (chờ lệnh riêng).
- Ràng buộc byte: standalone đầu vòng 10.446.592 (dư 39.168 so trần 10.485.760) → chỉ sửa code/texture canvas thủ tục, cấm asset nhị phân mới.

### A. QUÉT TOÀN BỘ CỔNG TRÊN BẢN V6 ĐỒNG BỘ (ưu tiên cao nhất — Chung Hy báo bản V6 Antigravity "có lỗi", chưa rõ lỗi gì)
Chạy trên code hiện tại (V6 sync + các sửa V7 ở mục B, đều qua cùng bộ cổng):
- diag_runtime 900: **SẠCH** (INIT OK, 900 frame không ngoại lệ)
- SEED_SAVE 300 (save cũ chohb3d-v1): **SẠCH**
- standalone diag 300 (SRC_FILE=index-standalone.html, đóng gói lại): **SẠCH**
- audit_ground_v54: **lỗi cứng 0, nhảy lưới 0** (sạch hơn cả checkpoint REALISM-1: nhảy lưới 54 → 0)
- traffic v52_traffic_harness: **26/26 PASS**
- check_sweep3: **ALL CHECKS PASS**
- test_real1: **PASS**
- test_bd2: lượt đầu **ĐỎ 1 lỗi** — "goods: STALL_DEFS phải = 44, thấy 45". Rà soát: 45 sạp có id PHÂN BIỆT đủ (không trùng id, audit đếm 45 sạp lỗi cứng 0) → đây là sạp thứ 45 do phía V6 Antigravity thêm, test còn giữ chuẩn đếm của vòng BD2 (44) nên báo sai. Đã sửa chuẩn trong scripts/test_bd2.mjs 44 → 45 kèm chú thích nguồn gốc → chạy lại **ALL CHECKS PASS**. Đây là lỗi CHUẨN TEST CŨ, không phải lỗi game.
- **KẾT LUẬN QUÉT CỔNG: không tái hiện được lỗi runtime nào trên bản head 0dc7859** — đủ 8 cổng xanh. Lỗi Chung Hy gặp có thể nằm ở bản local Antigravity chưa đẩy, hoặc lỗi chỉ lộ khi chơi thật trên web (điểm mù cố hữu của harness) — cần anh mô tả cụ thể lỗi đã gặp để bắt đúng.

### B. BẢNG RÀ LỆCH PLAN V6 (mục 1–2 + 5 chặng mục 3) — bằng chứng grep/đọc code trên bản V6
| Hạng mục plan | Mức | Bằng chứng |
|---|---|---|
| ① Dây bóng vàng 2 bên đường vào + dây ngang qua đường | CÓ | stringLights mỗi 22u (khối V6 chặng ① ~dòng 4563) + lanternString ngang (−62/−48) |
| ① Dây điện ngang chằng chịt | CÓ | khối REALISM-1 ~dòng 7856, bó dây mỗi ~14m dọc phố chợ đêm |
| ① Bạt sọc **3 màu** (xanh dương/đỏ/trắng ngà) giăng chéo chồng lấn | **YẾU → ĐÃ SỬA (mục C)** | stripeMat cũ chỉ 2 màu/bạt (xanh–trắng, lá–trắng, đỏ–trắng ngà); sạp code-built đường vào (5 sạp ăn phía nam) + xe đẩy Đà Lạt dùng mái màu PHẲNG (roofCol/pCol) |
| ① Vệt ướt phản chiếu đèn trên nhựa | CÓ nhưng mờ | wetGlows (glowDisc additive) bật đêm opacity 0.4 → **đã tăng 0.55 (mục C)**; harness mini không vẽ được lớp này, chốt khi chơi thử web |
| ① Biển dọc hộp đèn (tiệm vàng, hiệu thuốc) 2 bên đường vào | **THIẾU** | grep "TIỆM VÀNG"/"HIỆU THUỐC"/"hộp đèn" = 0; vBanner dọc chỉ có ở rạp (RẠPHÒA/PHIMHAY). Chưa sửa vòng này: cần đặt theo mặt tiền shophouse + render kiểm vị trí, tránh biển nổi giữa đường — để vòng sau |
| ① Chữ đỏ "CHỢ ĐÀ LẠT" mặt tiền phát sáng đêm | CÓ | signGlowMats chữ 3D (~dòng 670), emissiveIntensity đêm 2.6 |
| ① Sạp áo len treo cao thành 2 bức tường màu | CÓ | STALL_DEFS len1/len2/len3/aokhoac/aolen + dãy sạp 2 bên trục |
| ① Xe máy dựng sát mép sạp | CÓ MỘT PHẦN | REALISM-1 đã thêm 9 xe máy đậu; ảnh thật dày hơn — tăng số lượng cần rà va chạm, để vòng sau |
| ① Lòng đường 14–16m (số thật) | KHÁC CÓ CHỦ ĐÍCH | Game giữ đường vào rộng 45,5u theo lệnh nới đường của Chung Hy ở các vòng trước — không thu hẹp lại |
| ① Nhiệt độ giảm dần, giữ ấm | CÓ | warmth drain theo thời gian (~5900–5931), áo ấm giảm drain |
| ② Biển cầu thang + Góc Hong Kong + lan can/chiếu nghỉ có quán | CÓ | biển "BẬC THANG CHỢ ĐÀ LẠT" (825), mốc check-in GÓC HONG KONG (4617), chiếu nghỉ chú Ba + sạp (BD2), quest leo thang di sản (6378) |
| ③ Rạp 3 Tháng 4 + quảng trường + Cà phê Tùng + góc hát | CÓ | biển "RẠP HÒA BÌNH — Rạp 3 Tháng 4, xây 1937" (1072), 2 vBanner rạp, "CÀFÉ TÙNG · 06 Khu Hòa Bình — từ 1956" (1091), ca sĩ góc hát (NPC-SPECIAL-1), dấu hộ chiếu Đồi Hòa Bình |
| ④ Hoa Sữa: menu nành đường / nành bò / bánh tiêu chấm sữa | **CÓ ĐỦ** | menu hoasua: "Sữa đậu nành nóng (nành đường)", "Nành bò", "Nành phụng", "Nành xanh", "Bánh tiêu — Chấm sữa nóng là hết sảy", su kem + sừng trâu đồng giá 6k. LƯU Ý: grep chữ thường "nành bò" = 0 chỉ vì tên món viết hoa chữ đầu — đọc trực tiếp menu mới đúng |
| ④ Hoa Sữa: không mái, nồi siêu to bốc hơi, tủ kính bánh, ghế vỉa hè | CÓ | roof:'none' + Awning bị ẩn (2409), nồi phụ + hơi (3312), tủ kính 6 ô (2284) |
| ④ Ăn/uống Hoa Sữa hồi **100%** độ ấm | YẾU (gameplay) | cơ chế chung: món nóng/buff warm hồi +40 warmth (4943), chưa phải 100% như plan. Không sửa vòng này (ưu tiên thị giác theo lệnh deadline; chỉnh riêng cần thêm cờ cho món Hoa Sữa + test cân bằng) |
| ⑤ Hồng Trà ki-ốt 30–32 + signature + trà sữa hạnh nhân chôm chôm | CÓ ĐỦ | stall hongtra menu 3 món đủ cả "Trà sữa hạnh nhân chôm chôm"; dãy ki-ốt 28–34 + biển (4619); bình ủ inox + khay topping (2305) |
| Mục 2: kit sạp mô-đun theo loại (treo len / nướng / nồi nước / ki-ốt) | CÓ | HERO_STALLS + props theo loại sạp trong placeStall; poly budget không đo lại vòng này |

### C. ĐÃ SỬA (1 chặng gộp, hiệu quả thị giác cao / byte thấp)
1. **Bạt sọc 3 màu đúng plan**: stripeMat() đổi bộ màu 2 màu → 3 màu luân phiên (xanh dương #2e5fa3 / đỏ #c0392b / trắng ngà #f2ead8), 3 biến thể lệch pha để sạp kề nhau không trùng hệt. Áp cho MỌI sạp GLB (đường cũ qua placeStall).
2. **Sạp code-built đường vào có bạt sọc**: 5 sạp ăn phía nam (southFoodStalls) + xe đẩy Đà Lạt (makeDalatPushCart) trước đây mái màu phẳng → gán vật liệu sọc theo biến thể.
   - Sự cố khi sửa: lượt diag đầu bắt **TDZ** "Cannot access '_stripeMats' before initialization" — code build sớm (~1392/1510) chạy TRƯỚC dòng khai báo const _stripeMats (~1980). Đã sửa dứt điểm bằng helper v7StripeMat() khai báo cạnh wetGlows (~696, trước mọi code build) dùng riêng cho 2 điểm build sớm; stripeMat gốc giữ nguyên cho placeStall. Diag chạy lại sạch (xem mục A).
3. **Vệt ướt đêm rõ hơn**: opacity wetGlows ban đêm 0.4 → 0.55 (applyDayNight).
- Số đo sau chặng: diag 900 SẠCH; package OK; **standalone cuối 10.447.688 byte** (đầu vòng 10.446.592 → +1.096 byte; dư 38.072 byte so trần). Toàn bộ cổng phụ xanh (mục A).

### D. CHỐT REALISM-1
- Đã render lại đủ 4 góc bằng code hiện tại: renders/real1-v7-r1..r4.png (Blender --threads 2, Cycles 24 mẫu, 640×480; camera theo ghi chú L6) + ghép đối chiếu renders/v7-cmp-r1..r4.png, đã soi bằng mắt từng ảnh.
- VERDICT đã điền vào mục REALISM-1 ở trên: **ĐẠT MỘT PHẦN** — R2/R4 đạt một phần (bố cục đúng, sườn facet L2 còn), R1 chưa đối chiếu được (khung bị vách mini che), R3 chưa đạt về khung đối chiếu (camera cũ lệch sau khi đảo dời −30). Không sửa thêm trong vòng này: các lệch còn lại hoặc là giới hạn harness, hoặc là hình học lõi địa hình (ngoài phạm vi + đã khóa), hoặc cần chơi thử web để chốt.
- Trạng thái cuối vòng: file nhất quán, backup index.html.bak-v7-start-20261109 giữ nguyên; standalone 10.447.688 byte; toàn bộ 8 cổng xanh (mục A). KHÔNG đẩy GitHub, KHÔNG upload link chơi thử.

## V7-IMPROVE-2 (10/11/2026) — 4 VIỆC TREO TỪ V7-IMPROVE-1 (lệnh Chung Hy "cứ làm tiếp đi"; KHÔNG đẩy GitHub, KHÔNG upload link)
- Baseline đầu vòng (kiểm chứng lại tươi): diag 900 SẠCH, standalone 10.447.688 byte (dư 38.072 so trần 10.485.760). Backup: index.html.bak-v7-2-start-20261110. Kỷ luật: từng việc một, sau mỗi việc diag 900 + package + đo byte; cuối vòng chạy lại toàn bộ 8 cổng.

### VIỆC 1 — BIỂN DỌC HỘP ĐÈN ĐƯỜNG VÀO: ✅ ĐẠT
- Thêm helper `vSign(x, rowZ, dir, text, bg, fg)` ngay sau dãy shophouse trục đường vào (~dòng 1520): chữ canvas xếp dọc 256×448, hộp đèn (0,24 × 3,0 × 1,7) nhô khỏi mặt tiền (tâm z = rowZ + dir×2,8 + dir×0,86), đáy biển y = groundH + 2,8 (qua mái hiên ~2,68, không đâm hiên), 2 thanh đỡ. Material mặt chữ để ở `window.__vSignMats` (bare block không giữ được const — cùng tiền lệ window.__REAL1); applyDayNight chỉnh: đêm emissiveIntensity 1,7 (phát sáng ấm), ngày 0,1 (tắt/xám).
- 6 biển: bắc (−151,7 KHÁCH SẠN), (−121,7 CÀ PHÊ), (−107,7 TIỆM VÀNG); nam (−128,3 HIỆU THUỐC), (−156,3 TRÀ SỮA), (−170,3 NHÀ NGHỈ). Đổi biển ngang cho khớp ngành: shophouse(−110) → "TIỆM VÀNG KIM HƯƠNG", shophouse(−126) → "HIỆU THUỐC TÂM AN".
- Sự cố khi làm: bản đầu khai const trong bare block → applyDayNight ReferenceError, diag bắt được; sửa dứt điểm bằng window.__vSignMats trước khi sang việc kế.
- **Lỗi CÓ SẴN từ V6, phát hiện + sửa trong vòng này** (không phải do V7-2): vòng hoa cẩm tú cầu dọc kè đá index `HYDRA_COLS[(fi + Math.floor(fx)) % len]` với fx âm → màu undefined → warning THREE + vài bông trắng. Đã sửa modulo âm an toàn `((x % len) + len) % len`. Cách bắt: gắn in stack vào setValues trong bản three chép ở /tmp/diag2, trỏ đúng vòng hoa. Bài học kèm: chạy diag với GAME_ROOT thiếu assets/ sẽ chết sớm và báo "0 warning" GIẢ — luôn kiểm chứng tại chỗ.
- Kiểm vị trí bằng render đêm (harness mở rộng VSIGN_NIGHT + parse vSign): renders/real1-v7-2-vsign.png (toàn cảnh từ cổng nhìn vào), vsign2 (cận dãy bắc), vsign3 (cận dãy nam trên sườn) — soi bằng mắt: đủ 6/6 biển bám mặt tiền, nhô ra phố, phát sáng đêm; không biển nào lơ lửng/giữa đường. Giới hạn: harness không vẽ chữ canvas nên hướng/độ đọc của chữ chỉ chốt khi chơi thử web.
- Số đo sau việc: diag 900 SẠCH; standalone 10.450.939 byte (dư 34.821).

### VIỆC 2 — HOA SỮA HỒI ẤM 100%: ✅ ĐẠT
- Cơ chế cũ: mọi món nóng/buff 'warm' hồi +40 warmth ở eatItem. Đã sửa đúng plan V6 chặng ④, 3 điểm chạm: (1) `finishCooking` gắn cờ `fw: stall.id === 'hoasua'` vào món khi mua tại Hoa Sữa (điểm push giỏ duy nhất của luồng mua; push "Kẹo dâu được tặng" không gắn cờ → falsy, an toàn); (2) `eatItem`: món có fw → warmth = 100; món nóng khác giữ +40 như cũ; (3) toast ăn/uống thêm đuôi "— ấm hẳn người (Hoa Sữa hồi 100% độ ấm)" khi fw.
- **Lựa chọn cân bằng (ghi rõ theo lệnh)**: CHỈ Hoa Sữa là điểm hồi đầy 100% — đúng vai trò "điểm giữ ấm" của plan; hệ lạnh toàn cục giữ nguyên (drain theo thời gian + nearHeat +13/s không đổi) để không phá cân bằng. Menu Hoa Sữa mọi món đều buff 'warm' nên mọi món tại đây đều hồi đầy. Save cũ chohb3d-v1: món trong giỏ không có field fw → falsy → hành vi cũ, không phá save.
- Số đo sau việc: diag 900 SẠCH + SEED_SAVE 300 SẠCH; standalone 10.451.377 byte (dư 34.383).

### VIỆC 3 — CAMERA HARNESS r1/r3 + VERDICT BỔ SUNG: ✅ ĐẠT (r1 đạt khung, r3 đạt một phần)
- Định lại trong scripts/render_real1.py: r1 (-52, groundH+2.8, -8) → (-10,6,13); r3 (0, stairH(-19)+2.2, -19) → (-30,1,2). Lý do + kết quả chi tiết đã APPEND vào mục REALISM-1 phần "BỔ SUNG V7-2" (verdict cũ giữ nguyên không xóa).
- Render: renders/real1-v7-2-r1.png, real1-v7-2-r3.png; ghép đối chiếu renders/v7-2-cmp-r1.png (cạnh ảnh thật 01), v7-2-cmp-r3.png (cạnh ảnh thật 10) — đã soi từng ảnh. R1: bố cục tương ứng ảnh 01 đọc rõ → ĐẠT khung. R3: thang + chiếu nghỉ + người ngồi tiền cảnh đúng ý ảnh 10, đảo trong tầm nhìn nhưng đọc yếu ở mini → ĐẠT MỘT PHẦN.

- **GHI CHÚ ĐÍNH CHÍNH (V8, 10/11/2026)**: ảnh ghép v7-2-cmp-r1.png / v7-2-cmp-r3.png của việc này dựng bằng harness mini (khối hộp thay model, trụ + bi thay tượng, không texture/chữ) — CHỈ có giá trị kiểm bố cục khối (điểm đứng, hướng ngắm, vật nào lọt khung), KHÔNG dùng để nghiệm thu độ giống. Verdict hình cho r1 đã bị rút lại và thay bằng render model thật — xem mục REALISM-1, phần "ĐÍNH CHÍNH V8".

### VIỆC 4 — SƯỜN FACET L2: ✅ ĐẠT (phương án phủ an toàn, KHÔNG sửa lưới groundH)
- Phương án đã chọn + lý do: (a) phủ texture canvas cỏ lên 3 mặt phẳng sườn + (b) trồng cây/bụi che facet. KHÔNG sửa lưới groundH vì audit_ground đang 0 lỗi cứng/0 nhảy lưới rất nhạy, và mặt phẳng sườn mới là bề mặt NHÌN THẤY (game không có mesh địa hình chạy theo groundH — đã grep kiểm chứng: groundH chỉ dùng đặt vật/nhân vật).
- (a) Texture: thêm `0x4a6b36: TEX_GRASS` vào bảng _r1Map của pass REALISM-1 (0x4a6b36 chỉ dùng đúng cho 3 mặt sườn). **Đo đối chứng**: test_real1 texMeshes 22 (không entry) → 25 (có entry) = +3 đúng 3 mặt sườn. (Số 27 trong verdict REALISM-1 là đo tại checkpoint TRƯỚC đồng bộ V6; nền hiện tại của bản V6 là 22 — không phải hồi quy.)
- (b) Cây/bụi: đặt theo PHƯƠNG TRÌNH MẶT PHẲNG THỊ GIÁC (không theo groundH — groundH vùng sườn kè đá cao hơn mặt phẳng tới ~3,9 là tồn tại cũ; đặt theo groundH cây sẽ lơ lửng trước mặt sườn nhìn từ đường): sườn kè đá (x −52..−14,5) 6 thông + 6 cụm bụi; sườn đông sau thang (x 20,5..70) 3 thông + 2 cụm bụi. pine() lấy y theo groundH nên bọc helper ép lại y theo mặt phẳng (−0,2 chân). Sườn seg1 sau dãy nhà nam bỏ qua phủ cây (không nhìn thấy từ đường vào), vẫn nhận texture.
- Kiểm chứng: harness mở rộng parse sPine/sBush, render renders/real1-v7-2-slope.png — 2 thông phía trên sườn (nơi lưới groundH của harness không che) bám đúng mặt phẳng, không lơ lửng/chìm; các cây thấp bị lưới mặt đất CỦA HARNESS che là tạo tác harness (harness vẽ lưới theo groundH, game thật không có lưới đó — bề mặt game chính là mặt phẳng đã phủ). Mức "hết facet" cảm quan cuối cùng vẫn chốt khi Chung Hy chơi thử web.
- Số đo sau việc: diag 900 SẠCH; test_real1 PASS; standalone 10.453.464 byte (dư 32.296).

### CỔNG CUỐI VÒNG (chạy lại toàn bộ 8 cổng trên bản cuối) — ✅ 8/8 XANH
- diag_runtime 900: **SẠCH** (INIT OK, 900 frame không ngoại lệ)
- SEED_SAVE 300 (save cũ chohb3d-v1): **SẠCH**
- standalone diag 300 (SRC_FILE=index-standalone.html): **SẠCH**
- audit_ground_v54: **lỗi cứng 0, nhảy lưới 0** (không chạm lưới nên giữ nguyên trạng thái sạch)
- traffic v52_traffic_harness: **26/26 PASS**
- check_sweep3: **ALL CHECKS PASS**
- test_bd2: **ALL CHECKS PASS** (chuẩn 45 sạp)
- test_real1: **PASS** (texMeshes 25 — gồm +3 mặt sườn mới phủ; facadeTex 208)
- **Standalone cuối vòng: 10.453.464 byte** (đầu vòng 10.447.688 → +5.776 byte cho cả 4 việc; dư 32.296 byte so trần 10.485.760).
- Sự cố môi trường khi chạy lượt full đầu tiên: 3 cổng (standalone diag, check_sweep3, test_bd2) crash **ENOSPC** vì /tmp (tmpfs 512MB) đầy 100% — thủ phạm chính là /tmp/vercel-cli 398MB của tuyến Poko (không đụng); đã dọn scratch của tuyến này (/tmp/diag2 + bản sao index tạm, ~34MB) rồi chạy lại: cả 3 cổng PASS. Không phải lỗi game.

### ĐIỂM MÙ CÒN LẠI (chỉ chốt khi Chung Hy chơi thử web)
- FPS thật trên máy anh; grade ngày trên web; chữ biển dọc đọc thật/hướng chữ; cảm giác sườn sau phủ cây ở bản web; đảo/tượng ở khung r3 bản web. Link chơi thử vẫn chờ lệnh "gửi đi" của Chung Hy ở chat Chợ — vòng này KHÔNG upload, KHÔNG đẩy GitHub.

## V9-FACADE-CURVE (10/11/2026) — MẶT TIỀN CONG VÒNG CUNG + GÓC BO TRÒN (lệnh Chung Hy 01:45 "Làm mặt tiền cong như thật"; KHÔNG đẩy GitHub, KHÔNG upload link)
- Backup đầu vòng: assets/market.glb.bak-flat-20261110 (1.634.008 byte, sha256 fd9898a6…e47020d2) + scripts/build_models.py.bak-flat-20261110. Rebuild từ script chưa sửa ra 1.634.000 byte, cấu trúc trùng bản đang dùng → build_models.py là nguồn sự thật.
- **ĐO ĐỘ CONG (luật đo-không-đoán)**: ảnh thật 01 (1400×933, PIL) — khoảng mullion đều ~25px suốt x 412–952 (cung chính thoai thoải), bo tập trung 2 đầu (vùng chuyển ~5m). Chốt theo tỉ lệ ảnh: **sagitta S = 4,0; nửa bề rộng a = 33,5; R = (a²+S²)/(2S) = 142,28**; góc tiếp tuyến đầu 13,6°; S/bề rộng ≈ 0,060; sai số ước lượng ±1. research/23 chỉ ghi "khối cong ôm bùng binh", không có bán kính số — số này là ước lượng có ghi phương pháp, không phải số đo hiện trường.
- **CÁCH SỬA (tận gốc trong build_models.py)**: hàm `_v9_curve_facade()` gọi ngay trước export("market") trong build_market(). Chọn đối tượng có tâm bbox thế giới y > 4,2; loại Floor*/Well*/Terrace* (sàn + giếng thang + neo cầu nổi giữ nguyên tuyệt đối); bỏ qua CURVE. Vật hẹp (≤1,3: cột/mullion) → tịnh tiến lùi d(x) + yaw −asin(x/R). Vật rộng → xử theo đảo hình học: đảo hộp đơn dài >12, sâu ≤0,7, cao ≤3,6, ≤160 đỉnh, 1 vật liệu → dựng lại thành lăng trụ cong 5 trạm theo cung (bỏ bevel, UV phẳng); đảo nhỏ còn lại dịch đỉnh theo tọa độ thế giới. Lượt build thật: bent=52 moved=72 rebuilt=29, **không có WARN**. Neo: d(0)=0 → tâm mặt tiền giữ nguyên, index.html/marketFrontZ=12 KHÔNG đổi.
- **KIỂM CHỨNG NEO BẰNG SỐ (parse GLB cuối)**: LetterWall bbox x −33,5..33,5; mặt trước local z tại tâm = −7,94 → thế giới 12,06 (khớp neo 12, lệch 0,06 do bề dày trạm); tại 2 đầu = −3,60 → thế giới 16,40. **Độ lùi thực đo = 4,34** (S thiết kế 4,0 + 0,34 hiệu ứng góc trạm cuối). Bản phẳng cũ: mặt trước phẳng −8,10 suốt bề rộng.
- **BYTE**: market.glb 1.634.008 → **1.650.712 (+16.704 ≤ ngân sách +24.222)**. Standalone 10.453.464 → **10.475.736 byte (dư 10.024 so trần 10.485.760)**.
- **CỔNG (đủ bộ, trên bản cuối V9)**: diag 900 **SẠCH**; SEED_SAVE 300 **SẠCH**; standalone diag 300 **SẠCH**; traffic **26/26**; audit_ground **lỗi cứng 0, nhảy lưới 0**; test_bd2 **ALL PASS**; check_sweep3 **ALL PASS**; test_real1 **PASS**. → 8/8 XANH.
- **NGHIỆM THU HÌNH (render model thật, scripts/render_facade_real.py, Cycles 32 mẫu 900×600)**: renders/v9-facade-real.png + ghép renders/v9-cmp-r1.png (TRÁI render / PHẢI ảnh thật 01, có nhãn).
- **VERDICT HÌNH V9 (tự soi)**: **ĐẠT PHẦN CONG** — so với v8 phẳng: nửa phải mặt tiền lùi dần theo cung đọc rõ, góc đông chuyển từ gãy 90° thành bo tròn ôm theo cung, các băng lam/kính/zigzag/quảng cáo uốn liên tục không gãy khúc; nửa trái cong thoai như ảnh thật (ảnh thật vốn thoai). Chữ CHỢ ĐÀ LẠT hơi ngả theo cung tại tâm (chấp nhận được, vẫn đọc rõ). Lệch còn lại (chuyển sang vòng rà SWEEP-NIGHT-1 ngay dưới): tượng vẫn trắng sáng so với đá sẫm thật; thiếu biển MARCHÉ trên mái; khối thang trái vẫn trơn; phía phải mặt tiền còn trống; màu render Cycles nhạt hơn web (giới hạn render, không phải màu game).

## SWEEP-NIGHT-1 (10/11/2026) — VÒNG RÀ LỖI XUYÊN ĐÊM (lệnh mở rộng 02:02 sau V9; KHÔNG đẩy GitHub, KHÔNG upload link)
- Nguồn rà: KE_HOACH_MUSE_AI_V6.md (mục 0–3) + research/25 + research/23 + các verdict còn mở REALISM-1/V7/V8 + 5 đầu mối tuyến chính giao. Backup đầu vòng: index.html.bak-sweepnight-20261110, assets/roundabout.glb.bak-v9done-20261110, scripts/build_models.py.bak-v9done-20261110. Kỷ luật từng mục: diag 900 + package + đo byte; mục rủi ro dừng ở trạng thái sạch.
- **BYTE**: đầu vòng (sau V9) standalone 10.475.736 → cuối vòng **10.479.200 byte (dư 6.560 so trần 10.485.760)**.

### BẢNG RÀ + VERDICT TỪNG MỤC
| # | Hạng mục (nguồn) | Verdict | Việc đã làm / lý do |
|---|---|---|---|
| 1 | Tượng đá quá sáng so với đá sẫm thật (V8 điểm 2; research/23 §4) | ✅ ĐÃ SỬA | ĐO PIL ảnh 01: thân tượng median sRGB #858e91, mặt sáng #a1adb1, tán thông đá #4b5556. Sửa tận gốc build_models.py: StatueStone (0,64/0,63/0,60) → **(0,37/0,42/0,44)** xám xanh sẫm; rebuild roundabout.glb 1.080.244 → 1.080.236 byte (−8). Render sweep: tượng sẫm rõ so với bản v9 trắng. Đêm vẫn nổi nhờ STATUE_FX spotlight/emissive riêng ở web. |
| 2 | Biển MARCHÉ trên mái còn thiếu (V8 điểm 5; ảnh 01) | ✅ ĐÃ SỬA | Code-only (canvas trong suốt, không plaque nền): chữ #1d4e9e + chấm tròn #f7b500 (đo từ ảnh: vùng biển median #61719b gồm nền trời), plane 8,4×1,58 tại (8, 22,2, 15,0) rotY PI, 2 cột đỡ 19,45..22,05 đứng trên RoofSlab. **Vị trí chốt bằng đường ngắm từ render**: bản đầu tâm (21,6 / z 17,5) bị mép mái che (ngưỡng nhìn qua mép mái tại z 17,5 là 22,6) → nâng tâm 22,2 + kéo ra z 15,0 (ngưỡng 21,4 → biển 21,4..23,0 đọc được). Render wide đọc được trên mái. Render mô phỏng dùng text "MARCHE" không dấu (font Blender); bản web canvas có É đầy đủ. |
| 3 | Khối thang choán góc trái khung mặt tiền (V8 điểm 3) | ✅ ĐẠT MỘT PHẦN | Web: clone vật liệu CHỈ 2 mesh SideWall của stairs → 0x8a8175 + TEX_GRIME (không đụng bậc/chiếu nghỉ); thêm 3 thông thềm tây (−13,8; z −22/−15/−8 theo groundH thềm 14,2/8,5/2,8) như sườn đồi có cây ảnh 01. Render: thông tiền cảnh che tường đạt nhưng rất lớn trong khung (gần camera) — tỉ lệ cảm quan chốt khi chơi thử web. Lưu ý đo màu: helper render đổi hex gần đúng kiểu tuyến tính nên tường trên render Cycles sáng hơn web (web setHex chuẩn sRGB → sẫm hơn). |
| 4 | Dãy nhà phố phía phải (đông) mặt tiền còn trống (V8 điểm 5; research/23 §12) | ✅ ĐẠT MỘT PHẦN | Thêm 1 dòng placeHotel('HotelB', 47, 23.5, 0, PI, 6.5, 4.5): khối 13×9, 5 tầng, x 40,5..53,5 (cách mép đông chợ 6,5), z 19..28 thẳng hàng khối chợ, groundH = 0, không chồng shop (46,12,5). Render đông-nam (sweep-night-east.png): khối lấp trống cạnh góc đông, thấp hơn mái chợ như ảnh thật. Hạn chế: mặt hông tây trơn (template hotels.glb chỉ chi tiết mặt tiền — không thêm GLB mới trong trần byte); từ góc tây-nam khối bị chợ che khuất (đúng hình học, kiểm bằng tia ngắm); mặt tiền chính hướng −z ra phố trước chợ có cửa sổ/ban công/biển COLLINE. |
| 5 | Độ bão hòa màu mặt tiền trên web (V8 điểm 4) | ✅ ĐÃ SỬA | clampSat riêng ASSETS.market: trần bão hòa 0,35 → **0,45** (đo ảnh 01: băng hồng đào median #f3b99b; Peach GLB s≈0,56 bị kẹp 0,35 nên rửa màu). Không đụng hotels/nhóm khác. test_real1 PASS sau sửa. Màu render Cycles vẫn nhạt hơn web — giới hạn pipeline render, không phải màu game. |
| 6 | Dây điện ngang phố chợ đêm (research/25 §1: thật mỗi 8–10m) | ✅ ĐÃ SỬA | Cột phía nam 8 → 15 (thêm cột trung điểm vào mảng cx sẵn có): khoảng dây ~15m → 7–9m, bó 3 dây/cột giữ nguyên. Chỉ geometry runtime, 0 byte GLB. |
| 7 | Xe máy dựng sát mép sạp (bảng rà V7-1: CÓ MỘT PHẦN) | ◐ SỬA MỘT PHẦN | Cụm đậu vệ đường vào 9 → 13 chiếc (nam 6→8, bắc 3→5, màu/jitter theo hash sẵn có, không solid). Dày như ảnh thật cần rà va chạm người đi bộ kỹ hơn — để vòng sau. |
| 8 | Lòng đường vào 14–16m thật vs 45,5u game (research/25 §1) | ⛔ KHÔNG SỬA | Khác CÓ CHỦ ĐÍCH: giữ theo lệnh nới đường của Chung Hy ở các vòng trước (đã khóa trong bảng rà V7-1). |
| 9 | Tượng phải ở tiền cảnh TRÁI như ảnh 01 (V8 điểm 1) | ⛔ KHÔNG SỬA | Vị trí tượng/đảo khóa GEOMETRY-2; dời tượng cần Chung Hy duyệt riêng. |
| 10 | Sườn đồi facet hình học gốc (REALISM-1 lệch (1)) | ⛔ KHÔNG SỬA vòng này | Đã phủ texture cỏ + cây/bụi ở V7-2; sửa lưới groundH rủi ro audit_ground (đang 0 lỗi cứng/0 nhảy lưới rất nhạy). |
| 11 | Tháp rạp: game là tháp đồng hồ, thật là trụ chữ nhật giật cấp (research/23 §3) | ⛔ KHÔNG SỬA | Research ghi CHƯA ĐỦ TƯ LIỆU ảnh mặt tiền rạp hiện nay — không dựng đoán. |
| 12 | Tuyến phố Tăng Bạt Hổ dựng riêng (research/23 §8) | ⛔ KHÔNG SỬA vòng này | Chưa đủ tư liệu toàn tuyến + ngân sách byte cuối vòng chỉ dư 6.560. |
| 13 | Đài phun nước (research/23 §6) | GIỮ NGUYÊN | Vị trí trong game là neo sáng tạo đã ghi rõ trong research, không phải vị trí thật. |

### CỔNG CUỐI VÒNG (bản cuối) — ✅ 8/8 XANH
- diag_runtime 900: **SẠCH** · SEED_SAVE 300: **SẠCH** · standalone diag 300: **SẠCH**
- traffic **26/26** · audit_ground **lỗi cứng 0, nhảy lưới 0** · test_bd2 **ALL PASS** · check_sweep3 **ALL PASS** · test_real1 **PASS**
- Standalone cuối: **10.479.200 byte** (trần 10.485.760, dư 6.560). market.glb 1.650.712; roundabout.glb 1.080.236.
- Từng mục đều đã qua diag 900 + package riêng trước khi sang mục kế (tượng → MARCHÉ → thang → HotelB → bão hòa → dây điện → xe máy → chỉnh vị trí MARCHÉ).

### RENDER KIỂM CHỨNG VÒNG (đã tự soi từng ảnh)
- renders/sweep-night-facade.png (script render_sweep_night.py — bản sao render model thật + áp lớp sơn code): tượng sẫm ✓; thông che thang ✓ (lớn tiền cảnh); MARCHÉ ở vị trí cũ bị mái che → đã sửa vị trí (xem mục 2).
- renders/sweep-night-wide.png (render_sweep_wide.py, camera (−88,12,−42)): MARCHÉ đọc được trên mái ✓; tượng xám sẫm ✓; HotelB bị khối chợ che từ tây-nam (đúng hình học).
- renders/sweep-night-east.png (render_sweep_east.py, camera (26,5,5,−30) → (42,8,22)): HotelB lấp trống đông ✓; góc đông mặt tiền cong ôm qua góc đọc rõ ✓.

### ĐIỂM MÙ CÒN LẠI (chỉ chốt khi Chung Hy chơi thử web)
- FPS thật; grade/bão hòa web thật sau nới clamp; chữ MARCHÉ canvas trên web; tỉ lệ thông tiền cảnh cạnh thang; mặt hông HotelB nhìn từ bùng binh. Link chơi thử vẫn chờ lệnh "gửi đi" của Chung Hy ở chat Chợ — vòng này KHÔNG upload, KHÔNG đẩy GitHub.

## LAYOUT-FIX-1 (10/11/2026) — DỜI BẬC THANG VỀ HÔNG TÂY (lệnh Chung Hy 02:55 "bạn sắp xếp vị trí sai bét hết rồi, cầu thang đâu nằm đó, nằm xa ra, đâu có cắt với bùng binh đâu"; KHÔNG tự đẩy GitHub — tuyến chính đẩy theo ngoại lệ anh lệnh 03:07)

### BƯỚC 1 — AUDIT ĐO TRƯỚC KHI DỜI (số đo từ code + dump GLB, không đoán)
- stairs.glb đặt tại (0, 0, −16), không quay: bậc rộng 22 (x −11..11 local), SideWall ±11,35, Landing1 tâm local z −4,75 (top y 11,31), Landing2 z +5,75 (top 5,65) → bbox thế giới **x −11,6..11,6, z −30..−2, leo 0→17 theo −z** — khớp stairH/groundH từng chuyến.
- Đảo (−30, 0, −6): đĩa CurbRing Ø22,3 → mép đông **−18,85**; vành xe CircleGeometry R11,8; tượng thế giới (−34,2, −2,8). Nhà lồng (0,0,20), mặt tiền z=12, vách tây x=−34.
- **KẾT LUẬN SAI LỆCH:** mép tây thang (−11,6) chỉ cách mép đông đảo (−18,85) **7,25u** (ở giữa là dải "quảng trường thềm chân thang" rộng 7,2) — thang đứng NGAY TRƯỚC mặt tiền, song song sát đảo. Ngoài thật (research/25 §2, ảnh 10): thang di sản ở **hông sườn phía tây** chợ (110 NTMK), chân ở mặt đường thung lũng, leo lên tầng lầu rồi đỉnh đồi; bùng binh + tượng ở phía trước (nam) nhà lồng; từ trên thang nhìn XUỐNG thấy bùng binh xa + thấp, không giao cắt. Bằng chứng hình: renders/layout-before.png (top-down GLB thật: khối thang trắng sát ngay đông đảo).
- Neo phụ thuộc đã kiểm kê đủ: STAIR_SITTERS 50 người; Chú Ba (5,6; −19,6) + FORTUNE_PT (2,8; −19,2); 2 sạp trên bậc khoainuong (6,2; −21,6) / suadau (6,2; −10,4); AW_NODES idx 8–14 + 30–33, cạnh chuỗi i→i+1; LOOP + 5 tuyến wanderer leo thang; TERR/TERRW/rimKiosk/tiểu thương thềm/2 người đứng thềm trên; biển "BẬC THANG CHỢ ĐÀ LẠT" + 2 cột; thềm groundH ±(11..14,5); detectZone, surfaceAt, bubbleZoneKey, npcZoneOf, minimap, ambZone, TOUR_CPS, GUIDE_STAGES chặng 4, TUT_STEPS bước 2.
- Phát hiện phụ quyết định tọa độ đích: phía tây x<−35 KHÔNG phải sườn 17m mà là **hành lang đường vào thấp (entryRampY 0–5,5)** + hàng sạp bắc z −19,7 → tâm thang khả thi duy nhất không đụng đĩa đảo (mép tây −41,15) là **x = −56** (mép đông thân thang −44,4, đệm 3,25u tới đĩa; cách vách tây chợ 10,4u). 3 sạp bắc nằm trong dấu thang mới (trái cây −46 / hủ tiếu −51 / bánh mì −56) phải dời chỗ — xuống hàng nam z 30 còn trống.

### BƯỚC 2 — DỜI (Δx = −56, thuần code/tọa độ, 0 byte GLB/asset mới)
| Neo | Cũ | Mới |
|---|---|---|
| stairs GLB | (0, 0, −16) | **(−56, 0, −16)** |
| groundH thân thang | x −11..11 | **x −67..−45** (nhánh chen TRƯỚC các nhánh hành lang đường vào) |
| groundH thềm tây | −14,5..−11 (2,8/8,5/14,2) | **−70,5..−67** (giữ 3 dải) |
| groundH thềm đông | 11..14,5 | **−45..−43,5, chỉ 2 dải trên** (bỏ dải 2,8 → sân phẳng trước chân thang đông; hộp TERR đông bỏ dải thấp tương ứng) |
| STAIR_SITTERS ×50 | x −8,6..8,5 | **x −64,6..−47,5** (dịch đều −56) |
| Chú Ba / FORTUNE_PT | (5,6; −19,6) / (2,8; −19,2) | **(−50,4; −19,6) / (−53,2; −19,2)** (vẫn trên chiếu nghỉ 1, y 11,33) |
| khoainuong / suadau | (6,2; −21,6) / (6,2; −10,4) | **(−49,8; −21,6) / (−49,8; −10,4)** (chiếu nghỉ 1 / 2 như cũ) |
| traicay / hutieu / banhmi (sạp bắc bị chiếm chỗ) | (−46/−51/−56; −19,7) rotY 0 | **(−61/−74/−88; 30) rotY π** — hàng nam, khe trống giữa bánh ướt −56 / mứt −68,5 / dâu3 −81,5 / bánh flan −95 |
| AW_NODES thang | idx8 (0,1), cột (−2, −6..−29), (0,−36), idx30/31 (3,−11)/(6,2,−9,6), idx32/33 (1,−20)/(2,8,−19,6) | idx8 **(−56,1)**, cột **(−58, −6..−29)**, **(−56,−36)**, idx30/31 **(−53,−11)/(−49,8,−9,6)**, idx32/33 **(−55,−20)/(−53,2,−19,6)** |
| AW_EDGES | chuỗi i→i+1 đủ 15 mắt + [8,19] | **bỏ mắt 7→8** (cạnh thẳng sẽ cắt qua đĩa đảo), thêm **[7,19]**, **[8,48]**, **[48,2]**; nút đệm mới **idx48 (−53, 0,2)** ngay trước chân thang (cắt làn W gần vuông góc) |
| LOOP + 5 wanderer leo thang | cột x −3..3 | **cột x −59..−48** (giữ nguyên lệch tương đối) |
| 2 wanderer ven hành lang (@3147/@3149 cũ) | đi z −5,5..−3,4 cắt qua dấu thang mới | **vòng phía nam chân thang** qua z 3,2–3,4 |
| TERRW decor / rimKiosk ×5 / tiểu thương thềm ×5 / 2 người đứng / đèn + thông thềm | x −14,9..−12,8 | **x −70,9..−68,8** (theo thềm tây mới) |
| Biển chân thang + 2 cột | (0, 3,4, −0,6), cột ±5,2 | **(−56, 3,4, −0,6)**, cột **−61,2 / −50,8** |
| detectZone / surfaceAt / bubbleZoneKey / npcZoneOf / minimap / ambZone / TOUR_CPS / GUIDE chặng 4 / TUT bước 2 | rect/đích theo thang tâm 0 | **theo thang tâm −56** (minimap: hình chữ nhật thang mmX(−67)) |
| Cầu nổi (17,5; z −30..9) + thang trong nhà | giữ nguyên | **giữ nguyên** — đỉnh thang mới vẫn đổ ra cao nguyên đỉnh đồi y17 (z ≤ −30) như cũ, kết nối đồi → cầu → sân thượng không đổi |
| Giữ nguyên có chủ đích | quảng trường thềm ven đảo (−14,6; −6) + ghế đá/cẩm tú cầu; kè đá x −52..−14,5; lan can điểm nhìn z −30,4; rimCafe đỉnh đồi | thành sân ven đảo / kè sườn như cũ — không phải neo của thang |

### SỰ CỐ TRONG VÒNG (đã sửa tận gốc, cổng chạy lại từ đầu sau sửa)
- Lượt sửa đầu chèn chú thích `//` vào giữa dòng ở LOOP / AW_EDGES / 5 STALL_DEFS / SP_EXP (nuốt phần code còn lại của dòng) → audit vỡ trích xuất. Đã gỡ toàn bộ chú thích giữa dòng, `node --check` sạch mọi file, chạy lại đủ cổng.
- Audit vòng 1 sau dời: 28 lỗi cứng + 4 nhảy lưới → nguyên nhân thật: (a) cạnh chuỗi 7→8 tự sinh bắc qua đảo; (b) cạnh nam đảo chạy dọc làn W; (c) thềm đông dải thấp gây nhảy 2,8→0 cho tuyến ven đảo; (d) mép bắc thềm z=−30 lệch ngữ nghĩa nhánh. Đã sửa như bảng trên → audit 0/0.
- Giữa vòng /tmp/diag/node_modules bị dọn mất (diag báo thiếu package 'three') → cài lại three@0.160.0 vào /tmp/diag như các vòng trước.
- Camera facade V8 (−62, 4,5, −20) nay nằm ĐÚNG TRONG khối thang mới (render đen) → cặp facade trước/sau dùng camera lùi về quảng trường đông đảo (−14, 5,5, −20) → (2, 9, 13), script scripts/render_facade_pair.py; script top-down mới scripts/render_topdown_real.py (tham số --stairs-x).

### CỔNG CUỐI VÒNG (bản cuối, sau mọi sửa) — ✅ 8/8 XANH
- diag_runtime 900: **SẠCH** · SEED_SAVE 300: **SẠCH** · standalone diag 300: **SẠCH**
- traffic **26/26** (T0c cập nhật chuẩn 49 nút/48 cạnh theo đồ thị mới) · audit_ground **lỗi cứng 0, nhảy lưới 0** (whitelist inStairs/inBands dời theo thang; snapshot AW khớp index) · test_bd2 **ALL PASS** (điểm mẫu surface 'thang' → (−56,−15)) · check_sweep3 **ALL PASS** (SP_EXP chuba → (−50,4,−19,6)) · test_real1 **PASS**
- Fixture harness giao thông cập nhật khớp game: AW/LOOP/STALLS/groundH thang + T-FOOT → (−48, 0,2) (nhiệm vụ M3 leo thang lấy sữa đậu: d = 10,6–11,3 ≤ 12 ✓), CROSSINGS nút 8 → (−56, 1).
- **Byte: standalone 10.479.200 → 10.481.499 (dư 4.261 / trần 10.485.760). index.html 565.404 → 567.703. GLB: không đổi một byte.**

### RENDER KIỂM CHỨNG (đã tự soi)
- renders/layout-before.png → renders/layout-after.png (top-down GLB thật, cùng camera ortho): TRƯỚC — khối thang trắng sát ngay phía đông đảo, mép gần chạm vành; SAU — thang nằm hẳn phía tây đảo, tách đĩa + vành xe với đệm rõ, chấm đỏ mốc chân thang cũ nằm giữa khoảng trống. **Thang không còn cắt/kề bùng binh ✓**
- renders/layout-facade-before.png → renders/layout-facade-after.png (cùng camera quảng trường): TRƯỚC — vách hông + tay vịn thang choán ~55% khung trái, mặt tiền chỉ còn "LẠT"; SAU — mặt tiền hiện trọn, đủ chữ CHỢ ĐÀ LẠT / lam / zigzag / bảng quảng cáo, khối thang ngoài khung. **Thang không còn án ngữ khung mặt tiền ✓**

### VERDICT LAYOUT-FIX-1: ✅ ĐẠT (ở mức bố cục đo được + render GLB thật)
Thang đã về hông tây đúng vị trí thật tương đối (chân ở mặt đường phía tây nhà lồng, leo dọc sườn lên đỉnh đồi, tách hẳn bùng binh), toàn bộ neo phụ thuộc dời nhất quán, cầu/tầng 2 giữ nguyên kết nối qua cao nguyên đỉnh đồi, 8/8 cổng xanh, byte trong trần.
### ĐIỂM MÙ CÒN LẠI (chỉ chốt khi Chung Hy chơi thử web)
- Thân thang mới đứng trên nền hành lang đường vào thấp (0–5,5m) thay vì sườn đất ôm 17m như vị trí cũ: về hình khối nó đọc như khối bê tông di sản độc lập (đúng chất cầu thang 110 NTMK) nhưng cảm giác "ôm sườn" khác trước — chốt bằng mắt khi chơi thử.
- Hàng sạp bắc z −19,7 nay còn 2 sạp (đậu hũ −41, cháo −37) phía đông thang; 3 sạp dời xuống hàng nam làm hàng nam dày hơn (9 sạp) — mật độ phố ăn thực tế khi chơi thử.
- FPS/grade/cảm giác đi thang mới trên web thật.

## MERGE-GITHUB-1 — 10/11/2026 04:0x (hợp nhất bản Antigravity 02927de + V7/V9/LAYOUT-FIX-1, đẩy GitHub theo lệnh Chung Hy 03:07)
- Remote head trước merge: 02927de "fix(v6-landmarks)" (Antigravity, 03:41): Hoa Sữa dời lên dốc Tăng Bạt Hổ (-22,-43) tren dinh doi, La Tulipe + L'angfarm dinh thang, Thanh Binh Hotel, skyline Dalat Center/Colline, bo streetSign Tang Bat Ho o (-174,27.4). Root index.html remote da doi redirect sang prototype-v2/index-standalone.html (7e07085) + .nojekyll (3c4ae39) — KHONG day de 2 file nay.
- Merge 3 phia index.html (base 0dc7859 / remote 02927de / local V9+LAYOUT-FIX-1): 1 xung dot duy nhat o TUT_STEPS — giai quyet: check buoc 1 theo remote, text buoc 2 theo remote (La Tulipe & L'angfarm), target buoc 2 theo LAYOUT-FIX-1 (-56,-33). Hoa Sua theo vi tri MOI NHAT cua Chung Hy (-22,-43); logic hoi am 100% V7-2 khong phu thuoc vi tri, giu nguyen.
- build_models.py remote khong doi ke tu 0dc7859 -> ban local (cong V9) la ban duy nhat moi. GLB remote khong doi (market 1.634.008 = ban phang cu; roundabout 1.080.244) -> GLB cong/sẫm local day bang web upload rieng.
- Sau merge: cat 413 byte comment thua de standalone ve duoi tran: 10.485.576 byte (du 184). CANH BAO: tran byte chi con du 184 byte — them bat ky noi dung nao cung phai nen/bot truoc.
- Cong sau merge: 8/8 XANH (diag 900 sach, SEED_SAVE 300 sach, standalone 300 sach, traffic 26/26, audit 0/0, test_bd2 PASS, check_sweep3 PASS, test_real1 PASS).
- Diem mo con lai: La Tulipe/L'angfarm dat o 2 ben dinh thang CU (x +-17.5); thang da dời ve x=-56 nen 2 toa nha gio o dinh doi phia dong cua dinh thang moi — khong va cham, cho Chung Hy choi thu cham lai vi tri.

## STAIR-TOP-PAIR-1 — 11/11/2026 (1 mục duy nhất theo luật 18:05 10/11: dời cặp nhà đỉnh thang về ôm đỉnh thang MỚI)
- Bối cảnh: buildLaTulipe/buildLangfarmStairs (bản Antigravity 02927de) ôm đỉnh thang CŨ (x=0); sau LAYOUT-FIX-1 thang về tâm x=-56 nên cặp nhà ôm khoảng trống.
- TỌA ĐỘ: La Tulipe (-17.5,-33.5,17) -> (-73.5,-36.4,17) [tây]; L'angfarm (17.5,-33.5,17) -> (-38.5,-36.4,17) [đông]. x giữ đúng gương ±17.5 quanh tâm thang mới -56 như bản cũ quanh 0 (khe solid tới mép thang 1.4u mỗi bên, khớp bản cũ). Chỉ đổi đối số 2 điểm gọi; pine nội bộ L'angfarm theo tương đối (-33.3,-37.6)/(-33.7,-33.2) — không đụng vật nào. Không còn tham chiếu cứng nào khác tới tọa độ cũ (grep toàn file: chỉ 2 điểm gọi).
- VÌ SAO z -33.5 -> -36.4 (lệch "quanh -33.5" của brief, có số đo): giữ z=-33.5 thì thân nhà mới (z -36.6..-30.4) CẮT MESH THẬT với hàng shophouse z=-28.5 (thân tới z=-31.3, bệ solid tới -31.4): chồng mặt bằng 0.9u theo z, phía đông chồng x tới 4.6u (shophouse Bánh Mì & Sữa Nóng -42), phía tây 1.4u (shophouse Homestay Hoa Sữa -80) — render top-down lượt 1 bắt được. Lùi bắc 2.9u -> mép nam thân nhà -33.3, cách thân shophouse 2.0u, solid cách 1.8u: SẠCH cả mesh lẫn solid.
- AUDIT VA CHẠM tại chỗ đặt cuối: groundH vùng đỉnh (z<=-30) = 17 phẳng toàn vùng ✓; TERRW/đèn/thông/người thềm tây ở x -69.6..-70.9 nhưng z>=-30 ✓ không chạm; ki-ốt (-24,-37) cách solid L'angfarm 8.5u ✓; Hoa Sữa (-22,-43) + dãy ghế (z -39.8..) cách mép đông L'angfarm ~9.7u ✓; đèn (-34,-40) ngoài footprint ✓; lối đỉnh thang -> quảng trường: đường thẳng (-56,-33)->(-19,-48) qua phía nam solid L'angfarm, khe hẹp nhất ~3.4u tại x=-38.5, không chắn ✓; không lấn đĩa đảo/vành xe (điểm gần nhất cách tâm đảo >25u) ✓.
- CỔNG: 8/8 XANH trên bản cuối (diag 900 SẠCH, SEED_SAVE 300 SẠCH, standalone 300 SẠCH, traffic 26/26, audit 0 lỗi cứng/0 nhảy lưới, test_bd2 ALL PASS, check_sweep3 ALL PASS, test_real1 PASS) — chạy lại đủ 2 lượt (sau khi đổi z phải chạy lại toàn bộ).
- BYTE: index.html 571.780 -> 571.781 (+1 byte do "17.5"->"-38.5"); standalone 10.485.576 -> 10.485.577 (trần 10.485.760, dư 183) ✓ không cắt nội dung nào.
- NGHIỆM THU HÌNH: renders/stairtoppair-topdown.png (script scripts/render_topdown_stairtoppair.py): GLB thang thật tại (-56,0,-16) + HỘP FOOTPRINT đúng kích thước code cho 2 tòa (code-built, không có GLB — giới hạn đã biết) + footprint hàng shophouse/ki-ốt + mốc TOUR/check-in. Tự soi: cặp nhà ôm đúng 2 bên đỉnh thang mới, khe sạch với hàng shophouse, lối ra quảng trường thoáng. Cảm giác thật trong game (mặt tiền 2 tòa quay về phía nam như cũ, biển/ánh sáng) chỉ chốt khi Chung Hy chơi thử.
- Backup: index.html.bak-stairtoppair-20261111. KHÔNG đẩy GitHub, KHÔNG upload link (luật 18:05). DỪNG tại đây chờ Chung Hy xem.

## FACADE-COLOR-1 — 11/11/2026 (1 mục duy nhất: sửa màu mặt tiền nhà lồng theo SỐ ĐO ảnh thật 01)
### ĐO MÀU ẢNH THẬT (PIL, median theo vùng + quy tắc lọc pixel, ảnh 01-mat-tien-cho-ngay.jpg 1400x933)
- Tường kem chính: x[800,1000] y[262,286] nắng phải #e7e0e0; x[300,480] y[266,292] trái #f3f1f0; cánh phải x[985,1090] y[268,345] p50 #e8e3e4 -> chốt ~#eae5e1 (L~0.90, S thấp, gần trung tính ấm).
- Cột (pilaster phải): x[932,962] y[300,470] #e4e6e7.
- Băng hồng đào: giữa x[380,800] y[388,414] #e9bda5; lọc sáng s>0.25,l>0.60 p50 #ecbfa7; cánh phải x[995,1090] #ead0c0 -> chốt #ecbfa7 (H 0.058, S 0.645, L 0.790).
- Băng đào phần cong/bóng: #d6b09c (H 0.057, S 0.414, L 0.725).
- Kính tầng 2 (tối): x[390,820] y[316,352] lọc l<0.42 #364858 (H 0.578, S 0.239, L 0.278).
- Lam trắng dưới kính: x[390,820] y[356,388] #e7eae9 (L 0.912).
- Chữ đỏ CHỢ ĐÀ LẠT: x[510,800] y[282,316] lọc s>0.45 p50 #be4052 (H 0.976, S 0.496, L 0.498).
- Zigzag: phần trắng #e1e1e0; toàn dải (kèm chevron xám) #b0b6bd.
- Viền tan/nâu ấm: trên băng đào cong x[850,1010] y[372,388] #d8a88f; khung lam phải #ebb89f -> chốt ~#d8a88f.
### ĐO MÀU HIỆN TẠI (tái tạo đúng pipeline web bằng three r160: GLB -> clampSat(0.15,0.45,warmGray) -> ghi đè khi đặt scene)
- WallCream/ColumnCream: GLB #f1e6ce/#e5ddce -> hiệu dụng #e3d7bd (L 0.816, S 0.404) — TỐI và VÀNG hơn ảnh (~0.90) => lệch lớn thứ 2.
- MarketWin (GlassWin2/GlassWin3 = băng cửa sổ mặt tiền + ShopInBacks): GLB #fde7bf -> hiệu dụng #efe4d1 (kem nhạt L 0.878) trong khi ảnh là kính TỐI #364858 => LỆCH LỚN NHẤT.
- Peach: GLB #e5ad84 -> #deb091 (L 0.720, S 0.538) vs ảnh #ecbfa7 (L 0.790, S 0.645): tối + nhạt bão hòa.
- PeachDk: #c0987c (L 0.620) vs ảnh phần cong #d6b09c (L 0.725): tối.
- LouverWhite: #f9f7f1 (L 0.961, ấm) vs ảnh #e7eae9 (L 0.912, mát): hơi sáng/ấm.
- ZigBack: #c4bbab (be ấm do warmGray) vs ảnh chevron xám mát #b0b6bd: sai tông ấm.
- TrimBrown: #bc9579 (L 0.606) vs viền ảnh #d8a88f (L 0.704): tối.
- SignLetters: ép #c8372d (S 0.633, hue 0.011 cam) vs lõi chữ ảnh #be4052 (S 0.496, hue 0.976 hồng): hơi cam/bão hòa quá.
- render_facade_real.py trước vòng này chỉ áp 2 ghi đè (SignLetters #c8372d, WallCream #e3d7bd) và đặt thẳng số sRGB vào ô linear của Blender (không chuyển đổi) -> render rửa sáng, không trung thực web.
### ĐÃ SỬA (chỉ phía code web trong index.html, KHÔNG dựng lại GLB)
- clampSat: SignLetters ép 0xc8372d -> 0xbf3b47.
- mk.traverse: WallCream/ColumnCream 0xe3d7bd -> 0xeae3d5; MarketWin thêm color.setHex(0x3a4c5e) (emissive đêm giữ nguyên); thêm bảng FACADE_HEX áp cho Peach 0xecbfa7, PeachDk 0xd8b198, LouverWhite 0xe8eae9, ZigBack 0xb3b9bf, TrimBrown 0xd3a78b (clone material trước khi set như các nhánh cũ).
- Sau sửa, hiệu dụng (đo lại bằng cùng pipeline): WallCream #eae3d5, Peach #ecbfa7 (= đúng median ảnh), PeachDk #d8b198, MarketWin #3a4c5e, LouverWhite #e8eae9, ZigBack #b3b9bf, TrimBrown #d3a78b, SignLetters #bf3b47 — mọi vùng đều nằm trong ~0.01-0.03 L/H của số đo ảnh.
- BYTE: code thêm +393 byte; cắt 470 byte COMMENT (dòng clampSat market 221, R-10 122, V4.8 127 — chỉ comment, giữ nguyên code) -> index.html 571.781 -> 571.704; standalone 10.485.577 -> 10.485.500 (trần 10.485.760, dư 260; đạt đích <= 10.485.700).
### RENDER ĐỐI CHIẾU (scripts/render_facade_real.py đã cập nhật)
- Áp BẢNG MÀU HIỆU DỤNG ĐẦY ĐỦ của web cho mọi material market (không chỉ 2 ghi đè) + set_base_color chuyển sRGB->linear đúng ColorManagement của three.js.
- PHÁT HIỆN: camera V8 cũ (-62, 4.5, -20) nay nằm TRONG khối thang mới (bbox thang x -67..-45, z -30..-2 sau LAYOUT-FIX-1) -> render ĐEN hoàn toàn (đã bisect: tắt khối màu vẫn đen; dời camera là hết). Camera mới three (-41, 6.5, -48) ngắm (5, 9, 12), khoảng cách mặt tiền ~78u như góc V8.
- Ảnh: renders/facade-color-after.png + ghép renders/facade-color-cmp.png (trái render, phải ảnh thật 01, có nhãn).
### VERDICT (tự soi ảnh ghép, chấm thẳng)
- ĐẠT/GẦN THẬT: băng kính tầng 2 — từ kem nhạt thành tối xanh-xám + lam trắng, đọc giống ảnh nhất trong các vùng (sửa được lệch lớn nhất); chữ đỏ đậm đúng tông; zigzag trắng/xám mát khớp; viền tan nhẹ đúng mức; lam trắng hết ngả ấm.
- ĐẠT MỘT PHẦN: tường kem — sáng và bớt vàng rõ so với trước, nhưng trên render vẫn hơi XÁM/LẠNH hơn tường nắng ấm trong ảnh (mặt tây vào bóng của đèn Blender + AgX; albedo đã khớp số đo nên phần còn lại là ánh sáng, không phải màu vật liệu). Băng hồng đào đúng hue nhưng hiện diện thị giác YẾU hơn ảnh (dải GLB mỏng 0.92u + viền lam/bóng che một phần — lệch hình khối, không phải màu).
- CHƯA ĐẠT toàn cục: render vẫn kém sống động hơn ảnh thật (nền đất xám trung tính, thiếu nhà phố/người/xe/cây và nắng gắt Đà Lạt) — ngoài phạm vi mục màu; bố cục tượng tiền cảnh lệch (việc đã khóa GEOMETRY-2, không thuộc mục này). KHÔNG chấm "giống thật" toàn cục.
### CỔNG: 8/8 XANH (diag 900 SẠCH, SEED_SAVE 300 SẠCH, standalone diag 300 SẠCH, traffic 26/26, audit 0 lỗi cứng/0 nhảy lưới, test_bd2 ALL PASS, check_sweep3 ALL PASS, test_real1 PASS)
- Backup: index.html.bak-facadecolor-20261111. KHÔNG đẩy GitHub, KHÔNG upload link (luật 18:05). DỪNG tại đây chờ Chung Hy xem.

## FRONTAGE-1 — 11/11/2026 (1 mục duy nhất: dãy pano + LED tầng trệt mặt tiền theo số đo ảnh 01)
### AUDIT HIỆN TRẠNG (dump GLB market bằng Blender + grep code)
- GLB ĐÃ CÓ sẵn: AdBand 9 ô (tâm x -32..32 bước 8, ô 7.5 x 1.2, y 3.95..5.15, mặt trước z thế giới 11.76 tâm) vật liệu PHẲNG AdGreen/AdYellow/AdWhite/AdLED + AdInsets trắng y 4.15..4.95; mái che ShopAwnings (mặt trước: y 3.37..3.87, mũi z 10.84); Entrance kính x -3.25..3.25 (mặt z 12.14..12.44); cột solid code tại z 12.2 bước 8. Sau clampSat web các ô Ad chỉ còn pastel (#95cb95/#e3d5a9/#c88181) KHÔNG họa tiết -> tầng trệt "thưa" như verdict FACADE-COLOR-1.
- Code-built trước mặt tiền: chỉ đèn lồng (y 8.4, z 11.5 — trên dải), thùng rác, cột điện ở đường vào; KHÔNG có pano/biển nào ở dải trệt. Tuyến đi bộ trước sạp z 9.3 không bị pano dán tường (z 11.71) ảnh hưởng; không thêm solid.
### ĐO ẢNH 01 (PIL: crop dải trệt x140..960/y395..565 phóng 2x đọc biên + median điểm)
- Dải pano: y ảnh ~447..487 ngay dưới zigzag (đáy zigzag ~439), đáy pano trên mái che; chiều cao ~40px / tầng trệt ~86px = ~0.43-0.47. LED giữa: x ~545..680, nền gần đen, chữ đỏ tươi 2-3 dòng ("TOÀN ĐẢNG, TOÀN DÂN, TOÀN QUÂN / THI ĐUA LẬP THÀNH TÍCH CHÀO MỪNG ĐẠI HỘI XIV"), ngay trên cửa chính. Ô pano: nền trắng chủ đạo, logo xanh lá "Cozy", túi/chai sản phẩm xanh-vàng-cam, nhịp ô ~60-70px tâm ảnh; vài ô nền vàng. Mái che be #babca6 dưới pano.
- GIỚI HẠN HÌNH HỌC GLB (đo từ dump): cửa sổ fascia thấy được từ tầm đường bị kẹp: zigzag nhô z 11.49 từ y 4.82 che trên; canopy y 3.37..3.87 mũi z 10.84 che dưới (đường ngắm mắt 1.7 tại z 0 -> tường chỉ lộ y ~4.04..4.82, ~0.8u). Pano phủ đúng cửa sổ này là tối đa code-only làm được; đạt tỉ lệ 0.43 của ảnh cần sửa GLB (ngoài phạm vi mục).
### ĐÃ SỬA (code-only trong index.html, 1 block FRONTAGE-1 sau khối market)
- 9 pano canvas 512x80 phủ đúng 9 nhịp AdBand GLB: 7.5 x 1.15, tâm y 4.55 (3.98..5.13), z = 11.71 + d(x) theo cung V9 (R 142.28), rotY = PI - asin(x/R); 4 texture dùng chung: 'G'/'Y' (nền trắng/vàng + logo Cozy xanh #2e7d32 + 2 túi TRÀ/MẬT xanh-vàng-cam), 'B' (4 chai xanh/vàng/cam), 'L' LED (nền #120608, chữ #ff2418, emissiveMap 0.5). Nhịp trái->phải: B G Y G L G G Y B (LED đúng tâm trên Entrance). Không chắn cửa (Entrance lùi z 12.14 sau pano, kính dưới y 3.98 vẫn lộ), không solid mới.
- Lượt 1 để pano 7.5x2.23 (đúng tỉ lệ ảnh) — render soi thấy 2/3 họa tiết bị canopy/zigzag nuốt, chỉ lộ vệt trên -> thu về 1.15 và dồn họa tiết 1 hàng vào đúng cửa sổ thấy được (ghi ở trên).
- BYTE: block +3.197; cắt 3.331 byte COMMENT (2 lượt, 11 dòng: HotelB/GEO2 route/ROUTE_HILL/pull-over/V5.5-POLISH/AW/laneZW/BD2/bảng màu áo... — chỉ comment, assert code giữ nguyên từng chỗ) -> index.html 571.704 -> 571.413; standalone 10.485.500 -> 10.485.209 (trần 10.485.760, dư 551; đạt đích <= 10.485.700).
### RENDER ĐỐI CHIẾU (scripts/render_frontage.py = render_facade_real.py + mô phỏng pano)
- Pano trong render là MÔ PHỎNG đúng thông số code (vị trí/kích thước/yaw/màu, texture PIL vẽ lại đúng bố cục canvas game) — KHÔNG phải mesh game; game tự vẽ bằng CanvasTexture trong index.html.
- Ảnh: renders/frontage-after.png + ghép renders/frontage-cmp.png (trái render, phải ảnh thật 01).
### VERDICT (tự soi ảnh ghép + crop phóng to dải trệt)
- GẦN THẬT HƠN: dải trệt từ vệt pastel phẳng thành dãy LIÊN TỤC có nhịp ô trắng/xanh/vàng đọc được từ góc mặt tiền + khối LED tối chữ đỏ đúng tâm trên cửa chính — hai đặc điểm đập mắt nhất của ảnh 01 đã có mặt; ở crop phóng to đọc được logo Cozy + túi/chai.
- CHƯA ĐẠT: tỉ lệ dải vẫn MỎNG hơn ảnh rõ rệt (cửa sổ fascia của GLB chỉ ~0.8-1.15u so với pano thật ~0.43 tầng trệt) — họa tiết không đọc nổi ở khoảng cách render 75u, chỉ rõ khi lại gần trong game; pano thật có ảnh sản phẩm chụp thật + chữ nhỏ dày đặc, bản game là họa tiết vẽ tối giản 4 mẫu lặp. Muốn lên nữa phải sửa hình khối GLB (nâng dải fascia/hạ canopy) — việc khác, chưa làm.
### CỔNG: 8/8 XANH trên bản cuối (diag 900 SẠCH, SEED_SAVE 300 SẠCH, standalone diag 300 SẠCH, traffic 26/26, audit 0 lỗi cứng/0 nhảy lưới, test_bd2 ALL PASS, check_sweep3 ALL PASS, test_real1 PASS)
- Backup: index.html.bak-frontage-20261111. KHÔNG đẩy GitHub, KHÔNG upload link (luật 18:05). DỪNG tại đây chờ Chung Hy xem.

## FASCIA-GEO-1 — 11/11/2026 (1 mục: mở cửa sổ fascia tầng trệt trong GLB) — **DỪNG Ở CỔNG BYTE, ĐÃ KHÔI PHỤC SẠCH**
### ĐO TRƯỚC (dump đỉnh thật market.glb ship, world three, chợ tại (0,0,20))
- AdBand/pano: y 3.95..5.15 (pano code 3.98..5.13, tâm 4.55), mặt z 11.71+d(x) cung V9. Zigzag chevron: y **4.82**..6.14, mặt trước z 11.49. ZigzagBack 4.77..6.19 (z 12.03). Canopy ShopAwnings: y 3.37..3.87, mũi (z 10.84, y 3.42), mặt trên tại mặt pano cao ~3.83. AdTrimB 3.79..3.93 / AdTrimT 5.17..5.31. PeachBand đáy 6.26.
- Cửa sổ từ camera chuẩn render_facade (-41, 6.5, -48): tia sượt mép dưới chevron (11.49, 4.82) cắt mặt pano tại y≈4.81 -> thấy 3.98..4.81 = **0.83u ≈ 72%** pano. Canopy không cắt ở góc này (sượt mũi cắt tại 3.38) nhưng cắt mạnh tầm mắt gần (đi bộ z=9.3 chỉ lộ từ ~4.36). _v9_curve_facade: AdBand/ZigzagBack thuộc nhóm rebuilt cong 5 trạm; Zigzag + ShopAwnings thuộc nhóm đảo dịch đỉnh — đổi tham số vị trí không đổi cách xử lý.
### THAY ĐỔI ĐÃ THỬ (build_models.py, tham số thuần, 0 đỉnh/mặt mới)
- Nâng zigzag **+0.24**: ZigzagBack z 5.48->5.72 + chevron_row z 5.48->5.72. Hạ canopy **-0.10**: tmpAwn z 3.62->3.52. AdBand/pano/index.html GIỮ NGUYÊN (pano vẫn khớp AdBand, LED tâm trên Entrance).
- Build thử bằng build_one_glb: dump lại đúng thiết kế — Zigzag y **5.06**..6.38, canopy **3.27..3.77** (mũi y 3.32, z 10.84 như cũ); cửa sổ dự tính: sượt 5.06 cắt pano tại ~5.05 -> thấy 3.98..5.05 = **1.07u ≈ 93%** (đích >=90%). Kiểm chứng cong V9 trên bản build thử: [V9] bent=52 moved=72 rebuilt=29, LetterWall front lệch tâm-đầu 3.842 ~ S=4.0 — GIỮ NGUYÊN.
### VÌ SAO DỪNG (điều kiện byte của brief)
- market.glb build thử = **1.652.364** (+1.652 so với bản ship 1.650.712 > ngưỡng +300). Truy nguyên: build lại bằng script GỐC chưa sửa fascia cũng ra **1.652.360** -> riêng sửa fascia chỉ **+4 byte**; +1.648 là **lệch có sẵn** giữa build_models.py trên đĩa (mtime 19:17 09/11) và GLB ship (build 19:04 09/11). Dump đối chiếu 2 bản: 214 mesh / 43.631 verts / 27.188 tri, bbox + màu từng mesh KHỚP HẾT ở độ chính xác 0.01 -> lệch nằm ở tầng JSON/float dưới 0.01, không phải hình học nhìn thấy được.
- Hệ quả: dùng GLB build lại -> standalone ~10.487.412 (base64 +~2.203) **vượt trần 10.485.760 khoảng ~1.652** (hiện 10.485.209, dư 551). Đúng điều kiện dừng của brief -> **KHÔI PHỤC**: market.glb = 1.650.712, build_models.py = bản backup (84.684), index.html/standalone không hề đụng (571.413 / 10.485.209 = nguyên trạng FRONTAGE-1, bản đã qua 8/8 cổng ở vòng đó). Backup giữ tại .bak-fascia-20261111 (market.glb + build_models.py + index.html). Không chạy cổng vòng này (không có thay đổi nào được giữ lại), không render fascia-after (GLB đã khôi phục — render sẽ là hình cũ, gây hiểu lầm).
### PHƯƠNG ÁN ĐỀ XUẤT (chờ tuyến chính/Chung Hy chọn)
- **A (khuyến nghị):** 1 vòng riêng: áp lại 2 tham số trên + build lại market.glb (1.652.364) + cắt ~1.7-2.2KB COMMENT khỏi index.html (tiền lệ FRONTAGE-1 đã cắt 3.331 byte comment an toàn, assert code nguyên) -> standalone về ~10.485.2xx dưới trần; chạy đủ 8 cổng + render đối chiếu như brief. Rủi ro thấp: dump đã chứng minh hình học build lại khớp bản ship mọi mesh.
- B: truy đúng 1.648 byte drift ở tầng exporter/JSON để GLB build lại ~bằng bản ship — tốn công, lợi ích chỉ giữ trần byte.
- C: bỏ qua cửa sổ fascia (giữ 72%) — pano giữ nguyên như FRONTAGE-1.

## FASCIA-GEO-2 — 11/11/2026 (1 mục: hoàn tất fascia theo PHƯƠNG ÁN A của FASCIA-GEO-1) — **XONG, 8/8 CỔNG XANH**
### THAY ĐỔI (đúng thiết kế vòng 1, tham số thuần, 0 đỉnh/mặt mới)
- build_models.py: ZigzagBack z 5.48->5.72 + chevron_row 5.48->5.72 (nâng zigzag +0.24); tmpAwn z 3.62->3.52 (hạ canopy -0.10). AdBand/pano/index.html logic GIỮ NGUYÊN.
- Build bằng build_one_glb (pipeline sẵn có): market.glb = **1.652.364** — khớp tuyệt đối con số vòng 1 (build gốc chưa sửa = 1.652.360 -> riêng sửa fascia chỉ +4 byte).
### KIỂM CHỨNG HÌNH HỌC (dump world-bbox + màu cả 214 mesh, bản ship vs bản mới)
- Tổng: 214 mesh / 43.631 verts / 27.188 tri — KHỚP. Chỉ **4 mesh** lệch bbox, tất cả đúng thiết kế: ZigzagBack y 4.77..6.19 -> **5.01..6.43** (+0.24); Zigzag dịch +0.24 (wpos 5.48->5.72, wctr 5.72->5.96); Cube248/Cube248_1 (= ShopAwnings) y 2.15..5.09 -> **2.05..4.99** (-0.10; wpos group 3.62->3.52, khoảng canopy 3.27..3.77). 210 mesh còn lại: bbox + màu khớp ở 0.01 (đa số khớp tuyệt đối 3 số thập phân).
- Cong V9 NGUYÊN VẸN: log build "[V9] bent=52 moved=72 rebuilt=29"; LetterWall lệch tâm-đầu **3.842 ~ S=4.0**; bbox LetterWall/SignLetters cũ/mới giống hệt từng trục.
### BÙ BYTE (chỉ comment, có assert)
- Cần hấp thụ +1.652 GLB (base64 ~+2.203): rút gọn **27 dòng comment toàn dòng** trong index.html xuống <=62 byte/dòng (giữ thụt lề + mã mục; assert từng dòng mới là TIỀN TỐ của dòng cũ, số dòng không đổi, 0 dòng code bị đụng) -> tiết kiệm **2.704 byte**.
- Byte từng bước: market.glb 1.650.712 -> 1.652.364 (+1.652); index.html 571.413 -> **568.709** (-2.704); standalone 10.485.209 -> **10.484.705** (dưới đích 10.485.700 là 995; dưới trần cứng 10.485.760 là 1.055).
### CỔNG 8/8 XANH (trên bản cuối)
diag 900 sạch · SEED_SAVE 300 sạch · standalone diag 300 sạch (GAME_ROOT=/tmp/fg2/sa) · traffic **26/26** · audit **0 lỗi cứng / 0 nhảy lưới** · test_bd2 PASS · check_sweep3 PASS · test_real1 PASS.
### NGHIỆM THU (render_frontage.py đã cập nhật ghi chú fascia mới, xuất fascia-after.png + fascia-cmp.png)
- Cửa sổ pano (tia sượt từ camera chuẩn (-41,6.5,-48) qua đáy chevron tới mặt pano z=11.71, tính từ thông số GLB đo thật): TRƯỚC đáy chevron 4.82 -> cắt pano tại 4.81 -> thấy 0.84u ~ **73%** (vòng 1 ghi 0.83u/72%, lệch làm tròn); SAU đáy chevron 5.06 -> cắt tại 5.05 -> thấy **1.08u ~ 94%** pano (đích >=90% ĐẠT).
- PIL hiệu ảnh (frontage-after vs fascia-after, cùng camera): điểm khác biệt mạnh chỉ nằm ở **2 cụm hàng 329-347 (dải zigzag) + 355-369 (canopy)**, tổng 1.606 điểm — sửa không lan ra ngoài fascia. Crop phóng to soi mắt: TRƯỚC răng chevron cắn vào đỉnh pano (ô LED tâm bị che phần trên); SAU pano lộ TRỌN chiều cao, khoảng hở chevron-pano mở rõ.
- **VERDICT THẲNG:** đạt mục tiêu phương án A — cửa sổ pano 72% -> 94%, pano hết bị che đỉnh. NHƯNG tỉ lệ pano/tầng-trệt trong game vẫn ~0.22 (pano 1.15u / tầng trệt ~5.3u) so với ảnh thật **0.43** — pano bản thân vẫn mỏng ~2 lần; muốn đạt phải tăng chiều cao AdBand + pano (sửa sâu hơn, NGOÀI phương án A, chưa làm).
### GHI CHÚ DRIFT (QUAN TRỌNG cho các vòng sau)
- **Từ vòng này, GLB SHIP = build của build_models.py HIỆN TẠI.** Drift 1.648 byte tầng JSON/float giữa script trên đĩa (sửa 19:17 09/11) và GLB ship cũ (build 19:04 09/11) đã được HẤP THỤ bằng cắt comment ở trên; hình học đã chứng minh khớp 0.01 toàn bộ 214 mesh. Các vòng sau build lại market.glb sẽ ra ~1.652.364 (xác định — build 2 lần cùng kích thước), KHÔNG coi 1.650.712 là chuẩn nữa, không "truy drift" lại.
- Backup vòng này: assets/market.glb.bak-fasciageo2-20261111 + scripts/build_models.py.bak-fasciageo2-20261111 + index.html.bak-fasciageo2-20261111. Không đẩy GitHub, không upload link (theo brief).

## GLB-QUANTIZE-1 — 11/11/2026 (1 mục: lượng tử hoá KHR_mesh_quantization toàn bộ 14 GLB trong assets/) — **XONG, 8/8 CỔNG XANH**
### QUY TRÌNH (đúng research/26 mục 1 + quy trình an toàn 6 bước)
- Công cụ: gltf-transform CLI 4.5.1 cài tại /tmp/diag (npm i @gltf-transform/cli) — KHÔNG cài vào dự án. Lệnh mặc định: `gltf-transform quantize` (POSITION 14-bit, NORMAL 10-bit, TEXCOORD 12-bit, COLOR 8-bit). KHÔNG meshopt (tránh decoder), KHÔNG weld/simplify, KHÔNG strip TEXCOORD_0 (luật cấm research/26 mục 3: web gắn TEX_GRIME bằng UV lúc chạy).
- Dump cấu trúc TRƯỚC bằng @gltf-transform/core (NodeIO + ALL_EXTENSIONS): cả 14 file đều **0 skin / 0 animation / 0 morph** (character.glb là mesh tĩnh nhiều primitive, không có skin) -> không cần tham số skin riêng.
- Quantize trên bản sao -> dump SAU -> đối chiếu: nodes/meshes/primitives/verts/tris/primsUV/morph/tên material **khớp 100% ở 14/14 file**; extension duy nhất thêm vào là KHR_mesh_quantization (market vốn có sẵn KHR_materials_emissive_strength từ trước, giữ nguyên). Không file nào bị loại. three r160 đọc native, 0 dòng code sửa.
- Thay assets kèm backup từng file: `assets/<ten>.glb.bak-quantize-20261111`.
### BẢNG BYTE (trước -> sau)
| file | trước | sau | giảm |
|---|---|---|---|
| bridge.glb | 353.360 | 78.432 | -77,8% |
| cafe.glb | 151.052 | 54.472 | -63,9% |
| character.glb | 361.500 | 224.468 | -37,9% |
| hotels.glb | 1.488.196 | 403.116 | -72,9% |
| lamp.glb | 100.012 | 71.692 | -28,3% |
| market.glb | 1.652.364 | 664.956 | -59,8% |
| pier.glb | 19.104 | 13.392 | -29,9% |
| pine.glb | 65.404 | 33.232 | -49,2% |
| roundabout.glb | 1.080.236 | 689.652 | -36,2% |
| shop.glb | 172.392 | 65.024 | -62,3% |
| stairs.glb | 95.096 | 38.256 | -59,8% |
| stall.glb | 1.110.612 | 526.280 | -52,6% |
| theater.glb | 426.716 | 152.104 | -64,4% |
| vehicle.glb | 360.472 | 222.200 | -38,4% |
| **TỔNG assets** | **7.436.516** | **3.237.276** | **-4.199.240 (-56,5%)** |
- Standalone: 10.484.705 -> **4.885.717** (-5.598.988, -53,4%). Trần 10.485.760 -> **HEADROOM MỚI = 5.600.043 byte** (trước vòng này chỉ dư 1.055). Nút thắt byte của dự án đã gỡ: từ nay thêm nội dung không còn phải cắt comment bù từng trăm byte (vẫn giữ kỷ luật đo trước/sau).
### CỔNG 8/8 XANH (trên bộ assets quantized)
diag 900 sạch · SEED_SAVE 300 sạch · package + standalone diag 300 sạch (GAME_ROOT=/tmp/quant1/sa) · traffic **26/26** · audit **0 lỗi cứng / 0 nhảy lưới** · test_bd2 PASS · check_sweep3 PASS · test_real1 PASS.
### NGHIỆM THU HÌNH (render_facade_real.py cùng thông số, GLB gốc vs quantized)
- Ảnh: renders/quantize-before.png + renders/quantize-after.png + ghép renders/quantize-cmp.png.
- Median PIL theo vùng màu hiệu dụng (phân đoạn theo màu đích FACADE-COLOR-1): tường kem [202,203,204] vs [202,203,204] lệch **0,0**; kính MarketWin [74,85,90] vs [74,85,90] lệch **0,0**; băng đào [184,181,179] vs [184,181,179] lệch **0,0**; chữ đỏ [181,99,87] vs [182,99,87] lệch **1,0**. Lệch lớn nhất **1,0/255 <= 2 ĐẠT** (chênh còn lại là nhiễu render Cycles). Số pixel từng vùng khớp sát (kính 43.069/42.997, đào 63.460/63.585) -> hình học thực tế không đổi. Soi mắt 2 ảnh: không phân biệt được.
### LUẬT PIPELINE MỚI (để lại đường lặp lại)
- **Từ nay MỖI lần build lại bất kỳ GLB nào từ Blender phải chạy `bash scripts/quantize_glbs.sh` trước khi đóng gói/ship** (script tự backup .bak-quantize-<ngày>, validate từng file mới thay, in bảng trước/sau; có DRY_RUN=1). Đã test script ở chế độ DRY_RUN trên bản gốc: cho lại đúng số byte 664.956/13.392 (xác định).
- GLB ship từ vòng này = bản QUANTIZED của build_models.py hiện tại; bản float gốc luôn nằm ở .bak-quantize-20261111 cạnh mỗi file. Không đẩy GitHub, không upload link (theo brief).

## ADBAND-TALL-1 — 11/11/2026 (1 mục: tăng chiều cao dải pano tầng trệt về tỉ lệ ảnh thật) — **XONG, 8/8 CỔNG XANH**
### ĐO THIẾT KẾ (trước khi sửa)
- Ảnh 01 (PIL quét mịn 3 cột x=600/790/880 + crop phóng to soi biên): đáy zigzag y≈452; pano y≈460..500 = **40px**; tầng trệt = đáy zigzag 452 → chân mặt tiền 538 = **86px** (khớp FRONTAGE-1) → tỉ lệ pano/tầng-trệt thật **0.465**.
- GLB float (dump market.glb.bak-quantize-20261111): mẫu số tầng-trệt = 0 → đáy ZigzagBack **5.01**. Chồng lớp trệt: ShopInCeils 3.35..3.49 · canopy tại mặt pano ~3.68..3.77 (tường) · AdTrimB 3.79..3.93 · **AdBand 3.95..5.15 (1.20)** · AdInsets 4.15..4.95 · AdFrame 3.80..5.30 · AdTrimT 5.17..5.31 · ZigzagBack 5.01..6.43 · Entrance kính −0.10..4.30. Tỉ lệ hiện tại: GLB 1.20/5.01 = **0.240**; canvas 1.15/5.31 = 0.217 (số verdict FASCIA-GEO-2).
- ĐÍCH: AdBand **3.00..5.15 (2.15)** → 2.15/5.01 = **0.429** (trên 5.31: 0.405) ✓ trong 0.38–0.45. Canopy hạ −0.85 (tâm 3.52→2.67; mép trên tại tường 3.77→2.92) nằm NGAY DƯỚI đáy pano 3.00 như ảnh, clearance tại mặt pano ≈0.12–0.17 (không xuyên hình khối — đã tính từ công thức xoay canopy). Tia ngắm camera chuẩn (−41,6.5,−48): chevron (11.49, 5.06) cắt mặt pano tại 5.055 → thấy 3.00..5.055 = **95,6%** ✓ ≥90%; mũi canopy mới (10.84, ~2.47) cắt tại 2.41 < đáy pano → không che thêm. Không chắn Entrance (kính 0..3.00 vẫn lộ, LED phủ phần kính trên như ảnh; không thêm solid), tuyến đi bộ z 9.3 không đổi.
### ĐÃ SỬA (build_models.py tận gốc → build → quantize, đúng luật GLB-QUANTIZE-1)
- build_models.py: AdBand (7.5, 0.14, **2.15**) tâm z **4.075**; AdInsets (6.4, 0.16, **1.75**) tâm 4.075 (giữ lề 0.20); AdFrame (7.9, 0.20, **2.45**) tâm 4.075 (2.85..5.30); AdTrimB z 3.86→**2.93** (2.86..3.00); tmpAwn z 3.52→**2.67**. Không đụng zigzag/PeachBand/cong V9.
- Build (build_one_glb market): log "[V9] bent=52 moved=72 rebuilt=29", LetterWall lệch **3.842 ~ S=4.0** — cong nguyên vẹn. Dump đối chiếu float cũ/mới: 214 mesh, **chỉ đúng 17 mesh đích lệch** (9 AdBand → 3.00..5.15; AdTrimB → 2.86..3.00; AdFrame → 2.85..5.29; 4 AdInsets → 3.20..4.95; 2 ShopAwnings dịch đúng −0.85), 197 mesh còn lại khớp tuyệt đối.
- Quantize RIÊNG market (ASSETS_DIR trỏ thư mục tạm chứa float mới, tránh quantize lại 13 file đã quantized): 1.652.272 → **664.960**. Kiểm chứng bản quantized: 209 mesh/214 prim/43.631 verts, extensions [KHR_materials_emissive_strength, KHR_mesh_quantization], TEXCOORD_0 giữ — khớp cấu trúc bản ship cũ. assets/market.glb.bak-quantize-20261111 đã thay bằng float mới (float cũ giữ ở .bak-adband-20261111 + .bak-fasciageo2-20261111).
- index.html (block FRONTAGE-1): pano canvas **512×144** (layout vẽ lại cho khung cao: LED **3 dòng** như ảnh 01, logo Cozy + 2 túi TRÀ/MẬT cao, 4 chai cao), PlaneGeometry(7.5, **2.11**), tâm y **4.075** (3.02..5.13); nhịp B G Y G L G G Y B giữ nguyên, LED tâm trên Entrance.
### BYTE TỪNG BƯỚC
- market float 1.652.364 → 1.652.272 (−92); market quantized (ship) 664.956 → **664.960** (+4); index.html 568.709 → **568.927** (+218); standalone 4.885.717 → **4.885.943** (+226; trần 10.485.760, headroom 5.599.817 — không cần cắt comment).
### CỔNG 8/8 XANH (trên bản cuối)
diag 900 sạch · SEED_SAVE 300 sạch · standalone diag 300 sạch (GAME_ROOT=/tmp/adband/sa) · traffic **26/26** · audit **0 lỗi cứng / 0 nhảy lưới** · test_bd2 PASS · check_sweep3 PASS · test_real1 PASS.
### NGHIỆM THU (render_frontage.py cập nhật pano 7.5×2.11 @ y 4.075 + texture mô phỏng 512×144; xuất adband-after.png + adband-cmp.png)
- PIL diff fascia-after ↔ adband-after: điểm ảnh đổi chỉ nằm ở **hàng 342..407** (đúng dải fascia: pano + canopy) — không lan ra phần nào khác của khung.
- PIL quét cột x=735 (ô 'G'): pano thấy được **11px → 23px**; tầng trệt trong render (đáy zigzag ~345 → chân ~395) = 50px → tỉ lệ render **0.22 → 0.46** (ảnh thật 0.465 — khớp trong sai số phối cảnh). Tỉ lệ hình học chính xác: 0.240 → **0.429**.
- Soi mắt ảnh ghép: dải pano giờ là một BĂNG có hiện diện thật dưới zigzag, canopy nằm sát ngay dưới pano như ảnh; Entrance không bị bịt (kính dưới LED vẫn lộ, lối vào thoáng); không thấy vệt xuyên hình khối giữa pano và canopy.
- **VERDICT THẲNG:** ĐẠT mục tiêu tỉ lệ — pano hết "mỏng", tỉ lệ khớp ảnh thật ở cả số hình học (0.429) lẫn số đo trên render (0.46 ≈ 0.465). Chưa đạt tuyệt đối: (1) texture pano trong render MÔ PHỎNG bị Cycles rửa nhạt ở khoảng 75u (ô LED tâm đọc sáng trong render — y hệt ở fascia-after TRƯỚC vòng này, mean RGB 165 vs 161: giới hạn pipeline render mô phỏng, KHÔNG phải lỗi game — trong game trình duyệt vẽ CanvasTexture tương phản đầy đủ như FRONTAGE-1 đã xác lập); (2) vùng cửa hàng dưới canopy trong game vẫn cao hơn ảnh (trần ki-ốt 3.35) — lệch tỉ lệ riêng của tầng trệt, ngoài phạm vi mục này.
- Backup: scripts/build_models.py.bak-adband-20261111 + index.html.bak-adband-20261111 + assets/market.glb.bak-adband-20261111 (float gốc). render_frontage.py đã cập nhật thông số pano mới. Không đẩy GitHub, không upload link (theo brief). DỪNG.

## WATER-1 — 11/11/2026 (1 mục: mặt nước đài phun rõ hơn, theo thiết kế research/27) — **XONG, 8/8 CỔNG XANH**
### PHÁT HIỆN GỐC RỄ BỔ SUNG (ngoài thiết kế 27 — đo bằng raycast three r160 trên hình học thật)
- Bồn đài phun là CylinderGeometry (2.7/2.9/0.55)@0.28 **ĐẶC CÓ NẮP**: đĩa nắp đá y **0.555** che KÍN đĩa nước y 0.50 + vòng gợn y 0.53/0.542. Kiểm chứng tia ngắm lệch tâm 1.2u từ camera diorama (34,7,12.2): chồng CŨ — BASIN hit trước (10.77) rồi mới WATER (10.86) = nước bị che 100%; chồng MỚI — WATER hit trước (10.81), BASIN sau (10.85) = nước nhìn thấy thật. Thứ người chơi thấy xưa nay ở bồn CHỈ là nắp đá + tia — đây mới là nguyên nhân sâu nhất của "hồ nước không rõ" (thiết kế 27 mới chỉ ra màu nhạt/tương phản yếu).
- Hệ quả bắt buộc: chồng mặt nước phải nâng LÊN TRÊN miệng bồn (đáy 0.558 / nước 0.58 / gợn 0.605+). Bồn giữ nguyên vị trí + kích thước + cơ chế phun; solid không đổi.
### ĐÃ SỬA (chỉ index.html, code-only — đúng thiết kế 27)
- Mặt nước: canvas 256² bake nền **0x276a8a** + 46 vệt gợn **#bfe6f5** (seed sin như stoneTex; bake màu vào texture vì map NHÂN màu material sẽ làm vệt sáng tối đi — material để trắng, màu hiệu dụng vẫn đúng 0x276a8a), `ripTex` RepeatWrapping repeat (2,2) SRGB; vật liệu roughness **0.15**, opacity **0.93** cố định, emissive 0x1d4e5f (intensity 0 ban ngày).
- Đĩa đáy **0x14425c** r2.45 y 0.558 (chặn đá bồn pha rửa màu qua lớp opacity); vành miệng bồn RingGeometry r 2.45–2.72 y 0.565 màu **0xd8d2c2**.
- tickWater: bỏ dao động opacity ±0.06 (nguồn rửa màu), giữ nhấp y ±0.02; thêm trôi offset texture chéo chậm (0.008/0.005 mỗi giây) — mặt nước chuyển động liên tục. Vòng gợn: đỉnh opacity 0.38 → **0.5** (trên nền teal tối CR lý thuyết 1.71 → 5.43). Tia: màu 0xcfe8f4 → **0xeaf6fc**, opacity quanh **0.7**.
- Đêm: `waterMats` (cơ chế list như uplightMats) — applyDayNight đêm → emissiveIntensity **0.55**, ngày → 0. applyDayNight chạy lúc khởi tạo (isNight=true mặc định 19:00) nên bản đêm mặc định đã áp.
### BYTE
- index.html 568.927 → **572.203** (+3.276 — gồm comment ghi phát hiện nắp bồn; ngân sách thiết kế ước 0.8–1.0KB là cho code trần, thực tế kèm tài liệu hoá theo idiom dự án). Standalone 4.885.943 → **4.889.219** (trần 10.485.760 — headroom ~5,6MB, không cắt comment).
### CỔNG 8/8 XANH (trên bản cuối)
diag 900 sạch · SEED_SAVE 300 sạch · package + standalone diag 300 sạch (GAME_ROOT=/tmp/water1/sa) · traffic **26/26** · audit **0 lỗi cứng / 0 nhảy lưới** · test_bd2 PASS · check_sweep3 PASS · test_real1 PASS.
### NGHIỆM THU (harness scripts/render_water.py — mô phỏng đúng thông số code, ACES 1.3; ảnh renders/water-{before-day,day,before-night,night}.png + ghép renders/water-cmp.png)
- PIL (hộp mẫu nước (470,275)-(580,320), sân (40,430)-(150,500) trên bản NGÀY): TRƯỚC — vùng "nước" median **(167,167,167) xám đá**, CR nước/sân **1.13** (không có nước nào để đo — đúng như raycast: chỉ có nắp đá). SAU — nước median **(40,91,126)** họ teal (đích thiết kế #276a8a=(39,106,138), lệch do ánh sáng/ACES), CR nước/sân **3.42 ≥ 2.0 ĐẠT** (thiết kế hex-CR 2.16).
- Soi mắt: NGÀY — trước: đĩa đá xám trơn, không một giọt nước; sau: đĩa teal đậm, vệt gợn trắng đọc rõ, vành sáng ôm mép, vòng gợn quanh cột thấy được. ĐÊM (bản chính 19:00) — trước: đĩa đá xám với vệt đèn chân; sau: đĩa teal phát sáng nhẹ, gợn vẫn đọc được, vành bắt đèn ấm — mảng lạnh nổi rõ giữa sân ấm, không chìm.
- **VERDICT THẲNG:** ĐẠT — lần đầu tiên bồn đài phun có nước NHÌN THẤY được trong game (trước vòng này mặt nước tồn tại trong code nhưng bị nắp bồn che 100%). Màu + gợn + vành + đêm đều đạt số đo thiết kế. Giới hạn còn lại: harness là mô phỏng Blender đúng thông số (không phải screenshot web thật — giới hạn QA đã biết của dự án); chuyển động trôi gợn chỉ kiểm chứng được khi chơi thử thật.
- Backup: index.html.bak-water-20261111. Không đẩy GitHub, không upload link (theo brief). DỪNG.

## XH-0 — 11/11/2026 (1 vòng: KHUNG hồ Xuân Hương — groundH + mặt đất trống + minimap + zone) — **XONG, 8/8 CỔNG XANH**
### PHẠM VI (đúng KE_HOACH_HO_XUAN_HUONG §9 vòng XH-0 + §11 S1)
Khung bản đồ tây-nam: mở biên về khung đã khóa (nước x −352..−224, z 36..116; biên mới x −360, z +132), groundH khu hồ, mặt đất trống tối thiểu, solid kè, nhãn zone, minimap khung mới. CHƯA làm: nước thật/kè đá/lát (XH-1), model thuyền + Thủy Tạ (XH-2), trang trí bờ + NPC (XH-3), đạp vịt (XH-4), stamp/photo (XH-5). Chỉ đụng index.html — không GLB, không build_models.py.
### ĐÃ SỬA (chỉ index.html)
- **groundH**: thêm 1 nhánh XH-0 đặt TRƯỚC nhánh hành lang trục tây + mọi nhánh mặc định, chỉ kích hoạt khi `x < -208 && z −25..140`: đĩa đảo Thủy Tạ R15 tâm (−250,58) = 5,5 (S1); dải cầu x −251.25..−248.75, z 36..43 = 5,5 (S1); taluy nam z ≥116 (ưu tiên tại đúng biên z 116: chân taluy 5,5) dốc 5,5 → 9 tới z 132, thềm sau 9 tới z 140; mặt nước x −352..−224, z 36..116 = 4,9; còn lại (thềm bờ bắc: lối nối + đường dạo + cỏ) = 5,5. **Sửa đúng bẫy "vách giả"** §2: trước sửa, x<−208 & z>34 rơi về nhánh mặc định `z>=−2 → 0` (thềm trục tây là 5,5).
- **Mặt đất trống** (khối code mới ngay trước khối trục đường vào; màu cỏ 0x5f8547 được REALISM-1 phủ TEX_GRASS): nền cỏ thềm bờ bắc 144×61 tại (−288, 5.45, 5.5); nền đường dạo phẳng 0xdde2e2 z 28..36; đáy hồ tạm trung tính 0x46545a plane 128×80 tại (−288, 4.86, 76) (mặt nước thật 4,9 ở XH-1); đĩa đảo R15 cỏ; dải cầu 3×7 lát tại (−250, 5.46, 39.5); bờ tây + bờ đông mỗi bên 8×80 cỏ; taluy nam = hộp xoay −0.219 khớp groundH (5,5→9); thềm sau z 132..142; kè tạm 0x5e5852 dọc z 36.
- **solid kè** z 36: 2 đoạn solid(−301.6, 36, 50.4, 0.4) + solid(−236.4, 36, 12.4, 0.4) → phủ x −352..−251.2 và −248.8..−224, **chừa khe cầu đảo 2,4u** tại −251.2..−248.8 (cầu rộng 2,5 tại −251.25..−248.75). Đoạn bến theo §7 (−266..−252) CHƯA mở — mở ở XH-3 khi có cầu bến, tránh người chơi đi xuống mặt nước chưa có bến.
- **detectZone**: thêm 4 nhãn trước nhánh quảng trường: đảo (R16 quanh (−250,58)) "Đảo Thủy Tạ — Hồ Xuân Hương"; mặt nước "Hồ Xuân Hương"; x≤−200 & z 18..36 "Bờ hồ Xuân Hương — Đ. Trần Quốc Toản"; x≤−200 & z 6..18 "Lối xuống hồ Xuân Hương". Không stamp (stamp 'lake' là việc XH-5 theo §8).
- **minimap**: mmX/mmY khung mới **x −360..92 (452u), z −88..132 (220u)**; cập nhật cả 4 rect vẽ tay dùng hệ số cũ (/304, /128 → /452, /220: đồi, nhà lồng, bậc thang, khu quần áo); thêm vẽ hồ (rect nước #2e6da4), đĩa đảo, dải đường dạo bờ bắc, nét lối nối (−206,8)→(−232,26). Rà grep: toàn bộ hằng số khung cũ chỉ nằm ở khối này.
### KIỂM CHỨNG RIÊNG CỦA VÒNG (script trích groundH từ bản mới + backup, diff lưới)
- **Khu cũ không đổi**: quét lưới x −216..92 × z −88..50 (bước 1): **0 điểm** khác ngoài vùng cho phép; điểm khác chỉ nằm trong {x<−208, z>34} (128 điểm lưới — đúng vùng hồ mới). Vì nhánh mới có điều kiện x<−208 đứng trước hành lang, mọi điểm x≥−208 giữ nguyên giá trị theo cấu trúc.
- **Bảng điểm mẫu khu hồ** (26 điểm, tất cả khớp): spawn (−206,5.6)=5,5; lối nối (−210,12)/(−220,19)/(−232,26)=5,5; đường dạo (−238..−338, 30)=5,5; nước (−300,76)/(−230,40)/(−345,110)/(−270,58)=4,9; đảo (−250,58)/(−250,45)=5,5; cầu (−250,37)/(−250,40)=5,5; taluy (−288,116)=5,5, (−288,124)=7,25, (−288,132)=9, (−288,138)=9; bờ tây (−356,76)=5,5, bờ đông (−222,76)=5,5.
- **Tuyến đi bộ** (lấy mẫu liên tục, ngưỡng nhảy >0,11): spawn → lối nối → cuối đường dạo (−338,30): thông, 0 nhảy; bờ (−250,30) → cầu → tâm đảo (−250,58): thông, 0 nhảy (kè solid chừa đúng khe cầu; mặt đất liên tục 5,5 suốt tuyến).
### BYTE
- index.html 572.203 → **576.484** (+4.281: groundH + khối đất + zone + minimap, đúng dự tính §9 +3–5KB). Standalone 4.889.219 → **4.893.500** (+4.281; trần 10.485.760 — headroom ~5,59MB).
### CỔNG 8/8 XANH (trên bản cuối)
diag 900 sạch · SEED_SAVE 300 sạch · package + standalone diag 300 sạch (GAME_ROOT=/tmp/xh0/sa) · traffic **26/26** · audit **0 lỗi cứng / 0 nhảy lưới** · test_bd2 PASS · check_sweep3 PASS · test_real1 PASS.
### NGHIỆM THU (scripts/render_xh0.py — mô phỏng đúng thông số code; renders/xh0-topdown.png + renders/xh0-diorama.png)
- Top-down: khung khớp sơ đồ §2 — dải đường dạo dọc bờ bắc mặt nước, cầu nối ra đĩa đảo Ø30 ở góc đông-bắc mặt nước (đầu gần chợ), bờ cỏ hai đầu, dải taluy phía nam; ngữ cảnh trục tây + bùng binh đầu chợ nối liền phía đông, không khối nào đè/nuốt khu cũ.
- Diorama (từ tây-nam nhìn đông-bắc): mặt hồ nằm thấp hơn thềm bờ đúng bậc 0,6 (5,5/4,9), đảo đọc rõ giữa hồ phía gần chợ, taluy nam dốc lên sau hồ; tỉ lệ hồ/đảo/đường dạo cân với mẫu số quảng trường như §1 (bờ 100u, nước 128×80u).
- **VERDICT THẲNG:** ĐẠT phạm vi khung — vị trí/tỉ lệ/cao độ/đường đi/minimap đúng kế hoạch khóa, khu cũ nguyên vẹn theo số (0 điểm groundH lệch ngoài vùng hồ). Giới hạn đúng tính chất vòng khung: đáy hồ là nền tạm trung tính (chưa phải nước — XH-1), bờ đông hồ (dải x −224..−216) đang đè lên chân khối sườn nam cũ (khối nền (−175,3,62) vươn tới x −220) — giao thoa hình khối xử lý ở XH-1 cùng khối bờ; thềm cỏ phía bắc hồ còn trống (trang trí XH-1/XH-3); mép nam mặt đất tạm có khe sáng nhỏ dưới chân taluy khi nhìn tầm thấp (XH-1 làm bờ thật sẽ khép).
- Backup: index.html.bak-xh0-20261111 (build_models.py không đụng). Không đẩy GitHub, không upload link (theo brief). DỪNG — vòng sau là XH-1.

## XH-1 — 11/11/2026 (1 vòng: NƯỚC & BỜ hồ Xuân Hương — mặt nước thật + kè + lát đường dạo + bờ đông sạch + đập Ông Đạo) — **XONG, 8/8 CỔNG XANH**
### PHẠM VI (đúng KE_HOACH_HO_XUAN_HUONG §9 vòng XH-1 + §11)
Mặt nước hồ THẬT thay nền tạm XH-0, kè bờ bắc + tường chân nam/tây/đông, lát đường dạo hoàn thiện, xử lý giao thoa bờ đông, cầu Ông Đạo dạng đập đá (§11 S4), thông + villa mờ bờ nam (khối nền, chi tiết XH-3). CHƯA làm: model thuyền + Thủy Tạ (XH-2), đèn bướm/ghế/NPC/bến mở (XH-3 — solid kè giữ nguyên như XH-0, bến chưa mở), đạp vịt (XH-4), phản chiếu đêm/stamp (XH-5). Chỉ đụng index.html + scripts/render_xh1.py — không GLB, không build_models.py, KHÔNG sửa groundH/minimap/save.
### THAY ĐỔI (3 điểm chèn trong index.html)
- **Khối XH-1 thay khối đất tạm XH-0 (~dòng 1508):** lát đường dạo = texture canvas (ô 2u, accent #b98a7a, repeat 18×1 trên dải 144×8) + dải lát lối nối xoay tới (−232, 26); đáy hồ 0x14425c @4.82 (thay nền tạm 0x46545a @4.86); texture đá `keTex`/`keMat(rx)` (makeGroundTex + clone repeat như stoneMat); kè bắc 2 đoạn x −352..−251.2 và −248.8..−224 (chừa khe cầu đảo đúng solid XH-0) + bó vỉa sáng 0xd8d2c2; tường chân nam z 116, mép tây x −352, mép đông x −224; vèn kè đảo cyl(15.7, 16.6, 1.2) + vòng đường lát đảo RingGeometry(9.0, 13.8) @5.5; **cầu Ông Đạo**: thân đập đá + mặt đường + lan can cọc trắng tại x −353, z 60..96 + solid(−353, 78, 4.2, 18) (mép solid tới x −348.8, hơi vào vùng nước — XH-4 phải biết khi định biên thuyền); 10 cây thông silhouette (8 taluy/thềm nam, 2 bờ đông) qua helper `pine()`; 2 villa mờ thềm nam (−318,135) và (−262,136) + solid từng villa.
- **Đăng ký mặt nước (chèn ngay TRƯỚC khối đài phun V5.5 — bắt buộc vì WATER_FX/waterMats khai báo ~dòng 3481, SAU khối XH ~1508; đăng ký tại khối XH sẽ TDZ):** PlaneGeometry 128×80 tại (−288, 4.9, 76); canvas teal 0x276a8a + 64 vệt gợn #bfe6f5 (đúng hàm seed sin của WATER-1), repeat (24,15), opacity 0.93, roughness 0.15, emissive 0x1d4e5f; push vào WATER_FX.surfs (bob ±0.02, min 4.88 > đáy 4.82) + waterMats (đêm emissive ×0.55 qua applyDayNight — đúng idiom WATER-1).
- **Bờ đông xử lý sạch (hết giao thoa XH-0 ghi nợ):** khối sườn nam cũ box(90, 14, 55) @−175 → box(76, 14, 55) @−169 (mặt tây −220 → **−207**); dải cỏ bờ đông box(8) @−220 → box(17, 0.06, 80) @−215.5 (x −224..−207, chạm chân khối mới).
- **Lỗi bắt bằng render nghiệm thu (đã sửa + render lại):** nắp trụ vèn kè đảo ở y 5.52 che kín mặt đảo (đĩa cỏ 5.48 + vòng lát 5.50 nằm dưới nắp) — top-down lượt 1 hiện đảo phủ đá sọc ngang. Hạ tâm trụ 4.92 → **4.84** (nắp 5.44, dưới đĩa cỏ/vòng lát): top-down lượt 2 đảo đúng cấu trúc cỏ tâm + vòng lát + vành đá mỏng.
### KIỂM CHỨNG RIÊNG CỦA VÒNG
- **groundH không sửa** — tự kiểm chứng bằng script trích hàm từ backup vs bản mới: khu cũ lưới x −216..92 × z −88..50 = **10.850 điểm, 0 lệch**; 26 điểm mẫu khu hồ (spawn/lối nối/đường dạo 5,5; nước 4,9; đảo/cầu 5,5; taluy 5,5/7,25/9) **26/26 khớp**. Save chohb3d-v1 nguyên vẹn (SEED_SAVE sạch).
### BYTE
- index.html 576.484 → **584.661** (+8.177: khối bờ/nước/đập/villa/texture + comment sửa vèn đảo; cao hơn ước tính §9 +4–6KB — nêu thẳng). Standalone 4.893.500 → **4.901.677** (trần 10.485.760 — headroom ~5,58MB).
### CỔNG 8/8 XANH (chạy lại đủ trên bản cuối SAU sửa vèn đảo)
diag 900 sạch · SEED_SAVE 300 sạch · package + standalone diag 300 sạch (GAME_ROOT=/tmp/xh1/sa) · traffic **26/26** · audit **0 lỗi cứng / 0 nhảy lưới** (2 cảnh báo mềm wanderer#10 băng làn — có từ trước) · test_bd2 PASS · check_sweep3 PASS · test_real1 PASS.
### NGHIỆM THU (scripts/render_xh1.py — mô phỏng đúng thông số code: renders/xh1-topdown.png + xh1-day.png + xh1-prom.png + xh1-night.png + xh1-cmp.png)
- **ĐO tương phản (PIL median + luminance WCAG như research/27; hộp lấy theo lưới mẫu 100px, xác nhận đúng bề mặt theo chữ ký màu):** PROM tầm mắt người chơi — nước (119,139,161) vs lát bờ bắc (192,197,202): **CR = 2,02 ✓ đạt đích ≥2.0**. DAY diorama — nước (111,144,169) vs cỏ bờ nam (168,181,165): CR = 1,57 (chênh sáng thấp nhưng tách hẳn theo sắc xanh dương/xanh lá; harness AgX rửa sáng hơn game ACES — research/26 — KHÔNG đổi màu nước khỏi dải đo thật #12669d–#649abb/bộ WATER-1 chỉ để đạt số harness). ĐÊM — nước vs cỏ bờ nam **CR = 2,90 ✓**: mặt nước là mảng sáng nhất khung, KHÔNG chìm.
- **Tự soi:** nước đọc rõ là nước (teal + gợn trôi, phân biệt hẳn với lát/cỏ ở cả 3 góc); kè bắc + bó vỉa sạch, khe cầu đúng chỗ; bờ đông hết đè khối (cỏ liền từ mép nước tới chân sườn đã lùi); đảo đúng cấu trúc sau sửa nắp; đập Ông Đạo đọc như bệ đá ở mép tây; đêm đảo còn tối (nhà + đèn là XH-2/XH-3), tiền cảnh prom bị 1 ô accent choán lớn — thuần vị trí camera harness, không phải lỗi bề mặt.
- **Đối chiếu ảnh thật:** renders/xh1-cmp.png = render prom cạnh ảnh thật theme/xuan-huong/03-duong-dao-ven-ho.jpg — cùng cấu trúc lát sáng + ô accent hồng nâu + bó vỉa trắng + mặt nước teal gợn; game không có lan can xanh/dãy cây sát mép như ảnh (lan can + trang trí bờ thuộc XH-3).
- **VERDICT THẲNG:** ĐẠT phạm vi XH-1 — nước thật đúng idiom WATER-1 (ngày đọc rõ CR 2,02 ở tầm người chơi; đêm không chìm CR 2,90), bờ/kè/đập/đảo đúng khung khóa XH-0, bờ đông sạch, khu cũ 0 lệch theo số. Giới hạn: tương phản luminance nước/cỏ ngày ở góc diorama xa = 1,57 (dưới đích 2.0 — cặp bề mặt chính nước/lát đạt); render là mô phỏng Blender (thông harness gần đúng bằng nón/trụ, không nạp GLB) — hình cuối chờ Chung Hy chơi thử; người chơi bước khỏi mép đảo (r>15) rơi về cao độ nước 4,9 và đi được trên mặt nước (tính chất khung groundH XH-0 — luật đi lại trên nước thuộc XH-4 khi có thuyền).
- Backup: index.html.bak-xh1-20261111 (build_models.py không đụng). Không đẩy GitHub, không upload link (theo brief). DỪNG — vòng sau là XH-2.

## XH-1.5 — 11/11/2026 (1 vòng: RESCALE mặt nước hồ Xuân Hương — phản hồi Chung Hy 20:30 11/11 "nhỏ xíu, không giống thật") — **XONG, 8/8 CỔNG XANH**
### LÝ DO + PHẠM VI
Chung Hy xem khung XH-0/XH-1 (nước 128×80) và chê "nhỏ xíu, không giống thật chút nào" → vòng này CHỈ mở rộng mặt nước + bờ xa theo số khóa của brief, giữ nguyên mọi số XH-0/XH-1 còn lại (bờ 5,5 / nước 4,9; đảo Thủy Tạ R15 (−250,58) + dải cầu; kè bắc + solid; lát đường dạo). Chỉ đụng index.html + harness scripts/render_xh15.py — không GLB, không build_models.py, không sửa save.
### SỐ KHÓA MỚI (thay khung nước XH-0/XH-1)
- **Mặt nước: x −560..−224 (dài 336), z 36..196 (rộng 160), tâm (−392, 4.9, 116)** — gấp 4,2 lần diện tích (10.240 → 53.760u²). Đáy hồ 0x14425c cùng phạm vi @4.82. Texture gợn WATER-1 giữ nguyên, repeat (24,15) → **(63,30)** — tile vẫn ~5,33u như cũ. Đăng ký WATER_FX/waterMats như XH-1 (khối riêng trước đài phun, tránh TDZ).
- **Cầu Ông Đạo: DỜI x −353 (z 60..96) → x −557, z 60..130** (thân đập 8×1,9×70 + mặt đường + cọc lan can −553.3); **solid(−353, 78, 4.2, 18) của XH-1 THAY BẰNG solid(−557, 95, 4.2, 35)** — ghi chú cũ "mép solid tới −348.8 hơi vào vùng nước" hết hiệu lực; biên tây vùng thuyền cho XH-4 nay là x −560.
- **Bờ nam XA (nền cảnh):** taluy z 196..224 dốc 5,5 → 9 (hộp 344×28,4 tại (−390, 7.22, 210), rot.x −0.1244 khớp groundH 3,5/28) + thềm sau = 9 (z 224..234); tường chân kè tại z 196 (thay tường z 116 của XH-1 — nay nằm giữa mặt nước, đã gỡ); **24 thông silhouette** dọc bờ (21 taluy z 206..218 + 3 thềm z 227..228, y theo groundH qua pine()) + **4 villa mờ** trên thềm (−505,228), (−430,229), (−352,228), (−272,229) + solid từng villa (XH-1: 2 villa ở z 135/136 — nay giữa nước, đã dời; 8 thông taluy cũ z 122..131 cũng đã gỡ vì đứng giữa nước).
- **Bờ tây:** dải nền cỏ x −572..−560, z 36..196 (12×160 @5.45) + vèn kè đá x −560 hai đoạn z 36..60 và z 130..196 (đoạn giữa là đập). Tường _keW cũ tại −352 đã gỡ.
- **Bờ đông:** tường mép nước x −224 kéo dài 80 → 160 (z 36..196, keMat 40); dải cỏ bờ đông giữ nguyên XH-1.
- **groundH:** nhánh hồ mở z tới 232: nước x −560..−224, z 36..196 = 4,9 (trừ đảo/cầu như cũ); taluy nam xa z 196..224 → 9; taluy XH-0 (z 116..132 → 9) giữ nguyên cho dải x ngoài vùng nước mới.
- **minimap:** khung mới **x −568..92 (660u), z −88..228 (316u)** — mmX = (x+568)/660×156, mmY = (z+88)/316×156; mọi rect vẽ tay đổi hệ số /452,/220 → /660,/316; vẽ lại: hồ (−560,36, 336×160), đảo R15 = 3,5px, đường dạo (−360,27, 144×9), thêm dải bờ nam xa + dải bờ tây.
- **detectZone:** vùng nước → x −560..−224, z 36..196 vẫn nhãn "Hồ Xuân Hương"; thêm nhãn "Bờ nam hồ Xuân Hương" cho x ≤ −208, z 196..232 (tránh rơi nhãn sai ở dải nền mới).
### ĐO FOG / CAMERA (bắt buộc theo brief — số đọc từ code, không đoán)
- **camera.far = 600** (PerspectiveCamera dòng 338). Khoảng cách lớn nhất cần thấy: spawn (−206, 5.6) → góc tây-nam (−560, 196) = **402u < 600** ✓ không cắt.
- **FogExp2:** fogBase ngày **0,0035** / đêm **0,0032** (applyDayNight) + fogHourBonus (19h +0,0012; 22h +0,0022) → mật độ hiệu dụng ngày 0,0035 · 19h **0,0044** · 22h 0,0054 (nhiệt 18° chưa cộng bonus lạnh). Truyền qua T = exp(−(ρd)²): bờ bắc (−288,32) → bờ nam xa (−392,210) d=206u: **T = 0,59 ngày / 0,44 lúc 19h / 0,29 lúc 22h**; cuối đường dạo tây (−338,30) → đập (−557,95) d=228u: **0,53 / 0,36 / 0,22**. → Bờ xa + đập HIỆN rõ dạng silhouette mờ ở mọi giờ chơi thường (mặc định 19h: 0,36–0,44) — **KHÔNG cần chỉnh fog/far** (số trước = sau, giữ nguyên bản XH-1).
### KIỂM CHỨNG RIÊNG CỦA VÒNG
- **groundH lưới diff** (trích hàm từ backup XH-1 vs bản mới, lưới bước 1 toàn khung x −580..92 × z −88..232 = **216.033 điểm**): **0 điểm lệch NGOÀI vùng mở rộng** — mọi điểm lệch đều nằm trong {x<−208, z≥116} ∪ {x<−352, 36≤z≤116}; **21/21 điểm mẫu** khớp số khóa (nước mới 4,9 tại (−400,76)/(−555,100)/(−288,150); taluy xa (−288,210)=7,25, (−288,224)=9; đảo/cầu/bờ bắc giữ 5,5; taluy cũ (−215,124)=7,25 giữ nguyên). Tuyến spawn → đường dạo và bờ → cầu → đảo: nhảy tối đa **0,000**. Save chohb3d-v1 nguyên vẹn (SEED_SAVE sạch).
- **Nợ cũ cập nhật:** diện tích "đi được trên mặt nước" (tính chất groundH từ XH-0) tăng theo khung mới (nước nay 53.760u²) — luật đi lại trên mặt nước vẫn thuộc **XH-4** như đã ghi; XH-4 nay định biên thuyền theo khung mới: bắc = kè z 36, đông x −224, **tây x −560 (đập tại −557)**, nam z 196.
### BYTE
- index.html 584.661 → **587.485** (+2.824). Standalone 4.901.677 → **4.904.501** (trần 10.485.760 — headroom ~5,58MB).
### CỔNG 8/8 XANH (trên bản cuối)
diag 900 sạch · SEED_SAVE 300 sạch · package + standalone diag 300 sạch (GAME_ROOT=/tmp/xh15/sa) · traffic **26/26** · audit **0 lỗi cứng / 0 nhảy lưới** (cảnh báo mềm wanderer băng làn — có từ trước, như XH-1) · test_bd2 PASS · check_sweep3 PASS · test_real1 PASS.
### NGHIỆM THU (scripts/render_xh15.py — mô phỏng đúng thông số code: renders/xh15-topdown.png + xh15-dia.png + xh15-prom-day.png + xh15-prom-night.png)
- **Top-down:** khung khớp số khóa — mặt nước 336×160, đảo Ø30 giữ đúng góc đông-bắc (không lệch vị trí tương đối), cầu nối nguyên, đập nằm đúng đầu tây z 60..130, hàng thông + 4 villa dọc bờ nam xa, dải bờ tây sau đập.
- **PROM ngày (đứng (−288, 32) nhìn tây-nam — ảnh quyết định "hồ hay ao"):** mặt nước mở liên tục tới bờ nam xa có hàng thông + villa, không còn thấy "đáy khung" như XH-0/XH-1; cảm giác đã là HỒ so với bản 128×80.
- **ĐO tương phản (PIL median + WCAG, hộp mẫu xác nhận chữ ký màu như XH-1):** PROM ngày — nước (142,162,179) vs lát bờ (192,197,202): **CR = 1,52**; nước vs tán thông bờ xa (101,130,116): **CR = 1,59**; nước vs cỏ taluy (170,183,168): CR = 1,26 — **DƯỚI đích brief (≥2,0 / ≥1,8), nêu thẳng.** Nguyên nhân đo được: góc nhìn prom mới lướt mặt nước 160–200u → phản xạ trời fresnel (roughness 0,15) làm nước sáng lên; số XH-1 (2,02) đo ở góc dốc gần bờ. PROM **đêm: nước (67,114,127) vs bờ xa (29,41,37) CR = 2,83 ✓** — nước là mảng sáng nhất khung, bờ xa đọc silhouette rõ. Diorama ngày: nước vs cỏ CR = 1,56 ≈ XH-1 (1,57) — quan hệ sáng này là tính chất của bảng màu WATER-1 đã khóa, không đổi theo rescale; tách biệt theo SẮC (xanh dương/xanh lá/trung tính) rõ ở cả 3 góc. Không tự ý đổi màu nước khỏi dải đo thật/WATER-1 chỉ để đạt số harness (đúng tiền lệ XH-1).
- **Tự soi:** nước mở tới bờ xa ✓; đập đúng đầu tây ✓ (thấy dạng vệt xám ở cuối tây trong prom + rõ ở top-down/diorama); đảo không lệch ✓; tiền cảnh prom ngày bị 1 ô accent lát choán lớn — vị trí camera harness (như XH-1 đã ghi), không phải lỗi bề mặt; harness không mô phỏng FogExp2 — độ mờ bờ xa trong game thật theo số đo fog ở trên (silhouette mờ hơn render harness một chút, đúng chất hồ thật).
- **VERDICT THẲNG:** ĐẠT phạm vi RESCALE — tỉ lệ hồ đã đúng cảm giác "hồ" (nước gấp 4,2 lần, bờ xa có hàng thông/villa, đập ở đầu tây), khung cũ giữ nguyên từng số (0 lệch groundH ngoài vùng mở rộng), 8/8 cổng xanh. Giới hạn: tương phản luminance NGÀY ở góc prom dưới đích số brief (1,52/1,59 — lý do góc lướt + fresnel, đã phân tích ở trên; đêm đạt 2,83); hình cuối vẫn chờ Chung Hy chơi thử.
- Backup: index.html.bak-xhscale-20261111. Không đẩy GitHub, không upload link (theo brief). DỪNG — vòng sau là XH-2.

## XH-2 — 11/11/2026 (1 vòng: MODEL Blender hồ Xuân Hương — SwanBoat ×2 bản sơn + Thủy Tạ + cầu đảo + cây đảo chuẩn mới) — **XONG, 8/8 CỔNG XANH**
### PHẠM VI (đúng KE_HOACH §6 + §9 vòng XH-2 + §11 S1/S6 + bổ sung Chung Hy 21:32 11/11)
Thêm `build_lake()` vào scripts/build_models.py → **lake.glb** (7 root: SwanBoat, SwanBoatPattern, ThuyTa, CherryTree, IslandBridge, PineUmbrella, Willow) → quantize → đăng ký loader + đặt trong index.html. CHƯA làm: trang trí bờ/ki-ốt/ghế/đèn/NPC (XH-3), cơ chế đạp vịt (XH-4 — vòng này chỉ neo tĩnh + để sẵn node), stamp/photo (XH-5). Không sửa groundH/solid/save (hàm groundH giống hệt bản XH-1.5 theo diff nguyên văn — khu cũ 0 lệch theo cấu trúc).
### MODEL — số đo từ ảnh thật (không dựng mẫu chung; grounding đo bbox trên ảnh 10 + 37)
- **SwanBoat** (mặt tiền −Y như character; origin tại mặt nước, game đặt y = 4,9): thân loft 9 tiết diện 2,19 × 1,66 (spec 2,2 × 1,6), draft 0,25, boong mũi/đuôi, lòng khoang trắng FRP, 2 băng ghế + bàn đạp; **cổ loft đường chữ S đo lại theo ảnh 10/06** (dưới ngả sau → trên trả về trước; bản đầu phình trước ở giữa đã sửa); đầu + mỏ vàng cam cụp nhẹ + mào đỏ 3 núm + mắt chấm; mái phẳng 4 cột — **đỉnh mái = 0,90 chiều cao tới mào (đo ảnh 10: 0,88)**; phao cam #e8a33d bên hông. Cổ từng hở seam (vệt tối ở render lượt 1) → khép vòng điểm cuối = điểm đầu, render lại sạch.
- **2 bản sơn:** (a) trắng cổ điển — thân #e0dfe2, mái trắng, ghế xanh lá (ảnh 10), cánh sơn teal nổi 2 bên hông (ảnh 06); (b) **SwanBoatPattern** — mái #7edcfc + ghế #fc508f (đo PIL §11.3), thân gắn **texture canvas hoa văn lúc chạy** (chấm + hoa 5 cánh như ảnh 23) qua vật liệu tên "SwanPattern" (GLB giữ UV). **ĐÃ ĐỔI KỸ THUẬT so với dự định nhúng ảnh vào GLB:** ảnh nhúng làm diag vỡ (`GLTFParser.loadImageSource: self is not defined` — lake là GLB đầu tiên có texture; trình duyệt thật không lỗi nhưng cổng diag là luật) → chuyển sang idiom canvas runtime sẵn có của game (như WATER-1/FRONTAGE-1), harness render cũng gắn texture tương đương để nghiệm thu đúng hình người chơi thấy.
- **ThuyTa** tại mép tây đảo (−262, 5.47, 58), rotY −90° (boong hướng −X ra hồ, cửa sau hướng tâm đảo): thân trắng #f2f0eb 9,6 × 5,6 × 2 tầng + dải kính tối, boong 10,8 × 7,4 + lan can trắng quây 3 mặt hồ, cột đỡ tầng trên, **mái 2 tầng profile LÕM kiểu chùa** (loft vòng chữ nhật: thoải ở hiên → dựng dần lên đỉnh + đầu góc vênh; thay pyramid thẳng sau khi đo ảnh 37), cột biển xanh #0268d0 + biển (chưa chữ — chữ thuộc XH-3 biển hiệu). **Tỉ lệ ngang/cao: đo ảnh 37 = 1,69 (từ mặt nước); model = 10,8 / (5,45 + 0,6 đảo trên mặt nước) = 1,79** (boong đã thu 11,5 → 10,8 theo số đo; lệch ~6% do giữ spec khóa §11.5 tường 10 × 6 × 5,5).
- **IslandBridge**: deck 2,5 × 7 (mặt deck = 5,50 đúng groundH) + lan can trắng 2 bên phủ dải cầu XH-0; **hạ dải lát tạm XH-0 (5,46 → 5,30)** làm nền dưới deck tránh z-fight (tiền lệ XH-1 thay nền tạm XH-0).
- **Cây đảo — áp điểm 2 của lệnh 21:32 (thông tán Ô):** dựng mới **PineUmbrella** (thân cao thẳng 5,2 + 3 đĩa tán DẸT phân tầng Ø4,5/3,4/2,4 — đúng dáng thông Đà Lạt) đặt trên bãi cỏ trong vòng đường (−244,5, 62,5) + **Willow** (vòm + tua rũ) ×2 ôm 2 bên nhà (−262,5; z 50,5/65,5). Đã kiểm chứng pine.glb cũ = **thông nón 4 tầng thân ngắn** (render /tmp/pinecheck-34) — vòng này KHÔNG đặt pine nón ở đảo/bờ; pine nón chỉ còn ở silhouette bờ nam xa (XH-1.5, ~200u — đúng ngoại lệ "silhouette rất xa" của lệnh) và toàn khu cũ (thay pine.glb toàn bản đồ = việc riêng ngoài phạm vi XH-2, đề xuất vòng riêng).
- **CherryTree** (tán cầu hồng 2 tông) đã dựng trong lake.glb theo §6 — **chưa đặt** (đặt ở XH-3 cùng trang trí bờ như kế hoạch §9).
- **Đặt thuyền 10 chiếc tĩnh:** 7 cung nam đảo (r 18,6–19,3, mũi hướng tâm đảo như ảnh 22/38; 3 hoa văn + 4 trắng) + bến bắc: hoa văn (−272, 39,5), trắng (−241, 39,5) + **SwanBoatPlayer trắng tại (−259, 39,3)** — node riêng tên rõ + registry `LAKE_BOATS`/`LAKE_PLAYER_BOAT` khai ngoài khối cho XH-4. **Áp điểm 3 của lệnh 21:32:** vòng đường đảo giữ trống để đi quanh nhà (cây đặt trong bãi cỏ/sát vành, không chắn vòng lát), luồng cầu x −250 z 36..43 trống hoàn toàn (thuyền bến bắc lệch ±9u khỏi trục cầu).
### BYTE
- lake.glb: thô 683.336 → **quantize 375.432 (−45,1%)** (lớn hơn ước tính §6 80–150KB — model chi tiết hơn dự tính: 2 thuyền đầy đủ + nhà 7 cụm + 3 cây; bản gốc giữ ở assets/lake.glb.bak-quantize-20261111). index.html 587.485 → **592.239** (+4.754: loader + clampSat + khối XH-2 + canvas hoa văn). Standalone 4.904.501 → **5.409.873** (trần 10.485.760 — headroom ~5,08MB).
### CỔNG 8/8 XANH (trên bản cuối — sau sửa seam cổ, chạy lại đủ bộ)
diag 900 sạch · SEED_SAVE 300 sạch · package + standalone diag 300 sạch (GAME_ROOT=/tmp/xh2/sa) · traffic **26/26** · audit **0 lỗi cứng / 0 nhảy lưới** (cảnh báo mềm wanderer băng làn — có từ trước) · test_bd2 PASS · check_sweep3 PASS · test_real1 PASS.
### NGHIỆM THU (scripts/render_xh2.py — nạp lake.glb THẬT bản quantized, Cycles + OIDN + ACES 1.3: renders/xh2-boat.png + xh2-boat-cmp.png + xh2-island-day.png + xh2-island-dusk.png + xh2-island-sw.png)
- **Cận thuyền (xh2-boat + cmp cạnh ảnh thật 35):** cổ chữ S liền mạch, mào đỏ/mắt/mỏ đọc rõ, mái xanh + ghế hồng + hoa văn thân đúng bộ màu ảnh 23; tỉ lệ mái/mào khớp số đo ảnh 10. (Ảnh 35 là Thủy Tạ bình minh — đối chiếu đúng chủ thể hơn ở cặp island-dusk; vẫn ghép theo đúng brief.)
- **Đảo ngày/tây-nam:** nhà đúng dáng Thủy Tạ (trắng, 2 tầng mái lõm, boong lan can nhô mặt hồ, cột biển xanh), cầu thẳng có lan can, cung thuyền nam ôm đảo như flycam 22/38, thông tán ô + liễu đúng chuẩn mới, vòng đường đảo thông thoáng.
- **Chạng vạng 19h:** nắng thấp ấm quệt ngang, nhà + thông đọc silhouette rõ; đèn đảo/bến là XH-3 (đảo đêm còn tối như đã ghi từ XH-1).
- **Tự soi thẳng:** mái nhà còn hơi "bẹt" so với ảnh (profile lõm đã có nhưng biên độ cong nhỏ ở tỉ lệ chibi); mỏ thiên nga hơi ngắn; thuyền neo chưa có phao/dây neo (XH-3/XH-4); nhà chưa có solid (đi xuyên được — brief vòng này khóa "chỉ thêm hình", solid nhà/cây để vòng sau như solid ki-ốt ở §7).
- **VERDICT THẲNG:** ĐẠT phạm vi XH-2 — model đo từ ảnh thật (có số grounding), đủ 3 điểm bổ sung 21:32 (đo ảnh + thông tán ô + giữ vòng đường/luồng cầu), 8/8 cổng xanh, byte an toàn. Hình cuối vẫn chờ Chung Hy chơi thử.
- Backup: index.html.bak-xh2-20261111 + scripts/build_models.py.bak-xh2-20261111. Không đẩy GitHub, không upload link (theo brief). DỪNG — vòng sau là XH-3.

## XH-3+ — 11/11/2026 (1 vòng: HỒ SỐNG DẬY — sửa đầu thiên nga XH-2.1 + trang trí bờ + SINH HOẠT quanh hồ + SƯƠNG LẠNH, theo KE_HOACH_SONG_QUANH_HO.md) — **XONG, 8/8 CỔNG XANH**
### PHẠM VI
Đúng brief vòng: (0) XH-2.1 sửa đầu thiên nga trong build_lake(); (1) trang trí bờ §7/§8/§11 S2/S3/S7 + mở khe bến + cầu bến; (2) sinh hoạt quanh hồ phần A bằng hệ NPC/sit/đèn SẴN CÓ; (3) sương lạnh phần B + thông tán ô thay nón phần C; (4) trả nợ solid XH-2. CHƯA làm: đạp vịt (XH-4), stamp/photo/phản chiếu (XH-5), nội thất chợ + bậc tam cấp (REALISM-INT-1/STAIR-1).
### ⚠️ PHÁT HIỆN LỚN NGOÀI KẾ HOẠCH — collide() KẸP NGƯỜI CHƠI Ở BẢN ĐỒ CŨ
`collide()` còn giữ biên thời V4 `clamp(px, -74, 74); clamp(pz, -80, 36)` trong khi spawn ở x −206 → **người chơi bị kéo về −74 ngay bước đi đầu tiên; toàn bộ trục tây + khu hồ KHÔNG tới được bằng đi bộ ở mọi bản từ trước tới nay** (các vòng XH-0→2 chỉ đo groundH nên không bắt được; đã kiểm chứng clamp này có ở mọi backup kể cả premerge 10/11). Đã nới theo khung minimap XH-1.5: `clamp(px, -566, 90); clamp(pz, -86, 226)` + comment ghi rõ trong code. **Cần Chung Hy chơi thử xác nhận đi bộ tới được hồ** — đây là sửa hành vi lớn nhất của vòng.
### XH-2.1 ĐẦU THIÊN NGA (đo từ ảnh thật 10/06 + verdict "đọc như gà" của Chung Hy)
Bỏ 3 núm mào đỏ; mỏ mới cyl r 0,014→0,082 dài 0,46 (phần thấy ~0,35 ≈ 1,4× đường kính đầu 0,24 — dải thiên nga câm thật 1,2–1,5×; bản cũ ~0,17), rotX 123,5° cụp xuống-trước ~34°, scale (1.10, 0.85, 1.0); thêm **núm đen thiên nga câm** r 0,052 trên gốc mỏ + chót mỏ đen r 0,021. **Nói thẳng:** ảnh thật 10 cho thấy thuyền thật CÓ mào đỏ nhỏ + mỏ vàng ngắn — hướng bỏ mào/mỏ dài là theo lệnh brief + verdict của Chung Hy (bản XH-2 đọc như gà thật ở góc render); đầu mới đọc ra thiên nga rõ (xem xh3-boat-head-cmp.png), đổi lại kém giống chi tiết thuyền thật ở đúng 2 điểm đó. lake.glb build lại + quantize riêng lake (validate đạt) = **373.216 byte** (XH-2: 375.432); các GLB khác không đụng (DRY_RUN quantize toàn bộ cho Δ ≈ 0).
### TRANG TRÍ BỜ (toàn bộ là code trong block XH-3+ cuối index.html, đặt trước animate để tránh TDZ với SIT_SPOTS)
- **Đèn BƯỚM ×7** bờ bắc z 27,4 nhịp 18u (x −346..−238): cột #1e4d2e h 3,2 + 2 cánh ellipse + panel phát sáng + đĩa huy hiệu — nối hệ đèn sẵn có (lampGlows/lampLights, PointLight cho đèn chẵn, tự set intensity theo isNight lúc dựng vì applyDayNight init chạy trước block).
- **Ghế bê tông 2 tấm ×10** (kem #e8e2d4/chân #4a423a) trên dải cỏ mép nước mới (x −352..−224, z 34,5..35,8, đỉnh 5,525): 8 ghế bờ bắc nhịp 12u + 2 ghế đảo; toán ngồi khớp ghế STAIR_SITTERS (đỉnh ghế = groundH + 0,32 ≈ origin người ngồi + 0,30); 2 ghế đăng ký SIT_SPOTS `lake:true` (−310, −238) + toast ngồi riêng "gió hồ lạnh tê, sương đang lên".
- **Ki-ốt vé** đầu cầu đảo (−254,8; 30,5): quầy + mái + 3 áo phao cam + biển "THUÊ THUYỀN THIÊN NGA" + biển giá "30 XU/5 PHÚT" (khớp giá §4.3 cho XH-4) + NPC bán vé (static 'chat'). **Biển NHIỆT ĐỘ** (phần B3): canvas tự vẽ lại khi giờ game đổi nhiệt độ nguyên — nội suy tuyến tính qua 9 mốc giờ Đà Lạt (13°C lúc 0h → 21,5°C lúc 14h → 16°C lúc 19h mặc định).
- **Mở khe bến §7**: kè mesh + solid tách tại x −266..−252; **cầu bến gỗ** 14×6 đỉnh đúng 5,5 (groundH có nhánh sàn riêng) + lan can trắng 2 bên (solid) + biển "BẾN THUYỀN THIÊN NGA" + biển chỉ dẫn ở lối nối (−225, 20). Đầu z 42 để mở cho XH-4 lên thuyền.
- **Cầu ngắm chữ Y ×2** (S7, cx −282/−318): thân gỗ kéo tới z 42,4 + 2 cánh chéo ±0,62 rad; **groundH kiểm tra ĐÚNG hình học rect xoay** — bản nháp đầu (xấp xỉ tuyến tính) để hở khe ở góc cánh làm NPC sụt 0,6u, bắt được bằng kiểm chứng số (9.076 điểm mẫu dọc mọi tuyến NPC: bản cuối **0 điểm lệch, maxJump 0**). Cánh không lan can/solid — ghi nợ cùng luật mặt nước XH-4.
- **Bollard ×7** (4 quanh đầu cầu đảo + 3 vòng đảo), **thông tán ô bờ bắc ×9** (clone PineUmbrella, gốc quét vôi trắng 0,8u) + thông bờ nam xa 24 cây XH-1 đổi nón → tán ô + 2 cặp bờ đông (phần C), **CherryTree ×2** đầu cầu đảo, **liễu ×2** sát mép nước 2 bên cầu đảo/bến.
- **Nợ XH-2 đã trả:** solid nhà Thủy Tạ (−262, 58, 3.7×5.4) + thông đảo + 2 liễu đảo — hết đi xuyên.
### SINH HOẠT (phần A — tái dùng wanderer/statics/sit, KHÔNG chế hệ mới; mọi NPC hồ mặc áo ấm + khăn/beanie qua lakePerson())
- **23 wanderer mới:** 8 người đi bộ lẻ (2 chiều đường dạo + vòng đảo, dừng ngắm 5–10s nhờ `lakeLong` mới trong tick + toast), 2 người chạy bộ (rank 0,58–0,62 → chỉ hiện giờ đông: sáng sớm + cao điểm tối), **4 cặp tình nhân đi đôi** (route lệch ngang ±0,35, đồng tốc 1,02, partner-sync mới trong tick: 1 người dừng ngắm thì người kia dừng cùng điểm) + **2 cặp ngồi ghế đá**, **5 xe đạp** làn ngoài 2 chiều (model xe chibi dựng bằng code: 2 vành torus + khung + yên + ghi đông; người đạp = lakePerson gắn nhóm, tick swingLimbs đạp chân), 2 người chụp ảnh giơ điện thoại (đầu cầu đảo + đầu cầu Y −318), 1 người bán vé.
- Mật độ theo giờ qua rank/crowdLevel sẵn có: 19:00 mặc định (mức 1,0) = đủ 23 + tĩnh; trưa 0,45 thưa hẳn; khuya 0,55.
### SƯƠNG LẠNH (phần B)
5 lớp plane alpha gradient (canvas radial) trôi chậm trên mặt nước (biên trôi ±7/±4u), opacity theo giờ game: 5–8h **0,30** (đậm nhất) → trưa 0,05 → 18–22h 0,20 → khuya 0,24. Bờ nam xa giữ scene fog sẵn có (B4 — kiểm chứng bằng render: silhouette mờ dần đúng chất hồ). tick qua `window.__tickXH3` gọi sau tickWater.
### BYTE
- index.html 592.239 → **616.662** (+24.423: block XH-3+ + sửa tick/groundH/collide/kè). lake.glb 375.432 → **373.216**. Standalone 5.409.873 → **5.431.344** (trần 10.485.760 — headroom ~5,05MB).
### CỔNG 8/8 XANH (trên bản cuối)
diag 900 sạch · SEED_SAVE 300 sạch · package + standalone diag 300 sạch (GAME_ROOT=/tmp/xh3_sa) · traffic **26/26** · audit **0 lỗi cứng / 0 nhảy lưới** (60 tuyến wanderer; cảnh báo mềm băng làn có từ trước) · test_bd2 PASS · check_sweep3 PASS (wandererYBad 0) · test_real1 PASS. **Thêm ngoài chuẩn:** diag 3600 frame sạch (ép nhánh browse/partner-sync/sương/nhiệt độ chạy đủ lâu) + kiểm chứng số tuyến NPC hồ 9.076 điểm mẫu = 5,5 toàn bộ (0 điểm trên mặt nước).
### NGHIỆM THU (scripts/render_xh3.py — nạp lake.glb + character.glb THẬT, mô phỏng đúng thông số code cho phần code-built, ACES + OIDN: renders/xh3-boat-head.png + xh3-boat-head-cmp.png + xh3-prom-night.png + xh3-dawn.png)
- **Đầu thuyền:** hết mào gà — mỏ cam dài cụp + núm đen đọc ra thiên nga câm ngay; cmp cạnh ảnh thật 10 cho thấy khác biệt chủ đích đã ghi ở trên.
- **Đường dạo 19:00:** đèn bướm sáng dọc bờ, ghế bên mép nước, cặp đôi + người đi bộ + người đạp xe trên đường dạo, thông tán ô dọc bờ — bờ hồ có người, có sinh hoạt.
- **Sáng sớm:** đường dạo có người chạy bộ + người đi bộ, đảo/Thủy Tạ + cầu đảo bên trái, thuyền neo ở bến, thông tán ô + phượng tím dọc bờ; sương đọc thành dải mờ nhẹ trên mặt nước — trong harness bị nhạt đi vì nước sáng + nắng sớm (opacity giữ đúng số code 0,30; game thật nước tối hơn + FogExp2 chồng thêm nên sương sẽ rõ hơn render).
- **Tự soi thẳng (3 câu của Chung Hy):** *Giống thật chưa* — cấu trúc bờ (đèn bướm/ghế/ki-ốt/cầu Y/thông tán ô) đúng các chi tiết đặc trưng đã đo; đầu thuyền đổi sang thiên nga câm là khác thuyền thật có chủ đích (đã ghi). *Lạnh chưa* — có đủ 3 lớp dấu hiệu: sương mặt hồ theo giờ + biển nhiệt độ 16°C buổi tối + 100% NPC hồ mặc áo ấm/khăn/mũ len; harness không mô phỏng FogExp2 nên sương trong game thật sẽ dày hơn render. *Sống chưa* — 23 NPC động + 7 tĩnh quanh hồ, cặp đôi dừng ngắm cùng nhau; harness render người ở pose đứng yên (không pose đi/đạp) — chuyển động thật kiểm chứng bằng diag 3600 + chờ Chung Hy chơi thử.
- **Điểm chưa đạt nói thẳng:** toast khi KẾT THÚC buổi ngồi (tickSit) vẫn là câu ăn uống chung — chỉ startSit có nhánh hồ; cánh cầu Y chưa có lan can (chủ đích, chờ luật mặt nước XH-4); người chơi vẫn đi được trên mặt nước ngoài vùng sàn (luật XH-4); cặp đôi có thể chạm nhau thoáng chốc ở đầu quay ping-pong (lực tách người xử lý, chưa thấy lỗi ở diag).
- Backup: index.html.bak-xh3-20261111 + scripts/build_models.py.bak-xh3-20261111 + assets/lake.glb.bak-xh2raw-20261111. Không đẩy GitHub, không upload link (theo brief). DỪNG — vòng sau là XH-4 (đạp vịt).

## XH-3R — 11/11/2026 (1 vòng: LÀM LẠI TỈ LỆ HỒ XUÂN HƯƠNG — trọng tâm CHIỀU CAO Z) — theo lệnh Chung Hy 23:52 11/11: "làm quá ẩu, làm lại; con đường gì nhỏ xíu; bạn hiểu X Y nhưng chiều cao Z bạn không hiểu"
### BƯỚC 0 — DỌN TRẠNG THÁI VÒNG XH-3+ BỊ HỦY (diff bằng file thật, không đoán)
Vòng XH-3+ (mục ngay trên) đã ghi gần trọn tính năng rồi bị hủy — hồ sơ "XONG" của nó KHÔNG còn đúng với code sau vòng này; XH-3R xử lý như sau:
- **index.html: REVERT toàn bộ về .bak-xh3-20261111 (trạng thái cuối XH-2)** — gỡ hết phần XH-3+ nửa vời: groundH sàn cầu bến + cầu chữ Y, kè cắt khe bến, solid bến/cầu Y, ghế/lamp bướm/bollard/ki-ốt/biển nhiệt độ, thông tán ô bờ bắc + bờ nam, sương mặt hồ, NPC sinh hoạt hồ, toast hồ, tick __tickXH3. (XH-3+ sẽ làm lại ở vòng riêng sau khi tỉ lệ chuẩn.)
- **GIỮ 1 sửa lỗi hoàn chỉnh, độc lập của vòng hủy — clamp người chơi trong collide():** bản XH-2 kẹp px∈[−74,74], pz∈[−80,36] (biên thời V4) mà collide() áp lên playerState MỖI frame; spawn ở (−206, 5,6) và toàn bộ trục tây + hồ nằm NGOÀI kẹp → người chơi bước là bị kéo về −74, KHÔNG BAO GIỜ tới được hồ (các vòng XH trước chỉ đo groundH nên không bắt được). Giữ số của vòng hủy: clamp (−566..90, −86..226) = khung minimap XH-1.5 lui 2u. Bỏ nó đi = cố ý ship lại lỗi chặn hồ.
- **scripts/build_models.py: GIỮ NGUYÊN** — diff vs .bak-xh3 chỉ đúng 1 chỗ: sửa đầu thiên nga XH-2.1 (bỏ 3 núm mào đỏ; mỏ cam dài 0,46 cúi ~34° + núm đen gốc mỏ + chót mỏ đen — thiên nga câm, đo ảnh 10/06). Không lẫn tính năng nào khác.
- **assets/lake.glb: GIỮ NGUYÊN** (373.216 byte) — kiểm chứng bằng render renders/xh3-boat-head.png của vòng hủy: đầu thuyền trong GLB hiện tại đã hết mào đỏ, mỏ dài + núm đen khớp source. (Số 375.432 ở brief là byte bản XH-2 trước sửa đầu; bản sau sửa nhỏ hơn 2.216 byte — khớp việc gỡ mào + thay mỏ.)
- Trạng thái trước XH-3R (gồm cả rác vòng hủy) đã lưu: index.html.bak-xh3r-20261111 + build_models.py.bak-xh3r-20261111.

### BƯỚC 1 — BẢNG TỈ LỆ CHIỀU CAO (đo TRƯỚC khi sửa; ghi tại đây rồi mới thi công)
**Mỏ neo game (ĐO, không giả định):** character.glb bbox bằng GLTFLoader (node, three r160): cao tổng 1,99u gồm mũ; **đỉnh đầu (không mũ) = 1,82u** — lấy **H = 1,82u** làm "1 người" (makePerson scale 1, player/NPC đều vậy). Quy đổi cảm giác: người thật 1,65m → 1u ≈ 0,907m. Model hiện trạng (bbox GLB): PineUmbrella cao 6,90u, tán Ø4,5; cầu đảo deck rộng 2,5 × dài 7,0; nhà Thủy Tạ 11,15 × 7,55, cao 8,25 cả cột biển (~5,6 tới mái); thuyền cao trên mặt nước 1,60u.

| # | Hạng mục | Số đo thật + cách đo | Tỉ lệ ÷ người | Game TRƯỚC XH-3R | Số khóa XH-3R |
|---|---|---|---|---|---|
| a | Đường dạo lát bờ bắc | Ảnh 03: lát ≈ 11–12 ô gạch ~0,5m → **5,5–6m**; §11.2: vỉa hè hồ 3–4m (đoạn đường xe), đoạn Thủy Tạ là **phố đi bộ hoá cả tiết diện ~11–12m** (S5 tự ghi nhận) — game không có lòng đường nên đường dạo = cả tiết diện đi bộ | lát thuần 3,3–3,6 H; tiết diện đi bộ hoá **6,7–7,3 H** | lát **8u (4,4 H)**, ô gạch **2u** → chỉ 4 ô ngang, đọc như lối nhỏ | **lát 12u (6,6 H), z 24..36; ô gạch 1u (12 ô ngang — khớp số ô đếm ở ảnh 03)** |
| b | Cao kè trên mặt nước | Ảnh 03: mép lát → mặt nước ~0,5–0,7m; ảnh 11: bờ đá neo thuyền gần ngang mặt nước, thuyền cao 1,6m làm thước | **0,30–0,42 H** | **0,6u (0,33 H) — ĐÚNG, giữ**; nhưng đỉnh tường kè hộp 5,63 nhô +0,14 trên mặt lát 5,49 thành gờ lạ ở tầm mắt | giữ cao độ 5,5/4,9; **hạ đỉnh tường kè về 5,50 flush** (bó vỉa 5,645 là gờ duy nhất như ảnh) |
| c | Thông trưởng thành | §3: thông 3 lá **15–25m**; ảnh 18: tán vươn trùm đường 7m, đáy tán ~3,5–4 H, ngọn 9–15 H; ảnh 37 (crop): cây trên đảo ≈ **1,2×** chiều cao nhà tới mái. Nén tỉ lệ game theo tiền lệ đèn bờ (5,5m thật → 3,2u ≈ ×0,53) | thật 9–15 H → đích game **6,3–6,9 H**, tán **4,0–4,4 H** | PineUmbrella **6,9u (3,8 H)**, tán Ø4,5 (2,5 H) — thấp/lùn so với mọi ảnh; bờ nam silhouette thông NÓN 7,5–9,8u (sai cả dáng) | **bờ bắc + bờ nam: PineUmbrella scale 1,7 → 11,7u (6,4 H), tán Ø7,7 (4,2 H)**; đảo giữ scale 1,0 (6,9u = 1,2× mái nhà 5,6 — khớp ảnh 37) |
| d | Đèn bờ (đèn bướm) | §11.5 + ảnh 28: cột thật **5–6m**, đĩa huy hiệu ở ~0,74 chiều cao (đo px ảnh 28: gốc 322 → đĩa 105 → ngọn cánh 30) | **3,0–3,6 H** | chưa dựng (colonial game 5,02u = 2,8 H) | chuẩn cho vòng trang trí sau: **5,5–6,0u (3,0–3,3 H)** — vòng này KHÔNG dựng đèn |
| e | Cầu ra đảo | S1: cầu thật hẹp ~2,5–3m; người game cao 1,82u "nặng" hơn tỉ lệ 1u=1m cũ nên 2,5u chỉ = 1,37 H (hai người tránh nhau chật) | **1,5–1,8 H** | deck **2,5u (1,37 H)**; groundH strip 2,5; khe kè/solid 2,4 | **deck 3,2u (1,76 H)**; groundH strip 3,2 (x −251,6..−248,4); khe tường kè + solid khớp 3,2 |
| f | Ghế đá bê tông | Ảnh 25 (crop đo px): lưng ghế 152px : mặt ngồi 72px → ngồi = 0,47× lưng; chuẩn ghế thật: dài 1,8–2,0m, ngồi 0,43–0,45m, lưng 0,9m | dài **1,1–1,2 H**; ngồi **0,27 H**; lưng **0,55 H** | chưa dựng ở bờ (idiom game cũ 1,8u) | chuẩn cho vòng trang trí sau: **dài 2,1u, ngồi 0,5u, lưng 1,0u** — vòng này KHÔNG dựng ghế |
| — | Vòng đường quanh đảo | Ảnh 37/38: lối viền đảo ~3m, ôm sát vành kè + lan can | ~1,8 H | Ring(9,0–13,8) rộng 4,8u, vành ngoài cách mép đảo 1,2u | **Ring(9,8–14,3) rộng 4,5u** — vành ngoài sát vành kè (cách 0,7u), tâm cỏ thu lại (đảo Ø30 giữ khóa S1) |

**Ngoài vùng hồ: KHÔNG đổi** — groundH chỉ sửa đúng strip cầu (trong nhánh hồ); vị trí khóa toàn map, save, minimap khung giữ nguyên (chỉ cập nhật rect đường dạo theo bề rộng mới).

### BƯỚC 2 — THI CÔNG THEO BẢNG ĐO (số khóa MỚI của vùng hồ, thay các số XH-0/1/1.5 tương ứng)
- **Đường dạo bờ bắc:** slab lát 144 × **12u**, z **24..36** (XH-1: 8u, z 28..36), đỉnh giữ 5.49; texture promTex repeat (36,3) → **ô gạch 1u** (cũ 2u). Cỏ thềm/model khác không đổi; tuyến spawn → connector (−219) → đường dạo nguyên vẹn (connector đáp z 1.4..33 nay nằm gọn trên thềm + lát). Minimap: rect đường dạo cập nhật mmY(24), cao 12/316.
- **Kè bắc:** 2 đoạn tường cao 1.3 → **1.14, tâm y 4.93 → đỉnh 5.50 FLUSH mặt bờ** (gờ +0,14 biến mất); bề rộng/khe cầu theo cầu 3.2: đoạn tây 100.4 @ −301.8 (x −352..−251.6), đoạn đông 24.4 @ −236.2 (−248.4..−224); bó vỉa theo cùng số; **solid kè: (−301.8, 36, 50.2, 0.4) + (−236.2, 36, 12.2, 0.4)**. Cao độ nước 4.9 / bờ 5.5 KHÔNG đổi (freeboard 0,6u đã đúng số đo).
- **Cầu đảo:** build_models.py `_xh_bridge()` deck 2.5 → **3.2**, cột/tay vịn lan can ±1.18 → ±1.52; lake.glb build lại + quantize RIÊNG file (375.776 byte; backup raw mới assets/lake.glb.bak-quantize-20261111 = bản 679.688). Đo lại bbox sau quantize: IslandBridge **3.20** × 7.00 ✓; SwanBoat 1.73 × 2.46, ThuyTa 11.15 × 7.55, PineUmbrella 4.50 × 6.90 — KHÔNG đổi ✓ (đầu thiên nga sửa XH-2.1 nằm trong source nên còn nguyên). groundH strip cầu x −251.6..−248.4; nền dưới cầu box rộng 3 → 3.8.
- **Thông:** helper `_umb()` clone PineUmbrella từ ASSETS.lake (castShadow bật): **hàng bờ bắc MỚI 9 cây** z 25.2, x −344..−220 cách ~14u, scale 1.64–1.79 (cao 11.3–12.4u), gốc quét vôi trắng trụ r 0.20–0.23×s cao 0.8 + solid thân (x, z, 0.38); **bờ nam 24 cây + thềm nam 3 + bờ đông 2 cây ĐỔI từ thông nón sang tán ô** scale 1.58–1.85 (giữ nguyên tọa độ XH-1.5). Cây đảo giữ scale 1.0.
- **Vòng đảo:** RingGeometry(9.0, 13.8) → **(9.8, 14.3)**.
- **Grid-diff groundH** (trích hàm từ index.html.bak-xh2-20261111 vs bản mới, lưới 1u x −580..92 × z −88..232 + điểm phân đoạn tại strip cầu): **0 điểm lệch ngoài strip cầu**; trong strip: (−251.5, 40) = (−248.5, 40) = 5.5 ✓, (−252, 40) = (−248, 40) = 4.9 ✓. Vị trí khóa toàn map không đụng; save chohb3d-v1 nguyên cơ chế.

### CỔNG 8/8 XANH
diag 900 SẠCH (447 NPC) · SEED_SAVE 300 SẠCH · standalone **5.412.385 byte** (< trần 10.485.760) + diag standalone 300 SẠCH (GAME_ROOT riêng) · traffic **26/26** · audit **0 lỗi cứng / 0 nhảy lưới** · test_bd2 PASS · check_sweep3 PASS · test_real1 PASS.

### NGHIỆM THU TẦM MẮT (scripts/render_xh3r.py — harness MỚI: lake.glb bản ship + môi trường đúng số XH-3R + 2 nhân vật character.glb làm thước sống)
- renders/xh3r-eye-day.png + xh3r-eye-dusk.png: camera cao 7.15 (mắt người đứng trên lát 5.49) tại (−238, 33) nhìn dọc bờ. Đọc bằng mắt: đường dạo tại vị trí người đứng rộng **~6,5 lần chiều cao người**; hàng thông cao **~6,4 người**, tán trùm xuống đường, gốc vôi trắng rõ; người B đứng sát mép kè — mặt nước thấp hơn mặt lát **~0,33 người (tới ống chân)** khớp ảnh 03/11.
- renders/xh3r-cmp.png: ghép cạnh ảnh thật 03-duong-dao-ven-ho.jpg — cùng cấu trúc: dải lát rộng, hàng cây cao một phía, mặt nước phía kia, kè thấp.
- **Verdict trung thực:** tỉ lệ CHIỀU CAO + bề rộng vùng hồ đã khớp bảng đo ở cả 3 khung tầm mắt (đây là thứ Chung Hy chê ở XH-3+). Còn lại, KHÔNG giấu: (1) tán thông vẫn là đĩa ellipsoid stylized của model XH-2 — đúng silhouette/tỉ lệ, chưa phải tán lá thật (nợ hình khối đã ghi từ XH-2); (2) mặt lát trong render harness phẳng (không vẽ texture ô 1u — giới hạn harness, trong game có texture canvas); (3) hàng thông game ở mép PHÍA CỎ của đường dạo, ảnh 03 (đoạn có đường xe) cây ở mép phía nước — tổng bề rộng tiết diện đi bộ khớp số đo, vị trí hàng cây theo đoạn phố đi bộ Thủy Tạ (ảnh 18); (4) đường dạo còn trống — ghế/đèn/bollard theo chuẩn đã đo ở bảng (mục d, f) thuộc vòng trang trí XH-3 làm lại, vòng này cố ý không dựng.
- Ngoài phạm vi đã dừng đúng lệnh: KHÔNG NPC sinh hoạt/sương mù/trang trí mới, KHÔNG đẩy GitHub, KHÔNG upload link. (Lưu ý tồn đọng từ XH-2: gói XH-2 vẫn chưa lên GitHub — chờ thẻ duyệt của Chung Hy.)

## XH-3S — 12/11/2026 (1 vòng: TRANG TRÍ BỜ + SINH HOẠT QUANH HỒ + SƯƠNG LẠNH — làm lại phần XH-3+ bị hủy, trên khung tỉ lệ XH-3R) — **XONG, 8/8 CỔNG XANH**
Dựng trên BẢNG TỈ LỆ CHIỀU CAO của XH-3R (ràng buộc cứng) + KE_HOACH_HO §7/§8/§11 (S2/S3/S7) + KE_HOACH_SONG_QUANH_HO phần A/B. Backup: index.html.bak-xh3s-20261112. Toàn bộ thi công nằm ở 3 chỗ: helper sàn nổi INLINE trong groundH (nhánh hồ), tách kè bắc trong khối XH-1, và 1 khối XH-3S cuối file (tránh TDZ — diag_runtime là cổng bắt buộc, không phải node --check).
### TRANG TRÍ BỜ (đúng số bảng XH-3R)
- **Kè bắc tách 3 đoạn tây** chừa khe: −352..−319,2 / −316,8..−283,2 / −280,8..−266 (khe cầu Y −318/−282 rộng 2,4 cho thân cầu 1,8) + **khe bến §7 x −266..−252**; bó vỉa + solid kè khớp từng đoạn (4 solid z 36).
- **Cầu bến §7:** 2 ngón gỗ 4×6,5 (đỉnh 5,50) + lối nối bờ 14×1,2; **SLIP giữa x −262..−256, z>37,2 vẫn là NƯỚC 4,9** (chứa SwanBoatPlayer −259,39,3); cọc đỡ, lan can trắng 2 thanh ở mép ngoài + đầu xa, mép trong slip để mở cho XH-4; biển BẾN THUYỀN THIÊN NGA tại (−267,6, 34,6) mặt về đường dạo. groundH sàn nổi **INLINE trong groundH** (audit_ground trích groundH độc lập — helper ngoài bị mất, đã vấp 1 lần và sửa tại gốc).
- **Cầu ngắm chữ Y ×2 (S7)** tại x −282/−318: thân 1,8×5 + 2 cánh RECT XOAY ±0,62 rad (2,6×1,4) — groundH kiểm tra rect xoay ĐÚNG HÌNH HỌC (bài học XH-3+: xấp xỉ tuyến tính hở khe → sụt 0,6u); lan can trắng 2 bên thân + solid thân; cánh chéo không solid (nợ luật mặt nước XH-4, như ghi nợ trước).
- **Đèn BƯỚM ×7** bờ bắc z 27,5 nhịp 18u (x −344..−236): cột xanh #1e4d2e cao 5,2 + cánh bướm + panel sáng + **đĩa huy hiệu ở +4,05 (≈0,74 chiều cao — đo ảnh 28)**, tổng cao ~5,9u (bảng XH-3R mục d: 5,5–6,0u; bản XH-3+ hủy dựng 3,2u là SAI). Panel/đĩa đăng ký lampGlows, 4 PointLight đăng ký lampLights — cháy sáng buổi tối qua applyDayNight sẵn có (vật dựng cuối file tự set trạng thái theo isNight lúc dựng).
- **Ghế bê tông 2 tấm ×9 bờ + ×2 đảo** theo bảng mục f: dài **2,1** / mặt ngồi **0,5** / tựa **1,0**, kem #e8e2d4, chân #5d534a — đặt trên **dải cỏ sát mép nước** (S3; verge đỉnh 5,53, x −352..−266 + đoạn đông) nhịp 12u quay ra hồ. SIT_SPOTS +3 ghế hồ (startSit thêm toast gió hồ lạnh; tickSit hỗ trợ yOff vì mặt ngồi 0,5 ≠ 0,28 của ghế sạp).
- **Ki-ốt vé đầu cầu đảo** (−258,5, 30,3, mặt quầy hướng đầu cầu): biển THUÊ THUYỀN THIÊN NGA + **biển giá 30 XU / 5 PHÚT** (§7 khóa) + 3 áo phao cam (render soi vòng này bắt được áo phao che biển giá → đã nâng áo phao 1,52→1,59, hạ biển giá 1,30→1,16 trong code thật) + solid ki-ốt + người bán vé tĩnh.
- **BIỂN NHIỆT ĐỘ** tại (−264,5, 33,9): canvas vẽ lại khi nhiệt nguyên đổi, số liệu từ **tempNow() sẵn có của game** (19:00 → 17°C, nhãn "Lạnh — nhớ mặc ấm") — SONG_QUANH_HO B3.
- **Bollard ×6** quanh đầu cầu đảo/bến (đầu phát sáng qua lampGlows) · **CherryTree (phượng tím) ×2** scale 1,5 tại (−253/−231, 25,2) + solid thân · **solid nhà Thủy Tạ (−262, 58, 3.7, 5.4)** theo bbox GLB rotY −90° — hết đi xuyên (nợ XH-2 đã trả).
### SINH HOẠT QUANH HỒ (phần A — tái dùng wanderer/statics/tủ đồ, KHÔNG hệ mới)
- **Dừng ngắm hồ** dùng lại mode 'browse' sẵn có của wanderer: gán sẵn _bStand ở lan can z 34,55 + browsePt giữa hồ → NPC trượt tới mép nước, quay mặt ra hồ, đứng 5–10s rồi đi tiếp.
- **8 người đi bộ lẻ** 2 chiều (lane z 30,8/28,4 trên lát 12u; một nửa có dừng ngắm) + **2 người vòng đảo** (route vòng r~12, né khối nhà Thủy Tạ) + **2 người chạy bộ** (z 32,6, tốc độ 2,55–2,8, rank 0,6 → hiện sáng sớm + chiều tối theo crowdLevelNow, ẩn trưa/khuya).
- **4 CẶP tình nhân:** B dùng route của A lệch −0,85z, gán cùng rank/speed/phase/i; tick keo form B→A và dừng ngắm thì dừng CẢ CẶP tại lan can (6–11s, chu kỳ 24–46s). **2 cặp ngồi ghế** (statics 'sit' tại ghế −310/−242, chân gập −1,45 như idiom ngồi sẵn có).
- **5 xe đạp** vòng kín quanh đường dạo (lane ngoài z 33,4 đi / 26,6 về, khép vòng ở 2 đầu — không cắt lane người đi bộ 28,4–31,7), model tự dựng (bánh torus r0,34 + khung ống + rider đạp chân trong tick), tốc độ 3,9–4,6 (~3× đi bộ), số xe hiện theo crowdLevelNow (19:00 đủ 5).
- **2 người chụp ảnh** (regSpecial + npcHoldPhone + spIdle giơ máy): đầu cầu đảo (−245,6, 34,7) + trên thân cầu Y −318. **Mọi NPC hồ mặc ấm** (dressWarm: khăn SCARF_COLS + beanie NPC_BEANIE, ẩn nón lá/mũ lưỡi trai).
### SƯƠNG LẠNH (phần B1)
5 lớp plane alpha canvas radial (95×26 … 120×34) ở cao 5,28–5,60 trên mặt nước, trôi chậm sin/cos; opacity nội suy theo giờ game: 0,30 lúc 6:30 sáng → 0,05 trưa → 0,20 lúc 18:30 → 0,24 đêm. Tick móc qua tickWater (idiom các vòng trước), KHÔNG đăng ký waterMats/WATER_FX.
### KIỂM CHỨNG SỐ (ngoài cổng chuẩn)
- Lấy mẫu groundH trích từ file: **2.679 điểm** dọc mọi tuyến NPC hồ + sàn bến (ngón = 5,5, **slip = 4,9** ✓) + thân/cánh cầu Y = 5,5, rãnh giữa 2 cánh = 4,9 — **0 sai**. Grid-diff vs backup: **216.033 điểm, lệch CHỈ trong vùng sàn mới (102 điểm), 0 lệch ngoài vùng**.
- check_sweep3: census SPECIAL_NPCS 4→6 (SP_EXP +2 người chụp ảnh hồ, đúng vị trí) — sửa test minh bạch kèm comment XH-3S, không nới lỏng kiểm nào khác.
### CỔNG 8/8 XANH (chạy lại đủ trên file cuối, sau sửa áo phao/biển giá)
diag 900 SẠCH · diag soak 3600 SẠCH · SEED_SAVE 300 SẠCH · standalone **5.436.353 byte** (< trần 10.485.760) + diag standalone 300 SẠCH · traffic **26/26** · audit **0 lỗi cứng / 0 nhảy lưới** · test_bd2 PASS · check_sweep3 PASS · test_real1 PASS.
### NGHIỆM THU TẦM MẮT (scripts/render_xh3s.py — harness mới theo số XH-3S; biển hiệu là ảnh PIL đúng nội dung canvas game)
- renders/xh3s-prom-night.png (19:00): đèn bướm cháy sáng + đĩa huy hiệu phát sáng trên cột, thông tán ô sừng sững bên phải, cặp tình nhân đi đôi (lưng về camera, hướng tây), xe đạp + người đạp hướng đông, cặp ngồi ghế ở dải cỏ trái, mặt nước teal hiện rõ, sương nhẹ trên nước.
- renders/xh3s-dawn.png: sương thành từng vệt trắng mềm rõ trên mặt nước, người chạy bộ trên đường dạo, bến + thuyền neo + cầu Y + đảo Thủy Tạ trong một khung, biển giá 30 XU / 5 PHÚT đọc rõ ở ki-ốt.
- renders/xh3s-kiosk.png: ki-ốt + biển chính đọc được, 2 khách quay LƯNG về camera đối diện quầy (bản render đầu quay ngược — đã sửa pose harness), bán vé sau quầy, bollard phát sáng, bến + thuyền bên trái; biển nhiệt độ đứng ở trái ki-ốt (trong harness chữ bị xoay/mờ vì plane hướng −z + vật liệu có sáng — trong game biển là MeshBasicMaterial tự sáng + rotation.y=π đứng thẳng, đọc rõ; nội dung 17°C khớp tempNow 19h).
- **Verdict trung thực:** GIỐNG THẬT — đủ bộ dấu hiệu bờ hồ thật (đèn bướm + huy hiệu, ghế bê tông trên cỏ, cầu Y, ki-ốt + áo phao, bến 2 ngón) đúng tỉ lệ bảng đo. LẠNH — khăn/beanie toàn tuyến, sương theo giờ, biển 17°C. SỐNG — 27 NPC hồ + 5 xe đạp theo mật độ giờ. Còn lại KHÔNG giấu: (1) tán thông vẫn đĩa stylized (nợ từ XH-2, việc riêng toàn map); (2) sương trong game là lớp alpha phẳng — mềm nhưng không có chiều sâu thể tích; (3) harness render_xh3s person() bị gương hướng so với game (đã ghi comment trong script) và biển hướng −z bị xoay chữ — cả hai là giới hạn harness, không phải lỗi game; (4) cánh cầu Y chưa có solid/lan can (chờ luật mặt nước XH-4 như đã ghi nợ).
- Ngoài phạm vi đã dừng đúng lệnh: KHÔNG làm XH-4 (cơ chế đạp vịt để vòng sau — bến/slip/solid đã sẵn sàng), KHÔNG đẩy GitHub, KHÔNG upload link.

## XH-4C — PHỐI MÀU LẠI + SỬA TIẾT DIỆN VÙNG HỒ THEO VIDEO THẬT (research/28) + BỔ SUNG 02:04 (nước hết phẳng + phân phối cây research/29) — 12/11/2026
Backup: index.html.bak-xh4c-20261112. KHÔNG rebuild GLB (tint runtime theo material.name), KHÔNG đổi groundH (audit lưới 0 lệch), KHÔNG đụng save/solid cũ (chỉ THÊM solid cho cây mới trồng).

### 1. Màu nước theo giờ (chỉ nước HỒ; đài phun giữ nguyên bộ WATER-1)
- Canvas bake: teal #276a8a -> XÁM BẠC #8b979c; gợn rgba(207,216,218) alpha hạ. Đáy hồ 0x14425c -> 0x4c5a5e.
- Màu theo giờ bằng TINT tuyến tính nhân trên canvas ngày (tick XH-4C bọc sau tick XH-3S, đọc gameHourF): ngày (1,1,1); 17:30 chàm (0,79/0,85/1,36) = #7e8cb4; đêm (0,26/0,32/0,50) = ~#4a5872. Emissive đêm của material hồ 0x1d4e5f -> 0x4a5a86 (applyDayNight vẫn 0,55 đêm/0 ngày cho cả waterMats — đài phun giữ emissive teal riêng của nó, không đổi).
- BỔ SUNG chống "tấm phẳng": canvas thêm 14 mảng sáng/tối mềm ±6% + 96 gợn nhỏ lớp 2 + 26 vệt sáng dài (tổng 150+ vệt, seed sin-hash không lặp đều); roughnessMap = chính canvas gợn (roughness 0,38 x gợn) -> độ nhám/loáng thay đổi theo gợn; DẢI MÉP NƯỚC SẪM (wet edge, gradient alpha #34424a) dọc bờ bắc + bờ nam + vòng quanh đảo (renderOrder 3); VỆT PHẢN CHIẾU ĐÈN BƯỚM x7 trên nước dưới bờ bắc (additive, chỉ đêm, tick theo isNight).

### 2. Palette vùng hồ trầm xuống (chỉ vùng hồ)
- Lát canvas #dde2e2 -> #a9aba8; accent hồng 4/16 ô -> 1/16 + alpha 0,55; mạch gạch sẫm hơn; vòng đảo + nền cầu đảo -> 0xa9aba8; lối nối đổi texture ĐÁ PHIẾN riêng #5f574f (ô biến thiên + mạch sẫm, thay clone lát sáng).
- PHÁ PHẲNG LÁT: mỗi ô lệch tông theo hash ô (±6,5%) + hash mảng 2 ô (±5%) — kiểu bàn cờ mảng như ảnh 03.
- Cỏ vùng hồ -> OLIVE texture riêng (sweep cuối file: chỉ mesh màu 0x5f8547 có tâm trong khung x[-580,-200] z[20,240] mới đổi; material 0x5f8547 dùng chung vùng chợ KHÔNG bị đụng): nền #66702f + mảng lớn 3 tông (#55662c/#66702f/#6e6d29) + vệt #46512a + speckle.
- Tint lake.glb runtime: PineDark #3a4f38 / PineMid #46604c / PineLight #5a7263 (xám xanh thưa), Trunk #6f655c, LeafGreen (liễu) #3d5231. Vôi gốc thông _umb 0xe8e2d4 -> 0xcfcfc8; bó vỉa đông 0xd8d2c2 -> 0xb9bcba; kè đá giữ #7e776c.

### 3. Tiết diện bờ bắc 4 lớp + cây theo BẢNG PHÂN PHỐI (research/29_PHAN_PHOI_CAY_HO.md)
- ĐƯỜNG NHỰA mới: box 144x5,6 tại z 17,4..23,0 (đỉnh 5,50 flush sàn), canvas nhựa #545c63 + speckle + 2 vệt bánh xe + vạch mép + vạch đứt giữa. Traffic KHÔNG mở rộng vào đường này (giữ test 26/26) — đường tĩnh + vạch như brief cho phép.
- DẢI TACTILE: box 144x0,45 tại z 30,0, canvas #8f9296 với 5 vạch dọc sẫm (ảnh 03/25), chạy liên tục — thay vai trò accent hồng rải đều.
- Mép nước: 3 đoạn kè bắc tây/trung + 2 đoạn kè tây -> CỎ DỐC (slope box nghiêng 0,23 rad, cạnh bắc flush thềm 5,48, cạnh nam chạm nước 4,80); đoạn ĐÔNG giữ kè đá + bó vỉa (gần bến/cầu Y như frame thật); solid chặn người ở z36 giữ nguyên (vô hình).
- CÂY TRỒNG LẠI theo research/29 (điều tra từ v1 30 frame + ảnh 01/03/18/25/36): hàng mép nước 10 cây theo nhịp CỤM-THƯA (cụm 2-3 cây cách 6-7u, giữa cụm trống 14-24u; 7 lá rộng nghiêng 0,50-0,68 rad + 3 THÔNG NGHIÊNG clone rotX 0,50-0,55 — ảnh 25 chứng minh thông nghiêng có thật); hàng trong z 25,2 PHÁ ĐỀU: bỏ 4/9 thông (-316/-288/-260/-220), thêm 2 lá rộng THẲNG (-316/-260), giữ 5 thông; hàng hậu cảnh MỚI sau đường z 14: 2 thông + 3 lá rộng; bờ tây đổi 3 lá rộng -> 3 THÔNG NGHIÊNG rotZ (ảnh 18 Trần Quốc Toản) + giữ 1 lá rộng; đảo thêm thông #2 + phượng tím + lá rộng nghiêng mép đông; hoa giấy x3 giữ (research/29: ~3-5 cụm/bờ). Mọi cây ven hồ đều có vôi gốc xám (lá rộng: tube dọc thân nghiêng; thông nghiêng: tube theo hướng nghiêng; thông thẳng: cyl như _umb).

### 4. Đêm Thủy Tạ MAGENTA
- 2 dải emissive #d94fd0 mặt tây nhà (cửa sổ y 7,55 + biển y 9,75) đăng ký lampGlows (applyDayNight chỉ set intensity 2,4/0 — giữ màu); PointLight magenta riêng (55, tầm 36) KHÔNG vào lampLights (bị set cứng 0xff9a3d) — tick XH-4C tự bật/tắt theo isNight; vệt phản chiếu magenta (plane 7,5x26, gradient alpha, additive, renderOrder 4) kéo từ chân đảo về phía bắc, opacity đêm 0,5±0,07 nhấp nháy chậm.

### Cổng (chạy 2 lượt: bản gốc + bản bổ sung 02:04 — cả hai đều đủ)
diag 900 SẠCH · soak 1800 SẠCH · SEED_SAVE 300 SẠCH (save cũ nguyên vẹn) · package + standalone diag 300 SẠCH (GAME_ROOT=/tmp/xh4c/sa), standalone 5.458.596 byte < trần 10.485.760 · traffic 26/26 · audit 0 lỗi cứng / 0 nhảy lưới (cảnh báo mềm wanderer#10 băng làn — có từ trước) · test_bd2 PASS · check_sweep3 PASS · test_real1 PASS.

### Nghiệm thu — render mô phỏng đúng thông số code (scripts/render_xh4c.py, Cycles/ACES/OIDN, nhân vật 1,82u làm thước)
- renders/xh4c-cmp-day.png: game bờ bắc buổi sáng | video v1 f024 — lát xám trầm, đường nhựa + vạch ở phía trong, hàng thông + lá rộng, nước xám bạc ở mép trái; frame thật: cây nghiêng + cỏ dốc + nước xám.
- renders/xh4c-cmp-dusk.png: game Thủy Tạ MAGENTA + nước chàm + vệt phản chiếu | video v3 f001 — khớp tông chàm + điểm hồng magenta phản chiếu xuống nước như frame thật.
- renders/xh4c-eye.png: tầm mắt từ mặt nước qua cụm cây nghiêng -298/-291: thân nghiêng + vôi gốc + hoa giấy tím sau ghế, nhân vật 1,82u đứng trên lát, các lớp nước -> cỏ -> lát -> nhựa xếp chồng đọc được.
- ĐO PIL (median, render harness — lệch tuyệt đối gồm cả hệ số nắng/bóng của harness, cùng phương pháp các vòng XH-1/3S): nước ngày (121,131,140) vs đích canvas (139,151,156), ĐỘ BÃO HÒA spread = 19 (canvas teal cũ spread = 99 -> hết hẳn tông bể bơi); lát (116,118,117) vs (169,171,168) — tiền cảnh nằm phía khuất nắng; cỏ đón nắng (65,74,43), cỏ trong bóng slope (38,45,26) vs đích (102,112,47) — hue olive đúng hướng (G>R>B), độ sáng thấp do slope quay lưng nắng; nước tối (39,55,102) — hue chàm đúng (B>>R). Giá trị PALETTE trong code/canvas = khớp 100% số research/28 (đó là nơi màu được khóa); render chỉ để soi đọc-hình.
- Tự soi 3 câu: (1) còn "bể bơi" không — KHÔNG: nước xám bạc/chàm, spread bão hòa 19; (2) tiết diện đủ lớp chưa — ĐỦ 4 lớp + tactile + cỏ dốc; (3) cây nghiêng đọc ra không — CÓ: thân nghiêng + vôi đọc rõ ở eye/dusk, cụm-thưa đọc ở day.

### Nợ / ngoài phạm vi (ghi rõ để vòng sau nối)
- Bờ nam: 24 thông vẫn đều nhịp (silhouette xa) — phá đều bờ nam theo research/29 để vòng sau.
- Tùng cột bờ đông gần quảng trường: có trong ảnh 01 nhưng KHÔNG trồng (lệnh bác thông nón/dáng cột vùng hồ từ XH-3R còn hiệu lực).
- Tán thông vẫn đĩa stylized (nợ XH-2, việc riêng toàn map); texture lát/cỏ/nước trong harness là màu phẳng tương đương (biến thiên từng ô chỉ có trong game thật qua canvas).
- Chưa làm: XH-4 đạp vịt, KHÔNG đẩy GitHub, KHÔNG upload link (theo lệnh vòng).

## XH-4 — ĐẠP VỊT THIÊN NGA CHƠI ĐƯỢC + LUẬT MẶT NƯỚC — 12/11/2026 — **XONG, 8/8 CỔNG XANH + TEST THUYỀN RIÊNG PASS**
Backup: index.html.bak-xh4-20261112. Thi công: 6 sửa nhỏ ở lõi (interact dispatch, phát hiện tương tác, ctxPrompt, chip tickV43, nhánh di chuyển animate, vẫy tay statics 'chat') + 1 khối XH-4 cuối file (trước animate(), sau wrapper XH-4C — đổi tên biến bọc tickWater thành _xh4BoatTW vì _xh4TW đã bị XH-4C dùng). KHÔNG sửa groundH (kiểm chứng nguyên văn hàm giống hệt bản backup → 0 lệch toàn khung), KHÔNG đổi save (trạng thái thuê không lưu, như thuê xe).

### 1. Thuê & chèo (bám khung thuê xe V5.2)
- Điểm thuê BOAT_RENT_PT (-259, 33,6) ở đầu cầu bến cạnh ki-ốt vé (-258,5, 30,3): interact 'boatrent' thắng 'chat' của chính người bán vé trong bán kính 4,6 (bán vé = người cho thuê). Đủ Xu → trừ **30 Xu / 300s (giá khóa)**, lên SwanBoatPlayer (node LAKE_PLAYER_BOAT của XH-2, đã gỡ đóng băng matrixAutoUpdate trong khối XH-4); thiếu Xu → toast từ chối như dịch vụ khác. KHÔNG miễn phí theo cấp (khác thuê xe — brief khóa 30 cho mọi người).
- Ghế ở local (0, -0,45) sau tâm thuyền (mũi = local +Z: cổ/đầu ở Blender -Y), origin người chơi = mặt nước + bob + 0,37 (hiệu chuẩn theo idiom tickSit: ghế hồ yOff 0,53 ≈ mặt ghế 0,5 + 0,03; mặt ghế thuyền Blender z 0,345). Pose đạp: chân -1,12 ± sin(pedal) 0,38 lệch pha, tay -0,62.
- Điều khiển bằng chính phím di chuyển (input camera của animate): **iy = ga đạp** (W tới tối đa 2,2u/s, S lùi 1,15u/s, quán tính: tăng tốc 1,35, hãm nước 2,1), **ix = lái** 0,61 rad/s (~35°/s theo KE_HOACH §5) hiệu quả theo đà (tối thiểu 35% để xoay được trong slip hẹp; lùi thì lái đảo chiều như thuyền thật). Bobbing sin theo vị trí + lắc nhẹ theo lái/tốc độ. Vệt nước: pool 14 vòng gợn riêng ở đuôi (không dùng WATER_FX.rings của đài phun), tuổi 1,7s nở ~3,3u; đụng biên có vòng lớn + tiếng "cốc" trầm. Tiếng đạp nước: tone(300→90) rất nhẹ mỗi 0,95s qua bus tone/masterGain chung với ambience (KHÔNG sửa ambZone để khỏi phá test âm thanh); sương quanh thuyền buổi sáng = hệ sương mặt hồ XH-3S sẵn có (thuyền chèo xuyên qua lớp sương) + gợn đuôi.
- Đồng hồ thuê trên HUD chip (tickV43, cùng cơ chế chip xe): đếm ngược 300s, cảnh báo 10s cuối. **Hết giờ → thuyền TỰ TRÔI VỀ BẾN** (như xe tự về bãi): marble steering — lái thẳng về slip, khi chạm vòng r17 đảo thì resolve đẩy radial ra nên thuyền tự trượt dọc vòng cung về phía đích (hội tụ cho vật cản lồi, không cần nhánh rẽ riêng); giảm ga khi gần đích; tới nơi tự xuống thuyền; chống kẹt bằng mốc 300s ép về. Trả sớm: về gần slip (dist < 4,6 tới (-259, 41)) bấm E → đứng lại trên bờ (-259, 34,9, groundH 5,5), thuyền tự lướt về neo trong 1,6s (idiom rentReturn). Chưa gần slip mà bấm E → toast nhắc về cầu bến.
- Người bán vé VẪY TAY khi thuyền rời slip lần đầu (z > 45,5) và khi trả thuyền: tái dùng hành vi giơ tay sẵn có của statics kind 'chat' (thêm điều kiện __xh4WaveUntil ép giơ tay vẫy 2,4s).
- Địa lý thật cần biết khi chơi: làn ra khỏi slip ở x=-259 chạm vòng r17 đảo ở z=43,58 (đảo Thủy Tạ sát bờ bắc như hồ thật) — hành lang giữa vòng đảo và kè bắc (z 38) là làn đi; test đã kiểm chứng vòng qua phía tây đảo thoát được.

### 2. Biên thuyền (xh4BoatResolve — đẩy ra khỏi vùng cấm, trượt dọc biên, kiểm bằng test)
Thứ tự: kẹp biên mặt nước x -556..-228, z 38..192 (brief ghi z 40 cho biên nam/bắc mở; chốt dùng **z ≥ 38 thống nhất** vì kè bắc/slip ở z 38 — lệch này ghi rõ tại đây) → vòng đảo r ≥ 17 từ tâm (-250, 58) (vòng này nuốt luôn cầu đảo: mọi điểm của dải cầu đều nằm trong r17) → rect vật cứng (2 ngón cầu bến, lối nối bờ, thân 2 cầu Y, đập Ông Đạo) mở rộng bán kính thân 1,05 → đoạn cánh chéo cầu Y (point-segment r 1,5, khớp rect xoay của groundH) → thuyền tĩnh (mọi LAKE_BOATS trừ thuyền người chơi, vòng tránh r 2,35) → kẹp lại đảo + biên. Đụng biên: tốc độ × 0,45, không kẹt không xuyên.
- **Xung đột brief đã phân giải:** biên tây khóa -556 nhưng đập Ông Đạo (solid -557±4,2 → mặt đông -552,8) nhô vào trong biên ở hàng z 60..130. Giải: trong dải z của đập, rect đập thắng — tâm thuyền dừng ở x ≥ -551,75 (mặt đập + 1,05); ngoài dải đập biên -556 vẫn nguyên. Test đo đúng -551,75 ở hàng z=95 và -556,00 ở hàng z=160.

### 3. LUẬT MẶT NƯỚC cho người đi bộ — cách đã chọn (ghi rõ theo lệnh brief)
**Chọn: chặn ở mép như vực + trượt dọc mép + tóe nước nhẹ** (khớp hệ collide/groundH hiện có, không sửa groundH): định nghĩa "mặt nước" = trong khung mặt nước mở rộng (x -560..-224, z 36..196) VÀ groundH < 5,0 — nhờ đó đảo (5,5), cầu đảo, cầu bến + slip-fingers, sàn nối và **cánh cầu chữ Y tự động là đất liền vì groundH của chúng đều trả 5,5** (nợ "cánh cầu Y phải solid khi đi bộ" của XH-3S được đóng theo đúng nghĩa này: đứng/đi trên cánh được, bước ra khỏi mép cánh là bị chặn như mép vực). Áp ở bước di chuyển sau collide() (chung cho đi bộ + cưỡi xe): đích là nước → thử trượt từng trục (giữ trục nào còn trên cạn), cả hai trục đều ướt → đứng yên; mỗi lần chặn (cooldown 0,8s) có vòng tóe nước + tiếng splash nhỏ tại điểm định bước. Người đang chèo không bị guard này đụng (nhánh thuyền riêng); NPC đi bộ không vào vùng hồ; thuyền tĩnh có vòng tránh riêng nên không kẹt thuyền người chơi.

### 4. Test riêng — scripts/test_xh4_boat.mjs (harness diag như test_bd2) — **ALL CHECKS PASS**
Số đo thật: thuê trừ đúng 30 Xu (100→70→40 qua 3 lần thuê, trả không trừ thêm; 10 Xu bị từ chối, Xu nguyên); biên bắc z = 38,00 · đảo r = 17,00 (làn tây trống) · cung thuyền tĩnh nam đảo dừng r = 20,95 (= 18,6 + 2,35 khớp số đặt thuyền) · biên tây x = -556,00 · đập Ông Đạo x = -551,75 · biên đông x = -228,00 · biên nam z = 192,00 · cầu Y dừng z = 43,58 trước thân/cánh · thuyền tĩnh tránh đúng 2,35 · lùi ra slip chạm vòng đảo 43,7 rồi vòng tây thoát (x -279,2, r 32,4) · hết giờ autopilot từ (-320, 120) tự về bến + tự xuống trong 1.120 bước mô phỏng (~56s) · save JSON không chứa boating/boatOn/boatState. Guard: bước từ cầu bến xuống nước bị giữ nguyên vị trí; bước chéo mép bờ bắc trượt dọc mép (x đi, z giữ); điểm giữa cánh cầu Y groundH 5,5 không phải nước.

### Cổng
diag 900 SẠCH · soak 1800 SẠCH · SEED_SAVE 300 SẠCH (đang thuê dở nạp lại không kẹt — trạng thái thuê vốn không vào save, test_xh4 mục 5 khóa điều này) · package + standalone diag 300 SẠCH (GAME_ROOT=/tmp/xh4/sa), standalone 5.474.608 byte < trần 10.485.760 · traffic 26/26 · audit 0 lỗi cứng / 0 nhảy lưới (cảnh báo mềm wanderer#10 băng làn — có từ trước) · test_bd2 PASS · check_sweep3 PASS · test_real1 PASS · **test_xh4_boat ALL PASS**. groundH: hàm giống hệt bản backup từng ký tự → 0 lệch toàn khung.

### Nghiệm thu — render mô phỏng đúng thông số code (scripts/render_xh4.py, Cycles/ACES/OIDN, nhân vật 1,82u; biển hiệu là ảnh PIL nội dung tương đương biển canvas trong game)
- renders/xh4-rent.png: người chơi vừa ngồi lên SwanBoatPlayer trong slip (ghế sau tâm, mặt hướng bờ), ki-ốt + biển "THUE THUYEN THIEN NGA" + biển giá "30 XU / 5 PHUT" + người bán vé sau quầy đều trong khung, chiều muộn có đèn ki-ốt.
- renders/xh4-row.png: từ sau thuyền giữa hồ (-330, 120) — người chèo + cổ thiên nga + vòng gợn đuôi ở mép dưới khung, nhìn về đảo Thủy Tạ + hàng thông bờ bắc + bến thuyền xa; sương sáng phủ mặt nước.
- renders/xh4-edge.png: thuyền người chơi dừng ở điểm vòng cung tây-bắc đảo (-262, 46) đúng r17, mũi hướng tâm đảo, khoảng nước hẹp giữa mũi thuyền và vành đảo đọc rõ; cầu đảo + Thủy Tạ phía sau.
- Tự soi: 3 câu — (1) lên thuyền ở slip có ki-ốt/biển giá trong khung chưa: CÓ, đọc rõ chữ; (2) tầm mắt từ thuyền có thấy đảo + bờ bắc + vệt đuôi chưa: CÓ đủ 3; (3) thuyền sát biên đảo có đọc được khoảng chặn chưa: CÓ — thuyền dừng ngoài vành, không chạm đảo. (Khung hình đã qua 3 lượt chỉnh camera: điểm r17 phía tây thuần bị nhà Thủy Tạ che trong ảnh nên shot 3 dùng điểm vòng cung tây-bắc — cùng một vòng r17, ghi rõ tại đây.)

### Nợ / ngoài phạm vi (ghi rõ để vòng sau nối)
- Companion (Couple/Family/Tour) KHÔNG ngồi cùng thuyền (như xe máy hiện tại — ngoài brief XH-4); XH-5 tích hợp lo phần đồng bộ nếu cần.
- Điểm ảnh 'lake' photo spot + nhiệm vụ hồ: thuộc XH-5 theo KE_HOACH, chưa làm ở vòng này.
- Autopilot hết giờ là marble steering hình học (không có tránh NPC/thuyền động — trên hồ hiện chỉ có thuyền tĩnh, đã có vòng tránh r 2,35 trong resolve nên vẫn an toàn).
- KHÔNG đẩy GitHub, KHÔNG upload link (theo lệnh vòng).

## MERGE-ARGON — HỢP NHẤT 3 PHÍA (bản mình XH-4 × bản AI Studio commit 3ebaca0) — 12/11/2026 — **XONG, ĐỦ BỘ CỔNG XANH**
Backup: index.html.bak-merge-20261112 (bản mình trước merge, 656.514 byte). Cách làm: git merge-file 3 phía với tổ tiên chung = bản XH-4C (md5 04a52dce, chính là cha 1d6ccf7 của commit Argon) — chỉ 1 xung đột thật (khối cuối file, cả hai cùng append) + xử lý tay 3 điểm nóng; KHÔNG lấy checklist từ remote (Argon đã xóa 39 dòng cuối trên remote — bản local này là nguồn đúng, giữ nguyên toàn bộ mục XH-4C + XH-4).

### GIỮ của Argon (đã vào bản hợp nhất)
- **HUD glassmorphism toàn bộ**: CSS panel/nút kính mờ nâu-vàng (blur 8px, viền vàng, hover), bố cục lại cột phải (minimap lên top 60, orderChip/eventChip/modePanel dịch xuống nhường chỗ), **thanh Đi Nhanh Địa Danh #quickNav** (6 mốc: Chợ Đêm / Nhà Lồng / Bậc Thang / Hòa Bình / Bến Hồ / Thủy Tạ — handler trích riêng, thêm khóa an toàn: đang trên thuyền XH-4 thì chặn nhảy + toast nhắc; đang hát thì stopSing trước khi nhảy).
- **A — Nội thất chợ**: 40 quầy phân hóa 7 nhóm hàng thật (GROUP_DEFS: rau củ / trái cây / hoa / vải-len / đồ khô / đặc sản / ẩm thực — biển tên sạp thật + số quầy), bày hàng đặc trưng từng nhóm, đèn tuýp ấm từng quầy + 6 quầy tương tác được làm giàu thêm, hệ cột nhà lồng (x −20,8..20,8 × z 13,55/27,45) + dầm + máng đèn lối đi, sàn gạch quả trám có vệt mòn/nước cũ. Kèm tiểu thương đứng sau MỖI quầy trang trí (đăng ký INDOOR_COUNTERS như bản gốc).
- **B — Tam cấp**: vệt mòn luồng bước chân (3 nhịp + 2 chiếu nghỉ, dùng stairH), lan can sắt 3 đường (x −64,4/−56/−47,6), TEX_GRIME phủ bề mặt bậc (traverse chỉ trong clone thang; SideWall giữ màu 0x8a8175 như SWEEP-NIGHT-1), chiếu nghỉ Chú Ba được làm giàu (bàn gỗ + khăn đỏ + ống xăm + đèn lồng + biển mới), **4 tiểu thương ngồi bậc** (mẹt dâu/bơ/khoai/hoa), **5 xe máy đậu chân thang**. LƯU Ý PHÂN GIẢI: khối Argon thay thế là bộ đạo cụ coi bói TRÙNG cũ ở (2,8, −20,8) (người + biển + solid ở điểm cũ) — đã gỡ theo Argon; **Chú Ba THẬT (regSpecial 'chuba' tại chiếu nghỉ (−50,4, 11,33, −19,6), điểm tương tác FORTUNE_PT (−53,2, −19,2)) không bị đụng**, test_bd2 PASS.
- **C — Quảng trường**: ghế đá công viên (2,1/0,5/1,0) + cột cờ phướn quanh đài phun (FNT 27, 5,2), ghế đá + hộp đàn tip + **vòng người nghe quanh Góc Hát đồi** (3 ngồi cũ → 7 người: 5 ngồi + 2 đứng), trang trí sân khấu (stage-deco), đài phun nâng cấp (6→8 tia + vòng tia phụ + vòng gợn thứ 3 — giữ, thuộc khu quảng trường).
- **E — Hơi thở lạnh + dấu hồ**: pool hơi thở 6 → **48 hạt** (8 người chơi + NPC wanderer/static gần, texture radial mềm, bật khi curTemp ≤ 19,5° hoặc effW < 40); **dấu hộ chiếu 'lake' THỐNG NHẤT 1 ĐƯỜNG DUY NHẤT**: STAMPS thêm {id:'lake'} (tổng 9 → **10 dấu**), zoneInfo trả stamp:'lake' cho cả 4 vùng hồ/đảo/bờ, toast hoàn thành dùng STAMPS.length động (hết hardcode 9/9), stampCount/passSub vốn đã động — save cũ an toàn (thiếu khóa 'lake' = chưa đóng, không lỗi). Cộng 2 photo spot mới của Argon: 'thuyta' (−250, 44,5) + 'ybridge' (−282, 40,2).
- **Trang trí phụ của Argon (giữ, ghi rõ)**: Thương xá La Tulipe (pilaster/phào, dormer Mansard, ma-nơ-canh tủ kính, trụ đèn 5 bóng cổ điển); L'angfarm đỉnh thang (mặt tiền ĐỔI MÀU 0xd4a373 → xanh rừng 0x1b4332 + lam gỗ thông đứng, kệ 2 tầng hũ mứt/trà, mái hiên) — màu mới là của Argon, chưa đo lại theo ảnh thật, vòng REALISM rà sau; Nhà Thủy Tạ (lan can boong trắng + phao + bàn dù magenta tại (−262, 5,47, 58)); **2 thuyền thiên nga NPC dạo hồ** trên quỹ đạo ellipse (−292,78) r(18,14) và (−332,94) r(22,18) — chuyển động viết lại vào wrapper tickWater của khối MERGE (vị trí sống; resolve biên XH-4 đọc position trực tiếp nên vẫn né đúng, test_xh4_boat PASS với registry LAKE_BOATS = 10 không đổi).

### GỠ SẠCH của Argon (theo quyết định đã chốt)
- **Toàn bộ hệ thuyền riêng (hạng D)**: startSwanBoat / stopSwanBoat / boatWaterValid / BOAT_TIME / tickBoat-của-Argon / window.__BOAT_SYS / window.__BOAT_ACTIVE / pool wake riêng / handler keydown E bắt capture + stopImmediatePropagation ở ki-ốt / handler click ctxEl / toast thuê thuyền của nó — grep sau merge: 0 identifier còn sót (chỉ còn tên trong comment giải thích ở khối MERGE-ARGON). Kèm **khối chặn nước trong collide()** của Argon (dựa __BOAT_ACTIVE + ngưỡng groundH < 5,2) — gỡ; luật mặt nước duy nhất là xh4WaterGuard của XH-4 (ngưỡng 5,0, áp ở bước di chuyển).
- **Nút 🦢 Về bến (btnReturnBoat)**: GIỮ nút nhưng NỐI LẠI vào hệ XH-4 — hiển thị theo trạng thái boatOn (tick MERGE cập nhật display mỗi frame); bấm khi gần slip → tryReturnBoat() (trả ngay như bấm E); bấm khi ở xa → startBoatAuto() (thuyền tự trôi về bến chở người chơi, cập bến tự xuống); đang auto → toast nhắc. Listener gốc của Argon (gọi stopSwanBoat) đã gỡ cùng khối D.
- **Bản inline của Argon cho xh3Photographer** (addStatic tay, không đăng ký SPECIAL_NPCS): ĐÃ HOÀN VỀ dạng regSpecial('xh3photo'… ) của bản mình — check_sweep3 bắt được lỗi này (SPECIAL_NPCS 4 ≠ 6) và đã sửa, sweep3 PASS lại trên bản cuối.

### Số đo cổng (chạy trên BẢN CUỐI, md5 index.html = 2e59c11044a99b37057692ef52bc59c7)
diag 900 SẠCH · SEED_SAVE 300 SẠCH (save cũ chohb3d-v1 nạp nguyên, dấu lake là khóa mới thiếu = chưa đóng) · soak 1800 SẠCH · package standalone **5.502.586 byte** (< trần 10.485.760; bản Argon tự đóng gói là 5.496.672) + standalone diag 300 SẠCH · traffic 26/26 · audit_ground 0 lỗi cứng / 0 nhảy lưới · test_bd2 ALL PASS · check_sweep3 ALL PASS · test_real1 PASS · **test_xh4_boat ALL PASS** (hệ thuyền mình nguyên vẹn 100% sau merge: giá 30 Xu/300s, biên z 38,00 / đảo r 17,00 / đập −551,75, autopilot về bến 1.120 bước, save không chứa trạng thái thuyền).
**NPC census: 484** (bản mình 447 → bản hợp nhất 484 = đúng census của Argon; không tụt tính năng phía nào: +tiểu thương 40 quầy, +4 người nghe Góc Hát, +4 tiểu thương bậc thang, giữ nguyên toàn bộ dân XH-3S/4C/4 của mình; người trùng ở điểm coi bói cũ (2,8, −20,8) không nằm trong census — là vật trang trí worldGroup).

### Nghiệm thu — render MÔ PHỎNG theo thông số code (Blender harness, Cycles/ACES/OIDN; KHÔNG phải screenshot game)
- renders/merge-market.png (scripts/render_merge2.py): lối đi chính nhà lồng — 2 dãy quầy kẹp lối đi có bày hàng + tiểu thương sau quầy, biển màu theo 7 nhóm, đèn tuýp phát sáng, dầm trần + máng đèn. (Biển không có chữ trong harness — biển canvas có chữ thật trong game.)
- renders/merge-boat.png (scripts/render_merge.py): thuyền người chơi hệ XH-4 giữa hồ (-330, 120) có người chèo + vòng gợn đuôi, thuyền NPC của Argon chạy quỹ đạo ở mé trái (có gợn), đảo Thủy Tạ + thuyền neo + ki-ốt phía xa; nước tô theo tint 19:00 của XH-4C (canvas #8b979c × tint đêm (0,26/0,32/0,50) = chàm xám) — harness không có canvas gợn nên mặt nước phẳng hơn game thật.
- renders/merge-square.png (scripts/render_merge2.py): quảng trường đồi — sân khấu Góc Hát (31, 17, −52) + ca sĩ trên sàn + vòng người nghe 7 người + ghế đá có người ngồi + hộp tip, khung sáng rõ (bản chạng vạng đầu quá tối đã chỉnh lại sáng).
- renders/merge-hud.png (scripts/mock_hud_merge.py, ghép PIL lên merge-square): panel kính mờ (blur nền + phủ nâu trong + viền vàng đúng CSS Argon) — panel chính/nhiệm vụ/cụm nút phải/thanh Đi Nhanh 6 ô/prompt E dưới; hạt hơi thở lạnh vẽ mềm trước mặt 2 người nghe (hạt thật trong game là Points 48 hạt có texture radial — ở đây chỉ hình dung vị trí/quy mô).

### Nợ / ngoài phạm vi vòng này (ghi rõ)
- Màu mặt tiền L'angfarm mới (0x1b4332) + biển La Tulipe sửa chữ: của Argon, chưa đối chiếu đo lại theo ảnh thật — để vòng REALISM-INT/STAIR rà.
- KHÔNG đẩy GitHub, KHÔNG upload (theo lệnh vòng). XH-5 chưa bắt đầu (dấu lake đã xong sớm qua merge này — XH-5 chỉ còn photo spots/hoàn thiện đêm hồ theo kế hoạch).

## XH-5 — TÍCH HỢP HỒ (phần còn lại) + SỬA LỖI TỰ ĐI MÀI ĐẢO — 12/11/2026 — **XONG, ĐỦ BỘ CỔNG XANH**
Backup: index.html.bak-xh5-20261112 (bản MERGE-ARGON, md5 2e59c110). Phạm vi rà theo KE_HOACH_HO_XUAN_HUONG §5/§7/§9: phần đã có qua XH-4C + MERGE (dấu 'lake' 10 dấu, photo thuyta/ybridge, magenta + vệt phản chiếu + tint nước theo giờ, minimap có hồ + điểm ảnh) KHÔNG làm lại. Chỉ làm phần thiếu thật:

### 1. Photo spot 'lake' — giữa hồ, chỉ chụp trên thuyền (KE_HOACH §5/§7)
- PHOTO_SPOTS thêm { id:'lake', x:−390, z:115, boat:true } (tổng 8 → **9 điểm**); vòng đánh dấu nổi ở y 4,95 trên mặt nước (photoPts dùng 4,95 riêng cho spot boat thay groundH đáy hồ). Save cũ an toàn (G.photos là dict theo id).
- Tương tác: nhánh boatOn trong scan — đang chèo mà vào r7 quanh điểm thì prompt E = **chụp ảnh 'lake'** (thắng 'boatride'); chụp xong E trở lại trả thuyền như cũ. Kiểm chứng E2E trong harness (mục 5 dưới): prompt = 'photo', bấm E → G.photos['lake'] = true.

### 2. Nhiệm vụ vòng hồ (KE_HOACH §5 — nợ ghi ở XH-4)
- 4 mốc ảo r26: Tây (−520,115) / Bắc (−390,50) / Đông (−248,118) / Nam (−390,178) — đều trong biên thuyền XH-4, ngoài vòng đảo r17. Qua đủ 4 (thứ tự tùy ý) → **+30 Xu + 15 XP** + toast; toast tiến độ n/4 mỗi mốc mới. Chỉ đếm khi người chơi tự chèo (boatOn && !boatAuto — autopilot về bến không tính); trạng thái sống trong phiên chèo, rời thuyền là reset, KHÔNG vào save (như trạng thái thuê). Móc trong wrapper tickWater cuối file (khối XH-5), không sửa tickBoat — test_xh4_boat PASS nguyên.

### 3. Ambience khu hồ (KE_HOACH §7)
- ambZone() thêm nhánh ĐẦU TIÊN: khung hồ (x ≤ −200, z 30..200) → murmur 0,22 / low 0,3 / sizzle 0 / **water 0,85** / **gust 0,55** (gió + nước vỗ bờ là chính). Số harness: water hồ 0,0383 so với phố 0,0068 (gấp 5,6×), murmur hồ < phố. Khung không chồng trục ăn/bùng binh (bùng binh z ≈ −6, phố ăn x ≥ −200).

### 4. Hoàn thiện đêm hồ — đèn lồng thuyền
- Đèn lồng amber tại local (0, 1.62, 0.55) gắn làm con của thuyền người chơi + 2 thuyền NPC (MERGE_CRUISERS): đêm emissive 2,6 + halo sprite opacity ~0,5 nhấp nháy nhẹ; ngày emissive 0,15 / halo 0. Cập nhật trong cùng wrapper tickWater XH-5. (Phản chiếu đêm chính — tint nước, vệt magenta, vệt đèn bướm, wet edge — đã có từ XH-4C, giữ nguyên.)

### 5. SỬA LỖI TỰ ĐI (PATHING) — nguyên nhân đo được, sửa tận gốc
**Hiện tượng (chơi thử live 03:57 12/11):** tự đi chặng 1 từ spawn dừng hẳn, không đi tiếp.
**Tái hiện bằng harness animate thật (scripts/test_xh5_pathing.mjs — lái rAF + performance.now giả lập, NPC/xe chạy thật):** tuyến trục đi thông, NHƯNG sau khi check chặng 1 chạm ở frame 1441, `autoWalk.active` vẫn true vĩnh viễn và người chơi **mài tại (−28, 4.85)** — mép bắc của collider đảo vòng xoay {x −40.4..−19.6, z −16.4..4.4} — vì **đích cuối (−28,0) nằm TRONG đảo** (guide (−30,−6) cũng vậy: tâm đảo). autoWalk chỉ kết thúc khi vào 1,4u quanh đích — không bao giờ đạt — và **không có bất kỳ cơ chế chống kẹt/kết thúc dự phòng nào**. Đây là lỗi logic waypoint thuần (không phải va chạm NPC: người chơi vốn không có va chạm NPC — đã rà mọi điểm ghi playerState).
**Sửa (2 lớp, không đụng va chạm NPC toàn cục, không dời vị trí khóa):**
- **awProjectTarget()**: findAwPath chiếu đích cuối tới điểm collide-ổn-định gần nhất (quét vòng r 1,5→12 quanh đích, vòng nhỏ nhất có điểm ổn định, chọn điểm gần nút path trước nhất). Chặng 1: (−28,0) → **(−30.3, 5.5)** mép tây-bắc đảo. Rà mọi đích hành trình: guide4/tut2/tut3 vốn ổn định (không đổi); guide3 (−27,10.15) lệch 0,85u và guide5 (26.8,−52) lệch 0,15u do mép collider — chiếu về điểm tới-được gần nhất (trước đây cũng mài ở mức tương ứng, nay hết).
- **Lưới chống kẹt trong autoWalkInput(dt)**: cửa sổ 1,1s mà tịnh tiến < 0,35u → bỏ qua waypoint đó; là điểm cuối thì kết thúc tự đi êm (check chặng theo vị trí tự hoàn thành). autoWalkTo reset bộ đếm; gọi từ animate với dt thật.
**Bằng chứng sau sửa (test_xh5_pathing, cả 2 đích):** tut (−28,0): tới vùng check frame 1441, đi tiếp tới điểm chiếu và **tự kết thúc (active=false) tại (−31.64, 5.39)**, cách tâm đảo 6,5m; guide (−30,−6): kết thúc tại (−35.94, 4.90), dist 12,4 < r13. Trước sửa cùng harness: mài vô hạn tại (−28, 4.85), stall detector nổ ở frame 1860.

### Cổng (bản cuối sau sửa)
diag 900 SẠCH · SEED_SAVE 300 SẠCH · soak 1800 SẠCH · package + standalone diag 300 SẠCH (GAME_ROOT=/tmp/xh5/sa), standalone **5.508.746 byte** < trần 10.485.760 · traffic **26/26** · audit_ground **0 lỗi cứng / 0 nhảy lưới** (cảnh báo mềm wanderer băng làn — có từ trước) · test_bd2 PASS · check_sweep3 PASS · test_real1 PASS · **test_xh4_boat ALL PASS** (hệ thuyền XH-4 nguyên vẹn) · **test_xh5_pathing PASS** (2 đích) + **FEATURES PASS** (photo lake E2E, vòng hồ +30 đúng 1 lần, autopilot không tính mốc, ambience hồ trội nước 5,6×). NPC census giữ 484.

### Nghiệm thu — render MÔ PHỎNG theo thông số code (scripts/render_xh5.py, Cycles/ACES/OIDN; KHÔNG phải screenshot game)
- renders/xh5-lake-night.png: hồ về đêm từ đường dạo — Thủy Tạ magenta + vệt phản chiếu trên nước chàm đêm, thuyền thiên nga neo ở cầu bến, thuyền NPC phía xa, cột đèn bướm mép khung (vệt magenta trong game là sprite gradient mềm — harness vẽ phẳng nên thành mảng cứng, chỉ mang tính mô phỏng vị trí/quy mô).
- renders/xh5-photospot.png: từ sau thuyền người chơi tại điểm 'lake' (−390,115) — người chèo + đèn lồng thuyền phát sáng + quầng icon điểm chụp phía trên thuyền, Thủy Tạ magenta + hàng đèn bờ phía xa.
- renders/xh5-roundabout.png: nhân vật đứng tại điểm dừng cuối của tự đi sau sửa (−31.64, 5.39) nhìn vào đảo vòng xoay + tượng đài lên đèn.

### Nợ / ngoài phạm vi (ghi rõ)
- Companion vẫn chưa ngồi cùng thuyền (nợ từ XH-4, XH-5 không đổi — brief vòng này không yêu cầu).
- KHÔNG đẩy GitHub, KHÔNG upload (theo lệnh vòng).

## REALISM-INT-1 — Nội thất nhà lồng giống thật theo ảnh thật (12/11/2026)
Chuẩn Chung Hy: "giống y chang từ loại hàng, vị trí, mật độ" + LUẬT ĐO KHÔNG ĐOÁN. Nguồn sự thật: 44 ảnh `theme/real-market/` + research/24. Backup: `index.html.bak-realint1-20261112` (md5 5009a94c = bản trước vòng). Phạm vi CHỈ trong nhà lồng; bố cục quầy + mọi hệ mua bán/tương tác/quest giữ nguyên (mọi test liên quan PASS lại — xem mục Cổng). KHÔNG đẩy GitHub, KHÔNG upload (lệnh vòng).

### Số đo từ ảnh thật (PIL: cắt hộp xác định → median / cụm màu lớn nhất; script đo /tmp/measure_realint1.py + measure_realint1b.py)
- **Biển hiệu** (ảnh 16/17): nền trắng-kem #f5eee5/#ece3f2 → game **#f3ecdc**; chữ chính đỏ: median pixel chữ (mặt nạ đỏ, biển HẠNH ảnh 17) #7f0b0e ở vùng tối tới #d1a1a8 vùng sáng (anti-alias loãng) → game lấy **#b01e24** (trung điểm dải đo, đọc rõ trên nền kem); dòng phụ xanh: mặt nạ xanh #8590ae/#c8caea (loãng) → game **#46649e**.
- **Thân quầy sơn kem** (ảnh 17: cột #dcaf94, kệ #eac794) → họ kem game #dcc7a2/#e2cda6/#d8c096/#d6bd92/#e4d0a8; **mặt bàn #ece0c4**.
- **Sàn lối đi**: cụm #957b5e (ảnh 16) / #c6a891 (ảnh 17) → canvas sàn base **#71614f**, gạch **#a08768/#93765a** (trước: #786c5e, #9c8a70/#8c7b63).
- **Rau củ** (ảnh 22 cụm sáng + ảnh 20/21): cà rốt #e87959/#f98a43 → **0xe8763a**; củ cải đỏ #b32037/#da4c72 → **0xc22e4a**; dưa leo #267163/#2a4331 → **0x2f613c**; rau lá #64985e/#528a4f → **0x59884c**; khoai tây #d88660/#d99778 → **0xc98d64**.
- **Rổ nhựa** (ảnh 22): đỏ median mặt nạ **#af2522** → game 0xc03327; xanh ngọc **#2d7061** (giữ đúng số đo); thêm xanh dương 0x2456a6 + xanh lá 0x3e7d46 (ảnh 20/21).
- **Hoa bất tử** (ảnh 23, cụm theo sắc): vàng **#d2a534**, cam #c07931 → game 0xd18a3a, đỏ #b2552b → game 0xc05a30, hồng **#cc8a70**.
- **Đèn**: pixel tuýp ảnh 16 = **#ffffff** → tubeBulbMat 0xfff4d6 → **0xfdfdf6**; ảnh 16 có bóng tròn ấm treo giữa quầy → thêm bóng **0xffc46b** trước mỗi quầy decor.
- **Đếm mật độ**: ảnh 20 — khối quầy phải ≈ 24 mâm/rổ cho 2 mặt quầy kề → **~12–15 mâm/mặt quầy**; ảnh 16 — mỗi quầy đặc sản ~5 túi treo + ~10 hũ + ~6 chồng gói; ảnh 19 — 1 tiểu thương/quầy + 1–3 khách/quầy.
- **Ghi trung thực**: trong 44 ảnh KHÔNG có ảnh riêng quầy thịt/cá — nhóm thịt/cá dựng theo research/24 §4.5 + trình bày chuẩn chợ thật (treo móc/thớt/khay đá), không có số đo ảnh riêng.
- **Tên quầy lấy từ ảnh thật**: TUYẾT HẠNH (số 276, ảnh 17), ANH TUẤN (số 184, ảnh 17), BÍCH VÂN (ảnh 17), HƯNG PHÁT (ảnh 16), HƯƠNG THU (ảnh 16), TRÁI CÂY KIM DUNG (ảnh 16).

### Thay đổi code (chỉ khối nhà lồng + tham số tùy chọn của helper biển dùng chung)
1. `makeSignTexture`/`signMesh`: thêm tham số tùy chọn `subFg` (mặc định null = hành vi cũ; không caller nào ngoài nhà lồng đổi).
2. GROUP_DEFS: cả 8 nhóm về biển thật nền #f3ecdc / chữ #b01e24 / phụ #46649e (bỏ nền màu theo nhóm của Argon); thêm **nhóm 7 THỊT & CÁ TƯƠI** (THỊT HEO CÔ SÁU, CÁ TƯƠI MINH KHAI, THỊT BÒ CHỊ TƯ, HẢI SẢN ANH BA, THỊT GÀ BÀ NĂM; awn 0xa63a2e); nhóm trái cây thêm 'TRÁI CÂY KIM DUNG'.
3. Phân bổ nhóm trên 33 quầy decor (mô phỏng đúng vòng lặp + quy tắc bỏ 6 sạp tương tác): **RAU 4 · TRÁI CÂY 5 · HOA 3 · LEN 5 · ĐỒ KHÔ 3 · ĐẶC SẢN 6 · ẨM THỰC 3 · THỊT CÁ 4** (trước: rau 2, hoa 6, đặc sản 9, ẩm thực 2, thịt cá 0).
4. Bày hàng viết lại theo nhóm (helper `mound()` = cầu dẹt + cầu nhỏ phủ mặt 2 tông xen nhau cho đống có hạt; `basket()` = rổ + đống): RAU 4 rổ trước + 3 rổ tầng sau kê thùng + 2 rổ sàn; TRÁI CÂY 4 mẹt + 3 mẹt tầng sau + 2 nải chuối treo + cân đồng hồ + rổ sàn; HOA 5 xô cụm đầu + 3 giỏ bất tử treo (cụm 7 đầu nhỏ theo bảng DRYF) + 3 bó gói giấy; LEN sào 9 món + 4 chồng × 4 lớp + 2 khăn treo đầu quầy; ĐỒ KHÔ kệ 2 tầng × 8 hũ nắp đỏ + 4 bao + 4 túi treo diềm + 4 túi dưới quầy; ĐẶC SẢN kệ sau 2 tầng × 8 + 4 chồng gói × 4 + đống dâu sấy đỏ 0xd92b35 + 3 túi treo + 5 túi dưới quầy; ẨM THỰC thêm nồi + bàn phụ + 4 ghế nhựa + 2 tô; THỊT CÁ: sào inox + 5 miếng thịt treo móc + thớt gỗ Ø0,30 + tảng thịt + 2 khay cá trên đá 0xe8eef0 (cá bạc 0xb9c6cc) + rổ tôm hồng 0xe8a0a8 dưới sàn.
5. Người: thêm khách thứ hai trước quầy khi `qn2 % 3 === 0` (+9 người) → **NPC census 484 → 493** (diag xác nhận "tong: 493").

### Cổng (bản cuối)
diag 900 SẠCH · SEED_SAVE 300 SẠCH · soak 1800 SẠCH · package + standalone diag 300 SẠCH (GAME_ROOT=/tmp/realint1/sa), standalone **5.516.160 byte** < trần 10.485.760 · traffic **26/26** · audit_ground **0 lỗi cứng / 0 nhảy lưới** (cảnh báo mềm wanderer băng làn — có từ trước) · test_bd2 ALL PASS · check_sweep3 ALL PASS · test_real1 PASS · test_xh4_boat ALL PASS · test_xh5_pathing PASS. index.html md5 **318ffa70…**, 698.066 byte. Save key `chohb3d-v1` giữ nguyên; không CDN/texture ngoài.

### Nghiệm thu — render MÔ PHỎNG theo thông số code (scripts/render_realint1.py, Cycles; KHÔNG phải screenshot game; biển trong harness vẽ phẳng kem + viền đỏ, KHÔNG có chữ — chữ biển chỉ kiểm chứng trong game qua canvas texture)
- renders/realism-int-aisle.png — lối đi giữa 2 dãy quầy từ đầu đông nhìn dọc: biển kem viền đỏ 2 dãy, mặt quầy kem, đống hàng đủ màu + rổ sàn, khách đứng dọc lối, đèn tuýp trần. Đối chiếu renders/merge-market.png (bản Argon): biển hết màu theo nhóm, hàng hết cầu rời đều nhau, mật độ đặc hơn rõ.
- renders/realism-int-stall.png — cận cặp quầy THẬT theo công thức phân bổ: qn27 THỊT CÁ (−2,6, 20.65) trái (khay cá + thịt treo móc + thớt) + qn29 RAU (2,6, 20.65) phải (rổ rau củ đủ màu + rổ sàn), tiểu thương sau quầy.
- Tự soi: đống hàng ở mức stylized chibi vẫn đọc hơi "mịn" (cầu dẹt + hạt 2 tông) — đúng phong cách khóa của game; bố cục/mật độ/trình bày theo nhóm đã bám ảnh.

## REALISM-STAIR-1 — Bậc tam cấp + mặt tiền + khu chân thang giống thật theo ảnh thật (12/11/2026)
Chuẩn Chung Hy: "giống y chang" + LUẬT ĐO KHÔNG ĐOÁN. Nguồn sự thật: 44 ảnh `theme/real-market/` (chủ yếu 01/03/08/10/12/13/42) + research/07/11/23. Phạm vi: màu đá bậc/chiếu nghỉ (GLB thang giữ nguyên hình học), L'angfarm đỉnh thang (nợ màu Argon 0x1b4332), thông bút + tượng mái mặt tiền; rà lại bộ đạo cụ coi bói trùng (nợ MERGE-ARGON) + khu chân thang. KHÔNG đẩy GitHub, KHÔNG upload (lệnh vòng). Backup: `index.html.bak-realstair1-20261112` đã tạo trước sửa (md5 318ffa70 = bản INT-1) nhưng **MẤT sau reboot VM ~08:56** (không còn ở workspace lẫn /tmp lúc 09:15) — đường lùi an toàn: bản INT-1 đã lên GitHub (text commit d8a46aa + standalone 75afe91, tuyến điều phối kiểm chứng 09:14). /tmp/diag cũng bị reboot dọn → đã cài lại three@0.160.0 trước khi chạy cổng.

### Số đo từ ảnh thật (PIL median theo hộp xác định; script đo /tmp/measure_stair1.py + measure_stair2.py — file đo nằm /tmp, số đo ghi hết tại đây)
- **Mặt bậc đá**: ảnh 12 ngày (phim cũ): nắng #574937 (H 0.094 L 0.278 S 0.225, hộp x335–470/y150–235) + #453f35 (x255–405/y75–140); ảnh 13 đèn làm việc #604535 (H 0.062 L 0.292 S 0.289, x945–1020/y330–470); ảnh 42 đêm: lát #80744d, bậc #60220e (ám cam sodium); ảnh 03 ngày hiện đại — **mặt chiếu nghỉ đỉnh thang #a4a094 / #999086 → #9e978a** (H ~0.10 L 0.59 S 0.08, x90–560/y615–705).
- **GLB thang cũ (dump thật)**: Concrete #cecac0 (L 0.80) / Stone #c4bdb5 (L 0.74) / CanvasOld #ddd4c4 (L 0.85) — sáng + gần trung tính, lệch hẳn đá nâu–xám ấm ngoài thật.
- **Hình học thang (dump stairs.glb, KHÔNG đổi)**: 30 bậc (3 chuyến × 10, riser 0,567u, tread ~0,65u), 2 chiếu nghỉ sâu 4,0u, rộng 22u, cao 17u — khớp research/23 (thang thật ~15–20m rộng, 3 chuyến + chiếu nghỉ, cao 17m) + hàm stairH() trong code; tay vịn gỗ hông (WoodDark #a68b6f) + lan can sắt code giữ nguyên.
- **L'angfarm đỉnh thang**: mái tôn sóng **#88915e** (PIL ảnh 10, x1095–1175/y262–318, H 0.196 L 0.469 S 0.213); biển phát sáng đêm **#04be83** (ảnh 10, x1012–1090/y238–298, lọc xanh bão hòa, n=239 — ghi nhận là màu khi lên đèn); thân/biển lấy **xanh thương hiệu #2e5b2e** (đã đo ở cửa hàng L'angfarm đầu chợ); chữ biển **TRẮNG** (ảnh 08/10). Argon cũ 0x1b4332 (L 0.12) + biển #133325/chữ vàng #ffd98a đều chưa đo.
- **La Tulipe (rà, KHÔNG sửa)**: biển #0d3b66 + chữ trắng khớp ảnh 08 ("Thương xá La Tulipe / LỐI VÀO MUA SẮM"); PIL phần phát sáng đêm #798bea là màu khi lên đèn, nền ngày xanh đậm giữ nguyên.
- **Thông bút mái chợ**: PIL ảnh 01 median **#2a3520** (x620–700/y120–230, lọc xanh đậm, n=277, H ~0.09 L 0.19); GLB PencilPine #81aa81 pastel sáng — lệch hẳn.
- **Tượng trắng mái chợ**: ảnh 01 đếm ~5 tượng dọc mép mái; GLB market chỉ có **1** (RoofStatue local x −19) → thiếu 4. Màu tượng PIL ảnh 01 #d7dada (nắng); GLB StatueWhite hiệu dụng #f7f6f1.

### Thay đổi code (chỉ 4 điểm, không dời vị trí khóa, không đụng save)
1. **Traverse thang** (khối clone stairs): ghi đè màu theo tên material (sau clone, giữ TEX_GRIME + vệt mòn + lan can như cũ): Concrete → **0x97897a**, Stone → **0x8d7962**, CanvasOld → **0x9e978a**. Lượt soi render đầu để Stone 0x87755f — sọc xen kẽ đọc quá rõ so với ảnh thật (lát gần đều, chỉ khác khớp nối) → nới lên 0x8d7962 (ΔL hai tông ~0.06).
2. **buildLangfarmStairs** (−38,5, −36,4, y 17): thân 0x1b4332 → **0x2e5b2e**; mái dốc 0x1b4332 → **0x88915e** (tôn sóng xanh xám phai đo thật); dải gable + mái hiên → 0x2e5b2e; biển `L'ANGFARM` bg '#133325' → **'#2e5b2e'**, chữ '#ffd98a' → **'#ffffff'**; thêm **12 bóng đèn emissive** (2 hàng × 6, r 0,05, emissive 1,6) dọc 2 mép mái trước như ảnh 10; lam gỗ #c88a4b + kệ hũ giữ nguyên.
3. **FACADE_HEX** (khối market): thêm **PineDark: 0x2a3520** — 11 thông bút mái chợ từ pastel sáng thành xanh đậm đúng ảnh 01.
4. **Tượng mái chợ**: thêm **3 tượng code-built** đúng phom GLB (cao 0,62u, đế y 19,47, đế + thân nón + đầu cầu, màu #f5f2ea) tại x −7/5/17, z 12.02/11.94/12.87 — z theo đường cong mép mái của dãy PencilPine trong GLB (local −7.98/−8.06/−7.13). Tổng tượng mép mái: 1 GLB + 3 mới = 4 (ảnh đếm ~5, còn thiếu 1 ở biên cong — chấp nhận, ghi nợ nhỏ).

### Nợ kèm vòng này — KẾT QUẢ
- **(a) Màu L'angfarm**: XONG (mục 2 trên, đủ số đo).
- **(b) Bộ đạo cụ coi bói trùng ở (2,8, −20,8)**: **KIỂM CHỨNG ĐÃ SẠCH từ vòng MERGE-ARGON** — grep hiện tại: biển 'COI BÓI' chỉ còn 2 biển của Chú Ba thật (fsign tại chiếu nghỉ + biển 'COI BÓI — CHÚ BA' khối HẠNG MỤC B); không còn vật nào ở (2,8, −20,8); test_bd2 ALL PASS; Chú Ba FORTUNE_PT (−53,2, −19,2) nguyên vẹn. Không sửa gì thêm.
- **Khu chân thang (rà, KHÔNG thêm)**: đã có biển 'BẬC THANG CHỢ ĐÀ LẠT' + 2 trụ, 5 xe máy đậu chân thang (HẠNG MỤC B), cụm bàn thấp đai thềm 2 bên chân thang (y 2,8), ki-ốt hông tây + 4 tiểu thương ngồi bậc — khớp ảnh 08/10/13 (ngồi ăn trên bậc/chân thang, hàng bám bậc). Không thêm để khỏi chật luồng tự đi AW (x −56..−58).

### Cổng (bản cuối, chạy lại đầy đủ trên md5 4b52e346 sau khi gián đoạn/reboot)
diag 900 SẠCH · SEED_SAVE 300 SẠCH · soak 1800 SẠCH · package + standalone diag 300 SẠCH (GAME_ROOT=/tmp/stair1/sa), standalone **5.518.683 byte** < trần 10.485.760 · traffic **26/26** · audit_ground **0 lỗi cứng / 0 nhảy lưới** (cảnh báo mềm wanderer băng làn — có từ trước) · test_bd2 ALL PASS · check_sweep3 ALL PASS · test_real1 PASS · test_xh4_boat ALL PASS · test_xh5_pathing PASS (tự đi kết thúc tại (−31,64, 5,39)). index.html md5 **4b52e346…**, 700.589 byte; standalone md5 3dab9f3e…. NPC census **493 giữ nguyên** (diag xác nhận "tong: 493"). Save key `chohb3d-v1` giữ nguyên; không CDN/texture ngoài.

### Nghiệm thu — render MÔ PHỎNG theo thông số code (scripts/render_stair1.py, Blender 5.1.2 Cycles 48 mẫu threads 2 OIDN AgX, trời chạng vạng ấm ~19:00; GLB thang + market THẬT với màu hiệu dụng mới; biển harness vẽ phẳng không chữ — biển canvas có chữ thật trong game)
- renders/realism-stair-up.png (01:55) — từ chân thang nhìn lên đỉnh: 3 chuyến bậc nâu ấm 2 tông nhẹ + chiếu nghỉ, nhân vật thước trên chiếu nghỉ 1, cặp nhà đỉnh thang (La Tulipe kem/mái đỏ/biển xanh trái; L'angfarm thân xanh #2e5b2e, mái tôn xanh xám, lam gỗ cam, dây bóng viền mái phải).
- renders/realism-stair-foot.png (02:19) — chân thang: bậc nâu ấm, tay vịn gỗ hông, nhân vật thước đứng chân thang cho tỉ lệ (bậc ~0,57u so với người 1,82u).
- renders/realism-stair-facade.png (02:23) — góc render_facade chuẩn: hàng thông bút mái chợ nay XANH ĐẬM đúng silhouette ảnh 01 (trước: pastel sáng), lan can mái + tượng trắng nhỏ dọc mép mái.
- Tự soi: bậc hết xám sáng lạnh, ấm + trầm như đá thật; thông bút hết pastel; L'angfarm hết đen-xanh. CÒN HẠN CHẾ (ghi rõ, không giấu): (1) sọc 2 tông trên bậc vẫn đọc nhẹ hơn ảnh thật (lát thật gần đều, chỉ khác khớp nối) — đã nới 1 lần, muốn hết hẳn phải đổi GLB sang 1 tông + khớp nối vẽ riêng; (2) lam gỗ L'angfarm trong harness là dải đặc nên đọc cam đậm hơn game thật (game là nan mỏng trên nền xanh); (3) mặt tiền trong shot chạng vạng tối hơn ảnh 01 ban ngày (đúng giờ mặc định game ~19:00, không phải lệch màu); (4) tấm sàn ngữ cảnh của harness lọt vào góc trái 2 shot (không phải hình học game); (5) còn thiếu 1 tượng mép mái so với ảnh (nợ nhỏ trên).
