# Production, cinema and effects

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [Motion, simulation, compositing and delivery](#chapter-production)
- [A shot that earns its cut](#chapter-cinema-and-delivery)
- [What it takes to aim at a Square Enix cinematic](#chapter-cinematic-shot)
- [Difficult effects: predict one event, then prove it happened](#chapter-difficult-effects)

<a name="chapter-production"></a>

## Motion, simulation, compositing and delivery

### Organize a shot
Give characters, set, lights and helpers named collections, set an active camera and separate working paths from delivery paths. Copy the `.blend` before irreversible bakes or exports. Set relevant scales, frame range and frame rate before rigging or simulation. Before handoff, check whether external images, fonts, libraries and caches are included or deliberately unnecessary. A packed texture does not replace an external simulation cache.

### Characters: from rest pose to a dependable rig
1. Settle the deformation mesh before rigging. In **Edit Mode**, place rest bones along the limbs; check left/right names and bone roll. Bend articulated regions rather than imitating every motion with object scale.
2. Put an Armature modifier on the mesh and match deform-bone names to vertex groups exactly. For `Armature Deform`, select the mesh first and the armature last as the active object. Automatic weights are a starting point, not finished skinning.[17] Blend groups deliberately at joints; do not apply soft transitions to rigid armor. In the technical lab, the root stays put while the weighted mesh tip travels a measurable distance.
3. **FK or IK?** Use FK for freely swinging chains and IK for planted feet or hands. On a biped, place the IK target at the chain end, limit chain length and put the pole target in the intended knee/elbow plane. If a joint flips, isolate roll, pole placement and chain first.[26][27] Match the incoming pose before switching between FK and IK to avoid a pop.
4. **Face:** Keep the Basis shape key; add relative keys for Blink, Smile and other expressions. Vertex correspondence must match the basis, so lock down topology first.[18] Move the eyelid over the eyeball and test combinations such as Smile + Blink. Correct a collapsing elbow with weights first; add a corrective shape if extreme poses still need control.
5. **Animation:** Establish three readable keys, then a breakdown with an arc and weight shift. In Graph Editor check timing and spacing before tangents; F-curves interpolate keyed values.[24] Choose Constant interpolation deliberately for a held pose. Do not export a duplicate final pose as an extra beat in a loop. Play at the target speed: three stills test poses, not timing.

### Cloth and other simulations
Start a scarf with a small, evenly subdivided patch and a simple collider. Pin one edge using a vertex group; its weights control pin influence.[29][36] Test gravity and pins, then collisions, then the moving body and self-collision. Use enough geometry for folds, but not a high-resolution render mesh for the first solver test. Try visible thickness and fine subdivision **after** the simulation modifier.

When building the simulation, evaluate from its start; jumping ahead is not a substitute for a bake. When **verifying an already baked delivery**, do the opposite: open a fresh copy away from the source and jump straight to a late frame. A sequential replay can hide a missing cache. If geometry, collisions or the frame range change, rebake a new version.[19] The original technical lab measures a free drop and pinned edge; the [disk-cache handoff](motion.md#chapter-cloth-cache-handoff) tests the transferred bake against known poses with a missing-cache control. Neither is a costume collision test.

### Render, composite and deliver
- **Look before effects:** Check beauty without bloom/glare before adding a film look. For selective corrections, enable the relevant object/material Cryptomatte passes in View Layer and select a matte with the compositor's Cryptomatte node. Inspect edges and transparency at final resolution.[21]
- **Master:** Separate a linear multilayer EXR for further processing from a display-referred PNG for visual approval.[11][35] For animation, render an image sequence first, not just one video container, so missing frames can be replaced. Verify crop, alpha on bright and dark backgrounds, first/last frame number, frame rate and any audio sync in the target.
- **Game/web → GLB:** Select export objects deliberately and define scale, origin, local axes and animation. Use Principled/bitmap metallic-roughness, tangent normal maps and UVs; translate or bake unsupported procedural materials. Meshes are triangulated; UV seams and split normals can increase exported vertex counts.[20] Keep modifiers and instances in the Blender master; evaluate an export copy. Reimport **and**, for an engine delivery, test in that runtime. Check bounds, materials, orientation, clip lengths, deformation and dependencies.
- **Still, animation or real time?** A product still needs a clear silhouette and reflections without crushed detail. Animation also needs stable shadows, strokes and contact over time. For real time measure triangles, material slots, texture memory and performance on the target device. A good Cycles image is not an FPS test.

#### Deliver a set of stills

1. **Separate proofs from finals.** List each shot's output name, intended dimensions and one detail that must read. Give parallel builds separate working folders so one `preview.png` cannot replace another. Render a small proof at the final aspect ratio. Fix the visible fault before raising samples: for example, move a reflected light strip off a dial's graduations if they disappear beneath it.
2. **Render what you saved.** Set the final camera, output size and resolution percentage in the `.blend`. In a fresh process, use `bpy.ops.wm.open_mainfile(filepath=str(scene_path), load_ui=False, use_scripts=False)` and render from that camera. Open the resulting PNG, not the proof. Compare the final filenames against the shot list and look at the images side by side; matching sizes won't catch a duplicated shot.
3. **Keep the approved pixels.** If preparing a shareable Blender PNG, remove unneeded text or EXIF metadata from a copy; keep the `IDAT` data, alpha and display-color chunks intact. For 8-bit RGB/RGBA, compare both files in Pillow: `a.size == b.size`, `a.mode == b.mode`, and `a.tobytes() == b.tobytes()`. If a filename is visible *in the picture*, turn off the render stamp and rerender; stripping metadata cannot remove painted pixels.
4. **Check optional native files separately.** A `.blend` can have no missing assets yet still retain the author's home path in file-browser state. Build distribution copies in a fresh process with a neutral home and working directory (for example, `/work` inside an isolated build). Check the decoded file for known private path prefixes; for a Zstandard-compressed scene, inspect the stream from `zstd -qdc -- "$SCENE"`, not the compressed bytes. If a path remains, regenerate the copy rather than editing binary strings, then compare its render with the approved one.
5. **Test the actual download.** Extract the finished archive into an empty folder, make the authoring folders unavailable, and reopen each extracted `.blend` with script execution disabled. Check the active camera, renderer, dimensions and dependencies there. If an optional scene fails, deliver the verified images without it; if editable files were requested, identify the specific scene still blocked.

### Diagnosis
Mesh stationary → inspect armature modifier and bone/group names. Double deformation → look for a second transform in armature, parent and constraint chains. Exploding cloth → isolate initial intersections, object scale and collision distance. Visible in viewport but missing from render → check render visibility, view layer, active camera, frame range and path. Gray GLB → check supported material path and embedded textures in the target viewer. [Sources](sources.md).

<a name="chapter-cinema-and-delivery"></a>

## A shot that earns its cut

By Noa3 · Blender 4.5.9 LTS baseline · Proposed workshop, not a built or mixed spot.

**Start with a viewer question:** Can a commuter open this travel mug with one hand? The answer must be visible before the end card. Cinematographer Zach Grullon describes starting with the motivation for camera placement, movement and actor blocking rather than treating beauty as the brief. [427] Translate adjectives into review questions: *premium* → does the moving highlight describe the rim without erasing the mark? *intimate* → can we see the thumb hesitate? *calm* → is there a still interval long enough to read the name? A shot can be beautiful and still fail all three.

### Block the cause, then choose the lens

| Shot | What changes on screen | How to stage it; when to reject it |
|---|---|---|
| Station wide | We find the traveller and the occupied hand. | Place the bag on the near side and leave space ahead of the traveller. Keep the platform sign behind, not sprouting from their head. If the eye follows a train instead, delay the train. |
| Medium action | The free thumb reaches the latch. | Keep the hand moving in the same screen direction across the cut; cut on the reach, not after it. Test shoulder and wrist silhouettes in flat gray. |
| Insert | A press releases the lid. | Show the locked state, contact, then daylight in the gap. Start locked off. Add a lateral slide only if the revealed gap was previously hidden. If contact reads only with the click, change the angle. |
| Packshot | The viewer remembers which mug it was. | Set the mug on a visible support, turn the mark towards camera, use a long reflection card to describe the wall and a dark card to separate the rim. Stop the turn before the name appears; do not rotate type through the read. |

Lock sensor fit, aspect and sensor size before comparing lenses. Blender’s perspective camera narrows its field of view as focal length increases; lowering the aperture f-stop increases the blur effect. [23] Try a 28 mm and an 85 mm from one tripod position: first compare the uncropped frames, then crop the wide to match the centre of the long. Now move the wide camera closer until the mug fills the same height. Look at the near rim against the far rim and the station sign against the mug: it is the relocation, not the millimetre marking alone, that changed their projected relationship. Choose the standing point for that relationship, then choose the lens for the frame. Put focus on the latch, scrub the full reach, and close the aperture if the open state or the printed name falls out of focus.

**Motion test:** Mark the first frame on which the latch can be understood. Compare a locked take, a pan that follows the wrist, and a short dolly past the rim. A pan changes aim; the dolly can reveal what was behind an edge. Key only the start, reveal and settle first. Scrub the in-betweens for overshoot and a background pole crossing the thumb. Keep the cheapest take that reveals the state on time. Ask a viewer on mute what changed, not whether they liked the camera.

### One product, different edits

For a **television commercial**, work backward from the commissioned running time and approved end-card hold. Reserve readable space for required copy in the storyboard. Test the logo, captions and legal line together at delivery resolution, not in a zoomed editing window. Shoot a separate vertical insert if protecting a portrait crop would make the thumb illegible in landscape. For a **feature reel**, keep only the evidence for its named feature: one-handed use needs the other hand visibly occupied and an uninterrupted press-to-open shot. A finish/material reel instead needs a fixed light reference and a reflection travelling across the surface; a mechanism reel needs a section or exploded view plus the assembled action. Label explanatory cutaways; do not substitute them for proof that the assembled product works. For a personal showreel, distinguish your lighting, modelling and compositing work from supplied assets.

### Deliver to the booking, not to a generic “TV” preset

Get the dated sheet and the booked duration from the receiving outlet. Record raster, cadence/field order, aspect, codec/wrapper, slate and black, timecode, title/action guides, caption format, colour encoding and levels, audio channel map, integrated loudness, true peak and tolerances. Unknown means **ask before master**, not “use the internet default.”

**Worked reading, not a universal spec:** CBC’s 2026 commercial sheet specifies 1920×1080, upper-field-first interlaced HD, BT.709 and a safe-title rectangle spanning 90% of picture width and height. [426] That rectangle is not a 90% margin on each side and is not a social-platform overlay. The same sheet calls for PCM at 48 kHz/24 bits, a −2 dBTP maximum and commercial integrated loudness of −24 LKFS ±1 LU under its stated measurement algorithm; its stereo track map also addresses described video on 7/8. [426] Do not export this map or loudness target for another broadcaster without its sheet. CBC’s video row literally prints “29/97” while the caption row specifies 29.97 fps drop-frame timecode: confirm the operative cadence with intake rather than silently repairing the sheet. [426]

Render a clean image sequence and preserve a scene-linear intermediate for changes; Blender distinguishes scene-linear render/composite work from display and storage transforms. [11] Specify the intended viewing transform to finishing, apply it once, and check the **encoded** output on scopes for the booked levels and colour, especially the saturated logo. Decode the actual master: step through field motion; read copy and captions inside the guides; listen to each assigned channel; measure integrated loudness across the commercial, not the slate, and measure true peak separately. If an encoder cannot produce the prescribed captions or wrapper, hand picture and stems to finishing; do not relabel a preview as a broadcast master.

### Cut to what the ear hears

Use VSE sound strips for editorial music, voice-over and precisely placed Foley: strips support waveform display and animated volume. [420] Use a scene Speaker instead for a bell that belongs at the far end of the platform: Blender’s Speaker provides distance attenuation and requires mono for its 3D audio effect. [421] Listen once with the camera approaching and once leaving. If the click is important to the claim, keep it intelligible in the editorial mix; do not play both a baked spatial click and its dry duplicate by accident.

At locked picture rate, import the cleared music, show the waveform, listen and mark the *attack* of the chosen downbeat, not the tallest sample in its decay. Mark the anticipatory reach separately from thumb contact. Align contact with the click; let the following musical accent introduce the packshot. For a steady tempo a rough beat interval in frames is `fps × 60 / BPM`; place markers from absolute elapsed time rather than repeatedly adding a rounded interval. Live drums may drift: the recorded attack wins. Try a cut one frame either side, play at speed, then check the decoded master for sync near both head and tail. A constant error suggests an offset; growing error calls for a cadence/timebase check. Leave quiet beats under speech and test once with music muted. A waveform peak is neither a loudness measurement nor evidence that the feature is understandable.

### Sources

[11] https://docs.blender.org/manual/en/4.5/render/color_management.html — Color Management - Blender 4.5 LTS Manual
[23] https://docs.blender.org/manual/en/4.5/render/cameras.html — Cameras - Blender 4.5 LTS Manual
[420] https://docs.blender.org/manual/en/4.5/video_editing/edit/montage/strips/sound.html — Sound Strip - Blender 4.5 LTS Manual
[421] https://docs.blender.org/manual/en/4.5/render/output/audio/speaker.html — Speaker Objects - Blender 4.5 LTS Manual
[426] https://solutionsmedia.cbcrc.ca/media/5220/cbc-television-commercial-technical-specifications-20260720.pdf — CBC Television Technical Specifications for Commercial Delivery
[427] https://mixedasianmedia.com/issue-009/2019/9/9/art-of-the-eye — Art Of The Eye: An Interview With Cinematographer Zach Grullon — Mixed Asian Media

<a name="chapter-cinematic-shot"></a>

## What it takes to aim at a Square Enix cinematic

**Author: Noa3. Benchmark: Agni's Philosophy, not every Final Fantasy production.** Specify whether the goal is a finished offline movie or an interactive real-time demonstration. They can share a visual target; only the latter has to meet a frame-time budget on a named machine while running. An offline Blender movie is not evidence of real-time performance.

### What the production sources actually say

Square Enix describes *Agni's Philosophy* as a collaboration between its Visual Works cinematic team and Advanced Technology Division. Their stated target was a **real-time** demo approaching pre-rendered CG. Their simulation presentation separates particle emission, simulation and rendering, discussing which independent updates can execute in parallel; it is not a prescription to build a custom GPU solver for every shot.[311]

A CEDEC report of the team's presentation describes concept/storyboard work, a pre-rendered visual target, and conversion to real time; the speakers also describe real hairstyle reference and using facial scan data. This is reporting on that demonstration, not evidence that a particular Blender node group, polygon count, workstation, or set of plug-ins produces that quality.[312]

### A solo production brief that tests the same kinds of decisions

**One proposed shot:** a station employee plants a foot, shifts weight, checks the clock, then glances back at an approaching light. A damp coat settles a moment after the body stops. Start with one fixed camera and a few seconds of acting. Only add a closer face shot if the facial performance itself is the test. The following gates are workshop recommendations, not Square Enix staffing estimates.

| Owner / discipline (one person may wear each hat) | Hand over | Do not advance if… |
|---|---|---|
| Director / layout | Licensed gesture and light references, an annotated shot board, lens, screen size of face and feet, timed gray animatic | The viewer cannot read who is waiting for what without a caption. |
| Character artist | Neutral body and expression sheet, clothed turntable, clean deform mesh; test in a gray material and then skin under two lights | Silhouette, jaw, lid closure or leg proportions break outside the beauty camera. |
| Rigger / animator | Approved range-of-motion poses, contact markers, a blocked performance; clean any captured/retargeted motion against reference | Soles drift in the hold, knees pop, eyes miss the clock or hips never take the body's weight. |
| Environment / look development | A visible load path for each hanging prop; material coupons at physical scale, clean/worn controls | Trace the clock → bracket → structural post in the actual shot. Stop if any connection disappears. Wear must have a physical cause. |
| Character FX / lighting | Approved animation cache, collision proxy, guide groom/cloth tests and cache manifest; compare no-FX vs FX under the shot lights | Cloth tunnels, contacts change after a rebake, hair scatters flicker, or the rim light hides the face. |
| Compositor / editorial / technical reviewer | Reopenable scene bundle, image sequence, grade, decoded delivery clip, per-shot notes and a same-camera reference comparison | The encoded shot clips highlights, halos around hair, loses the foot contact or stutters at the cut. |

**What to budget before promising the look:** access to appropriate references or consented/licensed scans and capture if used; anatomy and performance feedback from another person; time to iterate poses and assets; hair and costume work; storage for versioned textures, caches and EXRs. Benchmark a representative *hard* frame and a preview sequence on the target, not an empty scene. For real time, also test the moving shot in the target engine at the agreed output resolution and report frame-time distributions, peak memory and visible LOD transitions. No hardware model, head count, budget or deadline is implied by this study.

**Evidence ladder:** the gauge tests UVs, roughness and timing; the cutaway tests linked leg motion and support; a cloth strip and particle probe test individual mechanisms. None tests a speaking face, hair/cloth on a complete moving character, full lighting continuity or real-time delivery. The next meaningful milestone is a short, reference-matched **clay** acting shot with a planted foot, legible gaze, clean profile and independent pose review. Do not promote it to final hair, skin and rain while the acting still fails.

#### Brief for the next character test (not yet reproduced)

Film a willing performer rising from a trunk and looking at a clock; use your own or cleared footage. Match the camera height and trunk height first. Mark the last frame that the seat carries weight, the first frame the hips clear it, and the foot that supports the rise. In the clay playblast, review those events in profile and from the delivery camera. If the hips lift before weight can pass through a foot, fix the pelvis path and timing rather than pinning both shoes harder. Watch the same take at speed with the reference hidden: can a second viewer tell when the clock catches the character's attention?

Only then add a separate face crop and coat pass. Compare a complete blink and one audible lip closure against the performance (see [the lip-seal diagnosis](lab-notebook.md#chapter-surface-performance-decisions)). For the coat, preserve the approved body take and compare it with/without deformation and with a [relocated cache](motion.md#chapter-cloth-cache-handoff). A good technical match does not replace a human review of the acting. Neither this acting shot nor a realistic speaking face is included.

### Sources

[311] https://www.jp.square-enix.com/tech/library/pdf/SiggraphAsia2014_simulation.pdf — Practical Applications of Compute for Simulation in Agni's Philosophy
[312] https://gigazine.net/gsc_news/en/20120821-making-of-agnisphilosophy-cedec2012 — How did you make that demo that moved Final Fantasy as a super high quality real time CG?

<a name="chapter-difficult-effects"></a>

## Difficult effects: predict one event, then prove it happened

**By Noa3.** These are Blender shot-design and verification recipes, not four finished simulations. Decide which part must be simulated and which may be art-directed. Always test the sequence through cold reopen/scrub and the delivery camera; a cache that only works while its authoring process is warm is not a deliverable.

### A Rube Goldberg machine: causality before complexity

Write an event chain spectators can follow: ball rolls → lever rotates → gate clears → second ball drops → bell moves. Give each event an observable witness (first pivot rotation, gate clearance, first downward center motion, contact sound). Build it in small modules using active rigid bodies for moving pieces and passive colliders for track/base, actual scene scale, applied scale on proxies and separate render geometry. Place a hinge at the physical pin, not the center of the decorative object. Blender's rigid-body constraints link bodies; the world settings distinguish substeps from solver iterations, which stabilize constraints/stacking at different costs.[367][368]

Run each handoff from the same start before joining modules. Freeze the first ball or hold the gate: downstream events must now stop **unless** they are explicitly keyed art direction. If the ball tunnels, inspect collider thickness and substeps; if the lever chatters at its pivot, check alignment, adjacent intersection and iterations. A hidden motor or keyframe can rescue a commercial shot but then call it choreography. Frame each transfer long enough for the direction of force to read. Add sound on the observed impact frame, not on the planned storyboard frame.

### Mixing fluids: density, tracer and shading are different deliverables

Specify one question: two colors transported in one liquid, a surface swirl seen from above, or two **immiscible liquids** with a persistent interface? A domain encloses Blender's fluid solve; size/resolution affect what it can resolve.[373] For a graphic swirl in native Blender, an art-directed route is a carrier mesh with a procedural material-space flow or a transported scalar on a stable proxy. If the proxy has changing topology, index-based vertex colors can jump: use particle/field sampling or cache the transported attribute with the solver. A time-varying noise mix is a shading trick and does not demonstrate advection. A Geometry Nodes Simulation Zone carries state between evaluation steps; defining the transport and boundary condition is still the artist's job.[388]

For a documented optional alternative, FLIP Fluids has per-source color and a baked surface color attribute `flip_color`; mixing enabled lets nearby particles exchange that attribute.[371] Its own limitations distinguish color/variable viscosity from arbitrary variable density, surface tension, volumetric attributes and separated liquid meshes.[360] Do not describe the add-on as native Mantaflow, or promise that two domains push on each other. To show dye: inject two distinct tracer colors, render a debug surface with the attribute plugged into emission, compare mixing enabled/disabled, and check a side view of the interface. To claim immiscibility, require a solver explicitly supporting that physics and a separation/settling control; otherwise deliver a labeled visual approximation. For paint-like mixing, define the color model; a generic RGB blend is not physical pigment mixing.

### Cloth tearing: topology changes, not disappearing pixels

First decide whether the viewer needs a **precut scripted seam**, a force-driven tear, or only an appearance transition. Native Cloth sewing springs pull paired vertices together; they are not proof that Blender has dynamically fractured the fabric.[29] For a native directed tear, create disconnected sides with paired UVs and matching edge positions, then animate their boundary controls progressively along the seam. Preserve the shared pose/velocity at any release or mesh switch. Give the opened edge thickness or fibers only where visible. A dissolve or alpha mask cannot produce two independently moving flaps.

For stress-based rupture, SideFX documents Vellum Edge Fracture and breaking weld constraints; its examples compare behaviour at different resolutions/substeps.[369] This is an **external route**, not a Blender 4.5 checkbox. For a Blender handoff, import a baked mesh sequence with an appropriate topology-varying cache; do not assume shape keys can change vertex count. Check a UV stripe across the seam, silhouettes from both sides, newly exposed edge motion, and the same shot after transfer. Negative control: leave boundary pairs locked; no opening should develop. If release pops, repair rest positions and first free velocity before adding threads.

### A cinematic explosion as a computer-generated effect

This is wholly **digital VFX**. Sketch a readable expanding silhouette and layer a brief emissive flash, a slower opaque plume, diminishing embers and a separate dust/contact layer. Start with a bounded Blender gas domain and a simple animated source; choose the camera and a neutral reference object before resolution.[373][384] Solve the coarse bulk first, cache it, then add turbulence/detail: Blender gas Noise adds finer structure on top of the base motion and requires a matching cache.[385] Simulate or paint light spill on nearby set surfaces; a white compositor halo alone does not light the room. Change the graphic style by varying cadence, contour grouping and value steps, not by adding uniform detail everywhere.

Check a silhouette-only flipbook, exposure with the flash disabled, and the plume in front of **and** behind a foreground pole. The flash must read before the dust obscures it. If the plume looks tiny, give it scale cues and slower large-shape development before increasing noise; if the brightest area clips throughout, separate emission from smoke density and adjust the light/grade rather than crushing the whole shot. Deliver the density/temperature or render passes actually used, cache frame range and source frame rate. A convincing digital shot is not a measurement of a real blast.

### Sources

[29] https://docs.blender.org/manual/en/4.5/physics/cloth/settings/shape.html — Shape - Blender 4.5 LTS Manual
[360] https://github.com/rlguy/Blender-FLIP-Fluids/wiki/Limitations-of-the-FLIP-Fluids-addon — Limitations of the FLIP Fluids addon
[367] https://docs.blender.org/manual/en/4.5/physics/rigid_body/world.html — Rigid Body World - Blender 4.5 LTS Manual
[368] https://docs.blender.org/manual/en/4.5/physics/rigid_body/constraints/introduction.html — Introduction - Blender 4.5 LTS Manual
[369] https://www.sidefx.com/docs/houdini/vellum/breaking_tearing.html — Breaking and tearing
[371] https://github.com/rlguy/Blender-FLIP-Fluids/wiki/Domain-Attributes-and-Data-Settings — Domain Attributes and Data Settings
[373] https://docs.blender.org/manual/en/4.5/physics/fluid/type/domain/settings.html — Settings - Blender 4.5 LTS Manual
[384] https://docs.blender.org/manual/en/4.5/physics/fluid/type/domain/gas/index.html — Gas Settings - Blender 4.5 LTS Manual
[385] https://docs.blender.org/manual/en/4.5/physics/fluid/type/domain/gas/noise.html — Noise - Blender 4.5 LTS Manual
[388] https://docs.blender.org/manual/en/4.5/modeling/geometry_nodes/simulation/simulation_zone.html — Simulation Zone - Blender 4.5 LTS Manual
