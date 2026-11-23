"""Recombine three Cycles light groups from one linear render; Blender 4.5 LTS, no add-ons."""
import argparse
import json
from pathlib import Path
import sys
import bpy
import numpy as np
from mathutils import Vector


def aim(obj, target):
    obj.rotation_euler=(Vector(target)-obj.location).to_track_quat('-Z','Y').to_euler()


def area(group, xyz, power, color):
    bpy.ops.object.light_add(type='AREA',location=xyz)
    light=bpy.context.object; light.name=group+' / softbox'; light.lightgroup=group
    light.data.energy=power;light.data.shape='DISK';light.data.size=2.0;light.data.color=color
    aim(light,(0,0,0.4))


def render(out):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene=bpy.context.scene; scene.render.engine='CYCLES';scene.cycles.device='CPU';scene.cycles.samples=32
    scene.cycles.use_adaptive_sampling=False;scene.cycles.use_denoising=False;scene.cycles.seed=23
    scene.render.threads_mode='FIXED';scene.render.threads=4
    scene.render.resolution_x=180;scene.render.resolution_y=112;scene.render.resolution_percentage=100
    scene.render.film_transparent=False;scene.render.use_stamp=False
    world=bpy.data.worlds.new('Overcast reflection card');world.color=(0.12,0.18,0.25);world.lightgroup='Sky';scene.world=world
    groups=['Canopy','Practical','Sky']; layer=bpy.context.view_layer
    for g in groups:layer.lightgroups.add(name=g)
    bpy.ops.mesh.primitive_plane_add(size=200);floor=bpy.context.object;floor.name='Platform / receiver'
    mat=bpy.data.materials.new('Damp platform slate');mat.use_nodes=True;bsdf=mat.node_tree.nodes.get('Principled BSDF');bsdf.inputs['Base Color'].default_value=(0.13,0.18,0.20,1);bsdf.inputs['Roughness'].default_value=0.24;floor.data.materials.append(mat)
    for x in (-0.73,0.73):
        bpy.ops.mesh.primitive_uv_sphere_add(segments=40,ring_count=24,radius=0.63,location=(x,0,0.63));obj=bpy.context.object;obj.name='Curved light witness';[setattr(p,'use_smooth',True) for p in obj.data.polygons]
    area('Canopy',(-2,-1,3),270,(0.42,0.70,1.0));area('Practical',(1.8,-0.4,2.0),230,(1.0,0.33,0.09))
    bpy.ops.object.camera_add(location=(1.6,-6.2,2.3));cam=bpy.context.object;cam.name='Fixed camera';cam.data.lens=47;aim(cam,(0,0,0.61));scene.camera=cam
    scene.use_nodes=True;tree=scene.node_tree;tree.nodes.clear();rl=tree.nodes.new('CompositorNodeRLayers');fo=tree.nodes.new('CompositorNodeOutputFile');fo.base_path=str(out);fo.format.file_format='OPEN_EXR';fo.format.color_depth='32';fo.format.color_mode='RGB';fo.file_slots.clear()
    def save(name,socket):
        slot=fo.file_slots.new(name);tree.links.new(socket,slot)
    def add(a,b):
        n=tree.nodes.new('CompositorNodeMixRGB');n.blend_type='ADD';n.inputs[0].default_value=1;n.use_clamp=False;tree.links.new(a,n.inputs[1]);tree.links.new(b,n.inputs[2]);return n.outputs[0]
    c,p,w=[rl.outputs['Combined_'+g] for g in groups];without=add(c,w);total=add(without,p)
    for name,socket in [('beauty',rl.outputs['Image']),('canopy',c),('practical',p),('sky',w),('sum',total),('without-practical',without)]:save(name,socket)
    composite=tree.nodes.new('CompositorNodeComposite');tree.links.new(rl.outputs['Image'],composite.inputs[0]);bpy.ops.render.render()
    def load(name):
        src=out/(name+'0001.exr');dest=out/(name+'.exr');src.rename(dest);im=bpy.data.images.load(str(dest),check_existing=False);a=np.empty(len(im.pixels),dtype=np.float32);im.pixels.foreach_get(a);return a.reshape(im.size[1],im.size[0],4)[:,:,:3].copy()
    channels={n:load(n) for n in ('beauty','canopy','practical','sky','sum','without-practical')};beauty=channels['beauty'];diff=beauty-channels['without-practical'];half=beauty.shape[1]//2
    rmse=lambda x:float(np.sqrt(np.mean(np.square(x,dtype=np.float64))))
    metrics={'blender':bpy.app.version_string,'groups':groups,'size':[int(beauty.shape[1]),int(beauty.shape[0])],'all_groups_rmse':rmse(beauty-channels['sum']),'without_practical_rmse':rmse(diff),'muted_lamp_left_mean_delta':float(diff[:,:half,:].mean()),'muted_lamp_right_mean_delta':float(diff[:,half:,:].mean()),'direct_sum_rmse':rmse(beauty-channels['canopy']-channels['practical']-channels['sky'])}
    assert np.isfinite(beauty).all() and metrics['all_groups_rmse']<0.0005 and metrics['without_practical_rmse']>0.012,metrics
    (out/'light-group-checks.json').write_text(json.dumps(metrics,indent=2)+'\n');print(json.dumps(metrics))

if __name__=='__main__':
    argv=sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else sys.argv[1:]
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('new_output',type=Path,help='A new folder; existing output is never overwritten.');dest=ap.parse_args(argv).new_output.expanduser().resolve();dest.mkdir(parents=True,exist_ok=False);render(dest)
