"""Look up a Blender field card or production subject. Standard library only; read-only."""
import argparse
import csv
import json
from pathlib import Path, PureWindowsPath
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
MANUAL = "Give the user one action and what to look for. Status: untested. Do not claim you ran Blender."
MODES = {
    "manual": MANUAL,
    "inspect": "Stay read-only. Describe only evidence you can actually inspect; otherwise report untested.",
    "edit": "Inspect first. Use an authorized copy, change one thing, then reopen or test the output. No evidence means untested.",
}


def load_cards():
    data = json.loads((ROOT / "assets" / "route-cards.json").read_text(encoding="utf-8"))
    return {card["id"]: card for card in data["cards"]}


def subject_text(terms):
    """Require all query words in one title/alias record; do not guess a topic."""
    def words(value):
        plain = unicodedata.normalize("NFKD", value.casefold())
        return set(re.findall(r"[^\W_]+", "".join(c for c in plain if not unicodedata.combining(c))))

    with (ROOT / "assets" / "production-subjects.tsv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if not terms:
        return "\n".join(f"{row['id']}: {row['title']}" for row in rows)
    query = words(" ".join(terms))
    exact = [row for row in rows if ' '.join(terms).casefold() == row['id']]
    matches = exact or [r for r in rows if query and query <= words(r['title'] + ' ' + r['aliases'])]
    if not matches:
        raise ValueError("No subject match. Run 'subject' without a query for the index.")
    return "\n\n".join(f"{r['title']}\nRead: references/{r['chapter']}\nCheck: {r['check']}" for r in matches)


def card_text(card, mode="manual", rule=MANUAL):
    lines = [f"Route: {card['id']} — {card['title']}", f"Mode: {mode}. {rule}",
             "Choose when: " + card["choose_when"], "Work one step at a time:"]
    lines.extend(f"{n}. {step}" for n, step in enumerate(card["actions"], 1))
    lines.extend(["Check: " + card["check"], "If it fails: " + card["if_failed"],
                  "Without tools: " + card["without_tools"], "Example: " + card["example"],
                  "Further reading (optional): " + card["read_more"]])
    return "\n".join(lines)


def first_step(card):
    return (f"Route: {card['id']}\nNext: {card['actions'][0]}\n"
            f"Look for: {card['first_check']}\nStatus: untested (instructions only).")


def check_handoff(path, cards):
    record = json.loads(path.read_text(encoding="utf-8"))
    fields = {"route", "mode", "status", "observation", "evidence", "next_step"}
    if not isinstance(record, dict) or set(record) != fields:
        raise ValueError("required fields: " + ", ".join(sorted(fields)))
    for key in fields - {"evidence"}:
        if not isinstance(record[key], str) or not record[key].strip():
            raise ValueError(f"{key} must be nonempty text")
    if record["route"] not in cards or record["mode"] not in MODES:
        raise ValueError("unknown route or mode")
    if record["status"] not in ("observed", "untested", "blocked"):
        raise ValueError("status must be observed, untested or blocked")
    evidence = record["evidence"]
    if not isinstance(evidence, list) or not all(isinstance(p, str) and p.strip() for p in evidence):
        raise ValueError("evidence must be a list of relative file names")
    if record["status"] == "observed" and (record["mode"] == "manual" or not evidence):
        raise ValueError("observed requires inspect/edit mode and a real evidence file")
    base = path.resolve().parent
    for name in evidence:
        rel = Path(name)
        if rel.is_absolute() or PureWindowsPath(name).drive or "\\" in name or ".." in rel.parts:
            raise ValueError("use a local relative path inside the handoff folder")
        target = (base / rel).resolve()
        if not target.is_relative_to(base) or not target.is_file() or target.stat().st_size == 0:
            raise ValueError(f"missing, empty or external evidence: {name}")
    return f"Handoff structure and evidence paths accepted ({record['status']}); not a Blender verification."


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers(dest="command", required=True)
    cards = load_cards()
    actions.add_parser("list", help="list route IDs and when to choose them")
    subject = actions.add_parser("subject", help="find a production recipe and its acceptance check; omit words to list subjects")
    subject.add_argument("words", nargs="*")
    step = actions.add_parser("step", help="give one action and an immediate check without invoking a model")
    step.add_argument("route", choices=cards)
    card = actions.add_parser("card", help="print one copyable card")
    card.add_argument("route", choices=cards)
    card.add_argument("--mode", choices=MODES, default="manual")
    card.add_argument("--json", action="store_true", help="output structured data instead of text")
    check = actions.add_parser("check", help="check a handoff record and local evidence paths, not scene quality")
    check.add_argument("report", type=Path)
    args = parser.parse_args()
    if args.command == "list":
        print("\n".join(f"{key}: {item['choose_when']}" for key, item in cards.items()))
    elif args.command == "subject":
        try:
            print(subject_text(args.words))
        except ValueError as exc:
            parser.exit(2, f"{exc}\n")
    elif args.command == "step":
        print(first_step(cards[args.route]))
    elif args.command == "check":
        try:
            print(check_handoff(args.report, cards))
        except (ValueError, OSError, RuntimeError) as exc:
            parser.exit(2, f"Invalid handoff: {exc}\n")
    elif args.json:
        print(json.dumps({"schema_version": 1, "mode": args.mode, "instruction": MODES[args.mode],
                          "card": cards[args.route]}, indent=2, ensure_ascii=False))
    else:
        print(card_text(cards[args.route], args.mode, MODES[args.mode]))


if __name__ == "__main__":
    main()
