# Blender Workshop for Hermes Agent

Model, shade, animate, and verify Blender scenes. Blender Workshop gives Hermes ten field cards for modeling, materials, Geometry Nodes, rigging, rendering, and more. Each card gives you a next action, a concrete check, and what to try if the check fails.

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

The skill is a text workflow guide. Reading it does not require Blender, and installation adds no Blender add-on, scripts, or scenes. Check the version and render engine when applying steps to your scene.

## Blender showcase

Three original workshop stills rendered in Blender Cycles. They illustrate the kinds of work the field cards guide; the skill download itself contains only the guide.

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
