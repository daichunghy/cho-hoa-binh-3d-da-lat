# TÀI LIỆU KỸ THUẬT: ĐẶC TẢ MÔI TRƯỜNG & HỆ THỐNG NPC CHỢ ĐÊM ĐÀ LẠT

Tài liệu chuẩn hóa đầu vào (System Prompt / Context Spec) dùng cho AI Agent, Game Engine hoặc Mô hình Mô phỏng Thế giới.

## 1. THIẾT LẬP MÔI TRƯỜNG & KHÍ QUYỂN (ATMOSPHERIC & ENVIRONMENTAL ENGINE)

### 1.1. Tham số Khí tượng & Vật lý Môi trường
- Địa điểm: Đường Nguyễn Thị Minh Khai, Phường 1, TP. Đà Lạt, Tỉnh Lâm Đồng (Khu vực chợ trung tâm).
- Thời gian thiết lập (Time of Day): $19:30 - 21:30$ (Khung giờ mật độ đông nhất).
- Nhiệt độ môi trường ($T$): $15^\circ\text{C} - 16.5^\circ\text{C}$.
- Độ ẩm không khí ($RH$): $88\% - 94\%$.
- Hiện tượng thời tiết:
  - Mưa phùn hạt mịn (drizzle), vận tốc rơi chậm, nghiêng góc $10^\circ - 15^\circ$ theo gió sườn núi.
  - Sương mù mỏng (light mist), tầm nhìn xa hiệu dụng $40\text{m} - 60\text{m}$.
- Cảm biến nhiệt học (Thermal FX):
  - Hiệu ứng ngưng tụ hơi thở: NPC thở ra luồng hơi nước mỏng màu trắng xám mỗi chu kỳ $2.5 - 3.5$ giây khi giao tiếp hoặc thở dốc.
  - Vùng nhiệt cục bộ (Thermal pockets): Nhiệt độ tăng vọt lên $35^\circ\text{C} - 45^\circ\text{C}$ trong bán kính $0.8\text{m}$ quanh các lò than củi và nồi hấp xôi/sữa.

### 1.2. Thuộc tính Bề mặt & Ánh sáng (Shaders & Lighting Profiles)
- Bề mặt đường nhựa ướt (Wet Asphalt PBR Shader):
  - Base Color: #121214 (Đen xám than ẩm ướt).
  - Roughness: $0.08 - 0.15$ tại các vệt lún bánh xe đọng nước; $0.55 - 0.65$ tại các gờ đá viền vỉa hè.
  - Specular: $0.75 - 0.90$, tạo độ phản chiếu hình ảnh phản chiếu gương (mirror reflection) của ánh đèn led, biển hiệu Dalat Center và đèn pha xe máy.
- Hồ quang & Nguồn sáng:
  - Ánh sáng lều bạt: Đèn huỳnh quang / compact led treo trần bạt, nhiệt độ màu $6500\text{K}$ (trắng lạnh), quang thông $1200\text{lm}$, dây điện trần quấn quanh thanh sắt.
  - Ánh sáng ẩm thực than củi: Ánh lửa đỏ cam lập lòe (flickering), nhiệt độ màu $1800\text{K} - 2200\text{K}$, tần số dao động cường độ $3\text{Hz} - 8\text{Hz}$.
  - Ánh sáng biển hiệu cố định: Đèn pha rọi vàng ấm $3000\text{K}$ từ các chuỗi cửa hàng đặc sản L'angFarm và khách sạn xung quanh.
  - Nguồn sáng động: Bóng bay phát sáng gắn led dây đa sắc ($RGB$), chớp nháy di động ở độ cao $1.6\text{m} - 2.0\text{m}$.

## 2. BẢN ĐỒ KHÔNG GIAN & PHÂN VÙNG HÌNH HỌC (3D SPATIAL ZONING)

```
[Khu Vực Bậc Thang Hòa Bình]
         │ (Độ dốc 28°, bậc đá xám, tụ điểm sữa nóng & bánh tráng)
         ▼
[Vòng Xoay Bùng Binh Bờ Hồ / Dalat Center]
         │ (Giao thông hỗn hợp: Taxi, xe máy, khách bộ hành)
         ▼
[Cổng Chào Led: "CHỢ ĐÊM ĐÀ LẠT"]
         │ (Trục đường nhựa Nguyễn Thị Minh Khai rộng 15m)
         ▼
[Trục Phố Đi Bộ & Nhà Lồng Chợ]
 ├── Lề Trái: Dãy sạp đồ len, đồ lưu niệm, đặc sản sấy khô
 ├── Lòng Đường: Xe đẩy dâu lắc, lạp xưởng nướng đá, hạt dẻ cuội
 └── Lề Phải: Quầy ẩm thực ngồi bệt, quán ốc, xiên que nướng
```

- **Phân vùng 1: Bậc thang đá Chợ Đà Lạt (The Steps)**
  - Hình học: 45 bậc đá granit thô nhám, độ dốc trung bình $28^\circ$, chia làm 3 nhịp nghỉ lớn.
  - Mật độ vật cản: Dày đặc. Mỗi bậc thềm được tiểu thương tận dụng đặt 1 bếp nướng hoặc 1 mâm bánh.
  - Chỗ ngồi: Ghế nhựa đẩu lùn Song Long / Duy Tân cao $20\text{cm}$ (xanh dương, đỏ) hoặc các tấm bìa carton cắt rời kích thước $40 \times 40\text{cm}$ lót trực tiếp lên mặt đá lạnh.
- **Phân vùng 2: Vòng xoay giao thông trung tâm (The Roundabout)**
  - Cấu trúc: Đảo giao thông hình tròn với thảm hoa cỏ ẩm ướt ở giữa.
  - Tương tác: Điểm nghẽn giao thông. Dòng người đi bộ từ các bậc thang tràn xuống cắt ngang đầu xe taxi Vinasun, Mai Linh đang lùi hoặc rẽ; xe máy của người địa phương luồn lách ở vận tốc thấp ($10 - 15\text{km/h}$).
- **Phân vùng 3: Phố đi bộ Nguyễn Thị Minh Khai**
  - Hạ tầng ki-ốt: Các quầy di động kích thước chuẩn $2.0\text{m} \times 2.0\text{m} \times 2.2\text{m}$. Khung thép hộp $20 \times 20\text{mm}$, phủ bạt dù sọc xanh trắng hoặc bạt chống nước màu xanh dương.
  - Tuyến lưu thông: Lối đi bộ trung tâm rộng $6\text{m} - 8\text{m}$, mặt đường nhựa láng ướt, người đi bộ tản mát hai bên để tiếp cận quầy thử đặc sản.

## 3. THIẾT KẾ ĐẠO CỤ VI MÔ & QUY TRÌNH CHẾ BIẾN (MICRO-PROPS SPEC)

### 3.1. Sạp Bánh Tráng Nướng (Vietnamese Pizza Station)
- Đạo cụ vật lý (Physical Props):
  - Lò nướng: Lò đất nung đỏ đường kính $25\text{cm}$, bên trong chứa than hoa đượm tàn trắng, phủ trên là vỉ nướng thép mắt cáo $30 \times 30\text{cm}$ dính muội than đen.
  - Dụng cụ: Quạt nan tre viền vải rách mép, kéo bấm kim loại dài $25\text{cm}$, muỗng inox cán ngắn.
- Nguyên liệu tại chỗ:
  - Xô nhựa nhỏ chứa hành lá xắt nhuyễn ngâm dầu thực vật.
  - Hộp bơ thực vật Tường An màu vàng đã dùng vơi 1/2.
  - 2 vỉ trứng cút (mỗi vỉ 30 quả) và 1 rổ trứng gà so.
  - Các lọ nhựa tròn đựng tép khô nhuộm màu cam, hành phi giòn, xúc xích Đức cắt lát tròn dày $3\text{mm}$, bò khô xé sợi.
  - Chai xốt xịt: Chai tương ớt đỏ nắp nhọn, chai mayonnaise trắng đục có vân xốt dính quanh miệng.
- Quy trình logic chế biến (Cooking State Transition):
  - PUT_RICE_PAPER: Đặt bánh tráng tròn mỏng lên tâm vỉ than.
  - SPREAD_BASE: Múc 1 muỗng mỡ hành + 1 muỗng bơ, dùng lưng muỗng quét xoay tròn đều mặt bánh.
  - CRACK_EGG: Đập 2 quả trứng cút (hoặc 1 trứng gà), dùng muỗng khuấy dầm nát lòng đỏ trên mặt bánh trong 5 giây.
  - ADD_TOPPINGS: Rải nhúm tép khô, hành phi, xúc xích lát đều khắp chu vi.
  - ROTATION: Dùng tay không cầm mép bánh tráng xoay liên tục góc $45^\circ$ mỗi 2 giây để tránh cháy cục bộ.
  - SAUCE_AND_FOLD: Xịt tương ớt + sốt béo hình ziczac; dùng kéo gập đôi bánh tráng lại thành hình bán nguyệt.
  - WRAP: Kẹp nửa bánh vào tờ giấy báo cũ hoặc giấy kraft vuông $15 \times 15\text{cm}$, trao cho thực khách.

### 3.2. Quầy Sữa Đậu Nành Nóng & Bánh Ngọt (Hot Soy Milk Hub)
- Đạo cụ vật lý:
  - Bàn gấp inox $70 \times 120\text{cm}$ phủ khăn trải bàn nilon hoa văn mờ.
  - 3 ấm nhôm lớn (dung tích 7 lít) đun trực tiếp trên 3 kiềng bếp ga mini: Ấm 1 (Sữa đậu nành nguyên chất), Ấm 2 (Sữa đậu xanh), Ấm 3 (Sữa bắp hoặc sữa đậu phộng). Nắp ấm liên tục rung lách cách do áp suất sôi.
  - Tủ kính khung nhôm 2 tầng: Tầng dưới xếp bánh tiêu mè, bánh quẩy dài $15\text{cm}$ vàng ươm; tầng trên xếp bánh su kem, bánh sừng trâu.
  - Ly thủy tinh có quai lùn $220\text{ml}$, rổ đựng ống hút nhựa và muỗng nhựa ngắn.
- Tương tác phục vụ: Múc sữa bằng muôi nhôm dài, rót từ độ cao $20\text{cm}$ xuống ly để tạo bọt trắng mịn, bỏ thêm $1.5$ muỗng đường cát trắng theo yêu cầu của khách.

### 3.3. Xe Lạp Xưởng Nướng Sỏi Đá (Stone-Grilled Sausage Cart)
- Cơ chế: Chảo gang lòng nông đường kính $45\text{cm}$ đặt trên lò điện/than.
- Bề mặt nướng: Lớp sỏi cuội đen bóng đường kính $3 - 5\text{cm}$ phủ đều mặt chảo, ngấm mỡ lạp xưởng bóng nhẫy bốc khói cay nồng mùi quế hồi.
- Vật phẩm: 15 cây lạp xưởng tươi vỏ đỏ au xếp nan quạt trên mặt đá, phát ra tiếng mỡ rỉ xèo xèo.

### 3.4. Điểm Bán Dâu Tây Lắc & Nông Sản Tươi
- Đạo cụ:
  - Rổ tre đan đựng quả dâu tây tươi giống Mỹ đá, quả nhỏ hình nón, cuống xanh tươi.
  - Hũ thủy tinh lớn đựng muối ớt Tây Ninh trộn xí muội màu cam đỏ thẫm.
  - Ly nhựa trong PP $500\text{ml}$ có nắp cầu: Chứa dâu tây bổ đôi lắc đều muối ớt, kèm 1 cây xiên tre nhọn cắm sẵn giữa ly.
  - Khay nhựa thử mứt: Chia 6 ô chứa mẫu thử hồng treo gió, khoai lang dẻo, mứt dâu tằm, tăm tre cắm sẵn.

## 4. HỆ THỐNG NPC VÀ MÔ HÌNH HÀNH VI (BEHAVIOR TREES & FSM)

### 4.1. NPC Người Bán Hàng (Vendor State Machine)

```
       ┌────────────────────────┐
       │      STATE: IDLE       │ ◄─────────────────────────┐
       │ (Quạt than, nhìn dòng) │                           │
       └───────────┬────────────┘                           │
                   │ Khách dừng lại / gọi                   │
                   ▼                                        │
       ┌────────────────────────┐                           │
       │     STATE: ENGAGE      │                           │
       │ ("Ăn bánh gì người     │                           │
       │   đẹp ơi?")            │                           │
       └───────────┬────────────┘                           │ Giao dịch
                   │ Khách chọn món                         │ hoàn tất
                   ▼                                        │
       ┌────────────────────────┐                           │
       │     STATE: COOKING     │                           │
       │ (Chuỗi 7 bước nướng    │                           │
       │  bánh tráng / rót sữa) │                           │
       └───────────┬────────────┘                           │
                   │ Chế biến xong                          │
                   ▼                                        │
       ┌────────────────────────┐                           │
       │    STATE: DELIVER      │                           │
       │ (Kẹp giấy báo, nhận    │                           │
       │  tiền / chỉ mã QR)     │ ──────────────────────────┘
       └────────────────────────┘
```

- Hội thoại mẫu (Voice Bank):
  - CALL_01: "Bánh tráng nướng hột gà, xúc xích phô mai nóng hổi đây em ơi!"
  - CALL_02: "Sữa đậu nành bò, đậu xanh nóng không người đẹp? Ngồi ghế đi em."
  - PAYMENT_01: "Bánh đặc biệt ba lăm ngàn em nha. Quét mã dán trên thùng xốp kìa."
  - BARGAIN_REJECT: "Đồ len đan tay này bán đúng giá rồi người đẹp ơi, lạnh vầy không bớt được đâu."

### 4.2. NPC Khách Du Lịch (Tourist Behavior Tree)
- Hình thức (Visual Asset):
  - Trang phục: Áo phao chần bông, áo khoác dạ dài quá gối, quàng khăn len to bản, đầu đội mũ len beanie; hai tay xỏ túi áo khoác.
  - Phụ kiện cầm tay: Dù trong suốt che mưa nhẹ, hoặc 1 tay cầm ly dâu lắc/ly sữa nóng bằng cốc giấy.
- Chu kỳ hành vi (Behavior Loop):
  - Tốc độ di chuyển: $0.7 - 0.9\text{m/s}$ (đi dạo chậm, né tránh các vũng nước đọng).
  - Hành vi tại chỗ khi dừng:
    - Cúi người, hai bàn tay áp sát miệng lò than của tiểu thương để sưởi ấm, đầu gật gù trò chuyện.
    - Rút điện thoại thông minh chụp ảnh góc chéo món ăn bốc khói.
    - Vừa nhai, vừa phà hơi thở lạnh ngắt quãng.

## 5. THIẾT KẾ ÂM THANH KHÔNG GIAN (SPATIAL AUDIO MATRIX)

| Tầng âm thanh (Layer) | Tần số / Biên độ | Mô tả nguồn phát | Vị trí không gian |
|---|---|---|---|
| Ambience: Rain & Wet | $200\text{Hz} - 8\text{kHz}$ / $-24\text{dB}$ | Tiếng mưa phùn lộp độp trên mái bạt nilon, tiếng bánh xe taxi lăn trên mặt đường nhựa ướt sũng. | Toàn không gian (Omnidirectional) |
| Ambience: Crowd Murmur | $400\text{Hz} - 2.5\text{kHz}$ / $-18\text{dB}$ | Tạp âm hàng trăm người trò chuyện xì xào, tiếng cười rúc rích, tiếng bước chân ủng cao su. | Toàn không gian |
| Point SFX: Kitchen Tools | $1.2\text{kHz} - 6\text{kHz}$ / $-12\text{dB}$ | Tiếng kéo kim loại bấm "tách tách" khi cắt bánh; tiếng muỗng gõ vào thành ly thủy tinh "keng". | Tọa độ quầy sạp ($x, y, z$) |
| Point SFX: Sizzling & Coal | $500\text{Hz} - 4\text{kHz}$ / $-15\text{dB}$ | Tiếng mỡ sôi xèo xèo trên đá nướng; than củi nổ lách tách khô giòn. | Tọa độ bếp than ($x, y, z$) |
| Point SFX: Chestnut Roaster | $150\text{Hz} - 1.8\text{kHz}$ / $-14\text{dB}$ | Tiếng lồng sắt chứa hạt dẻ và sỏi đen quay rào rạo đều đặn theo nhịp mô-tơ. | Quầy hạt dẻ xe đẩy |
| Foley: Pedestrians | $100\text{Hz} - 800\text{Hz}$ / $-20\text{dB}$ | Tiếng giày ma sát nền ướt dính, tiếng vải nilon áo phao cọ xát xoẹt xoẹt khi bước đi. | Quanh vị trí Camera/Player |

## 6. BỘ SCHEMA JSON ĐẦU VÀO CHO AI AGENT (RAW SYSTEM CONFIG)

```json
{
  "simulation_id": "dalat_night_market_realistic_v2",
  "world_metadata": {
    "location": "Dalat Night Market, Nguyen Thi Minh Khai St",
    "timestamp": "20:00:00",
    "weather": {
      "temperature_celsius": 16.0,
      "humidity_percentage": 92,
      "precipitation": "drizzle",
      "wind_speed_kmh": 6.5,
      "fog_density": 0.035
    },
    "visual_shader_flags": {
      "wet_asphalt_reflection": true,
      "dynamic_puddle_ripples": true,
      "smoke_dispersion_horizontal": true,
      "breath_condensation_particles": true
    }
  },
  "spatial_nodes": [
    {
      "node_id": "zone_stairs",
      "type": "staircase",
      "slope_degree": 28,
      "dominant_smell": "wood_smoke_and_grilled_butter",
      "dominant_props": ["plastic_stools_20cm", "clay_stoves", "carton_seat_pads"],
      "allowed_vendor_types": ["banh_trang_nuong", "soy_milk_stalls"]
    },
    {
      "node_id": "zone_roundabout",
      "type": "traffic_circle",
      "traffic_density": "high_mixed",
      "dominant_audio": "scooter_engines_taxi_horns_wet_tires",
      "structures": ["dalat_center_facade", "sandals_flora_hotel", "water_fountain"]
    },
    {
      "node_id": "zone_walking_street",
      "type": "commercial_pedestrian",
      "width_meters": 15.0,
      "booth_dimensions": {"w": 2.0, "l": 2.0, "h": 2.2},
      "dominant_vendors": ["strawberry_shake", "wool_clothing", "dried_persimmon", "stone_sausage"]
    }
  ],
  "agent_inventory_database": {
    "banh_trang_nuong_station": {
      "heat_source": "charcoal_clay_pot_25cm",
      "ingredients": [
        {"item": "rice_paper", "spec": "thin_round_22cm"},
        {"item": "quail_eggs", "unit_per_service": 2},
        {"item": "scallion_oil", "container": "plastic_tub"},
        {"item": "tuong_an_margarine", "status": "half_used"},
        {"item": "dried_shrimp_flake", "color": "orange_dyed"},
        {"item": "mayonnaise_chili_sauce", "dispenser": "squeeze_bottles"}
      ],
      "serving_paper": "recycled_newspaper_sheet_15x15cm",
      "base_price_vnd": 30000
    },
    "soy_milk_station": {
      "pots": [
        {"type": "soybean", "capacity_liters": 7, "state": "simmering"},
        {"type": "mung_bean", "capacity_liters": 7, "state": "simmering"}
      ],
      "pastries": ["tieu_cake", "fried_dough_stick", "cream_puff"],
      "base_price_vnd": 15000
    }
  },
  "npc_profiles": [
    {
      "role": "Vendor_BanhTrang",
      "voice_tone": "high_pitch_friendly_southern_vietnamese",
      "catchphrases": [
        "Bánh tráng nướng nóng hổi người đẹp ơi!",
        "Ngồi đi em, hai phút có liền nha."
      ],
      "idle_animations": ["fanning_coal_fire", "wiping_counter_with_rag"],
      "reaction_to_cold": "blows_warm_air_into_hands_when_no_customers"
    },
    {
      "role": "Tourist_Couple",
      "clothing": ["puffer_jacket", "wool_scarf", "beanie_hat"],
      "movement_speed_mps": 0.8,
      "interaction_states": ["shivering_near_stove", "taking_food_photos", "eating_drizzled_strawberries"]
    }
  ]
}
```

---

*Nguồn: tài liệu Chung Hy cung cấp 19:25 ngày 13/11/2026 (lưu nguyên văn). Lưu ý khi agent dùng: một số thông số trong tài liệu (ví dụ 45 bậc thang, trục đường rộng 15m, cổng chào LED "CHỢ ĐÊM ĐÀ LẠT", giá 30.000đ/35.000đ) chưa đối chiếu với số đo khóa của dự án (vị trí khóa GEOMETRY-2, bảng tỉ lệ XH-3R, kinh tế Xu Chợ hiện hành) — trước khi áp vào game phải rà chéo với research/28, research/32 và V4-CHECKLIST, giữ nguyên các khóa đã chốt của dự án.*
