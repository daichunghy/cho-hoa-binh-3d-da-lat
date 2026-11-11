# -*- coding: utf-8 -*-
"""XH-1 — RENDER NGHIỆM THU NƯỚC & BỜ HỒ XUÂN HƯƠNG (mô phỏng đúng thông số code).

Mở rộng render_xh0.py: chép đúng các khối XH-1 trong index.html (mặt nước teal
+ texture gợn sinh bằng đúng hàm seed JS — renders/xh1-ripple-tex.png; kè đá
texture khối đá xh1-stone-tex.png; lát dạo xh1-prom-tex.png; bó vỉa sáng; tường
chân nam/tây/đông; vèn đảo + vòng đường đảo; cầu Ông Đạo S4; thông silhouette
gần đúng bằng nón/trụ — harness không nạp GLB pine; 2 villa bờ xa; khối sườn
nam ĐÃ THU mặt tây về -207) + ngữ cảnh trục tây như XH-0.

Thông số nước theo code: base teal 0x276a8a (bake trong texture), roughness
0.15, alpha 0.93; ĐÊM: emissive 0x1d4e5f x 0.55 (applyDayNight/waterMats) —
bản đêm là bản chính vì game mặc định 19:00. Đèn bờ hồ CHƯA có ở XH-1 (XH-3)
nên đêm chỉ có trăng + emissive nước + 2 đèn đường trục tây có thật ở đầu lối nối.

Quy ước trục: three (x, y-up, z) -> Blender (x, -z, y); rotY -> rotation_z.

Chạy: ~/workspace/vinh-trang-3d/tools/blender5/blender --background \
        --threads 2 --python scripts/render_xh1.py
Xuất: renders/xh1-day.png, xh1-night.png, xh1-prom.png, xh1-topdown.png
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
WATER = mat_tex('water', 'xh1-ripple-tex.png', 24, 15, 0.15)
_bsdf_w = WATER.node_tree.nodes['Principled BSDF']
_bsdf_w.inputs['Alpha'].default_value = 0.93
_er, _eg, _eb = 0x1d / 255.0, 0x4e / 255.0, 0x5f / 255.0
_bsdf_w.inputs['Emission Color'].default_value = (_er, _eg, _eb, 1.0)
_bsdf_w.inputs['Emission Strength'].default_value = 0.0   # ngày: 0 — đêm bật 0.55

# ---------- KHU HỒ XH-1 — chép đúng số trong index.html ----------
box(144, 0.06, 61, 0x5f8547, -288, 5.45, 5.5)                       # nền cỏ thềm bờ bắc
boxm(144, 0.04, 8, PROM, -288, 5.47, 32)                            # lát đường dạo z 28..36
boxm(6, 0.05, 31.6, PROM_PATH, -219, 5.515, 17, rot_z=math.atan2(-26, 18))  # lối nối lát đá
plane(128, 80, 0x14425c, -288, 4.82, 76, rough=1.0)                 # đáy hồ sâu
planem(128, 80, WATER, -288, 4.9, 76)                               # MẶT NƯỚC THẬT
boxm(100.8, 1.3, 0.7, STONE25, -301.6, 4.98, 36)                    # kè bắc tây
boxm(24.8, 1.3, 0.7, STONE6, -236.4, 4.98, 36)                      # kè bắc đông
box(100.8, 0.09, 0.9, 0xd8d2c2, -301.6, 5.6, 36)                    # bó vỉa sáng
box(24.8, 0.09, 0.9, 0xd8d2c2, -236.4, 5.6, 36)
boxm(128, 1.15, 0.7, STONE32, -288, 4.95, 116)                      # tường chân nam
boxm(0.7, 1.15, 80, STONE20, -352, 4.95, 76)                        # mép nước tây
boxm(0.7, 1.15, 80, STONE20, -224, 4.95, 76)                        # mép nước đông
cyl(15, 0.06, 0x5f8547, -250, 5.45, 58)                             # đĩa đảo R15
cylm(15.7, 16.6, 1.2, STONE24, -250, 4.84, 58, 40)                  # vèn kè đảo (nắp 5.44 — dưới đĩa cỏ/vòng lát)
cyl(13.8, 0.02, 0xdde2e2, -250, 5.49, 58)                           # vòng đường lát đảo (đĩa)
cyl(9.0, 0.02, 0x5f8547, -250, 5.5, 58)                             # cỏ tâm đảo trên vòng lát
box(3, 0.08, 7, 0xdde2e2, -250, 5.46, 39.5)                         # dải cầu -> đảo
box(8, 0.06, 80, 0x5f8547, -356, 5.45, 76)                          # bờ tây
box(17, 0.06, 80, 0x5f8547, -215.5, 5.45, 76)                       # bờ đông nới rộng
box(128, 0.08, 16.6, 0x5f8547, -288, 7.22, 124, rot_x=-0.219)       # taluy nam
box(128, 0.06, 10, 0x5f8547, -288, 8.94, 137)                       # thềm sau taluy
# cầu Ông Đạo (S4)
boxm(8, 1.9, 36, STONE9, -353, 5.15, 78)
box(8.4, 0.12, 36, 0x4a4a4a, -353, 6.16, 78)
for dz in range(62, 95, 4):
    box(0.09, 0.55, 0.09, 0xe8e4da, -349.3, 6.5, dz)
box(0.07, 0.07, 34, 0xe8e4da, -349.3, 6.74, 78)
box(0.07, 0.07, 34, 0xe8e4da, -349.3, 6.47, 78)
# thông silhouette + bờ đông (y = groundH theo code)
for (px, pz, ps, gy) in [(-338, 124, 1.25, 7.25), (-322, 130, 1.1, 8.56), (-306, 122, 1.3, 6.81),
                         (-292, 128, 1.0, 8.13), (-276, 124, 1.2, 7.25), (-260, 131, 1.05, 8.78),
                         (-244, 123, 1.28, 7.03), (-230, 129, 1.12, 8.34),
                         (-212, 100, 1.15, 5.5), (-213, 48, 1.05, 5.5)]:
    pine_fake(px, gy, pz, ps)
# 2 villa mờ bờ xa
for (vx, vz) in [(-318, 135), (-262, 136)]:
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
    print('[xh1] rendered', name)

shoot('xh1-topdown.png', (-262, 230, 58.01), (-262, 5, 58), ortho=300, res=(1100, 850))
shoot('xh1-day.png', (-392, 46, 178), (-218, 4, 14))
shoot('xh1-prom.png', (-224, 7.4, 29.0), (-285, 4.8, 62), lens=24.0)

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
shoot('xh1-night.png', (-392, 46, 178), (-218, 4, 14))
print('[xh1] DONE')
