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

## THỨ TỰ & NGHIỆM THU

- Làm lần lượt Phase 1 → 6, mỗi phase xong phải: chạy đủ bộ test scripts của repo và báo số thật; mô tả thay đổi trong CHANGELOG kèm **ảnh chụp màn hình preview** của từng khu ở góc tầm mắt người chơi (nếu môi trường của bạn render được) hoặc mô tả chính xác những gì đã thay để người kiểm chứng đối chiếu.
- Tiêu chí đạt của mỗi khu: (1) đủ "nhận diện bắt buộc"; (2) có đủ 3 lớp chi tiết; (3) có tương tác chạy được; (4) không phá luật khóa + không đen màn hình + save cũ nguyên vẹn.
- Sync về GitHub vào **nhánh `aistudio-v1`**, không ghi đè `main`. Bên dự án sẽ kéo về chạy kiểm chứng độc lập rồi mới hợp nhất — vì vậy CHANGELOG phải trung thực tuyệt đối: làm được tới đâu ghi tới đó, mục chưa xong ghi "CHƯA XONG", cấm nhận bừa.
