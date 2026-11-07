# 15 — THIẾT KẾ VẬT PHẨM TRANG PHỤC (P0-1: Tủ đồ mặc được thật)

> Lệnh Chung Hy 03:16 ngày 07/11/2026: "thêm 1 lượt thiết kế các vật phẩm trang phục cho game, lập danh sách rồi làm" — tài liệu này là **danh sách thiết kế**; lượt dựng đi ngay sau theo research/14 mục 2.
> Nền đã khóa, không thiết kế lại: 5 ô trang bị (Mũ / Khăn / Áo / Tay cầm / Giày) + ô Phụ kiện; `state.wardrobe[]` + `state.equipped{}` trong save `chohb3d-v1`; **bảng 14 màu áo cố định** (research/13, đã khóa ở v4.3); node mũ `HatBeanie / HatCap / HatNonLa` và node `Scarf` đã có sẵn trên character (NPC đang dùng, người chơi đang đội beanie đỏ đô).
> Thước đo hình dáng: ảnh chốt `theme/CHOT-phong-cach-cho-dem.png` — mũ len có chóp bông, khăn dày quấn cổ, áo khoác dạ, ba lô vải: đúng chất **đồ len Đà Lạt**.
> **Cập nhật 03:21 ngày 07/11/2026:** Chung Hy chốt bản 21 món là "quá ít" → mở rộng lên **60 món**: giữ nguyên vẹn 21 món cũ (M1–P4), thêm 39 món mới + ô Giày (G1–G8) + 5 bộ sưu tập theo chủ đề (mục 2), cân lại phân tầng mở khóa 40/35/25 (mục 3). Toàn bộ chuẩn đã khóa (bảng 14 màu, thang ấm, sạp gắn, 0 GLB mới) giữ nguyên.

## 0. Bảng 14 màu cố định (lấy đúng hex trong code — `CROWD_SHIRTS`, index.html)

| # | Tên màu | Hex | # | Tên màu | Hex |
|---|---|---|---|---|---|
| 1 | Đỏ đô | `#a62b25` | 8 | Dương | `#3a6bc2` |
| 2 | Cam đất | `#d97a30` | 9 | Oải hương | `#8668c4` |
| 3 | Vàng mù tạt | `#d9a62e` | 10 | Hồng đào | `#e58e6b` |
| 4 | Kem bơ | `#e8c87e` | 11 | Hồng sen | `#c95d7e` |
| 5 | Xanh rêu | `#6b8f3e` | 12 | Nâu cà phê | `#7a4a2e` |
| 6 | Xanh thông | `#2e6b46` | 13 | Nâu đất | `#96683f` |
| 7 | Teal | `#2f8f83` | 14 | Navy ấm | `#35507a` |

Ngoại lệ duy nhất ngoài bảng: đỏ nhấn `#c8372d` (đã khóa trong palette v4.3 cho chữ CHỢ ĐÀ LẠT) — chỉ dùng cho **chi tiết nhỏ phát sáng** của lồng đèn sao, đúng quy tắc "đỏ nhấn ≤5% khung hình".

**Thang Độ Ấm tham chiếu** (thanh Độ Ấm 0–100, lạnh <25 bị chậm — hệ sẵn có): mũ +5…+9 · khăn +10…+12 · áo +15…+20 (riêng gile lớp ngoài +10) · giày +1…+6 · găng/phụ kiện +0…+7 · đồ nóng cầm tay +2…+3. Full set thường ≈ **+45**; full set đẹp nhất ≈ **+64**, cộng +3 khi mặc đủ 1 bộ sưu tập → trần ≈ **+67** — đủ để đi đêm khuya mà không "bất tử" trước cái lạnh (chi tiết ở mục 3).

**Sạp gắn đúng trong game:** `LEN BÀ BẢY` (id `len1`, trong nhà lồng) · `MŨ & GĂNG LEN` (id `len2`, trong nhà lồng) · `QUÀ LƯU NIỆM` (id `luuniem`, đồi Hòa Bình) · `KI-ỐT ĐỒNG HỒ` (id `dongho`, đồi Hòa Bình) · sạp sữa đường vào (id `suatuoi`) · sạp `KHOAI/BẮP NƯỚNG` + sạp `BÁNH TRÁNG NƯỚNG` (cụm sạp nóng chợ đêm — bán bản "cầm khoe" của món đang nướng). Cấp = cấp **"Khách quen chợ"** (P0-2 đã xong ở v4.3, 11 mốc cấp).

---

## 1. DANH SÁCH VẬT PHẨM — 60 món / 6 ô

### Ô MŨ (12 món)

| # | Món | Hình dáng dựng | Màu (hex) | Ấm | Giá / mở khóa | Hiếm |
|---|---|---|---|---|---|---|
| M1 | **Mũ len beanie trơn** | Tái dùng nguyên node `HatBeanie`, chỉ `recolor` — món người chơi đang đội sẵn. Độ khó **S** | Đỏ đô `#a62b25` | +8 | **Có sẵn từ đầu** (bản bán thêm các màu ở len2: 30 Xu) | Thường |
| M2 | **Mũ len chóp bông** ⭐ ảnh chốt | `HatBeanie` + 1 cầu bông nhỏ trên đỉnh + vành gập dày hơn (cyl thấp). **S** | Vàng mù tạt `#d9a62e` | +9 | 45 Xu — `MŨ & GĂNG LEN` (len2) | Thường |
| M3 | **Mũ len dâu tây** | `HatBeanie` hồng sen + chóp lá xanh (2 box mỏng hình lá) + chấm hạt trắng (chấm canvas trên vật liệu). **M** | Hồng sen `#c95d7e`, lá xanh thông `#2e6b46` | +8 | 55 Xu — len2 | Hiếm |
| M4 | **Bịt tai bông len** | 2 cầu bông ép dẹt ở 2 bên đầu + dải vòng qua đỉnh (torus cắt nửa). Không dùng node mũ — group riêng gắn đầu. **M** | Hồng đào `#e58e6b` | +6 | 40 Xu — len2 | Thường |
| M5 | **Mũ nồi beret kiểu Pháp** | Cyl dẹt đường kính lớn + núm cầu nhỏ trên đỉnh — gợi kiến trúc Pháp của Đà Lạt. **S** | Nâu cà phê `#7a4a2e` | +5 | 50 Xu — `LEN BÀ BẢY` (len1), **yêu cầu cấp 3** | Hiếm |
| M6 | **Nón lá Đà Lạt** | Tái dùng nguyên node `HatNonLa` của NPC. Món ban ngày: ấm thấp nhưng là dấu hiệu "đi chợ sáng". **S** | Kem bơ `#e8c87e` (màu lá khô sẵn có) | +2 | 35 Xu — `QUÀ LƯU NIỆM` (luuniem) | Thường |
| M7 | **Mũ bucket len tai bèo** | `HatBeanie` + vành cyl dẹt ôm quanh đầu — bucket bản len, silhouette khác hẳn beanie. **S** | Xanh rêu `#6b8f3e` | +7 | 50 Xu — len2, **yêu cầu cấp 3** | Hiếm |
| M8 | **Mũ len sọc ngang** | `HatBeanie` + texture canvas 2 sọc ngang (đồng bộ họa tiết với A3). **S** | Teal `#2f8f83` × kem bơ `#e8c87e` | +8 | 50 Xu — len2 | Thường |
| M9 | **Mũ len cẩm tú cầu** 🌸 Bộ Cẩm Tú Cầu | `HatBeanie` + chấm hoa canvas cùng họa tiết K4 để nhận diện bộ. **M** | Oải hương `#8668c4`, chấm dương `#3a6bc2` | +8 | 65 Xu — len1, **điều kiện: dấu hộ chiếu khu Nông sản & Hoa** | Đặc biệt |
| M10 | **Mũ len tai mèo** | `HatBeanie` + 2 tai tam giác (box vát) trên đỉnh — món dễ thương cho người chơi trẻ. **M** | Hồng đào `#e58e6b` | +7 | 60 Xu — len2, **yêu cầu cấp 3** | Hiếm |
| M11 | **Mũ len thêu nhà ga** 🚂 Bộ Nhà Ga | `HatBeanie` + decal canvas hình nhà ga Đà Lạt nhỏ trước trán. **M** | Cam đất `#d97a30` | +8 | 70 Xu — luuniem, **yêu cầu cấp 4** | Hiếm |
| M12 | **Mũ len dã quỳ** 🌼 Bộ Dã Quỳ | `HatBeanie` + 1 bông dã quỳ (cầu + cánh) lệch bên như chi tiết A4. **M** | Vàng mù tạt `#d9a62e`, hoa cam đất `#d97a30` | +8 | **Thành tựu: ăn đủ 5 món khác nhau trong Sổ Đặc Sản** — không bán | Đặc biệt |

### Ô KHĂN (8 món)

| # | Món | Hình dáng dựng | Màu (hex) | Ấm | Giá / mở khóa | Hiếm |
|---|---|---|---|---|---|---|
| K1 | **Khăn choàng len trơn** | Tái dùng nguyên node `Scarf` (đang ẩn ở người chơi, NPC dùng), bật visible + `recolor`. **S** | Xanh thông `#2e6b46` | +10 | 35 Xu — `LEN BÀ BẢY` (len1). *Món này đã bán trong game, chỉ cần nối vào tủ đồ* | Thường |
| K2 | **Khăn choàng kẻ caro** | Node `Scarf` + texture canvas kẻ caro 2 màu vẽ bằng code (không thêm file ảnh). **M** | Đỏ đô `#a62b25` × kem bơ `#e8c87e` | +11 | 60 Xu — len1 | Hiếm |
| K3 | **Khăn len dài tua rua** | `Scarf` kéo dài xuống ngực + 4 dải tua (box mỏng) ở 2 đầu khăn đung đưa theo bước đi (xoay nhẹ theo nhịp đi sẵn có). **M** | Cam đất `#d97a30` | +12 | 70 Xu — len1, **yêu cầu cấp 4** | Hiếm |
| K4 | **Khăn choàng cẩm tú cầu** | `Scarf` oải hương + chấm hoa canvas (chấm tròn xanh dương/hồng như hoa cẩm tú cầu). **M** | Oải hương `#8668c4`, chấm dương `#3a6bc2` | +10 | 65 Xu — len1, **điều kiện: đã đóng dấu hộ chiếu khu Nông sản & Hoa** | Đặc biệt |
| K5 | **Khăn len ống** | Torus dày ôm quanh cổ (khăn ống không tua — silhouette gọn, khác hẳn K1/K3). **S** | Navy ấm `#35507a` | +11 | 55 Xu — len1, **yêu cầu cấp 3** | Hiếm |
| K6 | **Khăn choàng sọc dọc** | `Scarf` + texture canvas sọc dọc 2 màu. **M** | Nâu đất `#96683f` × kem bơ `#e8c87e` | +10 | 55 Xu — len1, **yêu cầu cấp 3** | Hiếm |
| K7 | **Khăn choàng dâu tây** 🍓 Bộ Dâu Tây | `Scarf` + chấm dâu canvas (quả đỏ đô nhỏ + lá xanh thông). **M** | Hồng sen `#c95d7e` | +10 | 70 Xu — len1, **yêu cầu cấp 4** | Hiếm |
| K8 | **Khăn choàng chợ đêm** 🌙 Bộ Chợ Đêm | `Scarf` + chấm sao/lồng đèn canvas vàng phát sáng nhẹ ban đêm. **M** | Navy ấm `#35507a`, chấm vàng mù tạt `#d9a62e` | +11 | 75 Xu — len1, **điều kiện: dấu hộ chiếu Chợ đêm Âm Phủ + chỉ bán ban đêm** | Đặc biệt |

### Ô ÁO (10 món)

Áo dựng bằng **đổi vật liệu thân + thêm chi tiết mesh mỏng** trên thân nhân vật hiện có (không dựng character mới). Lưu ý phân lớp với nâng cấp "Áo ấm" cũ: áo tủ đồ cộng **Độ Ấm trực tiếp**; nâng cấp cũ giữ vai trò **giảm tốc độ mất ấm** — hai lớp khác nhau, không trùng chỉ số.

| # | Món | Hình dáng dựng | Màu (hex) | Ấm | Giá / mở khóa | Hiếm |
|---|---|---|---|---|---|---|
| A1 | **Áo len cổ lọ** | Thân `recolor` + cổ cyl cao ôm cổ. **S** | Nâu cà phê `#7a4a2e` | +15 | 60 Xu — `LEN BÀ BẢY` (len1). *Đã bán trong game, nối vào tủ đồ* | Thường |
| A2 | **Áo khoác dạ dài** ⭐ ảnh chốt | Thân kéo dài qua hông (scale hộp thân) + 2 ve áo (box mỏng chéo) + hàng 3 nút cầu nhỏ trước ngực. **M** | Navy ấm `#35507a` | +20 | 120 Xu — len1 | Hiếm |
| A3 | **Áo len kẻ sọc ngang** | Thân + texture canvas 2 sọc ngang vẽ bằng code. **M** | Teal `#2f8f83` × kem bơ `#e8c87e` | +15 | 85 Xu — len1 | Thường |
| A4 | **Áo len thêu hoa dã quỳ** | Thân vàng + 1 bông dã quỳ nhỏ trước ngực (tâm cầu nâu + 6 cánh box vàng cam, hoặc decal canvas). **M** | Vàng mù tạt `#d9a62e`, hoa cam đất `#d97a30` | +16 | **Thành tựu: ăn đủ 10 món khác nhau trong Sổ Đặc Sản** (P0-3) — không bán | Đặc biệt |
| A5 | **Áo gile len** | Lớp gile mặc NGOÀI áo hiện có: hộp thân thứ hai mỏng hơn + viền cổ — vì là lớp ngoài nên +10 (thấp hơn áo len kín, đúng thang ở mục 0). **M** | Xanh thông `#2e6b46` | +10 | 55 Xu — len1, **yêu cầu cấp 3** | Hiếm |
| A6 | **Áo poncho len** | Thân loe (cyl loe dần xuống qua hông) phủ vai — silhouette "trùm" khác hẳn mọi áo khác. **M** | Đỏ đô `#a62b25` | +18 | **Mở khóa: sở hữu đủ 10 món trong Tủ đồ** — sau đó mua 110 Xu ở len1 | Đặc biệt |
| A7 | **Áo len kẻ caro** | Thân + texture canvas caro (đồng bộ họa tiết với khăn K2). **M** | Nâu cà phê `#7a4a2e` × kem bơ `#e8c87e` | +15 | 90 Xu — len1, **yêu cầu cấp 4** | Hiếm |
| A8 | **Áo len dâu tây** 🍓 Bộ Dâu Tây | Thân + chấm dâu canvas toàn thân (như M3/K7). **M** | Hồng sen `#c95d7e` | +16 | 100 Xu — len1, **yêu cầu cấp 4** | Hiếm |
| A9 | **Áo khoác dạ cẩm tú cầu** 🌸 Bộ Cẩm Tú Cầu | Khung A2 (dạ dài + ve + nút) + chấm hoa canvas. **M** | Oải hương `#8668c4` | +19 | 130 Xu — len1, **điều kiện: dấu hộ chiếu khu Nông sản & Hoa** | Đặc biệt |
| A10 | **Áo len chợ đêm** 🌙 Bộ Chợ Đêm | Thân + họa tiết lồng đèn canvas nhỏ trước ngực. **M** | Navy ấm `#35507a` | +17 | 120 Xu — len1, **điều kiện: dấu hộ chiếu Chợ đêm Âm Phủ + chỉ bán ban đêm** | Đặc biệt |

### Ô TAY CẦM (10 món)

Gắn vào tay phải của nhân vật bằng group con tạo trong code (xem ghi chú kỹ thuật mục 4). Tay cầm là lớp "khoe" + tương tác: cầm đồ nóng thì ấm tay, cầm lồng đèn thì phát sáng.

| # | Món | Hình dáng dựng | Màu (hex) | Ấm | Giá / mở khóa | Hiếm |
|---|---|---|---|---|---|---|
| T1 | **Ly sữa đậu nành giữ nhiệt** | Cyl nhỏ + nắp cyl dẹt + ống hút box mỏng — ly inox cầm mãi, không tiêu hao (khác ly sữa uống liền trong giỏ). **S** | Kem bơ `#e8c87e` | +3 | 20 Xu — sạp sữa đường vào (`suatuoi`) | Thường |
| T2 | **Lồng đèn sao cầm tay** ⭐ | Khung sao 5 cánh (2 hình sao lồng nhau bằng box mỏng) + lõi cầu emissive phát sáng cam `#ff9a3d` ban đêm + cán ngắn. **M** | Đỏ nhấn `#c8372d` (chi tiết nhỏ, đúng quy tắc ≤5%) | +2 | 50 Xu — `QUÀ LƯU NIỆM` (luuniem), **chỉ bán ban đêm + yêu cầu cấp 3** | Đặc biệt |
| T3 | **Túi tote cẩm tú cầu** | Box dẹt xách tay + 2 quai (torus cắt nửa) + mặt trước in hoa canvas. **M** | Kem bơ `#e8c87e`, hoa oải hương `#8668c4` | +1 | 45 Xu — luuniem | Thường |
| T4 | **Bắp nướng cầm tay** | Cyl vàng xếp hạt (chấm canvas) + đoạn lõi thò dưới tay cầm — bản "cầm khoe" của món sạp nướng, khác bắp ăn liền trong giỏ tiêu thụ. **S** | Vàng mù tạt `#d9a62e` | +3 | 15 Xu — sạp `KHOAI/BẮP NƯỚNG` | Thường |
| T5 | **Khoai lang nướng cầm tay** | Cầu dẹt vỏ nâu + mặt cắt tím (khoai tím Đà Lạt — sạp chỉ nướng mẻ nhỏ cho khách quen). **S** | Vỏ nâu đất `#96683f`, ruột oải hương `#8668c4` | +3 | 15 Xu — sạp `KHOAI/BẮP NƯỚNG`, **yêu cầu cấp 3** | Hiếm |
| T6 | **Bánh tráng nướng cầm tay** | Cyl dẹt mỏng cầm kiểu quạt tay + chấm topping canvas — đúng kiểu ăn vặt cầm đi trong chợ đêm. **S** | Kem bơ `#e8c87e`, topping cam đất `#d97a30` | +2 | 18 Xu — sạp `BÁNH TRÁNG NƯỚNG` | Thường |
| T7 | **Xiên nướng cầm tay** | Que box mỏng + 3 cầu nướng xếp chồng + vệt khói nhẹ ban đêm. **M** | Nâu cà phê `#7a4a2e`, đỏ đô `#a62b25` | +2 | 22 Xu — sạp `KHOAI/BẮP NƯỚNG` (cụm nướng chợ đêm), **yêu cầu cấp 3** | Hiếm |
| T8 | **Ô hoa cẩm tú cầu** 🌸 Bộ Cẩm Tú Cầu | Ô: cone dẹt 8 múi + cán cyl + chấm hoa canvas — cầm mở che sương/mưa phùn. **M** | Oải hương `#8668c4` | +1 | 60 Xu — luuniem, **yêu cầu cấp 4** | Hiếm |
| T9 | **Dù hoa dã quỳ** 🌼 Bộ Dã Quỳ | Ô như T8 + 1 bông dã quỳ canvas lớn ở tâm ô. **M** | Vàng mù tạt `#d9a62e` | +1 | **Thành tựu: ăn đủ 15 món khác nhau trong Sổ Đặc Sản** — không bán | Đặc biệt |
| T10 | **Lồng đèn giấy tròn chợ đêm** 🌙 Bộ Chợ Đêm | Cầu giấy phát sáng cam `#ff9a3d` mạnh hơn T2 (đèn "trưởng đoàn") + quai cầm ngắn. **M** | Viền đỏ nhấn `#c8372d` (chi tiết nhỏ ≤5%) + lõi cam phát sáng | +2 | **Thành tựu: check-in chụp ảnh đủ 6 điểm** — không bán | Đặc biệt |

### Ô PHỤ KIỆN (12 món)

| # | Món | Hình dáng dựng | Màu (hex) | Ấm | Giá / mở khóa | Hiếm |
|---|---|---|---|---|---|---|
| P1 | **Găng tay len** | 2 box bo tròn phủ lên 2 bàn tay (group con theo tay). **S** | Xanh rêu `#6b8f3e` | +7 | 25 Xu — `MŨ & GĂNG LEN` (len2). *Đã bán trong game, nối vào tủ đồ* | Thường |
| P2 | **Ba lô vải bố** ⭐ ảnh chốt | Box bo sau lưng + nắp hộp mỏng + 2 quai (box cong giả bằng 2 đoạn) + túi trước nhỏ. Gắn sau thân, không qua ô tay. **M** | Nâu đất `#96683f` | +4 | 75 Xu — `QUÀ LƯU NIỆM` (luuniem) | Hiếm |
| P3 | **Kính mát cao nguyên** | 2 vòng torus nhỏ + gọng box mỏng trước mặt — món phong cách ban ngày, ấm 0 là cố ý (để người chơi đổi style sáng/đêm). **S** | Nâu cà phê `#7a4a2e` (gọng) | 0 | 35 Xu — `KI-ỐT ĐỒNG HỒ` (dongho). *Ki-ốt đã bán kính mát, nối vào tủ đồ* | Thường |
| P4 | **Móc khóa nhà ga Đà Lạt** | Hộp mini hình nhà ga (box + mái tam giác) treo ở hông bằng đoạn dây ngắn, đung đưa khi đi. **S** | Cam đất `#d97a30` | 0 | 15 Xu — luuniem. *Đã bán trong game* — món sưu tầm rẻ nhất, mua đầu tiên | Thường |
| P5 | **Tất len cao cổ** | 2 vòng cyl quanh cổ chân trên giày — chi tiết nhỏ làm "bộ đồ len" liền mạch. **S** | Xanh rêu `#6b8f3e` | +3 | 18 Xu — len2, **yêu cầu cấp 3** | Hiếm |
| P6 | **Cài áo hoa dã quỳ** 🌼 Bộ Dã Quỳ | Bông dã quỳ nhỏ (như chi tiết A4) gắn ngực trái. **S** | Vàng mù tạt `#d9a62e`, tâm nâu cà phê `#7a4a2e` | 0 | 20 Xu — luuniem | Thường |
| P7 | **Cài áo cẩm tú cầu** 🌸 Bộ Cẩm Tú Cầu | Cụm 3 cầu hoa nhỏ gắn ngực. **S** | Oải hương `#8668c4` + dương `#3a6bc2` | 0 | 20 Xu — luuniem | Thường |
| P8 | **Vòng tay len bện** | Torus nhỏ ở cổ tay phải, bện 2 màu — món rẻ nhất tủ đồ. **S** | Đỏ đô `#a62b25` × kem bơ `#e8c87e` | +1 | 12 Xu — len2 | Thường |
| P9 | **Túi đeo chéo mini hồ Xuân Hương** | Box nhỏ đeo chéo (dây box mỏng qua thân) + mặt túi thêu sóng hồ canvas — ba lô mini bản đeo chéo. **M** | Teal `#2f8f83` | +2 | 55 Xu — luuniem, **yêu cầu cấp 3** | Hiếm |
| P10 | **Móc khóa tháp chuông** 🚂 Bộ Nhà Ga | Hộp mini tháp chuông (box cao + chóp tam giác) treo hông như P4 — cặp địa danh với móc khóa nhà ga. **S** | Cam đất `#d97a30` | 0 | 15 Xu — luuniem | Thường |
| P11 | **Móc khóa chợ Đà Lạt** 🚂 Bộ Nhà Ga | Hộp mini mặt tiền chợ (box + mái + khối chữ nhỏ) treo hông — hoàn tất bộ móc khóa địa danh. **M** | Đỏ đô `#a62b25` | 0 | 25 Xu — luuniem, **yêu cầu cấp 4** | Hiếm |
| P12 | **Huy hiệu Khách quen chợ** | Đĩa tròn vàng gắn ngực, viền phát sáng nhẹ — huy hiệu "dân chợ chính hiệu". **S** | Vàng mù tạt `#d9a62e` | 0 | **Thưởng đạt cấp 6 "Khách quen chợ"** — không bán | Đặc biệt |

### Ô GIÀY (8 món) — ô MỚI thêm ở bản 60

Giày dựng bằng **recolor phần chân + thêm đế/ống primitive** trên character hiện có (không cần node mới trong GLB); ô Giày trang bị 1 đôi mỗi lúc, cộng ấm như một lớp phụ kiện chân.

| # | Món | Hình dáng dựng | Màu (hex) | Ấm | Giá / mở khóa | Hiếm |
|---|---|---|---|---|---|---|
| G1 | **Giày vải đi chợ** | Đế box mỏng + thân giày recolor phủ bàn chân. **S** | Kem bơ `#e8c87e` | +2 | 25 Xu — len2 | Thường |
| G2 | **Ủng len cao cổ** | Cyl ống ôm chân lên gần gối + đế dày — đôi ủng "đi chợ khuya" ấm nhất ô giày. **M** | Xanh rêu `#6b8f3e` | +6 | 60 Xu — len2, **yêu cầu cấp 3** | Hiếm |
| G3 | **Giày len thêu dâu** 🍓 Bộ Dâu Tây | Giày + chấm dâu canvas như M3. **M** | Hồng sen `#c95d7e` | +4 | 65 Xu — len2, **yêu cầu cấp 4** | Hiếm |
| G4 | **Ủng dạ đi đêm** 🌙 Bộ Chợ Đêm | Ủng như G2 + viền đế phát sáng nhẹ (đi đêm nổi bật). **M** | Navy ấm `#35507a` | +6 | 70 Xu — len2, **điều kiện: dấu hộ chiếu Chợ đêm Âm Phủ** | Đặc biệt |
| G5 | **Giày thêu cẩm tú cầu** 🌸 Bộ Cẩm Tú Cầu | Giày + hoa canvas hai bên. **M** | Oải hương `#8668c4` | +4 | 60 Xu — len2, **điều kiện: dấu hộ chiếu khu Nông sản & Hoa** | Đặc biệt |
| G6 | **Giày dã quỳ** 🌼 Bộ Dã Quỳ | Giày vàng + 1 bông dã quỳ nhỏ ở mũi giày. **M** | Vàng mù tạt `#d9a62e` | +4 | **Mở khóa: đóng đủ 9/9 dấu Hộ chiếu Đi Chợ** — sau đó mua 50 Xu ở len2 | Đặc biệt |
| G7 | **Dép tổ ong đi chợ** | Đế dẹt + 2 quai box — món "huyền thoại" đi chợ Việt Nam; ấm thấp là cố ý (phong cách hơn chỉ số). **S** | Cam đất `#d97a30` | +1 | 30 Xu — len2, **yêu cầu cấp 3** | Hiếm |
| G8 | **Giày len Khách quen vàng** | Giày + viền vàng phát sáng nhẹ — đôi giày "tốt nghiệp" của dân chợ. **M** | Vàng mù tạt `#d9a62e` | +5 | **Thưởng đạt cấp 6 "Khách quen chợ"** — không bán | Đặc biệt |

**Tổng: 60 món** (Mũ 12 · Khăn 8 · Áo 10 · Tay cầm 10 · Phụ kiện 12 · Giày 8) — giữ nguyên 21 món bản đầu, trong đó **6 món đã có sẵn hàng trong sạp** (K1, A1, M1(biến thể), P1, P3, P4) chỉ cần nối cơ chế mặc; 39 món mở rộng đều dựng bằng node/primitive sẵn có, **0 byte GLB mới**. Phân tầng: **24 món mua ngay bằng Xu (40%) · 21 món cần cấp 3–4 (35%) · 15 món Đặc biệt (25%)** — lộ trình chi tiết ở mục 3, bộ sưu tập ở mục 2.

---

## 2. BỘ SƯU TẬP THEO CHỦ ĐỀ (SET) — 5 bộ / 24 món

Mặc **đủ các món của 1 bộ cùng lúc** (món thuộc bộ đang equipped ở ô của nó; phụ kiện tính khi đang đeo) sẽ nhận **+3 Độ Ấm bộ** (riêng Bộ Dã Quỳ +4) và **1 đặc quyền** của bộ. UI Tủ đồ hiện tiến độ từng bộ (vd "Dâu Tây 3/4"). Các món trong bộ vẫn có dòng riêng ở mục 1 — bảng dưới chỉ là lớp gom bộ.

| Bộ | Món thành viên | Đặc quyền khi đủ bộ (ngoài +ấm bộ) |
|---|---|---|
| 🍓 **Bộ Dâu Tây** (4 món) | M3 mũ dâu · K7 khăn dâu · A8 áo dâu · G3 giày dâu | Giảm 10% tại sạp kem bơ & dâu / trái cây; NPC thỉnh thoảng khen "bộ dâu tây" trong bong bóng thoại |
| 🌸 **Bộ Cẩm Tú Cầu** (6 món) | M9 mũ · K4 khăn · A9 áo dạ · T8 ô hoa · P7 cài áo · G5 giày | Giảm 10% tại `QUÀ LƯU NIỆM` và sạp hoa; cánh hoa rơi nhẹ quanh người khi đứng yên |
| 🌼 **Bộ Dã Quỳ** (5 món) | M12 mũ · A4 áo thêu · T9 dù hoa · P6 cài áo · G6 giày | **+4 ấm bộ** (bộ ấm nhất); giảm 10% tại 2 sạp đồ len |
| 🚂 **Bộ Nhà Ga** (4 món) | M11 mũ thêu nhà ga · P4 móc khóa nhà ga · P10 móc khóa tháp chuông · P11 móc khóa chợ | Giảm 10% tại `QUÀ LƯU NIỆM`; danh hiệu phụ "Khách du lịch Đà Lạt" hiện cạnh thẻ tên |
| 🌙 **Bộ Chợ Đêm** (5 món) | T2 lồng đèn sao · K8 khăn đêm · A10 áo đêm · T10 đèn giấy tròn · G4 ủng dạ đêm | Vùng sáng quanh người rộng hơn (halo ấm); giảm 10% tại các sạp chợ đêm |

**Cân bằng set:** mọi bộ đều có ít nhất 1 món rẻ/mua ngay (cài áo 20 Xu, móc khóa 15 Xu, mũ dâu 55 Xu...) để người chơi "ngửi thấy" bộ từ sớm; món chốt bộ luôn là món Đặc biệt hoặc cấp cao (dấu hộ chiếu / Sổ Đặc Sản / cấp 4) — đủ bộ là thành tựu để khoe, không phải điều kiện bắt buộc để chơi tiếp. Hai bộ gắn với 2 dấu hộ chiếu khác nhau (hoa / chợ đêm) khiến hộ chiếu và tủ đồ kéo nhau đi lên.

---

## 3. BỘ KHỞI ĐẦU + LỘ TRÌNH MỞ KHÓA

**Người chơi mới có sẵn (0 Xu):**
- Đang mặc: **M1 Mũ len beanie đỏ đô** (đúng tạo hình nhân vật hiện tại) + áo cơ bản đỏ đô (chỉ là màu thân, +0 ấm, thay được khi mua áo tủ đồ) — tổng ấm khởi đầu **+8**, đủ đi chợ đầu đêm, chưa đủ đi khuya lâu.
- Tủ đồ rỗng ngoài M1; Xu khởi đầu 300 (số hiện tại của game) đủ mua ngay 1 khăn + 1 găng trong lần ghé nhà lồng đầu tiên.

**Mua được ngay (đợt đầu, tổng ~200 Xu):** K1 khăn trơn 35 · P1 găng 25 · M2 mũ chóp bông 45 · T1 ly giữ nhiệt 20 · P4 móc khóa 15 · M6 nón lá 35 → mặc vào là ấm +30 trở lên và **nhìn khác hẳn NPC** (đúng thiếu hụt "người chơi nghèo nhất chợ" ở research/13).

**Mục tiêu trung hạn (cấp 3–4 + để dành Xu):** M5 beret (cấp 3) · T2 lồng đèn sao (cấp 3, mua ban đêm) · K3 khăn tua rua (cấp 4) · A2 áo dạ dài 120 Xu · P2 ba lô 75 Xu · K2 khăn caro 60 Xu · lớp mở rộng cấp 3: M7 · M10 · K5 · K6 · A5 · T5 · T7 · P5 · P9 · G2 · G7 · cấp 4: M11 · K7 · A7 · A8 · T8 · P11 · G3.

**Đích cấp 6:** **P12 Huy hiệu** + **G8 Giày Khách quen vàng** là **thưởng đạt cấp 6** (không bán) — đích dài hạn nhìn thấy được ngay trên người các "cựu khách quen".

**Mục tiêu dài hạn (đặc biệt, không mua bằng Xu thuần) — 15 món:**
- **Theo dấu hộ chiếu (8):** K4 · M9 · A9 · G5 (dấu Nông sản & Hoa) · K8 · A10 · G4 (dấu Chợ đêm Âm Phủ) · G6 (đủ 9/9 dấu) — biến hộ chiếu thành chìa khóa tủ đồ.
- **Theo Sổ Đặc Sản (3):** M12 (ăn 5 món) · A4 (ăn 10 món) · T9 (ăn 15 món) — biến "ăn sưu tầm" thành phần thưởng mặc được.
- **Theo thành tựu / hệ thống (4):** T10 (check-in đủ 6 điểm ảnh) · A6 (sở hữu đủ 10 món tủ đồ) · P12 · G8 (đạt cấp 6).
- Đây là lớp "đồ khoe" để người chơi lâu trông khác biệt — đúng cơ chế game thật (trang phục = tín hiệu cấp/thành tựu).

**Phân tầng 60 món (đã cân lại theo lệnh mở rộng):**

| Tầng | Số món | Tỉ lệ | Gồm |
|---|---|---|---|
| Mua ngay bằng Xu | 24 | 40% | Món Thường + vài món Hiếm giá Xu thuần, rải đủ 6 ô |
| Cần cấp 3–4 | 21 | 35% | Cấp 3: 13 món · Cấp 4: 8 món (tính cả M5/K3/T2 bản đầu) |
| Đặc biệt | 15 | 25% | Dấu hộ chiếu 8 · Sổ Đặc Sản 3 · thành tựu/hệ thống 4 (gồm 2 thưởng cấp 6 không bán) |

**Tổng ấm khi mặc full (bản 60):** set mua ngay cơ bản — M1 +8 · K1 +10 · A1 +15 · T1 +3 · P1 +7 · G1 +2 ≈ **+45**; set đẹp nhất — M2 +9 · K3 +12 · A2 +20 · T1 +3 · P1 +7 · P5 +3 · P2 +4 · G2/G4 +6 ≈ **+64**, +3 khi đủ 1 bộ sưu tập (Dã Quỳ +4) → trần ≈ **+67/100**, vẫn chừa khoảng lạnh để đồ ăn nóng/bếp lửa còn ý nghĩa.

**Nguyên tắc cân bằng:** không món nào bán ở 2 sạp; giá hiếm ≈ 2–4 giờ chơi tích Xu bình thường; mọi món đặc biệt đều nhìn thấy được từ xa (màu/chi tiết nổi) để đáng công săn.

---

## 4. GHI CHÚ KỸ THUẬT CHO LƯỢT DỰNG

1. **State (theo research/14):** `state.wardrobe = [itemId...]` (đã sở hữu), `state.equipped = { hat:null|'M2', scarf:..., coat:..., hand:..., shoes:..., extra:[...] }` — Phụ kiện cho phép **nhiều món cùng lúc** (găng + ba lô + kính + móc khóa không tranh ô nhau); 5 ô chính (Mũ/Khăn/Áo/Tay cầm/Giày) mỗi ô 1 món. Migration: save cũ không có 2 trường này → mặc định `wardrobe:['M1']`, `equipped.hat='M1'`. **Không phá save `chohb3d-v1`.**
2. **Định danh món:** mỗi món 1 `id` cố định (M1…G8 như bảng trên) + trường `slot`, `warm`, `price`, `stallId`, `unlock` (`null | {level:3} | {stamp:'produce'} | {stamp:'night'} | {achievement:'tasted10'} | {night:true}`), thêm trường `set` cho 24 món thuộc bộ sưu tập — khai báo 1 bảng `WARDROBE_DEFS` cạnh `STALL_DEFS` để UI tủ đồ + logic mua dùng chung.
3. **Đường mua → mặc:** mua tại sạp các món có `slot` thì **không vào Giỏ tiêu thụ** mà vào `state.wardrobe` + toast "Đã thêm vào Tủ đồ"; nút **Tủ đồ** cạnh nút Túi đồ (theo research/14): lưới món đã có, món đang mặc viền vàng, bấm Mặc/Gỡ, preview trực tiếp trên nhân vật trong game.
4. **Hiển thị mặc:** dùng lại cơ chế NPC đang chạy — `makePerson` đã có chọn mũ (`HatBeanie/HatCap/HatNonLa` bật/tắt visible) + `Scarf` visible + `recolor()`. Người chơi mặc = set visible node tương ứng + recolor theo hex của món; chi tiết thêm (chóp bông, lá dâu, ve áo, nút, tua rua, hoa thêu) là **group primitive con** (cyl/cầu/box/torus + canvas texture) gắn vào node sẵn có, bật/tắt theo món đang mặc. Ba lô/găng/kính/móc khóa/lồng đèn/ly/tote = group con gắn thân/tay phải/đầu — **toàn bộ bằng code Three.js trong index.html, 0 byte GLB mới** → không đụng trần 9,97MB (chỉ còn dư ~35KB; canvas texture kẻ caro/sọc/hoa vẽ bằng code cũng không tốn file).
5. **Độ Ấm:** tổng ấm = Σ `warm` của món đang mặc, cộng thẳng vào thanh Độ Ấm hiện có; gỡ đồ giữa đêm lạnh là ấm tụt ngay (quyết định chơi thật). Áo tủ đồ (ô Áo) cộng ấm trực tiếp, **không** thay chỉ số nâng cấp "Áo ấm" cũ (lớp giảm tốc độ mất ấm) — tránh trùng, đã ghi ở mục Ô Áo.
6. **Kiểm chứng lượt dựng (chuẩn đã chốt):** node --check đạt; mở save cũ không lỗi; render cận cảnh nhân vật mặc từng ô (mũ chóp bông, khăn tua rua, áo dạ, lồng đèn phát sáng ban đêm); ảnh UI tủ đồ. Liệt kê thẳng món nào chưa dựng xong trong báo cáo — không gộp "đã làm hết" nếu còn thiếu.

**Thứ tự dựng đề xuất trong lượt sau:** (a) khung tủ đồ + state + nối 6 món đã có hàng trong sạp (toàn S) → mặc được ngay; (b) 9 món primitive đơn (M2, M5, A1-cổ, A3, P1–P4, T1); (c) 6 món M có chi tiết/canvas (M3, M4, K2, K3, K4, A2, A4, T2, T3) — chia 2 đợt render kiểm chứng.

**Mở rộng 60 món — ghi chú thêm:** 39 món mới khai báo cùng bảng `WARDROBE_DEFS` (thêm `slot:'shoes'`); ô Giày dựng bằng recolor chân + đế/ống primitive nên không cần node GLB mới. Hiệu ứng đủ bộ tính ở 1 hàm `checkSetBonus()` chạy mỗi lần thay đồ (đếm món thuộc set đang equipped → cộng ấm bộ + bật đặc quyền). Thứ tự dựng sau bản 21: (d) các món **S** của bản mở rộng — M7 · M8 · K5 · T4 · T6 · P5 · P6 · P7 · P8 · P10 · P12 · G1 · G7; (e) các món **M** còn lại theo ô; (f) cơ chế set + đặc quyền bộ + tiến độ bộ trong UI tủ đồ. Mọi món mở rộng vẫn **0 GLB mới**, không đụng trần dung lượng.
