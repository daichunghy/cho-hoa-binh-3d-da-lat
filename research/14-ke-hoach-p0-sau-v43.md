# KẾ HOẠCH P0 SAU V4.3 — Chợ Hòa Bình Online

Lập 07/11/2026 từ research/13 (Phần P0) đối chiếu trạng thái thật sau v4.3.
Nguyên tắc: chỉ triển khai sau khi Chung Hy chốt đợt; mọi model mới phải nén GLB (trần dung lượng ở mục 4).

## 1. Trạng thái từng mục P0 sau v4.3

| Mục | Sau v4.3 | Còn lại |
|---|---|---|
| P0-5 Palette khóa chuẩn | ✅ XONG ở v4.3 (bảng 14 màu, dải HSV, before/after A/B) | Chỉ rà soát định kỳ khi thêm nội dung mới |
| P0-2 EXP + cấp "Khách quen chợ" | ✅ XONG ở v4.3 (11 mốc cấp, XP mọi hành động, mở khóa cấp 3/4/5, danh hiệu trên thẻ tên) | Cân bằng lại số XP sau khi có P0-1/P0-3/P0-4 để các nguồn XP khớp nhau |
| P0-3 Sổ Đặc Sản trong Hộ chiếu | ⚠️ MỘT PHẦN: đã có mầm `eatenCount`, bộ sưu tập ảnh check-in và bảng thành tựu trong Hộ chiếu | Tab Sổ Đặc Sản riêng: ~45 món theo 5 khu, món đã ăn sáng lên, % hoàn thành từng khu, toast "+1 Sổ Đặc Sản" khi ăn món mới — effort S |
| P0-4 Quest ngày | ⚠️ MỘT PHẦN: v4.3 có pool 8 nhiệm vụ chọn 3/ngày (+40 Xu +30 XP) | Dồn tối đa 3 ngày (quest chưa xong không mất), quest sinh từ NPC tiểu thương có tên (Cô Lan...), thêm mẫu quest gắn tương tác mới (chụp ảnh khi lên đèn, tìm sạp giảm giá) — effort M |
| P0-1 Tủ đồ mặc được thật | ❌ CHƯA LÀM — thiếu hụt lớn nhất theo research/13 | Toàn bộ mục 2 dưới đây — effort M |

## 2. P0-1 Tủ đồ — thiết kế triển khai (làm đầu tiên ở đợt sau)

- **Ô trang bị (4):** Mũ / Khăn / Áo / Tay cầm. **8 món đầu:** lấy từ hàng đang bán ở khu Đồ len + lưu niệm (mũ len, khăn choàng, áo dạ, găng tay, túi vải...) — mua ở sạp = vào tủ, không chỉ vào Giỏ tiêu thụ.
- **Kỹ thuật:** tái dùng node mũ (beanie) và khăn (scarf) mà character.glb đã có cho NPC; áo = đổi màu/vật liệu thân + thêm chi tiết thêu đơn giản; tay cầm = gắn mesh nhỏ (ly, túi, lồng đèn) vào node tay. KHÔNG dựng character.glb mới nếu chưa cần — gắn/thay node bằng code như cách NPC đang biến thể.
- **Save:** thêm `state.wardrobe[]` (món đã sở hữu) + `state.equipped{mũ, khăn, áo, tay}` vào save `chohb3d-v1`, migration mặc định rỗng — không phá save cũ.
- **UI:** màn hình Tủ đồ mở từ nút cạnh Túi đồ: lưới món đã có, món đang mặc có viền, bấm Mặc/Gỡ; preview trực tiếp trên nhân vật (camera vẫn trong game).
- **Gameplay:** mỗi món mặc cộng Độ Ấm nhìn thấy được trên thanh Độ Ấm (mũ +8, khăn +10, áo +15...) — mặc đồ len thành quyết định chơi thật khi trời lạnh, nối thẳng hệ nhiệt độ sẵn có.
- **Mở khóa:** 2–3 món đặc biệt chỉ mở bằng cấp "Khách quen chợ" / thành tựu (nối P0-2 đã xong).

## 3. Thứ tự đợt sau (đề xuất)

1. P0-1 Tủ đồ (M) — thiếu hụt lớn nhất, mở khóa giá trị cho cả khu Đồ len đang bán nhưng không dùng được.
2. P0-3 Tab Sổ Đặc Sản (S) — rẻ, tăng động lực ăn đủ món.
3. P0-4 Quest ngày dồn 3 ngày + quest từ NPC (M).
4. Cân bằng lại kinh tế/XP tổng (S): giá, thưởng, nguồn XP sau khi 3 hệ trên vào.

## 4. Trần dung lượng — điều kiện cứng

- Standalone v4.3: 10.450.769 byte, chỉ còn dư ~35KB dưới trần 10MiB của link chia sẻ.
- Đợt sau bắt buộc **nén GLB** (Draco/meshopt hoặc giảm segment/merge geometry trong build_models.py) TRƯỚC khi thêm bất kỳ model nào; mục tiêu lấy lại ít nhất 1–1,5MB trống. Việc nén phải kiểm chứng bằng render so sánh (không vỡ hình/mất vật liệu) mới tính đạt.
- Nếu nén không đủ, phương án dự phòng: tách link chơi thử sang host khác (GitHub Pages của repo sẵn có) thay vì file standalone một cục.

## 5. Kiểm chứng bắt buộc cho đợt sau (như chuẩn đã chốt)

- node --check đạt; save cũ mở lên không lỗi (migration).
- Render đối chứng: nhân vật mặc từng lớp (mũ/khăn/áo) cận cảnh; tab Sổ Đặc Sản; quest ngày ở ngày 2 còn dồn.
- Báo cáo liệt kê thẳng mục chưa xong; điều phối tự soi ảnh trước khi báo Chung Hy.
