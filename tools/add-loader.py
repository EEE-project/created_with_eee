#!/usr/bin/env python3
"""Put the loading overlay (tools/_loader.py) into every exported lesson page below a pages checkout. Safe to re-run: a page that has the overlay is left alone.

`make export-notebooks` puts the overlay into each page it exports; this tool puts it into the pages exported before. A hub page (made by gen_hub.py, it has no root div)
is skipped. Only writes local files, never commits or pushes: review with `git status` and `git diff` in the checkout.

Usage:
    python3 tools/add-loader.py <pages-checkout>

Exit status 0: done; 1: a page has more than one root div; 2: no index.html below the checkout (a mistyped path never counts as done).
"""
import argparse
import pathlib
import sys

import _loader


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("pages_dir", type=pathlib.Path, help="Pages-branch checkout (Codeberg's, by convention)")
    args = parser.parse_args()

    pages = _loader.index_pages(args.pages_dir) if args.pages_dir.is_dir() else []
    if not pages:
        print(f"no index.html below {args.pages_dir}", file=sys.stderr)
        sys.exit(2)
    added = had = hubs = 0
    failed = []
    for path in pages:
        rel = path.relative_to(args.pages_dir)
        text = path.read_bytes().decode("utf-8")
        if _loader.MARKER in text:
            had += 1
        elif _loader.ROOT not in text:
            hubs += 1
        else:
            try:
                path.write_bytes(_loader.add_loader(text).encode("utf-8"))
                added += 1
                print(f"added: {rel}")
            except ValueError as err:
                failed.append(f"{rel}: {err}")
    print(f"\n{added} page(s) got the overlay, {had} had it, {hubs} hub page(s) skipped.")
    if failed:
        print("Failed:", *failed, sep="\n  ", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
