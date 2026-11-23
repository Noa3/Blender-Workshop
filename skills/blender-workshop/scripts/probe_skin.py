"""Measure subsurface transport through two thicknesses of a *synthetic* closed slab.
Run in a separate empty Blender 4.5 background Python process. No scene or image is delivered.
The dimensions, scale and color profile below are a diagnostic, not a skin preset.
"""
import argparse
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory


def main():
    import bpy
    from mathutils import Vector
    if not bpy.app.background or bpy.data.filepath:
        raise RuntimeError('Use an empty, separate background process.')
    bpy.ops.wm.read_factory_settings(use_empty=True)
    s=bpy.context.scene;s.render.engine='CYCLES';s.cycles.samples=160;s.cycles.seed=11
    s.cycles.use_denoising=False;s.cycles.max_bounces=8;s.render.threads_mode='FIXED';s.render.threads=4
    s.render.resolution_x=s.render.resolution_y=48;s.render.resolution_percentage=100
    s.render.image_settings.file_format='OPEN_EXR';s.render.image_settings.color_depth='32';s.render.image_settings.color_mode='RGB'
    world=bpy.data.worlds.new('Black world');world.use_nodes=True;world.node_tree.nodes['Background'].inputs['Strength'].default_value=0;s.world=world
    bpy.ops.object.camera_add(location=(0,0,.32));s.camera=bpy.context.object;s.camera.rotation_euler=Vector((0,0,-1)).to_track_quat('-Z','Y').to_euler();s.camera.data.type='ORTHO';s.camera.data.ortho_scale=.07;s.camera.data.clip_start=.001
    bpy.ops.object.light_add(type='AREA',location=(0,0,-.065));light=bpy.context.object;light.rotation_euler=Vector((0,0,1)).to_track_quat('-Z','Y').to_euler();light.data.shape='DISK';light.data.size=.052;light.data.energy=1.
    bpy.ops.mesh.primitive_cube_add(size=1);block=bpy.context.object
    mat=bpy.data.materials.new('Diagnostic — neutral albedo, unequal scattering lengths');mat.use_nodes=True;block.data.materials.append(mat)
    surf=mat.node_tree.nodes.get('Principled BSDF');surf.subsurface_method='RANDOM_WALK';surf.inputs['Base Color'].default_value=(.75,.75,.75,1);surf.inputs['Roughness'].default_value=.6;surf.inputs['Specular IOR Level'].default_value=0.;surf.inputs['Subsurface Radius'].default_value=(1.,.36,.17);surf.inputs['Subsurface Scale'].default_value=.005
    result={}
    with TemporaryDirectory(prefix='sss-probe-',dir=os.environ.get('TMPDIR')) as td:
        for label,thick,sss,watts in [('thin',.002,1.,1.),('thick',.012,1.,1.),('sss_off',.002,0.,1.),('light_off',.002,1.,0.)]:
            # Put the rear at z=0 in each case; do not move the light closer to the thicker surface.
            for vert in block.data.vertices:
                x,y,z=vert.co;vert.co=(.05 if x>0 else -.05,.05 if y>0 else -.05,thick if z>0 else 0.)
            block.data.update();surf.inputs['Subsurface Weight'].default_value=sss;light.data.energy=watts
            dest=Path(td)/(label+'.exr');s.render.filepath=str(dest);bpy.ops.render.render(write_still=True)
            im=bpy.data.images.load(str(dest),check_existing=False);pix=im.pixels[:];n=im.size[0]
            result[label]=[sum(pix[4*(y*n+x)+i] for y in range(16,32) for x in range(16,32))/256 for i in range(3)];bpy.data.images.remove(im)
    assert max(result['sss_off'])<.005 and max(result['light_off'])<.005, result
    assert result['thin'][0]>result['thick'][0]+.03 and result['thin'][0]>result['thin'][2]+.03, result
    result['runtime']=bpy.app.version_string;result['measure']='central 16 by 16 scene-linear mean RGB; front of a back-lit slab'
    print('SSS_PROBE '+json.dumps(result,sort_keys=True))


if __name__=='__main__':
    argparse.ArgumentParser(description=__doc__).parse_args();main()
