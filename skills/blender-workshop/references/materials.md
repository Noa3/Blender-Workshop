# Materials, UVs and optical surfaces

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [Materials, light and camera](#chapter-materials-light)
- [Texturing: from a seam to two usable maps](#chapter-texturing-workflow)
- [Materials by optical behavior and physical scale](#chapter-surface-recipes)
- [Relief, surface history, glass and transmitted light](#chapter-optical-surfaces)
- [Worn surfaces, secondary motion and the final composite](#chapter-wear-and-finishing)

<a name="chapter-materials-light"></a>

## Materials, light and camera

### Build a test stand instead of guessing sliders
Compare a sphere, a slightly rounded cube and a flat sample under the same large area light. Matte gray and mirror controls help distinguish light color from the reflected environment. Lock camera, exposure and view transform during comparisons. A glossy black sphere with no recognizable light source says little about roughness.

### PBR recipes in the Shader Editor
Principled BSDF combines diffuse, metallic, transmission and subsurface components under additional layers such as coat.[3] `Metallic` is not highlight strength: bare metal shows its color in reflections; paint puts a nonmetallic color layer over it. Start pure metal/dielectric at 1/0 respectively. Intermediate values are for mixed texels or masks, not a general realism control.[3]

| Surface | Build and test |
|---|---|
| Satin brass | Warm Principled base color, Metallic 1. Limit `Noise (Fac) → Map Range → Roughness` to a narrow range (center 0.30 in the lab, not 0–1). A broad softbox and a dark environment edge produce readable reflection bands. Move the light in a variant: a true reflection travels; a painted highlight does not. |
| Ceramic/enamel | Nonmetallic colored base, controlled roughness, optionally a finer coat layer. A narrow bevel and a clean reflected light often sell the glaze better than heavy noise.[1][3] |
| Wood/stone | Set separate scales for large color structure, medium roughness variation and fine height detail. Check coordinates on the object. Run wood grain along the fibers, not equally along all axes. Do not feed the same structure at equal strength into color, roughness and bump. |
| Glass/clear coat | For solid glass, use closed geometry with thickness, Transmission Weight and suitable IOR. Place bright and dark strips behind it to reveal refraction.[3] Alpha fading is not glass. If it looks black, check the background, normals, overlapping walls and engine first. |
| Skin/cloth/hair | Check subsurface at actual object scale; lips, sclera and wet eyelid rims need distinct materials. Put cloth silhouette and folds in geometry, fiber response in roughness/sheen.[3] Cycles offers Principled Hair BSDF for realistic hair curves. Check clumps and highlight direction in backlight.[33] For anime, shape the large hair masses before individual fibers. |

**Image textures:** Albedo/base color is usually sRGB. Set numerical roughness, metallic, height and normal data to `Non-Color` to avoid color transformations on measurements.[11][12] Normal texture → **Normal Map** → BSDF Normal. Height map → **Bump: Height** → Normal. Bump changes the shading normal, not the silhouette.[30] For combined details, Normal Map → Bump `Normal`, then Bump → BSDF `Normal`. For actual displacement, check subdivision and silhouette separately. Do not paint hard shadows into albedo for a scene that needs relighting.

### Product lighting: one lamp at a time
1. Start matte gray. Place a key to the side and slightly above, large enough for the desired shadow edge. Design the **size** and **position** of the reflected light shape before adjusting energy. When changing size, check the Blender version's power and normalization settings.[22]
2. Begin with a darker far side. Add only enough fill to read the important form. A rear strip separates edges from the background. If lighting looks flat, reduce fill/world or move the key farther to the side before doubling material contrast.
3. The metal lab has separate key, rim and front reflection lights. Disable one via render visibility, compare from the same camera, then restore it. Knurling must remain visible as geometry.
4. Use an orthographic camera for technical comparisons or patterns at constant scale. For perspective, choose viewpoint and the relative size of foreground/background first, then focal length for framing. Add depth of field only after approving the form; focus on a named object.[23]

**Character acceptance test:** From a fixed camera, compare key only, key + fill, rim only, then all three. Fill should reveal the shadow cheek without erasing the key direction. In isolation a good rim reads at an ear or hair edge, not as a second frontal key. The Blender Fundamentals comparisons at 00:50, 01:15/01:20 and 01:30 show these distinct jobs.[47]

### Color management, rendering and diagnosis
- **Realism:** Start with AgX; it does not replace lighting. **Graphic palette:** Compare Standard when neutral exposure should show the chosen bands directly. Calculate in scene-linear space and apply the display transform once. An OpenEXR master and a PNG for visual approval serve different purposes.[11][35]
- **Cycles:** Test a camera crop containing difficult shadows/highlights. Adjust adaptive sampling/noise threshold, then compare denoised and raw crops: thin embossing and pores must survive.[14] For animation, inspect consecutive frames; a clean still does not prove temporal stability.
- **Symptoms:** Smooth but chalky → test light cards and roughness separately. Reversed lettering/normals → UVs and tangent basis. Dirty relief → reduce Bump Distance relative to object scale. Wrong red after export → compare source color space, display transform and target viewer. Do not assume shaders outside Principled/bitmap PBR are glTF-portable.[20]

[Sources](sources.md).

<a name="chapter-texturing-workflow"></a>

## Texturing: from a seam to two usable maps

**Route: `material`.** Can the print stay in the right place while its finish responds to the light? Generate `Tide-Register.blend` locally with [the optional Tide Register exercise](portable-use.md#tide-register). At frame 10, render the camera. Find the pale band near the tip of the red needle. Scrub to the opposite extreme, frame 34: the band should turn with the needle, not stay at the same place on the dial. The needle is the worked example; the cylinder and paint exercises below are manual variations (`untested` in your file).

### 1. Decide what the coordinates must follow

| If the mark belongs to… | Start with | First check |
|---|---|---|
| A particular face: lettering, a painted scratch, a needle stripe | A named UV map feeding the Image Texture's **Vector** input | Rotate the part; the mark still covers the same face and points the same way. |
| A volume of material: a block of stone or a turned wooden handle | Object coordinates from the part or a deliberately chosen reference object, then Mapping | Double the length of a test copy. Is the grain meant to stretch or are there meant to be more rings? Move the reference independently to see what anchors the pattern. |
| A quick procedural sketch sized to one mesh's bounds | Generated coordinates | Compare a short and a long copy before committing to the pattern's physical scale. A convincing swatch is not a scale reference. |

UVs describe a surface layout; Generated and Object coordinates are different inputs, not interchangeable presets.[57] Note the part dimensions and intended viewing distance. On a static practice mesh with nonuniform object scale, apply **Scale** on a copy before unwrapping. Do not apply transforms to a rigged or animated asset just to fix a texture. Check the UVs or Mapping node first.

### 2. Unwrap where a break can be tolerated

Try a capped cylinder in the **UV Editing** workspace. In mesh Edit Mode select the top and bottom boundary loops and one longitudinal chain on the back. **Edge → Mark Seam**. Select the faces and use **UV → Unwrap**. Expect two caps and one continuous side wall. The lengthwise seam opens the wall; cap seams alone leave it a closed tube. Put the longitudinal cut away from a front label or at a material join. A tileable image does not hide an arbitrary change of phase across a mesh seam.[298]

Feed a numbered UV grid to Base Color temporarily. Inspect the actual object from front, back and end: numbers upright on the label, squares not stretched, comparable square size on surfaces that need the same detail. **Average Islands Scale**, then **Pack Islands** with space for filtering where independent pieces need comparable texel density.[294] A large hero label may deliberately get more space. Keep painted or baked islands unique unless the marks are intentionally identical; stacked mirrored islands also mirror text and wear. If one column kinks, fix that island or seam before raising image resolution.

### 3. Build one mask, then choose what it controls

**Paint when the position tells a story.** Add an Image Texture with a new named image, such as `Wear_mask`, set its color space to **Non-Color**, and select that image as the paint target in **Texture Paint**. Start black, then paint one white stroke on a place that would be handled. Preview the mask alone. Can you find the same stroke on the model and in the Image Editor? If it paints elsewhere, check the active image, face/material assignment and UV map before changing the brush. Save the painted image using **Image → Save As** or pack it into the `.blend`; save the project and reopen it. A saved mesh is not proof that an external paint image was saved.[292][308]

**Use nodes when the rule is easier to describe than to paint.** For a straight printed ring use `UV → Separate XYZ → Y → Color Ramp`. Give the band two boundaries, not a threshold that colors the entire tip. For cell edges try Voronoi **Distance to Edge** into a narrow Color Ramp and inspect the mask before connecting a **Mix Color** node.[304] Make one large-scale feature read before adding noise. If every edge is equally worn, multiply the rule by a hand-painted mask rather than adding more noise everywhere.

Let the mask choose two base colors and, independently, two roughness values. A pale marking need not be glossier. Paint over a metal body is ordinarily a dielectric top surface; use metallic where the mask actually exposes metal, not anywhere the color happens to be bright. A scratch that changes the outline needs geometry, not darker paint. See [surface recipes](materials.md#chapter-surface-recipes) for further samples.

### 4. Wire color and data by meaning

| Image role | Interpretation and destination | Check before blaming the light |
|---|---|---|
| Base color in a conventional color PNG | **sRGB** → Principled **Base Color** | No painted-in highlight or cast shadow if the asset must relight. |
| Roughness, metallic, paint mask, height | **Non-Color** → the matching scalar socket; height goes to **Bump → Height** | A white roughness patch should broaden the reflection under the same light. Do not apply a display transform to these values.[11][30] |
| Gloss / smoothness | Read as data. For a source defined as the inverse of roughness, calculate `1 − gloss` once | The glossy reference patch should have the narrower highlight. Check the supplier's convention; do not invert an existing roughness map. |
| Tangent-space normal | **Non-Color** → **Normal Map** node's **Color** → Principled **Normal**, with the UV set used to bake it | Light from two sides. Check the source's OpenGL/DirectX Y convention if dents appear raised; don't invert all three channels.[12] |

To combine height and normals, send **Normal Map → Bump: Normal**, then **Bump: Normal → Principled: Normal**. Height is scalar; an RGB normal encodes a direction. Neither displaces the silhouette by itself.[12][30] Compare finishes in the same camera crop with one broad light at a grazing angle. Changing the exposure, light and roughness at once makes the result impossible to diagnose.

### 5. Bake without baking in the light

Use **Cycles** when delivering ordinary images from nodes. Keep the editable source material. On a UV-unwrapped copy, make an unconnected **Image Texture** node for the first destination and click it so it is the **active** node in the baking material. A target visible in the Image Editor is not necessarily the bake target.[13] For several material slots, set the active target in every participating material or isolate one on a test piece.

1. For a procedural base color, temporarily connect the **color signal** to **Emission: Color** with strength 1, then **Emission → Material Output: Surface**. Bake type **Emit** to the color destination. This copies the signal, not the lit appearance. For a same-surface bake leave **Selected to Active** off.
2. Make a **different** target for roughness, set it to **Non-Color**, select its node and feed the roughness scalar to Emission instead. Bake **Emit** again. Restore the source shader afterward. A tangent normal is not a grayscale emission pass: use a **Normal** bake with the required space and target UVs.[13]
3. Leave margin around islands and enough padding for the lowest delivered texture size. Save or pack each result. Build a fresh material using only the output images; assign it to the **visible faces**. On the reopened file, check two known patches and the UV registration. Seeing the images in a list does not prove that the renderer uses them.

**Tide Register, reproduced in Blender 4.5.9 LTS:** the editable `Print master | editable stripe separations` uses a flat UV test piece. Two separate 256 × 256 Emit bakes are packed. The needle's upper face uses `Needle face | baked witness band` and UV map `Blade print`. The red and pale sample roughnesses reopened at **0.2784** and **0.7020**, respectively (design values 0.28 and 0.70). The dark sides intentionally use a different material. This tests color and roughness, not a normal bake, painted brush stroke or high-to-low projection.

### When it looks wrong

- **Black bake:** check the active destination node, selected mesh, nonempty UV map, and the signal reaching the active Material Output. Try a constant white emission on a small spare target. Do not overwrite a good map to troubleshoot.
- **Pale band vanishes after reopening:** inspect the material on the top face, its UV node, and whether each image is packed or resolvable relative to the project. A pink missing-file surface and a valid black mask are different failures.
- **Visible border on a repeating tile:** test a 3 × 3 repeat at delivery size. Inspect both axes and the corners in base color **and** in the data maps. Baking an image does not make its opposite borders match.[309] Do not hide a roughness seam by editing only the color.
- **High-to-low normals show neighboring parts:** isolate the pair on a duplicate, check the active low-poly receiver and cage/ray distance, then inspect the silhouette under moving light.[13] For engine delivery, check the imported result in the [game-art route](game-assets.md#chapter-game-art), not just the Blender viewport.

Continue with the [animation workflow](motion.md#chapter-animation-workflow) to check a marking over time, or open the [creator lessons and source notes](learning-notebook.md#chapter-surface-motion-sources) to see what each tutorial actually supports.

The [scene builder](../scripts/build_tide_register.py) performs both Emit bakes and packs them in the locally generated scene. Inspect the two packed images in Blender’s Image Editor. Check color and roughness independently while scrubbing the needle.

### Sources

[11] https://docs.blender.org/manual/en/4.5/render/color_management.html — Color Management - Blender 4.5 LTS Manual
[12] https://docs.blender.org/manual/en/4.5/render/shader_nodes/vector/normal_map.html — Normal Map Node - Blender 4.5 LTS Manual
[13] https://docs.blender.org/manual/en/4.5/render/cycles/baking.html — Render Baking - Blender 4.5 LTS Manual
[30] https://docs.blender.org/manual/en/4.5/render/shader_nodes/vector/bump.html — Bump Node - Blender 4.5 LTS Manual
[57] https://docs.blender.org/manual/en/4.5/render/shader_nodes/input/texture_coordinate.html — Texture Coordinate Node - Blender 4.5 LTS Manual
[292] https://docs.blender.org/manual/en/4.5/sculpt_paint/texture_paint/introduction.html — Blender 4.5 LTS: Texture Paint — Introduction
[294] https://docs.blender.org/manual/en/4.5/modeling/meshes/uv/editing.html — Blender 4.5 LTS: Editing UVs
[298] https://www.youtube.com/watch?v=VKqOFMr6Ns0 — Blender Inferno: How to UV Unwrap a Cylinder in Blender 4.5 for Beginners!
[304] https://www.youtube.com/watch?v=X7NXotJUkUA — Blender Inferno: The Voronoi Texture in Blender 4.5 - In Depth Blender Lesson
[308] https://www.youtube.com/watch?v=bR4HtqxA9tk — Ryan King Art: Texture Paint Metallic Maps and Edge Wear (Blender Tutorial)
[309] https://www.youtube.com/watch?v=VAjGtE678o0 — Ryan King Art: Bake Procedural Materials to Tileable Texture Maps (Blender & Gimp Tutorial)

<a name="chapter-surface-recipes"></a>

## Materials by optical behavior and physical scale

Keep a sample object and the actual object. A sphere is good for highlights but hides a distorted floor tile; a flat board exposes tiling but not the shape of a reflection. The supplied library uses six equal beveled coupons, fixed lighting, a striped backing card for glass, and extra oak and linen close-ups. It is a stylized, editable practice collection, not a collection of measured scans.

| Material | Editable graph or geometry in the library | What to inspect / when to change approach |
|---|---|---|
| **Honed limestone** | Low-frequency 3D Noise → warm Color Ramp and a restrained Roughness range. A separate fine Noise feeds Bump at very small distance. Retain the large machined edge in geometry.[55][30] | Under raking light, the bevel should read before individual pores. If the texture looks like camouflage, narrow the color range; if the stone looks waxy, inspect roughness and studio reflections before changing the hue. |
| **Fired clay tile** | Brick Texture in the floor's local XY plane; set brick width, row height, offset and mortar separately. Color varies per tile; its mortar factor drives inverted shallow Bump. The library uses 0.58 by 0.29 local-meter pattern inputs at scale 1.[53] | Check the tile against a foot or seat, turn the slab and look along grout lines. Bump does not produce a chipped silhouette; use mesh for foreground broken edges. Do not copy the XY projection onto a wall without rotating the vector. |
| **Oiled oak** | Stretched 3D Noise supplies fibers; a small distorted Wave contribution breaks the fiber bundles into grain lines. Scale the coordinates anisotropically, keep the long grain aligned with the board's local Y, then grade with a warm two-color ramp.[54][55][58] | Look at two adjacent boards. Perfect ruler-straight stripes are not wood; too much distortion looks like marble. This coupon is a long-grain approximation, not end grain or a knot model. For close furniture, give the end cut a dedicated projection. |
| **Bronze with oxide** | A ramp turns noise into an oxidation mask. Drive three responses from the same mask: warm reflective bronze vs. green oxide, higher roughness on the oxide and a mostly nonmetallic oxide response. Do not just tint the entire metal teal.[3] | Move a white card across the reflection. The highlight should break where oxide appears. The example uses noise to teach the response; on a hero prop guide the mask with creases, rain streaks and protected vs. rubbed areas. |
| **Cast sea glass** | Closed rounded coupon, Principled Transmission Weight 1, IOR 1.46 and a small roughness. Put a striped card *behind* it. The glass is not made by lowering alpha.[3] | Read the backing through the center and the refraction at the bevel. If it appears white, verify thickness, normals, background and transmission bounces. Use a volume absorption model if the reference specifically needs thickness-dependent color; this simple coupon does not model it. |
| **Woven linen** | Crossed Wave fields multiplied together → small color contrast and shallow Bump; Principled sheen produces a different grazing response. Use real draped geometry for the edge hanging over the gallery bench.[54][30][3] | The close view shows the illustrative weave; the distant shot should read as fabric from folds and edge thickness. If the weave shimmers in motion, reduce its contrast/frequency or bake/filter it instead of adding samples to every frame. |

#### Coordinates are a design decision

`Generated` coordinates fit an object's bounding box; `Object` coordinates can reference an object, while UVs follow the authored layout.[57] For equal-sized floor tiles across separately placed modules, use a shared coordinate reference or aligned UVs and agree which transform is authoritative. For an animation, use UVs or a coordinate frame attached to the part when the pattern must stay with it. A Mapping node transforms the incoming coordinates; the apparent texture motion depends on mapping type.[58] To diagnose a swimming or stretched pattern, render a numbered checker, move *just* the object or origin, then rerender. The library bakes dimensions into each coupon's mesh so its default local unit is meaningful.

#### Build up the surface in three scales

1. **Construction:** silhouettes, thickness, seams and intersections live in geometry if they affect the outline. 2. **Finish:** distinguish metal from oxide, paint from a bare edge or a wet patch from dry ground with a coverage mask. A wet ceramic patch generally needs different reflectance/roughness more than simply darker albedo. 3. **Microstructure:** bring in pores, scratches or weave last. Preview the scalar field before feeding the shader; `F1` Voronoi distance, its cell color and `Distance to Edge` are different signals, not interchangeable noise outputs.[56]

**Other style routes.** For hand-painted wood, keep large brush-shaped value groups, paint only the important edge accents and test with a neutral light. For anime architecture, reduce albedo variation around the focal outline; only distant facades should lose contrast. For real-time, bake the appearance needed by the target instead of exporting a tangle of Blender-only procedural nodes. Treat normal and roughness images as data, not display color; check the tangent basis and green-channel convention in the destination.[12][20] See the [game asset handoff](game-assets.md#chapter-game-art).

<a name="chapter-optical-surfaces"></a>

## Relief, surface history, glass and transmitted light

**By Noa3.** Choose a lighting test before picking a material. Use the same framing, exposure, backdrop and transform for both halves of a comparison. If something changes the silhouette, a shading normal alone is not enough. If the brief says “glows through”, first ask whether the object produces light or is lit from behind.

### Height, bump, normals, parallax and geometry

**Choose by what's visible.** Put a brick relief or a letterpress mark at the intended size. Save three views: face on, grazing, and in silhouette against white. A height image is a scalar, a tangent normal is a direction, and true displacement changes the surface; Blender distinguishes bump-only shading from geometric displacement.[12][30][364] Load a linear height or normal image as Non-Color. For a tangent-space normal, `Image Color → Normal Map Color → Principled Normal`; for height, `Image → Bump Height → Normal`. To combine them, feed the normal map result into `Bump Normal`. Do not feed a color-managed purple bitmap straight into a shader normal or normalize a height image like a vector.

**Parallax** is a view-dependent offset of sampling coordinates; a one-sample offset is not the same as a heightfield intersection search.[357] For an engine POM material, transform the view direction into tangent space; walk along that direction through normalized height layers, bracket the first crossing, refine the UV there. Sample albedo, roughness **and** detail normal at that same UV. Specify whether white means high; cap offsets near grazing angles, keep UV islands padded and fade the effect at distance. Compare the checker painted across the seam with the camera left and right. If the feature must break the actual mesh outline, cast a physical shadow or collide, use sufficient subdivision/displacement or explicit geometry. A Blender bump graph is not a portable POM shader; validate the consuming engine independently. Do not sell one-off view offsets as universal native Blender POM.

### A dirt map is a placement hypothesis

Adobe's Dirt generator uses baked mesh maps including curvature, AO, position and world-space normals to create a monochrome dirt mask; Blender's AO node measures occlusion, not dirt.[382][383] Use that distinction to tell a story: recess grime near a gasket, dust on upward-facing shelves, grease where a hand actually touches, rain dragging dirt *down from a source*. A polished button may be **cleaner** than its surround.

Build separate masks: `recess seed × noise breakup`, `up-facing weight × exposed area`, and a painted contact/cleaning exclusion. Invert an AO bake if white means unoccluded and cavities must receive grime. Preview each mask in emission before using it to blend base color, roughness and a very small height contribution. Test in a moving highlight; if the story vanishes without darkening the albedo, the finish is missing. For game delivery, bake wear at known UV scale, pad islands and test a lower mip. Reject equal rust on plastic, edge wear on every edge or ambient shadow permanently burned into the product label.

### Clear, frosted, tinted and layered glass

| Look | Build | Diagnostic and first correction |
|---|---|---|
| Clear drinking/architectural glass | Give the wall actual thickness and consistent outward normals; model a lip or bevel that catches a card. Use Glass BSDF or Principled transmission, and choose IOR for the specified material. Glass BSDF combines refraction and grazing reflection.[361] | Put black/white cards behind and to the sides. Blank glass may need something to reflect, not a higher IOR. Check duplicate faces, sealed air bubbles and the wall profile first. |
| Frosted or etched | Add surface roughness locally; fixed-scale micro-normal only where polishing or etching changes. Keep the opposite polished face distinguishable where appropriate. | Move the background pattern away from the sheet: the pattern should soften rather than simply darken. If everything looks like milky plastic, strip volume scattering off first. |
| Colored optical glass | Use a clear surface and `Volume Absorption → Material Output.Volume` on a closed volume; density controls absorption.[362] Model thick and thin sections using the same material. | Edge paths should attenuate differently from thin faces. If a tint looks painted on at both thicknesses, check units, density and whether the mesh encloses a volume before tinting albedo. |
| Laminated, coated or smoked glazing | For a close-up, separate the glass and interlayer with believable depth and no coincident faces. Use a coating only if two interfaces/highlights are actually needed. Treat smoked absorption and rough frosting independently. | Inspect two depths and a grazing reflection; compare the single-interface control first. Multiple sheets with coplanar surfaces create false black edges. For a distant facade a simplified exterior glass shell may read better and cost less. |

### Backlit sheet, thick scattering solid, or emitter?

For a thin paper lantern, leaf or shell, mix a front diffuse component and **Translucent BSDF** using a thickness/mask map; it supplies diffuse transmission, not clear refraction.[363] Put an actual light behind the sheet and switch it off: the transmitted component must lose its source. For thick wax or skin, use a closed model and scale-aware subsurface scattering under localized side/back light; changing radius is different from adding emission.[3] For an LED, hot filament or panel, use an emissive element with its housing, reflector and diffuser as separate surfaces; Blender's emission node has color and strength inputs.[386] Compositor glare is a lens/image effect and cannot make the housing receive the missing light. If the whole diffuser stays unnaturally bright with its internal source disabled, check for self-emission leaked into the diffuser graph.

**What was actually run:** [the optional backlight control](../scripts/probe_backlight.py) placed an ideal sheet in a black world with a single light behind it. In Blender 4.5.9 LTS Cycles, a central scene-linear RGB average went from **1.8423 to 0** when the backing lamp was disabled on the Translucent sheet; the opaque diffuse control was **0** in both cases and the emitter stayed at **0.6500**. These are relative pixel measurements in one diagnostic setup, not measurements of paper or a skin preset. The script uses a disposable empty background process and removes its temporary EXRs. It does not produce a film or modify an existing shot.

### Paper and posters: print master versus photographed object

Create the design as a flat master with actual type, margin, trim, live area and print-provider bleed. Adobe distinguishes extending artwork into bleed from placing crop marks that indicate trim.[380] Do not rely on a perspective render for a print-ready file. In Blender UV the *trimmed* rectangle, give the sheet a small bend and place curl/attachment according to glue, pins or clips; vary roughness between uncoated paper, glossy ink and foil. For a billboard use viewing distance and word hierarchy, not microscopic fibers. Check one straight-on proof for legibility and one raking-light detail for edges/shadows. If a TV/poster composite must preserve readable legal text, composite type from the master after framing rather than inventing sharpening detail.

### Sources

[3] https://docs.blender.org/manual/en/4.5/render/shader_nodes/shader/principled.html — Blender 4.5 LTS: Principled BSDF
[12] https://docs.blender.org/manual/en/4.5/render/shader_nodes/vector/normal_map.html — Normal Map Node - Blender 4.5 LTS Manual
[30] https://docs.blender.org/manual/en/4.5/render/shader_nodes/vector/bump.html — Bump Node - Blender 4.5 LTS Manual
[357] https://developer.nvidia.com/gpugems/gpugems2/part-i-geometric-complexity/chapter-8-pixel-displacement-mapping-distance-functions — Chapter 8. Per-Pixel Displacement Mapping with Distance Functions
[361] https://docs.blender.org/manual/en/4.5/render/shader_nodes/shader/glass.html — Glass BSDF - Blender 4.5 LTS Manual
[362] https://docs.blender.org/manual/en/4.5/render/shader_nodes/shader/volume_absorption.html — Volume Absorption - Blender 4.5 LTS Manual
[363] https://docs.blender.org/manual/en/4.5/render/shader_nodes/shader/translucent.html — Translucent BSDF - Blender 4.5 LTS Manual
[364] https://docs.blender.org/manual/en/4.5/render/materials/components/displacement.html — Displacement - Blender 4.5 LTS Manual
[380] https://helpx.adobe.com/ee/indesign/how-to/set-print-bleed.html — How to set a print bleed in InDesign
[382] https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/effects/generators/dirt — Dirt | Adobe Substance 3D Painter
[383] https://docs.blender.org/manual/en/4.5/render/shader_nodes/input/ao.html — Ambient Occlusion Node - Blender 4.5 LTS Manual
[386] https://docs.blender.org/manual/en/4.5/render/shader_nodes/shader/emission.html — Emission - Blender 4.5 LTS Manual

<a name="chapter-wear-and-finishing"></a>

## Worn surfaces, secondary motion and the final composite

**Author: Noa3.** Use a small repeatable shot: a painted station handrail emerging from shelter into rain. Keep the camera, exposure, light and frame the same between controls. Make a dry, clean baseline. The steps below are production exercises, not claims that the whole tram platform has physically simulated rain.

### Author the maps by asking what happened here

| What happened | Where it belongs | What proves it |
|---|---|---|
| Passengers rubbed paint smooth | Paint a broad hand-contact mask in UV space. Lower roughness locally before changing color at all. | A long reflected area light narrows on the grip, not on every upper edge. Move the light: the polished zone stays put, the highlight moves. |
| Paint chipped through to metal | Combine a sparse, hand-placed chip mask with fine breakup. Use it to select **two material states**: paint (dielectric) and exposed substrate. Keep primer as a separate layer if visible. | Inspect metallic as data, then the beauty. Bare conductive metal should not extend through intact paint. Don't turn rust metallic just because the substrate is iron. |
| Water and dirt ran downward | Paint drainage paths from a joint or lip, interrupted by ledges. Give sheltered undersides a different mask. Apply the wet response over the underlying paint, not in place of its history. | A duplicate under cover should not have the same wetness. A chip can be dry or wet. If every map is the same grayscale noise, the story is missing. |
| Fine nicks and larger damage broke the profile | Use height → Bump for fine relief, tangent normal for transferred detail, displacement with sufficient geometry or a modeled bevel for the outline. | Sweep a grazing light past the surface; compare the silhouette against the clean mesh. Bump alone should not carve the outline. |

**Make the maps, don't just wire them.** Unwrap the low mesh and inspect a numbered checker. Paint a unique contact mask on a named image; save or pack and reopen. For procedural roughness or metalness, route **one scalar** through Emission into an active Non-Color bake target and bake Emit in Cycles. For base color, bake unlit color into an sRGB target; never treat a lit beauty as albedo. Work each channel in isolation before packing channels for a particular export contract. The [Tide Register exercise](materials.md#chapter-texturing-workflow) includes two packed bakes you can inspect.[13]

For a high-to-low normal bake: keep a clean low mesh with final UVs and intended triangulation, plus an aligned high-detail source. On the low material(s) select the target Image Texture; select source(s) then the low object **last/active**. Choose Cycles **Normal**, **Tangent**, **Selected to Active**. Start with a small cage/extrusion; look for misses at deep recesses and projections from nearby pieces. Isolate a part or use a fitted cage before increasing ray distance indiscriminately. Save the map, reopen it as **Non-Color → Normal Map (Tangent, matching UV) → Principled Normal**. Inspect with a moving light on both sides of a UV seam. Don't flip green unless the receiving tangent convention actually requires it. Bake AO to its own non-color image if requested; do not bake it into albedo by default. Preserve a higher-precision linear height master before reducing bit depth. These are manual variations, not additional bakes claimed for the gauge.[12][13]

### Make the physics effect earn its cost

1. **Choose the observation.** Static damp floor? Shader and contact shadows may be enough. Drops crossing a backlight? Use sparse instanced drops or an emitter. A scarf hitting a shoulder? Use cloth, pinned where sewn, with a collision proxy. A tank filling and sloshing needs a different solver. Do not start a fluid domain for a still wet handrail.
2. **Establish scale and timing.** Set scene units, gravity and fps; lock the collision mesh and animation version. For cloth, start coarse with stable collision clearance, pin the sewn edge, run from the cache start, then compare the pin and a free corner before raising mesh density. Bake a final cache into a versioned path; reopen with the original build/cache location unavailable to catch missing dependencies.[19]
3. **For rain, separate emission, flight and impact.** Emit from a plane above the visible region; choose start/end, seed, parent count and lifetime so drops reach the surface. Make drop instances small relative to known geometry. Backlight the sweep; inspect silhouettes against both dark and bright surfaces. Add splashes only at surface hits and keep mist a separate contribution. A glint on a puddle does not prove a particle collision. For a loop compare birth, death and density on both sides of the seam.[315]
4. **Test the simplest mechanism first.** The included [rain probe](../scripts/rain_probe.py) evaluated a new 24-particle emitter in Blender 4.5.9. Frames 1/4/9/16 held 0/24/24/0 live drops. Between frames 4 and 9 they fell about 0.316 m on average under gravity and 0 m in the zero-gravity control. The locally generated [technical lab](lab-notebook.md#chapter-first-labs) shows a cloth strip dropping at its free corner while its pinned edge holds. These are solver checks, **not** a rendered rain simulation, collision or portable cache test.

### Finish in compositing without hiding mistakes

- Render a short sequence of multilayer scene-linear EXRs, not just an encoded movie. Keep a Combined baseline. Add only passes with a named job: Cryptomatte for a selective trim, Mist or depth for distance separation, emission or light groups to control lamps. Inspect the ungraded beauty, individual passes and alpha on a checker. A pass is not always a display-ready color image.[60]
- Set one view transform for shot review. Composite in scene-linear, keep the linear master, and apply the delivery view transform **once** to display output. Compare the bright metal edge and the dark figure under the same exposure. Put a matte over black **and** over white to catch alpha fringes. If glare makes a clock rod disappear, lower it or fix the bracket and its lighting; a grade cannot attach geometry.[11]
- Compare denoise on/off on crops of eyes, hair, fabric, railings and wet highlights. Play adjacent frames: sparkling roughness or a disappearing thin rod can pass on a still. Inspect the decoded delivery movie at normal speed, compare frame count, cadence and crop with the image sequence, and keep a silent or audio specification explicit. Never use bloom, depth of field or grain to conceal unsupported props or broken anatomy.

### Sources

[11] https://docs.blender.org/manual/en/4.5/render/color_management.html — Color Management - Blender 4.5 LTS Manual
[12] https://docs.blender.org/manual/en/4.5/render/shader_nodes/vector/normal_map.html — Normal Map Node - Blender 4.5 LTS Manual
[13] https://docs.blender.org/manual/en/4.5/render/cycles/baking.html — Render Baking - Blender 4.5 LTS Manual
[19] https://docs.blender.org/manual/en/4.5/physics/cloth/settings/cache.html — Cache - Blender 4.5 LTS Manual
[60] https://docs.blender.org/manual/en/4.5/render/layers/passes.html — Passes - Blender 4.5 LTS Manual
[315] https://docs.blender.org/manual/en/4.5/physics/particles/emitter/emission.html — Emission · Blender Manual 4.5
