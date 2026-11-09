# research/22 — Âm thanh + màu sắc THẬT của chợ đêm Đà Lạt (SOUND-COLOR-1, 09/11)

Phương pháp theo lệnh Chung Hy: **tự tải về rồi coi/nghe trực tiếp** — không đoán mò.
Màu đo bằng script `prototype-v2/scripts/sample_colors_sc22.py` (k-means 4 màu trội trên
ảnh thu nhỏ 120px + màu trung bình 3 dải trên/giữa/dưới). Âm thanh đo bằng
`prototype-v2/scripts/analyze_ref_audio.py` (giải mã opus → PCM 16kHz mono, FFT theo
cửa sổ 30s: RMS + tỉ lệ năng lượng 5 dải tần).

## 1. NGUỒN ĐÃ DÙNG (cả thất bại — để đợt sau khỏi lặp lại)

- **Ảnh thật:** 19 ảnh trong `theme/real-market/` (12 ảnh gốc của script + 7 ảnh bổ sung:
  44 vòng xoay phun nước, 09 bậc thang đông, 34 cổng neon, 35 sạp súp cua, 37 Khu Hòa Bình
  đêm, 38 ly sữa đậu nành, 39 bùng binh chiều tối). SOURCES.md đã có mục 40–44.
- **Audio thật:** YouTube `4rPBnyriJjY` — ambience chợ đêm Đà Lạt, **13 phút 29 giây**,
  opus 48kHz stereo, 12,56 MiB, tải về `/tmp/sc22/yt1.webm` (file tham khảo, KHÔNG nhúng
  vào game — 13MB vượt xa trần standalone còn dư ~60KB).
  - Lần 1 (đợt trước): `-f worstaudio/worst` kẹt ở 3,1MB từ 04:54, 2 tiến trình cùng ghi
    1 file → kill + xóa.
  - Lần 2 (đợt trước): video khác `kaVLoOsBbOk` lỗi `Requested format is not available`
    (worstaudio/worst không có format).
  - Lần 3 (đợt này): `-f bestaudio/best` → **thành công trong 9 giây** (2,1 MiB/s).
  - Kết luận: với YouTube hiện tại, `worstaudio/worst` hay kẹt/lỗi; dùng `bestaudio/best`.
- **Giới hạn:** chỉ nghe được bằng phân tích phổ (máy không có loa/tai nghe để nghe trực
  tiếp); số đo phổ + RMS dưới đây là bằng chứng thay cho tai nghe.

## 2. MÀU THẬT — BẢNG ĐO (k-means, % = tỉ lệ pixel)

| Ảnh | 4 màu trội | Ghi chú dùng cho game |
|---|---|---|
| 40 đường NTMK đêm, sạp 2 bên | #182650 28%, #c18861 28%, #855442 26%, #d2bca9 17% | Đêm: nền xanh đậm + tông ấm đất nung là 2 cực chủ đạo |
| 30 đám đông áo phao đêm | #373423 36%, #d7d2bf 25%, #8d9287 23%, #a7873b 15% | Áo thật: olive tối + kem sáng + **xám rêu** + mù tạt |
| 04 bùng binh đêm trên cao | #1b1210 31%, #ae844e 30%, #67502e 23%, #c8b39a 16% | Đêm quanh đảo: nâu đất ấm áp đảo |
| 14 bánh tráng nướng cận | #0d0b0c 34%, #904f16 27%, #cdaf88 23%, #44342f 16% | Than đen + cam cháy #904f16 |
| 31 sạp xiên nướng cận | #2f2731 45%, #73716d 24%, #c06c44 16%, #d8d3c8 15% | **Terracotta #c06c44** — màu sạp nướng thật |
| 08 bậc thang ngồi ăn đêm | #362727 30%, #dacec4 26%, #cf7851 22%, #797282 21% | Da cam cá hồi #cf7851 (người/đồ ăn) |
| 43 chợ đêm quần áo | #3c4430 34%, #20281e 31%, #675d38 22%, #658e7b 13% | Quần áo đêm: xanh rêu tối, KHÔNG màu chói |
| 41 sữa đậu nành Hoa Sữa | #d1c090 39%, #948976 25%, #675e56 22%, #48342b 14% | Kem sữa #d1c090 áp đảo |
| 28 bùng binh mặt đất, xe + người | #554746 34%, #261e25 29%, #7e7f78 21%, #c0bfb5 16% | Mặt đường đêm: nâu xám #665045 (dải dưới) |
| 07 đường chợ ngày trên cao | #a38d7e 33%, #dcccc3 26%, #5e4b41 23%, #c16b44 18% | Ngày: tông đất hồng nhạt, **terracotta #c16b44** lặp lại |
| 06 đường chợ đêm trên cao | #151412 33%, #4d4740 28%, #7e776e 27%, #b3b1ac 12% | Đêm từ trên cao: gần như đơn sắc nâu-xám tối |
| 32 tượng rọi sáng đêm | #4f4949 44%, #999796 21%, #eceae5 19%, #1a191a 15% | Tượng/đá: xám trung tính, trắng sáng 19% |
| 44 vòng xoay phun nước | #d3e9f5 38%, #949d97 29%, #727465 19%, #3e4437 14% | Nước/trời phản chiếu: xanh nhạt #d3e9f5 |
| 09 bậc thang đông kín đêm | #38291c 33%, #6f4f38 32%, #ac8158 24%, #dad1bb 10% | Bậc đêm: nâu đất ấm |
| 34 cổng neon trang phục | #1d1e17 39%, #594e34 26%, #968b6f 24%, #dbd6c2 11% | Neon không áp đảo phổ màu — nền vẫn tối |
| 35 sạp súp cua | #251d1e 42%, #5f4c47 32%, #ae846d 16%, #e3dfd3 10% | Sạp ăn đêm: tối + nâu ấm |
| 37 Khu Hòa Bình đêm đông | #463739 52%, #887579 21%, #2d5b71 15%, #c4c3c4 12% | Đám đông đêm: nâu sẫm 52% + teal #2d5b71 |
| 38 ly sữa đậu nành | #141413 41%, #51422c 39%, #887e6b 11%, #c8c1a9 9% | Tối + nâu sữa |
| 39 bùng binh chiều tối | #352e38 29%, #3d4c8c 27%, #8d7272 26%, #7389c5 17% | Hoàng hôn: xanh dương #3d4c8c/#7389c5 — bầu trời thật không tím |

### Kết luận màu (so với code game hiện tại)
- **ĐÃ ĐÚNG, không sửa:** mặt tiền kem ấm 0xe3d7bd (≈ #dcccc3/#d1c090); nhựa 0x453f3a
  < vỉa hè 0x84796a < sân 0x978a78 (đúng thứ tự tông, khớp dải dưới các ảnh 28/06/07);
  trời đêm xanh sâu 0x274263 (≈ #31395d dải trên ảnh 40); đèn sodium #ff9a3d (khớp
  tông ấm #c18861/#ae844e áp đảo ảnh đêm); áo NPC đã có kem + đen (V5.1/V5.2).
- **LỆCH, SỬA ĐỢT NÀY (4 điểm, đều là albedo — chuyển được sang web):**
  1. `CROWD_SHIRTS`: xanh rêu bão hòa 0x6b8f3e → **0x8d9287 xám rêu** (đo 23% ảnh 30;
     đám đông thật xám-olive, không xanh lá tươi).
  2. `AWNS` (mái bạt sạp): cam sáng 0xe8862e → **0xc06c44 terracotta** (đo ảnh 31 + lặp
     lại #c16b44 ở ảnh 07); xanh lá sáng 0x3f9e4d → **0x68804f** (xanh nông sản muted,
     đã có trong bảng district). Giữ đỏ nhấn 0xc8372d (khóa ≤5%) + dương 0x2e6da4
     (khớp #2d5b71/#3d4c8c ảnh 37/39) + tím/mù tạt.
  3. Nước đài phun 0x7fb2c9 → **0xa8cfe0** (nhạt hơn theo #d3e9f5 ảnh 44 — nước phản
     chiếu trời, không xanh đậm).
  4. Áo treo trên giá (`clothesRack` cols): vàng chói 0xe8c832 → **0xd7d2bf kem sáng**
     (đo 25% ảnh 30; quần áo đêm ảnh 43 toàn tông tối/muted, không có màu chói).
- **KHÔNG SỬA:** exposure/đèn/sky shader (grade web không kiểm chứng được từ Blender —
  điểm mù đã biết từ V5.4/V5.5; chỉ chốt khi Chung Hy chơi thử). Đề xuất ghi nhận:
  trời đêm game 0x0e1a30 hơi tối hơn dải trên ảnh 40 (#31395d) — nhưng đó là màu
  nền/backdrop, không tự đổi khi chưa thấy trên web.

## 3. ÂM THANH THẬT — SỐ ĐO PHỔ (13,5 phút, cửa sổ 30s)

| Cửa sổ | RMS | <250Hz | 250–800Hz | 0,8–2,5kHz | 2,5–6kHz | >6kHz |
|---|---|---|---|---|---|---|
| 0–120s (đông) | −19..−21dB | 23–27% | **54–65%** | 2–4% | 1–2% | 0% |
| 120–150s | −18,5dB | 32% | 60% | 2% | 1% | 0% |
| 150s (lặng) | −24,1dB | 24% | 11% | 11% | 8% | 1% |
| 180s | −19dB | 26% | 70% | 2% | 1% | 0% |
| 210s (lặng) | −25,7dB | 13% | 11% | 10% | 4% | 1% |
| 270–360s (đông nhất) | −17..−18dB | 24–35% | 51–64% | 3–6% | 1% | 0% |
| 420s (lặng nhất) | −26,5dB | 23% | 21% | 14% | **13%** | 2% |
| 450s | −18,4dB | **55%** | 40% | 4% | 1% | 0% |
| 480s (lặng) | −31,2dB | 8% | 30% | **31%** | 11% | 1% |
| 510s | −19,8dB | 29% | 26% | 14% | **13%** | 2% |
| 600–750s | −17..−23dB | 18–31% | 26–65% | 2–11% | 1–2% | 0% |

- **Đọc phổ:** năng lượng tập trung ở **250–800Hz (47–70% lúc đông)** = dải rì rầm đám
  đông/giọng nói trầm — KHÔNG có giọng nói rõ từng câu (dải 0,8–2,5kHz chỉ 2–6%),
  nên nhiễu lọc băng tần là cách tái tạo ĐÚNG (không cần giọng nói tổng hợp).
- **<250Hz 23–35%** (có lúc 55%) = thân dưới của đám đông + động cơ xe/tiếng trầm.
- **2,5–6kHz chỉ 1–2% lúc đông, vọt 8–13% lúc lặng** = tiếng xì xèo/chảo/va chạm kim
  loại chỉ lộ khi đám đông lắng — sizzle là lớp PHỤ, không phải nền.
- **Động thái:** RMS dao động −17dB (đông nhất) → −31dB (lặng nhất), ~14dB — chợ thật
  thở theo từng đợt người, không phẳng đều. Peak >0,5 xuất hiện dày (0s, 5s, 45s,
  140s…) = tiếng gọi/rao/va chạm thoáng qua.
- **Suy ra đặc tả game (mỗi khu một công thức gain — xem mục 4):** rì rầm 250–800Hz là
  nền CHỦ; trầm <250Hz là nền PHỤ; xì xèo 2,5–6kHz chỉ gần sạp ăn; xe máy là quét
  tần thấp thoáng qua; gió là nhiễu trầm rất nhẹ ở chỗ cao/vắng.

## 4. ĐẶC TẢ ÂM THANH GAME (sinh thủ tục WebAudio — KHÔNG file nhạc)

| Khu (theo tọa độ game) | Rì rầm 500Hz | Trầm 150Hz | Xì xèo 4,5kHz | Nước 1,1kHz | Gió 280Hz | Ghi chú |
|---|---|---|---|---|---|---|
| Phố ăn (x −60..43, z −17..24) | 1,00 | 0,50 | 1,00 gần hàng sạp | 0 | 0,10 | Đông nhất — khớp RMS −17dB |
| Bậc tam cấp (x −6..6, z −31..−1) | 0,60 | 0,35 | 0,45 | 0 | 0,10 | Ngồi ăn, rì rầm vừa |
| Đài phun (cách (24,5; 5,2) < 16u) | 0,55 | 0,30 | 0 | 1,00 | 0,10 | Nước là lớp chủ ở đây |
| Đường vào (x −131..−60) | 0,35 | 0,45 | 0 | 0 | 0,25 | Xe qua lại, thưa người |
| Sân đông/quảng trường còn lại | 0,70 | 0,40 | 0 | 0,15 | 0,15 | Mặc định |
| Trên cao/vắng (y > 3, ngoài các khu) | 0,25 | 0,20 | 0 | 0 | 1,00 | Gió lên khi vắng |
| ĐÊM (isNight) | ×1,3 | ×1,15 | ×1,2 | ×1,0 | ×0,8 | Đêm đông + ồn hơn |
| NGÀY | ×0,8 | ×0,9 | ×0,8 | ×1,0 | ×1,2 | Ngày thưa, gió rõ hơn |

- Xe máy vụt qua: khi xe đường gần người chơi < 22u (cooldown 5s) — quét sawtooth
  70→160→70Hz trong 1,4s + nhiễu trầm, âm lượng theo khoảng cách.
- Rì rầm có LFO chậm 0,07Hz (±20%) để "thở" như RMS thật dao động 14dB theo đợt.
- Nút 🔊/🔇 trên HUD (lưu `state.muted` vào save `chohb3d-v1`, mặc định bật tiếng);
  tắt tiếng = master gain 0 (cả SFX + nhạc sân khấu + ambience). Âm thanh chỉ khởi
  động sau tương tác đầu tiên (AudioContext tạo từ SFX như hiện tại).
