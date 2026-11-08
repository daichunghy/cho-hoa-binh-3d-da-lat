# KẾ HOẠCH THÀNH PHẦN XE MÁY — Chợ Hòa Bình Online

Lệnh của Chung Hy (14:20, 08/11): "Xe máy nữa này, quan trọng nè — bạn cần plan kỹ về nhiệm vụ, cách hoạt động của thành phần này nhé."

Hiện trạng đo trong code (index.html): có `makeMoto` + 1 xe thuê đỏ ở bãi trước chợ (30 Xu/90s, cấp 5 miễn phí), xe chạy vòng đảo (islandBump) và xe đậu rải rác ~100 chiếc. Tất cả đang ở mức "trang trí + 1 tương tác đơn", CHƯA thành hệ thống. Kế hoạch này nâng xe máy thành một thành phần có vai trò rõ trong cả khung cảnh lẫn lối chơi.

## 1. NHIỆM VỤ (xe máy để làm gì trong game)

| # | Vai trò | Giá trị |
|---|---------|---------|
| 1 | **Giao thông sống** — xe chạy vòng bùng binh + trục đường vào | Tạo cảm giác phố Việt thật; bùng binh về đêm phải có vành xe + vệt đèn như tư liệu đêm (research/18, điểm 5) |
| 2 | **Xe đậu** — hàng dài quanh đảo, trước mặt tiền, bãi xe | Lớp thị giác đặc trưng nhất của chợ VN; là mốc không gian để người chơi định hướng |
| 3 | **Phương tiện của người chơi** — thuê xe chạy quanh map | Gameplay thật: đi nhanh giữa 5 khu, làm nhiệm vụ giao hàng, khám phá đồi |
| 4 | **Xe của NPC** — người cưỡi xe chạy qua / dừng mua hàng | Đời sống: chợ có người đến–đi bằng xe, không chỉ đi bộ |
| 5 | **Bề mặt nhiệm vụ** — giao đồ ăn bằng xe, thử thách vòng đảo | Gắn vào hệ nhiệm vụ/ngày sẵn có, cho Xu/XP có chỗ tiêu và chỗ kiếm thêm |

## 2. CÁCH HOẠT ĐỘNG

### 2.1 Tuyến xe chạy (traffic)
- **3 tuyến cố định theo waypoint xe riêng** (không dùng chung đường đi bộ): (a) vòng bùng binh 2 làn ngược chiều kim đồng hồ, bán kính bám vành đảo; (b) trục đường vào 2 chiều (xuống thung lũng ↔ lên quảng trường); (c) đường vòng chân đồi nối bãi xe – mặt tiền.
- Tốc độ 6–9 unit/s tùy tuyến; giãn cách tối thiểu giữa các xe cùng làn; xe **chậm lại khi người chơi/NPC cắt ngang làn**, không bao giờ xuyên qua người (đây là lỗi đã từng bị bắt ở cầu nổi — không lặp lại).
- Mật độ theo khung giờ game: giờ chợ đêm cao điểm đông nhất; trần xe chạy đồng thời **14 xe** (kèm người cưỡi), quá trần thì xếp hàng chờ ở đầu tuyến.
- Ban đêm: đèn pha = nón sáng giả + vệt sáng trên mặt đường, đèn hậu đỏ; vòng đảo nhìn từ trên phải đọc thành **vệt sáng chuyển động** như video đêm.

### 2.2 Xe đậu (parked)
- Quy tắc xếp: hàng chéo ~45° theo vạch, 3 khu mật độ giảm dần: vành đảo > trước mặt tiền > bãi xe sau chợ; chừa lối đi bộ tối thiểu 2 unit (kiểm bằng harness trên AW_NODES).
- Đa dạng: 6 màu sơn theo tỉ lệ thật (đen/xám nhiều nhất), vài xe treo mũ bảo hiểm ở gương, 2–3 xe giao hàng có thùng sau, 1–2 xe cổ (cub) làm điểm nhấn gần góc hát.
- Toàn bộ xe đậu dùng chung geometry/material (instancing) — đếm drawcall trước/sau, không để phình hiệu năng.

### 2.3 Xe người chơi (thuê + cưỡi)
- Điểm thuê giữ ở bãi trước chợ (đã có RENT_PT); giá 30 Xu/90s, **cấp 5 miễn phí** (đã chốt trong code hiện tại — giữ nguyên).
- Khi cưỡi: tốc độ tối đa ~11 unit/s, rẽ theo phím/joystick hiện có, camera bám sau; **xuống xe ở bất cứ đâu** — xe đỗ lại tại chỗ, có nút "Trả xe" đưa xe về bãi (hoặc bấm vào xe để cưỡi tiếp trong thời gian thuê còn lại).
- Hết giờ thuê: xe không biến mất đột ngột — hiện đếm ngược 10s trên HUD, sau đó xe tự "được dắt về bãi" (mờ dần), người chơi đứng lại tại chỗ.
- An toàn gameplay: cưỡi xe không đâm ngã NPC (NPC né nhẹ sang bên), không leo được bậc thang/bậc thềm (đúng thật), xuống dốc về chợ được, lên đồi theo đường vòng.
- Gắn nhiệm vụ: thêm loại nhiệm vụ ngày **"Giao hàng bằng xe"** (nhận món ở sạp A, giao cho NPC ở khu B trong thời gian đếm ngược, thưởng Xu/XP cao hơn nhiệm vụ đi bộ) — tận dụng vòng LOOP + đồ thị waypoint sẵn có.

### 2.4 Xe NPC (người cưỡi)
- Người cưỡi dùng chính hệ trang phục đa dạng của v5.1 (phom/màu/túi) + mũ bảo hiểm bắt buộc (đúng luật VN + đúng ảnh thật).
- Hành vi đơn giản mà sống: chạy theo tuyến 2.1, thỉnh thoảng 1 xe tấp vào lề trước sạp, người xuống → thành người đi bộ mua hàng → quay lại xe đi tiếp (chu trình khép kín, số lượng nhỏ 2–3 xe để không rối hiệu năng).

### 2.5 Hiệu năng & trần kỹ thuật
- Xe chạy: ≤14 (kèm rider) + xe người chơi; xe đậu instancing toàn bộ.
- Mọi thứ bằng model vehicle.glb hiện có + biến thể màu; **không thêm GLB mới** trừ khi dựng lại trong Blender theo chỉ thị Blender-first (phải báo byte trước/sau, tổng standalone vẫn ≤ 10MiB).
- Save `chohb3d-v1` không đổi schema (trạng thái thuê xe là tạm thời, không lưu).

## 3. LỘ TRÌNH LÀM

- **P1 — đang gộp trong v5.1 (Mục C):** mật độ xe đậu vành đảo + hàng xe trước mặt tiền đúng tư liệu đêm; vành xe chạy vòng đảo có đèn đêm. Đây là phần thị giác.
- **P2 — đợt riêng v5.2 (sau v5.1):** hệ tuyến xe 3 tuyến hoàn chỉnh + người cưỡi NPC + chu trình tấp lề mua hàng + đèn pha/vệt sáng đêm. Nghiệm thu: render đêm góc A/B cạnh tư liệu đêm + harness kiểm xe không cắt lối đi bộ/không xuyên NPC.
- **P3 — cùng đợt hoặc nối tiếp:** thuê xe nâng cấp (xuống xe tự do, trả xe, đếm ngược HUD) + nhiệm vụ ngày "Giao hàng bằng xe". Nghiệm thu: harness chạy kịch bản thuê → cưỡi → giao hàng → hết giờ.

## 4. TIÊU CHÍ ĐẠT (để Chung Hy chấm)
1. Đứng ở bùng binh ban đêm: thấy vành xe chạy có vệt đèn + hàng xe đậu dài + đảo đông người — đặt cạnh video đêm tham khảo không còn "thiếu xe".
2. Thuê xe chạy được một vòng chợ – đồi – quảng trường mượt, không xuyên người, xuống xe ở đâu cũng được.
3. Có ít nhất 1 nhiệm vụ giao hàng bằng xe chơi được trọn vòng.
