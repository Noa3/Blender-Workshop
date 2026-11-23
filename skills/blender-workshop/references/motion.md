# Animation, cloth and handoffs

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [Animation: block a motion, close the loop, deliver the frames](#chapter-animation-workflow)
- [Motion field study: what stays in contact?](#chapter-motion-field-study)
- [Production transfers: contact, capture and reusable assets](#chapter-production-transfers)
- [Anime follow-through: weight without the jelly tremor](#chapter-secondary-motion-direction)
- [A cloth file that still works on another machine](#chapter-cloth-cache-handoff)

<a name="chapter-animation-workflow"></a>

## Animation: block a motion, close the loop, deliver the frames

**Route: `animation`.** Does the motion communicate the intended beat at playback speed? Generate `Tide-Register.blend` locally with [the optional Tide Register exercise](portable-use.md#tide-register). Play frames **1–48** at **24 fps** twice. The needle sweeps past a reading, settles, holds briefly, then crosses the center toward the opposite side. Its spindle should not travel. This is a two-second mechanical test, not a character mocap example.

### 1. Block the idea before polishing the curve

Write down **what moves, what must stay planted, and when the viewer should notice the change**. Set the delivery frame rate and range in Output Properties before keying. Pick a camera or side view where the path is legible. Place a visible stationary reference at the joint or foot contact. On a copy of a mechanical asset, put the animated object's origin at the hinge, or parent it to a correctly placed pivot. Rotate by hand and undo; if the hub describes a circle, fix the pivot before setting keys.

At the first frame hover over the one transform you intend to animate (for the needle, **Z Rotation**) and press `I`. Move to the extreme, change that value, key it, then mark the return. Use the Dope Sheet to move a beat in time without changing the pose. Start with **Constant** interpolation (`T` over selected keys in the Dope Sheet or Graph Editor): you can now read each pose and hold without in-between motion disguising it.[293] For a body, block support, passing and landing poses from the camera; don't key every finger to solve a late landing.

| Tide Register beat | Frame(s) | What to look for |
|---|---:|---|
| Cross center | 1, 25 | Same location, opposite travel direction. Identical poses need not mean identical motion. |
| Overshoot | 10, 34 | The largest excursions, −59° and +59° around local Z. |
| Settle and hold | 14–17, 38–41 | The needle backs off to −52° or +52°, then stays still. |
| Close for inspection only | 49 | Matches frame 1 in pose and continues in the same direction. Exclude this duplicate from playback and export. |

### 2. Separate timing from spacing

**Timing** is when the needle reaches the mark; **spacing** is how far the tip travels between frames. If the beat is late, slide the relevant keys in the Dope Sheet. If the beat is on time but feels weightless, leave the frames in place and inspect the **Graph Editor**: slope indicates rate of change of that channel, not the full spatial path.[24] Start with one channel visible.

- **Constant** is for blocking, switches or a deliberate stepped move. The interpolation on a key governs the segment **after** that key.[293]
- **Linear** gives constant change in that channel between keys. Use it to test constant angular speed; it does not guarantee constant world-space speed on a multi-joint chain.
- **Bézier** shapes acceleration and deceleration. Use Auto Clamped handles as a first pass where overshoot is unwanted; set an explicit overshoot key where it is wanted. Flatten a hold with equal values and flat intervening curve, or use Constant on the hold's first key. Inspect the frames *between* hold keys. Matching the two values alone is not proof of a still hold.[24][293]

Track the **tip** or actual point of contact rather than just the object's origin. The origin of a correct hinge barely moves while the needle tip travels in an arc. For a character, calculate a **Motion Path** for the relevant bone over the shot range, update it after editing, and inspect the planted point against a world-space marker.[301] Fix a sliding foot at its contact or root motion first; smoothing the entire action blurs the impact. For body weight, facial transitions and a measured landing, use the [motion field study](motion.md#chapter-motion-field-study).

### 3. Inspect the seam, not just its endpoints

Duplicate the first pose at the closing frame to edit the curve; play only the unique frames. Step **48 → 1 → 2**. If the needle pauses at center, check both for an extra exported frame and for an unintended ease to zero at either end. If it lurches, compare direction and distance per frame on both sides. Match the outgoing and incoming tangent in the Graph Editor for a crossing at speed; a deliberate reversal at an extreme is a different requirement. This rule applies to a pose loop: a locomotion clip with intentional root travel needs a defined displacement per cycle instead of forcing its root back to zero.

**Tide Register, reproduced in Blender 4.5.9 LTS:** the check samples evaluated geometry at every played frame and the closure. The measured spindle drift and angular variation during the holds were **0.0**. The two steps either side of the seam were about **7.73° and 7.33°**, in the same direction; they need not be numerically identical. Two stills with the same pose would not establish any of this.

### 4. Character branch: transfer, correct, then assemble

For a native two-person example rather than a transferred clip, [Between Beats](figure-workflows.md#chapter-adult-figure-staging) shows how to catch a one-frame hand flip before it contaminates the baked swing of a wrist pendant.

Do not treat these as three names for the same operation. The following is a manual route (`untested` on your rig). Dunbar's examples use third-party add-ons; this workshop requires none to play the needle. Blender's NLA does **not** retarget a skeleton by matching strip names.[299][305][306]

| Job | What to do | What should survive the check |
|---|---|---|
| **Retarget** a performance onto another rig | Preserve an untouched take. Check source/target size, facing direction and rest poses. Map the pelvis/root, then torso, arms and legs by function. Choose where root translation belongs and whether the target limb controls are in FK or IK. Test one arm and a planted foot before processing the take.[299] | The intended limb bends on the intended axis, height is plausible, the root does not travel twice, and the support foot stays on its mark. If every pose is rotated, fix the rest-pose/basis mismatch, not every key. |
| **Correct** the resulting motion | Keep the transferred Action; make a working copy or a supported correction layer. Mark the bad contact interval. Set a pelvis or foot offset for that interval; taper it to zero outside it. Compare on/off over the interval plus the adjacent frames. Dunbar's *Animation Layers* is an add-on workflow, not a required native panel.[305][306] | The foot no longer slides or penetrates, but the rest of the performance has not shifted. If both legs drift, inspect the root before compensating both feet. |
| **Assemble** already compatible clips | Give each Action a meaningful name and confirm its assigned **Action Slot** belongs to the intended data-block. In Blender's Nonlinear Animation (NLA) editor, use Action strips to place and trim actions in scene time. Check the strip's action range, scene range, scale/repeat, influence, blend and extrapolation. Solo or mute tracks to locate doubled motion.[295][296][300] | At each cut, check support foot, root position, facing and speed. A crossfade can soften a pose change; it cannot reconcile a planted foot with a moving floor. Align the clips or correct contact before lengthening the blend. |

Use footage and motion data you have permission to use. Keep the original take and the editable actions; if the receiver needs sampled keys, bake a **delivery copy** and check it in the receiving application. A successful Blender preview is not an engine-import test. No capture suit, paid add-on or third-party motion file is supplied or required here.

### 5. Render a recoverable sequence

Set a new output folder, frame range, step **1**, frame rate, camera and resolution. Render a cheap preview at the intended fps; inspect the contacts, holds and seam twice. For a final, choose a numbered **PNG** sequence (or multilayer **OpenEXR** when compositing requires the passes), then **Render → Render Animation**. With a sequence, a failed frame can be rerendered without losing a nearly complete movie.[297]

Before encoding, verify exactly the intended consecutive filenames, read the images at the requested dimensions, and compare the first, extreme, hold and last poses. Encode the verified sequence at the **same** fps, then decode or play the movie and check its frame count, range and the repeated seam. If the movie is too fast but the PNGs are correct, fix the input fps at encoding; do not retime the Action. One final camera still is useful for finish and framing, not proof of movement.

**For tracking shots with linked motion:** derive a repeating ground tile's length from the wheel circumference times a whole number of turns. Drive the near and far scenery with the same displacement and let perspective supply the parallax; a stationary nearby landmark can appear attached to the subject. Match the crank path to the pedal platform's *top*, then cold-open the delivery scene and compare the evaluated sole height as well as the foot origin. Include the check pose in the rig but not the MP4. Compare a separately rendered closure still to frame one, then measure the last-to-first change on the decoded video against normal adjacent steps—identical endpoint poses alone do not detect a duplicate frame, reversal or encoding stutter.

For the stripe that travels on the needle, use the [texturing workflow](materials.md#chapter-texturing-workflow). For chapter starts, narration evidence and the boundaries of the mocap adaptation, use the [creator lessons and source notes](learning-notebook.md#chapter-surface-motion-sources).

The [Tide Register exercise](portable-use.md#tide-register) includes a checker for the generated file. Check rendered playback separately; a pivot and two keyed poses cannot prove timing.

### Sources

[24] https://docs.blender.org/manual/en/4.5/editors/graph_editor/fcurves/introduction.html — Introduction - Blender 4.5 LTS Manual
[293] https://docs.blender.org/manual/en/4.5/animation/keyframes/introduction.html — Blender 4.5 LTS: Keyframes and interpolation
[295] https://docs.blender.org/manual/en/4.5/editors/nla/strips.html — Blender 4.5 LTS: NLA Strips
[296] https://docs.blender.org/manual/en/4.5/animation/actions.html — Blender 4.5 LTS: Actions and Action Slots
[297] https://docs.blender.org/manual/en/4.5/render/output/animation.html — Blender 4.5 LTS: Rendering Animations
[299] https://www.youtube.com/watch?v=AutNCxcK0Xc — Jamie Dunbar: Motion Capture - Retargetting
[300] https://docs.blender.org/manual/en/4.5/editors/nla/sidebar.html — Blender 4.5 LTS: NLA Sidebar
[301] https://docs.blender.org/manual/en/4.5/animation/motion_paths.html — Blender 4.5 LTS: Motion Paths
[305] https://www.youtube.com/watch?v=uIf1kNTxvZo — Jamie Dunbar: Motion Capture - Animation Layers
[306] https://www.youtube.com/watch?v=64SDRd6zkDY — Jamie Dunbar: Motion Capture - combining animations

<a name="chapter-motion-field-study"></a>

## Motion field study: what stays in contact?

Use the first two lessons to plan a landing, the third to inspect the path *between* poses, and the last three to diagnose cloth. The timestamps below point into the original publishers’ videos. The exercises are transfers, not reconstructions.

**1. Block the landing before the limbs.** [SamBam Studios — Landing Animation](https://www.youtube.com/watch?v=oB_M_RGNqFY).[94] Evidence: narration plus 18 sampled storyboard images, roughly 25 seconds apart; not continuous playback. Image times, not instruction starts: **00:45** elongated body proxy; **01:05** two sphere shapes; **01:55** juxtaposed reference poses; **02:20** low, wide stance; **04:00** key, extreme, breakdown and in-between pose list. Put the sphere origin at its underside so squash does not lift it. Block fall, compression and recovery as holds; choose a breakdown for the route, not the arithmetic midpoint. Refresh the motion path after changing a curve. Transfer: retime a two-legged puppet to preserve its foot plants rather than copying the sphere timing. The source rig supplies accessory follow-through; this is not a cloth setup.[94]

**2. Spline the body without losing the hold.** [Blender Studio — Character Animation in Blender](https://www.youtube.com/watch?v=zhktftWbumE).[95] Evidence: public recap transcript and publisher chapter markers; these are entries in the **recap**, not the longer streams. **02:55** plan counter and prop contacts; **03:40** block torso beats first; **09:40** isolate body controls and bracket the end of a hold before splining, leaving face and fingers stepped; **28:10** stagger finger contacts and *reduce* an excessive bounce.[95] Transfer: open a hinged lid, keep it still, then test how little delayed ribbon motion is enough to read the stop.

**3. Test the path through a facial selector.** [Vertex Arcade — Blender 4.0 Facial Animation with NO RIGGING!](https://www.youtube.com/watch?v=1Is3oUvHwdM).[96] Evidence: public narration transcript, with title and uploader checked on the watch page; times are transcript block starts. **05:43** lock local Y while leaving X/Z free; **07:24** round the transform to snap; **10:43** drive a shape key by distance to its icon; **11:45** remove rounding for blends or snap more finely; **13:31** an intervening icon can activate during playback. The constraint holds the plane; the driver changes the mesh. Zero distance means full weight and one means zero *at the demonstrated spacing*.[96] Transfer: key a rubber ball from flat to tall; scrub for an unintended tilted shape and reroute the selector if needed.

**4. Fix the collider before tuning the cloth solver.** [Lewdineer — Making Cloth Interaction with Body Physics](https://www.youtube.com/watch?v=WuBD1Rz7VrM).[97] Evidence: narration transcript checked against timed captions. **01:52** restrict the collision proxy to the contact area; **09:46** shorten and cap a proxy that pinches; **10:36** rebind Surface Deform after changing topology. **11:31** subdivision before Cloth increases solver geometry; **13:56** subdivision after Cloth smooths the output; **14:37** put Solidify after Cloth and before final subdivision. The driving motion is already available; these are not universal clearance or quality settings.[97] Transfer: shorten a capsule collider under a loose cuff, rebind, then replay from the same starting state before changing solver steps.

**5. Release a seam, not the anchors.** [Angel S — How to rip clothes in blender](https://www.youtube.com/watch?v=amUGn13gukc).[98] Evidence: transcript and timed captions for the opening cloth strip and a later shading note. **00:21** the author's mid-simulation split jumps; **00:54** pre-split and pin matching boundaries; **01:25** use a seam-only group in Vertex Weight Mix; **01:39** add at *scene frame* 40, subtract at 41; **02:36** a final Weld reduces the shading break while the seam is held. This brittle, predetermined seam is not stress-driven tearing.[98] Transfer: stretch a streamer between pegs. Scrub the release frame and its neighbors; only the center should part.

**6. Separate gravity, solver cost and wind.** [Disabled Blenderman — Why Your Blender Flags Look Fake](https://www.youtube.com/watch?v=up3zVqyTIpM).[99] Independent baseline selected separately from the first five; evidence is timestamped narration. **00:47** apply rotation and scale; **01:42** reselect the pole-edge group to verify membership; **04:59** assign the pin group and enable self-collision. **05:39** sag without wind and slow evaluation are distinct; **06:04** simplify and retest; **06:35** aim the wind; **10:29** start the cache at *scene frame* −50 for pre-roll. A flag on a fixed edge is not a garment on a moving body.[99] Transfer: compare gravity-only and angled-wind runs with the same pennant; keep its pinned edge still and compare frame one with and without pre-roll.

### Original lab: one pivot change

In the locally generated `landing_pivots.blend`, blue (left) scales about its underside; orange (right) scales about its center. Both follow the same descent to frame 11. Examine the lowest mesh vertex rather than the object origin: at frame 14, both spheres have half their original height, yet only the orange sphere has a gap (0.5 Blender units). At frame 25 both touch again. The floor lies at world Z = 0. This is a transform comparison, not a physics simulation or footage from the lessons.

Set `PY` to the Python executable in a separate environment with `bpy` 4.5.9. From the skill directory, run:

```sh
OUT=$(mktemp -d) || exit 1
"$PY" -IB scripts/landing_lab.py build "$OUT/landing"
"$PY" -IB scripts/landing_lab.py verify "$OUT/landing"
```

Build refuses an existing output directory. Verify reopens the generated scene with scripts disabled, measures all 25 frames, and prints the measurements as JSON. It fails on a contact error. To render the three 384 × 240 stills for first contact, deepest squash and rest, add `--render` to the build command and use a new output directory. Those stills are not evidence for intervening frames.

### Sources

[94] https://www.youtube.com/watch?v=oB_M_RGNqFY — SamBam Studios: How to make a Landing Animation - Blender Animation Tutorial
[95] https://www.youtube.com/watch?v=zhktftWbumE — Blender Studio (presenter: Rik): Character Animation in Blender
[96] https://www.youtube.com/watch?v=1Is3oUvHwdM — Vertex Arcade: Blender 4.0 Facial Animation with NO RIGGING!
[97] https://www.youtube.com/watch?v=WuBD1Rz7VrM — Lewdineer: [Blender] Making Cloth interaction with Body Physics Tutorial
[98] https://www.youtube.com/watch?v=amUGn13gukc — Angel S: How to rip clothes in blender
[99] https://www.youtube.com/watch?v=up3zVqyTIpM — Disabled Blenderman: Why Your Blender Flags Look Fake – Fix It Now

<a name="chapter-production-transfers"></a>

## Production transfers: contact, capture and reusable assets

### A pickup that does not pop

Build the pickup exercise below, then open the generated `pickup.blend`. Play frames **1–18**. The orange token should follow the mint gripper across the gap, then stay on the right base while the empty gripper moves on. Scrub 4→5 and 11→12: neither switch should move the token. The two neighboring frames are deliberately stationary at each handover, separating a switch error from real travel.

1. For a rigid prop, add **Child Of** to the prop, targeting the carrier. Establish the offset at contact; in the UI use **Set Inverse** with other constraints on the owner inactive, before moving the target. Key the constraint's **Influence** rather than changing the object hierarchy mid-shot.[81]
2. For a hard grab, step from 0 to 1 rather than blending through half-influence. At release, first read the evaluated world pose while attached; transfer it to the prop's free transform, then switch influence to 0. Matching only the influence keys will not preserve the free pose. This fixture has no rotating parent and keys translation only; a rotated or scaled real rig needs the complete world transform converted into the correct parent space.
3. Test three independent properties: no discontinuity at either switch, constant relative offset *during* the carry, and no drift *after* release even when the carrier keeps moving. A smooth-looking still proves none of these. If the item jumps, isolate the offset and the free transform before smoothing the animation curves.

**Actual Blender 4.5.9 LTS result:** in a fresh process, all 18 frames evaluated. The token traveled 2.80 m during the carry; maximum change in its offset from the gripper was below 0.000001 m. The pickup jump, release jump and later token drift each measured 0.00 m; the freed carrier moved 1.53 m. Deleting the token's constraint caused the independent check to fail. This is a world-position test of one rigid token, not a test of finger forces or retargeted rotations. The check prints your new scene's results as JSON; add `--render` on a fresh build to create four camera frames locally.

With `PY` set to the isolated `bpy` interpreter, run from the skill directory:

```sh
OUT=$(mktemp -d) || exit 1
"$PY" -IB scripts/pickup_lab.py build "$OUT/pickup"
"$PY" -IB scripts/pickup_lab.py check "$OUT/pickup"
```

**When an add-on is justified:** Roman Volodin's Dynamic Parent automates a similar animated `Child Of` workflow. Its maintainer distinguishes current Blender 5 support from the earlier 4.x-compatible line. This lab uses the native constraint; it does not install the add-on or certify it for your version.[80][81]

**Two ways to diagnose a jump.** In Blender's short *Child Of Bone Constraint* demo, the 7.1 s frame shows the target selector; at 13.0 s both labeled bones have tilted. Inspect which object drives which before adjusting keys. Six frames were sampled; this is a visual observation, not a claim about an unshown inverse matrix.[91] In *Parenting — Blender 2.80 Fundamentals*, the presenter explains selecting the intended parent last around 1:52 and distinguishes clearing the parent from clearing it **while keeping the transform** at 6:14–6:46. The menu is visible at 6:20.[92] Use ordinary parenting for a fixed hierarchy; use keyed influence and pose matching for a handoff. Selecting the right parent cannot correct a mismatched release pose.

### Link or append? Prove who owns the next edit

* **One library, changes should propagate:** `File → Link`. If what you need to move is a linked collection, position a local collection instance. Do not promise that the linked source object itself becomes locally editable.[82]
* **One independent variant:** `File → Append` in a separate clean file. A pre-existing linked copy can change the result of an append, so test the intended starting state rather than clicking both commands in one file.[82]
* **Own checkpoint:** a one-unit shelf module was used by two clean consumers. Its source mesh was then doubled in X. After reopening both consumers, the linked shelf measured **2.0 units** and still pointed to a library; the appended shelf measured **1.0 unit** and had no library pointer. When sharing a linked project, move the project **with** its source library and reopen it. A local render is not a packaging test.

**Loading is not placing.** In Blender's *Asset Linking* lesson, the narration at 4:24–5:11 distinguishes the names available in a source file from the names requested by the receiving file. By 10:52 the script also creates a local instance; the later explanation around 14:48 separates linking data into the file from placing it in the scene.[93] If an item is listed in the data browser but absent from the camera, inspect the scene collection or instance before loading it again. A missing instance is different from a missing source file. Our shelf test above measures propagation, not every step of the film's import operator.

**Evidence boundary:** for the two longer Blender lessons, the complete publisher audio was processed into local speech-recognition notes, selected passages were checked, and six timed frames per lesson were examined. These notes are not publisher captions. No recordings, frame grabs, or transcripts are redistributed.

### Motion capture is not retargeting

FreeMoCap's project and author documentation separate first-recording checks, camera calibration, ground-plane setup and visualization in Blender. Start by confirming the capture pipeline itself works; a valid point track is not proof the target character is posed correctly.[84][85]

**Transfer exercise:** record or use a consented short clip with a planted foot, a quarter turn and a step. First check the source skeleton's up direction, scale, frame rate and rest pose. Then map the target rig. Plot or measure a foot in world space during the intended stance; compare before and after any smoothing. If the source foot stays put and only the target slides, inspect retarget scale, root translation and contact handling before filtering the capture. No real actor or camera calibration was tested for this edition.

For facial capture distinguish *registration* (consistent mesh correspondence) from *animation cleanup*. The Wrap4D release page describes 4D sequence processing; its creator's syllabus separates marker tracking, lip/eyelid contours, facial wrapping and intersection cleanup. These are publisher descriptions, **not** a reproduced commercial workflow or a watched course.[83][86] A neutral Blender exercise: make two expressions with identical topology and check the lid against the eyeball at an in-between frame. Matching vertex counts alone does not establish matching vertex order.

### Use an optional tool only when a native check is clear

| Problem | Native baseline first | What the publisher actually documents |
|---|---|---|
| Joint pinches or weights bleed across a gap | Pose the elbow at rest, halfway and near its limit. Correct a small group locally; keep rigid pieces out of smoothing. | **Smooth Weights** averages vertex-group weights. Surface vs. volume smoothing and symmetry mapping are different decisions. If nearby fingers share influence accidentally, test the neighborhood mode on one finger before a flood operation.[89] |
| A correction depends on several joint angles | Establish one corrective shape first. Test the desired pose, an intermediate pose and an unrelated pose. | Ingo Clemens distinguishes **RBF Nodes** (several driver values and output properties) from **Rapid SDK** (mapping a driving relationship). For a single hinge, the simpler relationship may suffice.[90] |
| Art direction says “put the highlight here” | Move one area light while the camera and exposure stay fixed. Compare reflection placement and shadow shape before adjusting power. | **SMagnusson's Light Painter** places lights based on indicated regions. It is a placement aid, not a material painter or proof of a physically measured source.[88] |
| Many shots or artists repeatedly redo the same work | On one test asset, write down whether the bottleneck is weights, a corrective shape or publishing. | Blender Studio lists **Easy Weights**, **Pose Shape Keys** and **Asset Pipeline** for distinct jobs. Read the individual tool and version requirements before adding a dependency.[87] |

No third-party extension is needed for the shipped exercise. A product page, a course listing and a demo reel are not interoperability or performance tests.

### Sources

[80] https://github.com/romanvolodin/dynamic_parent — Roman Volodin: Dynamic Parent — scope and version requirements
[81] https://docs.blender.org/manual/en/4.5/animation/constraints/relationship/child_of.html — Blender 4.5 LTS: Child Of Constraint
[82] https://docs.blender.org/manual/en/4.5/files/linked_libraries/link_append.html — Blender 4.5 LTS: Link & Append
[83] https://vimeo.com/429211419 — R3DS: Wrap4D release film — publisher description only
[84] https://github.com/freemocap/freemocap — FreeMoCap: original project documentation
[85] https://docs.freemocap.org — FreeMoCap: camera calibration, capture and Blender visualization
[86] https://faceform.com/wrap4d — Faceform: Wrap4D processing order and consistent topology
[87] https://studio.blender.org/pipeline/addons/overview — Blender Studio: optional add-ons by production task
[88] https://extensions.blender.org/add-ons/lightpainter — SMagnusson: Light Painter on Blender Extensions
[89] https://www.braverabbit.com/tools/smooth-weights-blender/documentation — Ingo Clemens: Smooth Weights for Blender — brush and symmetry map
[90] https://github.com/IngoClemens/blender/wiki — Ingo Clemens: tool guide — RBF Nodes and Rapid SDK
[91] https://video.blender.org/videos/watch/9b83a0d6-5a76-4e7d-8c9b-b00e0eac34ae — Blender Manual: Child Of Bone Constraint demonstration
[92] https://video.blender.org/videos/watch/9c41ef16-447e-42fe-87b7-bb24ab3b5802 — Blender: Parenting — Blender 2.80 Fundamentals
[93] https://video.blender.org/videos/watch/28799822-1788-4635-b95b-c17f58d49bb8 — Blender: Asset Linking | Scripting for Artists [12]

<a name="chapter-secondary-motion-direction"></a>

## Anime follow-through: weight without the jelly tremor

**By Noa3.** The anime panel in *Pressure & Release* is a **negative style reference for the tail**, even though it passed the contact tests. The small repeated shaking reads like literal gelatin. What to retain: local compression, support from the garment, a clear release and weight following the larger pose. What to change: concentrate the visible motion in a broad arc and let the contour become quiet. A physical pass is not an aesthetic sign-off. Do not silently re-render the old shot or make its damping values a default.

### Read the silhouette before tuning springs

Lock the camera, mute secondary motion and play the primary gesture. Mark when the support stops, then compare the free contour with a seam attached to the torso. Repeat with one broad return enabled. If the silhouette already settles at playback speed, leave the smaller controls muted. This is a proposed comparison on your own rig, not a measurement of someone else's animation.

### Build the motion in three passes

1. **Primary action:** block only the rib cage, support and contact driver. Mark entry, maximum load, first free frame and where the body itself becomes still. On a moving torso, place one tracking mark on a stable body landmark and one on the moving contour. Their *difference* is the secondary motion; a world-space trace mixes it with the whole gesture.
2. **Broad return:** begin with one low-frequency control across a coherent mass, a firmly supported attachment and less motion near the strap/anchor. Sculpt the pressed shape and one broad return with shape keys, or use a low-resolution cage. If using Blender Soft Body, goal weights control attachment to the desired positions and edge settings provide stiffness and damping; do not paste numbers from a custom solver into those controls.[374][375] Start with one readable follow-through and a clean settle. Add a smaller return only if it improves the pose at normal speed. A second oscillation is not an obligation.
3. **Local contact and final hold:** let the contact point indent locally while the wider region lags. Remove residual high-frequency animation *after* release; do not low-pass a baked surface through a moving collider. If the solver chatters only during contact, inspect collision thickness, coarse faces and substeps instead of increasing global damping until the whole performance goes dead. Recheck the [actual garment surface and any raised trim](figure-workflows.md#chapter-adult-figure-staging).

**Accept or reject it at the delivery camera:** compare rigid, broad-only and broad-plus-detail on the same stroke. Watch once at speed and without graphs: can you see weight transfer, and do you stop noticing the mechanism? Then inspect the torso-relative curve from the first free peak to rest. Count visible reversals above a stated screen-space noise floor and measure how long the silhouette keeps reversing; do not maximize overshoot as a score. Use a matte/clay pass and stable lighting to distinguish a shaking outline from sparkling highlights. In the final hold, a quiet drawing beats a technically active solver. A pleasing amount of overshoot in one framing is not a universal millimetre limit.

### Sources

[374] https://docs.blender.org/manual/en/4.5/physics/soft_body/settings/edges.html — Edges - Blender 4.5 LTS Manual
[375] https://docs.blender.org/manual/en/4.5/physics/soft_body/settings/goal.html — Goal - Blender 4.5 LTS Manual

<a name="chapter-cloth-cache-handoff"></a>

## A cloth file that still works on another machine

**Author: Noa3. Tested in Blender 4.5.9 LTS.** A `.blend` can open normally even when the intended simulated pose is missing. Test what the recipient will do: **open the delivery and jump straight to a late frame**. Playing forward from frame 1 first may quietly compute a replacement and hide a broken delivery.

### Decide what you are delivering

- **Editable setup:** include the starting geometry, pins, collisions, frame rate and solver settings. Tell the recipient to recompute; don't promise a specific cached performance.
- **Approved cloth motion:** include the actual bake. In the 4.5 point-cache workflow the default baked cache can be stored in the saved `.blend`; with **Disk Cache** enabled it is written next to the saved file under `blendcache_[filename]`. The separate **External** option uses an explicitly selected path; the cache name and index have to match. These are distinct workflows.[323]
- **Final images only:** deliver the approved image sequence. This preserves appearance, not editable fabric motion. Pack Resources is useful for eligible external assets; it is not a substitute for copying and testing a disk-cache directory.[324][323]

### Make a portable disk-cache delivery

1. Work in a copy with its intended final `.blend` filename. In **Physics Properties → Cloth → Cache**, set the shot's start and end, enable **Disk Cache** and bake. Save again. For this kind of bake, keep preview and render subdivision consistent on geometry feeding the solver. Changing the cloth mesh, its position or the cache range requires revisiting the bake; don't clear a working approved version in place.[19][323]
2. Archive the `.blend` **and its sibling cache folder** together. Record the Blender version, solver, frame range, pinned object/group and expected cache filenames. Keep the pair named consistently. Mark whether colliders, textures or linked libraries are required as separate resources. A successful ZIP integrity check proves readable bytes, not a usable pose.
3. Extract into a different directory. Make the authoring files unavailable. Start a fresh Blender process with scripts disabled. Seek directly to a late frame, back to an early one, then a middle one. Compare with known-good poses rather than a generic “Bake” indicator. Inspect the held seam as well as the free end. Try a second copy without the cache; the check should fail for the expected reason.
4. If the result changes, check the sibling folder name, frame coverage and bake version **before** altering pins, gravity or animation. A stale cache can exist and still belong to another edit. For delivery of a large shot, hash the approved cache members and store the versioned manifest alongside the archive. Do not generalize the point-cache directory naming to fluids, Geometry Nodes, or external Alembic/USD caches without testing their own formats.

### Worked example: the same native file, with and without its cache

In the original handoff test, the same saved cloth opened with and without its disk cache. The pose hung from its rail at frame 16 and projected nearly horizontally at frame 1. The native case study is not bundled; the procedure above applies to a cloth scene you bake yourself.

In Blender 4.5.9 the transferred disk bake reproduced the sequential reference at frames **16 → 4 → 12 → 8 → 1**, checking **all 77 vertices** each time (acceptance tolerance 0.1 mm). The free tip dropped 0.933 m and the chosen pin did not move. Removing just the sibling folder from a second copy of the **same baked `.blend`** gave a largest vertex error of **1.143 m** at the first seek, even though opening the scene succeeded. The earlier `technical.blend` could cold-seek without sidecars; it already contained frame data and was not evidence that *disk* caches travel inside a `.blend`.

Capture evaluated vertex positions from the approved run, then compare them with the relocated copy. A checker should not bake a replacement first. Use a missing-cache control to prove the check observes cached motion rather than successful file opening alone.

### Sources

[19] https://docs.blender.org/manual/en/4.5/physics/cloth/settings/cache.html — Cache - Blender 4.5 LTS Manual
[323] https://docs.blender.org/manual/en/4.5/physics/baking.html — Baking Physics Simulations - Blender 4.5 LTS Manual
[324] https://docs.blender.org/manual/en/4.5/files/blend/packed_data.html — Packed Data - Blender 4.5 LTS Manual
