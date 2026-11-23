# Creator notebook — part 4

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [@FreedomArts3D — source notes](#chapter-creator-freedomarts3d)
- [@mr.h — source notes](#chapter-creator-mr-h)
- [@snehaverma1991 — source notes](#chapter-creator-snehaverma1991)
- [@W3-productions — source notes](#chapter-creator-w3-productions)
- [@YNG3D — source notes](#chapter-creator-yng3d)

<a name="chapter-creator-freedomarts3d"></a>

## @FreedomArts3D — source notes

1,645 public Videos entries; 478 Shorts; 13 individually noted.

[All creators and coverage](channel-register.md) · [Apply a lesson to the tram](channel-workshop.md). Evidence and proposed exercises are distinguished below.

#### How to Export FBX from Blender with Shape Keys (Preserve Morph Targets & Facial Keys)

Video · Sampled frames.[233]

**Evidence:** Public YouTube player storyboard, visually inspected at labelled sample times; creator chapter labels also inspected. **Locator:** 00:08; 00:40; 00:48; 01:25; 02:12; 02:32

**Observed:** Open-eyed character before export; export dialog at 00:48; reimported character later shown with eyes shut and mouth open. Creator chapters explicitly identify disabling Apply Modifiers at 00:40, an earlier-version import test at 01:25, and morph verification at 02:12. The toggle name comes from the chapter, not legible pixels.[233]

**Try:** Export a duplicate mesh with a known blink and expression as FBX, disable Apply Modifiers for this test, then import into a clean file.

**Check:** Confirm named keys exist and moving each from zero to one visibly changes the intended vertices; do not count a successful import as proof.

#### Blender 5.0 FBX Export with Shape Keys Preserved | Keep Blendshapes for Animation

Video · Narration.[281]

**Evidence:** Public watch-page narration extract; no frame inspection. **Locator:** 00:37; 01:14; 02:11

**Observed:** The Blender FBX exporter warns that Apply Modifiers prevents exporting shape keys. The narrator disables it and reimports the FBX to find the facial keys on the face mesh.[281]

**Try:** Keep facial deformation data as a separate acceptance criterion from mesh appearance.

**Check:** Import into an empty file and drive a named expression slider; a correct neutral face alone is insufficient.

#### Blender to iClone 8 Workflow: Create Realistic 3D Road Signs (UV, FBX, Materials)

Video · Narration.[159]

**Evidence:** Timestamped narration; Blender section and later export distinguished. **Locator:** 03:14–06:27 materials and fitting UVs; 11:26 export test

**Observed:** The front face receives the sign graphic, with its UV fitted to the graphic on the sheet; the back and pole retain a different finish. The later FBX handoff is a separate step.[159]

**Try:** For a textured berth sign, assign the printed face separately and fit that island to the right tile. Use editable text instead when the wording changes frequently.

**Check:** Look at the back and the thin edge from an oblique view. Neither should show fragments of the front graphic.

#### Blender 4.2 Texture Tutorial | How to Manually Attach Material Textures (FBX Fix Guide)

Video · Narration.[272]

**Evidence:** Public watch-page narration extract; no frame inspection. **Locator:** 00:35; 00:40

**Observed:** For an FBX whose image has not attached, the narrator selects the mesh, adds a material and chooses Image Texture for Base Color.[272]

**Try:** Repair the affected material slot instead of reimporting the whole model.

**Check:** In Material Preview, confirm the intended image is on that mesh, not just present in the file.

#### Mixamo to Blender Tutorial: Retarget Animations to Any 3D Avatar with Rokoko Plugin

Video · Narration.[269]

**Evidence:** Public watch-page narration extract; no frame inspection. **Locator:** 06:35

**Observed:** A duplicate target-bone error stops Rokoko retargeting. The narrator traces the hip/spine/chest assignments, removes the redundant entry, resets the armature X location and retargets again.[269]

**Try:** Audit source-to-target mappings before changing weights or rebuilding a rig.

**Check:** Hide the source rig and play the clip on the target; check torso and limbs, not just the absence of an error.

#### Blender to Unreal Engine 5.4: Rig & Import 3D Characters (Player & NPC Setup)

Video · Narration.[253]

**Evidence:** Public watch-page narration extract; no frame inspection. **Locator:** 09:40

**Observed:** The instructor identifies Freedom Animation Pipeline as a separate plug-in for converting the FBX exported by Auto-Rig Pro; this is not a stock Unreal importer feature.[253]

**Try:** For a Blender-to-Unreal rig handoff, record both the exporter and the conversion plug-in rather than promising the FBX is self-sufficient.

**Check:** Test the same FBX on the receiving workstation and check for the expected rig before building animation around it.

#### GLB to FBX 3D Model Conversion | Tutorial | Blender | 3D Modeling

Video · Narration.[280]

**Evidence:** Public watch-page narration extract; no frame inspection.

**Observed:** The narrator imports GLB, previews its textures, enables FBX Path Mode Copy plus embedding, and opens the result in a separate 3D viewer.[280]

**Try:** Use an independent viewer to test a format conversion before handing it to the next artist.

**Check:** Move the exported FBX away from the working texture directory and check its image materials again.

#### Daz Studio to Blender 3.6 - Pipeline Tutorial - Daz to Blender Bridge

Video · Narration.[277]

**Evidence:** Public watch-page narration extract; no frame inspection. **Locator:** 03:51; 04:26; 05:02

**Observed:** The Daz bridge targets a specific Blender installation. The narrator enables the add-on there, sends from Daz, then explicitly imports the new Genesis figure in Blender.[277]

**Try:** Treat sender configuration and receiver activation as separate steps in a bridge handoff.

**Check:** Look for the bridge in the receiving Blender sidebar, then inspect the imported figure in textured view.

#### Procedural Building Generator 2 - Blender 3.6 Tutorial - Generate & Export FBX

Video · Narration.[249]

**Evidence:** Public watch-page narration extract; no frame inspection. **Locator:** 01:31

**Observed:** The instructor converts the generated building to mesh, saves the diffuse image, reconnects it to Base Color, and exports the selected building with FBX Copy and embedding enabled.[249]

**Try:** Keep a procedural master and deliver a separate mesh copy to tools that cannot evaluate its generator.

**Check:** Open the FBX outside the source scene: verify the building and facade texture together.

#### FBX Mesh Transparent when imported? Fixed - Blender Tutorial

Video · Narration.[257]

**Evidence:** Public watch-page narration extract; no frame inspection.

**Observed:** In this older Blender example a freshly imported character looks see-through. The narrator disables Show Backface for the affected material and checks the eyes separately.[257]

**Try:** Diagnose per-material transparency before changing an entire imported character. The setting name is version-specific.

**Check:** Orbit the face and inspect the eyes separately; preserve any parts that are supposed to be transparent.

#### Mixamo autorig and add motion to Blender

Video · Narration.[278]

**Evidence:** Public watch-page narration extract; no frame inspection.

**Observed:** During Mixamo preparation the narrator names separate unrigged and T-pose FBXs, then selects In Place for a walk so a motion path can be supplied later.[278]

**Try:** Decide who owns forward travel before downloading a locomotion clip.

**Check:** Preview the clip: for an in-place delivery the character should cycle its legs without travelling forward.

#### Vroid to Blender & FBX

Video · Narration.[262]

**Evidence:** Public watch-page narration extract; no frame inspection. **Locator:** 12:01; 12:25

**Observed:** In the historical VRoid workflow, the importer’s file filter hides the exported VRM. The narrator clears the filter, imports it and inspects bones, expressions and textures.[262]

**Try:** Distinguish a file-browser filter from a failed export; verify rig data as well as visible geometry.

**Check:** Confirm the VRM exists, then check a bone, facial expression and textured surface in Blender.

#### AccuRig Auto Rigging for Blender 5.0 in 1 minutes with Character Creator 5 (CC5) #blender #rigging

Short · Sampled frames.[206]

**Evidence:** Public YouTube player storyboard, visually inspected at labelled sample times; no narration used. **Locator:** 00:00; 00:08; 00:12

**Observed:** Accelerated promotional Short: a neutral character, a Character Creator window around 00:08 and the figure back in a viewport at 00:12. The overlay points to a full-speed tutorial. Joint markers and weights cannot be verified in these frames.[206]

**Try:** Treat neutral-pose return as an interchange checkpoint, not as proof of usable skin weights.

**Check:** On return to Blender pose one elbow and one knee; check for trapped vertices and incorrect bone assignment.

### Sources

[159] https://www.youtube.com/watch?v=CH0h87EtG5k — Blender to iClone 8 Workflow: Create Realistic 3D Road Signs (UV, FBX, Materials)
[206] https://www.youtube.com/shorts/VnDQPQ6zkcw — AccuRig Auto Rigging for Blender 5.0 in 1 minutes with Character Creator 5 (CC5) #blender #rigging
[233] https://www.youtube.com/watch?v=no2z2JndG6E — How to Export FBX from Blender with Shape Keys (Preserve Morph Targets & Facial Keys)
[249] https://www.youtube.com/watch?v=18xXn-FbhpM — Procedural Building Generator 2 - Blender 3.6 Tutorial - Generate & Export FBX
[253] https://www.youtube.com/watch?v=8jIX2FXV4G8 — Blender to Unreal Engine 5.4: Rig & Import 3D Characters (Player & NPC Setup)
[257] https://www.youtube.com/watch?v=D9puZPfwOVI — FBX Mesh Transparent when imported? Fixed - Blender Tutorial
[262] https://www.youtube.com/watch?v=NhI3F_e4sw0 — Vroid to Blender & FBX
[269] https://www.youtube.com/watch?v=UcXIWi3fKBA — Mixamo to Blender Tutorial: Retarget Animations to Any 3D Avatar with Rokoko Plugin
[272] https://www.youtube.com/watch?v=W7MJHCuWBvU — Blender 4.2 Texture Tutorial | How to Manually Attach Material Textures (FBX Fix Guide)
[277] https://www.youtube.com/watch?v=bg5lH_uJF1I — Daz Studio to Blender 3.6 - Pipeline Tutorial - Daz to Blender Bridge
[278] https://www.youtube.com/watch?v=fnLi04ufv1M — Mixamo autorig and add motion to Blender
[280] https://www.youtube.com/watch?v=fyiItV61Ufs — GLB to FBX 3D Model Conversion | Tutorial | Blender | 3D Modeling
[281] https://www.youtube.com/watch?v=haPsP5EfVTY — Blender 5.0 FBX Export with Shape Keys Preserved | Keep Blendshapes for Animation

<a name="chapter-creator-mr-h"></a>

## @mr.h — source notes

16 public Videos entries; 2 Shorts; 7 individually noted.

[All creators and coverage](channel-register.md) · [Apply a lesson to the tram](channel-workshop.md). Evidence and proposed exercises are distinguished below.

#### How to Render & Combine 2D and 3D Animation (Without Complex Compositing)

Video · Sampled frames.[240]

**Evidence:** Visually inspected timestamped YouTube player storyboard samples, not continuous playback. Creator-written chapters read on public watch page; chapter starts are signposts, not frame times. **Locator:** chapters 03:14 separate sequences, 06:18 assembly, 08:27 final output; frames 05:40, 06:40, 08:30

**Observed:** A pale character appears alone on transparency at 05:40. At 06:40 the video editor shows only a blue background plate; at 08:30 several stacked strips produce the combined image. The creator distinguishes layered image-sequence output from rendering directly to video.[240]

**Try:** Render painted sky, tram, and foreground rain as aligned image sequences. Assemble the strips before encoding the final movie so rain can be revised alone.

**Check:** Toggle each strip; the rear plate must remain visible through transparent pixels. Check first/last frame registration and edge halos over light and dark backgrounds.

#### How to Integrate & Animate 3D Models with 2D Characters

Video · Narration.[279]

**Evidence:** Public English transcript read; no footage viewed. The creator lists Blender 5.3. **Locator:** 01:08; 05:31; 06:24; 07:36

**Observed:** The droid parts are parented together so the controller can move the full prop relative to a Grease Pencil bear. The creator checks the crossing from above, then returns to the camera to make the droid appear to look at the bear.[279]

**Try:** Block the path in top view but pose the interaction in the shot camera.

**Check:** Scrub the crossing: do all parts follow, and does the gaze meet the drawn character on screen?

#### The Easiest 2D Style for 3D Models in Blender

Video · Narration.[255]

**Evidence:** Public English transcript read; no footage viewed. Native Workbench engine; the creator lists Blender 5.3. **Locator:** 00:33; 01:06; 02:16; 04:54

**Observed:** Workbench shadows establish the two-tone form. The droid’s colors come from material viewport-display colors, including a separate black material assigned just to the lens face, rather than from a shader-node network.[255]

**Try:** Build a small palette for a 3D prop that must match a drawn character.

**Check:** Render from the shot camera with Workbench: confirm the lens keeps its own flat color and the shadow direction matches the drawing.

#### Blender for 2D Artists: Learn 3D Modeling from Scratch

Video · Narration.[263]

**Evidence:** Public English transcript extract read; no footage viewed. The creator lists Blender 5.3. **Locator:** 38:17; 43:20; 47:26; 51:24

**Observed:** After creating scene Line Art with Grease Pencil, the creator marks selected edges on the droid to include interior panel lines rather than relying only on the outer silhouette. Line Art is hidden temporarily while working on the wing.[263]

**Try:** Use selective edge marks for a prop whose panel divisions need to read in a 2D shot.

**Check:** Render at actual shot size; remove marks that turn into visual noise or merge into the outline.

#### Intro to Grease Pencil in Blender - A Tutorial for Beginners

Video · Narration.[203]

**Evidence:** English narration in direct watch-page extract; no video frames inspected. **Locator:** 9:18–11:59; 11:59–12:59

**Observed:** Mr. H places the cursor at the pendulum hinge and rotates both strokes about it. He duplicates only the intervening drawings, mirrors their timing and ends at frame 24 rather than repeating frame 1 at 25.[203]

**Try:** Make a hand-drawn swinging shop sign with one fixed hinge and a reversible set of in-betweens.

**Check:** Track the hinge through a cycle and step across the loop boundary: no hinge slip or doubled endpoint hold.

#### 2D/3D Style Animation in Blender

Short · Description / chapters.[195]

**Evidence:** Public creator description, not playback.

**Observed:** The artist explicitly assigns the vehicle to 3D objects, character and foreground elements to Grease Pencil, and the background painting to Krita. This is a production breakdown, not a verified list of tools or strokes used frame by frame.[195]

**Try:** Use 3D for tram perspective, draw riders and foreground accents, and paint the distant background.

**Check:** Preview a camera move: if painted elements slide against the vehicle, change their placement or restrict the camera move.

#### Brandon Graham's Artwork Animated in Grease Pencil

Short · Description / chapters.[286]

**Evidence:** Creator-written public description only; no footage or transcript reviewed. The public player supplied no timed sampling interval.

**Observed:** The creator identifies a single image from Brandon Graham’s Royal Boiler sketchbook as the source for a Blender Grease Pencil animation and links the finished project. The description does not explain how the drawing was separated or timed.[286]

**Try:** Try a single-image motion study using your own drawing rather than redrawing a whole scene.

**Check:** Compare the still pose with the source drawing before evaluating the motion.

### Sources

[195] https://www.youtube.com/shorts/ORqig2ojoy8 — 2D/3D Style Animation in Blender
[203] https://www.youtube.com/watch?v=TrsL2AOHwYw — Intro to Grease Pencil in Blender - A Tutorial for Beginners
[240] https://www.youtube.com/watch?v=vi-nqmqDXTs — How to Render & Combine 2D and 3D Animation (Without Complex Compositing)
[255] https://www.youtube.com/watch?v=AycKuYYWqGc — The Easiest 2D Style for 3D Models in Blender
[263] https://www.youtube.com/watch?v=OOfaN2ZrQKk — Blender for 2D Artists: Learn 3D Modeling from Scratch
[279] https://www.youtube.com/watch?v=fx3q1sA4Uh4 — How to Integrate & Animate 3D Models with 2D Characters
[286] https://www.youtube.com/shorts/pyH6r55DSac — Brandon Graham's Artwork Animated in Grease Pencil

<a name="chapter-creator-snehaverma1991"></a>

## @snehaverma1991 — source notes

5 public Videos entries; 42 Shorts; 3 individually noted.

[All creators and coverage](channel-register.md) · [Apply a lesson to the tram](channel-workshop.md). Evidence and proposed exercises are distinguished below.

#### How to Model a Sci-Fi Industrial Case in Blender | Complete 3D Modeling Tutorial

Video · Sampled frames.[197]

**Evidence:** Public YouTube player storyboard, visually inspected at labelled sample times; no narration used. **Locator:** 00:40; 05:30; 10:50; 29:10; 35:50

**Observed:** Reference stays beside the modeling viewport: a chamfered rectangular mass at 00:40, close views of a rounded panel corner and an angled border, later a bank of repeated horizontal recesses and a full end view. The reference is colored; the edited mesh is gray.[197]

**Try:** Model a case using the reference for the overall clipped corners first, then a panel border and one repeated vent profile.

**Check:** Check corner radius in front and oblique views; check vent spacing and highlights in clay, not against the colored reference alone.

#### How to Model Insta360 X6 in Blender 3D/Step-by-Step Tutorial

Video · Sampled frames.[170]

**Evidence:** Public YouTube player storyboard, visually inspected at labelled sample times; no narration used. **Locator:** 03:20; 13:00; 16:20; 21:40

**Observed:** The camera reference is visible beside the working mesh. The front is lined up over the image, the view moves close to a raised side control, a rectangular lower recess and a circular lens opening with surrounding edges.[170]

**Try:** Use separate checks for body outline, control projection and lens rim rather than matching the camera only from the front.

**Check:** In an oblique clay view, the buttons must protrude and the lens opening must remain round without a dent at the shell transition.

#### Want to learn how I made this sci-fi 3D asset? / HOLOCOM  #3dartist

Short · Sampled frames.[199]

**Evidence:** Public YouTube player storyboard, visually inspected at labelled sample times; no narration used. **Locator:** 00:04; 00:08; 00:13; 00:16

**Observed:** Finished HOLOCOM reel: an illuminated screen, a panel of labels, a cool-lit fan grille and then the entire prop. These frames show presentation, not how it was modeled or lit.[199]

**Try:** Make a prop shot list: display, functional detail, then whole silhouette, or reverse the order for an establishing shot.

**Check:** A viewer should be able to locate each detail on the final wide shot.

### Sources

[170] https://www.youtube.com/watch?v=4yQpx5zh0C0 — How to Model Insta360 X6 in Blender 3D/Step-by-Step Tutorial
[197] https://www.youtube.com/watch?v=Qz6C8BNplJo — How to Model a Sci-Fi Industrial Case in Blender | Complete 3D Modeling Tutorial
[199] https://www.youtube.com/shorts/S8oS6ZC0UsY — Want to learn how I made this sci-fi 3D asset? / HOLOCOM  #3dartist

<a name="chapter-creator-w3-productions"></a>

## @W3-productions — source notes

130 public Videos entries; 35 Shorts; 3 individually noted.

[All creators and coverage](channel-register.md) · [Apply a lesson to the tram](channel-workshop.md). Evidence and proposed exercises are distinguished below.

#### Stylized Candle Flame in Blender – No Fire Simulation!

Video · Written companion.[163]

**Evidence:** First-party written companion, steps 1–7, plus creator chapters; no video frames. **Locator:** chapter starts 02:47 stored height, 04:15 wobble, 06:56 color, 08:48 edge fade, 11:53 flicker

**Observed:** The companion models a teardrop from local Z=0 at the base to 1 at the tip. It stores clamped Z on the point domain as flame_h before Set Position, uses height-weighted animated 4D noise to keep the wick pinned, and reads the stored attribute for the emission ramp. A separate point light supplies illumination in EEVEE.[163][247]

**Try:** For a station-window candle, keep deformation and shading tied to the same undeformed height. Animate a separate light contribution rather than relying on a bright pixel to illuminate the sill.

**Check:** Scrub motion: the wick must not drift and color bands must not swim. Compare emission alone with point light enabled; if the flame turns white, reduce emission before changing the color ramp.

#### Blender 2.8 Transparent Material Eevee - Alpha Transparency

Video · Narration.[190]

**Evidence:** English narration in direct watch-page extract; no video frames inspected. **Locator:** 0:01 (transcript block start)

**Observed:** The presenter compares an older shader mix to the then-new Principled Alpha input; setting alpha to zero and one tests the endpoints, then image alpha cuts out individual hair cards.[190]

**Try:** Separate the mask feeding the shader from material-level transparency handling; the cited Eevee Blend Mode UI is from Blender 2.8.

**Check:** Test fully opaque and fully transparent first; if only some hair cards remain rectangular, inspect their individual materials.

#### Fix A-Pose to T-Pose Fast (Genesis 8/9 → Blender | Diffeomorphic)

Short · Sampled frames.[177]

**Evidence:** Visually inspected timestamped YouTube player storyboard samples, not continuous playback. Creator-written chapters read on public watch page; chapter starts are signposts, not frame times. **Locator:** frames 00:27, 00:45, 01:12, 01:39

**Observed:** The rig overlay shows both arms angled down at 00:27. At 00:45 one arm is horizontal; at 01:12 both are out, with a whole-body front view at 01:39. The description names Diffeomorphic pose tools, but its short chapter timing does not line up with the sampled demonstration.[177]

**Try:** Normalize a licensed original passenger rig’s reference pose on a duplicate before retargeting motion. Separate changing a pose from changing its rest state.

**Check:** Compare shoulder width, elbow axis, garment deformation and an existing action before and after; reject if the old action shifts unexpectedly.

### Sources

[163] https://www.youtube.com/watch?v=ShtmS-qNZrY — Stylized Candle Flame in Blender – No Fire Simulation!
[177] https://www.youtube.com/shorts/9tgcNfJegtE — Fix A-Pose to T-Pose Fast (Genesis 8/9 → Blender | Diffeomorphic)
[190] https://www.youtube.com/watch?v=KlWiqrk2-o4 — Blender 2.8 Transparent Material Eevee - Alpha Transparency
[247] https://w3productions.com/how-to-create-a-stylized-candle-flame-in-blender — W3 Productions: Stylized Candle Flame — written companion

<a name="chapter-creator-yng3d"></a>

## @YNG3D — source notes

27 public Videos entries; 68 Shorts; 4 individually noted.

[All creators and coverage](channel-register.md) · [Apply a lesson to the tram](channel-workshop.md). Evidence and proposed exercises are distinguished below.

#### 1 Hour Focus on Sculpt With Me: Chill & Relax Music | Slow Living As A 3D Artist (Ep2)

Video · Sampled frames.[236]

**Evidence:** Public YouTube player storyboard, visually inspected at labelled sample times; no narration used. **Locator:** 08:20; 16:20; 41:40; 51:40

**Observed:** A stylus works below a large circular form on an ornamental creature head at 08:20. The pulled-back view at 16:20 shows the branching silhouette; the closer 41:40 and 51:40 views show long raised contours and shorter nested ridges. Not a from-scratch blockout or a demonstrated Blender brush preset.[236]

**Try:** On a decorative mask, define a few long ridges before cutting secondary grooves; switch between detail and whole-head views.

**Check:** At icon size the main brow must still read without the smaller marks.

#### How to Sculpt Reze Head & Face in ZBrush | Chainsaw Man 3D Fan Art

Video · Sampled frames.[175]

**Evidence:** Public YouTube player storyboard, visually inspected at labelled sample times; no narration used. **Locator:** 00:04; 00:08; 00:12; 00:16

**Observed:** The pale bald head gains front locks crossing one eye, then a complete uncolored bob, then purple hair. A compressed ZBrush progression, not brush-by-brush instruction.[175]

**Try:** Design front locks as masses against the face before assigning hair color.

**Check:** The eye line and part remain identifiable in neutral clay.

#### Mix volumetric and lighting color to the best fog in cyberpunk city blender Tutorial

Video · Description / chapters.[164]

**Evidence:** Creator description only; no footage or usable transcript in the extract.

**Observed:** The description names fog color and illumination in a Blender city shot, but does not specify the shader, node order or density.[164]

**Try:** Use it as a visual lead only. For a separate exercise compare an unchanged bounded fog volume with a warm and a cool lamp.

**Check:** Do not credit any specific volume-node settings to this source. A valid comparison holds the camera, exposure and medium fixed.

#### Miku Hatsune - 3D Sculpting Process in ZBrush 🎨🎮Part 1 - head

Short · Sampled frames.[225]

**Evidence:** Public YouTube player storyboard, visually inspected at labelled sample times; no narration used. **Locator:** 00:12; 00:18; 00:24; 00:30; 00:36

**Observed:** A colored face without hair precedes the turquoise fringe; a back view shows grooves in the cap; long tail forms appear before the final paired-tail front view.[225]

**Try:** Block fringe, cap and tails separately on a stylized bust; inspect from behind as well as the front.

**Check:** Turn the bust through a full rotation; no scalp holes or tails apparently floating off the cap.

### Sources

[164] https://www.youtube.com/watch?v=Dgika_gEW0U — Mix volumetric and lighting color to the best fog in cyberpunk city blender Tutorial
[175] https://www.youtube.com/watch?v=97l111y1tDg — How to Sculpt Reze Head & Face in ZBrush | Chainsaw Man 3D Fan Art
[225] https://www.youtube.com/shorts/hWA-cnCAirE — Miku Hatsune - 3D Sculpting Process in ZBrush 🎨🎮Part 1 - head
[236] https://www.youtube.com/watch?v=oel9qygcnc0 — 1 Hour Focus on Sculpt With Me: Chill & Relax Music | Slow Living As A 3D Artist (Ep2)
