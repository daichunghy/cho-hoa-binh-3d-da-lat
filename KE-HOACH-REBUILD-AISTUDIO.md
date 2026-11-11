# KẾ HOẠCH REBUILD "GIỐNG THẬT" — DÁN CHO ARGON (AI STUDIO)

Bạn đã đọc repo. Việc tiếp theo KHÔNG phải thêm tính năng mới tràn lan, mà là **REBUILD độ giống thật** của các khu đã có. Hiện trạng game mới ở mức "mô phỏng": đúng bố cục nhưng phẳng, thưa chi tiết, nhìn là biết đồ họa dựng vội. Mục tiêu của đợt này: người từng đến Đà Lạt mở game lên phải **nhận ra ngay từng khu** trong 3 giây, và người chưa đến phải thấy đây là một nơi chốn thật có đời sống — không phải sân khấu khối hộp.

## NGUYÊN TẮC GIỐNG THẬT (áp cho mọi khu)

1. **Mật độ 3 lớp chi tiết** — mỗi khu phải có đủ: (a) lớp silhouette: hình khối lớn đúng tỉ lệ/đúng vị trí như thật; (b) lớp trung: vật dụng đặc trưng (bàn ghế, sọt hàng, biển hiệu, xe cộ, cây đúng loài); (c) lớp vi: chi tiết nhỏ tạo "đã từng có người sống ở đây" — vệt mòn, giấy dán, thùng xốp, dây điện, chậu cây, menu viết tay (vẽ bằng canvas texture trong code, không tải ảnh ngoài).
2. **Biển hiệu là danh tính**: dùng TÊN THẬT của địa điểm/quán (đọc trong `research/`), chữ Việt đúng dấu, đúng màu thương hiệu đã ghi trong research. Cấm biển "SHOP 1 / QUÁN ĂN" chung chung.
3. **Ánh sáng theo giờ là một nửa của sự giống**: mỗi khu phải đẹp nhất đúng "giờ vàng" của nó ngoài đời (hồ: sáng sớm sương + hoàng hôn; chợ + quảng trường + sữa đậu nành: tối lên đèn).
4. **Đời sống đi kèm kiến trúc**: mỗi khu tối thiểu 1 hành vi NPC đặc trưng + 1 tương tác cho người chơi. Khu đẹp mà chết là chưa đạt.
5. Giữ nguyên toàn bộ LUẬT KHÓA trong `PROMPT-AISTUDIO-TOAN-DIEN.md` (key save `chohb3d-v1`, vị trí khóa, thước 1,82u, palette đã đo, cấm teal, cấm thông nón, dung lượng standalone ≤ 10.485.760 byte, không CDN/texture ngoài). Trước khi nộp mỗi phase phải tự chạy bộ test trong `prototype-v2/scripts/` (diag_runtime, audit_ground, test_real1, traffic harness) và báo kết quả thật.

---

## PHASE 1 — HỒ XUÂN HƯƠNG (nền của mọi thứ)

**Nhận diện bắt buộc (thiếu 1 = chưa đạt):** mặt nước xám bạc ngày / chàm chiều theo research/28; đảo Thủy Tạ tròn tách bờ + cầu cong; nhà Thủy Tạ lên đèn **hồng magenta** ban đêm phản chiếu xuống nước; đập Ông Đạo đầu tây; hàng cây bờ bắc đúng bảng phân phối research/29 (cây lá rộng nghiêng ra mặt nước là chính, thông tán ô xen kẽ, liễu ở đoạn gần Thủy Tạ, phượng tím + hoa giấy điểm nhấn); đường dạo 4 lớp tiết diện (cỏ dốc chạm nước → lát + dải tactile tối → đường nhựa → hàng cây).

**Chi tiết phải dựng thêm:**
- Nước: gợn sóng 2–3 lớp nhiễu không lặp đều + vệt phản chiếu dài dưới đèn bờ và dưới Thủy Tạ về đêm + dải nước sẫm nông sát mép bờ; thuyền thiên nga trắng bơi chậm thành đàn 3–5 chiếc ở vùng giữa hồ (ngoài chiếc cho thuê).
- Bờ: ghế bê tông 2 tấm đúng mẫu thật trên cỏ sát nước; đèn bướm cột xanh; thùng rác xanh; biển "HỒ XUÂN HƯƠNG" ở đầu cầu; xe đạp đôi cho thuê dựng ở bến.
- Sinh hoạt: người tập thể dục sáng sớm, cặp đôi ngồi ghế quay mặt ra hồ, người câu cá ở đập Ông Đạo (cần câu + xô), người bán bánh tráng nướng lưu động buổi tối gần cầu.

**Tương tác người chơi:** đạp vịt trọn vòng (đã có khung ở PROMPT trước — làm cho xong), ngồi ghế ngắm hồ (camera chậm), chụp ảnh tại 2 photo spot (cầu đảo + bờ bắc nhìn về Thủy Tạ).

## PHASE 2 — QUẢNG TRƯỜNG HÒA BÌNH + FOUNTAIN

**Nhận diện bắt buộc:** mặt tiền chợ cong nhìn thẳng từ quảng trường; đài phun nước ở quảng trường; không gian mở lát đá, tối đông người.

**Chi tiết phải dựng:**
- **Fountain**: bồn tròn nhiều tầng, tia nước cong theo parabol + bọt trắng ở chân tia + nước trong bồn gợn + đèn đổi màu chậm dưới nước buổi tối; âm thanh nước khi đứng gần (hệ ambience sẵn có). Cấm "đĩa nước tĩnh".
- Góc hát: ca sĩ + loa kéo + vòng người nghe ngồi bệt/xếp ghế nhựa, bảng ghi bài hát; xe hàng rong quanh quảng trường (bánh tráng, sữa đậu nành, khoai nướng) có khói/bốc hơi khi tối.
- Cột đèn cao quảng trường, ghế đá, bồn hoa theo mùa, bảng thông tin sự kiện của thành phố.

**Tương tác:** ném xu cầu may vào fountain (+Xu may mắn nhỏ, hiệu ứng sáng), nghe hát (đứng trong vòng nghe → mở bảng chọn bài), mua đồ ăn vặt mang đi.

## PHASE 3 — ĐƯỜNG VÀO CHỢ + BẬC TAM CẤP + KHU TRÊN ĐỈNH

**Nhận diện bắt buộc:** trục đường từ bùng binh lên chợ; mặt tiền chợ cong với pano quảng cáo + chữ CHỢ ĐÀ LẠT; tam cấp dài lên đồi; đỉnh thang là Hoa Sữa + La Tulipe + L'angfarm.

**Chi tiết phải dựng:**
- Đường vào: bùng binh + tượng giữ nguyên vị trí khóa; vỉa hè có hàng quán nhỏ, xe máy chạy + đậu đúng làn, biển chỉ đường, cây xanh đường phố; mặt tiền chợ đủ nhịp pano/LED như bản đã chốt (đừng phá).
- **Bậc tam cấp**: bậc có vệt mòn ở giữa, lan can sắt, chiếu nghỉ có **chú coi bói** (giữ nguyên), người bán vé số/đồ lưu niệm ngồi bậc, học sinh ngồi ăn vặt trên bậc buổi chiều; đứng giữa thang nhìn xuống thấy quảng trường + mặt tiền chợ — đây là góc "postcard", phải đẹp.
- **Khu trên đỉnh**: Hoa Sữa (điểm cao nhất, ngắm toàn cảnh), sân nhỏ + lan can ngắm cảnh, biển hiệu 2 shop đúng thương hiệu; từ đây nhìn xuống thấy mái chợ + quảng trường + một phần hồ xa.

**Tương tác:** coi bói (đã có), ngắm cảnh đỉnh thang (photo spot), mua đặc sản ở 2 shop (gắn với hệ shop sẵn có).

## PHASE 4 — KHU SỮA ĐẬU NÀNH + HỒNG TRÀ HÒA BÌNH (khu ẩm thực đêm ở khu Hòa Bình)

Đọc `research/25-thu-thap-web-hoa-sua-hong-tra-cau-thang.md` trước khi dựng — tên quán, vị trí, khung cảnh lấy từ đó, không tự bịa.

**Nhận diện bắt buộc:** dãy quán/xe sữa đậu nành nóng buổi tối gần khu thang/quảng trường — bàn ghế nhựa thấp, nồi sữa bốc khói, ly thủy tinh sữa nóng, bánh ngọt ăn kèm; quán hồng trà với biển hiệu + menu tường.

**Chi tiết phải dựng:** nồi/ấm kim loại có **hơi bốc liên tục**, cô bán hàng múc sữa bằng vá, khách ngồi ghế nhựa cầm ly hai tay cho ấm, đèn vàng ấm hắt ra vỉa hè lạnh; bảng menu viết tay (canvas texture): sữa đậu nành, sữa đậu xanh, hồng trà, bánh tiêu/bánh quẩy…

**Tương tác (gắn với hệ lạnh sẵn có — quan trọng):** mua ly sữa nóng **15 Xu** → uống tại chỗ: nhân vật bốc hơi ấm, chỉ số "ấm" tăng, hết trạng thái run lạnh trong 3 phút game; hồng trà mang đi được (item trong túi, dùng lúc đang đi hồ). Đây là khu cho người chơi "sạc ấm" trước khi ra hồ buổi tối — phải nối đúng vào hệ nhiệt độ hiện có, không làm hệ mới.

## PHASE 5 — HỆ GAMEPLAY SỐNG: MUA – ĂN – ĐI DẠO – TƯƠNG TÁC – COI BÓI

Các phase trên dựng NƠI CHỐN; phase này dựng VIỆC LÀM trong nơi chốn đó. Game hiện đã có khung (tiền Xu Chợ, túi đồ cơ bản, tủ đồ, thuê xe/thuyền, hộ chiếu) — nhiệm vụ là làm chúng thành vòng chơi trọn vẹn, không làm hệ song song trùng lặp.

### 5.1 Túi đồ & vật phẩm (nền của mọi thứ dưới đây)
- Túi đồ có giao diện mở được (phím/nút riêng), chia 4 ngăn: **Đồ ăn – Thức uống – Đặc sản & lưu niệm – Đồ dùng**. Vật phẩm mua ở bất kỳ đâu phải VỀ ĐÚNG NGĂN và còn đó sau khi lưu/nạp lại (ghi vào save `chohb3d-v1`, tương thích save cũ).
- Mỗi vật phẩm có: tên Việt đúng, giá, mô tả 1 dòng, hiệu ứng khi dùng, hạn dùng nếu là đồ ăn (đồ ăn để quá 1 ngày game = hỏng, bỏ thùng rác được Xu 0 nhưng +điểm sạch sẽ nhỏ — chi tiết vui, đừng bỏ).
- Đặc sản mua ở chợ/2 shop đỉnh thang (mứt, trà, len…) là vật phẩm **tặng được**: tặng NPC tăng thân thiện (xem 5.5), tặng đủ người mở thành tựu trong hộ chiếu.

### 5.2 Mua sắm trọn vòng (chợ + quầy rong + shop)
- Tới quầy → bấm tương tác → bảng hàng của quầy đó (mỗi quầy bán đúng nhóm hàng của nó, giá theo Xu, có món đắt/rẻ khác nhau) → chọn món → **mặc cả** (mini-tương tác 1 chạm: 50% giảm 10–20%, thất bại tiểu thương lắc đầu nhưng vẫn bán giá gốc; mỗi quầy mặc cả được 1 lần/ngày game) → trả Xu → món vào túi + tiểu thương nói 1 câu theo kết quả.
- Mua xong phải THẤY được: nhân vật cầm túi đồ đi theo vài giây, hoặc món ăn cầm trên tay ngay (xem 5.3). Cấm mua xong "biến mất vào hư không" không dấu vết.
- Hàng rong quanh hồ/quảng trường cũng mua được theo cùng vòng này (bánh tráng nướng, khoai nướng, kẹo chỉ…), không cần bảng lớn — menu rút gọn 3 món.

### 5.3 Ăn & uống (hành động phải nhìn thấy)
- Đồ ăn/thức uống trong túi bấm **Dùng** → nhân vật thực hiện hành động: cầm lên ăn/uống (animation đơn giản bằng chuyển động tay + vật phẩm trên tay + hiệu ứng: hơi nóng bốc với đồ nóng, tiếng "ngon" dạng bong bóng chữ), mất vài giây game, không bị cắt giữa chừng bởi di chuyển (đang ăn thì đứng/ngồi yên).
- Hiệu ứng rõ ràng, nối vào hệ sẵn có: đồ nóng (sữa đậu nành, khoai nướng, bánh tráng) → **+ấm** (hệ lạnh); đồ ngọt/kem → +vui (chỉ số tâm trạng hiển thị ở HUD nhỏ); nước/trà → mang đi dùng khi đang đi dạo.
- Ăn tại điểm đẹp (ghế bờ hồ, bậc thang, quảng trường) cho +vui gấp đôi — khuyến khích người chơi picnic; ăn xong có **vỏ/rác trên tay** phải bỏ thùng rác (tương tác nhỏ, thùng rác đã có ở bờ hồ + chợ).

### 5.4 Hành động & đi dạo
- **Bánh xe hành động** (giữ phím/nút cảm xúc): Vẫy tay, Cúi chào, Ngồi xuống (ngồi được trên ghế/bậc thang/bờ cỏ đúng điểm), Pose chụp ảnh (2–3 pose), Nhảy theo nhạc (chỉ "bắt nhịp" khi gần góc hát/fountain có nhạc), Chỉ tay ngắm cảnh.
- **Chế độ đi dạo**: nút chuyển đi thường ↔ đi dạo thong thả (tốc độ chậm, camera hạ thấp + lia nhẹ điện ảnh, nhân vật thỉnh thoảng tự ngẩng ngắm cảnh khi qua điểm đẹp). Đi dạo quanh hồ đủ 1 vòng = ghi nhận vào hộ chiếu (thành tựu "Một vòng Xuân Hương").
- NPC cũng dùng các hành động này (ngồi ghế, vẫy chào người chơi khi thân thiện cao) — thế giới sống hai chiều, không phải mình người chơi diễn.

### 5.5 Tương tác NPC có chiều sâu
- Chào hỏi theo giờ ("Chào buổi sáng cô!"), NPC nhớ mặt: mua quen ở 1 quầy 3 lần → lần sau được giảm 5% + gọi tên; tặng quà đúng sở thích (ghi trong hội thoại gợi ý) → thân thiện tăng, mở câu thoại mới + đôi khi tặng lại món nhỏ.
- Xin chụp ảnh cùng NPC (nối Phase 6 selfie): NPC đồng ý thì đứng cạnh pose; từ chối khéo khi đang bận bán hàng giờ đông.

### 5.6 Coi bói — làm cho ra trò (chú Ba ở chiếu nghỉ tam cấp, GIỮ NGUYÊN vị trí)
- Một phiên bói trọn vẹn: ngồi xuống chiếu → chọn hình thức (**Xem bài** / **Xin xăm** / **Xem chỉ tay**) → trả **20 Xu** → chú Ba xào bài/rút xăm với animation → ra **quẻ có tên + lời giải 3–4 câu viết sẵn theo quẻ** (kho tối thiểu 12 quẻ, rút ngẫu nhiên có trọng số theo "vận" trong ngày) → quẻ gắn **hiệu ứng nhỏ thật trong ngày game**: vd quẻ Tài = mặc cả dễ thành hơn, quẻ Duyên = NPC thân thiện nhanh hơn, quẻ An = trời ít lạnh hơn.
- **Quẻ ngày**: mỗi ngày thật (theo đồng hồ máy) người chơi có 1 quẻ nền; xem ở trang đầu hộ chiếu. Coi bói ở chú Ba là phiên sâu hơn, tốn Xu.
- Viết lời quẻ: giọng Nam bộ hóm hỉnh, không hù dọa, không phán chết chóc/bệnh tật; quẻ xấu phải có câu "hóa giải" bằng hành động trong game (vd: ném xu fountain, tặng quà 1 người) — nối các hệ lại với nhau.

## PHASE 6 — UGC SELFIE & CHIA SẺ ẢNH (tính năng mới, làm sau Phase 5 vì dùng pose ở 5.4)

Mục tiêu: người chơi chụp selfie trong game và **chia sẻ ra ngoài** được, ảnh nhìn là biết ngay Chợ Hòa Bình Online (khung + địa điểm + nhân vật chibi của người chơi).

**Phạm vi kỹ thuật (game tĩnh, không server — làm đúng vậy, không hứa hẹn backend):**
1. **Chế độ chụp ảnh**: nút camera trong HUD → ẩn HUD, camera tự do giới hạn quanh nhân vật + chế độ **selfie** (camera trước mặt nhân vật, thấy mặt chibi + cảnh phía sau). Nút chuyển góc: selfie / toàn cảnh / cận cảnh.
2. **Điểm selfie chính thức** (gắn với photo spot sẵn có): mặt tiền chợ, giữa tam cấp nhìn xuống, cầu đảo Thủy Tạ, bờ hồ hoàng hôn, fountain quảng trường, đỉnh Hoa Sữa, bàn sữa đậu nành. Đứng đúng điểm có gợi ý góc chụp đẹp (camera tự về vị trí vàng khi bấm selfie tại điểm).
3. **Khung & tem ảnh**: khung viền theo từng địa điểm (tên địa điểm + dòng "Chợ Hòa Bình Online • Đà Lạt" + ngày giờ trong game), 3 bộ lọc (Ấm tối Đà Lạt / Sáng sớm sương / Phim cũ), sticker chibi đơn giản vẽ bằng canvas (tim, ly sữa, thuyền vịt). Ảnh xuất tỉ lệ **4:5 (1080×1350)**.
4. **Chia sẻ**: chụp xong hiện ảnh → nút **Chia sẻ** (Web Share API `navigator.share` kèm file ảnh; máy không hỗ trợ thì tải PNG về máy) + nút lưu vào **Album Đi Chợ** trong game (localStorage chỉ lưu metadata + ảnh nén nhỏ; có giới hạn số ảnh, cảnh báo khi đầy).
5. **UGC trong game**: "Tường ảnh du khách" ở quảng trường — bảng lớn hiển thị các ảnh người chơi đã lưu trong Album (chỉ máy của họ, nói rõ trong CHANGELOG là local, không giả vờ có server). Hộ chiếu Đi Chợ có thêm trang **Album**: chụp đủ selfie tại 7 điểm chính thức = nhận dấu đặc biệt "Nhiếp ảnh gia Hòa Bình".
6. **Kỹ thuật chụp**: render frame riêng lúc chụp (không bật preserveDrawingBuffer toàn cục để tránh tốn hiệu năng), độ phân giải chụp cố định, chụp khi đang pause chuyển động nền 1 nhịp để ảnh nét.

**Chống lạm dụng phạm vi:** không làm mạng xã hội trong game, không bình luận, không tài khoản. UGC ở đây = người chơi tạo ảnh của mình + chia sẻ ra nền tảng ngoài bằng công cụ của máy.

---

## PHASE 7 — KHÍ QUYỂN, SƯƠNG MÙ & GÓC NHÌN (phần "nghề" làm game 3D)

Các phase trước dựng vật và việc; phase này là thứ biến "mô phỏng" thành "có hồn": không khí Đà Lạt + cách người chơi NHÌN thế giới.

### 7.1 Sương mù — chữ ký của Đà Lạt (quan trọng nhất phase này)
- **Sương theo giờ thật của Đà Lạt**: 5:00–7:30 sương dày nhất (tầm nhìn 60–90u, hồ chỉ còn bóng đảo mờ), tan dần tới 9:00; chiều tối sau 17:30 sương quay lại mỏng trên mặt nước trước, rồi lan lên bờ; đêm khuya sương nhẹ quanh đèn (mỗi bóng đèn có quầng halo trong sương).
- **Kỹ thuật 3 lớp chồng nhau** (không chỉ FogExp2 trơn): (1) sương xa theo FogExp2 đổi màu theo bầu trời (sáng: xám bạc `#c9ced2`, hoàng hôn: hồng chàm, đêm: chàm tối); (2) **cuộn sương thấp trôi** — các mảng alpha mềm lớn trôi chậm trên mặt hồ + **cuộn xuống từ đỉnh đồi qua mái chợ** vào sáng sớm (dùng lại idiom mảng sương của hồ, mở rộng lên sườn đồi); (3) sương cục bộ ở hẻm/thung nhỏ sau mưa.
- **Đồi xa xếp lớp**: dựng 2–3 dải silhouette đồi thông bao quanh phía hồ + sau đồi chợ, màu nhạt dần theo khoảng cách (aerial perspective) — nhìn từ đỉnh Hoa Sữa và bờ hồ phải thấy "núi đồi Đà Lạt trong sương", không phải chân trời trống.
- Sương phải là GAMEPLAY: điểm selfie "săn sương" (Phase 6) chỉ mở khung đặc biệt khi chụp trong sương sớm; NPC thưa hẳn khi sương dày; đèn xe máy xuyên sương có vệt sáng.

### 7.2 Thời tiết Đà Lạt (xoay vòng nhẹ, không cực đoan)
- 4 trạng thái: **Nắng sớm trong** / **Sương mù** / **Mưa phùn chiều** (mưa nhỏ hạt mịn: mặt đường + lát chuyển sẫm và bóng loáng phản chiếu đèn, NPC che ô + áo mưa, hàng rong che bạt, mặt hồ lăn tăn dày) / **Hoàng hôn hồng** (bầu trời gradient cam–hồng–chàm 20 phút game trước khi đêm hẳn).
- Chuyển trạng thái mềm trong vài phút game, có dấu hiệu báo trước (gió mạnh lên, mây kéo). Thời tiết ghi vào "quẻ ngày" (Phase 5.6) cho có liên kết hệ thống.

### 7.3 Camera & góc nhìn — đạo diễn như game thật
- **4 chế độ camera**: (1) Diorama (mặc định hiện tại, góc ~45°); (2) **Tản bộ** — camera ngang vai sau lưng, FOV hẹp hơn, lia mềm khi rẽ, dành cho đi dạo/chợ đông; (3) **Ngắm cảnh** — tại các điểm ngắm (đỉnh Hoa Sữa, giữa tam cấp, cầu đảo, bờ hồ) bấm tương tác là camera tự về **góc postcard đã đạo diễn sẵn** của điểm đó, người chơi chỉ việc ngắm/chụp; (4) **Ảnh** — camera của Phase 6.
- **Chống kẹt camera**: camera không xuyên mái chợ/tường/thân cây lớn (va chạm mềm + tự nâng khi leo thang), leo tam cấp camera tự lùi để thấy cả người lẫn quảng trường phía dưới; vào nhà lồng camera tự hạ trần ảo (không quay qua mái).
- **Tầm nhìn có chủ đích (vista design)**: kiểm tra và dọn 5 khung nhìn vàng — spawn nhìn dọc trục lên chợ; giữa thang nhìn xuống quảng trường + mặt tiền cong; cầu đảo nhìn về Thủy Tạ; đỉnh Hoa Sữa nhìn xuống mái chợ + hồ xa trong sương; bờ bắc nhìn chéo mặt hồ về đảo lúc hoàng hôn. Không vật lạ nào được mọc chắn 5 khung này.
- Chuyển cảnh mềm giữa các chế độ (0,6–1s ease), không cắt cụt gây chóng mặt; FOV thay đổi nhẹ theo tốc độ khi chạy xe.

### 7.4 Ánh sáng & màu — phần còn lại của "giống thật"
- Chu kỳ ngày: bình minh (sương + nắng xiên vàng qua hàng thông, bóng dài), trưa (sáng phẳng, ít dùng), **giờ vàng 17:00–18:30** (ấm, bóng dài, hồ lấp lánh), chạng vạng (đèn lên dần theo từng khu: chợ trước, hồ sau), đêm (vũng sáng đèn + tối lạnh xung quanh, Thủy Tạ magenta là điểm sáng chủ đạo phía hồ).
- Mặt nước có **lấp lánh nắng** (specular glint theo hướng mặt trời/trăng) — thiếu cái này nước sẽ mãi trông như nhựa.
- Ướt sau mưa phùn: lát + nhựa đường sẫm + phản chiếu vệt đèn (idiom vệt sáng sẵn có), mái quầy đọng sáng.

### 7.5 Chuyển động nhỏ & âm thanh không gian (thế giới thở)
- Cây đu theo gió (đỉnh tán lệch nhịp ngẫu nhiên, mạnh khi sắp mưa), khăn/áo NPC bay nhẹ, khói hàng ăn cuộn lên và tan theo gió, pano LED nhấp nháy rất nhẹ, đàn chim bay qua hồ buổi sáng + bóng chim trên mặt nước.
- Âm thanh theo khoảng cách thật: đứng gần fountain nghe nước, gần góc hát nghe nhạc rõ, trong chợ nghe ồn ào người + tiếng rao, bờ hồ nghe gió thông + nước vỗ bờ nhỏ; xe máy chạy qua có tiếng lớn dần rồi xa dần. (Hệ ambience 5 lớp sẵn có — mở rộng theo vị trí, không thay mới.)

### 7.6 CHỢ ĐÊM cuối tuần (biến hình theo lịch — cảnh đêm Hòa Bình nổi tiếng nhất)
- Tối thứ 6–Chủ nhật (ngày game): khu quảng trường + chân tam cấp + đường trước chợ **biến thành chợ đêm**: hàng quán sáng đèn dựng thêm theo hàng, dây đèn vàng chăng ngang, đông người gấp đôi, hàng ăn khói nghi ngút, có gian đồ len/đặc sản; sữa đậu nành (Phase 4) đông nhất giờ này.
- Biến hình phải MƯỢT: quán dựng dần từ 17:30, dọn dần sau 22:00, NPC tiểu thương chợ đêm là nhóm riêng. Đây là "sự kiện" để người chơi quay lại game đúng giờ — ghi vào lịch trong hộ chiếu.

### 7.7 Đẹp nhưng phải nhẹ (ràng buộc kỹ thuật cho Argon)
- Mọi vật lặp (ghế, đèn, quầy, cây) dùng InstancedMesh hoặc merge hình học; cây xa dùng bản LOD ít đa giác; bóng đổ chỉ từ 1 nguồn sáng chính + đèn điểm không đổ bóng; sương dùng mảng alpha rẻ tiền, cấm volumetric thật.
- Ngân sách: giữ 60fps trên máy yếu và standalone ≤ trần byte đã khóa; phase này xong mà tụt hiệu năng là CHƯA ĐẠT dù đẹp.

## THỨ TỰ & NGHIỆM THU

- Làm lần lượt Phase 1 → 7, mỗi phase xong phải: chạy đủ bộ test scripts của repo và báo số thật; mô tả thay đổi trong CHANGELOG kèm **ảnh chụp màn hình preview** của từng khu ở góc tầm mắt người chơi (nếu môi trường của bạn render được) hoặc mô tả chính xác những gì đã thay để người kiểm chứng đối chiếu.
- Tiêu chí đạt của mỗi khu: (1) đủ "nhận diện bắt buộc"; (2) có đủ 3 lớp chi tiết; (3) có tương tác chạy được; (4) không phá luật khóa + không đen màn hình + save cũ nguyên vẹn.
- Sync về GitHub vào **nhánh `aistudio-v1`**, không ghi đè `main`. Bên dự án sẽ kéo về chạy kiểm chứng độc lập rồi mới hợp nhất — vì vậy CHANGELOG phải trung thực tuyệt đối: làm được tới đâu ghi tới đó, mục chưa xong ghi "CHƯA XONG", cấm nhận bừa.
