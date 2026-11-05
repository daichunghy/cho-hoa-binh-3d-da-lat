# Nghiên cứu 03 — Sansa (산사): chùa online Hàn Quốc viral cuối 10/2026

> Mục đích: rút bài học thiết kế cho dự án **Chợ Hòa Bình 3D — Đà Lạt** (thế giới 3D trên trình duyệt cho người ta đi tham quan, khám phá hàng quán, mua đồ ăn/nước uống).
> Ngày nghiên cứu: 05/11/2026. Nguồn: báo Hàn/Việt/Đài + guide trải nghiệm trực tiếp sansatempleweb.com (kiểm chứng 31/10/2026).
> Lưu ý độ tin cậy: số lượt truy cập là **số do nhà phát triển tự công bố**, báo chí ghi rõ chưa được kiểm chứng độc lập. Ngày ra mắt cũng lệch giữa các báo (26/10 theo đa số nguồn Hàn; một số báo Việt ghi 29/10). Các chi tiết gameplay lấy từ guide đã chơi thử trực tiếp + báo trải nghiệm tại chỗ (Asia Business Daily, EasyTicket) nên đáng tin hơn số liệu traffic.

---

## 1. Tổng quan

- **Sansa** (산사 = "sơn tự", chùa trên núi), địa chỉ chính thức duy nhất: `sansatemple.com` (bản đầu ở `sansa-online-temple.vercel.app`).
- Tác giả: **Park Jin-won**, 26 tuổi, tốt nghiệp Ngữ văn Anh, đang tìm việc, **không có nền tảng lập trình, không phải Phật tử**. Nick phát triển: Metamong.
- Cách làm: **vibe coding** bằng Codex của OpenAI — mô tả tính năng bằng ngôn ngữ tự nhiên cho AI viết code. Phiên bản đầu tiên chạy được sau **~30 phút**; từng tính năng nhỏ (lạy, lần tràng hạt) thêm vào khoảng 10 phút. Trong 1 năm trước đó Park đã "trò chuyện với AI mỗi ngày" và làm ~30 app/dịch vụ nhỏ.
- Động cơ ban đầu rất đời thường: muốn ghé chùa ngồi một lát để nghỉ nhưng **không còn thời gian và sức lực** đi thật; ban đầu làm **chỉ cho 1 người dùng** (chính anh).
- Quy mô lan truyền (số nhà phát triển công bố):
  - Ngày đầu: >10.000–12.000 lượt, server sập.
  - 3 ngày đầu: **~600.000 lượt**; 31/10: >900.000; **01/11: vượt 1 triệu**; ~100.000 lượt/ngày giai đoạn cao điểm.
  - Sáng 30/10: **4.679 người online đồng thời** trên 100 phòng Thanh Liên Đường (18h cùng ngày: 5.119), 5 phòng kín 100/100.
  - Đài Loan: ~50.000 lượt trong một đêm; Việt Nam, Thái Lan cũng tham gia đáng kể dù giao diện toàn tiếng Hàn.
- Hạ tầng: sức chứa nâng liên tục **20 → 100 → 1.200 → 10.000 chỗ** (= 100 phòng × 100 người), chạy ~100 server qua Cloudflare. Sau này có mặt trên Toss mini-app; Park dự định đưa lên App Store.
- Tiền: ban đầu không có mô hình thu tiền. Người dùng **chủ động đề nghị được đóng góp** → Park thêm tính năng **"cúng gạo" (공양미)** để đỡ chi phí server (từng phải tạm khóa vì quá tải; QR KakaoPay bị chặn, phải đổi kênh). Báo chí thống nhất nhận định: **viral ≠ có doanh thu bền vững** — đây là bài toán chưa giải của Sansa.

## 2. Thiết kế thế giới 3D

Nguyên tắc bao trùm: **một không gian nhỏ, ít khu vực, mỗi khu vực đúng một "mood" và một hành động chủ đạo** — không bản đồ lớn, không nhiệm vụ bắt buộc.

### 2.1. Bố cục không gian (theo guide chơi thử 31/10)

| Khu vực | Vị trí / cách vào | Nội dung & mood |
|---|---|---|
| Cổng chùa + sân trước | Điểm spawn | Lối đi đá dẫn thẳng tới chính điện mái ngói; người chơi "đáp" xuống sân và đi ngay, không qua menu rườm rà |
| **Chính điện Thanh Liên Đường (Cheongyeondang)** | Đi từ cổng vào, bấm nút vào điện hiện gần cửa (đi qua cửa thôi chưa đủ — phải bấm nút chuyển cảnh) | Tượng Phật lớn ở trung tâm, hàng bồ đoàn xếp ngay ngắn. Hood chính: lạy Phật, chắp tay, nghe tụng kinh |
| Vườn trái | Rẽ trái khi từ cổng nhìn về chính điện | **Hồ sen + sàn gỗ trên mặt nước**, đường mòn cong, cây cối. Chỉ để đi dạo/ngắm — guide kiểm chứng **không có** tương tác nhặt đồ/ghi ước/thưởng tại đây |
| Vườn phải → **Sân Trăng (Moonlight Courtyard)** | Bấm nút "vào Sân Trăng" ở lối vào | Khu "ngược mood": cùng phím số 1 nhưng **đổi từ lạy thành nhảy (dance)**; có nhạc riêng, hiện tên track, nút mute riêng |
| Màn hình tràng hạt | Mở bằng phím 2 / nút 염주 | **Thoát khỏi thế giới 3D** sang màn hình 2D riêng: tràng hạt gỗ xếp dọc trên nền be, bộ đếm x/108 ở góc. Cảm giác như "bước vào phòng riêng" |

- Âm thanh là một lớp "kiến trúc" riêng: chia 3 kênh tách biệt trong cài đặt — **tiếng môi trường (gió, chim), tiếng tụng kinh (Bát Nhã Tâm Kinh), hiệu ứng**. Nhạc ở Sân Trăng có điều khiển riêng, tắt âm thanh chung không tắt nhạc sân (chi tiết nhỏ nhưng cho thấy họ quản lý mood theo khu vực).
- Có **nhân vật thường trú (resident characters)** trong cảnh, tách biệt với số người chơi online hiển thị — thế giới không bao giờ trông trống rỗng kể cả khi ít người. Số nhân vật nhìn thấy có thể khác số occupancy hiển thị.

### 2.2. Nhân vật chú tiểu

- Vào là được **gán tự động** một chú tiểu (dongja-seung) mũm mĩm mặc áo tu, **không cần đăng ký, không cần tạo nhân vật**.
- **Tên (pháp danh) gán ngẫu nhiên**, kiểu thơ + hơi hài: "Mây thong dong / Leisurely Cloud", "Ánh trăng dịu nhẹ / Soft Moonlight", "Bước chân chậm rãi", "Lá thông non / Little Pine Needle", "Chim núi nhỏ", "Cây cảm xúc / Emotional Tree"... Tên hiện trên đầu nhân vật — đây là chi tiết được chụp màn hình chia sẻ nhiều nhất nhì.
- Guide kiểm chứng 31/10: **không có** trình sửa tên/trang phục trong giao diện thường; đổi phòng = được gán tên và vị trí bắt đầu mới. (Một số bài phân tích marketing về sau nhắc người dùng tự đặt pháp danh/chọn giao diện — nhiều khả năng là tính năng thêm ở phiên bản sau hoặc nhầm với các bản phái sinh; khi áp dụng nên coi "tự đặt tên" là nhu cầu đã được thị trường xác nhận, không phải tính năng gốc.)

### 2.3. Điều khiển — tối giản đến mức cực đoan

- Desktop: WASD / phím mũi tên hoặc **click mặt đất để đi**, kéo chuột xoay camera, lăn chuột zoom. Chỉ **3 nút hành động** ở thanh dưới + vài nút ở góc trên là toàn bộ UI.
  - Phím **1**: lạy / dừng (ở Sân Trăng: nhảy / dừng)
  - Phím **2**: mở tràng hạt
  - Phím **3**: chắp tay
- Mobile: chạm đất để đi, vuốt xoay góc nhìn, pinch zoom; các nút đủ lớn để bấm. Tải trang ~6 giây trên điện thoại (theo trải nghiệm của EasyTicket).
- **Hành động có "vật lý xã hội"**: bấm lạy thì nhân vật **không lạy tại chỗ** — hiện thông báo "đang tới bồ đoàn", nhân vật tự đi tìm **bồ đoàn trống**, tới nơi mới lạy, và lạy liên tục cho tới khi bấm dừng. Một bồ đoàn = đúng một người. Yêu cầu chắp tay trong lúc đang lạy phải **xếp hàng chờ** hành động hiện tại xong.

## 3. Cơ chế xã hội: nhiều người cùng hiện diện, không có ô chat

Đây là quyết định thiết kế nổi tiếng nhất của Sansa — và theo chính Park, nó là **cố ý cắt bỏ**: bản đầu **từng có** tính năng trò chuyện, anh **gỡ ra**.

- **Không chat chữ, không voice, không tin nhắn riêng, không kết bạn.** Tagline của sản phẩm: nơi "ngồi cạnh nhau mà không thể bắt chuyện" — Park tóm gọn: *"ngồi chung thì được, bắt chuyện thì không."*
- Hình thức giao tiếp duy nhất: **chắp tay chào**. Khi ai đó chắp tay, người xung quanh nhận **dòng thông báo** kiểu "X vừa chắp tay chào bạn". Nhận biết sự hiện diện của nhau mà **không tạo nghĩa vụ phải trả lời** — khác hẳn mọi nền tảng xã hội khác.
- Hiện diện là thật và đồng bộ: mọi động tác (đi lại, lạy, chắp tay) hiện ngay trên màn hình của người cùng phòng. Sự đông đúc nhìn thấy được chính là nội dung: chính điện kín chú tiểu là hình ảnh biểu tượng của Sansa.
- Cơ chế phòng (room/shard): tự động gán phòng khi vào; mỗi phòng Thanh Liên Đường tối đa 100 người; có danh sách phòng kèm occupancy, thông báo phòng đầy và chọn phòng khác/refresh. Giờ cao điểm người đến sau phải **đi lòng vòng, đứng chờ hoặc xếp hàng** vì hết bồ đoàn — khan hiếm này vô tình thành meme (xem mục 5).
- Hệ quả tâm lý được người dùng và chuyên gia lặp lại: cảm giác **đồng hành không áp lực** — "biết có người ngồi cạnh lúc nửa đêm" là đủ; người hướng nội "lần đầu dám ngồi hàng đầu". GS. Sung Hae-young (ĐH Quốc gia Seoul): nhiều người muốn cảm giác bình yên của nơi thờ tự **mà không muốn chịu áp lực thực hành đức tin**, và tính ẩn danh/không-giao-tiếp đáp ứng đúng nhu cầu đó.

### Lịch lễ chung (ritual có giờ hẹn)

- Cài đặt của Sansa thông báo **lễ chung (예불) mỗi ngày lúc 05:00 và 18:00 giờ Hàn Quốc (KST, UTC+9)** — quy ra giờ Việt Nam là **03:00 và 16:00**. Lưu ý: guide chỉ xác nhận thông báo trong giao diện; việc trực tiếp dự lễ đúng giờ và tính đồng bộ phát giữa các máy **chưa được kiểm chứng**.
- Ngoài giờ lễ chung, người dùng tự bật nghe tụng kinh cá nhân bất cứ lúc nào (phân biệt rõ "nghe riêng" vs "lễ chung theo giờ").
- Ý nghĩa thiết kế: chỉ 2 mốc giờ/ngày nhưng tạo **lý do quay lại đúng giờ** và cảm giác "cả cộng đồng cùng làm một việc" — retention bằng lịch hẹn, không bằng điểm số.

## 4. Vì sao viral & cơ chế giữ chân (retention)

### 4.1. Vì sao viral

1. **Rào cản = 0**: mở link là vào — không cài app, không tài khoản, không tạo nhân vật, vài giây là "đang ở trong chùa". Mọi ma sát bị cắt trước khi người dùng chạm giá trị đầu tiên.
2. **Một ý tưởng nói trong 1 câu là hiểu và thấy lạ**: "ngôi chùa online nơi mọi người ngồi cùng nhau mà không nói gì". Nghịch lý này tự nó là hook truyền thông.
3. **Hình ảnh tự nó kể chuyện**: một chính điện chật kín hàng trăm chú tiểu giống hệt nhau ngồi im — chụp màn hình là thành bài đăng, không cần giải thích (chi tiết ở mục 5).
4. **Đúng nhu cầu có sẵn**: giới trẻ Hàn đang trong làn sóng "Phật giáo hip" (hội chợ Phật giáo Seoul 2024–2026 kỷ lục khách 20–30 tuổi, nhân vật DJ NewJeansNim phối EDM với kinh Phật...); áp lực công việc/thất nghiệp tạo "thế hệ nghỉ ngơi" muốn một chỗ ngồi yên không bị đòi hỏi gì.
5. **Câu chuyện tác giả**: một thanh niên thất nghiệp, học Ngữ văn Anh, làm bằng AI trong 30 phút — báo chí và mạng xã hội có sẵn một nhân vật để kể.
6. **Lan truyền không biên giới**: giao diện toàn tiếng Hàn vẫn hút 50.000 lượt Đài Loan trong một đêm (báo Đài còn ra guide riêng) — vì trải nghiệm không phụ thuộc ngôn ngữ.

### 4.2. Retention — giữ chân bằng nhịp, không bằng game hóa

Sansa **không có** điểm, cấp độ, nhiệm vụ, bảng xếp hạng, đăng nhập hằng ngày (bộ đếm tràng hạt còn reset khi thoát ra vào lại). Thứ giữ người quay lại:

- **Phiên ngắn, ghé bất cứ lúc nào**: mở tab ngồi cùng trong lúc làm việc, ghé trên đường đi làm, trước giờ ngủ — nhiều người dùng kể ra vào **nhiều lần trong ngày**, mỗi lần vài phút. Sansa hoạt động như một "ambient tab" hơn là một game phải chơi.
- **Nghi thức lặp có đếm**: 108 lạy / 108 hạt là mục tiêu tự thân, có tiến trình nhìn thấy được, làm đi làm lại được — vòng lặp thiền định thay cho vòng lặp phần thưởng.
- **Lịch lễ cố định 05:00 & 18:00**: hẹn giờ quay lại (xem 3).
- **Sự hiện diện của người khác thay đổi mỗi lần vào**: phòng đông/vắng, người ngồi cạnh khác nhau — cùng một cảnh nhưng không lần nào giống hệt lần nào.
- **Nội dung theo mùa & mở rộng do chính tác giả hứa hẹn**: thêm âm thanh ngoài Tâm Kinh, cải thiện mõ/tràng hạt, mở rộng bản đồ, sự kiện treo đèn lồng mùa thi đại học (CSAT), tính năng đi dạo/thả đèn theo mùa, bản App Store — tạo kỳ vọng "lần sau vào sẽ có cái mới".
- **Cộng đồng bên ngoài sản phẩm**: cuộc trò chuyện tiếp tục trên Threads/TikTok/Facebook sau khi rời chùa (meme, khoe pháp danh, than hết chỗ) → kéo người chưa vào tò mò vào thử, và nhắc người cũ quay lại. Xem mục 5.

> Đối chứng đáng lưu ý: các nền tảng Việt Nam phái sinh (Niệm Phật Online...) giữ chân bằng lớp ngược lại — nhiệm vụ ngày/tuần, điểm công đức, cấp độ, vật phẩm sưu tầm, bảng xếp hạng. Advertising Vietnam nhận xét hai hướng đều có lý do quay lại, nhưng cảnh báo **game hóa quá tay có thể làm lệch ý nghĩa trải nghiệm**; Sansa chứng minh hướng "tĩnh" cũng giữ được người — ít nhất trong cửa sổ viral. Chưa có số liệu công khai về giữ chân 7/30 ngày của Sansa; 1 triệu lượt tuần đầu **chưa chứng minh được gắn bó dài hạn**.

## 5. Làn sóng Threads / TikTok / Facebook (bổ sung 05/11/2026)

> Phạm vi kiểm chứng: công cụ tìm kiếm social chuyên dụng bị timeout khi truy vấn nên **không lấy được bài TikTok/Facebook gốc theo link**. Các dữ kiện dưới đây lấy từ báo chí Hàn/Việt/Đài **tường thuật và trích lại** bài đăng, bình luận, số liệu tương tác trên Threads/Instagram/TikTok/Facebook — đủ để nắm dạng nội dung và phản ứng, nhưng khi cần trích nguyên văn một bài cụ thể phải đối chiếu lại link gốc.

### 5.1. Kênh và nhịp lan truyền

- **Điểm gieo (seeding) chính là Threads + Instagram của chính Park** (tài khoản @metamong.dev). Park dùng Threads như **nhật ký phát triển công khai (devlog)**: thông báo server sập, công bố mốc người dùng, xin lỗi, hứa tính năng. Bài thông báo sự cố server được ~**7.100 lượt thích**, bài báo mốc 100.000 lượt/ngày ~**4.500 lượt thích** (Nongmin Shinmun, qua Soha) — tức **chính quá trình vận hành trở thành nội dung được follow**, không chỉ sản phẩm.
- Nhịp tăng trưởng theo mốc anh tự đăng: 29/10 đăng ~12.000 người/ngày đầu và server sập → ngay tối đó đăng mốc 100.000/ngày → 31/10 báo chí dẫn mốc 600.000/3 ngày. Mỗi mốc là một đợt bài mới.
- **Nhảy biên giới qua Threads**: Đài Loan bùng trước (báo Đài ra guide, Threads Đài lan mạnh), rồi Việt Nam và Thái Lan. Một **bài Threads tiếng Việt** kèm ảnh chính điện kín chú tiểu đạt **152.000 lượt xem, 8.600 lượt thích trong 7 giờ** (được ít nhất 3 báo độc lập dẫn lại: Soha, Asia Daily, thitruonghanghoa).
- Sau đó là **lớp nội dung phái sinh ăn theo**: hàng loạt blog/guide SEO "cách vào chùa, cách lạy, giờ tụng kinh" (CafeBiz ghi nhận tìm "Sansa" trên mạng Hàn ra cả loạt blog hướng dẫn viết để hút view), báo chí các nước viết lại, và **~300 không gian ảo phái sinh** ra đời trong vài ngày (nhà thờ online InPeace/Chanmi, sauna Goyo, campsite, hầm mỏ...) — mỗi sản phẩm con lại là một đợt nhắc tên sản phẩm mẹ.

### 5.2. Các dạng bài/reel lan truyền mạnh nhất

1. **Ảnh/quay màn hình chính điện đông nghẹt chú tiểu** — dạng hero content số 1. Hàng trăm avatar giống hệt nhau ngồi kín bồ đoàn lúc 7h sáng; caption tiếng Việt tiêu biểu được báo dẫn: *"thị trường đi chùa online dạo này khắc nghiệt, mới sáng sớm server đã chật kín người"*. Công thức: hình ảnh phi lý (đông nghẹt) + bối cảnh tĩnh lặng = tương phản gây cười và gây tò mò cùng lúc.
2. **Meme xếp hàng / hết bồ đoàn / full phòng** — người vào sau đứng lòng vòng không tìm được chỗ ngồi trở thành trò đùa toàn mạng. Netizen Hàn (qua báo Đài LTN): *"người hiện đại hỏa khí lớn thật, đến lạy Phật online cũng phải xếp hàng dài"*. Bản Việt: *"phải chuyển máy chủ vì chính điện quá đông, lo mất chỗ ngồi"*, *"mất Wi-Fi có phải tích phước lại từ đầu không?"*, *"mua gói VIP có lên làm trụ trì được không?"*. Khan hiếm hạ tầng (lỗi vận hành) biến thành **bằng chứng xã hội + chất liệu meme** thay vì chỉ là phàn nàn.
3. **Clip lạy 108 lần / lần tràng hạt** — dạng video lặp, gần như ASMR: chú tiểu cúi lạy đều đều, hạt tràng lăn qua tay, bộ đếm leo tới 108. Bình luận được dẫn: *"vừa vào đã lần hết hai vòng tràng hạt mà vẫn chưa tịnh tâm được bao nhiêu"*; nhiều bài nhấn hook *"nằm trên giường vẫn làm được 108 lạy"*.
4. **Khu nhảy / "DJ zone"** — nội dung ngược mood gây share mạnh: Asia Business Daily (02/11) ghi lại ở một gian bên phải chính điện có **~15 người dùng tụ thành vòng tròn nhảy theo nhạc Phật** bằng nút Dance/chắp tay, không có khung chat. Cùng cơ chế là **Sân Trăng**: vào khu này nút hành động đổi từ lạy thành nhảy múa dưới nhạc riêng. Trong một không gian trang nghiêm, một góc "quẩy tập thể không lời" là điểm nổ hài hước — và nó ăn theo sẵn văn hóa "Phật giáo hip/DJ" đang nóng ở Hàn (DJ NewJeansNim tại Hội chợ Phật giáo Seoul).
5. **Khoe pháp danh ngẫu nhiên** — ảnh chụp nhân vật kèm cái tên thơ/hài được gán ("Mây thong thả", "Ánh trăng dịu dàng", "Cây cảm xúc") là dạng bài cá nhân hóa, rẻ, ai vào cũng có một phiên bản của riêng mình để đăng.
6. **Bài "tôi mở tab ngồi cùng khi làm việc"** — ảnh màn hình desktop: một góc là deadline/bảng tính, một góc là chú tiểu ngồi im trong điện. Đây là dạng nội dung đồng cảm (relatable) của dân văn phòng, lan trên Threads Việt và Hàn, và là bằng chứng usage thật chứ không chỉ tò mò.
7. **Devlog/sập server như serial** — xem 5.1: thông báo quá tải, nâng sức chứa 20 → 10.000 chỗ được đăng nối tiếp như một câu chuyện khởi nghiệp trực tiếp, người xem quay lại Threads của Park để "xem tập tiếp theo".

### 5.3. Bình luận khen — người dùng nói họ được gì

- **Tĩnh thật, "healing" thật**: *"thật sự yên tĩnh, rất thích"*, *"nhờ đó nằm trong phòng vẫn làm 108 lạy, thấy được chữa lành"*, *"ghé vào nhiều lần trong ngày để ngồi một lát"* (phản hồi Threads do Yonhap dẫn).
- **Không theo đạo vẫn vào được**: nhiều người tự nhận không tôn giáo, cả tín đồ Tin Lành/Công giáo, vẫn thấy tâm trạng dịu lại — tính mở, không đòi đức tin là điểm được khen lặp lại.
- **Lần đầu trong đời "đi chùa"**: một người viết sáng đi làm ghé vào để giữ bình tĩnh và đó là lần đầu tiên họ đi chùa (dù là online).
- **Thân thiện với người hướng nội**: *"lần đầu tiên dám ngồi hàng đầu"*; ngồi cạnh người lạ mà không phải bắt chuyện là câu khen cốt lõi, xuất hiện ở cả báo Hàn, Việt, Đài.
- **Dùng như bạn đồng hành nền**: định mở trang để "ngồi cùng" trong lúc làm việc — nhu cầu đồng hiện diện thụ động giống video "study with me".

### 5.4. Bình luận chê / phàn nàn — và cách Park xử lý công khai

| Phàn nàn | Hệ quả xử lý (đều công khai trên Threads/báo) |
|---|---|
| Hết chỗ: vào từ sáng không còn bồ đoàn, phòng 1.200 người đầy, đứng mãi không tìm được chỗ | Nâng sức chứa liên tục 20 → 100 → 1.200 → 10.000; chia 100 phòng × 100 người |
| Server sập, xếp hàng chờ vào | Xin lỗi + cập nhật tình trạng theo thời gian thực; biến thành devlog được follow (5.1) |
| **Tiếng mõ dùng chung quá ồn** | **Gỡ mõ chung, đổi thành mõ riêng cho từng người** + cơ chế chống chồng âm |
| Hai người ngồi chồng lên một bồ đoàn (lỗi) | Chặn lại: 1 bồ đoàn/1 người thành luật cứng của hệ thống |
| Đồ họa đơn giản, điều khiển không có gì sâu; âm thanh mặc định tắt phải tự bật; kỳ vọng hiệu ứng sẽ thấy "nhạt" | Park không chạy theo hướng thêm hiệu ứng; báo trải nghiệm nhận xét sự "nhạt" này hợp với nhu cầu ngồi vài phút rồi đi — nhưng đây là giới hạn giữ chân dài hạn chưa có lời giải |
| Chi phí server / bài toán tiền: thêm quảng cáo hay gói phí có thể phá vỡ cảm giác "nơi này không đòi hỏi gì ở mình" | Mở "cúng gạo" tự nguyện theo đề nghị của chính người dùng; chưa có mô hình thu bền vững |
| **Lo ngại tôn giáo bị giải trí hóa**: xã luận Hyunbul News (báo Phật giáo Hàn) cảnh báo nếu Phật giáo chỉ được tiêu thụ như "hình ảnh đẹp" thì chỉ là trào lưu nhất thời; chuyên gia Việt cũng cảnh báo nghi lễ biến thành nút bấm/điểm số dễ làm mê cơ chế game hơn là bình tâm; có người dùng Việt xóa app ngay hôm sau vì thấy mất trang nghiêm | Chưa có giải pháp chính thức; ranh giới này là rủi ro thương hiệu dài hạn của cả làn sóng, không riêng Sansa |

### 5.5. Tính năng người dùng yêu cầu — backlog do cộng đồng viết

Đây là phần "vàng" cho dự án chợ: cộng đồng Sansa không chỉ dùng, họ **đề xuất tính năng cụ thể** và Park làm theo công khai:

1. **Xin được đóng góp tiền duy trì server** → sinh ra tính năng "cúng gạo". (Người dùng xin trả tiền trước khi sản phẩm nghĩ ra cách thu tiền.)
2. **Thêm chỗ ngồi / ổn định server** — yêu cầu áp đảo giai đoạn đầu, được đáp ứng bằng nâng cấp hạ tầng công khai.
3. **Tapdori** — đi vòng quanh tháp (nghi thức đi nhiễu tháp) bản ảo (Korea Times dẫn các đề xuất "đổ về" Park).
4. **Jukbi** — tùy chọn để nhà sư gõ thước trúc (gậy thiền dùng trong thiền tông) vào người dùng — yêu cầu kiểu "thêm tương tác có tính nghi thức và hơi hài".
5. **Thêm âm thanh** ngoài Bát Nhã Tâm Kinh, **cải thiện mõ và tràng hạt**, **mở rộng bản đồ chùa** — Park công bố roadmap đúng theo ba ý này.
6. **Sự kiện theo mùa**: treo đèn lồng mùa thi đại học, đi dạo, thả đèn lồng theo mùa; bản App Store — kỳ vọng "có cái mới để quay lại".
7. Người dùng tự tạo cách chơi ngoài thiết kế: tự đặt kỳ vọng 108 lạy mỗi ngày, dùng chùa như phòng ngồi cùng khi làm việc, tổ chức "quẩy" ở Sân Trăng — tức **tính năng tốt nhất đôi khi là hành vi cộng đồng tự phát được sản phẩm chừa đất cho nó xảy ra**.

### 5.6. Bài học riêng từ làn sóng social cho Chợ Hòa Bình 3D

- **Thiết kế sẵn "khoảnh khắc chụp được"**: Sansa có chính điện đông nghẹt; chợ cần tương đương — ví dụ khung giờ chợ đêm lên đèn kín người, cảnh chen mua một sạp hot, hàng người xếp hàng trước một quán ăn nổi tiếng trong chợ. Đông đúc nhìn thấy được = nội dung tự lan.
- **Cho mỗi người một "pháp danh chợ"**: tên ngẫu nhiên thơ/hài kiểu "Khách mối của sạp rau", "Người trả giá một lần là mua" — rẻ, cá nhân hóa, ai cũng có ảnh để khoe.
- **Chừa một zone ngược mood**: Sân Trăng/DJ zone là van xả hài hước của một không gian nghiêm túc. Ở chợ: một góc nhạc sống/biểu diễn đường phố theo giờ, hoặc khu "chợ đêm" đổi mood hoàn toàn so với chợ ngày.
- **Vận hành công khai như một kênh nội dung**: mở Threads/TikTok của dự án và đăng devlog — hôm nay thêm sạp nào, sập/quá tải thì xin lỗi kiểu hài, công bố mốc khách thứ N. Người ta follow quá trình, không chỉ sản phẩm.
- **Biến phàn nàn thành tính năng công khai và nhanh**: mõ ồn → mõ riêng là câu chuyện được báo kể lại như điểm cộng. Ở chợ: phản hồi nào xử lý được trong ngày thì xử lý và đăng bài cảm ơn người góp ý (gắn tên họ) — đó là retention + PR cùng lúc.
- **Đừng sợ meme về chính mình**: xếp hàng/hết chỗ là lỗi, nhưng là lỗi chứng minh "đông khách". Thiết kế chợ nên có hàng quán giới hạn số suất/ngày để khan hiếm xảy ra thật — và để cộng đồng đùa về nó.
- **Nội dung phái sinh là kênh miễn phí**: guide, blog "cách đi chợ", clip của người dùng tự quay... Muốn có lớp này, sản phẩm phải có đủ chi tiết lạ để người ta viết guide (giờ mở sạp, món ẩn, đường tắt trong chợ).

## 6. Bài học áp dụng cho Chợ Hòa Bình 3D — Đà Lạt

Chợ khác chùa ở một điểm căn bản: **chùa giữ người bằng tĩnh, chợ phải giữ người bằng náo nhiệt, mùi vị và mua bán**. Học cấu trúc của Sansa, đừng chép nội dung của nó:

1. **Cắt ma sát ở cửa vào**: mở link là đứng giữa chợ — không đăng ký, không tạo nhân vật cầu kỳ. Gán sẵn một avatar khách đi chợ + một cái tên vui ngẫu nhiên kiểu Sansa ("Người đi chợ không mua gì", "Tín đồ dâu tây"...). Đây cũng là "món" để chụp khoe.
2. **Bản đồ nhỏ, khu vực ít, mỗi khu một mood một hành động**: cổng chợ / khu chợ đêm / khu đặc sản / khu ăn uống... Mỗi khu đúng 1–2 hành động chủ đạo (ở chùa là lạy/tràng hạt; ở chợ là: xem sạp, chọn món, ăn/uống tại chỗ, mua mang về). Đừng tham nhiều tính năng trong một khu.
3. **Một hành động lặp có đếm, làm "nghi thức" của chợ**: tương đương 108 hạt — ví dụ đi đủ X sạp, ăn đủ Y món trong "hộ chiếu ẩm thực chợ", sưu tầm con dấu từng khu. Cho tiến trình nhìn thấy được nhưng giữ nhẹ, tránh biến chợ thành game nhiệm vụ nặng.
4. **Đồng hiện diện không chat chữ**: giữ công thức "đi chợ cùng nhau mà không phải nói gì" — giao tiếp bằng cử chỉ (vẫy tay, giơ món vừa mua, thả tim) + thông báo nhẹ ("X vừa mua một ly sữa đậu nành nóng"), thay vì ô chat. Chợ đông người thật nhìn thấy được là bằng chứng sống còn của dự án.
5. **Phòng/shard ngay từ đầu**: thiết kế sẵn mô hình nhiều "phiên chợ" (phòng) tối đa ~100 người/phòng như Thanh Liên Đường, có occupancy và phòng đầy chọn phòng khác. Hạ tầng phải tính trước kịch bản viral, đừng để sập mới nâng như Sansa.
6. **Giờ hẹn chung thay cho lễ 05:00/18:00**: chợ có nhịp thật còn đẹp hơn — "chợ lên đèn" buổi tối, giờ mở hàng ăn sáng, phiên chợ đêm cuối tuần, giờ biểu diễn nhạc ở quảng trường Hòa Bình. Hai mốc giờ cố định mỗi ngày là đủ tạo thói quen quay lại đúng giờ.
7. **Âm thanh theo khu, có mute riêng**: tiếng rao hàng/khu ăn uống, tiếng nhạc khu quảng trường, tiếng mưa Đà Lạt... tách kênh như Sansa tách tụng kinh/môi trường/nhạc sân. Âm thanh là một nửa của cảm giác "đang ở chợ thật".
8. **Nhân vật thường trú để chợ không bao giờ vắng**: tiểu thương NPC đứng sạp, vài khách quen đi lại — kể cả 3h sáng mở vào cũng thấy chợ "sống", đúng bài học resident characters của Sansa.
9. **Tiền: học cả thành công lẫn bài toán dở của Sansa**. "Cúng gạo" chạy được vì nó khớp văn hóa của không gian và do người dùng xin trước. Ở chợ, cơ chế khớp văn hóa sẵn có là **mua bán thật**: bán đồ ăn/nước uống trong chợ (đặt món ảo gắn đơn thật/voucher) — đừng đợi viral xong mới nghĩ cách thu tiền và đừng phá mood bằng quảng cáo chen ngang.
10. **Chừa đất cho hành vi tự phát**: Sân Trăng sinh ra điệu nhảy tập thể ngoài ý đồ. Ở chợ, chừa một khoảng sân/khu trống có nhạc và cử chỉ vui để cộng đồng tự chế ra "nghi thức" của riêng họ — đó mới là thứ quay clip lan truyền được.
11. **Vận hành minh bạch kiểu Park**: tác giả xuất hiện bằng tên thật, đăng devlog, sửa lỗi theo phản hồi ngay trên Threads. Với dự án cá nhân/indie, "người làm ra nó" là một phần của sản phẩm và là kênh marketing rẻ nhất.
12. **Cảnh báo giữ lại**: (a) Số liệu viral của Sansa là tự công bố — đừng lấy làm KPI hứa hẹn; (b) viral 1 tuần ≠ giữ chân 30 ngày — chợ cần lý do quay lại sau khi hết tò mò: hàng quán thay đổi theo ngày/mùa, món giới hạn giờ, sự kiện theo lịch Đà Lạt thật; (c) tránh game hóa quá tay làm mất chất "đi dạo chợ" — điểm/nhiệm vụ chỉ là lớp mỏng phủ lên trải nghiệm tham quan.

## 7. Nguồn tham khảo chính

- Znews — "Cơn sốt 'đi chùa online' lan rộng ở châu Á" (04/11/2026): https://znews.vn/znews-post1693961.html
- VnExpress — "Tác giả 'chùa online' khuấy đảo mạng với 30 phút lập trình AI": https://vnexpress.net/tac-gia-chua-online-khuay-dao-mang-voi-30-phut-lap-trinh-ai-5140379.html
- Lao Động — "Chùa online thu hút 1 triệu lượt truy cập và bài toán kiếm tiền từ AI": https://laodong.vn/van-hoa-giai-tri/chua-online-thu-hut-1-trieu-luot-truy-cap-va-bai-toan-kiem-tien-tu-ai-1793712.ldo
- The Korea Herald — "Finding peace, one click at a time" (qua vietnam.vn): https://www.vietnam.vn/en/ngoi-chua-ao-han-quoc-thu-hut-hon-600-000-luot-truy-cap
- The Korea Times — "AI-built virtual Buddhist temple draws 1 mil. visitors in less than a week": https://www.koreatimes.co.kr/southkorea/20261103/ai-built-virtual-buddhist-temple-draws-1-mil-visitors-in-less-than-a-week
- Asia Business Daily — "Can an 'Online Temple' Built With Vibe Coding Revive the Metaverse…": https://www.asiae.co.kr/en/article/2026110209301323649
- Asia Daily — "Sansa draws 800,000 visits as young Koreans seek…": https://asiadaily.org/news/17149/
- EasyTicket — "Why 600,000 People Visited the Online Temple Sansa, and the Sites That Followed" (trải nghiệm trực tiếp + đối chiếu site phái sinh): https://easyticket.co.kr/en/posts/2026/%EC%98%A8%EB%9D%BC%EC%9D%B8-%EC%A0%88-%EC%82%B0%EC%82%AC-%EB%B9%84%EC%8A%B7%ED%95%AC-%EC%82%AC%EC%9D%B4%ED%8A%B8%EB%93%A4/
- Sansatemple Web Guide (chơi thử, kiểm chứng 31/10/2026) — bố cục, điều khiển, Sân Trăng, giờ lễ, giới hạn kiểm chứng: https://sansatempleweb.com/en/ và https://sansatempleweb.com/en/sources/
- Soha — "Chùa online không cho nói chuyện, 100.000 người trẻ chen nhau vào ngồi" (số liệu Threads, phản hồi người dùng, DJ NewJeansNim, xã luận Hyunbul News): https://soha.vn/con-sot-dang-hot-nhat-tren-mxh-chua-online-khong-cho-noi-chuyen-100000-nguoi-tre-han-quoc-van-chen-nhau-vao-ngoi-198261030185924395.htm
- CafeBiz — "Chân dung chàng trai 26 tuổi khiến hàng nghìn người rủ nhau 'đi chùa online'" (phản hồi Threads, blog guide phái sinh): https://cafebiz.vn/chan-dung-chang-trai-26-tuoi-khien-hang-nghin-nguoi-ru-nhau-di-chua-online-dan-ngoai-ngu-that-nghiep-khong-theo-dao-phat-176261101130406376.chn
- Điện tử Ứng dụng — "Đi chùa online: Người trẻ tìm kiếm điều gì sau một cú chạm màn hình?" (bình luận hài trên MXH Việt, ý kiến chuyên gia): https://dientuungdung.vn/di-chua-online-nguoi-tre-tim-kiem-dieu-gi-sau-mot-cu-cham-man-hinh-19389.html
- Advertising Vietnam — "'Đi chùa online' thương hiệu học được gì từ hiện tượng này?" (phân tích funnel/retention/gamification, cảnh báo vận hành): https://advertisingvietnam.com/article/di-chua-online-thuong-hieu-hoc-duoc-gi-tu-hien-tuong-nay
- POPBEE — "Viral Korean Online Worship! sansatemple Virtual Temple and inpeace Online Church" (cơ chế xếp hàng, lan trên Threads Đài Loan): https://popbee.com/en/lifestyle/korea-virtual-temple-sansatemple-inpeace
- LTN (Đài Loan) — "10萬人湧入線上佛堂 排隊轉佛珠擠爆伺服器" (meme xếp hàng, mõ chung → mõ riêng): https://art.ltn.com.tw/article/breakingnews/5625358
- Báo Mới — "Cơn sốt 'chùa trực tuyến' không ô chat…" (meme xếp hàng tịnh tâm trên Threads/TikTok/Facebook tại Việt Nam): https://baomoi.com/con-sot-chua-truc-tuyen-khong-o-chat-hang-tram-nghin-nguoi-tre-chen-chan-tim-su-tinh-lang-c56413681.epi
- Thị trường Hàng hóa — "Cơn sốt đang hot nhất trên MXH…" (bài Threads Việt 152.000 view/8.600 like, lượt thích các bài của Park trên Threads): https://www.thitruonghanghoa.com/tin-tuc/con-sot-dang-hot-nhat-tren-mxh-chua-online-khong-cho-noi-chuyen-100000-nguoi-tre-han-quoc-van-chen-nhau-vao-ngoi-360895.html
