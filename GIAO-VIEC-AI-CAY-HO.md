# GIAO VIỆC: Bộ mẫu cây ven hồ Xuân Hương (Đà Lạt) cho game 3D

Bạn nhận việc dựng **một bộ mẫu cây 3D** cho game web 3D "Chợ Hòa Bình Online" (Three.js). Đây là việc độc lập: bạn chỉ giao FILE MẪU, không sửa code game. Mọi yêu cầu dưới đây là chuẩn nghiệm thu — làm sai chuẩn là bị trả về.

## 1. Phong cách & ràng buộc kỹ thuật (bắt buộc)

- Phong cách: **chibi diorama** — màu phẳng (flat vertex color, KHÔNG dùng texture ảnh), tông ấm, hình khối mềm ít cạnh. Nhìn phải hợp với một game mà nhân vật người cao 1,82 đơn vị (unit), đầu to tròn.
- Công cụ: Blender (bản nào cũng được), xuất **glTF binary (.glb)**, 1 file = 1 loại cây, gốc tọa độ tại chân cây, cây mọc theo trục +Y trong game (Blender xuất mặc định là được).
- Mỗi file GLB **≤ 120 KB** sau khi nén hình học (khuyến khích: ít đa giác, tán cây bằng các khối/cụm mặt phẳng cong nhẹ hoặc khối cầu dẹt biến dạng — không dùng particle/hair).
- Màu dùng **vertex color** hoặc material màu phẳng tên theo mã hex cho trước. Không emissive, không transparency (trừ liễu: cành rủ bằng dải mặt phẳng 2 mặt, vẫn không alpha texture).
- Đặt tên vật/mesh rõ ràng trong Blender (VD: `Trunk`, `Canopy`, `LimeWash`, `Flowers`).

## 2. Thước đo (khóa cứng — nhân vật người trong game cao 1,82u)

Chiều cao cây lấy theo cây thật ở hồ Xuân Hương (Đà Lạt) so với người đứng cạnh. Không tự bịa tỉ lệ khác.

## 3. Năm mẫu cây phải giao

### A. Thông tán ô Đà Lạt (cải tiến — mẫu hiện tại bị chê "như cái đĩa")
- Thân thẳng cao, vỏ nâu xám `#6b5847`, có **vệt quét vôi ở gốc cao ~1,0u, màu trắng ngả xám `#919798`** (không trắng tinh).
- Tán gồm **2–3 tầng tán dẹt xếp lệch nhau** ở độ cao 8,5–12u, tổng chiều cao cây **11,5–12,5u**; tán KHÔNG phải đĩa tròn đều: mép tán lượn sóng/lệch tâm, đường kính tán 6–8u, màu lá sẫm `#29362a` pha mảng `#35482f`.
- Yêu cầu đọc từ xa vẫn ra "thông Đà Lạt": thân cao mảnh, tán ô dẹt trên đỉnh.

### B. Cây lá rộng nghiêng ra mặt nước (dấu ấn mạnh nhất của bờ hồ thật)
- Thân **nghiêng 25–45°** (biến thiên giữa các cây do người trồng trong game xoay — bạn dựng 1 mẫu nghiêng ~35°), thân phân 2–3 nhánh lớn.
- Tán lá rộng xòe bất đối xứng về phía nghiêng, lá xanh sẫm `#2f4429` pha `#43582f`; gốc quét vôi `#919798` cao ~1,0u.
- Tổng cao (theo phương đứng) **7–9u**, chiều vươn ngang của tán ≥ 5u.

### C. Liễu rủ
- Thân ngắn 2,5–3,5u, tán chính ở 4–5u; **cành rủ dài chạm gần mặt đất/nước** (dài 3–4u), làm bằng các dải cong mảnh xếp lớp, màu lá xanh sáng hơn các cây khác: `#5a7038` pha `#718c46`.
- Tổng cao **5,5–6,5u**.

### D. Phượng tím (điểm nhấn)
- Thân 4–5u phân nhánh chữ Y, tán xòe rộng 6–7u ở cao 5,5–7u; lá xanh thẫm `#2c3f2a`, điểm **mảng hoa tím `#7a5fa8` / `#8d74b8`** phủ ~35% bề mặt tán trên (mảng cục, không rải đều như rắc bột).

### E. Bụi hoa giấy ven đường
- Bụi thấp **1,2–1,8u**, dạng nửa cầu lệch, lá xanh `#3d5230`, hoa **hồng tím đậm `#a83a6b` / `#bf4f83`** thành từng chùm lớn ở mặt ngoài.

## 4. Sản phẩm phải giao

1. **5 file .glb** (mỗi mẫu 1 file, ≤120 KB/file).
2. **1 ảnh render nghiệm thu**: cả 5 cây đứng cạnh **một nhân vật người cao 1,82u** (dựng 1 hình người đơn giản đúng chiều cao làm thước), góc camera tầm mắt người (cao ~1,6u) + 1 ảnh góc cao 45° kiểu diorama. Nền trung tính.
3. **1 bảng kê ngắn** (file .md): chiều cao thật trong file của từng cây (đo trong Blender), số đa giác, dung lượng file.

## 5. Tự kiểm trước khi giao (đạt hết mới gửi)

- [ ] Mở từng .glb bằng 1 trình xem glTF bất kỳ: không lỗi, cây đứng đúng gốc, không bị lật/nghiêng ngoài ý muốn (trừ mẫu B nghiêng có chủ đích).
- [ ] Chiều cao đo lại khớp mục 3 (±10%).
- [ ] Không texture ngoài, không vật liệu phát sáng, màu đúng hex (±5 mỗi kênh).
- [ ] Ảnh render cho thấy rõ: thông hết giống đĩa, cây B nghiêng rõ ra một phía, liễu rủ chạm thấp, phượng tím đọc ra hoa, hoa giấy đọc ra bụi hoa.

## 6. Ngoài phạm vi (đừng làm)

- Không sửa/không cần code game, không trồng cây vào bản đồ — chỉ giao mẫu.
- Không thêm người, nhà, vật trang trí khác vào file cây (nhân vật thước chỉ nằm trong ảnh render).
