# Báo cáo QA & Cải thiện Toàn diện V6 — Hành trình 5 Chặng Chợ Đêm Đà Lạt

## 1. Tổng quan Cải thiện & Đối chiếu Kế hoạch (`KE_HOACH_MUSE_AI_V6.md`)

| Chặng | Hạng mục cải thiện trong `prototype-v2/index.html` | Trạng thái |
|---|---|---|
| **① Tuyến đường chợ đêm (Nguyễn Thị Minh Khai)** | Dây bóng đèn vàng ấm (3000K) dọc 2 mép đường (`x = -196..-64`) + dây giăng ngang qua đường mỗi 28m; dãy sạp quần áo len/jean treo nhiều màu với mái bạt xanh/đỏ/trắng + bàn hàng + ghế nhựa mỗi 9m bám độ dốc `entryRampY(x)`; bổ sung 6 căn nhà phố 4–5 tầng khép kín hẻm đoạn kéo dài (`x = -140..-169`: Tiệm Vàng Kim Phát, Nhà Thuốc Đà Lạt, Đặc Sản Dâu & Mứt, Khách Sạn Minh Khai, Tiệm Đồ Len Cô Ba, Phở Đêm Đà Lạt); thêm 8 nhịp cột điện + bó 3 dây điện chằng chịt võng ngang đường (`x = -165..-61`); quầng sáng phản chiếu mặt nhựa ướt đêm (`glowDisc`) dọc hai mép đường. | Hoàn tất |
| **② Cầu thang lớn Ngô Viết Thụ & Chợ Âm Phủ** | Lan can sắt hai mép cầu thang (`x = ±11.2, z = -29..-3`) bám sát độ dốc `stairH(z)`; 4 cụm bàn thấp + ghế nhựa đỏ/xanh + bóng đèn vàng ấm tại các chiếu nghỉ (`z = -8.5, -13.5, -19.5, -25.5`); biển hiệu chân cầu thang `"CẦU THANG LỚN — KHU HÒA BÌNH (KTS Ngô Viết Thụ)"` và mốc chụp ảnh `"📸 GÓC HONG KONG — CHỢ ĐÀ LẠT"` tại đỉnh lan can (`x = -11.8, z = -30.35, y = 18.55`). | Hoàn tất |
| **③ Khu Hòa Bình (Rạp Hòa Bình / Cà phê Tùng)** | Kết nối liền mạch với đỉnh cầu thang (`y = 17`), mốc check-in Bước 3/5 trong `TUT_STEPS`, giữ nguyên biển Rạp Hòa Bình (Rạp 3 Tháng 4 — xây 1937) và Cà phê Tùng (06 Khu Hòa Bình — từ 1956). | Hoàn tất |
| **④ Sữa đậu nành Hoa Sữa (3F Tăng Bạt Hổ — số 64 cũ)** | Gỡ bỏ mái bạt/ô dù (`roof:'none'`) đúng thực tế quán ngồi ngay mép vỉa hè không mái che; dựng biển `"3F TĂNG BẠT HỔ (64 CŨ)"`; bổ sung 6 ghế nhựa + bàn thấp tràn ra lề; đưa `hoasua` vào `HERO_STALLS` với nồi inox lớn nấu sữa, tủ kính 2 tầng trưng bày bánh su kem / sừng trâu / bánh tiêu đồng giá 6k, cột hơi nước mềm (`addSteamSprites`), và thực đơn thật (nành đường/bò/phụng/xanh, mè đen, sữa bắp 7–10k). | Hoàn tất |
| **⑤ Hồng Trà Hòa Bình (Ki-ốt 30–32 Khu Hòa Bình)** | Đặt tại đỉnh đồi Khu Hòa Bình (`x = 6.0, z = -35.5, y = 17, rotY = 0`) nhìn ra quảng trường; dựng biển `"KI-ỐT 30–32 · HỒNG TRÀ HÒA BÌNH (Mở cửa 9:00–23:00)"`; dựng thêm 2 ki-ốt liền kề hai bên (`KI-ỐT 28–29 · BÁNH NGỌT` tại `x = 1.4` và `KI-ỐT 33–34 · QUÀ LƯU NIỆM` tại `x = 9.4`) tạo thành dãy ki-ốt Khu Hòa Bình; đưa `hongtra` vào `HERO_STALLS` với 2 bình ủ hồng trà inox, khay topping hạnh nhân chôm chôm, chồng ly đỏ và hơi trà nóng. | Hoàn tất |

## 2. Kết quả Kiểm định Tự động (Automated QA Gate)

1. **`diag_runtime.mjs` (90 frames headless runtime)**:
   - `MODULE INIT OK` — `ANIMATE 90 frames SẠCH — không ngoại lệ.`
   - Tổng số NPC phân bổ hợp lý: 457 NPC (`duong-vao`: 88).
2. **`v52_traffic_harness.mjs` (Kiểm định giao thông & đồ thị tự đi `AW_NODES`)**:
   - `26/26 PASS` (0 va chạm xe-sạp, 0 lệch làn, bảo toàn 46 nút / 45 cạnh đồ thị `AW_NODES`).
3. **`audit_ground_v54.mjs` (Kiểm định cao độ `groundH` & mặt đất)**:
   - `60 tuyến wanderer + AW (46 nút), 45 sạp | lỗi cứng: 0`.
4. **Đóng gói `index-standalone.html`**:
   - Dưới ngưỡng 10 MB, đồng bộ 100% với `index.html`.
