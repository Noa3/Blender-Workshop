# Creator notebook — part 3

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [@cgboost — source notes](#chapter-creator-cgboost)
- [@CGI_Secrets — source notes](#chapter-creator-cgi-secrets)
- [@christopher3d475 — source notes](#chapter-creator-christopher3d475)
- [@CRNTDESIGNERS — source notes](#chapter-creator-crntdesigners)
- [@DemNikoArt — source notes](#chapter-creator-demnikoart)

<a name="chapter-creator-cgboost"></a>

## @cgboost — source notes

169 public Videos entries; 235 Shorts; 8 individually noted.

[All creators and coverage](channel-register.md) · [Apply a lesson to the tram](channel-workshop.md). Evidence and proposed exercises are distinguished below.

#### How to Light Almost Anything in Blender #b3d

Video · Description / chapters.[184]

**Evidence:** Public creator description, not playback. Creator-written chapters read on public watch page; chapter starts are signposts, not frame times. **Locator:** chapter starts 00:22 lighting arrangement, 00:47 practical example, 04:43 additional tips

**Observed:** The creator describes this as a three-point lighting demonstration and distinguishes its explanation from the practical setup. No placement angles, ratios or power values were verified.[184]

**Try:** Separate key, fill and rim on a metal tram nose. Keep each contribution switchable before committing to a night look.

**Check:** With each light soloed, verify that the key describes shape, fill preserves a shadow side, and the rim does not trace every edge equally.

#### Hard-Surface Modeling in Blender for Beginners (Full Course) #b3d

Video · Sampled frames.[246]

**Evidence:** Visually inspected timestamped YouTube player storyboard samples, not continuous playback. Creator-written chapters read on public watch page; chapter starts are signposts, not frame times. **Locator:** chapter starts 02:37 blockout, 11:52 bevels, 15:49 cuts, 57:29 materials, 1:04:40 rig prep, 1:32:20 primary motion, 1:41:32 secondary motion, 2:01:58 lights; frames 12:40, 50:20, 1:03:00, 1:53:20, 2:05:55

**Observed:** The instructor keeps the green robot concept beside a gray primitive assembly at 12:40; by 50:20 a circular side part has radial topology and a distinct center. At 1:03:00 colored parts appear alongside material swatches. Later the animation curves and then a rendered preview beside the stage are visible. Course structure separates mesh prep, rigging and two passes of motion.[246]

**Try:** Use the course as staged gates for a station service cart: silhouette against a sketch, bevels/cuts, material separation, rigid part prep, primary travel, then secondary antenna movement and shot lighting.

**Check:** Compare silhouette from final camera before cutting details. Pose each moving part without shading or lighting tricks before adding secondary movement; switch secondary motion off and verify the main action still reads.

#### 8 Mistakes to Avoid when Animating Cameras #b3d

Video · Narration.[162]

**Evidence:** Narration; no exact click or chapter time used.

**Observed:** CG Boost compares abrupt stops with a weighted camera, and points out that a calm walking move paired with running-strength shake is internally inconsistent.[162]

**Try:** Lock the intended speed and easing before adding handheld drift. Judge the whole approach to the platform, not a single pose.

**Check:** Watch once at playback speed with shake disabled and once enabled. A sudden brake or walking shot that feels like running needs a timing change, not more shake.

#### Change Your Lighting Without Re-Rendering | Blender Light Groups Tutorial #b3d

Video · Narration.[154]

**Evidence:** Narration and creator chapters; the following times are chapter starts. **Locator:** 02:23 assignment; 05:16 compositor use

**Observed:** CG Boost separates the contributions of lights before compositing so a source can be adjusted after rendering. A group follows the light it emits, not the objects it illuminates.[154]

**Try:** In Cycles assign the car lights, station lamps and harbour world to separate groups. Multiply each color contribution, then add them in linear light before glare.

**Check:** At unit gains the sum must match the raw beauty. Muting the station group must also remove its reflected light on the car or paving.

#### Blender Light Linking #b3d

Short · Sampled frames.[205]

**Evidence:** Visually inspected timestamped YouTube player storyboard samples, not continuous playback. **Locator:** 00:07; 00:29; 00:43; 00:57; 01:19

**Observed:** The Short repeatedly compares the blue vehicle render with the editing viewport and properties. The roof and blue body carry bright accents against a separately readable ground. Linking UI labels and individual receiver assignments are too small to verify.[205]

**Try:** In a wet tram shot, test a vehicle-only accent as a separate artistic decision, not an excuse to increase every lamp.

**Check:** A/B the accent off/on: check body silhouette and nearby asphalt. If ground brightens unintentionally, inspect receiver membership; if the tram floats, restore motivated contact light.

#### How you can paint broken low poly glass in Blender. #b3d #blender3d

Short · Narration.[156]

**Evidence:** Timestamped narration from the Short. **Locator:** 00:10–00:17 mask group; 00:34–00:42 smoothing boundary

**Observed:** The author masks out painted glass, restricts smoothing so the outer border does not move, then gives the surviving sheet thickness.[156]

**Try:** Use one group to retain glass and another to define what can smooth. Stack Mask → Smooth → Solidify on a subdivided pane.

**Check:** A ray must pass through the hole while the intact pane still blocks it. Compare the frame corner with an unprotected duplicate.

#### How to animate cameras switching in Blender #b3d #3danimation #blender3d

Short · Narration.[187]

**Evidence:** English narration in direct watch-page extract; no video frames inspected. **Locator:** 0:46–0:52

**Observed:** The surviving excerpt demonstrates selecting and moving a timeline marker with G to retime a camera switch. Initial camera binding is outside the available passage.[187]

**Try:** Retime an already-bound two-camera cut without moving either camera.

**Check:** Check which camera is active one frame before and exactly at the moved marker.

#### Lay down some cables as curves using the draw tool #b3d #blender3d #3d

Short · Narration.[158]

**Evidence:** Narration from the Short; the extract has one caption block. **Locator:** 00:00 opening block

**Observed:** The presenter gives a curve bevel depth, clears the starting spline and uses Curve Draw with cursor placement or placement on a surface.[158]

**Try:** For a static conduit, draw its path on the housing rather than simulating a cable. Set radius independently; use a different depth mode for a suspended span.

**Check:** Orbit the housing. The cable should follow the surface without disappearing inside it; inspect bends at the intended diameter.

### Sources

[154] https://www.youtube.com/watch?v=IjFXi2axl-8 — CG Boost: Change Your Lighting Without Re-Rendering
[156] https://www.youtube.com/watch?v=LraQIwC6uBo — How you can paint broken low poly glass in Blender. #b3d #blender3d
[158] https://www.youtube.com/watch?v=DlbZxDWahKw — Lay down some cables as curves using the draw tool #b3d #blender3d #3d
[162] https://www.youtube.com/watch?v=gLNl8Lidzk0 — 8 Mistakes to Avoid when Animating Cameras #b3d
[184] https://www.youtube.com/watch?v=HN2B92Sl0hQ — How to Light Almost Anything in Blender #b3d
[187] https://www.youtube.com/watch?v=KTynnt8UyCg — How to animate cameras switching in Blender #b3d #3danimation #blender3d
[205] https://www.youtube.com/shorts/VAFvEJHV7no — Blender Light Linking #b3d
[246] https://www.youtube.com/watch?v=zxhaCD-Zlfw — Hard-Surface Modeling in Blender for Beginners (Full Course) #b3d

<a name="chapter-creator-cgi-secrets"></a>

## @CGI_Secrets — source notes

72 public Videos entries; 108 Shorts; 6 individually noted.

[All creators and coverage](channel-register.md) · [Apply a lesson to the tram](channel-workshop.md). Evidence and proposed exercises are distinguished below.

#### The Hobbiton House in Blender Part 4 | Cinematic Lighting, Rendering & AI Post-Production

Video · Untimed or approximate stills.[241]

**Evidence:** Public YouTube numbered video stills 1.jpg, 2.jpg, 3.jpg, visually inspected. No published timestamp per still; not a custom thumbnail or proof of an operator. Exact handle videos tab lists this ID under UCinGVbrKPKd99npIgGO1laQ. **Locator:** Untimed: numbered stills 1–3

**Observed:** Part 4 stills show the house with a camera frame, then a close-up viewport with saturated false-color-like ground regions against outlined architecture. The description explicitly distinguishes a raw render from online/offline AI enhancement. These stills do not identify the colored overlay, lighting values or AI tool.[241]

**Try:** Keep the raw render when testing external post-production, so it is possible to identify which architectural details changed outside Blender.

**Check:** Compare the raw and enhanced entrance, arches and window divisions edge-for-edge; reject invented openings.

#### The Hobbiton House in Blender Part 3 | Create Realistic Grass, Trees & Fantasy Environment

Video · Untimed or approximate stills.[222]

**Evidence:** Public YouTube numbered video stills 1.jpg, 2.jpg, 3.jpg, visually inspected. No published timestamp per still; not a custom thumbnail or proof of an operator. Exact handle videos tab lists this ID under UCinGVbrKPKd99npIgGO1laQ. **Locator:** Untimed: numbered stills 1–3

**Observed:** Part 3 public stills show a gray house and porch on sloping ground, followed by rows of sphere previews above branching forms. The title and description name grass and trees; neither the scatter method nor final density is readable.[222]

**Try:** Use the unplanted house on the terrain as a baseline for an environment pass: preserve the entrance silhouette when adding foliage.

**Check:** Compare planted and unplanted camera views; if the porch vanishes, change plant placement rather than altering the house.

#### The Hobbiton House in Blender Part 2 | Professional UV Mapping & Realistic Materials

Video · Narration.[200]

**Evidence:** Timestamped narration, selected window passage; not a review of every minute of the episode. **Locator:** 00:53 inward extrusion; 02:09 pane; 03:40–05:19 opening the grille; 06:10–07:04 seating

**Observed:** The inspected passage extrudes the opening inward, fills its inner loop for the glass, and separately builds a grille from a gridded plane by insetting cells and removing faces. The episode title advertises UVs; those are not the actions in this passage.[200]

**Try:** Reuse a cab window boundary for the pane. Build its grille as a separate part with visible thickness, then seat both in the same recess.

**Check:** Orbit with a bright backdrop. Look for blocked cells, coincident faces or a hairline gap around the glass.

#### The Hobbiton House in Blender Part 1 | Complete 3D Modeling & Architectural Details

Video · Sampled frames.[212]

**Evidence:** Public YouTube player storyboard, visually inspected; timestamps are sampled tile starts at its published interval. Exact handle videos tab lists this ID under UCinGVbrKPKd99npIgGO1laQ. **Locator:** 25:40, 32:10, 38:30, 57:50, 64:10

**Observed:** The gray shell, supports and projecting roof are visible at 25:40; at 32:10 a large round form passes through the porch area. At 57:50 the roof has a semicircular dormer with vertical divisions. The 64:10 assembly shows the curved roof, round entrance zone, steps and posts together.[212]

**Try:** Block the shell around the round entrance first; use a related but smaller arch on the roof to repeat the motif without duplicating its scale.

**Check:** Check the relative entrance/dormer sizes in a material-free three-quarter view and verify steps and posts do not obscure the entrance.

#### Move Only the Origin in Blender! 🤯🔥 | Hidden Blender Trick #Shorts

Short · Sampled frames.[194]

**Evidence:** Public YouTube player storyboard, visually inspected; timestamps are sampled tile starts at its published interval. Exact handle shorts tab lists this ID under UCinGVbrKPKd99npIgGO1laQ. **Locator:** 00:07, 00:13, 00:16–00:23, 00:29

**Observed:** A transform popover shows Origins; a snap menu and a cursor over the selected box lid follow. At 29s the lid is open while the base remains in place. The exact snapped point is not resolved.[194]

**Try:** For a hinged prop, position the lid’s origin on the intended hinge axis instead of rotating about its center.

**Check:** Rotate through an open/close cycle: hinge edge should stay on the base, and the closed lid should return flush.

#### Stop Hitting the ZOOM WALL in Blender! 🤯 | Blender Tips #Shorts

Short · Narration.[179]

**Evidence:** English narration in direct watch-page extract; no video frames inspected.

**Observed:** The narrator encounters a zoom limit, then enables Depth under Navigation preferences.[179]

**Try:** Try depth-aware navigation when close inspection stalls before reaching the surface.

**Check:** Compare zoom over the same mesh feature before and after; do not confuse viewport navigation with camera focal length.

### Sources

[179] https://www.youtube.com/watch?v=BIJpROmxx94 — Stop Hitting the ZOOM WALL in Blender! 🤯 | Blender Tips #Shorts
[194] https://www.youtube.com/shorts/ORpby_y4FuA — Move Only the Origin in Blender! 🤯🔥 | Hidden Blender Trick #Shorts
[200] https://www.youtube.com/watch?v=SmOzWdANpz8 — The Hobbiton House in Blender Part 2 | Professional UV Mapping & Realistic Materials
[212] https://www.youtube.com/watch?v=bIISl3S5K7I — The Hobbiton House in Blender Part 1 | Complete 3D Modeling & Architectural Details
[222] https://www.youtube.com/watch?v=f0ZNwuNDqMU — The Hobbiton House in Blender Part 3 | Create Realistic Grass, Trees & Fantasy Environment
[241] https://www.youtube.com/watch?v=wTh0_w_G_PU — The Hobbiton House in Blender Part 4 | Cinematic Lighting, Rendering & AI Post-Production

<a name="chapter-creator-christopher3d475"></a>

## @christopher3d475 — source notes

212 public Videos entries; 15 Shorts; 7 individually noted.

[All creators and coverage](channel-register.md) · [Apply a lesson to the tram](channel-workshop.md). Evidence and proposed exercises are distinguished below.

#### The secret architecture to predictable materials

Video · Narration.[161]

**Evidence:** Narration; no action timestamps in the material-layer extract.

**Observed:** A clear coat sits above the underlying surface: some light reflects at the coat and the remainder reaches the base. A metal base and its coat are not two independent full-strength highlights added together.[161]

**Try:** Compare bare and clear-coated metal under one fixed strip light. Change coat roughness without changing the base color or the card position.

**Check:** Watch the highlight travel from face-on to grazing. If both finishes only brighten uniformly, the lighting comparison is not isolating the coat.

#### THIN WALL, the incredible new Principled BSDF feature in Blender 5.2

Video · Sampled frames.[221]

**Evidence:** Visually inspected public YouTube player storyboard sequence; times in seconds from player storyboard interval. Creator description identifies version and use cases; no benchmark result independently verified. **Locator:** 120 s; 220 s; 430 s; 550 s; 870 s; 950 s

**Observed:** The creator compares transmission concepts, thin fabric/window scenes and a glazed architectural interior; description specifies the Blender 5.2 Principled Thin Wall feature for sheet materials. Not an add-on or a 4.5 baseline feature.[221]

**Try:** If Thin Wall is present, compare a single-face pane with a solid thick glass block over a striped card using an oblique camera.

**Check:** Keep the pane visually distinct from the block: if both distort stripes as thick glass, verify geometry and shader mode.

#### Modeling pleated curtains using shape keys and cloth simulation

Video · Sampled frames.[244]

**Evidence:** Visually inspected public YouTube player storyboard sequence; times in seconds from player storyboard interval. Creator-authored chapters inspected. **Locator:** 60 s; 350 s; 1040 s; 1220 s; 1380 s

**Observed:** Creator chapters explicitly sequence a single pleat, two vertex groups, duplicates, cloth, an animated shape key, then Apply as Shape Key. Frames show repeated ringed panels and the gathered mesh. Stock cloth/shape keys.[244]

**Try:** Test three pleats with a driven top edge and free lower edge; preserve a settled cloth result as a shape key on a copy.

**Check:** Scrub the saved shape-key value with simulation disabled: folds should return without rebaking, and attachment holes should remain at their supports.

#### Randomize textures with the Geometry node, Random Per Island.

Video · Sampled frames.[230]

**Evidence:** Visually inspected public YouTube player storyboard sequence; times in seconds from player storyboard interval. Creator description confirms island scope. **Locator:** 30 s; 160 s; 395 s; 630 s; 685 s

**Observed:** One wood texture is varied over disconnected planks; the creator identifies Geometry &gt; Random Per Island for per-piece variation. Stock shader node, not Geometry Nodes scattering.[230]

**Try:** Use an array of disconnected boards and drive a texture-coordinate offset with the per-island value. Compare a fixed patch on each board.

**Check:** Grain should remain continuous within each board but not repeat the same knot across boards; an identical knot indicates insufficient variation.

#### Ico Spheres and the Cast modifier! #shorts

Short · Sampled frames.[209]

**Evidence:** Visually inspected public YouTube player storyboard sequence; times in seconds from player storyboard interval. Creator description corroborates purpose. **Locator:** 13 s; 20 s; 26 s; 52 s; 56 s

**Observed:** The faceted ico sphere becomes smooth before displacement produces an irregular surface. Creator describes using the stock Cast modifier on triangular geometry to avoid pole pinching.[209]

**Try:** Displace a UV sphere and a cast ico sphere with identical texture scale; compare the silhouettes at the poles.

**Check:** Look for converging streaks or a dimple unique to one topology; judge both at comparable mesh density.

#### Seamless Cubic Mapping, No UVs! #shorts

Short · Narration.[218]

**Evidence:** English narration in direct watch-page extract; no video frames inspected. **Locator:** 0:00–0:40

**Observed:** For box projection without UVs, the speaker exposes texture space, disables automatic sizing, sets all three extents to the largest original value, and uses Generated coordinates.[218]

**Try:** Keep projected grain scale comparable on three faces of a rectangular package.

**Check:** Compare a square-grid image across differently proportioned faces; inspect seams separately from stretching.

#### Part 2, Curve Aligned handles are awesome!

Short · Narration.[210]

**Evidence:** English narration in direct watch-page extract; no video frames inspected. Title and author handle independently matched using YouTube oEmbed. **Locator:** 0:23–0:53

**Observed:** The speaker sets lower handles to Vector and upper handles to Aligned. Moving the top section and scaling it in X leaves the aligned handles collinear with their vector siblings.[210]

**Try:** Shape a bottle outline where a straight side flows into a curved shoulder.

**Check:** Widen the outline and inspect the tangent at the shoulder; it should not acquire a kink.

### Sources

[161] https://www.youtube.com/watch?v=56o9wbRsLVA — The secret architecture to predictable materials
[209] https://www.youtube.com/shorts/Z7odDAISjFQ — Ico Spheres and the Cast modifier! #shorts
[210] https://www.youtube.com/watch?v=a4p6_e-jDsw — Part 2, Curve Aligned handles are awesome!
[218] https://www.youtube.com/watch?v=dR-RrB8M8Ck — Seamless Cubic Mapping, No UVs! #shorts
[221] https://www.youtube.com/watch?v=eQLCfPwEcrI — THIN WALL, the incredible new Principled BSDF feature in Blender 5.2
[230] https://www.youtube.com/watch?v=ke0FzONVkxk — Randomize textures with the Geometry node, Random Per Island.
[244] https://www.youtube.com/watch?v=xXLRDpN6TWE — Modeling pleated curtains using shape keys and cloth simulation

<a name="chapter-creator-crntdesigners"></a>

## @CRNTDESIGNERS — source notes

769 public Videos entries; 103 Shorts; 4 individually noted.

[All creators and coverage](channel-register.md) · [Apply a lesson to the tram](channel-workshop.md). Evidence and proposed exercises are distinguished below.

#### How to Model a Mechanical Mounting Plate in Blender | Hard Surface Modeling

Video · Untimed or approximate stills.[239]

**Evidence:** Public YouTube numbered video stills 1.jpg, 2.jpg, 3.jpg, visually inspected. No published timestamp per still; not a custom thumbnail or proof of an operator. Exact handle videos tab lists this ID under UCC2eUQU7_ArzoojrMfibdyg. **Locator:** Untimed: numbered stills 1–3

**Observed:** A mounting plate is shown in a flat view with projecting rounded ends, then with a raised central rectangular panel and rounded end channel; a close-up isolates a circular center. The creator description mentions circular cutouts and bevels.[239]

**Try:** Start with the plate footprint and verify end clearances before detailing the raised central pad.

**Check:** Check the rim around the circular feature remains even; inspect corners separately from the broad flat pad.

#### From Simple Shapes to a Cute Retro Camera Design in Blender | Blender Hard Surface Modeling

Video · Sampled frames.[243]

**Evidence:** Public YouTube player storyboard, visually inspected; timestamps are sampled tile starts at its published interval. Exact handle videos tab lists this ID under UCC2eUQU7_ArzoojrMfibdyg. **Locator:** 00:30, 01:00, 01:25, 02:25, 03:55, 04:50

**Observed:** The camera housing is initially capsule-shaped. Close-up shows one rounded inset with concentric border loops, then two matching circular details in the front; a side projection and a short underside foot are developed later.[243]

**Try:** Build the primary enclosure and lens surrounds before small protrusions; inspect concentric spacing straight on.

**Check:** Compare left/right recess spacing front-on and inspect the depth of the side/foot profiles from a second angle.

#### How You Can Model This Industrial Junction Box in Blender? Blender Hard Surface Modeling

Video · Sampled frames.[216]

**Evidence:** Public YouTube player storyboard, visually inspected; timestamps are sampled tile starts at its published interval. Exact handle videos tab lists this ID under UCC2eUQU7_ArzoojrMfibdyg. **Locator:** 00:30, 01:05, 02:10, 03:15, 04:20, 04:50, 05:25

**Observed:** On the junction-box enclosure, a stepped top profile precedes a prominent circular end detail. Later close-ups show a small lower circular inset, a long recessed front panel and an end recess.[216]

**Try:** Separate enclosure silhouette, top lip and recessed face details into distinct modeling passes.

**Check:** At thumbnail size the box silhouette and lip should read; at close range check that recessed corners do not collapse into the outer bevel.

#### Blender Modeling - BM69 #blendermodeling #3dmodelingtutorial #shorts #hardsurfacemodeling

Short · Sampled frames.[237]

**Evidence:** Public YouTube player storyboard, visually inspected; timestamps are sampled tile starts at its published interval. Exact handle shorts tab lists this ID under UCC2eUQU7_ArzoojrMfibdyg. **Locator:** 00:05, 00:16, 00:26, 00:32, 00:37, 00:47

**Observed:** A rounded slab has a circular feature set into its end; wire inspection shows surrounding faces and concentric rings. Later a side close-up shows a beveled transition at a notch. No end use is specified.[237]

**Try:** Use an isolated rounded plate as a practice shape for the transition from a circular inset to long planar faces.

**Check:** Inspect the inset straight on and the outer bevel in grazing light; the ring should remain circular and the long face visually flat.

### Sources

[216] https://www.youtube.com/watch?v=d5uAg0duGNM — How You Can Model This Industrial Junction Box in Blender? Blender Hard Surface Modeling
[237] https://www.youtube.com/shorts/rQWqorkXbqM — Blender Modeling - BM69 #blendermodeling #3dmodelingtutorial #shorts #hardsurfacemodeling
[239] https://www.youtube.com/watch?v=uoVKc6b1FQ0 — How to Model a Mechanical Mounting Plate in Blender | Hard Surface Modeling
[243] https://www.youtube.com/watch?v=x3V-qjyu71o — From Simple Shapes to a Cute Retro Camera Design in Blender | Blender Hard Surface Modeling

<a name="chapter-creator-demnikoart"></a>

## @DemNikoArt — source notes

97 public Videos entries; 126 Shorts; 4 individually noted.

[All creators and coverage](channel-register.md) · [Apply a lesson to the tram](channel-workshop.md). Evidence and proposed exercises are distinguished below.

#### Rig a Real Joystick in Blender Using Rigid Body Constraints

Video · Narration.[258]

**Evidence:** Timestamped narration; selected lever and constraint passages. **Locator:** 01:03 lever behaviour; 02:37 local rotation limit; 09:10 constraint axes; 12:27 rotation controls

**Observed:** In DemNikoArt’s lift demonstration, lever deflection sets the speed of the response. The control is limited on local axes; the constraint’s axis, not the visible shape’s orientation, defines the driven rotation.[258]

**Try:** Test a single rigid actuator before duplicating any linkage: give the control a local angular limit and check direction on either side of neutral.

**Check:** A small deflection should produce a slower response than a large one, with no sideways rotation. Test the return to neutral as well as both end stops.

#### Control your ENTIRE Rig with ONE Bone (Blender) - Step by Step

Video · Description / chapters.[223]

**Evidence:** Public creator description, not playback. Creator-written chapters read on public watch page; chapter starts are signposts, not frame times. **Locator:** chapter starts 00:55 bones, 03:44 parent objects, 05:15 Copy Rotation, 08:08 Transformation constraint, 13:06 cage adjustment

**Observed:** The creator identifies a lift driven by one control, with a separate stage for parenting rigid objects, then a Copy Rotation stage followed by a Transformation constraint stage. Specific target axes, ranges and space settings were not verified.[223]

**Try:** For an animated maintenance lift, establish a single height control, align pivots in a side view, and test one crossed linkage before duplicating it.

**Check:** Scrub collapsed, mid and raised positions; pivot centers should coincide and the basket should not tilt or move through the chassis.

#### The "Simple" Rig That's Actually Complicated - Blender Tutorial

Video · Sampled frames.[186]

**Evidence:** Visually inspected timestamped YouTube player storyboard samples, not continuous playback. Creator-written chapters read on public watch page; chapter starts are signposts, not frame times. **Locator:** chapter starts 01:28 analyze, 04:44 IK, 08:26 troubleshoot; frames 03:55, 05:15, 11:50

**Observed:** A side view isolates the seat/leg linkage. Armature elements lie over the pivots at 03:55 and 05:15; 11:50 zooms onto the physical link and its two pivot holes. The creator describes a mismatch between model proportions and folding logic, not just a constraint toggle.[186]

**Try:** For a fold-down passenger seat, mark actual hinge centers on the mesh before building the bone chain. Check proportions before compensating for a bad fold with extra keys.

**Check:** In side view scrub to folded: hinge holes and bone endpoints should stay concentric, the seat should clear its frame, and rigid bars should retain length.

#### NEW TUTORIAL - rigging a scissor lift in blender #b3d #blender3d #rigging #3danimation #tutorial

Short · Sampled frames.[238]

**Evidence:** Visually inspected timestamped YouTube player storyboard samples, not continuous playback. **Locator:** 00:04; 00:08; 00:20; 00:27; 00:31

**Observed:** The Short is a rig demonstration, not a constraint tutorial: separated colors clarify crossing links at 00:08; the full stack is visible at 00:20. At 00:27 the red basket sits close to its base, and by 00:31 it is raised with control overlays.[238]

**Try:** Use a color-coded side-view diagnostic and compare end poses before rendering an articulated prop.

**Check:** A rigid link must not visibly stretch or detach at either end; inspect mid-travel too. Do not infer exact solver settings from this Short.

### Sources

[186] https://www.youtube.com/watch?v=KNhBr-ODIjk — The "Simple" Rig That's Actually Complicated - Blender Tutorial
[223] https://www.youtube.com/watch?v=fQY12vlWWP4 — Control your ENTIRE Rig with ONE Bone (Blender) - Step by Step
[238] https://www.youtube.com/shorts/thRT9toFnX4 — NEW TUTORIAL - rigging a scissor lift in blender #b3d #blender3d #rigging #3danimation #tutorial
[258] https://www.youtube.com/watch?v=EFH4wZeXu3w — Rig a Real Joystick in Blender Using Rigid Body Constraints
