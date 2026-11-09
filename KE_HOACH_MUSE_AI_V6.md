# KẾ HOẠCH V6 CHO MUSE AI — "Cảm giác Đà Lạt" + "Chơi được"

> Tài liệu giao việc cho Muse AI. Đọc hết mục 0–2 trước khi sửa bất cứ thứ gì.
> Code: `prototype-v2/index.html` (một file, ~5000 dòng, three.js r160). Model: `prototype-v2/assets/*.glb`, sinh bởi `prototype-v2/scripts/build_models.py` (Blender).

## 0. Nguyên nhân các lần trước thất bại (đọc kỹ)

| # | Vấn đề | Hệ quả | Quy tắc mới |
|---|--------|--------|-------------|
| 1 | Muse "nhớ" hình thật bằng văn bản mơ hồ ("chợ đêm đông, đèn vàng") | Dựng theo mẫu chung, không giống Đà Lạt | Mỗi khu có **bảng đo đối chiếu ảnh thật** (mục 3). Không có số đo = không được dựng. |
| 2 | Model Blender thô: hộp khối, tam giác facet lớn, xám phẳng (xem `renders/real1-deviations.md`) | Cảnh trông "đồ chơi lỗi", không có hồn | Dùng **kit mô-đun + texture vẽ** thay vì mô hình hoá từng khối (mục 2). |
| 3 | Sửa nhiều thứ một lượt, không kiểm chứng | Lần trước đã dính **màn hình đen** (TDZ) | Làm **từng khu một**, sau mỗi khu chạy cổng kiểm (mục 6). |
| 4 | Ảnh tham khảo của game (AFKmobi) là ảnh minh hoạ AI, không phải Đà Lạt thật | Lệch phong cách | Chỉ lấy **bố cục sạp + UI**, màu/kiến trúc lấy từ ảnh thật (mục 1). |

## 1. Hướng nghệ thuật: Đà Lạt thật, không phải "chợ phương Tây ấm cúng"

Từ 2 ảnh người dùng gửi:

- **Ảnh B (chợ đêm thật, nhìn từ trên cao)** = chuẩn của *không gian*: hẻm hẹp ~4–6 m, hai bên **sạp treo quần áo len/jean thành dãy dài**, mái bạt xanh/ trắng/ đỏ lộp xộn, **chuỗi bóng đèn trắng-vàng** chạy dọc tạo đường dẫn mắt tới điểm sáng cuối hẻm, **dây điện chằng chịt**, nhà ống 4–5 tầng ven đường (ban công sắt, biển hiệu hộp vàng/đỏ như "TIỆM VÀNG"), nền nhựa đường xám đen ướt, người mặc áo khoác dày đủ màu (đỏ, cam, xanh jean).
- **Ảnh A (game AFKmobi)** = chuẩn của *UI & độ "chơi được"*: biển sạp gỗ lớn có giá ("SỮA ĐẬU NÀNH NÓNG 15K"), nút **Mua** to, NPC bán hàng có hoạt hình, hơi nước bốc, bảng nhiệm vụ bên phải, thanh công cụ dưới. **Không** copy: lồng đèn Trung Hoa, nền đá cuội, phong cách chibi cao bồi — Đà Lạt chợ đêm dùng bóng đèn trần + bạt, không phải lồng đèn.

Bảng màu (khoá cứng): nền đường `#3a3d40`→`#5a5e62` có vệt ướt; đèn sạp `#fff1c9` (3200K) + quầng; mái bạt xanh `#2f7fa8`, đỏ `#b8322a`, trắng ngà; áo len: đỏ, cam, xanh jean, be; sương: xanh lạnh `#9fb4c4` mật độ nhẹ ở xa (không che sạp).

## 2. Cách làm model (thay cho cách cũ)

Blender không nên dựng "cả khu". Chỉ dựng **bộ kit nhỏ, tái dùng, có bevel + texture**:

1. **Kit sạp (6 mẫu)**: sạp treo áo, sạp đồ ăn có bếp, sạp nước có nồi, sạp rau/dâu, xe đẩy, quầy kính. Mỗi mẫu: khung ống thép, mái bạt có nếp (subdivide + noise), đèn bóng trần, 3 biến thể màu qua vertex-colour/ tint.
2. **Kit nhà ống (4 mẫu mặt tiền)**: tầng trệt cửa cuốn + biển; tầng 2–5 ban công sắt, cửa sổ, điều hoà, bình nước nóng, dây điện. Texture mặt tiền vẽ trong canvas/Blender, **không** để tường be trơn.
3. **Prop nhỏ** (đây là thứ tạo cảm giác "sống"): ghế nhựa thấp, thùng xốp, rổ nhựa, nồi sữa to + ly thuỷ tinh, bình trà, xe máy, cột điện + bó dây, thùng rác, cây thông.
4. Quy tắc chất lượng model: không mặt phẳng lớn > 8% khung hình; mọi cạnh có bevel; mỗi bề mặt lớn có texture/noise; poly budget mỗi sạp ≤ 3k tri; xuất GLB, kiểm bằng `scripts/dump_glb_general.mjs`.
5. Nếu Blender tiếp tục làm xấu: **ưu tiên dựng trực tiếp bằng three.js** (hộp + texture canvas + prop) cho phần nền/mặt tiền, giữ Blender chỉ cho nhân vật/xe/tượng.

## 3. Lộ trình theo đúng thứ tự người chơi sẽ đi

Thứ tự khu (người dùng yêu cầu): **① Tuyến đường chợ → ② Cầu thang → ③ Khu Hòa Bình → ④ Sữa đậu nành Tăng Bạt Hổ → ⑤ Hồng trà Hòa Bình.**
Mỗi khu làm xong + qua cổng kiểm mới sang khu sau. Mỗi khu gồm 3 phần: *Cảnh*, *Chơi*, *Đối chiếu*.

### ① Tuyến đường chợ (đường vào, ban đêm)
- **Cảnh**: trục hẹp 4–6 m, 2 hàng sạp sát nhau, mái bạt **chồng lấn không đều**; nhà ống cao 4–5 tầng 2 bên che trời → trời chỉ còn dải hẹp; chuỗi bóng đèn kéo dọc 2 phía + dây điện ngang đường (cứ ~8 m một bó); nền nhựa xám đen + vệt ướt; quần áo treo dày ở sạp (màu đỏ/cam/xanh jean); điểm sáng rực cuối hẻm (hội tụ phối cảnh); xe máy đậu sát lề; người dày ở giữa, xe máy lách chậm.
- **Chơi**: đi bộ thấy **một mục tiêu sáng** ở cuối hẻm; đi ngang sạp có "gọi mời" (bubble) + hỏi giá nhanh; mua áo len → mặc được (ăn khớp tủ đồ có sẵn).
- **Đối chiếu**: so 1 ảnh render góc nhìn từ cao ~15 m với ảnh B: cùng bố cục dọc, mật độ đèn, ≥ 3 màu mái bạt, dây điện thấy rõ.

### ② Cầu thang chợ
- **Cảnh**: cầu thang bê tông rộng, tay vịn sắt, bậc rộng 0,3–0,35 m, **người ngồi ăn trên bậc** (ghế nhựa thấp), đèn bên cạnh, hàng quán hai bên chân thang, sương nhẹ ở đỉnh.
- **Chơi**: leo thang có tiếng bước chân, camera nâng nhẹ; ở giữa thang có chú Ba coi bói (đã có); đỉnh thang "mở" ra quảng trường (đóng dấu hộ chiếu).
- **Đối chiếu**: độ dốc, số bậc (~40–60), chiều rộng thang so với chiều rộng người (1 : 8 người đứng ngang).

### ③ Khu Hòa Bình (quảng trường – rạp – bùng binh)
- **Cảnh**: mặt rạp Hòa Bình, tượng đài/bùng binh với thảm hoa, ghế đá, đèn cam sodium, xe máy quanh vòng, biển hiệu đỏ.
- **Chơi**: nhiệm vụ chụp ảnh (đã có `📸`), nghe hát ở góc hát, mua dâu/ hoa.
- **Đối chiếu**: tỉ lệ rạp so với bùng binh; số cửa; màu mặt tiền theo ảnh thật.

### ④ Sữa đậu nành Tăng Bạt Hổ (quán Hoa Sữa — `id:'hoasua'`, x −128, z 19.5)
- **Cảnh**: nồi sữa nhôm rất to bốc hơi, tủ kính bánh tiêu/ sừng trâu, ly thuỷ tinh, ghế nhựa thấp ngồi sát vỉa hè, biển quán đỏ chữ trắng; người ngồi uống tay ôm ly (có sẵn nhóm ngồi).
- **Chơi**: gọi món → NPC múc sữa (animation rót) → hơi nước → **buff ấm** (đã có). Thêm: "ăn bánh chấm sữa" tăng buff.
- **Đối chiếu**: đối chiếu số bàn ghế, kích thước nồi so với người bán (≈ ngang thắt lưng).

### ⑤ Hồng trà Hòa Bình (`id:'hongtra'`, đã thêm ở bản này — x 17, z 11)
- **Cảnh**: quầy nhỏ, bình đun trà lớn bốc hơi, dãy ly nhựa/ly thuỷ tinh, thùng trà đen, bảng menu viết tay "Hồng trà nóng 12K / Hồng trà sữa 15K / Hồng trà đào 18K".
- **Chơi**: 3 món (đã có trong code); thêm hoạt cảnh pha trà ~3 giây, biển menu bấm xem được.
- ⚠️ **Cần người dùng xác nhận**: địa chỉ/diện mạo thật của quán "Hồng trà Hòa Bình" (ảnh mặt tiền) — hiện chỉ là mẫu quầy trà chung vì chưa có ảnh tham khảo. Gửi ảnh để Muse dựng đúng.

## 4. Biến game thành "chơi được" (không chỉ đi xem)

Vòng chơi 10 phút, theo thứ tự ①→⑤ (thay vì hướng dẫn hiện tại sữa → thang):
1. Vào đầu tuyến chợ đêm: nhiệm vụ "Đi hết hẻm chợ, ngắm 3 sạp len" (+Xu).
2. Leo cầu thang → dấu hộ chiếu 1.
3. Quảng trường Hòa Bình: chụp ảnh check-in → dấu 2.
4. Uống sữa đậu nành Tăng Bạt Hổ → buff ấm → dấu 3.
5. Mua hồng trà → hoàn tất "Ấm bụng" → thẻ tổng kết "Hôm nay bạn đã ăn gì ở Đà Lạt".
- Có **thanh nhiệt độ lạnh** (đã có) làm áp lực nhẹ: lạnh quá → đi chậm; đồ nóng/áo len giải quyết.
- UI theo ảnh A: biển giá lớn trên sạp, nút Mua nổi, panel nhiệm vụ phải (đã có panel 🧭 — chỉ cần đổi sang 5 bước trên).

## 5. Việc cần làm cụ thể (checklist cho Muse)

- [ ] Sửa `TUT_STEPS` (index.html, ~dòng 5918) theo 5 bước mục 4.
- [ ] Dựng kit sạp/ nhà ống mới (mục 2), thay dần trong khu ① trước.
- [ ] Thêm dây điện + chuỗi đèn ngang đường khu ①.
- [ ] Khu ②–⑤ lần lượt như mục 3.
- [ ] Mỗi khu: 1 render đối chiếu cạnh ảnh thật, ghi vào `prototype-v2/renders/v6-<khu>.md` (số đo, không viết cảm tính).

## 6. Cổng kiểm bắt buộc sau MỖI khu

```bash
# three r160 đã cài ở /tmp/diag/node_modules (npm i three@0.160.0 tại /tmp/diag)
cd prototype-v2
DIAG_NODE_MODULES=/tmp/diag/node_modules node scripts/diag_runtime.mjs 90   # phải: "ANIMATE ... SẠCH"
python3 scripts/package_standalone.py                                      # build index-standalone.html
```
Không qua cổng = không commit. Không sửa nhiều khu trong 1 lần.

## 7. Điều Muse phải dừng lại và hỏi người dùng
- Thiếu ảnh thật của khu/quán nào → hỏi, **không** bịa.
- Muốn thay đổi bố cục tổng (vị trí khu) → hỏi.
