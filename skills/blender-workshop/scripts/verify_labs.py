"""Read-only acceptance check for the two Blender Atelier generators."""

import argparse
import json
import math
import sys
from pathlib import Path
import bpy
import numpy as np


def need(ok, message):
    if not ok:
        raise ValueError(message)


def open_sample(root, name):
    p = root / name / (name + ".blend")
    need(
        "FINISHED"
        in bpy.ops.wm.open_mainfile(filepath=str(p), load_ui=False, use_scripts=False),
        str(p),
    )
    return bpy.context.scene


def rgb(path):
    image = bpy.data.images.load(str(path), check_existing=False)
    try:
        need(tuple(image.size) == (600, 500), f"Wrong PNG size: {path}")
        a = np.empty(len(image.pixels), dtype=np.float32)
        image.pixels.foreach_get(a)
        return a.reshape(500, 600, 4)[:, :, :3]
    finally:
        bpy.data.images.remove(image)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    opts = parser.parse_args(
        sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]
    )
    root = opts.root.expanduser().resolve()
    need(
        bpy.app.background and not bpy.data.filepath, "Use a fresh background process."
    )
    report = {}
    for name, engine in (
        ("metal", "CYCLES"),
        ("rosette", "CYCLES"),
        ("mask", "BLENDER_EEVEE_NEXT"),
    ):
        s = open_sample(root, name)
        need(s.camera and s.render.engine == engine, "Camera/engine " + name)
        path = Path(bpy.path.abspath(s.render.filepath)).resolve()
        need(path == root / name / (name + ".png"), "Nonportable render path")
        img = rgb(path)
        need(
            float(img.std(axis=(0, 1)).max()) > 0.045,
            "Image has no useful contrast: " + name,
        )
        report[name] = {
            "engine": s.render.engine,
            "view": s.view_settings.view_transform,
            "size": [s.render.resolution_x, s.render.resolution_y],
        }
        if name == "rosette":
            mod = next(
                m for obj in s.objects for m in obj.modifiers if m.type == "NODES"
            )
            ids = {
                x.name: x.identifier
                for x in mod.node_group.interface.items_tree
                if getattr(x, "in_out", None) == "INPUT"
            }
            need(
                mod[ids["Count"]] == 24 and not mod[ids["Realize for mesh output"]],
                "Source should retain 24 instances",
            )
        if name == "mask":
            obj = next(o for o in s.objects if o.type == "EMPTY")
            poses = []
            for f in (1, 7, 13, 19, 25):
                s.frame_set(f)
                poses.append(round(math.degrees(obj.rotation_euler.z), 3))
            need(
                poses[0] == -14
                and poses[2] == 0
                and poses[-1] == 14
                and poses == sorted(poses),
                "Pose check",
            )
            info = json.loads(
                (root / name / "metrics.json").read_text(encoding="utf-8")
            )
            colors = np.array(info["palette_linear_rgb"])
            targets = np.where(
                colors <= 0.0031308,
                12.92 * colors,
                1.055 * np.power(colors, 1 / 2.4) - 0.055,
            )
            for filename in ("pose-01.png", "mask.png", "pose-25.png"):
                pic = rgb(root / name / filename)
                areas = [
                    int((np.abs(pic - c).max(axis=2) < 0.015).sum()) for c in targets
                ]
                need(min(areas) > 1500, "A major tonal band is missing: " + filename)
                report[name][filename] = areas
    s = open_sample(root, "technical")
    need(bpy.data.images["Test atlas"].packed_file, "Atlas not packed")
    need(len(bpy.data.objects["FK | Two links"].data.bones) == 2, "FK rig not saved")
    need(
        "Arch" in bpy.data.objects["Test strip"].data.shape_keys.key_blocks,
        "Shape key missing",
    )
    atlas = bpy.data.images.load(
        str(root / "technical/uv-emit.png"), check_existing=False
    )
    need(tuple(atlas.size) == (64, 32), "Wrong UV bake size")
    probes = [
        list(atlas.pixels[4 * (16 * 64 + x) : 4 * (16 * 64 + x) + 3]) for x in (16, 48)
    ]
    left, right = probes
    need(
        left[0] > 0.55 and left[2] < 0.15 and right[2] > 0.55 and right[0] < 0.15,
        "UV bake centers are not red/blue",
    )
    report["technical"] = {
        "packed_atlas": True,
        "fk_bones": 2,
        "shape_key": "Arch",
        "external_atlas_probes": probes,
    }
    bpy.ops.wm.read_factory_settings(use_empty=True)
    need(
        "FINISHED"
        in bpy.ops.import_scene.gltf(filepath=str(root / "rosette/rosette.glb")),
        "GLB import",
    )
    objs = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    need(len(objs) == 1, "Expected only the petals, no stage")
    obj = objs[0]
    need(
        len(obj.data.polygons) == 12672
        and all(len(p.vertices) == 3 for p in obj.data.polygons),
        "Unexpected triangulation",
    )
    need(
        0.01 > abs(obj.dimensions.x - 2.9)
        and 0.01 > abs(obj.dimensions.y - 2.9)
        and bool(obj.data.materials),
        "Invalid bounds or material",
    )
    report["glb"] = {
        "triangles": len(obj.data.polygons),
        "size": [round(x, 4) for x in obj.dimensions],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
