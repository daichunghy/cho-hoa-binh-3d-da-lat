# Research 21 — Tham khảo 3D, đường thật, bậc tam cấp, Tăng Bạt Hổ, đài phun nước & khu quần áo (V5.5)

> Viết 09/11/2026, TRƯỚC phần sửa hình của đợt V5.5, theo lệnh Chung Hy: "bạn chưa
> hiểu về con đường này và chợ đó" — nghiên cứu để hiểu đúng trước khi sửa.
> Nguồn: tìm kiếm web 09/11/2026 (bài quy hoạch khu Hòa Bình trên nguoidothi.net.vn,
> lamdong.edu.vn, ashui.com, thethaovanhoa.vn; hồ sơ quán Hoa Sữa trên latour.vn,
> mytour.vn, vinpearl.com, lofita.vn), ảnh thật sẵn có 01–39 + 5 ảnh mới 40–44
> trong `theme/real-market/` (ghi nguồn ở SOURCES.md).

## 1. Ai đã tái dựng Chợ Đà Lạt / Khu Hòa Bình dạng 3D chưa?

- **Không tìm thấy mô hình 3D công khai đáng kể riêng cho Chợ Đà Lạt** (Sketchfab,
  3D Warehouse, game/mod) ở thời điểm tìm 09/11/2026. Các bản tái dựng "chính thống"
  hiện có là:
  - **Lớp 3D photogrammetry của Google Earth / Bing Maps** cho trung tâm Đà Lạt
    (GeoHack liệt kê Bing 3D + Google Earth cho trang Da Lat Market): khối nhà theo
    chiều cao thật, chợ là MỘT KHỐI LỚN án ngữ cuối trục đường, địa hình dốc là mảng
    liên tục — đọc bằng silhouette, không đọc bằng chi tiết sạp.
  - **Nghiên cứu UAV photogrammetry Đà Lạt** (IOP Conf. Series 1391, 2024): dựng mô
    hình 3D từ ảnh bay, tách DTM (địa hình trơ) khỏi DSM (vật thể trên mặt đất) —
    đúng cách game đang làm (groundH riêng, vật thể riêng).
  - **Mô hình thu nhỏ Chợ Đà Lạt ở Đường hầm đất sét** (Clay Tunnel): xử lý biểu
    tượng — giữ mặt tiền + khối tháp làm dấu ấn, giản lược mọi thứ còn lại.
- **Sự thật kiến trúc quan trọng:** cầu nổi nối Hòa Bình → tầng 2 chợ và cầu thang
  lớn xuống chợ là thiết kế của **KTS Ngô Viết Thụ** (thethaovanhoa.vn) — cầu thang
  là CÔNG TRÌNH ĐIỂM NHẤN của khu, không phải lối đi phụ. Trong game nó phải đọc
  như quảng trường bậc cấp, không phải dải thang.
- **Trục quy hoạch của cả khu** (đồ án 1/500 khu trung tâm Hòa Bình): trục chính đi
  từ **vòng xoay đài phun nước** (Nguyễn Văn Cừ / Lê Đại Hành / Trần Quốc Toản, gần
  cầu Ông Đạo, phía hồ Xuân Hương) THẲNG lên Dinh tỉnh trưởng, chạy qua chợ +
  đường Nguyễn Thị Minh Khai (được quy hoạch thành quảng trường trung tâm). Tức:
  đài phun nước nằm ở ĐẦU DƯỚI của trục (phía đông–nam, về phía hồ), đồi Hòa Bình
  ở đầu trên; chợ + bậc thang nằm giữa trục.

**Bài học áp dụng cho game:**
1. Ưu tiên silhouette: mặt tiền chợ + tượng đài + thang rộng phải đọc được từ xa
   (khung mở đầu), chi tiết sạp là lớp thứ hai.
2. Đường vào là TRỤC THẲNG có điểm nhìn cuối (vista): hai dãy nhà LIÊN TỤC hai bên
   tạo "ống" dẫn mắt về bùng binh/mặt tiền — không ngắt quãng bằng mảng trống.
3. Bậc thang là điểm nhấn kiến trúc: bề mặt bậc là KHÔNG GIAN Ở (ngồi ăn, bán
   hàng), không chỉ là mặt di chuyển.

## 2. Con đường vào chợ — Nguyễn Thị Minh Khai (ảnh 06, 07, 40, 43)

- Mặt cắt đã đo ở research/20b: tổng ~16m = vỉa hè 3m + lòng đường 10m + vỉa hè 3m.
- Ngày (ảnh 07, 40): dãy mặt tiền nhà phố 3–5 tầng LIÊN TỤC hai bên, biển hiệu nhỏ,
  ban công; lòng đường nhựa sẫm, vỉa hè lát gạch sáng hơn nhựa nhưng sẫm hơn sân
  chợ; xe máy đậu dọc hai lề.
- Đêm (ảnh 06, 43): sạp dựng tràn hai bên vỉa hè + một phần lòng đường, mái bạt sọc,
  người + xe len giữa; đường vẫn RỘNG — cảm giác đông nhưng không chật vì mặt cắt
  lớn và sạp lùi hẳn về hai phía.
- Kết luận cho game: muốn hết "chen chúc" phải nới KHOẢNG TRỐNG GIỮA HAI MẶT SẠP
  (hiện 13,5u) — đợt này đặt đích ×2,5 = 33,75u ở đoạn đường vào (x −58..−35, nơi
  có đủ hai hàng sạp và không bị mặt tiền nhà lồng khóa cứng); đoạn trước mặt tiền
  (x −34..34) bị lưng sạp chạm cột mặt tiền z=12 nên không dời được hàng nam —
  xử lý bằng dời cụm bàn ăn + thưa đám đông khỏi dải đi bộ (ghi rõ trong checklist).

## 3. Bậc tam cấp Hòa Bình (ảnh 08, 09, 10, 13, 42)

- Ảnh 08 (chụp từ đỉnh thang nhìn xuống): bậc RỘNG (toàn cảnh ~15–20m), người
  NGỒI ĂN NGAY TRÊN BẬC bằng ghế nhựa nhỏ, ngồi thành cặp/nhóm ĐỐI DIỆN nhau qua
  mặt bậc; hàng rong bám hai bên và các chiếu nghỉ; chân thang là biển xe máy +
  đường chợ; đỉnh thang là khu Hòa Bình (Thương xá La Tulipe bên trái).
- Ảnh 09: đêm đông kín bậc — bậc là "khán đài" của chợ. Ảnh 13: hàng nướng đặt
  ngay trên bậc.
- Game hiện có: thang 22u rộng (x −11..11) + thềm 3 cấp hai bên + 28+ người ngồi
  + 2 điểm bán trên bậc. Còn thiếu so với ảnh: mật độ người ngồi ăn THEO BẬC kiểu
  đối diện nhau, điểm bán ở các CHIẾU NGHỈ, và đời sống ở hai thềm bên (bàn thấp).
  → Đợt này bổ sung đúng các lớp đó, không nới hình học thang (đụng địa hình lõi).

## 4. Góc sữa đậu nành Tăng Bạt Hổ (ảnh 38, 41)

- **Quán Hoa Sữa, 64 Tăng Bạt Hổ, Phường 1** (một nguồn ghi 3F Tăng Bạt Hổ) — cách
  chợ Đà Lạt chỉ ~50m, tồn tại 40+ năm, là "góc sữa đậu nành" nổi tiếng nhất.
- Dạng quán VỈA HÈ đúng nghĩa: một **nồi nấu sữa siêu to** bốc hơi, tủ kính bánh
  ngọt (bánh tiêu, bánh sừng trâu/con sò), vài bộ **bàn ghế nhựa thấp** xếp dọc
  vỉa hè, ly thủy tinh đựng sữa; mở ~16:00–22:00 (có nguồn 23:30), đông nhất ~21h.
- Tăng Bạt Hổ là phố nhỏ NGAY SÁT phía tây chợ — đầu trục đường vào. → Game đặt
  landmark "SỮA ĐẬU NÀNH HOA SỮA — GÓC TĂNG BẠT HỔ" tại đầu tây của trục đường
  vào kéo dài (cạnh cổng chào mới), là sạp mua được (khu đồ uống) + cụm bàn ghế
  thấp + nồi lớn bốc khói + khách ngồi đêm.

## 5. Đài phun nước & khu quần áo (gói địa lý của Chung Hy)

- Đài phun nước thật: vòng xoay Nguyễn Văn Cừ / Lê Đại Hành / Trần Quốc Toản gần
  cầu Ông Đạo — đầu dưới của trục quy hoạch (mục 1). Trong game KHÔNG có đài phun
  nước (đã kiểm code). **Neo đặt trong game (theo bố cục Chung Hy mô tả):** đài
  phun nước đặt ở SÂN TRƯỚC phía đông bậc tam cấp — khoảng sân trống hiện tại
  (x ~21..34, z −2..9, trước góc tây nhà lồng, dưới chân cầu nổi) — làm mốc của
  quảng trường bậc cấp: bồn tròn + cột nước + đèn, người chơi đi qua là thấy.
- Khu quần áo: chợ đêm Đà Lạt bán quần áo/áo len dọc trục Nguyễn Thị Minh Khai và
  trong chợ (ảnh 43; các cửa hàng Áo Len Đà Lạt quanh phường 1). **Neo đặt trong
  game:** dãy sạp + giá treo QUẦN ÁO ở MÉ ĐÔNG của sân đài phun nước (x ~36,5,
  quay mặt về phía tây) — tức BÊN PHẢI khi đứng từ phía chợ nhìn lên bậc tam cấp,
  ĐỐI DIỆN bậc tam cấp qua sân và ĐỐI DIỆN đài phun nước. Đặc điểm nhận diện khác
  hẳn khu ăn: mắc/giá treo áo khoác + áo len treo dày, không khói, không bàn ăn,
  có người ướm đồ. Hai sạp bán được thuộc khu Đồ len trong Sổ Đặc Sản.

## 6. Số đích V5.5 (từ nghiên cứu này + brief)

| Hạng mục | Hiện tại | Đích |
|---|---|---|
| Khoảng trống 2 mặt sạp (đoạn vào) | 13,5u (mặt −4,6 / 8,9) | **33,75u (×2,5)** (mặt −13,6 / 20,15) |
| Chiều dài đoạn đường vào (cổng → bùng binh) | ~46u (cổng x=−81) | **~96u (×2)** (cổng x=−131) |
| Rig ngày | exposure 1,05 · sun 1,1 · hemi 0,85 · amb 0,12 · sương 0,0075 | exposure 0,88 · sun 0,95 · hemi 0,55 · amb 0,10 · sương 0,0058 + mặt tiền ngả kem + tách tông nền (nhựa < vỉa hè < sân) |
| Khung mở đầu | spawn (−76, 5,6), camPitch 0,8 — khung chủ yếu là mặt đường | spawn đầu đường mới (−126, 5,6), camPitch 0,55 — trục dài + 2 hàng sạp dẫn mắt về tượng + mặt tiền |
| Bậc tam cấp | 28+ người ngồi, 2 điểm bán | + người ngồi ăn đối diện theo bậc, + 2 điểm bán chiếu nghỉ, + cụm bàn thấp 2 thềm bên |
| Đài phun nước / khu quần áo | chưa có / chỉ có trong nhà lồng | đài phun nước ở sân đông bậc tam cấp + dãy quần áo mé đông sân |
