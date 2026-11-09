# 24 — RÀ SOÁT HÀNG HÓA THẬT vs HÀNG HÓA TRONG GAME

**Game:** Chợ Hòa Bình 3D — Đà Lạt (`prototype-v2/index.html`)
**Ngày rà soát:** 09/11/2026
**Phạm vi:** Đối chiếu danh mục hàng hóa THẬT của Chợ Đà Lạt (chợ ngày trong nhà lồng + chợ đêm Âm Phủ ngoài trời) với hàng hóa hiện có trong game; chỉ ra quầy thiếu, quầy đã bổ sung trong vòng **BLENDER-DEEP-2**, và những loại hàng thật đến cuối vòng này vẫn chưa có.
**Cách làm (đo, không đoán):** phía "thật" lấy từ 4 bài nguồn ở Mục 1; phía "game" đọc trực tiếp `const STALL_DEFS` trong `prototype-v2/index.html` (đếm và trích menu từng sạp bằng script, không nhớ tay) + đọc khối lưới quầy decor trong nhà lồng ngay sau `STALL_DEFS`. Mục "đã bổ sung BLENDER-DEEP-2" ghi theo hồ sơ vòng đó được giao kèm nhiệm vụ rà soát này — xem lưu ý kiểm chứng ở Mục 5.

---

## 1. Nguồn thật đã dùng

| # | Nguồn | URL (nguyên văn) | Dùng để lấy |
|---|-------|------------------|-------------|
| 1 | Nam Thiên Travel — Kinh nghiệm đi chợ đêm Đà Lạt | https://namthientravel.com.vn/kinh-nghiem-di-cho-dem-da-lat/ | Nhóm hàng tổng quát: đồ len thủ công, rau củ quả, hoa quả đặc sản, các loại mứt, trà atiso, cà phê, rượu vang, hoa quả sấy, nước cốt trái cây |
| 2 | Nam Thiên Travel — Chợ đêm Đà Lạt có gì ngon | https://namthientravel.com.vn/cho-dem-da-lat-co-gi-ngon/ | Giá + mặt hàng chợ đêm: đồ len/áo khoác, **quần áo secondhand**, mứt, trà atiso/cà phê, trái cây tươi, hoa tươi và cây cảnh (sen đá, xương rồng) |
| 3 | Travel.com.vn (Vietravel) — Chợ đêm Đà Lạt có gì? Ăn gì? Chơi gì? | https://travel.com.vn/tin-tuc-du-lich/cho-dem-da-lat-v18326.aspx | Đặc sản làm quà kèm giá: hồng treo gió, dâu tây, trái cây sấy dẻo (hồng/kiwi/dâu/phúc bồn tử), mứt, trà atiso, cà phê Arabica; quần áo + lưu niệm (áo len, khăn, mũ/găng, áo khoác, túi vải/postcard/sổ tay, móc khóa/nam châm, đồ handmade len/gỗ/da); món ăn tối quanh chợ (lẩu, ốc, miến, cháo) |
| 4 | Blog Vexere — Chợ Đà Lạt: địa chỉ, đường đi và kinh nghiệm mua sắm | https://blog.vexere.com/cho-da-lat-dia-chi-duong-di-va-kinh-nghiem-mua-sam-vexere/ | Hàng chợ NGÀY: rau củ (súp lơ, hành tây, atiso, khoai tây, khoai lang), trái cây (hồng giòn, bơ, dâu), mứt + rượu vang, quần áo len; cấu trúc 3 tầng chợ (trệt: đồ khô/trái cây/hoa/bách hóa — lửng: ăn uống — trên: thủ công mỹ nghệ/điện máy/quần áo/mỹ phẩm/túi xách); ăn vặt đêm: bánh tráng nướng, sữa đậu nành, khoai nướng, bánh căn, bánh mì xíu mại, dâu lắc, chè, nem nướng; trong chợ có bánh canh cá lóc, bánh xèo |

Ghi chú độ tin cậy: cả 4 nguồn đều là bài cẩm nang du lịch (không phải niên giám chợ), nhưng 3 nhà khác nhau (Nam Thiên, Vietravel, Vexere) trùng nhau ở gần như toàn bộ nhóm hàng cốt lõi — đủ cơ sở để dùng làm danh mục đối chiếu. Giá trong bài chỉ để tham khảo bối cảnh, game dùng đơn vị Xu Chợ riêng nên không đối chiếu giá.

---

## 2. Danh mục hàng hóa THẬT (tổng hợp từ 4 nguồn)

### 2.1 Đặc sản mang về làm quà
- **Dâu tây tươi** (80.000–250.000đ/kg tùy mùa/nguồn)
- **Mứt các loại:** dâu tây/dâu tằm, hồng, khoai lang, mận, me, gừng, hoa hồng, cà chua
- **Trái cây sấy / sấy dẻo:** hồng sấy dẻo, kiwi, dâu tây, phúc bồn tử; thêm mít sấy, khoai lang sấy, mãng cầu sấy, cà rốt sấy
- **Hồng treo gió** (180.000–350.000đ/kg), **hồng giòn** tươi
- **Bơ sáp / bơ 034** (40.000–60.000đ/kg), chuối la ba
- **Trà atiso** (50.000–250.000đ), trà ô long/lài/khổ qua/bồ công anh
- **Cà phê** Cầu Đất / Arabica / Moka (120.000–400.000đ/kg)
- **Rượu vang Đà Lạt** (nho, mận, dâu tằm), **nước cốt trái cây** đóng chai (dâu tây, chanh dây, phúc bồn tử)

### 2.2 Hoa và rau củ cao nguyên (chợ ngày)
- **Hoa tươi:** cẩm tú cầu, hồng, baby, cúc, cẩm chướng, lay ơn; hoa khô; sen đá/xương rồng mini
- **Rau củ:** atiso, su su, cà rốt, súp lơ, khoai tây, khoai lang, hành tây, xà lách, cà chua bi, ớt chuông, bắp cải

### 2.3 Thời trang và lưu niệm
- **Đồ len thủ công:** áo len, khăn choàng, mũ len, găng tay, tất len, **búp bê len**
- **Quần áo:** áo khoác (dạ, gió, giữ nhiệt), quần áo thường/trend
- **Đồ si / secondhand** (10.000–100.000đ — "săn" áo khoác, váy vintage)
- **Lưu niệm:** móc khóa, nam châm tủ lạnh, bưu thiếp/postcard, sổ tay, túi vải, **tranh gỗ / tranh bút lửa / tranh khắc gỗ**, **chuông gió**, gấu bông, đồ handmade len/gỗ/da, lụa Đà Lạt
- Hàng trong nhà lồng theo tầng (Vexere): đồ khô, bánh kẹo, giò chả, gia vị, bách hóa, thịt & cá tươi, vải, điện máy, mỹ phẩm, túi xách, giày dép, gốm sứ

### 2.4 Đồ ăn / đồ uống tại chợ đêm
Bánh tráng nướng ("pizza Đà Lạt"), bánh tráng trộn, sữa đậu nành nóng, bánh căn, súp cua, chè (nhiều loại), xiên nướng/thịt xiên, hải sản nướng, bánh mì xíu mại, bánh ướt lòng gà, khoai lang/bắp nướng, dâu lắc/trái cây lắc, kem bơ, sinh tố bơ, yaourt phô mai, đậu hũ nóng, cháo đêm, hủ tiếu/mì đêm, nem nướng, bánh xèo, bánh canh cá lóc, bánh flan; quanh chợ còn có lẩu gà lá é, lẩu bò, ốc bươu nhồi thịt, miến gà/ngan (quán quanh khu Hòa Bình, không phải sạp trong chợ).

---

## 3. Hiện trạng game TRƯỚC vòng BLENDER-DEEP-2 (đo từ code)

### 3.1 Sạp tương tác — `STALL_DEFS`

> ⚠️ **Số đếm thật: 33 sạp, không phải 31.** Brief rà soát ghi "31 sạp tương tác" nhưng đếm trực tiếp mảng `STALL_DEFS` trong `prototype-v2/index.html` (từ `const STALL_DEFS = [` tới `];`) cho **33 phần tử**. Hai sạp dễ bị sót khi đếm tay là `aokhoac` và `aolen` (nằm cuối mảng, khu phải bậc tam cấp). Mọi đối chiếu dưới đây dùng con số đo được: **33**.

| # | id | Tên sạp | Menu (món mua/ăn được) |
|---|----|---------|------------------------|
| 1 | `banhtrang` | BÁNH TRÁNG NƯỚNG | Bánh tráng nướng trứng; Bánh tráng nướng phô mai |
| 2 | `khoai` | KHOAI & BẮP NƯỚNG | Khoai lang mật nướng; Bắp nướng mỡ hành |
| 3 | `banhcan` | BÁNH CĂN | Bánh căn trứng cút; Bánh căn hải sản |
| 4 | `supcua` | SÚP CUA & CHÈ NÓNG | Súp cua nóng; Chè nóng đậu xanh |
| 5 | `sua` | SỮA ĐẬU NÀNH | Sữa đậu nành nóng; Sữa đậu xanh lá dứa; Bánh su kem |
| 6 | `caphe` | CÀ PHÊ PHIN | Cà phê phin đen; Cacao nóng; Cà phê sữa nóng |
| 7 | `yaourt` | YAOURT & SINH TỐ | Yaourt phô mai; Sinh tố bơ |
| 8 | `len1` | LEN BÀ BẢY | Áo len cổ lọ; Khăn choàng len |
| 9 | `len2` | MŨ & GĂNG LEN | Mũ len beanie; Găng tay len |
| 10 | `rau` | RAU CỦ ĐÀ LẠT | Atiso tươi (1kg); Su su & cà rốt |
| 11 | `dau` | DÂU TÂY & KEM BƠ | Kem bơ Đà Lạt; Dâu tây tươi (hộp); Dâu lắc muối tôm; Bơ 034 (1kg) |
| 12 | `khoainuong` | KHOAI & BẮP NƯỚNG | Khoai lang nướng mật; Bắp nướng mỡ hành |
| 13 | `suadau` | SỮA ĐẬU NÀNH NÓNG | Sữa đậu nành nóng; Đậu hũ nước đường gừng |
| 14 | `hoa` | HOA TƯƠI ĐÀ LẠT | Bó cẩm tú cầu; Bó hoa baby |
| 15 | `dacsan` | ĐẶC SẢN MỨT & HỒNG | Hộp mứt dâu; Hồng treo gió; Trà atiso túi lọc |
| 16 | `tra` | TRÀ & CÀ PHÊ HẠT | Cà phê hạt Cầu Đất; Trà ô long (hộp) |
| 17 | `dongho` | KI-ỐT ĐỒNG HỒ | Kính mát; Đồng hồ đeo tay |
| 18 | `luuniem` | QUÀ LƯU NIỆM | Móc khóa Đà Lạt; Bưu thiếp Đà Lạt |
| 19 | `xien` | XIÊN NƯỚNG ĐÊM | Xiên thịt nướng; Chân gà nướng |
| 20 | `che` | CHÈ NÓNG ĐÊM | Chè trôi nước |
| 21 | `tron` | BÁNH TRÁNG TRỘN | Bánh tráng trộn |
| 22 | `dauhu` | ĐẬU HŨ NÓNG | Đậu hũ nước gừng |
| 23 | `banhuot` | BÁNH ƯỚT LÒNG GÀ | Bánh ướt lòng gà; Xíu mại chén |
| 24 | `suatuoi` | SỮA TƯƠI & ĐẬU HŨ | Sữa tươi nóng; Đậu hũ nước gừng |
| 25 | `banhmi` | BÁNH MÌ XÍU MẠI | Bánh mì xíu mại; Bánh mì chảo |
| 26 | `hutieu` | HỦ TIẾU & MÌ ĐÊM | Hủ tiếu xương; Mì khô xá xíu |
| 27 | `traicay` | TRÁI CÂY LẮC & NƯỚC ÉP | Trái cây lắc muối tôm; Nước ép dâu tằm |
| 28 | `chao` | CHÁO & SÚP ĐÊM | Cháo gà nóng; Súp cua |
| 29 | `hoasua` | SỮA ĐẬU NÀNH HOA SỮA | Sữa đậu nành nóng; Sữa nành bò; Bánh tiêu; Bánh sừng trâu |
| 30 | `haisan` | HẢI SẢN NƯỚNG ĐÊM | Xiên hải sản nướng; Hàu nướng mỡ hành |
| 31 | `banhflan` | BÁNH FLAN CARAMEL | Bánh flan caramel; Flan cà phê |
| 32 | `aokhoac` | ÁO KHOÁC ĐÀ LẠT | Áo khoác dạ dày; Áo khoác gió 2 lớp |
| 33 | `aolen` | ÁO LEN & KHĂN | Áo len cardigan; Khăn len dài |

Nhận xét nhanh: tuyến **ăn uống đêm rất dày** (sữa đậu nành có tới 4 sạp: `sua`, `suadau`, `suatuoi` liên quan, `hoasua`; khoai/bắp nướng 2 sạp; súp cua 2 sạp) — khớp đúng thói quen chợ Âm Phủ thật. Tuyến **đặc sản mang về** trước vòng này chỉ có đúng 2 sạp (`dacsan`, `tra`) + gánh lẻ trong `dau`/`rau`/`hoa` — mỏng hẳn so với chợ thật, và đây chính là chỗ thiếu lớn nhất (chi tiết Mục 4).

### 3.2 Quầy decor trong nhà lồng (không tương tác)

Khối lưới quầy ngay sau `STALL_DEFS` dựng quầy trang trí theo lưới **48 vị trí** (4 hàng × 12 cột: z 14,55 / 26,7 / 19,35 / 20,65), biển "QUẦY SỐ n" luân phiên 8 nhóm biển phụ: `RAU CỦ`, `TRÁI CÂY`, `ĐỒ KHÔ`, `MỨT & KẸO`, `GIA VỊ`, `HOA TƯƠI`, `THỊT & CÁ`, `BÁNH KẸO`. Sau khi trừ vị trí chừa miệng thang trong nhà và vị trí trùng sạp tương tác, **số quầy decor thực dựng là 33** (mô phỏng lại đúng điều kiện lọc trong code). Nghĩa là các nhóm hàng chợ ngày (thịt cá, gia vị, đồ khô…) mới chỉ có **ở mức biển hiệu + khối hàng màu**, không sạp nào mua được.

Ngoài ra còn 32 sạp decor dọc đường vào kéo dài (16 bắc + 16 nam, biển luân phiên: trà nóng, bánh tráng, sữa nóng, xôi đêm, bắp nướng, chè nóng, đậu hũ, bánh mì, trái cây, khoai nướng, xiên que, nước ép) — cũng chỉ decor, không tương tác.

---

## 4. BẢNG ĐỐI CHIẾU CHÍNH — hàng thật → game

Ký hiệu: ✅ Có, mua/ăn được ở sạp tương tác · 🟡 Có một phần (gộp chung / chỉ decor / thiếu món lẻ) · ❌ Chưa có (trước BLENDER-DEEP-2). Cột cuối ghi thay đổi sau vòng BLENDER-DEEP-2 (chi tiết Mục 5).

### 4.1 Đặc sản mang về làm quà

| Loại hàng thật | Trước BLENDER-DEEP-2 | Sạp / món trong game | Thiếu gì (trước vòng) | Sau BLENDER-DEEP-2 |
|---|---|---|---|---|
| Dâu tây tươi | 🟡 Có nhưng chỉ 1 sạp | `dau` — "Dâu tây tươi (hộp)" | Chợ thật dâu tây dày đặc nhiều sạp; game chỉ 1 điểm bán lẻ | ✅ Đỡ hẳn: thêm `dau2`, `dau3`, `dau4` → **tổng 4 quầy dâu** |
| Mứt dâu (tây/tằm) | ✅ Có | `dacsan` — "Hộp mứt dâu" | — | ✅ Thêm mặt hàng ở `dau3`, `mut`, tiệm lớn |
| Mứt hồng | ❌ Chưa có món lẻ | — (chỉ có hồng treo gió ở `dacsan`) | Thiếu hẳn vị mứt bán chạy thứ hai | 🟡 Có quầy `mut` + kệ mứt tiệm lớn; **chưa xác nhận món lẻ "mứt hồng" trong menu** |
| Mứt khoai lang | ❌ Chưa có món lẻ | — | Thiếu | 🟡 Như trên — ở mức tên quầy/kệ, chưa xác nhận món lẻ |
| Mứt mận | ❌ Chưa có món lẻ | — | Thiếu | 🟡 Như trên |
| Mứt me | ❌ Chưa có món lẻ | — | Thiếu | 🟡 Như trên |
| Mứt gừng / hoa hồng / cà chua / dâu tằm tách vị | ❌ Chưa có | — | Nguồn thật liệt kê là dòng mứt phụ phổ biến | ❌ Vẫn chưa xác nhận có |
| Trái cây sấy (nhóm chung) | ❌ **Không có món nào mua được** | Chỉ có biển decor `ĐỒ KHÔ`, `MỨT & KẸO` trong nhà lồng | **Lỗ hổng lớn nhất tuyến đặc sản**: chợ thật đây là nhóm hàng chủ lực | ✅ Có quầy `mut` 'MỨT & TRÁI CÂY SẤY' + kệ trái cây sấy trong tiệm lớn |
| Hồng sấy dẻo | ❌ Chưa có | — (hồng treo gió ≠ hồng sấy dẻo) | Thiếu | 🟡 Thuộc nhóm của quầy `mut`; chưa xác nhận món lẻ |
| Kiwi sấy | ❌ Chưa có | — | Travel.com.vn nêu đích danh | 🟡 Như trên — chưa xác nhận món lẻ |
| Dâu sấy | ❌ Chưa có | — | Thiếu | 🟡 Như trên |
| Phúc bồn tử (sấy / nước cốt) | ❌ Chưa có | — | Travel.com.vn + Nam Thiên đều nêu | ❌ Chưa xác nhận có ở quầy mới |
| Mít sấy / khoai sấy / mãng cầu sấy | ❌ Chưa có | — | Dòng sấy phụ của chợ thật | ❌ Chưa xác nhận có |
| Hồng treo gió | ✅ Có | `dacsan` — "Hồng treo gió" | Chỉ 1 điểm bán | ✅ Thêm quầy chuyên `hong` 'HỒNG TREO GIÓ & BƠ SÁP' |
| **Hồng giòn (tươi)** | ❌ **Chưa có** | — | Cả 3 nguồn đều nêu hồng giòn là trái cây đặc trưng; game chỉ có hồng treo gió | ❌ **Vẫn chưa có** — quầy `hong` mới cũng chỉ treo gió + bơ (xem Mục 6) |
| Bơ sáp / bơ 034 | ✅ Có, khá đủ | `dau` — "Bơ 034 (1kg)", `yaourt` — "Sinh tố bơ", kem bơ ở `dau` | — | ✅ Thêm ở quầy `hong` |
| Trà atiso | ✅ Có | `dacsan` — "Trà atiso túi lọc" | Chỉ 1 món lẻ, không có quầy chuyên | ✅ Thêm quầy chuyên `tra2` 'TRÀ ATISO & CÀ PHÊ' + kệ trà tiệm lớn |
| Trà khác (ô long…) | ✅ Có | `tra` — "Trà ô long (hộp)" | Trà lài/khổ qua/bồ công anh chưa có (nhóm phụ, chấp nhận được) | ➖ Không đổi |
| Cà phê hạt mang về | ✅ Có | `tra` — "Cà phê hạt Cầu Đất"; uống tại chỗ ở `caphe` | — | ✅ Thêm ở `tra2` + kệ cà phê tiệm lớn |
| Rượu vang Đà Lạt | ❌ **Chưa có** | — | Cả Nam Thiên và Vexere đều nêu là đặc sản chợ | ❌ **Vẫn chưa có** (không quầy mới nào bán) |
| Nước cốt trái cây đóng chai | ❌ Chưa có dạng quà | Chỉ có "Nước ép dâu tằm" uống tươi ở `traicay` | Thiếu dạng đóng chai mang về | ❌ Vẫn chưa xác nhận có |
| Chuối la ba | ❌ Chưa có | — | Trái cây phụ, Nam Thiên nêu | ❌ Vẫn chưa có (nhóm nhỏ) |

### 4.2 Hoa và rau củ

| Loại hàng thật | Trước BLENDER-DEEP-2 | Sạp / món trong game | Thiếu gì (trước vòng) | Sau BLENDER-DEEP-2 |
|---|---|---|---|---|
| Hoa cẩm tú cầu | ✅ Có | `hoa` — "Bó cẩm tú cầu" | — | ✅ Thêm quầy chuyên `hoa2` 'HOA TƯƠI CẨM TÚ CẦU' |
| Hoa baby | ✅ Có | `hoa` — "Bó hoa baby" | — | ➖ Không đổi |
| **Hoa hồng** | ❌ Chưa có món lẻ | — | Hoa hồng là mặt hàng hoa chủ lực chợ thật | ❌ **Vẫn chưa có món lẻ** — `hoa2` vẫn là cẩm tú cầu |
| **Hoa cúc** | ❌ Chưa có món lẻ | — | Thiếu | ❌ **Vẫn chưa có món lẻ** |
| Hoa cẩm chướng / lay ơn | ❌ Chưa có | — | Nhóm phụ | ❌ Chưa có |
| Hoa khô | ❌ Chưa có | — | Nguồn thật có bán hoa khô làm quà | ❌ Chưa có |
| Sen đá / cây cảnh mini | ❌ Chưa có | — | Nam Thiên nêu ở nhóm hoa + cây cảnh | ❌ Chưa có |
| Atiso tươi | ✅ Có | `rau` — "Atiso tươi (1kg)" | — | ➖ Không đổi (đủ) |
| Su su | ✅ Có (gộp) | `rau` — "Su su & cà rốt" | Gộp chung 1 món với cà rốt | ➖ Không đổi |
| Cà rốt | ✅ Có (gộp) | `rau` — "Su su & cà rốt" | Như trên | ➖ Không đổi |
| Rau củ khác: súp lơ, khoai tây, khoai lang (tươi), hành tây, xà lách, cà chua bi, ớt chuông, bắp cải | 🟡 Chỉ decor | Biển `RAU CỦ` quầy decor nhà lồng; khoai lang chỉ có dạng nướng ở `khoai`/`khoainuong` | Không có sạp rau tương tác thứ hai, menu rau chỉ 2 món | ❌ Vẫn vậy — vòng mới không bổ sung sạp rau |

### 4.3 Thời trang, đồ si, lưu niệm

| Loại hàng thật | Trước BLENDER-DEEP-2 | Sạp / món trong game | Thiếu gì (trước vòng) | Sau BLENDER-DEEP-2 |
|---|---|---|---|---|
| Áo len / cardigan | ✅ Có | `len1` — áo len cổ lọ; `aolen` — cardigan | — | ✅ Thêm `len3` 'ĐỒ LEN GIÁ RẺ' |
| Khăn choàng / khăn len | ✅ Có | `len1`, `aolen` | — | ✅ Thêm ở `len3` (theo tên quầy) |
| Mũ len | ✅ Có | `len2` — mũ beanie | — | ➖ Đủ |
| Găng tay len | ✅ Có | `len2` — găng tay len | — | ➖ Đủ |
| Tất len | ❌ Chưa có món lẻ | — | Nguồn thật liệt kê trong bộ đồ len | ❌ Chưa xác nhận có ở `len3` |
| Búp bê len | ❌ Chưa có | — | Món len lưu niệm đặc trưng (kiêm lưu niệm) | ❌ Chưa xác nhận có |
| Áo khoác | ✅ Có | `aokhoac` — dạ dày, gió 2 lớp | Áo khoác giữ nhiệt kiểu mới chưa có (phụ) | ➖ Đủ dùng |
| Quần áo thường / trend | 🟡 Yếu | Chỉ áo khoác + áo len; giá treo quần áo decor ở khu chợ la | Không có sạp quần áo phổ thông riêng | 🟡 Có thêm `dosi` cho mảng si; quần áo mới thường vẫn mỏng |
| **Đồ si / secondhand** | ❌ **Chưa có hẳn** | — | Nam Thiên nêu rõ là nhóm hàng được giới trẻ "săn" ở chợ đêm | ✅ **Đã bổ sung** quầy `dosi` 'ĐỒ SI SECONDHAND' (45;22,5) |
| Móc khóa | ✅ Có | `luuniem` — "Móc khóa Đà Lạt" | — | ✅ Thêm `luuniem2` + kệ lưu niệm tiệm lớn |
| Bưu thiếp / postcard | ✅ Có | `luuniem` — "Bưu thiếp Đà Lạt" | — | ➖ Đủ |
| **Tranh gỗ / tranh bút lửa / tranh khắc gỗ** | ❌ Chưa có | — | Thủ công mỹ nghệ đặc trưng được nguồn nêu đích danh | ❌ Chưa xác nhận món lẻ ở `luuniem2`/tiệm lớn |
| **Chuông gió** | ❌ Chưa có | — | Lưu niệm phổ biến ở chợ thật | ❌ Chưa xác nhận có |
| Nam châm tủ lạnh | ❌ Chưa có | — | Travel.com.vn nêu đích danh | ❌ Chưa xác nhận có |
| Gấu bông / túi vải / sổ tay | ❌ Chưa có món lẻ | — | Nhóm lưu niệm phụ | ❌ Chưa xác nhận có |
| Đồng hồ / kính mát | ✅ Có (ngoài danh mục chợ thật cốt lõi) | `dongho` | — (điểm cộng riêng của game, ki-ốt xưa cạnh rạp) | ➖ Không đổi |

### 4.4 Đồ ăn / đồ uống đêm

| Món thật | Trước BLENDER-DEEP-2 | Sạp trong game | Ghi chú |
|---|---|---|---|
| Bánh tráng nướng | ✅ Có | `banhtrang` (trứng, phô mai) + decor | Đủ, đúng vị thế "pizza Đà Lạt" |
| Bánh tráng trộn | ✅ Có | `tron` | Đủ |
| Sữa đậu nành nóng | ✅ Có, dày | `sua`, `suadau`, `hoasua` (+ sữa tươi ở `suatuoi`) | 3–4 điểm bán — khớp chợ thật |
| Bánh căn | ✅ Có | `banhcan` (trứng cút, hải sản) | Đủ |
| Súp cua | ✅ Có | `supcua`, `chao` | 2 điểm bán |
| Chè nóng | ✅ Có | `supcua` (đậu xanh), `che` (trôi nước) | Đủ cơ bản; chè thập cẩm/đậu đen chưa tách món (phụ) |
| Xiên nướng | ✅ Có | `xien` (thịt, chân gà), `haisan` (hải sản, hàu) | Đủ |
| Bánh mì xíu mại | ✅ Có | `banhmi` (+ xíu mại chén ở `banhuot`) | Đủ |
| Bánh ướt lòng gà | ✅ Có | `banhuot` | Đủ |
| Khoai / bắp nướng | ✅ Có | `khoai`, `khoainuong` | 2 điểm bán |
| Dâu lắc / trái cây lắc | ✅ Có | `dau` (dâu lắc), `traicay` (trái cây lắc, nước ép) | Đủ |
| Kem bơ / sinh tố bơ / yaourt | ✅ Có | `dau`, `yaourt` | Đủ |
| Đậu hũ nóng | ✅ Có | `dauhu`, `suadau`, `suatuoi` | Đủ |
| Cháo đêm / hủ tiếu / mì đêm | ✅ Có | `chao`, `hutieu` | Đủ |
| Bánh flan | ✅ Có | `banhflan` | Đủ |
| Cà phê / cacao nóng tại chỗ | ✅ Có | `caphe` | Đủ |
| Nem nướng | ❌ Chưa có | — | Vexere nêu trong nhóm ăn vặt đêm |
| Bánh xèo | ❌ Chưa có sạp | — | Vexere nêu ở khu ăn trong chợ |
| Bánh canh cá lóc | ❌ Chưa có sạp | — | Vexere nêu ở khu ăn trong chợ |
| Lẩu gà lá é / lẩu bò / ốc nhồi thịt / miến gà | ❌ Chưa có | — | Là **quán quanh chợ** (Travel.com.vn ghi rõ địa chỉ ngoài chợ, cách tới 2km) — ngoài phạm vi sạp chợ, ghi nhận để biết chứ không tính là lỗi thiếu sạp |

### 4.5 Hàng chợ ngày trong nhà lồng (thịt cá, gia vị, bách hóa…)

| Loại hàng thật | Trong game | Ghi chú |
|---|---|---|
| Thịt & cá tươi | 🟡 Chỉ biển decor `THỊT & CÁ` | Không có sạp tương tác |
| Gia vị | 🟡 Chỉ biển decor `GIA VỊ` | Không mua được |
| Đồ khô / bánh kẹo / mứt kẹo (sạp trong nhà) | 🟡 Chỉ biển decor `ĐỒ KHÔ`, `BÁNH KẸO`, `MỨT & KẸO` | Tuyến đặc sản tương tác nằm ở sạp ngoài trời + tiệm lớn mới |
| Giò chả, vải, điện máy, mỹ phẩm, túi xách, giày dép, gốm sứ | ❌ Chưa có kể cả biển decor riêng | 8 nhóm biển decor hiện tại chưa phủ các nhóm này; đây là hàng tầng trên chợ thật — ưu tiên thấp cho game chợ đêm |

---

## 5. ĐÃ BỔ SUNG TRONG VÒNG BLENDER-DEEP-2

Theo hồ sơ vòng BLENDER-DEEP-2 (ghi vào mục này theo brief, không đối chiếu lại từng món lẻ):

| id | Tên quầy | Vị trí | Lấp lỗ hổng nào |
|----|----------|--------|-----------------|
| `dau2` | DÂU TÂY ĐÀ LẠT | Đường vào, hàng bắc (−80; −19,7) | Dâu tây chỉ có 1 sạp |
| `dau3` | DÂU TÂY & MỨT DÂU | Đường vào, hàng nam (−81,5; 30) | Dâu + mứt dâu ở tuyến đường vào |
| `dau4` | DÂU TÂY TƯƠI | Mặt tiền chợ (12; 11) | Dâu ở mặt tiền — **tổng quầy dâu = 4** kể cả `dau` cũ |
| `mut` | MỨT & TRÁI CÂY SẤY | (−68,5; 30) | Nhóm mứt đa vị + trái cây sấy từng **không có quầy riêng** |
| `hong` | HỒNG TREO GIÓ & BƠ SÁP | (−93; −19,7) | Hồng treo gió + bơ từng chỉ là món lẻ trong sạp khác |
| `tra2` | TRÀ ATISO & CÀ PHÊ | (−114,5; −19,7) | Trà atiso từng chỉ 1 món lẻ ở `dacsan` |
| `hoa2` | HOA TƯƠI CẨM TÚ CẦU | (−106,5; 30) | Hoa tươi từng chỉ 1 sạp 2 món |
| `luuniem2` | LƯU NIỆM ĐÀ LẠT | Khu phải bậc tam cấp (45; 17,5) | Lưu niệm ở khu phải bậc (trước chỉ có `luuniem` trên đồi) |
| `dosi` | ĐỒ SI SECONDHAND | (45; 22,5) | **Đồ si từng thiếu hẳn** |
| `len3` | ĐỒ LEN GIÁ RẺ | (40; 27,5) | Thêm phân khúc len giá rẻ cạnh `aokhoac`/`aolen` |

**Cộng 1 TIỆM LỚN 'ĐẶC SẢN – LƯU NIỆM' vào được bên trong** tại khu phải bậc tam cấp (mặt tiền x=49, sâu tới 59, z 14,5–25,5): bên trong có kệ trái cây sấy / mứt / trà / cà phê / lưu niệm / đồ len + quầy tính tiền. Đây là bổ sung có trọng lượng nhất của vòng: lần đầu tuyến đặc sản mang về có một điểm bán kiểu cửa hàng (đúng mô hình L'angfarm / cửa hàng đặc sản tầng 1 mà các nguồn thật khuyên mua), thay vì chỉ sạp lẻ.

> ⚠️ **Lưu ý kiểm chứng (ghi thẳng, không che):** trong bản `prototype-v2/index.html` được đọc để rà soát ngày 09/11/2026, các id `dau2`, `dau3`, `dau4`, `mut`, `hong`, `tra2`, `hoa2`, `luuniem2`, `dosi`, `len3` và tên tiệm 'ĐẶC SẢN – LƯU NIỆM' **chưa xuất hiện trong `STALL_DEFS`** (grep toàn file: 0 kết quả cho cả id lẫn tên quầy). Tức là ở thời điểm rà soát, các quầy này hoặc nằm ở lớp dựng khác ngoài `STALL_DEFS`, hoặc chưa hợp nhất vào file này. Trước khi nghiệm thu vòng, cần một lượt mở game / quét code xác nhận các quầy đã thực sự hiện diện và mua được — rà soát này chỉ ghi nhận chúng theo hồ sơ vòng, đúng như brief giao.

---

## 6. CÒN THIẾU / CHƯA LÀM (sau cả vòng BLENDER-DEEP-2)

Ghi thẳng, không che giấu — các loại hàng thật dưới đây game **vẫn chưa có** ở dạng món mua được, tính đến hết vòng BLENDER-DEEP-2:

1. **Hồng giòn tươi** — thiếu hẳn và là thiếu rõ nhất còn lại của tuyến trái cây: cả 3 nguồn đều nêu, game chỉ có hồng treo gió (kể cả quầy `hong` mới cũng là treo gió + bơ sáp, không có hồng giòn).
2. **Mứt tách vị có tên món lẻ** — mứt hồng, mứt khoai lang, mứt mận, mứt me (và phụ: gừng, hoa hồng, cà chua): quầy `mut` + kệ mứt tiệm lớn đã có ở mức tên quầy/kệ, nhưng chưa xác nhận menu có từng vị tách riêng như chợ thật; ở `STALL_DEFS` cũ vẫn chỉ 1 món gộp "Hộp mứt dâu".
3. **Trái cây sấy tách loại có tên món lẻ** — kiwi sấy, phúc bồn tử sấy, dâu sấy, hồng sấy dẻo (khác hồng treo gió), mít sấy, khoai sấy: cùng tình trạng như mứt — có quầy/kệ theo nhóm, chưa xác nhận món lẻ; phúc bồn tử chưa thấy ở bất kỳ đâu.
4. **Hoa hồng và hoa cúc** — hai mặt hàng hoa chủ lực của chợ thật vẫn không có món lẻ nào; sạp hoa cũ chỉ cẩm tú cầu + baby, quầy mới `hoa2` vẫn chuyên cẩm tú cầu. Cẩm chướng, lay ơn, hoa khô, sen đá/cây cảnh cũng chưa có.
5. **Rượu vang Đà Lạt** — chưa có ở bất kỳ sạp/quầy/tiệm nào, dù 2 nguồn nêu là đặc sản chợ.
6. **Nước cốt trái cây đóng chai** (dâu, chanh dây, phúc bồn tử) — chỉ có nước ép uống tươi, chưa có dạng quà đóng chai.
7. **Tất len và búp bê len** — hai món len đặc trưng chưa có món lẻ; `len3` mới ở mức tên quầy giá rẻ, chưa xác nhận có hai món này.
8. **Tranh gỗ / tranh bút lửa, chuông gió, nam châm tủ lạnh, gấu bông, túi vải, sổ tay** — nhóm lưu niệm thủ công mà nguồn nêu đích danh; `luuniem` cũ chỉ có móc khóa + bưu thiếp, chưa xác nhận `luuniem2` và kệ lưu niệm tiệm lớn có các món này.
9. **Sạp rau củ thứ hai / menu rau mở rộng** — rau tương tác vẫn chỉ 1 sạp 2 món (atiso; su su & cà rốt gộp); súp lơ, khoai tây, xà lách, cà chua bi, ớt chuông, bắp cải, hành tây chỉ ở mức biển decor nhà lồng.
10. **Hàng tươi sống và bách hóa chợ ngày** — thịt & cá tươi, gia vị, giò chả: chỉ có biển decor, không sạp tương tác nào (chấp nhận được nếu game giữ trọng tâm chợ đêm, nhưng nếu muốn mô phỏng đủ chợ ngày thì đây là khoảng trống nguyên vẹn).
11. **Nem nướng, bánh xèo, bánh canh cá lóc** — món ăn Vexere nêu trong khu chợ, chưa có sạp.
12. **Chuối la ba** — trái cây phụ của chợ thật, chưa có (thiếu nhỏ).

Ngoài hàng hóa, hai lệch số liệu cần vòng sau sửa hồ sơ: (a) tài liệu ghi "31 sạp tương tác" nhưng code thực tế có **33**; (b) lưới quầy decor nhà lồng thường được nói "~48 quầy" — đó là số **vị trí lưới**, số quầy thực dựng sau lọc là **33**.

---

## 7. Kết luận và thứ tự ưu tiên gợi ý

- **Ăn uống đêm: đã đủ chất chợ Âm Phủ.** Hầu như mọi món nguồn thật nêu (bánh tráng nướng/trộn, sữa đậu nành, bánh căn, súp cua, chè, xiên nướng, bánh mì xíu mại, bánh ướt lòng gà, khoai/bắp nướng, dâu lắc, kem bơ…) đều có sạp tương tác, nhiều món có 2–4 điểm bán như chợ thật.
- **Đặc sản mang về: từ "thiếu nặng" thành "gần đủ" nhờ BLENDER-DEEP-2.** Trước vòng này chỉ có 2 sạp đặc sản mỏng (`dacsan`, `tra`) và nhóm trái cây sấy **không có món nào mua được**; vòng này thêm 10 quầy + 1 tiệm lớn vào được bên trong, phủ đúng các nhóm yếu nhất: dâu (×4 quầy), mứt & trái cây sấy, hồng treo gió & bơ, trà atiso & cà phê, hoa cẩm tú cầu, lưu niệm khu phải, đồ si, len giá rẻ.
- **Ưu tiên vòng sau (nếu làm tiếp):** P1 — thêm món lẻ **hồng giòn** và tách vị **mứt / trái cây sấy** thành món có tên trong menu quầy `mut` + tiệm lớn (kiwi, phúc bồn tử trước); P2 — thêm **hoa hồng, hoa cúc** vào menu hoa; P3 — **rượu vang** + **nước cốt đóng chai** ở kệ tiệm lớn, và các món lưu niệm lẻ (tranh gỗ, chuông gió, nam châm). Đồng thời nghiệm thu trực tiếp 10 quầy + tiệm lớn của BLENDER-DEEP-2 trong bản game chạy thật (xem lưu ý ở cuối Mục 5).
