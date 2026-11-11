# -*- coding: utf-8 -*-
"""XH-0 — RENDER NGHIỆM THU KHUNG HỒ XUÂN HƯƠNG (mô phỏng đúng thông số code).

Dựng lại bằng nguyên khối các mặt đất XH-0 vừa thêm vào index.html (cùng kích
thước/vị trí/màu) + tối thiểu ngữ cảnh trục tây (nhựa seg3, nền, khối sườn nam,
2 bùng binh, khối nhà lồng đơn giản) để soi: khung bờ hồ đúng vị trí/tỉ lệ kế
hoạch §2 chưa, tuyến đi spawn -> đường dạo -> cầu -> đảo có thông không, khu cũ
có bị phá hình không. Đây là MÔ PHỎNG thông số code (như render_frontage.py),
không phải mesh game — nước/kè/Thủy Tạ thật ở XH-1/XH-2.

Quy ước trục: three (x, y-up, z) -> Blender (x, -z, y); three rotation.x giữ
nguyên dấu sang Blender (đã kiểm chứng hình học).

Chạy: ~/workspace/vinh-trang-3d/tools/blender5/blender --background \
        --threads 2 --python scripts/render_xh0.py
Xuất: renders/xh0-topdown.png (ortho, bắc = lên) + renders/xh0-diorama.png
(góc từ tây-nam trên cao nhìn về đông-bắc: hồ trước, chợ sau).
"""
import bpy, math, os
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
OUT = os.path.join(ROOT, "renders")
os.makedirs(OUT, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)

def tb(p):  # three -> blender
    return Vector((p[0], -p[2], p[1]))

def mat_rgb(hexcol):
    m = bpy.data.materials.new('m%06x' % hexcol)
    m.use_nodes = True
    r = ((hexcol >> 16) & 255) / 255.0; g = ((hexcol >> 8) & 255) / 255.0; b = (hexcol & 255) / 255.0
    m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (r, g, b, 1.0)
    m.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value = 0.95
    m.diffuse_color = (r, g, b, 1.0)
    return m

def box(w, h, d, hexcol, x, y, z, rot_x=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1)
    o = bpy.context.active_object
    o.dimensions = (w, d, h)              # blender: X=w, Y=d(three z), Z=h
    o.location = tb((x, y, z))
    if rot_x: o.rotation_euler.x = rot_x
    o.data.materials.append(mat_rgb(hexcol))
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return o

def cyl(r, h, hexcol, x, y, z, verts=40):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=h, vertices=verts)
    o = bpy.context.active_object
    o.location = tb((x, y, z))
    o.data.materials.append(mat_rgb(hexcol))
    return o

def plane(w, d, hexcol, x, y, z):
    bpy.ops.mesh.primitive_plane_add(size=1)
    o = bpy.context.active_object
    o.dimensions = (w, d, 0)
    o.location = tb((x, y, z))
    o.rotation_euler.x = 0  # plane Blender nằm sẵn mặt XY (ngang theo chuyển đổi)
    o.data.materials.append(mat_rgb(hexcol))
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return o

# ---------- KHU HỒ XH-0 — chép đúng số trong index.html ----------
box(144, 0.06, 61, 0x5f8547, -288, 5.45, 5.5)          # nền cỏ thềm bờ bắc
box(144, 0.04, 8, 0xdde2e2, -288, 5.47, 32)            # nền đường dạo phẳng
plane(128, 80, 0x46545a, -288, 4.86, 76)               # đáy hồ tạm trung tính
cyl(15, 0.06, 0x5f8547, -250, 5.45, 58)                # đĩa đảo Thủy Tạ R15
box(3, 0.08, 7, 0xdde2e2, -250, 5.46, 39.5)            # dải cầu -> đảo
box(8, 0.06, 80, 0x5f8547, -356, 5.45, 76)             # bờ tây
box(8, 0.06, 80, 0x5f8547, -220, 5.45, 76)             # bờ đông
box(128, 0.08, 16.6, 0x5f8547, -288, 7.22, 124, rot_x=-0.219)  # taluy nam
box(128, 0.06, 10, 0x5f8547, -288, 8.94, 137)          # thềm sau taluy
box(128, 0.55, 0.5, 0x5e5852, -288, 5.17, 36)           # kè tạm z 36

# ---------- NGỮ CẢNH TRỤC TÂY (số từ code hiện hữu) ----------
box(88, 0.07, 49, 0x34302c, -172, 5.48, 7)             # nhựa seg3 tới bùng binh đầu chợ
box(88, 0.06, 100, 0x978a78, -172, 5.44, 0)            # nền đoạn kéo dài
box(90, 14, 55, 0x6b6257, -175, 3.0, 62)               # khối sườn nam cũ
cyl(8, 0.12, 0x494a4d, -196, 5.5, 2)                   # bùng binh đầu chợ (đĩa đường)
cyl(4.5, 0.16, 0x5f8547, -196, 5.52, 2)                # đảo cỏ đầu chợ
cyl(11.8, 0.1, 0x494a4d, -30, 0.02, -6)                # vành bùng binh chính trước chợ
box(68, 17, 16, 0xe3d7bd, 0, 8.5, 20)                  # khối nhà lồng (đơn giản, định hướng)
box(170, 0.05, 130, 0x978a78, 0, -0.02, 18)            # plaza

# ---------- ánh sáng ----------
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

def shoot(name, cam_loc_three, target_three, ortho=None, res=(1000, 750)):
    cd = bpy.data.cameras.new('Cam')
    if ortho:
        cd.type = 'ORTHO'; cd.ortho_scale = ortho
    else:
        cd.lens = 30.0
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
    print('[xh0] rendered', name)

# top-down: trục z của three hướng XUỐNG ảnh (nam ở dưới) nên nhìn từ trên với
# camera lệch nhẹ về nam để track-quat ổn định; bắc (z nhỏ) ở trên ảnh.
shoot('xh0-topdown.png', (-262, 230, 58.01), (-262, 5, 58), ortho=300, res=(1100, 850))
# diorama: từ tây-nam trên cao nhìn đông-bắc — hồ tiền cảnh, trục + chợ hậu cảnh.
shoot('xh0-diorama.png', (-392, 46, 178), (-218, 4, 14), res=(1100, 750))
print('[xh0] DONE')
