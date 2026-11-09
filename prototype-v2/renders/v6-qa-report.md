# Báo cáo QA & Cải thiện Toàn diện V6 — Hành trình 5 Chặng Chợ Đêm Đà Lạt

## 1. Tổng quan Cải thiện & Đối chiếu Kế hoạch (`KE_HOACH_MUSE_AI_V6.md`)

| Chặng | Hạng mục cải thiện trong `prototype-v2/index.html` | Trạng thái |
|---|---|---|
| **① Tuyến đường chợ đêm (Nguyễn Thị Minh Khai)** | Dây bóng đèn vàng ấm (3000K) dọc 2 mép đường (`x = -196..-64`) + dây giăng ngang qua đường mỗi 28m; dãy sạp quần áo len/jean treo nhiều màu với mái bạt xanh/đỏ/trắng + bàn hàng + ghế nhựa mỗi 9m bám độ dốc `entryRampY(x)`; bổ sung các căn nhà phố 4–5 tầng khép kín hẻm; bó 3 dây điện chằng chịt võng ngang đường; quầng sáng phản chiếu mặt nhựa ướt đêm (`glowDisc`) dọc hai mép đường; dọn sạch các biển hiệu đường sai vị trí. | Hoàn tất |
| **② Cầu thang lớn Ngô Viết Thụ & Khán đài ăn uống** | Lan can sắt hai mép cầu thang (`x = ±11.2, z = -29..-3`) bám sát độ dốc `stairH(z)`; các cụm bàn thấp + ghế nhựa đỏ/xanh + người ngồi ăn bánh tráng nướng & uống sữa nóng ngắm toàn cảnh chợ đêm; biển hiệu chân cầu thang `"CẦU THANG LỚN — KHU HÒA BÌNH (KTS Ngô Viết Thụ)"` và mốc `"📸 GÓC HONG KONG — CHỢ ĐÀ LẠT"`. | Hoàn tất |
| **②B Khung cảnh đỉnh cầu thang (Ảnh chuẩn 08 & 10)** | **Thương xá La Tulipe** phía Tây (`x = -17.5, z = -33.5, y = 17`): 3 tầng kiểu Pháp, mái ngói đỏ, biển xanh chữ trắng `"Thương xá La Tulipe — LỐI VÀO MUA SẮM"`; **Cửa hàng L'ANGFARM Store** phía Đông (`x = 17.5, z = -33.5, y = 17`): 2 tầng ốp gạch nung ấm, biển xanh lá sáng đèn `"L'ANGFARM — ĐẶC SẢN ĐÀ LẠT"`, cửa kính trưng bày hũ mứt & trà atiso, hàng thông Đà Lạt xanh mướt (khớp 100% ảnh 08). | Hoàn tất |
| **②C Khung cảnh đối diện bùng binh & Skyline (Ảnh chuẩn 27 & 06)** | **Khách sạn Thanh Bình (Thanh Bình Hotel)** đối diện bùng binh (`x = -38.5, z = 35.5, y = 0`): 5 tầng trắng cổ điển, biển neon chữ xanh dương nổi bật `"Thanh Bình Hotel"` trên nóc; **Skyline đêm**: ánh sáng vàng neon `"DALAT CENTER"` & `"HÔTEL COLLINE"` trên đường chân trời xa (khớp 100% ảnh 27). | Hoàn tất |
| **③ Khu Hòa Bình (Rạp Hòa Bình / Cà phê Tùng)** | Kết nối liền mạch với đỉnh cầu thang (`y = 17`), mốc check-in Bước 3/5 trong `TUT_STEPS`, giữ nguyên biển Rạp Hòa Bình (Rạp 3 Tháng 4 — xây 1937) và Cà phê Tùng (06 Khu Hòa Bình — từ 1956). | Hoàn tất |
| **④ Sữa đậu nành Hoa Sữa (Đúng vị trí 3F Tăng Bạt Hổ trên đồi)** | **ĐÃ SỬA VỊ TRÍ**: Dời từ dưới đường vào (`x = -128`) lên đúng **Đầu dốc đường Tăng Bạt Hổ trên đồi Khu Hòa Bình** (`x = -22, z = -43, y = 17`), cách Rạp Hòa Bình 15m; quán vỉa hè không mái che, biển `"3F TĂNG BẠT HỔ (64 CŨ) — SỮA ĐẬU NÀNH HOA SỮA"`, biển phố `"ĐƯỜNG TĂNG BẠT HỔ — PHỐ ẨM THỰC ĐÊM"`, 6 ghế nhựa thấp tràn vỉa hè, nồi inox nấu sữa bốc khói/hơi nước, tủ kính bánh ngọt su kem / sừng trâu / tiêu 6k, thực đơn thật (nành bò, nành đường, mè đen, sữa bắp 7–10k). | Hoàn tất |
| **⑤ Hồng Trà Hòa Bình (Ki-ốt 30–32 Khu Hòa Bình)** | Đặt tại đỉnh đồi Khu Hòa Bình (`x = 6.0, z = -35.5, y = 17, rotY = 0`) ngay cạnh Rạp Hòa Bình và dốc Tăng Bạt Hổ; biển `"KI-ỐT 30–32 · HỒNG TRÀ HÒA BÌNH (Mở cửa 9:00–23:00)"`, 2 ki-ốt liền kề (28–29 & 33–34), bình ủ trà inox, topping hạnh nhân chôm chôm, hơi trà nóng thơm nồng. | Hoàn tất |

## 2. Kết quả Kiểm định Tự động (Automated QA Gate)

1. **`diag_runtime.mjs` (90 frames headless runtime)**:
   - `MODULE INIT OK` — `ANIMATE 90 frames SẠCH — không ngoại lệ.`
   - NPC phân bổ hợp lý, toàn map hoạt động mượt mà.
2. **`v52_traffic_harness.mjs` (Kiểm định giao thông & đồ thị tự đi `AW_NODES`)**:
   - `26/26 PASS` (0 va chạm xe-sạp, 0 lệch làn, bảo toàn đồ thị tự đi).
3. **`audit_ground_v54.mjs` (Kiểm định cao độ `groundH` & mặt đất)**:
   - `60 tuyến wanderer + AW (48 nút), 45 sạp | lỗi cứng: 0`.
4. **Đóng gói `index-standalone.html`**:
   - Dưới ngưỡng 10 MB (9.97 MB), đồng bộ 100% với `index.html`.

