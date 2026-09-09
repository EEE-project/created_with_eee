#!/usr/bin/env python3
"""Copy freshly regenerated hub index.html files from Codeberg's pages
worktree into the other hosts' local checkouts.

Sibling to sync-pages-export.py, which copies whole LESSON export
directories. A hub's own output directory (gen_hub.py's HUBS[key]["out"])
also holds that course's lesson subdirectories -- or, for the root/category
hubs, most of the site tree -- so reusing that script's directory-level
replace_dir() on a hub would hugely over-copy. This script copies just the
one index.html file per hub instead.

Destination layout mirrors sync-pages-export.py's own rules (see that
script's docstring): GitHub mirrors Codeberg's relative path exactly;
GitLab-unified does too, except a split-off course is skipped there and
copied into its own GitLab project's checkout instead, at a shorter,
flattened path. SPLIT_HUB_MAP below is kept in sync by hand with
sync-pages-export.py's SPLIT_COURSE_MAP -- not shared code, matching that
script's own stated reasoning for a deliberately parallel copy.

Only copies files -- never commits or pushes.

Usage:
    python3 tools/sync-hub-pages.py --source-dir <codeberg-pages-worktree> \\
        [--github-dir <path>] [--gitlab-unified-dir <path>] \\
        [--split-projects-dir <path>] \\
        root ancient_greek modern_greek b1greeklanguageandculture ...

Hub keys are gen_hub.py's own HUBS dict keys.
"""
import argparse
import pathlib
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from gen_hub import HUBS  # noqa: E402

# Kept in sync by hand with sync-pages-export.py's own SPLIT_COURSE_MAP.
# dest_prefix is where the hub's index.html lands *inside* the split
# project -- "" for a course whose own hub sits at that project's root.
SPLIT_HUB_MAP = {
    "ancient_greek/odyssey": ("created-with-eee-odyssey", ""),
    "ancient_greek/palaestra/ancient_greek.2026.summer": ("created-with-eee-palaestra", ""),
    "modern_greek/b1greeklanguageandculture": ("created-with-eee-b1glc", ""),
    "modern_greek/b1greeklanguageandculture/kapodistrias": ("created-with-eee-b1glc", "kapodistrias"),
    "modern_greek/b1greeklanguageandculture/kavafis_ithaki": ("created-with-eee-b1glc", "kavafis_ithaki"),
    "modern_greek/b1greeklanguageandculture/zorba": ("created-with-eee-b1glc", "zorba"),
}


def copy_file(src: pathlib.Path, dest: pathlib.Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source-dir", required=True, type=pathlib.Path,
                         help="Pages-branch checkout already holding the fresh hub export (Codeberg's, by convention)")
    parser.add_argument("--github-dir", type=pathlib.Path, default=None,
                         help="GitHub pages-branch checkout (unified layout)")
    parser.add_argument("--gitlab-unified-dir", type=pathlib.Path, default=None,
                         help="GitLab-unified pages-branch checkout (unified layout, split courses skipped)")
    parser.add_argument("--split-projects-dir", type=pathlib.Path, default=None,
                         help="Parent directory holding each split GitLab project's own checkout")
    parser.add_argument("hubs", nargs="*", help="gen_hub.py HUBS dict keys, e.g. root ancient_greek ellinika_b (default: all)")
    args = parser.parse_args()

    if not any([args.github_dir, args.gitlab_unified_dir, args.split_projects_dir]):
        parser.error("pass at least one of --github-dir / --gitlab-unified-dir / --split-projects-dir")

    copied = 0
    for key in (args.hubs or list(HUBS.keys())):
        if key not in HUBS:
            print(f"skip (unknown hub key): {key}", file=sys.stderr)
            continue
        out = HUBS[key]["out"]
        rel = pathlib.PurePosixPath("index.html") if out == "." else pathlib.PurePosixPath(out, "index.html")
        src = args.source_dir / rel
        if not src.is_file():
            print(f"skip (no export found): {rel}", file=sys.stderr)
            continue

        if args.github_dir:
            dest = args.github_dir / rel
            copy_file(src, dest)
            print(f"github: {rel} -> {dest}")
            copied += 1

        split = SPLIT_HUB_MAP.get(out)

        if args.gitlab_unified_dir:
            if split:
                print(f"gitlab-unified: skip {rel} (split off)")
            else:
                dest = args.gitlab_unified_dir / rel
                copy_file(src, dest)
                print(f"gitlab-unified: {rel} -> {dest}")
                copied += 1

        if args.split_projects_dir:
            if split is None:
                print(f"split-projects: skip {rel} (not a split course)")
            else:
                project, dest_prefix = split
                dest_rel = pathlib.PurePosixPath("index.html") if not dest_prefix else pathlib.PurePosixPath(dest_prefix, "index.html")
                dest = args.split_projects_dir / project / dest_rel
                copy_file(src, dest)
                print(f"split-projects: {rel} -> {dest}")
                copied += 1

    print(f"\n{copied} file(s) copied.")


if __name__ == "__main__":
    main()
