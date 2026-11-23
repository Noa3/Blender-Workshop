# Architecture and Geometry Nodes

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [Plan the shot before finishing the building](#chapter-scene-and-architecture)
- [Procedural environments that remain art-directable](#chapter-environment-generators)
- [Geometry Nodes: from one element to a system](#chapter-geometry-nodes)
- [Curves, instances and space that must stay empty](#chapter-spacing-field-study)
- [Build the walk before the skyline](#chapter-city-and-nextgen)

<a name="chapter-scene-and-architecture"></a>

## Plan the shot before finishing the building

Choose one sentence that the camera has to communicate: *a sheltered reading gallery opens towards a bright courtyard*. That dictates the near frame, the route of the eye, where the darkest mass sits and where light can reasonably enter. A room, a marketing elevation and a playable street require different proof; a good image from one corner is not a tested walkthrough.

### Three starting briefs

| Scene | Start here | Recommendation and acceptance |
|---|---|---|
| Daylit interior / arcade | In plan: footprint, openings, circulation, bench for scale. In elevation: floor, spring line, lintels, ceiling depth. Set a standing or seated camera height deliberately. | Look through repeated bays towards a single landmark; leave space in front of the camera for foreground framing. Render clay first. A bench back must not touch a pier edge in projection, and the exit must read without a texture. |
| Exterior facade / street | Establish a constant module pitch, setbacks, sill heights and roofline. Separate straight, corner, end and deliberately unique pieces. Place the camera far enough back for the important layers to separate. | Use linked windows or modules while the kit is fluid. Break rhythm at the entrance, not on every bay. For an elevation, use orthographic deliberately; for a perspective still keep the camera level and shift the frame if verticals must remain parallel.[23][52] |
| Playable garden or environmental story | Block the traversal corridor and eye height first. Put one large landmark past a turn, group plant masses by slope or exposure and keep an exclusion margin for traversal. | Inspect from the actual player camera as well as overhead. Preserve a light/dark or color difference between path and planting. A free point center alone does not guarantee that a leaf or collision hull clears the player. |

### A dimensional, editable bay

1. Define units and one module origin on the grid. Write down clear span **between inner faces**, pitch **between module origins** and wall depth. They are not interchangeable. Assign one dimension change to test the kit after assembly. For a visual study these are design dimensions, not accessibility, safety or building approvals.
2. Establish the floor and the midline. Shape the opening in elevation. In the supplied pavilion the same continuous closed profile forms two legs and a semicircular arch. A rectangular slice through its depth catches light on the inside return. For a large wall with editable openings, an alternative is a closed cutter; inspect the result before adding a bevel.[50][1]
3. Repeat the tested bay without cloning topology. Align floor modules, cornice returns and caps; test a run of three plus an end/corner, not just one isolated module. Use trim pieces for intentional joints rather than coplanar overlapping surfaces. Linked duplicates keep object transforms independent while sharing mesh edits.[52]
4. Place the camera, then simple props: a seat sets human scale, a vessel breaks the repeated silhouette, a contrasting end panel marks the destination. Inspect the contact under each object. Do not widen the lens to hide an implausibly shallow room: move the camera first and compare the near-to-far size relationship. Lens shift changes framing without tilting the camera.[23]
5. Build illumination around an opening. Use a clay override to expose depth, blocked apertures and light leaks. Switch one variable at a time, then restore the saved beauty setup. Visible sky outside need not be the brightest object inside the composition.

#### Worked example: Meridian gallery

The camera is 1.55 m above the floor with a 28 mm lens, horizontal optical axis and upward shift. Four editable bays share **one** mesh on a 2.4 m pitch; the clear span measures **4.04 m**. A fresh reopen checks the common mesh, manifold edges, station positions, and projected vertical drift. The photographs use one Cycles scene; the large angular sun smooths the shadow diagonals while the small sun draws the repetition across the floor. These dimensions are specific to the lab. See [advanced labs](lab-notebook.md#chapter-advanced-labs) to reproduce the checks.

**Fix common failures in order.** If the space reads flat, hide materials and check overlap, foreground framing and the key direction. If stone looks like stucco foam, compare bevel width to a bench board before adding pores. If the photo reads like a dollhouse, check eye height, depth of field, furniture and lens together. If a window looks pasted on, reveal the sill and jamb thickness at an oblique view. For a real building use measured drawings and qualified project review; this is a visual-design workflow.

<a name="chapter-environment-generators"></a>

## Procedural environments that remain art-directable

Start with a spatial rule you can draw. Example: a garden slope has planted shoulders, a deliberate footpath between them and a few irregular accents. “Scatter lots of plants” is not a rule. Make the path, habitat zones and hero exceptions visible in the viewport before adding species. See the [fields primer](spaces.md#chapter-geometry-nodes) and [course notebook](learning-notebook.md#chapter-course-notebook).

### Build and inspect one branch at a time

1. **Metric emitter.** Establish dimensions, origin, upward/plant axis and where changes of terrain shape should occur. Evaluate slope in the intended space. A world-up slope filter and a local-up one disagree on a rotated emitter. Decide whether a change of scale should resize plants, affect density per square meter, or neither. Keep the test scene's emitter transforms explicit.
2. **Eligibility is separate from density.** Evaluate a path exclusion, exposed soil and slope ranges before varying coverage. A noise field alone usually paints salt-and-pepper, not ecologically convincing clusters. Create large patches first, a second band along the boundary next, then a few hand-placed hero plants. A binary exclusion must stay binary where a path is meant to be empty. Beware of averaging point/corner fields onto coarse faces; preview the actual domain on which the selection is evaluated.[8][9]
3. **Distribute points, then choose prototypes.** For a spacing constraint use Poisson Disk and test it, or explicitly describe random distribution as random. Density changes and seed changes are not the same control. Align a plant's growth axis to the surface normal first, *then* add variation around that local growth axis. Stones can tilt more than reeds. Share prototypes as instances while editing.[9][10]
4. **Use instances until a downstream operation needs real mesh geometry.** A realized mesh consumes different memory; for an exporter, realize on a separate branch or use supported native instancing. Inspect the actual destination file. Do not claim that keeping instances in Blender automatically yields GPU instancing or fewer draw calls in an engine.[2][20]
5. **Replace a beautiful plant with a crude diagnostic mesh.** Use an arrow or cube with an obvious top, apply the same graph and visualize the mask. Fix the positions/axes first, then restore the species. This is also visible in the 3.0-alpha pebble demonstration, where the spreadsheet distinguishes instances from mesh points.[72]

### Expose controls that a scene artist can use

- **Seed:** same input, same graph, same Blender version → repeatable layout. Keep a show seed when comparing lighting; vary the seed only when judging composition. Do not promise identical random distributions across Blender versions or topological changes.
- **Density or spacing, path size, prototype weights:** include units or define the role. Do not name three unrelated values `Scale`. Test empty density, a narrow path and a wide path. Report whether a path test is center-only or includes the maximum leaf/stone envelope.
- **Variant selection:** avoid independent rotation of child leaves after the clump is constructed. Put the prototype origin at its ground contact, not its visual center. For wind, keep the root pinned and measure tip displacement; a still image is not a wind test.
- **Temporal stability:** if the emitter changes topology every frame, evaluate how instance identities vary in motion. Stable input does not automatically mean stable placement on a remeshed surface. Check adjacent frames at the actual output size.

### From generator to composition

Start with a top view of mask coverage, a player-eye view of the route, and one near crop for plant silhouettes. Order the species into large/medium/fine masses instead of assigning a random size across several orders of magnitude. Avoid placing high-contrast stones equally everywhere: group them around one bend, preserve a quiet band near the path and verify these decisions survive another seed. The supplied garden exercise and its output measurements are indexed in [advanced labs](lab-notebook.md#chapter-advanced-labs).

<a name="chapter-geometry-nodes"></a>

## Geometry Nodes: from one element to a system

**Ask first:** Are the parts identical, or does each need its own vertex data? Instances share source geometry. `Realize Instances` turns them into independently editable geometry and can cost much more memory.[2][10] A conventional modifier or Array is enough for a shelf board. Use Geometry Nodes for variable counts, surface masks or multiple prototypes.

### Build a radial fan
1. Add a **Geometry Nodes** modifier to an empty mesh. Give the group a `Geometry` output and inputs `Count` (integer, minimum 3), `Radius` (float) and `Realize for mesh output` (boolean). The carrier may be empty: the group generates its own geometry.
2. Add `Mesh Circle` with no faces: `Count → Vertices`, `Radius → Radius`. Connect its mesh to `Instance on Points: Points`. The circle vertices supply the distribution without a duplicate endpoint or a `Distribute Points` node.
3. Build a petal: `UV Sphere → Set Shade Smooth → Set Material → Instance on Points: Instance`. Set different scale values for length, width and thickness; local **X** is the long axis. Connect `Position → Align Rotation to Vector (Axis X) → Instance on Points: Rotation`. Position points outward because the circle is centered on the local origin. For an offset circle, subtract its center first. Identical round spheres hide rotation errors: debug with an asymmetric petal.
4. Route direct instances and `Realize Instances` to a `Switch (Geometry)` controlled by the boolean, then to Group Output. Default to **instances**; switch branches only for downstream mesh operations, measurements or an export tested with that branch.[2] The `.blend` remains parametric. Switch back afterward.
5. **Measure:** Change Count and count faces on the realized branch. In the reference lab, 12 petals yield 3456 polygons and 24 yield 6912. The small GLB contains only petals, not the base. It is triangulated: exported triangles and Blender polygons are different counts.[20]

### Surface scatter: stones, grass and window details
- Build one clean asset with its origin at the contact point. Standardize forward and up axes in the asset library. For a sideways tree, inspect prototype axes before rotating the entire scatter and hiding the cause.
- Surface → `Distribute Points on Faces` → `Instance on Points`. In Poisson Disk mode use `Distance Min` for minimum spacing and a density field to control where more points are allowed. The distributor's rotation can align local Z to the surface normal.[9] Add random rotation **around the local** up axis rather than replacing the full world rotation. Test on a sloping ramp, not just flat ground.
- For variants, use `Collection Info` with separate children as instances and enable `Pick Instance` on the destination. Decide whether to preserve or reset child transforms. Bound per-point scale: broad shape variation plus subtle jitter reads better than arbitrary noise.
- **ID versus index:** `Distribute Points on Faces` generates stable IDs for surviving points. Drive random size/variant from the ID; an index may refer to another element after a topology change.[9] A fixed seed makes a comparison repeatable but does not guarantee identical points after arbitrary topology edits.

### Fields and troubleshooting
A field is an instruction evaluated per element in the consuming node's context.[8] `Position` **before** instancing can mean a point position; after realization, on the mesh point domain, it describes individual petal vertices. The same wire can therefore answer two different questions. Name the domain of a mask (point, face, face corner or instance). Capture a value before changing topology if it must survive; explicitly name an attribute for later material use and verify its domain.

| Symptom | Smallest useful test |
|---|---|
| Empty group | Connect a primitive directly to output, inspect just the distribution in Viewer/Spreadsheet, then try **one** instance. Compare viewport and render modifier switches. |
| Everything the same size | Vary `Scale` on the instance node, not the source object. Test the field first with two distinct colors or sizes. |
| Petals orbit the wrong point | Compare object and group coordinates; visualize the center vector. Check the prototype origin. |
| Render suddenly expensive | Disconnect realization. Measure count, prototype density and material cost separately, in that order. Do not optimize two variables at once. |
| Empty or altered export | Explicitly evaluate an export copy, realize required instances, use supported materials and import into a fresh scene. Compare dimensions and triangle count. |

Next: animate radius with constant count. Change count separately and watch for flipped orientation or jumping IDs. [Sources](sources.md).

<a name="chapter-spacing-field-study"></a>

## Curves, instances and space that must stay empty

### Place one fitting before choosing how many

Amandeep's cable demo shows a curved span at 0:40, repeated dips at 0:50 and a bundle at 1:10. His written GeoCables guide distinguishes clicking face anchors, splitting a run and converting the edges of an existing mesh. These are different ways of defining the route; adding more strands does not correct a misplaced anchor.[100][101] In Ryan King Art's lights lesson, the fitting can be seen on its own at 13:20, repeated along two spans at 33:20, and lit in a room at 53:20.[102] A useful order: check the hanging line from the delivery camera, check the spacing with plain markers, then design the light or material. No add-on is needed for the following exercise.

**Build a comparable test:** create an open poly spline with deliberately uneven control points and inspect it with a Geometry Nodes modifier. The source is a straight, open poly spline with control points deliberately close at one end. Set **Curve to Points** to **Evaluated**, then **Count** with `5`. The node's modes distinguish existing evaluated points from sampling each spline at equal distances.[109]

| Mode | Measured local X positions of marker centers |
|---|---|
| Evaluated | 0, 0.25, 4 |
| Count = 5 | 0, 1, 2, 3, 4 |

If you want the original anchors, **Evaluated** is right for this polyline. If you want five equally spaced fittings, **Count** is right. Count is **per spline**, not an asset-wide total.[109] For direction-sensitive fittings, use the node's tangent/rotation output and inspect both ends; equal positions alone do not guarantee correct orientation.[109] The fixture does not measure error on curved Bézier splines, bundle tension or sag.

### Separate eligibility, spacing and variation

In Khamurai's scatter tutorial, patches are visible at 0:45 and a shaped subject with detail concentrated near its top at 1:40. Those samples justify comparing a flat diagnostic surface with the real subject; they do **not** identify the sampling algorithm in the film.[104] In the VFX Grace instance lesson a row of tree crowns varies in color at 3:20; at 4:25 the on-screen explanation connects instance attributes to shader variation.[103] Do not use a geometry seed to fix a color-only problem. As a separate **unmeasured** exercise, map one per-instance value to two sign colors; check that changing the color mapping leaves the sign centers unchanged.

**Try it:** build two square faces meeting at local X = 0. Connect `Position → Separate XYZ → X > 0` to the **Selection** of **Distribute Points on Faces**. The original comparison used Poisson Disk minimum distance 0.32, Density Max 80, and identical small cubes on the points. Realize only the diagnostic branch so you can measure centers. Keep the production branch instanced unless the receiver requires a mesh.[9][10][2]

| Seed | Centers | Closest pair, local units | Centers on reserved face |
|---:|---:|---:|---:|
| 4 | 14 | 0.3344 | 0 |
| 19 | 11 | 0.32298 | 0 |

The count changed; the two intended constraints held at both tested seeds. At seed 4, rounding center coordinates before the distance calculation gives 0.33441, while rounding only the final distance gives 0.33442. That last digit is not a different layout. To diagnose a failure, first preview the selection on the actual distribution domain, then measure center spacing. Inspect leaf or fitting overhang separately; this check only tests **centers**. The illustrated map plots evaluated marker positions, not a beauty render.

**Independent check:** the original checker reopened the generated fixture without executing embedded scripts. Reopen your own scene, then vary sampling and compare spacing and count independently.

**Learning evidence:** twelve time-indexed publisher storyboard samples per film, not continuous playback. No usable captions were obtained for these four; precise sockets and measured values above come from the manual and the independent native scene, not guessed from tiny preview pictures.

### Sources

[2] https://docs.blender.org/manual/en/4.5/modeling/geometry_nodes/instances/realize_instances.html — Blender 4.5 LTS: Realize Instances
[9] https://docs.blender.org/manual/en/4.5/modeling/geometry_nodes/point/distribute_points_on_faces.html — Distribute Points on Faces - Blender 4.5 LTS Manual
[10] https://docs.blender.org/manual/en/4.5/modeling/geometry_nodes/instances/instance_on_points.html — Instance on Points Node - Blender 4.5 LTS Manual
[100] https://www.youtube.com/watch?v=OCTwhHCklvs&start=1 — Amandeep: Hanging Cables in Blender Geometry Nodes | Free Script Series S02E02 | GeoCables Free Addon
[101] https://amanbairwal.gumroad.com/l/GeoCables — Amandeep: GeoCables - Geometry Nodes Cables - Free Addon
[102] https://www.youtube.com/watch?v=2Xwu8Rx-asw — Ryan King Art: Customizable Christmas Lights - Geometry Nodes 🎄 (Blender Tutorial)
[103] https://www.youtube.com/watch?v=NuARDAgZMio — VFX Grace: Blender Tutorial: Geometry Instance - Geometry Node
[104] https://www.youtube.com/watch?v=U550q0XQNOo — Khamurai: Next Level Scattering in Blender 3.3 | Geometry Nodes Tutorial
[109] https://docs.blender.org/manual/en/4.5/modeling/geometry_nodes/curve/operations/curve_to_points.html — Blender 4.5 LTS: Curve to Points

<a name="chapter-city-and-nextgen"></a>

## Build the walk before the skyline

By Noa3 · Blender 4.5.9 LTS baseline · Unbuilt design and comparative test proposals; no rendered results or timing claims.

Draw a line from a shop door across the street to a station platform. Make that line a person can actually follow before scattering a single window. The architectural brief is not “a believable metropolis”: it is “a first-time visitor can find the accessible station entrance from the shop.” Keep one elevated planning view and one pedestrian camera. The plan exposes dead ends; the eye-height shot exposes the sign hidden behind a bus shelter.

### A street you can measure and maintain

1. **Section before facade.** Set a metric scene and draw a dimensioned cross-section: shop threshold, pavement, kerb, gutter, carriageway, opposite landing and station entrance. Choose a person-height proxy, door leaf and opening based on a measured reference; label the *clear* opening separately from nominal leaf width. Test with door swung, bin in place and passengers waiting. The US Access Board’s ADA guide illustrates why this matters: under its cited rule the continuous clear route is generally at least 36 inches wide, with a reduction to 32 inches only at points of limited length and further constraints at turns. [425] This is one jurisdiction’s reference, not certification or a world city template. Use the actual jurisdiction and project standard for a real commission.
2. **Walk both ways.** From the shop, approach the crossing at standing and seated viewpoints. Trace a continuous surface through the kerb ramps to the entrance, ticket area and lift or ramp to platform level; do not let a stair-only shortcut masquerade as the whole route. Check open doors for manoeuvring space, columns for pinch points, paving for unintended steps and route signs for visibility on the return trip. A camera flying through a turnstile is a failed route test, not a successful walkthrough.
3. **Give infrastructure a destination.** Follow one downpipe to drainage, one service access door to a loading area and the station canopy to columns and foundations. Leave access to cabinets; stop utility covers and furniture at doorway and boarding exclusions. Put a bench where someone might wait without blocking a queue. Include kerb transitions, expansion joints and paving changes where the construction changes, not as random noise.
4. **Repeat what is really repeated.** Instance facade bays, sleepers and lanterns along authored guides with an explicit stable seed. Separate “buildable frontage,” “clear route,” “sightline” and “service access” masks. Override the corner shop, station sign and threshold by hand; delete the corresponding procedural copies, rather than hiding them a millimetre inside the hero mesh. Change the seed, regenerate and verify the lift door and sign remain unobstructed. Keep far blocks as silhouettes until the pedestrian camera demonstrates a need for more geometry.
5. **Explain the architecture with light.** Choose a sun direction from an agreed site orientation/time reference or clearly label it illustrative. A Blender Sky Texture provides a procedural sky and exposes sun elevation and rotation in applicable models. [417] Place a test pole and canopy in the shot; follow the shadow across both so direction and contact agree. If adding a Sun lamp, compare sky-only, lamp-only and combined renders for doubled direct light. Lock exposure and compare the bright paving, shaded doorway and interior beyond it. Recover the doorway by changing the lighting or material that obscures it, not by flattening the whole exterior. For a facade elevation, compare a level perspective camera with lens shift against the tilted camera; choose whether converging verticals explain the height or misrepresent the design. Retain a section or orthographic view when a perspective view cannot explain clearance.

### Engine selection is a shot decision

Blender 4.5 names EEVEE its physically based realtime renderer, Cycles its physically based path tracer, and Workbench its layout, modelling and preview engine. [422] “Realtime” is a design aim, not a promise about this scene or a prohibition on final-frame output. Choose by the intended evidence:

| Native 4.5 route | What to ask it to show | Decision if it fails |
|---|---|---|
| Workbench | Play the walk as a clay/silhouette study. Is the entrance legible before the camera reaches it? | Fix height, obstruction or framing. Do not approve glass, final daylight or metal reflectance from this pass. A deliberate diagrammatic clay deliverable is a different brief. |
| EEVEE | Iterate quickly in the viewport, then render the actual sequence and inspect glass, canopy contacts, reflection continuity and thin wires during motion. | Adjust the offending lighting/reflection setup or simplify the shot; compare a Cycles reference before committing the sequence. |
| Cycles | Use an offline reference crop where an arcade receives indirect light; compare noise and preserved texture with and without denoising. | If frame cost exceeds the delivery budget, address the noisy light path, simplify distant geometry or change engines. A clean still is not proof of temporal stability. |
| Intentional NPR | In EEVEE, Shader to RGB plus a ramp can turn a diffuse response into toon bands; that node is EEVEE-only. [4] Try bands for wayfinding zones and silhouettes instead of photoreal roughness. | If shadow bands flicker across steps or labels disappear, widen the tonal separation or author the graphic directly. Do not expect that EEVEE node graph to transfer intact to Cycles. |

### Three advanced techniques, three different problems

There is no **next-gen button**. A sampling strategy, a temporal upscaler and a captured-scene representation act at different points in production. Do not sell one as a substitute for the other two.

**1 · Find indirect light — Blender 4.5 native, Cycles CPU path guiding.** Cycles learns important light directions as it samples; the manual specifically cites small openings, restricts guiding to CPU, and cautions that complex caustics are not its design target. [14] Use the ticket hall seen through a narrow entrance, not a sunlit blank wall. Render the same dark corner with guiding off/on on the same CPU and include training in elapsed time. Compare at equal wall time against a longer reference, then play a contiguous move through the threshold looking for sparkling tiles or denoiser smear. Measure ordinary GPU Cycles separately as a production alternative, not as the controlled experiment. If learning buys nothing within budget, keep the simpler renderer setup; for a difficult glass caustic, reconsider what the shot actually needs to show.

**2 · Recover detail over time — external, Epic’s Unreal Engine TSR.** TSR starts from a lower internal resolution and spreads reconstruction across frames; Epic describes newly disoccluded areas as needing to accumulate detail quickly. [424] That is not a Blender 4.5 EEVEE switch. For a comparison in its host engine, lock output resolution and camera path; compare native-resolution output against TSR at reduced internal resolution. Record GPU frame time including reconstruction. Pan past a dark pole against bright station lettering; then cut abruptly and watch the newly exposed letters during the first frames, not just after settling. If trails, shimmer or slow convergence damage essential typography, raise the internal resolution or keep the title as a separately rendered full-resolution graphic. No Unreal benchmark was performed here.

**3 · Reconstruct a place from photographs — external research, 3D Gaussian Splatting.** Kerbl and colleagues describe a representation starting from sparse calibration points, optimizing anisotropic 3D Gaussians and rendering them with visibility-aware splatting for novel views. [423] This is not an automatic conversion into editable watertight station architecture, nor a native 4.5 city generator. Consider a captured distant courtyard rather than the hero entrance that the architect must revise. Withhold real camera views for comparison; budget capture coverage, training time, disk, runtime memory and playback separately. Travel sideways between capture positions, then deliberately pass outside that corridor. Inspect railings, holes and floating patches; test a requested change of daylight before promising relighting. If the shot fails, constrain the path, capture missing views with permission, or replace the foreground with surveyed mesh. The paper’s demonstrated performance is not a promise for your machine or scene.

**Version boundary:** Blender 5.0 release notes, for example, report improved compatibility with the OpenColorIO configuration for ACES 2.0. [428] That is a newer compatibility change, not the explanation for a sharper 4.5 render. Record Blender version and colour configuration with any reference frame; compare displays using the same transform before attributing differences to an engine.

**A newer native option for a stylized shot — 5.1 shader Raycast, not a 4.5 node.** A shader can ask whether a ray hits and how far it traveled. EEVEE traces in screen space; Cycles treats the geometry tested by this node as opaque, even where a material looks transparent. [390][391] To test a stylized contact accent, nominate a direction, start just outside the surface to avoid a self-hit, bound the ray length in scene units and use `Is Hit` to gate a softened distance mask. Preview the mask before tinting the palette. Slide the camera until the candidate occluder leaves the frame, then put a transparent card in its place. If a hero face changes expression because an offscreen occluder vanishes or clear glass darkens it, use an authored head-local mask for the face and reserve the ray effect for noncritical accents. This is a versioned recipe, not a 5.1 render test or a reason to upgrade the production file.

**Keep the city editable during handoff.** Put a block, a repeated facade and a moving tram in a small test USD stage before exporting a district. Record unit scale, up-axis, frame clock, prim paths, material assignments and which assets remain instances. Blender 4.5 imports a USD `PointInstancer` using a point cloud and Geometry Nodes; animated geometry can acquire a Mesh Sequence Cache modifier. Import is not an authoring-preserving round trip for arbitrary USD layer and reference compositions. [389] Reopen the result in the receiving tool, change one source window and see which copies update, seek the tram past mid-shot, and move the camera around one pane. Keep the source stage alongside a baked fallback if collaborators must change the architecture; a visually correct single frame does not establish editability.

**Decision sheet for the supervisor (proposed):** Define the target before the test: output dimensions and rate, playback or offline deadline, memory ceiling, camera route, cuts and protected details. Record device, settings, peak memory, cold-start or training cost, and per-frame time including denoising/upscaling; distinguish worst frames from the median. Compare the *same* shot at native display size, at speed, and in crops of the handrail, platform sign and shaded threshold. Repeat after one real revision (door moved, weather changed or cut shortened). Choose the least costly route that still passes the moving-camera and revision tests. If no route passes, name the failed frame and its consequence rather than publishing a technology ranking.

### Sources

[4] https://docs.blender.org/manual/en/4.5/render/shader_nodes/converter/shader_to_rgb.html — Blender 4.5 LTS: Shader to RGB
[14] https://docs.blender.org/manual/en/4.5/render/cycles/render_settings/sampling.html — Sampling - Blender 4.5 LTS Manual
[389] https://docs.blender.org/manual/en/4.5/files/import_export/usd.html — Universal Scene Description — Blender 4.5 LTS Manual
[390] https://developer.blender.org/docs/release_notes/5.1/eevee — Blender 5.1 — EEVEE & Viewport, Shader Raycast
[391] https://docs.blender.org/manual/en/5.1/render/shader_nodes/input/raycast.html — Raycast Node — Blender 5.1 Manual
[417] https://docs.blender.org/manual/en/4.5/render/shader_nodes/textures/sky.html — Blender 4.5 Manual — Sky Texture Node
[422] https://docs.blender.org/manual/en/4.5/render/introduction.html — Introduction - Blender 4.5 LTS Manual
[423] https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting — 3D Gaussian Splatting for Real-Time Radiance Field Rendering
[424] https://dev.epicgames.com/documentation/en-us/unreal-engine/temporal-super-resolution-in-unreal-engine — Temporal Super Resolution in Unreal Engine | Unreal Engine 5.9 Documentation | Epic Developer Community
[425] https://www.access-board.gov/ada/guides/chapter-4-accessible-routes — Chapter 4: Accessible Routes
[428] https://developer.blender.org/docs/release_notes/5.0/color_management — Color Management - Blender Developer Documentation
