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
