# 28 — PHÂN TÍCH VIDEO ĐI DẠO HỒ XUÂN HƯƠNG (màu + tiết diện + cây)

> Nghiên cứu nối tiếp, hoàn tất 12/11/2026. Mục đích: trả lời phản hồi của Chung Hy
> 00:34 12/11 — "có giống thật đâu, xem mấy video đi dạo hồ Xuân Hương giùm;
> màu sặc… phối màu lại hết luôn". Mọi số màu dưới đây ĐO bằng PIL (median theo
> vùng chọn tay) trên frame trích từ video thật; số game trích từ
> V4-CHECKLIST mục XH-1/XH-1.5/XH-3R + đo PIL trực tiếp trên
> renders/xh3r-eye-day.png. KHÔNG sửa code ở vòng này.

## 1. NGUỒN VIDEO (ffprobe trên file trong research/video-xh/src/)

| File | YouTube ID | Nội dung thật (theo frame) | Thời lượng | Độ phân giải bản tải |
|---|---|---|---|---|
| v1_loop_sang_ELHah4i9lnY.mp4 | ELHah4i9lnY | Một vòng quanh hồ buổi SÁNG (chạy bộ/đạp xe quay dọc): bờ bắc gần chợ → đường Trần Quốc Toản → vòng bờ nam/tây cây nghiêng → về chợ (f029) | 544,5s (9:04) | 144×250 (dọc, RẤT thấp) |
| v2_tour_AIGDdsV_9b4.mp4 | AIGDdsV_9b4 | **KHÔNG PHẢI HỒ** — tour Dinh III Bảo Đại (nội thất dinh là chính). Chỉ f001 (đường vào, thông cao) + f002 (sân, phượng tím) dùng tham khảo cây | 299,5s (4:59) | 854×480 |
| v3_chieu_Tts6-E3vhYI.mp4 | Tts6-E3vhYI | Chạng vạng nhìn từ bờ nam sang bờ bắc: Thủy Tạ lên đèn, thuyền đạp vịt, khung cây tiền cảnh (có watermark VivaVideo) | 60,2s | 640×360 |

Giới hạn bằng chứng (ghi rõ, không giấu):
- v1 chỉ 144×250 → màu tin ở mức TÔNG TỔNG THỂ (sai số sắc có thể ±5–8%), cấu trúc/tiết diện tin được hoàn toàn.
- v3 qua filter VivaVideo (tím hoá) → số buổi chiều là tương đối, dùng cho hướng màu, không dùng tuyệt đối.
- Đã tự xem trực tiếp 14 frame: v1 f003, f007, f012, f013, f015, f018, f021, f024, f026, f029; v2 f001, f002; v3 f001, f004 (+ 3 contact sheet toàn bộ 53 frame).

## 2. PALETTE ĐO TỪ VIDEO (median PIL, vùng chọn tay)

| Hạng mục | Hex đo | Frame nguồn | Ghi chú |
|---|---|---|---|
| Trời nắng sáng | #90b1da | v1/f015 | xanh vừa, không chói |
| Trời nhiều mây | #7f8fa7 | v1/f018 | xám xanh |
| Trời hoàng hôn | #9aa5d1 | v3/f001 | tím xám (qua filter) |
| **Nước ngày (mây) gần** | **#949ea0** | v1/f024 | xám trung tính, ngả xanh RẤT nhẹ |
| **Nước ngày xa** | **#9ba1a5** | v1/f021 | gần như xám bạc |
| Nước ngày (mặt rộng) | #8f9595 | v1/f019 | |
| Nước đoạn cuối vòng | #788189 | v1/f028 | sẫm hơn khi ngược sáng |
| **Nước chiều** | **#899bd3** | v3/f004 | chàm sáng theo trời |
| **Nước hoàng hôn** | **#838eb2** | v3/f001 | chàm tím |
| Nước chạng vạng sẫm | #434d66 (p75 #6e7dae) | v3/f002 | |
| Lát vỉa hè chính | #acadab | v1/f015 | XÁM TRUNG, không trắng |
| Lát đoạn cây | #9ea6ae | v1/f007 | |
| Lát ướt | #91989c | v1/f014 | |
| Dải tactile dọc trên lát | #909499 | v1/f015 | dải TỐI chạy DỌC liên tục |
| Lát đá phiến tổ ong (lối phụ) | #5f574f | v1/f003 | đá SẪM, mạch nâu đất |
| Đá phiến (nắng) | #716358 | v1/f001 | |
| Cỏ nắng | #6e6d29 | v1/f005 | VÀNG OLIVE rõ |
| Cỏ mép nước (bóng) | #55662c | v1/f021 | olive sẫm |
| Cỏ dải hẹp sát nước | #4b5c2e | v1/f024 | |
| Cỏ phía trong | #788054 | v1/f007 | |
| Tán cây lá rộng nghiêng | #29362a | v1/f024 | RẤT sẫm, xanh rêu |
| Tán cây nghiêng (khác) | #38442a | v1/f018 | |
| Tán cây nhỏ ven hồ | #435338 | v1/f021 | |
| Hoa giấy tím (median lẫn lá) | #581a53 – #623059 | v1/f010, f012 | hoa thuần sáng hơn: magenta sẫm |
| Phượng tím (trong bóng) | #442c39 (p75 #5e4752) | v2/f002 | cụm xa/nền tối |
| Nhựa đường | #525c65 | v1/f015 | xám sẫm trung tính |
| Nhựa sân (tham khảo) | #595651 – #65625e | v2/f001, f002 | |
| Thân cây quét vôi (trong bóng) | #919798 | v1/f021 | trắng đã ngả xám/bẩn |
| Thân thông trên đoạn vôi | #7b7471 | v1/f026 | nâu xám (vùng lẫn, tham khảo) |
| Đèn Thủy Tạ hoàng hôn | HỒNG MAGENTA (định tính) | v3/f001, f006 | vùng đo lẫn nền tối nên median không sạch; mắt thường: khối đèn hồng rực + vệt phản chiếu hồng trên mặt nước |

**Kết luận màu cốt lõi:** hồ Xuân Hương trong video là một bảng màu TRẦM —
nước XÁM BẠC, lát XÁM, cỏ OLIVE, tán cây SẪM. Không có mảng teal/xanh tươi/
trắng nào đủ lớn để làm "màu chủ đạo" như bản game hiện tại.

## 3. TIẾT DIỆN ĐƯỜNG DẠO THEO FRAME THẬT (từ mặt nước → phía trong)

**Đoạn bờ bắc (gần chợ / Trần Quốc Toản — v1/f007, f013, f014, f015):**
1. Nước
2. **Dải cỏ HẸP sát mép nước** — cây ven hồ trồng trên dải này; kè đá nếu có thì rất thấp, khuất sau cỏ
3. **Lát vỉa hè RỘNG** (gạch xám ~#acadab) — có **dải tactile TỐI chạy dọc liên tục** + ô nhấn hồng RẤT thưa
4. **ĐƯỜNG NHỰA xe chạy** (xe máy đông, v1/f015) — dải này game đang THIẾU HẲN
5. Phía trong: cỏ/bồn hoa, hàng cây thứ hai, công trình

**Đoạn vòng hồ nam/tây (v1/f017–f028):** nước → **cỏ dốc thấp** xuống nước
(không tường kè) → lát hẹp → nhựa đường. Cây lá rộng trồng sát mép nước,
thân **NGHIÊNG 25–45°**, tán vươn hẳn ra mặt hồ (f018, f022–f027 liên tiếp).

**Đoạn đầu hồ/công viên (v1/f001–f005):** lối đi **đá phiến tổ ong sẫm**
+ thảm cỏ rộng + bồn hoa cắt tỉa.

## 4. HỖN HỢP CÂY VEN HỒ THẬT (tần suất xuất hiện trong v1)

| Loại | Mức độ | Bằng chứng |
|---|---|---|
| **Cây lá rộng tán tròn, nhiều cây NGHIÊNG ra hồ** | **ĐA SỐ ở bờ nước** | f018, f021–f027 (ít nhất 7 frame), tán sẫm #29362a |
| Thông cao thẳng | Xen kẽ, nhiều ở đoạn đường lớn + phía trong | f013–f015, f026; v2/f001 (thân thẳng, tán thưa trên cao) |
| Hoa giấy tím (cụm lớn ven đường) | Điểm nhấn màu mạnh | f010, f012 — cụm tím phủ cả góc frame |
| Phượng tím | Lẻ, điểm nhấn | v2/f002; v3 tiền cảnh |
| Liễu rủ | Lẻ | v1/f007 phía xa |

→ Hàng cây bờ bắc THẬT là **hỗn hợp lá rộng nghiêng + thông xen kẽ + hoa giấy**,
KHÔNG phải một hàng thông đồng nhất. Mọi loại cây ven hồ đều có **gốc quét
vôi trắng** (cả cây nghiêng f021 lẫn thông f026), vôi cao ~1–1,2m, màu trắng
ngả xám/bẩn chứ không trắng tinh.

## 5. ĐỐI CHIẾU BẢN GAME HIỆN TẠI — SAI/THIẾU CỤ THỂ

Số game hiện tại: nước canvas **0x276a8a** + gợn #bfe6f5, đáy 0x14425c,
đêm emissive 0x1d4e5f (XH-1); lát nền **#dde2e2** + accent #b98a7a 4/16 ô,
ô 1u (XH-1/XH-3R); cỏ **0x5f8547**; kè #7e776c + bó vỉa 0xd8d2c2; thông
PineUmbrella đĩa (đo render: tán **#396645**, lát render #bec6c8, cỏ render
#567d4e); bờ bắc 9 thông tán ô thẳng hàng (XH-3R).

**Về MÀU:**
- **S1 (lớn nhất) — Nước sai hệ màu:** game teal bão hòa 0x276a8a; thật xám
  bạc #8f9595–#9ba1a5 ban ngày. Đây là gốc của cảm giác "sặc" + "bể bơi".
  (Số teal cũ đo từ ảnh tĩnh trong theme/ — ảnh tĩnh đã qua hậu kỳ màu mạnh;
  video cho tông thật trầm hơn hẳn.)
- **S2 — Lát quá trắng:** nền game #dde2e2 (render hiệu dụng #bec6c8) vs
  thật #acadab. Lát game sáng hơn thật rõ rệt ở tầm mắt.
- **S3 — Cỏ quá xanh tươi:** game 0x5f8547/render #567d4e vs thật olive
  #55662c–#6e6d29. Thiếu hẳn sắc vàng olive + vùng sẫm dưới bóng cây.
- **S4 — Tán cây quá xanh/đều:** thông game một tông #396645 đặc, phẳng;
  thật: lá rộng sẫm #29362a, thông thưa xám xanh lẫn trời.
- **S5 — Accent lát sai nhịp:** game rải accent #b98a7a đều 4/16 ô; thật ô
  nhấn rất thưa và chi tiết dọc chủ đạo là **dải tactile TỐI #909499 chạy
  dọc liên tục** — game không có dải này.
- **S6 — Thiếu hệ màu buổi chiều/đêm của hồ:** thật nước chuyển chàm
  #838eb2–#899bd3, Thủy Tạ lên đèn **magenta** phản chiếu hồng; game đêm chỉ
  có emissive teal 0x1d4e5f — sai cả hue.

**Về TIẾT DIỆN / CẤU TRÚC:**
- **S7 — Thiếu dải đường nhựa** phía trong đường dạo bờ bắc (lớp 4 của tiết
  diện). Không có nó, đường dạo game lơ lửng giữa cỏ và nước, không ra "phố
  ven hồ".
- **S8 — Mép nước sai vật liệu:** game tường kè đá hộp 1.14u liên tục + bó
  vỉa sáng chạy dài; thật phần lớn là **cỏ dốc thấp** chạm nước, kè thấp/
  khuất (freeboard 0,6u của game đúng số, nhưng hình thức mép sai).
- **S9 — Thiếu CÂY NGHIÊNG:** dấu ấn mạnh nhất của hồ trong video (7 frame)
  hoàn toàn vắng trong game; hàng bờ bắc game là 9 thông thẳng đều tăm tắp.
- **S10 — Thiếu hoa giấy ven đường:** điểm nhấn tím lớn nhất phía bờ
  (f010/f012) chưa có trong game.
- **S11 — Thiếu chất liệu lát thứ hai:** đá phiến tổ ong sẫm #5f574f ở đoạn
  đầu hồ/công viên.
- **S12 — Vôi gốc chưa đủ:** game mới có trụ vôi 0xe8e2d4 (quá trắng) ở 9
  thông bờ bắc; thật vôi ở MỌI cây ven hồ, cao ~1–1,2m, trắng ngả xám #919798
  (bóng) tới ~#d8d8d2 (nắng).

## 6. ĐỀ XUẤT PALETTE MỚI CHO VÙNG HỒ (giữ/đổi từng màu + lý do đo)

| Hạng mục | Hiện tại | Đề xuất | Lý do (số đo) |
|---|---|---|---|
| Nước ngày | 0x276a8a teal | **#8b979c** | trung vị dải đo ngày #8f9595–#9ba1a5, giữ lạnh nhẹ |
| Vệt gợn nước | #bfe6f5 | **#cfd8da** | giảm chói theo nước xám |
| Đáy hồ | 0x14425c | **#4c5a5e** | đáy xám sẫm hợp nước xám; bỏ xanh biển sâu |
| Nước chiều (mới, theo giờ) | — (chỉ có đêm teal) | **#7e8cb4** | đo v3/f001 #838eb2, f004 #899bd3 |
| Emissive đêm hồ | 0x1d4e5f | **#4a5a86** (chàm) | theo dải chàm v3, bỏ teal |
| Đèn Thủy Tạ đêm (mới) | — | **#d94fd0** + vệt phản chiếu hồng trên nước gần đảo | quan sát v3/f001, f006 |
| Lát chính | #dde2e2 | **#a9aba8** | đo #acadab (f015) |
| Accent lát | #b98a7a, 4/16 ô | **giữ hue, giảm còn ~1–2 ô/36** | thật rất thưa (f015) |
| Dải tactile dọc (mới) | — | **#8f9296** chạy dọc liên tục | đo #909499 (f015) |
| Bó vỉa | 0xd8d2c2 | **#b9bcba** | hạ sáng theo lát mới |
| Cỏ | 0x5f8547 | **#66702f** + vệt vàng khô/bóng sẫm #46512a trong TEX_GRASS | dải đo #55662c–#6e6d29 |
| Tán lá rộng (cây nghiêng, mới) | — | **#2f3d2b** | đo #29362a–#38442a |
| Tán thông | (GLB, render #396645) | **#46604c** xám xanh, thưa hơn | thông thật tán thưa lẫn trời (v2/f001) |
| Thân thông/cây | nâu GLB | **#6f655c** | dải nâu xám đo f026 + v2/f001 |
| Vôi gốc | 0xe8e2d4 | **#cfcfc8** | trắng ngả xám; đo bóng #919798 |
| Kè đá | #7e776c | **giữ** | đá xám nâu hợp dải đo; chỉ giảm độ dài tường lộ (xem §7) |
| Nhựa đường (mới) | — | **#545c63** | đo #525c65 (f015) |
| Hoa giấy (mới) | — | hoa **#9c2b8c** + lá #33502e | hoa thuần ước từ median lẫn lá #581a53–#623059 |
| Phượng tím | (theo ảnh tĩnh cũ) | **#54405a** cho cụm xa | đo cụm bóng v2/f002 #442c39–#5e4752 |

## 7. SỬA CẤU TRÚC KÈM THEO (đề xuất cho vòng thi công sau)

1. **Thêm dải đường nhựa** (rộng ~5–6u, #545c63, có vạch kẻ mờ) phía trong
   đường dạo bờ bắc + nối vào trục đường hiện có ở hai đầu; về sau traffic
   xe máy có thể chạy vòng hồ.
2. **Thêm cây lá rộng NGHIÊNG**: biến thể model nghiêng 25–45° ra mặt nước,
   gốc quét vôi, tán #2f3d2b — đặt 5–7 cây dọc bờ bắc + bờ tây; thông bờ bắc
   giảm xuống ~40% và xen kẽ, bỏ hàng đều tăm tắp.
3. **Thêm 2–3 cụm hoa giấy** lớn ven đường (đầu cầu đảo + giữa bờ bắc).
4. **Mép nước đổi vật liệu theo đoạn:** giữ kè đá ở đoạn bến + quanh đảo;
   các đoạn còn lại chuyển **taluy cỏ dốc thấp** chạm mặt nước (đúng f017–f028).
5. **Lối đá phiến tổ ong** #5f574f cho đoạn lối nối đầu hồ (thay lát xám ở
   đoạn công viên).
6. **Màu nước theo giờ** trong applyDayNight: ngày #8b979c → chiều #7e8cb4
   → đêm chàm sẫm + phản chiếu đèn đảo/bờ (mở rộng waterMats hiện có).

*Hồ sơ này chỉ là nghiên cứu. Thi công phối màu lại vùng hồ cần vòng riêng
theo đúng nhịp chuẩn (đo → sửa → render tầm mắt đối chiếu → 8 cổng → đẩy
GitHub).*
