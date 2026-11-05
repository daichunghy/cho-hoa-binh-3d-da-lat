# 08 — Gamification & Giữ chân người dùng trong thế giới ảo tham quan / cozy games
### Bài học thiết kế cho Chợ Hòa Bình 3D — Đà Lạt

- **Phạm vi:** cơ chế quest theo ngày, hộ chiếu đóng dấu, sưu tầm, thành tựu, sự kiện theo giờ/mùa, cá nhân hoá avatar — trong các thế giới ảo tham quan và cozy games.
- **Mục tiêu áp dụng:** người vào Chợ Hòa Bình 3D thấy thú vị ngay trong 5 phút đầu, có lý do đi hết chợ trong phiên đầu, và có lý do *tự nguyện* quay lại vào ngày khác / giờ khác / mùa khác — mà không cần cơ chế ép buộc gây mệt mỏi (FOMO, streak phạt nặng).
- **Ngày nghiên cứu:** 05/11/2026. Chỉ nghiên cứu, chưa triển khai.

---

## 1. Tóm tắt điều hành — 7 kết luận lớn

1. **Vòng lặp giữ chân của cozy games không phải "chơi lâu", mà là "mỗi ngày có một ít thứ mới".** Cozy Grove giới hạn có chủ đích: mỗi ngày chỉ mở 30–60 phút nội dung quest mới, làm xong vẫn được ở lại câu cá/trang trí tuỳ thích. Animal Crossing dùng đồng hồ thời gian thực + chu kỳ mùa để người chơi hình thành thói quen ghé vào xem "hôm nay có gì khác".
2. **Quest ngày hiệu quả khi ngắn, có giờ reset cố định và phần thưởng chắc chắn:** một tín hiệu quen thuộc (reset ngày) + một hành động ngắn + một phần thưởng đảm bảo, lặp vài tuần sẽ thành thói quen thay vì quyết định phải cân nhắc. Thiết kế tốt khống chế quest ngày ở khoảng 10–20 phút để không biến thành việc nhà.
3. **Sưu tầm chỉ kéo người khi bộ sưu tập *hữu hạn, có cấu trúc rõ và hiển thị được khoảng trống*.** Nghiên cứu tâm lý sưu tầm (đăng trên Futurity, nguồn University of Arizona) cho thấy người chơi có động lực mạnh hơn hẳn khi bộ gần hoàn thành và cấu trúc bộ rõ ràng; ngược lại, việc liên tục thêm món mới vào một bộ tưởng đã xong sẽ gây ức chế.
4. **Hộ chiếu đóng dấu là cơ chế có sẵn ngoài đời thật và rất hợp với tham quan:** goshuin (Nhật Bản) là dấu đỏ + thư pháp ghi tên nơi đến và *ngày ghé thăm*, sưu tầm trong một cuốn sổ riêng (goshuinchō) — cuốn sổ tự nó trở thành kỷ vật của hành trình. Hệ eki-stamp/stamp rally mở rộng ra ga tàu, bảo tàng, điểm du lịch: mỗi điểm một dấu riêng phản ánh đặc trưng địa phương, gom đủ số dấu thì đổi quà.
5. **Sự kiện phải xếp lớp theo 3 nhịp: giờ trong ngày → tuần → mùa.** Pokémon GO chạy lịch nhiều tầng (Spotlight Hour theo giờ, Community Day 3 giờ/tháng, sự kiện mùa nhiều tuần). Disney Dreamlight Valley xếp lớp tương tự: Star Path kéo dài cả mùa + sự kiện ngắn 2–3 tuần + DreamSnaps là thử thách ảnh *theo tuần* để lấp khoảng trống giữa các đợt nội dung lớn.
6. **Avatar cá nhân hoá không chỉ là làm đẹp — nó tăng khám phá.** Một nghiên cứu thực nghiệm trong metaverse giáo dục ghi nhận avatar tự tuỳ chỉnh khiến người dùng khám phá không gian rộng hơn, và khi kết hợp với giao tiếp bằng giọng nói thì tương tác xã hội tăng thêm. Nghiên cứu về Roblox cho thấy avatar được dùng đồng thời để giống mình thật, thể hiện "mình lý tưởng" và gửi tín hiệu bản sắc cho người khác.
7. **Ranh giới đỏ: giữ chân bằng FOMO sẽ phản tác dụng về dài hạn.** Phân tích fatigue của Gamota chỉ ra người chơi rời game không phải vì chán mà vì *mệt*: daily thành "công việc thứ hai", battle pass thành máy chạy bộ đếm ngược, sự kiện nối nhau không khoảng nghỉ tạo cảm giác tội lỗi khi bỏ lỡ. Cơ chế chữa lành đã được nhiều game áp dụng: cho quest *chồng dồn 2–3 ngày*, streak lỡ một ngày không reset về 0, sự kiện quay lại theo chu kỳ.

> **Công thức rút ra cho Chợ Hòa Bình 3D:**
> `Phiên chơi 5–12 phút hoàn chỉnh` + `Hộ chiếu đóng dấu theo khu` + `3 quest ngày nhẹ, dồn được 3 ngày` + `Chợ thay đổi theo giờ thật (sáng/chiều/đêm)` + `Lịch hoa & lễ hội Đà Lạt theo mùa thật` + `Avatar đồ len/đặc sản mở khoá bằng trải nghiệm` − `mọi hình phạt khi vắng mặt`.

---

## 2. Các case đã khảo sát và cơ chế cốt lõi của chúng

| Case | Cơ chế giữ chân chính | Điểm mạnh nhất học được | Điểm yếu / cảnh báo |
|---|---|---|---|
| **Animal Crossing: New Horizons** (Nintendo) | Đồng hồ thời gian thực; cá/côn trùng/vật phẩm chỉ xuất hiện theo giờ & mùa cụ thể; shop thay hàng mỗi ngày; sự kiện theo lễ thật (Bunny Day, Festivale…) với vật phẩm độc quyền; bảo tàng (museum) để trưng bộ sưu tập cá/côn trùng/hoá thạch | Biến "kiểm tra hôm nay có gì" thành nghi thức; người chơi *tự đặt mục tiêu* (sưu tầm đủ, trang trí đảo, kết thân NPC) | Nhịp chậm; người chơi mới dễ thấy ít việc nếu không tự đặt mục tiêu |
| **Cozy Grove / Camp Spirit** (Spry Fox) | Đồng hồ thời gian thực, mỗi ngày một đợt quest mới 30–60 phút; quest chưa xong thì hôm sau vẫn còn, không cộng dồn áp lực — "bạn được quyền khám phá theo nhịp của mình"; hoàn thành quest mở dần khu vực mới của đảo | Phần nội dung "có hạn mỗi ngày" khiến một campaign 40+ giờ kéo dài được nhiều tháng thay vì bị cày hết trong một cuối tuần | Time-gating bị một bộ phận người chơi phàn nàn là giới hạn; phải có hoạt động tự do đủ vui sau khi hết quest ngày |
| **Disney Dreamlight Valley** (Gameloft) | Star Path (battle-pass bản cozy) theo mùa; sự kiện giới hạn 2–6 tuần; **DreamSnaps**: thử thách chụp ảnh theo chủ đề mỗi tuần, cộng đồng bình chọn, thưởng tiền tệ cao cấp; Event Board theo dõi tối đa 3 sự kiện cùng lúc | DreamSnaps tạo nội dung do người chơi sản xuất hàng tuần, giữ nhịp khi chưa có update lớn; ảnh đẹp tự lan truyền ra mạng xã hội | Sự kiện chồng sự kiện dễ tạo FOMO nếu cửa sổ hoàn thành quá ngắn; bản thân game phải liên tục nới thời hạn/bắt đầu sớm vẫn hoàn thành được theo nhịp riêng |
| **Pokémon GO** (Niantic) | Streak 7 ngày (quay PokéStop / bắt con đầu ngày); Daily Adventure Incense miễn phí 15 phút mỗi ngày; lịch sự kiện nhiều tầng: Spotlight Hour (1 giờ/tuần), Raid Hour, Community Day (3 giờ, 1 lần/tháng), GO Fest (sự kiện lớn năm) | "Cửa sổ giờ cố định" tạo hẹn hò cộng đồng: mọi người cùng online một lúc; phần thưởng ngày đủ nhỏ để việc ghé 30 giây cũng có ý nghĩa nhưng đủ hiếm (Pokémon huyền thoại từ incense ngày) để đáng ghé | Streak và cửa sổ giờ cứng gây áp lực; các bản sau đã phải nới rule để lỡ ngày không mất sạch tiến trình |
| **Goshuin & Eki-stamp / Stamp Rally** (Nhật Bản, ngoài đời thật) | Mỗi đền/chùa một con dấu riêng; bản giới hạn theo mùa/lễ hội khiến người sưu tầm quay lại đúng dịp; stamp rally: đi đủ một tuyến nhiều điểm → nhận quà; có thị trấn phối hợp 8 đền + 1 chùa thành một circuit đi bộ chung, biến 1 kỷ vật đơn lẻ thành hành trình cả địa phương | Chứng minh cơ chế đóng dấu hoạt động *ngoài đời thật*, không cần game hoá nặng; giá trị nằm ở thiết kế riêng của từng dấu + ngày tháng + cuốn sổ đẹp | Goshuin là vật thiêng (chứng nhận đã đến lễ), không phải trò "gom cho đủ" — khi vay mượn cho chợ ảo phải giữ tinh thần "dấu = đã thật sự trải nghiệm khu đó", tránh cơ chế bấm bừa lấy dấu |
| **Sansa / chùa online & các thế giới tham quan nhẹ** (bối cảnh dự án) | Vào là đi dạo được ngay, hiện diện cùng nhiều người, vài hành động đơn giản lặp lại được (lạy, lần tràng, ngồi thiền), lễ chung theo giờ cố định | Ngưỡng vào cực thấp + cảm giác "đang ở cùng người khác trong một nơi yên tĩnh" tự nó là phần thưởng; không cần thắng/thua | Ít mục tiêu dài hạn → dễ ghé 1–2 lần rồi thôi; đây chính là khoảng trống mà hộ chiếu/quest/sưu tầm của Chợ Hòa Bình phải lấp |
| **Roblox / thế giới avatar xã hội** | Avatar là nơi thể hiện bản sắc: giống mình, lý tưởng hoá, và tín hiệu xã hội; đặc tính avatar còn ảnh hưởng ngược tới tự tin và hành vi trong thế giới ảo | Kho đồ avatar là động cơ quay lại + khoe + chi tiêu bền nhất trong thế giới xã hội, nếu đồ gắn với *câu chuyện/kỷ niệm* thay vì chỉ bán | Nghiên cứu VR khác cho kết quả thận trọng hơn: tuỳ chỉnh avatar đơn thuần không tự động tăng mọi chỉ số gắn kết — cần gắn tuỳ chỉnh với hoạt động và cộng đồng mới phát huy |

---

## 3. Phân tích từng cơ chế

### 3.1. Quest theo ngày (daily quests)

**Cách các game làm tốt:**
- Reset vào một giờ cố định (thường nửa đêm giờ địa phương) để tạo "mốc hẹn" tâm lý; quest hết hạn tạo khẩn cấp nhẹ, nhưng xu hướng hiện nay là **cho chồng dồn 2–3 ngày** (Hearthstone, Overwatch 2) để người bận vẫn đuổi kịp.
- Nội dung quest ngày tốt nhất là *biến tấu của hành động cốt lõi* chứ không phải việc lạ: ghé shop xem hàng mới, nói chuyện với 1 NPC, tìm 1 vật thay đổi vị trí mỗi ngày (message bottle, glowing spot trong Animal Crossing).
- Phần thưởng ngày phải **nhỏ nhưng chắc chắn**, và có một mốc thưởng lớn ở ngày 7 (streak bonus) để tuần nào cũng có "đỉnh" mong chờ.

**Áp dụng cho Chợ Hòa Bình:**
- **3 quest/ngày, tổng 5–10 phút**, sinh từ NPC tiểu thương: ví dụ "Mua 1 ly sữa đậu nành nóng ở đầu dốc", "Tìm quầy mứt hôm nay giảm giá", "Chụp 1 ảnh ở bùng binh khi đèn vừa lên".
- Quest **dồn tối đa 3 ngày**; quá 3 ngày chỉ thay quest mới, *không trừ điểm, không mất chuỗi*.
- Chuỗi ngày dùng bản mềm: đếm "số ngày đã ghé trong tuần" (đủ 4/7 ngày là nhận thưởng tuần) thay cho streak liên tiếp — giữ được cảm giác tích luỹ, bỏ được nỗi sợ đứt chuỗi.
- Một **quest ẩn mỗi ngày** (không ghi trong danh sách): ví dụ một con mèo của chợ ngồi ở vị trí khác nhau, một quầy bí mật chỉ mở khi mưa sương. Đây là "lý do để đi dạo" cho người đã hết quest chính — học từ khoảng tự do sau quest của Cozy Grove.

### 3.2. Hộ chiếu đóng dấu (passport / stamp book)

**Vì sao cơ chế này mạnh:** dấu là bằng chứng vật lý của hành trình; bộ dấu hữu hạn + mỗi dấu một thiết kế riêng + đóng kèm ngày tháng khiến người dùng muốn (a) đi hết các điểm, (b) quay lại vào dịp có dấu phiên bản đặc biệt, (c) giữ cuốn sổ làm kỷ vật và khoe. Towns ở Nhật phối hợp nhiều điểm thành một circuit chứng minh dấu còn có tác dụng *kéo người đi hết một khu vực* thay vì chỉ ghé điểm nổi tiếng nhất.

**Áp dụng cho Chợ Hòa Bình — "Hộ chiếu Đi Chợ":**
- Mỗi khu của chợ một dấu riêng, chỉ đóng khi người chơi *làm xong một trải nghiệm nhỏ tại khu đó* (không phải chỉ đi ngang): ăn thử 1 món ở khu ẩm thực, nghe tiểu thương kể 1 câu chuyện ở khu đặc sản, thử 1 món đồ len ở khu đồ len…
- Các ô dấu gợi ý (khớp cấu trúc khu trong README dự án):
1. Cổng Chợ Đà Lạt / bùng binh Hòa Bình — dấu mặt tiền chợ
2. Rạp Hòa Bình — dấu rạp hát
3. Khu rau & hoa — dấu cẩm tú cầu / atiso
4. Khu đặc sản mứt & dâu — dấu trái dâu
5. Khu đồ len — dấu cuộn len
6. Khu ẩm thực sáng — dấu ly sữa đậu nành
7. Khu chợ đêm — dấu bánh tráng nướng + đèn vàng
8. Dốc & cầu thang chợ — dấu bậc thang trong sương
- **Dấu mùa:** cùng một khu nhưng dấu có biến thể theo mùa hoa (mai anh đào tháng 1–2, dã quỳ tháng 10–11…) và **dấu sự kiện** (Festival Hoa, Tết, Trung thu). Đây là lý do quay lại mạnh nhất của hệ goshuin: thiết kế giới hạn theo mùa khiến chuyến thăm đúng dịp trở nên đặc biệt.
- Đủ bộ 8 dấu thường → mở trang "Hoàn thành một vòng chợ" + huy hiệu *Khách quen Hòa Bình*; đủ bộ dấu của một mùa → khung bìa hộ chiếu riêng của mùa đó (vật phẩm khoe được trong ảnh chụp).
- Hộ chiếu phải xem lại được dạng cuốn sổ lật trang, có ngày đóng dấu — yếu tố "ngày tháng trên dấu" chính là thứ biến dấu thành nhật ký, theo đúng mẫu goshuin.

### 3.3. Sưu tầm (collecting)

**Nguyên lý tâm lý:** tiến trình phải *nhìn thấy được* (album đầy dần, ô trống ít dần); hiệu ứng "thiếu một món cuối" (Zeigarnik / completion) tạo động lực rất mạnh khi bộ gần xong; và bộ sưu tập đồng thời là cách người chơi kể câu chuyện về mình — trưng bày bộ sưu tập là một hình thức tự sự. Trong cozy games, sưu tầm còn có giá trị vì rủi ro thấp, nhịp thư giãn: một buổi tối đi tìm một món đồ "chỉ vì mình muốn" là trải nghiệm hợp lệ.

**Áp dụng cho Chợ Hòa Bình — 4 bộ sưu tập song song, mỗi bộ hữu hạn và công bố trước tổng số:**
| Bộ | Quy mô gợi ý | Cách thu thập | Hiển thị |
|---|---|---|---|
| **Sổ Đặc Sản** (mứt, trà atiso, cà phê, hồng treo gió…) | 24 món | Mua nếm tại quầy / làm quest của quầy đó | Kệ trưng bày trong "góc phòng" của người chơi |
| **Bưu thiếp Đà Lạt** | 12 tấm theo 12 tháng | Chụp ảnh đúng điểm check-in trong tháng tương ứng | Album bưu thiếp, gửi tặng bạn bè được |
| **Công thức chợ** (bánh tráng nướng, kem bơ, chè, sữa đậu nành…) | 10 món | Giúp NPC đủ số lần → được truyền công thức | Sổ tay nấu ăn; "nấu" lại được tại quầy bếp chung |
| **Hoa theo mùa** | 4–5 loài/mùa | Tìm và chụp/quét hoa đang nở trong chợ theo lịch mùa thật | Vườn hoa nhỏ trang trí khu vực cá nhân |

Quy tắc cứng rút từ nghiên cứu: **không chèn thêm món vào bộ đã công bố giữa mùa**; muốn thêm thì mở bộ mới (Series 2) để không phá cảm giác hoàn thành của người đã gom đủ.

### 3.4. Thành tựu & cấp bậc (achievements / tiers)

- Thành tựu hiệu quả nhất trong thế giới tham quan là loại **ghi lại hành vi khám phá** chứ không phải sức mạnh: "Lần đầu đi chợ trước 7h sáng", "Đi hết chợ trong một đêm mưa", "Nói chuyện với mọi tiểu thương", "Ghé chợ đủ 4 mùa".
- Cấp bậc nên là **danh xưng thân thuộc** thay cho số level khô: *Khách lạ → Khách ghé chơi → Khách quen → Bạn của chợ → Thổ địa Hòa Bình*. Mỗi cấp mở: khung avatar, biểu cảm mới, một ô trưng bày thêm — không mở sức mạnh/chênh lệch gameplay.
- Tránh bảng xếp hạng cạnh tranh gắt (không hợp tinh thần cozy và không hợp chợ tham quan); nếu cần yếu tố cộng đồng, dùng **mục tiêu chung toàn server** kiểu Cozy Grove/Dreamlight: "Cả chợ cùng gom 10.000 bông hoa cho Festival" — ai cũng thắng khi cả cộng đồng thắng.

### 3.5. Sự kiện theo giờ (time-of-day events)

Đây là lợi thế riêng của bối cảnh *chợ*: chợ thật vốn có nhịp giờ rất rõ.

- **Đồng hồ thật đồng bộ:** thế giới dùng giờ Việt Nam thật; một số quầy/NPC/món chỉ xuất hiện trong cửa sổ giờ của chúng — cơ chế đã chứng minh hiệu quả ở Animal Crossing (sinh vật chỉ có theo giờ/mùa khiến người chơi điều chỉnh nhịp ghé) và ở Pokémon GO (Spotlight Hour 1 giờ cố định mỗi tuần tạo điểm hẹn cộng đồng).
- Lịch giờ gợi ý cho Chợ Hòa Bình:
- **05:30–08:00 Chợ sớm:** sương mù dày, xe rau vào chợ, quest "đi chợ sớm" — phiên bản "Daily Adventure Incense" của chợ: một cửa sổ ngắn mỗi ngày nhưng đáng ghé.
- **08:00–17:00 Chợ ngày:** đủ quầy, quest NPC chính, giá "ban ngày".
- **17:30–18:30 Giờ lên đèn:** khoảnh khắc chuyển cảnh toàn chợ (đèn vàng bật, chụp ảnh đẹp nhất) — biến một thời điểm thành sự kiện tự nhiên mỗi ngày.
- **19:00–23:00 Chợ đêm:** khu ẩm thực mở hết, biểu diễn đường phố, hàng lưu niệm đêm; đây là khung giờ đông người nhất để hẹn bạn bè vào cùng.
- Mọi cửa sổ giờ phải **lặp lại hằng ngày** để người lỡ hôm nay không mất gì vĩnh viễn — chỉ "hôm nay chưa kịp, mai ghé".

### 3.6. Sự kiện theo mùa (seasonal events) — dùng lịch Đà Lạt thật

Đà Lạt có sẵn một "live-service calendar" ngoài đời: mỗi tháng một mùa hoa khác nhau — tháng 1–2 mai anh đào (và ban trắng, lavender), tháng 3–4 phượng tím + mùa dâu, tháng 10–11 dã quỳ, tháng 12 cỏ hồng và Festival Hoa Đà Lạt. Festival Hoa 2026 dự kiến khai mạc 19/12/2026 và bế mạc đêm 31/12/2026, với không gian hoa quanh hồ Xuân Hương và phố trà–cà phê–rượu vang. Chợ đêm cũng tự nó đã là trải nghiệm theo mùa: món nướng và đồ nóng "lên ngôi" khi trời lạnh cuối năm.

**Lịch mùa áp dụng (khớp nhịp Star Path của Dreamlight: 1 đường thưởng mùa + vài sự kiện ngắn lồng bên trong):**

| Giai đoạn | Chủ đề trong chợ | Nội dung mở |
|---|---|---|
| Tháng 1–2 | **Mùa Mai Anh Đào** + Tết | Dấu hộ chiếu bản hoa đào; quest Tết (lì xì NPC, gói bánh); trang trí chợ đỏ/vàng |
| Tháng 3–4 | **Mùa Phượng Tím & Dâu** | Bộ sưu tập dâu; quầy vườn dâu tạm thời; cuộc thi ảnh tím |
| Tháng 5–9 (mùa mưa) | **Mùa Sương & Mưa** | Không khí sương/mưa là "sự kiện thời tiết"; món nóng đặc biệt; dấu bản mưa (người ở xa vẫn có lý do vào vì mùa này ít khách du lịch thật) |
| Tháng 10–11 | **Mùa Dã Quỳ** | Đường hoa dã quỳ vào cổng chợ; quest săn hoa; dấu bản dã quỳ |
| Tháng 12 | **Festival Hoa + Cỏ Hồng + Giáng sinh** | Sự kiện lớn nhất năm: đường thưởng mùa đầy đủ, mục tiêu cộng đồng trang trí chợ, chợ đêm Noel |

Nguyên tắc vận hành:
- Mỗi mùa: **1 tuyến quest mùa (làm thong thả cả mùa) + 2 sự kiện ngắn 1–2 tuần + dấu/bưu thiếp mùa** — đúng cấu trúc xếp lớp đã thấy ở Dreamlight Valley (Star Path cả mùa, sự kiện phụ 2–3 tuần, DreamSnaps hằng tuần).
- Vật phẩm mùa **quay lại vào mùa sau** (có thể đổi màu/biến thể nhẹ) thay vì biến mất vĩnh viễn — giữ được tính sưu tầm mà không trừng phạt người đến muộn.
- Giữa các mùa luôn có **hoạt động nhịp tuần** (thi ảnh theo chủ đề như DreamSnaps) để không có "tuần chết".

### 3.7. Avatar cá nhân hoá

- **Kho đồ phải gắn với chợ, không phải kho đồ chung chung:** áo len Đà Lạt (mở khoá ở khu đồ len / mùa lạnh), khăn quàng, mũ nồi, túi vải đi chợ (nâng cấp dần theo số dấu hộ chiếu), ô trong suốt cho mùa mưa, phụ kiện hoa theo mùa.
- Cho phép thể hiện cả 3 lớp bản sắc mà nghiên cứu Roblox ghi nhận: giống mình thật / phiên bản lý tưởng / tín hiệu nhóm (ví dụ đồ đồng phục "team chợ đêm").
- Đồ avatar là phần thưởng chính của quest/dấu/sự kiện (thay cho tiền tệ vô nghĩa), vì nó *khoe được trong ảnh* — và ảnh là kênh lan truyền. Kết hợp với thử thách ảnh tuần (mục 3.6) để đồ mới luôn có dịp dùng.
- Lưu ý giới hạn từ nghiên cứu: tuỳ chỉnh avatar đơn thuần chưa đủ tạo gắn kết nếu không gắn với hoạt động/khám phá — vì vậy đồ phải *kiếm bằng đi chợ* chứ không chỉ mở menu là có, và phải có không gian xã hội (chợ đông người, chụp ảnh nhóm) để đồ được nhìn thấy.

### 3.8. Yếu tố xã hội & nội dung người chơi tạo ra

- **Hiện diện nhẹ (ambient presence):** thấy người khác đang đi chợ, ngồi ăn, chụp ảnh — giống cảm giác đông vui của chợ thật và của chùa online; không bắt buộc chat.
- **Thi ảnh theo chủ đề hằng tuần** (bản chợ của DreamSnaps): chủ đề như "Góc sương đẹp nhất", "Món ăn đêm bắt mắt nhất"; bình chọn trong cộng đồng; thưởng xu mềm + khung ảnh. DreamSnaps được người chơi Dreamlight Valley tự nhận là thứ kéo họ quay lại trong giai đoạn ít nội dung mới.
- **Quà tặng & gửi bưu thiếp:** gửi bưu thiếp (mục 3.3) kèm lời nhắn cho bạn ngoài game là kênh kéo người mới tự nhiên nhất của một thế giới tham quan.
- **NPC có trí nhớ:** tiểu thương nhớ tên, nhớ món bạn hay mua, câu thoại thay đổi theo số lần ghé và theo mùa — mô phỏng "tình thân khách quen" của chợ thật; đây là dạng quan hệ NPC tạo thói quen ghé thăm như việc chào dân làng mỗi ngày trong Animal Crossing.

### 3.9. Tiền tệ & phần thưởng (economy nhẹ)

- Một loại **xu mềm duy nhất** (gợi ý tên: *Xu Thông*) kiếm bằng quest/dấu/bán lại món sưu tầm thừa; tiêu cho: đồ avatar, khung ảnh, ô trưng bày, đổi món ăn ảo.
- Không bán xu bằng tiền thật trong giai đoạn đầu; không có "năng lượng" giới hạn số lần đi chợ; không có vật phẩm tăng sức mạnh. Doanh thu (giai đoạn sau, theo README dự án) đến từ đồ thật/voucher/affiliate — gamification chỉ nên *dẫn* tới quầy hàng, không được biến thành máy slot.

---

## 4. Vòng lặp giữ chân tổng hợp cho Chợ Hòa Bình 3D

```
TRONG 1 PHIÊN (5–12 phút)
Vào chợ → xem "Hôm nay ở chợ" (thời tiết sương/nắng, quầy đặc biệt, 3 quest ngày)
→ đi 1 vòng: làm quest + đóng 1 dấu khu / tìm 1 món sưu tầm
→ ghé quầy ăn 1 món → chụp 1 ảnh → nhận Xu Thông + tiến trình hiện rõ

GIỮA CÁC PHIÊN TRONG NGÀY
Khung giờ khác = chợ khác: chợ sớm (sương, rau vào) / chợ ngày / giờ lên đèn / chợ đêm (ẩm thực)

THEO TUẦN
Đủ 4/7 ngày ghé → thưởng tuần • Thi ảnh chủ đề mới mỗi thứ Tư • 1 NPC "khách đặc biệt" cuối tuần

THEO MÙA (lịch hoa Đà Lạt thật)
Dấu & bưu thiếp bản mùa • Tuyến quest mùa • Trang trí chợ thay đổi • Festival tháng 12 là đỉnh năm

DÀI HẠN
Hộ chiếu đầy dần 4 mùa • Danh xưng Khách quen → Thổ địa • Bộ sưu tập hoàn thành từng bộ hữu hạn
```

Điểm kiểm soát thiết kế quan trọng nhất: **mỗi lớp thời gian (phiên/ngày/tuần/mùa) phải tự nó trọn vẹn** — người chỉ chơi lớp phiên vẫn vui; người chơi lớp mùa có thêm, không phải bị lớp dưới "khoá" lại.

---

## 5. Chống FOMO & dark pattern — quy tắc bắt buộc cho dự án này

| Không làm | Làm thay thế |
|---|---|
| Streak liên tiếp, lỡ 1 ngày về 0 (dùng loss aversion ép đăng nhập) | Đếm ngày ghé trong tuần (4/7 là đạt); chuỗi chỉ tăng, không reset |
| Quest ngày hết hạn là mất trắng | Quest dồn 3 ngày; hết hạn chỉ thay mới, không phạt |
| Sự kiện nối nhau không khoảng nghỉ, đồng hồ đếm ngược khắp màn hình | Mỗi mùa tối đa 2 sự kiện ngắn, có "tuần yên" ở giữa; đếm ngược chỉ hiện trong trang sự kiện |
| Vật phẩm mùa biến mất vĩnh viễn | Vật phẩm quay lại mùa sau; người đến muộn mua/bắt kịp ở "Quầy Kỷ Niệm" |
| Battle pass trả phí mà không kịp cày là mất tiền | Nếu có đường thưởng mùa trả phí: mua sau vẫn nhận đủ theo tiến trình đã chơi; không hết hạn tiến trình |
| Thông báo đẩy gây tội lỗi ("Tiểu thương đang chờ bạn khóc…") | Tối đa 1 thông báo/ngày, nội dung thông tin ("Chợ đêm nay có hội hoa đăng"), có tắt theo chủ đề |

Lý do kinh doanh, không chỉ đạo đức: phân tích của Gamota kết luận người chơi rời đi vì cảm giác *mệt & mắc nợ game* chứ không phải hết nội dung, và retention dài hạn đang nghiêng về các game tôn trọng thời gian người chơi. Với một dự án tham quan dựa trên địa điểm thật và định hướng bán đặc sản thật, niềm tin là tài sản lớn hơn tỉ lệ mở app mỗi ngày.

---

## 6. Lộ trình áp dụng theo giai đoạn

**MVP (đủ để kiểm chứng giữ chân):**
1. Hộ chiếu Đi Chợ: 8 dấu khu, đóng bằng trải nghiệm nhỏ tại khu; trang hoàn thành vòng chợ.
2. 3 quest ngày từ NPC (dồn 3 ngày) + bảng "Hôm nay ở chợ".
3. Chu kỳ ngày/đêm theo giờ thật với 2 trạng thái rõ rệt (chợ ngày / chợ đêm) + khoảnh khắc lên đèn.
4. 1 bộ sưu tập hữu hạn (Sổ Đặc Sản 24 món) có album hiển thị ô trống.
5. Avatar cơ bản + 6–8 món đồ len/đặc sản mở khoá bằng dấu & quest; chế độ chụp ảnh + thẻ tổng kết chuyến đi để chia sẻ.

**Giai đoạn 2:**
6. Lịch mùa hoa (bắt đầu bằng mùa gần nhất khi ra mắt) + dấu/bưu thiếp bản mùa.
7. Thi ảnh chủ đề hằng tuần + gửi bưu thiếp cho bạn bè.
8. Danh xưng cấp bậc + thành tựu khám phá; NPC nhớ khách quen.
9. Đủ 4 khung giờ chợ (thêm chợ sớm) + quest ẩn mỗi ngày.

**Giai đoạn 3:**
10. Mục tiêu cộng đồng toàn server theo sự kiện (trang trí chợ đón Festival Hoa).
11. Tuyến quest mùa dài + đường thưởng mùa (miễn phí trước, cân nhắc trả phí sau khi đã có người dùng trung thành).
12. Liên kết gamification với mua thật: dấu/voucher tại quầy đối tác, giỏ đặc sản ảo → đặt hàng thật (theo định hướng trong README dự án).

**Chỉ số đo (đo để sửa thiết kế, không để ép người dùng):** tỉ lệ quay lại D1/D7/D30; % người đóng ≥4 dấu trong phiên đầu; % hoàn thành ≥1 quest ngày trong ngày quay lại; phân bổ phiên theo khung giờ (kiểm chứng chợ đêm/chợ sớm có kéo được phiên mới không); % người tham gia thi ảnh tuần; tỉ lệ người quay lại trong 7 ngày đầu của mùa mới.

---

## 7. Nguồn tham khảo

- Cozy Grove (Steam, Spry Fox) — đồng hồ thời gian thực, 30–60 phút nội dung quest mới mỗi ngày: https://store.steampowered.com/app/1458100/Cozy_Grove/?l=english&curator_clanid=36850605
- Cozy Grove & nhịp chơi không áp lực (quest chưa xong giữ sang hôm sau): https://ravenbookstore.com/pcs-paperbacks-cozy-grove
- How Daily Quests and Login Rewards Keep Players Engaged — reset ngày, streak, chồng dồn quest, burnout: https://www.duanzhengyue.com/artikel/daily-quests-login-rewards-engagement.html
- Gamota — Mobile Game Fatigue: When Play Starts to Feel Like Pressure: https://gamota.com/en_GB/gamota-lab/mobile-game-fatigue-when-play-starts-to-feel-like-pressure/
- Animal Crossing: New Horizons — daily tasks, seasonal events, real-time (tổng hợp): https://thefoxclick.com/animal-crossing-new-horizons-daily-tasks-master-cheatsheet/
- Disney Dreamlight Valley — Season of Scares / Star Path / Event Board (Steam News): https://store.steampowered.com/news/app/1401590/view/686391258373947713?snr=1_5_9_
- DreamSnaps — thử thách ảnh hằng tuần (Dreamlight Valley Wiki): https://dreamlightvalleywiki.com/DreamSnaps
- Pokémon GO — lịch sự kiện tháng (Spotlight Hours, Community Day): https://www.gamespot.com/articles/pokemon-go-november-2026-events-raids-spotlight-hours-community-day-and-more/
- Goshuin: Japan's Temple & Shrine Stamps, Explained (NihongoHub): https://www.nihongo-hub.com/blog/goshuin-temple-shrine-stamps.html
- Eki Stamps & Stamp Rallies — The Ultimate Collection Guide (TOMOGO!): https://www.tomogo-travel.com/blog/eki-stamps-stamps-in-japan-the-ultimate-collection-guide
- Why do people collect stuff? — nghiên cứu tâm lý sưu tầm, University of Arizona (Futurity): https://www.futurity.org/why-do-people-collect-3292682/
- The Psychology of Collecting in Cozy Games (Velvet Quest): https://velvetquest.shop/blogs/the-edit/the-psychology-of-collecting-in-cozy-games
- Avatar dynamics & engagement in an educational metaverse (Garcia, 2025): https://manuelgarcia.info/media/original/metaverse-social-interaction.pdf
- Đà Lạt mùa nào đẹp nhất — lịch mùa hoa theo tháng & Festival Hoa (MIA.vn): https://mia.vn/cam-nang-du-lich/da-lat-mua-nao-dep-nhat-15216
- Đà Lạt rực rỡ sắc hoa trước Festival Hoa 2026 (Báo Lao Động, 04/11/2026): https://laodong.vn/du-lich/kham-pha/da-lat-ruc-ro-sac-hoa-lo-dien-loat-diem-check-in-don-festival-hoa-2026-1794545.html
