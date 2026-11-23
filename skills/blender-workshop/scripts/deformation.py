"""Isolated deformation, cloth and UV-bake exercises for Blender 4.5."""

import argparse
import json
import math
from pathlib import Path
import sys
import bpy


def grid(name, nx, ny, point):
    vs = [point(i / nx, j / ny) for j in range(ny + 1) for i in range(nx + 1)]
    faces = []
    for j in range(ny):
        for i in range(nx):
            a = j * (nx + 1) + i
            faces.append((a, a + 1, a + nx + 2, a + nx + 1))
    data = bpy.data.meshes.new(name)
    data.from_pydata(vs, [], faces)
    data.update()
    ob = bpy.data.objects.new(name, data)
    bpy.context.collection.objects.link(ob)
    return ob


def coord(ob, idx):
    bpy.context.view_layer.update()
    ev = ob.evaluated_get(bpy.context.evaluated_depsgraph_get())
    return ev.data.vertices[idx].co.copy()


def rig_test(s):
    strip = grid("Test strip", 16, 2, lambda x, y: (2 * x, (y - 0.5) * 0.31, 0))
    strip.shape_key_add(name="Basis")
    key = strip.shape_key_add(name="Arch")
    for vert, k in zip(strip.data.vertices, key.data):
        k.co.z += (
            0.15
            * math.sin(math.pi * vert.co.x / 2)
            * max(0, 1 - abs(vert.co.y) / 0.155)
        )
    rest = coord(strip, 25)
    key.value = 1
    lift = coord(strip, 25).z - rest.z
    key.value = 0
    if abs(lift - 0.15) > 0.005:
        raise RuntimeError(f"Unexpected shape key lift: {lift}")
    data = bpy.data.armatures.new("FK")
    arm = bpy.data.objects.new("FK | Two links", data)
    bpy.context.collection.objects.link(arm)
    arm.show_in_front = True
    bpy.context.view_layer.objects.active = arm
    arm.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    root = data.edit_bones.new("Root")
    root.head = (0, 0, 0)
    root.tail = (1, 0, 0)
    tip = data.edit_bones.new("Tip")
    tip.head = (1, 0, 0)
    tip.tail = (2, 0, 0)
    tip.parent = root
    tip.use_connect = True
    bpy.ops.object.mode_set(mode="OBJECT")
    strip.parent = arm
    gs = [strip.vertex_groups.new(name=n) for n in ("Root", "Tip")]
    for v in strip.data.vertices:
        w = max(0, min(1, (v.co.x - 0.75) / 0.5))
        for g, value in zip(gs, (1 - w, w)):
            if value > 0:
                g.add([v.index], value, "REPLACE")
        if abs(sum(e.weight for e in v.groups) - 1) > 1e-5:
            raise RuntimeError("Weights are not normalized")
    mod = strip.modifiers.new("FK | Soft tissue", "ARMATURE")
    mod.object = arm
    tip = arm.pose.bones["Tip"]
    tip.rotation_mode = "XYZ"
    for f, deg in ((1, 0), (13, 50), (25, 0)):
        tip.rotation_euler.z = math.radians(deg)
        tip.keyframe_insert(data_path="rotation_euler", index=2, frame=f)
    s.frame_set(1)
    p = coord(strip, 33)
    base = coord(strip, 17)
    s.frame_set(13)
    delta = (coord(strip, 33) - p).length
    fixed = (coord(strip, 17) - base).length
    if delta < 0.7 or fixed > 1e-5:
        raise RuntimeError(f"FK control points: {delta} / {fixed}")
    s.frame_set(1)
    return {
        "shape_key_lift": round(lift, 5),
        "fk_tip_travel": round(delta, 5),
        "fk_root_travel": round(fixed, 5),
    }


def cloth_test(s):
    cloth = grid("Cloth | Pinned edge", 10, 6, lambda x, y: (x, 2 + y * 0.6, 1.5))
    group = cloth.vertex_groups.new(name="Edge")
    group.add([11 * j for j in range(7)], 1, "REPLACE")
    mod = cloth.modifiers.new("Cloth", "CLOTH")
    mod.settings.vertex_group_mass = group.name
    mod.settings.quality = 6
    mod.point_cache.frame_start = 1
    mod.point_cache.frame_end = 16
    s.frame_set(1)
    start = coord(cloth, 43)
    pin = coord(cloth, 33)
    for f in range(2, 17):
        s.frame_set(f)
        coord(cloth, 43)
    drop = start.z - coord(cloth, 43).z
    drift = (coord(cloth, 33) - pin).length
    if drop < 0.05 or drift > 0.025:
        raise RuntimeError(f"Cloth control points: {drop} / {drift}")
    s.frame_set(1)
    return {
        "cloth_free_drop": round(drop, 5),
        "cloth_pin_drift": round(drift, 5),
        "cache": "16 frames evaluated sequentially; no saved bake",
    }


def uv_test(out, s):
    panel = grid("UV test | Two patches", 2, 1, lambda x, y: (x, 4 + y, 0))
    data = panel.data
    uv = data.uv_layers.new(name="Atlas")
    atlas = bpy.data.images.new("Test atlas", width=64, height=32, alpha=False)
    atlas.file_format = "PNG"
    atlas.filepath_raw = str(out / "uv-emit.png")
    for poly in data.polygons:
        idx = poly.index
        m = bpy.data.materials.new(("Coral", "Cobalt")[idx])
        m.use_nodes = True
        data.materials.append(m)
        poly.material_index = idx
        t = m.node_tree
        e = t.nodes.new("ShaderNodeEmission")
        e.inputs[0].default_value = ((0.8, 0.02, 0.01, 1), (0.015, 0.04, 0.8, 1))[idx]
        t.links.new(e.outputs[0], t.nodes.get("Material Output").inputs["Surface"])
        n = t.nodes.new("ShaderNodeTexImage")
        n.image = atlas
        t.nodes.active = n
        lo = 0.04 + 0.5 * idx
        hi = 0.46 + 0.5 * idx
        for loop, xy in zip(
            poly.loop_indices, ((lo, 0.08), (hi, 0.08), (hi, 0.92), (lo, 0.92))
        ):
            uv.data[loop].uv = xy
    bpy.ops.object.select_all(action="DESELECT")
    panel.select_set(True)
    bpy.context.view_layer.objects.active = panel
    s.render.engine = "CYCLES"
    s.cycles.device = "CPU"
    s.cycles.samples = 1
    s.render.bake.margin = 1
    if "FINISHED" not in bpy.ops.object.bake(type="EMIT"):
        raise RuntimeError("Bake failed")

    def rgb(x):
        off = 4 * (16 * 64 + x)
        return list(atlas.pixels[off : off + 3])

    left, right = rgb(16), rgb(48)
    if left[0] < 0.55 or right[2] < 0.55 or left[2] > 0.15 or right[0] > 0.15:
        raise RuntimeError(f"Atlas centers are not red/blue: {left} | {right}")
    atlas.save()
    atlas.pack()
    atlas.filepath_raw = "//uv-emit.png"
    atlas.packed_files[0].filepath = atlas.filepath_raw
    return {
        "bake": "EMIT, not a high-to-low normal bake",
        "atlas_probes": [[round(x, 3) for x in a] for a in (left, right)],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("out", type=Path)
    args = parser.parse_args(
        sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]
    )
    out = args.out.expanduser().resolve()
    if not bpy.app.background or bpy.data.filepath:
        raise SystemExit("Use a fresh, empty background process.")
    out.mkdir(parents=True, exist_ok=False)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    s = bpy.context.scene
    s.frame_end = 25
    s.render.use_stamp_filename = False
    s.render.filepath = "//preview.png"
    s.render.fps = 24
    s.render.threads_mode = "FIXED"
    s.render.threads = 4
    results = {
        "blender": bpy.app.version_string,
        **rig_test(s),
        **cloth_test(s),
        **uv_test(out, s),
    }
    s.frame_set(1)
    bpy.ops.wm.save_as_mainfile(filepath=str(out / "technical.blend"), compress=True)
    (out / "metrics.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(results, ensure_ascii=False))


if __name__ == "__main__":
    main()
