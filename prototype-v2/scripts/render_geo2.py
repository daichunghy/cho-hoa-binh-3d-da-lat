# -*- coding: utf-8 -*-
"""GEO2 — render kiem chung TAM MAT cho Cho Hoa Binh 3D (ban don gian, dung so do).

Script PARSE index.html luc chay (STALL_DEFS / spawn / dao / FNT / STAIR_SITTERS /
QUEUES / shophouse / LOOP / RB_ARC + cac khoi tuy chon NEW_RB, DECOR_N_XS/S_XS neu co)
nen chay lai sau khi sua game se ra bo anh SAU tuong ung.

Quy uoc truc: game three.js (x, y-up, z) -> Blender (x, -z, y).
Xoay quanh truc dung: game rotY -> Blender rotation_z = +rotY (da doi chieu voi
ham tbox cua cac script mini truoc: local +Z game -> Blender -Y).

Chay: ~/workspace/vinh-trang-3d/tools/blender5/blender --background --threads 2 \
         --python scripts/render_geo2.py
Cycles 24 mau, 640x480, threads 2.
Xuat: renders/geo2-before-a.png .. geo2-before-e.png
"""
import bpy, math, os, random, re
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
OUT = os.path.join(ROOT, "renders")
os.makedirs(OUT, exist_ok=True)
HTML = os.path.join(ROOT, "index.html")
SRC = open(HTML, encoding="utf-8").read()

# ============================================================
# 1) PORT groundH / stairH / entryRampY — Y HET code game
# ============================================================
def entryRampY(x):
    return min(5.5, (-52 - x) * 0.07) if x < -52 else 0.0

def stairH(z):
    if z >= -2: return 0.0
    if z <= -30: return 17.0
    if z > -8.25:
        s = min(1.0, math.floor((z + 8.25) / 6.25 * 10) / 10.0)
        return 5.67 * (1 - s)
    if z > -12.25: return 5.67
    if z > -18.75:
        s = min(1.0, math.floor((z + 18.75) / 6.5 * 10) / 10.0)
        return 11.33 - 5.66 * s
    if z > -22.75: return 11.33
    s = min(1.0, math.floor((z + 30) / 7.25 * 10) / 10.0)
    return 17 - 5.67 * s

def innerStairH(z):
    if z <= 18.4:
        t = (z - 12) / 6.4
        s = min(1.0, math.floor(t * 10) / 10.0 + (0.1 if t >= 0.999 else 0.0))
        return 12.6 - 6.05 * min(1.0, s)
    if z <= 20.4: return 6.55
    t = (z - 20.4) / 6.4
    s = min(1.0, math.floor(t * 10) / 10.0 + (0.1 if t >= 0.999 else 0.0))
    return 6.55 - 6.05 * min(1.0, s)

def groundH(x, z):
    if 14.5 <= x <= 20.5 and -30 <= z <= 9: return 17.14 - (z + 30) * 0.11282          # (1)
    if 29 <= x <= 33 and 12 <= z <= 26.8: return innerStairH(z)                          # (2)
    if 14 <= x <= 21 and 7 <= z <= 12: return 12.6                                       # (3)
    if 21 <= x <= 33 and 7 <= z <= 12.2: return 12.6                                     # (4)
    if -34 <= x <= 34 and 12 <= z <= 28: return 0.5                                      # (5)
    if -58 <= x <= -35 and -16.5 <= z <= -2:                                             # (6)
        return entryRampY(x) + 0.11 if x < -52 else 0.0
    if -131 <= x <= -59 and -13.9 <= z <= -11.1: return entryRampY(x) + 0.11             # (7)
    if -82.5 <= x <= -51.5 and 10.5 <= z <= 13.9: return entryRampY(x) + 0.11            # (8)
    if -133 <= x < -58 and -17.5 <= z <= 24:                                             # (9)
        r = entryRampY(x)
        return r + 0.11 if (z < -14.5 or (13.5 < z <= 20.2)) else r
    if -133 <= x < -52 and z > 24: return entryRampY(x)                                  # (10)
    if -84 <= x <= -34 and 13.5 < z <= 24: return entryRampY(x) + 0.05                   # (11)
    if x < -52 and -17.5 <= z <= 24: return entryRampY(x)                                # (12)
    if z <= -30: return 17.0                                                             # (13)
    if z >= -2: return 0.0                                                               # (14)
    if -11 <= x <= 11: return stairH(z)                                                  # (15)
    if (-19 <= x < -11) or (11 < x < 14.5):                                              # (16)
        if z > -8.25: return 2.8
        if z > -18.75: return 8.5
        return 14.2
    if -45 <= x < -19 and -30 < z < -2:                                                  # (17)
        if z >= -16: return 0.0
        return 17 * ((-16 - z) / 14.0)
    return 17 * ((-2 - z) / 28.0)                                                        # (18)

def stall_base_y(x, z):
    # buildStall() trong game: sap o dai hanh lang dong (x 21..33, z 7..12.2)
    # dung tren mat dat 0, KHONG theo groundH (groundH o do la mat hanh lang 12.6).
    if 21 <= x <= 33 and 7 <= z <= 12.2: return 0.0
    return groundH(x, z)

# ============================================================
# 2) PARSE index.html
# ============================================================
def eval_rot(expr):
    e = expr.strip().replace("Math.PI", "pi")
    return float(eval(e, {"__builtins__": {}}, {"pi": math.pi}))

def fnum(s):
    return float(s)

# --- STALL_DEFS ---
STALLS = []  # {id,x,z,rotY}
_blk = re.search(r'const STALL_DEFS\s*=\s*\[(.*?)\n\];', SRC, re.S)
assert _blk, "khong tim thay STALL_DEFS"
_parts = re.split(r"\{\s*id:'", _blk.group(1))
for part in _parts[1:]:
    sid = part.split("'", 1)[0]
    head = part.split("menu:", 1)[0]
    mx = re.search(r'\bx:\s*(-?[\d.]+)', head)
    mz = re.search(r'\bz:\s*(-?[\d.]+)', head)
    mr = re.search(r'rotY:\s*([^,\s}]+)', head)
    if not (mx and mz): continue
    STALLS.append({"id": sid, "x": fnum(mx.group(1)), "z": fnum(mz.group(1)),
                   "rotY": eval_rot(mr.group(1)) if mr else 0.0})
STALL_BY_ID = {s["id"]: s for s in STALLS}

# --- spawn ---
_m = re.search(r'player\.position\.set\(\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*\)', SRC)
SPAWN = (fnum(_m.group(1)), fnum(_m.group(3)))  # (x, z)

# --- dao chinh ---
_m = re.search(r'rb\.position\.set\(\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*\)', SRC)
RB_CENTER = (fnum(_m.group(1)), fnum(_m.group(3)))  # (x, z)
STATUE_OFF = (-4.2, 3.2)

# --- dai phun ---
_m = re.search(r'const FNT\s*=\s*\{\s*x:\s*(-?[\d.]+)\s*,\s*z:\s*(-?[\d.]+)\s*\}', SRC)
FNT = (fnum(_m.group(1)), fnum(_m.group(2)))

# --- STAIR_SITTERS ---
SITTERS = []
_blk = re.search(r'const STAIR_SITTERS\s*=\s*\[(.*?)\];', SRC, re.S)
for mm in re.finditer(r"\[\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*,\s*'([^']+)'\s*\]", _blk.group(1)):
    SITTERS.append((fnum(mm.group(1)), fnum(mm.group(2)), mm.group(3)))

# --- QUEUES ---
QUEUES = []
_blk = re.search(r'const QUEUES\s*=\s*\[(.*?)\];', SRC, re.S)
for mm in re.finditer(r"\{\s*id:'([^']+)'\s*,\s*n:\s*(\d+)\s*,\s*dir:'([^']+)'\s*,\s*sp:\s*([\d.]+)\s*\}", _blk.group(1)):
    QUEUES.append({"id": mm.group(1), "n": int(mm.group(2)), "dir": mm.group(3), "sp": float(mm.group(4))})

# --- nha pho: moi loi goi shophouse(x, z, w, floors, color, ...) ---
SHOPS = []
for mm in re.finditer(r"shophouse\(\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*,\s*(\d+)\s*,\s*(0x[0-9a-fA-F]+)", SRC):
    SHOPS.append({"x": fnum(mm.group(1)), "z": fnum(mm.group(2)), "w": fnum(mm.group(3)),
                  "floors": int(mm.group(4)), "color": int(mm.group(5), 16)})

# --- tuy chon: dao nho moi + sap trang tri (BEFORE chua co -> bo qua) ---
NEW_RB = None
_m = re.search(r'const NEW_RB\s*=\s*\{\s*x:\s*(-?[\d.]+)\s*,\s*z:\s*(-?[\d.]+)\s*,\s*r:\s*([\d.]+)\s*\}', SRC)
if _m: NEW_RB = (fnum(_m.group(1)), fnum(_m.group(2)), fnum(_m.group(3)))

def parse_num_list(name):
    mm = re.search(r'const %s\s*=\s*\[([^\]]*)\]' % name, SRC)
    if not mm: return None
    return [float(v) for v in re.findall(r'-?[\d.]+', mm.group(1))]
DECOR_N_XS = parse_num_list("DECOR_N_XS")
DECOR_S_XS = parse_num_list("DECOR_S_XS")

# --- LOOP va RB_ARC ---
def parse_pts(name):
    mm = re.search(r'const %s\s*=\s*\[(.*?)\];' % name, SRC, re.S)
    if not mm: return []
    return [(fnum(a), fnum(b)) for a, b in
            re.findall(r'\[\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*\]', mm.group(1))]
LOOP = parse_pts("LOOP")
RB_ARC = parse_pts("RB_ARC")

print("[geo2] parse: stalls=%d shops=%d queues=%d sitters=%d LOOP=%d RB_ARC=%d "
      "spawn=%s rb=%s FNT=%s NEW_RB=%s DECOR_N=%s DECOR_S=%s" % (
          len(STALLS), len(SHOPS), len(QUEUES), len(SITTERS), len(LOOP), len(RB_ARC),
          SPAWN, RB_CENTER, FNT, NEW_RB,
          None if DECOR_N_XS is None else len(DECOR_N_XS),
          None if DECOR_S_XS is None else len(DECOR_S_XS)), flush=True)

# ============================================================
# 3) SCENE — helpers (toa do game -> Blender)
# ============================================================
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'
sc.cycles.samples = 24
sc.cycles.use_denoising = True
sc.render.threads_mode = 'FIXED'
sc.render.threads = 2
sc.render.resolution_x = 640
sc.render.resolution_y = 480
sc.render.resolution_percentage = 100

w = bpy.data.worlds.new("W"); sc.world = w
w.use_nodes = True
_bg = w.node_tree.nodes["Background"]
_bg.inputs[0].default_value = (0.52, 0.56, 0.60, 1.0)  # xam sang vua
_bg.inputs[1].default_value = 1.1

_MATS = {}
def mat(hexv, rough=0.9):
    if hexv in _MATS: return _MATS[hexv]
    m = bpy.data.materials.new("m%06x" % hexv); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = ((hexv >> 16 & 255) / 255.0,
                                            (hexv >> 8 & 255) / 255.0,
                                            (hexv & 255) / 255.0, 1.0)
    b.inputs["Roughness"].default_value = rough
    _MATS[hexv] = m
    return m

def C(x, y, z):
    """game (x, y-up, z) -> Blender (x, -z, y)"""
    return (x, -z, y)

def box(name, w_game, h_game, d_game, cx, cy, cz, hexv, rotY=0.0):
    bpy.ops.mesh.primitive_cube_add(location=C(cx, cy, cz))
    o = bpy.context.object; o.name = name
    o.dimensions = (w_game, d_game, h_game)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if rotY: o.rotation_euler = (0, 0, rotY)
    o.data.materials.append(mat(hexv))
    return o

def cyl(name, r, h, cx, cy, cz, hexv, seg=20, r_bottom=None):
    bpy.ops.mesh.primitive_cone_add(vertices=seg, radius1=(r if r_bottom is None else r_bottom),
                                    radius2=r, depth=h, location=C(cx, cy, cz))
    o = bpy.context.object; o.name = name
    o.data.materials.append(mat(hexv))
    return o

def sphere(name, r, cx, cy, cz, hexv):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=C(cx, cy, cz), segments=12, ring_count=8)
    o = bpy.context.object; o.name = name
    o.data.materials.append(mat(hexv))
    return o

# anh sang: sun
_sd = bpy.data.lights.new("Sun", 'SUN'); _sd.energy = 3.0
_so = bpy.data.objects.new("Sun", _sd); bpy.context.collection.objects.link(_so)
_so.rotation_euler = (math.radians(50), 0, math.radians(35))

# ============================================================
# 4) MAT DAT — luoi x -215..60, z -35..35, buoc 2.5, mau theo vung
# ============================================================
GR_MATS = [mat(0x453f3a), mat(0x978a78), mat(0x8a7f72), mat(0x5f8547)]  # nhua / san / da / xanh suon
xs = []
v = -215.0
while v <= 60.0 + 1e-9:
    xs.append(round(v, 4)); v += 2.5
zs = []
v = -35.0
while v <= 35.0 + 1e-9:
    zs.append(round(v, 4)); v += 2.5
verts = []
for gz in zs:
    for gx in xs:
        verts.append(C(gx, groundH(gx, gz), gz))
faces = []
fmats = []
nx = len(xs)
for j in range(len(zs) - 1):
    for i in range(nx - 1):
        a = j * nx + i; b = a + 1; c = a + nx; d = c + 1
        faces.append((a, b, d, c))
        cx = (xs[i] + xs[i + 1]) / 2.0; cz = (zs[j] + zs[j + 1]) / 2.0
        hc = groundH(cx, cz)
        if cx < -30 and abs(cz - 2) <= 16.5 and abs(hc - entryRampY(cx)) <= 0.2:
            fmats.append(0)
        elif abs(hc) <= 0.01 and -4 <= cz <= 13:
            fmats.append(1)
        elif abs(cx) <= 20 and -30 <= cz <= -2:
            fmats.append(2)
        else:
            fmats.append(3)
mesh = bpy.data.meshes.new("GroundMesh")
mesh.from_pydata(verts, [], faces)
mesh.update()
for m in GR_MATS: mesh.materials.append(m)
for poly, mi in zip(mesh.polygons, fmats):
    poly.material_index = mi
gobj = bpy.data.objects.new("Ground", mesh)
bpy.context.collection.objects.link(gobj)

# ============================================================
# 5) CONG TRINH
# ============================================================
STALL_COLS = [0xc8372d, 0x2e6da4, 0xc06c44, 0x68804f]

def build_stall(x, z, rotY, idx):
    y0 = stall_base_y(x, z)
    col = STALL_COLS[idx % len(STALL_COLS)]
    box("StallBody", 4.3, 1.0, 2.0, x, y0 + 0.5, z, 0x7a5c38, rotY)
    box("StallRoof", 4.6, 0.08, 2.6, x, y0 + 2.04, z, col, rotY)
    s, c = math.sin(rotY), math.cos(rotY)
    for lx, lz in ((-1.95, -0.85), (1.95, -0.85), (-1.95, 0.85), (1.95, 0.85)):
        # local -> world (khop cong thuc front: +Z local -> (sin, cos), +X local -> (cos, -sin))
        wx = x + lx * c + lz * s
        wz = z - lx * s + lz * c
        box("StallPost", 0.09, 2.0, 0.09, wx, y0 + 1.0, wz, 0x4a3826)

for i, s_ in enumerate(STALLS):
    build_stall(s_["x"], s_["z"], s_["rotY"], i)

# sap trang tri (chi khi code game co DECOR_N_XS / DECOR_S_XS)
_decor_i = len(STALLS)
if DECOR_N_XS:
    for dx in DECOR_N_XS:
        build_stall(dx, -15.7, 0.0, _decor_i); _decor_i += 1
if DECOR_S_XS:
    for dx in DECOR_S_XS:
        build_stall(dx, 26.0, math.pi, _decor_i); _decor_i += 1

# dao chinh + tuong lech tam
rbx, rbz = RB_CENTER
cyl("Roundabout", 10.5, 0.93, rbx, 0.465, rbz, 0x8a7f72, seg=36)
sx, sz = rbx + STATUE_OFF[0], rbz + STATUE_OFF[1]
box("StatueBase", 8.8, 1.14, 8.8, sx, 0.93 + 0.57, sz, 0x9a9184)
cyl("StatueCol", 0.5, 4.0, sx, 0.93 + 1.14 + 2.0, sz, 0xb8b0a0, seg=14)
sphere("StatueBall", 0.8, sx, 0.93 + 1.14 + 4.0, sz, 0xd8d2c2)

# dao nho moi (chi khi co NEW_RB)
if NEW_RB:
    cyl("NewRoundabout", NEW_RB[2], 0.93, NEW_RB[0], 0.465, NEW_RB[1], 0x8a7f72, seg=32)

# nha long cho
box("MarketHall", 68, 13, 16, 0, 6.5, 20, 0xa89a80)

# cong chao x=-131
_gy = groundH(-131, 2)
box("GatePost", 0.5, 7.6, 0.5, -131, _gy + 3.8, -13.5, 0x6a4a30)
box("GatePost", 0.5, 7.6, 0.5, -131, _gy + 3.8, 17.5, 0x6a4a30)
box("GateBeam", 0.6, 0.7, 31.5, -131, _gy + 7.7, 2, 0x5d2f24)

# dai phun nuoc
cyl("Fountain", 2.7, 0.55, FNT[0], 0.275, FNT[1], 0x8a8074, seg=24)

# nha pho
for shp in SHOPS:
    hgt = shp["floors"] * 3.05
    y0 = groundH(shp["x"], shp["z"])
    box("Shophouse", shp["w"], hgt, 5.6, shp["x"], y0 + hgt / 2.0, shp["z"], shp["color"])
    box("ShopRoof", shp["w"] + 0.8, 0.26, 6.6, shp["x"], y0 + hgt + 0.13, shp["z"], 0x8a4a38)

# ============================================================
# 6) NGUOI — capsule (tru r0.26 h1.05 + cau r0.26), mau seed co dinh
# ============================================================
_rng = random.Random(20261109)
PALETTE = [0xc8372d, 0x2e6da4, 0xd9a62e, 0x6b8f3e, 0x8668c4, 0xe58e6b,
           0x35507a, 0xf0ead8, 0x2e2a26, 0xc95d7e, 0xd97a30, 0x2f8f83]
_n_people = 0
def person(x, z, base_y):
    global _n_people
    col = _rng.choice(PALETTE)
    cyl("Person", 0.26, 1.05, x, base_y + 0.525, z, col, seg=10)
    sphere("PersonHead", 0.26, x, base_y + 1.05, z, col)
    _n_people += 1

# hang cho — tinh dung cong thuc game
for q in QUEUES:
    st = STALL_BY_ID.get(q["id"])
    if not st: continue
    fx = st["x"] + math.sin(st["rotY"]) * 2.1
    fz = st["z"] + math.cos(st["rotY"]) * 2.1
    ox, oz = (fx - st["x"]) / 2.1, (fz - st["z"]) / 2.1
    by = stall_base_y(st["x"], st["z"])
    for i in range(q["n"]):
        if q["dir"] == 'out':
            px, pz = fx + ox * (0.45 + i * q["sp"]), fz + oz * (0.45 + i * q["sp"])
        else:  # side
            px, pz = fx + (i - (q["n"] - 1) / 2.0) * q["sp"], fz - oz * 0.1
        person(px, pz, by)

# nguoi ngoi bac thang (y = stairH(z) + 0.3)
for (px, pz, _sched) in SITTERS:
    person(px, pz, stairH(pz) + 0.3)

# dong nguoi doc tuyen LOOP (khep kin) va RB_ARC, moi ~4u
def people_along(pts, closed):
    if len(pts) < 2: return
    seq = list(pts) + ([pts[0]] if closed else [])
    next_at = 0.0   # moc khoang cach (do doc tuyen) cua nguoi tiep theo
    travelled = 0.0
    for a, b in zip(seq[:-1], seq[1:]):
        seg_len = math.hypot(b[0] - a[0], b[1] - a[1])
        if seg_len <= 0: continue
        while next_at <= travelled + seg_len:
            t = (next_at - travelled) / seg_len
            px, pz = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
            person(px, pz, groundH(px, pz))
            next_at += 4.0
        travelled += seg_len
people_along(LOOP, True)
people_along(RB_ARC, False)
print("[geo2] people total =", _n_people, flush=True)

# ============================================================
# 7) 5 KHUNG HINH — lens 24
# ============================================================
def shot(tag, cam_game, tgt_game):
    _only = os.environ.get("GEO2_ONLY")
    if _only and tag not in _only.split(","): return
    for o in list(bpy.data.objects):
        if o.type == 'CAMERA': bpy.data.objects.remove(o, do_unlink=True)
    cd = bpy.data.cameras.new("Cam"); cd.lens = 24
    co = bpy.data.objects.new("Cam", cd); bpy.context.collection.objects.link(co)
    co.location = C(*cam_game)
    co.rotation_euler = (Vector(C(*tgt_game)) - Vector(C(*cam_game))).to_track_quat('-Z', 'Y').to_euler()
    sc.camera = co
    sc.render.filepath = os.path.join(OUT, "geo2-%s-%s.png" % (os.environ.get("GEO2_TAG", "before"), tag))
    bpy.ops.render.render(write_still=True)
    print("[geo2] rendered", tag, "cam", cam_game, "-> tgt", tgt_game, flush=True)

spx, spz = SPAWN
_g_spawn = groundH(spx, spz)
# (a) spawn: phia sau nguoi choi, nhin ve diem spawn (truc duong vao chay tiep ve phia +x)
shot("a", (spx - 11.15, _g_spawn + 6.5, spz), (spx, _g_spawn + 2.1, spz))
# (b) giua duong vao
shot("b", (-80, groundH(-80, 5.6) + 1.7, 5.6), (-40, groundH(-40, 3) + 1.7, 3))
# (c) duoi bac thang
shot("c", (0, groundH(0, 9.5) + 1.7, 9.5), (0, 6.0, -14))
# (d) dem bung binh - bac thang
shot("d", (-16, groundH(-16, 1.0) + 1.7, 1.0), (2, 3.5, -8))
# (d2) dung tren dia dao moi nhin ve bac (bo sung GEOMETRY-2 AFTER: khung chua tung co o BEFORE vi dao chua doi)
# NOTE: groundH port tra 0 o tam dao -> camera y 1.7 lot TRONG khoi dia (h 0.93 + tuong) = khung den; dung y co dinh 2.7 (mat dia 0.93 + tam mat 1.7)
shot("d2", (-30, 2.7, -6), (0, 4.5, -10))
# (e) pho an gio dong (day sap bac nhin sang day sap nam / pho an phia tay)
shot("e", (-47, groundH(-47, 6) + 1.7, 6), (-38, 1.2, -13))
print("[geo2] DONE", flush=True)
