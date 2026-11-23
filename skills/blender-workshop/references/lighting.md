# Lighting, compositing and render diagnostics

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [Choose light, renderer and proof together](#chapter-render-choices)
- [A light on a surface, a beam in air, or a reflection?](#chapter-light-field-study)
- [Two bench tests: relight a quay and keep glass in its frame](#chapter-tram-light-lab)

<a name="chapter-render-choices"></a>

## Choose light, renderer and proof together

| Output | First working setup | Stop when / do not claim |
|---|---|---|
| Architectural daylight still | Level camera and a neutral clay layer. Separate sun direction, sun angular diameter and sky fill. Add material after the shadow pattern explains the volume. Use Cycles when transmission or indirect bounce is central to the shot. | Vertical edges and human scale read as intended; openings motivate the light; lit and unlit surfaces stay distinguishable. A PNG is not a lighting simulation or an illuminance calculation. |
| Product / portfolio prop | Large key for the shape of the reflection, independent backdrop and one rim if the silhouette needs it. Rotate the object or the card before adding several more lights.[22] | Handle opening and contact patch read in two views; metal has a readable environment to reflect. A uniform gray metal can be an uninteresting reflection rather than a bad base color. |
| Translucent organic close-up | Model the outer membrane and the folded interior as separate forms. Light the rim from the side; place secondary forms farther back and off the main silhouette. | At thumbnail size the subject separates from the background; at full size the inner folds remain visible *through* the shell. If they disappear, isolate the shell and its light before adding emission or bloom, which can hide the same depth cue. |
| Anime or graphic look | Design shadow groups and line weight in camera. Choose EEVEE if the graph depends on Shader to RGB; avoid assuming its output is portable to Cycles or glTF.[4][59] | Inspect face and hair in adjacent frames, not just heroic poses. A change in saturation or band placement may be the view transform, not the material. |
| Real-time scene | Treat Blender as authoring and look development. Preview in the intended rendering path with the engine's lighting, camera, output transform, texture filtering, LOD thresholds and display resolution. | Frame time measured on the target hardware, silhouettes at switch distances, material/UV integrity and game collision all pass. A headless import is useful but cannot certify shader appearance or frame rate. |

### A light comparison that can falsify a choice

1. Lock the camera, exposure, view transform, material, scene geometry and seed. For direct sun angle, keep **sun power and direction fixed**; change angular diameter only. For an area light compare size first, then separately compensate power if its exposure changes. Do not change both size and power and call the result a one-variable test.[22]
2. Render the same floor line or the same glossy edge. In the gallery's hard-angle image the long diagonal on the floor has a hard boundary. At 14° the same boundary spreads and the narrow bands lose contrast. Use the harder option for rhythm and direction; the softer one for surface continuity and a quiet room. Neither is more correct independent of the brief.
3. If a room is flat, temporarily isolate direct light and background fill. If shadows appear noisy, inspect an undenoised crop at final resolution before deciding between more samples, more efficient light placement, or relaxing an unimportant material detail. Compare the result to a higher-sample crop rather than treating a sample count as a quality badge.[14]
4. Use AgX or another explicitly chosen view transform for the review and keep it the same between A and B. A display PNG is not a linear intensity measurement. For later recomposition, save scene-linear multilayer EXR separately from the display-referred client preview; enabling passes alone does not place them in a PNG.[11][35][60]

**Diagnosis by pass:** check Normal for a shading discontinuity, Z/depth for staging, diffuse/glossy contribution for an unexpectedly dark material, and masks for isolation.[60][21] For banding or flicker, render a short contiguous sequence with fixed evaluation conditions, not just sparse samples. For EEVEE compare in the actual camera; rasterized visibility and screen-dependent effects are not evidence that hidden geometry contributes as it would in a path tracer.[59]

**Practical review sequence:** thumbnail silhouette → clay render → untextured light A/B → material board and two close-ups → beauty at actual size → reopen from disk. Add a motion or engine gate only when that is the output. Write down what each image proves and what it cannot prove. See [advanced labs](lab-notebook.md#chapter-advanced-labs) for filenames and reproduced measurements.

<a name="chapter-light-field-study"></a>

## A light on a surface, a beam in air, or a reflection?

**Choose the observation before changing the shader.** A projected image needs a receiver. A beam visible from the side needs light scattered into the camera. A puddle is a surface whose reflections differ across its boundary. Turning up the lamp is not a common repair for all three.

| Seen in the original | Transfer to a different scene |
|---|---|
| In Ryan King Art's projector lesson a rectangular blue image is visible around 7:30, but at 12:15 the side view shows a purple shaft narrowing toward the source.[106] | Decide whether the failure is on the receiving wall or in the space **before** the wall. Hide the receiver on a working copy and see whether a shaft is still visible from the side. |
| In stache's fog lesson the enclosing box at 4:50 contrasts with the isolated patch at 12:10. The narration around 12:08–12:17 discusses lowering density and placing local patches.[105] | For one pool of light, use a bounded mesh with a volume shader; its bounds define where scattering can occur. For a whole-scene veil, a world volume or an enclosing mesh are different choices. A visually global veil need not mean a World shader.[108] |
| In Blender Guru's puddle lesson a tree reflection appears on part of the ground at 14:10; separate reflective patches remain at 24:20.[107] | Keep normals, color, camera and lights fixed. Test a uniform rough surface against one with a two-region roughness mask under a broad bright card. The mask sets **where** the change occurs; roughness controls how sharp the reflection is.[3] This suggested test is not a water simulation and was not rendered here. |

### Reproduce the side-view beam

For the historical beam comparison, the side camera saw no receiving surface. Rebuild the minimal set described here to run your own comparison. A downward **Spot** sits above a cube whose material has **Volume Scatter → Material Output / Volume** and no Surface connection. A black world supplies no intended fill. Render once before changing anything. Then set density to zero, render again, restore density, and set the spot to zero. Keep the camera, exposure, view transform, samples and seed fixed.

| Saved example | Density | Spot power | Mean red in the central patch |
|---|---:|---:|---:|
| `local_on.png` | 0.1 | 400 W | 0.299129 |
| `empty.png` | 0 | 400 W | 0.000218 |
| `lamp_off.png` | 0.1 | 0 W | 0.000218 |

Only the first image has a visible cone. Removing the medium isolates scattering; removing the lamp checks that the medium is not self-luminous. If a fresh test stays bright with the lamp off, inspect other lights, the world and emission before increasing density. If the shaft exists but its edge is cropped in an unwanted place, inspect the **volume bounds** before softening the spotlight.

**Measured on Blender 4.5.9 LTS:** 160 × 120, Cycles, 48 samples, seed 12, Standard view transform. Values are means of the central 12 × 12 **red-channel samples read back from the saved PNGs by Blender**, not meter readings or a universal density prescription. There was no world-volume comparison, projection-texture test or render-performance benchmark.

**Independent check:** render the three control states of the scene you made into a new output directory and compare the same region of each frame. A dark no-medium or lamp-off control should fail to show the beam. Leave the source scene unchanged.

**Learning evidence:** first-party storyboard frames and publisher chapters; a timed public narration excerpt was also read for the local fog decision. No exact numerical node value is attributed to the videos. The settings and control renders in this chapter belong to the independent exercise.

### Sources

[3] https://docs.blender.org/manual/en/4.5/render/shader_nodes/shader/principled.html — Blender 4.5 LTS: Principled BSDF
[105] https://www.youtube.com/watch?v=A4zd42y0Af0 — stache: Cinematic Fog in Blender - The Ultimate Guide
[106] https://www.youtube.com/watch?v=z3WgYm09fME — Ryan King Art: Create Light Projectors in Blender (Tutorial)
[107] https://www.youtube.com/watch?v=TxYVMw94FXE — Blender Guru: Blender Tutorial: Photorealistic Puddles
[108] https://docs.blender.org/manual/en/4.5/render/materials/components/volume.html — Blender Manual contributors: Volumes — Blender 4.5 LTS Manual

<a name="chapter-tram-light-lab"></a>

## Two bench tests: relight a quay and keep glass in its frame

### Relight an existing render, not the camera exposure

**Use it when:** a station practical is too strong but the car windows and harbour sky already read. CG Boost’s chapter starting **02:23** assigns lights to groups; **05:16** moves into their use after rendering. These are chapter starts, not exact click times.[154] A Cycles light group is a contribution from emitters, including their reflected light; it is *not* an object mask. The world can belong to a group too.[60]

**What the earlier Lumen Quay master demonstrated:**

1. The original scene started from the denoised beauty. Its compositor offered an alternate sum of separate Car, Station and Harbour passes.
2. Enable the checkbox on **Use relit passes**. The three Multiply nodes are named **Car gain**, **Station gain** and **Harbour gain**. Their *unconnected color inputs* start at white. Set Station gain to neutral gray, or black to mute it. Let the compositor update; do not press F12 again to change a tint or gain.
3. Compare the pools under the lamps, the platform reflections, and the highlights on the tram. A reflection of a station light on the tram belongs to **Station**, not **Car**. Putting Station gain back at white restores that contribution. Uncheck the switch at any time to compare against the original beauty. The PNG alone contains no separate light passes.

**Build this in another scene:** use Cycles; create groups on the View Layer, then assign lamps, light-emitting meshes and World to the right group. Render. From Render Layers, multiply each `Combined_<name>` pass by its own color; **Add** them at factor 1 with clamping off. Denoise the sum once if needed, then apply glare and the display transform. Do not add the main Image pass to the sum: that counts the same light twice. If the neutral sum is dark, find unassigned emitters or a missing World before increasing a gain. A gain cannot recreate a new lamp position or shadow direction; those need another render.

**What was measured:** the [light group diagnostic](../scripts/light_group_lab.py) writes six 32-bit scene-linear EXRs from **one** render of a damp receiver plus two spheres. With all three groups, the RGB root-mean-square difference from the original was below `0.000001`; removing the warm practical raised it above `0.56`. In the tram master, a separate fixed-seed 180 × 108 camera test gave a neutral-sum difference of `0.0`, a change greater than `0.61` when Station was muted, and zero RGB with all three groups muted. The comparison intentionally turns off denoising and glare; it is not a claim of bit-identical results between differently denoised final images.

### Cut a hole without shrinking the whole pane

**Use it when:** a broken edge needs softening, but the glass must remain seated. In CG Boost’s painted-glass Short, the author assigns a Mask group at **00:10–00:17**, protects the outer edge with a second group around **00:34–00:42**, and adds Solidify after smoothing.[156] The Mask controls which vertices remain; the Smooth modifier can be restricted to its own vertex group.[165][166]

1. Subdivide a plane enough to describe the break. Assign the whole pane to a retention group. Lower weights where the hole belongs; put the **Mask** modifier first. Check for a real opening in wireframe, not an alpha patch.
2. Assign the outer edge loop to a second group. Restrict **Smooth** to the inverse of that group, or positively select just the movable interior. Put **Solidify** after it. Separate the structural frame from the movable glass. The example does not simulate fracture or create loose shards.
3. Duplicate the pane twice. On one copy let Smooth act on everything; on the other keep the center sealed. Compare all three in orthographic view with the frame corner marked. A successful test requires an open center, a surviving patch away from the break, and a stationary corner.

The [roof pane diagnostic](../scripts/roof_pane_lab.py) measures the evaluated geometry rather than its modifier names. Both cut controls passed a ray through the center and stopped one through an intact patch. At **6 mm** thickness, the unprotected corner moved **47.0 mm**; the protected corner moved **less than 0.001 mm**. The uncut control blocked the center ray. Those dimensions are ours, not the author’s. The three-pane comparison is a separate study, not damage to the passenger shelter.

### Reproduce in Blender 4.5 LTS

Run these as separate, fresh background processes from the skill folder. Use new output folders; neither script overwrites an existing one. Each script resets its own process to an empty file. The historical tram scene is not included; both diagnostics generate their own inputs.

```sh
blender -b --factory-startup --python-exit-code 1 -P scripts/light_group_lab.py -- ./light-check
blender -b --factory-startup --python-exit-code 1 -P scripts/roof_pane_lab.py -- ./pane-check
```

`light-group-checks.json` records the image comparison; `pane-checks.json` records geometry probes. `Glazing-Controls.blend` contains the three editable stacks. The executed runtime was the official **4.5.9 LTS `bpy` module** in separate Python processes. The interactive F12 workflow uses the saved scene; validation reopened it and rendered the active camera without enabling scripts.

### Sources

[60] https://docs.blender.org/manual/en/4.5/render/layers/passes.html — Passes - Blender 4.5 LTS Manual
[154] https://www.youtube.com/watch?v=IjFXi2axl-8 — CG Boost: Change Your Lighting Without Re-Rendering
[156] https://www.youtube.com/watch?v=LraQIwC6uBo — How you can paint broken low poly glass in Blender. #b3d #blender3d
[165] https://docs.blender.org/manual/en/4.5/modeling/modifiers/generate/mask.html — Mask Modifier - Blender 4.5 LTS Manual
[166] https://docs.blender.org/manual/en/4.5/modeling/modifiers/deform/smooth.html — Smooth Modifier - Blender 4.5 LTS Manual
