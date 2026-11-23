# Living worlds and creatures

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [Living worlds: from a valley floor to an orbital dawn](#chapter-living-worlds)
- [Creatures and scale: design from the bearing surface outward](#chapter-creatures-and-scale)

<a name="chapter-living-worlds"></a>

## Living worlds: from a valley floor to an orbital dawn

**Noa3 · Blender 4.5.9 LTS · Native tools only.** These are unrendered workshop recipes, not results from a supplied scene. Each test tells you what to inspect before spending geometry or light on the next layer.

### Carve the valley before scattering the forest

At Glacier National Park the river-cut example has a V profile; the glacier-cut valley has a broad U floor and steep sides. Bird Woman Falls descends from a tributary valley left high above the main trough. See *Glacial Geology*, “U-shaped Valleys” and the Bird Woman Falls caption. [406]

1. Draw the main watercourse in top view as a guide curve. Across it, cut a grid into broad flat-bottomed cross-sections with rising shoulders. Vary the width along the bend. Terminate a smaller tributary on a shelf above one shoulder; put its waterfall there rather than over a random noise peak.
2. Subdivide enough for that cross-section first. In Geometry Nodes (GN), use **Set Position** for secondary displacement; multiply Noise by a painted `rock_breakup` mask that falls to zero along the water. Keep the far ridge as a separate low-detail mesh. Frame the near shoulder against it before adding mist. Give the bank, not the whole valley, a dark wet strip using distance to the drawn shore.
3. **Test:** hide everything but the ground. Inspect three cross-sections and then a low, side-lit clay view. If you see a V under what ought to be a glacier floor, widen the floor vertices; if the water disappears uphill, lower the bed locally. Neither fault is a material problem.

### Meadow, trees and animals: three different distributions

The Agate Fossil Beds account contrasts dry-area bunch grasses in spaced clumps with the closer sod in wetter places; it describes this particular prairie, not a rule for every biome. [407] In Blender’s **Distribute Points on Faces**, Poisson Disk imposes minimum spacing; the node supplies stable IDs and a rotation derived from the surface normal. [9]

- **Grass:** make an upright narrow blade with a center crease and a bent tip; construct three clumps with different counts and spreads. Put each clump origin at soil level. On the evaluated ground mesh, read painted `dry`, `wet` and `trail` fields. Feed `dry × (1 − trail)` to Poisson Disk **Density Factor**; choose **Distance Min** for gaps between whole clumps, not blades. Feed a separate wet-bank mask to a denser short sod pass. Send Points and Rotation to **Instance on Points**; select a clump from **Collection Info** with Separate Children and Pick Instance. Vary local yaw and scale by point ID. Keep instances; **Join Geometry** with the ground last. For wind, bend the source blades with displacement weighted from zero at the root to full at the tip; vary phase among clump variants, not among vertices at random. **Test:** from above, the path should be continuous and the dry soil should show between groups. If soil shows inside every clump but not between them, increase point spacing rather than deleting individual blades. At distance replace blades with patches whose color already includes some soil; inspect a moving camera for sparkle.
- **Tree line:** make a trunk curve with a few unequal forks, then lateral branches, then leaf sprays. Reserve separate meshes for the crown silhouette and lower bare limbs. Scatter tree origins in a separate pass outside trail and water; control crown width and spacing together. Keep hero trees upright on sloping ground instead of plugging the grass normal rotation straight into them. Place a sapling, mature crown and broken snag in the same light. **Test:** the skyline should still separate the three without leaves; fix crown heights and fork positions before adding another leaf material.
- **Fauna:** give a small browsing group an actual route. Draw a curve from cover to a gap by the water, place one leader at the bank and two followers at unequal distances along it. Key body motion first, then place stance feet on the final terrain; clear a little foliage at the muzzle, not a circular hole around the whole animal. **Test:** in profile the muzzle must reach the water while the hind feet stay on the bank. If it cannot, move the animal to a shallower approach rather than stretching its neck. Blender Studio’s *Spring* synopsis pairs a shepherd girl and a dog with ancient spirits; it is a reference for assigning roles at different scales, not a source for this scatter setup. [409]

### Bonsai: make age readable at pot scale

Virginia Cooperative Extension’s *The Art of Bonsai*, paragraph beginning “Plants chosen for bonsai,” asks for a proportionate trunk, visible basal buttressing and gradual taper toward the apex. [408]

Choose the front before cutting branches. Model the pot rim and soil surface first; mark the trunk’s footprint on that surface. Use one Bézier spline from root flare to apex with decreasing control-point radius; branch off below each major direction change. Carry the thick branch a short distance into the parent and sculpt the junction on a converted working copy. Shape root flares that vanish into soil rather than tubes sitting on top. Build foliage pads on twig ends, leaving a window through the crown that exposes a fork. Use bark coordinates running along each branch; reduce relief on the thinnest twigs. Light across, rather than directly into, the front so the root flare casts a small readable shadow.

**Test:** silhouette the tree without its pot; then restore the pot and inspect a low three-quarter view. If it reads as a lollipop, shorten the uninterrupted trunk or cut a window between two pads. If the base looks like tentacles draped over a disk, lower their tips into the soil and widen only their attachment. A smaller object scale alone will not fix either problem.

### Daylight and the Sun: choose what the camera is observing

A Blender Sun light has direction but no meaningful position for illumination; **Angle** is its angular diameter. [22] The Nishita Sky Texture separately offers elevation, rotation and angular **Sun Size**, with a **Sun Disc** lighting switch in Cycles. Its altitude control is limited to 60 km: it is not an orbital-atmosphere solver. [417] NASA tabulates the apparent solar diameter at one astronomical unit as 1919 arcseconds, about 0.533 degrees. [419]

- **Camera on the ground:** in Cycles connect Nishita Color → Background Color → World Output Surface. Enable its disc, set Sun Size to about 0.533° for the Earth-distance study, and establish elevation from the intended shadow direction. Do not add a second Sun by habit. Alternatively disable the world disc, keep daylight fill, and rotate a separate Sun to the same direction with the same Angle. In that split setup provide a matching camera-visible disc only if the shot needs one; the lamp itself is not an image of the Sun. **Test:** put one pole in the shot. A sky-only exposure should show sky fill; the finished setup should give one dominant shadow. If the pole casts two differently directed shadows, isolate each source and remove or align the duplicate. Do not inflate solar diameter just to brighten the sky.
- **Camera observing a star in space:** use a black World, a directional Sun for the planet and a separate camera-visible emissive disc or sphere behind it. Set the disc’s apparent diameter by camera angle, not lamp energy; coordinate lamp direction with the disc center and exclude the visible prop from indirect lighting if the lamp already supplies it. An Earth-distance calibration is not appropriate for every planet. **Test:** sweep the planet across the disc. It should occult cleanly while the lit hemisphere faces the star. If the crescent faces away, correct the light rotation, not the planet texture.

### Planet, atmosphere and anomaly: record which distances are real

NASA’s *Sunrise from the Station*, image description, distinguishes a warm lower atmospheric band and blue above it in that particular edge-on sunrise. It is not an all-around neon outline. [416] Scene **Unit Scale** changes the display conversion, not internal physics. [418]

1. Choose one conversion for the shot, for example **1 Blender unit represents 100 km**. Record the chosen body radius, shell heights, camera altitude and any exceptions in a scene text block. Divide every physical length by the same km-per-unit factor. Work near the local origin; tighten camera clipping around this shot. If a cloud deck must be exaggerated, record its true and display heights separately. A planet near the origin plus a directional star is a lighting model, not a distance-accurate solar system.
2. Give rock/ocean one sphere, clouds their own slightly larger shell and the atmosphere a bounded volume. For a controllable density field, use centered object coordinates in a common Empty’s space → **Vector Math: Length** → **Map Range** from surface radius to outer radius, with density highest at the surface and zero at the boundary; multiply by a density control into **Principled Volume**, connected to Material Output **Volume**. Apply uniform object scale and keep the Empty at the planet center. Use the directional star to reveal the long path at the limb. This is a visual approximation, not spectral scattering. **Test:** compare sunward limb, terminator and night limb with the clouds hidden. If all three glow equally, remove unconditional emission; if the planet looks coated in thick glass, correct shell thickness against the radius before lowering density.
3. **Invented anomaly:** sketch a broken arc crossing the orbital plane. Build the arc from a beveled curve, taper its ends and drive emission from a lengthwise ramp; separate its faint haze into a local volume. Put part of the curve behind the planet and part in front of a moon. Reuse the unchanged planet lighting as a control. **Test:** disable the haze and move the camera sideways. If the arc always reads as a screen overlay, move its control points in depth until the occultation changes. Label the radius and mechanism **invented**; do not present a decorative arc as measured aurora, gravitational lensing or a scale diagram.

### Sources

[9] https://docs.blender.org/manual/en/4.5/modeling/geometry_nodes/point/distribute_points_on_faces.html — Distribute Points on Faces - Blender 4.5 LTS Manual
[22] https://docs.blender.org/manual/en/4.5/render/lights/light_object.html — Light Objects - Blender 4.5 LTS Manual
[406] https://www.nps.gov/glac/learn/nature/glacial-geology.htm — National Park Service — Glacial Geology
[407] https://www.nps.gov/agfo/learn/nature/grasses.htm — National Park Service — Grasses, Agate Fossil Beds
[408] https://www.pubs.ext.vt.edu/content/pubs_ext_vt_edu/en/426/426-601/426-601.html — Virginia Cooperative Extension — The Art of Bonsai
[409] https://studio.blender.org/films/spring — Blender Studio — Spring
[416] https://science.nasa.gov/earth/earth-observatory/sunrise-from-the-station-152259 — NASA Earth Observatory — Sunrise from the Station
[417] https://docs.blender.org/manual/en/4.5/render/shader_nodes/textures/sky.html — Blender 4.5 Manual — Sky Texture Node
[418] https://docs.blender.org/manual/en/4.5/scene_layout/scene/properties.html — Blender 4.5 Manual — Scene
[419] https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html — NASA — Sun Fact Sheet

<a name="chapter-creatures-and-scale"></a>

## Creatures and scale: design from the bearing surface outward

**Noa3 · Blender 4.5.9 LTS · Native tools only.** All recipes below are unrendered. The gait observations, specimen features and instrument descriptions are sourced; control layouts, invented organisms and proposed tests are workshop decisions.

### Dog: build the animal under the coat

In the University of Minnesota’s canine *Trot* diagrams, opposite fore and hind limbs alternate support. The running example has suspension between diagonals; the slow trot need not. The text even notes a small hind-before-fore impact offset despite the apparent paired beat. [412]

Block rib cage and pelvis as separate masses with a flexible waist; record shoulder height, chest depth, muzzle length and paw width from the **same** dog reference. For a second individual alter the blockout and refit the joints before varying coat color: stretching a finished rig lengthwise also stretches its foot placements. Trace shoulder blade, elbow, wrist and toe on the forelimb; trace hip, stifle, hock and toe on the hind limb. Place knee-direction pole targets in the intended bend planes. Keep the shoulder blade on its own movable control. Give each paw a ground-space IK target and a toe-roll control with its pivot at the pad contact, not the ankle.

**Animate the trot:** mute the tail and fur. Put the left fore/right hind pair down, move the chest and pelvis across those targets, release, then exchange diagonals. Add a suspension interval only for the running version. Inspect in world space with a chalk mark under each planted pad. If a pad travels with the root, remove root inheritance from its stance target or key the target stationary in world space. If the gait reads as a pace, change the hind-leg phase, not the speed. Restore the tail after the uncoated dog reads correctly.

**Fur and distance:** attach hair curves to the deformed skin; comb short guides from muzzle toward cheek, give neck and flank distinct guide directions, then interpolate by region. Mask lips, pads and eyelids before increasing density. Light the coat from behind to expose the silhouette. For a mid shot retain only silhouette clumps over painted directional color; in the far shot retain the shape of ears, tail and ruff in the base mesh. Compare the same head turn at both distances. If the jaw grows a halo, shorten guides near the lip rather than thinning the whole coat.

### Horse: prove three gaits with four hoof markers

The Nebraska extension demonstration names **walk** contacts left hind → left fore → right hind → right fore (00:10–00:37), **trot** as alternating diagonal pairs (01:20–01:36), and **left-lead canter** as right hind → left hind + right fore → left fore (02:23–02:43), followed by suspension (03:01). [413]

Start from a side reference of one horse: block withers, barrel and croup; mark shoulder, elbow, carpus, fetlock and hoof on the front, stifle, hock, fetlock and hoof behind. Put the hoof-control pivot at the sole and add a toe pivot for breakover. Keep the neck base independent of the head, and weight the hind leg clear of the belly at full forward reach. Use contrasting markers on the four hoof controls. Create three Actions with separate contact keys rather than retiming one cycle.

| Action | Block first | Failure → correction |
|---|---|---|
| Walk | Key the four named contacts in order and keep at least one hoof planted throughout this study. Translate the root across the supports before adding head motion. | Two hooves strike together: stagger their contact keys, then check that the wrist does not pop on the passing pose. |
| Trot | Pair left fore with right hind, then right fore with left hind. For the demonstrated suspended trot, leave a short airborne interval. | A front view shows both legs on one side swinging together: swap the hind phases, not the labels. A skating sole needs a stationary stance target. |
| Left-lead canter | Block the single rear strike, diagonal strike, single leading fore strike, then suspension. Let pelvis and chest pitch across the sequence rather than bobbing as one rigid block. | The right fore lands last: inspect one full stride and mirror the entire sequence if the wrong lead was built; moving only the last key breaks the diagonal. |

**Test:** hide mane and tail; record the hoof names in order for two loops with the root moving forward. Check that the last pose blends into the next stride without a repeated contact beat. Then try a compact and a long-backed variant: move the controls to the new joints and recheck hoof clearance under the belly rather than scaling the stride by eye. Reserve separate mane clumps for the near view; from afar keep their crest silhouette, not individual fibers.

### Bird: fold a wing without shrinking the feathers

Cornell Bird Academy’s “Wing feathers” describes the asymmetry of the flight vane; the flight discussion distinguishes independently rotating outer primaries from overlapping inner secondaries. [414]

1. Draw the extended and resting outline for one chosen bird on the same side-view sheet. Build breast and shoulder mass first; place shoulder → elbow → wrist → hand controls. Use two feather families, not one mirrored leaf: a narrow leading vane and broader trailing vane around an off-center shaft. Make primaries from hand-rooted pivots, secondaries from forearm-rooted pivots, and a short separate cover layer across their roots. Mirror the **whole wing** and inspect leading edges, not just normals.
2. Key a rest fold in stages: bring the upper arm alongside the body, flex elbow and wrist so the hand turns back along the flank, then reduce primary fan angles until the tips stack. Set feather roll and layer offsets by row. Make a half-fold pose before polishing either endpoint. Keep the shaft length fixed; use small local rotations to resolve overlap.
3. **Test:** scrub slowly from extended through half-fold to rest under a broad side light. If the tips slide through the chest, check the wrist arc; if shafts slice through adjacent vanes, change fan order and roll instead of scaling the feathers shorter. Use separate shaft and vane geometry in a close-up, overlapping row cards in mid shot, a single wing silhouette at distance. Compare both wings edge-on as they fold; an edge that vanishes needs thickness or revised card orientation, not more painted barbs.

### Tiger beetle: a macro shot, not microscopy

ASU’s tiger beetle overview describes a head broader than the thorax; “Thorax” attaches all six legs and both wing pairs there. Hardened forewings cover the folded clear hindwings at rest. [410]

Use a chosen specimen’s body length as the model dimension; if none is available label the size illustrative. Make head, thorax and abdomen separate shells. Split two elytra along a dorsal seam, add hinges near their anterior attachment and tuck a thin folded hindwing underneath each. Parent three leg pairs to the thorax; set coxa pivots near its sides and tarsal contact targets against a modeled leaf. Build curved jaws and raised eye domes before any scratches. Use one broad reflection strip to reveal the forewing camber and a narrower highlight for the seam; vary roughness more than base color. Focus a macro camera on the nearer eye, but start with depth of field disabled.

**Test:** in underside view count the six attachments. In side view open the covers before deploying the hindwings. If a hindwing emerges through a closed shell, offset its deployment key or reroute its fold. Restore depth of field and check that the eye and seam can still be identified; broaden focus before intensifying highlights. This is an enlarged camera view of an external body, not a claim about structures resolved by an electron microscope.

### Diatom: make a scientific plate that survives resizing

**Macrostructure is not the same as a macro lens.** For any multiscale surface, decide which structures change the silhouette, which form relief, and which only change the highlight. On a rocky hide, for example, sculpt the large folded envelope, instance overlapping plates following a tangent field, and add grain at its own physical size via roughness or bump. Inspect the silhouette without either detail layer, then re-enable one layer at a time at three camera distances. If all layers read as the same noise, change their scale, direction and placement or remove one; if detail aliases in the far shot, filter or fade it rather than enlarging every pore. For a scientific subject, label invented structure rather than implying that one can resolve pores in an overview image.

UC Berkeley’s Monterey Formation microfossil page identifies environmental scanning electron microscope images with micrometer bars. The “Diatoms” captions distinguish a hoop-shaped cingulum, side view and perforated end plate. [411]

Select **one** image and retain its original bar, view direction and specimen identity in the working notes. With an orthographic camera, derive projected specimen width as `specimen width in source pixels / source bar length in pixels × labeled bar length`. Record the micrometer-to-Blender-unit ratio explicitly; do not infer depth from this one projection. Revolve a drawn wall profile, add the cingulum as a separate band, then lay out end-plate perforations in the reference’s arrangement. Use real holes only where the opening is resolved; use a bump or tone field elsewhere. For an SEM-inspired plate choose monochrome values and soft relief lighting. Label inferred depth and false color, if any, as interpretation; a Blender material is not a simulation of electron detection.

**Test:** add a bar of known model length at specimen depth, align it to the camera plane, and match the source bar-to-width ratio before adding the caption. Resize specimen and bar together. If their ratio changes after layout, regenerate the bar for the final crop; if unresolvable pores form stripes, switch that pore band to averaged tone rather than claiming additional detail. Without a legible reference bar, publish the image as an uncalibrated structural illustration, not a measured specimen.

### Dragon hide: where do the scales stop?

The Digital Atlas of Idaho’s gopher snake description contrasts its keeled scales with smooth scales on juvenile racers. A keel is therefore a useful choice to compare, not a universal instruction to cover a reptile in ridges. [415] The following dragon, its armor layout and its dimensions are invented.

Make a smooth body and rig it **before** designing plates. Draw a spine-to-flank direction map and reserve soft fold strips behind the jaw and on the inside of the elbow. Create two scale masters with compatible footprints: one smooth, one with a low longitudinal ridge. Draw staggered guide curves along the posed body, resample to plate spacing and instance a master per point. Orient its long axis along the curve tangent and its outward axis to the skin normal; vary width by body region rather than randomizing every angle. For animation bind guide roots to the deforming surface and evaluate plate transforms after skin deformation; do not project fresh randomly distributed points every frame. Build belly bands separately across the body. Light across the ridges, then reverse the light to distinguish real relief from painted streaks.

**Test:** bend the elbow and turn the neck to their production extremes. If the joint jams, shorten or remove inner-row plates; do not solve intersections by raising the entire coat off the skin. Keep overlapping geometry at the near silhouette; bake tangent-space normals for the middle distance and use broad color and roughness regions in the far view. At the cut between levels, compare the outline of the jaw ridge and the mean brightness of the flank. A sharp brightness pop calls for matching material response across levels, not adding more scales.

### Eldritch animal: break one anatomical rule on purpose

Blender Studio’s *Spring* premise contrasts a familiar dog with ancient spirits. [409] Borrow the contrast, not the characters: invent a marsh walker with four load-bearing legs and a suspended ring that turns independently above its chest. Note its designed shoulder height beside an ordinary reed or figure; neither that height nor its floating organ is a scientific measurement.

Block the chest, hips, weight-bearing joints and neck first. Use the walk contact sequence above for the supporting body. Give the ring a separate non-deforming control at the chest and mark one notch on its rim so rotation reads. Key the ring to pause while the walker turns underneath it; then let it catch up. Keep its illumination low enough to preserve the shadow under the planted feet. Build variants by changing body mass and ring diameter together, not by scattering extra limbs over the surface.

**Test:** hide materials and play the turn from front and side. A viewer should be able to name the supporting feet and point to the one impossible motion. If everything seems to float, restore sole contact and chest weight transfer first. If the ring becomes an ordinary collar in profile, tilt its plane or increase the visible air gap. Keep a neutral frame and dimension note with the shot so artistic scale cannot be mistaken for specimen data.

### Sources

[409] https://studio.blender.org/films/spring — Blender Studio — Spring
[410] https://askabiologist.asu.edu/tiger-beetle-anatomy — Arizona State University, Ask A Biologist — Tiger Beetle Anatomy
[411] https://ucmp.berkeley.edu/tertiary/mio/montmicro.html — UC Museum of Paleontology — Monterey Formation: Microfossils
[412] https://vanat.ahc.umn.edu/gaits/trot.html — University of Minnesota — Trot
[413] https://mediahub.unl.edu/media/24357 — University of Nebraska–Lincoln — Footfall sequnces of horse gaits
[414] https://academy.allaboutbirds.org/feathers-article — Cornell Lab Bird Academy — Everything You Need To Know About Feathers
[415] https://www.isu.edu/digitalatlas/biology/reptiles — Idaho State University — Digital Atlas of Idaho: Reptiles
