#!/usr/bin/env python3
"""Copy a freshly re-exported WASM session from Codeberg's pages worktree
into the other hosts' local checkouts.

`tools/export-notebooks.py` writes into ONE pages-branch worktree (Codeberg's,
by Makefile default) -- the export itself is host-portable, so the same
bytes just need to land in GitHub's, GitLab-unified's, and (for split-off
courses) the matching GitLab split project's checkout too, before each is
committed and pushed by hand. This step used to be a manual `cp -r` typed
per host; this script makes it deterministic and reusable, matching this
repo's own tools/fix-*.py convention of small checked-in scripts for
repo-hosting changes instead of ad-hoc commands.

Destination layout differs by host (see README's "Course deployment" step 7):
- GitHub mirrors Codeberg's own relative path exactly.
- GitLab-unified also mirrors it, EXCEPT a split-off course's directory is
  skipped there entirely -- it lives in its own GitLab project instead (see
  fix-gitlab-unified-pages-scope.py's SPLIT_COURSE_DIRS, which this list is
  kept in sync with by hand).
- A split-off course's session goes into its own GitLab project, at a
  shorter, flattened path (see SPLIT_COURSE_MAP below, kept in sync by hand
  with codeberg2gitlab.sh's index.tsv rewrite -- both already duplicate this
  mapping independently, so this is a third, deliberately parallel copy
  rather than a new shared dependency).

Only copies files -- never commits, pushes, or runs fix-split-session-root.py
(run that separately afterward for any split-project destination touched).

Usage:
    python3 tools/sync-pages-export.py --source-dir <codeberg-pages-worktree> \\
        [--github-dir <path>] [--gitlab-unified-dir <path>] \\
        [--split-projects-dir <path>] \\
        ancient_greek/odyssey/2026_06_01/notebook.py \\
        ancient_greek/odyssey/2026_06_15/notebook.py ...

Notebook paths are the same relative `.py` source paths passed to
export-notebooks.py -- this script uses their parent directory, exactly like
that script does, so both can share one $(NOTEBOOKS) value in the Makefile.
"""
import argparse
import pathlib
import shutil
import sys

# Coarse membership check: is this course split off at all? Kept in sync by
# hand with fix-gitlab-unified-pages-scope.py's own SPLIT_COURSE_DIRS.
SPLIT_COURSE_DIRS = [
    "ancient_greek/odyssey",
    "ancient_greek/palaestra",
    "modern_greek/b1greeklanguageandculture/kapodistrias",
    "modern_greek/b1greeklanguageandculture/kavafis_ithaki",
    "modern_greek/b1greeklanguageandculture/zorba",
]

# Precise mapping: source prefix -> (split project name, dest prefix inside
# it). Kept in sync by hand with codeberg2gitlab.sh's index.tsv rewrite.
SPLIT_COURSE_MAP = {
    "ancient_greek/odyssey": ("created-with-eee-odyssey", ""),
    "ancient_greek/palaestra/ancient_greek.2026.summer": ("created-with-eee-palaestra", ""),
    "modern_greek/b1greeklanguageandculture/kapodistrias": ("created-with-eee-b1glc", "kapodistrias"),
    "modern_greek/b1greeklanguageandculture/kavafis_ithaki": ("created-with-eee-b1glc", "kavafis_ithaki"),
    "modern_greek/b1greeklanguageandculture/zorba": ("created-with-eee-b1glc", "zorba"),
}


def _prefix_parts(rel_dir: pathlib.PurePosixPath, prefix: str) -> "tuple[str, ...] | None":
    prefix_parts = pathlib.PurePosixPath(prefix).parts
    if rel_dir.parts[: len(prefix_parts)] == prefix_parts:
        return rel_dir.parts[len(prefix_parts):]
    return None


def is_split_course(rel_dir: pathlib.PurePosixPath) -> bool:
    return any(_prefix_parts(rel_dir, prefix) is not None for prefix in SPLIT_COURSE_DIRS)


def split_destination(rel_dir: pathlib.PurePosixPath) -> "tuple[str, pathlib.PurePosixPath] | None":
    """Return (split project name, dest-relative path within it), or None
    if rel_dir doesn't belong to any split-off course."""
    for prefix, (project, dest_prefix) in SPLIT_COURSE_MAP.items():
        tail = _prefix_parts(rel_dir, prefix)
        if tail is not None:
            dest = pathlib.PurePosixPath(dest_prefix, *tail) if dest_prefix else pathlib.PurePosixPath(*tail)
            return project, dest
    return None


def replace_dir(src: pathlib.Path, dest: pathlib.Path) -> None:
    """Clean-replace dest with src's contents, so files removed/renamed in
    src don't linger as stale ghosts at dest."""
    if dest.exists():
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dest)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source-dir", required=True, type=pathlib.Path,
                         help="Pages-branch checkout already holding the fresh export (Codeberg's, by convention)")
    parser.add_argument("--github-dir", type=pathlib.Path, default=None,
                         help="GitHub pages-branch checkout (unified layout)")
    parser.add_argument("--gitlab-unified-dir", type=pathlib.Path, default=None,
                         help="GitLab-unified pages-branch checkout (unified layout, split courses skipped)")
    parser.add_argument("--split-projects-dir", type=pathlib.Path, default=None,
                         help="Parent directory holding each split GitLab project's own checkout")
    parser.add_argument("notebooks", nargs="+", type=pathlib.Path,
                         help="Notebook source paths, relative to this repo's root (same as export-notebooks.py)")
    args = parser.parse_args()

    if not any([args.github_dir, args.gitlab_unified_dir, args.split_projects_dir]):
        parser.error("pass at least one of --github-dir / --gitlab-unified-dir / --split-projects-dir")

    copied = 0
    for notebook in args.notebooks:
        rel_dir = pathlib.PurePosixPath(notebook.parent.as_posix())
        src = args.source_dir / rel_dir
        if not src.is_dir():
            print(f"skip (no export found): {rel_dir}", file=sys.stderr)
            continue

        if args.github_dir:
            dest = args.github_dir / rel_dir
            replace_dir(src, dest)
            print(f"github: {rel_dir} -> {dest}")
            copied += 1

        if args.gitlab_unified_dir:
            if is_split_course(rel_dir):
                print(f"gitlab-unified: skip {rel_dir} (split off)")
            else:
                dest = args.gitlab_unified_dir / rel_dir
                replace_dir(src, dest)
                print(f"gitlab-unified: {rel_dir} -> {dest}")
                copied += 1

        if args.split_projects_dir:
            mapped = split_destination(rel_dir)
            if mapped is None:
                print(f"split-projects: skip {rel_dir} (not a split course)")
            else:
                project, dest_rel = mapped
                dest = args.split_projects_dir / project / dest_rel
                replace_dir(src, dest)
                print(f"split-projects: {rel_dir} -> {dest}")
                copied += 1

    print(f"\n{copied} director{'y' if copied == 1 else 'ies'} copied.")


if __name__ == "__main__":
    main()
