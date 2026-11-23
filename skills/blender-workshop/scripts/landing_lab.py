"""Build or measure an original landing-pivot comparison in fresh Blender 4.5 Python."""
import argparse
import json
import math
from pathlib import Path
import sys

FILE = 'landing_pivots.blend'
BALLS = ('Bottom pivot', 'Center pivot')
POSES = ((1, 2.8, 1), (7, 1.6, 1), (11, 0, 1), (14, 0, .5), (20, 0, .92), (25, 0, 1))


def build(bpy, directory, render):
    from mathutils import Vector

    directory.mkdir(parents=True, exist_ok=False)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.name = 'Landing | pivot comparison'
    scene.frame_start, scene.frame_end, scene.render.fps = 1, 25, 24
    bpy.context.preferences.edit.keyframe_new_interpolation_type = 'LINEAR'

    def paint(obj, name, color):
        material = bpy.data.materials.new(name)
        material.diffuse_color = (*color, 1)
        obj.data.materials.append(material)

    for i, (name, x, color) in enumerate(zip(BALLS, (-1.7, 1.7), ((.08,.48,.78), (.9,.32,.08)))):
        bpy.ops.mesh.primitive_uv_sphere_add()
        obj = bpy.context.object
        obj.name = name
        paint(obj, name, color)
        if i == 0:
            for vertex in obj.data.vertices:
                vertex.co.z += 1
        bpy.ops.object.shade_smooth()
        for frame, height, squash in POSES:
            obj.location = (x, 0, height + i)
            width = 1 / math.sqrt(squash)
            obj.scale = (width, width, squash)
            obj.keyframe_insert('location', frame=frame)
            obj.keyframe_insert('scale', frame=frame)
        animation = obj.animation_data
        strip = animation.action.layers[0].strips[0]
        for curve in strip.channelbag(animation.action_slot).fcurves:
            for key in curve.keyframe_points:
                key.interpolation = 'LINEAR'

    bpy.ops.mesh.primitive_plane_add(size=30)
    bpy.context.object.name = 'Floor'
    paint(bpy.context.object, 'Floor', (.22,.25,.3))
    bpy.ops.object.camera_add(location=(0,-14,3))
    camera = bpy.context.object
    camera.rotation_euler = (Vector((0,0,1.9)) - camera.location).to_track_quat('-Z','Y').to_euler()
    camera.data.type, camera.data.ortho_scale = 'ORTHO', 8.5
    scene.camera = camera
    bpy.ops.object.light_add(type='AREA', location=(-2,-5,8))
    light = bpy.context.object
    light.rotation_euler = (-light.location).to_track_quat('-Z','Y').to_euler()
    light.data.energy, light.data.shape, light.data.size = 1500, 'DISK', 5
    scene.world = bpy.data.worlds.new('Studio')
    scene.world.color = (.3,.3,.3)
    scene.render.engine = 'CYCLES'
    scene.render.use_stamp_filename = False
    scene.cycles.samples, scene.cycles.use_denoising = 8, True
    scene.render.resolution_x, scene.render.resolution_y, scene.render.resolution_percentage = 384, 240, 100
    for frame, name in ((1,'Descent'), (11,'First contact'), (14,'Max squash: compare gaps'), (25,'Rest')):
        scene.timeline_markers.new(name, frame=frame)
    scene.frame_set(14)
    scene.render.filepath = '//landing-preview.png'
    bpy.ops.wm.save_as_mainfile(filepath=str(directory / FILE))
    if render:
        for frame in (11, 14, 25):
            scene.frame_set(frame)
            scene.render.filepath = str(directory / f'pivot-{frame}.png')
            bpy.ops.render.render(write_still=True)


def verify(bpy, directory):
    bpy.ops.wm.open_mainfile(filepath=str(directory / FILE), load_ui=False, use_scripts=False)
    scene = bpy.context.scene
    if (not scene.camera or bpy.data.libraries or bpy.data.texts or
            (scene.frame_start, scene.frame_end, scene.render.fps) != (1, 25, 24)):
        raise ValueError('Expected a standalone 25-frame camera study at 24 fps.')
    rows = []
    for frame in range(1, 26):
        scene.frame_set(frame)
        deps = bpy.context.evaluated_depsgraph_get()
        def heights(name):
            obj = scene.objects[name].evaluated_get(deps)
            return [(obj.matrix_world @ v.co).z for v in obj.data.vertices]
        if any(abs(z) > 1e-5 for z in heights('Floor')):
            raise ValueError(f'Floor displaced at frame {frame}')
        row = {'frame': frame}
        for name in BALLS:
            row[name] = min(heights(name))
        # Compare against the intended linear descent and recovery, not just the extrema.
        a, b = next((a,b) for a,b in zip(POSES, POSES[1:]) if a[0] <= frame <= b[0])
        t = (frame-a[0]) / (b[0]-a[0])
        h, scale = ((1-t)*a[i] + t*b[i] for i in (1,2))
        for name, expected in zip(BALLS, (h, h+1-scale)):
            if not math.isclose(row[name], expected, abs_tol=1e-5):
                raise ValueError(f'{name} contact at frame {frame}: measured {row[name]:.6f}, expected {expected:.6f}')
            row[name] = round(row[name], 6)
        rows.append(row)
    return {'bpy': bpy.app.version_string, 'units':'world Z of lowest evaluated mesh vertex; floor = 0', 'rows':rows}


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    verbs = parser.add_subparsers(dest='verb', required=True)
    make = verbs.add_parser('build', help='create a new folder; never overwrite')
    make.add_argument('directory', type=Path)
    make.add_argument('--render', action='store_true', help='also render frames 11, 14 and 25')
    check = verbs.add_parser('verify', help='measure the saved scene without writing; emit JSON')
    check.add_argument('directory', type=Path)
    args = parser.parse_args(argv)
    import bpy
    if not bpy.app.background or bpy.data.filepath:
        parser.exit(2, 'Use a fresh background process without an open file.\n')
    directory = args.directory.absolute()
    if args.verb == 'build':
        if directory.exists() or directory.is_symlink():
            parser.exit(2, 'Output already exists; choose a new directory.\n')
        build(bpy, directory, args.render)
    elif not (directory / FILE).is_file():
        parser.exit(2, f'Missing {FILE}.\n')
    else:
        try:
            print(json.dumps(verify(bpy, directory)))
        except (KeyError, ValueError) as exc:
            parser.exit(1, f'Verification failed: {exc}\n')


if __name__ == '__main__':
    main(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else sys.argv[1:])
