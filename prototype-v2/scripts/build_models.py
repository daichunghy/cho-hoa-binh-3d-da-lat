# -*- coding: utf-8 -*-
"""
Dựng MODEL 3D chi tiết cho Chợ Hòa Bình 3D Đà Lạt (prototype v2).
Quy ước trục Blender: X = ngang, Y = sâu (trước/sau), Z = cao. 1 đơn vị = 1m.
Quy ước mặt tiền khi export glTF (glTF.z = -blender.y):
  - market : tiền ở +Y blender  -> three -Z (hướng ra đường)
  - theater, cafe, stall, character : tiền ở -Y blender -> three +Z
Mỗi model export 1 file .glb vào ../assets/
"""
import bpy, math, os, random
from mathutils import Matrix, Vector

random.seed(42)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
OUT = os.path.normpath(OUT)
os.makedirs(OUT, exist_ok=True)

# ---------------- materials ----------------
MATS = {}
def M(name, color, rough=0.9, metal=0.0, emit=None, ei=0.0):
    if name in MATS: return MATS[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Metallic"].default_value = metal
    if emit is not None:
        bsdf.inputs["Emission Color"].default_value = (*emit, 1.0)
        bsdf.inputs["Emission Strength"].default_value = ei
    MATS[name] = m
    return m

def mats_init():
    M("WallCream",  (0.88,0.79,0.62), 0.95)
    M("WallBrick",  (0.62,0.40,0.28), 0.97)
    M("FacadeOld",  (0.66,0.38,0.27), 0.97)
    M("TrimBrown",  (0.50,0.30,0.19), 0.9)
    M("RoofTile",   (0.55,0.28,0.20), 0.95)
    M("Concrete",   (0.62,0.59,0.53), 0.95)
    M("ConcreteDk", (0.45,0.42,0.38), 0.95)
    M("Stone",      (0.55,0.51,0.46), 0.98)
    M("Wood",       (0.55,0.38,0.22), 0.9)
    M("WoodDark",   (0.38,0.26,0.16), 0.9)
    M("WoodLight",  (0.68,0.52,0.34), 0.9)
    M("Glass",      (0.50,0.65,0.68), 0.3, 0.05)
    M("GlassDark",  (0.13,0.16,0.17), 0.4, 0.2)
    M("CafeWin",    (0.85,0.62,0.30), 0.5, 0.0, emit=(0.80,0.45,0.12), ei=0.0)
    M("MarketWin",  (0.98,0.80,0.52), 0.5, 0.0, emit=(1.0,0.62,0.25), ei=0.0)
    M("SignBoard",  (0.24,0.16,0.11), 0.85)
    M("Gold",       (0.85,0.66,0.30), 0.5, 0.3)
    M("Awning",     (0.55,0.45,0.35), 0.95)   # web sẽ tô lại theo district
    M("CanvasOld",  (0.72,0.66,0.55), 0.98)
    M("Shirt",      (0.45,0.38,0.30), 0.95)   # web sẽ tô lại
    M("Pants",      (0.25,0.24,0.22), 0.95)   # web sẽ tô lại
    M("Skin",       (0.93,0.71,0.56), 0.85)
    M("Blush",      (0.96,0.63,0.56), 0.9)
    M("HairDark",   (0.10,0.08,0.07), 0.9)
    M("Straw",      (0.80,0.68,0.42), 0.95)
    M("Beanie",     (0.48,0.20,0.16), 0.98)
    M("CapBlue",    (0.23,0.30,0.38), 0.95)
    M("Scarf",      (0.85,0.63,0.19), 0.98)
    M("Shoe",       (0.16,0.13,0.11), 0.9)
    M("PineDark",   (0.22,0.40,0.22), 0.98)
    M("PineMid",    (0.28,0.48,0.26), 0.98)
    M("PineLight",  (0.37,0.57,0.32), 0.98)
    M("Trunk",      (0.32,0.24,0.16), 0.98)
    M("MetalDark",  (0.22,0.21,0.20), 0.55, 0.5)
    M("LampGlow",   (1.0,0.85,0.55), 0.4, 0.0, emit=(1.0,0.65,0.25), ei=0.0)
    M("LanternGlow",(1.0,0.62,0.25), 0.6, 0.0, emit=(1.0,0.55,0.20), ei=0.9)
    M("PotMetal",   (0.32,0.32,0.34), 0.5, 0.25)
    M("GoodsA",     (0.85,0.45,0.15), 0.85)
    M("GoodsB",     (0.65,0.25,0.20), 0.85)
    M("GoodsC",     (0.90,0.72,0.35), 0.85)
    M("Soil",       (0.30,0.24,0.18), 1.0)
    M("LeafGreen",  (0.38,0.52,0.30), 0.98)
    M("BanhTrang",  (0.92,0.82,0.60), 0.9)
    M("CoffeeDark", (0.16,0.10,0.06), 0.55)
    M("CharGlow",   (0.95,0.35,0.10), 0.7, 0.0, emit=(0.95,0.30,0.08), ei=0.8)
    for i, c in enumerate([(0.72,0.32,0.40),(0.85,0.60,0.22),(0.65,0.28,0.38),
                           (0.88,0.86,0.82),(0.75,0.42,0.22),(0.55,0.35,0.55)]):
        M("Flower%d" % i, c, 0.9)

# ---------------- helpers ----------------
def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for d in (bpy.data.meshes, bpy.data.curves):
        pass

def finish_obj(obj, mat=None, bevel=0.0):
    if mat: obj.data.materials.append(mat)
    if bevel > 0:
        mod = obj.modifiers.new("bev", 'BEVEL')
        mod.width = bevel; mod.segments = 2
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier=mod.name)
    obj.select_set(False)
    return obj

def box(name, dims, loc, mat=None, bevel=0.02, rot=None):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    o = bpy.context.object; o.name = name
    o.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if rot: o.rotation_euler = rot
    return finish_obj(o, mat, bevel)

def cyl(name, r1, r2, h, loc, mat=None, verts=14, bevel=0.01, rot=None):
    bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r2, radius2=r1, depth=h, location=loc)
    o = bpy.context.object; o.name = name
    if rot: o.rotation_euler = rot
    return finish_obj(o, mat, bevel)

def cone(name, r, h, loc, mat=None, verts=12, bevel=0.0):
    return cyl(name, 0.01, r, h, loc, mat, verts, bevel)

def sphere(name, r, loc, mat=None, scale=(1,1,1)):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=loc, segments=14, ring_count=10)
    o = bpy.context.object; o.name = name; o.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finish_obj(o, mat, 0.0)

def torus(name, R, tube, loc, mat=None, rot=None, scale=(1,1,1)):
    bpy.ops.mesh.primitive_torus_add(major_radius=R, minor_radius=tube, major_segments=18, minor_segments=8, location=loc)
    o = bpy.context.object; o.name = name; o.scale = scale
    if rot: o.rotation_euler = rot
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finish_obj(o, mat, 0.0)

def join_into(objs, name):
    """Join objs[1:] into objs[0]; kết quả giữ origin của objs[0], đổi tên."""
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs: o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.object.join()
    o = bpy.context.object; o.name = name
    o.select_set(False)
    return o

def export(name):
    path = os.path.join(OUT, name + ".glb")
    bpy.ops.export_scene.gltf(filepath=path, export_format='GLB', export_apply=True)
    print("EXPORTED", path, os.path.getsize(path))

mats_init()

# ============================================================
#  NHÂN VẬT CHIBI (chuẩn Niệm Phật Online): đầu to tròn ~45% chiều cao, thân nhỏ,
#  mặt đơn giản dễ thương (mắt chấm + má hồng + miệng nhỏ). Part riêng có pivot
#  tại khớp (hông/vai) để web vung tay/chân. Mặt hướng -Y blender (= +Z three).
# ============================================================
def build_character():
    clear_scene()
    skin, shirt, pants = MATS["Skin"], MATS["Shirt"], MATS["Pants"]
    # --- chân ngắn: pivot tại hông z=0.50, geometry dịch xuống -0.20 ---
    for side, sx in (("L", -0.12), ("R", 0.12)):
        leg = box("tmpLeg", (0.20, 0.22, 0.52), (sx, 0, 0.50), pants, 0.05)
        leg.data.transform(Matrix.Translation((0, 0, -0.20)))
        shoe = box("tmpShoe", (0.22, 0.36, 0.12), (sx, -0.06, 0.06), MATS["Shoe"], 0.04)
        join_into([leg, shoe], "Leg" + side)
    # --- thân nhỏ bo tròn: hộp bo lớn + bụng cầu dẹt ---
    torso = box("tmpTorso", (0.62, 0.34, 0.55), (0, 0, 0.82), shirt, 0.10)
    belly = sphere("tmpBelly", 0.30, (0, -0.02, 0.80), shirt, scale=(1.05, 0.68, 0.92))
    join_into([torso, belly], "Torso")
    collar = torus("tmpCollar", 0.16, 0.05, (0, 0, 1.08), shirt, scale=(1, 0.85, 0.7))
    # --- tay ngắn: pivot tại vai z=1.02, geometry dịch xuống -0.18 ---
    for side, sx in (("L", -0.38), ("R", 0.38)):
        arm = box("tmpArm", (0.15, 0.17, 0.48), (sx, 0, 1.02), shirt, 0.06)
        arm.data.transform(Matrix.Translation((0, 0, -0.18)))
        hand = sphere("tmpHand", 0.085, (sx, 0, 1.02 - 0.42), skin)
        join_into([arm, hand], "Arm" + side)
    # --- ĐẦU TO TRÒN r=0.42 (1.06..1.90): da + tóc + mắt chấm + má hồng + miệng ---
    head = sphere("Head", 0.42, (0, 0, 1.48), skin)
    hair = sphere("tmpHair", 0.435, (0, 0.045, 1.53), MATS["HairDark"], scale=(1, 1, 0.9))
    nose = cone("tmpNose", 0.035, 0.07, (0, -0.415, 1.46), skin, verts=8)
    nose.rotation_euler = (-math.pi/2, 0, 0)
    mouth = sphere("tmpMouth", 0.022, (0, -0.408, 1.40), MATS["HairDark"], scale=(1.6, 0.5, 0.9))
    parts = [head, hair, nose, mouth]
    for sx in (-0.40, 0.40):
        parts.append(sphere("tmpEar", 0.075, (sx, 0, 1.44), skin, scale=(0.5, 0.85, 0.95)))
    for sx in (-0.15, 0.15):
        parts.append(sphere("tmpEye", 0.045, (sx, -0.385, 1.52), MATS["HairDark"]))
    for sx in (-0.26, 0.26):
        parts.append(sphere("tmpCheek", 0.055, (sx, -0.315, 1.40), MATS["Blush"], scale=(1, 0.4, 0.8)))
    join_into(parts, "Head")
    # --- mũ nón lá vành rộng phủ đầu to ---
    brim = cone("tmpNonLa", 0.68, 0.34, (0, 0, 1.86), MATS["Straw"], verts=18)
    tip = sphere("tmpNonLaTip", 0.06, (0, 0, 2.05), MATS["WoodDark"])
    join_into([brim, tip], "HatNonLa")
    # --- mũ beanie len + pom (đội cao hơn đỉnh đầu 1.90) ---
    dome = sphere("tmpBeanie", 0.45, (0, 0, 1.56), MATS["Beanie"], scale=(1, 1, 0.85))
    ring = cyl("tmpBeanieRing", 0.455, 0.465, 0.12, (0, 0, 1.42), MATS["Beanie"], verts=18)
    pom = sphere("tmpPom", 0.10, (0, 0, 2.00), MATS["CanvasOld"])
    join_into([dome, ring, pom], "HatBeanie")
    # --- mũ lưỡi trai ---
    capdome = sphere("tmpCap", 0.44, (0, 0, 1.58), MATS["CapBlue"], scale=(1, 1, 0.78))
    capbrim = box("tmpCapBrim", (0.36, 0.26, 0.045), (0, -0.46, 1.44), MATS["CapBlue"], 0.02)
    join_into([capdome, capbrim], "HatCap")
    # --- khăn quàng (chỉ nhân vật chính bật) ---
    scarf = torus("Scarf", 0.26, 0.09, (0, 0, 1.10), MATS["Scarf"], scale=(1, 0.95, 0.8))
    tail = box("tmpScarfTail", (0.17, 0.05, 0.34), (0.17, -0.20, 0.94), MATS["Scarf"], 0.03)
    join_into([scarf, tail], "Scarf")
    bpy.data.objects["Scarf"].hide_viewport = False
    export("character")

# ============================================================
#  GIAN HÀNG — khung gỗ, mái bạt võng, quầy có nan, sọt hàng, nồi (Pot*)
#  Mặt tiền (phía khách) ở -Y blender (= +Z three). Kích thước ~4.2 x 2.6, cao 2.75
# ============================================================
def build_stall():
    clear_scene()
    wood, woodD, woodL = MATS["Wood"], MATS["WoodDark"], MATS["WoodLight"]
    # 4 cột + xà ngang
    for sx in (-1.6, 1.6):
        for sy in (-0.85, 0.85):
            box("Post", (0.12, 0.12, 2.6), (sx, sy, 1.3), wood, 0.02)
    box("BeamF", (3.4, 0.10, 0.10), (0, -0.85, 2.52), wood, 0.02)
    box("BeamB", (3.4, 0.10, 0.10), (0,  0.85, 2.52), wood, 0.02)
    # quầy: thân + mặt quầy + nan trang trí mặt tiền + vách sau thấp
    box("Counter", (3.4, 1.5, 1.05), (0, 0, 0.53), woodL, 0.03)
    box("CounterTop", (3.6, 1.7, 0.10), (0, 0, 1.10), woodD, 0.02)
    for i in range(7):
        box("Slat", (0.10, 0.04, 0.80), (-1.35 + i * 0.45, -0.77, 0.55), woodD, 0.01)
    box("BackWall", (3.4, 0.25, 0.75), (0, 0.95, 0.38), wood, 0.02)
    box("Shelf", (3.2, 0.5, 0.07), (0, 0.82, 1.55), woodL, 0.01)
    for sx in (-1.45, 1.45):
        box("ShelfPost", (0.08, 0.08, 0.5), (sx, 0.82, 1.32), wood, 0.01)
    # mái bạt VÕNG (lưới grid biến dạng sin) + lớp mái phụ
    for k, (w, d, zc, sag, tilt) in enumerate([(4.2, 2.9, 2.66, 0.17, 0.10), (4.2, 2.6, 2.44, 0.13, -0.08)]):
        bpy.ops.mesh.primitive_grid_add(x_subdivisions=12, y_subdivisions=8, size=2.0, location=(0, -0.1 * k, zc))
        roof = bpy.context.object; roof.name = "Awning" if k == 0 else "Awning2"
        roof.scale = (w / 2, d / 2, 1)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        for v in roof.data.vertices:
            nx = v.co.x / (w / 2); ny = v.co.y / (d / 2)
            v.co.z += -sag * (1 - nx * nx) * (1 - 0.4 * abs(ny)) + tilt * v.co.y
        sol = roof.modifiers.new("sol", 'SOLIDIFY'); sol.thickness = 0.045
        bpy.context.view_layer.objects.active = roof
        bpy.ops.object.modifier_apply(modifier=sol.name)
        roof.data.materials.append(MATS["Awning"] if k == 0 else MATS["CanvasOld"])
        roof.select_set(False)
    # sọt / thúng hàng hai bên quầy
    for sx, sy in ((-1.95, -0.5), (1.95, -0.4), (-1.9, 0.55)):
        cyl("Basket", 0.30, 0.22, 0.42, (sx, sy, 0.21), MATS["Straw"], verts=12)
        sphere("BasketGoods", 0.24, (sx, sy, 0.48), MATS["GoodsA"], scale=(1, 1, 0.6))
    box("Crate", (0.62, 0.5, 0.4), (2.0, 0.55, 0.2), wood, 0.02)
    box("Crate2", (0.55, 0.45, 0.34), (2.02, 0.55, 0.57), woodL, 0.02)
    # hàng hoá trên quầy: 2 hàng x 3 (3 material GoodsA/B/C)
    gmats = [MATS["GoodsA"], MATS["GoodsB"], MATS["GoodsC"]]
    for i in range(6):
        gx = -1.25 + (i % 3) * 1.25; gy = -0.28 - (i // 3) * 0.55
        if i % 2 == 0:
            sphere("Goods", 0.20, (gx, gy, 1.32), gmats[i % 3], scale=(1, 1, 0.85))
        else:
            box("Goods", (0.5, 0.42, 0.32), (gx, gy, 1.31), gmats[i % 3], 0.04)
    # nồi + nắp (web ẩn/hiện theo quầy có khói) + muôi
    pot = cyl("Pot", 0.40, 0.34, 0.30, (-0.9, -0.15, 1.30), MATS["PotMetal"], verts=16)
    lid = cyl("PotLid", 0.30, 0.40, 0.10, (-0.9, -0.15, 1.50), MATS["PotMetal"], verts=16)
    sphere("PotKnob", 0.06, (-0.9, -0.15, 1.58), MATS["WoodDark"])
    # --- PROP RIÊNG QUẦY BÁNH TRÁNG: vỉ nướng than + bánh tráng trên vỉ (web hiện theo def.prop='grill') ---
    grill_parts = []
    grill_parts.append(box("tmpGrillBody", (0.95, 0.60, 0.20), (0.85, -0.10, 1.25), MATS["MetalDark"], 0.02))
    grill_parts.append(box("tmpGrillCoal", (0.85, 0.50, 0.05), (0.85, -0.10, 1.37), MATS["CharGlow"], 0.01))
    for i in range(6):
        grill_parts.append(box("tmpGrillBar", (0.90, 0.045, 0.035), (0.85, -0.32 + i * 0.09, 1.42), MATS["PotMetal"], 0.0))
    for sx in (-0.35, 0.35):
        grill_parts.append(box("tmpGrillLeg", (0.07, 0.07, 0.22), (0.85 + sx, -0.10, 1.06), MATS["MetalDark"], 0.01))
    join_into(grill_parts, "Grill")
    cyl("GrillCake", 0.27, 0.27, 0.035, (0.85, -0.10, 1.46), MATS["BanhTrang"], verts=18)
    sphere("GrillCakeTop", 0.13, (0.78, -0.16, 1.49), MATS["GoodsA"], scale=(1, 1, 0.45))
    # --- PROP RIÊNG QUẦY CÀ PHÊ: chồng phin xếp + ly thuỷ tinh có phin đang nhỏ giọt (web hiện theo def.prop='phin') ---
    phin_parts = []
    for i in range(3):  # chồng 3 phin
        phin_parts.append(cyl("tmpPhinBody", 0.105, 0.085, 0.075, (1.30, 0.42, 1.19 + i * 0.085), MATS["PotMetal"], verts=14))
        phin_parts.append(cyl("tmpPhinRim", 0.115, 0.115, 0.02, (1.30, 0.42, 1.155 + i * 0.085), MATS["PotMetal"], verts=14))
    phin_parts.append(cyl("tmpPhinLid", 0.10, 0.10, 0.025, (1.30, 0.42, 1.46), MATS["PotMetal"], verts=14))
    sphere("tmpPhinKnob", 0.03, (1.30, 0.42, 1.49), MATS["WoodDark"])
    join_into(phin_parts, "PhinStack")
    cyl("PhinGlass", 0.075, 0.06, 0.15, (0.95, 0.42, 1.23), MATS["Glass"], verts=12)
    cyl("PhinCoffee", 0.068, 0.055, 0.07, (0.95, 0.42, 1.19), MATS["CoffeeDark"], verts=12)
    cyl("PhinOnGlass", 0.105, 0.085, 0.075, (0.95, 0.42, 1.345), MATS["PotMetal"], verts=14)
    box("PhinBag", (0.34, 0.24, 0.42), (0.45, 0.45, 1.36), MATS["GoodsB"], 0.03)
    # đèn lồng giấy treo trước quầy (đối chiếu ref-online-02: lồng đèn cam dưới mái)
    for sx in (-1.5, 1.5):
        cyl("LanternCord", 0.015, 0.015, 0.34, (sx, -1.12, 2.05), MATS["WoodDark"], verts=6)
        sphere("Lantern", 0.17, (sx, -1.12, 1.76), MATS["LanternGlow"], scale=(1, 1, 1.25))
    # bảng hiệu (web áp canvas texture lên mặt trước -Y)
    box("SignBoard", (3.7, 0.06, 0.90), (0, -0.94, 2.12), MATS["SignBoard"], 0.02)
    box("SignTrim", (3.8, 0.08, 0.10), (0, -0.94, 2.60), MATS["Gold"], 0.01)
    export("stall")

# ============================================================
#  NHÀ LỒNG CHỢ ĐÀ LẠT — 3 tầng, tiền ở +Y blender (= -Z three, hướng ra đường)
#  Origin: tâm footprint, mặt đất z=0. Rộng X 70, sâu Y 16, cao ~19.5 + bảng hiệu 21.6
#  Gồm cả sân thượng tầng 2 (khối x +14..+21, lùi về -Y local của three = +Y blender xa)
# ============================================================
def build_market():
    clear_scene()
    wall, trim, conc, concD = MATS["WallCream"], MATS["TrimBrown"], MATS["Concrete"], MATS["ConcreteDk"]
    colM = M("ColumnCream", (0.78, 0.72, 0.62), 0.95)
    # --- sàn các tầng (nhô ra làm ban công) ---
    box("Floor0", (70, 18, 0.5), (0, 0, 0.25), MATS["Concrete"], 0.02)
    box("Floor1", (70, 18.6, 0.45), (0, 0.3, 6.55), colM, 0.02)
    box("Floor2", (70, 18.6, 0.45), (0, 0.3, 12.85), colM, 0.02)
    box("RoofSlab", (71, 19.2, 0.6), (0, 0.3, 19.15), trim, 0.03)
    # gờ mái kính lấy sáng (gợi ý A4/A6: mái kính lớn của nhà lồng)
    sk1 = box("Skylight", (40, 3.4, 0.18), (0, -1.15, 20.0), MATS["Glass"], 0.01, rot=(0.5, 0, 0))
    sk2 = box("Skylight", (40, 3.4, 0.18), (0, 1.75, 20.0), MATS["Glass"], 0.01, rot=(-0.5, 0, 0))
    box("SkylightCap", (40, 0.5, 0.22), (0, 0.3, 20.82), trim, 0.01)
    box("RooftopBox", (10, 7, 2.2), (-8, -1, 20.4), conc, 0.04)
    box("Parapet", (71, 0.5, 0.9), (0, 9.6, 19.8), trim, 0.02)
    box("ParapetB", (71, 0.5, 0.9), (0, -9.0, 19.8), trim, 0.02)
    # --- tường hông + tường sau (-Y) ---
    box("WallL", (0.7, 16, 19), (-34, 0, 9.5), wall, 0.02)
    box("WallR", (0.7, 16, 19), (34, 0, 9.5), wall, 0.02)
    box("WallBack", (68, 0.7, 19), (0, -7.8, 9.5), wall, 0.02)
    # sọc trang trí tường hông
    for sx in (-34.45, 34.45):
        for zz in (4.5, 10.5, 16.5):
            box("SideTrim", (0.15, 15.6, 0.5), (sx, 0, zz), trim, 0.01)
    # --- cột mặt tiền +Y, x -32..32 bước 8 ---
    for x in range(-32, 33, 8):
        box("Column", (0.9, 0.9, 19), (x, 7.8, 9.5), colM, 0.04)
        box("ColBase", (1.2, 1.2, 0.8), (x, 7.8, 0.4), concD, 0.03)
        box("ColCap", (1.15, 1.15, 0.5), (x, 7.8, 18.6), colM, 0.03)
    # --- vách kính tầng 2 & 3 + khung chia ô ---
    for fz in (9.6, 15.9):
        glass = box("GlassWin", (66, 0.25, 5.4), (0, 7.75, fz), MATS["MarketWin"], 0.0)
        for x in range(-32, 33, 4):
            box("Mullion", (0.14, 0.3, 5.4), (x, 7.8, fz), MATS["MetalDark"], 0.0)
        box("Sill", (67, 0.5, 0.35), (0, 7.8, fz - 2.85), colM, 0.02)
    # --- LƯỚI HOA GIÓ mặt tiền tầng 2-3 (đối chiếu ref-cho-dem-da-lat: mặt đứng
    #     nhà lồng có lưới ô vuông trang trí rất đặc trưng, phủ trước vách kính) ---
    lat = []
    for fz in (9.6, 15.9):
        for x in range(-33, 34, 3):
            lat.append(box("tmpLatV", (0.10, 0.14, 5.6), (x, 8.02, fz), colM, 0.0))
        for dz in (-2.7, -1.35, 0.0, 1.35, 2.7):
            lat.append(box("tmpLatH", (66.5, 0.14, 0.10), (0, 8.02, fz + dz), colM, 0.0))
        lat.append(box("tmpLatFrame", (67, 0.2, 0.28), (0, 8.0, fz + 2.85), trim, 0.0))
        lat.append(box("tmpLatFrame", (67, 0.2, 0.28), (0, 8.0, fz - 2.85), trim, 0.0))
    join_into(lat, "Lattice")
    # --- tầng trệt: cửa cuốn / ô cửa tối giữa các cột ---
    for x in range(-28, 29, 8):
        box("ShopDark", (5.6, 0.18, 3.6), (x, 7.85, 1.85), MATS["GlassDark"], 0.01)
        box("Shutter", (5.6, 0.22, 0.5), (x, 7.85, 3.85), MATS["MetalDark"], 0.01)
        for i in range(4):
            box("ShutterLine", (5.6, 0.24, 0.07), (x, 7.86, 0.7 + i * 0.8), MATS["MetalDark"], 0.0)
    # --- lan can ban công 2 tầng ---
    for ry in (7.6, 13.9):
        box("RailTop", (68, 0.18, 0.16), (0, 8.15, ry), MATS["WoodDark"], 0.01)
        posts = []
        for x in range(-32, 33, 4):
            posts.append(box("tmpRailPost", (0.12, 0.12, 1.0), (x, 8.15, ry - 0.5), MATS["WoodDark"], 0.0))
        join_into(posts, "RailPosts")
    # --- mái hiên cong tầng trệt (hiên uốn bằng dải segment) ---
    import math as _m
    for i in range(9):
        t0 = i / 9; t1 = (i + 1) / 9
        yc = 8.2 + (t0 + t1) / 2 * 4.2; zc = 4.9 - _m.sin((t0 + t1) / 2 * _m.pi * 0.5) * 0.85
        seg = box("AwningSeg", (72, 0.55, 0.16), (0, yc, zc), MATS["CanvasOld"], 0.01)
        seg.rotation_euler = (-0.5 + (t0 + t1) / 2 * 0.55, 0, 0)
    for x in range(-32, 33, 8):
        box("AwnPost", (0.14, 0.14, 4.1), (x, 12.15, 2.05), MATS["MetalDark"], 0.0)
    # --- dầm trần nội thất + cột trong ---
    for zz in (6.3, 12.6):
        box("BeamIn", (68, 15, 0.4), (0, 0, zz), concD, 0.01)
    for x in range(-24, 25, 12):
        for yy in (-3.5, 3.5):
            box("ColIn", (0.7, 0.7, 6.3), (x, yy, 3.4), conc, 0.03)
    # --- bảng hiệu lớn trên nóc + bảng phụ (web áp canvas) ---
    box("SignBoard", (35, 0.5, 5.2), (0, 7.95, 21.6), MATS["SignBoard"], 0.04)
    box("SignBoard2", (20, 0.4, 2.4), (0, 7.9, 17.6), MATS["SignBoard"], 0.03)
    box("SignPost", (0.4, 0.4, 2.2), (-14, 7.9, 20.2), MATS["MetalDark"], 0.0)
    box("SignPost", (0.4, 0.4, 2.2), (14, 7.9, 20.2), MATS["MetalDark"], 0.0)
    # --- sân thượng tầng 2 (khối phụ phía đông, three local x 14..21, z 7..12) ---
    # three local (17.5, 6.3, -10.5) -> blender (17.5, +10.5, 6.3)
    box("Terrace", (7, 5, 12.6), (17.5, 10.5, 6.3), M("TerraceMat", (0.76, 0.70, 0.60), 0.95), 0.03)
    box("TerraceRail", (7, 0.18, 0.9), (17.5, 13.1, 13.05), MATS["WoodDark"], 0.01)
    export("market")

# ============================================================
#  RẠP HÒA BÌNH — tiền ở -Y blender (= +Z three). Origin tâm footprint, đất z=0
# ============================================================
def build_theater():
    clear_scene()
    brick, fac, trim = MATS["WallBrick"], MATS["FacadeOld"], MATS["TrimBrown"]
    box("Body", (24, 13, 11), (0, 0, 5.5), brick, 0.04)
    # khối lùi 2 bên + pilaster
    box("WingL", (3.5, 11, 8.5), (-13.2, 0, 4.25), fac, 0.04)
    box("WingR", (3.5, 11, 8.5), (13.2, 0, 4.25), fac, 0.04)
    for sx in (-9.8, 9.8):
        box("Pilaster", (1.1, 0.7, 10.6), (sx, -6.4, 5.3), trim, 0.03)
    # mặt tiền + phù điêu: panel, dải ngang, 2 dải dọc, huy hiệu tròn
    box("Facade", (20, 0.5, 8.6), (0, -6.6, 4.6), fac, 0.03)
    box("ReliefBand", (20.2, 0.6, 0.7), (0, -6.65, 8.55), trim, 0.02)
    box("ReliefBand2", (20.2, 0.6, 0.5), (0, -6.65, 1.15), trim, 0.02)
    for sx in (-6.2, 6.2):
        box("ReliefStrip", (0.8, 0.58, 6.4), (sx, -6.65, 4.9), trim, 0.02)
    # --- Đối chiếu ảnh thật (ref-khu-hoa-binh.jpg): mặt tiền Art Deco ---
    # tường đầu hồi BẬC THANG trên mặt tiền
    box("Parapet1", (20.5, 0.7, 1.3), (0, -6.55, 11.6), fac, 0.02)
    box("Parapet2", (13.5, 0.7, 1.3), (0, -6.55, 12.85), fac, 0.02)
    box("Parapet3", (7.0, 0.7, 1.4), (0, -6.55, 14.15), fac, 0.02)
    # cửa sổ TRÒN lớn giữa mặt tiền (oculus)
    ring = torus("Oculus", 1.35, 0.17, (0, -6.95, 9.3), MATS["Stone"])
    disc = cyl("OculusGlass", 1.28, 1.28, 0.15, (0, -6.9, 9.3), MATS["GlassDark"], verts=24)
    disc.rotation_euler = (math.pi/2, 0, 0)
    box("OculusCross1", (0.14, 0.2, 2.5), (0, -6.98, 9.3), MATS["Stone"], 0.0)
    box("OculusCross2", (2.5, 0.2, 0.14), (0, -6.98, 9.3), MATS["Stone"], 0.0)
    # dải HOA GIÓ chevron dưới cửa tròn
    for i in range(15):
        d = box("LatticeDia", (0.52, 0.18, 0.52), (-8.4 + i * 1.2, -6.95, 7.15), MATS["Stone"], 0.01)
        d.rotation_euler = (0, math.pi/4, 0)
    box("LatticeBandT", (18.5, 0.55, 0.22), (0, -6.9, 7.62), trim, 0.01)
    box("LatticeBandB", (18.5, 0.55, 0.22), (0, -6.9, 6.68), trim, 0.01)
    # THÁP ĐỒNG HỒ cao mảnh bên phải mặt tiền
    box("ClockTower", (3.6, 4.2, 23), (14.3, -3.2, 11.5), fac, 0.04)
    box("TowerCap", (4.2, 4.8, 0.6), (14.3, -3.2, 23.2), trim, 0.03)
    for gx in (-1.0, 0.0, 1.0):
        box("TowerGroove", (0.35, 0.25, 15), (14.3 + gx, -5.35, 13.5), trim, 0.0)
    clk = cyl("ClockFace", 0.95, 0.95, 0.2, (14.3, -5.45, 20.6), MATS["CanvasOld"], verts=20)
    clk.rotation_euler = (math.pi/2, 0, 0)
    torus("ClockRing", 0.95, 0.09, (14.3, -5.58, 20.6), MATS["Gold"])
    box("ClockHand1", (0.09, 0.15, 0.75), (14.3, -5.6, 20.85), MATS["HairDark"], 0.0)
    box("ClockHand2", (0.55, 0.15, 0.09), (14.55, -5.6, 20.6), MATS["HairDark"], 0.0)
    crest = cyl("Crest", 1.1, 1.1, 0.3, (-6.2, -6.95, 4.9), MATS["Gold"], verts=24)
    crest.rotation_euler = (math.pi/2, 0, 0)
    # cửa rạp + bậc cấp
    box("Door", (7, 0.4, 3.4), (0, -6.8, 1.7), MATS["GlassDark"], 0.01)
    for sx in (-2.2, 2.2):
        box("DoorLine", (0.12, 0.45, 3.4), (sx, -6.8, 1.7), MATS["Gold"], 0.0)
    box("Step1", (10, 1.6, 0.35), (0, -7.4, 0.18), MATS["Stone"], 0.01)
    box("Step2", (9, 1.0, 0.7), (0, -7.1, 0.35), MATS["Stone"], 0.01)
    box("Step3", (8, 0.5, 1.05), (0, -6.85, 0.52), MATS["Stone"], 0.01)
    # mái 2 dốc kiểu v1 + nóc
    r1 = box("Roof1", (24.6, 8.4, 0.35), (0, -3.3, 13.2), MATS["RoofTile"], 0.02); r1.rotation_euler = (0.6, 0, 0)
    r2 = box("Roof2", (24.6, 8.4, 0.35), (0, 3.3, 13.2), MATS["RoofTile"], 0.02); r2.rotation_euler = (-0.6, 0, 0)
    box("Ridge", (24.6, 1.2, 0.4), (0, 0, 15.3), trim, 0.02)
    # cửa sổ nhỏ 2 bên mặt tiền
    for sx in (-11.5, 11.5):
        box("SideWin", (1.4, 0.3, 2.2), (sx, -5.6, 6.2), MATS["GlassDark"], 0.01)
    export("theater")

# ============================================================
#  CAFÉ TÙNG — tiền ở -Y blender. Origin tâm footprint, đất z=0. 9 x 7, cao 6.4
# ============================================================
def build_cafe():
    clear_scene()
    wall = M("CafeWall", (0.50, 0.42, 0.33), 0.97)
    box("Body", (9, 7, 6.4), (0, 0, 3.2), wall, 0.04)
    box("Roof", (9.6, 7.6, 0.4), (0, 0, 6.6), MATS["WoodDark"], 0.03)
    box("Cornice", (9.3, 7.3, 0.3), (0, 0, 6.05), MATS["TrimBrown"], 0.02)
    # cửa chính + 3 cửa sổ viền gỗ, kính CafeWin (phát sáng đêm qua web)
    box("Door", (1.6, 0.25, 3.0), (0, -3.55, 1.5), MATS["WoodDark"], 0.01)
    for sx in (-2.6, 2.6, 0):
        if sx == 0: continue
        box("WinFrame", (1.9, 0.22, 1.7), (sx, -3.55, 2.6), MATS["WoodDark"], 0.01)
        box("CafeWin", (1.7, 0.26, 1.5), (sx, -3.55, 2.6), MATS["CafeWin"], 0.0)
        box("WinBar", (0.08, 0.28, 1.5), (sx, -3.56, 2.6), MATS["WoodDark"], 0.0)
    # mái hiên nhỏ + bảng hiệu (web áp canvas)
    awn = box("CafeAwn", (8.4, 1.6, 0.12), (0, -4.2, 3.9), MATS["CanvasOld"], 0.01); awn.rotation_euler = (0.35, 0, 0)
    box("SignBoard", (7, 0.18, 1.6), (0, -3.62, 5.2), MATS["SignBoard"], 0.02)
    # bàn ghế nhỏ trước quán
    for sx in (-2.8, 2.8):
        cyl("Table", 0.45, 0.45, 0.06, (sx, -4.6, 0.78), MATS["WoodLight"], verts=12)
        cyl("TableLeg", 0.05, 0.05, 0.75, (sx, -4.6, 0.38), MATS["MetalDark"], verts=8)
        box("Chair", (0.45, 0.45, 0.5), (sx - 0.8, -4.6, 0.25), MATS["Wood"], 0.03)
        box("Chair", (0.45, 0.45, 0.5), (sx + 0.8, -4.6, 0.25), MATS["Wood"], 0.03)
    export("cafe")

# ============================================================
#  CÂY THÔNG — thân + cành + 4 tầng tán jitter hữu cơ. Cao ~7m
# ============================================================
def build_pine():
    clear_scene()
    cyl("Trunk", 0.13, 0.22, 2.4, (0, 0, 1.2), MATS["Trunk"], verts=9)
    for i in range(3):
        a = i * 2.1
        br = cyl("Branch", 0.04, 0.06, 1.1, (math.cos(a) * 0.5, math.sin(a) * 0.5, 1.9 + i * 0.3), MATS["Trunk"], verts=6)
        br.rotation_euler = (math.sin(a) * 1.1, -math.cos(a) * 1.1, 0)
    layers = [(1.55, 2.7, 3.0, "PineDark"), (1.25, 2.3, 4.3, "PineMid"), (0.95, 2.0, 5.5, "PineLight"), (0.60, 1.6, 6.6, "PineLight")]
    for r, h, z, mn in layers:
        c = cone("Canopy", r, h, (0, 0, z), MATS[mn], verts=10)
        for v in c.data.vertices:
            v.co.x += random.uniform(-0.07, 0.07)
            v.co.y += random.uniform(-0.07, 0.07)
    export("pine")

# ============================================================
#  ĐÈN ĐƯỜNG — đế, cột, tay cong, chao + cầu LampGlow. Cao ~5.2
# ============================================================
def build_lamp():
    clear_scene()
    cyl("Base", 0.16, 0.22, 0.5, (0, 0, 0.25), MATS["MetalDark"], verts=10)
    cyl("Pole", 0.07, 0.10, 4.6, (0, 0, 2.7), MATS["MetalDark"], verts=10)
    arm = torus("Arm", 0.55, 0.055, (0.42, 0, 4.95), MATS["MetalDark"], rot=(0, 0, 0))
    arm.scale = (1, 1, 0.6)
    cyl("Drop", 0.035, 0.035, 0.35, (0.95, 0, 4.85), MATS["MetalDark"], verts=8)
    cone("Shade", 0.30, 0.22, (0.95, 0, 4.72), MATS["MetalDark"], verts=12)
    sphere("LampGlow", 0.17, (0.95, 0, 4.58), MATS["LampGlow"])
    export("lamp")

# ============================================================
#  BÙNG BINH HOA — bệ tròn, đất, vòng hoa nhiều màu, đài trung tâm. R ~6.6
# ============================================================
def build_roundabout():
    clear_scene()
    cyl("Base", 6.6, 6.9, 0.55, (0, 0, 0.28), MATS["Stone"], verts=28)
    cyl("Soil", 5.9, 5.9, 0.30, (0, 0, 0.62), MATS["Soil"], verts=28)
    cyl("InnerRing", 2.0, 2.2, 0.5, (0, 0, 0.75), MATS["Stone"], verts=20)
    # vòng hoa: 3 vòng bán kính 2.8 / 4.2 / 5.3, mỗi hoa = cầu dẹt + lá
    fmats = [MATS["Flower%d" % i] for i in range(6)]
    k = 0
    for ring, n in ((2.8, 12), (4.2, 18), (5.3, 22)):
        for i in range(n):
            a = (i / n) * math.pi * 2 + ring
            x, y = math.cos(a) * ring, math.sin(a) * ring
            sphere("Flower", 0.21, (x, y, 0.92), fmats[k % 6], scale=(1, 1, 0.72)); k += 1
            sphere("Leaf", 0.26, (x * 0.97, y * 0.97, 0.80), MATS["LeafGreen"], scale=(1, 1, 0.5))
    # GÒ HOA trung tâm (chuẩn NP khóa: mau-np-01 + A3 — gò xanh phủ hoa giữa
    # vòng hoa, không tượng/đài phun như các bản tham khảo bán thực trước)
    sphere("Mound", 1.55, (0, 0, 1.02), MATS["LeafGreen"], scale=(1, 1, 0.52))
    fm2 = [MATS["Flower%d" % i] for i in range(6)]
    for i in range(7):
        a2 = i / 7 * math.pi * 2
        sphere("MoundFlower", 0.17, (math.cos(a2) * 0.85, math.sin(a2) * 0.85, 1.62), fm2[i % 6], scale=(1, 1, 0.75))
    sphere("MoundFlower", 0.20, (0, 0, 1.80), fm2[1], scale=(1, 1, 0.75))
    export("roundabout")

# ============================================================
#  CẦU NỔI — mặt cầu + lan can 2 bên (origin tâm mặt cầu, dài theo Y blender = Z three)
#  + PIER: trụ đỡ đơn vị cao 1m, origin ở chân (web scale Y theo chiều cao cần)
# ============================================================
def build_bridge():
    clear_scene()
    box("Deck", (6, 39.2, 0.55), (0, 0, 0), MATS["Concrete"], 0.02)
    box("DeckEdge", (6.3, 39.2, 0.18), (0, 0, -0.32), MATS["ConcreteDk"], 0.01)
    # lát gạch mặt cầu: vạch ngang mờ mỗi ~3.3m (đối chiếu ref-rap-hoa-binh)
    strips = []
    for i in range(12):
        strips.append(box("tmpStrip", (5.9, 0.10, 0.03), (0, -18 + i * 3.3, 0.29), MATS["ConcreteDk"], 0.0))
    join_into(strips, "DeckStrips")
    # lan can = TƯỜNG BÊ TÔNG THẤP ĐẶC 2 bên (ảnh thật: tường đặc ~1m, không phải song sắt)
    for sx in (-2.82, 2.82):
        box("Parapet", (0.35, 39.2, 0.95), (sx, 0, 0.75), MATS["Concrete"], 0.02)
        box("ParapetCap", (0.52, 39.2, 0.13), (sx, 0, 1.28), MATS["ConcreteDk"], 0.01)
    # MÁI KÍNH VÒM che cầu + kính hông + dây đèn (chuẩn A6: cầu mái kính vào chợ)
    for sx in (-2.82, 2.82):
        for yy in (-18, -9, 0, 9, 18):
            box("RoofPost", (0.16, 0.16, 1.5), (sx, yy, 2.05), MATS["WoodDark"], 0.01)
        for yy in (-13.5, -4.5, 4.5, 13.5):
            box("SideGlass", (0.05, 8.4, 1.15), (sx, yy, 1.95), MATS["Glass"], 0.0)
    for ang, xo, zo in ((-0.9, -2.58, 3.15), (-0.45, -1.44, 4.07), (0.0, 0, 4.40), (0.45, 1.44, 4.07), (0.9, 2.58, 3.15)):
        rp = box("RoofGlass", (1.78, 39.2, 0.07), (xo, 0, zo), MATS["Glass"], 0.0)
        rp.rotation_euler = (0, ang, 0)
    box("RidgeBeam", (0.2, 39.2, 0.2), (0, 0, 4.48), MATS["WoodDark"], 0.01)
    for yy in (-19.4, 19.4):
        box("EndBeam", (5.6, 0.18, 0.22), (0, yy, 3.35), MATS["WoodDark"], 0.01)
    for i in range(9):
        sphere("RoofLight", 0.075, (0, -16 + i * 4, 3.95), MATS["LanternGlow"])
    export("bridge")
    clear_scene()
    pier = cyl("Pier", 0.45, 0.58, 1.0, (0, 0, 0.5), MATS["Concrete"], verts=12)
    box("PierCap", (1.3, 1.3, 0.10), (0, 0, 0.97), MATS["ConcreteDk"], 0.01)
    export("pier")

# ============================================================
#  BẬC THANG LỚN — khớp hàm stairH của v1: 3 chuyến x 10 bậc + 2 chiếu nghỉ
#  Origin: tâm dải thang (three z=-16). Blender: top ở +Y (three z=-30), đáy ở -Y.
#  world z_three = -(blender y) - 16 ; chiều cao blender z = world y.
# ============================================================
def build_stairs():
    clear_scene()
    stone, stone2 = MATS["Stone"], MATS["Concrete"]
    def flight(y_top, run_total, steps, h_top, h_bot):
        run = run_total / steps
        for i in range(steps):
            h = h_top + (h_bot - h_top) * (i / steps)
            yc = y_top - run * (i + 0.5)
            box("Step", (11, run + 0.06, max(h, 0.25)), (0, yc, max(h, 0.25) / 2), stone if i % 2 else stone2, 0.01)
    # chuyến A: y +14..+6 (world -30..-22), 17 -> 11.33
    flight(14, 8, 10, 17, 11.33)
    # chiếu nghỉ 1: y +6..+3.5 (world -22..-19.5), h 11.33
    box("Landing1", (13, 2.5, 11.33), (0, 4.75, 11.33 / 2), stone2, 0.01)
    box("Landing1Top", (11, 2.5, 0.35), (0, 4.75, 11.5), MATS["CanvasOld"], 0.01)
    # chuyến B: y +3.5..-4.5 (world -19.5..-11.5), 11.33 -> 5.67
    flight(3.5, 8, 10, 11.33, 5.67)
    # chiếu nghỉ 2: y -4.5..-7 (world -11.5..-9), h 5.67
    box("Landing2", (13, 2.5, 5.67), (0, -5.75, 5.67 / 2), stone2, 0.01)
    box("Landing2Top", (11, 2.5, 0.35), (0, -5.75, 5.84), MATS["CanvasOld"], 0.01)
    # chuyến C: y -7..-14 (world -9..-2), 5.67 -> 0
    flight(-7, 7, 10, 5.67, 0)
    # vách hông dốc 2 bên (khối nghiêng theo sườn tổng)
    for sx in (-5.85, 5.85):
        wall = box("SideWall", (0.5, 33, 1.6), (sx, 0, 8.0), MATS["ConcreteDk"], 0.02)
        wall.rotation_euler = (math.atan2(17, 28), 0, 0)
        rail = box("HandRail", (0.16, 31, 0.16), (sx * 0.96, 0, 9.3), MATS["WoodDark"], 0.01)
        rail.rotation_euler = (math.atan2(17, 28), 0, 0)
    export("stairs")

build_character()
build_stall()
build_market()
build_theater()
build_cafe()
build_pine()
build_lamp()
build_roundabout()
build_bridge()
build_stairs()
print("ALL DONE")
