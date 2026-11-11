# 27 — HỒ NƯỚC: KHẢO SÁT + THIẾT KẾ BẢN SỬA (chưa sửa code)

> Lệnh: Chung Hy 19:36 11/11 "hồ nước cần rõ hơn nữa". File này chỉ khảo sát + thiết kế;
> không đụng index.html / build_models.py / assets (đang có worker khác sửa).
> Mọi số đều ĐO thật: màu game đọc từ code, màu thật đo PIL từ ảnh trong theme/,
> tương phản tính bằng relative luminance WCAG từ các hex đó.

## 0. Xác định đối tượng — game chỉ có ĐÚNG 1 mặt nước

- **Không có hồ lớn trong thế giới game.** Hồ Xuân Hương không hề được dựng; `assets/pier.glb`
  KHÔNG phải bến thuyền — nó là **trụ cầu** của cầu nổi vào tầng 2 (index.html:1191-1192,
  `cloneAsset('pier')` đặt tại (17.5, 0, −2) và (17.5, 0, −16), scale y 13.4/15.0).
  `roundabout.glb` + code đảo bùng binh (−30, −6): 0 vật liệu nước — đảo là tượng + hoa + cỏ
  (vị trí tượng/đảo đã khóa GEOMETRY-2, không thuộc phạm vi mục này).
- **Mặt nước duy nhất = bồn đài phun nước** ở sân trước chợ, tâm **(27, 5.2)** (FNT,
  index.html:3458-3488). Đây là "hồ nước" mà người chơi nhìn thấy — mục này thiết kế cho nó.
  Nếu Chung Hy muốn một hồ lớn kiểu Xuân Hương thì đó là tính năng MỚI (địa hình + solid +
  tuyến đi mới), ngoài phạm vi bản sửa này — cần anh chốt riêng.

## 1. AUDIT mặt nước hiện tại (index.html:3461-3468, tickWater 3451-3455)

| Thành phần | Thông số hiện tại |
|---|---|
| Mặt nước `fwater` | CircleGeometry r **2.45** (Ø 4.9u), 20 seg, tại (27, **0.5**, 5.2), MeshStandardMaterial màu **0xa8cfe0**, roughness 0.25, transparent, opacity gốc 0.9 |
| Animation mặt nước | `tickWater`: y nhấp ±0.02 (sin t·1.7); opacity dao động **0.84 ± 0.06** (sin t·2.3). **Không có texture, không gợn, không phản chiếu giả** — một đĩa trơn |
| Vòng gợn `rings` | 2 RingGeometry (r trong 0.5/1.3, ngoài 0.62/1.42), MeshBasicMaterial **0xeaf6fc**, opacity chạy 0.38→0 theo chu kỳ 3.1s, scale 0.7→2.4 |
| Tia nước `jets` | 7 tia trụ mảnh, MeshBasicMaterial **0xcfe8f4**, opacity 0.55 ± 0.08, scale y ±7% |
| Bồn chứa | cyl r 2.7/2.9 cao 0.55 đá **0x8a8074**; cột giữa + 2 bát cũng 0x8a8074; mặt nước y 0.5 nằm **thấp hơn miệng bồn** (đỉnh cyl ≈ 0.555) |
| Nền xung quanh | Tấm sân plaza **0xa79a84** (167,154,132) ngay dưới bồn; quảng trường đá + stoneTex |
| Đêm | `applyDayNight` KHÔNG đụng mặt nước; chỉ có đèn chân đài phun `fup` (emissive 0xffc98a, qua `uplightMats`, đêm intensity 2.8) + glowDisc r 3.4. Game mặc định ~19:00 tông ấm |
| Ràng buộc sẵn | `solid(FNT.x, FNT.z, 2.9, 2.9)` (index.html:3495) — chân đài phun đã đăng ký vật cản; minimap vẽ đài phun #7fb2c9 (index.html:6824) |

**Màu hiệu dụng thật của mặt nước** (đĩa bán trong suốt phủ lên đá bồn):
0.84 × (168,207,224) + 0.16 × (138,128,116) ≈ **(163,194,207)** — xanh nhạt rửa.

## 2. ĐO THAM CHIẾU THẬT (PIL, median theo vùng)

Nguồn ảnh mặt nước trong dự án **rất ít — nói thẳng**: 44 ảnh `theme/real-market/` không có
ảnh hồ Xuân Hương nào; ảnh toàn cảnh trong `theme/` là ảnh AI concept (không có hồ).
Ảnh thật duy nhất có nước là đài phun vòng xoay:

- `theme/real-market/44-vong-xoay-phun-nuoc.jpg` (ngày, 1024×490):
  - Tia phun: **#eef0f5** (238,240,245) — trắng gần tuyệt đối.
  - Dải nước trong bồn dưới tia (vùng x500-620, y295-318): **#9ea9a1** (158,169,161) —
    xám xanh lá, **tối và đục**, bão hòa chỉ ~0.07. (Vùng nhỏ, lẫn bóng tia — độ tin cậy vừa.)
  - Thành/kè bồn: #cbbfab; vỉa đảo: #866961; lòng đường: #8a9595.
- `theme/real-market/04-bung-binh-dem-tren-cao.jpg` (đêm): vòng xoay thật **không lộ mặt
  nước** — ban đêm thứ đọc được là ánh đèn ấm + quầng sáng, không phải màu nước.

**Kết luận đo:** nước thật trong bồn nông đọc là màu xám-xanh TỐI, không phải xanh nhạt
sáng như game đang để. Nhưng sao chép y hệt #9ea9a1 vào game chibi tông ấm sẽ thành
mảng xám chết — bản sửa lấy **hướng** của số đo (tối hơn + xanh teal hơn nền) và đẩy
bão hòa lên theo đúng bảng màu đã khóa của game (biển dùng 0x2e6da4 bão hòa).

## 3. VÌ SAO NHÌN KHÔNG RÕ — xếp hạng theo số đo

Tương phản độ sáng (relative luminance Y, tỉ lệ CR = (Y₁+0.05)/(Y₂+0.05)):

| Cặp | CR hiện tại |
|---|---|
| Nước hiệu dụng (Y 0.509) ↔ sân plaza 0xa79a84 (Y 0.330) | **1.47 — rất yếu** |
| Vòng gợn 0xeaf6fc (Y 0.904) ↔ nước hiệu dụng | **1.71 — gợn gần như tàng hình** |
| Nước hiệu dụng ↔ đá bồn 0x8a8074 (Y 0.221) | 2.10 — chỉ khá ở vành bồn |

1. **Màu nước quá nhạt + ít bão hòa (nguyên nhân chính).** 0xa8cfe0 có L≈0.77, S≈0.14;
   phủ 84% lên đá bồn vẫn ra (163,194,207). Nó chỉ sáng hơn sân plaza xung quanh 1.47 lần —
   ở camera diorama 45° và tông ấm 19:00 (ACES + đèn vàng), mảng xanh nhạt này rửa về
   xám ấm, lẫn vào sân. Cả cụm đài phun (nước + gợn 0xeaf6fc + tia 0xcfe8f4) nằm chung
   một dải màu nhạt → đọc thành **một khối trắng xám**, không thành "nước".
2. **Mặt phẳng trơn tuyệt đối.** Không texture/gợn/phản chiếu; chuyển động duy nhất là
   nhấp y ±0.02u và opacity ±0.06 — ở khoảng cách diorama không nhìn thấy. Mắt không có
   tín hiệu "đây là chất lỏng".
3. **Vòng gợn sai tương phản.** Gợn trắng #eaf6fc trên nền nước nhạt = CR 1.71, lại còn
   fade về 0 — thành phần đáng lẽ báo hiệu mặt nước nhất lại vô hình.
4. **Đĩa nước nhỏ + nằm thấp.** Ø 4.9u giữa sân 64u; miệng bồn cao hơn mặt nước ~0.05u
   che mất vành khi nhìn xiên 45° từ phía thấp. (Yếu tố phụ — không đổi kích thước bồn
   trong bản này vì đụng solid/bố cục đã chốt.)
5. **Đêm không có cơ chế riêng.** Mặt nước không vào danh sách applyDayNight nào; ban đêm
   chỉ靠 đèn chân ấm hắt — nước vẫn giữ màu ngày bị tối đi, không có điểm nhấn lạnh để
   tách khỏi sân ấm.

## 4. THIẾT KẾ BẢN SỬA — thông số áp ngay được

Tất cả bằng **code trong index.html**, đúng idiom sẵn có (CanvasTexture + RepeatWrapping
như stoneTex index.html:1891-1898 và dirtTex :3164; animate trong `tickWater` như hiện tại;
đêm qua cơ chế list-material như `uplightMats` :6483/6510). Không sửa GLB, không đổi solid.

### 4.1 Màu + vật liệu mặt nước (thay thông số `fwater`, index.html:3461)
- Màu nền: **0x276a8a** (39,106,138) — teal đậm cùng họ 0x2e6da4 của biển hiệu;
  Y = 0.126 → CR với sân plaza = **2.16** (từ 1.47), và là mảng TỐI duy nhất giữa sân sáng
  → đọc ngay là hố nước.
- Thêm **đĩa đáy bồn** ngay dưới mặt nước (CircleGeometry r 2.45, y 0.47, MeshBasicMaterial
  hoặc Standard **0x14425c**): chặn việc opacity pha màu đá bồn 0x8a8074 làm rửa màu —
  màu hiệu dụng từ nay do mình kiểm soát, không phụ thuộc nền dưới.
- opacity: giữ transparent nhưng **0.93** nền; bỏ dao động opacity ±0.06 (giữ nhấp y ±0.02)
  — dao động sáng chính là thứ làm nước "nhấp nháy rửa màu".
- roughness 0.25 → **0.15** (bắt đèn chân ấm ban đêm thành vệt sáng rõ hơn trên mặt tối).

### 4.2 Texture gợn canvas + chuyển động (cơ chế chính tạo cảm giác nước)
- Tạo CanvasTexture 256×256: nền trong suốt, vẽ ~40 cung tròn/vệt ngắn màu **#bfe6f5**
  alpha 0.5-0.9, bề rộng 2-3px, phân bố ngẫu nhiên cố định (seed theo sin như các hàm
  họa tiết NPC sẵn có); `wrapS/wrapT = RepeatWrapping`, `repeat.set(2,2)`,
  `colorSpace = SRGB`, dùng làm `map` phủ lên vật liệu ở 4.1 (map nhân với màu nền teal —
  vệt sáng thành #7fb2c9-ish trên nền đậm) — màu vệt trên nền đích: CR ≈ 3+ (đo lại khi làm).
- Animate trong `tickWater` (mở rộng entry `surfs` thêm `tex`): mỗi frame
  `tex.offset.x = (t*0.008) % 1; tex.offset.y = (t*0.005) % 1;` — trôi chéo rất chậm
  (đúng kiểu game đang trôi offset repeat ở các texture tĩnh; tốc độ này ở Ø4.9u là
  ~0.04u/s, không gây chóng mặt). Đây là thay đổi hành vi nhìn thấy lớn nhất: mặt nước
  **chuyển động liên tục** thay vì đứng yên.

### 4.3 Vòng gợn + tia (chỉnh thông số, không thêm cơ chế)
- Rings: giữ nguyên hình học/chu kỳ; trên nền teal đậm, màu 0xeaf6fc cho CR **5.43**
  (từ 1.71) — tự khắc nhìn rõ; nâng opacity đỉnh 0.38 → **0.5**.
- Jets: màu 0xcfe8f4 → **0xeaf6fc**, opacity 0.55 → **0.7**: tia trắng trên nền nước tối
  + bồn đá xám sẽ tách lớp rõ (tham chiếu ảnh 44: tia thật #eef0f5 gần trắng tuyệt đối).

### 4.4 Vành miệng bồn (tương phản bờ)
- Thêm 1 ring phẳng (RingGeometry r 2.45-2.72) tại y 0.56 trên miệng bồn, màu **0xd8d2c2**
  (sáng, họ đá sáng của bó vỉa 0x5a5248 đảo ngược tông): tạo đường viền sáng khép kín
  ngăn cách đĩa teal tối với đá bồn xám — "bờ" đọc được từ mọi hướng camera.
  (Thuần thị giác, nằm trong footprint solid 2.9×2.9 sẵn có.)

### 4.5 Ban đêm
- Đưa material mặt nước vào một list kiểu `uplightMats` (hoặc gán thẳng trong
  applyDayNight): đêm → `emissive 0x1d4e5f, emissiveIntensity 0.55`; ngày → 0.
  Nước thành mảng teal phát nhẹ giữa sân ấm — đúng cách ảnh đêm 04 đọc được cảnh
  (điểm lạnh nổi giữa biển đèn vàng). Đèn chân `fup` + glowDisc đã có giữ nguyên.

### 4.6 Ngân sách byte
- Ước tính code thuần: texture gợn ~350-450 byte, đĩa đáy + vành ~200 byte, thay thông
  số + tick mở rộng + hook đêm ~250 byte → **tổng ≈ 0.8-1.0 KB**. Headroom standalone
  hiện ~5.6MB (sau GLB-QUANTIZE-1) → không cần cắt comment, không rủi ro trần.

## 5. RỦI RO + KIỂM CHỨNG KHI LÀM

- **Solid/tuyến đi:** bản sửa không đổi hình học bồn, không thêm solid; vành + đĩa đáy
  nằm gọn trong solid (27, 5.2, 2.9×2.9) đã đăng ký → audit_ground/tuyến đi bộ không đổi.
  Bàn ghế quanh đài phun (plazaTable 17.4/18.5) cách tâm ≥ 9u — không liên quan.
- **Pier/cầu nổi:** không liên quan (khác khu, khác asset) — bản sửa không đụng GLB nào,
  không phải chạy lại quantize.
- **Hiệu năng:** +2 mesh phẳng + 1 CanvasTexture 256² — không đáng kể; tickWater thêm
  2 phép gán offset/frame.
- **Cổng bắt buộc sau khi làm:** đủ 8 cổng chuẩn của dự án (diag 900 · SEED_SAVE 300 ·
  standalone diag 300 · traffic 26/26 · audit_ground 0/0 · test_bd2 · check_sweep3 ·
  test_real1) + render nghiệm thu đài phun ngày & đêm đặt cạnh trạng thái trước,
  đo lại median vùng nước trên render (đích: median vùng nước tiến về họ teal đậm,
  CR nước/sân trên ảnh render ≥ 1.9).
- **Không làm trong bản này:** đổi kích thước bồn/đài phun (đụng bố cục + solid đã chốt),
  thêm hồ lớn (tính năng mới, chờ Chung Hy chốt riêng), nước ở bùng binh (đảo đã khóa).

## 6. THỨ TỰ LÀM ĐỀ XUẤT

1. 4.1 màu + đĩa đáy + bỏ dao động opacity (hiệu quả lớn nhất, ~15 dòng).
2. 4.2 texture gợn + trôi offset trong tickWater.
3. 4.3 rings/jets + 4.4 vành miệng bồn.
4. 4.5 hook ban đêm.
5. Package + 8 cổng + render đối chiếu ngày/đêm → đẩy GitHub như các vòng trước.
