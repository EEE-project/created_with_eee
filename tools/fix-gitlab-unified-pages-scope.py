#!/usr/bin/env python3
"""Restore GitLab-unified-specific scope after resetting the `pages` branch
from Codeberg.

GitLab's `created_with_eee` project is **not** a byte-identical mirror of
Codeberg's `pages` branch, for two independent reasons:

1. Odyssey, Palaestra, and b1glc's child courses (kapodistrias/kavafis_ithaki/
   zorba) were split off into their own GitLab projects (1GB Pages-per-project
   cap -- see this repo's README). Their content must NOT exist under this
   project's own `pages` branch; the hub pages that link OUT to those split
   projects (`ancient_greek/index.html`,
   `modern_greek/b1greeklanguageandculture/index.html`, etc.) stay here, just
   not the lesson content itself -- and their cards must open the split
   projects' own GitLab Pages URLs: the hub generator writes Codeberg-style
   paths (`/created_with_eee/ancient_greek/odyssey/`) and relative links
   (`kapodistrias/`) that 404 here once the content is gone. gen_hub.py's
   `data-gitlab-href` script covers only some cards (Odyssey, Palaestra) and
   only with JavaScript; the three B1 course cards had no fix at all (5 dead
   cards found 2026-10-07), so the links themselves are rewritten here.
2. `.gitlab-ci.yml` is GitLab-only CI config that has never existed on
   Codeberg's `pages` branch at all (Codeberg/GitHub Pages don't need it).

A plain `git fetch codeberg pages && git reset --hard codeberg/pages` --
otherwise the correct, documented way to sync this branch (see
`~/work/greek/EEE/CLAUDE.md`'s "Git & Codeberg Integration") -- silently
undoes BOTH of these every time, because neither one exists in Codeberg's
own history to reset "back" to. This has regressed in production at least
twice (2026-08-12, 2026-08-27) before this script existed; both times the
symptom was identical: GitLab Pages either serves stale content indefinitely
(no CI pipeline gets queued -- `glab api .../pipeline` returns `{"message":
{"base":["Missing CI config file"]}}`) or starts re-serving the split
courses' own content from the wrong project entirely.

Usage:
    python3 tools/fix-gitlab-unified-pages-scope.py <gitlab-unified-pages-checkout-dir>

Run against a local checkout of GitLab's `created_with_eee` `pages` branch,
immediately after any `reset --hard codeberg/pages` there and before
committing. Idempotent -- safe to run even when nothing needs fixing.
Prints every change; does not commit or push -- that stays a separate,
confirmed step.
"""
import argparse
import pathlib
import posixpath
import re
import shutil
import sys

# Course directories that must never exist on GitLab's unified `pages`
# branch -- each has its own separate GitLab project instead. Paths are
# relative to the checkout root; the value is that project and the directory
# it serves at its own root.
SPLIT_COURSE_PROJECTS = {
    "ancient_greek/odyssey": ("created-with-eee-odyssey", "ancient_greek/odyssey"),
    "ancient_greek/palaestra": ("created-with-eee-palaestra", "ancient_greek/palaestra/ancient_greek.2026.summer"),
    "modern_greek/b1greeklanguageandculture/kapodistrias": ("created-with-eee-b1glc", "modern_greek/b1greeklanguageandculture"),
    "modern_greek/b1greeklanguageandculture/kavafis_ithaki": ("created-with-eee-b1glc", "modern_greek/b1greeklanguageandculture"),
    "modern_greek/b1greeklanguageandculture/zorba": ("created-with-eee-b1glc", "modern_greek/b1greeklanguageandculture"),
}
SPLIT_COURSE_DIRS = list(SPLIT_COURSE_PROJECTS)

PAGES_BASE = "https://eee-project.gitlab.io"
UNIFIED_ROOT = "/created_with_eee/"  # this project's own path prefix on gitlab.io, as the hub generator writes it
HREF = re.compile(r'href="([^"]*)"')

# Recovered from the project's own history (commit bfa30c4e) the last time
# this regressed -- Codeberg's `pages` branch has no equivalent file to
# source this from, so it's hardcoded here rather than fetched.
GITLAB_CI_YML = """\
pages:
  stage: deploy
  image: alpine:latest
  script:
    - mkdir .public
    - cp -r * .public/
    - mv .public public
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_BRANCH == "pages"
"""


def split_course_url(href: str, file_dir: str) -> str | None:
    """The split project URL that a hub link (written in a page under
    file_dir) into a removed course should open instead, or None for any
    other link -- including one that already is such a URL.
    """
    if href.startswith(UNIFIED_ROOT):
        path = href[len(UNIFIED_ROOT):]
    elif href.startswith(("/", "#")) or ":" in href:  # other absolute path, in-page anchor or full URL
        return None
    else:
        path = posixpath.normpath(posixpath.join(file_dir, href)) + ("/" if href.endswith("/") else "")
    bare = path.rstrip("/")
    for course_dir, (project, root) in SPLIT_COURSE_PROJECTS.items():
        if all(bare == d or bare.startswith(d + "/") for d in (course_dir, root)):
            return f"{PAGES_BASE}/{project}/{path[len(root):].lstrip('/')}"
    return None


def relink_hubs(target_dir: pathlib.Path) -> list[str]:
    """Point every link into a removed split course at that course's own
    GitLab project. Returns the pages changed.
    """
    changed = []
    for html_file in sorted(target_dir.rglob("index.html")):
        text = html_file.read_bytes().decode("utf-8")  # bytes round trip keeps the file's own line endings
        file_dir = html_file.parent.relative_to(target_dir).as_posix()
        new_text = HREF.sub(lambda m: f'href="{split_course_url(m.group(1), file_dir) or m.group(1)}"', text)
        if new_text != text:
            html_file.write_bytes(new_text.encode("utf-8"))
            changed.append(f"relinked {html_file.relative_to(target_dir).as_posix()}")
    return changed


def fix_checkout(target_dir: pathlib.Path) -> list[str]:
    """Remove split-course content, point the hub links at the split
    projects and restore .gitlab-ci.yml under target_dir. Returns a list of
    human-readable descriptions of what changed (empty if nothing needed
    fixing).
    """
    changed = []

    for rel in SPLIT_COURSE_DIRS:
        course_dir = target_dir / rel
        if course_dir.is_dir():
            shutil.rmtree(course_dir)
            changed.append(f"removed {rel}/")

    changed += relink_hubs(target_dir)

    ci_file = target_dir / ".gitlab-ci.yml"
    if not ci_file.exists() or ci_file.read_text(encoding="utf-8") != GITLAB_CI_YML:
        ci_file.write_text(GITLAB_CI_YML, encoding="utf-8")
        changed.append("wrote .gitlab-ci.yml")

    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("target_dir", type=pathlib.Path, help="Local checkout of GitLab's created_with_eee pages branch")
    args = parser.parse_args()

    if not args.target_dir.is_dir():
        print(f"not a directory: {args.target_dir}", file=sys.stderr)
        sys.exit(1)

    changed = fix_checkout(args.target_dir)
    for c in changed:
        print(c)
    print(f"\n{len(changed)} change(s) made." if changed else "\nAlready correct, nothing to do.")


if __name__ == "__main__":
    main()
