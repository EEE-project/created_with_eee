#!/usr/bin/env python3
"""Fix WASM session pages whose embedded _ROOT still points at Codeberg
after their course was split off to its own GitLab Pages project.

marimo's `export html-wasm` bakes the notebook's `_ROOT` variable (the raw
Codeberg URL used to fetch index.tsv/ga.json at runtime) verbatim into the
exported index.html -- **twice**: once as plain text, once URL-percent-
encoded (used by a "view source" style link). Pushing new data to a
different branch never touches either copy; only re-exporting the
notebook or patching the deployed HTML does. When a course is split off
to its own GitLab project, its session pages keep fetching from
Codeberg's raw endpoint unless both embedded copies are rewritten to
GitLab's raw endpoint instead -- at which point they pick up whatever
`index_url` that course's index.tsv already has on GitLab's own main
branch (fix that data first; this script only fixes which host the page
fetches it from).

Usage:
    python3 fix-split-session-root.py <split-project-checkout-dir> [...]

Run against a local checkout of a split course's `pages` branch (e.g.
`~/work/greek/git/gitlab/EEE-project/created-with-eee-<course>`) *after*
copying/committing the exported WASM pages there. Prints every file it
changes; does not commit or push -- that stays a separate, confirmed step.
"""
import argparse
import pathlib
import sys

OLD_PLAIN = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
NEW_PLAIN = "https://gitlab.com/EEE-project/created_with_eee/-/raw/main"

OLD_ENCODED = (
    "https%3A%2F%2Fcodeberg.org%2FEEE-project%2Fcreated_with_eee"
    "%2Fraw%2Fbranch%2Fmain"
)
NEW_ENCODED = (
    "https%3A%2F%2Fgitlab.com%2FEEE-project%2Fcreated_with_eee"
    "%2F-%2Fraw%2Fmain"
)


def fix_directory(target_dir: pathlib.Path) -> list[pathlib.Path]:
    """Rewrite both embedded _ROOT copies in every index.html under target_dir.

    Returns the list of files actually changed.
    """
    changed = []
    for html_file in sorted(target_dir.rglob("index.html")):
        text = html_file.read_text(encoding="utf-8")
        if OLD_PLAIN not in text and OLD_ENCODED not in text:
            continue
        new_text = text.replace(OLD_PLAIN, NEW_PLAIN).replace(OLD_ENCODED, NEW_ENCODED)
        html_file.write_text(new_text, encoding="utf-8")
        changed.append(html_file)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "target_dirs", nargs="+", type=pathlib.Path,
        help="One or more local checkouts of a split course's `pages` branch",
    )
    args = parser.parse_args()

    total = 0
    for target_dir in args.target_dirs:
        if not target_dir.is_dir():
            print(f"skip (not a directory): {target_dir}", file=sys.stderr)
            continue
        changed = fix_directory(target_dir)
        for f in changed:
            print(f"fixed: {f}")
        total += len(changed)

    print(f"\n{total} file(s) changed.")


if __name__ == "__main__":
    main()
