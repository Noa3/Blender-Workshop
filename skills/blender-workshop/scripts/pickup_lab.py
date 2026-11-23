"""Build or inspect a native Child Of pickup study using a fresh Blender 4.5.9 Python process."""
import argparse
import json
from pathlib import Path
import sys


def build(bpy, directory, render):
    from mathutils import Vector

    directory.mkdir(parents=True, exist_ok=False)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.name = "Transit | single-parent pickup"
    scene.unit_settings.system = "METRIC"
    scene.frame_start, scene.frame_end, scene.render.fps = 1, 18, 12
    scene.world = bpy.data.worlds.new("Slate studio")
    scene.world.color = (0.21, 0.24, 0.27)

    def mat(name, color, metal=0):
        m = bpy.data.materials.new(name)
        m.use_nodes = True
        m.diffuse_color = (*color, 1)
        bsdf = m.node_tree.nodes.get("Principled BSDF")
        bsdf.inputs["Base Color"].default_value = (*color, 1)
        bsdf.inputs["Metallic"].default_value = metal
        bsdf.inputs["Roughness"].default_value = .32
        return m

    slate = mat("Slate | frame", (.052, .106, .121), .44)
    mint = mat("Enamel | carrier", (.22, .63, .56), .28)
    copper = mat("Orange | token", (.93, .25, .045), .38)
    ground = mat("Dove | table", (.36, .41, .40))

    def mesh(name, location, dimensions, material, *, parent=None, cylinder=False):
        if cylinder:
            bpy.ops.mesh.primitive_cylinder_add(vertices=48, location=location)
        else:
            bpy.ops.mesh.primitive_cube_add(location=location)
        obj = bpy.context.object
        obj.name = name
        obj.dimensions = dimensions
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        obj.data.materials.append(material)
        edge = obj.modifiers.new("Machined edge", "BEVEL")
        edge.width = min(.045, min(dimensions) * .18)
        edge.segments = 3
        obj.modifiers.new("Face normals", "WEIGHTED_NORMAL")
        if parent:
            obj.parent = parent
        return obj

    mesh("Studio table", (0, 0, -.14), (22, 22, .25), ground)
    for side, tag in ((-1.4, "Pickup"), (1.4, "Drop")):
        mesh(tag + " | base", (side, 0, .13), (.98, .98, .26), slate)
        mesh(tag + " | lip", (side, 0, .293), (.85, .85, .065), mint)
    mesh("Bridge | crossbar", (0, .54, 2.07), (4.35, .15, .16), slate)
    for side in (-2.04, 2.04):
        mesh("Bridge | upright", (side, .54, 1.02), (.13, .14, 2.04), slate)
    carrier = bpy.data.objects.new("Carrier", None)
    scene.collection.objects.link(carrier)
    carrier.empty_display_type = "PLAIN_AXES"
    carrier.empty_display_size = .25
    mesh("Yoke", (0, 0, .10), (.82, .29, .14), mint, parent=carrier)
    for x in (-.358, .358):
        mesh("Jaw", (x, 0, -.105), (.07, .28, .34), slate, parent=carrier)
    token = mesh("Token", (-1.4, 0, .475), (.63, .63, .30), copper, cylinder=True)
    bpy.context.preferences.edit.keyframe_new_interpolation_type = "LINEAR"
    for frame, x, z in ((1, -1.4, 1.43), (4, -1.4, .76), (5, -1.4, .76), (7, -1.4, 1.29),
                        (9, 1.4, 1.29), (11, 1.4, .76), (12, 1.4, .76), (15, 1.4, 1.37), (18, 0, 1.37)):
        carrier.location = (x, 0, z)
        carrier.keyframe_insert("location", frame=frame)
    scene.frame_set(5)
    switch = token.constraints.new("CHILD_OF")
    switch.name = "Grip | keep world pose on pickup"
    switch.target = carrier
    switch.inverse_matrix = carrier.matrix_world.inverted()
    bpy.context.preferences.edit.keyframe_new_interpolation_type = "CONSTANT"
    for frame, value in ((1, 0), (4, 0), (5, 1), (11, 1), (12, 0), (18, 0)):
        switch.influence = value
        switch.keyframe_insert("influence", frame=frame)
    # When the grip lets go, store the evaluated world pose in this unparented token's local track.
    for frame, x in ((1, -1.4), (11, -1.4), (12, 1.4), (18, 1.4)):
        token.location = (x, 0, .475)
        token.keyframe_insert("location", frame=frame)

    bpy.ops.object.camera_add(location=(3.1, -8.8, 3.45))
    cam = bpy.context.object
    cam.name = "Camera | inspection"
    cam.rotation_euler = (Vector((0, 0, .9)) - cam.location).to_track_quat('-Z', 'Y').to_euler()
    cam.data.type, cam.data.ortho_scale = "ORTHO", 5.25
    scene.camera = cam
    for pos, size, power in (((-3, -4, 6), 4.5, 680), ((3, 1, 4.8), 3.0, 490)):
        bpy.ops.object.light_add(type="AREA", location=pos)
        light = bpy.context.object
        light.data.energy, light.data.shape, light.data.size = power, "DISK", size
        light.rotation_euler = (Vector((0, 0, .7)) - light.location).to_track_quat('-Z', 'Y').to_euler()
    scene.render.engine = "CYCLES"
    scene.render.use_stamp_filename = False
    scene.cycles.samples, scene.cycles.use_denoising = 12, True
    scene.render.resolution_x, scene.render.resolution_y, scene.render.resolution_percentage = 480, 288, 100
    for f, marker in ((4, "BEFORE"), (5, "GRIP"), (8, "CARRY"), (11, "ARRIVE"), (12, "RELEASE"), (18, "PARK")):
        scene.timeline_markers.new(marker, frame=f)
    scene.frame_set(8)
    scene.render.filepath = "//pickup-preview.png"
    bpy.context.view_layer.objects.active = token
    bpy.ops.wm.save_as_mainfile(filepath=str(directory / "pickup.blend"))
    if render:
        for f in (4, 8, 12, 18):
            scene.frame_set(f)
            scene.render.filepath = str(directory / f"frame-{f:02}.png")
            bpy.ops.render.render(write_still=True)


def observe(bpy, directory):
    bpy.ops.wm.open_mainfile(filepath=str(directory / "pickup.blend"), load_ui=False, use_scripts=False)
    scene = bpy.context.scene
    token, carrier = (scene.objects[n] for n in ("Token", "Carrier"))
    switch = next((c for c in token.constraints if c.type == "CHILD_OF" and c.target == carrier), None)
    if switch is None:
        raise ValueError("Missing Child Of target on Token")
    marks = {}
    for f in range(1, 19):
        scene.frame_set(f)
        deps = bpy.context.evaluated_depsgraph_get()
        marks[f] = tuple(o.evaluated_get(deps).matrix_world.translation.copy() for o in (token, carrier))
    def dist(fr, to, obj=0):
        return (marks[fr][obj] - marks[to][obj]).length
    offsets = [marks[f][0] - marks[f][1] for f in range(5, 12)]
    rec = {"blender": bpy.app.version_string, "frames_evaluated": len(marks),
           "pickup_jump_m": dist(4, 5), "carried_travel_m": dist(5, 11),
           "carried_relative_drift_m": max((v - offsets[0]).length for v in offsets),
           "release_jump_m": dist(11, 12), "released_drift_m": max(dist(12, f) for f in range(12, 19)),
           "carrier_travel_after_release_m": dist(12, 18, 1)}
    for key in ("pickup_jump_m", "carried_relative_drift_m", "release_jump_m", "released_drift_m"):
        if rec[key] > 1e-4:
            raise ValueError(f"{key} failed: {rec[key]}")
    if rec["carried_travel_m"] < 2.5 or rec["carrier_travel_after_release_m"] < .8:
        raise ValueError("The token or the released carrier did not travel")
    return rec


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    verbs = parser.add_subparsers(dest="verb", required=True)
    make = verbs.add_parser("build", help="create a new output folder")
    make.add_argument("directory", type=Path)
    make.add_argument("--render", action="store_true", help="also render four camera poses")
    check = verbs.add_parser("check", help="measure the saved scene in a fresh background process")
    check.add_argument("directory", type=Path)
    args = parser.parse_args(argv)
    import bpy
    if not bpy.app.background or bpy.data.filepath:
        parser.exit(2, "Use a fresh background process; do not pass a user scene.\n")
    out = args.directory.resolve()
    if args.verb == "build":
        if out.exists():
            parser.exit(2, "Output directory already exists; choose a new one.\n")
        build(bpy, out, args.render)
    elif not (out / "pickup.blend").is_file():
        parser.exit(2, "No pickup.blend in the supplied directory.\n")
    else:
        print(json.dumps(observe(bpy, out), sort_keys=True))


if __name__ == "__main__":
    main(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:])
