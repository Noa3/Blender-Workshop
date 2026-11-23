"""Check a two-palette face mask in Cycles on a flat UV chart, not a game asset.

Use standalone background bpy 4.5 Python. The camera follows the chart, so
patch positions are always head-relative. No user scene or output is saved.
"""
import json
import math
import os
from pathlib import Path
from tempfile import TemporaryDirectory


def main():
    import bpy
    from mathutils import Vector

    if not bpy.app.background or bpy.data.filepath:
        raise RuntimeError('Use an empty, separate background process.')
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.render.engine = 'CYCLES'; scene.cycles.samples = 2
    scene.cycles.use_denoising = False; scene.cycles.seed = 7
    scene.render.threads_mode = 'FIXED'; scene.render.threads = 2
    scene.render.resolution_x = scene.render.resolution_y = 48
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'OPEN_EXR'
    scene.render.image_settings.color_depth = '32'
    scene.world = bpy.data.worlds.new('Black world'); scene.world.color = (0,0,0)
    bpy.ops.mesh.primitive_plane_add(size=2)
    head = bpy.context.object
    bpy.ops.object.camera_add(location=(0,0,3))
    cam = bpy.context.object; cam.parent = head
    cam.rotation_euler = (0,0,0); cam.data.type = 'ORTHO'; cam.data.ortho_scale = 2.2
    scene.camera = cam
    # The key marker is a *nominated* direction; light transport does not drive this shader.
    key = bpy.data.objects.new('Designated key direction', None); scene.collection.objects.link(key)
    mat = bpy.data.materials.new('Original face-mask diagnostic'); mat.use_nodes = True
    head.data.materials.append(mat)
    nodes = mat.node_tree.nodes; nodes.clear(); link = mat.node_tree.links.new
    coords = nodes.new('ShaderNodeTexCoord'); xyz = nodes.new('ShaderNodeSeparateXYZ')
    link(coords.outputs['UV'], xyz.inputs[0]); u = xyz.outputs['X']
    mirror = nodes.new('ShaderNodeMath'); mirror.operation = 'SUBTRACT'
    mirror.inputs[0].default_value = 1.; link(u, mirror.inputs[1])
    side = nodes.new('ShaderNodeMixRGB'); link(u, side.inputs[1]); link(mirror.outputs[0], side.inputs[2])
    gate = nodes.new('ShaderNodeMapRange'); gate.interpolation_type = 'SMOOTHSTEP'; gate.clamp = True
    link(side.outputs[0], gate.inputs['Value'])
    palette = nodes.new('ShaderNodeMixRGB'); link(gate.outputs[0], palette.inputs[0])
    palette.inputs[1].default_value = (.08,.03,.04,1); palette.inputs[2].default_value = (.72,.42,.26,1)
    emission = nodes.new('ShaderNodeEmission'); link(palette.outputs[0], emission.inputs['Color'])
    output = nodes.new('ShaderNodeOutputMaterial'); link(emission.outputs[0], output.inputs['Surface'])
    states = [('right', 0, (1,0,0), True), ('left', 0, (-1,0,0), True),
              ('front', 0, (0,1,0), True), ('head_turn', 180, (1,0,0), True),
              ('head_and_key_turn', 90, (0,1,0), True), ('fixed_world_control', 180, (1,0,0), False)]
    result = {}
    with TemporaryDirectory(prefix='palette-chart-', dir=os.environ.get('TMPDIR')) as tmp:
        for name, yaw, light_position, head_local in states:
            head.rotation_euler.z = math.radians(yaw); key.location = light_position
            bpy.context.view_layer.update()
            direction = key.matrix_world.translation - head.matrix_world.translation
            if head_local:
                direction = head.matrix_world.to_quaternion().inverted() @ direction
            horizontal = Vector(direction[:2]).normalized()  # test states contain no vertical key
            amount = (1-horizontal.y)/2
            side.inputs[0].default_value = float(horizontal.x < 0)
            gate.inputs['From Min'].default_value = amount-.025; gate.inputs['From Max'].default_value = amount+.025
            path = Path(tmp)/(name+'.exr'); scene.render.filepath = str(path)
            bpy.ops.render.render(write_still=True)
            image = bpy.data.images.load(str(path), check_existing=False); px = image.pixels[:]; width = image.size[0]
            result[name] = [[sum(px[4*(y*width+x)+c] for x in range(start,start+4) for y in range(22,26))/16
                             for c in range(3)] for start in (12,32)]
            bpy.data.images.remove(image)
    def red_difference(state):
        return result[state][1][0] - result[state][0][0]
    assert red_difference('right') > .5 and red_difference('left') < -.5, result
    assert red_difference('head_turn') < -.5 and red_difference('fixed_world_control') > .5, result
    assert red_difference('head_and_key_turn') > .5 and abs(red_difference('front')) < .005, result
    print('PALETTE_PROBE ' + json.dumps({'runtime': bpy.app.version_string, 'samples': result}, sort_keys=True))


if __name__ == '__main__':
    main()
