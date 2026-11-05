# Tổng hợp thiết kế — Chợ Hòa Bình 3D Đà Lạt
*Bản chốt từ 10 báo cáo trong `research/` (05/11/2026). Đây là design doc để bắt đầu làm prototype.*

## 1. Định vị
Cả thị trường "đi chùa online" (23+ sản phẩm đã khảo sát) đều là tôn giáo / tĩnh lặng / tư liệu — **chưa ai làm một địa điểm đời thường Việt Nam có hàng quán, ăn uống, mua sắm**, chưa ai gắn địa danh thật với hàng thật giao tận nhà. Moat của dự án không phải code mà là: **địa danh thật + chuỗi hàng thật + vận hành sự kiện theo mùa/giờ**.

## 2. Công thức lõi học từ Sansa / Chùa Sen / Niệm Phật Online
- Vào ngay trên trình duyệt, **không bắt đăng ký**, có mặt trong thế giới <10 giây; đăng nhập chỉ để lưu tiến trình (và phải 1 tài khoản xuyên suốt — sửa điểm trừ "tiến độ phân mảnh theo server, dễ mất nhân vật" của niemphat.online).
- Một không gian + vài "động từ" thôi; **nút hành động theo ngữ cảnh, 1 chạm** khi đến gần quầy/vật.
- Hiện diện không áp lực: **không chat tự do**, chỉ chào preset + biểu cảm (bài học từ Sansa và Chùa Sen).
- Điều khiển copy nguyên mẫu đã kiểm chứng: mobile joystick trái + vuốt phải + chạm sàn tự đi; PC WASD / click-to-move / phím F.
- Phòng nhỏ 30–100 người (shard ngay từ đầu), chỉ hiện tên ~10 người gần nhất để chống lag.
- Đám đông là nội dung: NPC tiểu thương thường trú để chợ không bao giờ vắng; khoảnh khắc đông người phải "chụp màn hình được".

*Đính chính nguồn: site Chùa Sen thật là **chuasen.com** (chuasen.online không phân giải được).*

## 3. Thế giới — khóa theo tư liệu thật (research/07)
- **Hai cốt cao độ, cấm làm phẳng:** khu Hòa Bình trên đỉnh đồi, Chợ Đà Lạt dưới thung lũng; nối bằng bậc thang ~17m (3 đợt nghỉ) và cầu nổi vào thẳng tầng 2 chợ.
- Giữ nguyên trạng di sản: nhà lồng chợ (KTS Nguyễn Duy Đức; Ngô Viết Thụ chỉnh trang), rạp Hòa Bình (tòa chợ gạch 1937), bùng binh hoa, Café Tùng 06 Hòa Bình.
- **5 district** (phân biệt bằng màu/âm thanh/mùi vị trực quan): Ẩm thực nóng · Sữa & đồ uống · Đồ len (thử lên avatar) · Nông sản & hoa · Đặc sản mang về.
- **2 trạng thái trên cùng 1 map:** chợ ngày / chợ đêm (chợ đêm "Âm Phủ" — tên từ đèn dầu leo lét trong sương, là chi tiết kể chuyện vui, không làm kinh dị). 3 preset môi trường: sương sáng sớm / nắng trưa cao nguyên / đêm đèn vàng + khói than.

## 4. Vòng lặp chính — đi chợ, ăn uống (research/06, 09)
Chuẩn 7 bước tại mỗi quầy: đến quầy xem menu treo → chọn món + tuỳ biến → trả **Xu Chợ** (tiền ảo kiếm bằng đi chợ) → NPC chế biến thật vài giây, có số thứ tự → nhận vào **giỏ đi chợ xách theo** (không popup shop) → ngồi ăn/uống có hoạt cảnh → nhận 1 trong 3 buff: *Ấm bụng* (chống sương đêm), *Khoẻ chân* (leo dốc), *Tỉnh táo* (cà phê).
- **6 quầy đợt 1, mỗi quầy 1 gameplay riêng:** sữa đậu nành nóng (thổi nguội, combo su kem) · bánh tráng nướng (tự chọn topping + nướng than) · cà phê phin/vợt (chờ nhỏ giọt) · dâu tây & kem bơ · khoai/bắp nướng (điểm nghỉ xã hội) · gian đặc sản (đóng hộp quà).
- **Tiền thật chỉ xuất hiện khi nhảy ra ngoài:** món nóng chỉ bán trải nghiệm/voucher; món khô (mứt, hồng treo gió, trà atiso, cà phê hạt) mới gắn affiliate. Lộ trình doanh thu 5 tầng: mã quà tại quầy thật → affiliate đặc sản → voucher combo chợ đêm → deep-link giao đồ ăn tại Đà Lạt → cho thuê quầy ảo.

## 5. Giữ chân — không FOMO (research/08)
- Phiên trọn vẹn 5–12 phút; **Hộ chiếu Đi Chợ 8 dấu theo khu**, đóng dấu bằng trải nghiệm nhỏ tại khu ("chìa khóa mềm" mở khu mới — cơ chế học từ hành trình nhiều tầng, research/04).
- 3 quest/ngày từ NPC, **dồn được 3 ngày**, không phạt khi bỏ lỡ; streak kiểu "ghé 4/7 ngày", vật phẩm mùa quay lại mùa sau.
- Đồng hồ giờ thật: chợ sớm trong sương → chợ ngày → **lên đèn 17:30** → chợ đêm. Mùa hoa Đà Lạt thật: 1–2 mai anh đào, 3–4 phượng tím, 10–11 dã quỳ, 12 Festival Hoa.
- 4 bộ sưu tập hữu hạn công bố trước tổng số (Sổ Đặc Sản 24 món, Bưu thiếp 12 tháng...).

## 6. Viral — thiết kế sẵn (research/00, 03, 05)
- Khung hình viral khóa sẵn: chợ đêm lên đèn nhìn từ bậc thang Hòa Bình.
- Khan hiếm sinh meme có chủ đích: quầy hot hết hàng thật, xếp hàng sữa đậu nành giờ cao điểm.
- Tên món/tên khách ngẫu nhiên "nói thành câu đùa được"; thẻ tổng kết chuyến đi share 1 chạm.
- 2 giờ hẹn chung mỗi ngày (chợ sáng 5h, lên đèn 19h); devlog công khai kiểu Park Jin-won; cụm bài hướng dẫn/SEO cho từng quầy từ ngày đầu.
- Tuyệt đối tránh: điểm thi đua + tiền/quà gắn hứa hẹn tâm linh (nguồn cơn mọi cảnh báo trục lợi) — chợ là thương mại đời thường nên livestream bán hàng dùng được, minh bạch giá.

## 7. Kỹ thuật (research/10)
- **Three.js (TypeScript + Vite) + PWA**, WebGL2. Asset Blender → GLB nén Draco/meshopt + texture KTX2 qua CDN; tải lười theo khu; InstancedMesh cho sạp/hàng lặp lại; bake sáng, không bóng động.
- Ngân sách cứng: tải lần đầu ≤5MB, draw call <100, DPR cap 1.5, mục tiêu 30 FPS ổn định trên Android tầm trung; fallback tour 2D cho máy yếu.
- Multiplayer giai đoạn 2: Colyseus, phòng 30–50 người; giao dịch mua bán đi qua REST riêng, tách khỏi kênh realtime.

## 8. MVP — làm ít mà kỹ (rút từ bài học "18 Levels of Hells": hứa nhiều, bỏ dở)
1. Blockout 2 cao độ + đi dạo được + chợ đêm lên đèn.
2. 6 quầy ăn uống bằng Xu Chợ + giỏ đi chợ.
3. Hộ chiếu 8 dấu + quest ngày + thẻ share.
4. Multiplayer nhẹ + affiliate đặc sản (sau khi có traffic).
