#!/usr/bin/env python3
"""Fix a split GitLab project's own hub card links that still use the
unified created_with_eee project's absolute path structure.

gen_hub.py renders course-hub card links as page-relative paths (e.g.
`href="kapodistrias/"`), which resolve correctly from the unified repo's
own `modern_greek/b1greeklanguageandculture/index.html` on Codeberg/GitHub/
GitLab alike. A split GitLab project's root index.html was hand-adapted
from that same generated markup and can retain the source's absolute-path
form instead (`/created_with_eee/modern_greek/b1greeklanguageandculture/
kapodistrias/`) -- correct only on the unified project's own domain, a 404
on the split project's own domain (`eee-project.gitlab.io/created-with-eee-
b1glc/`, no `/created_with_eee/` prefix at all).

Usage:
    python3 tools/fix-split-hub-card-links.py \\
        --prefix /created_with_eee/modern_greek/b1greeklanguageandculture/ \\
        <split-project-checkout-dir> [...]

Run against a local checkout of a split course's `pages` branch. Prints
every file it changes; does not commit or push -- that stays a separate,
confirmed step.
"""
import argparse
import pathlib
import posixpath
import re

from _fix_common import run_fix


def relative_href(file_dir: str, suffix: str) -> str:
    """Compute the correct relative href from a file's own directory
    (file_dir, relative to the split project's root) to the logical target
    `suffix` (also relative to the split project's root) -- so a sub-hub's
    back-link to the root (suffix="") becomes "../", not "" (which would
    just reload itself).
    """
    rel = posixpath.relpath(suffix or ".", start=file_dir)
    if suffix.endswith("/") or not suffix:
        rel += "/"
    return rel


def fix_directory(target_dir: pathlib.Path, prefix: str) -> list[pathlib.Path]:
    """Rewrite href="{prefix}<suffix>" to a same-site-relative href, correct
    from each file's own directory depth. Returns the list of files
    actually changed.
    """
    pattern = re.compile(r'href="' + re.escape(prefix) + r'([^"]*)"')
    changed = []
    for html_file in sorted(target_dir.rglob("index.html")):
        text = html_file.read_text(encoding="utf-8")
        file_dir = html_file.parent.relative_to(target_dir).as_posix()
        new_text = pattern.sub(
            lambda m: f'href="{relative_href(file_dir, m.group(1))}"', text
        )
        if new_text == text:
            continue
        html_file.write_text(new_text, encoding="utf-8")
        changed.append(html_file)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--prefix", required=True,
        help="Absolute path prefix to strip, e.g. /created_with_eee/modern_greek/b1greeklanguageandculture/",
    )
    parser.add_argument(
        "target_dirs", nargs="+", type=pathlib.Path,
        help="One or more local checkouts of a split course's `pages` branch",
    )
    args = parser.parse_args()
    run_fix(args.target_dirs, lambda target_dir: fix_directory(target_dir, args.prefix))


if __name__ == "__main__":
    main()
