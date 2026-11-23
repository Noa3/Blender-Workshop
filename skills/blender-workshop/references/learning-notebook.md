# Video, course and book studies

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [Course notebook: from a blockout to a rendered shot](#chapter-course-notebook)
- [Learn from a course without copying its project](#chapter-course-paths)
- [Environment film studies: from a floor plan to a shot](#chapter-environment-film-studies)
- [Video observations and production examples](#chapter-video-notes)
- [Surface and motion: what to borrow from three creators](#chapter-surface-motion-sources)
- [Modeling lessons from six supplied PDFs](#chapter-book-modeling)
- [What was actually studied?](#chapter-study-coverage)

<a name="chapter-course-notebook"></a>

## Course notebook: from a blockout to a rendered shot

Use these as exercises, not as lists of shortcuts. The four parts of Julien Kaspar's **Blender Beginner Tutorial** follow the same cube-shaped owl from blank scene to final lighting. All four official recordings were retrieved, their full audio processed locally into timestamped English speech notes, and six comparison frames from each part inspected. The following times refer to the original players. Audio notes are machine transcription, not official subtitles; the descriptions below are paraphrases. No third-party footage or transcripts are distributed. See also the [earlier video studies](learning-notebook.md#chapter-video-notes).

| Lesson and evidence | Transfer the decision rather than the old UI | Test it |
|---|---|---|
| **1. Blocking** — 02:02–02:22: Kaspar describes wings built from a cube, a plane for a feather, cylinders for feet; 03:28–03:43: mirror half the face about its origin. At 03:38 the image shows a half control cage; at 05:15 the wing sits proud of the body.[67] | Choose primitives by their *profile*; set the mirror plane before refining either half. For a lamp, separate body, handle opening and foot; for a bay, separate pier, spring and crown. | In untextured front and three-quarter views, the main volumes should still read. Move a vertex at the mirror seam and inspect it with clipping on and off. |
| **2. Modeling** — 00:36–01:03: slide before locally extruding the beak area. 01:24–01:46: bevel the box to catch light; add supporting loops if subdivision softens the edge too far. At 01:35 the hard body and smooth face read differently.[68] | Slide an existing edge to correct a proportion. Add a loop only where the surface has to hold a sharper transition. A machine housing need not be globally subdivided just because its grip is round. | Move a single large light across the edge. If the highlight wobbles on a flat panel, diagnose topology and normals before adding more cuts. |
| **3. Shading** — 01:14: apply a checker to expose UV distortion. 02:05–02:25: cut seams, unwrap, average island scale, then pack. At 02:32 both UVs and the checker-covered character are visible; at 04:54 the painted wing and atlas are visible together. Around 05:07–05:13 the artist calls out saving or packing the image.[69] | Test UV orientation and scale before painting. A gray render cannot tell you whether an atlas is stretched. Paint a distinct mark across a seam; avoid overlapping UVs where unique damage is required. | Inspect at target texel density, reopen with the source texture directory unavailable, then review distant mip levels in the target renderer. |
| **4. Rendering** — 00:35–00:54: model the curved floor-to-wall transition of a studio sweep. 01:11–01:35: decide distinct roles for warm key, larger cool fill, and narrower rim. 02:36–02:46: isolate diffuse lighting or highlights while adjusting the shot. At 03:00 a framed render and the separate lighting rig appear together.[70] | For a product shot use a curved sweep to remove an accidental horizon; for a real room keep its corners and motivate the key from an opening. Inspect the diffuse and reflection contribution separately before increasing exposure. | Freeze the camera, hide each light in turn, and compare the contact patch and the silhouette against the backdrop. |

**Practice assignment.** Run this sequence on one new prop: a ten-minute blockout with the three largest volumes; one revision from its side view; one checker/UV screenshot; a single-material lighting test; then textures and a final shot. The order is the transferable part of the owl course, not its art style. The architecture and prop labs exercise these decisions on different geometry.

### Additional video studies

**Generated/Procedural Textures – Blender Fundamentals**, produced by Dillon Gu. At 01:46–01:50 the narration changes Voronoi scale to obtain smaller cells; at 02:08 the cube shows a grayscale cellular pattern. At 03:03 a multicolored `Cells` result and Mapping panel are visible; around 03:21–03:35 the narration distinguishes color and scalar output. Audio transcribed locally across the full recording and six frames inspected.[71] **Exercise:** feed a cell mask into a ramp, inspect it unshaded, then reuse the mask for roughness rather than leaving random cell colors in the finished shader. The historical frame shows Blender 2.78.5: use the actual 4.5 feature, distance and color sockets, not the old `Cells` menu. `F1` and `Distance to Edge` answer different questions.[56]

**Geometry Nodes Fields: Explained!**, Blender, featuring Dalai Felinto. At 04:30 the older pebble node tree sits below its rendered result. At **08:46** a `Cube` feeds `Instance on Points`; a `Viewer` exposes the intermediate result, and the spreadsheet shows **432 instances** rather than a new solid terrain mesh. At **24:20** a largely empty band separates patches of pebbles; large/medium/small inputs and a named mask are visible on the group. This is a frame study, not a transcript of the full talk.[72] **Exercise:** replace the plant prototype with a cube while debugging distribution. Inspect point centers and mask boundaries first; only then put expensive species back. The talk demonstrates the 3.0 alpha transition, not a current socket reference. Use the developer's explanation for data vs. function flow and the 4.5 docs for the receiving field's context.[73][8]

**Further structured study, not claimed as watched:** Simon Thommes' *Geometry Nodes from Scratch* syllabus explicitly separates concepts from building procedural nature assets. Start with its public Basics material, then try a rock generator from a clean file before comparing a teaching file. Only the public course index was reviewed here; subscription lessons are not counted in the video studies.[66]

<a name="chapter-course-paths"></a>

## Learn from a course without copying its project

Choose one exercise and its failure test. The camera, assets and numerical results in the linked workshop labs are our own. Historical courses can teach a decision even when today’s controls are different. To find every listed lesson, position and evidence type, open `Study-Index.html` from the full package. The short [coverage note](learning-notebook.md#chapter-study-coverage) explains which sources were only indexed.

### 1. Build the silhouette before scattering detail

The Blender 3.0 Donut series is a project in 16 parts plus a learning-plan supplement.[110] Part 3 breaks apart duplicating the upper mesh, separating it and changing modifier order. The preview sequence moves from a top selection toward a separate edge.[116] Part 9 distinguishes the weight-controlled area from the instances scattered on it; the sampled frames show small repeated forms over the icing, not the exact value of a socket.[117]

**Try it on a different object:** duplicate the top faces of a plain ceramic lid into a separate enamel cap. Check in side view that the cap follows the dome without lifting off. Only then place speckles on its rim. Preview the mask without any speckles. If they appear in the center, diagnose the mask on the lid before turning down density; turning the seed until it looks right is not a fix. The [spacing exercise](spaces.md#chapter-spacing-field-study) gives a measured comparison of that decision.

**Which edition?** The author’s Blender 5.0 resource page links a new course, a troubleshooting guide and a shortcut sheet. Its eight listed lessons and its full-length compilation are not nine independent training topics and do not replace missing historical material.[126] The native examples in this workshop were tested in 4.5.9, not 5.0.

### 2. Match a camera before deciding what to model

The fSpy tutorial labels principal point, field of view, dimensions and depth as separate problems; its description also addresses cropped input.[123] Ian Hubert’s *Lazy Tutorials* are independent shortcuts, not a single project to follow in order.[114] The indexed narration around 0:24 in the depth-map lesson describes moving through a displaced still; it is not evidence of a complete 3D reconstruction.[119]

**Try it:** frame a doorway with simple boxes, using the camera crop you will actually deliver. Match two families of straight edges and check an independent third edge. Then slide the camera sideways. If the edge exposes a surface the reference never showed, model that return or restrict the move. For a locked shot, adding geometry behind the camera will not repair a bad camera match. See the [gallery camera lab](spaces.md#chapter-scene-and-architecture).

### 3. Diagnose a shadow edge separately from a dark subject

Blender Guru’s playlist contains an introduction, five principle lessons and a worked critique.[115] The size lesson and the creator’s companion distinguish direction, apparent source size, exposure and subject separation. A bigger apparent source changes the edge; raising power is not the same experiment.[120][127]

**Try it:** render one shadow that crosses a recognizable floor joint. Leave the camera, light direction and exposure alone; increase only the Sun Angle. Compare the width of the same transition in both images. In the workshop gallery it widened from **1.12 to 10.67 pixels** on the documented scan; those numbers belong to [that image pair](lab-notebook.md#chapter-advanced-labs), not to the video. If the width is right but the subject still disappears into the background, start a **separate** fill/rim or exposure comparison. For a shaft visible from the side, use the [three volume controls](lighting.md#chapter-light-field-study) instead.

### 4. Verify a transfer at the failing stage

The V6 transfer series has three pipeline lessons plus a separate animation-library lesson.[111] Part 3’s sampled frames show character views and another editor; its chapter list separates export and destination import. A Blender-only material preview does not prove a target shader or collider.[118] Diffeomorphic documents a different handoff: a `.duf` and same-named `.dbz` supply different information for mesh fitting. A missing counterpart should be investigated before repainting weights.[134]

**Try it with an asset you own:** export one prop or one two-bone test clip. Inspect one known dimension, one material boundary and one rotation in the destination. If the size is already wrong on import, correct the unit/axis handoff before changing keyframes. For gameplay, run a player-sized hit and a miss in the target level. The [service-lamp lab](game-assets.md#chapter-game-art) tests the actual GLB in Godot; it does **not** certify either tutorial’s character pipeline in Unity.

### 5. Decide whether a capture needs reshooting

In FreeMoCap’s 2022 walkthrough, the presenter separates overlapping views (13:10), the physical board-square size (29:45), frame-versus-time synchronization (32:25) and the Blender executable path at export (around 48:20). These are from nine selected windows of the creator-linked transcript, not a full viewing or current installation instructions.[121][124] In a separate missing-textures demo the scene is still magenta at 0:36 and 1:14; at 1:54 some materials are back but not all.[122]

**Try it:** save a copy at each boundary: source recording, calibration/reconstruction, Blender import and packaged asset. If the last stage alone fails, reopen the preceding result before reshooting. For missing textures, move a **copy** of the project to a new directory and check every material that uses an image, not just the first object that regained its color. No camera capture was made for this exercise.

### 6. Read a syllabus or product page for the right reason

| Decision | What the creator documents; what to check yourself |
|---|---|
| Practise acting or debug an actual joint? | Blender Studio’s outline moves from bouncing balls and follow-through to body mechanics (8 chapters, 13 videos). It is a study sequence, not evidence all lessons were watched.[132] Start with [the two-pivot landing](motion.md#chapter-motion-field-study): fix floor contact across a squash before adding limbs. |
| Inspect a rig or polish a gait? | VFX Grace separates modeling, texturing, grooming, rigging and animation.[129] The rigging and animation syllabi each expose 29 numbered lessons; the first two in each are labeled free.[130][131] If a joint breaks in a held pose, return to rigging. If both extremes hold but the planted foot slides between them, inspect its world-space path. Paid lesson footage was not used. |
| Paint a cloth mask or tune the solver? | Schaken’s three linked lessons concern setup, colliders and weight maps for a **Unity** cloth runtime.[125] Select the intended moving vertices first, then compare a pinned and a free point in the application that simulates them. A painted mask in Blender is not a Unity simulation test. |
| Need a flow map or the shape of a liquid volume? | The producer of Cell Fluids describes a displaced 2D grid and a flow-map handoff.[133] For shallow water, test whether the map moves a surface marker in the expected direction in the receiver. If two layers of water must cross at the same horizontal position, a single-valued height field cannot describe that shape. No add-on or engine integration was run here. |
| Saw a tool trailer and need a repeatable procedure? | The RBDLab manual explains the target collection and identifies its documented Blender version.[128] Verify the target collection on a neutral test scene, use the manual matching the installed release, and keep the original. A trailer or product price is not a test. |

These are practice decisions, not endorsements, downloads or proof of compatibility. The [field studies](workshop-index.md) describe which native workflows were actually run.

### Sources

[110] https://www.youtube.com/playlist?list=PLjEaoINr3zgFX8ZsChQVQsuDSjEqdWMAD — Blender 3.0 Beginner Donut Tutorial (OLD)
[111] https://www.youtube.com/playlist?list=PLhiuav2SCuvc-wbexi2vwSnVHnZFwkYNP — [V6] Export your Koikatsu waifu to Blender and more
[114] https://www.youtube.com/playlist?list=PL4Dq5VyfewIxxjzS34k2NES_PuDUIjRcY — Lazy Tutorials
[115] https://www.youtube.com/playlist?list=PLjEaoINr3zgH9vCr47kSS5W8PEJBNIiwK — Lighting Course
[116] https://www.youtube.com/watch?v=7wKnPclzYY8 — Blender 3.0 Beginner Tutorial Part 3: Modifiers
[117] https://www.youtube.com/watch?v=4WAxMI1QJMQ — Blender 3.0 Beginner Tutorial Part 9: Geometry Nodes
[118] https://www.youtube.com/watch?v=4Z02sY6Y8GI — [V6] Export your Koikatsu waifu to Blender and more (part 3 of 3)
[119] https://www.youtube.com/watch?v=cabSoB28aOM — Animating Environments with Depth Maps - Lazy Tutorials
[120] https://www.youtube.com/watch?v=xLcIZTFh2Kk — Lighting for Beginners - Size (Part 2/5)
[121] https://www.youtube.com/watch?v=GxKmyKdnTy0 — FreeMoCap Rough Cut Tutorial/Walkthrough/Brain Dump (Nov 2022)
[122] https://www.youtube.com/watch?v=rWrj3jud0w8 — Fix Pink Models in Blender
[123] https://www.youtube.com/watch?v=daiMOYR8GS8 — BEST way to use fSpy | ALL Options explained | FULL camera matching workflow with Blender
[124] https://share.descript.com/view/vsqpqBJ9UNi — FreeMoCap: creator-linked transcript, selected windows
[125] https://schaken-hub.com/Schaken/GPU_Cloth_Physics/wiki/Home — Schaken: GPU Cloth Physics, training index and Unity runtime
[126] https://www.blenderguru.com/posts/blender-donut-v5-tutorial — Blender Guru: Blender 5.0 Beginner Donut Tutorial and resource guide
[127] https://www.blenderguru.com/posts/2019/lighting-mastery — Blender Guru: Lighting Mastery Series, written companion
[128] https://befxstudios.com/documentation/RBDLab/en/introduction — BEFX Studios: RBDLab documentation and version requirements
[129] https://www.vfxgrace.com/product/tutorial-bundle — VFX Grace: creature training syllabus
[130] https://www.vfxgrace.com/product/rigging — VFX Grace: rigging curriculum
[131] https://www.vfxgrace.com/product/animation — VFX Grace: animation curriculum
[132] https://studio.blender.org/training/animation-fundamentals — Blender Studio: Animation Fundamentals syllabus
[133] https://superhivemarket.com/products/cell-fluids — Shahzod: Cell Fluids, shallow-water solver and flow-map handoff
[134] https://github.com/Diffeomorphic/import_daz/wiki — Diffeomorphic: DAZ Importer, mesh fitting and source files

<a name="chapter-environment-film-studies"></a>

## Environment film studies: from a floor plan to a shot

The two cases below are based on timestamped frame samples from the public recordings. They are **visual observations**, not transcripts or claims that the entire lectures were watched. The exercises are our proposed way to transfer the decisions. No frame proves light powers, physical dimensions or the contents of an offscreen node graph.

### The process behind architectural visualization

Filippo Zorgno and Tommaso Sergi, Blender Conference 2023.[78]

| Time | Visible in the recording | Try this on a different building |
|---|---|---|
| **05:55** | The slide compares a render and a later photo of the same residential building. Both show the dark central wing, projecting balconies and planted frontage.[78] | Place two similarly framed views at the same width. Mark roofline, outer balcony edge and ground contact. Correct massing or camera position before tuning the surface color. |
| **10:00** | A white building mass is presented beside close facade photographs: slab edges, a balcony railing and vertical cladding strips.[78] | Build one gray bay. Hide the slab, railing and cladding in turn; spend geometry first on the part that changes the silhouette from the output camera. |
| **15:20** | A figure is seen from behind at ground level and a bench is visible to the right; planted space and buildings surround the courtyard.[78] | Add a pedestrian-height view even if the deliverable is an aerial still. Check where circulation and seating read as distinct spaces. This does not tell us which navigation system the speakers used. |

### Interior Visualization in Blender under 1 hour.

Lech Sokolowski, Blender Conference 2018.[79]

| Time | Visible in the recording | Try this on a different room |
|---|---|---|
| **04:40** | Wall geometry is extruded above a still-visible floor plan; the drawing includes furniture symbols.[79] | Build only walls and a doorway, then compare in top view. Verify a known length before adding anything that relies on scale. |
| **13:30** | The unfurnished flat-roofed shell is inspected obliquely from outside. A wide front opening exposes the floor; a side opening is also visible.[79] | Save this inspection view. Check the return, sill, lintel and floor junction before cabinets or curtains can hide a broken opening. |
| **32:00** | The main camera view shows upper cabinets and two chairs. A second working viewport shows the same kitchen area from another angle.[79] | Keep the first viewport locked to the output camera; move a chair in the other view. Decide from a thumbnail whether the two backs still separate in silhouette. |

**Version and method boundary:** Use the 2018 lesson for staging and inspection, not present-day menu positions. A separate 4.5 camera exercise compares shift with rotation; the manual shows their different projection effects.[23] Neither recording is evidence that its author used the lens shift, sun angle or material setup of our [gallery](spaces.md#chapter-scene-and-architecture).

<a name="chapter-video-notes"></a>

## Video observations and production examples

These are original, brief summaries. A film frame demonstrates composition, not the nodes, lamp positions or shader values that produced it. The manual and separate Blender tests supply technical cross-checks. See the [numbered source register](sources.md).

### Intro to Shading – Blender 2.80 Fundamentals (Blender, produced by Dillon Gu)
**Review method:** Twelve time samples from the publicly available HD video; relevant node links enlarged in the original frames. No transcript quotations.[41]

- **00:42 → 01:08:** First the Principled BSDF output feeds `Material Output → Surface`. Later the material “Green” shows a green Base Color field; the selector lists “Green” and “Material.” **Apply:** If an edit has no visible effect, check the material datablock actually assigned to the object and its output connection before changing lights or exposure.[41]
- **02:29:** An image is loaded in the World graph, but its Color output is not connected. A **Background** node feeds the **World Output** Surface. **Exercise:** Place an image as a visible reference, then separately inspect its role in the shader. An editor thumbnail does not prove a texture lights the world or colors the object.[41]
- **Version boundary:** This is 2.80. Object material, world and output remain separate concepts; do not transfer old Principled UI groups, names or defaults blindly to 4.5.[3][41]

### Trace Images into Grease Pencil – Blender Today (Blender channel)
**Review method:** Twelve HD frame samples from the demonstration of then-in-development 2.91, including the operator panel and color picker at original resolution. This is tracing an image, **not** camera-driven contour generation with the Line Art modifier.[15][42]

- **00:52:** `Trace Image to Grease Pencil` shows `Color Threshold` and `Turn Policy` on the Blender wordmark. **Apply:** For your own anime emblem, load a high-contrast black-and-white drawing as an Image Empty. Change only the threshold first and inspect letter counters or eye shapes. Do not trace arbitrary photos at maximum resolution: the manual warns of unnecessarily dense strokes.[42][43]
- **02:02 → 02:33:** The material color picker is followed by a blue-and-red version of the mark with a noticeably different visual read. **Apply:** Approve contours and negative spaces before choosing fill and stroke colors. On a character, trace just the emblem or selected eye/costume details; the 3D outer contour is a separate job.[42]
- **Version boundary:** Use 4.5 documentation for current options such as `Radius`. Historical panel values are not recommended settings. Tracing was studied from the video and manual; the rendered 3D mask uses modeled color strips instead.[42][43]

### Extrude – Blender 2.80 Fundamentals
**Frame evidence, 04:23–04:41:** The top of a shallow seat slab is divided into nine faces. Around **04:28**, the back row of upper faces is selected; around **04:31**, four separate underside corner faces join the selection. In one operation `Extrude Along Normals` makes a continuous backrest above and four legs below.[46] Face selection is the key decision: translating all faces along world Z would be different. **Rebuilt in Blender 4.5.9 LTS:** Seven selected faces, then three upper and four lower cap faces at the expected heights; see [Form and topology](modeling.md#chapter-modeling).

### Three Point Lighting – Blender 2.80 Fundamentals
**Frame evidence:** Around **00:50** the key shapes Suzanne's forehead and eye region from the upper left. The **01:15/01:20** comparison shows fill revealing the dark side. Around **01:30**, isolated backlight leaves little besides a rim along skull and ears. For the second point light the panel shows 1000 W around **03:33** and 32.2 W around **03:56**; the shadow side is readable again in the latter image.[47] **Apply:** Lock camera and exposure, enable each lamp separately and name the part of the image it explains. Wattages from this shot are not a recipe.

### Playing with Grease Pencil: an Adventure in 2.5D – Sharon Snow
Blender Conference 2023 talk. The demo status bar reads Blender 3.6.2. The review examined recorded frames, not a speaker transcript.[44][45]

- **14:24/14:30:** An oblique working view reveals gaps between drawn landscape elements. From the camera, dark foreground shapes frame a bright meadow. For a 2.5D set, check spacing from the side and overlap from the delivery camera.[45]
- **15:38/15:46:** After a point light is selected, a cyan highlight appears on the top of a previously uniform blue head. Black facial lines remain legible. Compare your flat color with and without local light; the frame does not specify a mandatory power or shader.[45]
- **16:02/16:50:** First, key-light arrows and a drawn shadow shape sit beside the character image. Later, a blue character's eyes and mouth are precisely drawn while the line under the cheek trails off. **Exercise:** Sketch the broad intended shadow on a still, then interrupt exactly one outer line. Check whether color contrast carries the form and the eyes still hold attention.[45]

### Sintel – official trailer (Blender Foundation / Durian)
**Review method:** Twelve frames from the freely offered original video (720p), not a plot summary or transcript. Times refer to the short trailer, **not** the feature film.[38][39]

- **00:08:** A relatively dark figure reads against light-gray snow/fog planes of similar value. **Exercise:** Desaturate the background and compress its value range; judge face and outline at thumbnail size. This does not identify a particular volume shader.[39]
- **00:26:** Two flying silhouettes of very different sizes share a warm sky. The smaller reads despite sparse detail because open space separates it from the larger. **Exercise:** Test the action line first with just two black shapes and a background.[39]
- **00:38:** A small dark figure interrupts layered dunes. Alternating bright ridges and darker slopes give depth without filling foreground and background with texture detail. **Exercise:** Start with three coarse terrain masses, one directional light and a figure for scale. Add sand detail later.[39]

**Additional production source, not a video review:** Blender Studio's *Charge* overview lists shot files, a “Reference vs Final” piece and a “Quadsplit Edit Progression” piece. Use the overview to select one lit shot and its development stages for a future study. Its listing is not evidence that these contributions were watched or their `.blend` files inspected here.[40]

<a name="chapter-surface-motion-sources"></a>

## Surface and motion: what to borrow from three creators

Start with the problem, not the playlist. For a mark that slides across a moving part, use [Texturing](materials.md#chapter-texturing-workflow). For a mark that stays put but a part that moves badly, use [Animation](motion.md#chapter-animation-workflow). The same gauge lets you tell those faults apart.

**How to read these notes.** A *narration excerpt* supports what the speaker said in that passage. A *chapter start* is a place to open the video, not a claim that every operation was observed. The ten selections below are not a complete viewing of the channels or their Shorts. The exercises and the tide gauge are original workshop work. No creator's rig, footage, texture or project file is needed.

### Blender Inferno — decide where a surface can break

| Source and evidence | What to take to the workbench |
|---|---|
| Cylinder UVs in 4.5 — narration excerpt. Even an image that repeats can show a join where the UV layout interrupts the pattern; the speaker discusses cylinders such as limbs and trunks.[298] | Mark a longitudinal seam away from the main view and separate the caps. Unwrap, apply a numbered checker, and inspect both sides of the join. **Check:** a number reads upright and the checks stay roughly square. A seamless image cannot correct stretched UVs. |
| Normal maps in 4.3 — published chapters: map setup **02:49**, OpenGL **03:54**, DirectX **05:03**.[302] | For a tangent normal map, set the image to Non-Color and pass it through a Normal Map node. Compare a known raised groove under one grazing light. If the source uses the opposite Y convention, invert **green only**, before decoding. Do not compensate with negative bump strength.[12] |
| Texture painting in 4.3 — published chapters: UV unwrap **04:51**, paint setup **05:46**, painting with textures **08:44**.[303] | Separate the brush texture, which shapes the stroke, from the target image, which stores it. Put one unmistakable stroke on a copy; save or pack that image, reopen, and find the stroke on the same face. |
| Voronoi in 4.5 — narration near **05:38** uses Distance to Edge with close Color Ramp stops and uses the mask to mix colors.[304] | Preview the mask alone. Change feature scale to change cell size; change the ramp to change border thickness. Check the material from the delivery camera before sending the mask to more sockets. A warning stripe that must hit an exact spot is a UV job, not a Voronoi job. |

### Ryan King Art — make each map answer one question

| Source and evidence | What to take to the workbench |
|---|---|
| *How to Texture Bake Procedural Materials in Blender (Tutorial)* — chapter listing and indexed narration excerpt about the destination image and UVs. Chapters start at **06:58** for color, **11:47** for roughness and **13:17** for using the baked texture.[307] YouTube's metadata confirms the author and title, not the procedure.[310] | Keep the editable shader. Bake to a different named image for each channel; then disconnect the original inputs on a duplicate and use **only** the baked images. Compare the same face under the same light. A color map is not a substitute for a roughness map. |
| Metallic and edge-wear painting — published chapters separate saving the first map (**07:55**), the edge-wear node setup (**08:25**), painting the wear (**15:11**) and baking (**17:30**).[308] | Decide where wear could actually occur: choose a touched corner and protect a recessed one. Paint the mask, preview it as grayscale, and save it. Use it to reveal the substrate where the coating is missing; do not make every geometrical edge shiny. |
| Tileable texture maps — published chapters distinguish the roughness bake (**06:40**), testing the new material (**08:00**) and making the images tileable (**09:34**).[309] | Lay the result out in a 3-by-3 repeat. Inspect the middle tile's four borders in **each** map: roughness can reveal a seam even when color matches. Repair the maps in registration and repeat the grazing-light check. A completed bake does not guarantee a tileable image. |

### Jamie Dunbar — choose which motion problem you have

| Source and evidence | Decision and check |
|---|---|
| *Motion Capture - Retargetting* — published chapters cover Auto-Rig Pro (**01:58**), the rest pose (**13:35**), retargeting (**15:25**) and FK/IK (**16:42**).[299] | **Different skeleton:** map source to target roles, align their reference poses, then transfer. Before tweaking curves, compare one neutral frame and one planted foot. If limbs consistently twist in the same direction, check bone axes and the rest pose first. |
| *Motion Capture - Animation Layers* — the opening narration distinguishes adapting a transferred performance from retargeting it in the first place.[305] | **Right skeleton, wrong pose:** preserve the base Action; test one reversible correction, e.g. a hip offset during contact. Mute the correction, then re-enable it and compare the planted foot. Do not rebuild the bone map to fix one pose. |
| *Motion Capture - combining animations* — published chapters: combining clips **11:20**, creating an offset **11:50**, lowering the hips **16:45**.[306] | **Two good takes, bad join:** match travel direction, root position and support foot before blending. In the native NLA Editor, place strips referencing your own Actions; inspect the frames before, during and after the transition. A wider blend cannot fix two incompatible foot plants.[295][300] |

Dunbar uses third-party tools, including **Auto-Rig Pro** and **Animation Layers**. The workshop's native Actions/NLA exercise is an alternative way to study the decisions, **not** a reproduction or compatibility test of those add-ons.[299][305][306]

### One experiment that joins the routes

For the cuboid UV, gloss, chipped brick, clay, shared atlas, procedural loop and facial-capture selections, see [Seven source lessons](lab-notebook.md#chapter-surface-performance-decisions). They are not counted among the ten on this page.

Generate the scene with [the Tide Register exercise](portable-use.md#tide-register) in Blender 4.5 LTS. In camera view compare frames **10** and **34**. The light band should stay near the tip of the painted needle at both extremes; the brass spindle should stay in the same place. Play **1–48**, not 1–49. Frame 49 is there to inspect the closure pose; playing it as well would count the starting pose twice.

**What was tested:** the saved example was reopened in Blender 4.5.9 LTS. Its visible upper face uses its named UV map and two packed images. Roughness samples from the body and band were **0.2784** and **0.7020**. Across the sweep, measured spindle drift and variation during the holds were both **0** at the checker's reported precision. A 48-frame camera sequence was rendered. These are results for the supplied needle, not for the creators' files. The cylinder, hand-painting, character retargeting and clip-assembly exercises above are manual variants: `untested`.

For why the two maps differ, follow [the bake and reopen exercise](materials.md#chapter-texturing-workflow). For why a matched end pose is not enough, follow [the loop-boundary exercise](motion.md#chapter-animation-workflow). Numbered references resolve in the [source register](sources.md).

### Sources

[12] https://docs.blender.org/manual/en/4.5/render/shader_nodes/vector/normal_map.html — Normal Map Node - Blender 4.5 LTS Manual
[295] https://docs.blender.org/manual/en/4.5/editors/nla/strips.html — Blender 4.5 LTS: NLA Strips
[298] https://www.youtube.com/watch?v=VKqOFMr6Ns0 — Blender Inferno: How to UV Unwrap a Cylinder in Blender 4.5 for Beginners!
[299] https://www.youtube.com/watch?v=AutNCxcK0Xc — Jamie Dunbar: Motion Capture - Retargetting
[300] https://docs.blender.org/manual/en/4.5/editors/nla/sidebar.html — Blender 4.5 LTS: NLA Sidebar
[302] https://www.youtube.com/watch?v=DxSo5NTwHW4 — Blender Inferno: How to Apply Normal Maps Properly in Blender 4.3...
[303] https://www.youtube.com/watch?v=U-y0WDHhhqk — Blender Inferno: Blender 4.3 Texture Painting with Textures for Beginners!
[304] https://www.youtube.com/watch?v=X7NXotJUkUA — Blender Inferno: The Voronoi Texture in Blender 4.5 - In Depth Blender Lesson
[305] https://www.youtube.com/watch?v=uIf1kNTxvZo — Jamie Dunbar: Motion Capture - Animation Layers
[306] https://www.youtube.com/watch?v=64SDRd6zkDY — Jamie Dunbar: Motion Capture - combining animations
[307] https://www.youtube.com/watch?v=B2kFeMBBBjc — Ryan King Art: How to Texture Bake Procedural Materials in Blender (Tutorial)
[308] https://www.youtube.com/watch?v=bR4HtqxA9tk — Ryan King Art: Texture Paint Metallic Maps and Edge Wear (Blender Tutorial)
[309] https://www.youtube.com/watch?v=VAjGtE678o0 — Ryan King Art: Bake Procedural Materials to Tileable Texture Maps (Blender & Gimp Tutorial)
[310] https://www.youtube.com/oembed?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DB2kFeMBBBjc&format=json — YouTube oEmbed: author and title of the procedural baking tutorial

<a name="chapter-book-modeling"></a>

## Modeling lessons from six supplied PDFs

**Start with the plate in B2 if you are new to Edit Mode.** If you already have a model that looks right but fails a test, skip to [Build and check a functional mesh](modeling.md#chapter-modeling-checks). A bowl needs a bottom; a cable opening must **not** have one. The same modeling operation can be right for one and wrong for the other.

**How to use the references:** `B1`–`B6` identify the supplied files. All page numbers below are **physical PDF pages, starting at 1**, including covers and front matter. They are not the numbers printed on the pages. “Book” reports an inspected passage; “Plate” reports what an illustration shows; numbered links refer to documentation or publisher identification. “Try” and “Check” are workshop instructions, not the authors’ claims. The original PDFs and their artwork are not included. This is a selection of lessons, not a claim to have read or verified every page.

| If the problem is… | Start here | Stop when… |
|---|---|---|
| A rim collapses when smoothed | B2 pp. 126–140; B4 pp. 278–283 | The coarse control mesh still edits easily and the side profile holds at delivery size. |
| A repeated feature drifts off its circle | B1 pp. 327, 333–337; B3 p. 145 | There are the specified number of distinct centers, at one radius and even pitch. |
| Two halves touch but may not be joined | B3 p. 36; B5 pp. 49–51 | The **evaluated** closed test shell has one connected component and no open seam. |
| A recess should admit a cable or show daylight | B4 pp. 258–260; B3 p. 148 | The opening has an inner wall, no end cap, and the clearance test passes. |
| A branch changes shape badly when bent | B6 pp. 29, 118; B1 pp. 239–243 | The intended region bends while its neighbor and rigid attachments stay put. |

#### B1 — Sandra Kolar (SaTales), *Beginner’s Guide to Blender*, January 2026 file

**Where it fits.** The 363-page file starts its tutorials at chapter 24, not chapter 1. Its contents (p. 5) repeat both 26 and 30 for different subjects. Use subject and page, not chapter number alone. The bucket starts on p. 110 and names 4.2.1; the plant starts on p. 175 and names 4.3.2; the balloon names 4.4.0 on p. 274. The flower and scatter lessons start on pp. 327 and 338 and explicitly name 5.0. The 2026 date on the cover is not the version of every screenshot.

- **Bowl, pp. 7, 10–14.** The book uses an orthographic through-selection to remove half a sphere, extrudes along normals and bevels the rim. Try the sequence in side view; turn X-Ray off afterwards. Before shading, inspect a cross-section: there should be an outside, an inside and a rim joining them. Four bevel segments are a choice for that example, not a target for all edges. For a variable shell, keep Solidify live, set the offset towards the side you can afford to move, and measure where the wall is tightest: even-thickness options are approximations.[1][49]
- **The orientation overlay, pp. 12–13.** Do not reject a mesh because its outside does not turn blue. The manual describes front/back face colors; the factory themes inspected in the two lab runtimes had **transparent front** and **visible red back**. Orbit a known face with Overlays and Face Orientation enabled; check unexpected back faces, not a required front color.[149] On a closed shell use Edit Mode → Mesh → Normals → Recalculate Outside; on an isolated sheet decide which side is meant to face out instead of relying on an automatic inference.[140]
- **Repeated petals, pp. 327, 333–337.** The author edits one source and adjusts count and radius in the new **Array → Circle**, not Array Legacy. Use this when the spacing matters; do not place copies by eye. The 5.0 and 5.3 manuals describe the circular layout; 4.5 instead documents a rotating Object Offset.[146][147][51] The [dial-marker exercise](modeling.md#chapter-modeling-checks) measures the same pattern by both routes without copying the flower.
- **Mushroom rig, pp. 239–243.** The deciding check in the book is moving the bone: the eyes should not follow an unrelated bone, but should follow the head. Apply that logic to your asset: pick a rigid point, one joint that should carry it and one that must not; test both. A weight color refers to a particular group, not to whether the whole rig works.

- **Forest path, pp. 338–350, 351–363.** Put the pine's origin at the trunk base before scattering it. On p. 362 the painted path makes the exclusion visible. Try changing the seed: inspect the new tree **centers** against that path, then check whether branches overhang it. A density mask can solve the first problem without solving the second. The 5.0 *Scatter on Surface* modifier is version-specific.[153] The [spacing study](spaces.md#chapter-spacing-field-study) provides a separate, measured exclusion example.

#### B2 — Sandra Kolar, *A Beginner’s Guide to Blender*, 2025 part one

**Where it fits.** This 298-page file covers the foundation, numbered 1–23, and ends with a pumpkin (pp. 273–298). Its index also uses 21 twice (p. 6). Read this before B1. They revisit tools, but the January PDF is a continuation with different projects, not a replacement copy of the beginner chapters.

- **Extrusion, pp. 57–74.** Practice on two neighboring faces. Extrude a **region** when it must remain a single ledge; use **individual faces** for separate bosses. View the shared edge from the side: two unwanted side walls between neighbors mean you chose the wrong operation. “Along normals” is not the same as translating everything along world Z; check face directions before adding distance.
- **Plate, pp. 126–140.** Make one circular profile, work from a coarse cage, toggle Subdivision off to see what you are editing, and compare adjacent viewport levels before keeping the higher one. The insets and merge-to-center on pp. 137–139 close the plate. On a cable sleeve that same merge would obstruct the passage: connect the inner and outer profiles around the annulus instead.[61][62] Judge the outline at the intended size, not by the level number.[37]
- **Loop cut, pp. 88–91.** Put a supporting loop near a rim to control its roll under subdivision. If the loop unexpectedly stops, inspect the face where the preview ends; triangles and n-gons interrupt the usual quad strip.[145] Do not densely subdivide the entire object to repair one corner. A center pole can be fine on a flat cap; keep it away from the visible rolled shoulder or a bending joint.

- **Pumpkin and stem, pp. 273–283.** Set up repeated longitudinal bands before pulling out lobes. Use a small proportional-editing falloff so one lobe does not move its neighbor. The stem needs to move independently without tearing the fruit. On p. 280, separating a selection makes a new **object**, not a new collection: in Edit Mode use **P → Selection**, then move the stem in Object Mode to test it.[151]

#### B3 — James Chronister, *Blender Basics*, classroom tutorial, fifth edition (2017)

**Date it correctly.** The edition and author are identified on p. 2; p. 7 explicitly says **Blender 2.78**. Use the exercises for shape and diagnosis, not as a modern menu map.

- **Coincident geometry, p. 36.** After an accidental extrusion, a surface can look unchanged but contain extra geometry. The old *Remove Doubles* instruction becomes Edit Mode → Mesh → Clean Up → **Merge by Distance**. Select the suspect seam only, start with a tolerance smaller than the narrowest intentional gap, and compare counts before and after.[136][139] This is not a blanket fix for coplanar faces, separate objects, intersecting walls or reversed winding. If you just made the unwanted extrusion, undo it rather than guessing which vertices to weld.
- **Live tools, pp. 145–148.** Object Offset repeats a form; Bevel changes its edge profile; Solidify builds a wall from a surface. Keep the generator and any cutter editable. Toggle each stage on its own and measure the final mesh. Applying a modifier is not the same as applying object scale; the latter changes the object's transform representation and can affect dependencies.[141] Preserve a source copy, especially for a rig or shared mesh. Do not use Edge Split merely to imitate a smooth highlight: it physically separates geometry; choose the shading tool when the shape is already correct.[148]

- **Door hinge, p. 33.** A door can look correctly placed until you try to open it. Select the hinge edge in Edit Mode and snap the cursor to the selection. In Object Mode use **Set Origin → Origin to 3D Cursor**, not *Geometry to Origin*.[152] With a single selected door and the pivot set to Median Point, rotate about the vertical hinge axis. The hinge edge must stay still while the opposite edge swings.

#### B4 — *Blender 3D: Noob to Pro*, historical Wikibooks compilation

`BlenderDocumentation4.pdf` is **not the Blender 4 reference manual**. The cover identifies Wikibooks (p. 1); both the extrusion and smoothing modules explicitly label themselves **2.57** (pp. 262, 278). Treat versions at the module level rather than assigning the entire 2,254-page compilation one target.

- **House, pp. 249, 257–260.** Put the pivot at ground level if the base must stay on the floor while the house scales. The exercise then creates shallow inward extrusions on selected wall faces. That is useful relief, not automatically an open window. For a through-window in a thick wall, use an editable through-cutter or bridge the corresponding front and back loops. From inside, inspect sill, jambs and head; the back wall should not close the opening.[50][62]
- **Simple person, pp. 278–283.** Compare the coarse cage, the subdivided silhouette and smooth shading separately. Interpolation changes highlights; subdivision adds geometry and can round off a form.[37][148] The text's **Ctrl-N** to recalculate normals (p. 282) is historical. Use the named command **Recalculate Outside** (Shift-N in the modern default keymap), not the old shortcut.[140] Do not assume an old right-click selection diagram matches your active keymap.

- **Support loop or crease, pp. 202–203.** Compare two copies of a rounded block at the same subdivision level. Add and slide a loop on one; crease the existing edge on the other. Use the loop when you need another row of vertices to shape the shoulder; keep the crease when only that edge needs a sharper transition. Inspect both the highlight and the outline.[37][145]

#### B5 — Oliver Villar, *Learning Blender: A Hands-On Guide to Creating 3D Animated Characters*, third-edition sample

**What is actually supplied.** The title and edition are on p. 6; copyright is 2021 (p. 7), and the author identifies Blender **2.83** on p. 30. The instructional excerpt is **chapter 3, “Your First Scene in Blender,” PDF pp. 36–61** (printed pp. 41–66). P. 62 is a blank divider; pp. 63–89 are the index. The contents and index name later character-modeling and rigging chapters, but they do not supply those lessons.

- **Shared data, pp. 44–47.** Name the object and mesh separately. If editing one repeated piece changes all its siblings, check whether they share the same mesh. Keep the link for identical manufactured parts; make the mesh single-user before editing one special part. Moving an object is not a test for linked mesh edits.[52]
- **Shading and stack order, pp. 48–52.** The sample distinguishes smooth shading from adding geometry and gives Mirror-before-Subdivision as an example rather than a universal stack. For a continuous symmetric surface, have Mirror merge a clean center loop, then let Subdivision smooth the joined result.[48][37] If a seam persists, isolate it **with subdivision disabled**. A narrow crease may be a support loop; two coinciding boundaries are a connectivity defect. The fixture in the next chapter distinguishes them without guessing from a render.

#### B6 — *Unreal Engine 5 Character Creation, Animation and Cinematics*, color-image companion

The ISBN in `9781801812443_ColorImages.pdf` matches Packt’s companion repository, which identifies the separate color-figure PDF.[150] The 267-page attachment has chapter dividers and illustrations. It is **not** the instruction text. Use it to ask what changed between pictures, not to reconstruct undocumented settings.

- **Plate, p. 29:** side-by-side plant junctions and a before/after at the base show changes in the transition between surfaces; the brush outline is visible. **Try:** block a stem and one branch, inspect their junction from the reverse side, and soften only the abrupt intersection. The plate does not establish the brush, strength, voxel size or whether UVs survived. Voxel remeshing can help a sculpt, but does not design edge flow for an animated joint.[6][144]
- **Plate, pp. 38, 42:** the first juxtaposes a flat map and globe, then shows a highlighted loop on a wireframe; the second shows an export dialog. Neither verifies the UVs or tangents on an imported asset. **Check:** apply a directional checker at delivery resolution; look at the back and underside, then inspect the actual imported result. See [UV and bake diagnostics](modeling.md#chapter-modeling).
- **Plate, p. 118:** a bent two-segment form is shown with bone overlays, a 0–1 color scale and Auto Normalize enabled. **Check:** pose the joint both ways, inspect the inner fold and outer silhouette, and check a nearby point that should not move. If the wrong region moves, inspect group membership and weights first. If the intended weights move too few rows of vertices to describe the bend, revise the cage. The picture supplies neither numeric per-vertex weights nor a passed deformation test.

### Carry the decision, not the keystrokes

State the target Blender version, write down the geometric result, find the operation by name, then test **one** observable property on a copy. The general workshop remains based on 4.5.9 LTS. Blender’s download page listed 5.3.0 when this edition was checked; only the explicitly named exercises were cross-tested.[135] The screenshots are not a promise of matching menus, colors, engine behavior or speed. For an exercise with actual pass/fail examples, go to [Build and check a functional mesh](modeling.md#chapter-modeling-checks).

### Sources

[1] https://docs.blender.org/manual/en/4.5/modeling/modifiers/generate/bevel.html — Blender 4.5 LTS: Bevel Modifier
[6] https://docs.blender.org/manual/en/4.5/modeling/meshes/retopology.html — Remeshing - Blender 4.5 LTS Manual
[37] https://docs.blender.org/manual/en/4.5/modeling/modifiers/generate/subdivision_surface.html — Subdivision Surface Modifier - Blender 4.5 LTS Manual
[48] https://docs.blender.org/manual/en/4.5/modeling/modifiers/generate/mirror.html — Mirror Modifier - Blender 4.5 LTS Manual
[49] https://docs.blender.org/manual/en/4.5/modeling/modifiers/generate/solidify.html — Solidify Modifier - Blender 4.5 LTS Manual
[50] https://docs.blender.org/manual/en/4.5/modeling/modifiers/generate/booleans.html — Boolean Modifier - Blender 4.5 LTS Manual
[51] https://docs.blender.org/manual/en/4.5/modeling/modifiers/generate/array.html — Array Modifier - Blender 4.5 LTS Manual
[52] https://docs.blender.org/manual/en/4.5/scene_layout/object/editing/duplicate_linked.html — Duplicate Linked - Blender 4.5 LTS Manual
[61] https://docs.blender.org/manual/en/4.5/modeling/meshes/editing/face/inset_faces.html — Inset Faces - Blender 4.5 LTS Manual
[62] https://docs.blender.org/manual/en/4.5/modeling/meshes/editing/edge/bridge_edge_loops.html — Bridge Edge Loops - Blender 4.5 LTS Manual
[135] https://www.blender.org/download — Blender Foundation: release download page (5.3.0 at review)
[136] https://docs.blender.org/manual/en/4.5/modeling/meshes/editing/mesh/cleanup.html — Clean Up - Blender 4.5 LTS Manual
[139] https://docs.blender.org/manual/en/5.3/modeling/meshes/editing/mesh/cleanup.html — Clean Up - Blender 5.3 Manual
[140] https://docs.blender.org/manual/en/4.5/modeling/meshes/editing/mesh/normals.html — Editing Normals - Blender 4.5 LTS Manual
[141] https://docs.blender.org/manual/en/4.5/scene_layout/object/editing/apply.html — Apply Transforms - Blender 4.5 LTS Manual
[144] https://docs.blender.org/manual/en/5.3/modeling/meshes/retopology.html — Remeshing versus deformation topology - Blender 5.3 Manual
[145] https://docs.blender.org/manual/en/4.5/modeling/meshes/tools/loop.html — Loop Cut - Blender 4.5 LTS Manual
[146] https://docs.blender.org/manual/en/5.0/modeling/modifiers/generate/array.html — Array Modifier - Blender 5.0 Manual
[147] https://docs.blender.org/manual/en/5.3/modeling/modifiers/generate/array.html — Array Modifier - Blender 5.3 Manual
[148] https://docs.blender.org/manual/en/4.5/scene_layout/object/editing/shading.html — Shading - Blender 4.5 LTS Manual
[149] https://docs.blender.org/manual/en/4.5/editors/3dview/display/overlays.html — Viewport Overlays - Blender 4.5 LTS Manual
[150] https://github.com/PacktPublishing/Unreal-Engine-5-Character-Creation-Animation-and-Cinematics — Packt: Unreal Engine 5 Character Creation, Animation and Cinematics — companion identification
[151] https://docs.blender.org/manual/en/4.5/modeling/meshes/editing/mesh/separate.html — Separate - Blender 4.5 LTS Manual
[152] https://docs.blender.org/manual/en/4.5/scene_layout/object/origin.html — Object Origin - Blender 4.5 LTS Manual
[153] https://docs.blender.org/manual/en/5.0/modeling/modifiers/generate/scatter_on_surface.html — Scatter on Surface Modifier - Blender 5.0 Manual

<a name="chapter-study-coverage"></a>

## What was actually studied?

Read [video study notes, part 1](video-study-notes-01.md) and [part 2](video-study-notes-02.md) for the observations preserved from the audit. These are original written notes and links, not footage or transcripts. The survey totals below are historical and are not counts of included assets or full playbacks.

### Which numbers can be combined?

| Population | What the audit established |
|---|---|
| Directly named YouTube videos | **256** distinct IDs. Player statuses: 218 public, 6 age-gated, 28 terminated-account messages, 2 private, 2 unavailable without a stated reason. A public response is not proof of playback. |
| Direct visual study | Three or more timed publisher preview frames were inspected for **204** direct IDs: technical and adjacent references, not 204 complete lessons. The remaining 14 public items were classified as entertainment or unrelated. Separately, 142 IDs had untimed numbered previews; many overlap. 111 direct IDs have a note based on their description or chapters. |
| Direct playlists | **6 named**, **5 enumerated**. All 144 positions declared by those five were accounted for, with 144 distinct IDs. **7** also occur directly: the union is **393**, not 400. No member count was disclosed for the unavailable list. |
| Four course/companion lists | **50** entries have individual technique notes. For 20, watch-page descriptions and timed publisher frames were inspected; 45 have an indexed caption excerpt attributed to the exact original URL; 19 have inspected chapter entries. The groups overlap. Index excerpts are not verified direct transcripts, and visible first/last caption starts do not imply continuous coverage. |
| Motion preview list | The other **94** positions are a performance/download collection by its labels, not 94 instructional lessons. No motion file was fetched or assessed for rights.[112] |
| Further publisher leads | **25** additional IDs linked by original publishers or their curricula (including eight later-edition course members, demos, one compilation and one third-party review). Original oEmbed confirmed 24 title/publisher pairs; one returned HTTP 401. These checks alone establish no technique. |
| Additional catalog candidates | **21** distinct historical leads, all returning HTTP 404 on original oEmbed. The index retains the original ID and observed lookup result, not an unverified title, mirror or reconstruction. The historical survey counted **439 distinct candidate IDs**, not 439 accessible tutorials. |

### The six original lists

| List | Visible / declared | How to read it |
|---|---:|---|
| Blender Guru’s Blender 3.0 Donut | 17 / 17 | 16 project lessons and a learning-plan supplement.[110] |
| V6 Blender transfer | 4 / 4 | Three transfer stages; one animation-library topic.[111] |
| MMD Dance Motions | 94 / 94 | Performance previews, not setup instruction.[112] |
| `PLjN13WtFmo8YzEl6SO3byPa4TIF-D4iDB` | 0 visible / **unknown** | Provider: “The playlist does not exist.” Do not infer it always contained zero videos.[113] |
| Ian Hubert’s Lazy Tutorials | 22 / 22 | Independent shorts, including a depth-map demonstration.[114] |
| Blender Guru’s Lighting Course | 7 / 7 | Introduction, five principles, applied critique.[115][127] |

### Limits that matter in practice

- **Title or metadata:** identifies a publication. **Description or chapter:** identifies the author’s stated scope. **Timed still:** shows one visible state, not a sequence of clicks. **Narration:** identifies what was said, with separate labels for direct transcript, indexed excerpt and local speech recognition. **Workshop experiment:** a check on a particular original scene. Do not promote one kind into the next.
- The broad direct audit used selected windows of a creator-linked FreeMoCap transcript.[121][124] Some of those same IDs have **separate, deeper** studies; for example, the landing lesson had narration and 18 additional samples.[94] Those are overlays, not extra videos. The flag exercise is an independent alternative, not a recovered original from a missing list.[99]
- Unavailable videos and rate-limited captions were recorded as access gaps, not reconstructed from mirrors. These statuses describe the audit, not an assertion about current access.
- Outside YouTube, four technical preview requests returned HTTP 403. No action is inferred from those clips. For the Wrap4D release, public publisher information was available, not access to the Vimeo player configuration.[83] Its syllabus is a separate source, not a substitute viewing.[86]
- Reaction images, unauthenticated file-host links, personal chat exports, mixed-author folders, mirrors, paid lessons and unverified project files were not republished or used as instructions. Some may contain additional unknown items; no complete historical course size can be inferred. No credentials, third-party media or transcripts are required for or distributed with this handbook.

### Sources

[83] https://vimeo.com/429211419 — R3DS: Wrap4D release film — publisher description only
[86] https://faceform.com/wrap4d — Faceform: Wrap4D processing order and consistent topology
[94] https://www.youtube.com/watch?v=oB_M_RGNqFY — SamBam Studios: How to make a Landing Animation - Blender Animation Tutorial
[99] https://www.youtube.com/watch?v=up3zVqyTIpM — Disabled Blenderman: Why Your Blender Flags Look Fake – Fix It Now
[110] https://www.youtube.com/playlist?list=PLjEaoINr3zgFX8ZsChQVQsuDSjEqdWMAD — Blender 3.0 Beginner Donut Tutorial (OLD)
[111] https://www.youtube.com/playlist?list=PLhiuav2SCuvc-wbexi2vwSnVHnZFwkYNP — [V6] Export your Koikatsu waifu to Blender and more
[112] https://www.youtube.com/playlist?list=PLGD6S2S5Qd07kW13qP1voF9G7KNzDlcfg — [MMD] Dance Motions [Motion DLs]
[113] https://www.youtube.com/playlist?list=PLjN13WtFmo8YzEl6SO3byPa4TIF-D4iDB — Unavailable playlist — no disclosed member count
[114] https://www.youtube.com/playlist?list=PL4Dq5VyfewIxxjzS34k2NES_PuDUIjRcY — Lazy Tutorials
[115] https://www.youtube.com/playlist?list=PLjEaoINr3zgH9vCr47kSS5W8PEJBNIiwK — Lighting Course
[121] https://www.youtube.com/watch?v=GxKmyKdnTy0 — FreeMoCap Rough Cut Tutorial/Walkthrough/Brain Dump (Nov 2022)
[124] https://share.descript.com/view/vsqpqBJ9UNi — FreeMoCap: creator-linked transcript, selected windows
[127] https://www.blenderguru.com/posts/2019/lighting-mastery — Blender Guru: Lighting Mastery Series, written companion
