"""Compare three Mirror seams on a five-face half box in an empty background job. No file I/O."""
import argparse
from collections import Counter
import json
import sys


def measure(mesh):
    """Inspect actual face incidence and edge connectivity, not proximity in space."""
    use = Counter(edge for face in mesh.polygons for edge in face.edge_keys)
    adjacent = [set() for _ in mesh.vertices]
    for edge in mesh.edges:
        a, b = edge.vertices
        adjacent[a].add(b)
        adjacent[b].add(a)
    remaining = set(range(len(adjacent)))
    islands = 0
    while remaining:
        todo = [remaining.pop()]
        while todo:
            neighbors = adjacent[todo.pop()] & remaining
            remaining.difference_update(neighbors)
            todo.extend(neighbors)
        islands += 1
    coords = [vertex.co[:] for vertex in mesh.vertices]
    return {
        'vertices': len(coords), 'faces': len(mesh.polygons), 'islands': islands,
        'boundary_edges': sum(use[edge.key] == 1 for edge in mesh.edges),
        'bounds_mm': [round(1000 * (max(a) - min(a)), 4) for a in zip(*coords)],
        # On this symmetric box the two innermost X rings delimit the seam.
        'measured_seam_gap_mm': round(2000 * min(abs(v[0]) for v in coords), 4),
    }


def case(bpy, seam_mm, weld):
    verts = [(x * .001, y * .001, z * .001) for x in (seam_mm, 50)
             for y, z in ((-20, 0), (20, 0), (20, 10), (-20, 10))]
    faces = [(i, (i + 1) % 4, 4 + (i + 1) % 4, 4 + i) for i in range(4)] + [(4, 5, 6, 7)]
    mesh = bpy.data.meshes.new('Open half')
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new('Seam test', mesh)
    bpy.context.scene.collection.objects.link(obj)
    try:
        mirror = obj.modifiers.new('Local X seam', 'MIRROR')
        mirror.use_axis = (True, False, False)
        mirror.use_clip = True
        mirror.use_mirror_merge = weld
        mirror.merge_threshold = .0001  # 0.1 mm in this one-metre-per-unit study.
        bpy.context.view_layer.update()
        evaluated = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
        final = evaluated.to_mesh()
        try:
            return {**measure(final), 'merge': bool(mirror.use_mirror_merge),
                    'clipping': bool(mirror.use_clip), 'source_boundary_edges': measure(mesh)['boundary_edges']}
        finally:
            evaluated.to_mesh_clear()
    finally:
        bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.meshes.remove(mesh)


def main(args):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['compare'], help='evaluate three in-memory variants; print JSON')
    parser.parse_args(args)
    import bpy
    if not bpy.app.background or bpy.data.filepath:
        parser.exit(2, 'Use a fresh background process without an open file.\n')
    results = {key: case(bpy, gap, weld) for key, gap, weld in (
        ('welded', 0, True), ('coincident_unwelded', 0, False), ('outside_distance', 1, True))}
    for key, expected in [('welded', (1, 0, 0)), ('coincident_unwelded', (2, 8, 0)),
                          ('outside_distance', (2, 8, 2))]:
        row = results[key]
        actual = row['islands'], row['boundary_edges'], row['measured_seam_gap_mm']
        if actual != expected or row['source_boundary_edges'] != 4:
            raise SystemExit(f'{key}: unexpected seam measurement: {row}')
    print('MIRROR_SEAM ' + json.dumps({'blender': bpy.app.version_string, 'cases': results}, sort_keys=True))


if __name__ == '__main__':
    main(sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else sys.argv[1:])
