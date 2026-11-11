# PROMPT CHO AI STUDIO (Gemini) — DÁN NGUYÊN KHỐI DƯỚI ĐÂY

---

Bạn đang làm việc trên repo game web 3D **"Chợ Hòa Bình Online"** (Đà Lạt) đã được import sẵn. Đây là sản phẩm thật đang chạy, KHÔNG phải bài tập. Đọc kỹ toàn bộ yêu cầu trước khi sửa bất cứ dòng nào. Chuẩn của dự án này là **khắt khe**: mọi thứ phải giống địa danh thật (chợ Đà Lạt, hồ Xuân Hương, quảng trường Hòa Bình), đo từ ảnh/video thật — làm ẩu, làm cho có, hoặc dùng hình khối tạm (placeholder) là bị trả về.

## 0. Sự thật về dự án (đọc từ repo, đừng đoán)

- Stack: Three.js r160, game nằm gần như trọn trong `prototype-v2/index.html`; model 3D là các file `.glb` trong `prototype-v2/assets/` (dựng bằng Blender, màu phẳng vertex color).
- Phong cách khóa cứng: **chibi diorama** — đầu to tròn, camera nghiêng ~45°, màu phẳng ấm, không photoreal, không texture ảnh ngoài.
- Nghiên cứu đo đạc thật nằm trong thư mục `research/` (đặc biệt: `research/28_VIDEO_HO_XUAN_HUONG.md` = palette + tiết diện bờ hồ đo từ video đi dạo thật; `research/29_PHAN_PHOI_CAY_HO.md` = bảng phân phối cây quanh hồ; `research/00–27` = các phần còn lại). **Mọi con số trong các file đó là luật.** Đọc chúng trước khi làm phần liên quan.
- Hồ sơ các vòng đã làm: `prototype-v2/V4-CHECKLIST.md`. Đọc các mục gần nhất để biết cái gì đã xong, tránh làm lại hoặc phá vỡ.

## 1. Luật bất di bất dịch (vi phạm = hủy toàn bộ kết quả)

1. **KHÔNG đổi khóa lưu game**: localStorage key phải giữ nguyên `chohb3d-v1`; cấu trúc save cũ phải nạp được.
2. **KHÔNG dời vị trí khóa**: mặt tiền chợ ở z=12; thang tam cấp tại (−56, 0, −16); đảo bùng binh (−30, 0, −6) và tượng (−34.2, 0, −2.8); điểm spawn trên trục Nguyễn Thị Minh Khai x=−188; hồ Xuân Hương: mặt nước x −560..−224, z 36..196, đảo Thủy Tạ tâm (−250, 58).
3. **Thước tỉ lệ**: nhân vật cao 1,82 đơn vị. Mọi vật mới phải theo tỉ lệ người thật: ghế dài 2,1 / cao ngồi 0,5 / tựa 1,0; đèn đường 5,5–6,0; thông ven hồ 11,5–12,5; đường dạo bờ bắc rộng 12.
4. **KHÔNG viết lại từ đầu.** Sửa trên code hiện có, giữ nguyên tên hàm, hệ thống (NPC, traffic, ngày/đêm, nhiệt độ lạnh, hộ chiếu, thuê xe/thuyền) và mọi tính năng đang chạy. Cấm xóa tính năng để "làm cho dễ".
5. **KHÔNG thêm thư viện/CDN/tài nguyên ngoài mới.** Không texture ảnh tải từ web. Model mới chỉ ở dạng hình học + màu phẳng trong code hoặc GLB.
6. **Dung lượng**: bản standalone (`index-standalone.html` đóng gói từ index.html + assets) phải ≤ 10.485.760 byte. Đừng làm phình assets.
7. **Hiệu năng**: không cấp phát bộ nhớ trong vòng lặp mỗi frame ở các hàm nóng (update NPC/traffic/nước); giữ nhịp 60fps trên máy yếu.
8. **Không lỗi đen màn hình**: mọi biến/hàm phải được định nghĩa trước khi dùng theo đúng thứ tự nạp của file (lỗi TDZ đã từng làm sập game — cực kỳ cẩn thận khi chèn code mới).
9. Nước hồ **cấm quay lại màu teal/xanh bể bơi**. Palette hồ khóa theo research/28: nước ngày xám bạc, chiều/đêm chàm; lát xám `#acadab`; cỏ olive; tán cây sẫm.
10. Cây quanh hồ trồng **đúng bảng phân phối research/29** (loài, vị trí, mật độ từng đoạn). Cấm rải cây đều tăm tắp; thông **cấm hình nón** (phải là thông tán ô thân cao).

## 2. Việc phải làm (làm SÂU từng hạng mục, theo đúng thứ tự ưu tiên)

### A. Nội thất chợ Đà Lạt — giống thật
- 40 quầy trong nhà lồng phải phân hóa hàng hóa thật: rau củ, trái cây, hoa, vải, đồ khô, đặc sản, đồ ăn — mỗi nhóm có màu sắc, cách bày (sọt, thúng, kệ tầng, treo) khác nhau; cấm 40 quầy giống hệt nhau.
- Lối đi thông thoáng đúng nhịp cột; biển hiệu từng quầy (chữ Việt, đúng chính tả); đèn ấm treo; sàn có vệt cũ/mòn; tiểu thương ngồi sau quầy, khách đứng mua.
- Đối chiếu mô tả + ảnh trong thư mục `theme/real-market/` của repo nếu có.

### B. Bậc tam cấp + khu đỉnh thang
- Bậc thang có độ mòn, lan can, người bán hàng ngồi bậc, xe máy đậu chân thang; chú coi bói ở chiếu nghỉ (tính năng đã có — giữ nguyên vị trí, làm giàu khung cảnh quanh).
- Hai shop đỉnh thang (La Tulipe, L'angfarm) giữ vị trí; thêm chi tiết mặt tiền đúng thương hiệu.

### C. Quảng trường Hòa Bình
- Đài phun nước (nước phải có chuyển động + tia, không phải đĩa tĩnh), góc hát ở quảng trường với ca sĩ + vòng người nghe, ghế đá, đèn, cờ; buổi tối là điểm tụ đông nhất sau chợ.
- Khung cảnh phải đọc ra "quảng trường trước chợ Đà Lạt": mở, thoáng, nhìn thẳng mặt tiền chợ cong.

### D. Hồ Xuân Hương — hoàn thiện
- Trồng cây đúng research/29; nước có gợn nhiều lớp + phản chiếu mép bờ, hết cảm giác tấm phẳng.
- Đạp vịt phải chơi được trọn vòng: tới ki-ốt → trả 30 Xu / 5 phút → xuống thuyền → chèo trong vùng nước cho phép (không xuyên kè/đảo/cầu) → hết giờ hoặc quay về bến thì trả thuyền. Không được đi bộ trên mặt nước khi không có thuyền.
- Thủy Tạ ban đêm lên đèn hồng magenta + phản chiếu xuống nước như research/28.

### E. Hệ thống & cảm giác lạnh Đà Lạt
- Hộ chiếu Đi Chợ đủ dấu gồm dấu hồ; điểm chụp ảnh (photo spots) hoạt động.
- Cái lạnh phải NHÌN THẤY được: biển nhiệt độ đúng giờ, hơi thở NPC/người chơi khi trời lạnh, NPC mặc áo ấm/khăn/mũ, sương sớm trên mặt hồ.

## 3. Cách làm việc bắt buộc

1. Trước khi sửa, xuất một **kế hoạch ngắn**: bạn sẽ sửa file nào, mục nào (A–E), theo số đo nào trong research/.
2. Làm **trọn vẹn từng hạng mục một** theo thứ tự A→E. Nếu không đủ lượt làm hết, làm A và B hoàn hảo còn hơn làm cả 5 hạng mục nửa vời — và nói rõ đã dừng ở đâu.
3. Sau mỗi hạng mục, tự rà: có phá save không, có dời vị trí khóa không, có biến nào dùng trước khi định nghĩa không, có tính năng cũ nào bị mất không.
4. Đầu ra cuối cùng gồm: (i) toàn bộ file đã sửa (đầy đủ, không cắt "…"), (ii) **CHANGELOG** liệt kê từng thay đổi + lý do + số đo nguồn, (iii) **bảng tự kiểm đã điền thật** theo mục 4 dưới đây — mục nào không tự kiểm được phải ghi "CHƯA KIỂM ĐƯỢC", cấm ghi đạt bừa.

## 4. Bảng tự kiểm (điền trung thực khi giao)

- [ ] Save cũ `chohb3d-v1` nạp được, không mất xu/dấu hộ chiếu.
- [ ] Không vị trí khóa nào bị dời (liệt kê tọa độ bạn đã giữ).
- [ ] Không thêm CDN/thư viện/texture ngoài.
- [ ] Mọi mã màu/tỉ lệ dùng trong phần mới đều có nguồn (research/ hoặc đo từ ảnh trong repo) — liệt kê.
- [ ] Không còn placeholder, không còn TODO trong phần bạn chạm vào.
- [ ] Thứ tự định nghĩa trong file an toàn (không TDZ) — nêu cách bạn kiểm.
- [ ] Ước lượng dung lượng standalone sau thay đổi.

## 5. Cấm tuyệt đối

- Viết lại game theo phong cách khác / đổi engine / đổi sang React.
- Đổi tên file, đổi cấu trúc thư mục, đổi key save.
- Bịa số đo, bịa địa danh, thêm công trình không có thật ở chợ Đà Lạt – hồ Xuân Hương – quảng trường Hòa Bình.
- Giao code cắt ngắn, code "..."省略, hoặc chỉ giao mô tả mà không giao file sửa.
