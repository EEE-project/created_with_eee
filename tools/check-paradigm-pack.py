#!/usr/bin/env python3
"""Check the paradigm pack step of the WASM exports (tools/_paradigm_pack.py). Read-only: it needs neither `uv` nor the network and writes nothing into the repository.

For every lesson and hub notebook:
1. The PEP 723 script header parses and lists its dependencies.
2. With a made-up pack (no paradigms, four package versions), `add()` gives a notebook that parses and has the pack cell as its first cell, once. Each of the four
   packages is pinned (==) once in the header, and every other dependency stays as it was.
3. `add()` with `pin_versions=False` leaves the header as it was.
Then, for the first ancient Greek lesson, `lesson_copy()` puts the tracked files directly in the lesson folder and in the folder above it into a scratch folder
with the same relative paths and the same bytes, and `git status` of the repository does not change (a run in the copy cannot leave files in the repository).

`--run NOTEBOOK` also builds the real pack of one lesson (needs `uv` and the network; about a minute): the pack must hold at least MIN_PARADIGMS paradigms and the
versions of the four packages.
Exit status 1 when a check fails.

Usage:
    python3 tools/check-paradigm-pack.py                     # every lesson and hub notebook
    python3 tools/check-paradigm-pack.py ancient_greek       # the notebooks below one path
    python3 tools/check-paradigm-pack.py --run ancient_greek/odyssey/2026_06_01/notebook.py
"""
import argparse
import ast
import importlib.util
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import zlib

import _embed_data
import _paradigm_pack

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
VERSIONS = {"ancient-greek-backend-eee": "9.8.7", "greek-inflexion-eee": "9.8.6", "greek-accentuation": "9.8.5", "inflexion": "9.8.4"}

_spec = importlib.util.spec_from_file_location("check_embedded_data", REPO_ROOT / "tools" / "check-embedded-data.py")
_embedded = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_embedded)       # the list of exported notebooks is defined there once


def fake_pack() -> bytes:
    return zlib.compress(json.dumps({"format": 1, "versions": VERSIONS, "paradigms": [], "lists": []}).encode())


def requirement_name(requirement: str) -> str:
    return re.split(r"[ <>=!~@\[;]", requirement, maxsplit=1)[0].lower().replace("_", "-")


def check_notebook(notebook: pathlib.Path) -> "list[str]":
    source = notebook.read_text(encoding="utf-8")
    before = _paradigm_pack.header_dependencies(source)
    if not before:
        return ["the script header lists no dependencies, or it does not parse"]
    packed = _paradigm_pack.add(source, fake_pack())
    try:
        tree = ast.parse(packed)
    except SyntaxError as error:
        return [f"the notebook with the pack cell does not parse: {error}"]
    problems = []
    first = next((n for n in tree.body if isinstance(n, ast.FunctionDef) and any(ast.unparse(d).startswith("app.cell") for d in n.decorator_list)), None)
    if first is None or "load_paradigm_pack" not in (ast.get_source_segment(packed, first) or ""):
        problems.append("the pack cell is not the first cell")
    if packed.count("load_paradigm_pack") != 1:
        problems.append(f"the pack cell appears {packed.count('load_paradigm_pack')} times, not once")
    after = _paradigm_pack.header_dependencies(packed)
    for name, version in VERSIONS.items():
        found = [d for d in after if requirement_name(d) == name]
        if found != [f"{name}=={version}"]:
            problems.append(f"{name} must be pinned once as {name}=={version}, the header has {found}")
    if [d for d in before if requirement_name(d) not in VERSIONS] != [d for d in after if requirement_name(d) not in VERSIONS]:
        problems.append("the pinning changed a dependency that is not one of the four packages")
    if _paradigm_pack.header_dependencies(_paradigm_pack.add(source, fake_pack(), pin_versions=False)) != before:
        problems.append("add(..., pin_versions=False) changed the header")
    return problems


def repository_status() -> str:
    return subprocess.run(["git", "-C", str(REPO_ROOT), "status", "--porcelain"], capture_output=True, text=True, check=True).stdout


def check_lesson_copy(notebook: pathlib.Path) -> "list[str]":
    status = repository_status()
    expected = [p for folder in (notebook.parent, notebook.parent.parent) for p in _embed_data.tracked_files(REPO_ROOT, folder) if p.is_file()]
    problems = []
    with tempfile.TemporaryDirectory() as tmp:
        copy = _paradigm_pack.lesson_copy(notebook, REPO_ROOT, pathlib.Path(tmp))
        if copy != pathlib.Path(tmp) / notebook.relative_to(REPO_ROOT):
            problems.append(f"the copy of the notebook is at {copy}")
        for source in expected:
            target = pathlib.Path(tmp) / source.relative_to(REPO_ROOT)
            if not target.is_file() or target.read_bytes() != source.read_bytes():
                problems.append(f"{source.relative_to(REPO_ROOT)} is missing in the copy or differs")
        copied = sum(1 for p in pathlib.Path(tmp).rglob("*") if p.is_file())
        if copied != len(expected):
            problems.append(f"the copy holds {copied} files, git tracks {len(expected)} in the two folders")
    if repository_status() != status:
        problems.append("git status of the repository changed")
    return problems


def check_run(notebook: pathlib.Path) -> "list[str]":
    data, note = _paradigm_pack.make_pack(notebook, REPO_ROOT)
    print(note or "(not an ancient Greek lesson)")
    if data is None:
        return [note or "the lesson has no ancient Greek backend: no pack to check"]
    pack = json.loads(zlib.decompress(data))
    count = sum(len(entry["paradigm"]) for entry in pack["lists"])
    problems = []
    if set(pack["versions"]) != set(VERSIONS):
        problems.append(f"the pack records the versions of {sorted(pack['versions'])}")
    if count < _paradigm_pack.MIN_PARADIGMS:
        problems.append(f"the pack holds {count} paradigms")
    return problems


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("scope", nargs="?", type=pathlib.Path, default=pathlib.Path("."), help="only the notebooks below this path (default: all)")
    parser.add_argument("--run", type=pathlib.Path, metavar="NOTEBOOK", help="also build the real pack of this lesson (needs uv and the network)")
    args = parser.parse_args()

    notebooks = _embedded.lesson_notebooks(args.scope)
    failures = 0
    for notebook in notebooks:
        problems = check_notebook(notebook)
        if problems:
            failures += 1
            print(f"FAIL {notebook.relative_to(REPO_ROOT)}")
            for problem in problems:
                print(f"     {problem}")
    greek = next((n for n in notebooks if "ancient_greek_backend_eee" in n.read_text(encoding="utf-8")), None)
    if greek is not None:
        problems = check_lesson_copy(greek)
        if problems:
            failures += 1
            print(f"FAIL lesson_copy of {greek.relative_to(REPO_ROOT)}")
            for problem in problems:
                print(f"     {problem}")
    if args.run:
        problems = check_run((REPO_ROOT / args.run).resolve())
        if problems:
            failures += 1
            print(f"FAIL --run {args.run}")
            for problem in problems:
                print(f"     {problem}")
    print(f"{len(notebooks)} notebook(s) checked; the lesson copy was checked on {greek.relative_to(REPO_ROOT) if greek else 'no lesson'}; {failures} check(s) failed.")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
