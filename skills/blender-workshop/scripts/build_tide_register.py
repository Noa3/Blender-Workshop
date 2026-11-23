"""Build an original harbor instrument in a fresh Blender 4.5 background process."""
import argparse
import math
from pathlib import Path
import sys

import bpy
from mathutils import Vector

CX, CY, PIN_Z = -.78, .03, .348
POSES = [(1, 0), (7, -43), (10, -59), (14, -52), (17, -52), (19, -45), (25, 0),
         (31, 43), (34, 59), (38, 52), (41, 52), (43, 45), (49, 0)]


def rgb(code):
    def linear(n):
        v = int(n, 16) / 255
        return v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4
    return (*[linear(code[i:i+2]) for i in (0, 2, 4)], 1.)


def material(name, code, metal=0., rough=.42):
    m = bpy.data.materials.new(name)
    m.diffuse_color = rgb(code)
    m.use_nodes = True
    b = m.node_tree.nodes.get('Principled BSDF')
    b.inputs['Base Color'].default_value = m.diffuse_color
    b.inputs['Metallic'].default_value = metal
    b.inputs['Roughness'].default_value = rough
    return m


def group(scene, name):
    col = bpy.data.collections.new(name)
    scene.collection.children.link(col)
    return col


def put(o, col, name, mat=None):
    o.name = name
    for previous in list(o.users_collection):
        previous.objects.unlink(o)
    col.objects.link(o)
    if mat:
        o.data.materials.append(mat)
    return o


def soften(o, width):
    if width:
        b = o.modifiers.new('Edge highlight', 'BEVEL'); b.width = width; b.segments = 3
        n = o.modifiers.new('Face normals', 'WEIGHTED_NORMAL'); n.keep_sharp = True
    return o


def box(col, name, loc, dims, mat, bevel=0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = put(bpy.context.object, col, name, mat)
    for v in o.data.vertices:
        v.co = (v.co.x*dims[0], v.co.y*dims[1], v.co.z*dims[2])
    o.data.update()
    return soften(o, bevel)


def disc(col, name, x, y, z, radius, depth, mat, bevel=0):
    bpy.ops.mesh.primitive_cylinder_add(vertices=96, radius=radius, depth=depth, location=(x,y,z))
    o = put(bpy.context.object, col, name, mat)
    for p in o.data.polygons:
        p.use_smooth = len(p.vertices) == 4
    return soften(o, bevel)


def ring(col, name, x, y, z, radius, thickness, mat):
    bpy.ops.mesh.primitive_torus_add(major_segments=128, minor_segments=12, major_radius=radius, minor_radius=thickness, location=(x,y,z))
    o = put(bpy.context.object, col, name, mat)
    for p in o.data.polygons: p.use_smooth = True
    return o


def text(col, body, x, y, z, size, mat, align='LEFT', spacing=1.05):
    d = bpy.data.curves.new(body, 'FONT'); d.body = body; d.align_x = align; d.align_y = 'CENTER'
    d.size = size; d.space_character = spacing; d.resolution_u = 5
    o = bpy.data.objects.new('Type | '+body, d); o.location = (x,y,z)
    return put(o, col, o.name, mat)


def needle_shape(col, mat):
    # Counterclockwise blade outline, with a single point for a measurable tip.
    outline = [(-.068,-.255),(.068,-.255),(.082,.025),(.062,.59),(.045,.745),(0,.884),(-.045,.745),(-.062,.59),(-.082,.025)]
    count = len(outline)
    vertices = [(x,y,z) for z in (0,.025) for x,y in outline]
    faces = [tuple(reversed(range(count))),tuple(range(count,2*count))]
    faces += [(i,(i+1)%count,(i+1)%count+count,i+count) for i in range(count)]
    me = bpy.data.meshes.new('Needle blade mesh'); me.from_pydata(vertices, [], faces); me.update()
    ob = put(bpy.data.objects.new('Sweep needle', me), col, 'Sweep needle', mat)
    ob.location = (CX,CY,PIN_Z)
    return ob


def bake_print(ob, scene):
    """Bake a flat UV coupon, then use the same print coordinates on the moving face."""
    scene.render.engine = 'CYCLES'
    scene.cycles.device = 'CPU'; scene.cycles.samples = 1
    scene.render.threads_mode = 'FIXED'; scene.render.threads = 8
    bpy.ops.mesh.primitive_plane_add(size=2)
    coupon = bpy.context.object; mesh = coupon.data
    source = material('Print master | editable stripe separations', 'bd3f2a')
    source.use_fake_user = True; mesh.materials.append(source)
    nodes = source.node_tree.nodes; link = source.node_tree.links.new
    bs = nodes.get('Principled BSDF'); output = nodes.get('Material Output')
    bs.location = (350,120); output.location = (680,120)
    tex = nodes.new('ShaderNodeTexCoord'); tex.location = (-650,100)
    sep = nodes.new('ShaderNodeSeparateXYZ'); sep.location = (-440,100)
    link(tex.outputs['UV'], sep.inputs[0]); ramps = []
    for channel, base, band, y in [('Base Color',rgb('bd3f2a'),rgb('f1e1bd'),200),
                                   ('Roughness',(.28,.28,.28,1),(.70,.70,.70,1),-100)]:
        ramp = nodes.new('ShaderNodeValToRGB'); ramp.label = channel + ' separation'; ramp.location = (-180,y)
        r = ramp.color_ramp; r.interpolation = 'CONSTANT'
        r.elements[0].color = base; r.elements[1].position = .80; r.elements[1].color = base
        r.elements.new(.72).color = band
        link(sep.outputs['Y'], ramp.inputs[0]); link(ramp.outputs['Color'], bs.inputs[channel]); ramps.append(ramp)
    emission = nodes.new('ShaderNodeEmission'); emission.location = (350,-160)
    link(emission.outputs[0], output.inputs['Surface'])
    images = []
    for channel, ramp, space in zip(('Base Color','Roughness'),ramps,('sRGB','Non-Color')):
        img = bpy.data.images.new('Needle | '+channel, width=256, height=256, alpha=False, is_data=space=='Non-Color')
        img.colorspace_settings.name = space; img.file_format = 'PNG'
        dest = nodes.new('ShaderNodeTexImage'); dest.image = img; dest.label = channel + ' bake target'
        for node in nodes: node.select = False
        dest.select = True; nodes.active = dest
        link(ramp.outputs['Color'], emission.inputs['Color'])
        if bpy.ops.object.bake(type='EMIT', margin=8, use_clear=True) != {'FINISHED'}:
            raise RuntimeError('Cycles did not finish the '+channel+' separation')
        img.pack()
        # Name the packed bytes after baking. Setting a path first can trigger a disk lookup.
        png_path = '//textures/needle-' + channel.lower().replace(' ', '-') + '.png'
        img.filepath_raw = png_path
        img.packed_files[0].filepath = png_path
        images.append(img); nodes.remove(dest)
    nodes.remove(emission); link(bs.outputs[0],output.inputs['Surface'])
    bpy.data.objects.remove(coupon,do_unlink=True); bpy.data.meshes.remove(mesh)

    uv = ob.data.uv_layers.new(name='Blade print')
    for loop in ob.data.loops:
        p = ob.data.vertices[loop.vertex_index].co
        uv.data[loop.index].uv = (p.x/.20+.50, (p.y+.28)/1.20)
    finish = material('Needle face | baked witness band','bd3f2a')
    ob.data.materials.append(finish)
    max(ob.data.polygons,key=lambda face:face.normal.z).material_index = len(ob.data.materials)-1
    nodes = finish.node_tree.nodes; link = finish.node_tree.links.new
    uv_node = nodes.new('ShaderNodeUVMap'); uv_node.uv_map = uv.name; uv_node.location = (-580,50)
    bs = nodes.get('Principled BSDF')
    for channel,img,y in zip(('Base Color','Roughness'),images,(220,-100)):
        n=nodes.new('ShaderNodeTexImage'); n.image=img; n.label=channel; n.location=(-340,y)
        link(uv_node.outputs['UV'],n.inputs['Vector']); link(n.outputs['Color'],bs.inputs[channel])


def key_needle(ob, scene):
    for frame, degrees in POSES:
        ob.rotation_euler.z = math.radians(degrees)
        ob.keyframe_insert(data_path='rotation_euler', index=2, frame=frame, group='Fixed spindle')
    ad = ob.animation_data; ad.action.name = 'Sweep test | overshoot, settle, return'
    bag = ad.action.layers[0].strips[0].channelbag(ad.action_slot)
    curve = next(c for c in bag.fcurves if c.data_path=='rotation_euler' and c.array_index==2)
    for k in curve.keyframe_points:
        k.interpolation = 'BEZIER'; k.handle_left_type = k.handle_right_type = 'AUTO_CLAMPED'
    # Same tangent on either side of the boundary: closure is a pose, not a halt.
    for key in (curve.keyframe_points[0],curve.keyframe_points[-1]):
        f, a = key.co; key.handle_left_type = key.handle_right_type = 'FREE'
        key.handle_left = (f-2, a+math.radians(15)); key.handle_right = (f+2, a-math.radians(15))
    curve.update()
    for f, word in ((1,'Crossing'),(10,'High overshoot'),(14,'Seat / high'),(25,'Crossing back'),(34,'Low overshoot'),(38,'Seat / low'),(49,'Closure: do not export')):
        scene.timeline_markers.new(word, frame=f)


def build(path):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    s=bpy.context.scene; s.name='Tide Register | calibration sweep'
    case=group(s,'01 | Housing'); face=group(s,'02 | Dial and print'); motion=group(s,'03 | Animated needle'); stage=group(s,'04 | Studio')
    petrol=material('Kiln enamel | deep teal','235052',.32,.31); edge=material('Back shell | graphite','132c30',.55,.29)
    brass=material('Machined brass','c6a568',.83,.29); patina=material('Dark brass recess','796447',.63,.4)
    paper=material('Dial | warm ceramic','e6d8ae',0,.49); ink=material('Printed markings | blue black','16363b',0,.55)
    red=material('Signal vermilion','bd3f2a',0,.38); cream=material('Lettering | pale ivory','f2e3c4',0,.44)
    plate=material('Legend plate | midnight green','102e32',.3,.36); table=material('Slate workbench','172b30',0,.68)
    box(stage,'Work surface',(0,0,-.34),(200,200,.18),table)
    box(case,'Steel back shell',(0,0,-.12),(4.30,2.65,.24),edge,.11)
    box(case,'Bronze lip',(0,0,-.023),(4.23,2.57,.15),patina,.065)
    box(case,'Enameled faceplate',(0,0,.06),(4.20,2.54,.19),petrol,.085)
    for x in (-1.94,1.94):
        for y in (-1.10,1.10):
            disc(case,'Slotted case screw',x,y,.159,.049,.025,brass,.006)
            cut=box(case,'Dark screw slot',(x,y,.174),(.059,.011,.003),patina,.002); cut.rotation_euler.z=.64*x+.25*y
    disc(face,'Dial surround',CX,CY,.18,1.056,.105,edge,.025)
    disc(face,'Bezel bed',CX,CY,.222,1.018,.068,patina,.015)
    disc(face,'Ivory scale',CX,CY,.261,.974,.037,paper,.012)
    ring(face,'Rolled bezel',CX,CY,.279,.993,.028,brass)
    ring(face,'Inner bezel shadow',CX,CY,.279,.958,.007,patina)
    for i in range(61):
        angle=math.radians(-65+i*130/60); major=i%10==0; middle=i%5==0
        length=.116 if major else (.083 if middle else .052)
        radius=.913-length/2
        tick=box(face,'Scale | '+str(i),(CX+radius*math.sin(angle),CY+radius*math.cos(angle),.282),(.017 if major else .009,length,.004),red if i in (0,60) else ink)
        tick.rotation_euler.z=-angle
        if major:
            text(face,str(i//10),CX+.724*math.sin(angle),CY+.724*math.cos(angle),.286,.096,ink,'CENTER')
    text(face,'TIDE  LEVEL',CX,CY-.39,.286,.131,ink,'CENTER',1.16)
    text(face,'M E T R E S',CX,CY-.52,.286,.058,patina,'CENTER')
    box(face,'Dial rule',(CX,CY-.619,.284),(.32,.009,.004),patina)
    text(face,'L Q   /   0 4',CX,CY-.723,.286,.059,ink,'CENTER')
    box(case,'Legend surround',(1.09,.018,.165),(1.48,1.89,.054),patina,.026)
    box(case,'Legend insert',(1.09,.018,.194),(1.437,1.847,.027),plate,.01)
    left=.50; z=.212
    text(case,'PORT  INSTRUMENTS',left,.745,z,.087,cream,spacing=1.13)
    box(case,'Upper brass rule',(1.075,.62,z),(1.15,.016,.005),brass)
    text(case,'TIDE',left,.375,z,.31,cream,spacing=1.07)
    text(case,'REGISTER',left,.10,z,.215,cream,spacing=1.06)
    text(case,'CALIBRATION   /   04',left,-.118,z,.083,brass)
    box(case,'Legend fine rule',(1.075,-.276,z),(1.15,.007,.005),patina)
    for y,word,number in [(-.435,'STATION','NORTH PIER'),(-.625,'SERIES','LQ   /   27')]:
        text(case,word,left,y,z,.060,cream); text(case,number,1.68,y,z,.080,cream,'RIGHT')
    color=material('Needle | painted enamel','bd3f2a',0,.39)
    needle=needle_shape(motion,color); bake_print(needle,s); key_needle(needle,s)
    ref=bpy.data.objects.new('Spindle reference',None); put(ref,motion,ref.name); ref.empty_display_type='PLAIN_AXES'; ref.empty_display_size=.05; ref.location=(CX,CY,PIN_Z)
    disc(motion,'Pivot collar',CX,CY,.405,.127,.052,patina,.012)
    disc(motion,'Pivot cap',CX,CY,.435,.092,.037,brass,.014)
    disc(motion,'Bearing jewel',CX,CY,.459,.030,.017,edge,.006)
    def area(name,loc,power,sx,sy):
        d=bpy.data.lights.new(name,'AREA');d.energy=power;d.shape='RECTANGLE';d.size=sx;d.size_y=sy
        o=put(bpy.data.objects.new(name,d),stage,name);o.location=loc;o.rotation_euler=(-o.location).to_track_quat('-Z','Y').to_euler()
    area('Softbox | key',(-3.4,3.15,5),365,4.5,3.1); area('Card | edge',(2.8,1.2,3.4),165,1.3,3.6);area('Front fill',(.5,-3.4,3.1),88,3.2,2)
    world=bpy.data.worlds.new('Overcast studio'); s.world=world; world.use_nodes=True; world.node_tree.nodes['Background'].inputs['Color'].default_value=(.34,.39,.43,1);world.node_tree.nodes['Background'].inputs['Strength'].default_value=.29
    camera=bpy.data.cameras.new('Inspection lens'); cam=put(bpy.data.objects.new('Camera | workbench',camera),stage,'Camera | workbench');s.camera=cam
    cam.location=(0,-1.02,8);cam.rotation_euler=(Vector((0,0,0))-cam.location).to_track_quat('-Z','Y').to_euler();camera.type='ORTHO';camera.ortho_scale=4.86
    s.render.engine='CYCLES';s.cycles.samples=20;s.cycles.use_denoising=True;s.cycles.use_animated_seed=False;s.cycles.device='CPU'
    s.render.threads_mode='FIXED';s.render.threads=8;s.view_settings.view_transform='AgX';s.render.image_settings.file_format='PNG';s.render.image_settings.color_mode='RGB'
    s.render.resolution_x,s.render.resolution_y,s.render.resolution_percentage=800,496,100;s.frame_start,s.frame_end,s.render.fps=1,48,24;s.frame_set(10)
    s.render.use_stamp=False;s.render.use_stamp_filename=False;s.render.filepath='//frames/tide-';s.render.film_transparent=False
    for other in list(bpy.context.selected_objects): other.select_set(False)
    needle.select_set(True);bpy.context.view_layer.objects.active=needle
    for screen in bpy.data.screens:
        for a in screen.areas:
            if a.type=='VIEW_3D':
                space=a.spaces.active;space.region_3d.view_perspective='CAMERA';space.overlay.show_overlays=False;space.shading.color_type='MATERIAL'
    bpy.context.preferences.filepaths.save_version=0
    bpy.ops.wm.save_as_mainfile(filepath=str(path),compress=True,relative_remap=False)


def main(argv):
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('file',type=Path);args=parser.parse_args(argv);p=args.file.resolve()
    if not bpy.app.background or bpy.data.filepath: parser.exit(2,'Use a fresh background process without an open scene.\n')
    if p.suffix!='.blend' or p.exists() or not p.parent.is_dir(): parser.exit(2,'Choose a new .blend file in an existing directory.\n')
    build(p)


if __name__=='__main__':
    main(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else sys.argv[1:])
