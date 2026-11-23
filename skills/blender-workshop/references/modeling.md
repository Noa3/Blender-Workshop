# Modeling and made objects

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [Choose a modeling tool by the failure it solves](#chapter-tool-and-style-decisions)
- [Form, topology, UVs and baking](#chapter-modeling)
- [Build and check a functional mesh](#chapter-modeling-checks)
- [Manufactured objects, miniatures and soft goods](#chapter-made-objects)
- [A quality brief you can test](#chapter-quality-brief)

<a name="chapter-tool-and-style-decisions"></a>

## Choose a modeling tool by the failure it solves

Start with an orthographic elevation or a scaled side reference and a three-quarter camera. Draw the main mass, its largest opening, and the support/contact region. Block these as separate pieces before joining anything. At a small thumbnail, can someone recognize the object and which way it faces? If the answer is no, another bevel or texture will only polish the wrong shape.

| Geometry problem | Workflow | Look for this before going further |
|---|---|---|
| Symmetrical case with an asymmetric latch | Model one half with the center plane on its origin. Mirror the case only. Add the latch after the symmetric stage. Mirror can use an independent mirror object when the mesh origin belongs at a hinge.[48] | No light leak or pinched highlight at center. Sliding the hinge must not move the mirror plane. |
| Square recess in a panel | Inset the face for an even reveal; extrude the inner face inward. For a repeated real opening, test a separate closed Boolean cutter before edge finishing.[61][50] | Look at the back of the part. A black rectangle painted on a facade is not a through opening. A Boolean is not a repair for overlapping or open input. |
| Thin shell, folded sign or curtain edge | Build the mid-surface first. Use Solidify for thickness; inspect the offset side and corners. Move thickness after base proportions, before final edge treatment when a rim is meant to catch light.[49][1] | Give the front and back different temporary colors; inspect the inside corner at grazing angle. Reduce radius or repair self-intersections rather than forcing an even-thickness checkbox. |
| Tapered spout, transition duct, pointed arch | Sketch section profiles. Bridge compatible open loops, check the twist, then shape or add intermediate sections.[62] For a revolved vessel, turn a wall-thickness profile; give its rim a real return. | One highlight should travel around the transition without sudden flips. Use a section cut to inspect wall thickness. |
| Repeating bays or planks | Use Array with constant offset for dimensional pitch; relative offset follows bounding-box dimensions. Use linked duplicates where each module needs a separate transform but shares edits.[51][52] | Widen the prototype. A constant 2.4 m design pitch must not silently become 2.7 m. Make a single-user copy only for a deliberately unique piece. |
| Rounded grip on an otherwise planar casing | Keep a low-resolution cage. Edge Slide to correct proportions; bevel only the break lines; add support loops *where* the subdivided profile drifts. Do not subdivide a panel just to fix a shading error.[68][37] | Check in silhouette and with a narrow softbox. If the outline is right but reflections ripple, repair surface continuity before moving the outline. |
| Character or soft stylized figure | Block torso, head and hands as simple masses. Sculpt primary planes before pores; retopologize along mouth, shoulder and eyelid motion, not just along camera-visible contours.[6][25] | Make a small expression or joint bend before UV painting. Good static quads do not prove good deformation. |

### Styles imply different quality targets

| Style and use | Form / material / light priorities | A result to reject |
|---|---|---|
| Observational architectural still | Use scale cues, contact and a coherent light direction. Vary real materials at distinct physical scales; show thickness at openings. Keep verticals intentional. | A perfect shader on a room that looks miniature; a window acting as an unrelated second sun. |
| Graphic or low-poly environment | Reduce profile to memorable angles and overlapping depth bands. Budget contrast for the route and landmark; keep deliberate facets, not unintentional faceting everywhere. | Random triangles, equally noisy foreground and background, or unwalkable space that reads as a path. |
| Anime / cel | Design the light-shadow boundary as a shape; keep eye, nose and hair clumps readable at face distance. Try line weights at actual output size. Use the [anime workflow](character-surfaces.md#chapter-anime) before adding global outlines. | An outline that closes the eye in the secondary view, or a shadow band flickering across a nearly flat face. |
| Hand-painted game prop | Paint large value groups and a material-specific accent; put unique storytelling marks in visible atlas space. Keep painted light neutral enough for the intended dynamic light rig. | Painted rim on the unlit side that contradicts the actual key; readable only at texture-editor zoom. |
| Product close-up | Shape splits, real edge catches and a designed reflection first. Separate finish, contact wear and dust; avoid coating the whole object with one noise mask. | More texture explaining less form; edge wear along protected seams but none at grip points. |

**Refinement order:** primary silhouette → negative space → secondary construction → edge/profile → material breakup → microdetail. Change that order only for a reason: transparent products need early refraction tests, rigged assets need early bending, and tiling kits need early seam tests. Finish with two tests: the asset tiny in context, then large under moving light. A detail that disappears in the first and still costs in every frame is a candidate for baking or removal.

<a name="chapter-modeling"></a>

## Form, topology, UVs and baking

### Choose geometry for the job
A milled housing needs defined radii and flat mating surfaces. A face needs edges that follow a smile. A background rock needs a recognizable silhouette. Before modeling, identify the closest shot, any required deformation, and whether the object will be rendered, exported or printed. These cases need different topology and mesh budgets.

**For a first model**, use [Build and check a functional mesh](modeling.md#chapter-modeling-checks): make a rim, measure the opening, and distinguish a welded seam from two surfaces that only look joined. If you are following a book, the [six-PDF reading guide](learning-notebook.md#chapter-book-modeling) gives page numbers, explains what to keep from older editions and names the modern tools to use instead.

### Workshop piece: a machined control knob
1. Choose a reference diameter. In side view, block out the body height, lip and shadow gap as separate masses. Place the origin on the rotation axis. Resolve nonuniform object scale **before** dimension-sensitive modifiers, provided this will not harm a rig or linked asset. Work on a copy in an existing scene.
2. Start with a cylinder or a revolved profile. Keep the base, bezel, grip and insert editable. For a symmetrical cutout, try Mirror/Boolean before a narrow finishing bevel. Keep the cutters but hide them from the render. Give through-holes real thickness; a dark patch is no substitute for an inner wall.
3. Bevel rounds edges nondestructively; angle limits, bevel weights and segment counts control where it acts and how the edge rolls over.[1] Measure radii on the reference. Sweep a large area light across the surface at a grazing angle. If the highlight breaks, check normals, tiny faces and overlaps before changing roughness. `Clamp Overlap` can shrink the radius locally; do not simply increase the width.[1]
4. Separate detail by what it contributes to the image: model knurling at the silhouette, place graduations on the face and leave microscopic grain to the shader. A support loop near an edge sharpens the transition under subdivision; unnecessary loops across a broad surface make later edits harder.[37]
5. **Check:** Inspect front, side and low backlit views. Flat covers should not show wavy reflections; cylinder walls should not show unintended facets. Check internal dimensions and clearances on fitted parts. The lab's brass body has real ridges, not a normal map standing in for a silhouette.

### Control exercise: make a chair from one slab
Subdivide a shallow, closed seat slab with two loop cuts near the edges on each axis. In Face Select, select the three top faces in the back row **and** the four underside corner faces. Use `Extrude Along Normals` with a positive distance. The contiguous row rises into a backrest; the isolated corners descend into legs.[46] If everything goes up, it moved along a shared axis. If the back becomes three posts, the faces were extruded individually instead of as a region. To vary back and leg height, continue on only one side after the initial extrusion.

**Original 4.5.9 test:** Seven of the slab's 30 faces were selected. At slab thickness 0.16 and extrusion distance 0.75, four horizontal feet ended at Z = −0.75 and three backrest tops at Z = 0.91. These coordinates check the direction independently of perspective. This was a geometry test, not an additional supplied model.

### Organic characters: from sculpt to animation topology
- **Blockout:** Reduce the head, rib cage, pelvis and limbs to a few masses. Check the final camera and a black silhouette. Resolve joint heights and center of gravity before adding eyes, folds or pores. For an anime head, check the eye line and chin in three-quarter view as well as straight on.
- **Sculpt:** A coarse voxel remesh joins large masses; smaller voxels preserve finer detail at higher density. Neither automatically produces a good deformation mesh.[6][25] Keep a copy before remeshing. Use Grab for proportions, Clay/Crease for plane changes, and Smooth sparingly at transitions. For detail, use Multires as a separate approach instead of continually changing vertex structure.
- **Retopology:** Build a new low-poly mesh over the sculpt. Snapping/Shrinkwrap are aids, not evidence of quality. Loop around eyes and mouth, support both sides of joints and keep poles away from compressed areas. The decisive test is a blink, smile or bent elbow. Quads give control; a badly placed quad loop can deform worse than an intentional triangle on a quiet surface.
- **Check:** Inspect rest, intermediate and extreme poses for open boundaries, duplicate vertices, reversed normals and self-intersection. For printing, also check watertight volumes and physical wall thickness. Hair cards and cloth may deliberately have open edges.

### Unwrap and bake reliably
1. Finalize the low-poly mesh before committing to a UV layout and tangent basis. Plan seams like cuts in paper: split a cylinder lengthwise and detach its caps. Favor the less visible back side.[7]
2. Unwrap and apply a checker with letters or arrows. Stretched squares reveal distortion, backward letters show orientation and checker density reveals texel density. Leave island padding for the target resolution and its smaller mips. Overlap only intentionally identical parts; keep individually painted or baked islands separate.
3. **High-to-low normal bake (manual workflow):** Select the high-poly source and make the UV-mapped low-poly target active. Choose Cycles → Bake → Normal/Tangent, `Selected to Active`. Make the **Image Texture** node containing the target image active in the target material. Test the cage or ray distance at the tightest gap before baking the whole asset. Bake margin around islands and save or pack the image.[13]
4. Set a tangent-space normal map to `Non-Color` → **Normal Map** → Principled `Normal`, using the matching UV map.[12] If embossing looks recessed, check the target's Y convention and face orientation instead of inverting every channel. glTF expects +Y tangent normals.[20]
5. **Diagnose by symptom:** Black bake → active target, UVs, bake type. Neighboring detail stamped through → cage/ray distance. Seam visible only at a distance → padding/mips. Seam only in game → compare triangulation and tangent basis in the target. The technical lab tests a two-color **emission bake** on separate islands, not a high-to-low normal bake.

Exercise: render the same knob from a fixed camera with sharp edges, then with a slight bevel. If only overall exposure changes, the comparison was not controlled. [Numbered sources](sources.md).

<a name="chapter-modeling-checks"></a>

## Build and check a functional mesh

**First decision: what has to pass?** For a cable grommet, it is not enough for the top to *look* like a ring. A plug of the required size must fit from one side to the other. For a symmetric solid the two halves must share a seam. For a dial the markers should **not** be welded: their centers must sit evenly around a circle. Write that sentence before choosing a tool.

The three exercises below use original geometry. They do not require the books, a paid extension, a download of someone's scene, or an open Blender window. The [reading guide](learning-notebook.md#chapter-book-modeling) explains where the decisions came from. A manual check you have not performed is **untested**, not a pass.

### A. Make an opening that stays open

1. **Draw the section before making the circle.** In a side view through the center axis, mark the clear bore, sleeve outside, underside of the flange and highest point of the lip. Keep the section on one side of the axis. Trace the *material*, not the empty middle: the profile goes up the bore, out across the lip, down the outside, then back along the bottom rim. Both ends of the passage stay open; the material itself forms a closed shell.
2. **Choose a construction.** Revolve that closed profile about Z, with the 3D cursor on the intended axis. For Spin, set the axis and full revolution explicitly, keep *Use Duplicates* off, and check the first/last ring is joined; Auto Merge is designed for a full turn.[143] Alternatively build matching inner and outer loops and **Bridge Edge Loops** around the top and bottom rims.[62] Do not fill a whole end face: that makes a cap where the cable should pass. The generator uses a ring profile; the Spin route is a manual alternative, not the code path being tested.
3. **Finish only where the part needs it.** Round the lip so it catches light; do not spend the clearance budget on an inward bevel or add uniform subdivision to fix a single edge. Keep the source editable. Verify the evaluated opening again after the last modifier. For a sheet plus Solidify, wall thickness is an approximation at corners; measure the tight section rather than accepting the modifier value as a dimension.[49]
4. **Look through, then test the fit.** A ray down the center misses both a generous bore and a hole too small for the plug. Test across the clear width as well. Look for an end cap, a tilted inner bevel or a narrow throat halfway down. A finite set of probes is evidence about those samples, not certification for a real material, manufacturing process, arbitrary connector shape or print tolerance.

**Build the editable part.** Run the grommet generator below into a new local output directory. The fixture is an original desk grommet with a nominal 40 mm bore, 60 mm flange and 48 mm sleeve.

| Reopened geometry or control | Open/nonmanifold edges | Blocked axial passage samples | What it tells you |
|---|---:|---:|---|
| Original sleeve | 0 | 0 of 289 | The sampled paths are clear and the wall is closed. All 96 separate control rays aimed at the annular wall hit it. |
| Same sleeve with a quad removed | 4 | 0 of 289 | The passage test alone would miss the broken wall. |
| Closed solid cylinder | 0 | 289 of 289 | The manifold check alone would pass a completely blocked part. |

The axial rays sample the center and three rings out to 19.75 mm radius. At Z = −6 mm, midpoint-of-facet measurements gave a minimum bore radius of **19.989 mm**, slightly less than the 20 mm vertex radius. Nominal diameter and guaranteed clearance are not interchangeable. Run the [grommet generator and verifier](../scripts/grommet_lab.py) as shown below to create a local scene and a JSON report. The verifier reopens that scene and runs the controls in memory, without resaving it. The table records earlier results, not files included in the download.

### B. Tell touching faces from a welded Mirror seam

**Make it by hand.** Start with a closed box on a copy. In Edit Mode cut it through the middle and keep just the positive-X half. Remove any face that caps the cut; leave the four edges of the cut open. Put the object origin on the cut plane with the intended local axis, or use a Mirror Object located there. Flatten only the seam vertices onto that plane. Add Mirror on X with Merge enabled; choose a distance small enough not to catch a neighboring detail. Clipping constrains interactive edits at the plane; it is not a command to weld existing distant points.[48][138]

**Check the right mesh.** Four boundary edges on the *half* are expected; four on the *finished closed shell* are not. Inspect the evaluated mesh, or apply Mirror on a disposable duplicate and use Edit Mode → Select → Select All by Trait → Non-Manifold with boundary edges enabled.[137] Use linked selection on one side: on a welded result the selection crosses the seam. The intended number of components depends on the brief; this example explicitly calls for one closed shell. An open cloth panel or six dial markers have different contracts.

**Measured comparison:** the objects below all have ten faces and exterior dimensions of **100 × 40 × 10 mm**. Clipping is on for all three. Merge distance, where active, is 0.1 mm. The gap is measured between the innermost X rings of *this fixture*.

| Variant | Evaluated vertices | Connected components | Boundary edges | Seam gap |
|---|---:|---:|---:|---:|
| Seam on plane, Merge on | 12 | 1 | 0 | 0 mm |
| Seam on plane, Merge off | 16 | 2 | 8 | 0 mm |
| Half starts 1 mm from plane, Merge on | 16 | 2 | 8 | 2 mm |

All three results matched on Blender **4.5.9 LTS and 5.3.0**. The second row is why measuring a zero gap or comparing silhouettes cannot prove the vertices are shared. The third is why increasing a global weld tolerance is a poor first fix. Move the intended seam back onto the correct local plane and repeat the check. The test counts face incidences and connected components; it is not a general detector of self-intersection or bad normals.

Run [mirror_seam.py](../scripts/mirror_seam.py) with `compare`. Output: one `MIRROR_SEAM` JSON line. The command reports its new measurements directly.

### C. Rebuild one circular layout in two Blender versions

**Brief:** build six dial marks, then nine, on the same radius. Make each marker a single small face so its evaluated face center measures its position. Geometry is supposed to stay separate. The test below uses a 30 mm radius, not the artistic radius from Kolar’s flower.

| Blender | Make the layout | If it fails |
|---|---|---|
| 4.5 LTS | Leave the object origin at the dial center. In **Edit Mode** offset the marker to radius 30 mm. Add Array, Fixed Count, only Object Offset enabled. Use an Empty at the *same origin*, with unit scale and a Z rotation of 360° divided by the count.[51] | A spiral suggests translation or scale is accumulating; turn off Relative/Constant Offset and check both object transforms. When count changes, change the Empty’s rotation too. |
| 5.3 | Start with the marker centered on its own origin. Add the stock **Array** node modifier, Shape **Circle**, **Full**, axis **Z**, Count Method **Count**, radius 30 mm. This asset supplies the radius: do **not** also offset the base mesh by it. Realize instances for mesh inspection; leave Merge and randomization off.[147] | If you see only Relative/Constant/Object Offset, check whether you picked the legacy modifier. If you see one input face in Edit Mode, inspect the evaluated output, not just the cage. |

**Measured:** six distinct centers on both versions, all at 30 mm, six gaps of 60° including the wrap from the last to the first. Changing the count to nine gave nine distinct centers with nine gaps of 40°. These are centroid measurements, not a claim that differently shaped petals or markers will never overlap.

Run [radial_study.py](../scripts/radial_study.py) with `--count 6` or `--count 9` in a fresh process. It chooses the 4.5 modifier or the 5.3 bundled Essentials asset by runtime version, reads the evaluated polygon centers and prints `RADIAL_LAYOUT` JSON. Other Blender versions are not claimed by this script; the PDF’s 5.0 menu is also documented in that version’s manual.[146]

### Read shading last

If a silhouette is faceted, compare the outline against a plain background before changing normals. **Shade Smooth** interpolates the shading; it does not add any vertices. The old mesh-data Auto Smooth setting changed in Blender 4.1; the 4.5 manual’s **Object → Shade Auto Smooth** adds the **Smooth By Angle** modifier. The old label in a book can be partly right while an old checkbox location is wrong.[142][148] If the outline is right but the reflection kinks, inspect winding, overlapping faces and edge sharpness before adding more geometry. If the cross-section is wrong, changing roughness or normal maps cannot fix it.

### Run without changing an open project

From the installed skill directory, set `PY` to the full path to an isolated Python with the official Blender module. See [First labs](lab-notebook.md#chapter-first-labs) for the tested 4.5.9 setup. For 5.3.0 the tested combination was CPython 3.13 and `bpy==5.3.0`, including its bundled Essentials assets. Each command starts a **fresh background process**. The seam and marker comparisons are in memory; the grommet commands write only new files. The commands need no network once the Blender runtime is installed.

```sh
"$PY" -B scripts/mirror_seam.py compare
"$PY" -B scripts/radial_study.py --count 6
"$PY" -B scripts/radial_study.py --count 9
OUT=$(mktemp -d "${TMPDIR:-$PWD}/grommet.XXXXXX") || exit 1
"$PY" -B scripts/grommet_lab.py build "$OUT/practice.blend"
"$PY" -B scripts/grommet_lab.py verify "$OUT/practice.blend" "$OUT/practice.json"
```

With a matching Blender executable, an equivalent invocation is `blender --background --factory-startup --disable-autoexec --python-exit-code 1 --python scripts/mirror_seam.py -- compare`. The reported measurements were taken through `bpy`, not by driving a desktop UI.[5]

### Sources

[5] https://docs.blender.org/api/current/info_advanced_blender_as_bpy.html — Blender API: Blender as a Python Module
[48] https://docs.blender.org/manual/en/4.5/modeling/modifiers/generate/mirror.html — Mirror Modifier - Blender 4.5 LTS Manual
[49] https://docs.blender.org/manual/en/4.5/modeling/modifiers/generate/solidify.html — Solidify Modifier - Blender 4.5 LTS Manual
[51] https://docs.blender.org/manual/en/4.5/modeling/modifiers/generate/array.html — Array Modifier - Blender 4.5 LTS Manual
[62] https://docs.blender.org/manual/en/4.5/modeling/meshes/editing/edge/bridge_edge_loops.html — Bridge Edge Loops - Blender 4.5 LTS Manual
[137] https://docs.blender.org/manual/en/4.5/modeling/meshes/selecting/all_by_trait.html — Select All by Trait - Blender 4.5 LTS Manual
[138] https://docs.blender.org/manual/en/5.3/modeling/modifiers/generate/mirror.html — Mirror Modifier - Blender 5.3 Manual
[142] https://developer.blender.org/docs/release_notes/4.1/modeling — Blender 4.1 release notes: mesh shading and Auto Smooth
[143] https://docs.blender.org/manual/en/5.3/modeling/meshes/tools/spin.html — Spin - Blender 5.3 Manual
[146] https://docs.blender.org/manual/en/5.0/modeling/modifiers/generate/array.html — Array Modifier - Blender 5.0 Manual
[147] https://docs.blender.org/manual/en/5.3/modeling/modifiers/generate/array.html — Array Modifier - Blender 5.3 Manual
[148] https://docs.blender.org/manual/en/4.5/scene_layout/object/editing/shading.html — Shading - Blender 4.5 LTS Manual

<a name="chapter-made-objects"></a>

## Manufactured objects, miniatures and soft goods

**By Noa3.** These are build recipes and acceptance tests, not claims that a car, a train, a computer and a sewn toy were all produced for this edition. Start with what the object touches, what moves and the size of its largest shot. Use dimensions from the actual reference variant; a plausible-looking port which no plug can enter is a failed product model.

### Automotive — reflections are a measurement tool

1. Pick the exact body generation and wheel option. Align side/front references with a common wheelbase and ground line, not by matching the silhouette of an arbitrary perspective photograph. Block tire contact patches, wheel arches, cabin volume, beltline and overhang. Turn all trim off; the car should already have the right stance.
2. Build a small number of continuous body patches with controlled subdivision and continuous running edges at the shoulder line. Resolve windscreen curvature and wheel opening **before** cutting panel gaps, lights and handles. Make tire sidewalls, tread, glass thickness, lamp enclosure and paint separate material/geometry decisions.
3. Sweep long rectangular reflection cards across a neutral glossy body. Alias' diagnostic reflection tools use strip reflections/light tunnels to expose surface behaviour; the Blender transfer is a lighting diagnostic, not a certification of automotive Class-A geometry.[366] A kink traveling over the middle of a supposedly continuous panel means fix the control cage, not clearcoat roughness. Inspect the deliberate character crease separately. Body-coloured base plus a clear coat is a useful paint start; keep flake below the pixel scale at which it sparkles from frame to frame.

### Railway — wheelset → bogie → body → platform

Choose one prototype and period: tram vs intercity car is a different floor, doorway, suspension and curve problem. Alstom describes bogies as assemblies integral to train dynamics; do not model one decorative wheel stuck to each carriage side.[358] Set track gauge, wheel spacing and wheel diameter from **that reference**. Model a reusable axle/wheelset, put it in a bogie collection and let the body bridge its supports. On a bend, aim each bogie along its own local tangent; connect the body using the chord between its two support points. Model couplers, bump stops or bellows only where the prototype has them. Follow a door from platform edge to threshold and seat. Check wheel contact, swept corners at a bend and clearance between coupled cars; if platforms clip, fix the station/track/car geometry rather than reducing motion blur. For an overhead-powered vehicle, check the relationship between roof equipment and the modeled wire in side view.

### Computer parts, peripherals and product design

Framework publishes external CAD for the Laptop 16 system and modules and separates input modules and touchpad parts in the hardware documentation.[359] Use authorized reference dimensions to build **interfaces first**: a board datum and mounting pattern, socket opening, card and connector clearance, then component families. Make one fan blade/fin/connector pin a linked repeat, not thousands of hand-placed unique meshes. Use silkscreen or a decal for fine labels, geometry for a socket that must accept a cable. Avoid storing vendor files or logos in a handoff unless the rights cover that use.

For a keyboard, establish center spacing and profile per row; a spacebar needs its own geometry and stable travel. For a mouse, establish palm slope, finger contact, separable button gaps and a scroll wheel with clearance. Route the cable through strain relief and test the connector at both ends. Design a product around the grip, button travel, service opening and assembly order: make a clay hero view, a hand-scale orthographic plate and an exploded view along the **real assembly axes**. Check an inserted plug, an openable lid and a readable status symbol before scattering screws. Replace floating decals, unreadable labels or impossible part removal with a physically supported solution.

### Collectible figure on a stand; diorama

Pose the figure first. Trace the load from foot, flying support or peg down to the base. Put a socket or keyed peg where it actually supports the cast; hide it in the design, not by floating one mesh above the other. For a manufactured miniature, test the proposed split/cast seams, fragile tips and gravity projection onto the footprint. Compare silhouette at shelf-view distance and from the back; a flattering hero view alone won't reveal a stand going through a leg.

A **diorama** needs a slice of a world, not an assortment of assets: pick one event and a scale, cut the terrain to reveal an intentional edge, group props into foreground cue / action / backdrop, and leave a quiet area around the figure. Tie wear, footprints or bent plants to the action. Test it in untextured gray, from player eye height and from the intended display angle. If viewers cannot identify the subject in a thumbnail, remove competing shapes before increasing depth of field or saturation.

### Plush construction and the Fumo reference

A soft toy is a collection of cut panels held by seams, not a smooth figurine with fur added. Draw front/side patterns with darts or a gusset for head depth, mark seam pairs and grain, and leave a sensible closure. In Blender, block shell panels, stitch corresponding borders with loose connector edges, pin only the required regions and relax on a low-resolution copy. Blender Cloth sewing springs join vertices with edges not belonging to faces; finite sewing force is preferable to unlimited initial pulling.[29] Use thickness, embroidery and fine nap only after the silhouette works. For a game asset, transfer the settled shape to a clean mesh and bake small stitches rather than transporting a cloth cache.

Gift's official Reimu product listing specifies height **in the seated state**; it is visual/product evidence, not a published sewing pattern.[365] For a Fumo-like original, compare head/body ratio, distance between embroidered eyes, large planar hair/hat pieces, short limbs and the footprint of a seated pose. Build the face as colored cloth or embroidery with small, intentional relief; use directional sheen or restrained fuzz for the nap. Check the character in a flat front view and check seam bulge in grazing light. If it reads like PVC, soften transitions at stuffed seams and change the highlight before simply adding more fibers. Do not pass off an original as licensed merchandise or treat a photograph as authorization to reproduce the design.

### Sources

[29] https://docs.blender.org/manual/en/4.5/physics/cloth/settings/shape.html — Shape - Blender 4.5 LTS Manual
[358] https://www.alstom.com/solutions/components/flexx-bogies-safety-reliability-and-comfort-all-trains — Flexx bogies: Safety, reliability and comfort for all trains
[359] https://github.com/FrameworkComputer/Framework-Laptop-16 — GitHub - FrameworkComputer/Framework-Laptop-16: Documentation around the Mainboard and other key parts of Framework Laptop 16
[365] https://www.gift-gift.jp/nui/nui001.html — 東方ぬいぐるみシリーズ1【博麗霊夢】 ふもふもれいむ。 | グッズメーカーGift
[366] https://help.autodesk.com/cloudhelp/2024/ENU/Alias-Getting-Started/files/theory-builders/GUID-FDAFFC3D-A327-46E4-8AED-739043E175A7.html — Evaluation 2: Reflection Lines and Iso Angle

<a name="chapter-quality-brief"></a>

## A quality brief you can test

Fill this in before committing to detail. Pick the row for the actual deliverable, then replace the examples with the project's real numbers. A triangle limit, sample count or score is not a substitute for a picture judged from the intended view.

| Deliverable | Example acceptance test to agree | What it does not prove |
|---|---|---|
| Architectural still | At the delivery camera, the entrance and the route to it read in a 240 px thumbnail. In a full-resolution crop the sill has depth, the bench feet contact the floor and the tile scale agrees with a known dimension. Compare sun size at fixed exposure. | The plan is code-compliant or the lighting is physically measured. |
| Stylized or anime shot | On a neutral and a final background, the face and hand remain separate silhouettes. Review a contiguous range around the hardest turn: no unintended alternating line or shadow band. | A single striking still holds up over an animation. |
| Hero prop for a game | Record pixel height near the player, maximum expected copies, material slots and the target device. Compare two identical views at the proposed LOD switch; inspect the handle hole, silhouette and UV label. Then measure actual frame time with representative copies on the target device. | Fewer exported triangles necessarily improve frame time or a headless importer proves visual parity. |
| Procedural environment | Reproduce the featured seed, change it once, change density once, then widen the exclusion band. Record instance counts and intrusions for each relevant variant. Test player- or camera-clearance separately from center exclusion. | Clear point centers exclude every leaf, branch or collision surface. |
| Material close-up | Compare a flat coupon and the real form under the same neutral and raking light. Specify the visible scale of the largest feature, near/distant camera distance, color transform and final display size. | Matching one flat swatch from one angle gives measured optical properties. |

### Copy into a production note

```text
Subject / visual intent:
Delivery format, renderer, target device and display size:
Reference and one measurable scale cue:
Primary view / secondary or worst-case view:
Style priorities (silhouette, light groups, surface response):
Three pass/fail observations:
Budget or limit and how to measure it:
A/B variable; what stays fixed:
Evidence captured (render, frame range, import or timing):
What remains unverified:
```

When evaluating a failed test, name the **cheapest correction that changes that observation**. A doorway that disappears at thumbnail size calls for proportion, contrast or framing; higher samples only give a cleaner picture of the same problem.
