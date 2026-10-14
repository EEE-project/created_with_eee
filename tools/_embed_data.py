"""Embed a lesson's text data files in its WASM export.

A WASM page has no files beside the notebook, so each `gu.ensure_file()` call in a lesson downloads its file from Codeberg while the page starts: one
blocking request per file. This module finds the text data files a lesson can ask for and builds a copy of the lesson with one extra first cell. That
cell writes the files into the page's file system. `ensure_file()` then finds each file present and makes no request. The lesson file on disk stays unchanged.

Only files that git tracks are embedded. A lesson folder can also hold git-ignored copies that a local run downloaded from another repository (the Odyssey
`translations_*.md`); a page that embedded such a copy would show it instead of the current file.

Not embedded, so the page keeps fetching them at run time:
- `index.tsv` and `ga.json`: they keep old pages in step with the course list, and `ConfigStore.from_file_or_url` reads GA settings only from a local
  `ga.json` once it finds a local `index.tsv`, so embedding the index alone would turn Analytics off.
- PDFs and images: they add megabytes to every page for a gain inside the noise, and a lesson may pick a local image over its remote URL, which changes how it renders.
- files of another repository, files that sit more than one folder above the lesson, files over the size limit, and names a syntax tree cannot show.
"""
import ast
import base64
import functools
import os
import pathlib
import re
import subprocess
import zlib

TEXT_EXT = {".tsv", ".md", ".yaml", ".yml", ".json", ".txt", ".csv", ".html"}
LIVE_NAMES = {"index.tsv", "ga.json"}
DOC_NAMES = {"README.md", "AGENTS.md", "CLAUDE.md", "CHANGELOG.md"}
MAX_FILE = 250_000                                          # bytes; a bigger file stays a run-time fetch


@functools.lru_cache(maxsize=None)
def tracked_files(root: pathlib.Path, folder: pathlib.Path) -> "tuple[pathlib.Path, ...]":
    """The files that git tracks directly inside folder (an untracked or git-ignored file is not part of a page)."""
    listing = subprocess.run(["git", "-C", str(root), "ls-files", "-z", "--", str(folder.relative_to(root))], capture_output=True, check=True).stdout
    paths = (root / os.fsdecode(entry) for entry in listing.split(b"\0") if entry)
    return tuple(sorted(p for p in paths if p.parent == folder))


def fstring_glob(node: ast.JoinedStr) -> str:
    """An f-string as a glob: each placeholder becomes `*`."""
    return "".join(v.value if isinstance(v, ast.Constant) else "*" for v in node.values)


def glob_regex(glob: str) -> re.Pattern:
    return re.compile("^" + ".*".join(re.escape(part) for part in glob.split("*")) + "$")


def _named(tree: ast.AST) -> "tuple[set[str], list[re.Pattern]]":
    """File names a notebook mentions: exact string constants, and f-strings as patterns (a placeholder matches anything)."""
    exact, patterns = set(), []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            text = node.value
        elif isinstance(node, ast.JoinedStr):
            text = fstring_glob(node)
        else:
            continue
        if not (0 < len(text) < 160 and "/" not in text and "\n" not in text and pathlib.Path(text).suffix.lower() in TEXT_EXT):
            continue
        if "*" in text:
            patterns.append(glob_regex(text))
        else:
            exact.add(text)
    return exact, patterns


def discover(notebook: pathlib.Path, root: pathlib.Path) -> "dict[tuple[int, str], pathlib.Path]":
    """The tracked text data files a lesson can ask for: all of them in its own folder (key 0), those it names in the folder above (key 1)."""
    notebook, root = pathlib.Path(notebook).resolve(), pathlib.Path(root).resolve()
    exact, patterns = _named(ast.parse(notebook.read_text(encoding="utf-8")))

    def named(p: pathlib.Path) -> bool:
        return p.name in exact or any(rx.match(p.name) for rx in patterns)

    found = {}
    for up, folder in enumerate((notebook.parent, notebook.parent.parent)):
        if root not in (folder, *folder.parents):
            continue
        for p in tracked_files(root, folder):
            if (p.is_file() and p.suffix.lower() in TEXT_EXT and p.name not in DOC_NAMES | LIVE_NAMES and p.stat().st_size <= MAX_FILE
                    and (up == 0 or named(p))):
                found[(up, p.name)] = p
    return found


def provenance(root: pathlib.Path, files: "dict[tuple[int, str], pathlib.Path]") -> str:
    """A remark when the embedded bytes are not the committed ones on main: the branch, and the files that differ from HEAD. Empty when there is nothing to say."""
    def git(*args: str) -> str:
        done = subprocess.run(["git", "-C", str(root), "-c", "core.quotepath=false", *args], capture_output=True, text=True)
        return done.stdout.strip() if done.returncode == 0 else ""

    remarks = []
    branch = git("branch", "--show-current") or "no branch (detached HEAD)"
    if branch != "main":
        remarks.append(f"branch {branch}, not main")
    changed = git("diff", "--name-only", "HEAD", "--", *(str(p.relative_to(root)) for p in files.values())).splitlines()
    if changed:
        remarks.append("differs from HEAD: " + ", ".join(sorted(pathlib.Path(c).name for c in changed)))
    return "; ".join(remarks)


_CELL = '''\
@app.cell(hide_code=True)
def _():
    # Generated at export: the lesson's data files, written before any other cell runs.
    import base64 as _b64
    import zlib as _zlib
    from pathlib import Path as _Path
    for _up, _name, _blob in (
{entries}
    ):
        _folder = _Path(__file__).parent
        for _ in range(_up):
            _folder = _folder.parent
        if not (_folder / _name).exists():
            (_folder / _name).write_bytes(_zlib.decompress(_b64.b64decode(_blob)))
    return
'''


def cell_source(files: "dict[tuple[int, str], bytes]") -> str:
    entries = ",\n".join(f"        ({up}, {name!r}, {base64.b64encode(zlib.compress(data, 9)).decode('ascii')!r})" for (up, name), data in sorted(files.items()))
    return _CELL.format(entries=entries)


def inject(source: str, files: "dict[tuple[int, str], bytes]") -> str:
    """The notebook source with the data cell right after the `app = marimo.App(...)` statement (marimo runs the first registered of several free cells first)."""
    app_stmt = next((n for n in ast.parse(source).body
                     if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "app" for t in n.targets)
                     and isinstance(n.value, ast.Call) and getattr(n.value.func, "attr", "") == "App"), None)
    if app_stmt is None:
        raise ValueError("no `app = marimo.App(...)` statement found")
    lines = source.split("\n")
    return "\n".join(lines[:app_stmt.end_lineno] + ["", ""] + cell_source(files).rstrip("\n").split("\n") + ["", ""] + lines[app_stmt.end_lineno:])


def embedded_copy(notebook: pathlib.Path, files: "dict[tuple[int, str], pathlib.Path]", tmp_dir: pathlib.Path) -> pathlib.Path:
    """Write the lesson with its data cell into tmp_dir and return that path; the other entries of the lesson's folder are linked in, so marimo finds head files as before."""
    notebook = pathlib.Path(notebook).resolve()
    for entry in notebook.parent.iterdir():
        if entry.name != notebook.name:
            (tmp_dir / entry.name).symlink_to(entry)
    target = tmp_dir / notebook.name
    target.write_text(inject(notebook.read_text(encoding="utf-8"), {k: p.read_bytes() for k, p in files.items()}), encoding="utf-8")
    return target
