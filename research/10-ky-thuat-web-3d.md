# 10 — Kỹ thuật xây web 3D tham quan trên trình duyệt

> Mục tiêu: rút ra stack kỹ thuật phù hợp cho **Chợ Hòa Bình 3D (Đà Lạt)** — web 3D chạy thẳng trên trình duyệt điện thoại/máy tính, đi lại tham quan, ghé hàng quán, mua đồ ăn/nước uống — học từ cách các site chùa online đang viral (Niệm Phật Online, Chùa Sen, Sansa) vận hành.
> Ngày nghiên cứu: 05/11/2026. Chỉ nghiên cứu, chưa code.
> **Lưu ý trung thực về nguồn:** cả 3 site mẫu đều **không công bố tech stack**. `browser.open` chỉ lấy được text đã render (không xem được view-source/script bundle), nên phần "dấu hiệu stack" dưới đây tách rõ: **[Đã xác nhận]** = báo chí/trang chính thức của site nói; **[Suy luận]** = suy ra từ hành vi quan sát được, cần kiểm chứng thêm bằng DevTools khi làm thật.

---

## 1. Dấu hiệu kỹ thuật từ các site mẫu

### 1.1. Sansa (sansatemple.com, Hàn Quốc — site gốc của trend)

**[Đã xác nhận]**

- Tác giả Park Jin-won (bút danh Metamong), không phải lập trình viên chuyên nghiệp, xây bằng **"vibe coding" với Codex của OpenAI** — bản đầu trong ~30 phút. Bài học: rào cản code web 3D nay rất thấp, AI sinh code tốt nhất cho stack phổ biến nhất (xem mục 3).
- Kiến trúc **phòng (room)**: chính điện Thanh Liên Đường gồm **100 phòng/server, mỗi phòng tối đa 100 người**. Sức chứa nâng dần 20 → 100 → 1.200 → 10.000 người khi quá tải. Có thời điểm 4.679 người online đồng thời trên 100 phòng.
- Vận hành **~100 server qua Cloudflare** (theo Asia Economy). Không đăng nhập, không cài app, vào là được gán server tự động + tên nhân vật ngẫu nhiên.
- **Không có chat** — cố ý. Tương tác duy nhất là hành động (chắp tay, nhảy, lạy). Đây là quyết định sản phẩm giúp giảm mạnh chi phí kiểm duyệt + băng thông.
- Điều khiển: desktop = click mặt đất để đi (click-to-move), kéo để nhìn, lăn chuột zoom; mobile = chạm để đi, vuốt nhìn, pinch zoom. Nút hành động to ở thanh dưới trên mobile.
- Tính năng **tràng hạt là một màn hình 2D riêng** (nền be, vuốt để lần hạt, đếm tới 108), không nằm trong cảnh 3D — chi tiết rất đáng học: phần nào không cần 3D thì làm 2D cho nhẹ.

**[Suy luận]** Mô hình phòng 100 người + gán server tự động + chỉ đồng bộ vị trí/hành động cho thấy backend nhiều khả năng là WebSocket theo room (kiểu Colyseus/Cloudflare Durable Objects/custom ws), asset 3D low-poly rất nhẹ nên nghẽn nằm ở số kết nối chứ không ở đồ họa. Engine render không có nguồn nào xác nhận (không khẳng định là Three.js).

### 1.2. Niệm Phật Online (niemphat.online / s2.niemphat.online, Việt Nam)

**[Đã xác nhận/Quan sát được]**

- **Chia máy chủ (shard) ngay từ cổng vào:** trang chủ bắt **chọn máy chủ** (`s2.niemphat.online` là một subdomain riêng), và nói rõ *"mỗi máy chủ có nhân vật, tiến độ và Ngọc riêng"* — tức dữ liệu nhân vật/tiền tệ **gắn theo shard**, không dùng chung. Người chơi vào sai máy chủ là mất tiến độ.
- Có lớp game đầy đủ trên nền cảnh 3D: nhiệm vụ ngày/tuần, cấp độ, vật phẩm, điểm danh, bảng xếp hạng, hộ chiếu hành hương, bản đồ chùa 3 miền — tức có **backend lưu tiến độ bền vững + tài khoản**, không chỉ là phòng tạm thời như Sansa.
- Khi quá tải, trang hiển thị thông báo *"lượng người lên chùa đang tăng đột biến nên máy chủ chưa đáp ứng kịp"* ngay ở màn hình chờ — bài học: phải thiết kế sẵn màn hình xếp hàng/quá tải thân thiện.
- Âm thanh là một phần của trải nghiệm (mõ, chuông, giọng đọc AI tụng kinh, "nên đeo tai nghe").

**[Suy luận]** Shard theo subdomain + tiến độ riêng từng shard gợi ý kiến trúc server game tự host theo cụm (mỗi shard một tiến trình/DB riêng), WebGL canvas cho cảnh 3D. Engine (Three.js/Unity WebGL/Babylon) không quan sát được từ text trang.

### 1.3. Chùa Sen (chuasen.com — lưu ý: domain `chuasen.online` không phân giải được khi kiểm tra; site đang sống là `chuasen.com`)

**[Đã xác nhận/Quan sát được — đây là site để lại nhiều dấu vết kỹ thuật nhất qua tài liệu hướng dẫn chính thức]**

- **PWA:** có hộp thoại Cài đặt cho "cài lên màn hình chính" để vào nhanh như app — pattern PWA (manifest + service worker), không qua kho ứng dụng.
- **Điều khiển mobile hoàn chỉnh, đáng copy nguyên mẫu:**
  - Joystick ảo nửa trái màn hình (bật sẵn, tắt được trong Cài đặt), vuốt nửa phải để nhìn quanh, pinch zoom.
  - **Chạm lên sàn → nhân vật tự đi tới** (pathfinding/click-to-move), chạm vào vật (bồ đoàn, lư hương, chuông) → tự đi tới vật đó.
  - **Nút bấm ngữ cảnh (contextual action):** đến gần vật mới hiện nút "Thắp hương / Thỉnh chuông / Ngồi xuống / Lạy Phật". Trên desktop map sang phím F/Enter; di chuyển WASD/mũi tên + kéo chuột nhìn + Q/E xoay.
- **Multiplayer theo phòng, có đồng bộ âm thanh:** *"Thỉnh chuông — những người cùng phòng cũng nghe tiếng chuông của bạn"*. Tức hành động của một người được broadcast cho cả phòng, kể cả sự kiện âm thanh.
- **Không chat tự do:** chào nhau bằng **câu chào có sẵn** (Chắp tay, A Di Đà Phật, Tùy hỷ…) + lọc tên nhân vật (chặn tên tục tĩu/giả danh). Cùng triết lý với Sansa nhưng mềm hơn.
- **Lưu nhân vật không bắt buộc:** không đăng nhập vẫn vào được; muốn giữ nhân vật/công phu thì đăng nhập để lấy lại. Tiến độ được giữ giữa các lần vào.
- **Mở khóa tính năng theo cấp** (Thỉnh chuông/Dâng hoa mở từ cấp 2 "Hành trình", có tùy chọn "Hiện đủ mọi tính năng") — cơ chế progression nhẹ giữ người quay lại.

### 1.4. Kết luận chung từ 3 site

| Khía cạnh | Mẫu số chung |
|---|---|
| Vào chơi | Không cài app, không bắt đăng ký, vào thẳng từ trình duyệt (mobile-first) |
| Đồng bộ người chơi | Chia **phòng/shard nhỏ** (Sansa 100 người/phòng), không phải một thế giới duy nhất |
| Dữ liệu đồng bộ | Vị trí + trạng thái/hành động của avatar; sự kiện (tiếng chuông) broadcast trong phòng |
| Giao tiếp | Không chat tự do: emote/câu chào preset (giảm kiểm duyệt, giảm băng thông) |
| Đồ họa | Low-poly, cảnh nhỏ, ít vật liệu — nghẽn ở **số kết nối**, không ở GPU |
| Giữ chân | Cấp độ, nhiệm vụ ngày, vật phẩm, lưu tiến độ (bản Việt) — lớp "game nhẹ" phủ lên cảnh 3D |
| Phân phối | PWA cài màn hình chính (Chùa Sen), link chia sẻ qua Threads/Facebook/TikTok |

---

## 2. So sánh engine web 3D

Số liệu bundle/phổ biến theo tổng hợp các bài so sánh 2025–2026 (utsubo.com, simamdigital.com, viverse) — mang tính tham khảo, thay đổi theo phiên bản:

| Tiêu chí | **Three.js** | **Babylon.js** | **PlayCanvas** | Unity WebGL (đối chiếu) |
|---|---|---|---|---|
| Bản chất | Thư viện render cấp thấp, tự lắp hệ thống | Engine đầy đủ (Microsoft) | Engine + **editor đám mây** trực quan | Engine desktop xuất WASM |
| Bundle (gzip, full) | **~185 KB** (WebGL) / ~300 KB (WebGPU) | ~1,8 MB (tree-shake được, thực tế nhỏ hơn) | ~615 KB | **15–50 MB** cả dự án |
| Thời gian tới khung hình đầu | Nhanh nhất, tải như web thường | Trung bình | Nhanh, tối ưu mobile sẵn | 5–15 giây, phải nạp toàn bộ runtime |
| Vật lý / animation / audio | Tự lắp (cannon-es, tự viết…) | **Có sẵn** (Havok, audio, particles, XR) | Có sẵn ở mức engine | Có sẵn đầy đủ nhất |
| Tối ưu mobile | Tự làm (nhưng nhẹ nên dễ đạt) | Tự làm, có snapshot rendering | **Tốt nhất sẵn có**: nén texture theo nền tảng (ASTC/DXT), chỉnh GC | **Kém nhất**: Unity không hỗ trợ chính thức mobile browser cho WebGL; iOS Safari dễ crash tab vì giới hạn bộ nhớ WASM |
| WebGPU | Có từ r171, fallback WebGL2 | Có (5.0+, WGSL từ 8.0) | Beta, tự fallback WebGL2 | Chưa/ hạn chế |
| Hệ sinh thái | **Lớn nhất áp đảo**: ~12 triệu lượt tải npm/tuần (gấp ~39× Babylon, ~215× PlayCanvas), nhiều ví dụ nhất | Cộng đồng nhỏ hơn, tài liệu chính thức tốt, Playground thử code nhanh | Nhỏ nhất; mạnh ở đội có người không code nhờ editor trực quan | Asset Store lớn nhưng không dành cho web |
| AI/vibe-coding sinh code | **Tốt nhất** (dữ liệu huấn luyện + ví dụ công khai nhiều nhất) — đúng cách Sansa ra đời | Khá | Trung bình (nhiều thao tác nằm trong editor, AI khó can thiệp) | Không phù hợp quy trình này |
| Giấy phép | MIT, miễn phí | Apache-2.0, miễn phí | Engine MIT; editor miễn phí cho dự án public, trả phí cho private/team | Theo doanh thu, nặng nề cho dự án nhỏ |
| Điểm yếu chính | Không editor, không physics — đội dev phải tự chủ công nghệ | Bundle nặng, học lâu hơn, ít nhân lực VN quen | Phụ thuộc nền tảng/editor của họ, cộng đồng nhỏ | Quá nặng cho tham quan trên điện thoại — **loại** |

**Godot (web export)** cũng là lựa chọn phụ: build ~5–9 MB, nhẹ hơn Unity, miễn phí MIT — vẫn nặng hơn hẳn Three.js và hệ sinh thái web mỏng, chỉ nên cân nhắc nếu đội đã thạo Godot.

---

## 3. Khuyến nghị stack cho Chợ Hòa Bình 3D

### 3.1. Chốt stack

```
Frontend (web, PWA)
├─ Three.js (TypeScript) + Vite — render WebGL2, cân nhắc WebGPURenderer khi ổn định
├─ Vanilla TS hoặc Svelte nhẹ cho UI 2D (menu quán, giỏ hàng, bản đồ) — tránh React nặng không cần thiết
├─ Điều khiển: joystick trái + vuốt phải (mobile), WASD + chuột (desktop),
│  click/chạm-để-đi + nút hành động ngữ cảnh  ← copy nguyên mẫu Chùa Sen
└─ PWA: manifest + service worker (cài màn hình chính, cache asset theo version)

3D asset pipeline
├─ Blender (model low-poly cartoon) → glTF/GLB
├─ gltf-transform: Draco/meshopt (nén hình học) + KTX2/Basis (nén texture GPU) + dedup/prune
└─ CDN (Cloudflare R2/Pages) + tên file có hash để cache lâu dài

Backend
├─ Giai đoạn 1: CHƯA cần multiplayer thật — NPC tiểu thương/khách dạo chợ + người chơi đơn
├─ Giai đoạn 2: Colyseus (Node.js/TypeScript) — room-based, đồng bộ state kiểu patch nhị phân
│  (mặc định patch mỗi 50 ms), server authoritative; mỗi phòng 30–50 người
│  (phương án serverless thay thế: Cloudflare Durable Objects + WebSocket — đúng hướng Sansa đang chạy)
├─ Lưu trữ: PostgreSQL (tài khoản, giỏ hàng, đơn hàng) + Redis (presence/session Colyseus khi scale)
└─ Thanh toán/đơn hàng đồ ăn: REST API riêng, KHÔNG đi qua kênh realtime
```

**Vì sao Three.js chứ không phải Babylon/PlayCanvas?**

1. Khách của chợ đến chủ yếu từ link chia sẻ trên điện thoại — **thời gian tải lần đầu quyết định sống còn**; Three.js nhẹ hơn Babylon ~10 lần ở bundle core.
2. Cảnh chợ là kiến trúc low-poly + đi lại + tương tác đơn giản, không cần physics/phá hủy/XR của Babylon.
3. Đội nhỏ + làm cùng AI (vibe coding như Sansa): Three.js là stack AI sinh code chính xác nhất và dễ tuyển/nhờ người sửa nhất.
4. PlayCanvas chỉ thắng nếu có nhiều người không biết code cần sửa cảnh bằng editor — hiện tại chưa phải nhu cầu.

### 3.2. Tổ chức asset (quan trọng ngang chọn engine)

Chợ Hòa Bình có lợi thế lớn: **hàng quán lặp lại cực nhiều** — đúng thứ instancing sinh ra để xử lý.

- **Chia cảnh theo khu (zone), tải lười (lazy-load) theo khu:** cổng chợ/khu Hòa Bình (khu trung tâm, tải đầu tiên) → trong chợ Đà Lạt (sạp rau, sạp hoa, sạp đồ khô) → chợ đêm (sạp đồ ăn, đồ len, đặc sản) → hướng hồ Xuân Hương. Mỗi khu 1 file GLB riêng + 1 file manifest JSON (danh sách vật tương tác, điểm đứng của NPC, collider đơn giản).
- **InstancedMesh cho mọi thứ lặp:** sạp chợ, bàn ghế, ô dù, đèn lồng, chậu hoa atiso/dã quỳ, thùng rau, chai mứt dâu… — 1 draw call cho cả trăm bản sao. `BatchedMesh`/merge geometry cho vật tĩnh dùng chung vật liệu.
- **Avatar dùng chung 1–2 bộ xương/animation** (đi, đứng, vẫy tay, ăn/uống), đổi màu áo/bảng màu (palette swap) thay vì model riêng cho từng người.
- **Texture atlas** cho biển hiệu sạp + mặt hàng: gộp nhiều biển/món vào 1–2 atlas 1024² thay vì hàng trăm texture lẻ (mỗi texture lẻ = thêm draw call + bộ nhớ).
- **LOD 2 mức** cho công trình điểm nhấn (tòa chợ, tháp/rạp Hòa Bình): gần = bản đẹp, xa = khối đơn giản; vật nhỏ xa thì ẩn hẳn theo khoảng cách (fog nhẹ của Đà Lạt vừa đúng chất sương, vừa che được culling).
- **Ánh sáng rẻ:** bake AO/lightmap trong Blender, trong scene chỉ 1 directional + hemisphere light, **không đổ bóng động** trên mobile (dùng blob shadow tròn dưới chân nhân vật nếu cần).
- Đặt **ngân sách cứng** và kiểm tra tự động khi build asset: mỗi GLB khu ≤ 2–3 MB sau nén, texture ≤ 1024 (điểm nhấn tối đa 2048), tổng tải lần đầu (code + khu trung tâm) **≤ 5 MB**.

### 3.3. Multiplayer (giai đoạn 2) — chỉ đồng bộ cái cần

- Mô hình **room theo khu**, 30–50 người/phòng (Sansa dùng 100 — chợ có nhiều tương tác mua bán hơn nên để thấp hơn cho mượt).
- Chỉ sync: vị trí (x,y,z), hướng, trạng thái animation, hành động one-shot (vẫy tay, ngồi xuống ghế đá, nâng ly). Patch 10–20 Hz + nội suy (interpolation) phía client — không sync từng khung hình.
- **Interest management:** chỉ nhận dữ liệu của người cùng khu/tầm nhìn.
- NPC tiểu thương **không cần server**: chạy phía client theo kịch bản (chào hàng, đưa menu khi khách đến gần).
- Mua đồ ăn/nước là giao dịch tiền thật → đi qua REST + server kiểm tra giá/tồn kho, **server authoritative**; kênh realtime chỉ phát sự kiện hiển thị ("A vừa mua bánh tráng nướng") nếu muốn không khí.
- Giao tiếp: **emote/câu chào preset** như Chùa Sen/Sansa (tránh chat tự do ở giai đoạn đầu: đỡ kiểm duyệt, đỡ toxic, đúng tệp khách gia đình).
- Có sẵn **chế độ quá tải**: hàng chờ + thông báo thân thiện (bài học từ màn hình chờ của Niệm Phật Online) thay vì lỗi trắng trang.

---

## 4. Lưu ý hiệu năng trên điện thoại (phần quyết định dự án sống/chết)

Đa số khách vào từ Facebook/TikTok trên Android tầm trung — phải lấy **Android tầm trung làm máy chuẩn**, không phải iPhone đời mới.

**Ngân sách hiệu năng đề xuất (quality mặc định = mobile):**

| Hạng mục | Ngân sách |
|---|---|
| Draw call | < 100 / khung hình |
| Tam giác hiển thị đồng thời | ≤ 300–500k (model đơn lẻ 20–50k) |
| Độ phân giải render | Cap DPR ở **1.5** (tuyệt đối không render native 3×) |
| Texture | ≤ 1024², định dạng KTX2 (ASTC trên mobile) — JPEG/PNG thường ngốn VRAM gấp ~10 lần khi giải nén lên GPU |
| Vật liệu | Ít loại shader; ưu tiên MeshLambert/Basic cho vật phụ, tránh trong suốt (transparency) chồng nhiều lớp |
| Bóng đổ | Tắt shadow map động; bake tĩnh + blob shadow |
| FPS mục tiêu | 30 FPS ổn định trên máy tầm trung (mượt bền hơn 60 FPS rồi tụt vì nóng máy — thermal throttling sau vài phút là có thật) |
| Tải lần đầu | ≤ 5 MB để vào được khu trung tâm; các khu còn lại stream ngầm |

**Kỹ thuật bắt buộc:**

1. **Adaptive quality:** đo FPS chạy thực tế, tự hạ cấp (giảm DPR → tắt hiệu ứng phụ → giảm NPC) thay vì để giật; có sẵn preset Thấp/Trung/Cao.
2. **Pause khi ẩn tab** (dừng vòng render khi `visibilitychange`), giảm tải khi pin yếu.
3. **Nén asset bằng gltf-transform** trong CI: Draco/meshopt giảm 80–95% dung lượng hình học; KTX2 giữ texture nén ngay trong VRAM.
4. **Fallback tử tế:** máy không chạy nổi WebGL/quá yếu → hiện tour 2D (ảnh 360°/ảnh + bản đồ bấm điểm tham quan) thay vì trang trắng; trang SEO/nội dung HTML thật bao quanh canvas (các site mẫu đều làm: trang hướng dẫn, lịch, giới thiệu quán dạng HTML — vừa SEO vừa là lối vào cho máy yếu).
5. **Kiểm thử trên máy thật:** ít nhất 2 máy Android tầm trung phổ biến + 1 iPhone cũ; iOS Safari là nơi dễ chết nhất vì giới hạn bộ nhớ tab.
6. **Âm thanh:** nhạc nền/tiếng chợ dạng file nén (Opus/AAC), tải sau khi vào cảnh, chỉ phát sau thao tác chạm đầu tiên (chính sách autoplay của trình duyệt).

---

## 5. Lộ trình kỹ thuật gợi ý

1. **MVP (đơn người):** Three.js + 1 khu trung tâm (mặt tiền chợ + khu Hòa Bình) + điều khiển 2 nền tảng + 5–8 sạp có NPC bán hàng, bấm vào xem menu/mua thử (chưa thanh toán thật). Mục tiêu: vào từ link điện thoại < 5 giây, đi dạo mượt.
2. **Bản có người:** Colyseus, phòng theo khu, avatar + emote preset, sự kiện đông vui (giờ mở chợ đêm).
3. **Bản thương mại:** tài khoản, giỏ hàng, thanh toán thật cho gian hàng ăn uống/đặc sản, quản trị cho tiểu thương.

---

## 6. Nguồn tham khảo

- Cellphones Sforum — Cách chơi Niệm Phật Online (chọn máy chủ s2, tính năng): https://cellphones.com.vn/sforum/niem-phat-online
- FPT — Game đi chùa online / Niệm Phật Online (chơi trên trình duyệt, điện thoại & máy tính): https://fpt.vn/tin-tuc/game-di-chua-online-15777.html
- Vietnam.vn — Đi chùa online, trải nghiệm công nghệ hay thực hành tâm linh? (Sansa, Niệm Phật Online): https://www.vietnam.vn/di-chua-online-trai-nghiem-cong-nghe-hay-thuc-hanh-tam-linh
- Điện tử & Ứng dụng — Từ cơn sốt Sansa đến làn sóng chùa online tại Việt Nam: https://dientuungdung.vn/di-chua-online-nguoi-tre-tim-kiem-dieu-gi-sau-mot-cu-cham-man-hinh-19389.html
- Chùa Sen — Hướng dẫn đi chùa online (điều khiển mobile/desktop, PWA, cùng phòng): https://chuasen.com/huong-dan-di-chua-online/
- CafeBiz — Cơn sốt chùa online Sansa (100 phòng, sức chứa 20→10.000): https://cafebiz.vn/con-sot-dang-hot-nhat-tren-mxh-chua-online-khong-cho-noi-chuyen-100000-nguoi-tre-han-quoc-van-chen-nhau-vao-ngoi-176261031091045059.chn
- Soha — Chàng trai 26 tuổi tạo chùa online Sansa nhờ AI (Codex, vibe coding): https://soha.vn/chang-trai-26-tuoi-dung-sau-con-sot-chua-online-dang-that-nghiep-khong-he-co-kinh-nghiem-lap-trinh-chi-mat-30-phut-de-ra-ban-thu-dau-tien-nho-ai-198261102221609369.htm
- EasyTicket (EN) — Why 600,000 People Visited the Online Temple Sansa (click-to-move, gán server tự động, màn hình tràng hạt 2D): https://easyticket.co.kr/en/posts/2026/%EC%98%A8%EB%9D%BC%EC%9D%B8-%EC%A0%88-%EC%82%B0%EC%82%AC-%EB%B9%84%EC%8A%B7%ED%95%9C-%EC%82%AC%EC%9D%B4%ED%8A%B8%EB%93%A4/
- Asia Economy (EN) — Online Temple Built With Vibe Coding (Cloudflare, ~100 server): https://www.asiae.co.kr/en/article/2026110209301323649
- Utsubo — Three.js Alternatives Compared: Babylon.js vs PlayCanvas (bundle, npm downloads, mobile): https://www.utsubo.com/blog/threejs-vs-babylonjs-vs-playcanvas-comparison
- Simam Digital — Unity vs WebGL for Browser 3D (build size 15–40 MB vs 1–5 MB, mobile browser không được Unity hỗ trợ): https://www.simamdigital.com/unity-vs-webgl-browser-3d-experiences.html
- Utsubo — Three.js vs Unity for Web (load time, bundle): https://www.utsubo.com/blog/threejs-vs-unity-web-comparison
- Colyseus Docs — State Synchronization (schema, patch nhị phân, patchRate 50 ms): https://0-15-x.docs.colyseus.io/state/
- PlayCanvas Dev — Real-time Multiplayer with Colyseus (tutorial tích hợp engine + Colyseus): https://developer.playcanvas.com/tutorials/real-time-multiplayer-colyseus/
- AlphaExpansion — WebGL Performance Optimization (instancing, KTX2, cap DPR 1.5–2, thermal throttling): https://alphaexpansion.io/blog/webgl-performance-optimization-10000-objects

*Điểm chưa kiểm chứng được: engine/framework cụ thể trong mã nguồn của niemphat.online, chuasen.com và sansatemple.com (cần xem script bundle bằng DevTools ở bước làm thật — ngoài khả năng của công cụ fetch text). Mọi khẳng định về stack của 3 site này trong file đều đã gắn nhãn [Đã xác nhận] hoặc [Suy luận].*
