"""Shared CLI harness for the tools/fix-*.py maintainer scripts.

Each fix-*.py script owns its own argparse setup and its own
fix_directory(target_dir) -> list[Path] rewrite rule -- only the walk/report
loop around that rule is identical across scripts, so it lives here once.
"""
import pathlib
import sys
from collections.abc import Callable


def run_fix(
    target_dirs: list[pathlib.Path],
    fix_directory: Callable[[pathlib.Path], list[pathlib.Path]],
) -> None:
    """Run fix_directory over each target_dir, printing every file changed
    and a final total. Skips (with a warning) any path that isn't a
    directory. Never commits or pushes -- that stays a separate, confirmed
    step in every caller.
    """
    total = 0
    for target_dir in target_dirs:
        if not target_dir.is_dir():
            print(f"skip (not a directory): {target_dir}", file=sys.stderr)
            continue
        changed = fix_directory(target_dir)
        for f in changed:
            print(f"fixed: {f}")
        total += len(changed)

    print(f"\n{total} file(s) changed.")
