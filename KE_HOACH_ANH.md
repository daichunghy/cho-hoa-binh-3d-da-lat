# KẾ HOẠCH ẢNH — CHỢ HÒA BÌNH ONLINE

> Chung Hy yêu cầu lập ngày 06/11/2026, ngay sau khi CHỐT phong cách.
> Mọi ảnh trong kế hoạch này là **ảnh mẫu tham chiếu** để dựng model 3D + làm giao diện, không phải ảnh chụp game có sẵn.

## 0. Phong cách khóa (CHỐT 06/11/2026)

- Mẫu chốt số 1: `theme/CHOT-phong-cach-cho-dem.png` (ảnh chợ đêm Chung Hy gửi lại và nhắn "chốt") + `theme/mau-np-01-truoc-cho.webp`, `theme/mau-np-03-tren-doi.webp`.
- Nhân vật **chibi đầu to tròn, thân nhỏ** (đầu ≈ 1/2 chiều cao), mặt đơn giản dễ thương — kiểu Niệm Phật Online.
- Camera **góc cao ~45° kiểu diorama**; model 3D stylized, **màu phẳng ấm** (nâu gỗ, vàng đèn, xanh thông), không bán thực.
- Giao diện: panel nâu đậm bo tròn, nút vàng, thẻ tên + cấp trên đầu nhân vật, thanh icon ở đáy, bảng nhiệm vụ bên phải.
- Kiến trúc vẫn bám địa danh thật (đối chiếu `theme/reference/` — ảnh chụp thật) nhưng đơn giản hoá theo style trên.
- Ảnh mẫu tạo mới phải **sạch, không dính logo/watermark của trang khác** (bài học: ảnh mẫu dùng ảnh AFKmobi làm mẫu đã rò logo vào ảnh chợ đêm).

## A. CẤU TRÚC CHỢ & KIẾN TRÚC (nền cho model 3D)

| # | Ảnh | Nội dung cần thể hiện | Dùng để | Trạng thái |
|---|-----|----------------------|---------|-----------|
| A1 | Toàn cảnh 2 cao độ | Đồi Hòa Bình + rạp ở trên, thung lũng + nhà lồng chợ ở dưới, thang + cầu nối, bùng binh hoa | Khóa bố cục bản đồ tổng | Đã có bản bán thực (theme/01) — tạo lại bản chibi |
| A2 | Nhà lồng chợ — mặt tiền ngày | 3 tầng, hàng cửa/cửa cuốn, mái hiên, bảng CHỢ ĐÀ LẠT, sân trước + bùng binh hoa | Model nhà lồng | Đã có mẫu (mau-np-01) |
| A3 | Nhà lồng chợ — mặt tiền đêm | Cùng góc A2 nhưng lên đèn, sương, chợ đêm mở | Đối chiếu ngày/đêm | Chưa có |
| A4 | Bên trong nhà lồng | Lối đi giữa 2 dãy sạp, tầng lửng nhìn xuống, ánh sáng mái | Model nội thất vào được | Chưa có |
| A5 | Rạp Hòa Bình | Mặt tiền rạp + bậc cấp + quảng trường nhỏ trước rạp trên đồi | Model rạp | Đã có mẫu (mau-np-03) |
| A6 | Bậc thang + cầu nổi | Thang 3 chuyến có chiếu nghỉ, cầu vào thẳng tầng 2 chợ | Model thang/cầu | Có trong A1/mau-np-03 — cần ảnh riêng cận cảnh |
| A7 | Đường Nguyễn Thị Minh Khai về đêm | Dãy ki-ốt + gian chợ đêm ngoài trời, đèn đường, sương | Khu chợ đêm ngoài trời | Chưa có |
| A8 | Café Tùng + dãy phố Hòa Bình | Mặt tiền quán cà phê xưa, ki-ốt quanh quảng trường đồi | Chi tiết khu đồi | Chưa có |

## B. NHÂN VẬT (NGƯỜI)

| # | Ảnh | Nội dung cần thể hiện | Dùng để | Trạng thái |
|---|-----|----------------------|---------|-----------|
| B1 | Nhân vật chính chibi — bảng tạo hình | 1 nhân vật đứng thẳng, nhìn trước/bên, tỉ lệ đầu-thân chuẩn khóa | Model nhân vật người chơi | Chưa có (ưu tiên 1) |
| B2 | Biến thể trang phục | 4–6 bộ áo len/khăn/mũ len màu khác nhau cho nam và nữ | Hệ thống đổi đồ avatar | Chưa có |
| B3 | Tiểu thương 6 quầy đặc biệt | Cô bán sữa đậu nành, chú bánh tráng nướng, chủ quán cà phê phin, chị kem bơ/dâu, cô khoai bắp nướng, chủ quầy đặc sản | NPC thường trú từng quầy | Đã có 3/6 trong ảnh CHOT (sữa, bánh tráng, cà phê) |
| B4 | Tiểu thương 5 khu thường | Người bán rau củ, hoa, đồ len, nông sản, đặc sản khô (đội nón lá/tạp dề) | NPC 20 gian hàng | Một phần trong mau-np-01 |
| B5 | Khách đi chợ (NPC nền) | 5–7 mẫu khách: bạn trẻ áo len, cô chú trung niên, em bé, khách chụp ảnh | Đám đông sống trong chợ | Một phần trong các mẫu |
| B6 | Biểu cảm + hành động | Vui, vẫy tay chào, cầm ly sữa, ăn bánh tráng, đóng dấu hộ chiếu | Animation + biểu cảm preset | Chưa có |

## C. GIAN HÀNG & MÓN ĂN / ĐỒ UỐNG

| # | Ảnh | Nội dung cần thể hiện | Dùng để | Trạng thái |
|---|-----|----------------------|---------|-----------|
| C1 | Quầy sữa đậu nành nóng | Khung gỗ, nồi sữa bốc khói, bình rót, ly, bảng giá | Model quầy đặc biệt 1 | Đã có (ảnh CHOT) |
| C2 | Quầy bánh tráng nướng | Bếp nướng, bánh trên vỉ, topping trứng/hành | Model quầy đặc biệt 2 | Đã có (ảnh CHOT) |
| C3 | Quầy cà phê phin/vợt | Phin xếp chồng, vợt vải, ly cà phê đá/sữa | Model quầy đặc biệt 3 | Đã có (ảnh CHOT) |
| C4 | Quầy kem bơ & dâu | Tủ kem, ly kem bơ xanh, dâu tươi | Model quầy đặc biệt 4 | Chưa có |
| C5 | Quầy khoai/bắp nướng | Bếp than hồng, khoai bắp nướng, khói thơm | Model quầy đặc biệt 5 | Chưa có |
| C6 | Quầy đặc sản đóng hộp quà | Kệ hộp quà, mứt, trà, túi giấy gói quà | Model quầy đặc biệt 6 | Chưa có |
| C7 | Gian hàng thường theo 5 khu | Rau củ / hoa / đồ len / nông sản / đặc sản — mỗi khu 1 ảnh mẫu | Model 20 gian nhân bản | Một phần (rau, hoa trong mau-np-01) |
| C8 | Bộ icon món ăn & vật phẩm | Từng món/vật phẩm vẽ riêng nền trong suốt: ly sữa, bánh tráng, cà phê, kem bơ, khoai nướng, hộp quà, áo len… | Giỏ hàng, menu mua, hộ chiếu | Chưa có |

## D. GIAO DIỆN (UI)

| # | Ảnh | Nội dung cần thể hiện | Dùng để | Trạng thái |
|---|-----|----------------------|---------|-----------|
| D1 | HUD chính | Tên + Lv góc trái, Xu Chợ, minimap, thanh icon đáy, bảng nhiệm vụ phải | Chuẩn giao diện trong game | Đã có trong các ảnh mẫu |
| D2 | Menu mua tại quầy | Danh sách món + giá Xu, nút Mua vàng lớn, NPC chế biến | Màn hình mua đồ ăn/uống | Một phần (nút Mua trong ảnh CHOT) |
| D3 | Hộ chiếu Đi Chợ | Sổ hộ chiếu với 9 con dấu theo khu | Màn hình hộ chiếu | Chưa có |
| D4 | Màn hình tạo nhân vật | Chọn giới tính, tóc, màu da, áo len đầu tiên | Onboarding giống đối thủ | Chưa có |

## E. TRUYỀN THÔNG (để sau, khi game chạy được)

| # | Ảnh | Nội dung | Trạng thái |
|---|-----|----------|-----------|
| E1 | Key visual chính | Toàn cảnh chợ ngày + đêm chia đôi, nhân vật chibi vẫy tay | Chưa có |
| E2 | Ảnh thẻ share khoảnh khắc | Khung ảnh chụp trong game gắn tên người chơi + ngày | Chưa có |

## Thứ tự làm

1. **B1** (tạo hình nhân vật chuẩn) + **A3, A4, A6** (bổ sung cấu trúc còn thiếu) — phục vụ dựng model v2 ngay.
2. **B3 (3 quầy còn lại), C4–C6, C8** — đủ bộ 6 quầy đặc biệt.
3. **B2, B4–B6, C7, D2–D4** — hoàn thiện hệ thống.
4. **E** — khi bản chơi được đã ổn.
