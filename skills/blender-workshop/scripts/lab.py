"""Standalone Blender 4.5 LTS lab. Run in a fresh background process only."""

import argparse
import json
import math
from pathlib import Path
import sys

import bpy
from mathutils import Vector

TAU = math.tau


def node(tree, kind, x, y=0, label=None):
    n = tree.nodes.new(kind)
    n.location = (x, y)
    if label:
        n.label = label
    return n


def mesh(name, verts, faces, material=None):
    data = bpy.data.meshes.new(name)
    data.from_pydata(verts, [], faces)
    data.update()
    obj = bpy.data.objects.new(name, data)
    bpy.context.collection.objects.link(obj)
    if material:
        data.materials.append(material)
    return obj


def principled(name, color, metallic, roughness, spread=0):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1)
    m.use_nodes = True
    t = m.node_tree
    p = t.nodes.get("Principled BSDF")
    p.inputs["Base Color"].default_value = (*color, 1)
    p.inputs["Metallic"].default_value = metallic
    p.inputs["Roughness"].default_value = roughness
    if spread:
        noise = node(t, "ShaderNodeTexNoise", -540, -110, "Fine grain")
        noise.inputs["Scale"].default_value = 115
        remap = node(t, "ShaderNodeMapRange", -290, -110, "Vary roughness only")
        remap.inputs["To Min"].default_value = roughness - spread
        remap.inputs["To Max"].default_value = roughness + spread
        t.links.new(noise.outputs["Fac"], remap.inputs["Value"])
        t.links.new(remap.outputs["Result"], p.inputs["Roughness"])
    return m


def flat(name, color):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1)
    m.use_nodes = True
    t = m.node_tree
    t.nodes.clear()
    e = node(t, "ShaderNodeEmission", 0)
    e.inputs["Color"].default_value = (*color, 1)
    t.links.new(
        e.outputs[0], node(t, "ShaderNodeOutputMaterial", 210).inputs["Surface"]
    )
    return m


def bevel(obj, width, segments=3):
    mod = obj.modifiers.new("Edge highlight", "BEVEL")
    mod.width, mod.segments = width, segments
    mod.limit_method = "ANGLE"
    mod.harden_normals = True


def disk(name, r, z, depth, mat, edge=0.025):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=96, radius=r, depth=depth, location=(0, 0, z)
    )
    obj = bpy.context.object
    obj.name = name
    for p in obj.data.polygons:
        p.use_smooth = abs(p.normal.z) < 0.1
    obj.data.materials.append(mat)
    if edge:
        bevel(obj, edge)
    return obj


def ring(name, radius, tube, loc, mat, upright=False):
    bpy.ops.mesh.primitive_torus_add(
        major_radius=radius,
        minor_radius=tube,
        major_segments=112,
        minor_segments=12,
        location=loc,
    )
    obj = bpy.context.object
    obj.name = name
    if upright:
        obj.rotation_euler.x = math.pi / 2
    for p in obj.data.polygons:
        p.use_smooth = True
    obj.data.materials.append(mat)
    return obj


def look(obj, target):
    obj.rotation_euler = (
        (Vector(target) - obj.location).to_track_quat("-Z", "Y").to_euler()
    )


def lamp(name, loc, watts, color, size, target=(0, 0, 0.3), sun=False):
    data = bpy.data.lights.new(name, "SUN" if sun else "AREA")
    obj = bpy.data.objects.new(name, data)
    bpy.context.collection.objects.link(obj)
    obj.location = loc
    look(obj, target)
    data.energy, data.color = watts, color
    if not sun:
        data.shape = "DISK"
        data.size = size
    return obj


def camera(loc, target, scale):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    look(cam, target)
    cam.data.type, cam.data.ortho_scale = "ORTHO", scale
    bpy.context.scene.camera = cam


def studio():
    floor = principled("Slate | Stage", (0.032, 0.055, 0.075), 0.07, 0.50)
    bpy.ops.mesh.primitive_plane_add(size=200, location=(0, 0, -0.018))
    bpy.context.object.name = "Sweep | Floor"
    bpy.context.object.data.materials.append(floor)
    lamp("Softbox | warm", (-3.8, -3.3, 6), 650, (1, 0.83, 0.65), 4.2)
    lamp("Rim | Cool", (2.1, 3.0, 4.3), 760, (0.58, 0.80, 1), 3.2)
    lamp("Reflection | Front", (4, -3, 2), 175, (0.78, 0.89, 1), 2.3)


def dial():
    studio()
    brass = principled("Brass | Satin finish", (0.68, 0.35, 0.125), 1, 0.30, 0.13)
    enamel = principled("Enamel | Teal", (0.012, 0.095, 0.105), 0.16, 0.24)
    rubber = principled("Gasket | Dark", (0.021, 0.03, 0.035), 0, 0.54)
    index = principled("Index | Vermilion", (0.72, 0.073, 0.033), 0.05, 0.30)
    disk("01 | Base", 1.45, 0.105, 0.21, rubber, 0.065)
    disk("02 | Bezel", 1.30, 0.225, 0.15, brass, 0.035)
    # Two radii per period produce actual ridges, not a painted normal effect.
    n = 144
    verts = []
    for z, radius in ((0.28, 1.13), (0.32, 1.19), (0.59, 1.19), (0.63, 1.13)):
        for i in range(n):
            a = TAU * i / n
            r = radius - (0.055 if i % 2 else 0)
            verts.append((r * math.cos(a), r * math.sin(a), z))
    faces = [
        (k * n + i, k * n + (i + 1) % n, (k + 1) * n + (i + 1) % n, (k + 1) * n + i)
        for k in range(3)
        for i in range(n)
    ]
    faces.extend((tuple(reversed(range(n))), tuple(range(3 * n, 4 * n))))
    shell = mesh("03 | Knurling", verts, faces, brass)
    bevel(shell, 0.006, 2)
    disk("04 | Dial face", 1.115, 0.635, 0.105, enamel)
    ring("05 | Brass rim", 1.07, 0.018, (0, 0, 0.688), brass)
    ring("06 | Chapter ring", 0.81, 0.009, (0, 0, 0.688), brass)
    verts, faces = [], []
    for i in range(48):
        a = TAU * i / 48
        half = 0.017 if i % 4 == 0 else 0.009
        r0 = 0.855 if i % 4 == 0 else 0.934
        j = len(verts)
        for r, w in ((r0, -half), (1.021, -half), (1.021, half), (r0, half)):
            verts.append(
                (
                    r * math.cos(a) - w * math.sin(a),
                    r * math.sin(a) + w * math.cos(a),
                    0.690,
                )
            )
        faces.append(tuple(range(j, j + 4)))
    mesh("07 | 48 graduations", verts, faces, brass)
    needle = mesh(
        "08 | Pointer",
        [
            (-0.055, -0.24, 0.715),
            (0.055, -0.24, 0.715),
            (0.014, 0.78, 0.715),
            (-0.014, 0.78, 0.715),
        ],
        [(0, 1, 2, 3)],
        index,
    )
    needle.rotation_euler.z = -0.76
    disk("09 | Hub", 0.10, 0.723, 0.03, brass, 0.012)
    camera((3, -5, 4.4), (0, 0, 0.30), 3.95)
    return {"ridge_periods": n // 2, "scale_divisions": len(faces)}


def evaluated_faces(obj):
    bpy.context.view_layer.update()
    ev = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())
    data = ev.to_mesh()
    try:
        return len(data.polygons)
    finally:
        ev.to_mesh_clear()


def rosette(out):
    studio()
    jade = principled("Jade | Petals", (0.045, 0.37, 0.29), 0.35, 0.26)
    gold = principled("Gold | Center", (0.70, 0.35, 0.095), 0.85, 0.30)
    disk(
        "Base",
        1.63,
        0.075,
        0.15,
        principled("Ceramic | Base", (0.035, 0.072, 0.080), 0.18, 0.31),
    )
    ring("Rim", 1.55, 0.015, (0, 0, 0.155), gold)
    obj = mesh("Rosette | Count on modifier", [], [])
    obj.location.z = 0.285
    g = bpy.data.node_groups.new("Radial fan | Editable", "GeometryNodeTree")

    def sock(name, direction, typ):
        return g.interface.new_socket(name=name, in_out=direction, socket_type=typ)

    sock("Geometry", "OUTPUT", "NodeSocketGeometry")
    sock("Geometry", "INPUT", "NodeSocketGeometry")
    count = sock("Count", "INPUT", "NodeSocketInt")
    count.default_value = 24
    count.min_value, count.max_value = 3, 96
    radius = sock("Radius", "INPUT", "NodeSocketFloat")
    radius.default_value = 0.88
    radius.min_value = 0.01
    real = sock("Realize for mesh output", "INPUT", "NodeSocketBool")
    real.default_value = False
    gi = node(g, "NodeGroupInput", -750, 300)
    go = node(g, "NodeGroupOutput", 790, 200)
    circle = node(g, "GeometryNodeMeshCircle", -490, 300)
    inst = node(g, "GeometryNodeInstanceOnPoints", 160, 180)
    proto = node(g, "GeometryNodeMeshUVSphere", -740, -10)
    proto.inputs["Segments"].default_value = 24
    proto.inputs["Rings"].default_value = 12
    smooth = node(g, "GeometryNodeSetShadeSmooth", -500, -10)
    surf = node(g, "GeometryNodeSetMaterial", -270, -10)
    surf.inputs["Material"].default_value = jade
    pos = node(g, "GeometryNodeInputPosition", -500, -260)
    align = node(g, "FunctionNodeAlignRotationToVector", -265, -250)
    align.axis = "X"
    inst.inputs["Scale"].default_value = (0.57, 0.122, 0.116)
    re = node(g, "GeometryNodeRealizeInstances", 390, 0)
    switch = node(g, "GeometryNodeSwitch", 590, 180)
    switch.input_type = "GEOMETRY"
    for a, ao, b, bi in (
        (gi, "Count", circle, "Vertices"),
        (gi, "Radius", circle, "Radius"),
        (circle, 0, inst, "Points"),
        (proto, 0, smooth, 0),
        (smooth, 0, surf, 0),
        (surf, 0, inst, "Instance"),
        (pos, 0, align, "Vector"),
        (align, 0, inst, "Rotation"),
        (inst, 0, re, 0),
        (inst, 0, switch, "False"),
        (re, 0, switch, "True"),
        (gi, "Realize for mesh output", switch, "Switch"),
        (switch, 0, go, "Geometry"),
    ):
        g.links.new(a.outputs[ao], b.inputs[bi])
    mod = obj.modifiers.new("Radial instances", "NODES")
    mod.node_group = g

    def set_input(socket, value):
        mod[socket.identifier] = value
        obj.update_tag()
        bpy.context.view_layer.update()

    set_input(real, True)
    counts = {}
    for amount in (12, 24):
        set_input(count, amount)
        counts[str(amount)] = evaluated_faces(obj)
    if not counts["12"] or counts["24"] != 2 * counts["12"]:
        raise RuntimeError(f"Unexpected parametric geometry: {counts}")
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    result = bpy.ops.export_scene.gltf(
        filepath=str(out / "rosette.glb"),
        export_format="GLB",
        use_selection=True,
        export_apply=True,
    )
    if "FINISHED" not in result:
        raise RuntimeError("glTF export failed")
    set_input(real, False)
    disk("Core | Jade", 0.40, 0.29, 0.22, jade, 0.07)
    ring("Inner ring", 0.33, 0.021, (0, 0, 0.389), gold)
    disk("Pollen | Gold", 0.16, 0.409, 0.065, gold)
    camera((1.1, -3, 6.5), (0, 0, 0.13), 4.05)
    return {
        "evaluated_polygons_realized": counts,
        "saved_as_instances": not bool(mod[real.identifier]),
        "export": "rosette.glb (petals only, no base)",
    }


def cel():
    m = flat("Porcelain | Cel bands", (1, 1, 1))
    t = m.node_tree
    diffuse = node(t, "ShaderNodeBsdfDiffuse", -630)
    diffuse.inputs["Color"].default_value = (1, 1, 1, 1)
    rgb = node(t, "ShaderNodeShaderToRGB", -420)
    ramp = node(t, "ShaderNodeValToRGB", -210)
    ramp.color_ramp.interpolation = "CONSTANT"
    palette = [
        (0, (0.17, 0.20, 0.31)),
        (0.26, (0.63, 0.56, 0.57)),
        (0.56, (0.97, 0.83, 0.65)),
    ]
    cr = ramp.color_ramp
    cr.elements.remove(cr.elements[1])
    cr.elements[0].color = (*palette[0][1], 1)
    for x, c in palette[1:]:
        cr.elements.new(x).color = (*c, 1)
    t.links.new(diffuse.outputs[0], rgb.inputs[0])
    t.links.new(rgb.outputs["Color"], ramp.inputs["Fac"])
    t.links.new(ramp.outputs[0], t.nodes.get("Emission").inputs["Color"])
    return m, palette


def mask():
    s = bpy.context.scene
    white, palette = cel()
    ink = flat("Ink", (0.020, 0.026, 0.047))
    red = flat("Vermilion", (0.72, 0.085, 0.083))
    amber = flat("Gold lacquer", (0.93, 0.55, 0.17))
    bg = flat("Backdrop | Night", (0.018, 0.078, 0.092))
    group = bpy.data.objects.new("Mask | Turn test", None)
    bpy.context.collection.objects.link(group)

    def width(z):
        return 0.84 + 0.19 * z

    def front(x, z):
        return -0.48 * math.sqrt(max(0.001, 1 - z * z - (x / width(z)) ** 2))

    bpy.ops.mesh.primitive_uv_sphere_add(segments=80, ring_count=48)
    head = bpy.context.object
    head.name = "Porcelain shell"
    head.parent = group
    for v in head.data.vertices:
        x, y, z = v.co
        v.co = (x * width(z), 0.48 * y, z)
    head.data.update()
    for p in head.data.polygons:
        p.use_smooth = True
    head.data.materials.append(white)

    # Paired paint strips follow the curved surface instead of lying in one plane.
    def strip(name, side, profile, mat, offset=0.015):
        verts = []
        for x, z, w in profile:
            for h in (-w, w):
                verts.append((side * x, front(x, z + h) - offset, z + h))
        faces = [
            (2 * i, 2 * i + 2, 2 * i + 3, 2 * i + 1) for i in range(len(profile) - 1)
        ]
        obj = mesh(name, verts, faces, mat)
        obj.parent = group

    for side in (-1, 1):
        sign = "L" if side < 0 else "R"
        outer = [(0.22, 0.73), (0.87, 1.42), (0.86, 0.50), (0.74, 0.24)]
        vertices = [(side * x, y, z) for y in (0.10, -0.065) for x, z in outer]
        ear = mesh(
            "Ear " + sign,
            vertices,
            [(3, 2, 1, 0), (4, 5, 6, 7)]
            + [(i, (i + 1) % 4, 4 + (i + 1) % 4, 4 + i) for i in range(4)],
            white,
        )
        ear.parent = group
        bevel(ear, 0.038)
        inner = mesh(
            "Inner ear " + sign,
            [
                (side * x, -0.115, z)
                for x, z in ((0.45, 0.76), (0.811, 1.25), (0.784, 0.65), (0.66, 0.48))
            ],
            [(0, 1, 2, 3)],
            red,
        )
        inner.parent = group
        strip(
            "Eye " + sign,
            side,
            [
                (0.09, -0.055, 0.003),
                (0.21, -0.02, 0.040),
                (0.36, 0.04, 0.073),
                (0.51, 0.14, 0.061),
                (0.66, 0.235, 0.037),
                (0.73, 0.32, 0.002),
            ],
            ink,
            0.027,
        )
        strip(
            "Gold eyeliner " + sign,
            side,
            [
                (0.24, -0.018, 0.002),
                (0.36, 0.025, 0.010),
                (0.48, 0.10, 0.007),
                (0.56, 0.164, 0.002),
            ],
            amber,
            0.039,
        )
        strip(
            "Brow " + sign,
            side,
            [
                (0.12, 0.19, 0.002),
                (0.25, 0.244, 0.043),
                (0.39, 0.31, 0.059),
                (0.53, 0.39, 0.046),
                (0.61, 0.48, 0.002),
            ],
            red,
            0.027,
        )
        strip(
            "Cheek stripe " + sign,
            side,
            [
                (0.27, -0.35, 0.002),
                (0.43, -0.27, 0.028),
                (0.56, -0.18, 0.045),
                (0.69, -0.075, 0.020),
                (0.75, -0.04, 0.002),
            ],
            red,
            0.025,
        )
        strip(
            "Fine cheek stripe " + sign,
            side,
            [
                (0.29, -0.46, 0.001),
                (0.43, -0.395, 0.018),
                (0.52, -0.33, 0.024),
                (0.62, -0.24, 0.002),
            ],
            red,
            0.027,
        )
        strip(
            "Forehead " + sign,
            side,
            [
                (0.008, 0.43, 0.005),
                (0.075, 0.53, 0.023),
                (0.145, 0.65, 0.017),
                (0.198, 0.73, 0.002),
            ],
            amber,
            0.032,
        )
    nose = mesh(
        "Nose",
        [
            (x, front(x, z) - 0.03, z)
            for x, z in ((-0.096, -0.38), (0, -0.415), (0.096, -0.38), (0, -0.52))
        ],
        [(0, 1, 2, 3)],
        ink,
    )
    nose.parent = group
    ring("Halo ring", 1.18, 0.012, (0, 0.64, 0.20), amber, True)
    plane = mesh(
        "Background",
        [(-8, 1.9, -8), (8, 1.9, -8), (8, 1.9, 8), (-8, 1.9, 8)],
        [(0, 1, 2, 3)],
        bg,
    )
    camera((0, -6, 0.26), (0, 0, 0.20), 3.55)
    lamp(
        "Cel | Directional light",
        (-4, -4, 5),
        2.5,
        (1, 1, 1),
        0,
        target=(0, 0, 0),
        sun=True,
    )
    s.frame_start, s.frame_end = 1, 25
    for frame, deg in ((1, -14), (13, 0), (25, 14)):
        group.rotation_euler.z = math.radians(deg)
        group.keyframe_insert(data_path="rotation_euler", index=2, frame=frame)
    s.frame_set(13)
    return {
        "palette_linear_rgb": [list(p[1]) for p in palette],
        "pose_degrees": {"1": -14, "13": 0, "25": 14},
        "outlines": "Drawn shapes on the surface; no Line Art modifier",
    }


def main():
    a = argparse.ArgumentParser(description=__doc__)
    a.add_argument("study", choices=("metal", "rosette", "mask"))
    a.add_argument("out", type=Path, help="New directory; existing paths are refused")
    opts = a.parse_args(
        sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]
    )
    out = opts.out.expanduser().resolve()
    if not bpy.app.background or bpy.data.filepath:
        raise SystemExit(
            "Only run in a fresh background process without a loaded file."
        )
    out.mkdir(parents=True, exist_ok=False)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 0.01
    scene.render.engine = "BLENDER_EEVEE_NEXT" if opts.study == "mask" else "CYCLES"
    scene.render.use_stamp_filename = False
    (
        scene.render.resolution_x,
        scene.render.resolution_y,
        scene.render.resolution_percentage,
    ) = 600, 500, 100
    scene.render.threads_mode = "FIXED"
    scene.render.threads = 8
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"
    scene.world = bpy.data.worlds.new("Studio | Environment")
    scene.world.use_nodes = True
    world = scene.world.node_tree.nodes.get("Background")
    world.inputs[0].default_value = (0.22, 0.27, 0.32, 1)
    world.inputs[1].default_value = 0.18
    scene.view_settings.view_transform = "Standard" if opts.study == "mask" else "AgX"
    if opts.study == "mask":
        stats = mask()
    else:
        scene.cycles.device = "CPU"
        scene.cycles.samples = 32
        scene.cycles.use_denoising = True
        stats = dial() if opts.study == "metal" else rosette(out)
    scene.render.filepath = "//" + opts.study + ".png"
    result = bpy.ops.wm.save_as_mainfile(
        filepath=str(out / (opts.study + ".blend")), compress=True
    )
    if "FINISHED" not in result:
        raise RuntimeError("Saving blend failed")
    result = bpy.ops.render.render(write_still=True)
    if "FINISHED" not in result or not (out / (opts.study + ".png")).is_file():
        raise RuntimeError("Missing still")
    if opts.study == "mask":
        for f in (1, 25):
            scene.frame_set(f)
            scene.render.filepath = f"//pose-{f:02}.png"
            bpy.ops.render.render(write_still=True)
    record = {
        "study": opts.study,
        "blender": bpy.app.version_string,
        "engine": scene.render.engine,
        "view": scene.view_settings.view_transform,
        **stats,
    }
    (out / "metrics.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(record, ensure_ascii=False))


if __name__ == "__main__":
    main()
