# 19B — ĐẶC TẢ TỌA ĐỘ 3 TUYẾN XE MÁY V5.2

Tuyến song song B (08/11) — CHỈ trích xuất + thiết kế, không sửa code. Nguồn tọa độ: đọc trực tiếp `prototype-v2/index.html` (groundH/stairH/innerStairH/AW_NODES/LOOP/STALL_DEFS chép nguyên văn vào harness để đo). Mọi khoảng cách trong tài liệu này là **số đo của harness** `scripts/v52_traffic_harness.mjs` (26/26 PASS), không phải ước lượng.

> ⚠ **ĐỌC PHỤ LỤC Ở CUỐI TRƯỚC KHI DÙNG SỐ Ở THÂN BÀI:** trong lúc tuyến B làm việc, tuyến chính đã cài xong phần lớn v5.2 vào index.html (snapshot 07:36) — đổi profile làn đông, dời AW node 4/5/6, thêm ROUTE_RING/ROUTE_HILL riêng. Thân bài (mục 0–8) là thiết kế trên snapshot TRƯỚC cài; **Phụ lục A đối chiếu bản đang cài và thay thế các số tương ứng** (bán kính làn, R-02, R-03, danh sách rủi ro nâng lên 11 điểm).

## 0. Hiện trạng traffic trong code (điểm xuất phát)

- Xe chạy hiện tại: 6 mô tô + 1 ô tô, tất cả `kind:'road'`, chạy thẳng trục X, wrap ở ±86. Làn: dir+1 (sang đông) z gốc **−1.5**, dir−1 (sang tây) z gốc **4.5**; đoạn ngang đảo lượn nam theo `islandBump(x)`: `z = lane + (lane<2 ? 8.1 : 4.1) * islandBump(x)`. Cao độ xe lấy `entryRampY(x)` (0 khắp, trừ dốc tây x<−52 tối đa 2.0). Tốc độ mô tô 6–8, ô tô 5.4; một nửa xe chạy đêm (`nightRoad`).
- **Vòng xe kín quanh đảo đã bị BỎ từ v4.8** (comment trong code): đảo R10.5 tựa sườn đồi + thềm thang ở góc đông-bắc, vòng r10.6/11.9 cũ sẽ chạy xuyên đảo. Hệ quả cho thiết kế: "vòng bùng binh" trong research/19 phải hiểu là **cung lượn phía nam đảo** của 2 làn trục X (bán kính thực đo 12.6/14.6 từ tâm đảo), KHÔNG phải vòng tròn kín.
- Code hiện tại **chưa có** giãn cách (xe cùng làn tốc độ khác nhau 6–8 chắc chắn dồn/đè nhau sau đủ lâu), chưa có nhường người, chưa có tấp lề NPC, thuê xe hết giờ là biến mất ngay (`endRide`). Harness đã cung cấp logic thuần cho cả 4 thứ này (mục 7).

## 1. Bản đồ tọa độ các khu (trích xuất)

| Khu | Tọa độ khóa | Cao độ |
|---|---|---|
| Đảo bùng binh | tâm **(−24, −6)**, R **10.5**; collider vuông solid(−24,−6,10.4,10.4); mặt thảm y≈0.93 | thềm phẳng 0 (x −45..−19, z −16..−2) |
| Tượng đài | **(−28.2, −2.8)** lệch tây-nam tâm đảo 5.28; bệ đá 8.8×8.8; vành đèn uplight R11.6; điểm check-in tượng ở (−13.2, 2.8) | bệ y≈1.02–1.3 |
| Xe đậu vành đảo | R12.6 ở các cung 20/45/70/95/120/150/180°, R13.8 ở 200/238°; 3 ô tô phía tây (−40.2,−8), (−40.8,−3), (−40.2,2.5) | 0 |
| Đường vào / trục chính | làn E z=−1.5, làn W z=4.5, x −86..86; dốc đầu tây x<−52 | entryRampY: 0 → 2.0 (dốc 7%) |
| Xe đậu dọc đường vào | hàng z=−7.2 và z=9.9, x −78..−53 (bám dốc) | theo dốc |
| Dãy sạp trước chợ | z=10.15, x −56..37.5 (bánh ướt −56 → hoa 37.5); hàng xe đậu sau sạp z=11.75 (chừa trống x −5.5..5.5 lối vào) | 0 |
| Nhà lồng | x −34..34, z 12..28; hàng cột z=12.2 | sàn 0.5 |
| Bãi xe / thuê xe | RENT_PT hiện tại **(31.5, 13.8)** ⚠ xem R-01; hàng xe đậu đông (z=8.9, x 40..52) | — |
| Bậc thang lớn | x −11..11, z −30..−2: chuyến C −8.25..−2 (5.67→0), chiếu nghỉ 2 (5.67), chuyến B (11.33→5.67), chiếu nghỉ 1 (11.33), chuyến A (17→11.33); sạp trên thang: khoainuong (6.2,−21.6), suadau (6.2,−10.4) | bậc rời rạc 10 nấc/chuyến |
| Cầu nổi | deck x 14.5..20.5, z −30..9, dốc 0.11282 | 17.14 (z=−30) → 12.74 (z=9) — VƯỢT QUA đường trục |
| Đồi / quảng trường | z ≤ −30; Góc Hát (24.6,−48.5); đỉnh đồi check-in (10,−57) | 17 |
| Thang trong nhà | x 29..33, z 12..26.8: chuyến 1: 12.6→6.55 (z 12..18.4), chiếu nghỉ 6.55 (18.4..20.4), chuyến 2: 6.55→0.5 (20.4..26.8) | innerStairH |

Đồ thị người: **AW_NODES** 36 nút / 35 cạnh (trục chính: nút 0–15 từ đầu đường vào (−76,2) lên đỉnh đồi (24,−51), rẽ nhánh cầu 22–29, nhánh thang 30–35). **LOOP** đi bộ 21 điểm. Cả hai đã chép nguyên văn vào harness.

## 2. TUYẾN 1 — Cung nam đảo + trục đường vào (2 làn, trục X)

Giữ nguyên công thức đang chạy (đã quen mắt trong render), harness đo lại toàn bộ:

`zE(x) = −1.5 + 8.1·islandBump(x)` (dir +1) · `zW(x) = 4.5 + 4.1·islandBump(x)` (dir −1) · `islandBump` = smoothstep lên ở x −46..−30, xuống ở −18..−2.

| x | −86..−46 | −38 | −30 | −24 | −18 | −12 | −6 | −2..86 |
|---|---|---|---|---|---|---|---|---|
| islandBump | 0 | 0.50 | 1 | 1 | 1 | 0.684 | 0.156 | 0 |
| z làn E | −1.5 | 2.55 | **6.6** | **6.6** | **6.6** | 4.04 | −0.24 | −1.5 |
| z làn W | 4.5 | 6.55 | **8.6** | **8.6** | **8.6** | 7.30 | 5.14 | 4.5 |

Số đo kiểm chứng (harness T1/T1b/T2/T3):
- Bán kính cung nam đảo từ tâm (−24,−6): làn E **12.6**, làn W **14.6** → khe hở tới mép đảo R10.5: E 1.75, W 3.75 (sau khi trừ nửa xe 0.35). Không điểm nào của 2 làn lọt vào đĩa đảo, bệ tượng (R4.4+0.35), hay hộp collider đảo.
- Khe hở 2 làn đối diện: tâm–tâm tối thiểu **2.00** tại x=−30 (đỉnh lượn) → khe hở thực **1.30** ≥ 0.8 ✓. Trên đoạn thẳng: 6.0.
- Dốc: 0% khắp trục, riêng dốc đầu tây **7%** (entryRampY) ≤ 12% ✓. Xe không vào hình chữ nhật bậc thang x[−11,11]×z[−30,−2] ở bất kỳ mẫu nào.
- Cầu nổi: deck trên 2 làn cao tối thiểu **13.25** (tại z=4.5) → xe chạy DƯỚI cầu, tĩnh không ~10.4 ✓ (T1c). Cấm dùng groundH cho xe trên trục (xem R-07).

Vùng chậm của Tuyến 1 (chi tiết ở mục 5): SZ-1 cả 2 làn x −44..−6 cap 3.0 (cung đảo); SZ-2 x −5..5 cap 3.5 (mặt tiền); SZ-3 x −58..−46 cap 3.5 (đầu tây); SZ-5 chỉ làn W x −46..10 cap 3.5 (hàng sạp đêm z=3).

## 3. TUYẾN 3 (đề xuất tuyến B) — Spur bãi xe phía đông

Một chiều, hở 2 đầu: rời làn E ở (28,−1.5), vòng qua bãi xe đông + điểm thuê xe đề xuất, nhập lại làn W ở (28,4.5). Toàn tuyến groundH = 0, dốc 0% (T2), ngoài mọi vùng cấm (T1):

| Điểm | (28,−1.5) | (36,−1.3) | (43,−0.5) | (46.5,2.5) | (46.5,6.5) | (45,7.6) | (41,7.3) | (37,7.0) | (31,5.2) | (28,4.5) |
|---|---|---|---|---|---|---|---|---|---|---|
| s tích lũy | 0 | 8.0 | 15.0 | 19.7 | 23.7 | 25.5 | 29.5 | 33.5 | 39.8 | 42.9 |

Ràng buộc đã kiểm: chân bắc (45,7.6)→(37,7.0) giữ z ≤ 7.6, cách hàng xe đậu z=8.9 là 1.3 (khe hở 0.6 — điểm theo dõi, không nới thêm về bắc); cách sạp hoa (37.5,10.15) 3.15; AW node gần nhất (30.3,11) cách 5.8. (Bản đang cài dùng ROUTE_HILL khác — xem Phụ lục A.5; tuyến này giữ vai trò phương án dự phòng đã kiểm chứng sạch.)

## 4. Điểm tấp lề (pull-over) — 9 điểm, đo ở T8/T9

| ID | Tuyến | Tọa độ | Phục vụ | Khoảng cách đo |
|---|---|---|---|---|
| T1-E1 | E | (−13.2, 0.22) | khách chờ mép đông-nam đảo (−13.2, 2.8) | giao 2.58 |
| T1-E2 | E | (−52, −1.5) | đầu đường vào tây | — |
| T1-W1 | W (lệch làn) | (0, 6.2) | khách vỉa hè trước mặt tiền (0, 7.4) | giao 1.2; lệch làn W 1.7 |
| T1-W2 | W (lệch làn) | (22, 6.2) | sạp sua — mặt khách (22, 7.95) | lấy 1.75 |
| T1-W3 | W (lệch làn) | (−56, 6.2) | sạp banhuot — mặt khách (−56, 7.95) | lấy 1.75 |
| T1-W4 | W | (−50, 4.5) | khách đầu đường vào tây (−51, 1.2) | giao 3.45 |
| T-FOOT | E (lệch làn) | (8, 0.2) | gửi xe leo thang lấy hàng (suadau) | đi bộ 10.61 |
| T3-0 | 3 | (36, 7.1) | điểm thuê xe đề xuất (35.5, 8.5) | 1.49 |
| T3-1 | 3 | (41, 7.3) | khách bãi xe đông (41, 9.6) | giao 2.3 |

Quy tắc: điểm "lệch làn" nằm trên vỉa hè giữa làn và mặt sạp — cách tâm làn ≥1.7 để xe qua lại không cọ xe đang đỗ (T8 kiểm cả 9 điểm: không lấn làn đối diện, ngoài đảo).
## 5. Vạch sang đường + vùng chậm (an toàn người đi bộ)

Đồ thị AW chạy DỌC hành lang đường (trục đi bộ z=2 ở đầu tây cách 2 làn 3.5/2.5 — xử bằng yield theo bán kính, không cần vùng chậm) và CẮT làn tại cung đảo + mặt tiền. Mọi giao cắt ở cao độ đường đều nằm trong vùng chậm (T7 kiểm 3 lớp: node crossing / giao cắt cạnh / đoạn cạnh chạy sát làn <1.6):

| Giao cắt (cao độ đường) | Làn | Vùng chậm phủ |
|---|---|---|
| cạnh 3-4 (x≈−38.5), 4-5 (x≈−25), 5-6 (x≈−23), 6-7 (x≈−9) | E | SZ-1 |
| cạnh 7-8 (x≈−3.9), 8-19 (tại (0,4.5)) | W | SZ-2 |
| cạnh 24-25, 25-26 tại x=17.5 | cả 2 | PHÂN TẦNG ĐỨNG (đi trên deck cầu, groundH 13.8–12.99) — không cần yield |

Vùng chậm đầy đủ (khai trong harness `SLOW_ZONES`): SZ-1 E/W x[−44,−6] cap 3.0 · SZ-2 E/W x[−5,5] cap 3.5 · SZ-3 E/W x[−58,−46] cap 3.5 · SZ-5 W x[−46,10] cap 3.5 (mặt khách hàng sạp z=3 cách làn W 0.5–2.1) · SZ-W-đông x[5,11] + x[11,26] cap 3.5 (AW node 16/17/18 chạy song song làn W) · Tuyến 3: s[0,12] + s[52,78] cap 3.0 (đoạn nhập/xuất).

## 6. Ba nhiệm vụ giao hàng mẫu (đo ở T9, bán kính hoàn thành 3.6 như tiền lệ rent)

| NV | Lấy hàng (sạp → mặt khách) | Chặng chạy | Giao (khách chờ ← tấp lề) | Ngân sách giờ đề xuất |
|---|---|---|---|---|
| M1 | sua (22,10.15) → (22,7.95); đỗ T1-W2 (22,6.2), lấy 1.75 | làn W về tây ≈35 | (−13.2,2.8) ← T1-E1: 2.58 | 45s |
| M2 | banhuot (−56,10.15) → (−56,7.95); đỗ T1-W3, lấy 1.75 | làn E sang đông ≈84 + Tuyến 3 s≈29.5 → tổng ≈114 | (41,9.6) ← T3-1: 2.3 | 60s |
| M3 | suadau (6.2,−10.4) TRÊN thang (h 5.67) → mặt khách (8.4,−10.4); gửi xe T-FOOT (8,0.2), đi bộ leo thang 10.61 | làn W về tây ≈58 | (−51,1.2) ← T1-W4: 3.45 | 50s (gồm leo thang) |

M3 là nhiệm vụ "lai": xe không leo bậc thang (đúng research/19) — người chơi gửi xe ở chân thang, đi bộ lên lấy món, quay xuống chạy tiếp.

## 7. Bàn giao cho đợt cài đặt (logic thuần đã sẵn trong harness)

| Thuật toán | Hàm trong harness | Tham số đã kiểm chứng |
|---|---|---|
| Theo làn + giãn cách: `v = min(vRoute, max(0, (gap − minGap)·k))`, tới comfortGap chạy hết tốc độ | `followSpeed()` | minGap 2.2 · comfortGap 4.5 · trần-route trừ vùng chậm; sim 600s min gap: E 3.59 / W 3.74 (kèm 1 xe dừng 6s ở cung đảo) ≥ 2.0 ✓ (T10) |
| Nhường người qua đường: trong bán kính yieldR phía trước → giảm tốc tuyến tính, dừng ở stopGap | `yieldSpeed()` | lookAhead 7 · yieldR 2.6 · stopGap 1.3; test: dừng tại s=62.1, vạch ở 64.0, không xâm phạm vùng 0.7 quanh người (T11) |
| Chu trình tấp lề 8 trạng thái: CRUISE→DECEL→STOPPED→RIDER_DOWN→SHOP→RETURN→BOARD→DEPART→CRUISE | `poStep()` | dwell SHOP 6s; trọn vòng mô phỏng 20.6s ≤ 30s (T12) |
| FSM thuê xe: IDLE→RENTED (90s; xuống xe giữ deadline, không park-zone) → đếm ngược hiển thị khi ≤10s → hết giờ RETURNING (NPC tự lái về bãi) → IDLE | `rentStep()` | kiểm: countdown đúng mốc 10s, RETURNING xuất hiện ở đúng 30s mô phỏng còn lại, về đúng RENT_PT (T13) |

Trần xe chạy đồng thời: **14** (như research/19; sim T10 chạy 7 xe/làn là kịch bản đông nhất của thiết kế).

## 8. Cách chạy harness

```
node scripts/v52_traffic_harness.mjs [--verbose]
```

26 test (T0a–T16): T0 sanity dữ liệu + phơi bày R-01 · T1/T1b/T1c vùng cấm/đảo/cầu · T2 dốc · T3 khe hở 2 làn · T4 xe đậu vành đảo · T5 thân sạp · T6/T7 AW + vùng chậm · T8 tấp lề · T9 nhiệm vụ mẫu · T10 giãn cách sim 600s · T11 yield · T12 chu trình tấp lề · T13 FSM thuê xe · T14–T16 đo hình học BẢN ĐANG CÀI (vòng đảo / ROUTE_HILL / giao tuyến). Thoát mã 0 khi mọi test đạt (các test "PHƠI BÀY" đạt khi đo đúng rủi ro đã đăng ký).

---

# PHỤ LỤC A — ĐỐI CHIẾU BẢN ĐANG CÀI V5.2 (snapshot index.html 07:36, 08/11)

Tuyến chính cài v5.2 gần như đồng thời với tuyến B. Phụ lục này đo lại chính hình học bản đang cài bằng harness (đã nạp `laneZE/laneZW/vehBumpE` + AW_NODES mới + ROUTE_RING/ROUTE_HILL của bản cài) và **thay thế các số tương ứng ở thân bài**.

## A.1 Làn trục chính — công thức mới

- Làn đông: `laneZE(x) = −1.5 + 7.4·vehBumpE(x)`, `vehBumpE = s(−38,−27)·(1−s(−21,−10))` → đỉnh **z = 5.9** trên cao nguyên x −27..−21 (hẹp hơn islandBump cũ có chủ đích: né hàng chờ sạp mặt tiền + cụm bàn ăn nam đảo (−17.5, 5.5)).
- Làn tây: `laneZW(x) = 4.1 + 4.5·islandBump(x)` → gốc hạ 4.5→**4.1**, đỉnh **8.6**.
- Số đo thay thế mục 2: bán kính cung nam đảo làn E **11.81** (khe hở tới mép đảo **0.96**), làn W **14.6** (3.75); khe hở 2 làn đối diện tối thiểu: tâm–tâm **2.70** tại x=−27 → khe hở thực **2.00** ✓ (tốt hơn bản thiết kế 1.30).

## A.2 AW node 4/5/6 đã dời — thiết kế "đảo refuge" ĐẠT

Bản cài dời: node 4 (−36.5,2)→**(−35,2.5)**, node 5 (−24,6.8)→**(−24,7.15)**, node 6 (−11.5,2.5)→**(−11.5,0.2)**. Đo lại (T6): node 5 nằm giữa 2 làn nam — cách làn E **1.25**, làn W **1.45** (đều > 1.1; khe hở sau khi trừ nửa xe + bán kính người ≈ 0.55/0.75) → vai trò refuge khi sang đường khả thi, vẫn cần yield 2 phía (đã khai CROSSINGS). Node 4/6/16 đều ra khỏi lớp <1.1. **Node <1.1 duy nhất còn lại: node 7 (−4,4.5), cách laneZW 0.21** — giữ nguyên khuyến nghị yield + vùng chậm SZ-2. CROSSINGS rút còn {node 5 (refuge), node 7}.

## A.3 R-02 cập nhật — vành đậu cung nam xung đột NẶNG HƠN với làn E mới

Đo lại khoảng cách xe đậu vành đảo ↔ 2 làn đường (T4): deg20 **0.81**, deg45 **0.79**, deg70 **0.22**, deg95 **0.65**, deg120 **0.47**, deg150 **0.29** (cả 6 đều chật/xuyên sau khi trừ 2 nửa xe 0.7); deg180 **4.63**, deg200 **9.28**, deg238 **17.33** (an toàn với làn đường). Nguyên nhân: làn E mới chạy bán kính 11.9–12.4 ở cung nam, cắt qua vành đậu R12.6. **Khuyến nghị thay thế:** rút toàn bộ xe đậu khỏi cung nam đảo (deg 20–150) — chỉ giữ cung tây/bắc (180/200/238) + bổ sung vào hàng z=11.75. (Số cũ ở thân bài — deg95 d=0.04 theo islandBump cũ — không còn hiệu lực.)

## A.4 R-03 cập nhật — vehBumpE dọn sạch làn E; phát sinh phía làn W

- dauhu/xien vs làn E: **hết overlap** (laneZE tại x=−38 là −1.5; tại x=−12 là −0.76) ✓ — bản cài tự xử lý tốt hơn đề xuất dời sạp ở thân bài; khuyến nghị dời dauhu/xien **rút lại**.
- Phát sinh: laneZW gốc 4.1 áp sát hàng sạp đêm z=3 — theo xấp xỉ tròn tâm def, **che (6,3) và tron (30,3) overlap d=1.10** (ngưỡng thân 1.45). LƯU Ý: xấp xỉ tròn đặt thân sạp tại tâm def; nếu origin stall.glb lệch ra trước thì đây chỉ là graze. **Cần đối chiếu render/GLB trước khi kết luận** — R-03 (bản mới) ở trạng thái "chờ xác minh trực quan"; vùng chậm SZ-5 (làn W x −46..10, cap 3.5) đã bao phủ cả 2 sạp.

## A.5 Tuyến vòng đảo + chân đồi CỦA BẢN CÀI (khác thiết kế thân bài)

- **ROUTE_RING_OUT/IN có thật**: cung nam–tây–bắc quanh đảo trên thềm phẳng + sân nam, R14.2 (phình 16.2 ở 210°, 15.2 từ 320°) / R12.7 (cung nam 12.3), chạy pingpong + `ringSwitch` đổi làn ở 2 đầu cung. Đo T14a: mọi đỉnh cung ngoài đĩa đảo + bệ tượng, groundH = 0 ✓. (Thân bài kết luận "không có vòng kín" — đúng là không kín; bản cài dùng cung hở + quay đầu, hợp lệ.)
- **ROUTE_HILL khác Tuyến 3 ở thân bài**: loop kín z=12.3 sau dãy sạp mặt tiền → xuống x=−48.5 → hành lang nam đảo (−31,5.6), (−24,6.1), (−17,3.4) → trục z≈−1.3 → lên ở x=54. Tuyến 3 (spur bãi xe đông) ở thân bài vẫn là phương án dự phòng đã kiểm chứng sạch; bản cài không dùng nó.
- **R-09 (MỚI): vòng đảo × xe đậu vành đảo.** Dây cung RING_IN 300°→320° xuyên thẳng xe đậu **deg45: d = 0.04** (khe hở −0.66); RING_OUT ↔ deg200: **d = 0.39**. Khuyến nghị A.3 (rút xe đậu cung nam) xử lý được deg45; deg200 cần dời riêng hoặc nắn cung OUT ở góc 160°.
- **R-10 (MỚI): chân bắc ROUTE_HILL z=12.3 × hàng xe đậu z=11.75.** Khoảng cách 0.55 → khe hở **−0.15** (cọ hàng xe đậu mật độ ~82% dọc x −46..46, trừ gap −5.5..5.5 và hai đầu); đồng thời 2/13 đỉnh loop nằm trong dải sàn nhà lồng z≥12 ở |x|≤34, và hàng cột sạp ở z=12.2 chạy dọc cùng hành lang. Có thể là chủ đích "làn sau sạp" nhưng với hàng xe đậu hiện hữu thì xe chạy sẽ cọ xe đậu — **cần soi render để kết luận chủ đích hay lỗi**.
- **R-11 (MỚI): ROUTE_HILL × ROUTE_RING_IN chạm nhau ở nam đảo** (khoảng cách nhỏ nhất **0.01** tại ~(−24, 6.1–6.3)). `updateTraffic` của bản cài chỉ giãn cách xe **cùng tuyến** (`o.rt === v.rt`) — 2 tuyến cắt nhau không có cơ chế nhường; xe 2 tuyến có thể đè nhau tại điểm này. Khuyến nghị: gán điểm giao là nút nhường chung (mọi xe trong bán kính 4 quanh (−24,6.2) giảm tốc ≤3) hoặc nắn 1 trong 2 tuyến lệch ≥2.5.

## A.6 Những phần bản cài đã tự làm (thay thế R-08 một phần)

- `updateTraffic`: đã có giãn cách cùng làn (gap<7 → giảm tốc, sàn 0.8) + chậm/dừng khi người chơi/wanderer cắt ngang (lateral <1.7, ahead <5.5, dừng ở ~1.2) — gần khớp đặc tả logic thuần của harness (T10/T11 giữ vai trò kiểm chứng độc lập).
- Tấp lề NPC: đã có 2 xe (sạp sua — đỗ [19.6,4.4]; banhtrang — đỗ [−33.2,4.5]) với chu trình steer → dwell 9–17s → shopper đi bộ → quay lại. Lưu ý: 2 điểm đỗ nằm ngay trên làn W (laneZW tại các x đó ≈ 4.1–4.3) — xe đỗ chắn làn, xe sau xử bằng giãn cách (chấp nhận được, đúng chất phố thật).
- Thuê xe P3: đã có mục riêng trong code (header "V5.2 P3: THUÊ XE NÂNG CẤP" + NPC né xe người chơi). R-01 (RENT_PT trên thang trong nhà): tại snapshot 07:36, RENT_PT vẫn là (31.5, 13.8) — **chưa thấy dời**; khuyến nghị dời về (35.5, 8.5) giữ nguyên hiệu lực.

## A.7 Tổng kết rủi ro sau đối chiếu: 11 điểm

R-01 (RENT_PT — còn mở) · R-02 (vành đậu nam × làn E mới — nặng hơn, đã có khuyến nghị mới) · R-03 (che/tron × laneZW — chờ xác minh render) · R-04 (trục đi bộ tây — đã xử bằng refuge + yield) · R-05 (graze sạp mặt tiền — vùng chậm) · R-06 (ô tô tây đảo — vùng chậm) · R-07 (groundH bóng cầu — đã ghi luật entryRampY) · R-08 (logic giãn cách/yield/tấp lề/thuê — bản cài đã làm, harness kiểm chứng độc lập) · R-09 (vòng đảo × xe đậu — mới) · R-10 (chân bắc ROUTE_HILL × hàng xe đậu — mới, chờ soi render) · R-11 (giao tuyến nam đảo — mới).
