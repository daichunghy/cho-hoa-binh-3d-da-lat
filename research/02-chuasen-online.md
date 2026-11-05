# Nghiên cứu Chùa Sen Online — tham khảo cho Chợ Hòa Bình 3D Đà Lạt

> Ngày nghiên cứu: 05/11/2026. Phương pháp: `browser.search` + `browser.open` đọc trực tiếp các trang chính thức của Chùa Sen và video của người sáng tạo. Chỉ nghiên cứu, không đăng nhập / không vào phòng 3D trực tiếp bằng trình duyệt thật — các mô tả tính năng dưới đây dựa trên trang hướng dẫn, nội quy, trang tính năng chính thức (cập nhật 04/11/2026) và video hậu trường của tác giả, có ghi rõ chỗ nào là suy luận.

## 0. Lưu ý quan trọng về tên miền

- Chung Hy nhắc tên **chuasen.online** — nhưng khi thử truy cập, tên miền này **không phân giải / không mở được** (`browser.open` báo lỗi không có URL công khai truy cập được).
- Site đang hoạt động thật mà mọi nguồn đều trỏ về là **chuasen.com** — "Chùa Sen Online". Trang hướng dẫn, nội quy và video của chính tác giả (Ben / benpiaz) đều ghi "vào Chùa Sen Online: https://chuasen.com/".
- **Bài học ngay từ đầu cho Chợ Hòa Bình:** chốt 1 tên miền chính duy nhất, mọi kênh mạng xã hội / video / bài SEO đều trỏ về đúng 1 địa chỉ, tránh loãng và tránh người khác chiếm tên tương tự (xem mục 8 về TikTok — đã có tài khoản trùng tên "Chùa Sen Online" livestream mà không rõ có phải chính chủ hay không).

## 1. Tổng quan

- **Chùa Sen (chuasen.com)** là một **ngôi chùa 3D chạy ngay trên trình duyệt** (web, không cài app, không bắt buộc đăng ký), nơi nhiều người cùng vào một "phòng" chùa để niệm Phật, tụng kinh, thiền, thắp hương, thỉnh chuông, thả đèn hoa đăng.
- Tự định vị rất rõ trong nội quy: *"không gian chùa 3D trên trình duyệt để mọi người cùng niệm Phật, tụng kinh và thiền; đây là dự án phần mềm độc lập, không phải chùa thật hay tổ chức tôn giáo"* — và **miễn phí, không quảng cáo, không có tính năng / trang phục / thứ hạng nào phải trả tiền**.
- Bối cảnh ra đời: ăn theo làn sóng "đi chùa online" từ **Sansa** (Hàn Quốc, của Park Jin-won — 600.000 lượt trong 3 ngày, 1 triệu người dùng trong tuần đầu, lan qua Threads/Instagram). Chùa Sen là phiên bản Việt hóa, nhiều tính năng hơn Sansa: có cấp độ, nhiệm vụ tu tập, nhiều không gian phụ.
- Tác giả: cá nhân (Ben — benpiaz), công khai quá trình làm bằng **vibe coding với Claude** (video YouTube "Mình Vibe Coding với Opus 5.5 đốt hơn 5,400$ API để tạo ra Chùa Sen Online", cắt từ livestream 2 giờ 15 phút) — chính câu chuyện "người không biết code làm chùa 3D bằng AI" cũng là một kênh truyền thông cho sản phẩm.

## 2. Tính năng chính

### 2.1. Nhân vật & vào chùa (onboarding)
- Vào thẳng từ trình duyệt, **không cần đăng ký, không cần cài đặt**.
- Tạo nhân vật: nhập **pháp danh** (tên hiển thị — bị kiểm duyệt theo nội quy: không tục tĩu, không quảng cáo, không giả danh), chọn **giới tính, kiểu áo, màu áo** → bấm "Vào chùa".
- Đăng nhập là **tùy chọn**, chỉ để lưu nhân vật + Hành trình + thống kê công phu lên mạng và dùng lại trên máy khác. Không đăng nhập vẫn chơi đầy đủ.
- Có thể **cài lên màn hình chính như app (PWA)** từ hộp thoại Cài đặt.

### 2.2. Không gian (cấu trúc chùa)
Theo trang hướng dẫn và các trang tính năng, khuôn viên gồm:
- **Cổng tam quan** — điểm bắt đầu, tạo cảm giác "bước qua cổng" rất rõ.
- **Sân chùa + ao sen** — không gian mở để đi dạo, thả đèn hoa đăng trên ao.
- **Gác chuông** — thỉnh chuông, người cùng phòng cùng nghe tiếng chuông.
- **Chánh điện** — tượng Phật, hàng **bồ đoàn**; đến gần bồ đoàn bấm "Ngồi xuống" thì **bảng công phu** mới mở ra ở thanh dưới màn hình.
- **Cây bồ đề** — treo lời nguyện bằng dải lụa (người khác chỉ thấy dải lụa ẩn danh, tồn tại ~6 giờ).
- Các điểm phụ được làm thành trang riêng: **sân thiền (ngồi thiền ngoài trời), tượng Quan Âm, thả đèn hoa đăng ở ao sen**…

### 2.3. Hoạt động tu tập (core loop)
- **Thắp hương** ở lư hương (nút ngữ cảnh hiện khi đến gần; PC bấm phím F).
- **Thỉnh chuông** ở gác chuông — âm thanh phát cho cả phòng.
- **Lạy Phật** trước tượng Phật trong chánh điện.
- **Ngồi bồ đoàn → chọn công phu** trên thanh công phu: **Tràng hạt** (lần từng hạt, PC bấm Space/Enter cho mỗi hạt), **Tụng kinh** (có tiếng mõ), **Thiền**.
- **Dâng hoa**; **Thả đèn hoa đăng**: viết lời nguyện (tùy chọn, tối đa 120 ký tự — **chỉ lưu local trên máy người dùng**, không gửi lên mạng), chọn 1 trong 6 ý nguyện (Cầu an, Cầu siêu, Sức khỏe, Gia đạo, Học hành · thi cử, Tùy tâm) → đèn hoa sen nổi trên ao, trôi chậm rồi tắt dần; người cùng phòng chỉ thấy đèn ẩn danh có màu theo ý nguyện.
- **Hồi hướng**: kết thúc buổi bằng Kệ Hồi Hướng 4 câu — một "nghi thức đóng phiên" rõ ràng.
- **Lời chào preset thay cho chat**: Chắp tay, "A Di Đà Phật", "Tùy hỷ", "Chúc bình an"… **Không có chat tự do.**

### 2.4. Gamification giữ chân — hệ "Hành trình"
- Có **cấp độ Hành trình**: tính năng được **mở khóa dần theo cấp** — ví dụ Thỉnh chuông + Dâng hoa mở từ **cấp 2**, Thả đèn hoa đăng mở từ **cấp 3**. Người mới muốn dùng ngay vẫn có đường tắt: bật "Hiện đủ mọi tính năng" trong Cài đặt (không khóa cứng — tôn trọng người dùng).
- Hiển thị xã hội nhẹ: người cùng phòng thấy **cấp Hành trình, huy hiệu và "ngọn đèn tinh tấn"** của nhau (ẩn được trong Cài đặt).
- **Thống kê công phu** được lưu lại qua các lần vào (nhân vật và công phu "vẫn được giữ cho lần sau" kể cả khi chỉ đóng tab trình duyệt).
- Nội dung theo lịch: **lịch âm hôm nay, ngày rằm / mùng một, ngày lễ Phật giáo, cách lễ Phật tại nhà, cách đi chùa ngày rằm** — lý do quay lại theo chu kỳ âm lịch.

## 3. Thiết kế giao diện / trải nghiệm (UX)

- **Điều khiển đa cách, ưu tiên chạm**: 
  - Mobile: **joystick ảo nửa trái màn hình** (bật sẵn), vuốt nửa phải để nhìn quanh, pinch zoom, **chạm lên sàn để nhân vật tự đi tới**, chạm vào vật (bồ đoàn, lư hương, chuông…) để tự đi tới đó.
  - PC: WASD / phím mũi tên, click sàn để đi, giữ chuột để đi theo con trỏ, kéo chuột hoặc Q/E để xoay, lăn chuột zoom, **F / Enter để tương tác**, chế độ toàn màn hình có tâm ngắm giữa màn hình.
  - Có tùy chọn tắt joystick, đảo chiều kéo kiểu Street View.
- **Nút ngữ cảnh theo vị trí (contextual actions)** là mẫu UX cốt lõi: nút "Ngồi xuống / Thắp hương / Thỉnh chuông / Lạy Phật" **chỉ hiện khi đứng gần vật tương ứng** → giao diện luôn gọn, người mới không bị ngợp menu.
- **Menu "Thêm" phân nhóm** (nhóm Dâng lễ, Thêm nữa…) để chứa tính năng phụ mà không phá vỡ màn hình chính.
- **Thanh công phu dưới đáy màn hình** chỉ xuất hiện đúng lúc (sau khi ngồi bồ đoàn) — UI theo trạng thái, không phô bày tất cả cùng lúc.
- **Kiểm duyệt bằng thiết kế**: không chat tự do → không spam / không toxic; tên hiển thị bị lọc từ cổng; nội quy cấm bot, cấm chiếm bồ đoàn, cấm bấm chuông / lời chào liên tục làm phiền người khác → giữ được không khí yên tĩnh vốn là "sản phẩm" chính.
- **Riêng tư làm thành tính năng**: lời nguyện chỉ lưu local, người khác chỉ thấy biểu tượng ẩn danh (đèn / dải lụa có màu) — vừa an toàn vừa tạo tò mò xã hội nhẹ.

## 4. Âm thanh / hình ảnh

- **Âm thanh là một nửa trải nghiệm**: tiếng **chuông** (đồng bộ cả phòng khi một người thỉnh), tiếng **mõ** khi tụng kinh, nhạc / tiếng tụng — trang hướng dẫn khuyên "nên bật âm thanh và giữ màn hình sáng khi thiền để nghe chuông đúng giờ", có **thanh Âm lượng trong Cài đặt**.
- Âm thanh mang tính **sự kiện xã hội**: hành động của một người (thỉnh chuông) trở thành trải nghiệm chung của cả phòng → cảm giác "đang ở cùng nhau" mà không cần chat.
- Hình ảnh (qua mô tả chính thức và video tác giả): chùa 3D phong cách đơn giản, sáng, nhiều sen / nước / cây xanh; nhân vật đồng nhất một kiểu (áo tu, khác màu áo) giúp phòng đông vẫn dễ đọc, không rối. Đây là hướng "đồ họa nhẹ — chạy mượt trên điện thoại" giống Sansa, không đua photoreal.

## 5. Flow người dùng (tóm tắt hành trình)

1. Mở chuasen.com → 2. Tạo nhân vật (pháp danh + áo) → 3. Vào chùa, bước qua cổng tam quan → 4. Dạo sân, ngắm ao sen → 5. Thắp hương → 6. Thỉnh chuông / dâng hoa (cấp 2) → 7. Vào chánh điện, lạy Phật → 8. Ngồi bồ đoàn → 9. Chọn công phu: tràng hạt / tụng kinh / thiền → 10. Ra ao sen thả đèn hoa đăng + viết nguyện (cấp 3), treo nguyện ở cây bồ đề → 11. Hồi hướng, kết thúc → 12. Đóng tab, dữ liệu công phu + Hành trình được giữ → quay lại vào rằm / mùng một / ngày lễ để tiếp tục lên cấp.

Điểm đáng chú ý: flow có **điểm bắt đầu nghi thức (qua cổng)**, **đỉnh trải nghiệm (ngồi công phu trong chánh điện)**, **điểm kết nghi thức (hồi hướng)** và **vòng lặp quay lại (cấp độ + lịch âm)** — đủ 4 lớp như một buổi đi chùa thật rút gọn trong vài phút.

## 6. Điểm giữ chân (retention)

1. **Cấp độ Hành trình + mở khóa tính năng theo cấp** — lý do quay lại cụ thể, nhìn thấy tiến bộ.
2. **Thống kê công phu tích lũy** — công sức đã bỏ ra nằm lại trong tài khoản / máy, bỏ thì tiếc.
3. **Hiện diện xã hội không áp lực**: thấy người khác đang ngồi thiền / niệm cùng phòng, thấy cấp + huy hiệu + đèn tinh tấn của nhau, nhưng **không chat, không cạnh tranh** — "ngồi cùng nhau mà không nói gì" chính là giá trị cốt lõi học từ Sansa.
4. **Sự kiện theo lịch âm**: rằm, mùng một, Vu Lan, Phật Đản… tạo nhịp quay lại tự nhiên, không cần push notification gượng ép.
5. **Nghi thức cá nhân hóa có tính share / lưu niệm**: đèn hoa đăng mang màu ý nguyện, dải lụa trên cây bồ đề tồn tại 6 giờ.
6. **Ma sát bằng 0**: không cài, không bắt đăng nhập, vào là chơi; PWA để "cài như app" cho người quay lại thường xuyên.
7. **Cụm nội dung SEO quanh site** (mục 7) kéo người mới vào liên tục từ Google.

## 7. Kỹ thuật & vận hành (từ video hậu trường của tác giả)

- Xây bằng **vibe coding với Claude (Opus)**, nhiều agent chạy song song; tác giả công khai cả chi phí API (hơn 5.400 USD theo tiêu đề video) — minh bạch quá trình làm cũng là nội dung marketing.
- Khi tính chi phí realtime cho 100 / 1.000 / 5.000 người chơi, tác giả chọn **phương án rẻ nhất trên Cloudflare** cho server realtime.
- Test tải bằng **phòng 50 bot**, và tối ưu hiệu năng kiểu game online: **chỉ hiện tên 10 người gần nhất** để không lag khi phòng đông.
- Mô hình kinh tế: **miễn phí hoàn toàn, không quảng cáo, không bán vật phẩm** (ghi rõ trong nội quy) — đổi lại là tốc độ lan truyền và uy tín; chi phí server do tác giả tự chịu. Đây là điểm Chợ Hòa Bình **không nên sao chép nguyên xi** vì chợ của Chung Hy có mục tiêu bán đồ ăn / đồ lưu niệm (xem mục 9).

## 8. Chùa Sen trên mạng xã hội (Threads / TikTok / Facebook)

> Mục bổ sung theo yêu cầu của Chung Hy. Tìm bằng `browser.search` ngày 05/11/2026 với các từ khóa kèm "TikTok", "Threads", "Facebook", "chuasenonline", "benpiaz". Kết quả phân biệt rõ 3 lớp: (a) kênh của chính tác giả, (b) tài khoản trùng tên chưa xác minh được chủ sở hữu, (c) làn sóng "chùa online" nói chung (Sansa) — không gộp chung.

### 8.1. TikTok — có tài khoản trùng tên, đang livestream, CHƯA rõ chính chủ
- Tìm thấy nhiều trang LIVE của **hai tài khoản TikTok tên `@chuasenonline` và `@chuasenonline2`**, tiêu đề kiểu *"Chùa Sen Online is LIVE"*, mô tả ngắn *"Nam Mô A Di Đà Phật"*, *"Đi Chùa Sen Online"*; mỗi kết quả là một phòng live khác nhau (room_id khác nhau), vùng chia sẻ VN, dữ liệu crawl mới trong 3–4 ngày gần đây → các tài khoản này **livestream khá thường xuyên**.
- Nhiều link live có tham số **`tt_from=facebook` / `utm_source=facebook`** → link live được **chia sẻ qua lại từ Facebook sang TikTok**.
- **Điều chưa xác minh được:** không có bằng chứng trong kết quả tìm kiếm cho thấy hai tài khoản TikTok này thuộc về tác giả chuasen.com (Ben/benpiaz). Với bối cảnh trend "đi chùa online / phóng sinh online" trên TikTok mà báo chí và công an đã cảnh báo (livestream nhận quà tặng), khả năng đây là **người khác mượn tên "Chùa Sen Online" để livestream** là hoàn toàn có thể. **Trong báo cáo này chỉ ghi nhận "có tài khoản trùng tên đang hoạt động", không khẳng định là kênh chính thức.**

### 8.2. Threads — KHÔNG tìm thấy bài về Chùa Sen; Threads là nơi Sansa (bản gốc Hàn) bùng nổ
- Tìm với từ khóa "Chùa Sen Online / chuasen.com + Threads": **không ra bài Threads nào về Chùa Sen**.
- Những gì ra được đều về **Sansa**: Park Jin-won **ra mắt Sansa ngay trên Threads và Instagram**; bài thông báo sự cố server trên Threads đạt ~7.100 lượt thích; một bài Threads tiếng Việt đùa về cảnh chính điện chật kín chú tiểu đạt **152.000 lượt xem, 8.600 lượt thích sau 7 giờ**; bình luận Threads được báo chí dẫn lại ("thực sự rất yên tĩnh và dễ chịu", "nằm ở nhà thực hiện 108 lạy"…).
- → Bài học: trong hệ sinh thái này, **Threads là kênh "kể câu chuyện + khoe ảnh chụp màn hình cảnh đông người"** hiệu quả nhất, và Chùa Sen (bản Việt) dường như **chưa khai thác Threads** — khoảng trống mà Chợ Hòa Bình có thể chiếm trước.

### 8.3. Facebook — KHÔNG tìm thấy fanpage / bài đăng riêng về Chùa Sen
- Tìm "Chùa Sen online + Facebook": **không thấy fanpage hay bài đăng Facebook nào về chuasen.com**. Kết quả chỉ gồm: (i) các link TikTok live được chia sẻ từ Facebook (mục 8.1); (ii) ở phần mô tả video YouTube, tác giả để **Facebook cá nhân (/hieuthien1407)** và Instagram (/benpiaz) của mình, cộng đồng Facebook được nhắc trong một video khác là nhóm OpenClaw VN — tức Facebook với tác giả là **kênh cá nhân / cộng đồng sẵn có**, không phải fanpage sản phẩm.
- Kênh truyền thông công khai rõ nhất của Chùa Sen thực ra là **YouTube của tác giả** (loạt video vibe coding, livestream quá trình làm, cộng đồng Telegram benpiaz) + **cụm bài SEO trên chính chuasen.com**.

### 8.4. Kết luận mạng xã hội
- **Tìm thấy:** TikTok có tài khoản trùng tên "Chùa Sen Online" livestream thường xuyên (chưa rõ chính chủ) và được share từ Facebook; tác giả dùng YouTube + Telegram + Facebook/Instagram cá nhân để kể quá trình làm.
- **Không tìm thấy:** bài Threads về Chùa Sen; fanpage Facebook của Chùa Sen; chiến dịch social chính thức nào cho chuasen.com ngoài video của tác giả.
- Nói cách khác: Chùa Sen lan chủ yếu nhờ **(1) ăn theo sóng Sansa trên báo chí MXH, (2) SEO Google bằng cụm bài hướng dẫn / kiến thức, (3) video hậu trường "làm bằng AI"** — chứ không nhờ hệ thống kênh social của riêng sản phẩm. Đây vừa là điểm yếu của họ, vừa là cơ hội cho Chợ Hòa Bình: làm social bài bản ngay từ đầu (Threads khoe cảnh chợ đông, TikTok live cảnh chợ đêm, Facebook cho nhóm tiểu thương / cộng đồng địa phương) là vượt được họ ở mảng này.

## 9. Bài học áp dụng cho Chợ Hòa Bình 3D Đà Lạt

| Mẫu của Chùa Sen | Áp dụng vào Chợ Hòa Bình |
|---|---|
| Vào ngay trên trình duyệt, không cài, không bắt đăng ký; đăng nhập chỉ để lưu tiến trình | Giữ nguyên: khách tham quan vào chợ trong <10 giây; tài khoản chỉ cần khi lưu "hành trình đi chợ", giỏ hàng, đơn ăn uống |
| Tạo nhân vật + chọn trang phục ngay đầu phiên | Cho chọn avatar + outfit đi Đà Lạt (áo len, khăn choàng, mũ len…) — vừa là onboarding vừa là gợi ý bán đồ thật sau này |
| Cổng tam quan = điểm bắt đầu nghi thức | **Cổng chợ / vòng xoay Khu Hòa Bình** = điểm check-in bắt đầu hành trình; qua cổng là vào "phiên chợ" |
| Nút ngữ cảnh chỉ hiện khi đến gần vật | Đến gần quầy thì hiện nút theo quầy: "Xem món", "Nghe cô bán hàng giới thiệu", "Mua thử", "Chụp ảnh" — UI chợ luôn gọn dù có hàng chục quầy |
| Điều khiển: joystick trái + vuốt nhìn + chạm sàn để tự đi; PC: WASD + click-to-move + F tương tác | Sao chép gần như nguyên bộ điều khiển này cho mobile/PC — đã được Chùa Sen kiểm chứng với người dùng Việt không rành game |
| Không chat tự do, chỉ lời chào preset + lọc tên hiển thị | Chợ cũng nên dùng **câu chào / biểu cảm preset** ("Ngon quá!", "Bớt chút đi cô") thay chat tự do ở bản đầu: tránh spam, giữ vui, đúng chất chợ mà an toàn kiểm duyệt |
| Âm thanh sự kiện chung cả phòng (thỉnh chuông ai cũng nghe) | Âm thanh chợ sống: tiếng rao, tiếng xèo xèo bánh tráng nướng, nhạc chợ đêm… khi có sự kiện (mở phiên chợ đêm, đếm ngược…) thì phát cho cả khu |
| Hệ "Hành trình" mở khóa tính năng theo cấp 2, 3 + huy hiệu + thống kê tích lũy | Làm **"Hành trình đi chợ"**: cấp 1 dạo chợ ngày, cấp 2 mở **chợ đêm Hòa Bình**, cấp 3 mở khu ẩm thực / đặc sản; huy hiệu kiểu "Đã ăn 5 món Đà Lạt", sổ tích lũy món đã thử / quầy đã ghé — thay cho thống kê công phu |
| Lời nguyện chỉ lưu local, người khác thấy biểu tượng ẩn danh | Áp dụng cho tính năng nhạy cảm tương tự: "gửi lời nhắn / treo điều ước ở cây thông chợ" — nội dung riêng tư lưu local, người khác chỉ thấy đèn / thẻ ẩn danh |
| Cụm bài SEO quanh sản phẩm (hướng dẫn, lịch âm, ý nghĩa từng nghi thức…) + CTA "Vào chùa ngay" ở mọi trang | Làm cụm bài quanh **từng quầy / món / góc chợ**: "Bánh tráng nướng Đà Lạt ăn ở đâu trong chợ", "Chợ đêm Hòa Bình mở mấy giờ", "Đi chợ Hòa Bình 3D: hướng dẫn dạo chợ online"… mỗi bài 1 CTA "Vào chợ ngay" |
| Sự kiện theo lịch (rằm, mùng một, lễ) | Lịch sự kiện chợ: **phiên chợ đêm cuối tuần, lễ hội hoa, mùa dâu / mùa hồng giòn, Noel – Tết** ở Đà Lạt — tạo nhịp quay lại theo mùa thay vì theo âm lịch |
| Chỉ hiện tên 10 người gần nhất, test bằng bot, server realtime rẻ (Cloudflare) | Ghi vào yêu cầu kỹ thuật ngay từ đầu: giới hạn hiển thị người/tên quanh avatar, test tải bằng bot trước khi mở public, ưu tiên hạ tầng realtime chi phí thấp |
| Minh bạch "không phải chùa thật", miễn phí hoàn toàn | Chợ Hòa Bình nên ghi rõ là **mô hình 3D tham quan / giải trí lấy cảm hứng từ khu Hòa Bình – chợ Đà Lạt thật**, không mạo nhận là kênh chính thức của chợ hay của thành phố |

**Khác biệt cốt lõi cần giữ:** Chùa Sen cố tình **không bán gì** để giữ sự thanh tịnh và lan truyền; Chợ Hòa Bình của Chung Hy thì ngược lại — **hàng quán và mua đồ ăn / nước uống / đặc sản chính là linh hồn của chợ**. Vì vậy chỉ học Chùa Sen ở **khung trải nghiệm** (vào nhanh, điều khiển, nút ngữ cảnh, hiện diện xã hội nhẹ, hành trình mở khóa, SEO + social), còn lớp thương mại phải tự thiết kế: quầy hàng có chủ quầy NPC, menu món ăn Đà Lạt (bánh tráng nướng, sữa đậu nành, xiên nướng, dâu, mứt, atiso…), gọi món tại quầy, ăn uống tại bàn trong chợ và mua đặc sản mang về — những thứ một ngôi chùa không bao giờ làm được, và chính là lý do người ta ở lại chợ lâu hơn ở chùa.

## 10. Nguồn đã đọc

- chuasen.com — *Hướng dẫn đi chùa online từng bước* (cập nhật 04/11/2026)
- chuasen.com — *Nội quy Chùa Sen* (cập nhật 04/11/2026)
- chuasen.com — *Thả đèn hoa đăng online: ý nghĩa và cách nguyện* (cập nhật 04/11/2026)
- YouTube (kênh benpiaz) — *Mình Vibe Coding với Opus 5.5 đốt hơn 5,400$ API để tạo ra Chùa Sen Online* và *Vibe Coding: Xây Chùa Online với Claude Opus 5.5*
- TikTok — các trang LIVE của @chuasenonline / @chuasenonline2 (kết quả tìm kiếm, crawl 3–4 ngày trước 05/11/2026)
- Báo chí về Sansa (CafeBiz, Soha, Đời sống & Pháp luật / Người Đưa Tin, aFamily, CafeF, MarketTimes, 01–03/11/2026) — phần Threads / Instagram của Sansa
- Ghi chú: chuasen.online (tên Chung Hy cung cấp) không truy cập được tại thời điểm nghiên cứu; mọi dữ kiện trên thuộc về chuasen.com.
