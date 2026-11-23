"""Noa3 · disposable Blender 4.5 emitter test, not a cached rain shot.
Run in fresh standalone bpy or blender -b -P rain_probe.py. No files required.
"""
import json
import bpy


def probe(gravity):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene=bpy.context.scene; scene.gravity.z=gravity; scene.render.fps=24
    bpy.ops.mesh.primitive_plane_add(size=2,location=(0,0,2))
    obj=bpy.context.object; bpy.ops.object.particle_system_add(); system=obj.particle_systems[0]; system.seed=17
    settings=system.settings; settings.count=24; settings.frame_start=2; settings.frame_end=3; settings.lifetime=10; settings.normal_factor=0; settings.factor_random=0; settings.display_percentage=100
    graph=bpy.context.evaluated_depsgraph_get(); samples={}
    for f in range(1,17):
        scene.frame_set(f); ev=obj.evaluated_get(graph); live=[p.location.z for p in ev.particle_systems[0].particles if p.alive_state=='ALIVE']; samples[f]=(len(live),sum(live)/len(live) if live else None)
    assert samples[1][0]==0 and samples[4][0]==24 and samples[9][0]==24 and samples[16][0]==0, samples
    return {'live_f1_f4_f9_f16':[samples[f][0] for f in (1,4,9,16)],'mean_fall_f4_to_f9_m':samples[4][1]-samples[9][1]}


if __name__=='__main__':
    if not bpy.app.background or bpy.data.filepath: raise SystemExit('Start in a fresh background process')
    normal=probe(-9.81); zero=probe(0); assert normal['mean_fall_f4_to_f9_m']>.08 and abs(zero['mean_fall_f4_to_f9_m'])<.0001
    print(json.dumps({'blender':bpy.app.version_string,'gravity':normal,'no_gravity':zero},indent=2))
