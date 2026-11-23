# Game assets and retro looks

Original workshop writing by Noa3. Earlier lab measurements describe the stated fixture, not the reader’s scene.

- [Design the game asset from the player camera backwards](#chapter-game-art)
- [Retro graphics, reimaginings and machinery that belongs in its world](#chapter-retro-and-machines)

<a name="chapter-game-art"></a>

## Design the game asset from the player camera backwards

Start with a contract, not a triangle count. Record **purpose**, normal viewing distance/coverage in pixels, target device and renderer, scale, pivot, interaction, expected simultaneous copies and texture limits. A hand-held hero item and a row of 100 corridor lamps need different tradeoffs. No target supplied? State one illustrative target and separate measured facts from suggested budgets.

### From sketch to handoff

1. **Choose a silhouette and a point of contact.** For a portable lamp, preserve the handle opening, body/foot separation and a lens large enough to read at gameplay size. Mark the bottom-center pivot and grasp point before increasing topology. Place it next to a known-size object in a test level. A bright emissive panel should be a visual cue even if the runtime does not let it cast light.
2. **Define clean construction.** Split the editable source by function; keep the low-poly export's material count intentional. Model silhouette, occluding shapes and prominent bevels; prefer a bake or texture for flush screws, markings and distant seams. If using a high-to-low bake, agree on triangulation, normal map space and seams, use a cage or explicit ray-distance settings, and inspect both sides of narrow gaps.[13][12]
3. **Assign UVs for the way the asset is seen.** Check a numbered square grid, orient prominent faces and budget more area for near/readable ones. Share mirrored islands only when the art is truly symmetric. Give atlases padding at the smallest mip that will be sampled; test a reduced texture, not just the authoring sheet. A tileable trim sheet suits repeated architectural edges, an atlas suits many small related surfaces and a unique set suits a close hero. The course shows a checker before painting.[69]
4. **Choose a portable material response.** Metallic–roughness glTF describes base color and surface parameters, not an arbitrary Blender node graph.[20][63] For core glTF the metallic–roughness texture stores **roughness in G** and **metallic in B** as linear data; base-color texture encoding is distinct. glTF uses meters and a right-handed coordinate system. Inspect the *exported* axes rather than manually rotating a mesh twice.[74] Keep the export free of backing planes, cameras and collision meshes unless the runtime convention explicitly asks for them.
5. **Author LODs from the same source at the same pivot.** LOD1 should remove small bevel loops, interior recess detail or small markings before narrowing the handle opening. Compare identical framing and the screen size near a switch. A reduction percentage is meaningless if the silhouette jumps, the anchor moves or a material is replaced by accident.
6. **Give physics its own representation.** Start with simple convex shapes for rigid interactive props; use several if an important opening must remain traversable. A single convex hull around a handle closes its hole by design. For static scene geometry, Godot also supports importer-specific collision naming (`-colonly`, `-convcolonly`); these are not promises in the generic glTF standard.[65] Test both a ray that should hit and an offset ray that should miss. If players must reach through a hole, add a third ray *through the hole*.

### Which quality bar?

| Use | Spend on | Practical acceptance |
|---|---|---|
| Repeated background prop | Few material changes, instancing when the runtime supports it, shared maps and simple collision | Silhouette clear at typical distance, no sparkle at mip/LOD transitions; measure frame time with the expected copy count. |
| Near, interactive desktop prop | Grip clearance, action pivot, visible edges, believable highlight and named parts if animation requires them | Looks correct held and at rest; UVs survive import; motion and physics meaningfully match play. Record units and renderable mesh bounds. |
| Hero asset / close inspection | Clean topological shading, sharper texture allocation on focal features, readable material separation and a disciplined source mesh | Rotating grazing light reveals no waves on flat panels; logo and other unique marks are legible at actual output. A portfolio render does not validate game performance. |

**Count after export.** UV seams and hard normals may split render vertices. Count exported triangles and material primitives, not only edit-mode polygons; GPU draw calls depend on renderer, batching, passes and copies.[20] Godot's automatic mesh LOD uses a screen-space metric; two separate `.glb` files do not configure automatic LOD just by existing.[64] Make an explicit game-side policy or use the target importer's LOD feature, then test resolution, field of view and motion at the transition.

**Independent proof.** In the original workshop test, Godot's runtime document reader imported the actual mesh arrays. The test built convex physics shapes from the isolated proxy and ran a hit/miss pair during a physics step.[75][76][77] This was an integration smoke test, not a benchmark or proof of GPU visual parity. See [advanced lab results](lab-notebook.md#chapter-advanced-labs) for the scope and repeat the checks with your own assets.

<a name="chapter-retro-and-machines"></a>

## Retro graphics, reimaginings and machinery that belongs in its world

**By Noa3.** Write down what the audience should recognize before adding a retro filter or calling the asset futuristic. Use a color thumbnail, a moving camera and one functional detail as three different tests. These are design workflows; no era-accurate hardware implementation is claimed.

### PS1 versus PS2: choose a particular game and signal path

The original PlayStation's affine texture interpolation can warp a slanted surface; quantized vertex placement and texture warping are different artifacts, and dithering is another choice entirely.[376] For a PS1-inspired asset start with a low-polygon silhouette, deliberate triangulation, small painted textures, limited value ramps and a low internal render resolution scaled to the delivery size. In Blender an Image Texture can use Closest interpolation; this reproduces nearest sampling, **not** affine interpolation or vertex snapping.[387] Exaggerate only the artifact present in your reference. For actual affine mapping in a suitable target shader, interpolate UV without perspective correction; an offline visual approximation is not console emulation. Compare a diagonal checker during a gentle dolly. If the checker swims while the mesh is entirely still under a static camera, that is not useful PS1 character.

The PlayStation 2 Graphics Synthesizer applies perspective correction and supports bilinear/trilinear filtering with mipmaps; do not simply turn PS1 wobble up and rename it PS2.[377] Identify one game's geometry density, painted/baked lighting, vertex colors, alpha cards, fog distance and composited effects. In Blender block with modest geometry, author selective bevels and texture density, and light to the original scene's value groups. Separate display/scanline simulation from asset art: export a clean render first, then compare a delivery-display treatment. Tests: static close-up for palette/UV filtering, face or wheel silhouette in motion, distant clutter, a second camera that reveals where detail runs out. There is no universal PS1/PS2 triangle count or native presentation resolution for every title.

### Remaster, remake or reimagination?

Define the promise for *this* audience with a side-by-side board: **keep**, **translate**, **reinterpret**. A remaster brief might prioritize original geometry, camera and timing with cleaner presentation. A remake can rebuild form and materials while retaining a landmark, color hierarchy and emotional beat. A reimagination can deliberately change them, but should identify what still makes the work recognizable. These are working definitions, not a consumer survey. In the Resident Evil 4 remake interview, producer Yoshiaki Hirabayashi stresses respect for the original while noting different players cherish different things.[370]

Pick one iconic angle, one traversal or performance beat and one nuisance the old constraints imposed. Compare the new composition at the original shot's size and with sound off. Ask a returning viewer *what they recognized* and a newcomer *where they would look or go*. If the landmark vanishes behind physically correct clutter, restore its value and shape hierarchy rather than copying every polygon. Do not present a small feedback test as proof of what all fans want, or reproduce protected designs/assets without appropriate rights.

### Sci-fi, vintage and retrofuturism

“Vintage” specifies a time, available fabrication and a use history; “sci-fi” specifies what the imagined technology can do. They are not opposites. Design one working panel three ways: stamped metal, replaceable engraved plates, incandescent indicator and captive screws for a chosen historical reference; sealed modules, service hatches and embedded displays for one future; old housings retrofitted with future electronics for a hybrid. Put one access operation in the shot. Assign wear to the grip and replaceable part, not every bevel. Test a monochrome silhouette and remove labels: if the two eras are only sepia versus neon, revisit construction and interface logic.

### Grounded and game-readable spacecraft

On Voyager the antenna pointing, science instruments and command/attitude subsystems are visibly related to mission requirements.[372] For an original grounded spacecraft, write a mission first: where does it collect energy, reject heat, observe, communicate and dock? Block the craft and the clear fields of view of dish, instrument and radiator. Add service panels and insulation only after that layout makes sense. Give specular fragments a controlled size against a dark background, and check that the craft still reads from its intended solar direction. For a game-like ship, preserve these cues but exaggerate orientation, silhouette and faction color at play distance; make the thruster axis, camera side and collision proxy intentional. Compare one still hero image **and** a moving player-sized silhouette. Detail budgets and silhouettes of real craft are references, not requirements for fictional propulsion.

### Robots: hard shell, soft joint, readable performance

Choose industrial manipulator, humanoid service robot, toy, or graphic mecha. Name the task, reach, support polygon and service access; block the mechanism with rigid links and pivot axes. Sweep each joint to both working extremes *before* fitting shells. For a service robot leave room for cables/bellows and human controls; for an industrial arm read axis order and end-effector; for anime mecha favor characteristic limb proportions and clear joint silhouettes. Use hinge parents/limits for truly rigid pieces, a deform rig for bellows, and shape correctives only where a real flexible cover could stretch. Verify shielding/cables do not pass through the joint in the mid-pose, and that the stand/feet carry the load. Changing armor scale, line weight and value grouping should create style, not conceal a broken pivot.

### Sources

[370] https://www.gamepressure.com/newsroom/interview-yoshiaki-hirabayashi-about-resident-evil-4-remake/z75297 — Out of Love to Original. Interview with Yoshiaki Hirabayashi about Resident Evil 4 Remake
[372] https://science.nasa.gov/mission/voyager/spacecraft — Spacecraft - NASA Science
[376] https://www.copetti.org/writings/consoles/playstation — PlayStation Architecture | A Practical Analysis
[377] https://www.copetti.org/writings/consoles/playstation-2 — PlayStation 2 Architecture
[387] https://docs.blender.org/manual/en/4.5/render/shader_nodes/textures/image.html — Image Texture Node - Blender 4.5 LTS Manual
