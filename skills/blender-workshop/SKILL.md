---
name: blender-workshop
description: Use for Blender scene work. Model, shade, animate, verify.
version: 1.0.0
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

No Blender installation or plugin is required to read the cards. Check names and render-engine behavior against the user's Blender version. Original workshop by Noa3. [License](references/LICENSE.md).
