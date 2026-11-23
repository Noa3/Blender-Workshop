# Read the workshop or run a local exercise

Start with the [field cards](field-cards.md) or the [library](workshop-index.md). To use a card in another chat tool, copy it as text and describe the brief and the tools that are actually available. A response without scene evidence should say `untested`.

## Offline commands

Run these from the installed skill directory, or from `skills/blender-workshop/` in a checkout. The command uses Python 3.9+ and only the standard library. It reads its bundled index and does not open Blender, modify scenes, install anything, or contact a service.

```sh
python3 scripts/workshop.py list
python3 scripts/workshop.py subject horse
python3 scripts/workshop.py step procedural
python3 scripts/workshop.py card game --mode inspect --json
python3 scripts/workshop.py check templates/handoff.json
```

`subject` prints a matching chapter link and acceptance check. Search without a query to see the topic list. `check` validates a handoff record and its local evidence paths, not the quality or origin of the evidence. For `observed` use `inspect` or `edit` mode with a real, nonempty evidence file relative to the report. Keep `untested` if the scene was not checked.

## Optional Blender labs

The [lab notebook](lab-notebook.md) describes the study controls and what was measured. Run a generator only when you want to create a local study. It is separate from installation. Work in a fresh background process and point output at a new directory. Do not load a user's open scene into a generator. The reference environment for these exercises is Blender 4.5.9 LTS. Some rendering tests require a working Cycles or EEVEE graphics setup.

For a lightweight modeling check, compare welded and unwelded instances in memory:

```sh
blender --background --factory-startup --disable-autoexec --python-exit-code 1 \
  --python scripts/mirror_seam.py -- compare
```

Expected: `MIRROR_SEAM` with measurements for three variants. Judge seam vertices, not just whether the front camera hides a gap.

### Tide Register

Build the animated gauge locally to try both UV placement and pivot motion. No textures, add-ons or scene files need to be downloaded. Run both commands in separate Blender processes:

```sh
OUT=$(mktemp -d)
blender --background --factory-startup --disable-autoexec --python-exit-code 1 \
  --python scripts/build_tide_register.py -- "$OUT/Tide-Register.blend"
blender --background --factory-startup --disable-autoexec --python-exit-code 1 \
  --python scripts/check_tide_register.py -- "$OUT/Tide-Register.blend"
```

The second run should print `TIDE_CHECK` with motion and baked-texel readings. Open the generated scene and compare frames 10 and 34: the print should follow the needle and the needle should stay on its spindle. Those two frames do not prove that the loop plays smoothly; check playback separately.

### Using the Blender Python module

If you already have a separate Python environment with Blender's `bpy` 4.5.9 package, you can run the same scripts with that interpreter. For example, set `PY` to its Python executable, then run `"$PY" -IB scripts/mirror_seam.py compare`. Do not confuse Blender’s Python environment with the standard-library topic finder. The [first labs](lab-notebook.md#chapter-first-labs) document setup and output checks for the larger exercises.
