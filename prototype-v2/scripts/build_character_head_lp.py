# -*- coding: utf-8 -*-
"""CROWD-OPT-1: build RIÊNG character.glb thấp poly từ build_models.py.
Chỉ đổi segment 4 sphere thân/tay (belly + 2 vai 14x10->10x7, tay 14x10->8x6);
giữ nguyên pivot, tỉ lệ đầu, tên node, 4 phom, màu, mũ/khăn/đầu.
Chạy: blender -b --factory-startup -noaudio --python scripts/build_character_lp.py
Xuất vào ../assets/character.glb (backup bản cũ trước khi chạy).
"""
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
import bmesh
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
    # --- V4: material theo hồ sơ ảnh thật (research/11) ---
    M("Peach",      (0.78,0.42,0.23), 0.95)                       # băng hồng đào mặt tiền chợ (V4.1: đậm hơn hẳn)
    M("ZigBack",    (0.52,0.49,0.44), 0.95)                       # nền dải zigzag (V4.1: xám đậm để zigzag trắng bật)
    M("SignLetters",(0.62,0.13,0.09), 0.6, 0.0, emit=(0.85,0.10,0.07), ei=0.35)  # chữ CHỢ ĐÀ LẠT đỏ (web tăng emissive ban đêm)
    M("ElevGlass",  (0.35,0.62,0.45), 0.25, 0.1)                  # kính tháp thang máy xanh lá
    M("AdGreen",    (0.30,0.60,0.30), 0.8)
    M("AdYellow",   (0.93,0.74,0.24), 0.8)
    M("AdWhite",    (0.92,0.90,0.84), 0.8)
    M("AdLED",      (0.70,0.10,0.10), 0.6, 0.0, emit=(1.0,0.14,0.10), ei=1.1)   # biển LED đỏ cửa chính
    M("StripeA",    (0.18,0.43,0.64), 0.95)                       # bạt sọc xanh dương
    M("StripeB",    (0.96,0.96,0.94), 0.95)                       # bạt sọc trắng
    M("WhiteConc",  (0.90,0.89,0.85), 0.95)                       # bê tông sơn trắng (cầu thang ngoài trời)
    M("StatueStone",(0.64,0.63,0.60), 0.88)                       # V5.1: đá xám LẠNH sáng hơn — tượng rọi sáng nổi trên nền đêm (research/18)
    M("BenchWhite", (0.90,0.89,0.86), 0.95)
    M("StatueWhite",(0.93,0.92,0.88), 0.9)                        # tượng trang trí trắng sân thượng
    M("VehDark",    (0.12,0.12,0.13), 0.6, 0.3)
    M("TireMat",    (0.08,0.08,0.09), 0.95)
    M("BikeBody",   (0.55,0.16,0.14), 0.5, 0.15)                  # web tô lại theo xe
    M("RiderShirt", (0.30,0.45,0.62), 0.95)                       # web tô lại
    M("Helmet",     (0.85,0.72,0.20), 0.45, 0.1)                  # web tô lại
    M("CarBody",    (0.88,0.87,0.85), 0.45, 0.2)                  # web tô lại
    M("HeadLamp",   (1.0,0.92,0.62), 0.35, 0.0, emit=(1.0,0.85,0.50), ei=0.4)
    # --- V4 bổ sung 09:57: khách sạn + quán vỉa hè ---
    M("HotelWhite", (0.90,0.89,0.86), 0.95)
    M("HotelWinA",  (0.30,0.26,0.20), 0.4, 0.0, emit=(1.0,0.62,0.25), ei=0.0)  # web: sáng mạnh đêm
    M("HotelWinB",  (0.30,0.26,0.20), 0.4, 0.0, emit=(1.0,0.62,0.25), ei=0.0)  # web: sáng vừa đêm
    M("HotelWinC",  (0.16,0.19,0.22), 0.35, 0.1)                              # cửa sổ tối
    M("VIBWall",    (0.55,0.60,0.66), 0.7, 0.1)
    M("VIBGlass",   (0.20,0.30,0.42), 0.25, 0.3)
    M("HSYellow",   (0.45,0.32,0.08), 0.6, 0.0, emit=(1.0,0.74,0.20), ei=0.3)  # biển nóc phát sáng (web boost đêm)
    M("HSWhite",    (0.40,0.42,0.45), 0.6, 0.0, emit=(0.92,0.96,1.0), ei=0.3)
    M("HSBlue",     (0.10,0.20,0.40), 0.6, 0.0, emit=(0.35,0.62,1.0), ei=0.3)
    M("ShopWall",   (0.80,0.72,0.60), 0.95)
    M("ShopAwn",    (0.55,0.45,0.35), 0.95)   # web tô lại / sọc theo quán
    # --- V5.1 BLENDER-FIRST: vật liệu hàng sạp tĩnh + mái tôn (bão hòa theo palette khóa: hàng hóa 0.45–0.80) ---
    M("TinMat",     (0.60,0.61,0.58), 0.55, 0.35)                 # mái tôn sóng
    M("StickWood",  (0.72,0.56,0.34), 0.9)                        # que xiên tre
    M("SkewerMeat", (0.52,0.20,0.11), 0.75)                       # thịt nướng nâu đỏ
    M("SkewerVeg",  (0.32,0.52,0.22), 0.8)                        # đậu bắp / hành xanh
    M("SkewerCorn", (0.88,0.66,0.18), 0.8)                        # bắp vàng
    M("SkewerWhite",(0.90,0.85,0.76), 0.8)                        # mực / chả trắng
    M("JarCream",   (0.94,0.90,0.82), 0.6)                        # hũ yaourt kem
    M("CheGreen",   (0.25,0.60,0.30), 0.7)                        # chè xanh
    M("CheRed",     (0.78,0.18,0.16), 0.7)                        # chè đỏ / nắp hũ
    M("ChePurple",  (0.50,0.36,0.66), 0.7)                        # chè tím / khoai tím
    M("AmberJar",   (0.80,0.58,0.20), 0.45)                       # hũ nước đường đậu hũ
    for i, c in enumerate([(0.78,0.24,0.32),(0.90,0.55,0.15),(0.70,0.22,0.32),
                           (0.92,0.90,0.85),(0.80,0.38,0.18),(0.60,0.30,0.60)]):
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

def sphere(name, r, loc, mat=None, scale=(1,1,1), seg=14, ring=10):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=loc, segments=seg, ring_count=ring)
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

def trim_front_below(obj, z_cut, y_front=-0.02):
    """V4.1: cắt bỏ geometry nằm TRƯỚC mặt (y < y_front) và DƯỚI z_cut (toạ độ
    thế giới của nhân vật). Dùng cho tóc/mũ dạng cầu: phần cầu phồng ra trước
    trán dưới đường cắt sẽ bị xoá -> không còn dải tối che mắt khi nhìn từ
    trên/trước, mũ thành dạng vòm ôm đỉnh đầu như mũ thật."""
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bm = bmesh.new(); bm.from_mesh(obj.data)
    kill = [v for v in bm.verts if v.co.z < z_cut and v.co.y < y_front]
    if kill:
        bmesh.ops.delete(bm, geom=kill, context='VERTS')
    bm.to_mesh(obj.data); bm.free()
    obj.select_set(False)
    return obj

def sector(name, r0, r1, a0, a1, z0, z1, mat, seg=7):
    """V4.1: mảng quạt vành khăn đặc (r0..r1, góc a0..a1, dày z0..z1) — thảm
    hoa/cỏ LIỀN MẢNG cho bùng binh, thay cho hoa chấm thưa rời rạc."""
    verts = []
    for z in (z0, z1):
        for r in (r0, r1):
            for i in range(seg + 1):
                a = a0 + (a1 - a0) * i / seg
                verts.append((math.cos(a) * r, math.sin(a) * r, z))
    n = seg + 1
    faces = []
    for i in range(seg):  # mặt trên (z1) + mặt dưới (z0)
        faces.append((2 * n + i, 2 * n + i + 1, 3 * n + i + 1, 3 * n + i))
        faces.append((i, n + i, n + i + 1, i + 1))
        # mặt ngoài (r1) + mặt trong (r0)
        faces.append((n + i, 3 * n + i, 3 * n + i + 1, n + i + 1))
        faces.append((i, i + 1, 2 * n + i + 1, 2 * n + i))
    faces.append((0, n, 3 * n, 2 * n))                                # nắp đầu a0
    faces.append((seg, 2 * n + seg, 3 * n + seg, n + seg))            # nắp cuối a1 (i=seg)
    me = bpy.data.meshes.new(name)
    me.from_pydata(verts, [], faces)
    me.update()
    o = bpy.data.objects.new(name, me)
    bpy.context.collection.objects.link(o)
    bm = bmesh.new(); bm.from_mesh(me)
    bmesh.ops.recalc_face_normals(bm, faces=list(bm.faces))
    bm.to_mesh(me); bm.free()
    return finish_obj(o, mat, 0.0)

def export(name):
    path = os.path.join(OUT, name + ".glb")
    bpy.ops.export_scene.gltf(filepath=path, export_format='GLB', export_apply=True)
    print("EXPORTED", path, os.path.getsize(path))

# ---------------- V4 helpers: chữ nổi 3D + dải zigzag ----------------
_FONT = None
def get_font():
    global _FONT
    if _FONT is None:
        p = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
        if os.path.exists(p):
            _FONT = bpy.data.fonts.load(p)
    return _FONT

def text_obj(body, size, loc, rot, mat, extrude=0.16, name="SignLetters"):
    """Chữ nổi 3D. Mặt +Y (tiền chợ): rot=(-pi/2,0,pi); mặt -Y: rot=(pi/2,0,0)."""
    cu = bpy.data.curves.new("txt", 'FONT')
    cu.body = body
    f = get_font()
    if f: cu.font = f
    cu.size = size
    cu.align_x = 'CENTER'; cu.align_y = 'CENTER'
    cu.extrude = extrude
    cu.resolution_u = 3
    cu.bevel_depth = 0.008; cu.bevel_resolution = 1
    ob = bpy.data.objects.new(name, cu)
    bpy.context.collection.objects.link(ob)
    ob.location = loc; ob.rotation_euler = rot
    if mat: ob.data.materials.append(mat)
    ob.select_set(False)
    return ob

def chevron_row(x0, x1, y, z, mat, step=2.0, arm=1.35, thick=0.34, tall=0.45, lift=0.0):
    """Một hàng hoa văn zigzag ^^^ trong mặt phẳng X-Z tại độ sâu y. Trả về list obj."""
    parts = []
    n = int(round((x1 - x0) / step))
    for i in range(n):
        xu = x0 + step * (i + 0.5)
        a = box("tmpChev", (arm, thick, tall), (xu - 0.47, y, z), mat, 0.0)
        a.rotation_euler = (0, 0.60, 0)
        b = box("tmpChev", (arm, thick, tall), (xu + 0.47, y, z), mat, 0.0)
        b.rotation_euler = (0, -0.60, 0)
        parts += [a, b]
    return parts

def wheel(name, r, wdt, loc, mat, hub_mat=None):
    """Bánh xe: trục dọc X (đã bake vào geometry để web quay rotation.x), origin tại tâm."""
    bpy.ops.mesh.primitive_cylinder_add(vertices=18, radius=r, depth=wdt, location=loc)
    o = bpy.context.object; o.name = name
    o.data.transform(Matrix.Rotation(math.pi / 2, 4, 'Y'))
    o.data.materials.append(mat)
    if hub_mat:
        bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=r * 0.45, depth=wdt + 0.03, location=loc)
        h = bpy.context.object; h.name = "tmpHub"
        h.data.transform(Matrix.Rotation(math.pi / 2, 4, 'Y'))
        h.data.materials.append(hub_mat)
        o = join_into([o, h], name)
    o.select_set(False)
    return o

mats_init()

# ============================================================
#  NHÂN VẬT CHIBI (chuẩn ảnh chốt): đầu to tròn ~50% chiều cao (đợt model 07/11),
#  thân ngắn rộng, mặt đơn giản dễ thương (mắt chấm + má hồng + miệng nhỏ). Part
#  riêng có pivot tại khớp (hông/vai) để web vung tay/chân. Mặt hướng -Y blender (= +Z three).
# ============================================================
def build_character():
    clear_scene()
    skin, shirt, pants = MATS["Skin"], MATS["Shirt"], MATS["Pants"]
    # ĐỢT MODEL (07/11): tỉ lệ chibi theo ẢNH CHỐT — đầu r=0.45 (0.90..1.80, ~50%
    # chiều cao 1.80), thân ngắn RỘNG, chân ngắn. Đo trên GLB cũ: đầu 0.877 /
    # phần dưới đầu 1.06 (mặt 0.57 : dưới-mặt 1.06 = 1:1.86) — "cao/thanh".
    # Bản mới: đầu 0.90 / dưới đầu 0.90; mặt (cằm 0.90 -> trán 1.47) 0.57 :
    # dưới mặt 0.90 = 1 : 1.58 ~ 1:1.6 của research/13 theo cách đo mặt.
    # --- chân ngắn: pivot tại hông z=0.40, geometry dịch xuống -0.17 (đáy giày GIỮ 0..0.12 như cũ) ---
    for side, sx in (("L", -0.12), ("R", 0.12)):
        leg = box("tmpLeg", (0.21, 0.23, 0.42), (sx, 0, 0.40), pants, 0.07)
        leg.data.transform(Matrix.Translation((0, 0, -0.17)))
        shoe = box("tmpShoe", (0.23, 0.37, 0.12), (sx, -0.06, 0.06), MATS["Shoe"], 0.04)
        join_into([leg, shoe], "Leg" + side)
    # --- thân NGẮN RỘNG bo tròn: hộp bo lớn + bụng cầu dẹt ---
    torso = box("tmpTorso", (0.68, 0.36, 0.50), (0, 0, 0.66), shirt, 0.13)
    belly = sphere("tmpBelly", 0.31, (0, -0.02, 0.65), shirt, scale=(1.08, 0.70, 0.95), seg=10, ring=7)  # CROWD-OPT-1: 14x10 -> 10x7
    # cầu vai bo tròn — giảm cảm giác "hộp" ở vai/thân
    shL = sphere("tmpShoulder", 0.14, (-0.35, 0, 0.86), shirt, seg=10, ring=7)  # CROWD-OPT-1
    shR = sphere("tmpShoulder", 0.14, (0.35, 0, 0.86), shirt, seg=10, ring=7)  # CROWD-OPT-1
    join_into([torso, belly, shL, shR], "Torso")
    collar = torus("tmpCollar", 0.17, 0.055, (0, 0, 0.905), shirt, scale=(1, 0.85, 0.7))
    # --- tay ngắn: pivot tại vai z=0.88. GIỮ hình học LOCAL như bản cũ (bàn tay
    # ở local -0.42) để mọi neo AR/ARMS của tủ đồ KHÔNG phải dịch chuyển. ---
    for side, sx in (("L", -0.40), ("R", 0.40)):
        arm = box("tmpArm", (0.16, 0.18, 0.46), (sx, 0, 0.88), shirt, 0.08)
        arm.data.transform(Matrix.Translation((0, 0, -0.17)))
        hand = sphere("tmpHand", 0.085, (sx, 0, 0.88 - 0.42), skin, seg=8, ring=6)  # CROWD-OPT-1: 14x10 -> 8x6
        join_into([arm, hand], "Arm" + side)
    # --- ĐẦU TO TRÒN r=0.45 (0.90..1.80): da + tóc + mắt chấm + má hồng + miệng ---
    # V4.1: tóc/mũ dạng cầu PHẢI cắt bỏ phần trước-dưới (trim_front_below) —
    # cầu nguyên khối phồng ra trước mặt, che mắt thành "dải tối + mảng đỏ"
    # như render v4-03/04 đã bị bác. Sau khi cắt: tóc/mũ ôm đỉnh đầu, mặt sạch.
    head = sphere("Head", 0.45, (0, 0, 1.35), skin, seg=10, ring=7)  # HEAD-OPT-1: 14x10 -> 10x7
    hair = sphere("tmpHair", 0.455, (0, 0.06, 1.415), MATS["HairDark"], scale=(1, 1, 0.9), seg=10, ring=7)  # HEAD-OPT-1
    trim_front_below(hair, 1.50)
    nose = cone("tmpNose", 0.035, 0.07, (0, -0.445, 1.325), skin, verts=8)
    nose.rotation_euler = (-math.pi/2, 0, 0)
    mouth = sphere("tmpMouth", 0.022, (0, -0.437, 1.265), MATS["HairDark"], scale=(1.6, 0.5, 0.9), seg=10, ring=7)  # HEAD-OPT-1
    parts = [head, hair, nose, mouth]
    for sx in (-0.435, 0.435):
        parts.append(sphere("tmpEar", 0.075, (sx, 0, 1.31), skin, scale=(0.5, 0.85, 0.95)))  # HEAD-OPT-1 POLISH: tai giữ 14x10 (cận nghiêng lộ facet)
    for sx in (-0.16, 0.16):
        parts.append(sphere("tmpEye", 0.052, (sx, -0.42, 1.395), MATS["HairDark"]))  # HEAD-OPT-1 POLISH: mắt giữ 14x10 (cận 3/4 lộ facet)
    for sx in (-0.275, 0.275):
        parts.append(sphere("tmpCheek", 0.055, (sx, -0.34, 1.265), MATS["Blush"], scale=(1, 0.4, 0.8), seg=10, ring=7))  # HEAD-OPT-1
    join_into(parts, "Head")
    # --- mũ nón lá vành rộng phủ đầu to (đầu mới r=0.45, đỉnh 1.80) ---
    brim = cone("tmpNonLa", 0.72, 0.35, (0, 0, 1.73), MATS["Straw"], verts=18)
    tip = sphere("tmpNonLaTip", 0.06, (0, 0, 1.93), MATS["WoodDark"])
    join_into([brim, tip], "HatNonLa")
    # --- mũ beanie len + pom: vòm dẹt ôm đỉnh đầu, vành nằm TRÊN mắt (z>=1.44) ---
    dome = sphere("tmpBeanie", 0.47, (0, 0.02, 1.52), MATS["Beanie"], scale=(1, 1, 0.62))
    trim_front_below(dome, 1.46)
    ring = cyl("tmpBeanieRing", 0.465, 0.475, 0.10, (0, 0, 1.49), MATS["Beanie"], verts=18)
    pom = sphere("tmpPom", 0.10, (0, 0, 1.845), MATS["CanvasOld"])
    join_into([dome, ring, pom], "HatBeanie")
    # --- mũ lưỡi trai: vòm dẹt ôm đỉnh + vành ở trán (z~1.44), không che mặt ---
    capdome = sphere("tmpCap", 0.465, (0, 0.01, 1.50), MATS["CapBlue"], scale=(1, 1, 0.66))
    trim_front_below(capdome, 1.44)
    capbrim = box("tmpCapBrim", (0.38, 0.27, 0.045), (0, -0.475, 1.435), MATS["CapBlue"], 0.02, rot=(-0.18, 0, 0))
    join_into([capdome, capbrim], "HatCap")
    # --- khăn quàng (chỉ nhân vật chính bật) — cổ mới ở z~0.90..0.96 ---
    scarf = torus("Scarf", 0.27, 0.095, (0, 0, 0.96), MATS["Scarf"], scale=(1, 0.95, 0.8))
    tail = box("tmpScarfTail", (0.17, 0.05, 0.32), (0.18, -0.21, 0.80), MATS["Scarf"], 0.03)
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
    # ==== V5.1 BLENDER-FIRST: HÀNG TĨNH THEO SẠP (web bật theo def.id, như Grill/Phin) ====
    # SẠP XIÊN (research/18 ƯT3 #1 + ảnh 31): 3 khay nghiêng xếp tầng, xiên chĩa về
    # phía khách thành "rừng que" + vỉ than đỏ dưới khay. ~48 xiên/sạp.
    skw = []
    _fmats = [MATS["SkewerMeat"], MATS["SkewerVeg"], MATS["SkewerCorn"], MATS["SkewerWhite"]]
    for t in range(3):
        ty, tz = -0.58 + t * 0.17, 1.26 + t * 0.27
        if t > 0:
            skw.append(box("tmpSkwStand", (1.9, 0.34, 0.06), (0, ty + 0.10, tz - 0.16), MATS["MetalDark"], 0.0))
        tray = box("tmpSkwTray", (1.9, 0.55, 0.05), (0, ty, tz), MATS["PotMetal"], 0.0)
        tray.rotation_euler = (0.42, 0, 0)
        skw.append(tray)
        for i in range(16):
            sx = -0.85 + i * 0.113
            stick = cyl("tmpSkwStick", 0.011, 0.011, 0.34, (sx, ty - 0.06, tz + 0.05), MATS["StickWood"], verts=5, bevel=0.0)
            stick.rotation_euler = (0.95, 0, 0)
            head = sphere("tmpSkwHead", 0.046, (sx, ty - 0.21, tz + 0.20), _fmats[(i + t) % 4], scale=(1, 1, 1.5), seg=5, ring=3)
            head.rotation_euler = (0.95, 0, 0)
            skw += [stick, head]
    skw.append(box("tmpSkwGrill", (1.5, 0.5, 0.16), (0, -0.66, 1.14), MATS["MetalDark"], 0.0))
    skw.append(box("tmpSkwCoal", (1.4, 0.42, 0.04), (0, -0.66, 1.25), MATS["CharGlow"], 0.0))
    join_into(skw, "SkewerTrays")
    # SẠP CHÈ: 10 cốc chè màu 2 tầng (ảnh đêm: dãy cốc màu là dấu nhận diện)
    che = [box("tmpCheShelf", (1.6, 0.45, 0.05), (-0.6, -0.38, 1.44), MATS["WoodLight"], 0.01)]
    _cmats = [MATS["CheGreen"], MATS["CheRed"], MATS["SkewerCorn"], MATS["ChePurple"], MATS["JarCream"]]
    for r in range(2):
        for i in range(5):
            che.append(cyl("tmpCheCup", 0.052, 0.042, 0.13, (-1.24 + i * 0.33, -0.44 + r * 0.08, 1.225 + r * 0.245), _cmats[(i + r * 2) % 5], verts=10, bevel=0.0))
    join_into(che, "CheCups")
    # SẠP YAOURT: tháp hũ thủy tinh kem 3 tầng 5-4-3 + nắp đỏ
    yao = []
    for tier, cnt in enumerate((5, 4, 3)):
        yao.append(box("tmpYaoBoard", (1.05, 0.48, 0.03), (0.55, -0.32, 1.315 + tier * 0.125), MATS["WoodLight"], 0.005))
        for i in range(cnt):
            yao.append(cyl("tmpYaoJar", 0.048, 0.048, 0.095, (0.55 + (i - (cnt - 1) / 2) * 0.135, -0.32, 1.375 + tier * 0.125), MATS["JarCream"], verts=8, bevel=0.0))
            yao.append(cyl("tmpYaoLid", 0.050, 0.050, 0.018, (0.55 + (i - (cnt - 1) / 2) * 0.135, -0.32, 1.432 + tier * 0.125), MATS["CheRed"], verts=8, bevel=0.0))
    join_into(yao, "YaourtTower")
    # ĐẬU HŨ / BÁNH ƯỚT / SỮA ĐẬU: nồi thép + chồng 6 chén sứ + hũ nước đường hổ phách
    bowl = [cyl("tmpBowlPot", 0.30, 0.26, 0.26, (0.78, -0.28, 1.28), MATS["PotMetal"], verts=14, bevel=0.0),
            cyl("tmpBowlJar", 0.09, 0.09, 0.22, (-0.30, -0.38, 1.26), MATS["AmberJar"], verts=12, bevel=0.0)]
    for i in range(6):
        bowl.append(cyl("tmpBowl", 0.095, 0.065, 0.055, (-0.78, -0.32, 1.175 + i * 0.048), MATS["AdWhite"], verts=12, bevel=0.0))
    join_into(bowl, "BowlStack")
    # SẠP KHOAI: vỉ than + 8 bắp nằm ngang + 6 khoai tím/nâu
    corn = [box("tmpCornGrill", (1.7, 0.55, 0.18), (0, -0.45, 1.20), MATS["MetalDark"], 0.02),
            box("tmpCornCoal", (1.6, 0.45, 0.04), (0, -0.45, 1.31), MATS["CharGlow"], 0.01)]
    for i in range(8):
        cob = cyl("tmpCornCob", 0.050, 0.056, 0.30, (-0.70 + i * 0.20, -0.45, 1.40), MATS["SkewerCorn"], verts=8, bevel=0.0)
        cob.rotation_euler = (math.pi / 2, 0, 0)
        corn.append(cob)
    for i in range(6):
        corn.append(sphere("tmpPotato", 0.07, (0.32 + (i % 3) * 0.19, -0.58 + (i // 3) * 0.22, 1.40), MATS["ChePurple"] if i % 2 else MATS["GoodsB"], scale=(1.25, 1, 0.8), seg=8, ring=6))
    join_into(corn, "CornGrill")
    # Ô DÙ SẠP (web bật theo def.umb): cột + tán 2 lớp sọc xanh-trắng + bi viền
    umb = [cyl("tmpUmbPole", 0.03, 0.03, 2.6, (2.35, -0.95, 1.30), MATS["MetalDark"], verts=8, bevel=0.0),
           cone("tmpUmbTop", 1.45, 0.42, (2.35, -0.95, 2.58), MATS["StripeB"], verts=10),
           cone("tmpUmbBand", 1.47, 0.22, (2.35, -0.95, 2.44), MATS["StripeA"], verts=10)]
    for i in range(8):
        a = i / 8 * math.pi * 2
        umb.append(sphere("tmpUmbTip", 0.05, (2.35 + math.cos(a) * 1.42, -0.95 + math.sin(a) * 1.42, 2.38), MATS["StripeA"] if i % 2 else MATS["StripeB"], seg=6, ring=4))
    join_into(umb, "Umbrella")
    # MÁI TÔN SÓNG (web bật theo def.roof='tin', ẩn Awning): lưới ripple sin + solidify
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=24, y_subdivisions=4, size=2.0, location=(0, -0.1, 2.62))
    tin = bpy.context.object; tin.name = "TinRoof"
    tin.scale = (2.1, 1.45, 1)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    for v in tin.data.vertices:
        v.co.z += math.sin(v.co.x * 10.5) * 0.028 + 0.10 * v.co.y
    _sol = tin.modifiers.new("sol", 'SOLIDIFY'); _sol.thickness = 0.03
    bpy.context.view_layer.objects.active = tin
    bpy.ops.object.modifier_apply(modifier=_sol.name)
    tin.data.materials.append(MATS["TinMat"])
    tin.select_set(False)
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
    # --- sàn các tầng (GIỮ neo: cao 0.25 / 6.55 / 12.85, nóc 19.15) ---
    box("Floor0", (70, 18, 0.5), (0, 0, 0.25), MATS["Concrete"], 0.02)
    # ĐỢT MODEL (07/11): KHOÉT GIẾNG THANG TRONG NHÀ ở góc đông (web x 28.6..33.65,
    # tường đông áp vào x>=33.65) để đầu người chơi hết chạm mép sàn khi đi thang:
    # - Floor2 khoét web z 11.3..15.6 (blender y 4.4..8.7): đầu chuyến 1 (12.6 -> 6.55).
    #   Tại mép giếng z=15.6 đầu người (chân 9.575 + cao 1.80) = 11.38 < đáy slab 12.625.
    # - Floor1 khoét web z 18.2..23.8 (blender y -3.8..1.8): chiếu nghỉ giữa (6.55)
    #   + đầu chuyến 2; tại mép z=23.8 đầu (chân 3.53 + 1.80) = 5.33 < đáy slab 6.325.
    # Floor1 (mặt 6.775) — 4 mảnh quanh giếng y -3.8..1.8
    box("Floor1", (63.6, 17.2, 0.45), (-3.2, 0.1, 6.55), colM, 0.02)
    box("Floor1E", (6.4, 6.9, 0.45), (31.8, 5.25, 6.55), colM, 0.02)
    box("Floor1E", (6.4, 4.7, 0.45), (31.8, -6.15, 6.55), colM, 0.02)
    box("Floor1E", (1.35, 5.6, 0.45), (34.325, -1.0, 6.55), colM, 0.02)
    # Floor2 (mặt 13.075) — 3 mảnh quanh giếng y 4.4..8.7
    box("Floor2", (63.6, 17.2, 0.45), (-3.2, 0.1, 12.85), colM, 0.02)
    box("Floor2E", (6.4, 12.9, 0.45), (31.8, -2.05, 12.85), colM, 0.02)
    box("Floor2E", (1.35, 4.3, 0.45), (34.325, 6.55, 12.85), colM, 0.02)
    # viền miệng giếng (fascia bê tông tối bọc mép cắt, dày 0.5 giữa slab)
    box("WellTrim1W", (0.16, 5.6, 0.5), (28.6, -1.0, 6.55), MATS["ConcreteDk"], 0.0)
    box("WellTrim1S", (5.05, 0.16, 0.5), (31.125, -3.8, 6.55), MATS["ConcreteDk"], 0.0)
    box("WellTrim1N", (5.05, 0.16, 0.5), (31.125, 1.8, 6.55), MATS["ConcreteDk"], 0.0)
    box("WellTrim2W", (0.16, 4.3, 0.5), (28.6, 6.55, 12.85), MATS["ConcreteDk"], 0.0)
    box("WellTrim2S", (5.05, 0.16, 0.5), (31.125, 4.4, 12.85), MATS["ConcreteDk"], 0.0)
    # lan can miệng giếng Floor2 (mép tây + mép nam, kiểu RoofRail): trụ + 2 tay vịn
    box("WellRail2WT", (0.07, 4.1, 0.07), (28.55, 6.55, 13.60), MATS["MetalDark"], 0.0)
    box("WellRail2WM", (0.06, 4.1, 0.06), (28.55, 6.55, 13.33), MATS["MetalDark"], 0.0)
    for py in (4.7, 6.0, 7.3, 8.5):
        box("WellRail2P", (0.06, 0.06, 0.55), (28.55, py, 13.35), MATS["MetalDark"], 0.0)
    box("WellRail2ST", (4.8, 0.07, 0.07), (31.1, 4.35, 13.60), MATS["MetalDark"], 0.0)
    box("WellRail2SM", (4.8, 0.06, 0.06), (31.1, 4.35, 13.33), MATS["MetalDark"], 0.0)
    for px in (29.0, 30.6, 32.2, 33.4):
        box("WellRail2P", (0.06, 0.06, 0.55), (px, 4.35, 13.35), MATS["MetalDark"], 0.0)
    box("RoofSlab", (71, 17.6, 0.6), (0, 0.2, 19.15), trim, 0.03)
    # gờ mái kính lấy sáng
    box("Skylight", (40, 3.4, 0.18), (0, -1.15, 20.0), MATS["Glass"], 0.01, rot=(0.5, 0, 0))
    box("Skylight", (40, 3.4, 0.18), (0, 1.75, 20.0), MATS["Glass"], 0.01, rot=(-0.5, 0, 0))
    box("SkylightCap", (40, 0.5, 0.22), (0, 0.3, 20.82), trim, 0.01)
    # hộp kính sân thượng (thay khối bê tông cũ)
    box("RooftopGlass", (12, 6, 2.3), (-14, -0.5, 20.6), MATS["Glass"], 0.02)
    box("RooftopGlassCap", (12.6, 6.6, 0.25), (-14, -0.5, 21.85), trim, 0.02)
    box("Parapet", (71, 0.45, 0.85), (0, 8.85, 19.0), trim, 0.02)
    box("ParapetB", (71, 0.45, 0.85), (0, -8.6, 19.0), trim, 0.02)
    # lan can sân thượng mặt tiền: trụ + 2 tay vịn
    box("RoofRailTop", (68, 0.09, 0.09), (0, 8.55, 20.30), MATS["MetalDark"], 0.0)
    box("RoofRailMid", (68, 0.07, 0.07), (0, 8.55, 19.90), MATS["MetalDark"], 0.0)
    rposts = []
    for x in range(-33, 34, 3):
        rposts.append(box("tmpRailP", (0.07, 0.07, 0.85), (x, 8.55, 19.88), MATS["MetalDark"], 0.0))
    join_into(rposts, "RoofRailPosts")
    # hàng THÔNG CỘT (thông bút chì) dọc sân thượng + tượng trắng trang trí (ảnh 01)
    for x in range(-31, 32, 6):
        cyl("PencilPineTrunk", 0.06, 0.08, 0.9, (x, 8.15, 19.9), MATS["Trunk"], verts=6)
        cone("PencilPine", 0.37, 3.6, (x, 8.15, 22.15), MATS["PineDark"], verts=8)
    for x in (-19, 1, 21):
        cyl("RoofStatue", 0.11, 0.15, 0.62, (x, 8.15, 19.78), MATS["StatueWhite"], verts=8)
        sphere("RoofStatueHead", 0.11, (x, 8.15, 20.18), MATS["StatueWhite"])
    # --- tường hông + tường sau (-Y) ---
    box("WallL", (0.7, 16, 19), (-34, 0, 9.5), wall, 0.02)
    box("WallR", (0.7, 16, 19), (34, 0, 9.5), wall, 0.02)
    box("WallBack", (68, 0.7, 19), (0, -7.8, 9.5), wall, 0.02)
    for sx in (-34.45, 34.45):
        for zz in (4.5, 10.5, 16.5):
            box("SideTrim", (0.15, 15.6, 0.5), (sx, 0, zz), trim, 0.01)
    # --- cột mặt tiền +Y (GIỮ y=7.8 khớp collider web), x -32..32 bước 8 ---
    for x in range(-32, 33, 8):
        box("Column", (0.9, 0.9, 19), (x, 7.8, 9.5), colM, 0.04)
        box("ColBase", (1.2, 1.2, 0.8), (x, 7.8, 0.4), concD, 0.03)
        box("ColCap", (1.15, 1.15, 0.5), (x, 7.8, 18.6), colM, 0.03)
    # ============ MẶT TIỀN theo ảnh 01 (từ dưới lên) ============
    # V4.8 (research/17 điểm 3 — khác biệt lớn nhất tầm mắt): tầng trệt KHÔNG còn
    # cửa cuốn xám đóng. 7/8 ô là CỬA HIỆU MỞ: hốc sâu + tường hậu phát sáng ấm
    # (MarketWin/AdLED -> web + harness cho phát sáng về đêm) + kệ + hàng + quầy;
    # ô giữa (x=0) giữ CỬA VÀO kính. MÁI HIÊN SỌC liên tục dưới dải pano (ảnh 01).
    goods_mats = [MATS["GoodsA"], MATS["GoodsB"], MATS["GoodsC"], MATS["AdWhite"], MATS["AdGreen"]]
    # các chi tiết nội thất được GỘP (join) theo vật liệu để giữ GLB gọn
    J = {"backW": [], "backL": [], "trim": [], "ceil": [], "step": [], "shelf": [],
         "counter": [], "cord": [], "lamp": [], "goods": {}}
    for bi, x in enumerate(range(-28, 29, 8)):
        if x == 0:
            box("ShopDark", (5.6, 0.18, 3.6), (x, 8.02, 1.85), MATS["GlassDark"], 0.01)
            continue
        J["backL" if bi % 3 == 2 else "backW"].append(
            box("tmpBk", (5.6, 0.15, 3.3), (x, 6.70, 1.72), MATS["AdLED"] if bi % 3 == 2 else MATS["MarketWin"], 0.0))
        for sx in (-2.73, 2.73):
            J["trim"].append(box("tmpSd", (0.14, 1.5, 3.3), (x + sx, 7.30, 1.72), MATS["TrimBrown"], 0.0))
        J["ceil"].append(box("tmpCe", (5.6, 1.5, 0.14), (x, 7.30, 3.42), MATS["ConcreteDk"], 0.0))
        J["trim"].append(box("tmpHd", (5.6, 0.20, 0.55), (x, 8.02, 3.72), MATS["TrimBrown"], 0.0))
        J["step"].append(box("tmpSt", (5.6, 1.7, 0.10), (x, 7.30, 0.05), MATS["Stone"], 0.0))
        for sz in (1.15, 2.05):
            J["shelf"].append(box("tmpSh", (4.9, 0.30, 0.07), (x, 6.80, sz), MATS["WoodDark"], 0.0))
            for j in range(3):
                gm = goods_mats[(bi + j + (1 if sz > 1.5 else 0)) % 5]
                J["goods"].setdefault(gm.name, []).append(
                    box("tmpGd", (0.55, 0.40, 0.50), (x - 1.55 + j * 1.55, 6.85, sz + 0.32), gm, 0.0))
        J["counter"].append(box("tmpCt", (4.4, 0.80, 0.90), (x, 7.35, 0.50), MATS["Wood"], 0.0))
        for j in range(2):
            gm = goods_mats[(bi + j + 2) % 5]
            J["goods"].setdefault(gm.name, []).append(
                box("tmpGd", (0.42, 0.42, 0.36), (x - 0.80 + j * 1.60, 7.40, 1.13), gm, 0.0))
        J["cord"].append(box("tmpCd", (0.04, 0.04, 0.42), (x, 7.30, 3.14), MATS["MetalDark"], 0.0))
        J["lamp"].append(box("tmpLp", (0.17, 0.17, 0.17), (x, 7.30, 2.90), MATS["AdLED"], 0.0))
    join_into(J["backW"], "ShopInBacks"); join_into(J["backL"], "ShopInBacksLED")
    join_into(J["trim"], "ShopInTrims"); join_into(J["ceil"], "ShopInCeils")
    join_into(J["step"], "ShopSteps"); join_into(J["shelf"], "ShopShelves")
    join_into(J["counter"], "ShopCounters"); join_into(J["cord"], "ShopCords")
    join_into(J["lamp"], "ShopLamps")
    for gm_name, objs in J["goods"].items():
        join_into(objs, "ShopGoods_" + gm_name)
    box("Entrance", (6.5, 0.3, 4.4), (0, 7.75, 2.1), MATS["GlassDark"], 0.01)
    # mái hiên sọc từng ô (dưới dải pano, dốc xuống phía phố) — gộp 1 mesh
    awn_parts = []
    for bi, x in enumerate(range(-28, 29, 8)):
        awn = box("tmpAwn", (5.9, 1.15, 0.06), (x, 8.62, 3.62),
                  MATS["StripeA"] if bi % 2 == 0 else MATS["StripeB"], 0.0)
        awn.rotation_euler = (-0.40, 0, 0)
        awn_parts.append(awn)
    join_into(awn_parts, "ShopAwnings")
    # Dải BIỂN QUẢNG CÁO nhiều màu liền mạch trên ki-ốt + LED đỏ ở giữa (ảnh 01)
    # V4.8: pano cao hơn (1.20) + ô lồng hai tông màu cho có nhịp/chi tiết
    ad_mats = [MATS["AdGreen"], MATS["AdYellow"], MATS["AdWhite"], MATS["AdGreen"],
               MATS["AdLED"],
               MATS["AdYellow"], MATS["AdGreen"], MATS["AdWhite"], MATS["AdYellow"]]
    inset_mats = [MATS["AdWhite"], MATS["AdGreen"], MATS["AdLED"], MATS["AdYellow"],
                  MATS["AdWhite"],
                  MATS["AdGreen"], MATS["AdWhite"], MATS["AdYellow"], MATS["AdGreen"]]
    inset_parts = []
    for i, x in enumerate(range(-32, 33, 8)):
        if i == 4:
            box("AdFrame", (7.9, 0.20, 1.50), (x, 8.16, 4.55), MATS["TrimBrown"], 0.01)
        box("AdBand", (7.5, 0.14, 1.20), (x, 8.22, 4.55), ad_mats[i], 0.01)
        inset_parts.append(box("tmpIn", (6.4, 0.16, 0.80), (x, 8.26, 4.55), inset_mats[i], 0.0))
    join_into(inset_parts, "AdInsets")
    box("AdTrimT", (67, 0.2, 0.14), (0, 8.18, 5.24), trim, 0.0)
    box("AdTrimB", (67, 0.2, 0.14), (0, 8.18, 3.86), trim, 0.0)
    # Dải ZIGZAG trắng — chi tiết nhận diện mạnh nhất (ảnh 01 + chợ 1937)
    # V4.1: nền cao hơn (1.42) + xám đậm, chevron cao/dày hơn -> tương phản mạnh
    box("ZigzagBack", (66.5, 0.18, 1.42), (0, 8.04, 5.48), MATS["ZigBack"], 0.0)
    join_into(chevron_row(-33, 33, 8.30, 5.48, M("ZigWhite", (0.96, 0.94, 0.89), 0.9),
                          step=2.0, arm=1.42, thick=0.42, tall=0.62), "Zigzag")
    # Băng HỒNG ĐÀO + cửa sổ tầng 2 (kính MarketWin để web phát sáng đêm)
    # V4.1: băng đậm màu + 3 rãnh ngang tối mô phỏng lam sọc của băng thật
    box("PeachBand", (67, 0.38, 0.92), (0, 8.06, 6.72), MATS["Peach"], 0.01)
    for sz in (6.50, 6.72, 6.94):
        box("PeachSlat", (67, 0.44, 0.055), (0, 8.08, sz), M("PeachDk", (0.58, 0.30, 0.15), 0.95), 0.0)
    box("GlassWin2", (66, 0.25, 2.5), (0, 7.85, 8.35), MATS["MarketWin"], 0.0)
    # V4.8: khung chia ô MÀU KEM + thanh ngang giữa -> dải kính có NHỊP thay tấm phẳng
    for x in range(-32, 33, 4):
        box("Mullion2", (0.20, 0.36, 2.5), (x, 7.92, 8.35), colM, 0.0)
    box("Rail2", (67, 0.34, 0.16), (0, 7.92, 8.35), colM, 0.0)
    box("Sill2", (67, 0.5, 0.3), (0, 7.9, 7.02), colM, 0.02)
    box("Head2", (67, 0.5, 0.3), (0, 7.9, 9.72), colM, 0.02)
    # Dải LAM TRẮNG (louver) tầng 3: kính sau + lam ngang trắng dày
    box("GlassWin3", (66, 0.22, 3.0), (0, 7.82, 11.7), MATS["MarketWin"], 0.0)
    louvers = []
    for i in range(8):
        louvers.append(box("tmpLouver", (66.5, 0.16, 0.13), (0, 8.34, 10.38 + i * 0.39), M("LouverWhite", (0.95, 0.93, 0.88), 0.9), 0.0))
    join_into(louvers, "Louvers")
    # V4.8: cột đứng kem + thanh ngang giữa cho dải lam cũng có nhịp đứng (gộp 1 mesh)
    mull3 = [box("tmpM3", (0.20, 0.34, 2.6), (x, 7.92, 11.7), colM, 0.0) for x in range(-32, 33, 8)]
    mull3.append(box("tmpR3", (67, 0.34, 0.15), (0, 7.92, 11.7), colM, 0.0))
    join_into(mull3, "LouverTrim2")
    box("LouverFrameT", (67, 0.24, 0.26), (0, 8.3, 13.32), trim, 0.0)
    box("LouverFrameB", (67, 0.24, 0.26), (0, 8.3, 10.12), trim, 0.0)
    # Tường kem + CHỮ NỔI 3D "CHỢ ĐÀ LẠT" ĐỎ (ảnh 01) — material SignLetters
    box("LetterWall", (67, 0.5, 3.3), (0, 7.85, 15.15), wall, 0.01)
    text_obj("CHỢ ĐÀ LẠT", 2.6, (0, 8.12, 15.2), (math.pi / 2, 0, math.pi), MATS["SignLetters"], extrude=0.17)
    box("Cornice", (68, 0.4, 0.35), (0, 8.0, 17.05), trim, 0.01)
    # zigzag lặp lại BÊN TRONG nhà (tường trong trên lối đi đặc sản, ảnh 16)
    box("ZigzagBackIn", (60, 0.15, 1.0), (0, 7.30, 5.62), MATS["ZigBack"], 0.0)
    join_into(chevron_row(-30, 30, 7.12, 5.62, M("ZigWhite", (0.96, 0.94, 0.89), 0.9), step=2.4, arm=1.6), "ZigzagIn")
    # ============ MẶT SAU (hướng đồi/cầu — ảnh 02, 03) ============
    # Chữ nổi đỏ gỉ lớn hơn trên tường sau
    text_obj("CHỢ ĐÀ LẠT", 3.1, (3, -8.22, 15.4), (math.pi / 2, 0, 0), MATS["SignLetters"], extrude=0.20)
    box("BackGlassBand", (56, 0.22, 2.6), (3, -8.28, 11.4), MATS["MarketWin"], 0.0)
    # THÁP THANG MÁY KÍNH xanh lá cạnh cửa sau (nhận diện cực mạnh, ảnh 02)
    box("ElevShaft", (3.2, 1.6, 21.5), (-9, -9.0, 10.75), MATS["ElevGlass"], 0.02)
    for ex in (-10.5, -7.5):
        for ey in (-9.75, -8.25):
            box("ElevPost", (0.18, 0.18, 21.5), (ex, ey, 10.75), MATS["MetalDark"], 0.0)
    for zz in (3.5, 7.0, 10.5, 14.0, 17.5, 21.0):
        box("ElevBand", (3.4, 1.8, 0.18), (-9, -9.0, zz), MATS["MetalDark"], 0.0)
    box("ElevCap", (3.7, 2.1, 0.4), (-9, -9.0, 21.7), trim, 0.02)
    # cửa sau + BẠT SỌC xanh–trắng (ảnh 02, 03)
    box("BackDoor", (4.5, 0.3, 3.2), (3, -8.2, 1.6), MATS["GlassDark"], 0.01)
    awn_parts = []
    for i in range(12):
        m = MATS["StripeA"] if i % 2 == 0 else MATS["StripeB"]
        p = box("tmpAwnStripe", (0.55, 2.0, 0.06), (3 + (i - 5.5) * 0.55, -9.05, 3.75), m, 0.0)
        p.rotation_euler = (-0.5, 0, 0)
        awn_parts.append(p)
    join_into(awn_parts, "HillAwning")
    # CẦU THANG TRẮNG ngoài trời bên hông mặt sau (ảnh 03)
    for i in range(10):
        box("BackStairs", (2.2, 0.55, 0.35), (-20, -8.75 - i * 0.30, 6.1 - i * 0.62), MATS["WhiteConc"], 0.01)
    rail = box("BackStairsRail", (0.09, 0.09, 6.2), (-21.15, -10.1, 3.85), MATS["WhiteConc"], 0.0)
    rail.rotation_euler = (2.69, 0, 0)
    # biển tròn shop hai bên cửa sau (ảnh 02)
    for bx, bm in ((-3.5, MATS["AdYellow"]), (9.5, MATS["AdGreen"])):
        c = cyl("ShopDisc", 0.85, 0.85, 0.14, (bx, -8.35, 4.6), bm, verts=20)
        c.rotation_euler = (math.pi / 2, 0, 0)
    # --- dầm trần nội thất + cột trong (giữ nguyên) ---
    for zz in (6.3, 12.6):
        box("BeamIn", (68, 15, 0.4), (0, 0, zz), concD, 0.01)
    for x in range(-24, 25, 12):
        for yy in (-3.5, 3.5):
            box("ColIn", (0.7, 0.7, 6.3), (x, yy, 3.4), conc, 0.03)
    # --- sân thượng tầng 2 (GIỮ NGUYÊN vị trí/kích thước — neo cầu nổi của web) ---
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
    # V4.8 (research/17 điểm 6): đảo R 6.6 -> 10.5 theo tỉ lệ thật (Ø ~35-40m ở
    # tỉ lệ map), thảm hoa thành HỌA TIẾT HÌNH HỌC đọc rõ từ đỉnh thang: vành
    # đỏ liền quanh tâm + 8 quạt hoa/cỏ lớn + 4 vành hoa cầu trên quạt hoa.
    cyl("Base", 10.5, 11.0, 0.55, (0, 0, 0.28), MATS["Stone"], verts=36)
    cyl("Soil", 9.9, 9.9, 0.30, (0, 0, 0.62), MATS["Soil"], verts=36)
    cyl("Lawn", 9.8, 9.8, 0.18, (0, 0, 0.84), MATS["LeafGreen"], verts=36)
    torus("Hedge", 9.8, 0.34, (0, 0, 0.95), MATS["LeafGreen"], scale=(1, 1, 0.72))
    fmats = [MATS["Flower%d" % i] for i in range(6)]
    for s in range(8):
        a0 = s * math.pi / 4 + 0.03; a1 = (s + 1) * math.pi / 4 - 0.03
        sector("FlowerRing", 2.3, 3.5, a0, a1, 0.93, 1.13, MATS["Flower1"])
        if s % 2 == 0:
            sector("FlowerCarpet", 3.5, 9.45, a0, a1, 0.93, 1.13, fmats[(s // 2) % 6])
        else:
            sector("GrassCarpet", 3.5, 9.45, a0, a1, 0.91, 1.05, MATS["PineMid"])
    _fl = []  # V5.1: gộp toàn bộ hoa cầu thành 1 mesh (kẻo 200+ object rời phình GLB)
    for s in range(0, 8, 2):
        fmat = fmats[(s // 2) % 6]
        for ring, cnt, rr in ((4.6, 10, 0.16), (6.3, 13, 0.17), (8.0, 16, 0.16), (9.1, 13, 0.15)):
            for i in range(cnt):
                a = s * math.pi / 4 + (i + 0.5) / cnt * (math.pi / 4)
                x, y = math.cos(a) * ring, math.sin(a) * ring
                _fl.append(sphere("Flower", rr, (x, y, 1.16), MATS["AdWhite"] if i % 4 == 3 else fmat, scale=(1, 1, 0.7), seg=6, ring=4))
    # ============ TƯỢNG ĐÀI ĐÁ XÁM (ảnh 01, 05) ============
    # V4.8: bệ HỘP TRƠN -> CỤM ĐÁ tảng xoay lệch + jitter (bệ đá gồ ghề); cụm 3
    # người CAO hơn (robe 1.55 -> 2.30); toàn cụm LỆCH tây-nam trong đảo
    # (blender (-4.2,-3.2) = three (-4.2,+3.2)) để từ góc bùng binh của
    # research/17 (góc A) đọc TRỌN chữ CHỢ ĐÀ LẠT, tượng không che chữ đầu.
    st = MATS["StatueStone"]
    bx, by = -4.2, -3.2
    cyl("InnerRing", 3.3, 3.6, 0.5, (bx, by, 1.05), MATS["Stone"], verts=24)
    for i in range(14):
        a = i / 14 * math.pi * 2
        _fl.append(sphere("Flower", 0.15, (bx + math.cos(a) * 4.05, by + math.sin(a) * 4.05, 1.10), fmats[i % 6], scale=(1, 1, 0.72), seg=6, ring=4))
    # ==== V5.1 BLENDER-FIRST: TƯỢNG DỰNG LẠI (lệnh 14:15 08/11 — hết "khối xếp") ====
    # Bệ: 3 bậc bo chamfer + thân bệ + gờ nóc, gộp 1 mesh phẳng (StatueBase).
    base_parts = [
        box("tmpStStep1", (4.6, 4.6, 0.34), (bx, by, 1.47), st, 0.05),
        box("tmpStStep2", (3.8, 3.8, 0.34), (bx, by, 1.81), st, 0.05),
        box("tmpStStep3", (3.05, 3.05, 0.36), (bx, by, 2.15), st, 0.05),
        box("tmpStPlinth", (2.45, 2.45, 1.02), (bx, by, 2.84), st, 0.04),
        box("tmpStTrim", (2.74, 2.74, 0.16), (bx, by, 3.42), st, 0.03),
    ]
    join_into(base_parts, "StatueBase")
    # Cụm 3 tượng: robe THUÔN (cone 16 cạnh, chân 0.52 -> vai 0.30) + ngực nở +
    # đầu cầu + tay trụ giơ cao hướng ra ngoài; tượng GIỮA cao hơn và giơ 2 tay.
    # Gộp 1 mesh + smooth shading -> silhouette liền, nhìn cận cũng ra tượng.
    fig_base = 3.50
    fig_parts = []
    for (fa, fh, fs, two_arms) in ((0.0, 2.95, 1.0, True), (2.25, 2.55, 0.9, False), (4.15, 2.55, 0.9, False)):
        fx, fy = bx + math.cos(fa) * 0.58, by + math.sin(fa) * 0.58
        fig_parts.append(cyl("tmpFigRobe", 0.30 * fs, 0.52 * fs, fh * 0.80, (fx, fy, fig_base + fh * 0.40), st, verts=16, bevel=0.03))
        fig_parts.append(sphere("tmpFigChest", 0.40 * fs, (fx, fy, fig_base + fh * 0.82), st, scale=(1.05, 1.05, 0.85), seg=12, ring=9))
        fig_parts.append(sphere("tmpFigHead", 0.27 * fs, (fx, fy, fig_base + fh + 0.14), st, seg=12, ring=9))
        for sgn in ((1, -1) if two_arms else (1,)):
            ax, ay = fx + math.cos(fa) * 0.46 * sgn, fy + math.sin(fa) * 0.46 * sgn
            arm = cyl("tmpFigArm", 0.065, 0.10, 1.02, (ax, ay, fig_base + fh * 0.92), st, verts=8, bevel=0.02)
            arm.rotation_euler = (math.sin(fa) * 0.80 * sgn, -math.cos(fa) * 0.80 * sgn, 0)
            fig_parts.append(arm)
            fig_parts.append(sphere("tmpFigHand", 0.09, (ax + math.cos(fa) * 0.34 * sgn, ay + math.sin(fa) * 0.34 * sgn, fig_base + fh * 0.92 + 0.42), st, seg=8, ring=6))
    # thông đá trên đỉnh cụm (giữ silhouette đã chốt từ v4) — TUYẾN C đối chiếu
    # dump GLB cũ: đỉnh tượng cũ cao 9.56; thân thông kéo dài + nâng 3 tán để
    # tổng chiều cao cụm tượng khôi phục ~9.60 (bản dựng đầu của V5.1 chỉ 7.56).
    fig_parts.append(cyl("tmpStTrunk", 0.09, 0.13, 3.10, (bx, by, fig_base + 2.90), st, verts=8))
    for r, h, z in ((0.70, 0.95, fig_base + 4.55), (0.52, 0.82, fig_base + 5.20), (0.33, 0.70, fig_base + 5.75)):
        fig_parts.append(cone("tmpStPine", r, h, (bx, by, z), st, verts=9))
    statue_fig = join_into(fig_parts, "Statue")
    for p in statue_fig.data.polygons: p.use_smooth = True
    # V5.1: GHẾ ĐÁ BO CONG theo vành đảo (sector cong thay hộp thẳng) + gờ đá quanh đế.
    cyl("CurbRing", 11.15, 11.15, 0.14, (0, 0, 0.52), MATS["Stone"], verts=48)
    for i in range(4):
        am = math.pi / 4 + i * math.pi / 2
        sector("BenchSeat", 11.55, 12.25, am - 0.14, am + 0.14, 0.42, 0.56, MATS["BenchWhite"], seg=5)
        sector("BenchBack", 12.13, 12.25, am - 0.14, am + 0.14, 0.56, 1.05, MATS["BenchWhite"], seg=5)
        for sgn in (-1, 1):
            aa = am + sgn * 0.105
            box("BenchLeg", (0.40, 0.40, 0.42), (math.cos(aa) * 11.9, math.sin(aa) * 11.9, 0.21), MATS["BenchWhite"], 0.02)
    join_into(_fl, "Flowers")
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
    # V4.8 (research/17 điểm 9): hạ lan can + mái vòm THẤP/MỎNG hơn để cầu bớt
    # chiếm khung ở góc bùng binh & góc đường vào (điểm đáp tầng 2 giữ nguyên).
    for sx in (-2.82, 2.82):
        box("Parapet", (0.30, 39.2, 0.80), (sx, 0, 0.68), MATS["Concrete"], 0.02)
        box("ParapetCap", (0.46, 39.2, 0.12), (sx, 0, 1.13), MATS["ConcreteDk"], 0.01)
    # MÁI KÍNH VÒM che cầu + kính hông + dây đèn (chuẩn A6: cầu mái kính vào chợ)
    for sx in (-2.82, 2.82):
        for yy in (-18, -9, 0, 9, 18):
            box("RoofPost", (0.13, 0.13, 1.30), (sx, yy, 1.75), MATS["WoodDark"], 0.01)
        for yy in (-13.5, -4.5, 4.5, 13.5):
            box("SideGlass", (0.05, 8.4, 0.95), (sx, yy, 1.68), MATS["Glass"], 0.0)
    for ang, xo, zo in ((-0.9, -2.58, 2.55), (-0.45, -1.44, 3.22), (0.0, 0, 3.45), (0.45, 1.44, 3.22), (0.9, 2.58, 2.55)):
        rp = box("RoofGlass", (1.78, 39.2, 0.07), (xo, 0, zo), MATS["Glass"], 0.0)
        rp.rotation_euler = (0, ang, 0)
    box("RidgeBeam", (0.2, 39.2, 0.2), (0, 0, 3.52), MATS["WoodDark"], 0.01)
    for yy in (-19.4, 19.4):
        box("EndBeam", (5.6, 0.18, 0.22), (0, yy, 2.85), MATS["WoodDark"], 0.01)
    for i in range(9):
        sphere("RoofLight", 0.075, (0, -16 + i * 4, 3.05), MATS["LanternGlow"])
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
    # V4.5 (research/16 mục 4.1): thang RỘNG 22 (từ 11) = làn đi giữa 7 + 2 dải
    # "khán đài" ngồi ăn; chiếu nghỉ nới sâu 2.5 -> 4 (rút mỗi chuyến kề 0.75).
    # Bậc bỏ bevel (nén GLB — bevel 0.01 không đọc được ở tỉ lệ này).
    # LandingTop hạ cho MẶT TẤM = đúng stairH (bản cũ cao hơn 0.345: chân chìm).
    clear_scene()
    stone, stone2 = MATS["Stone"], MATS["Concrete"]
    W = 22
    def flight(y_top, run_total, steps, h_top, h_bot):
        run = run_total / steps
        for i in range(steps):
            h = h_top + (h_bot - h_top) * (i / steps)
            yc = y_top - run * (i + 0.5)
            box("Step", (W, run + 0.06, max(h, 0.25)), (0, yc, max(h, 0.25) / 2), stone if i % 2 else stone2, 0.0)
    # chuyến A: y +14..+6.75 (world -30..-22.75), 17 -> 11.33
    flight(14, 7.25, 10, 17, 11.33)
    # chiếu nghỉ 1: y +6.75..+2.75 (world -22.75..-18.75), h 11.33
    box("Landing1", (W + 2, 4, 11.33), (0, 4.75, 11.33 / 2), stone2, 0.0)
    box("Landing1Top", (W, 4, 0.35), (0, 4.75, 11.33 - 0.175), MATS["CanvasOld"], 0.01)
    # chuyến B: y +2.75..-3.75 (world -18.75..-12.25), 11.33 -> 5.67
    flight(2.75, 6.5, 10, 11.33, 5.67)
    # chiếu nghỉ 2: y -3.75..-7.75 (world -12.25..-8.25), h 5.67
    box("Landing2", (W + 2, 4, 5.67), (0, -5.75, 5.67 / 2), stone2, 0.0)
    box("Landing2Top", (W, 4, 0.35), (0, -5.75, 5.67 - 0.175), MATS["CanvasOld"], 0.01)
    # chuyến C: y -7.75..-14 (world -8.25..-2), 5.67 -> 0
    flight(-7.75, 6.25, 10, 5.67, 0)
    # vách hông dốc 2 bên (khối nghiêng theo sườn tổng)
    for sx in (-11.35, 11.35):
        wall = box("SideWall", (0.5, 33, 1.6), (sx, 0, 8.0), MATS["ConcreteDk"], 0.02)
        wall.rotation_euler = (math.atan2(17, 28), 0, 0)
        rail = box("HandRail", (0.16, 31, 0.16), (sx * 0.985, 0, 9.3), MATS["WoodDark"], 0.01)
        rail.rotation_euler = (math.atan2(17, 28), 0, 0)
    export("stairs")

# ============================================================
#  XE CỘ (V4 MỚI) — vehicle.glb gồm 2 group gốc: "Moto" (xe máy + người lái
#  chibi) và "Car" (bán tải). Mặt trước -Y blender (= +Z three) như nhân vật.
#  Bánh xe là object riêng (WheelF/WheelR/WheelFL...) để web quay theo tốc độ.
# ============================================================
def build_vehicle():
    clear_scene()
    dark, tire, pot = MATS["VehDark"], MATS["TireMat"], MATS["PotMetal"]
    # ---------- MOTO ----------
    wf = wheel("WheelF", 0.33, 0.09, (0, -0.78, 0.33), tire, pot)
    wr = wheel("WheelR", 0.33, 0.09, (0, 0.72, 0.33), tire, pot)
    body = []
    body.append(box("tmpBikeFloor", (0.34, 0.80, 0.10), (0, 0.02, 0.40), dark, 0.02))
    shield = box("tmpBikeShield", (0.42, 0.10, 0.64), (0, -0.50, 0.80), MATS["BikeBody"], 0.03)
    shield.rotation_euler = (-0.32, 0, 0); body.append(shield)
    body.append(box("tmpBikeBar", (0.48, 0.05, 0.05), (0, -0.56, 1.08), dark, 0.01))
    body.append(box("tmpBikeStem", (0.07, 0.09, 0.34), (0, -0.53, 0.94), dark, 0.01))
    body.append(box("tmpBikeSeat", (0.36, 0.64, 0.13), (0, 0.30, 0.80), dark, 0.03))
    body.append(box("tmpBikeRear", (0.38, 0.56, 0.44), (0, 0.44, 0.56), MATS["BikeBody"], 0.03))
    fender = box("tmpBikeFender", (0.30, 0.44, 0.06), (0, -0.78, 0.60), MATS["BikeBody"], 0.01)
    fender.rotation_euler = (0.5, 0, 0); body.append(fender)
    body.append(box("tmpBikeTail", (0.30, 0.10, 0.16), (0, 0.76, 0.72), MATS["BikeBody"], 0.02))
    bike = join_into(body, "BikeBody")
    lamp_m = sphere("HeadLamp", 0.075, (0, -0.585, 0.97), MATS["HeadLamp"])
    # người lái chibi ngồi (pose tĩnh): hông + thân nghiêng + tay tới tay lái + chân gập
    rider = []
    rider.append(box("tmpRiderHip", (0.40, 0.30, 0.26), (0, 0.30, 0.95), MATS["Pants"], 0.05))
    torso = box("tmpRiderTorso", (0.47, 0.27, 0.64), (0, 0.14, 1.30), MATS["RiderShirt"], 0.07)
    torso.rotation_euler = (0.16, 0, 0); rider.append(torso)
    rider.append(sphere("tmpRiderHead", 0.205, (0, 0.03, 1.74), MATS["Skin"]))
    for sx in (-0.29, 0.29):
        arm = box("tmpRiderArm", (0.11, 0.64, 0.11), (sx, -0.22, 1.27), MATS["RiderShirt"], 0.04)
        arm.rotation_euler = (-2.50, 0, 0); rider.append(arm)
        thigh = box("tmpRiderThigh", (0.13, 0.52, 0.13), (sx * 0.62, -0.05, 0.80), MATS["Pants"], 0.04)
        thigh.rotation_euler = (-1.15, 0, 0); rider.append(thigh)
        shin = box("tmpRiderShin", (0.12, 0.13, 0.46), (sx * 0.62, 0.10, 0.52), MATS["Pants"], 0.04)
        shin.rotation_euler = (0.25, 0, 0); rider.append(shin)
        rider.append(box("tmpRiderShoe", (0.13, 0.30, 0.09), (sx * 0.62, -0.02, 0.33), MATS["Shoe"], 0.02))
    rider_o = join_into(rider, "Rider")
    helmet = sphere("Helmet", 0.235, (0, 0.03, 1.76), MATS["Helmet"], scale=(1, 1, 0.85))
    moto = bpy.data.objects.new("Moto", None)
    bpy.context.collection.objects.link(moto)
    for o in (wf, wr, bike, lamp_m, rider_o, helmet):
        o.parent = moto
    # ---------- CAR (bán tải) ----------
    cbody = []
    cbody.append(box("tmpCarBase", (1.78, 4.30, 0.55), (0, 0, 0.62), MATS["CarBody"], 0.04))
    cbody.append(box("tmpCarCab", (1.68, 1.70, 0.62), (0, -0.55, 1.18), MATS["CarBody"], 0.04))
    shield = box("tmpCarShield", (1.58, 0.07, 0.55), (0, -1.33, 1.24), MATS["GlassDark"], 0.01)
    shield.rotation_euler = (0.35, 0, 0); cbody.append(shield)
    for sx in (-0.86, 0.86):
        cbody.append(box("tmpCarSideWin", (0.06, 1.35, 0.40), (sx, -0.55, 1.30), MATS["GlassDark"], 0.01))
        cbody.append(box("tmpCarBedSide", (0.08, 1.55, 0.52), (sx, 1.55, 0.98), MATS["CarBody"], 0.02))
    cbody.append(box("tmpCarBedTail", (1.78, 0.08, 0.52), (0, 2.30, 0.98), MATS["CarBody"], 0.02))
    cbody.append(box("tmpCarBumpF", (1.86, 0.25, 0.26), (0, -2.22, 0.45), dark, 0.02))
    cbody.append(box("tmpCarBumpR", (1.86, 0.25, 0.26), (0, 2.22, 0.45), dark, 0.02))
    car = join_into(cbody, "CarBody")
    cwheels = [wheel("WheelFL", 0.37, 0.24, (-0.82, -1.45, 0.37), tire, pot),
               wheel("WheelFR", 0.37, 0.24, (0.82, -1.45, 0.37), tire, pot),
               wheel("WheelRL", 0.37, 0.24, (-0.82, 1.45, 0.37), tire, pot),
               wheel("WheelRR", 0.37, 0.24, (0.82, 1.45, 0.37), tire, pot)]
    hl1 = sphere("tmpHL", 0.09, (-0.60, -2.16, 0.80), MATS["HeadLamp"])
    hl2 = sphere("tmpHL", 0.09, (0.60, -2.16, 0.80), MATS["HeadLamp"])
    carlamp = join_into([hl1, hl2], "HeadLamp")
    car_g = bpy.data.objects.new("Car", None)
    bpy.context.collection.objects.link(car_g)
    for o in [car, carlamp] + cwheels:
        o.parent = car_g
    export("vehicle")

# ============================================================
#  KHÁCH SẠN QUANH KHU (V4 bổ sung 09:57) — hotels.glb gồm 4 group gốc
#  HotelA/B/C/D. Phông nền: khối 4–6 tầng, cửa sổ đều nhịp có lớp (khung nổi
#  + kính lõm), ban công vài tầng, gờ chỉ từng tầng, biển chữ nổi nóc phát
#  sáng đêm (material HS*), cửa sổ 3 loại HotelWinA/B/C để web cho sáng rải
#  rác ban đêm. Mặt tiền -Y blender (= +Z three) như rạp/café.
# ============================================================
def _group_new(name, before):
    g = bpy.data.objects.new(name, None)
    bpy.context.collection.objects.link(g)
    for o in list(bpy.data.objects):
        if o not in before and o is not g and o.parent is None:
            o.parent = g
    return g

def _hotel_variant(sign, sign_mat, sign_size, W, D, floors, wall_mat, frame_mat,
                   band_style=False, tank=False):
    H = 1.2 + floors * 3.05
    box("HotelBody", (W, D, H), (0, 0, H / 2), wall_mat, 0.05)
    box("HotelBase", (W + 0.2, D + 0.2, 1.05), (0, 0, 0.52), MATS["TrimBrown"], 0.03)
    box("HotelDoor", (2.7, 0.22, 2.3), (0, -D / 2 - 0.02, 1.15), MATS["GlassDark"], 0.01)
    awn = box("HotelAwn", (3.6, 1.3, 0.09), (0, -D / 2 - 0.65, 2.55), MATS["CanvasOld"], 0.01)
    awn.rotation_euler = (0.42, 0, 0)
    win_mats = [MATS["HotelWinA"], MATS["HotelWinB"], MATS["HotelWinC"]]
    cols = max(3, int((W - 2.4) / 2.6))
    xs = [-(cols - 1) * 1.3 + i * 2.6 for i in range(cols)]
    for f in range(floors):
        zc = 2.0 + f * 3.05
        box("HotelCornice", (W + 0.4, D + 0.4, 0.18), (0, 0, 0.55 + (f + 1) * 3.05), frame_mat, 0.01)
        if band_style:
            box("HotelGlassBand", (W - 2.0, 0.14, 1.5), (0, -D / 2 - 0.05, zc), MATS["VIBGlass"], 0.0)
            for x in xs:
                box("HotelMullion", (0.12, 0.18, 1.5), (x, -D / 2 - 0.05, zc), MATS["MetalDark"], 0.0)
            continue
        for ci, x in enumerate(xs):
            wm = win_mats[(f * 7 + ci * 3) % 5 if (f * 7 + ci * 3) % 5 < 3 else 2]
            if (f * 7 + ci * 3) % 5 == 0: wm = win_mats[0]
            elif (f * 7 + ci * 3) % 5 == 2: wm = win_mats[1]
            else: wm = win_mats[2]
            box("HotelWinFrame", (1.25, 0.16, 1.55), (x, -D / 2 - 0.05, zc), frame_mat, 0.01)
            box("HotelWinGlass", (1.05, 0.08, 1.35), (x, -D / 2 - 0.10, zc), wm, 0.0)
            if f % 2 == 1 and ci in (1, cols - 2):
                box("HotelBalcony", (1.9, 0.85, 0.12), (x, -D / 2 - 0.45, zc - 0.85), frame_mat, 0.01)
                box("HotelBalcRail", (1.9, 0.06, 0.06), (x, -D / 2 - 0.85, zc - 0.30), MATS["MetalDark"], 0.0)
                for px in (-0.85, 0.0, 0.85):
                    box("HotelBalcPost", (0.05, 0.05, 0.55), (x + px, -D / 2 - 0.85, zc - 0.58), MATS["MetalDark"], 0.0)
    box("HotelRoofSlab", (W + 0.6, D + 0.6, 0.3), (0, 0, H + 0.12), frame_mat, 0.02)
    box("HotelParapet", (W + 0.2, 0.3, 0.65), (0, -D / 2 - 0.05, H + 0.55), wall_mat, 0.01)
    if tank:
        cyl("HotelTank", 0.95, 1.05, 1.7, (W / 2 - 1.8, D / 2 - 1.6, H + 1.1), MATS["ConcreteDk"], verts=12)
        cone("HotelTankCap", 1.15, 0.6, (W / 2 - 1.8, D / 2 - 1.6, H + 2.2), MATS["TrimBrown"], verts=12)
    box("HotelSignPost", (0.14, 0.14, 1.0), (-W / 4, -D / 2 - 0.1, H + 0.7), MATS["MetalDark"], 0.0)
    box("HotelSignPost", (0.14, 0.14, 1.0), (W / 4, -D / 2 - 0.1, H + 0.7), MATS["MetalDark"], 0.0)
    text_obj(sign, sign_size, (0, -D / 2 - 0.18, H + 1.55), (math.pi / 2, 0, 0), sign_mat, extrude=0.10, name="HotelSign")

def build_hotels():
    clear_scene()
    before = set(bpy.data.objects)
    _hotel_variant("DALAT CENTER", MATS["HSYellow"], 1.5, 16, 10, 6, MATS["HotelWhite"], MATS["WhiteConc"])
    _group_new("HotelA", before)
    before = set(bpy.data.objects)
    _hotel_variant("HOTEL COLLINE", MATS["HSWhite"], 1.3, 13, 9, 5, MATS["WallCream"], MATS["TrimBrown"], tank=True)
    _group_new("HotelB", before)
    before = set(bpy.data.objects)
    _hotel_variant("VIB", MATS["HSWhite"], 2.8, 14, 9, 6, MATS["VIBWall"], MATS["MetalDark"], band_style=True)
    _group_new("HotelC", before)
    before = set(bpy.data.objects)
    _hotel_variant("THANH BÌNH", MATS["HSBlue"], 1.4, 11, 8, 4, MATS["HotelWhite"], MATS["StripeA"], tank=True)
    _group_new("HotelD", before)
    export("hotels")

# ============================================================
#  QUÁN NƯỚC / CÀ PHÊ VỈA HÈ (V4 bổ sung 09:57) — shop.glb: nhà 2 tầng,
#  tiền -Y blender. Tầng trệt lõm tối + quầy, hiên bạt, biển (web áp canvas),
#  tầng 2 ban công nhỏ + 2 cửa sổ.
# ============================================================
def build_shop():
    clear_scene()
    glow = M("ShopGlow", (0.85, 0.62, 0.30), 0.5, 0.0, emit=(0.80, 0.45, 0.12), ei=0.5)
    box("Body", (5.4, 4.6, 6.8), (0, 0, 3.4), MATS["ShopWall"], 0.05)
    box("Base", (5.6, 4.8, 0.9), (0, 0, 0.45), MATS["TrimBrown"], 0.03)
    # tầng trệt: hốc quán tối + quầy + vách trong ấm sáng
    box("Recess", (4.6, 0.22, 2.9), (0, -2.32, 1.5), MATS["GlassDark"], 0.01)
    box("GlowBack", (4.4, 0.14, 2.5), (0, -1.15, 1.55), glow, 0.0)
    box("Counter", (4.2, 0.6, 0.95), (0, -1.80, 0.48), MATS["WoodDark"], 0.02)
    box("CounterTop", (4.4, 0.75, 0.08), (0, -1.80, 0.99), MATS["WoodLight"], 0.01)
    for i in range(3):
        cyl("StoolIn", 0.16, 0.13, 0.45, (-1.2 + i * 1.2, -1.55, 0.23), MATS["StripeA"], verts=10)
    # hiên bạt + biển hiệu (web áp canvas lên mặt trước bảng)
    awn = box("ShopAwn", (5.9, 2.3, 0.10), (0, -3.15, 3.15), MATS["ShopAwn"], 0.01)
    awn.rotation_euler = (0.42, 0, 0)
    box("SignBoard", (5.2, 0.16, 1.05), (0, -2.44, 4.55), MATS["SignBoard"], 0.02)
    # tầng 2: cửa ra ban công + 2 cửa sổ khung trắng + ban công
    box("BalconySlab", (4.8, 0.85, 0.12), (0, -2.68, 4.28), MATS["WhiteConc"], 0.01)
    box("DoorUp", (1.0, 0.14, 2.0), (0, -2.33, 5.15), MATS["GlassDark"], 0.01)
    for sx in (-1.55, 1.55):
        box("WinFrame", (1.1, 0.15, 1.4), (sx, -2.34, 5.2), MATS["WhiteConc"], 0.01)
        box("WinGlass", (0.92, 0.08, 1.22), (sx, -2.38, 5.2), MATS["HotelWinC"], 0.0)
    box("BalcRail", (4.8, 0.06, 0.06), (0, -3.08, 4.95), MATS["WoodDark"], 0.0)
    for px in (-2.3, -1.15, 0.0, 1.15, 2.3):
        box("BalcPost", (0.055, 0.055, 0.62), (px, -3.08, 4.65), MATS["WoodDark"], 0.0)
    # mái đua + khối nóc
    box("RoofSlab", (5.9, 5.1, 0.25), (0, 0, 6.95), MATS["TrimBrown"], 0.02)
    box("RoofBox", (2.2, 2.0, 0.9), (1.2, 0.2, 7.5), MATS["Concrete"], 0.03)
    export("shop")

build_character()
print("CHARACTER-HEAD-LP-POLISH DONE")
