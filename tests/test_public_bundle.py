import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "blender-workshop"
REPO = "Noa3/Blender-Workshop"


class PublicBundleTest(unittest.TestCase):
    def test_public_payload_is_self_contained(self):
        skill = ROOT / "skills" / SLUG
        expected = {"SKILL.md", "references/field-cards.md", "references/LICENSE.md"}
        paths = list(skill.rglob("*"))
        self.assertEqual(
            {p.relative_to(skill).as_posix() for p in paths if p.is_file()}, expected
        )
        self.assertFalse(any(p.is_symlink() for p in paths))
        entry = (skill / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = entry.split("---\n", 2)[1].splitlines()
        self.assertIn(f"name: {SLUG}", frontmatter)
        self.assertIn("license: MIT", frontmatter)
        self.assertEqual(
            set(re.findall(r"\]\(([^)\s]+)\)", entry)), expected - {"SKILL.md"}
        )
        cards = (skill / "references/field-cards.md").read_text(encoding="utf-8")
        self.assertEqual(
            re.findall(r"^## (\w+) — ", cards, re.MULTILINE),
            ["model", "architecture", "material", "procedural", "game", "animation",
             "anime", "render", "rigging", "composite"],
        )
        self.assertNotRegex(cards, r"\]\([^)]+\)")

    def test_readme_uses_the_public_install_identifier(self):
        readme = ROOT / "README.md"
        self.assertTrue(readme.is_file(), "The public installation guide is missing")
        text = readme.read_text(encoding="utf-8")
        self.assertIn(f"hermes skills install {REPO}/skills/{SLUG}", text)
        self.assertIn(f"/{SLUG} Plants from my Geometry Nodes", text)
        self.assertNotIn("blender-werkstatt", text)
