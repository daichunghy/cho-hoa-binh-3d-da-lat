# Kế hoạch — Chợ Hòa Bình 3D Đà Lạt

Nguyên tắc của Chung Hy: plan trước, làm kỹ, tự review rồi mới báo. Mọi mô hình/khu vực phải đối chiếu tư liệu thật của khu Hòa Bình — Chợ Đà Lạt (xem `research/07-cho-hoa-binh-that.md`).

## Giai đoạn 0 — Nghiên cứu (đang chạy)
10 tuyến nghiên cứu song song trong `research/`:
1. niemphat.online
2. chuasen.online
3. Sansa (Hàn Quốc) + làn sóng Threads/TikTok/Facebook
4. Địa ngục online — tham khảo cấu trúc hành trình nhiều khu
5. Toàn cảnh chùa online + mạng xã hội
6. Chợ ảo & bố trí hàng quán trong thế giới ảo
7. Tư liệu thật: khu Hòa Bình — Chợ Đà Lạt
8. Gamification & retention
9. Cơ chế mua đồ ăn / nước uống trong game và nối ra mua thật
10. Kỹ thuật web 3D (engine, hiệu năng mobile, multiplayer)

Đầu ra: bản tổng hợp thiết kế (design doc) chốt: bản đồ chợ, danh sách khu/quầy, tính năng v1.

## Giai đoạn 1 — Prototype đi dạo được
- Bản đồ khối (blockout) khu Hòa Bình: mặt tiền Chợ Đà Lạt, rạp Hòa Bình, vòng xoay, các trục đường quanh chợ.
- Nhân vật đi bộ được (bàn phím + chạm mobile), camera mượt, phong cách low-poly cartoon, sương + ánh đèn vàng.
- 5–7 quầy hàng đầu tiên với NPC tiểu thương và biển hiệu.

## Giai đoạn 2 — Hàng quán + mua đồ ăn, nước uống
- Tới quầy → mở menu → gọi món → hoạt cảnh chế biến/ăn uống → trừ tiền ảo, tăng điểm vui.
- Quầy mẫu: sữa đậu nành nóng, bánh tráng nướng, cà phê vỉa hè, kem bơ, chè, dâu tây & mứt đặc sản.
- Giỏ đi chợ: tổng kết chuyến đi thành thẻ "thực đơn Đà Lạt của bạn" để chia sẻ.
- Đồ lưu niệm/đặc sản: giỏ hàng riêng, đặt trước/affiliate là bước nối sau khi có traffic.

## Giai đoạn 3 — Giữ chân & sự kiện
- Chợ sáng / chợ đêm theo giờ thật (đèn lồng, hàng ăn đêm mở theo giờ).
- Hộ chiếu đi chợ đóng dấu theo khu, nhiệm vụ ngày, sưu tầm món ăn.
- Nhiều người cùng hiện diện (multiplayer nhẹ kiểu Sansa), biểu cảm/động tác thay cho chat.

## Giai đoạn 4 — Ra mắt & viral
- Khoảnh khắc quay màn hình được: chợ đêm lên đèn, mưa sương, đoàn người đi chợ.
- Nội dung Threads/TikTok/Facebook: clip đi chợ 30 giây, thử thách "ăn hết chợ với 100 điểm".

## Trạng thái v3 (cập nhật 06/11/2026, 02:2x) — GÓI CHUYỂN ĐỘNG "CHỢ SỐNG"
Đã xong và kiểm chứng tĩnh (node --check đạt, HTTP 200 cho index + 11 GLB, standalone node --check đạt):
- **Đám đông di động: 30 NPC** khách đi dạo theo tuyến khép kín khắp 2 cao độ (vòng bùng binh, lên/xuống bậc thang, qua cầu nổi, trong nhà lồng, quảng trường đồi, dọc đường chợ đêm). Máy trạng thái: đi → dừng trước quầy ngắm/chỉ món 2,5–7s → đi tiếp. NPC xa người chơi >45m chỉ tịnh tiến (tắt vung tay chân) để giữ hiệu năng.
- **Mật độ theo giờ thật:** 17–22h = 100%, sáng = 80%, sáng sớm = 65%, khuya = 55%, trưa 11–14h = 45%; NPC ca đêm chỉ xuất hiện khi chợ đêm mở và ngược lại.
- **Tiểu thương có việc làm** — hoạt ảnh tay riêng từng quầy: khuấy (sữa, súp, chè), lật bánh (bánh tráng), rót (cà phê, đậu hũ), múc (kem bơ/dâu, bánh căn, yaourt), trở (khoai/bắp, xiên nướng), xếp hộp (đặc sản), cân hàng (rau, trà), xếp đồ (len, lưu niệm, đồng hồ), ôm hoa (quầy hoa). Đang nấu cho khách thì nhún + khuấy nhanh.
- **Môi trường động:** khói bếp liên tục + hơi nước ly phin; lồng đèn từng quầy đu đưa + nhấp nháy ấm (material riêng từng quầy); 5+1 dây đèn trang trí nhấp nháy; 4 cờ + 1 băng rôn "CHỢ ĐÊM ĐÀ LẠT — ÂM PHỦ" bay theo gió (biến dạng đỉnh); 6 mảng sương trôi chậm; góc hát quảng trường đồi (ca sĩ gảy guitar, 3 khán giả ngồi vỗ tay, pool 10 nốt nhạc bay) — diễn 17–21h/giờ thật hoặc khi chợ đêm mở, tương tác Nghe/Tặng Xu móc vào `stageState` ở đợt tính năng chính.
- **Prop riêng đã bật trên web:** vỉ nướng (Grill*) ở quầy bánh tráng, bộ phin + ly cà phê (Phin*) ở quầy cà phê — model GLB đã xuất từ trước (stall.glb 726.184B).
- **Bản standalone 1 file:** `prototype-v2/index-standalone.html` (7.554.203B, nhúng đủ 11 GLB base64; vẫn cần internet để tải Three.js từ CDN).

### ĐÃ HOÃN vì điều phối CPU (chỉ đạo 02:12 — ưu tiên render 2 video, deadline 06:12)
- Mọi render kiểm chứng Blender Cycles và dựng model mới nặng: hoãn tới sau 06:12 / khi có lệnh tăng tốc lại. Gói chuyển động này thuần code web nên không bị ảnh hưởng.
- Chưa kiểm chứng runtime bằng trình duyệt thật (môi trường chặn loopback như các đợt trước) — mới đạt kiểm chứng tĩnh + HTTP.

## Trạng thái v3 bổ sung (06/11/2026, ~02:35) — 5 TÍNH NĂNG LÕI ĐÃ HOÀN THIỆN
[index.html](sandbox://workspace/cho-hoa-binh-3d/prototype-v2/index.html) = 99.157 byte; standalone đóng gói lại 7.575.305 byte. Toàn bộ thuần code web (không Blender — tuân thủ điều phối CPU 02:12). Kiểm chứng: `node --check` đạt cho cả index + standalone; script kiểm tra tĩnh 9/9 PASS; smoke test logic trong Node đạt (đường cong nhiệt độ, 14 quẻ đều có hiệu ứng thật, giá bán 60%/luck ×1.5); HTTP 200 cho index + đủ 11 GLB; standalone giải mã đủ 11 GLB (magic glTF đúng, không còn đường dẫn assets/). **Chưa kiểm chứng runtime bằng trình duyệt thật** (môi trường chặn loopback như các đợt trước) — cân bằng số liệu dưới đây là theo thiết kế, cần chơi thử để tinh chỉnh.

1. **BÁN LẠI ĐỒ:** mỗi món trong Giỏ có nút "💰 Bán +X" = 60% giá mua (lưu `price` khi mua; món save cũ không có giá thì tính giá mặc định 10). Có buff 🍀 May mắn thì giá bán ×1,5. Bán xong cộng Xu, lưu save, giỏ tự vẽ lại.
2. **NÂNG CẤP (nút ⬆️ trên HUD / phím U):** Túi đồ 3 cấp (giỏ 8→14→20 món, 80/160 Xu — mua bị chặn khi giỏ đầy, có toast hướng dẫn), Giày leo đồi 3 cấp (tốc độ +0/15/30%, 70/150 Xu), Áo ấm 3 cấp (mất độ ấm chậm hơn 0/35/60%, 90/180 Xu), Sức bền 2 cấp (buff ăn/uống +0/50% thời lượng, 100 Xu). Lưu trong `state.upgrades` cùng save `chohb3d-v1`, có migration cho save cũ.
3. **NHIỆT ĐỘ LẠNH:** HUD hiện nhiệt độ theo giờ máy thật (nội suy theo mốc: 5h→12,5° · 9h→17,5° · 13–14h→22,5–23,5° · 19h→17° · đêm 13°; dao động nhẹ ±0,4°). Thanh **Độ Ấm** 0–100: mất 0,45/giây ban ngày, 0,72/giây ban đêm (nhân hệ số lạnh + áo ấm + buff Ấm bụng ÷4); hồi +13/giây khi đứng trong ~3,4m quanh quầy có khói/bếp; ăn/uống món nóng +40. Độ Ấm < 25: tốc độ ×0,7, nhân vật run (lệch sin 42Hz biên 0,018), hơi thở khói trắng 6 hạt theo nhịp, thanh ấm chuyển xanh lạnh + cảnh báo trên HUD. Sương mù (fog) dày thêm tối đa +0,0039 khi nhiệt độ xuống dưới 15,5°.
4. **COI BÓI:** NPC **Chú Ba** ngồi trên thảm đỏ + ghế đẩu ở chiếu nghỉ giữa bậc thang (landing y=11,33, x=2,8, z=−20,8; dựng bằng clone nhân vật + khối cơ bản trong code, có biển "COI BÓI — CHÚ BA", có collider). Tới gần → phím E → thoại chào → **20 Xu/quẻ**, kho **14 quẻ** viết sẵn (ăn uống/mua sắm/tình duyên/duyên chợ) mỗi quẻ kèm hiệu ứng thật: buff 🍀 May mắn 240–300s, buff chân/tỉnh táo/ấm, hồi Độ Ấm, hoặc +15–60 Xu. Đếm số lần coi bói trong Hộ chiếu.
5. **HÁT QUẢNG TRƯỜNG:** móc vào `stageState` sẵn có — tới gần sân khấu khi đang diễn (17–21h) → phím E → **Nghe hát**: lời 6 câu về Đà Lạt/chợ đêm chạy chữ 4s/câu dưới màn hình + **nhạc WebAudio thật** (oscillator triangle, giai điệu pentatonic 8 nốt, vòng 430ms/nốt, tự dừng khi hết suất diễn); **Tặng 10 Xu**: ca sĩ cảm ơn, khán giả vỗ tay nhanh gấp đôi trong 6 giây, người chơi nhận buff ⚡ Tỉnh táo 45s. Ngoài giờ diễn panel báo rõ lịch diễn.
- **Nguồn Xu đã cân bằng lại:** bắt đầu 300 · nhiệm vụ ngày +120 · **thưởng đủ 9/9 dấu hộ chiếu +150 (một lần)** · bán lại đồ (nguồn chính, lặp vô hạn) · quẻ Tài Lộc/Trúng Số/Cà Phê +15–60.
## Render kiểm chứng 05:24 ngày 06/11 (sau khi gỡ lệnh giảm render)
- Chạy lại render_check.py Cycles: 3 ảnh 01-overview/02-stall/03-character tại prototype-v2/renders/. Gian hàng + chibi soi trực tiếp ĐẠT (mái hiên, lồng đèn sáng, giỏ hàng, chibi mũ len/nón lá mắt chấm + má hồng đúng style).
- Phát hiện cần cải thiện ở đợt model sau: nhà lồng chợ (market.glb) nhìn từ trên cao là khối mái phẳng trơn + tường trống, chưa có chi tiết mái/cửa sổ/biển hiệu — camera diorama trong game cũng sẽ thấy nhiều phần mái này. Ghi vào backlog model v4: thêm gờ mái, ô sáng, biển hiệu mặt tiền cho market.glb.
- Ảnh 01-overview đã thử 3 góc máy khác nhau, góc nào cũng bị khối nhà lồng chắn — đây là hạn chế của ảnh render kiểm chứng, không phải lỗi game.

## Trạng thái V4 (06/11/2026) — CẢI THIỆN SÂU THEO ẢNH THẬT (research/11)
Chung Hy bác v3 ("làm ẩu, không chi tiết, không không khí đông đúc") → đợt V4 dựng lại theo hồ sơ ảnh thật. Checklist đầy đủ: [V4-CHECKLIST.md](sandbox://workspace/cho-hoa-binh-3d/prototype-v2/V4-CHECKLIST.md) (đã tick đủ theo bằng chứng). Kiểm chứng: node --check đạt cho cả index + standalone; **6 ảnh render Cycles tự soi đạt** tại prototype-v2/renders/ (v4-01 mặt tiền, v4-01b mặt đồi, v4-02 bùng binh+xe, v4-03 bậc thang đông, v4-04 sạp đêm, v4-05 khách sạn). Chưa kiểm chứng runtime bằng trình duyệt thật (môi trường vẫn chặn loopback/domain như các đợt trước) — cần Chung Hy chơi thử bản standalone để nghiệm thu cảm giác thật.
- **Nhà lồng dựng lại (market.glb 1.563.916B):** chữ nổi 3D "CHỢ ĐÀ LẠT" đỏ CẢ 2 mặt (mặt đồi chữ to hơn), dải zigzag trắng, dải lam trắng, băng hồng đào #D98E5F, dải biển quảng cáo nhiều màu + LED đỏ tầng trệt, sân thượng lan can kính/thông cột/tượng trắng, mặt đồi có THÁP THANG MÁY KÍNH xanh lá + bạt sọc xanh–trắng + cầu thang trắng ngoài trời + dải kính. Bắt được và sửa 1 lỗi thật qua render: chữ mặt tiền ban đầu quay ngược (rotation text) — đã sửa + build lại + render xác nhận đọc đúng.
- **Bùng binh:** tượng đài đá xám (bệ 3 bậc + 3 tượng người trừu tượng + thông đá 3 tầng), thảm hoa họa tiết 8 quạt, 4 ghế đá trắng + collider. Bố cục vòng khớp ảnh 04: đảo r6.9 / ghế 8.3 / người ~9.5 / moto 10.6 / ô tô 11.9.
- **Xe cộ MỚI (vehicle.glb):** xe máy chibi có người lái + bán tải; 5 moto + 1 ô tô chạy vòng bùng binh, xe đường trước chợ CHỈ chạy ban ngày (đêm đường Âm Phủ là phố đi bộ như thật), bánh quay theo tốc độ, đèn pha emissive + nón sáng ban đêm; **bãi xe ~46 chiếc** đậu dày trước chợ + cụm cạnh bùng binh.
- **Đám đông 85 NPC** (30 đi động cũ + 55 tĩnh theo cụm): 12 người NGỒI ĂN trên bậc thang (ghế nhựa xanh/đỏ, tay ăn + gật đầu), 23 người XẾP HÀNG ở 7 sạp đặc biệt, 14 người NHÓM NÓI CHUYỆN, 6 khách ngồi quán vỉa hè; palette áo trầm ấm 14 màu + khăn quàng ~35–55% + mũ len/nón lá. Mật độ vẫn theo giờ thật.
- **Đèn đêm đúng công thức ảnh 09:** mỗi sạp 1 bóng đèn trắng + quầng halo sprite nhấp nháy lệch pha; chữ chợ phát sáng đỏ (emissive 2.6); biển nóc khách sạn phát sáng; cửa sổ khách sạn sáng rải rác 3 mức; dây đèn cũ giữ một phần.
- **Khách sạn (hotels.glb, 4 biến thể 4–6 tầng):** DALAT CENTER / HOTEL COLLINE / VIB (kính xanh hiện đại) / THANH BÌNH — cửa sổ có khung lõm/nổi, ban công, gờ chỉ từng tầng, bể nước nóc, biển chữ nổi; đặt 7 vị trí: dãy sau đồi (phông nền bậc thang), đông/tây, nam sau chợ.
- **Quán vỉa hè (shop.glb ×3):** CÀ PHÊ VỢT cạnh bùng binh, TRÀ & NƯỚC MÍA trước chợ, SINH TỐ ĐÊM phía đông — hiên bạt, biển canvas, khách ngồi.
- **Chất lượng 3D:** bevel cho khối chính, mặt tiền nhiều lớp, nhân vật thêm cầu vai bo tròn (character.glb dựng lại 475.700B).
- **Giữ nguyên 100% gameplay v3** (mua/bán/nâng cấp/lạnh/coi bói/hát/hộ chiếu, save `chohb3d-v1` không đổi — grep xác nhận đủ hàm).
- **Standalone:** `prototype-v2/index-standalone.html` = 9.856.024 byte (9,40 MB, 14 GLB) — dưới ngưỡng 10MB nhưng sát; nếu thêm model đợt sau cần nén GLB (giảm segment/text) trước.

## Trạng thái V4.1 (06/11/2026) — SỬA 4 ĐIỂM ĐIỀU PHỐI BÁC Ở V4
Checklist: [V4-CHECKLIST.md](sandbox://workspace/cho-hoa-binh-3d/prototype-v2/V4-CHECKLIST.md) mục V4.1. Gameplay + save giữ nguyên; node --check OK; standalone đóng lại 10.365.264 byte (9,89 MB, 14 GLB). **Chưa đẩy GitHub, chưa upload** (theo lệnh đợt này).
- **1. Mặt nhân vật (regression v4) — ĐÃ SỬA, có ảnh trước/sau:** nguyên nhân kép — render kiểm chứng v4 bật cả 3 mũ cùng lúc (web chỉ bật 1) tạo "dải tối + mảng đỏ", VÀ lỗi GLB thật: cầu mũ beanie/cap phủ xuống tận cằm chôn cả mắt. Đã cắt phần cầu mũ/tóc trước mặt (trim_front_below), vành mũ nâng lên trên trán, mắt to hơn. Ảnh: renders/v41-face-before-*.png → renders/v41-face-after-*.png; mặt sạch (2 mắt chấm + má hồng) cũng xác nhận trong cả 2 ảnh toàn cảnh. character.glb 459.580 byte.
- **2. Tượng đài + thảm hoa — ĐÃ SỬA:** tượng thành cụm 3 hình người trừu tượng (đầu/vai/tay đọc được ở cận cảnh) trên bệ 3 bậc + thông đá thu nhỏ; thảm hoa 8 quạt đặc xen kẽ hoa bão hoà/cỏ + hoa rải dày 3 vòng — cận cảnh renders/v41-01-crop-bung-binh.png cho thấy mảng hoa hồng/vàng/trắng liền, khớp tinh thần ảnh thật 04. roundabout.glb 1.500.476 byte.
- **3. Mặt tiền — ĐÃ SỬA:** băng hồng đào đậm hơn + 3 rãnh tối chạy dọc; zigzag nền đậm tương phản + chevron cao/dày hơn (arm 1.42 / thick 0.42 / tall 0.62). market.glb 1.569.348 byte.
- **4. Kiểm chứng toàn cảnh (mới, scripts/render_check_v41.py):** lắp toàn cảnh như web + 68 NPC đúng phân bố + xe chạy/bãi xe ~70 chiếc. **Verdict tự soi thẳng thắn:**
  - *Ngày* (renders/v41-01-toan-canh-ngay.png, góc cao phía tây): **ĐẠT về bố cục nghiệm thu** — bùng binh + tượng + thảm hoa + xe vòng, mặt tiền + chữ đỏ + tháp kính, bậc thang ~15 người, đồi + rạp + khách sạn đều trong 1 khung; đếm được ~40+ nhân vật. Chưa đạt mức "đông nghẹt": ở khung rộng người còn nhỏ, bãi xe trước mặt tiền nằm ngoài khung (xe quanh bùng binh + đường thì có). Muốn khung "đông" hơn phải chấp nhận khung hẹp hơn — đánh đổi đã chọn theo đúng yêu cầu brief (thấy cả 3 điểm nhấn).
  - *Đêm* (renders/v41-02-cho-dem.png, góc đường/bậc thang): **ĐẠT một phần** — bậc thang đông người, mặt nhân vật sạch rõ, 1 sạp góc phải phát sáng ấm đúng công thức bóng trắng, biển HOTEL COLLINE phát sáng. Hạn chế: khung tối, dãy sạp đường Âm Phủ ngoài khung nên "lung linh nhiều sạp" chưa thể hiện; vài người trên cầu trông như lơ lửng vì sàn cầu chìm trong tối (bản web có halo + ambient sáng hơn nên sẽ đỡ hơn render Cycles này).
  - Lỗi quy trình đã bắt + sửa trong lúc làm: hàm box() của script render bị Blender 5.0 nướng cả location vào mesh (transform_apply mặc định) khiến logic dọn sườn đồi chết lặng lẽ, sườn chôn mất đảo bùng binh ở 2 lần render đầu — đã sửa (location=False) + probe kiểm chứng bbox trước khi render lại.

## Trạng thái V4.2 (06/11/2026) — HÀNH TRÌNH ĐI VÀO + ĐÊM ẤM + VIBE ĐÀ LẠT + LỚP GAME + BÁM ẢNH CHỐT
Checklist đầy đủ: [V4-CHECKLIST.md](sandbox://workspace/cho-hoa-binh-3d/prototype-v2/V4-CHECKLIST.md) mục V4.2. Tóm tắt: (1) Trục hành trình dựng lại — đường vào có dốc/vỉa hè/nhà phố 2 bên/cổng chào/đèn thuộc địa/2 sạp mới, spawn + camera mở đầu đặt lại, mật độ dày nhất dọc trục; HotelD dời khỏi lòng đường. (2) Mặc định mở game là CHỢ ĐÊM ~19:15 + grade ấm toàn cảnh (nền nâu ấm, đèn vàng cam + quầng ướt, sương ấm). (3) Vibe Đà Lạt: phông đồi thông lớp lớp + tháp chuông hậu cảnh, sương nhiều cao độ + sương sát đất, cẩm tú cầu, đường ướt phản sáng, khói ống khói/hơi bếp. (4) Lớp game: nhiệm vụ dẫn đường 5 chặng theo đúng hành trình (cột sáng + HUD + thưởng Xu), thẻ tên khu vực, bong bóng thoại NPC, sparkles + popup +Xu, minimap. (5) Bám ảnh chốt: biển gỗ lớn có GIÁ + hình món, bày hàng riêng từng họ sạp, ấm rót + dòng rót + cột hơi lớn, lồng đèn giấy lớn + tua đỏ, cành thông nóc sạp, giỏ dâu/chậu cây, nền đá lát canvas, thẻ tên NPC pill. (6) Bổ sung research/12: UI nâu ấm toàn bộ HUD + đơn hàng "mua hộ" của NPC + quy tắc đèn dây (không giăng ngang trục Âm Phủ). Đối chiếu 19 mục research/12: 9 làm đủ, 2 làm một phần (bày hàng theo họ, đạo cụ cầm tay), 8 để đợt sau (ghi rõ trong checklist).
Kiểm chứng: node --check OK sau từng patch; index.html 163.360 byte; standalone đóng lại 10.410.292 byte (9,93 MB, 14 GLB). Render hành trình: scripts/render_journey.py (kế thừa render_check_v41 + lớp đường vào/phông/lớp sạp mô phỏng), 5 ảnh đêm ấm renders/v42-a..e — VERDICT: (điền sau khi soi ảnh). **Chưa đẩy GitHub, chưa upload** (theo lệnh đợt này).
