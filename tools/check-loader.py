#!/usr/bin/env python3
"""Check the loading overlay (tools/_loader.py) of the exported pages. Read-only (its self-test uses a temporary folder), no network, takes a second.

A lesson page (a page with the root div `<div id="root"></div>`) holds the overlay exactly once, before the root div, still with the style and the script that hide it, and has exactly one root div.
A hub page (made by gen_hub.py, no root div) holds no overlay: the script of the overlay waits for the root div, so on a hub it would cover the page for 150 s.

Usage:
    python3 tools/check-loader.py [PAGES_DIR ...]      # default: the Codeberg pages worktree next to this checkout

Run it on the Codeberg pages worktree before a deploy, and on the GitHub and GitLab checkouts after `make propagate-pages`.

Self-test: every run first applies the rules to made-up pages (a good one passes, each broken one fails), as tools/check-lesson-order.py does.

Exit status 0: every lesson page follows the rules; 1: a page breaks a rule; 2: nothing to check (a mistyped path never counts as a pass) or the self-test failed.
"""
import argparse
import pathlib
import sys
import tempfile

import _loader

DEFAULT_DIR = pathlib.Path(__file__).resolve().parent.parent.parent / "created_with_eee-pages-worktree"
SAMPLE = f"<html><head><title>A &amp; B</title></head><body>{_loader.ROOT}<script></script></body></html>"


def problems(page: str) -> "list[str]":
    """What is wrong with the overlay of one lesson page (a page with a root div)."""
    if page.count(_loader.ROOT) != 1:
        return [f"{page.count(_loader.ROOT)} root divs, expected 1"]
    if page.count(_loader.MARKER) != 1:
        return [f"{page.count(_loader.MARKER)} overlays, expected 1"]
    if page.index(_loader.MARKER) > page.index(_loader.ROOT):
        return ["the overlay stands after the root div"]
    before_root = page[:page.index(_loader.ROOT)]  # an overlay without its hide rule or its script would cover the lesson for ever
    if before_root.count("eee-ld-hidden") < 2 or not before_root.rstrip().endswith("</script>"):
        return ["the overlay is cut or changed: the style or the script that hides it is missing"]
    return []


def is_refused(page: str) -> bool:
    try:
        _loader.add_loader(page)
    except ValueError:
        return True
    return False


def self_test() -> "list[str]":
    """The names of the made-up cases that did not behave as expected."""
    good = _loader.add_loader(SAMPLE)
    overlay = _loader.LOADER.replace("%%TITLE%%", "x")
    evil = _loader.add_loader(SAMPLE.replace("A &amp; B", "&lt;script&gt;x"))
    with tempfile.TemporaryDirectory() as tmp:  # a made-up checkout: a right lesson page, a hub page that holds the overlay it must not hold, a clean hub page
        for name, text in (("lesson", good), ("hub", f"<html><body>{overlay}</body></html>"), ("clean-hub", "<html><body></body></html>")):
            (pathlib.Path(tmp) / name).mkdir()
            (pathlib.Path(tmp) / name / "index.html").write_text(text, encoding="utf-8")
        made_up = check(pathlib.Path(tmp))
    cases = {
        "a page with the overlay passes": problems(good) == [],
        "a page without the overlay fails": problems(SAMPLE) != [],
        "a page with two overlays fails": problems(good.replace(_loader.ROOT, overlay + _loader.ROOT)) != [],
        "a page with the overlay after the root div fails": problems(SAMPLE.replace(_loader.ROOT, _loader.ROOT + overlay)) != [],
        "a page whose overlay lost its script fails": problems(good.replace("<script>", "<!--").replace("</script>", "-->")) != [],
        "a page whose overlay lost its hide rule fails": problems(good.replace("#eee-loader.eee-ld-hidden", "#eee-loader.eee-ld-x")) != [],
        "a page with an empty overlay div fails": problems(SAMPLE.replace(_loader.ROOT, f"<div {_loader.MARKER}></div>" + _loader.ROOT)) != [],
        "a page with two root divs fails": problems(good.replace("<script></script>", _loader.ROOT)) != [],
        "adding the overlay twice changes nothing": _loader.add_loader(good) == good,
        "the title is shown as text": "<div class=\"eee-ld-title\">A &amp; B</div>" in good,
        "a title with markup is escaped": '<div class="eee-ld-title">&lt;script&gt;x</div>' in evil and "<script>x" not in evil,
        "a page with two root divs is refused": is_refused(SAMPLE.replace("<script></script>", _loader.ROOT)),
        "a page without a root div is refused": is_refused("<html><body></body></html>"),
        "a page that is fine is not refused": not is_refused(SAMPLE),
        "a hub page that holds the overlay is reported, a clean hub page is not": made_up == (1, 2, ["hub/index.html: a hub page holds the overlay"]),
    }
    return [name for name, ok in cases.items() if not ok]


def check(pages_dir: pathlib.Path) -> "tuple[int, int, list[str]]":
    """(lesson pages, hub pages, one message per broken rule) of one pages checkout."""
    lessons = hubs = 0
    broken = []
    for path in _loader.index_pages(pages_dir):
        rel = path.relative_to(pages_dir)
        page = path.read_bytes().decode("utf-8")
        if _loader.ROOT not in page:
            hubs += 1
            if _loader.MARKER in page:
                broken.append(f"{rel}: a hub page holds the overlay")
            continue
        lessons += 1
        broken += [f"{rel}: {problem}" for problem in problems(page)]
    return lessons, hubs, broken


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("pages_dirs", nargs="*", type=pathlib.Path, help="Pages checkouts to check (default: the Codeberg pages worktree)")
    args = parser.parse_args()

    failed = self_test()
    if failed:
        print("Self-test failed:", *failed, sep="\n  ", file=sys.stderr)
        sys.exit(2)
    status = 0
    for pages_dir in args.pages_dirs or [DEFAULT_DIR]:
        lessons, hubs, broken = check(pages_dir) if pages_dir.is_dir() else (0, 0, [])
        if not lessons:
            print(f"{pages_dir}: no lesson page found, nothing to check", file=sys.stderr)
            status = max(status, 2)
        elif broken:
            print(f"{pages_dir}: {len(broken)} problem(s) in {lessons} lesson page(s):", *broken, sep="\n  ")
            status = max(status, 1)
        else:
            print(f"{pages_dir}: ok, the overlay is in {lessons} lesson page(s), {hubs} hub page(s) have none")
    sys.exit(status)


if __name__ == "__main__":
    main()
