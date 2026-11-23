import csv
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SLUG = "blender-workshop"
REPO = "Noa3/Blender-Workshop"
SKILL = ROOT / "skills" / SLUG
LINK = re.compile(r"\]\(<?([^\s)>]+)")


class PublicBundleTest(unittest.TestCase):
    def test_public_payload_contains_only_readable_source(self):
        paths = list(SKILL.rglob("*"))
        self.assertFalse(any(p.is_symlink() for p in paths))
        files = [p for p in paths if p.is_file()]
        self.assertLessEqual(len(files), 50, "Keep the Hub bundle within its file-count budget")
        for path in files:
            with self.subTest(path=path.relative_to(SKILL)):
                self.assertIn(path.suffix, {".md", ".py", ".json", ".tsv"})
                self.assertLessEqual(path.stat().st_size, 256 * 1024)
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("\x00", text)
                self.assertNotRegex(text, r"^BLENDER[_-]?[vV]?\d{3}")
                self.assertNotRegex(text, r"/home/[^\s`]+/|/run/media/|\.hermes/profiles/")

    def test_skill_entry_points_to_the_expanded_library(self):
        entry = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = entry.split("---\n", 2)[1].splitlines()
        self.assertIn(f"name: {SLUG}", frontmatter)
        self.assertIn("license: MIT", frontmatter)
        self.assertTrue(
            {"references/field-cards.md", "references/LICENSE.md", "references/workshop-index.md",
             "references/production-atlas.md", "scripts/workshop.py"} <= set(LINK.findall(entry))
        )
        for path in SKILL.rglob("*"):
            if path.is_file() and path.name != "SKILL.md":
                self.assertIn(path.relative_to(SKILL).as_posix(), LINK.findall(entry),
                              "List support files explicitly for link-driven installers")

    def assert_local_target(self, page, link):
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return
        to = (page.parent / unquote(parsed.path)).resolve()
        boundary = ROOT if page == ROOT / "README.md" else SKILL
        self.assertTrue(to.is_relative_to(boundary), (page, link))
        self.assertTrue(to.is_file(), (page, link))
        if parsed.fragment and parsed.fragment.startswith("chapter-"):
            self.assertIn(f'name="{parsed.fragment}"', to.read_text(encoding="utf-8"), (page, link))

    def test_document_links_stay_inside_the_download(self):
        for page in [ROOT / "README.md", *SKILL.rglob("*.md")]:
            for link in LINK.findall(page.read_text(encoding="utf-8")):
                self.assert_local_target(page, link)

    def test_field_cards_keep_the_ten_routes(self):
        cards = (SKILL / "references/field-cards.md").read_text(encoding="utf-8")
        self.assertEqual(
            re.findall(r"^## (\w+) — ", cards, re.MULTILINE),
            ["model", "architecture", "material", "procedural", "game", "animation",
             "anime", "render", "rigging", "composite"],
        )

    def test_subject_lookup_finds_a_verified_chapter_link_without_blender(self):
        with (SKILL / "assets/production-subjects.tsv").open(encoding="utf-8", newline="") as source:
            rows = list(csv.DictReader(source, delimiter="\t"))
        self.assertGreaterEqual(len(rows), 74)
        self.assertEqual(len({row["id"] for row in rows}), len(rows))
        for row in rows:
            self.assert_local_target(SKILL / "SKILL.md", f"references/{row['chapter']}")
        for query, check_fragment in (("horse", "hoof contact"), ("Haaransatz", "root")):
            with self.subTest(query=query):
                output = self.workshop("subject", query)
                self.assertIn("Read: references/", output)
                self.assertIn(check_fragment, output.lower())

    def test_card_and_handoff_use_the_installed_data(self):
        output = json.loads(self.workshop("card", "procedural", "--json"))
        self.assertEqual(output["mode"], "manual")
        self.assertEqual(output["card"]["id"], "procedural")
        self.assert_local_target(SKILL / "SKILL.md", output["card"]["read_more"])
        self.assertIn("(untested)", self.workshop("check", str(SKILL / "templates/handoff.json")))

    def workshop(self, *args):
        return subprocess.check_output(
            [sys.executable, "-B", str(SKILL / "scripts/workshop.py"), *args],
            cwd=ROOT, text=True, timeout=10,
        )

    def test_readme_uses_the_public_install_identifier(self):
        readme = ROOT / "README.md"
        self.assertTrue(readme.is_file(), "The public installation guide is missing")
        text = readme.read_text(encoding="utf-8")
        self.assertIn(f"hermes skills install {REPO}/skills/{SLUG}", text)
        self.assertIn(f"/{SLUG} Plants from my Geometry Nodes", text)
        self.assertNotIn("blender-werkstatt", text)
