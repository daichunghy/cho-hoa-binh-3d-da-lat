# 18 — ĐÊM THẬT: TRANG PHỤC ĐÁM ĐÔNG · VẬT PHẨM ĂN UỐNG · BÙNG BINH VỀ ĐÊM (đợt sau v5.0)

> Nguồn cơn: Chung Hy chơi thử v5.0 và bác với 3 điểm cụ thể + 1 lệnh nguồn: *"Vẫn chưa đạt luôn, nhân vật đa dạng trang phục [chưa có], vật phẩm ăn uống chưa có, bùng binh không giống — tham khảo ảnh với video đi buổi tối đó"*.
> File này CHỈ nghiên cứu (không sửa code/model): (1) lấy tư liệu ĐÊM mới ngoài bộ research/16; (2) lập bảng trang phục đám đông đêm thật → ánh xạ hệ NPC bằng đúng kho 60 món + bảng 14 màu sẵn có; (3) kiểm kê vật phẩm ăn uống nhìn thấy được trong tư liệu đêm → đối chiếu game; (4) phân tích bùng binh về đêm đặt cạnh render góc A hiện tại (`prototype-v2/renders/v52-A-bung-binh-dem.png`).

---

## 0. TƯ LIỆU ĐÊM MỚI — lấy được tới đâu, giới hạn nói thẳng

**Video đi dạo buổi tối MỚI (ngoài bộ research/16)** — đã tra cứu danh mục + lấy khung hình đại diện cho cả 10:

| # | Video | Kênh | Độ dài | Khung đã lưu |
|---|---|---|---|---|
| 1 | Da Lat Vietnam, Visit Da Lat Night Market, Experience Vietnamese Street Food — 4K Virtual Travel | Walking On | 32:39 | 29 |
| 2 | [4K] Da Lat Night Market Walking Tour — One of the biggest night markets in Vietnam | Slow Walks | 47:01 | 30 |
| 3 | [4K] Dalat Night Market Tour — 달랏야시장 | Seoul Walker | 23:14 | 28 |
| 4 | [4K] Vietnam Walk, Da Lat Night Market — Vietnamese Street Food Tour | Walking Expedition | 27:46 | 31 |
| 5 | Da Lat Night Market — VIETNAM 4K Walking Tour of Famous Street Food & 'Hell Market' | Jonny Walk | 43:59 | 32 |
| 6 | Da Lat Night Market Walking Tour — Vietnam Nightlife 4K POV | EchoesAreEverywhere | 12:02 | 33 |
| 7 | [4K] Have you ever been here? Da Lat Night Market, Viet Nam 4K Walking Tour | WALK & TRAVEL 4K | 50:06 | 34 |
| 8 | DA LAT NIGHT MARKET TOUR WALKING SLOW 4K | Mr ROYCE Vlog | 25:43 | 35 |
| 9 | Vietnam, Da Lat: Night Market Evening to Night Walking Tour — 4K | Walking Asia | 40:04 | 36 |
| 10 | Đêm hè giá rét Đà Lạt đông vui từ Khu Hòa Bình về nhà sương mờ giăng lối | Đà Lạt ngày nay_Ống kính TV | 16:49 | 37 |

**Ảnh web đêm mới:** 38 (cận bàn sữa đậu nành — Vietnam Airlines), 39 (bùng binh chạng vạng trên cao — Phuotvivu). Tổng tư liệu mới: **12 file, đánh số 28–39** trong `theme/real-market/`, nguồn đã ghi vào `theme/real-market/SOURCES.md`.

**GIỚI HẠN KỸ THUẬT (quan trọng):** máy chủ bị YouTube chặn tải file video (HTTP 429 + yêu cầu đăng nhập xác thực bot) nên **không tải được video để trích nhiều khung**. Khung hình lưu lại là **ảnh bìa chính thức 1280×720 do chính kênh đăng cho video đó** — là khung hình thật của video, đủ đối chiếu bố cục/trang phục/vật phẩm ở mức cảnh, nhưng **mỗi video chỉ có đúng 1 khung** và một số khung bị chữ tiêu đề của kênh phủ lên (đã ghi chú ở SOURCES.md; khi dựng hình chỉ lấy phần cảnh). Muốn trích khung dày theo phút (đếm tỉ lệ trang phục chính xác theo mẫu lớn) cần tải video từ máy có phiên đăng nhập YouTube — việc đó nằm ngoài đợt nghiên cứu này. Tỉ lệ % ở mục 1 là **ước lượng bằng mắt từ 12 khung mới + bộ ảnh đêm sẵn có (04, 05, 08, 09, 13, 27)**, không phải đếm mẫu thống kê.

---

## 1. TRANG PHỤC ĐÁM ĐÔNG ĐÊM

### 1.1 Đám đông đêm thật mặc gì (từ tư liệu đêm)

Đà Lạt đêm lạnh (mốc game đang dựng: ~19:00, trời lạnh) — ảnh 29/30 là mẫu chuẩn mùa lạnh; ảnh 32/34 là đêm ấm hơn, dùng để cân tỉ lệ lớp nhẹ.

| Lớp trang phục | Tỉ lệ ước lượng (đêm lạnh) | Màu/chi tiết chủ đạo trong khung |
|---|---|---|
| **Áo phao (puffer)** — phom PHỒNG rõ | ~30–35% | **Trắng/kem và đen là 2 màu áp đảo** (cô gái áo phao trắng ở tiền cảnh ảnh 29 là hình mẫu), thêm đỏ, xanh navy |
| Áo khoác dạ/kaki dài, trench | ~15% | Be, nâu, đen; dài qua hông, có ve áo |
| **Hoodie** (kèm mũ trùm, một phần trùm lên đầu) | ~15% | Tím, xanh lá tươi, vàng mù tạt, xám — là lớp màu "nhảy" nhất đám đông (ảnh 34) |
| Áo len / cardigan / len sọc | ~10% | Len sọc nhiều màu (tiểu thương sạp xiên, ảnh 31), len trơn nâu/xám |
| Áo khoác jean / da | ~5% | Đen (da), xanh jean |
| Lớp nhẹ: áo thun, sơ mi, váy (khách từ vùng ấm; đêm hè) | ~10–15% | Trắng, kẻ caro, váy hoa (ảnh 32/34) — có nhưng là thiểu số trong đêm lạnh |
| **Mũ len beanie** | ~20–25% người | **Màu mũ THƯỜNG KHÁC màu áo** (beanie đỏ trên áo nâu, beanie xám trên áo đen…) |
| Mũ lưỡi trai | ~15% | Trắng/đen cơ bản |
| Mũ bucket / mũ trùm hoodie | ~5–10% | |
| **Nón lá** | ~3–5% | **Chỉ tiểu thương + người bán gánh** (ảnh 33); khách đi chợ gần như không đội |
| **Khăn quàng cổ** | ~15–20% | Màu tương phản với áo (đỏ trên đen, vàng trên nâu) |
| Khẩu trang | ~15% | Đặc điểm đám đông VN hiện nay — thấy ở mọi khung cận |
| Mang túi (ba lô / tote / túi chéo / giỏ nhựa đi chợ) | ~35–40% | Giỏ nhựa đỏ là dấu hiệu "người đi mua đồ" (ảnh 33) |
| **Tay cầm đồ** (túi nilon đồ đã mua, ly giấy, điện thoại, đồ ăn cầm tay) | ~50%+ | Xem mục 2 — đây là lớp "sống" mạnh nhất |
| Trẻ em đi cùng gia đình | ~8% | Áo phao/hoodie nhỏ, hay được dắt tay hoặc bế |

Hai quy luật thị giác rút ra:
1. **Đám đông đêm Đà Lạt đọc bằng PHOM trước, màu sau:** phồng (phao) — dài (dạ) — trùm (hoodie) — ôm (len). Bốn phom này xen nhau thì đám đông "đa dạng" ngay cả khi màu trùng.
2. **Mũ là mảng màu độc lập với áo** trong ảnh thật; và **lớp sáng nằm ở phao trắng/kem + hoodie màu tươi**, còn lại đa số là khối tối (đen/nâu/navy) — đám đông đêm thật TỐI hơn bảng màu game hiện tại khá nhiều.

### 1.2 Game hiện tại đơn điệu ở đâu (đo trực tiếp trong code `prototype-v2/index.html`)

Hàm dựng người: `makePerson(shirt, pants, hat, skin)` (~dòng 1063) + `crowdPerson()` (~1872). Kết quả đo:

| Hạng mục | GAME HIỆN TẠI | Hệ quả thị giác |
|---|---|---|
| Phom thân | **1 phom duy nhất** cho mọi NPC (cùng 1 character.glb, áo Shirt là lớp len ôm) | Không phao, không dạ dài, không hoodie → đám đông là "một người nhân bản đổi màu áo" |
| Chiều cao / tỉ lệ | **Không hề có scale ngẫu nhiên cho NPC** (grep: không scale nào áp lên person) — tất cả cao đúng 1,824; **không có trẻ em** | Hàng người đều tăm tắp như đội hình |
| Tông da | Tham số `skin` tồn tại nhưng crowd **không bao giờ truyền** → 100% NPC cùng tông da mặc định 0xd9a37e | Đồng nhất tuyệt đối ở cự ly gần |
| Mũ len | `recolor(g,'Beanie', shirt)` — **beanie luôn TRÙNG MÀU ÁO** (chủ đích "bảng tạo hình B1") | Mất hẳn mảng màu độc lập trên đầu; đầu và thân thành một khối một màu |
| Tỉ lệ mũ (crowd) | `CROWD_HATS = [beanie,beanie,cap,none,beanie,cap,nonla]` → beanie 43%, cap 29%, none 14%, **nón lá 14%** | Nón lá 14% cho KHÁCH là sai vai (thật ~0% ở khách, chỉ người bán); thiếu bucket/mũ trùm |
| Wanderer (người đi dạo) | `addWanderer`: quần **100% một màu** 0x4a4640, mũ mặc định cap, **khăn 0%** (makePerson tắt Scarf, wanderer không bật lại), áo 1 màu cố định/người | Lớp người chuyển động — lớp mắt thấy nhiều nhất — lại là lớp đơn điệu nhất |
| Tiểu thương | 100% nón lá, quần cùng 1 màu, áo theo `def.shirt` | Thật: tiểu thương đêm mặc len sọc/beanie/áo khoác đủ loại (ảnh 31, 35); nón lá chỉ là thiểu số ban đêm |
| Khăn quàng | crowd có (35% mặc định, 40–55% ở hàng chờ/sitters, 5 màu) — **điểm này game làm tốt hơn cảm giác chung** | Nhưng wanderer/vendor = 0% nên tổng thể vẫn thiếu |
| Túi / ba lô | **0% NPC có** — món P2 (ba lô vải bố), P9 (túi đeo chéo) có sẵn trong WARDROBE_DEFS nhưng hệ gắn chỉ chạy cho NGƯỜI CHƠI | Đám đông "đi chợ mà không mang gì" |
| Vật cầm tay | **0% NPC thường có** — T1 ly sữa, T4 bắp, T6 bánh tráng, T7 xiên đều có sẵn dạng part, chỉ gắn cho player | Xem mục 2 |
| Khẩu trang | Không có | Thiếu dấu hiệu đám đông VN hiện nay (nhỏ, tuỳ chọn) |

### 1.3 Ánh xạ thành HỆ TRANG PHỤC NPC (chỉ dùng kho sẵn có)

**Nguyên tắc:** không cần GLB mới. Kho 60 món WARDROBE_DEFS đã có cơ chế part primitive (box/cyl/sph theo anchor `R` thân / `AR` tay phải / `LEGS` chân) và character.glb đã có sẵn node `HatBeanie / HatCap / HatNonLa / Scarf`. NPC dùng chung đúng character.glb đó → mọi món dưới đây đều gắn được lên NPC bằng cùng hàm dựng part của tủ đồ, chỉ cần cho `crowdPerson` gọi thêm bước "mặc ngẫu nhiên theo bảng phân bổ".

| Lớp thật | Món sẵn có dùng cho NPC | Cách dùng |
|---|---|---|
| Áo phao (~30%) | Không có món phao — tạo bằng **scale ngang mesh Shirt ×1,18–1,28 + rút ngắn tay** (phom phồng), màu ưu tiên **trắng/kem 0xe8c87e pha sáng + đen 0x2e2a26 + đỏ đô** | Cần thêm 2 màu vào bảng crowd: trắng kem sáng và đen — bảng 14 hiện **không có trắng, không có đen** (màu tối nhất là nâu 0x2e2a26 ở bảng QUẦN) |
| Áo dạ dài (~15%) | **A2/A9** (áo khoác dạ dài: có sẵn part vạt dưới + ve áo + nút) | Gắn part A2, đổi màu theo bảng (navy 0x35507a, nâu 0x7a4a2e, be = màu A2 gốc) |
| Hoodie (~15%) | Beanie đổi vai thành **mũ trùm**: beanie màu trùng áo + khăn K5 (khăn ống) quấn cao; màu áo lấy nhóm tươi (tím 0x8668c4, xanh lá, vàng) | Đọc thành hoodie ở khoảng cách chơi |
| Áo len thường (~25%) | Shirt mặc định + hoạ tiết: A3 (sọc ngang), A7 (caro) — pattern đã có sẵn trong def | Xen kẽ để phá đơn sắc |
| Lớp nhẹ (~15%) | Shirt trơn màu sáng (kem, hồng đào, dương nhạt) + không khăn | Cho nhóm khách trẻ |
| Mũ len (~25%) | Node HatBeanie — **đổi màu ĐỘC LẬP với áo**, lấy từ bảng 14 + đỏ tươi 0xc8372d | Bỏ quy tắc trùng màu áo riêng cho NPC (player giữ nguyên) |
| Mũ lưỡi trai (~15%) | Node HatCap sẵn có | Giữ |
| Nón lá | Node HatNonLa — **chỉ vendor + người bán gánh**, tỉ lệ khách = 0 | Sửa CROWD_HATS: bỏ nonla khỏi pool khách |
| Khăn (~25% đêm lạnh) | Node Scarf (đã có) + K3 khăn tua rua (part) cho vài % nổi bật | Bật cho cả wanderer (hiện 0%) theo tỉ lệ 25% |
| Găng tay (~8%) | **P1** (part 2 box ở 2 tay) | Chủ yếu cho rider/người đứng chờ |
| Ba lô / túi (~35%) | **P2** ba lô, **P9** túi chéo, **T3** túi tote | Phân bổ ~35%, là lớp phá silhouette mạnh thứ hai sau phom áo |
| Trẻ em (~8%) | Scale tổng 0,70–0,78 + áo màu tươi + beanie chóp bông **M2** | Đặt cạnh 1 người lớn (cụm gia đình ở thang/quảng trường) |
| Chiều cao người lớn | Scale tổng 0,96–1,04 ngẫu nhiên | Phá hàng đều |
| Tông da | Truyền `skin` ngẫu nhiên trong 3 tông quanh 0xd9a37e (sáng/trung/nâu) | Cự ly gần mới thấy, chi phí 0 |

**Số tổ hợp tối thiểu để đọc "đa dạng":** bài toán không nằm ở tổng tổ hợp (14 áo × 4 quần × mũ × khăn × túi đã cho hàng nghìn) mà ở **phân bổ trong khung hình**. Chuẩn đề xuất: *trong bất kỳ 10 NPC liên tiếp trong một khung nhìn, không có 2 người trùng đồng thời (phom áo + màu mũ + có/khăn)*. Đạt được bằng bảng phân bổ theo vai trò:

| Nhóm NPC | Phao | Dạ dài | Hoodie | Len | Nhẹ | Mũ len khác màu | Cap | Khăn | Túi/ba lô | Cầm đồ ăn/uống |
|---|---|---|---|---|---|---|---|---|---|---|
| Người đi dạo (wanderer) | 30% | 15% | 15% | 25% | 15% | 25% | 15% | 25% | 35% | 30% (mục 2) |
| Hàng chờ mua | 30% | 10% | 15% | 30% | 15% | 25% | 15% | 30% | 30% | 15% (người đã mua xong ở cuối hàng) |
| Người ngồi ăn (thang/bàn) | 35% | 10% | 20% | 25% | 10% | 20% | 10% | 30% | để cạnh ghế | bàn có đồ (mục 2) |
| Tiểu thương | 10% | 0% | 10% | **50% (ưu tiên len sọc A3)** | 0% + tạp dề màu tối 30% | **beanie 35%** | 10% | 20% | — | nón lá **chỉ 20%** (đêm), còn lại beanie/trần |

---

## 2. VẬT PHẨM ĂN UỐNG

### 2.1 Kiểm kê: vật phẩm ăn uống NHÌN THẤY ĐƯỢC trong tư liệu đêm

**A. Trên tay người đi chợ** (lớp thiếu nặng nhất):

| Vật phẩm | Bằng chứng | Tỉ lệ cảm nhận |
|---|---|---|
| **Ly giấy đồ uống nóng có ống hút** (sữa đậu nành/sữa bắp) | Ảnh 32 (cô gái cầm giữa bùng binh), ảnh 35 (khách ngồi uống) | ~10% người đi bộ — vật phẩm nhận diện số 1 của chợ đêm Đà Lạt |
| **Túi nilon đựng đồ đã mua** (vàng/trong, căng đồ) | Ảnh 32 (túi vàng đầy), ảnh 28 (túi trắng lớn), ảnh 33 (túi xanh) | ~30% |
| Điện thoại trên tay | Mọi khung cận | ~20% |
| Bắp nướng / khoai nướng cầm tay (bọc giấy) | Ảnh 13 sẵn có + thực đơn sạp thang | ~5% |
| Xiên nướng cầm tay / khay xiên nhỏ | Ảnh 31 (khách với tay chọn xiên tại quầy) | Tại sạp xiên |
| Giỏ nhựa đỏ đi chợ | Ảnh 33 | Người mua thực phẩm tươi |
| Đòn gánh + 2 thúng (bán rong) | Ảnh 33 | 1–2 người bán rong lưu động |
| Bóng bay tạo hình (bán ở đầu thang/quảng trường) | Ảnh 36 | Điểm nhấn trẻ em |

**B. Trên bàn ăn / trên bậc thang:**

| Vật phẩm | Bằng chứng |
|---|---|
| **2 ly THỦY TINH sữa nóng bốc khói + thìa inox + đĩa bánh mì** — bộ bàn mẫu | Ảnh 38 (cận cảnh) |
| Tô súp cua + cốc nhựa | Ảnh 35 (sạp súp cua) |
| Đĩa bánh căn (4–6 bánh nhỏ) + chén nước mắm + rau | Ảnh 15 sẵn có + menu sạp |
| Khay xiên đã nướng + chén chấm đỏ | Ảnh 31/14 |
| Cốc chè nhiều màu, ly yaourt | Menu chợ đêm chuẩn (nghiên cứu 09) |
| Ly giấy + ống hút trên bàn thấp | Ảnh 35 |

**C. Trên quầy sạp:**

| Vật phẩm | Bằng chứng | Ghi chú dựng hình |
|---|---|---|
| **Khay xiên trăm chiếc xếp nghiêng nhiều tầng** (thịt viên, xúc xích, đậu bắp xanh, mực, chả) | Ảnh 31 — hình ảnh đặc trưng nhất | Xiên phải đọc thành "rừng que" ở khoảng cách chơi: que mảnh sáng + đầu thịt màu, xếp dãy dày |
| Vỉ nướng dài + bánh tráng đang nướng + chồng bánh sống | Ảnh 14 | |
| Hàng khuôn bánh căn đất nung trên bếp than đỏ | Ảnh sẵn có + hero hiện tại | |
| Nồi sữa lớn bốc hơi + **tháp ly thủy tinh** + chồng ly giấy | Ảnh 38 + sạp sữa thật | |
| Nồi súp cua + tô xếp chồng | Ảnh 35 | |
| Vỉ bắp/khoai xếp dãy trên than | Ảnh 13 | |
| Dãy cốc chè màu (xanh/đỏ/vàng/trắng) trong tủ kính sạp chè | Thực đơn chợ đêm | |
| Tháp hũ yaourt thủy tinh | Sạp yaourt Tăng Bạt Hổ/chợ đêm | |
| Bình gas + bếp khò cạnh sạp nướng | Ảnh 31 (bình xám phải khung) | Chi tiết phụ tăng thật |
| Biển LED đỏ chạy chữ trước sạp xiên/nướng | Ảnh 31 | |

### 2.2 Đối chiếu game hiện tại (đo code + render)

| Vị trí | THẬT | GAME HIỆN TẠI | Mức |
|---|---|---|---|
| Tay tiểu thương | Đạo cụ nghề | **ĐÃ CÓ TỐT** (v4.9): ấm rót, xẻng lật, muôi khuấy, kẹp gắp, cân tay, túi gói, bó hoa — theo từng sạp | Đạt |
| Quầy 6 sạp hero (sữa, bánh tráng, bánh căn, cà phê, súp cua, dâu) | Hàng đặc trưng | **ĐÃ CÓ**: nồi thép + tháp ly sứ (sữa), vỉ + xiên (bánh tráng), khuôn đất (bánh căn), phin (cà phê), bậc dâu 3 tầng + ly kem bơ (dâu)… | Khá |
| Quầy sạp ăn KHÔNG hero: **xiên**, khoai, khoainuong, chè, yaourt, đậu hũ, bánh ướt, suadau, suatuoi, tron | Khay xiên trăm chiếc, vỉ bắp khoai, dãy cốc chè, tháp yaourt… | Chỉ có dressing thường (decorateStall: bóng/quả màu + hộp rời theo district) — **sạp xiên KHÔNG có khay xiên**, sạp chè không có dãy cốc màu, sạp yaourt không có tháp hũ | **Thiếu nặng** |
| Tay người đi chợ / hàng chờ | Ly giấy ~10%, túi nilon ~30%, điện thoại, bắp cầm tay | **0% — toàn bộ NPC thường tay không.** Các món T1/T4/T6/T7 đã có sẵn dạng part nhưng chỉ gắn cho NGƯỜI CHƠI qua tủ đồ | **Thiếu nặng nhất** |
| Trên bàn ăn (eatSet/eatCluster) | 2 ly + đĩa/tô + chén chấm (ảnh 38) | **Đúng 1 ly trụ trắng r=0,05 cao 0,09** — ở khoảng cách chơi gần như vô hình; không tô, không đĩa, không ly thứ hai | **Thiếu nặng** |
| Trên bậc cạnh người ngồi (STAIR_SITTERS) | Ly giấy/tô đặt cạnh, túi đồ để bên | 1 ly trụ mini r=0,04 cạnh mỗi người — có ý nhưng quá nhỏ để đọc | Yếu |
| Người bán rong | Đòn gánh, bóng bay | Chưa có nhân vật bán rong lưu động nào | Thiếu (điểm nhấn) |

### 2.3 Danh sách dựng bổ sung (theo vị trí bắt buộc, kích thước đọc được ở khoảng cách chơi ~8–20 unit)

Ưu tiên 1 — tay NPC (tái dùng part sẵn có, 0 model mới):
1. **Ly giấy + ống hút** (= part T1 đổi màu giấy trắng/kem + ống hút đỏ): gắn tay phải **12% wanderer + người rời hàng chờ**; kích thước giữ nguyên T1 (cao 0,14) — đọc được ở 10 unit nhờ ống hút đỏ chéo.
2. **Túi nilon căng đồ**: part mới dạng box bo (0,26×0,32×0,16) màu vàng trong/trắng sữa + quai — gắn tay trái **25% wanderer**; màu vàng nilon là mảng màu nhận diện từ xa.
3. **Bắp nướng cầm tay** (= part T4 có sẵn): 5% wanderer gần sạp khoai/thang.
4. **Điện thoại**: box mỏng 0,07×0,14 tối + mặt sáng nhẹ: 15% (đặc biệt nhóm đứng ở đảo — tư thế "chụp ảnh tượng đài").

Ưu tiên 2 — bàn ăn (nâng eatSet từ 1 vật lên bộ 4–5 vật):
5. Mỗi bàn: **2 ly (1 thủy tinh sữa bốc hơi nhẹ + 1 ly giấy)** + **1 tô/đĩa theo khu** (đĩa bánh căn 4 bánh nhỏ ở cụm gần sạp bánh căn; tô súp ở cụm quảng trường; khay 3 xiên ở cụm gần sạp nướng) + chén chấm đỏ nhỏ. Ly nâng cỡ lên r=0,06 cao 0,13 để đọc được.
6. Bậc thang: cạnh mỗi cụm sitters thêm **túi nilon + ly giấy** đặt trên bậc (thay ly mini đơn độc).

Ưu tiên 3 — quầy sạp không hero (mỗi sạp 1 "khối hàng" đặc trưng, dùng instancing/primitive):
7. **Sạp xiên: khay nghiêng 3 tầng, mỗi tầng 12–18 xiên** (que cyl mảnh 0,012 + đầu sph/box 0,05 màu luân phiên nâu đỏ/vàng/xanh đậu bắp) — tổng ~45 xiên/sạp, đây là vật phẩm phải làm trước tiên.
8. Sạp khoai/khoainuong: vỉ than (box tối + điểm emissive đỏ) + dãy 8 bắp vàng + 6 khoai tím nâu xếp hàng trên vỉ.
9. Sạp chè: dãy **10 cốc màu** (cyl 0,05 nhiều màu sáng) 2 hàng trong quầy.
10. Sạp yaourt: tháp hũ thủy tinh 3 tầng (cyl trắng kem 0,045 × ~12).
11. Sạp đậu hũ/bánh ướt/suadau: nồi + chồng chén sứ trắng (cyl 0,05 × 6) + thùng nước đường vàng trong.

Ưu tiên 4 — điểm nhấn lưu động:
12. **Người bán gánh** (wanderer đặc biệt: đòn gánh cyl cong + 2 thúng cyl + nón lá) chạy tuyến đường vào ↔ chân thang; **người bán bóng bay** đứng đầu thang (chùm 5 bóng màu trên que dài).

---

## 3. BÙNG BINH VỀ ĐÊM

### 3.1 Bùng binh đêm thật đọc khác ban ngày ở đâu

| Yếu tố | Ban ngày (ảnh 01) | **Ban đêm** (ảnh 28, 29, 32, 39 + 04, 05, 27 sẵn có) |
|---|---|---|
| Tượng đài | Đá xám, đọc bằng bóng đổ | **Được rọi sáng**: ở cự ly gần tượng TRẮNG SÁNG nổi bật giữa nền tối (ảnh 32 — đèn hắt từ chân bệ); từ xa/xiên đọc xám xanh tối nhưng luôn có vành sáng chân đảo bao quanh (ảnh 28) |
| Thảm hoa đảo | Họa tiết 2 màu nhìn từ trên cao | Vẫn đọc họa tiết xoáy/viền khi nhìn từ thang/trên cao (ảnh 39 chụp chạng vạng: thảm hoa là MỘT BỀ MẶT VẼ HỌA TIẾT, không phải bụi rời); ở mặt đất hoa chìm tối, thay vào đó **đèn nấm + đèn viền đảo** là thứ đọc được |
| Vành xe | Xe chạy + xe đậu rải | **Vệt sáng đèn xe chạy vòng liên tục** + **hàng xe máy đậu dài kín lề phía tây/bắc** (ảnh 28: tường xe đậu bên trái khung) + bãi giữ xe khổng lồ phía chợ (ảnh 05) |
| Người | Đi lại, chụp ảnh | **Tụ tập**: đứng thành nhóm quanh vành đảo, ngồi trên mép bệ đảo, chụp ảnh trước tượng, ngồi ghế nhựa ăn ở vành ngoài — đảo là một "phòng khách ngoài trời" (ảnh 28, 32) |
| Phông xung quanh | Nhà + khách sạn xám trắng | **Bức tường sáng**: cửa sổ khách sạn sáng đèn + biển neon (Thanh Bình Hotel xanh dương — ảnh 28; SANDALS FLORA vàng — ảnh 29) + dãy sạp LED trắng dưới chân thang; bầu trời gần như đen, mọi sáng đều từ mặt đất |
| Không khí | Nắng, bóng cứng | Sương nhẹ + quầng quanh đèn sodium/LED; mặt đường phản sáng nhẹ |

### 3.2 Đặt cạnh render góc A hiện tại (`v52-A-bung-binh-dem.png`) — từng điểm chưa giống

Đã soi trực tiếp render v52-A (máy trong đảo nhìn về mặt tiền) cạnh ảnh 28/32/39:

| # | Điểm | THẬT (đêm) | RENDER v52-A | Chưa giống ở đâu |
|---|---|---|---|---|
| 1 | Tượng đài | Rọi sáng trắng từ chân bệ, là điểm sáng thứ cấp của khung | Tượng **màu be trơn, không được rọi** — chỉ có viền đèn chân nhỏ (uplight v4.4); thân tượng tối ngang nền trời, **chìm sau mặt tiền sáng** | Thiếu spotlight hắt thân tượng + quầng sáng chân bệ; vật liệu nên ngả **đá xám lạnh** thay vì be ấm |
| 2 | Thảm hoa đảo | Bề mặt họa tiết liền (từ trên cao) / vành đèn nấm đọc rõ (mặt đất) | Bụi cẩm tú cầu rời rạc từng cụm hồng/xanh trên đĩa cỏ — v5.0 đã nâng đúng cao độ nhưng vẫn là **chấm rời**, không thành thảm/viền | Cần thảm hoa dạng vành + họa tiết (canvas texture trên đĩa đảo hoặc instanced dày theo vòng), không phải bụi thưa |
| 3 | Người trên/quanh đảo | Nhóm đứng chụp ảnh trước tượng, người ngồi kín vành, đảo là nơi tụ tập | Đảo gần như **trống người**: 3 người ngồi vành nam + cụm ăn tây-bắc; tiền cảnh khung A là các NPC đứng NGOÀI đảo quay lưng | Thiếu: 2–3 nhóm đứng trước tượng (có người giơ điện thoại), thêm người ngồi vành đông + vành tây |
| 4 | Tiền cảnh khung | Xe máy đậu thành hàng + người qua lại ngay trước mắt | **Nửa dưới khung là mặt sân trống**; chỉ 2 xe máy lẻ phía nam (ngoài khung A này) | Hàng xe đậu dài phải vào được khung từ thang/đường vào (phía tây đảo) |
| 5 | Vành xe chạy | Vệt sáng + xe qua lại liên tục quanh đảo | Có hệ xe chạy vòng trong code, nhưng **khung tĩnh v52-A không có chiếc xe nào** và vành đường quanh đảo đọc như sân trống | Tăng mật độ xe vòng đảo + đèn pha/trắng đỏ rõ hơn để khung nào cũng bắt được xe |
| 6 | Phông hai bên khung | Khách sạn sáng đèn + neon tạo tường sáng bao quanh | Ngoài mặt tiền (sáng đạt), hai bên khung là **sườn đồi hoa chấm + khối tối**; biển khách sạn/neon quanh bùng binh chưa có | Thêm 2–3 biển neon khách sạn (Thanh Bình xanh, Sandals vàng) ở phông đông/bắc + cửa sổ sáng |
| 7 | Bầu trời / không khí | Trời gần đen, quầng đèn, sương mềm phông | Trời tím sao + **trăng to sau mái chợ** chiếm chú ý; sương quanh đảo mỏng | Trăng đang "trộm khung" — thu nhỏ/mờ trăng ở góc A; tăng quầng sáng quanh đèn đảo |
| 8 | NPC tiền cảnh | Người thật che khung một phần là chuyện thường (đầu/vai) | 2 NPC sát máy bên trái **đứng trên mép sườn cỏ, đọc như dán lên nền** (chân không bám đất rõ) | Kiểm lại cao độ đặt NPC ở vành tây đảo/sườn (groundH tại mép thảm) |

### 3.3 Đặc tả sửa theo khung hình (cho đợt dựng sau)

1. **Rọi tượng**: thêm 2 SpotLight ấm-trắng từ chân bệ hắt lên thân tượng (hoặc vật liệu tượng emissive nhẹ 0,15 + đĩa halo sáng r=3,5 dưới chân, cùng hệ glowDisc đã có) + đổi tông tượng sang xám lạnh 0x9aa0a4. Mục tiêu: trong khung A tượng phải là mảng sáng thứ 2 sau mặt tiền.
2. **Thảm hoa thành họa tiết**: phủ đĩa đảo bằng vòng hoa instanced DÀY 2–3 lớp (vành ngoài hoa đỏ/hồng, vành trong cẩm tú cầu) + giữ đèn nấm vành giữa; từ góc B (đỉnh thang) phải thấy đảo là một đĩa hoa có viền, không phải cỏ điểm hoa.
3. **Người trên đảo**: +2 nhóm đứng (3–4 người) trước tượng phía nam (1 người giơ điện thoại — part box mỏng), +4 người ngồi vành (đông + tây), +1 cụm gia đình có trẻ em. Tất cả quay mặt về tượng/về phố như ảnh 28/32.
4. **Hàng xe đậu phía tây đảo**: dãy 10–14 xe máy đậu xiên dọc lề tây (phía nhìn từ thang xuống thấy ngay), giữ 2 xe tiền cảnh nam hiện tại.
5. **Phông neon**: biển "Thanh Bình" xanh dương + 1 biển vàng ở khối khách sạn phía đông-bắc đảo, cửa sổ sáng 30–40% — chỉ cần plane emissive + canvas chữ như hệ signMesh sẵn có.
6. **Trăng**: giảm kích thước/quầng ở hướng nhìn mặt tiền hoặc dời khỏi trục khung A.

---

## 4. KẾT LUẬN — 5 THIẾU HỤT LỚN NHẤT THEO MẮT CHUNG HY

1. **Đám đông một phom, một lớp, một chiều cao.** NPC hiện tại = 1 thân người mặc áo len ôm đổi 14 màu, mũ len luôn trùng màu áo, quần wanderer 100% một màu, không scale, không tông da, không trẻ em. Ảnh/video đêm thật cho thấy đám đông đọc bằng **4 phom (phao phồng ~30% / dạ dài / hoodie / len) + mũ khác màu áo + khăn + túi** — game thiếu đúng lớp PHOM, và bảng màu crowd lại **thiếu hai màu áp đảo nhất của đám đông thật: trắng kem (phao) và đen**. → Sửa bằng bảng phân bổ mục 1.3, toàn bộ từ kho sẵn có (part A2, P1, P2, P9, K3 + scale phom), 0 GLB mới.

2. **Tay người đi chợ trống 100%, bàn ăn gần như trống.** Vật phẩm ăn uống "chưa có" là đúng ở lớp NGƯỜI: ly giấy có ống hút (~10% người thật) và túi nilon căng đồ (~30%) — hai vật phẩm nhận diện mạnh nhất của chợ đêm — chưa xuất hiện trên bất kỳ NPC nào; bàn ăn chỉ có 1 ly trụ mini vô hình thay vì bộ 2 ly + tô/đĩa như ảnh 38. Các part T1/T4/T6 đã có sẵn nhưng đang bị "giam" trong tủ đồ của riêng người chơi. → Ưu tiên 1+2 ở mục 2.3.

3. **Sạp ăn ngoài nhóm 6 hero gần như không có hàng đặc trưng — nặng nhất là sạp XIÊN.** Hình ảnh đặc trưng nhất của chợ đêm trong tư liệu mới (ảnh 31) là khay xiên trăm chiếc xếp tầng; sạp xien trong game không thuộc 6 sạp hero nên chỉ có hàng trang trí rời. Tương tự: vỉ bắp/khoai, dãy cốc chè, tháp yaourt đều chưa có khối hàng riêng. → Ưu tiên 3 ở mục 2.3 (khay xiên làm trước).

4. **Tượng đài không được rọi sáng + thảm hoa đảo không thành thảm.** Bùng binh đêm thật có trung tâm là tượng TRẮNG SÁNG trên đĩa hoa họa tiết có vành đèn; game là tượng be tối trên đĩa cỏ điểm bụi hoa rời — đảo mất vai trò điểm nhấn, đúng như Chung Hy nói "bùng binh không giống". → Đặc tả mục 3.3 điểm 1+2.

5. **Vành đảo vẫn thiếu người và thiếu "biển xe".** Đêm thật: người tụ kín vành đảo + hàng xe máy đậu dài + xe chạy vòng tạo vệt sáng — đảo là nơi đông nhất nhì khung hình. Game: đảo thưa người, hàng xe đậu chưa vào được các khung chính (A từ đảo, B từ đỉnh thang), nửa dưới khung A vẫn là mặt sân trống. → Đặc tả mục 3.3 điểm 3+4.

**Một câu tổng kết:** v5.0 đã sửa được KHUNG (đường rộng, mặt tiền sống, trời có nội dung) — đợt này tư liệu đêm cho thấy phần còn thiếu nằm ở LỚP NGƯỜI và LỚP VẬT PHẨM CẦM TAY/BÀN ĂN cùng ĐIỂM NHẤN TƯỢNG ĐÀI: đều là việc phân bổ + gắn part sẵn có + rọi sáng, không cần model mới — và cả 3 bảng đối chiếu trên đã ghi rõ món nào, tỉ lệ bao nhiêu, đặt ở đâu.
