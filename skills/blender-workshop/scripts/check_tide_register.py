"""Measure the evaluated tide needle in a saved Blender 4.5 file. Never save changes."""
import argparse
import json
import math
from pathlib import Path
import sys

import bpy



def require(test, message):
    if not test:
        raise ValueError(message)


def check_motion(scene):
    needle = scene.objects.get('Sweep needle')
    spindle = scene.objects.get('Spindle reference')
    require(needle is not None and spindle is not None, 'No sweep needle and fixed spindle to compare')
    require((scene.frame_start, scene.frame_end, scene.frame_step, scene.render.fps, scene.render.fps_base) == (1, 48, 1, 24, 1), 'Play frames 1–48 at 24 fps; do not play the repeated key at 49')
    require(scene.camera is not None, 'Set an active camera')
    tip_id = max(needle.data.vertices, key=lambda v: v.co.y).index
    axis = spindle.matrix_world.translation.copy()
    angles, radii, drifts = [], [], []
    for frame in range(1, 50):
        scene.frame_set(frame)
        ob = needle.evaluated_get(bpy.context.evaluated_depsgraph_get())
        pivot = ob.matrix_world.translation
        delta = ob.matrix_world @ ob.data.vertices[tip_id].co - axis
        drifts.append((pivot-axis).length)
        radii.append(math.hypot(delta.x, delta.y))
        angles.append(math.degrees(math.atan2(delta.x, delta.y)))
    require(max(drifts) < 1e-5 and max(radii)-min(radii) < 1e-5 and min(radii) > .6, 'The hinge moved or the evaluated needle tip left its circle')
    require(max(angles) > 56 and min(angles) < -56, 'No overshoot on both sides of the dial')
    require(49 < angles[13] < 55 and -55 < angles[37] < -49, 'Needle did not settle back from its overshoot')
    hold = max(abs(angles[i]-angles[start]) for start in (13,37) for i in range(start,start+4))
    require(hold < .01, 'Angle drift inside an intentional four-frame hold')
    inside, seam = angles[1]-angles[0], angles[48]-angles[47]
    require(abs(angles[0]-angles[-1]) < .001 and min(inside,seam) > 3 and abs(inside-seam) < 1, 'The loop lost its pose or speed across 48 → 1 → 2')
    return {'played_frames': 48, 'frames_measured_including_closure': len(angles), 'fps': 24, 'angle_range_degrees': [round(min(angles),3),round(max(angles),3)], 'settled_degrees': [round(angles[13],3),round(angles[37],3)], 'max_spindle_drift_scene_units': max(drifts), 'tip_radius_span_scene_units': max(radii)-min(radii), 'hold_variation_degrees': hold, 'seam_steps_degrees': [round(seam,4),round(inside,4)]}


def check_print(scene):
    needle = scene.objects['Sweep needle']
    top = max(needle.data.polygons, key=lambda p: p.normal.z)
    mat = needle.data.materials[top.material_index]
    graph = mat.node_tree
    shader = next(n for n in graph.nodes if n.type == 'BSDF_PRINCIPLED')
    values = {}
    for socket, space in [('Base Color', 'sRGB'), ('Roughness', 'Non-Color')]:
        links = shader.inputs[socket].links
        require(links and links[0].from_node.type == 'TEX_IMAGE', f'{socket} must use a baked image on the visible blade face')
        node = links[0].from_node
        image = node.image
        require(image and image.packed_file and image.colorspace_settings.name == space, f'{socket} needs a packed {space} image')
        filename = 'needle-' + socket.lower().replace(' ', '-') + '.png'
        require(image.filepath == '//textures/' + filename and len(image.packed_files) == 1 and image.packed_files[0].filepath == image.filepath,
                f'{socket} needs a portable unpack destination: //textures/{filename}')
        coords = node.inputs['Vector'].links
        require(coords and coords[0].from_node.type == 'UVMAP', 'Both images must follow the blade UV, not the room')
        uv = needle.data.uv_layers.get(coords[0].from_node.uv_map)
        require(uv is not None, 'The named UV layer is missing')
        by_vertex = [(needle.data.vertices[needle.data.loops[i].vertex_index].co, uv.data[i].uv) for i in top.loop_indices]
        require(all(abs(float(p.y) - (float(q.y)*1.2-.28)) < 1e-5 for p,q in by_vertex), 'Longitudinal print registration changed')
        w,h=image.size
        samples=[]
        for v in (.50,.76):
            offset=4*(int(v*h)*w+w//2); samples.append([round(x,4) for x in image.pixels[offset:offset+3]])
        values[socket] = samples
    body, band = values['Base Color']
    require(body[0] > 2*body[1] and band[1] > body[1]+.25 and band[2] > body[2]+.20, 'The light witness band or red enamel is missing')
    require(all(abs(value-target)<.02 for pixel,target in zip(values['Roughness'],(.28,.70)) for value in pixel), 'Roughness is reversed, color-managed, or flat')
    return values


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path)
    args = parser.parse_args(argv)
    require(bpy.app.background and not bpy.data.filepath, 'Use a fresh background process without an open scene')
    bpy.ops.wm.open_mainfile(filepath=str(args.file.resolve()), load_ui=False, use_scripts=False)
    print('TIDE_CHECK ' + json.dumps({'motion': check_motion(bpy.context.scene), 'baked_texel_samples': check_print(bpy.context.scene)}, sort_keys=True))


if __name__ == '__main__':
    main(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else sys.argv[1:])
