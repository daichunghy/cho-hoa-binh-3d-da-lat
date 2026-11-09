# KẾ HOẠCH V6 CHO MUSE AI — "Cảm giác Đà Lạt" + "Chơi được"

> Tài liệu giao việc và hướng dẫn chi tiết cho Muse AI. Đọc kỹ mục 0, 1, 2 và xem tài liệu khảo sát `research/25-thu-thap-web-hoa-sua-hong-tra-cau-thang.md`.
> Code: `prototype-v2/index.html` (chạy trên Three.js r160). Model: `prototype-v2/assets/*.glb`.

---

## 0. Nguyên nhân các lần trước chưa đạt cảm giác Đà Lạt

| # | Vấn đề | Hệ quả thực tế | Cách khắc phục bắt buộc |
|---|--------|----------------|-------------------------|
| 1 | Dựng theo văn bản mô tả chung chung ("chợ đêm đông, đèn vàng ấm") | Ra khung cảnh chợ phương Tây hoặc chợ làng, mất bản sắc Đà Lạt | Dùng **số liệu kích thước và dữ kiện kiến trúc thực tế** đã tra cứu (mục 3). |
| 2 | Model Blender thô: mặt phẳng facet lớn, màu xám phẳng, không chi tiết vỉa hè/đường phố | Nhìn như khối hộp đồ chơi, thiếu sự sống động | Dùng **bộ kit nhỏ, có bevel, map texture chi tiết** thay vì tạo khối rỗng lớn. |
| 3 | Sửa ồ ạt nhiều module cùng lúc | Gây lỗi cú pháp, màn hình đen (TDZ) | Triển khai **từng chặng một**, kiểm tra runtime sạch sau mỗi chặng qua `scripts/diag_runtime.mjs`. |
| 4 | Ảnh tham khảo là hình minh hoạ AI (AFKmobi) | Nhầm phong cách (thành lồng đèn Hội An/Trung Hoa, đường đá cuội) | Chỉ lấy **bố cục quầy sạp + giao diện tương tác (UI)** từ ảnh AFKmobi; còn kiến trúc, ánh sáng, vật liệu phải 100% bám theo **ảnh chợ đêm thực tế và tài liệu di sản**. |

---

## 1. Định hướng nghệ thuật: Đậm chất Đà Lạt về đêm

Từ 2 ảnh tham khảo:

* **Ảnh B (Chợ đêm Đà Lạt chụp từ trên cao — đường Nguyễn Thị Minh Khai)**:
  - **Không gian**: Con đường hẻm dài, lòng đường 14–16 m, hai bên nhà ống 4–5 tầng san sát che khuất bầu trời, chỉ để lộ một dải trời đêm xanh thẫm.
  - **Sạp hàng**: Các sạp quần áo len, áo khoác, đồ đông treo cao kín mít thành hai bức tường sắc màu (đỏ mận, cam đất, xanh jean, trắng len).
  - **Mái bạt**: Bạt sọc 3 màu (xanh dương, đỏ, trắng ngà) giăng chéo, chồng lấn tự nhiên.
  - **Ánh sáng**: Hàng trăm bóng đèn tròn trần treo dọc tuyến phát ánh sáng vàng ấm (3000–3200K) kèm quầng sáng (halo) mờ ảo trong sương. Phía xa cuối đường rực sáng tạo chiều sâu hút mắt.
  - **Mặt đất**: Mặt đường nhựa đen bóng có vệt ướt phản chiếu ánh đèn; vỉa hè thấp 10–12 cm.
  - **Chi tiết đô thị**: Bó dây điện chằng chịt ngang đường, biển hiệu dọc bằng hộp đèn (tiệm vàng, hiệu thuốc), xe máy Wave/Dream dựng sát mép sạp.

* **Ảnh A (Giao diện game AFKmobi)**:
  - **Bố cục sạp**: Biển gỗ ghi rõ tên món và giá tiền to bản ("SỮA ĐẬU NÀNH NÓNG — 15K").
  - **NPC bán hàng**: Đứng sau quầy, có thao tác nấu nướng/rót nước; khói và hơi nước nóng bốc lên nghi ngút giữa trời lạnh.
  - **UI/HUD trực quan**: Nút "MUA / ĂN" lớn ở vị trí dễ bấm; bảng "Nhiệm vụ / Việc tiếp theo" gọn gàng bên góc.

---

## 2. Quy chuẩn kỹ thuật dựng 3D

1. **Bộ kit sạp mô-đun (thay thế khối hộp đơn điệu)**:
   - Sạp treo đồ len: Khung sắt ống đen, thanh treo ngang nhiều tầng áo khoác, khăn len, nón len.
   - Sạp đồ ăn nướng: Bếp than đỏ lửa có khói bốc, vỉ nướng bánh tráng, xiên que.
   - Sạp nồi nước: Nồi nhôm to bốc hơi nước liên tục, ly thuỷ tinh/ly giấy xếp chồng.
   - Quầy ki-ốt: Quầy gỗ hoặc tôn kín gió, có cửa chớp hoặc bạt cuốn.
2. **Chi tiết nhỏ tạo chất Đà Lạt (Props)**:
   - Ghế nhựa thấp đỏ/xanh, bàn nhựa vuông nhỏ.
   - Nồi nấu sữa đậu nành cỡ lớn bốc hơi nghi ngút.
   - Cột điện bê tông kèm bó dây cáp xoắn chằng chịt ngang đường.
   - Cây thông ba lá Đà Lạt quanh bờ dốc.
3. **Poly budget**: Mỗi sạp ≤ 3.000 polygons, tận dụng texture map (noise, nếp vải bạt, gỗ cũ) thay vì cắt poly vụn.

---

## 3. Tuyến hành trình 5 chặng (Đúng thứ tự thực tế người dùng yêu cầu)

### Chặng ①: Tuyến đường Chợ Đêm (Đường Nguyễn Thị Minh Khai)
- **Thông số thực tế**: Chiều dài ~400 m, lòng đường 14–16 m, nối từ cổng chào vào bùng binh trước chợ.
- **Thị giác**: Cảnh đêm sầm uất, hai bên sạp áo len và đồ nướng rực rỡ, chuỗi đèn vàng dẫn thẳng vào mặt tiền chợ Đà Lạt có dòng chữ đỏ "CHỢ ĐÀ LẠT".
- **Gameplay**: Xuất phát từ cổng chào, đi dạo dọc đường, ghé sạp ngắm đồ len, nghe tiếng rao và cảm nhận cái lạnh Đà Lạt (nhiệt độ giảm dần nếu không giữ ấm).

### Chặng ②: Cầu thang di sản Ngô Viết Thụ (Góc Hong Kong bên hông chợ)
- **Thông số thực tế**: Vị trí tại 110 Nguyễn Thị Minh Khai, do KTS Ngô Viết Thụ thiết kế kết nối độ cao từ thung lũng (y ≈ 0) lên đỉnh đồi (y ≈ 17 m).
- **Thị giác**: Cầu thang bê tông cốt thép rộng, lan can sắt tối màu, các chiếu nghỉ có quán cóc kê ghế nhựa. Điểm nhìn từ trên xuống bao quát toàn bộ phố chợ đêm lung linh.
- **Gameplay**: Leo từng bậc thang, thưởng ngoạn "Góc Hong Kong", camera lia góc nhìn cinematic từ trên cao xuống phố chợ.

### Chặng ③: Quảng trường Khu Hòa Bình & Rạp 3 Tháng 4
- **Thông số thực tế**: Đỉnh đồi trung tâm, rạp chiếu bóng Hòa Bình xây dựng từ năm 1937 với mái vòm cong màu vàng đặc trưng, trước rạp là quảng trường rộng lát bê tông, đài tưởng niệm và bồn hoa.
- **Thị giác**: Kiến trúc hoài niệm màu vàng, quán Cà phê Tùng số 6, âm nhạc đường phố vang vọng.
- **Gameplay**: Check-in trước Rạp 3 Tháng 4, nhận dấu Hộ chiếu "Đồi Hòa Bình", nghe nhạc acoustic tại góc hát.

### Chặng ④: Sữa đậu nành Quán Hoa Sữa (3F Tăng Bạt Hổ)
- **Thông số thực tế**: Đường Tăng Bạt Hổ dài 250 m, lòng đường 5 m, vỉa hè 2 m. Quán Hoa Sữa tại số 3F (số 64 cũ), cách chợ 50 m, hơn 40 năm tuổi.
- **Thị giác**: Quán hoàn toàn **không mái che**, ghế nhựa thấp tràn vỉa hè ngã ba, nồi sữa nhôm siêu to bốc hơi nghi ngút, tủ kính đựng bánh su kem, bánh sừng trâu, bánh tiêu. Khách ngồi co ro ôm ly sữa nóng trong gió lạnh ("sữa đậu nành ôm").
- **Gameplay**: Chọn món đúng điệu Đà Lạt: "nành bò" (pha sữa bò), "nành đường", ăn kèm bánh tiêu chấm sữa nóng → Hồi phục 100% thanh độ ấm.

### Chặng ⑤: Hồng Trà Hòa Bình (Ki-ốt 30–32 Khu Hòa Bình)
- **Thông số thực tế**: Ki-ốt 30–32 thuộc cụm thương mại Khu Hòa Bình trên đỉnh đồi, phục vụ hồng trà đậm vị Signature của thương hiệu Phan Minh Trà, mở cửa 9:00 – 23:00.
- **Thị giác**: Ki-ốt ấm cúng, biển hiệu đỏ chữ vàng trang nhã, quầy pha chế thơm mùi trà đen và thảo mộc, ly trà bốc khói nhẹ.
- **Gameplay**: Thưởng thức ly Hồng trà signature hoặc Trà sữa hạnh nhân chôm chôm, hoàn thành trọn vẹn chuyến du ngoạn Chợ Hòa Bình Đà Lạt, nhận thẻ tổng kết lưu niệm.

---

## 4. Cổng kiểm tra bắt buộc (Quality Gate)

Sau khi Muse AI hoàn thành chỉnh sửa bất kỳ phần nào, PHẢI chạy chuỗi kiểm tra sau trong terminal:

```bash
cd prototype-v2
DIAG_NODE_MODULES=/tmp/diag/node_modules node scripts/diag_runtime.mjs 90
python3 scripts/package_standalone.py
```

* Yêu cầu đạt: `[diag] ANIMATE 90 frames SẠCH — không ngoại lệ` và file `index-standalone.html` được đóng gói thành công (< 10 MB).
* Nếu có bất kỳ lỗi nào xuất hiện, Muse AI phải dừng lại sửa dứt điểm trước khi chuyển sang bước tiếp theo.
