#!/usr/bin/env python3
"""Check the page order of the lesson notebooks. Read-only, no network, takes a second.

A lesson page shows: top bar, title, the text and translation widget (Odyssey), the explanations, the exercises, the links to the lecture presentations, the footer.
Marimo shows the cells of a notebook in file order, so the order of the cells in the file is the order on the page. The check reads each notebook with `ast` and finds
the cells by markers, never by line number. A cell "shows" when the last statement before its return is an expression.

Rules:
  1. A notebook with a materials cell (a cell that holds the label key 'lesson_materials_label' or the text 'Материалы занятия') has no cell that shows output between
     the materials cell and the footer cell (the cell that calls eee_footer): the links to the presentations are the last block before the footer.
  2. A Google Slides link ('docs.google.com/presentation') stands only in the materials cell (Kapodistrias: no link in the intro sentence).
  3. Odyssey (a notebook that calls interactive_text):
     a. no cell that shows output stands between the title cell (it calls magnify_image) and the poem heading cell ('poem_section_heading'), so no explanation precedes the widget;
     b. the poem heading cell, the widget cell and the exercises heading cell ('exercises_section_heading') stand in this order, and the materials cell stands after the exercises heading;
     c. no cell that shows output stands between the top bar cell (it calls eee_topbar) and the language picker cell (the string 'eee-lang-picker'): the picker is a row under the top bar.

Scope: Odyssey notebook*.py below ancient_greek/odyssey/2026_*; Palaestra notebook.py below ancient_greek/palaestra; Kapodistrias notebook.<date>.py (the per-language
files notebook_<lang>.<date>.py of that course are dead and are not read).

Usage:
    python3 tools/check-lesson-order.py                                  # every notebook in the scope
    python3 tools/check-lesson-order.py ancient_greek/odyssey/2026_06_01/notebook.py
    python3 tools/check-lesson-order.py --root /path/to/a/checkout       # another checkout, for example a snapshot of main

Self-test: every run first applies the rules to made-up lessons (a good one passes, each broken one fails), as tools/check-embedded-data.py does with its discovery rules.

Exit status 0: every notebook follows the rules; 1: a rule fails; 2: nothing to check (a mistyped path never counts as a pass) or the self-test failed.
"""
import argparse
import ast
import pathlib
import re
import sys
import tempfile

SCOPE = (
    ("ancient_greek/odyssey", re.compile(r"^2026_\d\d_\d\d$"), re.compile(r"^notebook.*\.py$")),
    ("ancient_greek/palaestra", re.compile(r".*"), re.compile(r"^notebook\.py$")),
    ("modern_greek/b1greeklanguageandculture/kapodistrias", re.compile(r"^\d\d_\d\d_\d\d$"), re.compile(r"^notebook\.\d\d_\d\d_\d\d\.py$")),
)


def notebooks(root: pathlib.Path) -> "list[pathlib.Path]":
    found = []
    for course, folder, name in SCOPE:
        base = root / course
        if base.is_dir():
            found += [p for p in base.rglob("*.py") if name.match(p.name) and any(folder.match(part) for part in p.relative_to(base).parts[:-1]) and "__marimo__" not in p.parts]
    return sorted(found)


def cells(path: pathlib.Path) -> "list[ast.AST]":
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.decorator_list and "app.cell" in ast.unparse(n.decorator_list[0])]


def shows(node: ast.AST) -> bool:
    body = [s for s in node.body if not isinstance(s, ast.Return)]
    return bool(body) and isinstance(body[-1], ast.Expr)


def strings(node: ast.AST) -> "list[str]":
    return [c.value for c in ast.walk(node) if isinstance(c, ast.Constant) and isinstance(c.value, str)]


def calls(node: ast.AST, name: str) -> bool:
    return any(isinstance(c, ast.Call) and name in (getattr(c.func, "id", None), getattr(c.func, "attr", None)) for c in ast.walk(node))


def find(nodes: "list[ast.AST]", test) -> "list[int]":
    return [i for i, n in enumerate(nodes) if test(n)]


def shown_between(nodes: "list[ast.AST]", first: int, last: int) -> "list[int]":
    return [i for i in range(first + 1, last) if shows(nodes[i])]


def problems(path: pathlib.Path) -> "tuple[bool, list[str]]":
    """(has a materials cell, a widget or a Slides link, the problems found)."""
    nodes = cells(path)
    found: "list[str]" = []
    mat = find(nodes, lambda n: "lesson_materials_label" in strings(n) or any("Материалы занятия" in s for s in strings(n)))
    foot = find(nodes, lambda n: calls(n, "eee_footer"))
    slides = find(nodes, lambda n: any("docs.google.com/presentation" in s for s in strings(n)))
    widget = find(nodes, lambda n: calls(n, "interactive_text"))
    if len(mat) > 1 or len(foot) > 1:
        found.append(f"{len(mat)} materials cells and {len(foot)} footer cells (one of each expected)")
        return True, found
    if mat and foot:
        between = shown_between(nodes, mat[0], foot[0])
        if mat[0] > foot[0]:
            found.append("the materials cell stands after the footer cell")
        elif between:
            found.append(f"{len(between)} cell(s) that show output stand between the materials cell (line {nodes[mat[0]].lineno}) and the footer cell (line {nodes[foot[0]].lineno}), first at line {nodes[between[0]].lineno}")
    for i in slides:
        if not mat or i != mat[0]:
            found.append(f"a Google Slides link stands in the cell at line {nodes[i].lineno}, not in the materials cell")
    if widget:
        poem = find(nodes, lambda n: "poem_section_heading" in strings(n))
        exer = find(nodes, lambda n: "exercises_section_heading" in strings(n))
        title = find(nodes, lambda n: calls(n, "magnify_image"))[:1]  # the first cell with an image is the title cell; a note may show an image too
        top = find(nodes, lambda n: calls(n, "eee_topbar"))
        pick = find(nodes, lambda n: any("eee-lang-picker" in s for s in strings(n)))
        if len(poem) != 1 or len(exer) != 1 or len(title) != 1 or len(top) != 1 or len(widget) != 1 or len(pick) != 1:
            found.append(f"markers not unique: poem heading {len(poem)}, exercises heading {len(exer)}, title {len(title)}, top bar {len(top)}, widget {len(widget)}, picker {len(pick)}")
        else:
            if title[0] > poem[0]:
                found.append("the poem heading stands before the title")
            elif gap := shown_between(nodes, title[0], poem[0]):
                found.append(f"{len(gap)} cell(s) that show output stand between the title cell (line {nodes[title[0]].lineno}) and the poem heading (line {nodes[poem[0]].lineno}), first at line {nodes[gap[0]].lineno}")
            if not poem[0] < widget[0] < exer[0]:
                found.append(f"the poem heading (line {nodes[poem[0]].lineno}), the widget (line {nodes[widget[0]].lineno}) and the exercises heading (line {nodes[exer[0]].lineno}) are not in this order")
            if mat and mat[0] < exer[0]:
                found.append(f"the materials cell (line {nodes[mat[0]].lineno}) stands before the exercises heading (line {nodes[exer[0]].lineno})")
            gap = shown_between(nodes, top[0], pick[0])
            if top[0] > pick[0] or gap:
                found.append(f"the language picker (line {nodes[pick[0]].lineno}) does not follow the top bar (line {nodes[top[0]].lineno}) directly")
    return bool(mat or widget or slides), found


CELLS = {      # a made-up lesson: one cell per role, each cell shows output
    "topbar": "eee_topbar(mo)",
    "picker": 'mo.Html("<div class=\\"eee-lang-picker\\"></div>")',
    "title": "eee.magnify_image(mo, 'title.jpg')",
    "poem": "mo.md(gu.ui_label('poem_section_heading', 'ru'))",
    "widget": "eee.interactive_text(mo, lines=[])",
    "note": "mo.md('a note')",
    "exercises": "mo.md(gu.ui_label('exercises_section_heading', 'ru'))",
    "exercise": "mo.md('an exercise')",
    "materials": "mo.md(gu.ui_label('lesson_materials_label', 'ru'))",
    "slides": "mo.md('[slides](https://docs.google.com/presentation/d/1/edit)')",
    "footer": "eee_footer(mo)",
}
LESSONS = (    # (must it pass?, the cells in file order, what the lesson shows)
    (True, "topbar picker title poem widget note exercises exercise materials footer", "a good lesson with a widget"),
    (True, "topbar note exercise materials footer", "a good lesson without a widget"),
    (False, "topbar picker title poem widget note materials exercises exercise footer", "the materials before the exercises"),
    (False, "topbar picker title poem widget note exercises materials exercise footer", "an exercise between the materials and the footer"),
    (False, "topbar picker title note poem widget exercises exercise materials footer", "a note before the widget"),
    (False, "topbar picker title poem exercises widget exercise materials footer", "the widget after the exercises heading"),
    (False, "topbar title picker poem widget note exercises exercise materials footer", "the picker not under the top bar"),
    (False, "topbar picker title poem widget slides note exercises exercise materials footer", "a Slides link outside the materials cell"),
    (False, "topbar materials note exercise footer", "the materials under the title"),
)


def self_test() -> "list[str]":
    """Apply the rules to the made-up lessons and return what the check itself gets wrong."""
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        path = pathlib.Path(tmp) / "notebook.py"
        for must_pass, order, what in LESSONS:
            cells = "\n\n\n".join(f"@app.cell\ndef _():\n    {CELLS[name]}\n    return" for name in order.split())
            path.write_text(f"import marimo\napp = marimo.App()\n\n\n{cells}\n", encoding="utf-8")
            if (not problems(path)[1]) != must_pass:
                failures.append(what)
    return failures


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", type=pathlib.Path)
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    if failures := self_test():
        print("cannot run: the self-test of the rules failed on: " + "; ".join(failures), file=sys.stderr)
        sys.exit(2)
    root = args.root.resolve()
    scope = notebooks(root)
    files = sorted({f.resolve() for p in args.paths for f in ([p] if p.is_file() else [s for s in scope if s.is_relative_to(p.resolve())])}) if args.paths else scope
    if not files:
        print("cannot run: no notebook in the scope", file=sys.stderr)
        sys.exit(2)
    checked = failed = 0
    for path in files:
        in_scope, found = problems(path)
        if not in_scope:
            continue
        checked += 1
        name = path.relative_to(root).as_posix() if path.is_relative_to(root) else str(path)
        for message in found:
            print(f"FAIL {name}: {message}")
        failed += bool(found)
    if not checked:
        print("cannot run: no notebook has a materials cell, a widget or a Slides link, so there is nothing to check", file=sys.stderr)
        sys.exit(2)
    print(f"{checked} notebook(s) checked, {failed} break the page order")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
