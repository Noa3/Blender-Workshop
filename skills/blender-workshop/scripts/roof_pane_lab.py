"""Measure an editable hole in glazing, including a shrinking-border and a sealed control.

Run in a separate Blender process, e.g. blender -b -P roof_pane_lab.py -- new-folder.
The output folder must not exist. Units are metres unless reported as millimetres.
"""
import json
from pathlib import Path
import sys
from math import hypot

import bpy


def pane(name, cut, protect):
    count = 20
    points = [(i / count - 0.5, (j / count - 0.5) * 0.8, 0.0)
              for j in range(count + 1) for i in range(count + 1)]
    faces = []
    for j in range(count):
        for i in range(count):
            a = j * (count + 1) + i
            faces.append((a, a + 1, a + count + 2, a + count + 1))
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(points, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    if cut:
        keep = obj.vertex_groups.new(name='Remaining glass')
        keep.add([i for i, (x, y, _) in enumerate(points) if hypot(x, y) > 0.14], 1.0, 'REPLACE')
        mask = obj.modifiers.new('Painted opening', 'MASK')
        mask.vertex_group = keep.name
    smooth = obj.modifiers.new('Soften the broken edge', 'SMOOTH')
    smooth.factor, smooth.iterations = 0.8, 6
    if protect:
        movable = obj.vertex_groups.new(name='Interior only')
        movable.add([i for i, (x, y, _) in enumerate(points) if abs(x) < 0.49 and abs(y) < 0.39], 1.0, 'REPLACE')
        smooth.vertex_group = movable.name
    thick = obj.modifiers.new('Glass thickness', 'SOLIDIFY')
    thick.thickness, thick.offset = 0.006, -1.0
    return obj


def measure(obj):
    bpy.context.view_layer.update()
    evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
    vertices = [v.co.copy() for v in evaluated.data.vertices]
    def hits(x, y):
        return bool(evaluated.ray_cast((x, y, 0.1), (0.0, 0.0, -1.0))[0])
    return {'corner_shift_mm': 1000 * min(hypot(p.x + 0.5, p.y + 0.4) for p in vertices),
            'clear_center': not hits(0.001, 0.002), 'hit_intact_patch': hits(0.31, 0.17),
            'thickness_mm': 1000 * (max(p.z for p in vertices) - min(p.z for p in vertices))}


def main(out):
    out.mkdir(parents=True, exist_ok=False)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    receipt = {'blender': bpy.app.version_string}
    for n, cut, protected, x in [('protected', True, True, 0), ('unprotected', True, False, 1.2), ('sealed_control', False, True, 2.4)]:
        obj = pane(n, cut, protected)
        obj.location.x = x
        receipt[n] = measure(obj)
    bpy.ops.wm.save_as_mainfile(filepath=str(out / 'Glazing-Controls.blend'), compress=True)
    (out / 'pane-checks.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(receipt))


if __name__ == '__main__':
    args = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else sys.argv[1:]
    if len(args) != 1:
        raise SystemExit('Pass one new output directory.')
    main(Path(args[0]).expanduser().resolve())
