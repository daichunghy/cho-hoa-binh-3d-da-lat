# KẾ HOẠCH — SINH HOẠT QUANH HỒ XUÂN HƯƠNG + CÁI LẠNH + NỢ THỰC TẾ

> Lập 21:32 ngày 11/11/2026 theo lệnh trực tiếp của Chung Hy, sau khi anh bác mức
> thực tế của hồ ("nhỏ xíu / không giống thật / có đạt đâu / cây cối đâu có chuẩn")
> và yêu cầu: (1) thể hiện được SỰ LẠNH Đà Lạt; (2) lập plan người đi bộ, tình
> nhân, xe đạp... quanh hồ; (3) triển khai trong NEXT STAGE; (4) ghi nợ: trong
> chợ và bậc tam cấp cũng chưa thực tế.
> Nguyên tắc xuyên suốt: cổng kỹ thuật xanh KHÔNG đồng nghĩa đạt — nghiệm thu
> bằng mắt đối chiếu ảnh thật (theme/xuan-huong/ + ảnh chợ/tam cấp thật).

## A. Sinh hoạt quanh hồ (triển khai ở stage kế tiếp sau XH-2, gộp vào XH-3+)

Tái dùng hệ NPC waypoint/BFS + tủ đồ hiện có của game; không viết hệ mới.

1. **Tuyến đi lại**: đường dạo bờ bắc (z 28..36) + lối nối từ bùng binh đầu chợ
   + cầu ra đảo + vòng quanh đảo Thủy Tạ. Worker thi công đo lại đường đi được
   từ groundH trước khi đặt waypoint.
2. **Người đi bộ lẻ**: 10–14 NPC đi hai chiều trên đường dạo, tốc độ đi bộ,
   thỉnh thoảng dừng ở lan can ngắm hồ 5–10s rồi đi tiếp.
3. **Tình nhân**: 4–6 CẶP đi đôi sát nhau (offset ngang ~0,5u, đồng tốc),
   có điểm dừng cố định ở chỗ ngắm cảnh (đầu cầu đảo, ghế đá, cầu chữ Y sau
   này); mật độ cặp cao nhất ở khung giờ mặc định 19:00. Vài cặp ngồi ghế đá.
4. **Xe đạp**: 4–6 xe chạy vòng trên đường dạo, 2 chiều, lane lệch phía ngoài
   (gần mép đường) để không cắt mặt người đi bộ; tốc độ ~3× người đi bộ;
   model xe đạp chibi đơn giản + người đạp mặc áo ấm. Nếu lane đường dạo
   không đủ rộng ở đoạn nào thì xe đạp chỉ chạy đoạn bờ bắc thẳng dài.
5. **Người ngồi/nghỉ**: NPC ngồi ghế đá (XH-3 đặt ghế), 1–2 người chụp ảnh
   ở đầu cầu đảo (đứng yên, giơ điện thoại), người bán hàng rong ở ki-ốt đầu
   cầu (theo §7 kế hoạch hồ).
6. **Mật độ theo giờ** (gắn hệ ngày/đêm sẵn có): sáng sớm = người chạy bộ +
   tập thể dục; trưa thưa; 17:00–20:00 đông nhất (dạo mát + tình nhân);
   khuya gần như vắng. Mặc định game 19:00 = cao điểm tối.
7. **Trang phục lạnh**: toàn bộ NPC quanh hồ mặc áo ấm/khăn quàng từ tủ đồ
   hiện có — hồ là vùng lạnh nhất map, phải nhìn thấy bằng mắt.

## B. Cái lạnh Đà Lạt ở hồ (cùng stage XH-3+, nối hệ nhiệt độ của goal)

1. **Sương mặt hồ**: 3–5 lớp sương mỏng (plane alpha mềm, texture canvas như
   idiom nước) trôi chậm trên mặt nước, cao hơn mặt nước ~0,3–0,8u; độ đậm
   theo giờ: sáng sớm + sau 18:00 rõ, trưa gần như tan. Đây là dấu hiệu lạnh
   số 1 của hồ Xuân Hương thật (sương sớm trên mặt hồ).
2. **Hơi thở + co ro**: NPC quanh hồ dùng chung hiệu ứng lạnh của hệ nhiệt
   độ (hơi thở khói nếu đã có; chưa có thì ghi vào vòng hệ lạnh, không tự
   chế riêng cho hồ).
3. **Bảng nhiệt độ ở ki-ốt bến thuyền**: biển nhỏ hiện nhiệt độ Đà Lạt theo
   giờ game (tối ~14–16°C) — chi tiết rẻ, đọc phát hiểu ngay "đang lạnh".
4. Bờ nam xa: sương đọng trên hàng thông (silhouette mờ hơn ở sáng/tối —
   fog hiện tại đã hỗ trợ, kiểm chứng bằng render, không đoán).

## C. Chuẩn cây (áp cho XH-3+ và mọi vòng sau; thay chuẩn cũ)

- **Thông Đà Lạt**: thân cao thẳng, tán Ô/dẹt nhiều tầng (thông ba lá) —
  CẤM thông hình nón (anh đã chỉ đích danh). Chiều cao game ~7–10u so với
  người 1,6u; tán rộng 3–5u. Đo tỉ lệ từ ảnh theme/xuan-huong/ (02/17/28).
- Áp dụng: bờ bắc (dãy thông ven đường dạo), đảo Thủy Tạ, bờ nam xa
  (silhouette cũng theo tán ô), và về sau rà toàn map (Hoa Sữa giữ riêng).
- Phượng tím: giữ làm điểm nhấn tím đúng ảnh bờ bắc (28/29), không lạm dụng.

## D. Nợ thực tế đã ghi (vòng REALISM riêng, sau các stage hồ chính)

1. **REALISM-INT-1 — trong chợ**: nội thất nhà lồng chưa thực tế; vòng riêng
  đo từ ảnh thật trong chợ (mật độ quầy, hàng treo, ánh sáng, lối đi) rồi sửa.
2. **REALISM-STAIR-1 — bậc tam cấp**: chưa thực tế; vòng riêng đo từ ảnh thật
  (bề rộng bậc, lan can, chiếu nghỉ — chỗ chú Ba coi bói —, nhịp nhà hai bên).
3. Cả hai vòng theo đúng nhịp chuẩn: đo từ ảnh → sửa nhỏ → render đối chiếu
  → 8 cổng → đẩy GitHub. Không gộp chung với stage hồ.

## Thứ tự stage từ đây

XH-2 (đang chạy: thuyền + Thủy Tạ + cầu) → **XH-3+** (trang trí bờ đúng chuẩn
cây C + đèn bướm + ghế đá + ki-ốt, KÈM sinh hoạt quanh hồ A và sương lạnh B)
→ XH-4 đạp vịt (+ luật mặt nước) → XH-5 tích hợp (dấu hộ chiếu hồ, photo,
đêm) → REALISM-INT-1 → REALISM-STAIR-1 (hoặc chen sớm hơn nếu Chung Hy gọi).
