# 12 — Đối thủ & Đa dạng: vì sao thế giới đang lặp, và checklist vá

> Mục đích: trả lời nhận xét của Chung Hy — game "chưa đa dạng lắm", bản dựng "chưa có giống" ảnh chốt.
> Thước đo số 1: `theme/CHOT-phong-cach-cho-dem.png` (sạp sữa đậu nành đêm). Mọi đánh giá "game đang ở đâu" đều kiểm chứng trực tiếp trong `prototype-v2/index.html` + `prototype-v2/assets/*.glb` và hồ sơ v4/V4-CHECKLIST tại thời điểm viết (sau v4.1).
> Loại trừ theo lệnh: các việc v4.1 đang làm (đường vào + spawn, mặc định buổi tối + tông ấm của cảnh, vibe đồi thông/sương/hoa, nhiệm vụ dẫn đường theo hành trình, minimap) KHÔNG được tính là mục mới trong checklist phần 3 — chúng chỉ xuất hiện trong bảng GAP phần 0 như chẩn đoán hiện trạng.

---

## PHẦN 0 — BẢNG GAP THEO ẢNH CHỐT (cấp độ SẠP + KHUNG CẢNH)

Ảnh chốt không thắng ở "nhiều model hơn". Nó thắng ở chỗ **mỗi sạp là một chân dung**: biển có giá, quầy có bộ đồ nghề riêng của món đó, người bán đang LÀM một hành động đọc được từ xa, hơi nước báo "món này nóng", đèn/tên/UI cùng một tông ấm. Game hiện tại có đủ khung (20 sạp, 85 NPC, hoạt ảnh tay, đèn từng sạp) nhưng các lớp "chân dung" này đang mỏng hoặc phẳng — đó là gốc của cảm giác lặp.

| # | Lớp trong ảnh chốt | Game đang ở mức nào (bằng chứng) | Cách đạt tới mức ảnh | Effort |
|---|---|---|---|---|
| 1 | **Biển sạp gỗ chữ nổi + GIÁ trên biển**: biển gỗ nâu, chữ kem khắc/nổi "SỮA ĐẬU NÀNH NÓNG — 15K —", vẽ kèm hình hũ đậu, chồng ly, tô, ly mang đi | Biển là **canvas phẳng** (`makeSignTexture`/`signMesh`, index.html ~249–266): nền tối `#33291f`, chữ vàng nhạt `#ffe9b0`, **chỉ có tên sạp — không giá, không hình món, không hiệu ứng gỗ/nổi**. 4 sạp trong nhà dùng biển kem chữ đỏ khổ lớn hơn (dòng ~779–781) nhưng vẫn phẳng và không giá. Giá chỉ xuất hiện trong menu mua | (a) Vẽ lại texture biển: nền gỗ có vân + viền tối, chữ có bóng đổ giả nổi, thêm dòng giá "15 Xu" + 1–2 icon món vẽ tay theo từng sạp — làm ngay bằng canvas, không cần model mới. (b) Đợt sau: biển hộp 3D mỏng có khung gỗ lồi (extrude nhẹ) cho 7 sạp đặc sản mặt tiền chợ đêm | S (texture) → M (biển 3D) |
| 2 | **Bày hàng chi tiết đúng món**: trên quầy sữa thấy hũ đậu thủy tinh, chồng ly sứ, tô đậu phộng, ly nhựa mang đi xếp hàng — nhìn quầy là biết bán gì không cần đọc biển | Quầy có nồi/vỉ/phin chung bật theo loại (`Pot*/Grill*/Phin*` trong stall.glb, dòng ~762–765) + v4 thêm mẹt/rổ/tường len/hộp quà/chai. Nhưng **chưa có "bộ đồ nghề" riêng cho từng món**: quầy sữa và quầy chè bỏ biển đi là khó phân biệt; không có chồng ly, hũ đựng nguyên liệu trong suốt, ly mang đi | Dựng 4–5 "set bày hàng" nhỏ dùng chung cho nhóm sạp cùng họ: set đồ uống nóng (hũ thủy tinh + chồng ly + tô topping + chồng ly mang đi), set nướng (vỉ + bánh xếp hàng + quạt), set kem/dâu (thùng kem + hộp dâu đỏ), set lưu niệm (móc khóa treo vòng). Mỗi set 6–10 chi tiết nhỏ từ hình khối sẵn có, gắn theo `decorateStall` | M |
| 3 | **Tiểu thương có HÀNH ĐỘNG + đạo cụ**: cô bán sữa đội mũ len có hoa, đang **rót từ ấm inox vào ly**, người hơi nghiêng theo việc | Đã có hoạt ảnh tay theo nghề (stir/flip/pour/scoop/turn/weigh/arrange/pack — VENDOR_ANIM, dòng ~632–684) — nền tốt. Nhưng **tay không cầm gì**: rót mà không ấm, lật mà không xẻng, khuấy mà không muôi; động tác đọc yếu từ góc camera diorama | Gắn 1 đạo cụ cầm tay theo từng hành động (ấm rót, xẻng lật, muôi dài, cân tay, kéo cắt vải…) vào nhóm tay phải của character.glb — model nhỏ, không cần rig mới vì tay đã có chuyển động sẵn. Thêm nghiêng người nhẹ theo nhịp hành động | M |
| 4 | **Cột hơi nước bốc rõ ở món nóng**: cột hơi trắng dày, cao gần 1 thân người trên nồi sữa và phin cà phê — tín hiệu "nóng/ngon" đọc từ xa | Hệ khói/hơi dùng chung 1 Points material: size 0.55, **opacity 0.32, màu xám 0xcccccc** (dòng ~593–601) — cột mảnh và nhạt; phin có cột riêng nhưng thấp. So với ảnh chốt, hơi hiện tại gần như vô hình ở góc nhìn toàn cảnh | Thay points bằng sprite có texture mềm (radial gradient), 2 lớp: cột chính trắng ấm opacity ~0.5 cao 1.2–1.6m xoáy nhẹ + lớp tản ở miệng nồi. Cường độ cột bám theo trạng thái (đang nấu cho khách = dày, chờ = mỏng). Lưu ý: lớp "khói/hơi khắp nơi" đã nằm trong gói vibe v4.1 — mục này là phần **độ đọc tại điểm chế biến**, không trùng phần sương/không khí chung | S |
| 5 | **Lồng đèn giấy LỚN nhiều cao độ + tua đỏ, giăng thành hàng**: đèn vàng ấm đường kính ~nửa thân người, treo 2–3 cao độ dọc đường, tua đỏ dài — tạo "trần ánh sáng" cho phố chợ | Mỗi sạp chỉ có vài `Lantern*` nhỏ trước quầy trong stall.glb (đu đưa + nhấp nháy, dòng ~769–775) + v4 thêm 1 bóng trắng + halo/sạp. **Không có đèn khổ lớn, không tua, không dây giăng ngang thành hàng nhiều cao độ** | Thêm biến thể đèn giấy lớn (sphere dẹt + texture giấy ấm + tua đỏ = vài dải mảnh) và dây đèn giăng ở **quảng trường + đường vào + hẻm ăn** với 2–3 cao độ. Chừa trục Âm Phủ: 26 ảnh thật (research/11) không có dây đèn ngang trục — ở đó giữ điểm sáng từng sạp như hiện tại để không sai chất chợ thật | M |
| 6 | **Trang trí nóc sạp**: cành thông + lá xanh phủ nóc, mỗi nóc một chút khác — nóc sạp cũng có "tính cách" | **Không có lớp nào**: nóc sạp chỉ là bạt sọc canvas 3 biến thể (v4). Nhìn từ camera 45° (góc nhìn chính của game!), nóc là bề mặt lớn nhất mỗi sạp chiếm — phẳng và đồng loạt | Prop "cành lá nóc" từ pine.glb thu nhỏ: 2–3 cụm cành + lá gắn ngẫu nhiên theo sạp (xoay/scale khác nhau), vài sạp thêm dây đèn nhỏ quấn cành. Vì camera nhìn từ trên xuống, đây là mục cho hiệu quả thị giác/mét-vuông cao nhất trong các mục S | S |
| 7 | **Đạo cụ mặt đất quanh sạp**: giỏ mây dâu tây đỏ đặt sát đất trước quầy, chậu sen đá/cây nhỏ — lớp "chân sạp" sống động | Có mẹt/rổ ở sạp nông sản, hộp quà, ghế nhựa + bàn ăn. **Thiếu giỏ dâu đặt đất** (dâu là biểu tượng chợ Đà Lạt) và chậu cây nhỏ điểm xuyết trước quầy; chân sạp đa số trống | Thêm prop giỏ mây (cylinder loe + lớp dâu đỏ bóng) + chậu cây nhỏ (2–3 kiểu lá), đặt theo cụm 2–4 cái lệch hàng trước ~10 sạp, tránh xếp đều như quân cờ | S |
| 8 | **Nền đường ĐÁ LÁT có texture + sương là mặt đất**: đá lát xám có vân và khe, sương trắng ôm sát mặt đất quanh chân sạp | Mặt đất là **plane màu phẳng**: plaza `0x8f8a80`, road `0x494a4d`, hilltop `0x97907f` (dòng ~370–389) — không texture, không khe lát. Sương có FogExp2 + 6 mảng sương trôi opacity chỉ 0.06 (dòng ~1173–1187) — rất nhẹ, chưa thành lớp sương chân đất như ảnh | (a) Texture lát đá vẽ bằng canvas (ô đá + khe tối + vết bẩn nhẹ), lặp theo ô cho quảng trường/đường chợ/bậc thang — không cần ảnh ngoài. (b) Phần sương dày thêm thuộc gói vibe v4.1, không tính mới ở đây | M (riêng texture) |
| 9 | **Thẻ tên lơ lửng trên đầu NPC**: pill nâu chữ kem "Cô Lan – Bán Sữa", "Chú Thành – Nướng", người chơi là "Bạn" — nhìn người là biết họ là ai, làm gì | **Hoàn toàn chưa có.** CanvasTexture hiện chỉ dùng cho biển sạp, halo đèn, sương, nốt nhạc (dòng ~261/693/704/1180/1229). 85 NPC trong game hiện vô danh — mắt người chơi không có điểm neo để nhớ từng người, cảnh đông mà "không quen ai" | Sprite canvas pill nâu bo tròn cho ~20 tiểu thương (tên + nghề: "Cô Lan – Bán Sữa") + Chú Ba coi bói + ca sĩ quảng trường + vài NPC đặc biệt; khách thường không cần tên hoặc hiện khi đến gần. Người chơi gắn thẻ "Bạn" như ảnh chốt | S |
| 10 | **Tông màu ấm sâu + UI nâu bo tròn + panel nhiệm vụ**: đêm nâu–đỏ ấm, UI nâu đậm viền sáng bo tròn lớn, panel nhiệm vụ bên phải, nút "Mua" vàng lớn | Cảnh: nền đêm `0x11161f` xanh đen lạnh (phần grade cảnh thuộc v4.1 đang sửa). **UI chưa đổi**: panel kính tối xanh-xám `rgba(16,20,24,.72)`, nền trang `#0e141b`, nút amber `#c8871a` — đúng chất "app" hơn là chất "chợ ấm" của ảnh chốt và Niệm Phật Online | CSS/UI thuần: panel nền nâu đậm `#2b1d12`–`#3a2718`, viền kem, bo góc 14–18px, nút chính vàng ấm, font chữ kem. Không đụng logic. Đây là mục rẻ nhất mà đổi cảm giác toàn cục nhất | S |

**Kết luận phần 0:** trong 10 lớp, game **thiếu hẳn 3** (thẻ tên NPC, trang trí nóc sạp, giá+hình trên biển), **yếu rõ 4** (bày hàng theo món, đạo cụ cầm tay, cột hơi, đèn giấy lớn), **phẳng 2** (nền đường, UI), và tông cảnh đang được v4.1 xử lý. Không lớp nào cần engine mới — toàn bộ nằm trong khả năng canvas texture + prop nhỏ + sprite.

---

## PHẦN 1 — ẢNH MẪU CÒN LẠI ↔ GAME HIỆN TẠI

| Ảnh mẫu | Yếu tố đa dạng ảnh có | Game hiện tại | Ghi chú |
|---|---|---|---|
| `mau-np-01` (trước chợ, ngày) | Mỗi sạp một "chuyên môn" đọc ngay: rau củ / hoa tươi / dâu–atisô; **xe đạp dựa cạnh sạp rau**; bồn hoa tròn lớn giữa quảng trường; **khách cầm giỏ, ôm bó hoa, bưng mâm** — người không ai tay không; thẻ tên + Lv trên đầu; nhiệm vụ có tiến độ dạng 3/5, 6/10 | Bùng binh đã có bồn hoa + tượng đài (v4/v4.1) nhưng quảng trường trước chợ chưa có điểm nhấn hoa có cấu trúc riêng; NPC khách **tay không 100%**; không xe đạp; thẻ tên chưa có (gap 9) | "Người cầm đồ" là khác biệt lớn nhất: chợ trong ảnh ai cũng đang MANG một thứ gì đó |
| `mau-np-03` (rạp Hòa Bình hoàng hôn) | **Banner dọc 2 bên mặt tiền rạp**, thảm đỏ sảnh, nhóm bạn đứng hàng chụp ảnh, **chậu cây lớn đặt đối xứng theo cặp**, nhà nhỏ mái ngói rải sườn đồi làm nền | theater.glb chưa có banner dọc; chậu cây lớn đối xứng chưa có; nhà nền phía đồi đang là khách sạn khối lớn (hotels.glb), thiếu nhà nhỏ mái ngói xen kẽ | Banner dọc + chậu đối xứng là trang trí "có chủ đích" rẻ tiền mà hiệu quả |
| `plan/A3` (mặt tiền chợ đêm) | Chữ viền **bóng đèn marquee**, **đồng hồ trên mặt tiền**, **cờ nhỏ nhiều màu cắm ban công**, chậu hoa ban công, **xe đẩy nướng di động bốc khói**, khách cầm ly/bó hoa/túi xách, ghế băng dài | Chữ nổi 3D đỏ (đúng chợ thật hơn A3 — giữ), nhưng: không đồng hồ, không cờ ban công, không chậu hoa ban công, không xe đẩy hàng rong di động (ảnh thật research/11 có gánh/xe đẩy — hợp lệ) | Lấy đồng hồ + cờ + xe đẩy; bỏ marquee (sai chất thật) |
| `plan/A4` (trong nhà lồng) | **Khay hàng nghiêng bậc thang**, mỗi loại rau một khay một màu; **áo len/khăn TREO thành dải màu gradient**; dây đèn bóng nhỏ dọc lan can tầng lửng; chậu cây trên lan can; khách xách giỏ đầy; sàn họa tiết kim cương | Nội thất có quầy + biển lớn chữ đỏ (đúng ảnh thật), nhưng hàng bày phẳng theo khối, chưa có khay nghiêng, chưa có hàng treo theo màu, không dây đèn lửng, sàn phẳng màu | Đây là "đa dạng theo chiều dọc" — mắt đi lên tường/lan can vẫn có cái xem |
| `plan/A6` (bậc thang + cầu kính) | **Đèn trụ cổ điển 2 hàng đối xứng dọc thang**, chậu hoa đặt trên bệ chiếu nghỉ, lan can đá có trụ trang trí, cầu kính có dải đèn dưới gầm, thông xen đá tảng | Cầu thang đã có ghế ăn + người ngồi (v4), cầu kính có; chưa có hàng đèn trụ đối xứng và chậu hoa chiếu nghỉ thành nhịp | Nhịp đối xứng dọc thang là thứ làm thang "đẹp" thay vì chỉ "có" |
| `plan/B1` (nhân vật) | **Hoa thêu trên áo len**, khăn có tua + họa tiết dệt, mũ len có vân đan và quả bông — chi tiết bề mặt vải | character.glb thay được màu áo/khăn/mũ theo palette (v4) nhưng bề mặt **trơn, không họa tiết**: không thêu, không vân đan, khăn không tua | Đa dạng bằng texture vải rẻ hơn đa dạng bằng model mới |
| `np-01..04` (Niệm Phật gameplay thật) | Chánh điện: **hàng bồ đoàn xếp lưới** = nhiều điểm nghi thức giống nhau có chủ đích nhưng mỗi người một tên/cấp; bản đồ hành hương ~17 điểm theo tuyến có tiến độ đóng dấu; **thời khóa đếm ngược theo lịch**; thông báo xã hội chạy ngang; số người online | Chợ có hộ chiếu 9 dấu (cùng họ với bản đồ hành hương — điểm mạnh sẵn có); chưa có hoạt động hẹn giờ tập thể, chưa có lời nhắn cộng đồng, chưa có lớp "sống chung" kiểu thông báo xã hội | Xem phân tích áp dụng ở phần 2.1 |

---

## PHẦN 2 — ĐỐI THỦ: HỌ CHỐNG LẶP BẰNG CÁCH NÀO

Ảnh minh họa đã tải về `theme/competitors/` (9 ảnh, nguồn trong `theme/competitors/SOURCES.md`). Mọi tính năng dưới đây đều có tư liệu nguồn — không suy đoán.

### 2.1 Niệm Phật Online (niemphat.online — AfreecaTV Studio VN)

Nguồn: `research/01-niemphat-online.md` + ảnh `competitors/np-01..03`.

**(a) Đa dạng ở đâu:**
- **Đa dạng địa điểm là xương sống:** 17 cảnh chùa khắp 3 miền trên một bản đồ hành hương (ảnh np-02), mỗi chùa có kiến trúc riêng, sự tích riêng và dấu đóng riêng theo tuyến (kiểu "Thăng Long tứ trấn 1/3"). Người chơi luôn có "nơi chưa đến".
- **Đa dạng hành động tại một điểm:** trong chánh điện (ảnh np-01) không chỉ có 1 tương tác — lạy Phật theo 3 phong cách, tràng hạt 108, gõ mõ, tụng kinh, ngồi thiền có vòng thở 5–30 phút, dâng hoa, thắp nến, thỉnh chuông, thả đèn hoa đăng **dính lời nguyện công khai của người chơi khác**.
- **Đa dạng theo THỜI GIAN:** thời khóa sáng/tối chạy theo lịch đếm ngược ("Thời khóa sáng sau 42 phút" — ảnh np-03) biến khung giờ thành sự kiện tập thể; nhiệm vụ ngày/tuần + điểm danh giữ nhịp quay lại.
- **Lớp xã hội:** tên + cấp trên đầu từng người, chat "Đạo hữu", thông báo chạy ngang khi ai đó kết duyên/đạt mốc, hiển thị số người đang online, **linh thú** đi theo nhân vật.
- **Kinh tế tách vai trò:** 3 loại tiền (Công đức / Sen / Ngọc) — mỗi hoạt động trả một thứ khác nhau nên không hành vi nào là "tối ưu duy nhất".

**(b) Áp được vào chợ Đà Lạt (đúng chất chợ thật):**
- Bản đồ hành hương ↔ Hộ chiếu Đi Chợ 9 dấu: **đã có sẵn** — đây là điểm chợ đang ngang cơ đối thủ, cần nuôi tiếp bằng tuyến/tiến độ rõ ràng chứ không phải làm mới.
- Thời khóa đếm ngược → **sự kiện hẹn giờ của chợ**: đếm ngược tới khoảnh khắc "lên đèn chợ đêm" và tới giờ mở chợ phiên sáng (xem checklist 13, 15). Chợ thật vốn vận hành bằng giờ (sạp mở theo ca ngày/đêm — research/11) nên cơ chế này không hề gượng.
- Đèn hoa đăng gắn lời nguyện → **đèn lồng ghi điều ước/lời nhắn** treo ở quảng trường vào buổi tối: đúng chất đèn lồng chợ đêm, là UGC nhẹ mà không cần hệ thống chat.
- Linh thú → thú cưng nhỏ đi theo (checklist 14).

### 2.2 Play Together (Haegin — Hàn Quốc)

Nguồn: FileHorse (mô tả tính năng), APKPure bản VNG, AppiReview, NamuWiki; ảnh `competitors/pt-01..03`.

**(a) Đa dạng ở đâu:**
- **Hub + tòa nhà chức năng khác hẳn nhau:** quảng trường trung tâm nối trường học (có lớp học theo lịch, trả tiền theo ngày học), Game Center, cửa hàng thời trang, đại lý xe, cửa hàng trứng thú cưng, khu cắm trại, bãi biển, nội thất nhà riêng. Mỗi tòa nhà là một "thể loại chơi" khác (ảnh pt-02, pt-03).
- **Minigame nhiều thể loại:** Game Party tối đa 30 người (obby, zombie, tháp, ném tuyết… — ảnh pt-01 là một minigame trên nóc nhà), Obby Race, Tower of Infinity.
- **Sưu tầm theo điều kiện:** câu cá **600+ loài** (đổi theo giờ/thời tiết/loại cần), bắt côn trùng **300+ loài**, đào hóa thạch, thiên thạch rơi ở quảng trường cho người chơi đào; tất cả ghi vào Illustrated Book.
- **Thú cưng có vòng đời:** 27+ loài, ấp từ trứng, cho ăn/tắm/dắt đi dạo, lên cấp, cưỡi được, biến hình.
- **Phương tiện cực rộng:** ván trượt, xe đạp, siêu xe, khinh khí cầu, ba lô phản lực, xe địa hình (ảnh pt-02 thấy xe buýt trường + xe cá nhân trên phố).
- **Sự kiện theo mùa + theo lịch:** sự kiện Tết theo từng nước, shop bí mật xuất hiện ngẫu nhiên, đảo Lost Island **chỉ mở cuối tuần** — khan hiếm theo giờ tạo lý do quay lại đúng giờ.

**(b) Áp được vào chợ Đà Lạt:**
- Bài học lớn nhất không phải "thêm minigame" mà là **mỗi điểm đến phải chơi khác nhau**: chợ đã có mua bán/coi bói/hát — hướng đúng; nên thêm điểm có tương tác khác hẳn (khung chụp ảnh ở cầu thang cầu vồng, quầy len thử đồ lên nhân vật) thay vì thêm sạp bán hàng thứ 21 giống 20 sạp cũ.
- Sưu tầm theo giờ/thời tiết → **món hiếm theo giờ/lạnh**: sạp/món chỉ xuất hiện khung giờ nhất định hoặc khi trời đủ lạnh (đã có mầm: sạp `nightOnly`, buff theo Độ Ấm) — ghi vào một "Sổ đặc sản" trong hộ chiếu.
- Lost Island cuối tuần → **chợ phiên đầu mối sáng sớm cuối tuần** (checklist 15): chợ thật Đà Lạt có phiên rau buôn sáng sớm, không bịa.
- Thú cưng → checklist 14. Phương tiện cho người chơi (xe đạp thuê quanh bùng binh): khả thi nhưng effort L và dễ phá nhịp đi bộ ngắm chợ — **không đưa vào checklist đợt này**, ghi nhận để sau.

### 2.3 Mini World: CREATA (Miniwan)

Nguồn: FileHorse/filetomob, modhello, APKKit; ảnh `competitors/mw-01-western-town.webp`, `mw-02.jpg`.

**(a) Đa dạng ở đâu:**
- **Đa dạng đến từ NGƯỜI CHƠI, không phải nhà phát hành:** editor tích hợp + gallery hàng triệu map/minigame cộng đồng (parkour, giải đố, FPS, chiến thuật, nhập vai) — mỗi lần mở game là một thế giới khác. Ảnh mw-01 là map thị trấn miền Tây, mw-02 là làng chài câu cá: hai "game" khác nhau trong cùng một app.
- Sinh tồn nhiều biome + hang/dungeon; hàng trăm skin/thú cưỡi/thú cưng; chế độ chơi chuyển đổi tự do.

**(b) Áp được vào chợ Đà Lạt:**
- UGC quy mô thật không khả thi cho bản web hiện tại — nhưng **phiên bản rút gọn rất hợp chợ**: một ô sạp trống để người chơi "thuê sạp" — chọn mặt hàng (trong danh mục chợ thật), chọn kiểu trang trí, treo biển tên của mình (checklist 19). Đây chính là cơ chế làm Township/Mini World không bao giờ giống nhau giữa hai người chơi.
- Bài học phụ từ 2 ảnh: mỗi khu vực của họ có **chủ đề thị giác tách bạch** (miền Tây ≠ làng chài: khác palette, khác vật liệu, khác đèn). Các district của chợ hiện khác nhau chủ yếu bằng biển tên; nên cho mỗi khu một dấu ấn vật liệu/đèn riêng (khu ăn = đèn vàng + ghế nhựa xanh; khu len = bạt ấm + hàng treo; khu hoa = sáng + nhiều chậu) — một phần đã có mầm ở v4, cần đẩy thành quy tắc khi thêm nội dung mới.

### 2.4 Township (Playrix)

Nguồn: Google Play + App Store (mô tả chính thức), iphoneappsarena, pocketapk; ảnh `competitors/ts-01.png` (thị trấn nhìn từ trên cao), `ts-02.png` (sở thú).

**(a) Đa dạng ở đâu:**
- **Chuỗi sản xuất nhiều tầng:** trồng trọt → nhà máy chế biến → đơn hàng qua trực thăng/tàu hỏa/máy bay. Cùng một nguyên liệu đi qua nhiều nơi, nên bản đồ có "việc" liên kết nhau thay vì các đảo rời (ảnh ts-01).
- **NPC có đơn hàng và tính cách:** cư dân đưa yêu cầu cụ thể; hoàn thành đơn mở khóa nội dung mới.
- **Bộ sưu tầm có trưng bày:** sở thú nuôi + lai giống thú (ảnh ts-02), bảo tàng trưng bày hiện vật khai quật từ mỏ.
- **Sự kiện theo mùa liên tục:** regatta co-op theo mùa + Season Pass theo chủ đề (Western, Halloween, Alpine, Christmas) + sự kiện ~20 ngày — thị trấn "thay áo" quanh năm.
- **Trang trí số lượng lớn:** kể cả landmark nổi tiếng (Big Ben, tượng Nữ thần Tự do) để mỗi thị trấn một diện mạo.

**(b) Áp được vào chợ Đà Lạt:**
- **Đơn hàng NPC** là mục áp nguyên vẹn được nhất (checklist 12): khách đưa đơn "mua hộ" vài món ở các sạp khác nhau — dùng nguyên hệ thống sạp/túi/Xu sẵn có, biến mua sắm rời rạc thành hành trình có câu chuyện, và buộc người chơi đi qua nhiều khu (tự nó tạo cảm giác đa dạng).
- Thay áo theo mùa → **decoration theo lễ thật của chợ**: Tết (mai/đào, câu đối), Trung thu (lồng đèn sao — ảnh thật research/11 đã có đèn sao ở thang cầu vồng), Noel (thông + đèn ấm). Chợ thật Đà Lạt đúng là đổi trang trí theo mùa lễ.
- Bộ sưu tầm trưng bày → "Sổ đặc sản" trong hộ chiếu (đi cùng ý sưu tầm theo giờ của Play Together ở 2.2).

---

## PHẦN 3 — CHECKLIST ĐA DẠNG (19 mục, xếp theo tác động/effort)

Đã loại: đường vào/spawn, mặc định tối + tông ấm cảnh, đồi thông/sương/hoa, nhiệm vụ dẫn đường, minimap (đang làm ở v4.1). "Đặt ở đâu" bám địa hình thật của chợ (research/11).

| # | Mục | Làm gì + đặt ở đâu | Vì sao bớt lặp | Dựa trên | Effort |
|---|---|---|---|---|---|
| 1 | **Thẻ tên lơ lửng cho tiểu thương & NPC đặc biệt** | Sprite pill nâu chữ kem "Tên – Nghề" cho ~20 tiểu thương + Chú Ba + ca sĩ; thẻ "Bạn" cho người chơi; khách thường hiện tên khi đến gần | 85 người vô danh → những "người quen" có danh tính; mắt có điểm neo, cảnh đông trở nên có câu chuyện | CHOT gap 9; NP np-01; mau-np-01 | S |
| 2 | **UI nâu ấm bo tròn đồng bộ ảnh chốt** | Panel/bảng nhiệm vụ/nút chuyển sang nâu đậm + viền kem + bo góc lớn; nút chính vàng ấm | Đổi cảm giác "app xám lạnh" → "chợ ấm" ở mọi khung hình, kể cả khi không nhìn cảnh | CHOT gap 10; NP (UI nâu) | S |
| 3 | **Biển sạp có GIÁ + hình món** | Vẽ lại texture biển: vân gỗ, chữ bóng nổi, dòng giá, 1–2 icon món/sạp | Biển từ "nhãn tên" thành "thực đơn nhìn" — mỗi sạp khác nhau ngay ở thứ đập vào mắt đầu tiên | CHOT gap 1 | S |
| 4 | **Cành thông + lá phủ nóc sạp** | 2–3 cụm cành lá gắn ngẫu nhiên trên nóc ~15 sạp + dây đèn nhỏ quấn ở vài sạp | Camera 45° nhìn nóc là chính — lớp này phá sự đồng loạt của hàng nóc bạt giống hệt nhau | CHOT gap 6 | S |
| 5 | **Giỏ mây dâu tây + chậu cây ở chân sạp** | Giỏ dâu đỏ + chậu hoa/sen đá đặt cụm lệch hàng trước ~10 sạp ở trục chợ đêm + quanh bùng binh | Lấp "vùng chết" chân sạp; dâu đỏ là điểm màu nhận diện Đà Lạt lặp lại có chủ đích | CHOT gap 7; mau-np-01; research/11 §5 | S |
| 6 | **Cột hơi nước đọc được tại điểm chế biến** | Sprite mềm 2 lớp, cao/dày theo món và trạng thái nấu; đặt ở nồi sữa, bếp chè, phin cà phê, vỉ nướng | Hơi là tín hiệu sống mạnh nhất trong ảnh chốt; hiện tại gần như vô hình ở góc toàn cảnh | CHOT gap 4 | S |
| 7 | **Texture nền lát đá** | Canvas lát đá có khe + vết bẩn cho quảng trường, đường chợ, bậc thang | Nền phẳng màu là thứ "game rẻ" dễ thấy nhất khi lia camera; đá lát neo mọi vật đứng lên trên nó | CHOT gap 8 | M |
| 8 | **Bộ bày hàng riêng cho từng họ sạp** | 4–5 set: đồ uống nóng (hũ, chồng ly, ly mang đi), nướng (vỉ + bánh xếp hàng), kem–dâu (thùng kem, hộp dâu), lưu niệm (vòng treo móc khóa), hoa (xô hoa cao thấp) | Bỏ biển đi vẫn biết sạp bán gì — hết cảnh "quầy nào cũng như quầy nào" | CHOT gap 2; research/11 §5 | M |
| 9 | **Đạo cụ cầm tay cho tiểu thương** | Ấm rót / xẻng lật / muôi khuấy / cân tay gắn tay phải, khớp với hoạt ảnh sẵn có | Hoạt ảnh tay không hiện tại đọc như "vẫy tay"; có đạo cụ là thành "đang làm nghề" | CHOT gap 3 | M |
| 10 | **Lồng đèn giấy lớn + tua đỏ giăng nhiều cao độ** | Đèn khổ lớn 2–3 cao độ + dây giăng ở quảng trường, đường vào, hẻm ăn (trục Âm Phủ giữ điểm sáng từng sạp theo ảnh thật) | Tạo "trần ánh sáng" và nhịp dọc — khung cảnh có thêm một lớp trên đầu thay vì chỉ ở mặt đất | CHOT gap 5; research/11 §6 | M |
| 11 | **Đơn hàng "mua hộ" của khách NPC** | Khách ở quảng trường/bậc thang đưa đơn 2–3 món từ các sạp khác nhau; giao đủ nhận Xu + điểm thân thiện; đơn đổi theo giờ | Biến mua sắm rời rạc thành hành trình có mục đích qua nhiều khu — đa dạng bằng HÀNH VI, không cần model mới | Township (đơn hàng NPC) | M |
| 12 | **Nội thất nhà lồng có chiều dọc** | Khay hàng nghiêng bậc thang theo màu, áo len/khăn treo dải gradient, dây đèn bóng nhỏ dọc lan can lửng, sàn họa tiết kim cương | Trong nhà hiện "phẳng một tầng mắt"; thêm lớp tường/lan can/sàn là thêm 3 bề mặt để mắt đi | plan/A4; research/11 §1.4 | M |
| 13 | **Sự kiện hẹn giờ + đèn lồng điều ước** | Đếm ngược công khai tới lúc lên đèn chợ đêm; người chơi treo 1 đèn lồng ghi lời nhắn ở quảng trường (lời nhắn mẫu + của mình), đèn ở lại cả buổi tối | Học "thời khóa" của NP: giờ giấc thành sự kiện; lời nhắn làm quảng trường khác nhau mỗi phiên chơi | NP np-03 + đèn hoa đăng (research/01) | M |
| 14 | **Mèo đi theo người chơi** | 1 mèo nhỏ (từ model sẵn/đơn giản hóa) đi theo sau người chơi, ngồi chờ khi mua hàng; nhận qua nhiệm vụ hoặc mua ở sạp lưu niệm | Mọi đối thủ đều có pet/linh thú vì nó cá nhân hóa nhân vật chính — người chơi hiện là "một mình giữa chợ" | NP (linh thú); PT (pet) | M |
| 15 | **Cầu thang cầu vồng + khung check-in** | Sơn cầu thang phụ theo dải cầu vồng, treo lồng đèn sao (đúng ảnh thật), thêm khung chụp ảnh + điểm tương tác chụp hình lưu khoảnh khắc | Điểm check-in thật nổi tiếng của chợ chưa hề có trong game; là "landmark thứ hai" ngoài tượng đài | research/11 ảnh 11 + §3 | M |
| 16 | **Chợ phiên đầu mối sáng sớm cuối tuần** | Khung 5–7h trong game, cuối tuần: thêm sạp rau bán buôn ở sân sau/sườn chợ, giá sỉ khác giá lẻ, sương dày, đèn vàng còn sáng | Khu vực "mở theo giờ" thứ hai (sau chợ đêm) — cùng một bản đồ, hai bộ mặt khác giờ | PT (Lost Island giới hạn giờ); research/11 (chợ đầu mối thật) | M |
| 17 | **Xe đẩy/gánh hàng rong di động + xe đạp ở sạp rau** | 1–2 xe đẩy (xiên nướng/bánh tráng) đi chậm dọc trục có khói nhẹ + dừng bán; xe đạp dựa tĩnh ở sạp rau quảng trường | Hàng rong di động là sinh hoạt thật của chợ; vật chuyển động "có việc" khác hẳn NPC đi dạo | research/11 §5; plan/A3; mau-np-01 | M |
| 18 | **Chi tiết mặt tiền: đồng hồ + cờ nhỏ + chậu hoa ban công** | Đồng hồ chạy giờ thật trên mặt tiền nhà lồng, cờ nhiều màu ở ban công tầng 2, chậu hoa dọc lan can mặt tiền | Mặt tiền là khung hình được nhìn nhiều nhất; 3 chi tiết nhỏ này là thứ ảnh A3 có mà bản dựng thiếu — và không mâu thuẫn ảnh thật | plan/A3 | S |
| 19 | **"Sạp của bạn" — ô sạp cho người chơi thuê** | 1 ô trống ở hẻm ăn: người chơi chọn mặt hàng (danh mục chợ thật), 1 trong 3 kiểu trang trí, biển ghi tên mình; NPC khách ghé mua thụ động sinh Xu nhỏ | UGC rút gọn kiểu Mini World/Township: thế giới khác đi vì NGƯỜI CHƠI; cho mục tiêu dài hạn ngoài hộ chiếu | Mini World (UGC); Township (decoration) | L |

**Thứ tự gợi ý khi bắt tay làm:** 1 → 2 → 3 (ba mục S đổi cảm giác toàn cục) → 4, 5, 6 (vẫn S, hoàn thiện cấp sạp của ảnh chốt) → 8, 9 (M, hoàn thiện "chân dung sạp") → 11 (M, đa dạng bằng hành vi) → các mục còn lại theo nguồn lực.
