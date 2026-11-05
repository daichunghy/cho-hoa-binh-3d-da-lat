# 06 — Chợ ảo / trung tâm mua sắm ảo 3D & game có khu chợ đông hàng quán

> Mục đích: rút cơ chế **bố trí hàng quán** và **mua sắm trong thế giới ảo** (bố cục gian hàng, NPC bán hàng, giỏ hàng / trả tiền, mua đồ ăn–nước uống) để áp dụng cho **Chợ Hòa Bình 3D — Đà Lạt**: một khu chợ 3D cho người ta đi tham quan, dạo chơi thấy thú vị, có hàng quán và có chế độ mua đồ ăn, nước uống.
> Phạm vi: chỉ nghiên cứu, chưa thiết kế/không code. Ngày nghiên cứu: 05/11/2026.

---

## 1. Bản đồ ví dụ đã khảo sát

| # | Ví dụ | Loại | Điểm đáng học nhất |
|---|-------|------|--------------------|
| 1 | **Alibaba Buy+** | Mall 3D/VR của sàn TMĐT | Đi dạo trong mall 3D, tương tác sản phẩm và **mua ngay không rời thế giới ảo**; VR chỉ là lớp phủ, lõi là "khám phá → mua liền mạch" |
| 2 | **Nike Virtual Store / IKEA / Sephora / Lowe's Holoroom** | Cửa hàng 3D của thương hiệu | Mỗi cửa hàng có **1 tương tác "thử" đặc trưng**: thử giày AR, đặt nội thất vào phòng, thử son AR, tự phối phòng. Bài học: gian hàng phải cho *sờ/thử*, không chỉ cho nhìn |
| 3 | **Bildyard — Nike 3D Virtual Store (three.js trên trình duyệt)** | Store 3D chạy web | Kiến trúc thực dụng: cảnh 3D thật (phòng, kệ, ánh sáng, bóng đổ) + **UI 2D phủ lên trên** (thẻ sản phẩm, ngăn giỏ hàng/cart drawer, thanh chọn khu vực). Sản phẩm là ảnh studio nhiều góc "diễn" như vật 3D. Sản phẩm bay vào giỏ khi chọn size — hiệu ứng nhỏ nhưng tạo cảm giác mua thật |
| 4 | **vrMall / vrFairs (VR360, Việt Nam)** | Hội chợ ảo, >100 gian hàng mẫu | Mô hình B2B gần nhất với Việt Nam: **sảnh hội chợ** làm nơi tập hợp/điều hướng tất cả gian hàng; mỗi gian tùy biến logo–màu–banner; sản phẩm cho xem, yêu thích, **đưa vào giỏ, đặt mua hoặc bấm sang sàn TMĐT** để thanh toán; tích hợp chat Zalo/Messenger với người bán thật |
| 5 | **Decentraland** (Fashion District, Vegas City, Dragon City…) | Thế giới xã hội 3D mở | Tổ chức theo **district (khu chuyên đề)**: mỗi khu một bản sắc (thời trang, casino, châu Á…). Giá trị nằm ở *vị trí + lưu lượng người qua lại (foot traffic)*: gian ở trục chính đắt/thu hút hơn gian trong hẻm. Có Genesis Plaza làm điểm xuất phát + cổng teleport tới sự kiện/gian hàng |
| 6 | **Second Life** | Thế giới xã hội lâu đời | Hai kênh bán song song: **đi dạo mua trong thế giới** (trải nghiệm) + **Marketplace web** (tìm nhanh, so giá). Tiền ảo riêng (Linden Dollar) có giá niêm yết rõ trên từng món |
| 7 | **Roblox — El Tianguis (chợ đường phố Mỹ Latin)** | Game chợ trong Roblox, ~14,2 triệu lượt ghé, server 50 người | Công thức chợ game thành công nhất để học: chợ chia thành **gian theo chủ đề cố định** — quần áo, tranh, đồ uống có hương vị, rau củ, đồ ăn, đồ chơi. Người chơi *thuê/nhận một gian, tự trang trí gian của mình* và bán cho người chơi khác. Chợ = nơi roleplay + khoe sáng tạo, không chỉ là menu mua hàng |
| 8 | **Roblox — Adopt Me! / Bloxburg / Work at a Pizza Place** | Game roleplay xã hội | (a) Quầy đồ ăn/nước uống đặt ở **điểm giao thông đông** trở thành máy kiếm tiền thụ động cho chủ quầy; (b) đồ ăn mua ở cửa hàng tạp hoá *giữ được trong túi đồ* và dùng ở mọi nơi, khác đồ "dùng tại chỗ" — phân biệt rõ 2 loại hàng tiêu hao; (c) việc làm tại quán ăn (nhận đơn → làm → giao) biến hàng quán thành gameplay, không chỉ là điểm bán |
| 9 | **Minecraft — server economy / chest shop / PhysicShop / ProsperitySMP** | Chợ do người chơi dựng trong game | Cơ chế "rương + biển hiệu = cửa hàng": đặt rương, gắn biển ghi giá, người khác đi ngang bấm vào biển là mua, **không cần chủ gian online**. Server tổ chức hẳn **khu chợ (market district/plaza)** riêng: gian được *thuê theo tuần* (rẻ, cho người mới) hoặc mua đứt lô đất; luôn có **server shop làm "chốt chặn giá"** mua lại đồ phổ thông để không món nào vô giá trị. Có thêm chợ xoay vòng (rotating market) giảm giá 10–40% theo giờ/ngày để tạo lý do quay lại |
| 10 | **Stardew Valley — lễ hội & Stardew Valley Fair** | Game nông trại/lễ hội | Lễ hội biến quảng trường thành chợ phiên: nhiều booth mini-game + **một quầy đổi quà trung tâm**. Người chơi chơi game kiếm *Star Token* (tiền riêng của lễ hội) rồi đổi đồ độc quyền tại quầy — mỗi món chỉ mua được 1 lần/sự kiện, tạo khan hiếm. Gian hàng ăn (Gus's Burger Booth) nằm lẫn với booth game, không tách khu |
| 11 | **Palengkero (Philippines, nghiên cứu ACM 2026)** | Game mô phỏng chợ truyền thống (palengke) | Chợ ướt được mô hình hoá đúng chất chợ thật: **trả giá (haggling)** — trả giá hỏng thì gian đó tạm "khóa", phải đổi chiến thuật; **NPC khách khác tranh mua** hàng ngon/rẻ có hạn, chậm chân là hết; giá biến động. Đây là 3 cơ chế làm chợ ảo "có đời sống" thay vì bảng giá chết |
| 12 | **Patchwork Pastry (indie, devlog)** | Game có chợ 3 gian | Chi tiết đắt giá về NPC: đến giờ chợ, người bán **tự đi ra gian và bày từng món lên quầy bằng tay** (0,3–0,8 giây/món, xoay lệch nhẹ cho tự nhiên) thay vì hàng hiện ra tức thì. NPC khách cũng mua dần trong ngày → muốn mua đủ đồ phải đến lúc gian vừa bày xong. Chợ có *nhịp thời gian* |
| 13 | **Ashes of Creation — Marketplace / Player Stalls** | MMORPG | Gian hàng người chơi (stall/kiosk) thuê theo thời gian tại khu chợ của khu dân cư; hàng được **niêm yết qua một NPC quản lý chợ**, người mua tương tác với NPC để xem từng "cửa hàng" và mua — gian bán được ngay cả khi chủ vắng mặt |

---

## 2. Cách bố trí gian hàng — các kiểu layout đã kiểm chứng

Nghiên cứu layout bán lẻ (áp vào cả 3D) phân biệt 3 kiểu cổ điển, và thực tế các thế giới ảo thành công đều **lai** chúng:

### 2.1. Ba kiểu layout gốc
- **Grid (lưới ô bàn cờ):** dãy gian song song, lối đi thẳng — dễ tìm, dễ mở rộng, hợp khu hàng khô/đặc sản đóng gói. Nhược: đơn điệu, đi một vòng là chán.
- **Freeform (tự do):** gian đặt lệch, uốn lượn, mỗi góc một bất ngờ — hợp khu khám phá, quà lưu niệm, check-in. Nhược: dễ lạc, khó quay lại đúng gian.
- **Racetrack / Loop (vòng đua):** một vòng đi khép kín bắt buộc ngang qua mọi khu — hợp nhất cho *tham quan*: người chơi không bỏ sót khu nào, và kết thúc đúng điểm bắt đầu.

### 2.2. Công thức bố cục rút ra cho một khu chợ ảo
1. **Một landmark trung tâm + một vòng loop quanh nó.** Decentraland có plaza trung tâm, chợ thật có nhà lồng/vòng xoay. Loop đảm bảo mọi gian đều có foot traffic, gian "mặt tiền vòng chính" là vị trí vàng.
2. **Chia district theo chủ đề, mỗi district một màu/mùi/âm thanh riêng** (El Tianguis, Decentraland): người chơi định vị bằng trí nhớ không gian ("khu đồ len ở phía cầu thang") thay vì mở bản đồ.
3. **Sảnh/cổng chào làm hub điều hướng** (vrMall): điểm xuất phát có bản đồ, danh sách gian, nút nhảy nhanh (teleport) tới từng khu — bắt buộc khi chợ lớn hơn ~20 gian.
4. **Hai lớp gian hàng:** (a) gian *cố định của hệ thống* (NPC bán, luôn mở, dạy người chơi cách mua) và (b) gian *cho thuê/sự kiện* (pop-up, đổi theo tuần/mùa) tạo nội dung mới liên tục — như stall thuê theo tuần của Minecraft và pop-up shop của Decentraland.
5. **Gian "neo" (anchor) ở các đầu vòng:** đặt 2–3 điểm hút mạnh (quán ăn nổi tiếng nhất, sân khấu nhạc, điểm check-in) ở xa nhau để kéo dòng người đi hết vòng, giống mall đặt siêu thị/rap phim ở hai đầu.
6. **Lối đi phụ & ngõ tắt:** vài ngõ nhỏ chứa gian "bí mật" (món hiếm, giá hời, NPC kể chuyện) — phần thưởng cho người khám phá, thứ khiến chợ ảo hơn hẳn trang TMĐT phẳng.
7. **Không gian trống có chủ đích:** xen giữa các dãy gian là ô nghỉ (ghế, bồn hoa, điểm ngắm cảnh) — nơi người chơi dừng ăn/uống món vừa mua và chụp ảnh; đây cũng là nơi đặt quầy đồ uống lưu động kiểu Adopt Me!.

---

## 3. NPC bán hàng — cách làm cho gian hàng "sống"

Từ Patchwork Pastry, Palengkero, Stardew Valley và các game roleplay, NPC bán hàng hiệu quả có 5 lớp:

1. **Có danh tính, không phải máy bán hàng đội lốt người:** tên riêng, mặt/ trang phục nhận diện theo gian, 2–3 câu thoại đặc trưng (giọng địa phương), câu chào thay đổi theo giờ (sáng/chiều/đêm) và theo thời tiết.
2. **Có hành động lao động:** bày hàng từng món khi mở gian, cân/đóng gói khi có người mua, dọn gian khi hết giờ. Hành động lặp nhỏ (animation loop: nướng, khuấy nồi sữa, đan len) là tín hiệu "gian đang mở" từ xa mà không cần UI.
3. **Có tồn kho thật và hết hàng thật:** mỗi gian số lượng hữu hạn, NPC khách khác cũng mua dần; hết món "hot" thì treo biển "hết — mai ghé lại". Khan hiếm tạo lý do quay lại đúng giờ (đến sớm lúc gian vừa bày).
4. **Có quan hệ/giá linh hoạt:** trả giá mini-game (Palengkero: trả giá hỏng bị khóa gian tạm thời — nên làm nhẹ hơn: hỏng thì NPC phàn nàn vui, mất lượt giảm giá), khách quen mua nhiều được giảm, giá thay đổi nhẹ theo khung giờ đông/vắng.
5. **NPC là người dẫn chuyện của khu chợ:** mỗi người bán giữ 1 mẩu thông tin (gian nào đang giảm giá, món ẩn ở ngõ nào, sự kiện tối nay mấy giờ) — biến việc đi chợ thành đi "hóng chuyện", đúng chất chợ truyền thống Việt Nam.

**Chống mẫu cần tránh:** NPC đứng yên + bấm vào là mở một bảng grid toàn chữ. Đó là TMĐT đội lốt 3D — mọi ví dụ thành công đều cho *thấy hàng trên quầy trước*, bảng giá chỉ xuất hiện khi đã đến gần/chạm vào món.

---

## 4. Giỏ hàng & trả tiền trong thế giới ảo

### 4.1. Luồng mua chuẩn (tổng hợp Bildyard, vrMall, Alibaba Buy+, Minecraft chest shop)
```
Đến gần gian → món hàng trên quầy phát sáng/nổi thẻ tên+giá
→ Bấm vào MÓN (không bấm vào menu) → thẻ sản phẩm 2D trượt lên:
  ảnh/xoay 360°, mô tả ngắn, biến thể (size/màu/mức cay…), số lượng
→ "Thêm vào giỏ" (món bay vào biểu tượng giỏ — hiệu ứng xác nhận)
→ Giỏ hàng là UI 2D phủ (drawer) dùng chung toàn chợ, mở ở mọi nơi
→ Thanh toán 1 lần cuối buổi dạo, thay vì trả tiền từng gian
→ Nhận hàng: (a) hàng ảo → vào túi đồ avatar ngay
             (b) hàng thật → mã đơn + theo dõi giao hàng ngoài đời
```

### 4.2. Các quyết định thiết kế quan trọng
- **Một giỏ chung cho cả chợ** (vrMall, mall thật): người chơi dạo tự do, gom đồ nhiều gian, trả một lần. Trả tiền từng gian phá nhịp tham quan.
- **Tách bạch 2 loại tiền tệ ngay từ UI:**
  - *Tiền trong thế giới* (xu/điểm kiếm được bằng tham quan, mini-game — kiểu Star Token của Stardew): mua đồ ảo, đồ ăn/nước uống cho avatar, thuê gian sự kiện.
  - *Tiền thật:* chỉ xuất hiện ở bước cuối khi mua đặc sản/lưu niệm giao về nhà, và **đi qua cổng thanh toán/Shopee/ZaloPay quen thuộc** (vrMall chọn cách liên kết sang sàn TMĐT thay vì tự xử lý thanh toán).
- **Mua vắng chủ:** học Minecraft/Second Life/Ashes of Creation — gian vẫn bán khi "chủ" không online nhờ niêm yết qua hệ thống (biển giá trên rương / NPC quản lý chợ). Với chợ do ban tổ chức vận hành thì tương đương: NPC bán thay, đơn thật chuyển về tiểu thương thật xử lý sau.
- **Xác nhận & chống bấm nhầm:** đơn tiền thật luôn có màn hình xác nhận tổng tiền + phí ship trước khi trả; đơn tiền ảo mua ngay 1 chạm nhưng có nút hoàn tác vài giây.
- **Giá phải nhìn thấy từ xa:** biển giá treo trên gian (sign shop) đọc được khi đi ngang — người chơi quyết định ghé hay không từ *không gian*, không phải từ menu tìm kiếm. Kèm theo vẫn có trang danh mục web phẳng (kiểu Second Life Marketplace) cho người muốn mua nhanh không dạo.
- **Khuyến mãi có nhịp thời gian:** chợ xoay vòng giảm giá theo ngày/giờ (Minecraft rotating market), "giờ vàng" buổi tối, món độc quyền sự kiện chỉ bán trong lễ hội — lý do quay lại hằng tuần.

### 4.3. Riêng cho đồ ăn – nước uống (chế độ ăn uống trong chợ)
Đây là mảng khiến chợ ảo khác siêu thị ảo, và Chợ Hòa Bình đã chốt phải có:
- **Đặt món tại quầy → chờ chế biến → nhận món:** NPC làm thật vài giây (nướng bánh tráng trên than, rót sữa đậu nành bốc khói). Thời gian chờ ngắn chính là lúc người chơi ngắm chợ/nghe nhạc — đừng rút thành mua-tức-thì.
- **Ăn là hành động xã hội:** món mua xong phải *cầm trên tay avatar*, mang ra ghế/bậc thang/quảng trường ngồi ăn với animation, hơi nóng bốc lên. Người khác nhìn thấy bạn đang ăn gì = quảng cáo sống cho quầy đó (đúng cơ chế quầy đồ ăn ở điểm đông người của Adopt Me!).
- **Hiệu ứng tiêu hao có ý nghĩa trong thế giới:** ở Đà Lạt trời lạnh — đồ nóng cho "buff ấm" (avatar hết run, tim/điểm thoải mái tăng), đồ uống cho năng lượng đi tiếp. Ăn uống gắn vào vòng tham quan chứ không phải chỉ trừ tiền.
- **Phân loại rõ:** món *ăn tại chỗ* (rẻ, tiền ảo, hiệu ứng ngay) và món *đặc sản mang về* (tiền thật, vào giỏ chung, giao tận nhà) — học cách Adopt Me! tách đồ giữ-trong-túi và đồ dùng-tại-chỗ.

---

## 5. Đối chiếu chợ thật: Chợ Hòa Bình / Chợ đêm Đà Lạt (nguyên liệu bố cục)

- Khu chợ nằm trên đường Nguyễn Thị Minh Khai, khu Hòa Bình; **3 lối vào** rõ rệt: vòng xoay chợ trên đường Nguyễn Thị Minh Khai, lối đi bộ từ quảng trường Hòa Bình, và **bậc thang trung tâm Hòa Bình** xuống chợ — bậc thang này là điểm check-in biểu tượng.
- **Hai nhịp sống:** ban ngày là nhà lồng chợ truyền thống (rau củ, hoa tươi phủ kín lối đi, nông sản, đặc sản — nhịp nhẹ, đi tham quan/mua đặc sản); ban đêm (gian hàng lên đèn ~17–18h, đông nhất 19–22h) biến thành chợ đêm ẩm thực + đồ len + lưu niệm, mùi món nướng lan khắp khu trong trời se lạnh.
- Địa hình **dốc nhiều cao độ**: các tầng/hành lang ở cao độ khác nhau nối bằng cầu thang và cầu nối — đặc trưng kiến trúc hiếm có, rất hợp làm level design 3D nhiều tầng thay vì một mặt phẳng.
- Lộ trình khách thật tự đi: từ khu Hòa Bình nhìn toàn cảnh → xuống khu hàng ăn → sang khu mua sắm → quay lại điểm xuất phát (đúng layout vòng loop ở mục 2.1).
- Mặt hàng neo: bánh tráng nướng, sữa đậu nành nóng, xiên nướng, bắp/khoai nướng (khu ăn); đồ len, áo khoác, đồ second-hand (khu mặc); dâu tây, rau củ, hoa tươi, mứt/đặc sản (khu mang về).

---

## 6. Bài học áp dụng cho Chợ Hòa Bình 3D

### 6.1. Bố cục đề xuất (layout)
1. **Giữ đúng xương sống thật:** quảng trường/bậc thang Hòa Bình (hub xuất phát + điểm check-in + bản đồ) → vòng loop quanh nhà lồng chợ → vòng xoay cuối chợ. Ba lối vào thật làm 3 cổng spawn/teleport.
2. **Vòng racetrack một chiều mềm:** vòng chính đi qua đủ 5 district, có ngõ tắt khám phá; không gian dốc nhiều cao độ của chợ thật là lợi thế — làm cầu thang/cầu nối thành "cầu nối ngắm toàn cảnh" thay vì san phẳng.
3. **5 district theo đúng hàng hoá thật:**
   - *Khu Ẩm Thực Nóng* (bánh tráng nướng, xiên, bắp khoai nướng) — đặt ngay chân bậc thang, mùi/khói/tiếng xèo xèo kéo người vào.
   - *Khu Sữa & Đồ Uống Nóng* (sữa đậu nành, sữa chua phô mai, cà phê) — xen ô nghỉ/ghế ngồi, là "trạm nạp năng lượng" giữa vòng.
   - *Khu Đồ Len & Áo Lạnh* — cho avatar **thử đồ trực tiếp** (học Nike/Sephora: tương tác thử là linh hồn của gian).
   - *Khu Nông Sản & Hoa* (dâu tây, rau củ, hoa tươi) — district của **chế độ ban ngày**.
   - *Khu Đặc Sản Mang Về* (mứt, trà, cà phê, hồng treo gió) — district duy nhất bán **hàng thật bằng tiền thật**, nối giỏ chung → thanh toán ngoài.
4. **Hai trạng thái ngày/đêm cho cùng một bản đồ** (điểm khác biệt lớn nhất, rẻ về chi phí làm map): ngày = chợ nhà lồng nông sản/hoa, nhịp chậm; đêm = lên đèn, mở khu ẩm thực + đồ len, đông NPC, có nhạc. Người chơi có lý do vào 2 lần/ngày.
5. **Gian 2 lớp:** ~15–20 gian NPC cố định (dạy cách mua, giữ chợ sống khi vắng người chơi) + dãy gian pop-up sự kiện cuối tuần/lễ (gian tiểu thương thật đăng ký, gian món theo mùa: hồng giòn mùa thu, mai anh đào mùa xuân).

### 6.2. NPC & hàng quán
- Mỗi gian 1 NPC có tên, giọng thoại miền Trung/Đà Lạt, animation lao động riêng (nướng, rót sữa, xếp len, cắm hoa) và **tự bày hàng lúc mở gian** (học Patchwork Pastry).
- Tồn kho hữu hạn theo buổi chợ; món hot hết thì treo biển hết hàng; NPC khách ảo đi dạo, dừng mua, ngồi ăn — chợ không bao giờ "trống" kể cả 3h sáng.
- Mỗi NPC giữ 1 tin đồn/chỉ đường (quầy nào mới giảm giá, ngõ nào có món ẩn, tối nay mấy giờ lên đèn) — đi chợ = đi khám phá thông tin.
- Cho phép trả giá vui ở vài gian đặc sản (mini-dialogue 1–2 lượt, hỏng thì NPC cười xí xoà, không phạt nặng như Palengkero).

### 6.3. Mua sắm & thanh toán
- **Giỏ chung toàn chợ (UI 2D drawer phủ lên 3D)**, gom cả 5 district, thanh toán 1 lần — theo đúng chuẩn vrMall/Bildyard.
- **2 ví tách bạch trên UI:** Ví Xu (kiếm bằng đi tham quan đủ 5 district, mini-game, check-in bậc thang) → mua đồ ăn/uống tại chỗ, đồ ảo cho avatar; Tiền thật → chỉ cho đặc sản mang về, thanh toán qua liên kết sàn TMĐT/cổng quen thuộc, có màn hình xác nhận tổng + ship.
- **Ăn uống là vòng lặp chính, không phải tính năng phụ:** đặt món → xem NPC chế biến → cầm trên tay → ra bậc thang/quảng trường ngồi ăn, nhận buff "ấm bụng" trong tiết trời lạnh ảo → có sức đi tiếp vòng chợ. Bạn đồng hành nhìn thấy món bạn ăn.
- Biển giá treo đọc được từ lối đi ở mọi gian; kèm trang web phẳng liệt kê đặc sản cho người muốn mua nhanh.
- Nhịp quay lại: món giảm giá xoay theo ngày, "giờ lên đèn" 19h là sự kiện cộng đồng hằng ngày, lễ hội theo mùa (hoa dã quỳ, mai anh đào) mở gian độc quyền giới hạn số lượng kiểu Stardew Valley Fair.

### 6.4. Thứ tự ưu tiên nếu làm MVP
1. Bản đồ loop + bậc thang Hòa Bình + chế độ đêm lên đèn (cái "wow" thị giác).
2. 6–8 gian ẩm thực/đồ uống có NPC chế biến + ăn tại chỗ bằng Ví Xu (cái "vui" để ở lại lâu).
3. Giỏ chung + 1 district đặc sản nối thanh toán thật (cái "ra tiền").
4. Sau đó mới thêm: thử đồ len cho avatar, gian pop-up sự kiện, trả giá, NPC tin đồn.

---

## Nguồn tham khảo chính
- Limina Studios — *5 Examples of 3D Virtual Stores* (Nike, IKEA, Sephora, Alibaba Buy+, Lowe's): liminastudios.com/blog/3d-virtual-stores-virtual-shopping-experience/
- Bildyard — *Build a 3D Virtual Store: The Complete Guide* (three.js, cart drawer, product card UI)
- VR360 — *vrMall / Hội chợ–Cửa hàng thực tế ảo*: vr360.com.vn/cua-hang-thuc-te-ao-vrmall (hơn 100 gian mẫu, giỏ hàng + liên kết sàn TMĐT, sảnh hội chợ)
- Nghiên cứu layout cửa hàng 3D: Krasonikolakis et al. (grid / freeform / racetrack) — dl.ifip.org; Vrechopoulos et al. — *Virtual Store Layout: An Experimental Comparison* (ResearchGate)
- Roblox — *El Tianguis* (gian hàng theo chủ đề, người chơi tự dựng gian): số liệu qua Roblox Game List 2026 (~14,2 triệu visits)
- Minecraft player shops: PhysicShop (SpigotMC), EconomyShop & Market plugins (Modrinth), ProsperitySMP (market district, thuê gian theo tuần, server shop chốt giá)
- Stardew Valley Festivals / Stardew Valley Fair (Star Token, shop booth, mini-game booths): qwiki.gg/stardew-valley/festivals/
- Palengkero — *A 2D Marketplace Simulation Game-Based Learning Tool* (ACM 2026): haggling, NPC cạnh tranh mua, giá biến động — dl.acm.org/doi/10.1145/3805862.3805881
- Patchwork Pastry — DevLog 9 *The Market* (NPC bày hàng bằng tay, nhịp thời gian chợ): stephenrockett.itch.io
- Ashes of Creation Wiki — *Marketplace / Player Stalls* (NPC quản lý chợ, stall thuê theo thời gian)
- Decentraland (districts, foot traffic, Genesis Plaza): tài liệu tổng hợp qua GNcrypto / WWD–MVFW
- Chợ đêm & Chợ Đà Lạt (bố cục thật, lối vào, giờ hoạt động, mặt hàng): travel.com.vn; hoadalattravel.vn/cho-dem-da-lat/ và /cho-da-lat/
