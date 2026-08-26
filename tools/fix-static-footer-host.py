#!/usr/bin/env python3
"""Fix static (non-WASM) hub pages whose footer "Source" link is hardcoded
to Codeberg, regardless of which host is actually serving the page.

Hub pages (root, subject-level, and course-level index.html files) are
plain static HTML -- unlike session/lesson pages, they never run Python/
Pyodide, so eee-project's host-aware `eee_footer()` fix (see
notebook_utils.py's `_source_host_base()`) can never reach them no matter
what version is on PyPI. Each one bakes in a literal
`<a href="https://codeberg.org/EEE-project" ...>codeberg.org/EEE-project</a>`
at whatever time it was last built/patched, correct by default for
Codeberg but wrong everywhere else until patched by hand.

Usage:
    python3 tools/fix-static-footer-host.py --host https://github.com/EEE-project <dir> [...]
    python3 tools/fix-static-footer-host.py --host https://gitlab.com/EEE-project <dir> [...]

Run against a local checkout of a `pages` branch (unified or a split
GitLab project). Prints every file it changes; does not commit or push --
that stays a separate, confirmed step.
"""
import argparse
import pathlib

from _fix_common import run_fix

CODEBERG_LINK = (
    '<a href="https://codeberg.org/EEE-project" target="_blank">'
    "codeberg.org/EEE-project</a>"
)


def fix_directory(target_dir: pathlib.Path, host_base: str) -> list[pathlib.Path]:
    """Rewrite the hardcoded Codeberg footer link to host_base in every
    index.html under target_dir. Returns the list of files actually changed.
    """
    label = host_base.removeprefix("https://")
    new_link = f'<a href="{host_base}" target="_blank">{label}</a>'

    changed = []
    for html_file in sorted(target_dir.rglob("index.html")):
        text = html_file.read_text(encoding="utf-8")
        if CODEBERG_LINK not in text:
            continue
        html_file.write_text(text.replace(CODEBERG_LINK, new_link), encoding="utf-8")
        changed.append(html_file)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--host", required=True,
        help="Target org URL, e.g. https://github.com/EEE-project or https://gitlab.com/EEE-project",
    )
    parser.add_argument(
        "target_dirs", nargs="+", type=pathlib.Path,
        help="One or more local checkouts of a `pages` branch (unified or a split GitLab project)",
    )
    args = parser.parse_args()
    run_fix(args.target_dirs, lambda target_dir: fix_directory(target_dir, args.host))


if __name__ == "__main__":
    main()
