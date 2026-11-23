# Building a rainy tram terminus: lessons from the channel study

Look at **Last Dispatch at Lumen Quay** in the [README gallery](https://github.com/Noa3/Blender-Workshop#blender-showcase): read the destination on the car, follow the line of roof ribs, then look for the lamp reflection beside the luggage. Those are three different problems: legibility, depth and material response. Pick the one that fails in your own shot. This is an original still, not a reconstruction of anyone’s tutorial. The scene is not distributed; [two local bench tests](lighting.md#chapter-tram-light-lab) let you try the lighting and glazing techniques with the included generators.

| If this fails | Try first | What counts as a pass |
|---|---|---|
| The window looks painted onto the body | Build a shallow rebate and fit the pane to its edge | Rim, reveal and glass stay distinct under grazing light |
| A station lamp or its reflection is too bright | [Relight the finished render](lighting.md#chapter-tram-light-lab) | The station contribution changes without turning off the car |
| Every paving stone looks varnished | Change the ground roughness, not exposure or light power | The wide lamp reflection breaks up, while the sign stays legible |
| The same detail needs fixing in seven bays | Edit the shared roof rib, not its placed copies | All seven bays change; the route down the platform stays clear |
| A broken pane is floating out of its frame | [Protect its boundary before smoothing](lighting.md#chapter-tram-light-lab) | The break is open, its intact patch still exists and its corner stays seated |

## 1. Build fittings from the opening, not from a second drawing

CG Loop’s vintage television is a useful *sequence*, not just a shape to copy. In Part 1, **02:32** introduces the screen recess and **06:05** the loop around its boundary. In Part 2, **05:12–05:44** shows why an edge pattern that works on a flat face overlaps on a steep one; **08:52** separates the recessed faces to start a fitted lid. Part 3 opens by reusing the original speaker cutter for its surround; **03:08** repeats the grille in two directions.[178][235][174]

**Try it on a cab window.** Block the nose in front and side views. Inset the window outline and extrude it inward a short distance. Duplicate the seated face or its outline to start the glazing; leave a real reveal. Put support loops beside the lip and keep five-edge junctions off the shoulder that catches the long highlight. For a vent, repeat one correctly sized opening *behind* the surround. From a grazing angle, look for a pinched reflection, a gap in the gasket, or two coincident surfaces flickering. Fix the first bad corner before repeating the panel.

For luggage, Sneha Verma’s case sequence goes from a chamfered mass at **00:40** to panel corners, angled borders and a bank of repeated slots; CRNT Designers’ compact camera separates a capsule-shaped housing from concentric lens details.[197][243] **Our adaptation:** get the case and lid seam to read first, then add straps and buckles only where the camera can resolve them. Hide the hardware: if the object stops reading as a suitcase, fix its proportions rather than adding more fasteners.

## 2. Give repeated structures a shared part and a fixed pitch

Blender Guru’s staircase uses an Array for rise and run; the older Christopher 3D handle lesson distinguishes straight Vector handles from Aligned handles at a curve transition.[196][210] Neither is a tram-station tutorial. At Lumen Quay a bowstring rib is a *collection instance*: a pair of chords, a tie and a lattice recur together. Changing one component in the kit changes all seven bays. The longitudinal glass and rails are separate, so a change to one span does not multiply the platform.

**Check:** look along the rail at camera height. Repetition should describe distance without crossing the destination roll. Switch to a side orthographic view before moving a support; perspective alone will not reveal uneven pitch. Arch on Arch’s Drawing View demonstration makes the case for a separate elevation and legible sheet notes. The add-on appears in the source; a stock orthographic camera and text are sufficient for this check.[228][193]

## 3. Separate the weather you see from the weather you simulate

The rain narration in *How to Create Realistic Rain in Blender* distinguishes an upper emitter, an impact surface and a lower particle-kill surface; it instances a small mesh for a drop.[155] Blender Made Easy’s Mantaflow comparison shows why a flat emitter and an inward-facing collider are separate failure modes and why an old bake can mask a fix.[168]

**For a single still**, start smaller: damp roughness on the platform, a little eave rain against a dark background, and a bounded volume between the foreground and distant buildings. The original Lumen Quay still used those controls without a rain or water bake. In your own scene, lock the camera and leave a dry-looking patch next to a wet one. Vary only the paving roughness; the width of the reflected lamp highlight should change locally. If global contrast changes, check lighting and the view transform. For a moving shot, test births, impacts and cleanup separately before spending time on a fluid cache.

## 4. Decide what a highlight belongs to

In Blender Guru’s lighting lesson, the same case sits against black at **05:50**, casts a long shadow at **11:20**, nearly loses detail at **14:50**, and reads again at **18:30**.[182] Christopher 3D distinguishes the material’s base response from a coating above it; the Blender Academy material study changes the finish of one test sphere while keeping its shape.[161][207]

**Try:** keep one card light and one fixed camera. On the tram, compare the ivory strip above the windows, red enamel and metal trim. Widen the card to test highlight width before changing roughness. Then change only the roughness or coat on a material. If the chrome and the painted panel suddenly look identical, undo that last change and identify which reflection describes the base and which describes the clear coat. A bright visible lamp globe and the pool it throws are also different controls; do not use global exposure to fix one of them. Use the [light-group lab](lighting.md#chapter-tram-light-lab) to distinguish the two.

## 5. Spend contrast on the passenger’s route

Keep the destination, platform number and clock distinguishable from their frames. Freedom Arts 3D’s road-sign lesson assigns the graphic to the front face and fits the UV to an image region.[159] The station used editable Blender text with a built-in font. Mr. H’s combined 2D/3D example stacks a character rendered on transparency over a background; that is an option if the figure needs a drawn treatment. The gallery still used geometry, not that composite.[240]

**Check:** shrink the final to phone width. The destination should read before the small brass plate on the pillar. If a bright roof brace cuts the letters, change the camera or brace placement before increasing text emission. For animation, CG Boost’s camera lesson identifies unnecessarily fast travel and shake that does not match the speed of the move; run the entire move, not just the first frame. This still does not test motion.[162]

## 6. Preserve the evidence and the software boundary

- BlendTweaks’ knurling Short shows detail confined to a grip collar. In a different prop, borrow the placement, not an unverified tool sequence: taper detail *out* on the smooth shaft and inspect it under a raking light.[183]
- DemNikoArt’s mechanical rig studies and Blender Academy’s parenting lesson suggest two distinct checks: rigid pieces should rotate around their pins, and a whole assembly should move once under its root. Do not smooth-skin rigid fittings to disguise a bad pivot.[186][160]
- Christopher 3D’s **Blender 5.2** thin-wall material demo is not a promise that its shader control exists in 4.5. Likewise, a YNG3D ZBrush sculpt can teach the order of hair masses without establishing a Blender brush preset.[221][175]
- For a morph export, follow Freedom Arts 3D’s blink test: reimport the file, set the key to zero and one, and look at the eyelids. A successful export or the name of a slider alone proves little.[233]
- Do not turn a showcase title into a recipe. The *Hobbiton* Part 2 passage inspected here is about seating a window and assembling its grille, not proof of a particular UV workflow. The Ascend rain stills do not reveal particle settings. The YNG3D fog listing alone is not a volume-node recipe.[200][204][164]

The [creator notebook](channel-register.md) records the credited items, what was actually accessible, a proposed transfer and a failure check. Its labels distinguish speech, timed frames, untimed frames, written companions and descriptions. A proposed exercise is not a measured result. The catalog is kept separately so thousands of unstudied titles do not become instructions.

## Sources

[155] https://www.youtube.com/watch?v=GeD8FT3NZ-A — How to Create Realistic Rain in Blender | Easy Particle Tutorial
[159] https://www.youtube.com/watch?v=CH0h87EtG5k — Blender to iClone 8 Workflow: Create Realistic 3D Road Signs (UV, FBX, Materials)
[160] https://www.youtube.com/watch?v=CnTYQAcxXPc — Blender Beginner Tutorial – Parent Objects
[161] https://www.youtube.com/watch?v=56o9wbRsLVA — The secret architecture to predictable materials
[162] https://www.youtube.com/watch?v=gLNl8Lidzk0 — 8 Mistakes to Avoid when Animating Cameras #b3d
[164] https://www.youtube.com/watch?v=Dgika_gEW0U — Mix volumetric and lighting color to the best fog in cyberpunk city blender Tutorial
[168] https://www.youtube.com/watch?v=2O0QcLpAxV4 — Common Mantaflow Problems & How to Fix Them!
[174] https://www.youtube.com/watch?v=8QttquaMgkY — Finishing the Vintage TV model | Part 3 of Vintage TV tutorial series
[175] https://www.youtube.com/watch?v=97l111y1tDg — How to Sculpt Reze Head & Face in ZBrush | Chainsaw Man 3D Fan Art
[178] https://www.youtube.com/watch?v=B9bNxUH_kZo — The Only 3D Modeling Tutorial You'll Ever Need.
[182] https://www.youtube.com/watch?v=ENnEYoUpFfU — Fundamentals of Lighting in Blender
[183] https://www.youtube.com/shorts/FmIqa8aRFBw — NOOB vs PRO: Knurling in Blender
[186] https://www.youtube.com/watch?v=KNhBr-ODIjk — The "Simple" Rig That's Actually Complicated - Blender Tutorial
[193] https://www.youtube.com/watch?v=O0FcbNrRIwc — Drawing View — Annotations in Blender
[196] https://www.youtube.com/watch?v=OnAmoFFn1jQ — How to make stairs in Blender
[197] https://www.youtube.com/watch?v=Qz6C8BNplJo — How to Model a Sci-Fi Industrial Case in Blender | Complete 3D Modeling Tutorial
[200] https://www.youtube.com/watch?v=SmOzWdANpz8 — The Hobbiton House in Blender Part 2 | Professional UV Mapping & Realistic Materials
[204] https://www.youtube.com/watch?v=Ujzd69gvGxY — Realistic Rain in Blender: Quick VFX Setup
[207] https://www.youtube.com/watch?v=Yj15h6UcMWY — A Simpler Approach to Adding Realistic Materials To Your Blender Model (Blender rendering tutorial)
[210] https://www.youtube.com/watch?v=a4p6_e-jDsw — Part 2, Curve Aligned handles are awesome!
[221] https://www.youtube.com/watch?v=eQLCfPwEcrI — THIN WALL, the incredible new Principled BSDF feature in Blender 5.2
[228] https://www.youtube.com/watch?v=jIu2la9LK5E — Drawing View — Architectural Drawing Add-on for Blender
[233] https://www.youtube.com/watch?v=no2z2JndG6E — How to Export FBX from Blender with Shape Keys (Preserve Morph Targets & Facial Keys)
[235] https://www.youtube.com/watch?v=oFmS1asrjcs — The BEST Way to model complex details | Part 2 of Vintage TV tutorial series
[240] https://www.youtube.com/watch?v=vi-nqmqDXTs — How to Render & Combine 2D and 3D Animation (Without Complex Compositing)
[243] https://www.youtube.com/watch?v=x3V-qjyu71o — From Simple Shapes to a Cute Retro Camera Design in Blender | Blender Hard Surface Modeling
