#!/usr/bin/env python3
"""Re-export one or more notebooks to WASM into a pages-branch checkout.

Wraps `marimo export html-wasm`, writing each notebook's export into the
same relative directory it already occupies on the pages branch (mirroring
its position under the source tree on main). Safe to re-run -- each export
overwrites its own target directory (`-f`) and leaves every other directory
untouched.

Usage:
    python3 tools/export-notebooks.py --pages-dir <path-to-pages-worktree> \\
        modern_greek/ellinika_b/chapter_01/chapter_01_notebook.py \\
        ancient_greek/odyssey/2026_06_01/notebook.py ...

Notebook paths are relative to this repo's root (main branch). Requires
the same Python environment the notebooks declare in their PEP 723 header
(this project's convention: ~/.venv/eee).
"""
import argparse
import pathlib
import subprocess
import sys


def export_one(notebook: pathlib.Path, pages_dir: pathlib.Path) -> "tuple[bool, str]":
    """Export one notebook. Returns (success, stderr-or-empty) -- no printing."""
    out_dir = pages_dir / notebook.parent
    result = subprocess.run(
        [sys.executable, "-m", "marimo", "export", "html-wasm",
         str(notebook), "-o", str(out_dir), "-f", "--mode", "run"],
        capture_output=True, text=True,
    )
    return result.returncode == 0, result.stderr


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pages-dir", required=True, type=pathlib.Path,
                         help="Pages-branch checkout/worktree root to export into")
    parser.add_argument("notebooks", nargs="+", type=pathlib.Path,
                         help="Notebook source paths, relative to this repo's root")
    args = parser.parse_args()

    failed = []
    for notebook in args.notebooks:
        ok, stderr = export_one(notebook, args.pages_dir)
        if ok:
            print(f"OK: {notebook} -> {args.pages_dir / notebook.parent}")
        else:
            print(f"FAILED: {notebook}\n{stderr}", file=sys.stderr)
            failed.append(notebook)

    print(f"\n{len(args.notebooks) - len(failed)} notebook(s) exported.")
    if failed:
        print("Failed:", *[str(f) for f in failed], sep="\n  ")
        sys.exit(1)


if __name__ == "__main__":
    main()
