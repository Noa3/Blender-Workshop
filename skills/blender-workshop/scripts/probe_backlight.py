"""Distinguish a backlit sheet from an emitter using linear pixel measurements.
Run in a separate headless Blender 4.5 Python process: python -IB probe_backlight.py
No .blend, demo or persistent images. Never run inside an artist's open session.
"""
import argparse
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory


def measure():
    import bpy
    from mathutils import Vector
    if not bpy.app.background or bpy.data.filepath:
        raise RuntimeError('Use an empty, separate background process, not an open project.')
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.render.engine = 'CYCLES'
    scene.cycles.samples = 48
    scene.cycles.seed = 19
    scene.cycles.use_denoising = False
    scene.cycles.max_bounces = 3
    scene.render.threads_mode = 'FIXED'
    scene.render.threads = 3
    scene.render.resolution_x = scene.render.resolution_y = 48
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'OPEN_EXR'
    scene.render.image_settings.color_depth = '32'
    scene.render.image_settings.color_mode = 'RGB'
    world=bpy.data.worlds.new('Unlit room');world.use_nodes=True
    world.node_tree.nodes['Background'].inputs['Strength'].default_value=0.0
    scene.world=world
    bpy.ops.object.camera_add(location=(0,0,2));scene.camera=bpy.context.object
    scene.camera.rotation_euler=Vector((0,0,-1)).to_track_quat('-Z','Y').to_euler()
    scene.camera.data.type='ORTHO';scene.camera.data.ortho_scale=1.4
    bpy.ops.mesh.primitive_plane_add(size=1.2)
    sheet=bpy.context.object;mat=bpy.data.materials.new('Test sheet');mat.use_nodes=True;sheet.data.materials.append(mat)
    tree=mat.node_tree;out=tree.nodes.get('Material Output')
    bpy.ops.object.light_add(type='AREA',location=(0,0,-.65));lamp=bpy.context.object
    lamp.rotation_euler=Vector((0,0,1)).to_track_quat('-Z','Y').to_euler();lamp.data.shape='DISK';lamp.data.size=.56
    v={}
    with TemporaryDirectory(prefix='backlight-',dir=os.environ.get('TMPDIR')) as td:
        for label,typ in [('opaque','ShaderNodeBsdfDiffuse'),('translucent','ShaderNodeBsdfTranslucent'),('emissive','ShaderNodeEmission')]:
            node=tree.nodes.new(typ);node.inputs['Color'].default_value=(.65,.65,.65,1);tree.links.new(node.outputs[0],out.inputs['Surface'])
            for setting,watts in [('lit',15.),('dark',0.)]:
                lamp.data.energy=watts;path=Path(td)/(label+'-'+setting+'.exr');scene.render.filepath=str(path)
                bpy.ops.render.render(write_still=True)
                im=bpy.data.images.load(str(path),check_existing=False);pix=im.pixels[:];width,height=im.size[:]
                assert (width,height)==(48,48)
                vals=[sum(pix[(y*width+x)*4:(y*width+x)*4+3])/3 for x in range(18,30) for y in range(18,30)]
                v[label+'_'+setting]=sum(vals)/len(vals);bpy.data.images.remove(im)
    assert v['translucent_lit']>v['opaque_lit']+.05 and v['translucent_lit']>v['translucent_dark']+.06, v
    assert v['emissive_dark']>.2 and abs(v['emissive_lit']-v['emissive_dark'])<.01, v
    return {**v,'runtime':bpy.app.version_string,'measurement':'central 12 by 12 scene-linear RGB, arithmetic mean; artificial diagnostic only'}


if __name__=='__main__':
    argparse.ArgumentParser(description=__doc__).parse_args()
    print('BACKLIGHT '+json.dumps(measure(),sort_keys=True))
