# Blender Workshop for Hermes Agent

Model, shade, animate, and verify Blender scenes. Blender Workshop gives Hermes ten field cards for modeling, materials, Geometry Nodes, rigging, rendering, and more. Each card gives you a next action, a concrete check, and what to try if the check fails.

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

## Find it in the Skills Hub

Add the GitHub repo as a search source (a tap), then search by name:

```sh
hermes skills tap add Noa3/Blender-Workshop
hermes skills search blender-workshop --source github
```

Adding the tap is optional. If search does not return the skill yet, the exact install command above still works. The skill also has a [public listing on skills.sh](https://skills.sh/noa3/blender-workshop/blender-workshop).

You can read the [field cards](skills/blender-workshop/references/field-cards.md) on GitHub without using Hermes.

Original workshop by Noa3. [MIT license](skills/blender-workshop/references/LICENSE.md).
