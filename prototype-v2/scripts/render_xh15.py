# -*- coding: utf-8 -*-
"""XH-1.5 RESCALE — RENDER NGHIỆM THU MẶT NƯỚC MỞ RỘNG HỒ XUÂN HƯƠNG (mô phỏng đúng thông số code).

Mở rộng render_xh1.py theo khung XH-1.5: mặt nước 336x160 tại (-392, 4.9, 116),
repeat gợn (63,30); đáy hồ cùng cỡ tại 4.82; tường chân taluy bờ nam XA z 196;
vèn mép nước tây x -560 (2 đoạn, giữa là đập); mép đông kéo dài z 36..196;
dải nền bờ tây x -572..-560; taluy nam xa z 196..224 (rot -0.1244) + thềm z
224..234; cầu Ông Đạo DỜI về (-557, 95) z 60..130; 24 thông silhouette bờ nam
xa (y = groundH mới); 4 villa mờ trên thềm nam; đảo/kè bắc/lát giữ nguyên XH-1.

Góc quyết định "hồ hay ao": PROM đứng bờ bắc (-288, 32) nhìn TÂY-NAM qua mặt
nước (ngày + đêm) + topdown khung mới + diorama từ đông-nam cao.

Thông số nước theo code: base teal 0x276a8a (bake trong texture), roughness
0.15, alpha 0.93; ĐÊM: emissive 0x1d4e5f x 0.55 (applyDayNight/waterMats) —
bản đêm là bản chính vì game mặc định 19:00. Harness KHÔNG mô phỏng FogExp2
của game (đo riêng bằng số: far 600; mật độ sương ngày 0.0035 / 19h 0.0044 /
22h 0.0054 — truyền qua tới bờ nam xa ~0.44 ở 19:00, silhouette mờ vẫn hiện).

Quy ước trục: three (x, y-up, z) -> Blender (x, -z, y); rotY -> rotation_z.

Chạy: ~/workspace/vinh-trang-3d/tools/blender5/blender --background \
        --threads 2 --python scripts/render_xh15.py
Xuất: renders/xh15-topdown.png, xh15-dia.png, xh15-prom-day.png, xh15-prom-night.png
"""
import bpy, math, os
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
OUT = os.path.join(ROOT, "renders")
os.makedirs(OUT, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)

def tb(p):
    return Vector((p[0], -p[2], p[1]))

def mat_rgb(name, hexcol, rough=0.95, emission=None, estr=0.0, alpha=1.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes['Principled BSDF']
    r = ((hexcol >> 16) & 255) / 255.0; g = ((hexcol >> 8) & 255) / 255.0; b = (hexcol & 255) / 255.0
    bsdf.inputs['Base Color'].default_value = (r, g, b, 1.0)
    bsdf.inputs['Roughness'].default_value = rough
    if alpha < 1.0: bsdf.inputs['Alpha'].default_value = alpha
    if emission is not None:
        er = ((emission >> 16) & 255) / 255.0; eg = ((emission >> 8) & 255) / 255.0; eb = (emission & 255) / 255.0
        bsdf.inputs['Emission Color'].default_value = (er, eg, eb, 1.0)
        bsdf.inputs['Emission Strength'].default_value = estr
    m.diffuse_color = (r, g, b, alpha)
    return m

def mat_tex(name, png, rx, ry, rough=0.95):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes['Principled BSDF']
    bsdf.inputs['Roughness'].default_value = rough
    tex = m.node_tree.nodes.new('ShaderNodeTexImage')
    tex.image = bpy.data.images.load(os.path.join(OUT, png))
    tex.extension = 'REPEAT'
    mp = m.node_tree.nodes.new('ShaderNodeMapping'); mp.inputs['Scale'].default_value = (rx, ry, 1.0)
    tc = m.node_tree.nodes.new('ShaderNodeTexCoord')
    m.node_tree.links.new(tc.outputs['UV'], mp.inputs['Vector'])
    m.node_tree.links.new(mp.outputs['Vector'], tex.inputs['Vector'])
    m.node_tree.links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])
    return m

def boxm(w, h, d, material, x, y, z, rot_x=0.0, rot_z=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1)
    o = bpy.context.active_object
    o.dimensions = (w, d, h)
    o.location = tb((x, y, z))
    if rot_x: o.rotation_euler.x = rot_x
    if rot_z: o.rotation_euler.z = rot_z
    o.data.materials.append(material)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return o

def box(w, h, d, hexcol, x, y, z, rot_x=0.0, rot_z=0.0):
    return boxm(w, h, d, mat_rgb('m%06x' % hexcol, hexcol), x, y, z, rot_x, rot_z)

def cylm(r_top, r_bot, h, material, x, y, z, verts=40):
    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=1, vertices=verts)
    o = bpy.context.active_object
    # CylinderGeometry three (rTop, rBottom): Blender cylinder đồng nhất — dùng cone để có 2 bán kính
    bpy.ops.object.delete()
    bpy.ops.mesh.primitive_cone_add(radius1=r_bot, radius2=r_top, depth=h, vertices=verts)
    o = bpy.context.active_object
    o.location = tb((x, y, z))
    o.data.materials.append(material)
    return o

def cyl(r, h, hexcol, x, y, z, verts=40):
    return cylm(r, r, h, mat_rgb('c%06x' % hexcol, hexcol), x, y, z, verts)

def plane(w, d, hexcol, x, y, z, rough=0.95):
    bpy.ops.mesh.primitive_plane_add(size=1)
    o = bpy.context.active_object
    o.dimensions = (w, d, 0)
    o.location = tb((x, y, z))
    o.data.materials.append(mat_rgb('p%06x' % hexcol, hexcol, rough))
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return o

def planem(w, d, material, x, y, z):
    bpy.ops.mesh.primitive_plane_add(size=1)
    o = bpy.context.active_object
    o.dimensions = (w, d, 0)
    o.location = tb((x, y, z))
    o.data.materials.append(material)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return o

def pine_fake(x, y, z, s):
    # thông gần đúng cho harness: thân + 2 nón (GLB pine thật chỉ ở trong game)
    m_trunk = mat_rgb('trunk', 0x5a4632)
    m_leaf = mat_rgb('leaf', 0x39543a)
    cylm(0.14 * s, 0.18 * s, 1.6 * s, m_trunk, x, y + 0.8 * s, z, 8)
    for (rr, hh, yy) in [(2.0, 3.4, 3.4), (1.4, 2.6, 5.4)]:
        bpy.ops.mesh.primitive_cone_add(radius1=rr * s, radius2=0.0, depth=hh * s, vertices=10)
        o = bpy.context.active_object
        o.location = tb((x, y + yy * s, z))
        o.data.materials.append(m_leaf)

# ---------- vật liệu texture (đúng file sinh từ hàm seed JS) ----------
PROM = mat_tex('prom', 'xh1-prom-tex.png', 18, 1, 0.92)
PROM_PATH = mat_tex('promPath', 'xh1-prom-tex.png', 0.75, 4, 0.92)
STONE25 = mat_tex('stone25', 'xh1-stone-tex.png', 25, 1, 0.95)
STONE6 = mat_tex('stone6', 'xh1-stone-tex.png', 6, 1, 0.95)
STONE32 = mat_tex('stone32', 'xh1-stone-tex.png', 32, 1, 0.95)
STONE20 = mat_tex('stone20', 'xh1-stone-tex.png', 20, 1, 0.95)
STONE24 = mat_tex('stone24', 'xh1-stone-tex.png', 24, 1, 0.95)
STONE9 = mat_tex('stone9', 'xh1-stone-tex.png', 9, 1, 0.95)
STONE84 = mat_tex('stone84', 'xh1-stone-tex.png', 84, 1, 0.95)
STONE40 = mat_tex('stone40', 'xh1-stone-tex.png', 40, 1, 0.95)
STONE18 = mat_tex('stone18', 'xh1-stone-tex.png', 18, 1, 0.95)
STONE17 = mat_tex('stone17', 'xh1-stone-tex.png', 17, 1, 0.95)
WATER = mat_tex('water', 'xh1-ripple-tex.png', 63, 30, 0.15)
_bsdf_w = WATER.node_tree.nodes['Principled BSDF']
_bsdf_w.inputs['Alpha'].default_value = 0.93
_er, _eg, _eb = 0x1d / 255.0, 0x4e / 255.0, 0x5f / 255.0
_bsdf_w.inputs['Emission Color'].default_value = (_er, _eg, _eb, 1.0)
_bsdf_w.inputs['Emission Strength'].default_value = 0.0   # ngày: 0 — đêm bật 0.55

# ---------- KHU HỒ XH-1.5 — chép đúng số trong index.html ----------
box(144, 0.06, 61, 0x5f8547, -288, 5.45, 5.5)                       # nền cỏ thềm bờ bắc
boxm(144, 0.04, 8, PROM, -288, 5.47, 32)                            # lát đường dạo z 28..36
boxm(6, 0.05, 31.6, PROM_PATH, -219, 5.515, 17, rot_z=math.atan2(-26, 18))  # lối nối lát đá
plane(336, 160, 0x14425c, -392, 4.82, 116, rough=1.0)               # đáy hồ sâu (XH-1.5: 336x160)
planem(336, 160, WATER, -392, 4.9, 116)                             # MẶT NƯỚC MỞ RỘNG
boxm(100.8, 1.3, 0.7, STONE25, -301.6, 4.98, 36)                    # kè bắc tây
boxm(24.8, 1.3, 0.7, STONE6, -236.4, 4.98, 36)                      # kè bắc đông
box(100.8, 0.09, 0.9, 0xd8d2c2, -301.6, 5.6, 36)                    # bó vỉa sáng
box(24.8, 0.09, 0.9, 0xd8d2c2, -236.4, 5.6, 36)
boxm(336, 1.15, 0.7, STONE84, -392, 4.95, 196)                      # tường chân taluy bờ nam XA z 196
boxm(0.7, 1.15, 24, STONE6, -560, 4.95, 48)                         # mép nước tây đoạn bắc z 36..60
boxm(0.7, 1.15, 66, STONE17, -560, 4.95, 163)                       # mép nước tây đoạn nam z 130..196
boxm(0.7, 1.15, 160, STONE40, -224, 4.95, 116)                      # mép nước đông z 36..196
cyl(15, 0.06, 0x5f8547, -250, 5.45, 58)                             # đĩa đảo R15
cylm(15.7, 16.6, 1.2, STONE24, -250, 4.84, 58, 40)                  # vèn kè đảo (nắp 5.44 — dưới đĩa cỏ/vòng lát)
cyl(13.8, 0.02, 0xdde2e2, -250, 5.49, 58)                           # vòng đường lát đảo (đĩa)
cyl(9.0, 0.02, 0x5f8547, -250, 5.5, 58)                             # cỏ tâm đảo trên vòng lát
box(3, 0.08, 7, 0xdde2e2, -250, 5.46, 39.5)                         # dải cầu -> đảo
box(12, 0.06, 160, 0x5f8547, -566, 5.45, 116)                       # dải nền bờ tây sau đập (x -572..-560)
box(17, 0.06, 80, 0x5f8547, -215.5, 5.45, 76)                       # bờ đông nới rộng
box(344, 0.08, 28.4, 0x5f8547, -390, 7.22, 210, rot_x=-0.1244)      # taluy bờ nam XA (z 196..224)
box(344, 0.06, 10, 0x5f8547, -390, 8.94, 229)                       # thềm sau taluy xa (z 224..234)
# cầu Ông Đạo (S4) — XH-1.5 tại đầu tây (-557, 95), z 60..130
boxm(8, 1.9, 70, STONE18, -557, 5.15, 95)
box(8.4, 0.12, 70, 0x4a4a4a, -557, 6.16, 95)
for dz in range(64, 127, 4):
    box(0.09, 0.55, 0.09, 0xe8e4da, -553.3, 6.5, dz)
box(0.07, 0.07, 68, 0xe8e4da, -553.3, 6.74, 95)
box(0.07, 0.07, 68, 0xe8e4da, -553.3, 6.47, 95)
# thông silhouette bờ nam xa + bờ đông (y = groundH bản XH-1.5 theo code)
for (px, pz, ps, gy) in [(-545, 209, 1.25, 7.125), (-528, 217, 1.1, 8.125), (-512, 206, 1.3, 6.75),
                         (-497, 215, 1.05, 7.875), (-481, 208, 1.2, 7.0), (-466, 218, 1.28, 8.25),
                         (-450, 207, 1.12, 6.875), (-435, 214, 1.22, 7.75), (-419, 206, 1.08, 6.75),
                         (-404, 216, 1.26, 8.0), (-388, 209, 1.15, 7.125), (-373, 217, 1.02, 8.125),
                         (-357, 207, 1.3, 6.875), (-342, 213, 1.1, 7.625), (-326, 206, 1.24, 6.75),
                         (-311, 216, 1.06, 8.0), (-295, 208, 1.18, 7.0), (-280, 215, 1.27, 7.875),
                         (-264, 207, 1.09, 6.875), (-249, 214, 1.21, 7.75), (-236, 209, 1.13, 7.125),
                         (-470, 227, 1.2, 9.0), (-385, 228, 1.32, 9.0), (-300, 227, 1.14, 9.0),
                         (-212, 100, 1.15, 5.5), (-213, 48, 1.05, 5.5)]:
    pine_fake(px, gy, pz, ps)
# 4 villa mờ trên thềm nam xa
for (vx, vz) in [(-505, 228), (-430, 229), (-352, 228), (-272, 229)]:
    box(9, 4.2, 6.5, 0xcfc4b2, vx, 11.0, vz)
    box(10, 0.5, 7.5, 0x74584a, vx, 13.3, vz)
    box(1.2, 1.6, 0.3, 0x5a4632, vx - 2, 10.2, vz - 3.3)

# ---------- NGỮ CẢNH TRỤC TÂY (số từ code hiện hữu, khối sườn nam = bản XH-1) ----------
box(88, 0.07, 49, 0x34302c, -172, 5.48, 7)                          # nhựa seg3
box(88, 0.06, 100, 0x978a78, -172, 5.44, 0)                         # nền đoạn kéo dài
box(76, 14, 55, 0x6b6257, -169, 3.0, 62)                            # khối sườn nam ĐÃ THU (XH-1)
cyl(8, 0.12, 0x494a4d, -196, 5.5, 2)                                # bùng binh đầu chợ
cyl(4.5, 0.16, 0x5f8547, -196, 5.52, 2)
cyl(11.8, 0.1, 0x494a4d, -30, 0.02, -6)                             # vành bùng binh chính
box(68, 17, 16, 0xe3d7bd, 0, 8.5, 20)                               # khối nhà lồng đơn giản
box(170, 0.05, 130, 0x978a78, 0, -0.02, 18)                         # plaza

# ---------- ánh sáng NGÀY ----------
world = bpy.data.worlds.get('World') or bpy.data.worlds.new('World')
bpy.context.scene.world = world
world.use_nodes = True
bg = world.node_tree.nodes['Background']
bg.inputs[0].default_value = (0.55, 0.70, 0.95, 1.0)
bg.inputs[1].default_value = 0.85
sun_data = bpy.data.lights.new('Sun', 'SUN'); sun_data.energy = 3.2; sun_data.angle = math.radians(2.0)
sun = bpy.data.objects.new('Sun', sun_data); bpy.context.scene.collection.objects.link(sun)
sun.location = (-60, 55, 80)
d = (Vector((0, 0, 0)) - sun.location).normalized()
sun.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.samples = 32
scene.cycles.use_denoising = False
scene.render.resolution_percentage = 100

def shoot(name, cam_loc_three, target_three, ortho=None, res=(1100, 750), lens=30.0):
    cd = bpy.data.cameras.new('Cam')
    if ortho: cd.type = 'ORTHO'; cd.ortho_scale = ortho
    else: cd.lens = lens
    cd.clip_start = 0.1; cd.clip_end = 900
    cam = bpy.data.objects.new('Cam', cd)
    bpy.context.scene.collection.objects.link(cam)
    cam.location = tb(cam_loc_three)
    t = tb(target_three)
    dd = (t - cam.location).normalized()
    cam.rotation_euler = dd.to_track_quat('-Z', 'Y').to_euler()
    scene.camera = cam
    scene.render.resolution_x, scene.render.resolution_y = res
    scene.render.filepath = os.path.join(OUT, name)
    bpy.ops.render.render(write_still=True)
    print('[xh15] rendered', name)

shoot('xh15-topdown.png', (-390, 260, 115.01), (-390, 5, 115), ortho=430, res=(1150, 820))
shoot('xh15-dia.png', (-150, 55, 235), (-400, 5, 110))
shoot('xh15-prom-day.png', (-288, 7.3, 30.5), (-440, 5.2, 145), lens=24.0)

# ---------- chuyển ĐÊM (mặc định game 19:00): trăng mờ + nước emissive + đèn trục tây có thật ----------
bg.inputs[0].default_value = (0.012, 0.018, 0.035, 1.0)
bg.inputs[1].default_value = 0.5
sun_data.energy = 0.3
sun_data.color = (0.55, 0.65, 0.95)
_bsdf_w.inputs['Emission Strength'].default_value = 0.55
for (lx, ly, lz) in [(-200, 8.5, 0), (-214, 8.5, 8)]:
    pd = bpy.data.lights.new('Lamp', 'POINT'); pd.energy = 500; pd.color = (1.0, 0.62, 0.3)
    po = bpy.data.objects.new('Lamp', pd); bpy.context.scene.collection.objects.link(po)
    po.location = tb((lx, ly, lz))
shoot('xh15-prom-night.png', (-288, 7.3, 30.5), (-440, 5.2, 145), lens=24.0)
print('[xh15] DONE')
