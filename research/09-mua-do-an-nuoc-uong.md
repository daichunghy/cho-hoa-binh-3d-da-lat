# 09 — Cơ chế mua đồ ăn / nước uống trong game & cách nối ra mua thật

> Phạm vi: nghiên cứu cơ chế gọi món – chế biến – ăn/uống trong game và thế giới ảo,
> và các mô hình biến "món ăn ảo" thành doanh thu thật (đơn hàng thật, affiliate, voucher, tài trợ quầy).
> Áp dụng cuối tài liệu: đề xuất cụ thể cho **Chợ Hòa Bình 3D — Đà Lạt**.
> Chỉ nghiên cứu, chưa phải đặc tả triển khai.

---

## 0. Kết luận nhanh (đọc 1 phút)

1. **Vòng lặp chuẩn của mọi game bán đồ ăn hay** đều là 5 bước: *tới quầy xem menu → chọn món (+ tuỳ biến) →
   NPC/người chơi chế biến có thời gian chờ nhìn thấy được → nhận món tại quầy → ăn/uống có hoạt cảnh + hiệu ứng (buff)*.
   Thiếu bước "chờ và xem chế biến" là mất nửa cái vui; thiếu "ăn có hiệu ứng" là món ăn chỉ còn là icon trong túi đồ.
2. **Buff phải gắn với việc khám phá**, không gắn với chiến đấu: với một thế giới tham quan như chợ Đà Lạt,
   chỉ cần 2 thanh trạng thái — **Ấm** (chống sương lạnh ban đêm) và **Năng lượng** (để leo dốc, đi bộ xa) —
   cộng thêm hiệu ứng xã hội (mời bạn, chụp ảnh món, emote).
3. **Nối ra tiền thật có 5 tầng**, từ nhẹ tới nặng: (1) phát mã ưu đãi/món miễn phí trong game → dùng ngoài đời,
   (2) link affiliate cho đặc sản ship được toàn quốc, (3) voucher đặt trước để tới Đà Lạt dùng tại quầy đối tác thật,
   (4) đặt giao tận nơi cho người đang ở Đà Lạt (qua GrabFood/ShopeeFood/Zalo OA của quán thật),
   (5) cho thương hiệu thuê quầy ảo / ra mắt món mới trong game trước.
   Chipotle, Wendy's, Jimmy John's, Domino's đều đã làm thật ít nhất một trong các tầng này.
4. **Món nóng ăn tại chỗ (bánh tráng nướng, sữa đậu nành) không ship toàn quốc được** — chúng là "mồi" tạo thèm và bán voucher/trải nghiệm.
   **Món khô ship được (mứt, hồng treo gió, trà atiso, cà phê hạt, dâu sấy) mới là hàng affiliate/e-commerce chính.**
   Tách rõ hai nhóm này ngay từ thiết kế menu là quyết định quan trọng nhất của file này.
5. Bài học từ Chipotle: nối ảo → thật cho số liệu rất đẹp trong tuần lễ sự kiện (4,1 triệu lượt chơi tuần đầu)
   nhưng lưu lượng rớt mạnh ngoài cửa sổ khuyến mãi. Muốn sống lâu phải có lý do quay lại hằng ngày
   (nhiệm vụ ăn uống, món giới hạn theo mùa, quầy mới), không chỉ có mã miễn phí.

---

## 1. Cơ chế trong game

### 1.1. Luồng gọi món tại quầy (order flow)

Mẫu số chung từ FiveM Restaurant Creator, Roblox Restaurant Tycoon, các game quán ăn trên Steam:

| Bước | Cách làm hay | Ghi chú thiết kế |
|---|---|---|
| 1. Tới quầy | NPC tiểu thương chào bằng thoại ngắn + bong bóng "Xem menu?"; bảng hiệu treo giá nhìn từ xa | Người chơi phải *nhìn thấy* món và giá trước khi bấm, như chợ thật |
| 2. Mở menu | Menu là bảng/kiosk tại quầy: chia nhóm (Ăn nóng / Nước nóng / Tráng miệng / Mang về), mỗi món có hình 3D/ảnh, giá tiền ảo, thời gian làm, độ "đặc sản" (sao) | Đừng mở một cửa sổ shop toàn màn hình kiểu e-commerce — mất cảm giác đang đứng ở quầy |
| 3. Tuỳ biến món | Chọn size, topping, mức đường/đá, thêm topping tính tiền thêm (kiểu Chipotle/Domino's: tự ráp món của mình) | Tuỳ biến là chỗ người chơi "sở hữu" món — cũng là dữ liệu để nối ra đơn thật sau này |
| 4. Thanh toán | Trả bằng tiền ảo trong giỏ/túi; hiện số thứ tự đơn (order number) | Số thứ tự tạo cảm giác chợ thật và cho phép nhiều người cùng chờ |
| 5. Chế biến | Đơn hiện lên "bảng bếp"; NPC đi lấy nguyên liệu → nấu/nướng/pha → bày lên quầy (xem mục 1.2) | Thời gian chờ 10–40 giây tuỳ món; cho người chơi đứng xem hoặc đi quầy khác quay lại khi có thông báo |
| 6. Nhận món | Tên/số đơn sáng lên bảng "món đã xong"; tới quầy bấm nhận, món vào **khay/giỏ đi chợ** | Mô phỏng bảng Kitchen Orders / Ready-for-Pickup của FiveM rất hiệu quả |
| 7. Ăn/uống | Ngồi ghế/bậc thềm gần quầy hoặc ăn tại chỗ; hoạt cảnh ăn từng miếng/uống từng ngụm (mục 1.3) | Ăn xong mới nhận buff + tem "đã thử món này" |

**Giỏ hàng trong thế giới ảo nên là vật nhìn thấy được** — giỏ đi chợ / khay bưng / túi đặc sản nhân vật xách theo,
đổ đầy dần theo chuyến đi. Đây là khác biệt lớn so với "giỏ hàng" của web bán hàng: nó vừa là inventory,
vừa là vật phẩm khoe được, vừa là bản tổng kết chuyến đi ("hôm nay bạn đã ăn gì ở chợ Đà Lạt" — thẻ chia sẻ).

### 1.2. NPC chế biến — phần tạo "sự sống" cho quầy

- **Mẫu FiveM (The Mariner's Table, Restaurant Creator):** khi không có người chơi làm nhân viên,
  NPC đầu bếp tự chạy quy trình thật: đi tới kho lấy nguyên liệu → nấu/pha chế → mang ra quầy giao.
  Đơn của khách hiện trên màn hình bếp; món xong hiện trên bảng nhận món.
  Người chơi cũng có thể *đóng vai nhân viên* (thu ngân, đầu bếp, giao món) để kiếm tiền ảo — vòng lặp nghề nghiệp của Bloxburg / Work at a Pizza Place (Roblox).
- **Chất lượng món theo tay nghề (quality tier):** Genshin Impact chia món nấu ra 3 hạng
  *Suspicious / Normal / Delicious* theo mini-game canh vạch khi nấu — hạng càng cao buff càng mạnh và lâu.
  Áp dụng cho chợ: các món nướng/pha có mini-game canh lửa/canh thời gian 3–5 giây cho người chơi tự làm,
  hoặc NPC làm thì chất lượng ngẫu nhiên theo "tay nghề" của quầy (quầy nổi tiếng = tỉ lệ món ngon cao hơn).
- **Quá lửa / cháy:** hệ thống bếp FiveM và game quán gyudon trên Steam đều cho món *cháy* nếu để quá thời gian —
  tạo tiếng cười và lý do làm lại, đồng thời tạo nghề "canh bếp" cho người chơi thích vai nhân viên.
- **Nguyên liệu & tồn kho (nâng cao, giai đoạn sau):** quầy có thể hết nguyên liệu cuối buổi chợ,
  phải "nhập hàng" từ khu chợ đầu mối buổi sáng — chỉ nên làm khi đã có người chơi đóng vai vận hành quầy.

### 1.3. Ăn/uống có hiệu ứng (buff) — dịch từ game lớn sang thế giới tham quan

Các hệ thống tham chiếu:

- **Genshin Impact:** thức ăn chia 4 nhóm buff (Tấn công / Phòng thủ / Nguyên tố / Thể lực),
  mỗi nhóm chỉ 1 buff chạy cùng lúc, ăn món mới cùng nhóm sẽ ghi đè; có thanh "no" (fullness) chặn hồi máu vô hạn.
  Bài học: *phân nhóm buff + luật ghi đè + thanh no* là khung chống lạm dụng đơn giản mà hiệu quả.
- **Stardew Valley:** món ăn và đồ uống nằm ở **2 khe riêng**, cộng dồn được với nhau
  (cà phê +1 Tốc độ; trà xanh +30 Năng lượng tối đa). Bài học: cho phép 1 món ăn + 1 món uống chạy song song —
  đúng thói quen thật ("bánh tráng nướng + sữa đậu nành") và khuyến khích mua combo.
- **Animal Crossing: New Horizons:** ăn trái cây tích "năng lượng" (tối đa 10) để làm việc nặng
  (nhổ cây, phá đá). Bài học: buff ăn uống nên *mở khoá hành động khám phá*, không chỉ cộng số.

**Dịch sang Chợ Hòa Bình 3D — chỉ giữ 3 hiệu ứng, dễ hiểu với người chơi casual:**

| Hiệu ứng | Nguồn | Tác dụng trong chợ |
|---|---|---|
| **Ấm bụng** (thanh Ấm) | Món/nước nóng: sữa đậu nành, khoai nướng, súp, chè nóng | Thanh Ấm tụt dần khi đi trong sương/đêm lạnh và ở khu ngoài trời lâu; về 0 thì nhân vật run, đi chậm, màn hình mờ sương. Ăn nóng nạp lại. Đây là "cơ chế thời tiết Đà Lạt" biến thành gameplay |
| **Năng lượng / khoẻ chân** | Món ăn no: bánh tráng nướng, bánh mì, xiên nướng | Leo dốc (khu Hòa Bình toàn dốc!) và đi bộ giữa các khu chợ tốn năng lượng; ăn no đi nhanh hơn, mở lối tắt leo dốc |
| **Tỉnh táo / vui vẻ (xã hội)** | Cà phê, trà atiso, kem bơ, dâu lắc | Cà phê: +tốc độ chạy ngắn; món ngọt/tráng miệng: mở emote đặc biệt, hiệu ứng tim/bong bóng khi chụp ảnh, tăng điểm khi mời bạn cùng ăn |

Quy tắc chống lạm dụng: thanh **No** (ăn quá nhiều trong thời gian ngắn thì nhân vật "no quá", phải đi dạo một lúc mới ăn tiếp),
mỗi nhóm hiệu ứng chỉ 1 buff, thời lượng buff tính bằng phút thật (2–10 phút).

### 1.4. Tiền ảo và kinh tế quầy hàng

- **Hai lớp tiền tệ (mẫu Animal Crossing: Bells + Nook Miles; Roblox: tiền việc làm + Robux):**
  - **Xu Chợ** (tiền mềm): kiếm bằng đi chợ, làm nhiệm vụ, làm ca tại quầy, bán lại nông sản nhặt được.
    Dùng mua đồ ăn/nước uống ảo và vật phẩm thường. *Đồ ăn ảo chỉ nên bán bằng tiền mềm* — ăn uống là vòng lặp cốt lõi, không nên paywall.
  - **Xu Hoa / điểm thưởng** (điểm gắn bó): nhận khi check-in quầy, thử món mới, quay lại nhiều ngày.
    Đổi skin, áo len cho nhân vật, khung ảnh — và ở tầng nối thật: đổi voucher (mục 2).
- **Người chơi kiếm tiền bằng nghề ăn uống:** làm ca 3 phút tại quầy (nhận đơn, canh bếp, giao món cho NPC khách)
  là nội dung chơi lặp lại tốt nhất của thể loại này (Bloxburg, Restaurant Tycoon) — nên có ít nhất 1 quầy cho người chơi tự vận hành.
- **Giá cả & "chợ" thật:** giá món thay đổi nhẹ theo giờ (chợ sáng rẻ rau, chợ đêm đắt món nóng),
  một món "đặc sản ngày" giá tốt — học cơ chế giá củ cải biến động theo buổi của Animal Crossing nhưng ở mức nhẹ, không làm đầu cơ.
- **NPC khách hàng:** ngoài người chơi, NPC du khách cũng xếp hàng mua, ngồi ăn, khen món —
  chợ đông và sống ngay cả khi ít người chơi online (bài học từ Sansa/chùa online: hiện diện đông tạo cảm giác "đang đi chợ thật").

### 1.5. Sưu tầm & nhiệm vụ ăn uống (lý do quay lại)

- **Sổ tay ẩm thực / Hộ chiếu chợ:** mỗi món có 1 tem; ăn lần đầu = đóng tem. Đủ bộ theo khu (khu ăn đêm, khu đặc sản...) mở quà.
- **Nhiệm vụ ngày:** "Thử 1 món nóng", "Mời 1 người bạn uống sữa đậu nành", "Tìm quầy bán dâu rẻ nhất hôm nay".
- **Combo địa phương có thật:** game gợi ý combo dân Đà Lạt hay ăn (sữa đậu nành + bánh su kem; bánh tráng nướng + dâu lắc)
  và thưởng khi ăn đúng combo — cách dạy văn hoá ẩm thực mà không cần bảng chữ dài.
- **Món theo mùa/sự kiện:** mùa hồng (hồng treo gió), mùa dâu, lễ hội hoa — món giới hạn thời gian là động cơ quay lại và là chỗ ra mắt sản phẩm thật (mục 2, tầng 5).

---

## 2. Ví dụ thực tế đã có người làm

### 2.1. Trong game / thế giới ảo thuần tuý

| Ví dụ | Cơ chế đáng học | Nguồn |
|---|---|---|
| FiveM — Restaurant Creator / The Mariner's Table (GTA RP) | Kiosk gọi món có giỏ hàng + số đơn; bảng bếp & bảng nhận món; mini-game nấu từng công đoạn, món cháy được; NPC nấu thay khi không có nhân viên; ăn/uống có hoạt cảnh, độ bền món giảm theo từng miếng/ngụm; hồi đói/khát | quasar-store.com/docs/restaurant-creator; forum.cfx.re/t/the-mariners-table-esx-qb-qbox/5417248 |
| Roblox — Restaurant Tycoon 2/3, Work at a Pizza Place, Bloxburg (Pizza Planet, Bloxy Burger) | Người chơi luân phiên vai khách / thu ngân / đầu bếp / giao hàng; gọi món qua điện thoại trong game và NPC giao tới nhà; tiền lương theo ca | robloxgames.org (Pizza Factory Tycoon / Restaurant Tycoon); welcome-to-bloxburg.fandom.com/wiki/Pizza_Planet |
| Genshin Impact | 4 nhóm buff, luật ghi đè cùng nhóm, thanh no, 3 hạng chất lượng món theo mini-game nấu, nhân vật có "món đặc biệt" | hostedgg.com/blog/genshin-impact-cooking-food-buffs-guide |
| Stardew Valley | Khe món ăn và khe đồ uống tách riêng, cộng dồn; cà phê tăng tốc độ; ăn để lấy năng lượng làm việc | playerecho.com/stardew-valley/cooking-guide; stardewvalleywiki.com (Energy) |
| Animal Crossing: New Horizons | Ăn trái cây tích năng lượng để làm việc nặng; 2 tiền tệ Bells + Nook Miles; giá mua/bán biến động theo buổi | game8.co/games/Animal-Crossing-New-Horizons/archives/354644; acnh.co/nook-miles |

### 2.2. Ảo → thật: thương hiệu F&B đã làm

| Ví dụ | Cách nối ra thật | Kết quả / bài học |
|---|---|---|
| **Chipotle — Burrito Builder & Grill Simulator (Roblox, 2022)** | Người chơi tự cuốn burrito trong game, nhận tiền ảo *Burrito Bucks*; 100.000 người đầu tiên đổi được **mã món chính miễn phí dùng trên app/web Chipotle thật**. Ra mắt món mới (Garlic Guajillo Steak) đồng thời ngoài đời và trong metaverse, chơi game để nhận mã dùng thử món thật | 4,1 triệu lượt chơi tuần đầu, 6 triệu tổng; hãng tự nhận là thương hiệu đầu tiên cho đổi tiền trong trải nghiệm ảo lấy đồ thật. Nhưng traffic rớt còn ~4.000 người/ngày ngoài đợt khuyến mãi → phải có nội dung sống tiếp sau sự kiện (newsroom.chipotle.com 13/09/2022; qsrmagazine.com; beta.campaignlive.com) |
| **Wendy's — Wendyverse (Horizon Worlds, 2022)** | Nhà hàng ảo đầy đủ: vào sau quầy trải nghiệm như nhân viên, ngồi bàn ăn đồ ảo cùng bạn; mini-game thắng **mã giảm giá / món miễn phí dùng tại cửa hàng thật** và qua app Wendy's | #1 thế giới được thăm nhiều nhất Horizon lúc ra mắt, trung bình 11,5 phút/lượt chơi. Bài học: phần thưởng thật nhỏ nhưng rõ ràng (tải app → nhận nuggets miễn phí) là cầu nối rẻ và hiệu quả (winning.work/work/2755-wendyverse; franchisewire.com; arinsider.co/2022/10/12/what-can-we-learn-from-the-wendyverse) |
| **McDonald's / Panera Bread (2022)** | Đăng ký nhãn hiệu "nhà hàng ảo có giao hàng tận nhà": đang chơi trong metaverse, đói thì vào nhà hàng ảo gọi món, món thật giao tới nhà. McCafé ảo kèm sự kiện/concert ảo | Mới ở mức nhãn hiệu/kế hoạch, chưa thành sản phẩm đại trà → tầng "đặt giao ngay trong thế giới ảo" là đích đến dài hạn, không phải MVP (cointelegraph.com/news/mcdonalds-files-trademarks-for-mcmetaverse-restaurants-that-deliver) |
| **Jimmy John's — Metasandwich (Decentraland, 2022)** | Người chơi tự ráp sandwich tuỳ ý trong nhà hàng ảo, **đặt mang về (pickup) ngoài đời thật được**, và gửi dự thi để món thắng cuộc thành món thật bán giới hạn; kèm mã khuyến mãi và merch | Mẫu "món do người chơi sáng tạo → thành món thật" rất hợp cho cuộc thi topping bánh tráng nướng (restaurantdive.com/news/pizza-hut-jimmy-johns-metaverse-NFT-decentraland/624148) |
| **Domino's — Pizza Hero & New Pizza Chef AR** | Game làm pizza trên iPad: dùng đúng thao tác đã luyện trong game để **tự ráp chiếc pizza của mình rồi bấm đặt — pizza thật được giao tới**; bản AR cho kéo-thả topping lên pizza ảo đúng tỉ lệ thật | Chứng minh "giao diện ráp món kiểu game" chuyển đổi thành đơn thật tốt hơn form chọn món khô khan (kotaku.com — Domino's iPad game; realitytechnologies.com — Domino's AR Pizza Chef) |
| **Pinduoduo — Duoduo Orchard (Trung Quốc)** | Trồng cây ăn quả ảo bằng nhiệm vụ hằng ngày + mời bạn; cây "chín" thì nền tảng **gửi một thùng trái cây thật miễn phí về nhà**. Mua sắm trong app được thưởng "nước tưới" | >11 triệu người chơi/ngày ở giai đoạn đầu; game trở thành kênh kéo người dùng và chuyển họ thành người mua thật. Đây là mẫu mạnh nhất cho món nông sản: *chăm cây dâu ảo ở Đà Lạt → nhận hộp dâu/mứt thật* (techinasia/pushtech.asia — Why is Shopee getting you to plant virtual trees; pmc.ncbi.nlm.nih.gov/articles/PMC11673948) |
| **Shopee Farm (Đông Nam Á / Việt Nam)** | Trồng "cây voucher / cây xu / cây sản phẩm", tưới bằng nhiệm vụ (đăng nhập, mua hàng, mời bạn tưới hộ); thu hoạch nhận **voucher, xu hoặc mã miễn phí 100% mua sản phẩm thật** trong ví voucher | Cho thấy người Việt đã quen cơ chế chơi → nhận voucher → mua thật; phần thưởng có hạn dùng (thường hết tháng sau) để ép chuyển đổi (vuahoanhatminh.vn — cách chơi trồng cây Shopee; chanhtuoi.com — Nông trại Shopee) |
| **Kichi-Kichi × AhaChat (Việt Nam)** | Mini-game vòng quay trên Messenger/Fanpage: chia sẻ cho bạn để thêm lượt; trúng **voucher 100K, combo buffet, quà ăn uống thật** | 59.186 lượt tham gia/45 ngày, phát >1.000 voucher — mô hình phát voucher qua mini-game + viral chia sẻ chạy được với F&B Việt Nam mà không cần thế giới 3D (wbn.ahachat.com/kichi-kichi) |
| **"Tiệm phở của anh Hai" (Việt Nam, 2025)** | Game quán phở nhỏ gây sốt; hàng loạt thương hiệu thật (Xanh SM, Thiên Long, Diêm Thống Nhất...) chen vào đặt chi tiết/sản phẩm cạnh tiệm phở ảo | Bằng chứng thị trường Việt: một không gian quán ăn ảo đủ dễ thương là thành "mặt bằng quảng cáo" — các nhãn tự tìm tới. Chợ Hòa Bình 3D nên thiết kế sẵn "quầy tài trợ" từ đầu (tuoitre.vn — Cơn sốt 'tiệm phở' và gamification) |

### 2.3. Social commerce — kênh bán đi kèm

- **Livestream bán hàng trong bối cảnh chợ:** quầy ảo có giờ "mở live" — người bán thật livestream (TikTok Shop / Shopee Live)
  ngay tại quầy tương ứng trong game; người chơi đứng xem trong thế giới 3D, bấm vào món đang live để sang trang mua.
  Đây là ghép nối nhẹ nhất giữa "đi chợ ảo" và doanh số thật, không cần tự xây thanh toán.
- **Zalo OA / Zalo Mini App cho F&B (Việt Nam):** đặt món (e-ordering), tích điểm, đổi voucher ngay trong Zalo không phí sàn —
  là đích đến thực tế cho nút "đặt món thật" của các quầy đối tác ở Đà Lạt, thay vì tự làm app giao đồ ăn.
- **Voucher địa điểm (location voucher):** mã nhận trong game chỉ dùng được tại quầy thật ở Đà Lạt trong chuyến đi thật —
  biến người chơi online thành khách du lịch tương lai, và đo được chuyển đổi offline (mã nào được dùng, ở quầy nào).

---

## 3. Mô hình nối ra doanh thu thật (5 tầng, làm dần)

Nguyên tắc xuyên suốt: **trong game chỉ dùng tiền ảo; tiền thật chỉ xuất hiện ở bước nhảy ra ngoài**
(nút "Mua mang về nhà" / "Dùng voucher tại Đà Lạt") để không phá cảm giác đi chơi chợ,
và luôn ghi rõ link tài trợ/affiliate theo quy định quảng cáo.

| Tầng | Mô hình | Ai trả tiền | Độ khó | Phù hợp món nào |
|---|---|---|---|---|
| 1 | **Mã quà trong game → dùng ngoài đời**: hoàn thành nhiệm vụ ăn uống nhận mã giảm giá/món miễn phí tại quầy đối tác thật hoặc trên app sàn | Quầy/thương hiệu đối tác (chi phí marketing) | Thấp — chỉ cần sinh mã + trang điều kiện | Mọi món; đặc biệt món nóng ăn tại Đà Lạt |
| 2 | **Affiliate đặc sản ship toàn quốc**: dưới mỗi món có nút "Mua mang về": sang Shopee/TikTok Shop/Lazada của nhà bán thật, gắn UTM theo từng quầy để biết quầy nào bán giỏi | Hoa hồng affiliate 5–15% từ nhà bán | Thấp | Mứt, hồng treo gió, trà atiso, cà phê hạt/bột, dâu sấy, khoai lang sấy, rượu vang Đà Lạt |
| 3 | **Voucher đặt trước cho chuyến đi thật**: mua/gom điểm đổi voucher combo "đi chợ đêm Đà Lạt" (gói 5 món tại 5 quầy thật), dùng khi tới nơi, quét mã tại quầy | Người dùng trả trước; chia doanh thu với quầy thật | Trung bình — cần đối tác quầy thật + đối soát mã | Combo chợ đêm, tour ẩm thực |
| 4 | **Đặt giao tận nơi khi đang ở Đà Lạt**: người chơi ở gần khu Hòa Bình bấm đặt món nóng, đơn nhảy sang GrabFood/ShopeeFood/Zalo Mini App của quán thật | Người dùng; nền tảng giao đồ ăn ăn phí sẵn có | Trung bình — bản chất là deep-link, không tự giao | Bánh tráng nướng, sữa đậu nành, chè, súp cua... |
| 5 | **Thuê quầy ảo & ra mắt sản phẩm**: thương hiệu (cà phê, trà, mứt, ngân hàng, telecom...) thuê quầy trong chợ ảo theo tháng/sự kiện; ra mắt vị mới trong game trước, phát sampling code | Thương hiệu trả phí tài trợ | Cao — cần traffic chứng minh được | Sản phẩm mới, chiến dịch lễ/Tết/Lễ hội Hoa |

**Kênh doanh thu phụ:** bán vật phẩm ảo (skin áo len, giỏ đi chợ đặc biệt, emote) bằng tiền thật nạp —
chỉ bán đồ *trang trí*, tuyệt đối không bán buff ăn uống để giữ cân bằng và thiện cảm.
**Chỉ số cần đo từ ngày đầu:** lượt xem menu → tỉ lệ gọi món ảo → tỉ lệ bấm "mua thật" → tỉ lệ dùng mã (redemption) → doanh thu affiliate theo quầy.
Đây chính là số liệu dùng để bán Tầng 5.

**Rủi ro cần tránh:** (a) đừng hứa chất lượng món thật thay nhà bán — ghi rõ đơn vị bán/phục vụ;
(b) voucher phải có hạn dùng và điều kiện rõ (bài học Shopee Farm);
(c) không thu thập địa chỉ/số điện thoại trong game khi chưa cần — việc đó để sàn/Zalo OA xử lý ở bước mua thật;
(d) món có cồn (rượu vang Đà Lạt) chỉ đặt ở gian đặc sản mang về, có cảnh báo tuổi, không làm mini-game uống.

---

## 4. Đề xuất cụ thể cho Chợ Hòa Bình 3D — Đà Lạt

### 4.1. Bản đồ quầy ăn uống đợt 1 (đúng chất chợ đêm Hòa Bình)

Chợ đêm Đà Lạt (khu Hòa Bình, đường Nguyễn Thị Minh Khai) ngoài đời mạnh nhất ở nhóm món nóng chống lạnh và đặc sản mang về —
đợt 1 làm 6 quầy, mỗi quầy một "chữ ký gameplay" khác nhau để người chơi không thấy lặp:

| Quầy | Món chủ lực | Cơ chế riêng (gameplay signature) | Buff | Nối ra thật |
|---|---|---|---|---|
| **Sữa đậu nành nóng** | Sữa đậu nành / đậu xanh / đậu phộng nóng + bánh su kem, bánh sừng trâu | Chọn kiểu sữa & mức ngọt; NPC rót từ nồi bốc khói, phải *thổi nguội* (giữ phím) trước khi uống; combo kèm bánh ngọt được gợi ý đúng kiểu dân địa phương | Ấm bụng mạnh nhất; combo + thời gian buff | Tầng 1/3: voucher tại quầy sữa thật khi tới Đà Lạt. Sữa tươi không ship xa — không affiliate |
| **Bánh tráng nướng** ("pizza Đà Lạt") | Bánh tráng nướng trứng, tép, hành, phô mai, khô bò... | **Mini-game nướng than là quầy chủ lực:** người chơi tự chọn topping → NPC (hoặc chính người chơi làm ca) nướng trên bếp than, canh thanh lửa, lật bánh đúng lúc; cháy/giòn tan/ngon theo tay. Ráp topping tuỳ ý = "bánh tráng của tôi" lưu thành thẻ công thức chia sẻ được | Năng lượng + vui vẻ | Tầng 5/1: cuộc thi topping theo mùa kiểu Jimmy John's Metasandwich — combo thắng thành món thật ở quầy đối tác 1 tuần; voucher ăn tại chỗ (Tầng 3) |
| **Cà phê** (quầy cà phê vợt/phin nhìn ra dốc Hòa Bình) | Cà phê phin, cà phê vợt, cacao nóng | Ritual chờ phin nhỏ giọt theo thời gian thật rút gọn (20–30 giây ngắm sương) — quầy "sống chậm" để ngồi ngắm chợ; chọn hạt (arabica Cầu Đất làm điểm kể chuyện) | Tỉnh táo: +tốc độ chạy, xoá hiệu ứng mờ sương ngắn hạn | **Tầng 2 mạnh nhất:** cà phê hạt/bột Cầu Đất ship toàn quốc qua affiliate — món dễ ship, giá trị đơn cao, mua lặp lại |
| **Dâu tây & dâu lắc / kem bơ** | Dâu tươi, dâu lắc muối tôm, sinh tố/kem bơ | Mini-game lắc dâu (lắc đúng nhịp); cây dâu ảo ở góc vườn quầy: tưới mỗi ngày, "chín" thì nhận quà (mẫu Duoduo Orchard/Shopee Farm) | Vui vẻ/xã hội: emote trái tim, chụp ảnh đẹp | Tầng 2: mứt dâu, dâu sấy, siro dâu ship toàn quốc; Tầng 1: voucher hộp dâu tươi nhận tại Đà Lạt (dâu tươi không ship xa) |
| **Khoai lang nướng & bắp nướng** | Khoai lang mật nướng than, bắp nướng mỡ hành | Quầy vỉa hè ngồi ghế nhựa thấp — chỗ "nghỉ chân" xã hội: ngồi ăn chung bàn với NPC/người chơi khác, nghe kể chuyện chợ | Ấm bụng + hồi phục khi ngồi | Tầng 2 phụ: khoai lang sấy/mật ong; chủ yếu là quầy tạo không khí, không đặt nặng doanh thu |
| **Khu đặc sản mang về** (gian mứt – trà – hồng) | Mứt dâu/dâu tằm/khoai lang dẻo, hồng treo gió, trà atiso, trà ô long, rượu vang Đà Lạt (gian riêng, có cảnh báo tuổi) | Không ăn tại chỗ: người chơi **đóng hộp quà** — chọn món vào giỏ quà, gói giấy, thắt nơ (mini-game gói quà); giỏ quà ảo hoàn chỉnh mở nút "Đặt hộp quà y hệt gửi về nhà" | — (đây là quầy mua sắm) | **Tầng 2 chính của toàn dự án:** hộp quà đặc sản là sản phẩm affiliate/e-commerce hoàn hảo — ship toàn quốc, mua làm quà, đơn giá cao. Tầng 3: đặt trước, tới Đà Lạt nhận hộp đã đóng sẵn |

Quầy đợt 2 (sau khi có traffic): chè nóng / súp cua (buff Ấm), xiên nướng (làm ca nướng theo đơn NPC), bánh căn, yaourt phô mai, lẩu gà lá é (món nhóm — gọi theo nhóm bạn cùng chơi, ăn chung nồi, buff chia cả nhóm: cơ chế "ăn cùng nhau" chưa game chợ nào làm).

### 4.2. Luồng trải nghiệm mẫu (một phiên chơi 7 phút)

1. 19h, vào chợ (giờ trong game = giờ thật, chợ lên đèn) → thanh Ấm bắt đầu tụt vì sương.
2. Ghé quầy sữa đậu nành: gọi ly đậu nành + bánh su kem (combo được gợi ý) → xem NPC rót, thổi nguội, uống → Ấm đầy, nhận tem món #1.
3. Sang quầy bánh tráng nướng: tự chọn topping, tự nướng mini-game → ra bánh "Ngon" → ăn tại bậc thềm → đầy Năng lượng, lưu thẻ công thức.
4. Chụp ảnh khoe thẻ công thức → bạn bè thấy, vào chợ chơi cùng.
5. Ghé gian đặc sản: đóng hộp quà mứt + hồng treo gió cho mẹ → bấm "đặt hộp y hệt" → nhảy Shopee của nhà bán (affiliate) — *đây là khoảnh khắc chuyển đổi tiền thật duy nhất trong phiên, đặt ở cuối hành trình ăn chơi, không chen ngang lúc đang vui.*
6. Về cổng chợ: tổng kết "Tối nay bạn đã ăn 3 món — còn thiếu dâu lắc và cà phê để đủ bộ 5 món chợ đêm" → lý do quay lại ngày mai.

### 4.3. Lộ trình làm (đợt nhỏ, đo được)

- **Đợt A (ảo thuần tuý):** 6 quầy đợt 1, luồng gọi món 7 bước, NPC chế biến, 3 buff (Ấm / Năng lượng / Tỉnh táo–vui vẻ),
  Xu Chợ, sổ tay ẩm thực + nhiệm vụ ngày. Chưa tiền thật — đo tỉ lệ gọi món và thời gian ở lại.
- **Đợt B (nối thật nhẹ):** mỗi gian đặc sản + cà phê có nút affiliate (Tầng 2) gắn UTM theo quầy;
  phát mã voucher đối tác đầu tiên tại Đà Lạt (Tầng 1). Đo click-through và redemption.
- **Đợt C (đối tác):** combo voucher chợ đêm (Tầng 3), cuộc thi topping bánh tráng theo mùa,
  mở "quầy tài trợ" đầu tiên (Tầng 5) khi có số liệu traffic.
- **Đợt D (nâng cao):** người chơi làm ca tại quầy, đơn nhóm/lẩu nhóm, cây dâu ảo → quà thật, đặt giao tại Đà Lạt qua deep-link (Tầng 4).

### 4.4. Dữ liệu cần có trong thiết kế (để dev khỏi hỏi lại)

- Mỗi món cần các trường: `id, quầy, nhóm (ăn nóng/nước/tráng miệng/mang về), giá Xu Chợ, thời gian chế biến,
  topping cho phép, nhóm buff + độ mạnh + thời lượng, độ no, tem sưu tầm, link nối thật (loại tầng + URL/UTM), đối tác`.
- Trạng thái đơn: `đã gọi → đang làm (tiến độ %) → xong, chờ nhận → đã nhận → đã ăn (buff chạy)`.
  Bảng đơn ở quầy hiển thị tối đa các đơn đang chờ để tạo cảm giác đông khách.
- Mọi nút nhảy ra ngoài (affiliate/voucher) phải mở tab/trang mới và **không làm mất phiên chơi**.

---

## 5. Nguồn tham khảo

- FiveM Restaurant Creator — quasar-store.com/docs/restaurant-creator
- FiveM The Mariner's Table (NPC cooking, ăn/uống có độ bền món) — forum.cfx.re/t/the-mariners-table-esx-qb-qbox/5417248
- Roblox Restaurant Tycoon / Pizza Factory Tycoon — robloxgames.org; Bloxburg Pizza Planet — welcome-to-bloxburg.fandom.com/wiki/Pizza_Planet
- Genshin Impact cooking & food buffs — hostedgg.com/blog/genshin-impact-cooking-food-buffs-guide
- Stardew Valley cooking/energy — playerecho.com/stardew-valley/cooking-guide; stardewvalleywiki.com (Energy)
- Animal Crossing turnips & Nook Miles — game8.co/games/Animal-Crossing-New-Horizons/archives/354644; acnh.co/nook-miles
- Chipotle Burrito Builder / Grill Simulator — newsroom.chipotle.com (13/09/2022); qsrmagazine.com/news/chipotle-creates-burrito-builder-metaverse; beta.campaignlive.com (brands on Roblox)
- Wendyverse — winning.work/work/2755-wendyverse; arinsider.co/2022/10/12/what-can-we-learn-from-the-wendyverse; franchisewire.com (McDonald's/Wendy's in the metaverse)
- McDonald's metaverse trademarks — cointelegraph.com/news/mcdonalds-files-trademarks-for-mcmetaverse-restaurants-that-deliver
- Jimmy John's Metasandwich & Pizza Hut — restaurantdive.com/news/pizza-hut-jimmy-johns-metaverse-NFT-decentraland/624148
- Domino's Pizza Hero / AR Pizza Chef — kotaku.com (Domino's iPad game); realitytechnologies.com (AR Pizza Chef)
- Pinduoduo Duoduo Orchard — pushtech.asia/why-is-shopee-getting-you-to-plant-virtual-trees (Tech in Asia); pmc.ncbi.nlm.nih.gov/articles/PMC11673948
- Shopee Farm Việt Nam — vuahoanhatminh.vn/cach-choi-tro-trong-cay-shopee; chanhtuoi.com/nong-trai-shopee-o-dau-p5935
- Kichi-Kichi mini-game voucher — wbn.ahachat.com/kichi-kichi
- Gamification & "Tiệm phở của anh Hai" — tuoitre.vn (Cơn sốt 'tiệm phở' — doanh nghiệp Việt và trò chơi hoá)
- Zalo Engagement Solution cho F&B (e-ordering, loyalty, voucher) — advertisingvietnam.com
- Ẩm thực chợ đêm Đà Lạt / khu Hòa Bình — peacetour.com.vn (Ăn gì và mua gì tại chợ đêm Đà Lạt?); saigonstartravel.com/cho-dem-da-lat; mytour.vn (Kinh nghiệm chợ đêm Đà Lạt)

*Ghi chú độ tin cậy: số liệu Chipotle/Wendy's lấy từ thông cáo và báo ngành của chính hãng (có tính quảng bá);
số liệu Duoduo Orchard/Shopee Farm lấy từ báo cáo học thuật và báo ngành. Cơ chế game (FiveM, Genshin, Stardew, ACNH)
mô tả theo tài liệu/wiki cộng đồng tại thời điểm tra cứu 11/2026.*
