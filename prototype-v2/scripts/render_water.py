# -*- coding: utf-8 -*-
"""WATER-1 — RENDER NGHIỆM THU ĐÀI PHUN (mặt nước code-built, không có trong GLB).

Mô phỏng ĐÚNG thông số index.html (đài phun tâm three (27, 5.2)):
- bồn: CylinderGeometry(2.7 top, 2.9 bottom, 0.55) tâm y 0.28 đá 0x8a8074 — ĐẶC CÓ NẮP
  (nắp y 0.555). Harness tái tạo nắp tường minh (cone end_fill NONE + đĩa nắp riêng).
- TRƯỚC: đĩa nước r2.45 y 0.50 màu 0xa8cfe0 alpha 0.84 + 2 vòng gợn y 0.53/0.542
  (nằm DƯỚI nắp bồn -> bị che kín, raycast three đã kiểm chứng: cap hit trước water).
- SAU (WATER-1): đĩa đáy 0x14425c y 0.558; nước y 0.58, texture gợn canvas (file
  renders/water-ripple-tex.png sinh bằng đúng hàm seed của JS), repeat 2, alpha 0.93,
  roughness 0.15; vành miệng 0xd8d2c2 r 2.45-2.72 y 0.565; gợn y 0.605/0.617;
  tia 0xeaf6fc; đêm: nước emissive 0x1d4e5f x 0.55.
- Cột/bát/tia theo code: cột cyl(0.26,0.44,2.3)@1.42, bát cyl(0.95,0.52,0.25)@2.62,
  bát 2 cyl(0.5,0.3,0.18)@3.12, cầu r0.16@3.34, 6 tia r0.5@2.95 nghiêng ra 0.6 rad.
- Sân plaza: tấm 64x14.2 0xa79a84 tại three (14, 0.01, 4.8).
Ánh sáng: ngày ~ web ngày (ACES 1.3, exposure -0.18 theo research/26);
đêm ~ web đêm 19:00 (exposure +0.29, trăng lạnh yếu + đèn chân ấm 0xffc98a).
Camera: three (34.5, 6.5, 12.7) -> ngắm (27, 0.9, 5.2), lens 35, 800x600.
Chạy: blender --background --threads 2 --python scripts/render_water.py
Xuất: renders/water-before-day.png, water-before-night.png, water-day.png, water-night.png
"""
import bpy, math, os
from mathutils import Vector, Quaternion

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
OUT = os.path.join(ROOT, "renders")
os.makedirs(OUT, exist_ok=True)
FX, FZ = 27.0, 5.2  # tam dai phun (three)

def T(p):  # three (x,y,z) -> Blender (x,-z,y)
    return Vector((p[0], -p[2], p[1]))

bpy.ops.wm.read_factory_settings(use_empty=True)

def mat(name, hexcol, rough=0.9, alpha=1.0, emission=None, estr=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes['Principled BSDF']
    r = int(hexcol[1:3], 16) / 255.0; g = int(hexcol[3:5], 16) / 255.0; b = int(hexcol[5:7], 16) / 255.0
    bsdf.inputs['Base Color'].default_value = (r, g, b, 1.0)
    bsdf.inputs['Roughness'].default_value = rough
    if alpha < 1.0:
        bsdf.inputs['Alpha'].default_value = alpha
    if emission:
        er = int(emission[1:3], 16) / 255.0; eg = int(emission[3:5], 16) / 255.0; eb = int(emission[5:7], 16) / 255.0
        bsdf.inputs['Emission Color'].default_value = (er, eg, eb, 1.0)
        bsdf.inputs['Emission Strength'].default_value = estr
    m.diffuse_color = (r, g, b, alpha)
    return m

STONE = mat('Stone', '#8a8074', 0.9)
PLAZA = mat('Plaza', '#a79a84', 0.95)
GROUND = mat('Ground', '#4a453e', 1.0)

def cube(name, size, three_center, material):
    bpy.ops.mesh.primitive_cube_add(location=T(three_center))
    o = bpy.context.active_object; o.name = name
    o.scale = (size[0] / 2, size[2] / 2, size[1] / 2)  # Blender: x, -z(depth), y(height)
    bpy.ops.object.transform_apply(scale=True)
    o.data.materials.append(material)
    return o

def cone(name, r_bottom, r_top, depth, three_center, material, fill='NOTHING'):
    bpy.ops.mesh.primitive_cone_add(radius1=r_bottom, radius2=r_top, depth=depth,
                                    end_fill_type=fill, location=T(three_center))
    o = bpy.context.active_object; o.name = name
    o.data.materials.append(material)
    return o

def disc(name, radius, three_pos, material, verts=28):
    bpy.ops.mesh.primitive_circle_add(vertices=verts, radius=radius, fill_type='NGON', location=T(three_pos))
    o = bpy.context.active_object; o.name = name
    o.data.materials.append(material)
    return o

def annulus(name, rin, rout, three_pos, material, seg=32):
    import bmesh
    me = bpy.data.meshes.new(name)
    vs, fs = [], []
    y = three_pos[1]
    for i in range(seg):
        a = 2 * math.pi * i / seg
        vs.append((three_pos[0] + rin * math.cos(a), -(three_pos[2] + rin * math.sin(a)), y))
        vs.append((three_pos[0] + rout * math.cos(a), -(three_pos[2] + rout * math.sin(a)), y))
    for i in range(seg):
        j = (i + 1) % seg
        fs.append((2 * i, 2 * j, 2 * j + 1, 2 * i + 1))
    me.from_pydata(vs, [], fs); me.update()
    o = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(o)
    me.materials.append(material)
    return o

def sphere(name, r, three_pos, material):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=T(three_pos))
    o = bpy.context.active_object; o.name = name
    o.data.materials.append(material)
    return o

def cyl_jet(name, r, length, three_base, tilt_axis_blender, tilt, material):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=length, location=(0, 0, 0))
    o = bpy.context.active_object; o.name = name
    q = Quaternion(tilt_axis_blender, tilt)
    mid_local = q @ Vector((0, 0, length / 2))
    base_b = T(three_base)
    o.location = base_b + mid_local
    o.rotation_mode = 'QUATERNION'; o.rotation_quaternion = q
    o.data.materials.append(material)
    return o

# ---------- nen + san ----------
bpy.ops.mesh.primitive_plane_add(size=400, location=(0, 0, -0.04))
gp = bpy.context.active_object; gp.name = 'GroundPlane'; gp.data.materials.append(GROUND)
cube('PlazaSlab', (64, 0.08, 14.2), (14, 0.01, 4.8), PLAZA)

# ---------- cum dai phun dung chung ----------
shared = []
shared.append(cone('Basin', 2.9, 2.7, 0.55, (FX, 0.28, FZ), STONE))
shared.append(disc('BasinCap', 2.7, (FX, 0.555, FZ), STONE))  # nap bon — thu che mat nuoc cu
shared.append(cone('Column', 0.44, 0.26, 2.3, (FX, 1.42, FZ), STONE))
shared.append(cone('Bowl1', 0.52, 0.95, 0.25, (FX, 2.62, FZ), STONE))
shared.append(cone('Bowl2', 0.30, 0.50, 0.18, (FX, 3.12, FZ), STONE))
shared.append(sphere('TopBall', 0.16, (FX, 3.34, FZ), STONE))
for ux, uz in [(25.1, 3.3), (28.9, 3.3), (25.1, 7.1), (28.9, 7.1)]:
    shared.append(cube('Uplight', (0.22, 0.18, 0.22), (ux, 0.09, uz), mat('UpDark', '#3a3f45', 0.5)))

JET_OLD = mat('JetOld', '#cfe8f4', 0.4, alpha=0.55)
JET_NEW = mat('JetNew', '#eaf6fc', 0.4, alpha=0.7)
def build_jets(material, tag):
    js = []
    for i in range(6):
        a = i / 6 * math.pi * 2
        base = (FX + math.cos(a) * 0.5, 2.95, FZ + math.sin(a) * 0.5)
        axis = Vector((math.sin(a), -math.cos(a), 0))  # truc ngang vuong goc huong tia (Blender)
        js.append(cyl_jet('Jet' + tag + str(i), 0.03, 1.5, base, axis, -0.6, material))
    js.append(cyl_jet('JetC' + tag, 0.04, 1.1, (FX, 3.85 - 0.55, FZ), Vector((1, 0, 0)), 0.0, material))
    return js
jets_old = build_jets(JET_OLD, 'Old')
jets_new = build_jets(JET_NEW, 'New')

# ---------- TRUOC: nuoc cu duoi nap ----------
before = []
before.append(disc('WaterOld', 2.45, (FX, 0.50, FZ), mat('WaterOld', '#a8cfe0', 0.25, alpha=0.84)))
RINGM = mat('RingOld', '#eaf6fc', 0.4, alpha=0.30)
before.append(annulus('RingOld1', 0.5, 0.62, (FX, 0.53, FZ), RINGM))
before.append(annulus('RingOld2', 1.3, 1.42, (FX, 0.542, FZ), RINGM))

# ---------- SAU: WATER-1 ----------
after = []
after.append(disc('BottomDisc', 2.45, (FX, 0.558, FZ), mat('Bottom', '#14425c', 1.0)))
# nuoc co texture gon
wm = bpy.data.materials.new('WaterNew'); wm.use_nodes = True
bsdf = wm.node_tree.nodes['Principled BSDF']
img = bpy.data.images.load(os.path.join(OUT, 'water-ripple-tex.png'))
tex = wm.node_tree.nodes.new('ShaderNodeTexImage'); tex.image = img; tex.extension = 'REPEAT'
wm.node_tree.links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])
bsdf.inputs['Roughness'].default_value = 0.15
bsdf.inputs['Alpha'].default_value = 0.93
bsdf.inputs['Emission Color'].default_value = (0x1d / 255, 0x4e / 255, 0x5f / 255, 1.0)
bsdf.inputs['Emission Strength'].default_value = 0.0  # dem moi bat 0.55
wnew = disc('WaterNew', 2.45, (FX, 0.58, FZ), wm)
for loop in wnew.data.uv_layers.active.data:
    loop.uv = (loop.uv[0] * 2, loop.uv[1] * 2)  # repeat 2,2 nhu code
after.append(wnew)
after.append(annulus('Rim', 2.45, 2.72, (FX, 0.565, FZ), mat('Rim', '#d8d2c2', 0.9)))
RINGN = mat('RingNew', '#eaf6fc', 0.4, alpha=0.33)
after.append(annulus('RingNew1', 0.65, 0.81, (FX, 0.605, FZ), RINGN))
after.append(annulus('RingNew2', 2.68, 2.93, (FX, 0.617, FZ), mat('RingNew2', '#eaf6fc', 0.4, alpha=0.10)))

# ---------- anh sang ----------
world = bpy.data.worlds.get('World') or bpy.data.worlds.new('World')
bpy.context.scene.world = world; world.use_nodes = True
bg = world.node_tree.nodes['Background']

def light_obj(name, ltype, energy, color, loc_three, angle=0.0):
    d = bpy.data.lights.new(name, ltype); d.energy = energy; d.color = color
    if ltype == 'SUN': d.angle = angle
    o = bpy.data.objects.new(name, d); bpy.context.scene.collection.objects.link(o)
    o.location = T(loc_three)
    return o

sun = light_obj('Sun', 'SUN', 3.0, (1.0, 0.95, 0.88), (-30, 60, -40), angle=math.radians(2.0))
d = (T((FX, 0, FZ)) - sun.location).normalized(); sun.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
moon = light_obj('Moon', 'SUN', 0.0, (0.55, 0.68, 0.95), (40, 50, -30), angle=math.radians(2.0))
d = (T((FX, 0, FZ)) - moon.location).normalized(); moon.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
night_pts = []
for ux, uz in [(25.1, 3.3), (28.9, 3.3), (25.1, 7.1), (28.9, 7.1)]:
    night_pts.append(light_obj('UpPt', 'POINT', 0.0, (1.0, 0.79, 0.54), (ux, 0.6, uz)))
glow = light_obj('GlowPt', 'POINT', 0.0, (1.0, 0.79, 0.54), (FX, 1.0, FZ))

# ---------- camera ----------
cam_data = bpy.data.cameras.new('Cam'); cam_data.lens = 35.0
cam_data.clip_start = 0.1; cam_data.clip_end = 600
cam = bpy.data.objects.new('Cam', cam_data); bpy.context.scene.collection.objects.link(cam)
cam.location = T((34.5, 6.5, 12.7))
tgt = T((27, 0.9, 5.2))
d = (tgt - cam.location).normalized(); cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
bpy.context.scene.camera = cam

scene = bpy.context.scene
scene.render.engine = 'CYCLES'; scene.cycles.samples = 48; scene.cycles.use_denoising = False
scene.render.resolution_x = 800; scene.render.resolution_y = 600; scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
try:
    scene.view_settings.view_transform = 'ACES 1.3'  # research/26: khop web ACES
except Exception as e:
    print('[water] ACES 1.3 khong dat duoc:', e)

def set_vis(objs, vis):
    for o in objs: o.hide_render = not vis

def render(tag, is_after, is_night):
    set_vis(before + jets_old, not is_after)
    set_vis(after + jets_new, is_after)
    if is_night:
        bg.inputs[0].default_value = (0.05, 0.10, 0.22, 1.0); bg.inputs[1].default_value = 0.35
        sun.data.energy = 0.0; moon.data.energy = 0.55
        for p in night_pts: p.data.energy = 14.0
        glow.data.energy = 10.0
        bsdf.inputs['Emission Strength'].default_value = 0.55 if is_after else 0.0
        scene.view_settings.exposure = 0.29
    else:
        bg.inputs[0].default_value = (0.55, 0.70, 0.92, 1.0); bg.inputs[1].default_value = 0.75
        sun.data.energy = 3.0; moon.data.energy = 0.0
        for p in night_pts: p.data.energy = 0.0
        glow.data.energy = 0.0
        bsdf.inputs['Emission Strength'].default_value = 0.0
        scene.view_settings.exposure = -0.18
    scene.render.filepath = os.path.join(OUT, tag + '.png')
    bpy.ops.render.render(write_still=True)
    print('[water] rendered', tag)

render('water-before-day', False, False)
render('water-day', True, False)
render('water-before-night', False, True)
render('water-night', True, True)
print('[water] DONE')
