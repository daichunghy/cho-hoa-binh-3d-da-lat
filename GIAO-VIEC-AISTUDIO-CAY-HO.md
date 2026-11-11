# GIAO VIỆC CHO AI STUDIO: Script Blender dựng 5 mẫu cây ven hồ Xuân Hương

Bạn viết **một file Python duy nhất** dùng Blender API (`bpy`) để dựng 5 mẫu cây 3D cho game web Three.js. Người nhận sẽ chạy file của bạn bằng Blender headless (`blender -b -P build_trees.py`), nên code phải chạy được từ đầu đến cuối không cần thao tác tay, không dùng add-on ngoài, không tải tài nguyên mạng.

## Đầu ra bắt buộc của script

- Tạo thư mục `./out/` và xuất 5 file: `tree_pine_umbrella.glb`, `tree_leaning.glb`, `tree_willow.glb`, `tree_jacaranda.glb`, `bush_bougainvillea.glb` (glTF Binary, apply modifiers, trục Y-up mặc định của exporter).
- Mỗi file ≤ 120 KB. Dùng ít đa giác (tán cây bằng khối cầu dẹt biến dạng/ngẫu nhiên hoá đỉnh nhẹ, KHÔNG particle/hair/metaball nặng).
- Chất liệu: material màu phẳng (Principled với Base Color đúng hex dưới đây, Roughness = 1) hoặc vertex color. **Không texture, không ảnh, không node phức tạp** (bản game đọc bằng GLTFLoader chuẩn).
- Gốc cây tại (0,0,0), cây đứng trên mặt phẳng z=0 của Blender.
- Cuối script in ra log: tên file, chiều cao đo được của cây, số mặt (tris).

## Thước đo khóa cứng

Nhân vật người trong game cao **1,82 đơn vị** (script dùng đơn vị mét của Blender = đơn vị game). Không tự đổi tỉ lệ.

## 5 cây phải dựng

**A. Thông tán ô** — thân thẳng nâu xám `#6b5847`; vệt quét vôi gốc cao 1,0, màu `#919798`; tán 2–3 tầng dẹt xếp lệch ở cao 8,5–12 (mỗi tầng = cầu dẹt tỉ lệ z ~0,18, mép lượn bằng cách ngẫu nhiên bán kính đỉnh ±12%), đường kính tán 6–8, lá `#29362a` pha mảng `#35482f`; tổng cao 11,5–12,5. **Tán không được là đĩa tròn đều.**

**B. Cây lá rộng nghiêng ra nước** — thân nghiêng ~35° về +X, phân 2–3 nhánh; tán xòe bất đối xứng theo hướng nghiêng, lá `#2f4429` pha `#43582f`; gốc vôi `#919798` cao 1,0; chiều cao đứng 7–9, tán vươn ngang ≥5.

**C. Liễu rủ** — thân 2,5–3,5; tán chính ở 4–5; cành rủ = nhiều dải cong (dùng curve hoặc chuỗi khối thuôn) dài 3–4 rủ xuống gần đất, lá `#5a7038` pha `#718c46`; tổng cao 5,5–6,5.

**D. Phượng tím** — thân 4–5 phân nhánh Y; tán rộng 6–7 ở cao 5,5–7, lá `#2c3f2a`; hoa tím `#7a5fa8`/`#8d74b8` thành mảng cục phủ ~35% mặt trên tán (dùng vật liệu riêng cho một số khối/mặt trên — không rải hạt đều).

**E. Bụi hoa giấy** — bụi nửa cầu lệch cao 1,2–1,8, lá `#3d5230`, hoa chùm mặt ngoài `#a83a6b`/`#bf4f83`.

## Phong cách

Chibi diorama: khối mềm, ít cạnh sắc, màu phẳng ấm. Cây phải đọc ra đúng loài ở khoảng cách xa (bóng silhouette): thông = thân cao + ô dẹt; cây B = nghiêng rõ; liễu = rủ rõ; phượng = tán rộng + tím; hoa giấy = bụi thấp + hồng tím.

## Tự kiểm trong code

Script tự `assert` chiều cao từng cây trong khoảng quy định (±10%) và dung lượng file ≤ 120 KB sau khi xuất; sai thì in cảnh báo rõ ràng ở log.
