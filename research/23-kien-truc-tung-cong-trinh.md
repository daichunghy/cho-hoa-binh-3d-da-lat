# 23 — Kiến trúc từng công trình: Chợ Hòa Bình / Chợ Đà Lạt

> Mục đích: hồ sơ đối chiếu từng công trình quanh khu Hòa Bình để dựng/sửa model 3D đúng ảnh thật, tránh dựng theo trí nhớ. Nguồn chính: bộ 44 ảnh thật `theme/real-market/` + `SOURCES.md`, `research/11`, `17`, `21`, đối chiếu model trong `prototype-v2/V4-CHECKLIST.md` (GEOMETRY-2, BLENDER-DEEP-1/2) và code `prototype-v2/index.html`; bổ sung web ghi URL ở từng mục. Chỗ không có ảnh/nguồn riêng ghi thẳng "chưa đủ tư liệu", không suy diễn.

## 1. Nhà lồng Chợ Đà Lạt

- **(1) Tư liệu đã có:** ảnh 01 (mặt tiền ngày), 02–03 (mặt đồi từ cầu bộ hành), 05 (đêm), 16–19 (trong nhà), 24–25 (chợ cũ 1937); Wikipedia: https://vi.wikipedia.org/wiki/Ch%E1%BB%A3_%C4%90%C3%A0_L%E1%BA%A1t ; Vinpearl: https://vinpearl.com/vi/cho-da-lat
- **(2) Đặc điểm khóa:** khối cong ôm bùng binh, sơn kem/trắng ngà `#F2EAD8`, khối phụ cam đất nhạt; trệt = ki-ốt + băng biển quảng cáo liền mạch + LED đỏ ở cửa chính; tầng 2 dải cửa sổ + dải zigzag/chevron trắng (di sản chợ cũ 1937); tầng 3 dải cửa sổ dài + lam ngang trắng; chữ nổi serif "CHỢ ĐÀ LẠT" đỏ sẫm `#B3392B` (mặt đồi đỏ gỉ, trên tường gạch men trắng); sân thượng lan can kính + thông cột; mặt đồi có tháp thang máy kính xanh lá sát cửa tầng 2, bạt sọc xanh dương–trắng ở cửa, cầu thang trắng ngoài trời; trong nhà: lối đặc sản hẹp, biển quầy lớn trắng/vàng chữ đỏ + số quầy, đèn tuýp trắng, tầng rau có lửng kính nhìn xuống, sàn ướt.
- **Giờ khóa cho chu kỳ ngày/đêm:** nhà lồng KHÔNG bán tối — đóng ~18:00–19:00 (Wikipedia: đóng 18h; các nguồn hướng dẫn: 6:30–19:00); khu đặc sản trong nhà mở tới ~21–22h (Vinpearl). Đêm trong game nhà lồng phải tối/đóng, hoạt động dồn ra chợ đêm ngoài trời.
- **(3) Đối chiếu model hiện tại:** đúng các khóa chính — chữ đỏ 2 mặt, zigzag, louver, băng hồng đào, pano trệt + LED, thang máy kính, bạt sọc, sân thượng (V4 mục A); lệch trước đây: thân từng đọc như tấm phẳng phát sáng, tầng trệt từng là cửa cuốn xám đóng (research/17 điểm 3–4) — đã sửa dần qua V4.1–V4.5 (40 quầy, lửng kính, thang trong nhà).
- **(4) Đã sửa trong BLENDER-DEEP-2:** không sửa trực tiếp nhà lồng; đợt này chỉ giữ nguyên dãy sạp trước mặt tiền (z=11) vì lưng sạp chạm cột nhà lồng — giới hạn cứng, không thuộc trục đường vào.
- **(5) Chưa đủ tư liệu:** số tầng/bố cục cầu kính đầy đủ trong nhà chưa rõ từ ảnh (research/11 mục 10) — không khẳng định sơ đồ chi tiết.

## 2. Chợ đêm Âm Phủ (ngoài trời — bổ sung cho chu kỳ ngày/đêm)

- **(1) Tư liệu đã có:** ảnh 04, 06, 09, 10, 28–35, 39–40, 43; Vinpearl (URL ở mục 1) và tổng hợp giờ ở mục 1.
- **(2) Đặc điểm khóa:** sạp dựng trên lòng đường Nguyễn Thị Minh Khai thành 2 dãy đối diện, bạt sọc xanh dương–trắng/xanh lá–trắng, ô tối cho sạp ăn, không mái cứng; mỗi sạp 1–2 bóng trắng trên sào 2–2,5m tạo hàng trăm điểm sáng; đồ len treo thành tường vải nhiều màu, mẹt tròn theo màu, khói bếp + sương tạo bloom; đông nhất ở trục thang + đường, không phải trong nhà lồng.
- **Giờ khóa:** mở từ chập tối ~17–19h tới 2–3h sáng, đông nhất 19:30–22:00 (Vinpearl: sôi động ~19h đến 2–3h sáng). Game mặc định đêm ~19:15 (V4.2) khớp khung đông này.
- **(3) Đối chiếu model hiện tại:** đúng hướng — sạp bạt sọc, đèn từng sạp, ghế nhựa xanh dương, vỉ nướng + khói; lệch mật độ trong khung từng bị thưa (research/17 điểm 10) dù tổng NPC toàn map lớn.
- **(4) Đã sửa trong BLENDER-DEEP-2:** trục sạp 2 bên đường vào nới ra (xem mục 7) giúp lối giữa 2 dãy thoáng đúng ảnh 06/43 — đông nhưng không chật.
- **(5) Chưa đủ tư liệu:** không thiếu ở mức bố cục; giá/biển từng sạp ngoài trời vốn là giấy viết tay (ảnh 15) — không có biển cố định để sao chép.

## 3. Rạp Hòa Bình (Rạp 3 Tháng 4)

- **(1) Tư liệu đã có:** ảnh 24–25 (tiền thân chợ cũ 1937: mặt tiền bậc thang/stepped, ô tròn, tháp cao sọc dọc), ảnh 26 (khu Hòa Bình + tháp sao — không phải cận rạp); web: VnExpress https://vnexpress.net/rap-hoa-binh-ky-uc-giua-long-da-lat-5127901.html ; Thanh Niên https://thanhnien.vn/da-lat-chuyen-khu-hoa-binh-tu-cho-cay-xua-den-rap-hoa-binh-nay-185839710.htm
- **(2) Đặc điểm khóa:** tiền thân là Chợ Cây (1929, cháy 1931) → chợ gạch đá 1937 do Sidec thi công, phong cách tiền tân kỳ/Art Deco; trụ tháp hình chữ nhật giật cấp hướng ra quảng trường là điểm nhấn; mặt tiền từng có phù điêu đôi nam nữ người dân tộc săn hổ + khẩu hiệu Latin "DALAT: Dat Aliis Laetitiam Aliis Temperiem"; sau 1960 chợ cũ cải tạo thành rạp 800 ghế, giữ nguyên kiến trúc, mái mặt tiền kéo phẳng, lược gờ dọc tháp.
- **(3) Đối chiếu model hiện tại:** `theater.glb` ở (-19, 17, -56) có tháp đồng hồ (mặt + kim + vòng vàng), ô tròn (oculus), mái ngói, biển canvas "RẠP HÒA BÌNH / Rạp 3 Tháng 4 — xây 1937" + dòng Latin — đúng tinh thần tháp + ô tròn + Latin; lệch: tháp trong game là tháp đồng hồ, tháp thật là trụ chữ nhật giật cấp (đồng hồ là chi tiết ảnh 25 của chợ cũ, cần phân biệt khi sửa sâu).
- **(4) Đã sửa trong BLENDER-DEEP-2:** không sửa rạp; BLENDER-DEEP-1 chỉ kiểm `theater.glb` đạt (khối cân đối, không lỗi mesh).
- **(5) Chưa đủ tư liệu:** chưa đủ tư liệu — bộ real-market không có ảnh chụp rõ mặt tiền rạp hiện nay (research/11 mục 10 ghi rõ); màu sơn, biển hiệu, ô cửa hiện trạng không khẳng định.

## 4. Vòng xoay + tượng đài trước chợ

- **(1) Tư liệu đã có:** ảnh 01, 04, 05, 10, 27–28, 32, 39, 44.
- **(2) Đặc điểm khóa:** vòng tròn lớn ngay trước mặt tiền; tâm là tượng đài đá xám: bệ cao + cụm điêu khắc nhiều nhân vật; quanh tượng thảm cỏ + ô hoa họa tiết hình quạt/tia (vàng/đỏ xen xanh, đọc rõ từ trên cao ảnh 04/39); vành ngoài là đường xe chạy vòng, vỉa hè lát đá + ghế đá trắng; đêm người tràn xuống lòng đường, đảo thành không gian đi bộ/chụp ảnh, tượng được rọi sáng trắng từ dưới (ảnh 32).
- **(3) Đối chiếu model hiện tại:** đảo ở tâm (-30, -6), tượng ở (-34.2, -2.8), đĩa Ø ~21u (r 10.5, chân r 11.0 đo ở BLENDER-DEEP-1), thảm 8 quạt hoa/cỏ + ghế vành — đúng bố cục; lệch so với thật: đảo thật Ø ước 35–40m và tượng nhóm cao ~8–10m (research/17 điểm 6), trong game cụm tượng tổng ~9.6 nhưng đĩa nhỏ hơn tỉ lệ thật, hoa từng là chấm thưa (đã sửa V4.1 thành quạt đặc).
- **(4) Đã sửa trong BLENDER-DEEP-2:** KHÔNG dời đảo/tượng thêm (GEOMETRY-2 vừa dời -6 đồng bộ làn xe/AW/harness, dời nữa phá harness); thay bằng tách bạch thị giác: vạch zebra ở x -13.5, hàng 5 chậu cẩm tú cầu x -13 (z -14..10), sân đổi tông sáng hơn + viền sẫm mép tây, biển "BẬC TAM CẤP ->".
- **(5) Chưa đủ tư liệu:** vạch kẻ đường/biển báo quanh vòng xoay — ảnh không chụp rõ (research/11 mục 10), không tự bịa.

## 5. Bậc tam cấp + cầu nổi (cầu bộ hành vào tầng 2)

- **(1) Tư liệu đã có:** ảnh 02, 03, 08–13, 27, 29, 42; research/21 (KTS Ngô Viết Thụ thiết kế cầu + thang); Wikipedia (mục 1, Ngô Viết Thụ bổ sung cầu nổi bê tông).
- **(2) Đặc điểm khóa:** thang rất rộng (~15–20m), bậc thấp lát đá xám–nâu, nhiều chuyến + chiếu nghỉ, là điểm nhấn kiến trúc của khu (không phải lối phụ); đêm thành "khán đài ăn" — ghế nhựa nhỏ đặt ngay trên bậc, người ngồi đối diện nhau, hàng nướng bám bậc/chiếu nghỉ; đầu thang có biển thương xá (La Tulipe) + cột đèn xanh lá chùm bóng cầu trắng; cầu nổi nối khu Hòa Bình → tầng 2 (có nguồn ghi tầng 3) chợ; thang phụ sơn cầu vồng mosaic + lồng đèn sao ("góc Hong Kong", ảnh 11).
- **(3) Đối chiếu model hiện tại:** thang rộng 22u, 3 chuyến, cao 17, 30 hộp bậc thật + 2 chiếu nghỉ (đo BLENDER-DEEP-1), sitters ngồi ăn trên bậc, 4 điểm bán trên thang, cầu `bridge.glb` ở (17.5, 14.65, -10.5) + 2 trụ pier, biển "CẦU NỔI — VÀO TẦNG 2"; lệch trước đây: cầu từng cắt ngang khung nhìn chính (research/17 điểm 9) và lỗi xoay cầu gây "đi trên trời" (đã sửa V4.3).
- **(4) Đã sửa trong BLENDER-DEEP-2:** không sửa thang/cầu đợt này; sửa nền ở BLENDER-DEEP-1: hạ khối Landing1 11.33→11.31, Landing2 5.67→5.65 để hết 2 mặt chiếu nghỉ đồng phẳng gây z-fight (tấm lót giữ nguyên, mặt đi vẫn đúng 11.33/5.67).
- **(5) Chưa đủ tư liệu:** không thiếu ở bố cục; chi tiết lan can/mặt bậc từng nấc ngoài phạm vi lưới render tối thiểu đã được xác minh bằng model thật ở BLENDER-DEEP-1.

## 6. Đài phun nước vòng xoay

- **(1) Tư liệu đã có:** ảnh 44 (toàn cảnh vòng xoay), 39 (bùng binh chạng vạng); research/21 mục 1+5; quy hoạch 1/500 khu Hòa Bình: Thanh Niên https://thanhnien.vn/rap-hoa-binh-da-lat-se-bi-pha-bo-thay-bang-khu-phuc-hop-da-nang-185833763.htm
- **(2) Đặc điểm khóa:** đài phun thật nằm ở vòng xoay Nguyễn Văn Cừ / Lê Đại Hành / Trần Quốc Toản gần cầu Ông Đạo, phía hồ Xuân Hương — là ĐẦU DƯỚI của trục quy hoạch đài phun → chợ → Dinh tỉnh trưởng; trong ảnh toàn cảnh chỉ đọc được như mốc vòng xoay có nước/hoa ở đầu trục, không phải đài phun trước mặt tiền chợ.
- **(3) Đối chiếu model hiện tại:** game KHÔNG đặt đài phun ở vòng xoay cầu Ông Đạo; theo bố cục Chung Hy chốt (research/21 mục 5), đài phun là neo sáng tạo trong game ở sân trước phía đông bậc tam cấp (27, 5.2), dưới chân cầu nổi, đối diện dãy quần áo mé đông (x ~36.5) — phải ghi rõ đây là vị trí trong game, không phải vị trí thật.
- **(4) Đã sửa trong BLENDER-DEEP-2:** nâng tổng cao ~2.8 → ~4.2: cột giữa 1.5→2.3 (bát chính y 2.62, miệng r 0.95), thêm bát tầng 2 (y 3.15) + chóp cầu, tia nghiêng dài 1.15→1.5 ở y 2.95 (đầu tia r ~0.84 < bồn r 2.45), thêm tia đứng giữa 1.2; bồn/đế giữ nguyên.
- **(5) Chưa đủ tư liệu:** chưa đủ tư liệu — không có ảnh cận đài phun thật (kiểu cột, số tầng bát, vật liệu) trong real-market; mọi chi tiết hình dáng đài phun trong game là dựng tự do, không phải bản sao.

## 7. Phố Nguyễn Thị Minh Khai

- **(1) Tư liệu đã có:** ảnh 06, 07, 40, 43 (dọc trục ngày/đêm); research/17 (nguồn tinbds: đường dài ~400m, lòng đường 10m, vỉa hè 3m mỗi bên — tổng mặt cắt ~16m); research/21 mục 2.
- **(2) Đặc điểm khóa:** trục thẳng từ bùng binh chợ chạy dọc chợ, điểm nhìn cuối là mặt tiền/tượng; nhà phố 3–5 tầng (có đoạn 4–6 tầng) LIÊN TỤC, đứng sát vỉa hè, biển hiệu nhỏ, ban công; ngày sạp chiếm lòng đường với bạt sọc xanh, đêm sạp tràn vỉa hè + một phần lòng đường, mái bạt, đèn từng sạp; lòng đường nhựa sẫm, vỉa hè sáng hơn nhựa nhưng sẫm hơn sân chợ; xe máy đậu dọc 2 lề.
- **(3) Đối chiếu model hiện tại:** trước GEOMETRY-2 nhà chỉ ~2 tầng, lùi 6–8u khỏi mép đường với dải đất trống — đường 18u vẫn đọc như đường nội bộ đất trống (research/17 điểm 8); sau các đợt sửa trục đã dài ~96u→ kéo tới bùng binh đầu chợ (-196), sạp liên tục 2 bên.
- **(4) Đã sửa trong BLENDER-DEEP-2:** mở rộng ĐỀU toàn trục: khoảng trống giữa 2 hàng sạp 37.5u → 45.5u (+21%) dọc trục bùng binh (-196) tới mặt tiền; hàng bắc z -15.7→-19.7, hàng nam z 26→30; nhựa 41→49u (z -17.5..31.5); nhà phố 2 bên lùi về z -28.5 (bắc) / +35.5 (nam); thêm biển tên đường "Đ. NGUYỄN THỊ MINH KHAI" tại (-160, -17.6) và (-70, 27.2), hàng thông + chậu cẩm tú cầu dọc đường vào.
- **(5) Chưa đủ tư liệu:** không thiếu ở mặt cắt/bố cục; biển hiệu từng nhà phố thật thay đổi theo thời điểm — game dùng biển canvas chung, không sao chép từng nhà.

## 8. Phố Tăng Bạt Hổ

- **(1) Tư liệu đã có:** ảnh 41 (góc Hoa Sữa trên phố này); research/21 mục 4; biển tên đường trong game đặt ở cổng trục vào.
- **(2) Đặc điểm khóa:** phố nhỏ ngay sát phía tây chợ, ở đầu trục đường vào; nổi tiếng bởi cụm quán vỉa hè sữa đậu nành (xem mục 9) và hàng ăn nhỏ (bánh căn ở số 14 theo Vinpearl đặc sản); mặt phố hẹp, đời sống vỉa hè là đặc trưng chính, không phải kiến trúc nhà cao tầng.
- **(3) Đối chiếu model hiện tại:** trong game Tăng Bạt Hổ được neo bằng biển "ĐƯỜNG TĂNG BẠT HỔ" ở góc quán Hoa Sữa + cổng chào đầu trục và sạp Hoa Sữa ở đầu tây trục kéo dài — đúng vai "phố nhỏ sát chợ"; chưa dựng thành tuyến phố riêng có 2 dãy nhà liên tục như Nguyễn Thị Minh Khai.
- **(4) Đã sửa trong BLENDER-DEEP-2:** không sửa riêng tuyến phố này; biển Tăng Bạt Hổ có sẵn từ V5.5 được giữ khi trục đường vào mở rộng, biển Nguyễn Thị Minh Khai được bổ sung thêm đợt này (mục 7).
- **(5) Chưa đủ tư liệu:** chưa đủ tư liệu — ngoài ảnh 41 ở góc Hoa Sữa, bộ real-market không có ảnh toàn tuyến Tăng Bạt Hổ (mặt tiền từng nhà, chiều rộng lòng đường) nên không dựng chi tiết từng nhà.

## 9. Quán Sữa đậu nành Hoa Sữa — 64 Tăng Bạt Hổ

- **(1) Tư liệu đã có:** ảnh 41 (nồi sữa Hoa Sữa), 38 (ly thủy tinh sữa nóng trên bàn), 35 (khách cầm ly giấy); web: LaTour https://latour.vn/tin-tuc/kham-pha-top-3-sua-dau-nanh-da-lat-ngon-nuc-tieng-nhat-2026-1586.html (64 Tăng Bạt Hổ, cách chợ ~50m, 40+ năm, 16:00–22:00, giá 7.000–15.000đ/ly).
- **(2) Đặc điểm khóa:** quán VỈA HÈ đúng nghĩa, không mặt tiền cửa hàng: một nồi nấu sữa siêu to bốc hơi là trung tâm, tủ kính bánh ngọt (bánh tiêu, bánh sừng trâu/con sò), vài bộ bàn ghế nhựa thấp xếp dọc vỉa hè, ly thủy tinh đựng sữa nóng; bán nhiều loại sữa (đậu nành, đậu xanh, đậu phộng, mè, bắp); đông nhất ~21h.
- **(3) Đối chiếu model hiện tại:** game đặt landmark "SỮA ĐẬU NÀNH HOA SỮA — GÓC TĂNG BẠT HỔ" tại đầu tây trục đường vào kéo dài, cạnh cổng chào: sạp mua được (khu đồ uống) + cụm bàn ghế thấp + nồi lớn bốc khói + khách ngồi đêm + hàng chờ 4 người (dir side) — khớp dạng vỉa hè + nồi + ghế thấp.
- **(4) Đã sửa trong BLENDER-DEEP-2:** không sửa riêng quán; vị trí giữ nguyên khi trục nới rộng, hàng sạp mới chừa khe cho sạp Hoa Sữa (GEOMETRY-2).
- **(5) Chưa đủ tư liệu:** không thiếu ở dạng quán; biển hiệu/màu tủ kính chính xác của quán thật — chưa đủ tư liệu từ ảnh 41 (chỉ thấy nồi) nên biển trong game là chữ canvas chung, không khẳng định giống biển thật.

## 10. Jollibee

- **(1) Tư liệu đã có:** KHÔNG có ảnh trong real-market; nhận diện chung Jollibee Việt Nam (mặt tiền đỏ/vàng, mascot ong, chữ quảng cáo tiếng Việt) + vị trí gợi mốc theo research/21; địa chỉ chi nhánh Đà Lạt được các danh sách ghi ở 49 Đinh Tiên Hoàng (không phải góc chợ) — xem toplist.vn qua tìm kiếm web 09/11/2026.
- **(2) Đặc điểm khóa (nhận diện phổ biến, không phải chi nhánh riêng):** nền/biển đỏ `#C8102E`, dải vàng `#FFC72C`, chữ "JOLLIBEE" trắng, mascot ong đỏ (thân đỏ, đầu vàng, cánh trắng), mái hiên sọc đỏ/trắng, cửa kính lớn, bảng menu đứng với chữ tiếng Việt kiểu "GÀ RÁN GIÒN • KHOAI TÂY CHIÊN", "COMBO GÀ GIÒN 39K".
- **(3) Đối chiếu model hiện tại:** trước BLENDER-DEEP-2 chỉ là shophouse gợi mốc "JOLLIBEE — GÀ RÁN" (GEOMETRY-2 ghi rõ không khẳng định bản sao); nay dựng ở (-183, -20) cạnh bùng binh đầu chợ (-196) — vị trí trong game để tạo mốc góc phố, không phải địa chỉ thật của chi nhánh.
- **(4) Đã sửa trong BLENDER-DEEP-2:** dựng THẬT bằng code geometry + biển canvas (`brandShop`, không GLB mới): khối 2 tầng 9.6×6.4×6.0 tường đỏ, dải vàng ngang, kính mặt tiền, hiên sọc đỏ/trắng, mascot ong trên mái, bảng combo + 2 bàn ngoài trời.
- **(5) Chưa đủ tư liệu:** chưa đủ tư liệu — ảnh mặt tiền RIÊNG của chi nhánh Jollibee Đà Lạt không có trong real-market; mọi chi tiết riêng chi nhánh (kích thước biển, bố cục kính, số tầng thật) không khẳng định, chỉ dựng theo nhận diện thương hiệu phổ biến.

## 11. L'angfarm — số 6 Nguyễn Thị Minh Khai

- **(1) Tư liệu đã có:** KHÔNG có ảnh mặt tiền riêng trong real-market; web xác nhận địa chỉ + loại hình: dalat.net.vn https://dalat.net.vn/bai-viet/nhung-dia-diem-mua-dac-san-da-lat-khi-di-du-lich-159 (số 6 Nguyễn Thị Minh Khai, 08:00–22:00, trà atiso/mứt/trái cây sấy); LAV https://lav.vn/langfarm-cho-dem-nguyen-thi-minh-khai-tp-da-lat (2 tầng, Store & Buffet, 300m², hoàn thành 12/2018, tầng trệt trưng bày atiso/mứt/trà/trái cây sấy).
- **(2) Đặc điểm khóa (theo brief + nhận diện chuỗi):** cửa hàng đặc sản 2 tầng tại số 6 Nguyễn Thị Minh Khai, mặt tiền gỗ ấm, biển "L'ANGFARM" / "ĐẶC SẢN ĐÀ LẠT" / "L'ANGFARM STORE", cửa kính lớn nhìn vào trong, kệ hộp quà + lọ đặc sản (mứt, trà, trái cây sấy, hoa khô), viền đèn quanh mặt tiền; ảnh 10/27 cho thấy một quán kính sáng đèn ngay đầu thang có vai trò mốc tương tự (được đối chiếu như LangFarm ở research/17).
- **(3) Đối chiếu model hiện tại:** trước BLENDER-DEEP-2 chỉ là shophouse gợi mốc kem/xanh thông "L'ANGFARM — ĐẶC SẢN ĐÀ LẠT"; vị trí trong game (-183, 31.5) ở góc bùng binh đầu chợ là neo bố cục của game, khác địa chỉ thật số 6 (sát chợ/đầu thang) — cần ghi rõ khi thuyết minh.
- **(4) Đã sửa trong BLENDER-DEEP-2:** dựng THẬT bằng `brandShop`: tường kem `#EFE3C2`, biển chính nền xanh lá `#2E5B2E` chữ trắng "L'ANGFARM" + phụ "ĐẶC SẢN ĐÀ LẠT • TRÀ • MỨT • HOA KHÔ", biển phụ "L'ANGFARM STORE", hiên xanh lá, kính mặt tiền, kệ gỗ 2 tầng trước cửa với 6 lọ mứt đủ màu + 5 hộp trà/quà, giỏ cẩm tú cầu 2 góc.
- **(5) Chưa đủ tư liệu:** chưa đủ tư liệu — ảnh mặt tiền RIÊNG của chi nhánh số 6 không có trong real-market; chi tiết gỗ ấm/viền đèn/bố cục kính riêng của chi nhánh này không khẳng định, model hiện dùng tông kem/xanh lá + kệ đặc sản theo nhận diện phổ biến.

## 12. Dãy khách sạn quanh khu Hòa Bình

- **(1) Tư liệu đã có:** ảnh 01 (khách sạn ~6 tầng sát góc phố phải khung), 05 (neon khách sạn sau bùng binh), 26 (khu Hòa Bình), 27 (Thanh Bình Hotel + khách sạn trắng cao đối diện đảo), 37, 39; chữ đọc được trong ảnh: "DALAT CENTER", "HOTEL COLLINE", "Thanh Bình Hotel".
- **(2) Đặc điểm khóa:** tạo thành "bức tường đô thị" 5–8 tầng khép kín quanh quảng trường/đảo: khối trắng/kem, cửa sổ đều nhịp (khách sạn trắng đối diện có cửa vòm), biển tên nóc/viền neon sáng đêm (vàng/xanh) làm nền trời; ô tô đỗ thành hàng dọc quảng trường (ảnh 26); thiếu dãy này là không gian "rò" ra phông trống (research/17 điểm 7).
- **(3) Đối chiếu model hiện tại:** `hotels.glb` có 4 biến thể 4–6 tầng (trắng/kem, cửa sổ lõm/nổi có khung, ban công, gờ chỉ từng tầng, mái đua + bể nước nóc), biển nóc chữ nổi phát sáng đêm DALAT CENTER (vàng) / HOTEL COLLINE (trắng) / VIB (trắng) / THANH BÌNH (xanh), cửa sổ sáng vàng rải rác đêm; bố trí dãy sau đồi + 2 bên đông/tây + 2 phía nam sau chợ — đúng vai phông khép kín.
- **(4) Đã sửa trong BLENDER-DEEP-2:** không sửa khách sạn; BLENDER-DEEP-1 kiểm `hotels.glb` đạt (4 group, biển nóc 4 kiểu; biến thể mái MetalDark là thiết kế, không phải lỗi đen mặt).
- **(5) Chưa đủ tư liệu:** chưa đủ tư liệu — không có ảnh cận mặt tiền RIÊNG từng khách sạn (Thanh Bình, Colline, Dalat Center) trong real-market; số tầng/biển/cửa vòm chi tiết từng tòa không khẳng định, model là biến thể chung quanh chợ.

## 13. Quán cà phê quanh chợ

- **(1) Tư liệu đã có:** ảnh 02 (ghế nhựa cam trước cửa trên), 08 (quán/biển quanh đầu thang), 17 (lồng đèn đỏ trong khu cải tạo — không phải cà phê riêng); model `cafe.glb`/`shop.glb` + biển canvas trong game (research/21 không có hồ sơ cà phê riêng).
- **(2) Đặc điểm khóa (mức khu vực, không phải từng quán):** quán nhỏ mặt đường 2 tầng, mặt tiền có lớp: cửa lõm, hiên/bạt che, biển chữ, ban công nhỏ; vỉa hè đặt bàn ghế thấp cho khách ngồi quay ra phố/chợ; trên đồi có dạng cà phê sân hiên (sàn gỗ, quầy pha chế, bàn nhìn xuống chợ); đêm cửa kính sáng ấm là điểm sáng phụ quanh chợ, không lấn lớp điểm sáng từng sạp.
- **(3) Đối chiếu model hiện tại:** `shop.glb` (nhà 2 tầng mặt tiền lớp) đặt 3 quán: cạnh bùng binh phía tây, chân bậc thang phía đông, đường đông trước chợ — có biển canvas từng quán + bàn ghế vỉa hè + khách ngồi; thêm 2 quán cà phê sân hiên ở mép đồi z -32.5 tại (-17) và (17.5) (V4.5) + `cafe.glb` ở (13, 17, -60) trên đồi; tương tác ngồi quán cho buff tỉnh táo (cafe sit).
- **(4) Đã sửa trong BLENDER-DEEP-2:** không sửa quán cà phê; BLENDER-DEEP-1 kiểm `cafe.glb`/`shop.glb` đạt (biển lớn + hiên + bàn ghế góc; ban công + lan can).
- **(5) Chưa đủ tư liệu:** chưa đủ tư liệu — bộ real-market không có ảnh riêng từng quán cà phê quanh chợ (tên, mặt tiền, màu biển từng quán); tên/biển trong game là canvas sáng tạo theo phong cách khu vực, không phải bản sao quán thật.
