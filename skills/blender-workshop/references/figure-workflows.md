# Anatomy, rigging and contact

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [Functional anatomy: build the adult figure from the support up](#chapter-human-anatomy)
- [Characters: build the person before the costume](#chapter-character-contact)
- [Adult figure studies: stage contact, then add the effects](#chapter-adult-figure-staging)
- [Figure studies: blocking, retargeting, condensation and light](#chapter-figure-source-map)

<a name="chapter-human-anatomy"></a>

## Functional anatomy: build the adult figure from the support up

**Author: Noa3 · Blender 4.5.9 LTS.** The practical directions below are workshop proposals, not a tested scene or a prescription for how an individual must move. Start with three marks in your reference: where the body bears weight, where a bone is close enough to the surface to track, and where soft tissue changes shape. A trouser crease can help with the last mark; it is a poor substitute for the first two.

### Measure the person, not the drawing convention

Here is one *bounded* reference population. ANSUR II measured US Army personnel (active duty, Reserve and National Guard) in October 2010–April 2012; the public working databases are stratified subsets, not a random sample of civilians. [429] The table below is an independent calculation on those public files, not a transcription of the report's tables. Keep records where `Age >= 18`: 1,985 women and 4,081 men, ages 18–58 in each group. Within each file, sort the measured millimetre field, take inclusive linearly interpolated percentiles, convert to centimetres and round to one decimal. Use `stature`, not `Heightin`. [429]

| Measurement in cm | Women: P5 / median / P95 | Men: P5 / median / P95 |
|---|---:|---:|
| Standing stature [429] | 152.5 / 162.6 / 174.0 | 164.8 / 175.5 / 187.0 |
| Sitting height [429] | 80.3 / 85.7 / 91.2 | 86.0 / 91.8 / 97.7 |
| Horizontal arm span [429] | 152.9 / 165.7 / 180.3 | 168.0 / 181.2 / 195.7 |
| Seated overhead fingertip reach [429] | 120.7 / 130.9 / 141.3 | 131.6 / 142.6 / 154.0 |

A 170 cm figure lies inside **both** middle-90% stature intervals. Among the 24 men in the adult file measured at exactly 170.0 cm tall, sitting height ran from 82.5 to 95.2 cm. Those are observed extremes in a small subgroup, not design limits. [429] Even at a given stature the other rows are not lookup values: a median arm span and median sitting height need not belong to the same person. A percentile is a rank within a specified group, not a proportion of a body. Neither sex presets nor an all-95th-percentile character follow from these numbers. Age also belongs on the sheet: this sample has no one over 58. Comparing different age groups in a single survey cannot tell you how one person's skeleton or posture will change over time. For an older character, collect age- and task-matched reference rather than bending the back of a median soldier. [429]

**Reproduce the measurements on the character.** Make a separate measurement pose, without shoes, hair volume or the scene's expressive slouch. Record distances and pose together; a fingertip coordinate without a shoulder pose is not a reach specification.

- **Stature:** floor to crown (vertex), not sole-object origin to hair tips. Orient the head using the handbook's horizontal line from right tragion at the ear to right orbitale at the lower orbital rim; do not level the nose. [430]
- **Sitting height:** level seat surface to vertex with the figure sitting erect. Do not include the seat height. Stature minus sitting height is a useful *vertical difference*, not femur length. Compare seated eye line separately when matching a car or desk. [430]
- **Span:** tip to tip of the middle fingers, arms extended horizontally against the wall, palms facing out. This includes shoulder breadth and both hands. Do not force it to equal height. [430]
- **Overhead reach:** in the seated protocol measure vertically from the seat to the right middle fingertip with the arm overhead; do not cheat the distance by leaning the torso. A reachable *grip* is another problem: pose the hand around the actual rail and check the thumb, not just the longest fingertip. [430]

**Two casting tests.** Give two figures the same standing crown height. For the first, transfer more of that height into the legs; for the second, into the seated trunk. Put them on the same bench: the seat-to-crown distances should now differ even if their standing silhouettes framed alike. Next keep the first figure's skeleton unchanged but change its abdominal and thigh padding. Sit it again. Solve the contact and hand clearance anew rather than spreading the hip sockets to correct a surface collision. These are deliberately invented contrasts, not reconstructions of survey participants.

### From a surface mark to a working joint

Mark the same points in front, profile and rear three-quarter views. Place small temporary empties at the surface landmarks and a differently named set at estimated internal pivots. Rotate one segment a little: **which mark should move with it?** If the elbow point stays on the upper arm when the forearm bends, a beautifully shaded elbow still fails this test.

**Axial skeleton.** The mobile column has seven cervical, twelve thoracic and five lumbar vertebrae above the sacrum and coccyx. In profile the neck and lower back curve in the opposite direction to the thoracic and sacral regions. [431] Block a pelvis with a sacral back plane, a rib cage with a sternum plane and a head with a jaw plane. Connect the three; do not begin with a smooth tube. Draw a line across the front points of the iliac crests (ASIS), and locate the ischial tuberosities underneath, where a seated pelvis meets its support. [432] For a hip hinge, turn the pelvic block over the thighs and carry the rib cage with it. For a curl toward the belt, change the rib-to-pelvis angle and distribute the bend up the intervening chain. Compare the distance from sternum to belt in the two profiles. If both actions make the same notch at the navel, change the allocation of rotation before sculpting a fold.

**Shoulder.** Trace sternum → clavicle → acromion. The acromion belongs to the scapula and makes the bony shoulder tip; the upper-arm ball sits in the scapula's glenoid, not in that tip or the outer deltoid contour. [433][434] Put the upper-arm pivot inside the cap. Give the girdle its own control: test reaching forward, drawing the elbow back, and reaching up. Forward reach should allow scapular protraction, not just arm rotation. [435] Upward rotation of the scapula and elevation of the humerus are coupled, but not by a universal gear ratio: a study of 13 healthy subjects found that the relative contributions changed across increments of scapular-plane elevation. Its whole-arc result is not a setting to enter on every rig. [436] Track the back edge of the shoulder blade and the shoulder tip while scrubbing. Let the blade turn and travel around the rib cage, then aim the humerus relative to that moving socket. Contrast an overhead shelf reach with a forward wall press at shoulder level: copying the same shrug into both brings the neck into the action for the wrong reason.

**Elbow, forearm, hand.** The elbow hinge involves the humerus and ulna; the projecting olecranon is part of the ulna. [434][437] Put the hinge through the elbow, not on its rear tip. In forearm pronation the distal radius crosses the ulna; in supination the bones return to a parallel arrangement. The direction the palm faces in world space also depends on the shoulder pose. [435] Bend the elbow, keep the upper arm still and turn a key in a lock. Track the thumb side from wrist toward elbow: spread the twist through the forearm rather than wringing a single ring of wrist vertices. Then test the same key-turn with an extended elbow. A twist solution that works only because the elbow is bent is not ready for the shot.

Opposition brings thumb tip toward fingertip at the thumb's base joint, not by bending the thumb tip alone. [435] Give the thumb a base inside the palm. For a mug, build the finger arcs around the handle and leave a credible thumb counter-contact. For a flat palm on glass, uncurl the digits separately and check pads against the plane. The same hand should read without a glove seam serving as the knuckle line.

**Hip and knee.** The femoral head meets the acetabulum inside the hip; the palpable greater trochanter is a lateral projection, not that ball's centre. [434][438] In a leg-lift test the lateral marker should travel with the thigh, while the anterior crest markers travel with the pelvis. Check from above as well as from the front. The knee is a modified hinge: the femoral condyles roll and glide on the tibia, and the patella lies in the quadriceps tendon anterior to them. [434][434] Approximate the bend axis between the condyles, behind the patella. In a deep squat keep the anterior knee readable as the shin and thigh approach. If the thigh seems to lengthen or the knee opens like a hinged box, inspect the axis and length first. Add a local tracking helper or corrective for the anterior contour only if the two long segments already track.

**Ankle and foot.** At the ankle the talus meets the distal tibia and fibula; use the malleoli as external guides to a pivot *between* them. Dorsiflexion brings the top of the foot toward the shin; plantar flexion points it away. Inversion and eversion involve joints within the hindfoot rather than simple rotation at the talocrural hinge. [434][435] Build separate controls for ankle pitch, heel lift around the forefoot and toe bend at the metatarsal heads. Trace heel, first and fifth metatarsal heads and the inside arch. The foot has medial and lateral longitudinal arches as well as a transverse arch. [439] Do not carve an identical inside arch on the outer edge or force the entire sole to touch a plane. For a boot, test the outsole against the ground and the ankle within the boot: a planted shoe can still conceal a detached leg.

**Face close-up.** The zygomatic arch runs from the cheek toward the area above the ear canal; jaw opening combines hinge and glide at the temporomandibular joint. [440][434] Use cheek arch, orbital rims, chin and jaw angles to establish the hard planes before sculpting expression. Seat lids around the globes and test closure. Open the mouth once barely and once widely; inspect the chin path and lower teeth against the skull from profile. If the lower incisors sweep an enormous arc while the cheek caves in, revisit the jaw pivot and its forward travel before painting a dark mouth corner.

### Muscle is an action; skin is a surface

A concentric action shortens a muscle under load; during an eccentric action it lengthens under tension; an isometric action can produce tension without changing joint angle. A biceps curl and its controlled lowering demonstrate why moving down is not the same as switching the flexors off. [441] Compare three takes with the same mug: lift, arrest halfway, lower slowly. Key the hand path first; give the elbow flexor mass a different effort in the hold than in an unloaded arm hanging at that angle. A bend angle can drive a crease; it cannot by itself tell you the weight of the mug.

Quadriceps extend the knee and the hamstring group flexes it; the posterior lower-leg compartment contributes plantar flexion. [442][442] Compare rising from a chair to lowering into it: in the controlled descent the knee can flex under load while the extensors brake it. Do not inflate the back of the thigh just because the knee is flexed. Compare that shape with a free heel drawn toward the seat against resistance. For a close calf, distinguish the mass above from the narrowing down toward the heel instead of scaling the entire shin to signal effort.

Deep fascia surrounds musculoskeletal structures; connective-tissue sheaths also organize muscle itself. They are not a second outline to emboss around every belly. [443][444] The hypodermis contains cushioning adipose and loose connective tissue; subcutaneous fat commonly collects around hips, buttocks, thighs and abdomen. The palms and soles have specialized thick skin. [445][446][445] Model the *specific distribution*, not a global surface offset. Compare an exposed bony elbow with a padded seat contact on the same figure. Trace which landmarks remain legible in both; soften transitions over the padded regions rather than erasing the underlying joint. Include thickness in profile as well as breadth in front view.

**Contact study:** put a forearm on a hard table, then on a soft cushion. On the table, flatten just the bearing patch, ease adjacent tissue out of its way and preserve the distant silhouette. On the cushion share the displacement between arm and prop and show the trough relaxing after release. Inspect a slice perpendicular to the support: a black contact shadow is not proof the surfaces meet. Do not trigger this deformation from elbow flexion alone; a bent arm held in air should not acquire a flat underside. Use an animator-controlled contact value when the load or support is not encoded in the skeleton.

### Bind the mesh so the diagnosis stays readable

1. **Fit rest geometry and axes.** On a copy, place pelvis, thigh, shin, foot, upper arm and forearm bones; add separate controls for scapula, limb twist and foot roll only where they solve a visible action. Use local axes consistently on the two sides and keep control bones nondeforming. Before painting, rotate each deform bone in isolation. An unexpected plane of movement is not a skinning defect.
2. **Place rows where the surface changes direction.** At the elbow, route one band across the bend and reserve rows on either side; leave room on the inner arm for the rows to gather. At the shoulder, run edges out of chest and back into the upper arm rather than circling the armhole with a dense, isolated cuff. Put topology junctions away from the armpit's deepest fold. Test the low-resolution cage first; subdivision can hide an edge without fixing the path its vertices take.
3. **Paint by ownership, then blend.** With Armature modifier vertex groups, bone names identify the mesh groups they affect. Preserve Volume changes how rotation is blended; it does not infer where a shoulder blade belongs. [447][447] Assign the olecranon area primarily to forearm, protect the chest from arm twist, and taper influences across the hinge instead of smoothing the whole limb. Inspect one group at a time, normalize the intended deform groups, and test for wrong-side or unweighted islands. Compare Preserve Volume on/off at the *same* twisted pose before adding geometry.
4. **Correct the residual, not the whole pose.** Suppose the hinge tracks but a flexed elbow loses its tip. Add a Basis and a relative key named `ElbowFlex.L`; relative shapes are defined against the Basis or another specified key. [18] Keep topology and vertex order unchanged. With the armature still evaluating, edit the active key's small local patch with the deformed edit cage visible where supported. Restore the missing tip and ease the inside fold; do not copy the already-posed whole arm into a pre-armature shape key or it will bend twice. If cage editing is ambiguous, make a small rest-space edit first and observe its direction in the pose. Return to neutral and set the key to zero. Preview manually at zero, halfway and full bend before attaching a driver to the intended local bend axis. If it fires while twisting a straight forearm, filter the rotation channel; if it fixes only one extreme and pops in transition, soften the response or make an intermediate target.

### Walk and support: stage the transfer, not two foot poses

Stance and swing are phases of one limb. In an ordinary heel-first walk the loaded foot progresses through heel, ankle and forefoot rockers: first the foot lowers, then the body advances over it, then the heel lifts for departure. A walking cycle includes double support as weight passes between feet. [439][448] For a shot, mark where each heel and forefoot actually bears weight on the world floor. At first contact pin the relevant heel patch, not the entire foot bone. In midstance let the shin advance over the lower foot. At departure keep the bearing forefoot patch steady while allowing the heel to travel. Release that final patch before swinging the leg. Do not set an unvarying percentage of frames from a textbook: use the actor's pace and the surface in the shot.

**Contrast a cautious step with a brisk one.** In the cautious take, give the incoming foot time to accept weight before the other leaves. In the brisk take, let the trunk continue forward across the exchange. Review frame by frame from the side with ground markers; then watch at speed without them. If the body stalls every time the feet overlap, move the pelvis through the handoff instead of fixing it to the midpoint. If a planted foot slides, check root motion and foot target parenting before adding a compensating ankle key.

**Contrast standing with sitting.** A still figure holding a rail may use feet and hand as supports; a seated figure may use seat and thighs as well as feet. Identify which support would change the pose if removed. For a chair rise, play pelvis and trunk forward while the seat still bears weight, release the seat, then finish the rise over the feet. If the seat unloads while the feet are still reaching for the floor, change the starting foot placement or seat height, not the facial expression.

**Shot acceptance.** Scrub entry, maximum load and release in a plain clay view, from the final camera and one view across its sightline. At each stage ask: does the support patch meet its surface; does the *right bone* carry the observed landmark; does the silhouette retain the person's proportions; and does the fold disappear when its cause is gone? Fix in that order: contact and pose → pivot and segment lengths → weights and topology → residual corrective → shading. Keep the smallest before/after crop that shows what the fix changed.

### Sources

[18] https://docs.blender.org/manual/en/4.5/animation/shape_keys/introduction.html — Introduction - Blender 4.5 LTS Manual
[429] https://mreed.umtri.umich.edu/mreed/downloads/anthro/ANSUR2Distribution.zip — 2012 Anthropometric Survey of U.S. Army Personnel: Methods and Summary Statistics; ANSUR II public working databases (University of Michigan distribution)
[430] https://mreed.umtri.umich.edu/Anthro/ANSUR%20II%20Measurement%20Definitions.pdf — Measurer’s Handbook: US Army and Marine Corps Anthropometric Surveys, 2010–2011
[431] https://pressbooks-dev.oer.hawaii.edu/anatomyandphysiology/chapter/the-vertebral-column — The Vertebral Column – Anatomy & Physiology
[432] https://pressbooks-dev.oer.hawaii.edu/anatomyandphysiology/chapter/the-pelvic-girdle-and-pelvis — The Pelvic Girdle and Pelvis – Anatomy & Physiology
[433] https://pressbooks-dev.oer.hawaii.edu/anatomyandphysiology/chapter/the-pectoral-girdle — The Pectoral Girdle – Anatomy & Physiology
[434] https://pressbooks-dev.oer.hawaii.edu/anatomyandphysiology/chapter/anatomy-of-selected-synovial-joints — Anatomy of Selected Synovial Joints – Anatomy & Physiology
[435] https://pressbooks-dev.oer.hawaii.edu/anatomyandphysiology/chapter/types-of-body-movements — Types of Body Movements – Anatomy & Physiology
[436] https://pmc.ncbi.nlm.nih.gov/articles/PMC3377910 — Assessment of scapulohumeral rhythm for scapular plane shoulder elevation using a modified digital inclinometer
[437] https://pressbooks-dev.oer.hawaii.edu/anatomyandphysiology/chapter/bones-of-the-upper-limb — Bones of the Upper Limb – Anatomy & Physiology
[438] https://pressbooks-dev.oer.hawaii.edu/anatomyandphysiology/chapter/bones-of-the-lower-limb — Bones of the Lower Limb – Anatomy & Physiology
[439] https://www.ncbi.nlm.nih.gov/books/NBK587361 — Anatomy, Bony Pelvis and Lower Limb: Arches of the Foot
[440] https://pressbooks-dev.oer.hawaii.edu/anatomyandphysiology/chapter/the-skull — The Skull – Anatomy & Physiology
[441] https://pressbooks-dev.oer.hawaii.edu/anatomyandphysiology/chapter/nervous-system-control-of-muscle-tension — Nervous System Control of Muscle Tension – Anatomy & Physiology
[442] https://pressbooks-dev.oer.hawaii.edu/anatomyandphysiology/chapter/appendicular-muscles-of-the-pelvic-girdle-and-lower-limbs — Appendicular Muscles of the Pelvic Girdle and Lower Limbs – Anatomy & Physiology
[443] https://my.clevelandclinic.org/health/body/23251-fascia — Fascia Tissue Function
[444] https://pressbooks-dev.oer.hawaii.edu/anatomyandphysiology/chapter/skeletal-muscle — Skeletal Muscle – Anatomy & Physiology
[445] https://pressbooks-dev.oer.hawaii.edu/anatomyandphysiology/chapter/layers-of-the-skin — Layers of the Skin – Anatomy & Physiology
[446] https://my.clevelandclinic.org/health/body/23968-subcutaneous-fat — Subcutaneous Fat: What You Need to Know About the Fat Beneath Your Skin
[447] https://docs.blender.org/manual/en/4.5/modeling/modifiers/deform/armature.html — Armature Modifier - Blender 4.5 LTS Manual
[448] https://www.ncbi.nlm.nih.gov/books/NBK557684 — Forensic Gait Analysis

<a name="chapter-character-contact"></a>

## Characters: build the person before the costume

**Author: Noa3.** Start with the shot. A commuter waiting on a platform has to convince us that they have weight, even when their face occupies only a few pixels. Choose a specific action: waiting while watching the tram, for instance. Get a front, side and three-quarter reference for that action (your own photos or licensed references); match the eye level and approximate focal length. Keep the unlit silhouette alongside the reference. Bigger skin textures cannot fix a backward knee.

### From reference to a body that can bend

For two interacting adult figures, open [the fingertip-contact and atelier study](figure-workflows.md#chapter-adult-figure-staging). It checks both participants, the particular two digits and the frames between poses. A foot standing still by itself does not establish the partner's contact.

1. **Block the support and gesture.** Mark the floor, supporting heel and ball, ankles, kneecaps, hip sockets, pelvic tilt, base of the neck and head angle. Draw the line of action through the rib cage and pelvis. For an ordinary still stance, can you tell which foot carries more weight? For a moving pose judge the momentum into and out of the pose instead of requiring the center of mass always to be over one foot.
2. **Sculpt large masses from two directions.** Lay in rib cage and pelvis separately with space for the waist. Check the side profile of glute, thigh, patella, calf and Achilles. The hinge is not at the visible front of the patella. Place the widest portions of thigh and calf from reference rather than tapering each bone symmetrically. Shape the shoe last over a blocked-in foot; its outsole, not its object origin, meets the floor. Mirror the neutral form if useful, not the weight-bearing pose. Review a neutral clay turntable before folds, hair or accessories.
3. **Decide where the mesh must deform.** Draw loops around eyelids and mouth according to closure; put spare rows both above and below the knee and elbow. Place poles away from the primary fold. Retopologize one bend first, not the entire body at once. Test an open hand, a fist, a bent knee and a seated hip. If the inside knee pinches to a point and the outside collapses, inspect edge spacing and weights before subdividing. Keep a neutral source mesh and the same vertex order for corrective shapes.[18]
4. **Fit clothes to the posed volume.** Establish waistband, crotch depth, shoulder seams, elbows and hem against the underlying body. Pull fabric tight at tension points; compress it on the inside of a bend. Check the gap between the thighs, a coat crossing a shin, a sole penetrating a platform, and a hand apparently cut off by a cuff. Review in silhouette, side view and final camera. Don't use a coat or camera crop to excuse an unverified pair of legs.
5. **Only build face and groom detail that survives the shot.** Seat eyeballs in the sockets; wrap lids around the globes and check full closure without globe penetration. Test a blink, lip seal and a voiced-to-closed-mouth transition. Look for eye direction in both eyes before adding corneal highlights. Establish asymmetric hair masses in silhouette before adding guide clumps and flyaways. Test skin under a large neutral light and a raking light; painted highlights or excessive subsurface scatter turn when the light should. Specific pore scale, skin color and facial proportions need subject reference, not a fixed material preset.

Blender Studio describes animator feedback on anatomy and appeal **during** construction of its Rain character, and a sequence from exploratory sculpt and facial poses to mesh, shading and lighting. Rain is a stylized production example, not a scanned human or a photorealism benchmark.[314]

### Bind, diagnose, correct

- Put deform bones at the intended joint centers in rest pose and mirror bone roll deliberately. Keep IK targets, poles and other controls out of deform groups. For a simple planted leg, use a two-link IK chain ending at the ankle; give the knee a small initial bend or an explicit pole. Test a squat in front **and** profile: a flat or reversed chain can choose the wrong side. Separate foot roll for heel lift from ankle translation.
- Make gross assignments first; inspect individual deform groups around thigh, shin, pelvis and opposite leg. Pose the joint to see what each group pulls. Normalize **deforming** influences, check for unweighted vertices and wrong-side contamination; protect intentional locked groups. Blender's Normalize All respects locked groups and its subset setting matters.[313] A sum of one means a complete assignment, not the right assignment. A boot weighted entirely to the opposite ankle can pass a numerical sum check.
- Bend through rest, intermediate and deep flexion; compare the kneecap from the front, calf volume from the side, and inner-leg clearance from below. If weights alone cannot preserve a specific crease or bulge, sculpt a corrective against the posed error and drive it by the intended local bend. Check the half-pose and zero pose as well as the target. Shape keys are a native tool for facial targets and local refinement; they are not a substitute for locating the joint correctly.[18]
- For animation: block contact, load, pass, release. Plot heel and ball paths in world space. Hold the planted contact, not an entire rigid foot through its roll. Remove root/foot double motion before polishing hands and head. Check real-time playback, slow playback and the side view. Return to [clip timing and retargeting](motion.md#chapter-animation-workflow) for mismatch at clip boundaries.

### Tested exercise: make a foot fail on purpose

In the original lower-body cutaway, compare the rest and bent poses as the pelvis bridge lowers. On your own posed figure, track a landmark on each sole relative to the floor rather than reading only the controller location.

Readback on the reopened file: 25 frames; pelvis lowered 0.145 m; worst shin-to-ankle gap under 0.06 mm; sole drift under 0.001 mm. Muting left IK opened a gap of about 0.153 m. Separate mesh bands and simplified shoes isolate the mechanism; these figures do **not** measure anatomical accuracy or convincing performance. Rebuild in a fresh directory with the study script (historical tool, not included) using `build`, then `check` in another process. The two camera proofs and `support-check.json` sit beside the native file.

**Stop rule for a person in a finished image:** check a crop at delivery resolution, not just the overall composition. Can another reader point out the pelvis, supporting knee and bearing foot? Does a seated figure load the seat rather than hover over it? If not, return to the pose or framing. Do not mark the character approved on the strength of a rig test.

**Lumen Quay, a worked correction.** Trace the clock dial to its brass pin and green mast in the README preview. For a seated figure, follow each thigh around its own knee to its boot, then inspect the weight-bearing contact between the seat and the figure in a side view of your own model.

### Sources

[18] https://docs.blender.org/manual/en/4.5/animation/shape_keys/introduction.html — Introduction - Blender 4.5 LTS Manual
[313] https://docs.blender.org/manual/en/4.5/sculpt_paint/weight_paint/editing.html — Editing Weight Paint · Blender Manual 4.5
[314] https://studio.blender.org/blog/introducing-rain — Introducing: Rain – Blog — Blender Studio

<a name="chapter-adult-figure-staging"></a>

## Adult figure studies: stage contact, then add the effects

**By Noa3.** Use this route for a life drawing or classical nude, a draped figure, dancers, an embrace, or an intimate scene between fictional adults. Nudity is a costume decision, not a pose or a genre. Establish what the people are doing and how the audience should read it. A scene can be tender, tense or matter-of-fact without changing the mesh.

### From a brief to a readable shot

1. **Write one sentence with a visible verb.** “Two adult dancers test their distance by touching index fingertips, then lower their hands” is actionable. Decide the exact contact surface, who initiates and who responds. Decide separately whether the deliverable is a still or a timed shot, how much anatomy is shown and which view matters. Ask only if the answer changes the work. Use fictional adults or age-confirmed, consenting adult references. With a real performer, agree separately on recording, likeness, intended pose, use and sharing. A model license is not a person's release. Do not upload private reference or motion capture to a service by default; keep it out of public handoffs and previews.
2. **Build the set to the people.** Put the support surfaces at measured heights; fix the camera and put down the heel, ball, seat or other load points before dressing the room. Block the rib cage and pelvis as distinct masses. In a standing pair, stagger the feet and soften the knees to suit the reach. In an embrace, decide which arm passes in front, where a palm meets a shoulder, and what the pelvis and rib cage do in response. Check the camera silhouette, a reverse view and one view along the contact normal. Darkness or depth of field must not be the only thing keeping limbs apart.
3. **Give each contact a time and an owner.** Block apart → first touch → hold or slide → release. In a handclasp only one rig should own a shared target; do not parent the hands to one another. An IK target can keep a wrist steady, but bone origin, wrist, fingertip and garment surface are different places.[26] Put an elbow pole on the intended side, avoid a dead-straight chain, then inspect the *deformed surfaces*. In a kiss or cheek contact, stage the head tilt, nose clearance and chin/shoulder overlap before adding expression. If bodies float apart in profile, repair spacing or the contact shape; changing the lens only hides it.
4. **Fix deformation locally.** Check shoulder volume under a raised arm, the inner elbow at half-bend, the waist beside the pelvis, and the back of a flexed knee. First inspect the actual deform groups and their neighbors; normalization alone cannot fix a wrong assignment.[313] For a pressure mark, add a local corrective shape keyed only over the loaded interval; test both released and half-loaded states.[18] For drapery, keep the animated body, a simple collision proxy, and the visible cloth separate. For a driven patch, bind Surface Deform in a matching rest state; changing target topology calls for a new bind.[348] Verify the seam and an unpinned point, not just the attractive side of the mesh. None of these mechanisms automatically gives realistic flesh or a complete costume.
5. **Evaluate the scene in layers.** First clay and contact at the final camera size. Next face, gaze, skin and fabric under a broad neutral light and a moving rim. Skin color should not carry a fixed specular highlight; verify where a highlight travels before adding pores. Last, enable wetness, fog, hair and loose elements one at a time. Watch a normal-speed preview and step consecutive frames near contact. Look at the feet and fingertips again with every effect on. Save the baseline so a later artist can isolate a bad pass.

### Worked example: Between Beats

**Historical case study, not a download.** Recreate the contact test with two simple figures in your own scene; the native files and base meshes are not supplied.

In the original Blender 4.5 study, two fictional adult casts touched index fingers. Frame 18 was the held contact, with separate contact and reverse cameras. The terracotta and celadon surfaces were deliberately stylized; the exercise tests geometry and timing, not skin realism.

| Question | Try it on a copy | What the Blender 4.5.9 readback established |
|---|---|---|
| Do the intended fingertips meet? | At 18, switch from `01 | Atelier` to `03 | Contact detail`. Move `Celadon | Rig` **+0.12 m in world X**. | On frames 14–22 the closest sampled vertex-to-opposite-surface distance between the two distal index regions was about **0.30 mm**, with no intersecting faces in the selected reaching hands on any of the 36 whole frames. Moving the partner opened the fingertip gap to **120.3 mm**. This is near-contact, not pressure simulation. |
| Do the feet stay on the floor? | Look for four separate soles, then follow each ankle back to its own knee. | Four sole regions were checked independently against the nominal tile-top plane; their vertex positions did not drift across the shot. This measures placement, not body weight or ground reaction force. |
| Can two correct key poses conceal a bad in-between? | Watch the arm during the **approach**, not just on the hold. When generating quaternion keys, choose the sign nearest the preceding rotation **before** inserting each key. Recheck the skinned finger path afterward. | An earlier build passed the held-contact test while a fingertip-region center jumped **458 mm in one frame**. After sign continuity was fixed, its worst step across either hand was **34.3 mm**. Changing the charm's damping would have treated the symptom. |
| Is the pendant attached, rigid or lagging? | Scrub 14–22. Watch the gold mount and teal drop separately. On a copy, unlink the `Charm | Swing` action and set its Y rotation to zero. | The mount was stationary through the hold, but the drop continued to move. Its largest sideways offset was **22.1 mm** (frame 15), versus zero with angular motion removed. The chain length stayed fixed. The motion is a **baked, single-plane damped pendulum** driven from the wrist path; re-time the wrist and it needs rebaking or rekeying. No live soft-body or cloth solver is hidden here. |
| Is the floor wet or is the light simply brighter? | In `Basalt | damp polish`, change only the **Wetness** Value from 1 to 0. Compare `Floor-Damp.png` with `Floor-Dry.png` near the foreground grout and feet. | Two matched Cycles renders use the same camera, light, exposure, frame and seed. The damp state locally sharpens reflections by changing roughness, not by darkening the base color. There are no simulated raindrops in this scene. |

The native file contains both editable rigs, geometry, keyframes, cameras, floor mask and lights; it requires no add-on or external image. Both figures use the same **CC0 MakeHuman body mesh**.[344]

The skeleton and skin weights also come from MakeHuman.[345][346] The builder selects the body faces, discards helpers, normalizes incoming deform weights and fits the figures to two scales. These are not two people sculpted from scratch.

The original exercise used separately licensed source data.[350] Workshop staging, motion and teaching by Noa3.

The independent check reopened the original scene with embedded scripts disabled, evaluated all 36 frames and left both deliberate breakages unsaved. Repeat that method on your own disposable copy.

### Test a pressure-and-release shot

For the reference clips, timing observations and a no-jitter review procedure, use [anime follow-through: weight without the jelly tremor](motion.md#chapter-secondary-motion-direction).

**Stylized follow-through:** “jelly” or *Wackelpudding* means that the mass gives and follows through, not that the surface should tremble like literal gelatin. The anime side of *Pressure & Release* had too much small, repeated shake. Keep it as a technical comparison, **not an approved aesthetic preset**. Start with a single broad follow-through, at most a restrained secondary return if it reads better, then a quiet hold. Do not add procedural noise or a wiggling vertex layer as a substitute for weight. Count reversals after the support stops; first watch the silhouette at playback speed, then check a tracked seam relative to the torso. If the outline is still but the highlight crawls, inspect shader/denoiser flicker before changing the spring. These are art-direction starting points, not universal counts, times or tissue constants.

Use the same probe path, scale, supports and camera on both sides of a naturalistic/stylized comparison. Change the return dynamics, not the depth of the stylized probe. A cel shader is a separate choice. Describe a bonded clothing shell as bonded; it cannot demonstrate fabric slipping over skin.

Do not accept a soft-body poke because the collision **nodes** clear the sphere or the total volume looks stable. Check signed local cell volumes as well. After baking, reopen the file and find the closest point on the **rendered garment triangles and raised binding** on every delivered frame. A sphere can cut through the space between perfectly nonpenetrating nodes. In that case project intermediate patch samples, converge the last contact pass, then repeat the mesh-surface test without loosening its tolerances. As a negative control, disable the shell animation on a disposable copy while keeping the same stroke: the checker should detect the rigid-shell intersection.

For a displacement graph, cast a ray along the fixed actuator axis and subtract its rest reading. Track a material point separately: that point can slide sideways out of the loaded region, so its motion and the indentation beneath the probe need not match. Compare the first *free* outward peak, the final residual and a no-input control. Distinguish a custom bake from a native Soft Body modifier, and a plausibly damped artistic response from measured human tissue.

### Transfer it to a more complex scene

- **Two adults in a narrow doorway, one helping the other up:** mark the last frame loaded on the seat and the first loaded on the foot. Choose the hand that transmits weight. Check the supporting forearm and shoulder from behind, then have someone identify who is supporting whom from the clay preview. This is a proposed next shot, not a verified lift.
- **Cloth and soft secondary motion:** keep a rigid control copy. Drive one attachment first (the working cuff is an example); compare amplitude, phase, clearance and settling. For soft tissue use a small local cage or a corrective driven by a pose, with the surrounding area anchored. For a skirt or towel use a simplified body collider; confirm that its pins follow the performer at the shot's frame rate. Do not confuse a delayed rotation, a deforming surface, and a colliding simulation. For a worked delivery test see [the relocated cloth bake](motion.md#chapter-cloth-cache-handoff).
- **Wet skin, glass or floor:** put the wet boundary where water arrives or drains. Check a roughness-only mask beneath a fixed reflected card first; add raised beads or streaks only if the camera can resolve them. Keep moving droplets separate from the resting film and from splashes. A real example of curve-based condensation and its limits is in the [source map](figure-workflows.md#chapter-figure-source-map).[351] The [rain and wear lab](materials.md#chapter-wear-and-finishing) measures particle fall; it is not a shot of rain colliding with a person.
- **Atmosphere:** render a clean silhouette, then put a bounded volume only where the backlight crosses the room. Check the beam with light on/medium off and vice versa. A Mist pass may separate the silhouettes in post, but it does not prove that light scattered between them. Use the [measured beam controls](lighting.md#chapter-light-field-study) instead of increasing fog until the bodies disappear.[349]

**Approval limit:** this is a short study of fixed stances, near-contact and secondary motion. The casts share a base morphology, the faces do not perform, and the rigid fingertips do not compress. The numeric checks cover selected surfaces on whole frames, not complete-body collision, subframe motion blur, dermatological realism, or a film-quality full performance. For close-up human skin, draped moving bodies or sustained acting, provide a separate reference-matched shot and inspect it at its actual delivery size.

### Sources

[18] https://docs.blender.org/manual/en/4.5/animation/shape_keys/introduction.html — Introduction - Blender 4.5 LTS Manual
[26] https://docs.blender.org/manual/en/4.5/animation/constraints/tracking/ik_solver.html — Inverse Kinematics Constraint - Blender 4.5 LTS Manual
[313] https://docs.blender.org/manual/en/4.5/sculpt_paint/weight_paint/editing.html — Editing Weight Paint · Blender Manual 4.5
[344] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/3dobjs/base.obj — MakeHuman CC0 data · 3dobjs/base.obj
[345] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/rigs/default.mhskel — MakeHuman CC0 data · rigs/default.mhskel
[346] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/makehuman/data/rigs/default_weights.mhw — MakeHuman CC0 data · rigs/default_weights.mhw
[348] https://docs.blender.org/manual/en/4.5/modeling/modifiers/deform/surface_deform.html — Surface Deform Modifier - Blender 4.5 LTS Manual
[349] https://docs.blender.org/manual/en/4.5/render/shader_nodes/shader/volume_scatter.html — Volume Scatter - Blender 4.5 LTS Manual
[350] https://github.com/makehumancommunity/makehuman/blob/a8bc2d54ff0ac92e78ff71431b1023eda42bf482/LICENSE.ASSETS.md — MakeHuman · asset license, separate from program code
[351] https://www.youtube.com/watch?v=TLOXzVKV_4M — condensation with geometry nodes

<a name="chapter-figure-source-map"></a>

## Figure studies: blocking, retargeting, condensation and light

Use each source for what can actually be checked. A sampled pose shows a contact; it does not disclose a rig or solver. The exercises below use workshop assets.

### Four independent sources

- **Blocking.** SamBam Studios' landing study shows an extended pose at 105 s, a labeled blocking pass on the platform at 220 s, then a denser keyframe editor at 340 s. These are sampled frames, not joint coordinates.[94] **Transfer:** mark approach, first touch and separation before interpolating. Check every intervening frame, not just the contact pose.
- **Retargeting.** CGDive's creator chapters distinguish import (7:57), a rest-pose issue (9:06) and its correction (10:09); the visual samples distinguish the capture tool from the skeleton in Blender.[352] **Transfer:** compare source and target at rest, then one loaded pose with a planted heel. Do not smooth a whole clip to repair a single bad bind. No capture service was used for the workshop figures.
- **Condensation.** Default Cube's narration instances streak curves on the point distribution and discusses the profile swept along a curve. The sampled views at 145, 305 and 470 s progress from a node graph to branching surface marks. They do not establish a particular numeric setting.[351] **Transfer:** on a glass test plate, view the outline from the side to distinguish raised drops from a flat roughness mask. The floor exercise only tests the latter kind of surface response; it does not reproduce the tutorial.
- **Light in air.** Samples at 66, 138 and 212 s in Olav3D Tutorials' Eevee lesson show a visible spotlight cone in a dark car scene; the property values are not legible.[347] Blender's Volume Scatter belongs on the **Volume** input, not Surface.[349] **Transfer actually exercised elsewhere in this workshop:** compare [light + medium, light alone, and medium alone](lighting.md#chapter-light-field-study) from the side in Cycles. That is not an Eevee version-equivalence test.

Start the independent [adult figure and contact study](figure-workflows.md#chapter-adult-figure-staging) for the native scene, animation and failure checks. The original workshop images, staging, actions and tests are credited to **Noa3**; third-party tutorials keep their original credits.

### Sources

[94] https://www.youtube.com/watch?v=oB_M_RGNqFY — SamBam Studios: How to make a Landing Animation - Blender Animation Tutorial
[347] https://www.youtube.com/watch?v=OwCh7SeXP8o — Blender Tutorial: Quick Volumetric Lighting for Beginners in EEVEE
[349] https://docs.blender.org/manual/en/4.5/render/shader_nodes/shader/volume_scatter.html — Volume Scatter - Blender 4.5 LTS Manual
[351] https://www.youtube.com/watch?v=TLOXzVKV_4M — condensation with geometry nodes
[352] https://www.youtube.com/watch?v=qLfrrtJNWP8 — Plask.ai: AI mocap from Video (+ Blender workflow)
