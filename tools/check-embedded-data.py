#!/usr/bin/env python3
"""Check the data embedding of the WASM exports (tools/_embed_data.py). Read-only.

First it runs the discovery rules on a made-up lesson in a scratch git repository, and checks that its notebook pattern equals the one in
`tools/propagate-pages.sh`. Then, for every lesson and hub notebook, it checks:
1. `index.tsv` and `ga.json` are not embedded.
2. No file name comes from two folders with different content (in the page the lesson's folder and the folder above are one folder).
3. The notebook with the data cell in it parses and the data cell is its first cell. That cell, run on its own in a scratch folder, writes every embedded
   file with the bytes of its source file.
4. Every tracked text file that the notebook passes to `ensure_file()` / `ensure_files()` by a name a syntax tree can show, and that exists in the lesson's
   folder or the folder above it, is embedded. A file that is not embedded would be fetched while the page starts, one blocking request per file.

Names the tree cannot show (a variable, a call) are counted but not checked. PDFs, images, `index.tsv` and `ga.json` stay run-time fetches by design.
Exit status 1 when a check fails.

A page keeps the data it was exported with. After a data file changes, `--who` lists the lessons whose page embeds it, so you can export them again.

Usage:
    python3 tools/check-embedded-data.py                                  # every lesson and hub notebook of the repo
    python3 tools/check-embedded-data.py ancient_greek/palaestra          # the notebooks below one path
    python3 tools/check-embedded-data.py --export ancient_greek/odyssey   # also export each data-cell copy with marimo (slow)
    python3 tools/check-embedded-data.py --who ancient_greek/odyssey/eee_note_en.md   # the lessons that embed this file
    python3 tools/check-embedded-data.py --who $(git diff --name-only main)           # ... or any file changed since main
"""
import argparse
import ast
import pathlib
import re
import subprocess
import sys
import tempfile

import _embed_data

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
NEVER_EMBED = {"index.tsv", "ga.json"}      # a copy here, not _embed_data's own list: the guard must not move with the code it guards
EXPORTED_NOTEBOOK = re.compile(r"(^|/)(notebook(\.[0-9_]+)?|.*_notebook)\.py$")      # the awk pattern of tools/propagate-pages.sh (check_notebook_rule keeps them equal): never the _el/_en/_ru variants


def lesson_notebooks(scope: pathlib.Path) -> "list[pathlib.Path]":
    """The tracked lesson and hub notebooks below scope."""
    tracked = subprocess.run(["git", "-C", str(REPO_ROOT), "ls-files", "-z", "*.py"], capture_output=True, text=True, check=True).stdout.split("\0")
    return [REPO_ROOT / f for f in tracked if EXPORTED_NOTEBOOK.search(f) and (REPO_ROOT / f).is_relative_to((REPO_ROOT / scope).resolve())]


def requested_names(tree: ast.AST) -> "tuple[set[str], list[re.Pattern], int]":
    """Names passed to ensure_file()/ensure_files(): exact names, f-string patterns, and the number of arguments a tree cannot resolve."""
    parents = {child: parent for parent in ast.walk(tree) for child in ast.iter_child_nodes(parent)}
    exact, patterns, unresolved = set(), [], 0

    def resolve(arg: ast.AST, call: ast.AST) -> None:
        nonlocal unresolved
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
            exact.add(arg.value)
        elif isinstance(arg, ast.JoinedStr):
            patterns.append(_embed_data.glob_regex(_embed_data.fstring_glob(arg)))
        elif isinstance(arg, (ast.Tuple, ast.List)):
            for element in arg.elts:
                resolve(element, call)
        elif isinstance(arg, ast.Name):
            node = call
            while node in parents:
                node = parents[node]
                loops = [(node.target, node.iter)] if isinstance(node, ast.For) else [(g.target, g.iter) for g in node.generators] if isinstance(node, (ast.ListComp, ast.SetComp, ast.GeneratorExp)) else []
                for target, iterable in loops:
                    if isinstance(target, ast.Name) and target.id == arg.id and isinstance(iterable, (ast.Tuple, ast.List)):
                        resolve(iterable, call)
                        return
            unresolved += 1
        else:
            unresolved += 1

    for call in ast.walk(tree):
        if isinstance(call, ast.Call) and getattr(call.func, "attr", getattr(call.func, "id", "")) in ("ensure_file", "ensure_files"):
            for arg in call.args:
                resolve(arg, call)
    return exact, patterns, unresolved


def check_notebook_rule() -> "list[str]":
    """The notebook pattern above is the awk pattern of tools/propagate-pages.sh; both files must hold the same one."""
    awk_pattern = "/" + EXPORTED_NOTEBOOK.pattern.replace("/", "\\/") + "/"
    if awk_pattern in (REPO_ROOT / "tools" / "propagate-pages.sh").read_text(encoding="utf-8"):
        return []
    return [f"tools/propagate-pages.sh does not hold the notebook pattern {awk_pattern}: change both files together"]


def check_rules() -> "list[str]":
    """The discovery rules on a made-up lesson in a scratch git repository: names from f-strings and constants, size limit, never-embed names, depth, tracked files only."""
    notebook_source = ('import marimo\napp = marimo.App()\n\n\n@app.cell\ndef _():\n    for _k in ("a", "b"):\n        gu.ensure_file(f"terms_{_k}.tsv")\n'
                       '    gu.ensure_file("named.md")\n    gu.ensure_file("deep.tsv")\n    return\n')
    layout = {
        "course/lesson/notebook.py": notebook_source, "course/lesson/own.tsv": "x", "course/lesson/big.tsv": "x" * (_embed_data.MAX_FILE + 1),
        "course/lesson/index.tsv": "x", "course/lesson/README.md": "x", "course/lesson/scan.pdf": "x", "course/lesson/pic.jpg": "x",
        "course/terms_a.tsv": "x", "course/named.md": "x", "course/unnamed.tsv": "x", "course/ga.json": "{}", "deep.tsv": "x",
        "course/lesson/ignored.tsv": "x", ".gitignore": "ignored.tsv\n",
    }
    expected = {(0, "own.tsv"), (1, "terms_a.tsv"), (1, "named.md")}
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        for relative, text in layout.items():
            (root / relative).parent.mkdir(parents=True, exist_ok=True)
            (root / relative).write_text(text, encoding="utf-8")
        for git_args in (["init", "-q"], ["add", "-A"]):
            subprocess.run(["git", *git_args], cwd=root, check=True, capture_output=True)
        (root / "course/lesson/untracked.tsv").write_text("x", encoding="utf-8")
        found = set(_embed_data.discover(root / "course/lesson/notebook.py", root))
    return [f"rules: expected {sorted(expected)}, found {sorted(found)}"] if found != expected else []


def check_never_embed(files: "dict[tuple[int, str], pathlib.Path]") -> "list[str]":
    return [f"{name!r} must stay a run-time fetch (see tools/_embed_data.py) but is embedded" for _, name in files if name in NEVER_EMBED]


def check_collisions(files: "dict[tuple[int, str], pathlib.Path]") -> "list[str]":
    """In the page the lesson's folder and the folder above are one folder, so a name found in both with different content cannot be both."""
    by_name = {}
    for (_, name), path in files.items():
        by_name.setdefault(name, []).append(path)
    return [f"{name!r} is embedded from two folders with different content; in the page both are one path" for name, paths in sorted(by_name.items())
            if len(paths) > 1 and len({p.read_bytes() for p in paths}) > 1]


def check_data_cell(notebook: pathlib.Path, files: "dict[tuple[int, str], pathlib.Path]") -> "list[str]":
    """The notebook with the data cell parses and the data cell is its first cell; that cell, run in a scratch folder, writes every file with the bytes of its source."""
    try:
        tree = ast.parse(_embed_data.inject(notebook.read_text(encoding="utf-8"), {k: p.read_bytes() for k, p in files.items()}))
    except (SyntaxError, ValueError) as exc:
        return [f"the notebook with the data cell does not parse: {exc}"]
    cells = [n for n in tree.body if isinstance(n, ast.FunctionDef) and any(ast.unparse(d).startswith("app.cell") for d in n.decorator_list)]
    first = cells[0].body[0] if cells else None
    if not (isinstance(first, ast.Import) and first.names[0].asname == "_b64"):
        return ["the data cell is not the first cell of the notebook"]
    problems = []
    with tempfile.TemporaryDirectory() as tmp:
        lesson_dir = pathlib.Path(tmp) / "lesson"
        lesson_dir.mkdir()
        cells[0].decorator_list = []      # run the cell as a plain function
        namespace = {"__file__": str(lesson_dir / "notebook.py")}
        exec(compile(ast.fix_missing_locations(ast.Module([cells[0]], [])), "<data cell>", "exec"), namespace)
        namespace["_"]()
        for (up, name), source in files.items():
            written = (lesson_dir if up == 0 else lesson_dir.parent) / name
            if not written.is_file() or written.read_bytes() != source.read_bytes():
                problems.append(f"the data cell does not write {name!r} (folder level {up}) with the bytes of its source")
    return problems


def check_covered(notebook: pathlib.Path, files: "dict[tuple[int, str], pathlib.Path]") -> "tuple[list[str], int]":
    """Text files the notebook requests by a name the tree shows, present beside it or in the folder above, and not embedded."""
    exact, patterns, unresolved = requested_names(ast.parse(notebook.read_text(encoding="utf-8")))
    missed = []
    for up, folder in enumerate((notebook.parent, notebook.parent.parent)):
        if REPO_ROOT not in (folder, *folder.parents):
            continue
        for p in _embed_data.tracked_files(REPO_ROOT, folder):
            wanted = p.name in exact or any(rx.match(p.name) for rx in patterns)
            if (p.is_file() and wanted and p.suffix.lower() in _embed_data.TEXT_EXT and p.name not in _embed_data.LIVE_NAMES | _embed_data.DOC_NAMES
                    and (up, p.name) not in files):
                missed.append(f"{p.relative_to(REPO_ROOT)} is requested but not embedded ({p.stat().st_size} bytes; the limit is {_embed_data.MAX_FILE})")
    return missed, unresolved


def export_copy(notebook: pathlib.Path, files: "dict[tuple[int, str], pathlib.Path]") -> "list[str]":
    with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as out:
        source = _embed_data.embedded_copy(notebook, files, pathlib.Path(tmp))
        result = subprocess.run([sys.executable, "-m", "marimo", "export", "html-wasm", str(source), "-o", out, "-f", "--mode", "run"], capture_output=True, text=True)
        return [] if result.returncode == 0 else [f"marimo cannot export the notebook with the data cell: {result.stderr.strip()[-300:]}"]


def print_who(paths: "list[str]") -> None:
    """For each file, the lessons whose page embeds it (a course hub, which sits beside its index.tsv, is no exported lesson)."""
    embedded_by = {}
    for notebook in lesson_notebooks(pathlib.Path(".")):
        if not (notebook.parent / "index.tsv").is_file():
            for path in _embed_data.discover(notebook, REPO_ROOT).values():
                embedded_by.setdefault(path.resolve(), []).append(notebook.relative_to(REPO_ROOT).as_posix())
    for given in paths:
        lessons = embedded_by.get((REPO_ROOT / given).resolve(), [])
        print(f"{given}: " + (f"{len(lessons)} lesson(s)" if lessons else "no lesson embeds it"))
        for lesson in lessons:
            print(f"     {lesson}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("scope", nargs="?", type=pathlib.Path, default=pathlib.Path("."), help="Only notebooks below this path, relative to the repo root")
    parser.add_argument("--export", action="store_true", help="Also export each notebook with its data cell through marimo (about 6 s each)")
    parser.add_argument("--who", nargs="+", metavar="FILE", help="Only list the lessons whose page embeds each FILE (a path relative to the repo root)")
    args = parser.parse_args()

    if args.who:
        print_who(args.who)
        return
    notebooks = lesson_notebooks(args.scope)
    embedded_total = unresolved_total = with_files = 0
    failures = 0
    for problem in check_rules() + check_notebook_rule():
        failures += 1
        print(f"FAIL {problem}")
    for notebook in notebooks:
        files = _embed_data.discover(notebook, REPO_ROOT)
        problems, unresolved = check_covered(notebook, files)
        unresolved_total += unresolved
        if files:
            with_files += 1
            embedded_total += sum(p.stat().st_size for p in files.values())
            problems += check_never_embed(files) + check_collisions(files) + check_data_cell(notebook, files)
            if args.export:
                problems += export_copy(notebook, files)
        if problems:
            failures += 1
            print(f"FAIL {notebook.relative_to(REPO_ROOT)}")
            for problem in problems:
                print(f"     {problem}")
    print(f"{len(notebooks)} notebook(s) checked; {with_files} of them embed data files ({embedded_total / 1024:.0f} KB in all); "
          f"{unresolved_total} file name(s) in ensure_file calls are not visible to a syntax tree; {failures} notebook(s) failed.")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
