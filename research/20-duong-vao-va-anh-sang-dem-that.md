# Research 20 — Đường vào chợ thật & ánh sáng đêm thật (V5.4)

> Nguồn: bộ ảnh thật `theme/real-market/` (39 ảnh, bộ đêm 28–39, đặc biệt ảnh 06 phố đêm
> nhìn từ trên cao và ảnh 28 bùng binh về đêm), research/11, 16, 17, 18 + đo trực tiếp
> code `prototype-v2/index.html` tại head b04ecb11. Viết 08/11/2026 sau phản hồi chơi thử:
> "đường nhỏ xíu, một hàng đồ ăn là kịch — đường vào chợ Đà Lạt thật rất rộng, hai hàng
> bán hai bên cùng với xe; ánh sáng như trong studio, đêm tô đen; người đi vào đất".

## 1. Mặt cắt đường vào chợ thật (từ ảnh)

Từ ảnh 06 (trục phố đêm nhìn dọc từ trên cao) và các ảnh mặt đất bộ đêm:

- **Trục vào là một phố thương mại rộng, không phải lối đi.** Hai dãy nhà/sạp sáng đèn
  LIÊN TỤC ở hai bên tạo thành "hành lang sáng"; giữa là dòng người + xe máy dày đặc.
  Không có cảm giác "một hàng sạp chắn hết đường" — sạp lùi vào hai phía, lòng đường
  ở giữa luôn thông.
- **Sạp quay mặt VÀO đường ở cả hai bên.** Bên nào cũng có: mái che nhô ra, hàng hoá
  tràn tới mép vỉa hè, người bán đứng sau quầy, người mua đứng thành cụm trước quầy.
- **Xe chạy giữa + đậu dọc hai bên** (xe máy đậu thành hàng sát vỉa hè, trước các sạp
  đóng cửa), người đi bộ len giữa xe đậu và quầy — mặt cắt thực tế gồm nhiều dải song
  song chứ không phải 3 dải cứng.
- **Mật độ người cao và phân bố khắp mặt cắt**: trước quầy, giữa đường, quanh bùng binh.
  Bùng binh (ảnh 28): tượng sẫm nổi trên nền phố sáng, xe + người vòng quanh liên tục.

### Số mục tiêu cho game (đường vào trục x, vùng đảo là điểm nghẽn hẹp nhất)

| Dải (bắc → nam tại trục đảo) | Vị trí z mục tiêu | Ghi chú |
|---|---|---|
| Hàng sạp BẮC (mới) | thân z −7.95..−5.45, mặt tiền z = −4.6 | 5 sạp quay mặt xuống đường (rotY 0) |
| Dải đi bộ bắc + hàng chờ | z −4.6..−2.7 | hàng chờ tràn vào dải này |
| Làn xe hướng đông (E) | tâm z = −1.5 (xa đảo) → 5.55 (cạnh đảo) | vòng ôm đảo, cách tâm đảo 11.55 |
| Dải tị nạn giữa 2 làn | z ≈ 6.35 tại đảo | người băng qua đứng chờ ở đây (điểm sang đường) |
| Làn xe hướng tây (W) | tâm z = 1.9 (xa đảo) → 7.15 (cạnh đảo) | khe 2 làn tại đảo: 1.6 tâm–tâm (hở 0.9) |
| Dải đi bộ nam (trước mặt tiền) | z ≈ 8.15 | giữa mép làn W (7.5) và mặt tiền (8.9) |
| Hàng sạp NAM | thân z 9.75..12.25, mặt tiền z = 8.9 | hàng hiện có, lùi thêm 0.85 về phía nhà lồng |

Hành lang sáng tổng tại trục đảo: từ −7.95 tới 12.25 ≈ **20 unit liên tục có hoạt động**
(so với bản cũ: 4 sạp đêm nằm GIỮA lòng đường tại z = 3 khiến hành lang xe + người bị
bóp còn ~5 unit và tạo cảm giác "một hàng là kịch").

## 2. Ánh sáng đêm thật (từ ảnh đêm)

- **Không nơi nào đen tuyệt đối trong khu hoạt động.** Trời đêm là xanh-nâu sâu; nền
  đường/nền nhà phản chiếu ánh đèn nên vùng "tối" vẫn đọc được hình khối. Đen tuyệt đối
  chỉ xuất hiện ở mảng trời xa và mái nhà không đèn.
- **Nguồn sáng là NHIỀU ĐIỂM NHỎ, không đồng đều:** đèn sạp trắng-ấm (sáng nhất, theo
  từng sạp, sạp sáng sạp mờ), đèn đường sodium cam (quầng ấm rõ, rã sáng nhanh — giữa
  hai cột đèn có khoảng tối tương đối), biển hiệu/neon điểm xuyết ở cuối trục, đèn xe.
- **Sương/khói bắt sáng:** quầng quanh mỗi nguồn sáng mềm và rộng; ánh sáng "có không
  khí", không phải chùm sáng cứng trên nền đen — đây là khác biệt lớn nhất với cảm giác
  "studio": studio = 1 nguồn lớn đều + nền đen phẳng; đêm thật = ambient thấp nhưng
  KHÔNG phẳng (trời lạnh ở trên, phản xạ ấm ở dưới) + nhiều điểm sáng rã tự nhiên.
- **Tượng/điểm nhấn KHÔNG trắng chói**: tượng ở bùng binh sẫm, đọc bằng tương phản với
  nền phố sáng phía sau.

### Rig ánh sáng HIỆN TẠI trong code (đo tại applyDayNight + khai báo đèn) — và vì sao "studio"

| Thành phần | Trị số hiện tại | Vấn đề |
|---|---|---|
| background | 0x191209 (nâu gần đen) | nền phẳng, chết |
| sky dome | top 0x131c3a / mid **0x3d2b52 (TÍM)** / bot 0xa86834 | dải tím như gel màu sân khấu |
| fog | 0x4a3420, density tới ~0.0126 khi lạnh | sương nâu đặc, nuốt xa thành đen |
| hemisphere | 0xffd9a0/0x4a3220, **0.92** | fill ấm đều từ trên xuống = đèn studio |
| ambient | 0xffc98a, **0.26** | cộng với hemi = mọi bề mặt sáng đều, không còn đêm |
| sun đêm / moon | sun 0.1; moonLight dùng lại màu 0xffc98a 0.55 | nguồn "mặt trăng" màu cam — sai vật lý, thêm fill |
| exposure | **1.34** | đẩy mọi thứ lên sáng đều |
| đèn đường | PointLight 0xffb45e, 120, distance 36, decay 1.8, cách 20u | quầng chồng lấp thành vệt sáng liên tục đều — không có khoảng tối giữa các cột như ảnh thật |
| bóng sạp | halo flicker 0.6±0.06 đồng loạt | mọi sạp sáng như nhau — mất biến thiên từng sạp |

### Trị số đích V5.4 (đối chiếu QUAN HỆ sáng trong render, không chấm trị số tuyệt đối)

- Trời: top 0x0e1a30, mid 0x274263 (xanh sâu, bỏ tím), bot 0xc07a36; background = 0x0e1a30.
- Fog: 0x3d3630 (xám ấm), base 0.0058, hệ số nhiệt 0.0008 — sương mỏng, xa vẫn đọc được.
- Hemisphere: trời 0x93a7cc (lạnh) / đất 0x40301e (nâu ấm phản hồi), 0.5 — trên lạnh dưới ấm.
- Ambient: 0xffd9b0, 0.12 (chỉ đủ nhấc vùng tối khỏi đen chết).
- Sun đêm = 0; moonLight 0xa9c3e8, 0.4 (trăng lạnh tạo khối, hết fill cam).
- Exposure 1.22. Đèn đường: distance 27, decay 2.0, intensity 88 → quầng tách rời, có
  khoảng tối giữa các cột. Halo sạp: biên độ theo pha riêng từng sạp (biến thiên sẵn có).

## 3. Đo code hiện tại — đường & người (trước khi sửa)

- Đường vào: plane 170×18 tại z = 1.5 (z −7.5..10.5). Hàng sạp nam quay mặt vào đường
  (front z = 8.05). **4 sạp đêm nằm giữa lòng đường tại z = 3** (dauhu −38, xien −12,
  che 6, tron 30) — nguồn gốc cảm giác chật. Phía bắc đường: KHÔNG có hàng sạp nào
  (chỉ vỉa hè + sườn đồi).
- Làn xe: laneZE đỉnh 5.9; laneZW đỉnh 6.65 → **khe 2 làn tại nam đảo chỉ 0.75 tâm–tâm**
  (hai xe ngược chiều gần như chạm nhau).
- groundH: thứ tự nhánh deck cầu → thang trong nhà → hành lang 12.6 → sảnh → ramp vào
  (x<−52) → đỉnh đồi 17 → thung lũng 0 → thang → đai thềm → thềm đảo → sườn. Dò bằng
  raycast (script tạm): mặt dốc vào khớp groundH ±0.06; mặt sườn khớp tuyệt đối;
  **vùng lệch duy nhất x −70..−52, z −7.5..−2**: groundH theo ramp (thấp) nhưng bề mặt
  nhìn thấy là mặt sườn (cao hơn 1.5–2.6) → người đứng đó chìm vào sườn; đồng thời vùng
  này chặn việc đặt hàng sạp bắc nếu không cắt sườn + thêm thềm.
- NPC lấy cao độ: wanderer dùng groundH + guard "dưới cầu/hành lang" (pos.y<8 → 0)
  nhưng guard **thiếu hẳn đoạn hành lang đông x 21..33, z 7..12.2** (người chơi có đủ
  3 đoạn, wanderer chỉ có 2) → người đi trước sạp sữa/cà phê bị groundH = 12.6 nhấc
  lên nóc hành lang. Người chơi: groundH + guard đủ 3 đoạn ✓.
- Audit tuyến người (scripts/audit_ground_v54.mjs, trích nguyên văn code): xác nhận
...[truncated 2085 chars]