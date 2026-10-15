#!/usr/bin/env python3
"""Re-export one or more notebooks to WASM into a pages-branch checkout.

Wraps `marimo export html-wasm`, writing each notebook's export into the
same relative directory it already occupies on the pages branch (mirroring
its position under the source tree on main). Safe to re-run -- each export
clears its own target directory first, then writes fresh output (`-f`),
leaving every other directory untouched. The target directory holds only
generated output (index.html, favicons, manifest, content-hashed assets/) --
clearing it first matters because Vite/Rollup hashes asset filenames, so
`-f` alone overwrites files it's about to rewrite but never deletes files
from a previous export that the new build simply doesn't reference anymore;
without the clear, stale content-hashed bundles accumulate forever.

Each page also carries the lesson's text data files (tools/_embed_data.py), so
it makes no request for them while it starts. The page is then a snapshot: a
data file changed on main shows up after the next export, not at once.
`--no-embed` exports the lesson as it is, and the page fetches its data files
from Codeberg while it starts.

An ancient Greek lesson that builds many paradigms also carries a paradigm pack
(tools/_paradigm_pack.py): the export runs the lesson once with `uv`, in an
environment resolved from the lesson's own script header, and the page starts
with the paradigms built. The page pins the four library versions that made the
pack (`--no-pin` leaves them free; `--no-pack` builds no pack).

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
import shutil
import subprocess
import sys
import tempfile

import _embed_data
import _paradigm_pack

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent


def export_one(notebook: pathlib.Path, pages_dir: pathlib.Path, embed: bool = True, pack: bool = True, pin: bool = True) -> "tuple[bool, str, str]":
    """Export one notebook. Returns (success, stderr-or-empty, note about the embedded data files and the paradigm pack) -- no printing."""
    out_dir = pages_dir / notebook.parent
    if out_dir.is_dir() and not (out_dir / ".git").exists():
        shutil.rmtree(out_dir)
    source, note = notebook, ""
    with tempfile.TemporaryDirectory() as tmp:
        files = _embed_data.discover(notebook, REPO_ROOT) if embed else {}
        if files:
            source = _embed_data.embedded_copy(notebook, files, pathlib.Path(tmp))
            remark = _embed_data.provenance(REPO_ROOT, files)
            note = f"{len(files)} data files embedded, {sum(p.stat().st_size for p in files.values()) / 1024:.0f} KB" + (f"; {remark}" if remark else "")
        if pack:
            data, pack_note = _paradigm_pack.make_pack(notebook, REPO_ROOT)
            note = "; ".join(filter(None, (note, pack_note)))
            if data:
                if source == notebook:
                    source = _embed_data.linked_copy(notebook, pathlib.Path(tmp))
                source.write_text(_paradigm_pack.add(source.read_text(encoding="utf-8"), data, pin), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, "-m", "marimo", "export", "html-wasm",
             str(source), "-o", str(out_dir), "-f", "--mode", "run"],
            capture_output=True, text=True,
        )
    return result.returncode == 0, result.stderr, note


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pages-dir", required=True, type=pathlib.Path,
                         help="Pages-branch checkout/worktree root to export into")
    parser.add_argument("--no-embed", action="store_true",
                         help="Do not embed the lesson's text data files in the page")
    parser.add_argument("--no-pack", action="store_true",
                         help="Do not build the paradigm pack of an ancient Greek lesson (needs `uv` and the network)")
    parser.add_argument("--no-pin", action="store_true",
                         help="Do not pin the library versions of the paradigm pack in the page (a later release then switches the pack off)")
    parser.add_argument("notebooks", nargs="+", type=pathlib.Path,
                         help="Notebook source paths, relative to this repo's root")
    args = parser.parse_args()

    failed = []
    for notebook in args.notebooks:
        ok, stderr, note = export_one(notebook, args.pages_dir, embed=not args.no_embed, pack=not args.no_pack, pin=not args.no_pin)
        if ok:
            print(f"OK: {notebook} -> {args.pages_dir / notebook.parent}" + (f" ({note})" if note else ""))
        else:
            print(f"FAILED: {notebook}\n{stderr}", file=sys.stderr)
            failed.append(notebook)

    print(f"\n{len(args.notebooks) - len(failed)} notebook(s) exported.")
    if failed:
        print("Failed:", *[str(f) for f in failed], sep="\n  ")
        sys.exit(1)


if __name__ == "__main__":
    main()
