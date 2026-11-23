"""Desk grommet workshop: a closed section swept around +Z. No external assets.

Use Python + bpy, or blender -b --factory-startup --python-exit-code 1
--python grommet_lab.py -- COMMAND ... . Use --help for commands.
"""
import argparse
import json
import math
from pathlib import Path
import sys

NAME = 'Desk grommet'
N = 96


def profile():
    """Radius, height in mm; desk contact is z=0. Arcs remain editable loops."""
    points = []
    def arc(r, z, radius, a, b):
        for i in range(5):
            angle = math.radians(a + (b-a)*i/4)
            points.append((r+radius*math.cos(angle), z+radius*math.sin(angle)))
    arc(23.4, -13.4, .6, -90, 0)      # sleeve toe
    arc(24.45, -.45, .45, 180, 90)     # shoulder fillet
    arc(29.4, .6, .6, -90, 0)          # flange underside
    arc(28.5, 1.5, 1.5, 0, 90)         # outer rolled edge
    arc(22, 1, 2, 90, 180)             # cable entry
    arc(20.6, -13.4, .6, 180, 270)     # bore exit
    return points


def make_part(bpy):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.unit_settings.system = 'METRIC'
    scene.unit_settings.scale_length = .001
    scene.unit_settings.length_unit = 'MILLIMETERS'
    p = profile()
    vs = [(r*math.cos(math.tau*i/N), r*math.sin(math.tau*i/N), z)
          for r,z in p for i in range(N)]
    faces = []
    for j in range(len(p)):
        k = (j+1) % len(p)
        for i in range(N):
            h = (i+1) % N
            faces.append((j*N+i, j*N+h, k*N+h, k*N+i))
    mesh = bpy.data.meshes.new('Revolved section | editable quad loops')
    mesh.from_pydata(vs, [], faces)
    mesh.update()
    for f in mesh.polygons:
        f.use_smooth = True
    obj = bpy.data.objects.new(NAME, mesh)
    scene.collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    obj['datum'] = 'Z=0: desktop contact; +Z: rounded entry'
    # Only keep Layout; other factory workspaces can store file-browser history.
    active = bpy.context.window.workspace
    bpy.data.batch_remove([w for w in bpy.data.workspaces if w != active])
    bpy.data.orphans_purge(do_recursive=True)
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                area.spaces.active.region_3d.view_distance = 100
                area.spaces.active.overlay.show_floor = False
    scene.sequence_editor_clear()  # discard the unused sequencer's import directory
    scene.render.filepath = '//'
    scene.render.use_stamp_filename = False
    return obj


def inspect(bm):
    from mathutils.bvhtree import BVHTree
    bm.normal_update()
    tree = BVHTree.FromBMesh(bm)
    def ray(start, direction, length):
        return tree.ray_cast(start, direction, length)
    angles = [math.tau*(i+.5)/N for i in range(N)]
    directions = [(math.cos(a), math.sin(a)) for a in angles]
    samples = [(0,0)] + [(r*x,r*y) for r in (10,18,19.75) for x,y in directions]
    blocked = sum(ray((x,y,8),(0,0,-1),32)[0] is not None for x,y in samples)
    wall_hits = sum(ray((22*x,22*y,8),(0,0,-1),32)[0] is not None for x,y in directions)
    def surface(inner):
        radii, dots = [], []
        for x,y in directions:
            r, sign = (0,1) if inner else (40,-1)
            hit,n,_,_ = ray((r*x,r*y,-6),(sign*x,sign*y,0),40)
            if hit is not None:
                radii.append(math.hypot(hit.x,hit.y))
                dots.append(-sign*(x*n.x+y*n.y))
        return {'hits':len(radii), 'min_radius_mm':min(radii,default=None),
                'max_radius_mm':max(radii,default=None),'min_normal_alignment':min(dots,default=None)}
    return {'vertices':len(bm.verts), 'edges':len(bm.edges), 'faces':len(bm.faces),
            'quads':sum(len(f.verts)==4 for f in bm.faces),
            'boundary_or_nonmanifold_edges':sum(not e.is_manifold for e in bm.edges),
            'inconsistent_edges':sum(not e.is_contiguous for e in bm.edges),
            'nonmanifold_vertices':sum(not v.is_manifold for v in bm.verts),
            'signed_volume_mm3':bm.calc_volume(signed=True),
            'bounds_mm':[[round(op(v.co[i] for v in bm.verts),5) for i in range(3)] for op in (min,max)],
            'passage_rays':len(samples),'blocked_passage_rays':blocked,'wall_rays':N,'wall_hits':wall_hits,
            'bore_middepth':surface(True),'sleeve_middepth':surface(False)}


def verify(bpy, src):
    import bmesh
    from mathutils import Matrix
    bpy.ops.wm.open_mainfile(filepath=str(src.resolve()), load_ui=False, use_scripts=False)
    scene = bpy.context.scene
    obj = scene.objects[NAME]
    ev = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
    bm = bmesh.new()
    mesh = ev.to_mesh()
    bm.from_mesh(mesh)
    bm.transform(ev.matrix_world)
    ev.to_mesh_clear()
    actual = inspect(bm)
    bm.faces.ensure_lookup_table()
    bm.faces.remove(bm.faces[0])
    opened = inspect(bm)
    bm.free()
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=N,
                          radius1=24, radius2=24, depth=14)
    solid = inspect(bm)
    bm.free()
    def radial_ok(result, radius):
        target = radius*math.cos(math.pi/N)  # apothem, not vertex radius
        return (result['hits']==N and result['min_normal_alignment']>.999 and
                all(abs(result[k]-target)<.01 for k in ('min_radius_mm','max_radius_mm')))
    checks = {'one_editable_mesh':len(scene.objects)==1 and obj.type=='MESH' and len(obj.data.polygons)==30*N,
              'identity_transform':obj.matrix_world==Matrix.Identity(4),
              'mm_units':scene.unit_settings.system=='METRIC' and abs(scene.unit_settings.scale_length-.001)<1e-9,
              'world_bounds':actual['bounds_mm']==[[-30,-30,-14],[30,30,3]],
              'closed_oriented_quads':actual['boundary_or_nonmanifold_edges']==actual['inconsistent_edges']==actual['nonmanifold_vertices']==0 and actual['signed_volume_mm3']>0 and actual['quads']==actual['faces'],
              'straight_passage_samples':actual['blocked_passage_rays']==0,
              'annular_wall_obstructs':actual['wall_hits']==N,
              'bore_radius_and_normals':radial_ok(actual['bore_middepth'],20),
              'sleeve_radius_and_normals':radial_ok(actual['sleeve_middepth'],24),
              'blocked_control':solid['boundary_or_nonmanifold_edges']==0 and solid['blocked_passage_rays']==solid['passage_rays'],
              'open_control':opened['boundary_or_nonmanifold_edges']==4 and opened['blocked_passage_rays']==0}
    return {'scene':src.name,'blender':bpy.app.version_string,'checks':checks,'evaluated_world_mesh':actual,
            'controls':{'solid':solid,'missing_quad':opened},
            'scope':'Static sampled straight axial rays, not a moving cable or connector fit simulation.'}


def main():
    parser = argparse.ArgumentParser(description='Model and inspect a 60 mm desk cable grommet. Outputs must be new.')
    cmds = parser.add_subparsers(dest='action',required=True)
    build = cmds.add_parser('build',help='Create the editable .blend scene')
    build.add_argument('scene',type=Path)
    check = cmds.add_parser('verify',help='Reopen the scene; inspect evaluated geometry and two in-memory controls')
    check.add_argument('scene',type=Path)
    check.add_argument('evidence',type=Path)
    args = parser.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else sys.argv[1:])
    if args.scene.suffix.lower()!='.blend':
        parser.error('scene must end in .blend')
    dest = args.scene if args.action=='build' else args.evidence
    if dest.exists() or dest.is_symlink():
        parser.error(f'refusing to overwrite {dest}')
    import bpy
    if not bpy.app.background or bpy.data.filepath:
        parser.exit(2, 'Use a fresh background process without an open file.\n')
    if args.action=='build':
        make_part(bpy)
        bpy.ops.wm.save_as_mainfile(filepath=str(dest.resolve()),compress=False)
    else:
        report = verify(bpy,args.scene)
        with dest.open('x', encoding='utf-8') as f:
            json.dump(report,f,indent=2,allow_nan=False)
            f.write('\n')
        failed = [k for k,v in report['checks'].items() if not v]
        if failed:
            raise RuntimeError('Failed: '+', '.join(failed))


if __name__=='__main__':
    main()
