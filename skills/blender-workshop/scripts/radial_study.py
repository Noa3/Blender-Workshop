"""Measure a dial's radial markers in Blender 4.5 or 5.3. Use a fresh background process."""
import argparse
import json
import math
from pathlib import Path
import sys

RADIUS = .03  # metres. One Blender unit = 1 m for this exercise.


def legacy_array(bpy, obj, count):
    # The pivot stays at the dial center. Move only the mesh, not the object.
    for vertex in obj.data.vertices:
        vertex.co.y += RADIUS
    empty = bpy.data.objects.new('Angular pitch', None)
    bpy.context.scene.collection.objects.link(empty)
    empty.rotation_euler.z = math.tau / count
    array = obj.modifiers.new('Rotating offset', 'ARRAY')
    array.fit_type = 'FIXED_COUNT'
    array.count = count
    array.use_relative_offset = array.use_constant_offset = False
    array.use_object_offset = True
    array.offset_object = empty
    array.use_merge_vertices = False


def circle_array(bpy, obj, count):
    # Append only Blender's own stock node asset. No user file, add-on or online asset.
    asset = Path(bpy.utils.system_resource('DATAFILES')) / 'assets/nodes/geometry_nodes_essentials.blend'
    if not asset.is_file():
        raise SystemExit('This Blender installation lacks its bundled Geometry Nodes Essentials library.')
    with bpy.data.libraries.load(str(asset), link=False, assets_only=True) as (source, target):
        if 'Array' not in source.node_groups:
            raise SystemExit('The installed Essentials library has no Array asset.')
        target.node_groups = ['Array']
    group, = target.node_groups
    sockets = {i.name: i for i in group.interface.items_tree if i.item_type == 'SOCKET' and i.in_out == 'INPUT'}
    for key, value in {'Shape': 'Circle', 'Central Axis': 'Z', 'Circle Segment': 'Full', 'Count Method': 'Count',
                       'Count': count, 'Radius': RADIUS, 'Realize Instances': True, 'Randomize': False, 'Merge': False}.items():
        sockets[key].default_value = value
    obj.modifiers.new('Full circle', 'NODES').node_group = group


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--count', type=int, default=6, help='number of separate marker faces, 3–64')
    args = parser.parse_args(argv)
    if not 3 <= args.count <= 64:
        parser.error('--count must be between 3 and 64')
    import bpy
    if not bpy.app.background or bpy.data.filepath:
        parser.exit(2, 'Use a fresh background process without an open file.\n')
    version = bpy.app.version[:2]
    if version not in {(4, 5), (5, 3)}:
        parser.exit(2, 'This comparison is scoped to Blender 4.5 and 5.3.\n')
    mesh = bpy.data.meshes.new('One marker face')
    mesh.from_pydata([(-.001, -.002, 0), (.001, -.002, 0), (.001, .002, 0), (-.001, .002, 0)], [], [(0, 1, 2, 3)])
    mesh.update()
    obj = bpy.data.objects.new('Dial markers', mesh)
    bpy.context.scene.collection.objects.link(obj)
    make = legacy_array if version == (4, 5) else circle_array
    make(bpy, obj, args.count)
    bpy.context.view_layer.update()
    evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
    final = evaluated.to_mesh()
    try:
        points = [(float(f.center.x) * 1000, float(f.center.y) * 1000) for f in final.polygons]
    finally:
        evaluated.to_mesh_clear()
    angle = lambda p: math.degrees(math.atan2(p[1], p[0])) % 360
    points.sort(key=angle)
    radii = [math.hypot(*p) for p in points]
    gaps = [(angle(b) - angle(a)) % 360 for a, b in zip(points, points[1:] + points[:1])]
    if (len(points) != args.count or any(abs(r - RADIUS * 1000) > .001 for r in radii)
            or any(abs(g - 360 / args.count) > .001 for g in gaps)):
        raise SystemExit(f'Unexpected marker geometry: {len(points)} faces; radii {radii}; angles {gaps}')
    print('RADIAL_LAYOUT ' + json.dumps({'blender': bpy.app.version_string, 'method': make.__name__,
          'centers_mm': [[round(c, 4) for c in p] for p in points], 'radii_mm': [round(r, 4) for r in radii],
          'angle_gaps_deg': [round(g, 4) for g in gaps]}, sort_keys=True))


if __name__ == '__main__':
    main(sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else sys.argv[1:])
