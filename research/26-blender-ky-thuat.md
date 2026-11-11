# 26 — Kỹ thuật Blender + glTF chắt lọc từ mạng, đối chiếu số đo thật của dự án

> Vòng nghiên cứu 11/11/2026. Mọi con số về market.glb dưới đây là ĐO THẬT trên file hiện tại
> (chạy gltf-transform 4.5.1 trên bản sao ở /tmp + probe bpy trên chính Blender 5.0.1 của dự án),
> không phải số ước lượng từ tài liệu. Không sửa code/model ở vòng này.

## 0. Giải phẫu market.glb hiện tại (đo bằng parser GLB + `gltf-transform inspect`)

| Hạng mục | Số đo |
|---|---|
| Tổng file | 1.652.360 byte (bản assets hiện hành lúc đo) |
| Buffer hình học | 1.480.528 byte trong bufferViews |
| POSITION | 523.572 B — 43.631 đỉnh × 3 × float32 |
| NORMAL | 523.572 B — float32 |
| TEXCOORD_0 | 349.048 B — 21% file |
| INDEX | 163.128 B |
| Mesh / node / material | 209 / 209 / 33 (tên material giữ nguyên: WallCream, MarketWin, SignLetters…) |
| Tam giác | 27.188 (đã rất thấp — không cần simplify) |
| Ảnh/animation/skin | 0 / 0 / 0 — file thuần hình học + màu phẳng |
| Cách game nạp | GLTFLoader three r160 thuần, KHÔNG decoder; standalone nhúng GLB dạng base64 (phình ×4/3) và nạp three từ importmap unpkg |

Hệ quả: mỗi 1 byte giảm ở GLB = giảm 1,33 byte trong standalone. Trần standalone 10.485.760,
bản hiện hành 10.485.209 → chỉ dư 551 byte. Đây là chỗ gỡ nút thắt dung lượng lớn nhất của dự án.

---

## 1. Lượng tử hoá hình học — KHR_mesh_quantization (gltf-transform `quantize`)

- **Kỹ thuật:** lưu POSITION dạng int16 14-bit (scale/offset gập vào node transform), NORMAL 10-bit,
  UV 12-bit, thay vì float32. Vertex điển hình ~48 B → ~20 B. Extension đã ratified của Khronos,
  **KHÔNG cần decoder**: GPU đọc trực tiếp, GLTFLoader của three.js hỗ trợ native từ r111.
- **Nguồn:** https://app.cinevva.com/guides/optimize-glb-for-web (mục Step 2: mặc định gltf-transform
  14/10/12/8 bit; test 28 MB → 22,8 MB khi chỉ quantize) + https://meshoptimizer.org/gltf/
  (bản mặc định gltfpack cũng quantize và nạp được bằng loader hỗ trợ KHR_mesh_quantization như three.js r111+).
- **ĐO THẬT trên market.glb (bản sao /tmp, gltf-transform 4.5.1):**
  - `gltf-transform quantize market.glb out.glb` → **661.156 B (−60,0%)**
  - thêm `--quantize-normal 8` → **581.908 B (−64,8%)**
  - Kiểm chứng toàn vẹn sau nén: 209 mesh, 27.188 tam giác, 43.631 đỉnh, 214 primitive còn TEXCOORD_0,
    33 tên material khớp 100% với bản gốc (FACADE_HEX remap theo tên material không bị đụng).
  - So sánh: `weld` rồi quantize = 661.668 B ≈ quantize trơn → **weld vô ích trên file này, đừng tốn công**
    (đỉnh đã tách theo cạnh phẳng/UV seam như Blender Manual cảnh báo, weld không gộp thêm được).
- **Áp dụng:** chạy quantize như bước hậu xử lý sau `build_models.py` export, cho market.glb trước,
  sau đó nhân ra cả 14 GLB. Riêng market: −991.204 B raw ⇒ standalone còn ≈ 9,16 MB,
  **dư trần từ 551 B → ~1,32 MB**. Áp cho hotels (1,49 MB), stall (1,11 MB), roundabout (1,08 MB)
  sẽ gỡ thêm cỡ ~2 MB nữa (chưa đo từng file — đo trước khi hứa số).
- **Rủi ro:** (a) 14-bit trên mesh đơn khổng lồ gây faceting — market trải ~90u → bước lượng tử
  ~0,0055u, vô hình ở tỉ lệ game; (b) NORMAL 8-bit có thể banding trên tường phẳng lớn dưới nắng —
  muốn lấy mốc −64,8% thì phải soi render mặt tiền ban ngày trước khi chốt, mặc định 10-bit là an toàn;
  (c) extension rơi vào `extensionsRequired` — viewer không hỗ trợ sẽ từ chối file, nhưng consumer
  duy nhất là game của mình (three r160) nên chấp nhận được.
- **Ưu tiên: ÁP NGAY VÒNG SAU.**

## 2. Nén Meshopt — EXT_meshopt_compression (gltf-transform `meshopt`)

- **Kỹ thuật:** codec nén bufferView (đỉnh + index) trên nền quantization, giải nén ~1 GB/s bằng WASM SIMD.
- **Nguồn:** https://app.cinevva.com/guides/optimize-glb-for-web (bảng so sánh: decoder Meshopt =
  module JS 32 KB kèm WASM inline; Draco = 192–286 KB WASM + 58 KB wrapper + fallback JS 719 KB;
  bake-off: gltfpack `-cc` 4,4 MB vs gltf-transform meshopt 5,1 MB trên cùng file test 28 MB)
  + https://meshoptimizer.org/gltf/ (three.js r122+ hỗ trợ qua `GLTFLoader.setMeshoptDecoder`).
- **ĐO THẬT:** `gltf-transform meshopt market.glb out.glb --level high` → **386.152 B (−76,6%)**,
  toàn vẹn cấu trúc như mục 1. Decoder của đúng three@0.160.0 mà game dùng —
  `examples/jsm/libs/meshopt_decoder.module.js` — **đo được 24.850 B**. Vì standalone hiện đã nạp
  three qua importmap unpkg, thêm `import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js'`
  + 1 dòng `gltfLoader.setMeshoptDecoder(MeshoptDecoder)` tốn ~0 byte file (chỉ tốn nếu sau này inline three:
  +24.850 B, vẫn lời ròng ~370 KB so với chỉ-quantize). Standalone ước còn ≈ 8,80 MB.
- **Áp dụng:** bước 2 sau mục 1, khi cần thêm headroom (vd vòng FASCIA-GEO phình GLB).
  Ưu tiên gltf-transform thay vì gltfpack `-cc`: gltfpack gộp mesh/đổi cấu trúc node theo mặc định
  (README thừa nhận "merging meshes… pruning the node tree") — nguy hiểm cho logic bám tên node/material
  của game; muốn dùng gltfpack phải thêm `-kn` (keep named nodes) + `-km` (keep named materials)
  và kiểm chứng lại toàn bộ. gltf-transform giữ nguyên cấu trúc (đã kiểm chứng ở mục 1).
- **Rủi ro:** quên set decoder trước load → file báo lỗi không nạp được (phải gắn 1 lần tại chỗ tạo
  GLTFLoader, index.html ~dòng 512). Phụ thuộc CDN giữ nguyên như hiện trạng, không phát sinh loại rủi ro mới.
- **Ưu tiên: THỬ NGHIỆM (ngay sau khi mục 1 đã qua cổng).**

## 3. QUY TẮC CẤM: không xoá TEXCOORD_0 khỏi market.glb

- **Phát hiện ngược với trực giác:** TEXCOORD_0 chiếm 349.048 B (21%) trông như rác vì GLB không chứa
  texture nào — nhưng code web **gắn map canvas TEX_GRIME lên mesh mặt tiền lúc chạy**
  (index.html dòng 873, 949, 1343: `o.material.map = TEX_GRIME` theo traverse + độ sáng material).
  three.js không có attribute `uv` thì map không hiển thị đúng. Xoá UV = vỡ lớp bẩn mặt tiền REAL1.
- **Áp dụng:** giữ UV, chỉ lượng tử hoá 12-bit (đã nằm trong mục 1). Với 13 GLB còn lại: chỉ được
  strip UV ở file nào grep chứng minh không có gán `.map =` lúc chạy nhắm vào nó.
- **Ưu tiên: ÁP NGAY (ghi thành luật pipeline).**

## 4. Khoá chặt tham số export trong build_models.py

- **Hiện trạng:** `bpy.ops.export_scene.gltf(filepath=path, export_format='GLB', export_apply=True)` —
  còn lại để mặc định. `export_apply=True` là đúng (áp modifier trước export).
- **Nguồn:** https://deepwiki.com/floorplanner/glTF-Blender-IO/2-user-guide (bảng property đầy đủ của
  exporter chính thức Khronos) + https://docs.blender.org/manual/ar/3.2/addons/import_export/scene_gltf2.html
  (mục Geometry: UVs / Normals / Tangents / Loose Edges / Loose Points; lưu ý "Discontinuous UVs and
  flat-shaded edges may result in moderately higher vertex counts").
- **Áp dụng — ghi tường minh khi export:** `export_texcoords=True` (bắt buộc, xem mục 3),
  `export_tangents=False` (không có normal map thì bật tangents tốn thêm ~700 KB float vô ích),
  `export_animations=False` + `export_extras=False` + `export_cameras=False` + `export_lights=False`
  cho model tĩnh, `export_loose_edges=False`, `export_loose_points=False`.
  Exporter có sẵn Draco (`export_draco_mesh_compression_enable`, đã probe thấy tồn tại trong 5.0.1)
  nhưng **không dùng**: decoder Draco nặng gấp ~10 lần Meshopt và giải nén chậm hơn (số ở mục 2).
- **Ưu tiên: ÁP NGAY (rẻ, đi kèm mục 1).**

## 5. Cycles nghiệm thu: bật Denoise OIDN — render script đang tự tắt

- **Kỹ thuật:** Cycles + OpenImageDenoise với passes Albedo + Normal cho phép mẫu thấp mà hình sạch;
  adaptive sampling dừng sớm ở vùng đã hội tụ (ngưỡng nhiễu 0,01).
- **Nguồn:** https://docs.blender.org/manual/vi/dev/compositing/types/filter/denoise.html
  (Denoise node dùng Open Image Denoise; workflow: bật Denoising Data → nối Noisy Image + Denoising
  Albedo + Denoising Normal; thiếu passes phụ trợ hình sẽ mềm/mất chi tiết)
  + https://superrendersfarm.com/article/blender-render-settings-optimization-guide
  (OIDN "typically giving the highest quality"; khuyến nghị tối thiểu passes Albedo vì chỉ-màu dễ nhoè
  chi tiết ở mẫu thấp; thực hành 128–256 mẫu + denoise cho cảnh ngoài trời trực sáng).
- **ĐO THẬT trên Blender 5.0.1 của dự án (probe bpy):** mặc định Cycles đã là
  `use_denoising=True`, `denoiser='OPENIMAGEDENOISE'`, `denoising_input_passes='RGB_ALBEDO_NORMAL'`,
  `use_adaptive_sampling=True`, `adaptive_threshold=0.01` — trong khi script nghiệm thu của dự án
  (render_facade_real.py) **chủ động đặt `use_denoising=False`** ở 32 mẫu. Chỉ cần bỏ dòng tắt đó là
  render sạch hơn ở cùng 32 mẫu, hoặc hạ 16 mẫu + denoise để soi nhanh gấp đôi.
- **Rủi ro:** denoise ở mẫu quá thấp làm nhoè chữ biển hiệu nhỏ → khi chấm chi tiết chữ/mặt tiền giữ
  ≥32 mẫu + denoise; denoise chỉ để chấm bố cục/màu tổng thể ở lượt nhanh.
- **Ưu tiên: ÁP NGAY (sửa 1 dòng trong các script render nghiệm thu).**

## 6. Khớp màu Blender ↔ three.js: bỏ AgX khi nghiệm thu màu

- **Sự thật của dự án:** web chạy `ACESFilmicToneMapping`, exposure ngày 0,88 / đêm 1,22,
  `outputColorSpace = SRGBColorSpace` (index.html dòng 329–331, 6470, 6498). Blender mặc định
  view transform **AgX** → render rửa sáng, nhạt bão hoà so với web. Đây là gốc của lệch "grade
  rửa sáng hơn web thật" đã ghi nhận nhiều vòng.
- **Nguồn:** https://www.zachsimms.com/3d/export/web-threejs/ (bảng triệu chứng: "Washed out or too
  contrasty → tone mapping differs: Blender uses AgX, three.js defaults to none → set
  renderer.toneMapping = AgXToneMapping (or NeutralToneMapping); compare exposure")
  + https://discourse.threejs.org/t/matching-blender-with-threejs-colors/60716
  + https://github.com/jairotorregrosa/jaiskills/blob/HEAD/skills/creative/motion-design/references/stack-3d-shaders.md
  (đo trên Blender 5.2: danh sách view transform có ACES 1.3 / ACES 2.0 / Khronos PBR Neutral / AgX / Standard;
  AgX làm cam → đào và nâng đen — đúng triệu chứng rửa màu của dự án).
- **ĐO THẬT:** probe trực tiếp Blender 5.0.1 local — đặt được cả: `Standard`, `ACES 1.3`, `ACES 2.0`,
  `Khronos PBR Neutral`, `Filmic`, `AgX`, `Raw` (gán từng giá trị đều OK).
- **Áp dụng (công thức nghiệm thu):** render chấm MÀU mặt tiền ban ngày đặt
  `scene.view_settings.view_transform = 'ACES 1.3'` (gần nhất với ACES filmic của three, không khớp bit)
  và `scene.view_settings.exposure = -0.18` (≈ log2(0,88)). Khi cần kết luận màu vật liệu dứt khoát:
  render `Standard` + lấy median PIL trên vùng vật liệu (số không bị đường cong tone lừa) — đúng
  phương pháp FACADE-COLOR-1 đã dùng. **Không bao giờ chấm màu bằng cách so mắt render AgX với web.**
- **Ưu tiên: ÁP NGAY (chỉ là cài đặt script render).**

## 7. Bevel nhẹ + Weighted Normal — cho khối chibi hết "rẻ tiền" mà ít tốn đỉnh

- **Kỹ thuật / công thức:** Bevel modifier `limit_method='ANGLE'` (30–40°), width = 2–5% bề dày chi
  tiết (hoặc ~1–3% kích thước vật), `segments=1..2`, `harden_normals=True`; nối tiếp Weighted Normal
  `keep_sharp=True` + shade smooth. Thứ tự stack chuẩn: Mirror → Array → Boolean → Solidify →
  **Bevel → Weighted Normal (CUỐI)**.
- **Nguồn:** https://github.com/studioigor/studioigor-skill/blob/HEAD/references/assets.md
  ("Bevel with limit_method=ANGLE, width 2–5% of the part's thickness, 1–2 segments, harden_normals;
  on top, Weighted Normal (keep_sharp) and smooth shading. Bevels catch the light, and low-poly stops
  looking cheap") + https://github.com/luminary19/atelier/blob/HEAD/skills/forge-model/references/modifier-stack.md
  (thứ tự stack là bất biến đúng-sai; WeightedNormal phải sau Bevel vì đọc face normal Bevel tạo ra;
  `harden_normals=True: critical`) + https://github.com/garyhtou/claude-plugins/blob/HEAD/plugins/high-fidelity-web/skills/building-3d-for-web/references/blender-procedural.md
  (bẫy: `bpy.ops.object.join()` chỉ giữ modifier của object active → apply từng object TRƯỚC join;
  pipeline build → apply modifiers → join → export; `export_apply=True` tự bake khi export).
- **Áp dụng:** áp cho khối kiến trúc hero (nhà lồng, khách sạn, cầu) ở vòng hình khối kế tiếp — cạnh
  bắt sáng là khác biệt dễ thấy nhất giữa "khối trơn" và chibi xịn. Chi phí đỉnh tăng theo segments:
  đo vert count trước/sau trên 1 mesh mẫu trước khi áp toàn cục; ngân sách byte đã được mục 1 gỡ
  (~1,32 MB headroom) nên chịu được segments=1 cho các khối chính.
- **Rủi ro:** bevel width quá tay trên chi tiết mỏng (lam, gờ zigzag) gây tự giao nhau — clamp overlap
  + chỉ áp theo danh sách mesh chọn lọc, không áp mù toàn scene.
- **Ưu tiên: THỬ NGHIỆM (vòng hình khối sau, sau khi pipeline nén ở mục 1 đã có).**

## 8. Nhân bản đều nhịp: Array / Mirror / linked-duplicate thay vì dựng tay từng khối

- **Kỹ thuật:** Array (Legacy) offset hằng số cho dãy lam/cột/ô cửa; Mirror dựng nửa mặt tiền đối
  xứng rồi nhân đôi; trong script bpy: tạo nhiều object **dùng chung một `obj.data`** (tương đương
  linked duplicate Alt+D) để exporter ghi 1 mesh nhiều node. Geometry Nodes Instance on Points thì
  **bắt buộc thêm node Realize Instances trước output** — exporter glTF bỏ qua instance GN thuần
  (trừ tuỳ chọn experimental); instance đã realize ≥5 bản có thể chuyển thành EXT_mesh_gpu_instancing
  bằng `gltf-transform instance`, three.js đọc native không cần decoder.
- **Nguồn:** https://www.zachsimms.com/3d/blender/buildings-scenes/ (bảng "What survives export":
  Array → "one merged mesh after Apply Modifiers"; GN instances → "dropped… Realize Instances as the
  last node"; linked duplicate → "glTF nodes sharing one mesh; with GPU Instances on,
  EXT_mesh_gpu_instancing") + https://github.com/rivendale/opensource/blob/HEAD/art/blender.md
  (đo thật: scatter 48 instance chưa realize export ra chỉ 2 tam giác — mất sạch; thêm Realize
  Instances → 578 tam giác đúng đủ).
- **Áp dụng:** dãy lam tầng 2, cột mặt tiền, 40 quầy nhà lồng, hàng sạp — mọi thứ lặp nhịp trong
  build_models.py nên đi qua 1 hàm dựng khối mẫu + nhân bản shared-data/array thay vì cộng khối rời
  từng cái (giảm cả thời gian build lẫn rủi ro lệch nhịp như vụ pano). Với đường cong V9: Array theo
  Curve (curve modifier) là phương án thay thế đáng thử cho các chi tiết bám cung thay vì tính tay.
- **Rủi ro:** quên realize/apply → mất chi tiết âm thầm khi export (chỉ phát hiện khi đếm tam giác —
  đưa "đếm tris trước/sau build" thành 1 dòng kiểm tra trong build log); Mirror quên apply transform
  scale âm gây lật normal.
- **Ưu tiên: THỬ NGHIỆM (áp dần khi chạm vào từng hệ chi tiết).**

## 9. Texture thủ tục/canvas: giữ nguyên tắc "0 texture nhúng trong GLB"

- **Hiện trạng đã đúng:** market.glb chứa 0 ảnh; mọi biển hiệu/pano/vết bẩn là CanvasTexture sinh
  lúc chạy trong JS — byte nằm ở code, không nằm ở file model, và FRONTAGE-1/FACADE-COLOR-1 đã chứng
  minh đường này đủ đẹp ở tầm game.
- **Nguồn:** https://app.cinevva.com/guides/optimize-glb-for-web (Step 1: texture thường chiếm ≥80%
  file ở model thường; WebP hoá 2,23 MB → 246 KB; KTX2 chỉ khác ở VRAM chứ không phải dung lượng tải)
  + https://meshoptimizer.org/gltf/ (gltfpack có `-tw` WebP / `-tc` KTX2 khi thật sự cần nhúng).
- **Áp dụng:** luật pipeline — cấm bake texture vào GLB của dự án này. Nếu một ngày phải nhúng:
  1 atlas chung ≤1024², encode WebP/JPEG (không PNG thô), và đo lại trần standalone trước.
  KTX2 tránh dùng: cần KTX2Loader (decoder phụ) — mâu thuẫn trần byte.
- **Ưu tiên: THAM KHẢO (giữ làm luật, không có việc làm ngay).**

---

## Trả lời trực diện: giảm market.glb đáng kể mà giữ nguyên hình — ĐƯỢC, đã đo

| Phương án | market.glb sau | Giảm | Đổi lại |
|---|---|---|---|
| Hiện tại | 1.652.360 B | — | — |
| `quantize` (mặc định) | **661.156 B** | **−60,0%** | 0 dòng code, 0 decoder |
| `quantize --quantize-normal 8` | **581.908 B** | **−64,8%** | cần soi banding tường phẳng |
| `meshopt --level high` | **386.152 B** | **−76,6%** | +1 import + 1 dòng setMeshoptDecoder (module 24.850 B trên CDN) |

Hình giữ nguyên theo nghĩa kiểm chứng được: số mesh/tam giác/đỉnh/UV/tên material **khớp tuyệt đối**
trước–sau (bảng kiểm ở mục 1); sai số vị trí lượng tử ~0,0055u trên khổ 90u — nhỏ hơn 1 pixel ở mọi
góc camera của game. Đây là nén "mất mát có kiểm soát", không phải giảm chất lượng hình học.

### Quy trình thử nghiệm an toàn (chạy trên bản sao, không đụng bản đang chạy)

1. `cp assets/market.glb /tmp/glbtest/orig.glb` → chạy 3 lệnh quantize/meshopt ra file riêng, ghi byte.
2. Diff cấu trúc bằng parser GLB (script đã dùng ở vòng này): meshes/tris/verts/primsWithUV/material-names
   phải khớp 100%; extension mới chỉ được là KHR_mesh_quantization (± EXT_meshopt_compression).
3. Đóng standalone thử bằng bản GLB mới trong thư mục GAME_ROOT riêng → chạy đủ 8 cổng
   (diag 900 · SEED_SAVE 300 · standalone diag 300 · traffic 26/26 · audit · test_bd2 · check_sweep3 · test_real1).
4. Render mặt tiền bằng GLB mới (render_facade_real.py trỏ sang file test, view ACES 1.3 như mục 6),
   ghép cạnh render bản cũ + ảnh thật 01; lấy median PIL vài vùng vật liệu — lệch màu phải = 0
   (quantize không đụng material), chỉ được khác ở mức nhiễu render.
5. Đạt cả 3 lớp mới thay vào `assets/` (giữ `.bak-quantize-<ngày>`), đóng gói lại, chạy lại 8 cổng
   trên bản chính, rồi mới đẩy GitHub như nhịp hiện tại.
6. Rollback = chép .bak đè lại + đóng gói lại; GLB gốc luôn là nguồn sự thật, file nén chỉ là sản phẩm đóng gói.

## Bảng ưu tiên tổng

| # | Kỹ thuật | Ưu tiên |
|---|---|---|
| 1 | Quantization KHR_mesh_quantization (−60% market, 0 code) | **Áp ngay vòng sau** |
| 3 | Luật cấm xoá TEXCOORD_0 (TEX_GRIME cần UV) | **Áp ngay (luật)** |
| 4 | Khoá tham số export tường minh trong build_models.py | **Áp ngay** |
| 5 | Bật Denoise OIDN trong script render nghiệm thu | **Áp ngay** |
| 6 | View transform ACES 1.3 + exposure −0,18 khi chấm màu | **Áp ngay** |
| 2 | Meshopt −76,6% (decoder 24.850 B) | Thử nghiệm sau #1 |
| 7 | Bevel 1–2 seg + Weighted Normal cho khối hero | Thử nghiệm |
| 8 | Array/Mirror/shared-data cho chi tiết lặp nhịp | Thử nghiệm |
| 9 | Luật 0 texture nhúng; WebP nếu bắt buộc nhúng | Tham khảo |
| — | Simplify cho market (27k tris đã thấp) / Draco (decoder quá nặng) | Không làm |
