# Reproducible labs and case studies

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [First labs: reproducible Blender studies](#chapter-first-labs)
- [Advanced labs: reproduce the evidence](#chapter-advanced-labs)
- [Five ways to practise combining tools](#chapter-combined-exercises)
- [Seven source lessons: when the image looks almost right](#chapter-surface-performance-decisions)
- [What worked with very small models?](#chapter-model-checks)

<a name="chapter-first-labs"></a>

## First labs: reproducible Blender studies

These four scenes are teaching fixtures, not production assets. They use no third-party textures, HDRI, paid services, bridge or add-on server. Three have a camera render; the fourth isolates deformation, cloth and baking. Never run the generators inside an open user scene. Each requires a **new** output directory and refuses an existing path. Tested on Linux with Blender **4.5.9 LTS**, using the official `bpy` module in separate Python processes. Blender documents this module for rendering and automation.[5]

### Inspect the locally generated scenes
After generating the studies below, open `metal.blend`, `rosette.blend` or `mask.blend` in their respective output directories and press F12. For `rosette`, change **Count** on its Geometry Nodes modifier. For `mask`, compare frames 1, 13 and 25. The `technical` fixture deliberately has no render camera; use the rig, cloth and UV editors to inspect it.

### Regenerate in separate processes
From the **English skill directory** containing `scripts/`, run in a POSIX shell:

```sh
SKILL=$(pwd -P)
OUT=$(mktemp -d "${TMPDIR:-$PWD}/blender-labs.XXXXXX") || exit 1
for STUDY in metal rosette mask; do
  blender --background --factory-startup --disable-autoexec --python-exit-code 1 \
    --python "$SKILL/scripts/lab.py" -- "$STUDY" "$OUT/$STUDY" || exit 1
done
blender --background --factory-startup --disable-autoexec --python-exit-code 1 \
  --python "$SKILL/scripts/deformation.py" -- "$OUT/technical" || exit 1
blender --background --factory-startup --disable-autoexec --python-exit-code 1 \
  --python "$SKILL/scripts/verify_labs.py" -- "$OUT"
```

**Tested desktop-free route:** Start with a new `OUT` as above (do not reuse generated study directories). Set `PY` to the absolute path of an isolated Python interpreter with `bpy==4.5.9` installed. The Linux x86-64 reference environment uses CPython 3.11, the matching PyPI wheel and a working graphics driver for EEVEE. If provisioning your own environment with `uv`, use `uv venv --no-project --python 3.11 "$OUT/venv"`, then `uv pip install --python "$OUT/venv/bin/python" 'bpy==4.5.9'` and `PY="$OUT/venv/bin/python"`. Do not install into the system or agent interpreter. No desktop window or port connection is required. A missing EEVEE graphics context is not a passing cel test: do not silently substitute a different renderer.

```sh
for STUDY in metal rosette mask; do
  "$PY" "$SKILL/scripts/lab.py" "$STUDY" "$OUT/$STUDY" || exit 1
done
"$PY" "$SKILL/scripts/deformation.py" "$OUT/technical" || exit 1
"$PY" "$SKILL/scripts/verify_labs.py" "$OUT"
```

The verifier expects the layout produced by the included English generators. It does not verify files from previous workshop editions or third-party scenes.

### What each test demonstrates
| Study | Variation | Evidence and limits |
|---|---|---|
| `metal` | Relief, narrow/wide bevels, metal/enamel/rubber and three area lights | Cycles/AgX, 600 × 500. Circumferential highlights reveal the knurling; graduations and pointer are separate. This is not a measurement of the gloss of real brass. |
| `rosette` | Count 12 → 24, instance/mesh switch | 3456 → 6912 realized Blender polygons. Reopened source retains 24 instances without realization. Only petals exported: reimport into empty Blender gives one mesh, jade material, 12672 triangles, bounds 2.9 × 2.9 × 0.232 Blender units. Not tested in a specific game engine. |
| `mask` | Rigid turn −14°, 0°, +14°; EEVEE, Standard, three cel bands | Each palette color covers more than 1500 matching pixels at each test pose; edge transitions/AA are not the target of the count. The original v1.1.0 review also rendered consecutive frames 9–17 after reopening and found the cheek and light edge readable over that interval. The English verifier checks three rendered poses and samples five rotation values, not a full animation or facial deformation. |
| `technical` | Two-bone FK, relative shape key, cloth pinned at one edge, two UV islands | Tip travel 0.84524 Blender units, root stationary; shape lift 0.15. Free cloth point fell about 0.93, pin stayed put. Center probes in the 64 × 32 emission-bake PNG are red/blue; the image is also packed after reopening. No clothing collision or high-to-low normal bake tested. |

### Develop the exercises
- **Geometry:** Change only radius, then only count. If a petal touches the rim, decide whether the rim should also be parameterized. Distinguish instanced and realized output in the Spreadsheet.
- **Look development:** Turn off the knob's rim light. Restore the original light and change only the roughness range. Compare side by side from the same camera; changing exposure or camera at the same time invalidates the comparison.
- **NPR:** Move a ramp threshold and check the three poses again. Compare two- and three-band versions with the same reference. For frame differences compare originals at **identical resolution**; a downsized preview is not a measurement image.
- **Further tests:** Build and measure separate fixtures for head retopology under Smile/Blink, Line Art during a camera move, a high-to-low normal bake or cloth against a moving body. These workflows are documented but not demonstrated by these four fixtures.

[Runtime source](sources.md).

<a name="chapter-advanced-labs"></a>

## Advanced labs: reproduce the evidence

These earlier workshop case studies record measured controls in Blender 4.5.9 LTS. Their scene files and builders are not bundled here. Apply the acceptance checks below to your own scene, or start from the self-contained exercises in the preceding chapter.

### Meridian gallery and surface library



The gallery comparison held the camera, materials and exposure fixed. Its separate six-material board included a stripe behind the transmissive glass and close-ups of oak and linen.

| What was actually tested | Result in the packaged exercise |
|---|---|
| Editable construction | Four arches at Y = −2.1, 0.3, 2.7 and 5.1 m share one source mesh. No non-manifold edges in that mesh; measured clear span 4.04 m. |
| Lens and alignment | Perspective camera, 28 mm, 1.55 m above floor. Two world points on the same vertical projected to the same image X (0.000000 px drift in the saved setup). This is not a structural or accessibility calculation. |
| Light isolation | 800 × 536, 48 Cycles samples, same camera, materials, seed, exposure and direction. Only the sun angular diameter changed: **0.75° vs. 14°**. On one calibrated vertical scan at x = 300, the displayed floor-shadow transition between 8-bit luma 100 and 70 spanned **1.12 vs. 10.67 px**. The check is specific to these images; it is not a penumbra prediction or physical radiometry. |
| Surface controls | Six equal-width samples reopened with connected Surface outputs. The stripe card sits behind the transmissive glass; high-frequency weave can disappear at a distance, which is why the board includes a separate crop. |

**Try it:** orient the camera upward instead of shifting it and inspect the pier verticals. Restore the camera. Then move just the sun direction to see how the architectural reading changes independently from the shadow-width experiment. If you save a variation, give it a new filename.

### Chalkpath: keep the path open while changing the planting



The original Chalkpath study used an explicit seed, density and exclusion half-width. Four plant prototype meshes were kept editable, their local +Z following the sloped surface. The same width drove both the ground shader and exclusion mask.

| Evaluated variation (Blender 4.5.9) | Plant instances | Root centers in the restricted band |
|---|---:|---:|
| Seed 17, standard settings | 3,712 | 0 |
| Seed 83, standard settings | 3,669 | 0 |
| Seed 17, half density | 1,853 | Checked by the generator |
| Seed 17, 1.60 m exclusion half-width | 3,440 | 0 |

Resetting the seed reproduced the sorted position hash. Opening the saved scene in a new process reproduced the full seed-17 measurement. The evaluated host still had the 11,408 polygons of the terrain; plants remained instances. **Scope:** clearance is measured for plant centers along local X, not perpendicular to the curved path; foliage may overhang. Random distribution does not guarantee a minimum plant-to-plant distance.

### AURA / 07: a portable service lamp



AURA / 07 separated the visible lamp into component groups and the collision proxy into its own export. The two visual LODs shared packed pigment, metallic–roughness and emission atlases; overlapping UVs were deliberate and would not work as a unique lightmap unwrap.

| Export | Triangles | Render primitives / materials | Role |
|---|---:|---:|---|
| `AURA_07_LOD0.glb` | 6,680 | 1 / 1 | Near view; rounded handle |
| `AURA_07_LOD1.glb` | 1,928 | 1 / 1 | More angular handle; unchanged outer dimensions and bottom-center pivot |
| `AURA_07_COLLISION.glb` | 36 | 1 / 0 | Separate coarse convex proxy; do not render |

Both visuals measured 0.138 × 0.128 × 0.2582 m in Blender X/Y/Z. LOD1 removed **71.14%** of the triangles. After GLB reimport the silhouette intersection-over-union was **0.988384**, from one portrait camera at 350 × 400, not all angles. The original verifier decoded the binary payload independently of Blender, checked UVs, indices and embedded PNGs, and rendered both masks.

#### Real engine gate (optional)

In your target engine, import your two visual LODs and a dedicated collision proxy. Verify the bounds, show one visual at a time, then run a ray that must hit and one that must miss.

In the original AURA / 07 test, Godot 4.5.1 read one textured surface and UVs on each visual, with matching Y-up bounds. A ray through the center hit the constructed convex proxy; an offset ray missed. An invalid test pair using LOD0 twice was rejected. The proxy intentionally filled the handle hole. This checked import and simple collision, **not** GPU appearance, automatic screen-space LOD switching, dynamic light output or frame rate on the target device.

### Before sharing a scene or a render

A packed texture can work on another machine **and still retain a private filename**. In Blender 4.5 the image's `filepath` and each entry in its `packed_files` collection have separate paths. In a distribution copy of a single-tile texture, keep the image and its packed unpack-destination on the same `//`-relative filename. Reopen the copy with its original working folder unavailable; check that the packed bytes and displayed material survived. Do not use this single-image shortcut for tiled sequences or linked libraries.

Turn off **Output Properties → Metadata → File** before making a render to share. An invisible stamp is not enough: Blender can put the absolute scene path in PNG text metadata even when there is no visible overlay. Inspect the exported file, not just its pixels. When removing metadata from existing PNGs, retain their pixel and color-profile chunks; compare the decoded image or original pixel stream, not the total file hash. Keep the working originals.

In the original fixtures the Shading workspace remembered the file browser's last directory. Shortening an image or render path left pieces of the old name **after the string terminator** in the saved file. For a privacy-sensitive handoff, inspect the decompressed `.blend`, not just the paths Blender displays. Build a fresh distribution copy in a neutral working directory and compare packed textures and rendered pixels with the approved originals. Do not run a blind binary search-and-replace on a scene.

<a name="chapter-combined-exercises"></a>

## Five ways to practise combining tools

**Author: Noa3.** These exercises combine lessons already documented in the [creator notebook](channel-register.md). The sources teach the ingredients, not these combined shots. All five are **proposed exercises**, not delivered scenes or reproduced results. Pick the one whose failure would matter in your project.

| Exercise | Build the smallest useful version | Try to break it |
|---|---|---|
| A swinging sign and a camera cut | Key one Grease Pencil sign rotating about its hinge. Bind two cameras to timeline markers, then retime the cut so it happens as the sign passes vertical. The source ingredients are a Grease Pencil animation and marker-controlled camera changes.[203][187] | Step across the loop with one fixed camera first. Then step across the camera cut. If the hinge drifts, fix the pivot; if the wrong view flashes for one frame, fix the marker instead. |
| A staircase with a curved handrail | Array only enough treads to see the rise and run. Shape a rail profile with straight and smoothly joined spans; place repeated fittings on the intended local axes.[196][210][173] | Widen the rail but keep the tread pitch. In side view, inspect a tread/stringer contact and the tangent where the rail bends. A visually smooth rail does not fix a floating tread. |
| A paint roller reveals a printed label | Keep box projection for the substrate, UVs for the label and a separate Dynamic Paint coverage mask. Multiply label alpha by coverage.[218][242] | Enlarge the label without moving the roller. The reveal must still follow the roller, with no black rectangular border and no change to the size of the background grain. |
| A spring-loaded display plinth | Drive coil spacing from platform travel. Animate the displayed object turning independently, with frame-driven rotation if appropriate.[213][231] | Freeze the turn, test both platform limits, then change the turn speed. The top of the coil must remain attached in all three cases. Don't tune a physics solver to repair a broken transform relationship. |
| A buoy with a decorative chain | Follow the height and tilt of a small patch of water. Deform the repeated links along a path attached to the buoy.[191][181] | At a crest and trough, inspect both tilt and chain attachment. A path-deformed chain is not a simulated tether; don't present it as a buoyancy or tension test. |

### Sources

[173] https://www.youtube.com/watch?v=8E4fNWvJhMU — Blender Beginner Tutorial – Understand Global vs Local Coordinates
[181] https://www.youtube.com/watch?v=C97pyuF8VRA — How to Make a Chain in Blender – Beginner Tutorial
[187] https://www.youtube.com/watch?v=KTynnt8UyCg — How to animate cameras switching in Blender #b3d #3danimation #blender3d
[191] https://www.youtube.com/watch?v=M7pCrEN3h88 — Make Objects Float in Blender in 1 Minute!
[196] https://www.youtube.com/watch?v=OnAmoFFn1jQ — How to make stairs in Blender
[203] https://www.youtube.com/watch?v=TrsL2AOHwYw — Intro to Grease Pencil in Blender - A Tutorial for Beginners
[210] https://www.youtube.com/watch?v=a4p6_e-jDsw — Part 2, Curve Aligned handles are awesome!
[213] https://www.youtube.com/watch?v=bMDj_GrX1qI — How To Make a Bouncy Spring in Blender!
[218] https://www.youtube.com/watch?v=dR-RrB8M8Ck — Seamless Cubic Mapping, No UVs! #shorts
[231] https://www.youtube.com/watch?v=mcRWIq0sk5g — How to Make Constant Animation in Blender
[242] https://www.youtube.com/watch?v=waoF3XpkPlE — Blender Tutorial - Applying a Texture/Logo to Dynamic Paint!

<a name="chapter-surface-performance-decisions"></a>

## Seven source lessons: when the image looks almost right

**Author: Noa3.** Use the left side of each entry to find the source; use the right side to test your own shot. These are selected public passages, not seven reproduced Blender builds. The earlier [surface and motion notes](learning-notebook.md#chapter-surface-motion-sources) cover ten different selections. A timestamp here identifies a narration block or a creator chapter, not an exact frame of a mouse click.

#### A crate looks correct until a checker is applied — Blender Inferno

**Source.** In the Blender 4.5 cuboid lesson, the **01:55** narration block uses a grid to spot stretch. At **07:02**, applying the object's scale is followed by a second unwrap; applying the scale alone is not the last step.[316]

**Try.** Duplicate a static, elongated crate with identical seams. On one copy, apply Scale in Object Mode, then unwrap the faces again in Edit Mode. On the other, keep the old UVs. Compare the *shape* of individual checks on the longest side, not just how much UV space the islands occupy. If both look equally stretched, check that the material actually reads the UV map you edited. Don't apply transforms to a bound character as a texture fix.

#### A gloss map makes polished metal look chalky — Blender Inferno

**Source.** The Blender 4.3 creator description labels **02:51** as roughness and **03:27** as gloss. Those chapter markers do **not** establish the creator's node wiring or the encoding of any particular texture pack.[317]

**Try.** Read the supplier's channel definition. If their linear smoothness is explicitly the complement of roughness, load it as Non-Color and subtract it from one **once** before Principled Roughness. A map labeled specular intensity is not evidence for that conversion. Keep one broad area light fixed: the polished control patch should have a narrower reflection than the scuffed one. If they exchange places, inspect inversion and color space before moving the light.

#### A chipped brick looks like foam — Ryan King Art

**Source.** The single-brick narration starts from approximate real proportions and roughly square faces (**00:50**, **01:44**); the damage ramp is later used for displacement, with the amount reduced (**17:45** block). No construction-standard brick dimension is supplied.[318]

**Try.** Compare an undamaged edge with one shallow chip at the same camera distance. Distribute geometry along the long side before raising subdivision everywhere. In silhouette, a chip should remove a piece of the edge, not swell the whole brick. Keep pore-scale grain in shading if it never affects the contour.

#### Fingerprints float next to their dents — Ryan King Art

**Source.** In the **09:48** block the same Voronoi pattern relates fingerprint ridges and thumb depressions. A separate ramp drives roughness; the **10:36** block changes how shiny the clay looks.[319]

**Try.** Move one press mark: its ridges and hollow should travel together. Then change only the roughness ramp and repeat under a raking light: the sheen should change, but the hollow should not move. Share a mask when two effects have the same physical cause; do not reuse it for every channel.

#### One material is missing from a baked atlas — Ryan King Art

**Source.** The shared-map tutorial assigns the same bake image as the active target in the participating materials. Diffuse color is baked with Direct and Indirect off. The sRGB versus Non-Color clarification is in the **creator's written description**; **00:51**, **05:21** and **09:50** are chapter starts, not exact node actions.[320]

**Try.** Give two differently colored mesh parts disjoint UV islands. Bake both into one fresh target; reopen and sample a texel well inside each island. Light the asset from the other side to expose baked-in lighting. If one patch is absent, check the active target in *that material*. For separate bake runs that share a target, plan clearing explicitly so the second run cannot erase the first.

#### The material pops when a moving shot loops — Ryan King Art

**Source.** The loop lesson uses two matching 4D Noise nodes with offset W animation, blends from one to the other and sets linear keys. The closure key sits one frame after the last exported frame (narration blocks from **01:35** and **02:22** onward).[321]

**Try.** For a short practice loop, take A from W=1 to 2, B from W=0 to 1, and blend A→B over the same interval. At the end B now samples A's starting W. Keep the same coordinates, scale and detail on both. Compare the first/closure images, **then** play the last exported frame into the first: equal endpoints alone do not prove smooth motion. Disable the blend as a failure control. Don't export the duplicate closure frame.

#### A captured face misses the consonant — Jamie Dunbar, Dragonboots Studios

**Source.** Indexed narration at **06:30–07:01** separates Live Link Face shape-key import from loading the audio. At **07:19–07:57** Dunbar listens for a missing M/B/P lip seal, preserves the captured animation and keys a local mouth correction. His later Faceit control-rig example is a distinct add-on path. These are spoken excerpts, not visual review or proof that either add-on is installed.[322]

**Try without add-ons.** On a head you may edit, use a licensed or self-recorded phrase. Align the sound and shot frame rate before touching the lips. If every syllable is late, fix the offset or rate instead of sculpting more expressions. If only one bilabial misses, preserve the base action and adjust a local lip-seal target on that beat. Check the profile one frame on either side and listen at normal speed: the lips meet without crossing and reopen into the vowel. A target named `mouthFunnel` is rig-specific, not a universal lip-close control. No speaking character is certified by this workshop.

### Sources

[316] https://www.youtube.com/watch?v=YR-ns4e7hVk — Blender Inferno: UV Unwrapping Basics in Blender 4.5 for Absolute Beginners!
[317] https://www.youtube.com/watch?v=ojr_wK2FNZs — Blender Inferno: How to Apply Gloss Maps Properly in Blender 4.3...
[318] https://www.youtube.com/watch?v=U7Fxp-GzGLg — Ryan King Art: Procedural Brick Material 🧱 (Blender Tutorial)
[319] https://www.youtube.com/watch?v=eYw5sbF5bhU — Ryan King Art: Procedural Clay Material (Blender Tutorial)
[320] https://www.youtube.com/watch?v=wG6ON8wZYLc — Ryan King Art: Bake Multiple Materials to One Texture Map (Blender Tutorial)
[321] https://www.youtube.com/watch?v=GT6-_FZ9VnA — Ryan King Art: How to Loop Procedural Textures in an Animation
[322] https://www.youtube.com/watch?v=aM_cGEgkCV0 — Jamie Dunbar: Face animation is easy now!

<a name="chapter-model-checks"></a>

## What worked with very small models?

**Do not delegate routing to a tiny model when the user already knows what has to pass.** Select the route yourself. The picker and `workshop.py step ROUTE` print the same first action, observation and `untested` status without running a language model. This is a fallback you can use even if a model invents tools, repeats the question, mixes up animation with game physics or does not follow an output format. See [portable use](portable-use.md).

### Test 1 — can the model pick the topic unaided?

Six short briefs mixed English and German. They pitted similar subjects against different deliverables: a moving barrier for a film versus collision in a game; a planted bed versus the surface finish beside it. The model received the **entry document only**, not the deeper chapters or a human-selected card. Both versions used identical questions, seven plain-English answer labels in fixed order, greedy decoding, a 4,096-token limit, and a fresh network-isolated CPU process for each question. Two additional free-response probes asked for a next step with no Blender access and after a game prop was reimported in Blender.

| Runtime | v2.0 entry: exact route | v2.1 entry: exact route | Concrete target-engine collision test proposed? |
|---|---:|---:|---|
| Qwen2.5-0.5B-Instruct, Q4_K_M | 0 of 6 | 0 of 6 | No, in either condition |
| SmolLM2-360M-Instruct, Q8_0 | 1 of 6 | 0 of 6 | No, in either condition |

The scoring is deliberately narrow. SmolLM2 replied `game` for the game barrier in v2.1: the **meaning was right** even though the requested label was `game asset`. It also replied `game` for the movie, which genuinely chose the wrong route. Neither model supplied both an honest status and an actionable next step for the no-tools teapot request. The baseline responses were identical on a repeat. Fixed option order, labels that do not all match the skill's route IDs, six briefs, and two very small quantized models limit the inference. This experiment **does not show improved autonomous routing** or say how a larger model performs. It does not evaluate Blender execution.

#### Does asking for the actual route IDs change that conclusion?

The same six briefs were also tested with the **ten IDs printed on the cards**, once in card order and once in reverse order. The entry document itself did not change. The scoring contract allowed either `architecture` or `render` for the station hall: its lighting reveals the space. The other five briefs each had one accepted route.

| Model | Exact ID, card order → reverse | Correct meaning, card order → reverse |
|---|---|---|
| Qwen2.5-0.5B | 0/6 → 1/6 | 0/6 → 1/6 |
| SmolLM2-360M | 0/6 → 0/6 | 1/6 → 1/6 |

Qwen picked `model` on every brief in card order. Reversing the choices changed all six selections. Smol chose `render` in backticks on every turn, so it got the hall's meaning right without returning the requested bare ID. Neither selected the correct route for any of the five unambiguous briefs in either order. These historical observations cover two models and two orders, not a comparison against v2.0. The raw chat logs are not included.

### Test 2 — can it adapt the right card to a different brief?

A person supplied the correct **game, material, render or procedural** card. Routing was not tested here. Four new briefs asked for one action and a discriminating observation in at most two sentences: an impassable archway, enamel that looks too glossy, a hard window shadow and a scatter exclusion zone. The English and German briefs, output limit and inference settings were identical between the archived entry and selected-card arms. The model had no Blender access. The third arm asked it to copy the card's `Check:` line without a brief; that is a different task.

| Model | v2 advice: strict / partial / fail | Selected card: strict / partial / fail | Exact line copy |
|---|---|---|---|
| Qwen2.5-0.5B | 0 / 0 / 4 | 0 / 1 / 3 | 4 of 4 |
| SmolLM2-360M | 0 / 2 / 2 | 0 / 0 / 4 | 0 of 4 |

Qwen proposed a player-sized hit and miss for the archway, but copied steps for a moving gate and ran out of output. For the lighting brief it advised **lowering** the Sun Angle to soften a shadow: the direction is wrong. Smol's copy for the archway kept the main physics check but left out the second sentence. Neither model confirmed the absence of a test when explicitly asked about the window render. A repeat produced the same raw generated text in all 24 cases/arms across the two models. Four paired briefs, one non-blind advice grading pass, and a short output limit do not support a general ranking. **A copied check is not a good diagnosis or a performed test.**

### Deterministic fallback — what is and is not verified

The picker has ten routes. In a local Firefox session with page JavaScript disabled, each opened its own first step; downloading the game card produced exactly the text distributed beside the picker. Each short output was 34–42 whitespace-separated words including the route and status. No shell, account or inference is needed for the HTML. For example, when roots appear on a path, the procedural first check asks you to inspect the allowed-region mask **before instancing**. If two seeds happen to look clear, that still does not prove every seed works or that leaves do not overhang.

The deterministic route is not a score for either model. It puts the choice in the user's hands and avoids substituting a lucky guess for an observable check.
