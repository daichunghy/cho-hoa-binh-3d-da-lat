# build_one_glb.py — Chạy build_models.py nhưng CHỈ xuất 1 GLB (BLENDER-DEEP-1).
# Dùng: blender5 -b --python build_one_glb.py -- <tên: stairs|stall|...>
# Nạp toàn bộ phần định nghĩa của build_models.py (bỏ khối lệnh build ở cuối)
# rồi gọi đúng 1 hàm build_<tên> — nguồn sự thật vẫn là build_models.py.
import os, sys

argv = sys.argv[sys.argv.index('--') + 1:]
name = argv[0]
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'build_models.py'), encoding='utf-8').read()
marker = '\nbuild_character()\n'
head = src.split(marker)[0]
assert head != src, 'không thấy khối lệnh build ở cuối build_models.py'
ns = {'__file__': os.path.join(here, 'build_models.py')}
exec(compile(head, 'build_models.py', 'exec'), ns)
fn = ns.get('build_' + name)
assert fn, 'không có hàm build_' + name
fn()
print('BUILD-ONE DONE', name)
