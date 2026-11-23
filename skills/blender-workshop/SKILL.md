---
name: blender-workshop
description: Use for Blender scene work. Model, shade, animate, verify.
version: 1.1.0
author: Noa3
license: MIT
metadata:
  hermes:
    tags: [blender, modeling, materials, texturing, geometry-nodes, animation, rigging, rendering, game-assets, compositing]
---

# Blender Workshop

Pick the check that is most likely to fail, then open the matching card in [Blender field cards](references/field-cards.md). Return the route, one next action, one observable check, and the evidence or `untested`. If two interpretations change the deliverable, ask one question before editing.

| What must pass? | Route |
| --- | --- |
| Shape, topology or silhouette | `model` |
| Scale, framing or camera verticals | `architecture` |
| Surface color, roughness or texture | `material` |
| A placement rule or editable repetition | `procedural` |
| Import, scale or collision in the target engine | `game` |
| Timing, contact or a loop | `animation` |
| Cel bands or shadow shapes | `anime` |
| Lighting, shadows or a camera render | `render` |
| Bone alignment or deformation | `rigging` |
| A matte, pass or isolated correction | `composite` |

- **Manual / no Blender access:** Give one action and say what the user should see. Report `untested`; do not claim to have opened, edited or rendered a scene.
- **Inspect / read-only:** Describe only evidence you can inspect. Never edit the scene in this mode.
- **Edit / authorized:** Inspect first, work on a copy, change one thing, and reopen or inspect the actual output before claiming a result. Do not run scripts embedded in unknown scenes.

Example: if Geometry Nodes plants appear on a path, use `procedural`. Preview the allowed-region mask before instancing. It should be false on the path and true in the planting bed. A seed change alone is not a fix.

## Open just the chapter you need

Use the [workshop library](references/workshop-index.md) to choose a chapter. For a specific subject, start with the [production atlas](references/production-atlas.md), or run the optional [offline topic finder](scripts/workshop.py) as `python3 scripts/workshop.py subject horse` from the skill directory. It prints the relevant chapter and its acceptance check. If the host opens a full volume, use the named section rather than treating all of it as instructions for the shot.

- **Model, scene and game:** [modeling and made objects](references/modeling.md), [architecture and Geometry Nodes](references/spaces.md), [living worlds and creatures](references/living-worlds.md), [game assets and retro looks](references/game-assets.md).
- **Surface, light and production:** [materials, UVs and optical surfaces](references/materials.md), [lighting and render diagnostics](references/lighting.md), [cinema, effects and delivery](references/production.md).
- **Motion and character:** [animation and cloth](references/motion.md), [anatomy, rigging and contact](references/figure-workflows.md), [character looks and grooming](references/character-surfaces.md), [morphs and deformation](references/deformation.md).
- **Evidence:** [lab notebook](references/lab-notebook.md), [Lumen Quay case study](references/channel-workshop.md), [video, course and book studies](references/learning-notebook.md), [creator register](references/channel-register.md), [creator notes 1](references/creator-notes-01.md), [2](references/creator-notes-02.md), [3](references/creator-notes-03.md), [4](references/creator-notes-04.md), [video study notes 1](references/video-study-notes-01.md), [2](references/video-study-notes-02.md), and [sources](references/sources.md). Distinguish what the creator showed from what the workshop measured. A title, a sampled image and a replayable test are not interchangeable.

## Optional offline tools and labs

The [local-use guide](references/portable-use.md) explains the CLI and optional Blender exercises. The CLI reads the [route cards](assets/route-cards.json), [topic index](assets/production-subjects.tsv) and a local handoff like the [template](templates/handoff.json). It needs no Blender, plug-in or network access. No `.blend` projects, course media or third-party assets are included. The lab scripts do not run on install. With permission, run them in separate fresh Blender processes, into new output paths; they can generate local fixtures for the user. Check Blender version and render-engine requirements first.

- **Geometry:** [mirror seam](scripts/mirror_seam.py), [radial spacing](scripts/radial_study.py), [grommet](scripts/grommet_lab.py), [roof pane](scripts/roof_pane_lab.py).
- **Scene and animation:** [first labs](scripts/lab.py), [deformation lab](scripts/deformation.py), [lab verifier](scripts/verify_labs.py), [Tide Register builder](scripts/build_tide_register.py) and [checker](scripts/check_tide_register.py), [landing](scripts/landing_lab.py), [pickup](scripts/pickup_lab.py).
- **Shading and render controls:** [light groups](scripts/light_group_lab.py), [expression](scripts/probe_expression.py), [toon palette](scripts/probe_palette.py), [backlight](scripts/probe_backlight.py), [skin](scripts/probe_skin.py), [rain](scripts/rain_probe.py).

Original workshop by Noa3. [MIT license](references/LICENSE.md) for the original text and code; linked third-party work retains its own attribution and terms.
