# Morphs, surface motion and research tests

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [MakeHuman: move the ankle without repainting the foot](#chapter-makehuman-morphs)
- [Three changes of volume: what moves, and what stays put](#chapter-volume-deformations)
- [Turn a figure reference into a test](#chapter-creator-techniques)

<a name="chapter-makehuman-morphs"></a>

## MakeHuman: move the ankle without repainting the foot

**Noa3 · workshop text and measurements.** This case uses classic MakeHuman, commit `a8bc2d54ff0ac92e78ff71431b1023eda42bf482`. The modelling plugin and hm08 seed come from that revision[457][344]. The default skeleton and its skin weights come from the same checkout[345][346]. No community asset pack is needed.

### Start with one control and one vertex

In **Modelling → Arms and Legs → left foot**, use **Move horizontally**, not **Scale foot**. In the front view watch the ankle relative to the shin, not the apparent size of the shoe. The title hides an important distinction: this slider edits the *rest shape*. It does not translate the foot bone in a pose. [458] [459]

The modelling plugin loads `modeling_modifiers.json` (what the control does) and `modeling_sliders.json` (where to display it)[457]. The UI resolves `armslegs/l-foot-trans-in|out` by name, creates a `ModifierSlider`, and previews changes with `modifier.updateValue`[460][461]. The slider label and modifier definition connect **Move horizontally** to the `in` and `out` endpoints of `l-foot-trans`[458][462].

For this two-ended `UniversalModifier`, the native control value `s` runs from −1 to +1; zero, **not** 0.5, is neutral. The coefficient of the inward file is `max(-s,0)`; that of the outward file is `max(s,0)`. Other definitions can have a center target with coefficient `1-abs(s)`, or only a positive endpoint. The modifier associates each target path with a list of factors; `getTargetWeights` multiplies them and `setDetail` records the resulting coefficient for that file. [463]

A text `.target` row is **zero-based seed vertex ID, signed ΔX, ΔY, ΔZ**, not an absolute point or four skin weights. The loader reads an integer and three floats; the ordinary unposed application adds `coefficient × delta` to each listed coordinate. Omitted IDs do not move *from this target*. Compiled target vectors read from the archive are decoded with `× 0.001`; do **not** apply that scale again to text files. On a full rebuild `applyAllTargets` resets the seed, then applies the nonzero detail stack. For vertex `i`: `rest[i] = seed[i] + sum(c[t] * delta[t,i])`. [464] [459]

**Measured on the text assets.** The seed has 19,158 `v` records including helpers. At ID **11416** the seed is `(2.4532, -6.8682, 0.0433)`. The horizontal sweep below isolates just this modifier; it is not a prediction of the complete default UI character. Y and Z remain unchanged in every row. [344] [465] [466]

| Native value | In coefficient | Out coefficient | Vertex ΔX (dm) | Vertex rest X (dm) | `foot.L` rest head X (dm) |
|---:|---:|---:|---:|---:|---:|
| −1 | 1 | 0 | −0.311 | 2.1422 | 1.8732 |
| 0 | 0 | 0 | 0 | 2.4532 | 2.1962 |
| 0.5 | 0 | 0.5 | +0.170 | 2.6232 | 2.3662 |
| 1 | 0 | 1 | +0.340 | 2.7932 | 2.5362 |

The positive endpoint is **3.4 cm** at this point. Positive X is outward on the character’s **left** foot; Y is height (`getHeightCm` uses ten times the Y extent); the left-foot *forward* target adds `(0,0,+0.396)` here, so Z is depth, positive forward[459][467]. Native lengths are decimeters; the exporter uses scales `1` for dm, `0.1` for m and `10` for cm[468]. Record both export and import conversion before comparing a Blender measurement. OBJ face references count from one, but the `v` records are appended in file order[469]. `11416` means the **11,417th vertex record**, not the 11,417th text line or OBJ face index 11416. Keep a seed copy with original order, helpers and topology; a visually identical welded or sorted copy is not a valid target basis.

### Macro sliders mix authored examples, not bones

On **Modelling → Main**, `Gender`, `Age`, `Muscle`, `Weight`, `Height` and `Proportions` are separate controls. The native macro names refer to a finite library of shapes; the slider is continuous. For instance `Gender=g` assigns `female=1-g`, `male=g`. Weight and muscle each use three factors: at 0 only `min` is 1, at 0.5 only `average` is 1, at 1 only `max` is 1; between adjacent knots the two factors crossfade. These are morph coefficients, not kilograms or muscle activations. Age has named knots baby 0, child approximately 0.1875, young 0.5, old 1 (the implementation uses rounded `5.333` on its first segment). The legacy `race` factors named `caucasian`, `asian`, `african` are normalized asset-library slots, not a biological classification or a guide to individual anatomy. [458] [470] [459]

A macro modifier sets the human property and reevaluates its group; the target-discovery code extracts recognized factor names from paths. Only the factors named for a given target enter its product. Do not multiply every target by every slider, and do not assume the contributions of *unrelated* local controls must sum to one. [463] [470]

**Mixed example at vertex 0.** Set `Gender=.25`, `Age=.75`, and the `caucasian` slot to 1 for this diagnostic. The two gender factors are .75 and .25; young and old are each .5. Read the two young endpoint vectors from their respective files[471][472]. The other two vectors come from the old endpoints[473][474]. Each table row is the actual signed vertex-0 displacement in dm **before** weighting.

| `macrodetails/caucasian-…` filename suffix | Product | ΔX | ΔY | ΔZ |
|---|---:|---:|---:|---:|
| `female-young.target` | .375 | .026 | −.500 | −.131 |
| `male-young.target` | .125 | .012 | +.904 | +.062 |
| `female-old.target` | .375 | .032 | −.651 | +.212 |
| `male-old.target` | .125 | .013 | +.517 | −.027 |

The sum of those four **weighted vectors** is `(+.024875, −.254, +.03475)`; adding it to seed vertex 0 gives `(-.324325, 7.0759, 1.44235)`. That is the contribution of this group on the seed, **not** a full-human evaluation including the universal, height, proportion or local detail groups. [344] [463]

### Why the joint moves but its skin weights do not

`default.mhskel` makes `foot.L` a child of `lowerleg02.L`; its head is the joint `foot.L____head`, mapped to IDs **13830–13837**[345]. The probe compared that set with every face reference of `joint-l-ankle` in the seed, after conversion to zero-based IDs: the sets match[344]. The rig computes the mean rest position of the mapped vertices (fallback: a named basemesh group), updates endpoints and rebuilds rest matrices[475]. After applying targets, MakeHuman updates stored rest coordinates and the base skeleton before restoring the pose[459]. At full outward displacement those eight helpers all move +0.34 dm in X, explaining the last column without a change to any bone weight[466].

Now inspect **the same skin vertex 11416** in `default_weights.mhw`. Under three different bone names are `[vertex ID, scalar]` entries: `foot.L=.125`, `lowerleg01.L=.162`, `lowerleg02.L=.713` (sum 1). The numbers say how to combine the bones’ pose transforms acting on the assembled rest point. They are *not* `(ΔX,ΔY,ΔZ)` and they stay the same for this sweep. The weights loader normalizes per vertex, merges duplicate assignments and handles unweighted vertices; do not assume every raw file row is a final runtime weight. `Skeleton.skinMesh` implements linear blend skinning. If the neutral outline is wrong, inspect the target stack; if neutral is right but a bend collapses, check the rest hinge and weights before changing the neutral silhouette. [346] [476] [475]

A fitted garment has a **third** kind of weight. A proxy point is reconstructed from up to three referenced human vertices: the weighted sum of their rest positions plus a transformed offset. This follows proportions; it is not cloth simulation or a guarantee of clearance in a bend. To follow the pose the proxy also needs **bone** weights, transferred through its mapping or supplied by the proxy itself. Do not paint the three fitting coefficients as bone weights. [477]

### Workshop pass: correct the right layer

1. **Block the figure in rest pose.** Set Main height and proportions first; compare head-to-body and hip-to-floor landmarks in front and side views. Use Torso depth and Hip waist position before local stomach tone. Change one group at a time and save the slider values, not just a screenshot. Check head width *and* depth in Face rather than flattening a profile to fix a front view. These controls are in the shipped slider definitions. [458]
2. **Fit limb landmarks.** Compare left/right shoulder caps, elbow, wrist and ankle from both views. Use Arms and Legs → shoulder muscle mass, arm thickness or foot position only for the corresponding landmark. For a foot stance change, test neutral and each endpoint, then check the ankle helper centroid. Do not move the shoe alone to hide a pivot that stayed behind. [458] [345] [466]
3. **Sculpt a residual, not the complete figure twice.** If the lateral ankle contour still needs correction at a particular macro mix, duplicate that *assembled, unposed* seed at unchanged indexing. Sculpt only the contour on one copy. Subtract its untouched assembled twin vertex by vertex in native coordinates; store nonzero differences as a separate sparse correction. Subtracting the canonical seed instead would include the already-active macro displacement a second time. Keep the helper untouched for a skin-only correction; if the intended pivot must move, edit/check its helper set separately. At correction 0 the input must be recovered; at 1 the same mixed state must reproduce the sculpt. Test another macro mix: if the correction damages it, restrict the correction to the intended mix rather than baking it into the neutral base. This is a suggested authoring test, not a claim that a pose driver was installed. [464] [459] [475]
4. **Test in this order: naked rest → naked bend → clothed rest → clothed bend.** A correct naked rest with a bad naked bend points toward pivot, weights or a pose-specific corrective. A correct naked bend with a bad shoe suggests the shoe mapping, its offsets, weights or insufficient clearance. Check both inside and outside the ankle; a front silhouette can conceal penetration. [475] [477]

**A failed shortcut, with numbers.** Negating the outward file predicts inward ΔX `−.340` at 11416. The authored inward file gives **−.311**, and the supports even differ: **1,695** inward IDs versus **2,038** outward. Use both files. A second check catches index drift: ID **11235** has outward ΔX `.001`; looking up 11234 instead yields no row, i.e. zero. An earlier trial at 11416 could *not* detect this off-by-one error: its neighbor has the same `.340` displacement. Test at a changing edge as well as a plateau. [465] [466]

**Export checkpoint.** Keep the source slider values, original seed and corrective as the editable master. Classic OBJ writes meshes at the configured scale and normally filters masked faces and unused vertices[478][469][468]. Do not expect a skeleton, editable sliders, helper geometry, or original vertex IDs from that surface export. Classic FBX can copy/scale a selected skeleton and transfer bone weights to proxy, masked or subdivided meshes; its exporter has an explicit TODO for attaching shapes[479]. A skinned export does not prove the authoring target library travelled with it. Reimport with the intended unit/axis settings; compare neutral height, ankle pivot, bend and shoe clearance. This chapter inspected exporter code, not a live exporter round trip.

**Scope of the numerical test.** The original probe checked helper membership and sparse supports against pinned source data, then ran negative controls. The recorded values above describe that reconstruction, not an interactive MakeHuman session, a posed rig or a garment collision test. Neither the probe nor the upstream data is bundled.

**Credits and license boundary.** Workshop and probe: Noa3. Classic MakeHuman’s program logic is AGPL-3.0-or-later; the inspected modules credit Marc Flerackers, Glynn Clements, Joel Palmius, Jonas Hauquier and Thomas Larsson among their authors[463][475]. The project's bundled graphical assets are CC0 1.0[480]. The target headers name Manuel Bastioni and record transfer to Data Collection AB, Joel Palmius and Jonas Hauquier; the weight data has its own credit header[466][346]. Check each third-party garment separately. No upstream mesh, target or skin-weight file is bundled here.

### Sources

[344] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/3dobjs/base.obj — MakeHuman CC0 data · 3dobjs/base.obj
[345] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/rigs/default.mhskel — MakeHuman CC0 data · rigs/default.mhskel
[346] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/rigs/default_weights.mhw — MakeHuman CC0 data · rigs/default_weights.mhw
[457] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/plugins/0_modeling_0_modifiers.py — MakeHuman — 0_modeling_0_modifiers.py
[458] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/modifiers/modeling_sliders.json — MakeHuman — modeling_sliders.json
[459] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/apps/human.py — MakeHuman — human.py
[460] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/apps/gui/guimodifier.py — MakeHuman — guimodifier.py
[461] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/lib/modifierslider.py — MakeHuman — modifierslider.py
[462] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/modifiers/modeling_modifiers.json — MakeHuman — modeling_modifiers.json
[463] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/apps/humanmodifier.py — MakeHuman — humanmodifier.py
[464] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/core/algos3d.py — MakeHuman — algos3d.py
[465] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/targets/armslegs/l-foot-trans-in.target — MakeHuman — l-foot-trans-in.target
[466] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/targets/armslegs/l-foot-trans-out.target — MakeHuman — l-foot-trans-out.target
[467] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/targets/armslegs/l-foot-trans-forward.target — MakeHuman — l-foot-trans-forward.target
[468] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/apps/gui/guiexport.py — MakeHuman — guiexport.py
[469] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/shared/wavefront.py — MakeHuman — wavefront.py
[470] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/lib/targets.py — MakeHuman — targets.py
[471] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/targets/macrodetails/caucasian-female-young.target — MakeHuman — caucasian-female-young.target
[472] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/targets/macrodetails/caucasian-male-young.target — MakeHuman — caucasian-male-young.target
[473] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/targets/macrodetails/caucasian-female-old.target — MakeHuman — caucasian-female-old.target
[474] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/targets/macrodetails/caucasian-male-old.target — MakeHuman — caucasian-male-old.target
[475] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/shared/skeleton.py — MakeHuman — skeleton.py
[476] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/shared/animation.py — MakeHuman — animation.py
[477] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/shared/proxy.py — MakeHuman — proxy.py
[478] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/plugins/9_export_obj/mh2obj.py — MakeHuman — mh2obj.py
[479] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/plugins/9_export_fbx/mh2fbx.py — MakeHuman — mh2fbx.py
[480] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/LICENSE.md — MakeHuman — LICENSE.md

<a name="chapter-volume-deformations"></a>

## Three changes of volume: what moves, and what stays put

**Noa3 · Adult figure and comparative animal art · Not medical advice.** Start with two drawings in exactly the same pose. If the change of state cannot be distinguished from leaning, breathing or camera perspective, adding a spring will not explain it. All control names, displacement fields and acceptance gates below are workshop choices, not anatomical measurements.

### After a meal: the shirt is often the better indicator

**Evidence and timing.** In healthy controls given a liquid test meal, the diaphragm relaxed and the upper abdominal wall showed compensatory muscle activity; the lower anterior muscles did not show the same change. This is not evidence for a round lower-belly bulge. [449] In a separate drink study, an *internal stomach cross-section* peaked at five minutes and decreased toward thirty minutes. That is neither the time to digest a dinner nor a curve for the outer skin. [450] For a quiet scene, it is perfectly reasonable to leave the body silhouette unchanged. Let a previously loose fold just touch the abdomen when the character sits back.

**Make the comparison.** In a neutral standing mesh mark the lower rib margin, umbilicus and front points of the pelvis. Keep transverse quad rows across the front wall, continuing around both flanks; avoid a fan of edges at the navel. Make a `Meal` key on the unclothed base. Move a broad patch between the lower rib margin and navel slightly forward, blending laterally into both flanks over several loops. Reduce the weight to zero over the ribs, back and bony pelvis; let the navel follow its local skin, not become a pinned dimple. Start with the smallest displacement visible in the side overlay. Do not trace the stomach as an external organ-shaped mound.

**Layer and reject.** Keys: baseline → barely fuller → quiet after-meal hold; use an edit or elapsed-time cue for the later return. Sit the same mesh with `Meal=0` first; correct the hip crease and rib–pelvis compression *in that pose*, then reapply `Meal`. Key breath separately and compare at the same respiratory phase. No new vein map, redness or glossy center. Bind a shirt proxy to the changed surface, pin shoulders and side seams, and let the front lose clearance before it stretches. Check a fixed profile and a waist-height three-quarter, standing and seated. Toggle a bad uniform torso scale: if your intended version moves the spine or waistband just as far, narrow the mask. In anime, a softer shirt fold and one held contour beat repeated expansion on every bite.

### Lactation: separate milk-related fullness from tissue swelling

**Evidence and timing.** Milk coming in can bring fullness, warmth and tenderness; engorgement may interfere with feeding and commonly settles over days, not within a single gesture. [451] Early postpartum engorgement commonly begins about three to five days after delivery, often affects both breasts and can feel firm or painful. Increased blood and lymph contribute to swelling; milk volume alone does not explain it. [452] Ordinary fullness need not progress to engorgement. For a neutral clinical illustration, show a clothed adult in the same chair before and after an elapsed-time cut. Do not use a dramatic colour change to imply a diagnosis.

**Build two state keys, not one scale.** Trace the chest-wall footprint, sternum and inframammary fold. Run concentric *bands* across each breast into the chest mesh, allowing extra rows at the lower fold and lateral transition; avoid a star pole on the projecting surface. On `Full_L/R`, distribute a modest outward displacement broadly across the mobile tissue. Keep the sternum, clavicle and ribs still; grade the mask down at the root, keep the fold attached, allow the lower contour above it to round. On `Swollen_L/R`, broaden and smooth the surface between landmarks instead of translating the apex forward again. Check both sides together but retain pre-existing asymmetry. Sculpt the second key relative to a measured full-state drawing, or attenuate the first as the second enters; adding two maximum sculpts blindly doubles the change. A less-full state after a feed is not an instantly emptied sac; leave residual swelling in an engorgement sequence.

**Pose, shader, cloth.** First compare rest/full with arms down; then raise one arm to reach for a folded towel. Correct underarm pull and support for that pose without changing `Full`. Use a plain supportive top: hold band and strap attachments, spread contact over the cup, check cup edge, fold and side seam for penetration. A fitted top redistributes the silhouette; it is not a second skin scaled outward. In the uncovered anatomical study only, an optional low-contrast vein tint should follow an existing UV map; no pulsing cords, emissive veins, painted wetness or automatic red patches. Use the same soft light, eye-level three-quarter and profile; frame from shoulders through waist. Negative: mute both state keys but keep the reach, then mute the reach but keep both states. Reject a moving sternum, sliding fold or identical spherical scaling. For anime, use one supported broad lag if the torso stops abruptly, then hold. Compare matte contour against the band: reject repeated post-stop reversals visible at delivery size.

**What was actually tested on a torso.** A synthetic garment-follow test (historical tool, not included) uses separate abdominal and unilateral chest shape keys. On a 1,365-vertex front patch the closest sampled garment vertex remained **1.982 mm outside** the body over nine zero, isolated and mixed states with Surface Deform bound. Muting the binding instead put the worst sampled vertex **9.903 mm inside**. The pelvis and opposite side stayed still at the test tolerance. This is evidence for the attachment and masks, not an anatomical displacement prescription or proof that a whole garment has no intersecting faces. Run in a fresh bpy-enabled process with a new JSON filename, then pass that file to the garment checker (historical tool, not included).

### African egg-eater: two journeys, only one egg-shaped silhouette

**Observed sequence.** Model a *Dasypeltis* feeding event, not a generic snake swallowing a ball. Gape in *D. gansi* involves substantial stretch between the lower jaws; allow the jaw tips to spread with tissue between them, not a jaw dislocating from the skull. [453] The intact egg passes into the anterior oesophagus. Gans describes local neck contraction squeezing the held egg and crushing the already cracked shell. [454] Contents go on toward the stomach; the empty shell is regurgitated. [455] This is not a universal template: in a field report a captured Burmese python regurgitated **intact** guineafowl eggs during transport, a different observation from a specialist routinely discarding an empty shell. [456] Preserve order, not an invented stopwatch: a stage hold or cut is editorial compression, not measured feeding time.

**Build the mechanism.** Give the neck continuous cross-section rings, more closely spaced than the narrowest squeeze. Run longitudinal edges through the mouth corners and across a flexible chin patch between separately controlled jaw halves. Keep skull roof and eyes anchored. Mark headward and tailward ends on the *anterior segment*, not the full animal. Give each section a rest-length coordinate `s`; record `s` on the mesh before bending. Move a bounded egg envelope along `s`, expanding the local cross-section rather than scaling world X/Y. Fade it to zero on both shoulders of the bulge; add a separate, shallower pinch on the mouthward side as the egg advances. Bias the production sculpt ventrally so the dorsal line does not inflate like a hose. Anchor the remote body. Use extra rings or a broader mask if the pinch is a single hard crease.

**Block distinct states.** (1) Contact and gradual gape around an external rigid egg. (2) Transfer the envelope from mouth to anterior neck; check that no second egg appears at the handoff. (3) Park travel, pose a local neck bend/contraction around the held egg, then reduce its cross-section as the shell collapses. (4) Show a much smaller folded empty-shell envelope returning mouthward; only the contents continue inward. (5) Expel the folded shell, close gape and restore the quiet neck. Keep locomotion, gape, cargo position and collapse as separate controls. A traveling pinch is a legibility aid, not a simulation of individual muscles. Pose the neck in a shallow curve and then straighten it with travel parked: the crest must stay at its body mark. Check lateral and overhead views against a still ground mark. Use UV-bound scale rows with more interscale skin showing under stretch; no cloth, moving vein stripe or wet specular pulse to tell the story. Negative: replace the envelope with whole-body dilation or send the intact bulge to the tail. Reject either even if the shot reads as a swallow. For a drawn look, hold a single clean neck curve after release instead of adding ripples.

**Executed geometric check.** The original neck probe built an open curved segment, wrote a shape key and measured four cargo positions. Ring spacing was 0.025 arbitrary units; resting radius was 0.10. At target arc length 2.39 the measured crest was at 2.400 (radius 0.179877); the mouthward pinch was at 1.825 (radius 0.080048). The other three stations also met the one-ring positional tolerance. End-ring radius drift rounded to zero; deliberate uniform dilation drifted **0.08**, failing the 0.00001 gate despite reaching the desired peak radius. Muting the field restored radius 0.10 throughout. The check demonstrates local placement and reset on one fixed arc, not jaw kinematics, shell fracture, a moving rig, rendered appearance or animal timing.

### Sources

[449] https://pubmed.ncbi.nlm.nih.gov/23645627 — Mechanisms of postprandial abdominal bloating and distension in functional dyspepsia
[450] https://pubmed.ncbi.nlm.nih.gov/29119636 — Gastric accommodation in healthy subjects studied by ultrasound, manometry, and impedancemetry
[451] https://www.healthiertogether.nhs.uk/new-parent-and-baby/overcoming-breastfeeding-problems — Overcoming Breastfeeding problems
[452] https://my.clevelandclinic.org/health/diseases/breast-engorgement — Breast Engorgement: Causes, Complications & Treatment
[453] https://doi.org/10.1111/jzo.13102 — Scaling relationships of maximal gape and prey size of snakes for an egg-eating specialist (Dasypeltis gansi) and a dietary generalist (Pantherophis obsoletus)
[454] https://doi.org/10.5962/p.203469 — The Functional Morphology of the Egg-eating Adaptations in the Snake Genus Dasypeltis
[455] https://pubmed.ncbi.nlm.nih.gov/23454629 — The effects of body temperature and mass on the postprandial metabolic responses of the African egg-eating snakes Dasypeltis scabra and Dasypeltis inornata.
[456] https://journals.ku.edu/reptilesandamphibians/article/download/13848/12809/28635 — Consumption of Bird Eggs by Invasive Burmese Pythons in Florida

<a name="chapter-creator-techniques"></a>

## Turn a figure reference into a test

**By Noa3.** Pick one visible change and ask what else could cause it. A dark line moving across an arm might be pigment, a ridge casting a shadow, or a reflection. A finished image cannot tell you which node, weight or solver produced it. The checks here are workshop exercises on assets you own; they do not reconstruct anyone else's scene.

| If the problem is… | Set up this comparison | What would change your diagnosis? |
|---|---|---|
| A vein or printed pattern swims in a pose | Paint one stripe across a moving skin patch. Give the colour and bump branches separate switches and render the same pose under two light directions. | A line that stays at the same UV but flips light and dark is a shading cue. A stripe sliding past the same vertex indicates a coordinate or attachment problem. See [hair and skin in motion](character-surfaces.md#chapter-hair-and-skin). |
| A hair part opens when the head turns | Give each side of the part a flat debug colour. Scrub a head turn, then a forehead shape change. Track roots against the scalp, not against the screen. | If roots drift, fix the surface attachment before adding strands. If the roots stay put but scalp shows through, adjust guide coverage and inspect the result under rim light.[484][487] |
| A fitted shirt clips only when the arm is up | Test neutral, arm raised, body shape alone and both together. Inspect the armpit and neckline. Mute the surface binding for a control.[348] | Wrong-side motion before the shape change points to weights. A fault confined to the combined pose calls for a local correction. Let loose sleeves move independently; a fitted transfer is not a cloth simulation. |
| A moving bulge looks like the whole body inflating | Keep the camera and two end landmarks fixed. Compare the cross-sections ahead of, at and behind the largest outline. | A travelling peak leaves the rear section near rest. A slow change in resting fullness is a different test. See [deformation by cause](deformation.md#chapter-volume-deformations). |
| An expression breaks with a costume or second expression | Test blink, smile and outfit separately, then together. Compare the same close camera view each time. | If both solo expressions pass, correct the combination rather than weakening each solo. For an exported avatar check the receiving platform's performance rank as well as its appearance.[516] |
| An effect looks right in a still but flickers in motion | Render the halftone or pore mask without lighting at delivery size. Move the asset with the camera fixed, then move only the camera. | Reduce the pattern frequency or improve filtering if small dots flicker. If the pattern consistently slides in one direction, inspect its coordinate space instead. |
| A lamp or bright hair rim looks pasted onto the shot | Render the emitter face alone, illumination alone, then both. Keep a neutral card in frame and disable bloom for the comparison. | A bright face without nearby spill is visible emission, not proof that the set is lit. If a grade loses the hairline, compare the ungraded plate before changing the groom. |
| A pose looks right in the creator tool but wrong after export | Take one reference pose and one extreme pose through the actual receiving application. Inspect the heel, hair roots, UV set, silhouette and outfit layers at the intended distance. | A sliding planted foot suggests rest-pose or limb-scale mismatch. A missing lace edge or lock at distance suggests transparency, coverage or LOD. Do not change both rig and shader in the same test. |

For an edit that seems to create a second contour, compare a hard cut and a short dissolve made from the same two frames. If only the dissolve doubles the contour, the mesh does not need a corrective. To judge a loop, compare the last exported frame to the first **in motion**: matching poses alone do not match velocity. For look development, compare a clay silhouette, an unlit colour pass and the lit frame from the same camera before committing to a topology change.

**Evidence boundary.** The earlier survey contained 5,351 distinct listing entries across 112 unfiltered pages. The separate filtered view added no new entries. The historical audit tallied overlapping subject counts; 2,915 titles did not establish a subject under the original tagging rules. No project file from those listings was inspected. A count is not evidence for a technique or permission to use an asset. The [anatomy](figure-workflows.md#chapter-human-anatomy), [MakeHuman target](deformation.md#chapter-makehuman-morphs) and [secondary-motion](motion.md#chapter-secondary-motion-direction) chapters offer independent starting points.

### Sources

[348] https://docs.blender.org/manual/en/4.5/modeling/modifiers/deform/surface_deform.html — Surface Deform Modifier - Blender 4.5 LTS Manual
[484] https://docs.blender.org/manual/en/4.5/modeling/geometry_nodes/hair/utility/attach_hair_curves_to_surface.html — Attach Hair Curves to Surface - Blender 4.5 LTS Manual
[487] https://docs.blender.org/manual/en/4.5/modeling/geometry_nodes/curve/operations/deform_curves_on_surface.html — Deform Curves on Surface Node
[516] https://creators.vrchat.com/avatars/avatar-performance-ranking-system — Performance Ranks | VRChat Creation
