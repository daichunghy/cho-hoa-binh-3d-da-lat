# 17 — ĐƯỜNG VÀO CHỢ ĐÀ LẠT: ĐỐI CHIẾU HÌNH ẢNH THẬT ↔ RENDER HIỆN TẠI

> Mục đích: tìm bằng MẮT vì sao đường vào trong game vẫn đọc "nhỏ/hẹp/chưa giống" dù đợt v4.7 đã đo tăng bề rộng đường 11 → 18.
> Phạm vi: đoạn BÙNG BINH → ĐƯỜNG TRƯỚC CHỢ (Nguyễn Thị Minh Khai) → MẶT TIỀN. Chỉ nghiên cứu, không sửa code/model.
> Render đối chiếu: `prototype-v2/renders/r17-doi-chieu-dem-dinh-thang.png` và `prototype-v2/renders/r17-doi-chieu-bung-binh-mat-tien.png` (render mới bằng harness v47, script tạm `/tmp/render_r17.py` — không đụng script gốc).

---

## 1. DANH MỤC TƯ LIỆU

### 1.1. Ảnh đã có trong dự án (theme/real-market/ + theme/reference/)

| File | Góc nhìn (đứng đâu / hướng nào / cao độ máy) | Dùng cho |
|---|---|---|
| `real-market/01-mat-tien-cho-ngay.jpg` | Mặt đất NGAY trong vòng xoay bùng binh, máy ~1,6 m, nhìn chếch đông–bắc về mặt tiền chợ; tượng đài tiền cảnh trái | **ẢNH CHUẨN NGÀY** |
| `real-market/27-bung-binh-dem-tu-dinh-thang.jpg` (mới bổ sung, nguồn web §1.2) | ĐỈNH cầu thang khu Hòa Bình, máy ~17–19 m trên mặt bùng binh, nhìn xuống đảo + sang trái là chợ, đối diện là dãy khách sạn | **ẢNH CHUẨN ĐÊM** |
| `real-market/05-bung-binh-dem-mat-dat.jpg` | Trên cầu thang (thấp hơn ảnh 27), nhìn xuống biển người + bãi xe quanh đảo; chợ ở trái khung, khách sạn đối diện | Bổ trợ đêm — cùng trục với ảnh 27 |
| `real-market/10-bac-thang-nhin-xuong-bung-binh.jpg` | Đỉnh thang, tiền cảnh là đám đông ĐANG TRÊN BẬC THANG; đảo + tượng giữa khung; chợ trái, LangFarm phải ngay đầu thang | Bổ trợ: tiền cảnh thang |
| `reference/ref-mat-tien-cho-dem.jpg` | Cùng góc đỉnh thang lúc chạng vạng (bản các đợt trước dùng làm chuẩn) | Bổ trợ |
| `real-market/04-bung-binh-dem-tren-cao.jpg` | Trên cao nhìn thẳng xuống đảo: thảm hoa họa tiết quanh tượng, vệt sáng xe vòng quanh | Bổ trợ: hình học đảo |
| `real-market/06-duong-cho-dem-tren-cao.jpg` | Trên cao (~tầng 3–4) nhìn DỌC trục Nguyễn Thị Minh Khai về phía tây (cuối trục là tháp Dalat Center + Hotel Colline); tường chợ lam trắng ở mép phải khung | Bổ trợ: phố hai bên đường |
| `real-market/07-duong-cho-ngay-tren-cao.jpg` | Trên cao nhìn dọc đoạn phố hông chợ: nhà 4–6 tầng hai bên, sạp chiếm lòng đường | Bổ trợ: tỉ lệ phố |
| `real-market/08, 09, 13` (bậc thang đêm) | Mặt đất/trên thang: người ngồi ăn trên bậc, sạp nướng trên chiếu nghỉ | Bổ trợ: thang là không gian sống |

### 1.2. Tư liệu web bổ sung đợt này

| Nguồn | Nội dung dùng được |
|---|---|
| vivuvietnam.net — ảnh `cho-dem-da-lat-1_1687963673.jpg` (đã lưu thành `real-market/27-...`, ghi vào SOURCES.md) | Ảnh chuẩn đêm (xem §2.2) |
| tinbds.com — trang đường Nguyễn Thị Minh Khai | SỐ ĐO CỨNG: đường dài ~400 m, **lòng đường rộng 10 m, vỉa hè rộng 3 m**; điểm đầu tại bùng binh chợ, chạy dọc chợ |
| phuotvivu.com / freshdalat.vn (bài chợ đêm) | Chợ đêm "bắt đầu từ bùng binh chợ Đà Lạt và trải dài dọc Nguyễn Thị Minh Khai"; **bùng binh là nơi gửi xe + tụ tập ăn uống** — tức mặt phẳng quanh đảo là không gian chợ, không phải đường xe chạy thuần túy |
| travel.com.vn (mục "Các lối vào chợ đêm") | 3 lối vào chính: (1) vòng xoay trên NTMK, (2) lối đi bộ từ quảng trường Hòa Bình, (3) **bậc thang trung tâm Hòa Bình xuống chợ** — trục thang → bùng binh là trục chính |
| Instagram @dalatstreetnhanlaca (reel 24/10/2026, mô tả qua kết quả tìm kiếm) | Video quay từ trên cao nhìn xuống cầu thang rộng: hàng trăm người trên bậc, L'ANGFARM bên hông — xác nhận góc chuẩn đêm là góc "quốc dân" của khu này |

Không dùng được: ảnh viettravelo CHO-DA-LAT.jpg (server trả rỗng), ảnh vinpearl cho-da-lat-13 (cận cảnh giỏ hoa, sai chủ đề) — không đưa vào kết luận.

---

## 2. HAI ẢNH CHUẨN — PHÂN TÍCH TỪNG ĐIỂM BẰNG MẮT

### 2.1. CHUẨN NGÀY — `01-mat-tien-cho-ngay.jpg` (từ bùng binh nhìn mặt tiền)

- **Vị trí máy:** đứng trong vòng xoay, sát đảo, cao ~1,6 m. Tượng đài nằm tiền cảnh trái, cách máy ước 8–12 m.
- **Bề rộng đường so với mặt tiền:** gần như KHÔNG có "đường" tách biệt trong khung — từ chân máy tới mặt tiền là một mặt lát liên tục (vòng xe + sân) ước 30–40 m chiều sâu. Mặt tiền chiếm **~75–80% bề ngang khung** và ~45% chiều cao khung. Tỉ lệ mặt tiền : khoảng mở trước nó ≈ tòa nhà áp đảo.
- **Hai bên:** trái khung là mép sườn dốc + mái thấp + cây (phía thang); phải khung là **khách sạn ~6 tầng đứng SÁT góc phố** (biển "SAN…" = một phần tên khách sạn). Không có dải đất trống nào giữa nhà và đường.
- **Vỉa hè:** không đọc được vỉa hè riêng — sân lát phẳng liền mạch từ đảo tới chân mặt tiền, người đi bộ tràn cả xuống lòng đường.
- **Mặt tiền đọc "lớn" nhờ:** (1) GẦN — lấp gần trọn khung; (2) LIỀN MẠCH 4–5 tầng không ngắt quãng; (3) các dải ngang chồng lớp đọc rõ từ xa: dải cửa sổ sẫm có chia ô → băng hồng đào → dải lam trắng → dải zigzag → **dải pano quảng cáo sặc sỡ ở tầng trệt**; (4) chữ CHỢ ĐÀ LẠT đỏ nằm giữa, trên cao, không bị che; (5) chân tường SỐNG: cửa hiệu mở, người + xe máy + ô tô ép sát.
- **Người/xe:** xe máy chạy vòng quanh đảo ngay tiền cảnh; người đứng/ngồi quanh đảo và dọc chân mặt tiền — mặt đất hầu như không còn mảng trống lớn.
- **Cầu thang + cầu nổi từ góc này:** cầu thang KHÔNG lọt khung (ở sau lưng/trái máy); cầu nổi KHÔNG thấy. Hai yếu tố "đặc sản" của game gần như vô hình ở góc nhìn quốc dân này.

### 2.2. CHUẨN ĐÊM — `27-bung-binh-dem-tu-dinh-thang.jpg` (từ đỉnh thang nhìn xuống)

- **Vị trí máy:** đầu cầu thang phía Hòa Bình, cao ~17–19 m so với mặt bùng binh. Tiền cảnh dưới khung: mép đầu thang lát gạch + dãy ô tô đậu dọc sườn trái (đường dốc bên hông thang); quán kính sáng đèn (dạng LangFarm) NGAY bên phải đầu thang.
- **Bố cục khung:** trời chỉ chiếm ~25% phía trên. Đảo bùng binh tròn nằm giữa khung (chiếm ~30% bề ngang khung), thảm hoa trên đảo thành **họa tiết vòng tròn đỏ–xanh đọc rõ từ xa**, tượng ở tâm đảo.
- **Chợ ở đâu:** BÊN TRÁI khung — chỉ thấy góc khối chợ: mép mái viền neon + chữ CHỢ ĐÀ LẠT vàng trên mép mái + dải pano Ferroli + sạp sáng đèn tràn ra chân. Mặt tiền KHÔNG đối diện thẳng máy; nó nằm chếch trái.
- **Đối diện đảo (phía xa khung):** một BỨC TƯỜNG ĐÔ THỊ: Thanh Bình Hotel trắng 5 tầng (biển xanh) + khách sạn trắng 7–8 tầng cửa vòm ngay sau + tháp tối đang xây. Đây là "phông" khép kín cái sân.
- **Mặt đất:** vòng xe quanh đảo thành vệt sáng; phần sân còn lại bị phủ bởi sạp + người + xe đậu — mảng trống gần như bằng 0.
- **Cảm giác tổng thể:** một "cái bát" đô thị khép kín, mọi phía đều có tường sáng đèn, tâm là đảo hoa + tượng.

---

## 3. MÔ PHỎNG CÙNG GÓC BẰNG HARNESS RENDER

Phương pháp: dùng nguyên harness `scripts/render_v47.py` (bản sao tạm ở /tmp, trỏ output ra /tmp — không sửa bản gốc), thêm 2 máy:

| Render | Máy (tọa độ Blender = three x, −three z, cao) | Đích nhìn | Lens | Ảnh thật tương ứng |
|---|---|---|---|---|
| `r17-bungbinh-len-mat-tien` | (−38, 14, 2,0) — mặt đất phía tây–nam đảo | (0, −12, 5) — mặt tiền | 24 mm | Ảnh chuẩn NGÀY 01 (cùng vị trí/hướng; chỉ khác ngày/đêm) — **khớp góc tốt** |
| `r17-dinh-thang-xuong` | (2, 33, 20,5) — đỉnh thang phía Hòa Bình | (−24, 6, 1,5) — tâm đảo | 24 mm | Ảnh chuẩn ĐÊM 27/05/10 — **khớp hướng, khớp một phần khung** (xem giới hạn) |

**Giới hạn phải ghi rõ:**
1. Địa hình trong harness là HỘP MÔ PHỎNG (Plaza/Road/Hill/Slope), không phải 100% hình học web. Ở góc đỉnh thang, mặt sườn dốc mô phỏng (Slope) chiếm phần lớn khung phải và che mất đảo — trong bản web, sườn này là địa hình khác. Vì vậy góc đỉnh thang chỉ dùng để chấm các điểm KHÔNG phụ thuộc sườn mô phỏng (vị trí chợ/trật tự trước–sau/mật độ/trời trống phía xa); kết luận về khung phải của góc này dựa trên ảnh render v47-a/b sẵn có + code vị trí.
2. Grade màu/ánh sáng của harness (Cycles + phơi sáng riêng) khác bản web (đã ghi nhận từ v4.5) → đối chiếu ở đây là BỐ CỤC / TỈ LỆ / MẬT ĐỘ / NỘI DUNG KHUNG, không chấm độ sáng.
3. Lens 24 mm ≈ ống rộng điện thoại của ảnh thật; các ảnh nghiệm thu cũ của game dùng lens 42–44 mm (hẹp hơn nhiều) — bản thân việc đổi lens đã cho thấy một phần "nhỏ" là do khung chụp hẹp, nhưng các khác biệt ở §4 vẫn còn nguyên khi đã cùng lens 24.

---

## 4. BẢNG ĐỐI CHIẾU TỪNG ĐIỂM

| # | Điểm | Ảnh thật | Render game hiện tại (cùng góc) | Khác ở đâu |
|---|---|---|---|---|
| 1 | Vị trí đảo so với trục thang | Đảo nằm gần như NGAY trước chân thang, hơi chếch tây; từ đỉnh thang nhìn xuống đảo ở giữa khung | Đảo đặt lệch hẳn sang tây (three x=−24 trong khi trục thang x=0); từ đỉnh thang đảo trượt khỏi tâm khung | Trục thang → đảo → mặt tiền ngoài thật là MỘT trục thị giác liền; trong game là hai trục chéo nhau |
| 2 | Khoảng đảo → mặt tiền | Ước 30–40 m mặt lát LIỀN, có vòng xe + sân chung, người tràn khắp | ~16 u từ tâm đảo tới dãy sạp mặt tiền nhưng ở giữa là sân be trống phẳng, không vòng xe đọc được, không viền | Số đo không nhỏ hơn thật nhiều — cảm giác xa/trống do mặt sân không có cấu trúc (không vành xe, không vỉa, không hoa văn lát) |
| 3 | Tầng trệt mặt tiền | Dải pano quảng cáo nhiều màu LIÊN TỤC + cửa hiệu MỞ + mái hiên + người/xe ép sát chân tường | Cửa cuốn XÁM ĐÓNG thành dãy + vài đốm sáng nhỏ; phía trước là dãy sạp rời | Đây là khác biệt lớn nhất ở tầm mắt người: chân chợ thật "sống và to", chân chợ game "đóng và chết" |
| 4 | Thân mặt tiền | 5 lớp dải ngang có họa tiết chia ô (cửa sổ sẫm, băng hồng, lam, zigzag) đọc rõ từ 40 m | Tầng trên là các TẤM TRẮNG PHẲNG PHÁT SÁNG không chia ô + một băng be trơn; zigzag có nhưng mảnh và chìm | Mặt tiền game đọc như phông sáng phẳng, mất "kết cấu kiến trúc" tạo cảm giác bề thế |
| 5 | Chữ CHỢ ĐÀ LẠT | Giữa khung, trên cao, không bị che (ngày); mép mái viền neon (đêm) | Bị tượng đài che mất chữ đầu ("…Ợ ĐÀ LẠT") ở góc bùng binh; ở góc đỉnh thang chữ nằm ngoài khung | Điểm nhận diện mạnh nhất bị khuất đúng ở góc nhìn chính |
| 6 | Đảo + tượng đài | Đảo Ø ước 35–40 m; thảm hoa HỌA TIẾT vòng tròn đỏ/xanh tương phản mạnh; tượng là NHÓM TƯỢNG ĐIÊU KHẮC cao ~8–10 m trên bệ đá xẻ nhiều mặt; quanh đảo có ghế, đèn, người ngồi | Đảo là ĐĨA XANH MỎNG, hoa là chấm li ti không thành họa tiết; tượng = bệ hộp xếp 3 tầng trơn + cụm khối đơn giản | Mất điểm neo tỉ lệ ở giữa sân: mắt không còn mốc "to" để suy ra sân rộng |
| 7 | Phía đối diện đảo (phông xa) | Tường khách sạn 5–8 tầng sáng đèn khép kín (Thanh Bình + nhà trắng cao + tháp) | Khoảng tối trống: phía tây là đường vào + nhà phố ~2 tầng lùi xa; phía bắc là sườn đồi trơn | Cái "bát đô thị" hở đáy → không gian rò ra ngoài, sân đọc như bãi đất trống ngoại ô |
| 8 | Hai bên đường vào (trục NTMK) | Nhà 4–6 tầng đứng SÁT vỉa hè 3 m, biển hiệu dọc, tạo hẻm phố (canyon) — ảnh 06 | Nhà phố cao ~6 u (≈2 tầng), LÙI 6–8 u khỏi mép đường với dải đất trống ở giữa; vài căn rời nhau | Đường thực tế lòng 10 m mà đọc "phố lớn" nhờ tường cao sát mép; game lòng 18 mà đọc "đường nội bộ khu đất trống" |
| 9 | Cầu nổi + trụ cầu | Hầu như KHÔNG lọt khung ở cả 2 góc chuẩn (nằm phía đông, khuất sau khối chợ) | Dải cầu cắt ngang phần trên khung ở góc đường vào (v47-a); trụ + khối trắng lớn đứng giữa khung nhìn về chợ | Một vật lạ chiếm khung ở đúng trục nhìn chính, phá cảm giác quảng trường |
| 10 | Phủ bề mặt (người/xe/sạp) | Trong khung chuẩn: hàng trăm người + thảm xe máy quanh đảo/trước mặt tiền; mặt đất trống <15% khung | Render harness đặt 264 người TOÀN MAP nhưng trong khung chuẩn chỉ lác đác ~10–20 hình; xe vòng đảo thưa; mảng sân trống ≈45–60% khung | "Đông" phải tính TRONG KHUNG HÌNH, không tính tổng map |
| 11 | Tiền cảnh đỉnh thang | Bậc thang + người phủ kín bề ngang dưới khung ("thác người"), quán sát bậc bên phải | Tiền cảnh là mặt sườn dốc trơn (harness) / trong web là hai sườn ít nội dung; quán LangFarm tương đương không có ở đầu thang | Mất tiền cảnh sống ở góc nhìn đẹp nhất của khu |
| 12 | Trời/khung trên | Trời chỉ ~25% khung (đêm) vì nhà cao bao quanh | Khung trên trống nhiều: phía xa không nhà cao, trời/hậu cảnh chiếm tỉ lệ lớn | Tỉ lệ trời cao = cảm giác ngoại ô, ít "trung tâm thành phố" |

---

## 5. KẾT LUẬN — VÌ SAO ĐO TĂNG MÀ NHÌN VẪN "NHỎ/HẸP"

Đợt v4.7 tăng bề rộng LÒNG ĐƯỜNG (11 → 18) ở trục tây. Nhưng con mắt không đo mét — nó đo **tỉ lệ trong khung hình và mức lấp đầy**. Năm nguyên nhân thị giác, xếp theo mức ảnh hưởng:

1. **Sai chỗ cần rộng.** Nơi người chơi/người xem thật sự cảm nhận "rộng" là MẶT SÂN QUANH ĐẢO + TRƯỚC MẶT TIỀN (ảnh chuẩn cho thấy đó là một quảng trường liền, bùng binh là bãi xe/tụ tập). Trong game, mặt sân này không thay đổi: vẫn phẳng, trống, không vành xe, không họa tiết lát, đảo thì nhỏ. Phần được nới (lòng đường trục tây) lại là phần ít quyết định cảm giác nhất.
2. **Tường hai bên thấp + lùi xa.** "Rộng" của phố thật đến từ nghịch lý: lòng đường chỉ 10 m nhưng nhà 4–6 tầng đứng SÁT mép → tỉ lệ bề ngang : chiều cao tường ≈ 16 : 15–20 → đọc như phố lớn. Game: lòng 18, nhà ~2 tầng, lại lùi thêm 6–8 u đất trống mỗi bên → tỉ lệ thành ~32 : 6 → đọc như đường trong khu đất trống. Nới đường mà không dựng tường sát mép thì càng nới càng trống.
3. **Điểm đích yếu.** Cuối trục nhìn là mặt tiền có tầng trệt ĐÓNG (cửa cuốn xám) và thân là tấm sáng phẳng. Mắt không có đích "to và sống" để đối chiếu, nên toàn trục bị đánh giá thấp. Ngoài thật, dải pano + cửa hiệu mở + chữ đỏ là nam châm thị giác kéo cả khung.
4. **Cái bát bị hở.** Thiếu bức tường khách sạn cao đối diện đảo và hai bên đầu thang → ánh mắt "rò" ra vùng trống/tối ở phông xa, không gian mất độ khép kín của trung tâm.
5. **Mật độ trong khung thấp.** Tổng người toàn map (~264–300) nghe lớn, nhưng chia cho cả map thì trong khung chuẩn chỉ còn ~10–20 hình người và mảng trống chiếm nửa khung. Ảnh thật: riêng trong khung là hàng trăm người + thảm xe. Cảm giác "chợ lớn" = mật độ phủ bề mặt, không phải tổng số NPC.

Nói ngắn: **v4.7 nới đúng con số nhưng sai đại lượng** — đại lượng cần nới là đảo + sân + tường bao + tầng trệt sống + mật độ trong khung.

---

## 6. ĐẶC TẢ SỬA THEO HÌNH ẢNH (mô tả bằng khung hình nghiệm thu)

Nghiệm thu bằng 2 khung chuẩn: (A) mặt đất trong đảo nhìn mặt tiền (như ảnh 01); (B) đỉnh thang nhìn xuống đảo (như ảnh 27). Mỗi mục dưới đây phải NHÌN THẤY được trong khung:

1. **Khung A:** mặt tiền chiếm ≥70% bề ngang khung; tầng trệt là một DẢI LIỀN gồm pano nhiều màu + cửa hiệu mở sáng + mái hiên, chạy không ngắt qua toàn bộ bề ngang mặt tiền; không còn ô cửa cuốn xám nào trong khung.
2. **Khung A:** chữ CHỢ ĐÀ LẠT nằm trọn, ở khoảng 1/3 trên của khung, không bị tượng che ở bất kỳ vị trí đứng nào trong đảo.
3. **Khung A + B:** đảo to tới mức ở khung B nó chiếm ~1/3 bề ngang khung; thảm hoa trên đảo thành HỌA TIẾT hình học (vòng tròn/cánh hoa đỏ–xanh tương phản) đọc rõ từ đỉnh thang; tượng là nhóm tượng có hình người cao, đứng trên bệ đá xẻ — ở khung A tượng cao ~1/5 chiều cao khung.
4. **Khung B:** phía xa đối diện đảo là một BỨC TƯỜNG khách sạn 5–8 tầng sáng cửa sổ, đứng sát mép sân — không còn khoảng tối trống ở phông xa; hai bên đầu thang có khối quán sáng đèn ôm sát bậc (như LangFarm trong ảnh 27).
5. **Khung đường vào (dọc NTMK):** hai dãy nhà 4–6 tầng đứng SÁT mép vỉa hè, biển dọc phát sáng; từ giữa đường nhìn dọc, hai tường nhà chiếm 2/3 chiều cao khung hai bên và hút về điểm mờ ở cuối trục (như ảnh 06) — không còn dải đất trống giữa nhà và đường.
6. **Mọi khung chính:** cầu nổi không cắt ngang phần trên khung; từ bùng binh và đỉnh thang, cầu chỉ được phép xuất hiện một phần nhỏ ở rìa đông hoặc khuất sau khối chợ.
7. **Mọi khung chính:** mặt đất trống <20% khung: vành xe máy đậu + xe chạy quanh đảo, cụm người dày ở chân thang/trước dãy sạp/trên đảo; ở khung B, tiền cảnh dưới là bậc thang phủ người liên tục xuống tới đảo.
8. **Khung B:** bậc thang đọc như một dải rộng phủ kín bề ngang tiền cảnh (không phải khe giữa hai sườn trơn); hai sườn thang có sạp/quán/ghế ngồi ôm sát từng đoạn.

---

## 7. FILE ĐỐI CHIẾU

- `prototype-v2/renders/r17-doi-chieu-bung-binh-mat-tien.png` — trái: ảnh thật 01 (ngày, từ bùng binh) · phải: render game cùng góc, lens 24. **Khớp góc: ĐẠT** (cùng vị trí mặt đất trong đảo, cùng hướng, tượng tiền cảnh + mặt tiền sau — bố cục hai khung tương ứng 1–1).
- `prototype-v2/renders/r17-doi-chieu-dem-dinh-thang.png` — trái: ảnh thật 27 (đêm, từ đỉnh thang) · phải: render game cùng hướng từ đỉnh thang, lens 24. **Khớp góc: GẦN ĐÚNG** — đúng cao độ/đúng hướng nhìn xuống đảo, nhưng khung render bị sườn dốc MÔ PHỎNG của harness chắn phần phải (giới hạn đã ghi ở §3); các điểm đối chiếu về chợ/đảo/phông xa vẫn đọc được ở phần khung còn lại và đã kiểm chéo với render v47-a/b.
