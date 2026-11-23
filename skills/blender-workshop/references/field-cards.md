# Blender field cards

Pick the route that matches the failing check.

## model — Shape the silhouette

The shape or a cutout is wrong even with a flat material.

1. Block the largest form at its intended dimensions before beveling or shading.
2. For a through-hole, cut a real opening; keep the cutter editable.
3. Inspect the outline and negative space from two intended views.

**After the first step:** Read the Dimensions fields and compare the longest side with the brief before adding detail.

**Final check:** Background shows through the opening at delivery size in both views.

**If it fails:** Widen the cutter just enough to keep the gap visible.

**Without tools:** Rotate the blockout yourself and share both views; I cannot verify clearance from a description.

**Example:** Model the handle hole; paint the flush label.

## architecture — Frame an architectural bay

The camera must explain a space, entrance or repeated module.

1. Mark the exit and set a level camera at the intended eye height.
2. Repeat one bay with linked duplicates at a fixed pitch.
3. Place a bench for scale and render the view in clay.

**After the first step:** In camera view, the marked exit is visible and the vertical sides of a pier do not converge.

**Final check:** The exit reads without textures; the bench outline clears the nearest pier.

**If it fails:** Slide the bench sideways until its outline clears the pier.

**Without tools:** Inspect the clay view through the active camera yourself; I cannot verify the projected gap.

**Example:** Measure pitch between origins, but clear width between inner faces.

## material — Read a surface under light

The outline works, but the finish or texture scale looks wrong.

1. Put a beveled sample beside the part under the same grazing light.
2. For sheen change only Principled Roughness; for fine relief change only Bump Strength.
3. Compare highlight width or pore depth in the same camera crop at delivery size.

**After the first step:** A highlight crosses both the test sample and the part in the same frame.

**Final check:** The requested finish changes without moving the highlight source or changing the silhouette.

**If it fails:** Return to the original render and isolate roughness from bump.

**Without tools:** Render the two finishes from one camera; I cannot verify the difference without both images.

**Example:** Use Bump for limestone pores; model a chip that breaks the edge.

## procedural — Keep a scattered path open

Placement must obey a rule when a seed changes.

1. Mark the path as an exclusion band on the terrain.
2. Feed the allowed region into Distribute Points on Faces: Selection; instance one plant on the points.
3. Compare overhead views at two seeds with density fixed.

**After the first step:** Preview the allowed-region mask before instancing: it is false on the path, true in the bed.

**Final check:** Count forbidden plant centers at both seeds. If leaf clearance is required, inspect overhang separately.

**If it fails:** Inspect the selection mask first; widen it for overhang only if the centers already pass.

**Without tools:** Switch seeds yourself and inspect both path edges; I cannot verify clearance without the layouts.

**Example:** Change seed for another layout; change density for fewer plants.

## game — Test a prop after export

A prop must import or collide correctly in the receiving engine.

1. Import the exported prop into the target engine and turn on its collision display.
2. Mark one spot that must block the player and one spot that must stay passable.
3. Run a hit and a miss in the engine; for a moving gate repeat in both poses.

**After the first step:** The engine's debug overlay shows a collision shape at the imported prop, not just the visible mesh.

**Final check:** A player-sized probe hits the solid region and passes the designated opening. A render is not this test.

**If it fails:** Inspect the collision shape at the failed position, not the render mesh.

**Without tools:** Try the blocked and clear positions in your engine; I cannot verify collision in Blender alone.

**Example:** Use one hull for a solid crate, multiple hulls for a traversable handle.

## animation — Time a looping motion

The poses work individually but the movement hesitates or pops.

1. Key the start, extreme and return poses of a swinging arm.
2. Add a breakdown pose along the swing arc.
3. Play at delivery frame rate across the loop seam.

**After the first step:** Scrub the three keyed frames: the extreme differs, and the last pose matches the first.

**Final check:** The arm follows the arc without an extra held beat at the seam.

**If it fails:** End playback one frame before the duplicate start pose.

**Without tools:** Play the loop twice yourself; I cannot verify timing from pose stills.

**Example:** Keep a repeated pose for an intentional hold; omit the duplicate endpoint from a seamless loop.

## anime — Separate cel shadow bands

The face needs graphic shadow shapes rather than a smooth gradient.

1. In EEVEE, connect white Diffuse BSDF to Shader to RGB, then Color to Color Ramp Fac.
2. Set the ramp to Constant; send its colors through Emission to Material Output.
3. Turn the face under a fixed key and inspect adjacent frames at thumbnail size.

**After the first step:** In EEVEE, trace the two links from Diffuse through Shader to RGB into the ramp's Fac input.

**Final check:** Light and shadow stay distinct on the cheek without a one-frame flash.

**If it fails:** Move the ramp threshold away from the flickering cheek value.

**Without tools:** Scrub the turn yourself in EEVEE; I cannot verify band stability from the node list.

**Example:** Use Shader to RGB in EEVEE; test Toon BSDF separately for Cycles.

## render — Choose a daylight shadow edge

Framing is settled; the shot needs harder or softer shadows.

1. Lock the camera, exposure, Sun direction and strength.
2. Render the same floor shadow twice, changing only Sun Angle.
3. Compare the shadow edges at the intended image size.

**After the first step:** Save the baseline frame and note which floor edge the shadow crosses before changing any light setting.

**Final check:** The softer version has a wider transition along the same floor joint.

**If it fails:** Compare a crop where direct sunlight crosses the joint.

**Without tools:** Render both angles yourself and compare the same crop; I cannot verify the edge width without images.

**Example:** Favor a narrow edge to emphasize repeated bays, a broad edge to quiet the floor pattern.

## rigging — Isolate elbow weights

A joint pinches or drags nearby vertices in a still pose.

1. Place the elbow pivot in Armature Edit Mode.
2. Match deform-bone names to vertex groups on the mesh with its Armature modifier.
3. Bend the elbow in Pose Mode and compare with rest.

**After the first step:** Inspect front and side views in rest pose: the hinge sits at the intended bend in both.

**Final check:** The forearm follows the bone; the upper sleeve stays put away from the joint.

**If it fails:** Remove stray forearm weights from the upper sleeve.

**Without tools:** Pose one elbow yourself and inspect the sleeve; I cannot verify deformation from bone names alone.

**Example:** Test a still bend for skinning; retime keys only if the bend itself is clean.

## composite — Isolate a correction with a matte

The rendered shot works except for one object’s color.

1. Enable the Object Cryptomatte pass in View Layer Properties and render.
2. Pick the object with a Cryptomatte node in the Compositor.
3. Use its Matte as the Mix factor between the original and corrected images.

**After the first step:** The new Render Result includes the Object Cryptomatte passes for the active view layer.

**Final check:** At full resolution the object changes color while its neighbor retains the original color.

**If it fails:** Remove the neighbor’s ID from the matte selection.

**Without tools:** Toggle the Mix result against the original yourself; I cannot verify edge spill without the images.

**Example:** Mask the sign to brighten its lettering; raise exposure only if the whole shot needs it.
