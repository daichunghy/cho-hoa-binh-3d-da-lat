# 13 — Từ "mô phỏng chợ" thành GAME THẬT: nghiên cứu hệ thống game chibi social & vá 8 trục

> Mục đích: trả lời chốt của Chung Hy (06/11/2026, sau khi chơi thử v4.2) — bản hiện tại "chỉ mới được ~20%" so với game thật; yêu cầu tham khảo game thật về **trang phục, mua sắm, hành động, tham quan, mua đồ** để thành game thật sự, cộng trục bổ sung **model 3D + màu sắc**.
> Cách làm: kiểm kê trực tiếp trong `prototype-v2/index.html` (163.360 byte, bản v4.2) + `V4-CHECKLIST.md`; game thật tra từ nguồn web (AppiReview, NamuWiki, wiki Animal Crossing Pocket Camp, tài liệu Zepeto, travel.com.vn/buulong cho hàng thật Đà Lạt — URL ở cuối file); Niệm Phật Online và Stardew Valley lấy từ hồ sơ có sẵn (`research/01`, `research/12`) và cơ chế đã biết.
> Nguyên tắc xuyên suốt: mọi đề xuất phải khả thi trong **1 file HTML web prototype** như hiện tại (không multiplayer server thật, không engine mới) — mục nào vượt khả năng thì ghi rõ "để giai đoạn sau".

---

## PHẦN 0 — KẾT LUẬN 1 TRANG

Bản hiện tại mạnh ở **khung cảnh và không khí** (22 sạp, 5 khu, 93 NPC có hoạt ảnh nghề, đèn đêm ấm, hành trình spawn→chợ) nhưng mỏng ở **hệ thống game**: người chơi mua được đồ ăn và ăn lấy buff, nhưng **đồ len mua về không mặc được**, **không có cấp độ**, **quest chỉ có 1 tuyến dẫn đường + đơn mua hộ**, **không quest ngày**, **không bộ sưu tập theo món**, **không sự kiện hẹn giờ**, **không người chơi khác**. Đó chính là khác biệt giữa "đi dạo trong mô hình chợ đẹp" và "chơi game".

| # | Trục | Game thật có | Mình đang ở | % |
|---|---|---|---|---|
| 1 | Trang phục | Tủ đồ theo ô (tóc/mũ/áo/quần/giày/túi/kính), mặc = hiện lên người, độ hiếm, shop thời trang riêng | Hàng len bán như hàng tồn kho; nhân vật chỉ đổi màu palette (`recolor`) | **5%** |
| 2 | Mua sắm | 2–3 tiền tệ tách vai trò, shop xoay hàng theo ngày, giá biến động, bán lại, hàng giới hạn | 1 tiền tệ Xu, mua/bán/đơn mua hộ chạy được, giá tĩnh, hàng cố định | **35%** |
| 3 | Hành động | Emote, ngồi, cầm đồ trên tay, chụp ảnh, tương tác vật thể đa dạng | Tiểu thương diễn nghề rất tốt; người chơi chỉ: đi, mở menu, ăn (buff), coi bói, nghe hát | **30%** |
| 4 | Tham quan | Bản đồ nhiều điểm đến có sưu tầm, điểm chụp ảnh, khu mở khóa dần | 9 khu + hộ chiếu đóng dấu + minimap + thẻ tên khu; chưa có sưu tầm theo điểm, nội thất chợ nông | **35%** |
| 5 | Mua đồ | Inventory có phân loại, đồ ăn có hoạt cảnh, quà tặng được, lưu niệm trưng bày/sưu tầm | Giỏ đồ có sức chứa + nâng cấp, ăn có buff Ấm/Năng lượng; lưu niệm mua xong nằm chết trong giỏ | **30%** |
| 6 | Nhiệm vụ & vòng lặp | Quest ngày/tuần, EXP + cấp, sự kiện hẹn giờ, mùa, điểm danh | 1 quest dẫn đường 5 chặng + đơn mua hộ ngẫu nhiên; **không cấp, không quest ngày, không sự kiện giờ** | **20%** |
| 7 | Xã hội | Người chơi thật, chat, thăm nhà, tặng quà, bảng thông báo cộng đồng | 93 NPC mô phỏng sống động (xếp hàng, nhóm chat, bong bóng thoại) nhưng **0 người chơi thật, 0 tương tác hai chiều** | **10%** |
| 8 | Model 3D + màu sắc | Art direction có bảng màu/độ bão hòa/ánh sáng được khóa thành chuẩn | Grade đêm ấm v4.2 đã đúng hướng nhưng màu nằm rải rác dạng hex trong code, chưa có chuẩn; model còn hộp | **35%** |

**Trung bình có trọng số ≈ 22% — khớp nhận định ~20% của Chung Hy.** Ba thiếu hụt lớn nhất: (1) **trang phục không mặc được**, (2) **không có tiến trình dài hạn** (cấp/quest ngày/sưu tầm), (3) **thiếu lớp xã hội & sự kiện hẹn giờ** khiến chợ không "sống theo giờ".

---

## PHẦN 1 — TRỤC 1: TRANG PHỤC (tủ đồ, mua/thay đồ, độ hiếm, phối đồ)

**Game thật làm gì**
- **Play Together (Haegin):** tủ đồ chia ô rõ ràng — tóc, biểu cảm, mũ, áo trên, quần, giày, túi, kính, trang điểm mặt, màu da (NamuWiki mục "adornment"). Có **Fashion Mall** là tòa nhà riêng chỉ bán trang phục; trang phục cũng là phần thưởng sự kiện (bộ Exorcist mở khóa từ sự kiện Haechi). Avatar creator chỉnh được tông da/kiểu tóc/mặt/thân hình ngay từ đầu.
- **Zepeto:** trang phục là **trung tâm kinh tế**: 2 tiền tệ Coins (kiếm free, tối đa ~2.500/ngày từ quest/sự kiện) và ZEM (premium); item có thang độ hiếm tới mức giới hạn số lượng (≤500 bản = ultra-rare); có **tặng đồ cho người khác trong world** và mannequin bày bán trang phục ngay trong thế giới 3D.
- **Animal Crossing: Pocket Camp:** quần áo mua ở Able Sisters trong Market Place, **hàng xoay mỗi ngày**; mở khóa thêm outfit qua cấp tình bạn với villagers; Catalog ghi lại mọi món từng sở hữu — tủ đồ đồng thời là bộ sưu tập.
- **Niệm Phật Online:** trang phục/pháp phục gắn với cấp và sự kiện theo mùa — mặc đồ đẹp = tín hiệu "chơi lâu, cấp cao" (tên + cấp hiện trên đầu).

**Mình đang có gì**
- Sạp len bán đúng mặt hàng mặc được ngoài đời: *Áo len cổ lọ, Khăn choàng len, Mũ len beanie, Găng tay len* (menu LEN BÀ BẢY / MŨ & GĂNG LEN) — nhưng mua xong chúng chỉ là **item trong giỏ** như mọi hàng khác.
- Nhân vật người chơi dùng `character.glb` + hàm `recolor` (đổi màu theo palette), có hệ nâng cấp `coat` (áo ấm) — đó là **chỉ số**, không phải **hình ảnh**: mặc áo mới không thấy khác gì trên người.
- Không có UI tủ đồ, không ô trang bị, không xem trước (preview), không độ hiếm.

**Thiếu gì (gốc của 5%)**
1. Không có khái niệm "mặc": mua áo len ≠ mặc áo len. Đây là thiếu hụt cảm xúc lớn nhất — ở chợ đêm Đà Lạt, mua đồ len là để **mặc ngay cho ấm và chụp ảnh**.
2. Không có ô trang phục (mũ/khăn/áo/găng/tay cầm) và nút "Thay đồ".
3. Không có độ hiếm/phân tầng giá trị: áo len thường vs áo thêu hoa giới hạn mùa.
4. NPC mặc đẹp đa dạng hơn người chơi (NPC có khăn/mũ ngẫu nhiên) — người chơi trông "nghèo" nhất chợ.

**Vá (xem backlog P0-1):** biến 6–8 món len/lưu niệm hiện có thành đồ **mặc được thật** bằng node gắn trên character.glb (mũ = beanie node có sẵn, khăn = scarf node NPC đã dùng), thêm màn hình Tủ đồ, mỗi món mặc cho +Độ Ấm nhìn thấy được.

---

## PHẦN 2 — TRỤC 2: MUA SẮM (tiền tệ, vòng lặp kiếm–tiêu, giá cả, bán lại)

**Game thật làm gì**
- **Play Together:** 3 tiền tệ tách vai trò — **Stars** (kiếm từ quest NPC 50–150 sao/nhiệm vụ, đi học theo lịch ở trường, bán cá/côn trùng/hóa thạch, Game Party), **Gems** (premium), **Gold bars** (nạp). Kiếm–tiêu khép kín: câu cá → bán → mua nội thất/trang phục; shop bí mật xuất hiện ngẫu nhiên bán đồ hiếm.
- **Stardew Valley:** shop có **giờ mở cửa và lịch nghỉ** (Pierre's đóng thứ Tư), mỗi shop một chuyên môn (Willy bán cần câu, Robin bán đồ gỗ); giá bán lại cố định theo công thức; **Community Center bundles** biến "mua/thu thập đủ bộ" thành nhiệm vụ lớn; hàng hóa theo mùa.
- **Pocket Camp:** Bells (kiếm trong game) + Leaf Tickets (premium); **Market Box**: người chơi tự bày bán cho người chơi khác; shop xoay hàng **mỗi ngày** tạo lý do ghé xem.
- **Niệm Phật Online:** 3 tiền Công đức / Sen / Ngọc — mỗi hoạt động trả một loại, tránh một hành vi "farm tối ưu duy nhất" (research/01).

**Mình đang có gì (nền tốt nhất trong các trục)**
- Xu là tiền tệ duy nhất; **kiếm**: thưởng chặng quest (30/60 Xu), đơn mua hộ (giá ×2 + 15 Xu), bán lại đồ (`sellItem`); **tiêu**: mua hàng 22 sạp, nâng cấp (túi 80/160 Xu, giày 70/150 Xu, áo ấm, thể lực).
- Biển sạp có giá nhìn từ xa (v4.2), menu tại quầy — đúng chất chợ.
- Hàng hóa đúng chất Đà Lạt thật (đối chiếu giá thật ở Phần 5).

**Thiếu gì**
1. **Giá tĩnh tuyệt đối**: không giảm giá giờ vàng, không mặt hàng "hôm nay rẻ", không khan hiếm — mua sắm thiếu cảm giác "săn được món hời" vốn là linh hồn chợ đêm (ngoài đời phải trả giá!).
2. Không có **mặc cả (trả giá)** — cơ chế đặc trưng chợ Việt Nam chưa game nào làm, làm được là khác biệt riêng.
3. Tiền tệ đơn vai trò: Xu vừa mua đồ ăn vừa nâng cấp — thiếu tầng "tiền sưu tầm" (ví dụ Tem Dâu đổi đồ giới hạn).
4. Bán lại phẳng: bán món nào cũng được, không có sạp thu mua riêng, không chênh lệch giá theo sạp.
5. Hàng không xoay: 22 menu cố định vĩnh viễn — ngày thứ 3 vào chợ đã thuộc hết hàng.

---

## PHẦN 3 — TRỤC 3: HÀNH ĐỘNG (emote, tương tác, ngồi ăn, chụp ảnh)

**Game thật làm gì**
- **Play Together:** emote/gesture là hàng bán và phần thưởng; ngồi ghế, nằm võng, cầm ô, chụp ảnh nhóm; tương tác vật thể khắp nơi (ngồi xích đu, chơi đàn, bơi). Fashion Runway là minigame "diễn" trang phục.
- **Zepeto:** cử chỉ/pose là item premium riêng (gói pose chụp ảnh), photo booth là nơi khoe đồ — hành động phục vụ **chụp ảnh chia sẻ**.
- **Stardew Valley:** hành động gắn nghề (câu, đào, tưới) + tương tác xã hội (tặng quà, nói chuyện 2 câu/ngày/NPC, khiêu vũ lễ hội).
- **Niệm Phật Online:** tại một điểm có **nhiều hành động nghi thức khác nhau** (lạy 3 kiểu, gõ mõ, lần tràng 108, ngồi thiền có vòng thở) — một địa điểm, nhiều lớp tương tác (research/12).

**Mình đang có gì**
- Phía NPC rất mạnh: tiểu thương có hoạt ảnh nghề (rót, lật, khuấy, cân — VENDOR_ANIM), khách xếp hàng, nhóm đứng nói chuyện, người ngồi ăn trên bậc thang, ca sĩ hát ở quảng trường (nghe được qua `toggleListen`).
- Phía người chơi: đi bộ/chạy, mở menu mua, ăn (nhận buff), coi bói (Chú Ba), nghe hát, đóng dấu hộ chiếu. **Người chơi là người ít "diễn" nhất trong chợ của chính mình.**

**Thiếu gì**
1. **Không emote nào** cho người chơi (vẫy tay, vỗ tay nghe hát, giơ tay chụp ảnh) — trong khi NPC có cả dàn cử chỉ.
2. Không **ngồi** được: ghế nhựa và bậc thang đầy người ngồi, trừ người chơi.
3. Ăn/uống không có hoạt cảnh trên người chơi: không cầm ly sữa, không cầm bánh tráng — ăn chỉ là trừ item + cộng buff (research/09 đã chỉ ra đây là nửa cái vui bị thiếu).
4. Không **chế độ chụp ảnh** (ẩn UI, khung check-in) dù chợ đã có điểm đẹp (bùng binh, thang cầu vồng trong kế hoạch) — mất kênh lan truyền tự nhiên nhất.
5. Tương tác vật thể ngoài sạp gần như bằng 0 (không gõ thử chuông, không xem bảng tin, không cho chim ăn...).

---

## PHẦN 4 — TRỤC 4: THAM QUAN (khám phá, địa danh, sưu tầm)

**Game thật làm gì**
- **Play Together:** đảo Kaia là hub + nhiều khu chức năng khác hẳn nhau (trường, bãi biển, khu cắm trại, trung tâm thương mại); **Lost Island chỉ mở cuối tuần**; sưu tầm theo điều kiện (cá theo giờ/thời tiết/loại cần) ghi vào **Illustrated Book**.
- **Pocket Camp / New Horizons:** thăm đảo/khu của người khác là hoạt động chính; vật sưu tầm xuất hiện theo **giờ và mùa thật**; bảo tàng trưng bày bộ sưu tập.
- **Niệm Phật Online:** bản đồ hành hương **17 điểm** theo tuyến, mỗi điểm một dấu + sự tích — tham quan có cấu trúc hành trình (research/01).
- **Stardew Valley:** bản đồ mở dần (mỏ, sa mạc cần sửa xe buýt), mỗi khu một tài nguyên/bí mật riêng.

**Mình đang có gì**
- Địa hình thật theo trục hành trình: đường vào → vòng xoay → nhà lồng chợ (2 cao độ) → bậc thang → quảng trường đồi; 9 khu có tên (thẻ tên khu hiện chữ lớn), **hộ chiếu 9 dấu** đóng theo khu, minimap có chấm mục tiêu.
- Phông nền: đồi thông lớp xa, tháp chuông nhà thờ, khách sạn có biển tên — đọc được "đang ở Đà Lạt".

**Thiếu gì**
1. Hộ chiếu đóng dấu theo **khu** (đến là có) chứ chưa có sưu tầm theo **điểm/món/trải nghiệm** (đến + làm gì đó mới có) — thiếu cảm giác "còn thiếu 3 cái nữa".
2. Nội thất nhà lồng nông (research/12 mục 12 đang để đợt sau): chưa có đa dạng theo chiều dọc (khay hàng nghiêng, hàng treo theo dải màu).
3. Không có **điểm chụp ảnh được thưởng** và không có bí mật khám phá (góc khuất, sạp ẩn giờ khuya).
4. Không có khu vực mở khóa theo tiến trình — toàn bản đồ mở từ đầu, hết bất ngờ sau phiên đầu.

---

## PHẦN 5 — TRỤC 5: MUA ĐỒ (inventory, đồ ăn dùng được, quà, lưu niệm) + KHO HÀNG ĐÚNG CHẤT ĐÀ LẠT

**Game thật làm gì**
- **Stardew Valley:** đồ ăn nấu được cho buff theo món; **tặng quà là hệ thống quan hệ**: mỗi NPC có món thích/ghét, tặng đúng sinh nhật ×8 hiệu ứng; lưu niệm/hiện vật vào bảo tàng.
- **Pocket Camp:** inventory phân tab rõ (nguyên liệu/đồ ăn/nội thất/quần áo), món thừa bán hoặc cho vào Market Box; đồ ăn đưa cho villagers để tăng tình bạn.
- **Play Together:** đồ sưu tầm 3 số phận — ghi sổ, **trưng bày ở nhà** (bể cá/bảo tàng mini), hoặc bán.

**Mình đang có gì**
- Giỏ đồ có sức chứa (8 → 14 → 20 theo nâng cấp túi), `eatItem` + buff Ấm/Năng lượng, `eatenCount` đã đếm số món đã ăn (mầm của sổ sưu tầm!), hàng lưu niệm có sẵn (móc khóa, bưu thiếp, hộp quà).
- Menu 22 sạp bám hàng thật (bảng đối chiếu dưới).

**Kho hàng thật chợ đêm Đà Lạt — đối chiếu & bổ sung**

| Nhóm | Hàng thật (giá tham khảo ngoài đời) | Trong game đã có | Nên bổ sung |
|---|---|---|---|
| Ăn nóng | Bánh tráng nướng, xiên nướng, bánh căn, súp cua, khoai/bắp nướng — 10–30k/phần | Đủ gần hết | Bánh ướt lòng gà đã có; thêm **ốc bươu nhồi thịt**, **bánh mì xíu mại chén** |
| Uống nóng | Sữa đậu nành 15k (biển chốt "15K"), sữa đậu xanh, cacao, cà phê phin | Đủ | **Sữa bắp**, **trà gừng** (món "cứu lạnh" theo mùa) |
| Dâu & kem | Dâu tươi 100–250k/kg theo mùa (vụ 11–4), dâu lắc 15–20k, kem bơ | Dâu tươi, dâu lắc, kem bơ | **Dâu sấy** (bản "mang về" của dâu tươi — tách 2 nhóm như research/09) |
| Đặc sản mang về | Hồng treo gió 180–350k/kg (cao cấp nhất), mứt 50–200k/hộp, trái cây sấy 70–250k/gói, trà atiso & cà phê 100–200k/gói | Hồng treo gió, mứt dâu, trà atiso, cà phê Cầu Đất, trà ô long | **Khoai lang mật sấy**, **hồng giòn**, **nước cốt dâu tằm**; hồng treo gió nên là món **hiếm theo mùa 9–11** |
| Đồ len | Áo len 50–150k, khăn/mũ/găng 30–200k, đồ thủ công thêu | Áo cổ lọ, khăn, mũ beanie, găng | **Áo len thêu hoa** (bản hiếm), **tất len**, **áo khoác dạ secondhand vintage** (đặc sản chợ đêm thật) |
| Lưu niệm | Móc khóa, bưu thiếp, đồ handmade 10–100k | Móc khóa, bưu thiếp, kính mát, đồng hồ | **Tranh/ảnh chợ đêm**, **nến thơm thông**, **túi vải thêu "Đà Lạt"** |

*Quy đổi cảm giác giá:* giữ tỉ lệ hiện tại ~1 Xu ≈ 1.000đ cảm giác (ly sữa 15 Xu khớp biển 15K trong ảnh chốt; áo len 80–150 Xu nằm trong dải nâng cấp 70–160 Xu hiện tại) — đừng phá tỉ lệ này khi thêm hàng.

**Thiếu gì**
1. Lưu niệm **mua xong vô dụng**: không tặng được cho NPC, không trưng bày, không ghi sổ — mua chỉ để đầy giỏ rồi bán lại.
2. Đồ ăn chưa phân tầng trải nghiệm: không món "phải thử" (must-try list), không đánh dấu món mới chưa thử trong menu.
3. Không có **tặng quà NPC**: Chú Ba, Cô Lan không nhận được gì từ người chơi — quan hệ một chiều.
4. Đồ ăn chưa có hoạt cảnh cầm trên tay (nối trục 3).

---

## PHẦN 6 — TRỤC 6: NHIỆM VỤ + VÒNG LẶP NGÀY/ĐÊM + SỰ KIỆN

**Game thật làm gì**
- **Play Together:** quest ngày ở Plaza + quest NPC (50–150 Stars), **đi học theo giờ học thật trong game** để nhận lương ngày, sự kiện theo mùa từng nước, đảo mở cuối tuần — lịch là một hệ thống.
- **Pocket Camp:** yêu cầu của villagers làm mới theo chu kỳ vài giờ; sự kiện mùa cho đồ giới hạn; "ghé xem hôm nay có gì" là vòng lặp chính.
- **Niệm Phật Online:** **thời khóa đếm ngược** (sáng/tối theo lịch) biến giờ thành sự kiện tập thể; nhiệm vụ ngày/tuần + điểm danh (research/01, 12).
- **Stardew Valley:** festival cố định theo lịch mùa (mỗi mùa 2 lễ), bảng tin "Help Wanted" trước nhà Pierre's thay mỗi ngày, quest lớn theo cốt truyện (bundles).

**Mình đang có gì**
- Quest dẫn đường 5 chặng (rất tốt cho phiên đầu), đơn mua hộ ngẫu nhiên có đếm ngược ~170 giây (đúng chất Township), ngày/đêm chuyển được + mặc định đêm 19:15, sạp `nightOnly`, giờ diễn của ca sĩ, hệ nhiệt độ theo giờ.
- Chợ đêm thật mở 17:00, đông nhất 18–22:00 — mặc định 19:15 của game đang khớp giờ vàng thật.

**Thiếu gì**
1. **Không EXP/cấp độ**: chơi 10 giờ vẫn "như mới" — thiếu thước đo tiến trình dài hạn rẻ nhất và hiệu quả nhất (Niệm Phật dùng tới 100 cấp; Play Together cấp mở quà mốc).
2. **Không quest ngày**: hết quest dẫn đường + đơn mua hộ ngẫu nhiên thì không còn cấu trúc — phiên 2 trở đi người chơi tự bơi.
3. **Không sự kiện hẹn giờ**: không đếm ngược "19:00 lên đèn", không giờ vàng giảm giá, không chợ phiên cuối tuần (đã nêu ở research/12 mục 16, chưa làm).
4. Không **điểm danh/ghế thăm hằng ngày** và không phần thưởng quay lại.
5. Không mùa: Đà Lạt có mùa dâu (11–4), mùa hồng (9–11), mùa hoa (dã quỳ 10–11, mai anh đào 1–2) — kho hàng và trang trí chưa đổi theo mùa thật.

---

## PHẦN 7 — TRỤC 7: XÃ HỘI

**Game thật làm gì**
- **Play Together / Zepeto:** người chơi thật là nội dung chính: chat, kết bạn, thăm nhà, Home Party, tặng đồ, chụp ảnh nhóm; thông báo cộng đồng khi ai đạt mốc.
- **Niệm Phật Online:** tên + cấp trên đầu, thông báo chạy ngang khi có người kết duyên/đạt mốc, số người online hiển thị, đèn hoa đăng mang lời nguyện của người khác — **cảm giác "có người thật"** ngay cả khi tương tác nhẹ (research/01, 12).
- **Pocket Camp:** thăm trại người khác + Market Box mua bán chéo — xã hội bất đồng bộ (không cần online cùng lúc).

**Mình đang có gì**
- Mô phỏng xã hội bằng NPC ở mức tốt so với prototype: 93 NPC có tên + nghề (thẻ tên), xếp hàng, nhóm nói chuyện có bong bóng thoại theo khu, tiểu thương nhớ mặt qua đơn mua hộ. Đây là nền "xã hội giả lập" đáng giữ.

**Thiếu gì (và giới hạn thật)**
- Multiplayer thật **không khả thi** trong bản 1 file HTML hiện tại — ghi rõ để không hứa hão. Nhưng 80% cảm giác xã hội có thể giả lập được:
  1. **NPC "khách du lịch" cư xử như người chơi**: có thẻ tên + cấp, mặc đồ đẹp hơn NPC thường, đứng chụp ảnh ở điểm check-in, thỉnh thoảng "thả" lời nhắn ở bảng tin.
  2. **Bảng tin chợ / sổ lưu bút**: NPC để lại lời nhắn theo ngày ("Dâu hôm nay ngọt lắm — bé Na, Huế") + đèn lồng điều ước ghi lời nhắn treo quảng trường buổi tối (ý từ research/12).
  3. **Thông báo chạy ngang** kiểu Niệm Phật: "Bạn An vừa mua được Áo len thêu hoa hiếm!" — tạo nhịp sống cộng đồng.
  4. **Tặng quà + thân thiết NPC** (nối trục 5): 5–7 NPC chính có thanh thân thiết, tặng đúng món thích → mở thoại mới/giảm giá — xã hội một người chơi nhưng có chiều sâu.

---

## PHẦN 8 — TRỤC 8: MODEL 3D + MÀU SẮC (trục bổ sung của Chung Hy)

**Game chibi social làm gì (chuẩn tham chiếu)**
- **Niệm Phật Online** (đã chốt làm thước phong cách): chibi đầu to tròn, camera diorama góc cao, **màu phẳng ấm**, UI nâu–vàng, thẻ tên + cấp trên đầu (research/01, ảnh `theme/mau-np-*`, `theme/niem-phat-style/`).
- **Play Together:** màu bão hòa cao, vật liệu gần như không xám (mọi bề mặt đều có hue rõ), ánh sáng phẳng sáng, viền tối nhẹ trên vật thể — đọc rõ ở khoảng cách xa và màn hình nhỏ.
- **Ảnh chốt của dự án** (`theme/CHOT-phong-cach-cho-dem.png`): đêm **nâu–đỏ ấm**, đèn vàng mật ong, điểm nhấn đỏ (chữ chợ, tua đèn), hàng hóa nhiều màu bão hòa trên nền tối ấm.

**Mình đang có gì**
- v4.2 đã grade đêm ấm: sương/nền `0x191209`, hemi vàng mật ong, đèn điểm `0xff9a3d`, đường ướt roughness 0.35, quầng sáng dưới đèn; biển gỗ có giá + hình món; mô hình đã qua đợt bevel/lớp mặt tiền (V4-CHECKLIST mục J).
- Nhưng: mã màu nằm **rải rác dạng hex** trong code từng sạp/vật (mỗi sạp tự khai `shirt:0x…`), chưa có bảng màu chuẩn; ngày đang yếu hơn đêm; độ bão hòa chưa có quy tắc (vẫn còn bề mặt xám phẳng: nền đường/plaza từng bị nêu ở research/12).

**CHUẨN MÀU ĐỀ XUẤT — khóa thành 1 khối `PALETTE` trong code, mọi vật liệu lấy từ đây**

*Bảng màu nền (đêm — trạng thái mặc định):*
| Vai trò | Giá trị | Ghi chú |
|---|---|---|
| Sương/nền trời đêm | `#191209` (đang dùng — giữ) | Nâu đen ấm, cấm dùng xanh đen `#11161f` |
| Ánh sáng môi trường (hemi) sky/ground | `#ffd9a0` / `#4a3220`, cường độ 0.55 | Vàng mật ong trên, nâu đất dưới |
| Đèn điểm chính | `#ff9a3d` (đang dùng — giữ) | Cam sodium chợ đêm |
| Đèn sạp / lồng đèn giấy | `#ffb45e`, emissive 0.65–0.9 | Vàng ấm sáng hơn đèn đường 1 bậc |
| Điểm nhấn đỏ | `#c8372d` | Chỉ cho: chữ CHỢ ĐÀ LẠT, tua đèn, biển đặc biệt — tối đa ~5% diện tích khung hình |
| Nền đường/plaza | `#4a4038` có texture đá lát, roughness 0.35 về đêm | Không để xám trung tính phẳng |

*Bảng màu ngày (để ngày không thua đêm):* trời `#a8d4f0` pha ấm, nắng `#fff2d8` cường độ 1.1, sương ngày `#d8e4e2`, bóng đổ mềm — mục tiêu "sáng trong như ảnh `theme/01-toan-canh-hoang-hon.webp`".

*Quy tắc bão hòa (áp cho mọi model mới & rà soát model cũ):*
1. Mọi vật liệu thuộc nhóm **hàng hóa/trang phục/đồ ăn**: độ bão hòa HSV **0.45–0.80** — màu phải "ngon" như hàng thật bày bán.
2. Nhóm **kiến trúc/nền**: bão hòa 0.15–0.35 (làm nền cho hàng hóa nổi lên), trừ biển hiệu và băng trang trí được lên 0.5.
3. **Cấm xám không hue** cho mọi bề mặt nhìn thấy được, trừ đá lát và kim loại; xám phải ngả ấm (`#8a7f72` thay `#8f8a80` kiểu cũ).
4. Áo NPC/người chơi lấy từ 1 bảng 14 màu cố định (đỏ đô, vàng mù tạt, xanh thông, tím oải hương, hồng đào, nâu cà phê, kem, xanh rêu…) — hết sinh màu ngẫu nhiên lệch tông.
5. Tone mapping ACES, exposure đêm 1.05 / ngày 1.0; đèn nhấp nháy lệch pha giữ nguyên (đang có).

*Chuẩn model (chibi + đọc từ xa):*
1. Tỉ lệ nhân vật đầu:thân ≈ **1 : 1.6** (đầu to kiểu Niệm Phật), mắt chấm + má hồng giữ nguyên (đã sửa sạch ở v4.1).
2. Mọi khối chính bevel tối thiểu **0.03–0.06** đơn vị; không còn cạnh sắc 90° ở vật gần camera (nối tiếp mục J v4).
3. Hàng hóa trên quầy: mỗi món 1 khối màu bão hòa riêng + **silhouette đọc được ở 15m** (hũ, chồng ly, vỉ nướng đã có — áp quy tắc này cho các set bày hàng còn thiếu ở research/12 mục 8).
4. Texture canvas: biển 512×256, vải/bạt 256×256 lặp, họa tiết len (vân đan/thêu) vẽ 1 lần dùng chung cho cả hệ đồ len — đây là tiền đề để trục trang phục "mặc lên thấy đẹp".
5. Ngân sách: standalone đang 9,93MB/10MB — mọi model mới phải qua nén GLB (gltfpack/Draco) và texture canvas thay ảnh chụp; thêm nội dung lớn phải đồng thời dọn nội dung cũ ít dùng.

---

## PHẦN 9 — BACKLOG ƯU TIÊN (khả thi với bản web prototype hiện tại)

### P0 — Làm xong là bước qua ngưỡng "game" (5 mục)
| # | Việc cụ thể | Trục | Cách làm trong kiến trúc hiện tại | Effort |
|---|---|---|---|---|
| P0-1 | **Tủ đồ mặc được**: 4 ô (Mũ / Khăn / Áo / Tay cầm), 8 món đầu tiên lấy từ hàng len + lưu niệm đang bán; mua ở sạp len = vào tủ, bấm Mặc = hiện node trên nhân vật người chơi + cộng Độ Ấm; màn hình Tủ đồ mở từ nút cạnh Túi đồ | 1, 5 | Tái dùng node mũ/khăn của character.glb (NPC đang dùng), state `state.wardrobe` + `state.equipped` lưu vào save `chohb3d-v1` | M |
| P0-2 | **EXP + cấp "Khách quen chợ"** (10 cấp đầu): EXP từ đóng dấu (+20), giao đơn mua hộ (+15), ăn món mới (+10), nghe hát/coi bói (+5); lên cấp mở khóa: món mới ở sạp, ô tủ đồ, danh hiệu hiện cạnh thẻ tên "Bạn" | 6, 4 | 1 biến `state.exp`, bảng cấp tĩnh, render cạnh thẻ tên sẵn có | S |
| P0-3 | **Sổ Đặc Sản** trong Hộ chiếu: liệt kê toàn bộ ~45 món theo 5 khu, món đã mua/đã ăn sáng lên, hiện % hoàn thành từng khu; ăn món mới có toast "+1 Sổ Đặc Sản" | 4, 5, 6 | Dữ liệu menu đã có sẵn; thêm `state.tasted{}` (đã có mầm `eatenCount`), 1 tab mới trong modal hộ chiếu | S |
| P0-4 | **Quest ngày (3 quest/ngày, dồn tối đa 3 ngày)**: sinh từ NPC tiểu thương ("Mua 1 ly sữa nóng", "Tìm sạp hôm nay giảm giá", "Chụp ảnh ở vòng xoay khi lên đèn"), thưởng Xu + EXP; reset theo ngày thật của máy người chơi | 6, 2 | Sinh quest từ bảng mẫu + trạng thái ngày trong save; hạ tầng nhận/trả quest đã có từ đơn mua hộ | M |
| P0-5 | **Khối `PALETTE` + khóa chuẩn màu/model** như Phần 8: gom mọi hex rải rác về 1 bảng, đổi áo NPC sang bảng 14 màu, thay các bề mặt xám phẳng còn sót, áp quy tắc bão hòa cho vật liệu hàng hóa | 8 | Sửa 1 lượt trong index.html + rà soát nhanh từng GLB theo checklist Phần 8; không thêm tính năng | S–M |

### P1 — Thêm chiều sâu (sau P0)
| # | Việc | Trục | Ghi chú |
|---|---|---|---|
| P1-1 | **Mặc cả**: ở sạp ăn/đặc sản, nút "Trả giá" — NPC đồng ý giảm 10–25% theo xác suất + mức thân thiết; trả giá hụt quá 2 lần NPC "hết vui" 1 phút | 2, 7 | Cơ chế riêng chưa game nào làm — điểm khác biệt chợ Việt |
| P1-2 | **Hàng xoay & giờ vàng**: mỗi ngày thật 3 sạp có "món hôm nay" (giảm 20%, biển thêm dải đỏ); 19:00–20:00 "giờ lên đèn" 1 khu giảm giá | 2, 6 | Dùng seed theo ngày để mọi máy giống nhau |
| P1-3 | **Hành động người chơi**: ngồi ghế nhựa/bậc thang (phím E gần ghế trống), 4 emote (vẫy tay, vỗ tay, giơ ly, chụp ảnh), ăn/uống cầm vật trên tay 5 giây | 3 | Tái dùng pose ngồi của NPC + node tay cầm của P0-1 |
| P1-4 | **Chế độ chụp ảnh**: ẩn UI, khung viền "Chợ Hòa Bình — Đà Lạt", 3 điểm check-in có cột sáng (vòng xoay, thang, quảng trường đồi) chụp đủ 3 = dấu hộ chiếu đặc biệt | 3, 4 | Canvas chụp frame sẵn có của trình duyệt |
| P1-5 | **Tặng quà + thân thiết NPC**: 6 NPC chính có món thích (tra trong thoại), tặng đúng +thân thiết, mốc 3/5 mở giảm giá riêng + thoại mới | 5, 7 | Dữ liệu `likes` gắn vào NPC có tên sẵn có |
| P1-6 | **Sự kiện hẹn giờ**: đồng hồ đếm ngược trên HUD tới 19:00 "Lên đèn chợ đêm" và tới giờ hát quảng trường; đến giờ có thông báo chạy ngang + hiệu ứng bật đèn toàn cảnh | 6, 7 | Hạ tầng giờ game + applyDayNight đã có |
| P1-7 | **Mùa vụ kho hàng**: theo tháng thật — mùa dâu (11–4) dâu rẻ + nhiều, mùa hồng (9–11) mở hồng treo gió hiếm, ngoài mùa giá ×1.5 hoặc "hết mùa" | 2, 5, 6 | Chỉ là bảng cấu hình theo tháng cho menu sẵn có |

### P2 — Để giai đoạn sau (đã ghi nhận, chưa làm)
| # | Việc | Vì sao để sau |
|---|---|---|
| P2-1 | Sạp của bạn (thuê 1 ô sạp, tự chọn hàng + trang trí + biển tên) — research/12 mục 19 | Effort L, cần P0-1/P0-3 làm nền kinh tế trước |
| P2-2 | Nội thất nhà lồng theo chiều dọc (khay nghiêng, hàng treo dải màu, dây đèn lửng) — research/12 mục 12 | Cần đợt model riêng + ngân sách MB đang sát trần |
| P2-3 | Mèo đi theo người chơi — research/12 mục 14 | Phụ thuộc hệ tay cầm/đi theo của P1-3 |
| P2-4 | Chợ phiên đầu mối cuối tuần (mở khu riêng sáng thứ 7/CN) — research/12 mục 16 | Cần sự kiện hẹn giờ P1-6 chạy ổn trước |
| P2-5 | Đèn lồng điều ước + bảng lưu bút cộng đồng giả lập | Cần lớp thông báo xã hội của P1-6 |
| P2-6 | Multiplayer thật / thăm chợ của bạn bè | **Ngoài khả năng bản 1 file HTML** — cần server; chỉ xét khi có bản host riêng |

---

## PHẦN 10 — "100% TRÔNG NHƯ THẾ NÀO" (định nghĩa lại đích đến)

Một phiên chơi chuẩn sau khi vá P0+P1: vào game lúc 19:10 (đếm ngược lên đèn vừa xong), nhận 3 quest ngày từ Cô Lan, ghé sạp sữa đang giờ vàng mua ly sữa nóng (mặc cả được −15%), **mặc áo len thêu hoa** vừa săn được hôm qua cho đủ ấm, ngồi bậc thang uống sữa (hoạt cảnh cầm ly), EXP +10 vì là món mới trong Sổ Đặc Sản (đạt 62%), giao đơn mua hộ hồng treo gió đang mùa, chụp ảnh check-in ở vòng xoay, ghé Chú Ba coi quẻ, thả tim vỗ tay cho ca sĩ ở quảng trường, xem thông báo "một bạn khách vừa mở khóa cấp 5 Khách quen chợ". **Đó là vòng lặp của một game** — bản hiện tại mới có khung cảnh và khoảng 1/5 số hệ thống trên.

---

## NGUỒN

- Play Together — AppiReview (lối chơi, kinh tế, Game Party, nhà ở): https://www.appireview.com/com.haegin.playtogether
- Play Together — NamuWiki (tiền tệ Stars/Gems, ô trang phục, Fashion Mall, quest NPC): https://en.namu.wiki/w/플레이투게더
- Animal Crossing: Pocket Camp — Wiki Getting Started (Catalog, Market Box, crafting, tình bạn mở khóa outfit): https://animalcrossingpocketcamp.fandom.com/wiki/Getting_Started
- Animal Crossing: Pocket Camp Complete — Nintendo Wiki (Market Place xoay hàng theo ngày, Leaf Tokens): https://nintendo.fandom.com/wiki/Animal_Crossing:_Pocket_Camp_Complete
- Zepeto — tài liệu World SDK (avatar items, gifting, mannequin): https://docs.Zepeto.me/world-sdk-guide/monetize-your-world-setting-up-products-and-currencies
- Zepeto — Coins/ZEM & độ hiếm (BitTopup News): https://news.BITTOPUP.com/news/zepeto-coin-gacha-2026-8-tips-to-max-your-zems-coins-rewards
- Chợ đêm Đà Lạt — hàng hóa & giá thật: https://travel.com.vn/tin-tuc-du-lich/cho-dem-da-lat-v18326.aspx ; https://buulong.com.vn/cho-dem-da-lat-ban-gi.html ; https://dulichviet.com.vn/tin-tuc/diem-danh-7-mon-dac-san-nen-mua-lam-qua-khi-du-lieu-da-lat
- Hồ sơ nội bộ: `research/01` (Niệm Phật Online), `research/07` + `research/11` (chợ thật), `research/09` (cơ chế ăn/uống), `research/12` (đối thủ & checklist 19 mục), `prototype-v2/V4-CHECKLIST.md`.
