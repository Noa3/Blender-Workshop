# Blender Workshop for Hermes Agent

Model, shade, animate, and verify Blender scenes. Start with ten field cards for choosing a next action, then use the workshop library for detailed workflows, source notes, and reproducible checks.

[Install and try it](#install-and-try-it) · [See the Blender showcase](#blender-showcase)

## Install and try it

With [Hermes Agent](https://hermes-agent.nousresearch.com/docs/) installed, run these in the profile you use for chat:

```sh
hermes skills inspect Noa3/Blender-Workshop/skills/blender-workshop
hermes skills install Noa3/Blender-Workshop/skills/blender-workshop
```

Review the source and the install prompt. In a new Hermes chat, try:

```text
/blender-workshop Plants from my Geometry Nodes setup are scattered on a path. No Blender tools are available. Give me one action and one check.
```

Expected: choose `procedural`, preview the placement mask before instancing, and check that it excludes the path but includes the planting bed. This is guidance, not a verified Blender edit.

### What's included

- A [workshop library](skills/blender-workshop/references/workshop-index.md) with workflows for modeling, texturing and UVs, Geometry Nodes, animation, rigging, rendering, and delivery.
- A [production atlas](skills/blender-workshop/references/production-atlas.md) with checks for specific subjects, plus an offline topic finder that runs on standard Python.
- The [creator notebook](skills/blender-workshop/references/channel-register.md), [video study notes](skills/blender-workshop/references/video-study-notes-01.md), and source links. The notes distinguish narration, sampled previews, written descriptions, and original workshop experiments.
- [Optional local lab scripts](skills/blender-workshop/references/portable-use.md) you can run separately with Blender, including a build-and-check exercise for the Tide Register gauge.

**No `.blend` scenes are downloaded or installed.** The skill contains documentation, reference data, and Python source. It installs no Blender add-on and runs no lab automatically. Optional labs create their fixtures locally when you run them, rather than fetching project files. The preview images below stay in the repository, outside the skill download.

## Blender showcase

Three original workshop stills rendered in Blender Cycles. They illustrate the techniques covered by the guide; the editable scenes are not part of the public release.

### Night Current — Jellyfish

![An amber jellyfish with a translucent bell and fine trailing tentacles in deep blue water](docs/showcase/night-current.webp)

**Organic modeling and translucency.** The backlight keeps the folds visible through the bell and separates the fine tentacles from the blue water.

### Last Dispatch at Lumen Quay — Tram terminus

![A red tram under a glass station canopy, with a seated reader and warm lights reflected on the wet platform](docs/showcase/last-dispatch-at-lumen-quay.webp)

**Scene composition and wet materials.** The roof ribs lead toward the tram, and the warm pools of light make the platform read as wet without hiding the destination sign.

### Meridian No. 04 — Compass-style navigator

![A brass navigator with a teal dial, red needle, crisp graduations, and a knurled rim](docs/showcase/meridian-no-04.webp)

**Hard-surface modeling and product lighting.** The red needle leads the eye across the dial, while the edge light shows the case profile and knurling without washing out the graduations.

## Find it in the Skills Hub

Add the GitHub repo as a search source (a tap), then search by name:

```sh
hermes skills tap add Noa3/Blender-Workshop
hermes skills search blender-workshop --source github
```

Adding the tap is optional. If search does not return the skill yet, the exact install command above still works. The skill also has a [public listing on skills.sh](https://skills.sh/noa3/blender-workshop/blender-workshop).

You can read the [field cards](skills/blender-workshop/references/field-cards.md) on GitHub without using Hermes.

Original workshop by Noa3. [MIT license](skills/blender-workshop/references/LICENSE.md).
