# REALISM-1 — Danh sách lệch (BEFORE) — Chợ Hòa Bình 3D

> Bước 1 vòng REALISM-1: chỉ đối chiếu + liệt kê lệch, chưa sửa gì.
> Ngày lập: 09/11/2026. Người soi: Muse (đọc trực tiếp 4 ảnh ghép PNG).

## Cặp đối chiếu

| Góc | Ảnh thật (trái) | Render (phải) | Ảnh ghép |
|---|---|---|---|
| r1 — mặt tiền + bùng binh | `theme/real-market/01-mat-tien-cho-ngay.jpg` (1400×933) | `renders/real1-before-r1.png` (640×480), cam (-38, 2.0, -14) → (0, 5, 12) | `renders/real1-cmp-before-r1.png` (1813×640) |
| r2 — đường vào từ trên cao | `theme/real-market/43-cho-dem-quan-ao.jpg` (1536×1229) | `renders/real1-before-r2.png` (640×480), cam (-100, groundH+12, 5.6) → (-30, 1.5, 5) | `renders/real1-cmp-before-r2.png` (1653×640) |
| r3 — đỉnh bậc tam cấp nhìn xuống đảo | `theme/real-market/10-bac-thang-nhin-xuong-bung-binh.jpg` (1200×800) | `renders/real1-before-r3.png` (640×480), cam (0, 18.8, -27) → (-30, 1.5, -6) | `renders/real1-cmp-before-r3.png` (1813×640) |
| r4 — chợ đêm tầm mắt | `theme/real-market/33-ganh-hang-rong-dem.jpg` (1280×720) | `renders/real1-before-r4.png` (640×480), cam (-47, groundH+1.7, 6) → (-38, 1.2, -13) | `renders/real1-cmp-before-r4.png` (1991×640) |

Render bằng `scripts/render_real1.py` (sao chép `render_bd2.py`, giữ nguyên parser/builder/`groundH`, chỉ thay 4 shot cuối; Cycles 24 mẫu, 640×480, Blender 5.0.1). Parse lúc chạy: 44 sạp, 14 shophouse, 24 hàng chờ, 50 người ngồi bậc, tổng 198 người trong cảnh.

## Giới hạn của phép đối chiếu này (đọc trước khi chấm)

- Cảnh mini Blender dùng **vật liệu phẳng mô phỏng**: không có GLB nhà lồng chợ — facade trong render là **hộp mô phỏng**; không vẽ **texture/chữ canvas của bản web**. Mọi lệch về chữ biển hiệu, lưới cửa sổ facade, họa tiết banner/quần áo được ghi nhãn **[chỉ chấm được ở code/web]** — render này không kết luận được phần đó.
- Cả 4 render dùng chung 1 mặt trời + nền trời xám phẳng (world 0.52/0.56/0.60), trong khi 3/4 ảnh thật (r2, r3, r4) là **cảnh đêm**. Lệch ngày/đêm là lệch hệ thống của phép đo, không phải lỗi riêng từng góc.
- Số đo màu (PIL, lượng tử hóa 8 màu median-cut, đếm pixel): 4 tông màu chiếm tỉ lệ lớn nhất trong render lần lượt là r1 **75%**, r2 **71%**, r3 **64%**, r4 **63%** tổng số pixel, và các tông trội đều là xám/xanh nhạt gần như không bão hòa (ví dụ (176,179,181), (175,179,181)). Ở ảnh thật, 4 tông trội chỉ chiếm 54–61% và gồm các tông tối đêm/xanh trời bão hòa.

---

## R1 — Mặt tiền + bùng binh (ảnh thật 01, ban ngày)

**Khung hình/hình học (lệch lớn nhất của góc này):**

1. Mặt tiền chợ **không xuất hiện chút nào** trong render (0% khung): khung phải bị một **mảng dốc xanh lá nhạt dạng tam giác facet chiếm ~40% bề rộng bên trái**, tiếp nối là các **mảng tường be trơn** ở giữa–phải và **nền xám phẳng chiếm ~35% chiều cao phía dưới**; bầu trời xám phẳng chiếm ~25% phía trên. Nhận diện được duy nhất: mảnh chữ "SAN" ở mép trên giữa–phải và một lát cột tượng ở mép phải cùng (~1% bề rộng). Trong ảnh thật, facade cong màu trắng chiếm ~55% bề rộng giữa khung, tượng đài chiếm ~15% bề rộng bên trái, đường nhựa + xe cộ chiếm toàn bộ 40% dưới khung.

**Vật liệu bề mặt:**

2. Mặt đường trong render là **1 tông xám sáng phẳng duy nhất** (hai tông trội (175,179,181) = 24% và (181,180,176) = 21% tổng pixel, không một vết vá/bóng loang); ảnh thật là nhựa đường **xám đen** có vá tông, vệt bánh xe và **bóng cây loang rõ ở góc dưới phải**.
3. Mảng dốc trong render gồm các **mặt tam giác phẳng cạnh sắc, mỗi mặt rộng ~8–10% khung**, màu xanh mint đồng nhất; sườn đồi thật ở mép trái ảnh có cây, đất, lan can và nhà xen kẽ, không có mặt phẳng nào lớn như vậy.

**Ánh sáng/bóng:**

4. Trời render xám đồng nhất 100% vùng trời; trời thật **xanh dương + mây trắng** chiếm ~25% chiều cao khung, nắng gắt đổ bóng xe/người rõ xuống mặt đường. Trong render gần như **không có bóng đổ nào đọc được** ở tiền cảnh.

**Rác đường phố VN:**

5. Đếm trong render: **0 xe tải, 0 xe bán tải, 0 xe máy, 0 biển hiệu có chữ, 0 dây điện**. Ảnh thật đếm được: 1 xe tải thùng đỏ giữa–phải, 1 bán tải trắng, ≥8 xe máy ở tiền cảnh, dãy **banner quảng cáo xanh/vàng chạy ngang tầng trệt** facade, bó dây điện ở phía phải facade, chữ đỏ "CHỢ ĐÀ LẠT" trên mái, hàng cây tùng + khinh khí cầu trang trí trên nóc. — Riêng chữ/biển/banner thuộc nhóm **[chỉ chấm được ở code/web]** (facade là hộp mô phỏng, không có canvas).

**Cây xanh:**

6. Render: **0 cây** lọt khung. Ảnh thật: hàng ~8 cây tùng bách cao mảnh trên nóc chợ, 1 cây xanh lớn mép trái, hàng rào cây cắt tỉa quanh đảo giao thông ở giữa dưới.

**Người:**

7. Render: **0 người** lọt khung. Ảnh thật: hàng chục người đứng trước cửa chợ ở giữa khung + người đi xe máy đội mũ bảo hiểm ở tiền cảnh chiếm tới ~20% chiều cao khung, thấy rõ áo khoác caro, áo hồng, mũ đỏ.

---

## R2 — Đường vào từ trên cao (ảnh thật 43, chợ đêm quần áo)

**Ánh sáng/bóng (lệch lớn nhất của góc này):**

1. Ảnh thật là **đêm**: hàng trăm bóng đèn sạp phát sáng ấm, ánh sáng hắt lên quần áo và mặt người, cuối đường sáng rực tới điểm biến mất. Render là **trưa phẳng**: trời xám chiếm ~40% phía trên, **0 điểm sáng phát xạ** trong toàn khung; bóng duy nhất là 3–4 **vệt bóng hình chữ nhật cạnh sắc** của khối shophouse đổ lên mặt đường phía phải.

**Vật liệu bề mặt:**

2. Mặt đường render là **1 mặt phẳng xám trơn chiếm ~45% chiều cao phía dưới khung** (tông trội (176,179,181) = 28% tổng pixel); ở ảnh thật mặt đường gần như bị sạp và người che kín, phần lộ ra là nhựa tối có rác nhỏ, bóng dây cáp và vệt sáng đèn.
3. Sạp hai bên trong render là **hộp rỗng + mái phiến phẳng pastel** (hồng/xanh/be), 13 sạp bắc + 13 sạp nam xếp đều tăm tắp sát mép đường; sạp thật lấn ra chiếm tới ~60% bề rộng lòng đường, mái là bạt/tôn gợn sóng, dưới mái là **giá treo quần áo ken đặc** đỏ/xanh/trắng.

**Rác đường phố VN:**

4. Đếm trong render: **0 dây điện, 0 biển dọc, 0 máy lạnh, 0 ghế nhựa, 0 thùng xốp, 0 món quần áo treo**. Ảnh thật: mạng dây điện ≥10 sợi chăng ngang tiền cảnh dưới khung, biển dọc hai phía (neon đỏ phía xa trái, biển vàng lớn phía phải giữa khung), ban công + máy lạnh trên facade hai bên, ghế nhựa và sọt hàng dưới các sạp. — Chữ trên biển thuộc nhóm **[chỉ chấm được ở code/web]**; hình khối dây/biển/máy lạnh thì chấm được ngay ở render này và đều vắng.

**Cây xanh:**

5. Góc này ảnh thật cũng là hẻm phố không cây — **không ghi nhận lệch cây xanh** ở r2.

**Người:**

6. Ảnh thật: đám đông **hàng trăm người** lấp kín lòng đường từ tiền cảnh tới điểm biến mất ở 1/3 trên khung. Render: người chỉ là các **chấm màu cao 2–5 px** điểm dọc bậc thang/đảo ở giữa xa; **nửa dưới khung (tiền cảnh) có 0 người**, dù tổng cảnh có 198 người — mật độ nơi camera nhìn gần nhất bằng không.

**Hình học phụ:**

7. Đảo + tượng ở giữa xa trong render đọc thành **đĩa trắng phẳng + cột trắng mảnh**; dãy nhà hai bên là các **tháp trắng trơn có nắp nâu mỏng**, 3 tháp trái và ~4 tháp phải giống hệt nhau, trong khi nhà thật khác nhau từng căn về chiều cao, màu sơn, mái và biển.

---

## R3 — Đỉnh bậc tam cấp nhìn xuống đảo (ảnh thật 10, đêm đông nghẹt)

**Người (lệch lớn nhất của toàn bộ vòng đối chiếu):**

1. Tiền cảnh ảnh thật: **≥50 mặt người/thân người đọc rõ** trong 1/3 dưới khung (áo khoác tối, mũ len đỏ, khăn quàng, mũ họa tiết da báo, tay nắm tay, túi xách), toàn khung ước **hàng trăm người** chen vai trên bậc, khoảng cách người–người < 0,5 m. Render: đếm được **~15 hình người ở tiền cảnh–trung cảnh**, mỗi hình là **1 trụ capsule + đầu cầu cùng một màu pastel** (hồng, xanh ngọc, xanh mint, xám, trắng) — **0 khuôn mặt, 0 tóc, 0 tay chân, 0 họa tiết áo**; khoảng cách giữa các capsule vài mét, mỗi capsule đổ **1 bóng oval cứng** sang phải. Màu áo pastel đơn sắc cũng ngược với ảnh thật (đa số áo tối + điểm đỏ).

**Vật liệu bề mặt/hình học:**

2. Bậc tam cấp trong render đọc thành **dốc phẳng facet trắng/xám nhạt chiếm ~55% chiều cao phía dưới**, chỉ thấy 4–5 mặt phẳng lớn, **0 gờ bậc/0 cạnh bậc** đọc được; bậc thật bị người phủ kín nhưng vẫn thấy cạnh bậc, tay vịn và đồ ăn bày trên bậc.
3. Nhà lồng chợ phía trái–giữa render là **1 hộp be trơn chiếm ~25% bề rộng**, trước hộp có 3 sạp nhỏ rỗng; phía phải ảnh thật là khối shop mái tôn xanh lá có **biển sáng + đèn viền**, phía trái là dãy biển quảng cáo sáng. — Chữ biển thuộc **[chỉ chấm được ở code/web]**, nhưng khối mái tôn xanh + dải sáng thì vắng hẳn trong render.

**Ánh sáng/bóng:**

4. Ảnh thật: đêm, **≥4 bảng quảng cáo phát sáng** ở 1/3 trên (gồm 1 màn hình lớn), đèn shop hắt ấm, tượng được rọi sáng giữa đám đông. Render: ngày phẳng, tượng rút thành **cột trắng + quả cầu trên đỉnh (dạng kẹo mút) ở giữa khung, rộng ~2% khung**, không rọi sáng, xung quanh không một bóng người.

**Rác đường phố VN:**

5. Render: **0 xe máy, 0 bảng hiệu, 0 túi/giỏ hàng, 0 bạt che**. Ảnh thật: xe máy đỗ mép khung, người cầm túi nilon/giỏ khắp tiền cảnh, ô/bạt của sạp ở trung cảnh, cổng chào ở render (khung chữ nhật mảnh phía xa phải) không mang biển/chữ nào.

**Cây xanh:**

6. Ảnh thật có **1 cây thông lớn tán tối chiếm ~15% chiều cao khung ở giữa–phải**, che một phần dãy shop. Render: **0 cây** trong toàn khung.

**Hình học phụ:**

7. Hàng nhà phía xa phải trong render là **7 tháp trắng gần như giống hệt nhau** (cùng cao, cùng nắp nâu mỏng) xếp hàng đều; dãy nhà thật phía xa khác chiều cao/màu/ánh đèn từng căn và có biển khách sạn phát sáng.

---

## R4 — Chợ đêm tầm mắt (ảnh thật 33, gánh hàng rong)

**Khung hình/vật liệu bề mặt:**

1. Render: **~50% chiều cao phía dưới là mặt đường xám phẳng trống trơn** (tông trội (151,149,146) = 21% tổng pixel), **~45% phía trên–trái là tường dốc xanh mint facet** với 3 mặt tam giác lớn; trải nghiệm "sạp sát mặt hai bên" của ảnh thật không tồn tại — sạp trong render là **~6 hộp be rỗng nằm trong một rãnh tối dưới chân dốc** ở giữa khung, **0 món hàng** trên bất kỳ sạp nào.
2. Phía phải ảnh thật bị **đống thú bông ≥30 món có lông xù** lấp ~25% bề rộng từ trên xuống dưới khung; phía phải render chỉ là **tường bùng binh xám trơn + cột tượng trắng đội cầu low-poly** (~8% bề rộng), bề mặt nhẵn tuyệt đối.

**Ánh sáng/bóng:**

3. Ảnh thật: đêm với **1 bóng đèn treo chói ở trên giữa khung**, đèn shop L'angfarm hắt sáng bên trái, đèn pha xe máy ở trung cảnh. Render: ngày phẳng, **0 nguồn sáng cục bộ**; điểm tối nhất là **vệt bóng xám dài ~30% bề rộng** của tường bùng binh đổ ngang giữa–phải khung — bóng "sạch" hình học, không có loang sáng đèn như thật.

**Rác đường phố VN (góc này lệch đậm nhất ở nhóm này):**

4. Yếu tố làm nên ảnh thật **vắng toàn bộ** trong render: người phụ nữ đội **nón lá gánh đòn gánh + 2 thúng** ở tiền cảnh trái (cao ~35% khung), **giỏ nhựa đỏ** giữa khung, xe máy có biển số đọc được ở trái–giữa, **≥5 sợi dây điện** vắt ngang nền trời, biển + mái hiên L'angfarm phát sáng bên trái, thúng rau ở góc dưới trái. Đếm trong render: 0 đòn gánh/thúng, 0 giỏ, 0 xe máy, 0 dây, 0 biển. — Chữ trên biển L'angfarm thuộc **[chỉ chấm được ở code/web]**; đòn gánh, giỏ, xe, dây là hình khối, chấm được ở render và đều thiếu.

**Cây xanh:**

5. Ảnh thật góc này không có cây trong khung — **không ghi nhận lệch cây xanh** ở r4.

**Người:**

6. Ảnh thật: ~15 người đọc rõ mặt/áo ở tầm mắt, người gần nhất (cô gánh hàng) cao ~**70% chiều cao khung**, thấy rõ mặt nghiêng, áo tím, nón lá; thêm cô bán hàng áo xanh đeo khẩu trang, bé gái áo trắng. Render: **~7 trụ capsule nhỏ** (cam, hồng, vàng) đứng ở mép bùng binh giữa–phải, cao nhất ~**5% chiều cao khung**, không mặt, không tóc, không nón, không tư thế gánh/đứng bán.

---

## 5 lệch lớn nhất toàn vòng (xếp theo mức phá vỡ nhận diện cảnh)

1. **R1 mất hẳn chủ thể:** mặt tiền chợ + tượng đài không lọt khung render — khung bị dốc facet xanh (~40%) và tường be trơn nuốt trọn; đây là lệch hình học/khung hình, không phải lệch chất liệu.
2. **Ngày/đêm + 0 điểm sáng:** 3/4 ảnh thật là đêm với hàng trăm đèn sạp/biển phát sáng; cả 4 render là trưa xám phẳng, 0 nguồn sáng phát xạ — toàn bộ cảm giác chợ đêm biến mất (r2, r3, r4).
3. **Người = capsule pastel đơn sắc:** trụ + đầu cầu cùng màu, 0 mặt/tóc/tay chân; mật độ sụp đổ — r3 chỉ ~15 capsule so với hàng trăm người thật, r1/r4 tiền cảnh gần như 0 người.
4. **Rác đường phố VN vắng toàn diện:** cộng cả 4 render: 0 dây điện, 0 xe máy/xe tải, 0 máy lạnh/bồn nước, 0 biển dọc, 0 bạt sọc, 0 ghế nhựa, 0 thùng xốp, 0 đòn gánh — trong khi ảnh thật góc nào cũng có ít nhất 3 nhóm này.
5. **Bề mặt phẳng đơn tông chiếm đa số khung:** mặt đường 1 tông xám chiếm ~45–50% khung ở r2/r4; bậc thang đọc thành dốc facet ở r3; đo PIL: 4 tông phẳng trội chiếm 63–75% pixel render (ảnh thật 54–61% và đa dạng bão hòa hơn hẳn).
