# Research 20b — Bổ sung V5.4: CHUYỂN ĐỘNG THẬT (từ video walking tour) + KIỂM CHỨNG SỐ ĐO

> Bổ sung theo lệnh của Chung Hy (09/11/2026): "nghiên cứu sâu ảnh tham khảo thôi —
> thiếu cái gì nữa?" — ảnh tĩnh chưa đủ: bổ sung (1) chuyển động thật từ các video
> walking tour đã dẫn ở research/16 + research/18 và (2) kiểm chứng số đo bằng nguồn
> bản đồ/báo chí trước khi chốt sửa nhóm A (đường/xe) và C (người).
>
> **Giới hạn tư liệu (nói thẳng, khớp research/18):** máy chủ bị YouTube chặn tải
> video (HTTP 429 + xác thực bot) nên KHÔNG trích được khung hình theo phút từ
> 14 video đã dẫn (4 ở research/16, 10 ở research/18). Bằng chứng chuyển động dưới
> đây dựng từ: ảnh bìa chính thức của chính các video đó (ảnh 28–37 trong
> `theme/real-market/`, là khung hình thật của video) + bộ ảnh thật 01–27 (đặc biệt
> 04 vệt sáng vòng đảo, 06/07 phố từ trên cao, 08/09/10 thang) + mô tả lộ trình/
> hành vi trong research/16 (nguồn Trip.com, vietnamtouristvn, Traveloka) +
> bài viết mô tả chợ đêm cập nhật 2026 (vietnamtravel.org, elitetour). Chỗ nào là
> suy luận từ khung tĩnh sẽ ghi rõ "suy từ khung tĩnh".

## 1. Chuyển động thật — 5 hành vi và đối chiếu game

### 1.1 Dòng xe quanh đảo: vòng TRỌN, ngược chiều kim đồng hồ (nhìn từ trên), chậm
- Ảnh 04 (trên cao, phơi sáng dài): vệt sáng xe chạy thành **vòng kín quanh đảo**,
  liên tục cả phía xa lẫn phía gần — dòng xe không quay đầu giữa chừng.
- Ảnh 28 (bìa Seoul Walker, mặt đất): ô tô ở đoạn gần camera (phía nam đảo) di
  chuyển **từ trái sang phải (tây → đông)**; xe ở đoạn tây đảo hướng xuống phía
  nam — tổ hợp này là **ngược chiều kim đồng hồ nhìn từ trên xuống** (đúng luật
  tay phải Việt Nam). Tốc độ cảm nhận: xe lăn bánh chậm giữa đám đông, mô tô len.
- Ảnh 01 (ngày): xe máy chạy vòng quanh đảo cả hai phía; vành đường vòng rộng
  ~1,5–2 làn ô tô.
- **Game:** ROUTE_RING_OUT/IN là 2 cung (140°→340°) ở bán kính 12.9/11.9 phía
  nam–tây đảo; xe đi hết cung thì `ringSwitch` lái chéo sang cung kia và quay
  ngược chiều (đi vòng ngoài, về vòng trong) — từ các góc nhìn chính (phía nam)
  cho đúng bức tranh thật: **đoạn nam đảo có xe hướng đông ở làn ngoài + xe
  hướng tây ở làn trong, tốc độ bị slowCapFor ép còn 3.0**. Lệch so với thật:
  (a) thật là vòng kín, game là 2 cung con thoi — đầu cung phía đông
  (−9.7,−0.8)/(−12.1,−1.7) nằm trên mặt đường mở (xe thật cũng quay đầu ở đó
  được) và đầu phía tây-bắc khuất sau đảo, nên lệch này **khó thấy khi chơi**;
  vòng kín đầy đủ không khả thi trong hình học game (phía đông đảo là đai
  thềm + chân thang). (b) Hướng vòng: game đi CCW ở chiều ra ✓ khớp thật.
  → **Kết luận: giữ nguyên, ghi nhận là đơn giản hoá có chủ đích.**
- Tốc độ: xe chạy trong code 6.0–6.5 (ring) / 6.2–7.4 (trục) và bị cap 3.0–3.5
  ở mọi vùng đông người (cung nam đảo, mặt tiền, đầu đường tây, dọc hàng sạp)
  — khớp cảm nhận video (xe bò chậm giữa đám đông, chỉ thoáng ở đoạn vắng).
  → Không đổi.

### 1.2 Người băng ngang đường vào: tự do, theo cụm, xe nhường bằng cách chậm
- Ảnh 28: nhiều cụm người băng **ngay giữa dòng xe vòng** ở mọi vị trí quanh
  đảo, không theo vạch cố định; người gánh hàng đi giữa lòng đường.
- Ảnh 32 (bìa Jonny Walk): người đứng nói chuyện + đi bộ **trên mặt đường**
  quanh vành đảo; ảnh 37 (SOURCES): có vạch sang đường ở quảng trường Hòa Bình
  nhưng hành vi chủ đạo vẫn là băng tự do.
- research/16 (gody.vn + quan sát video POV không lời bình): lộ trình đi bộ
  xuyên chợ đêm là len lỏi liên tục giữa sạp/xe, không có trục đi bộ cứng.
- **Game:** điểm sang đường chính thức tại AW node 4 (trên cung làn W phía tây
  đảo), node 5 (x −18.5, giữa 2 làn), node 8 (trước mặt tiền) + vùng chậm 2 làn
  x −44..−6; ngoài ra mọi tuyến wanderer đều băng làn ở góc dốc (audit V5.4:
  chỉ còn cảnh báo băng qua, 0 lỗi chạy dọc làn). Cơ chế nhường trong code là
  **theo VÙNG (slowCapFor)** chứ không phanh theo từng người (mô hình yield
  từng người chỉ có trong harness T11 như tư liệu thiết kế). So với thật: xe
  thật cũng chủ yếu **chậm lại theo khu vực đông** — xấp xỉ này chấp nhận được.
  → **Kết luận: khớp ở mức hành vi; không sửa.** (Nếu sau này muốn xe phanh
  trước từng người băng qua: việc riêng, cần sửa updateTraffic.)

### 1.3 Dòng người lên/xuống thang: hai chiều len giữa người ngồi, không có làn cố định
- Ảnh 08 (Zing): người ngồi ăn trên ghế nhựa **theo cụm 3–6 người ngay trên
  mặt bậc**, người đi bộ lên/xuống len qua phần bậc còn trống ở giữa/bên —
  không có làn đi riêng cố định; hai bên thang là mặt tiền shop sáng đèn.
- Ảnh 10: mật độ trên thang kín vai, dòng người vẫn di chuyển hai chiều.
- Ảnh 09 + research/16 (Trip.com ×3): "ghế đặt khắp mặt bậc", "ngồi ăn trên
  bậc ngắm dòng người" là hành vi đặc trưng; research/16 mục (b) đã chốt:
  thang = khán đài ăn uống + chợ phụ + điểm nhìn, giao thông chỉ là một phần.
- **Game:** người ngồi trên bậc có sẵn (statics ăn/ngồi trên thang + 2 sạp
  trên chiếu nghỉ khoainuong/suadau), tuyến wanderer + AW đi xuyên thang
  cả hai chiều (audit V5.4 đã rà: đi trên mặt bậc theo stairH, không chìm/
  không bay). Vị trí ngồi trong game tập trung ở mép bậc/cụm bàn — thật thì
  cụm ngồi rải khắp mặt bậc hơn. → **Khớp về cấu trúc; mức rải cụm ngồi là
  khác biệt mật độ, không sửa trong đợt này** (tăng statics trên bậc là việc
  trang trí riêng, không thuộc lỗi A/C).

### 1.4 Chỗ ĐỨNG CHỜ: vành đảo, trước mặt sạp, đầu thang/quảng trường
- Ảnh 32: người **ngồi thành hàng trên vành đảo** sau tượng + đứng chờ/nói
  chuyện trên mặt đường quanh đảo. Ảnh 28: đám đông đứng kín vành xa của đảo.
- Ảnh 29 (bìa Walking On, từ đỉnh thang): ghế nhựa xanh + người đứng/ngồi
  **dưới chân thang**; ảnh 36 (bìa Walking Asia): mascot + người bán bóng bay
  + đám đông **ở đầu thang/quảng trường Hòa Bình** — đầu thang là điểm tụ.
- research/16: đầu thang có thương xá La Tulipe, là điểm hẹn/điểm nhìn.
- **Game:** người ngồi vành nam đảo (RB_ARC + statics trên vành, y 0.93/0.55),
  hàng chờ trước mặt sạp (QUEUES dọc mặt tiền sau V5.4), người đứng ở đầu
  thang/đỉnh đồi có trong phân bố crowd hiện tại. → **Khớp; không sửa.**

### 1.5 NGỒI ĂN theo thời gian: ngồi LÂU, hướng ra dòng người
- research/16 (vietnamtouristvn): khách mua đồ ăn rồi tìm chỗ ngồi trên bậc
  "ngắm nhìn dòng người qua lại và thưởng thức" — hành vi **lưu lại lâu**,
  không phải ăn nhanh rồi đi. Ảnh 08/13: cụm ngồi giữ nguyên vị trí trong
  suốt khung hình đông; sạp nướng đặt ngay trên bậc (ảnh 13).
- **Game:** statics ngồi ăn là cố định lâu dài ✓ đúng bản chất; wanderer có
  dwell ở hàng chờ/browse trước sạp ✓. → **Khớp; không sửa.**

### 1.6 Cấu trúc phố đêm theo chiều dốc (bổ sung từ nguồn 2026)
- vietnamtravel.org (cập nhật 2026): chợ đêm nằm trên **sườn dốc đường
  Nguyễn Thị Minh Khai** từ khu Hòa Bình xuống bùng binh trước chợ; **phần
  trên (gần Hòa Bình + thang) là đồ ăn, phần dưới quanh bùng binh là quần
  áo/lưu niệm bày trên bạt**. elitetour: chợ chạy "từ cầu thang Hòa Bình
  đến cổng chợ", 19h–3h.
- **Game:** đường vào là dốc thật (entryRampY, đầu tây cao +2.0 → chợ ở 0) ✓
  hướng dốc khớp (từ phía Hòa Bình xuống chợ). Phân vùng ăn uống dọc đường
  vào + đặc sản/len quanh chợ ✓ tương ứng. → **Khớp; không sửa.**

## 2. Kiểm chứng số đo (bản đồ/báo chí) vs con số của research/20

Nguồn cứng tìm được (09/11/2026):
- **tinbds.com — hồ sơ đường Nguyễn Thị Minh Khai, Đà Lạt:** dài ~400m,
  **lòng đường rộng 10m, vỉa hè rộng 3m** (tức tổng hành lang đường 16m).
  Đây là mặt cắt CHUẨN của tuyến phố; đoạn trước chợ/bùng binh thực tế rộng
  hơn vì sạp tràn lòng đường (ảnh 07: "sạp chiếm lòng đường") + vành bùng binh.
- **nguyenphucorp.vn + VietKings (TOP 100 kỷ lục):** toà chợ **dài 80m,
  rộng 18m, cao 19.45m**, mỗi tầng 1.600m²; thang lộ thiên phía Lê Đại Hành
  **cao 17m, chia 3 đợt nghỉ** — khớp gần như tuyệt đối với game (đồi cao
  17u, stairH 3 chuyến × 5.67). Đây là neo tỉ lệ dọc tin cậy nhất: **1u ≈ 1m
  theo chiều cao**.
- **Nominatim/OpenStreetMap:** quan hệ "Chợ Đà Lạt" có bbox ≈ 107m × 135m
  (cả khuôn viên chợ + quảng trường, không phải chỉ toà nhà) — chỉ dùng làm
  mốc phụ. API hình học thô của OSM không trích được qua trình duyệt
  (trả XML không đọc được) — **không đo được trực tiếp từ bản đồ số trong
  đợt này**, ghi nhận là khoảng trống tư liệu.
- Khổ thang mặt tiền (thang "chợ Âm Phủ" từ bùng binh lên Hòa Bình): **không
  có số công bố**; ước lượng từ ảnh 08 + 10 (đếm bề ngang người trong đám
  đông đặc, vai ~0.45–0.55m/người ở mật độ đứng kín): **≈ 15–18m**.

Đối chiếu (neo 1u ≈ 1m theo chiều cao 17m):

| Hạng mục | Thật (nguồn) | Game V5.4 | Đánh giá |
|---|---|---|---|
| Lòng đường phố (mặt cắt chuẩn) | 10m + vỉa hè 3m×2 = 16m (tinbds) | hành lang hoạt động −7.95..12.25 ≈ 20.2u; lòng giữa 2 mặt tiền 13.5u | Game rộng hơn mặt cắt chuẩn ~+25% — **hợp lý cho đoạn trước chợ** (nơi sạp tràn lòng đường + vành bùng binh, ảnh 06/07); research/20 ghi ≈20u là con số ĐÚNG cho đoạn này, không phải 22u |
| Chiều cao đồi/thang chính | 17m, 3 đợt (báo chí ×2 nguồn) | 17u, 3 chuyến | ✓ khớp |
| Toà chợ | 80m × 18m | sảnh 68u × 16u (x −34..34, z 12..28) | Game nén ~−15% (diorama) — nhất quán với tỉ lệ nén chung |
| Khổ thang mặt tiền | ≈15–18m (ước lượng ảnh, sai số ±20%) | 22u (x −11..11) | Game rộng hơn ước lượng ~+20–40% — **ghi nhận lệch** (xem quyết định dưới) |
| Đảo bùng binh | Ø đảo hoa ~14–18m (ước lượng ảnh 01/04 theo bề ngang ô tô ~5m) | Ø 21u (R10.5) | Game nhỉnh hơn ~+15–30%, cùng khoảng lệch với khổ thang |

**Quyết định hiệu chỉnh:**
1. **Đường vào: KHÔNG đổi.** Con số research/20 (≈20u hành lang tại trục
   đảo) đứng vững khi đối chiếu: nó mô tả đoạn trước chợ + bùng binh chứ
   không phải mặt cắt chuẩn 16m của phố; lòng xe chạy 13.5u giữa 2 mặt tiền
   tương ứng lòng đường 10m + dải sạp/đậu tràn ra như ảnh thật.
2. **Khổ thang 22u: GHI NHẬN LỆCH, KHÔNG thu hẹp trong đợt này.** Lý do:
   (a) số thật chỉ là ước lượng từ ảnh (sai số ±20%, không có số bản đồ/
   công bố — OSM bị chặn trích xuất); (b) thang game là hợp nhất của 2
   thang thật (thang mặt tiền + thang Lê Đại Hành cao 17m) và đóng vai
   "khán đài" — khổ rộng hiện tại phục vụ đúng hành vi ngồi ăn trên bậc ở
   mục 1.3; (c) thu hẹp khổ thang là thay đổi địa hình lõi (stairH, 2 đai
   thềm, sạp trên chiếu nghỉ, hàng chục tuyến người) — rủi ro hồi quy lớn,
   nằm ngoài phạm vi sửa A/C của đợt V5.4. Nếu Chung Hy muốn siết tỉ lệ,
   đợt riêng nên thu về x −8.5..8.5 (17u) kèm rà soát toàn bộ điểm bám thang.
3. Đảo Ø21u: cùng nhóm lệch tỉ lệ với khổ thang — giữ nguyên cùng lý do,
   xử lý chung nếu có đợt siết tỉ lệ.

## 3. Tổng kết bổ sung cho đợt V5.4
- 5 hành vi chuyển động + cấu trúc dốc: game **khớp 5/6**, 1 lệch đã ghi
  nhận (vòng đảo là 2 cung con thoi thay vì vòng kín — đơn giản hoá khó
  thấy, có lý do hình học). **Không phát sinh sửa code A/C từ mục bổ sung
  này** — các sửa A/C đã làm trong đợt đứng vững sau đối chiếu chuyển động.
- Số đo: đường vào ✓ giữ nguyên; khổ thang + đảo ghi nhận lệch
  +20–40%/+15–30% so với ước lượng ảnh, chờ quyết định đợt siết tỉ lệ
  riêng (không tự ý sửa trong đợt này).
