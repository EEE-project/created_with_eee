#!/usr/bin/env python3
"""Check that every Odyssey lesson wires the translator choice of its two translation exercises. Read-only, no network, takes a second.

Each lesson has a translator multi-select above the stanza match (`sm_translators`) and above "the word in the translation" (`tp_translators`)
(eee-project 1.26.0). The selector changes nothing unless the exercise reads its value: a lesson that forgets one keyword still runs and still asks
about translators that the learner switched off. The tool reads the syntax tree of each lesson notebook and checks, by name:
  - `sm_translators = ....translator_multiselect(...)` exists when the lesson calls `stanza_match_form`, and `tp_translators = ....translator_multiselect(...)`
    exists when it calls `translation_presence_form`;
  - `stanza_match_widgets(...)` and `stanza_match_form(...)` get `valid_translators=sm_translators.value`, and `stanza_match_form(...)` gets `translator_choice=True`;
  - `translation_presence_form(...)` gets `valid_translators=tp_translators.value`, and the first argument of `balance_presence_items(...)` names `tp_translators`.
The Kavafis lessons have one translator and are not checked.

Usage:
    python3 tools/check-translator-choice.py                                # every notebook below ancient_greek/odyssey
    python3 tools/check-translator-choice.py ancient_greek/odyssey/2026_06_01/notebook.py

Exit status 0: every lesson is wired; 1: a lesson lacks a part; 2: nothing to check (a mistyped path never counts as a pass).
"""
import ast
import pathlib
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_SCOPE = "ancient_greek/odyssey"


def notebooks(scope: pathlib.Path) -> "list[pathlib.Path]":
    scope = (REPO_ROOT / scope).resolve()          # an absolute scope stays as it is
    if scope.is_file():
        return [scope]
    return sorted(p for p in scope.rglob("notebook*.py") if "__marimo__" not in p.parts) if scope.is_dir() else []


def name_of(call: ast.Call):
    return getattr(call.func, "attr", getattr(call.func, "id", None))


def keyword(call: ast.Call, key: str):
    """The source text of the keyword argument `key`, or None when the call does not pass it."""
    return next((ast.unparse(k.value) for k in call.keywords if k.arg == key), None)


def check(path: pathlib.Path) -> "tuple[bool, list[str]]":
    """(does the notebook have one of the two exercises, the parts that it lacks)."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call)]

    def named(name: str) -> "list[ast.Call]":
        return [c for c in calls if name_of(c) == name]

    selectors = {t.id for n in ast.walk(tree) if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call) and name_of(n.value) == "translator_multiselect"
                 for t in n.targets if isinstance(t, ast.Name)}
    missing = []
    has_sm, has_tp = bool(named("stanza_match_form")), bool(named("translation_presence_form"))
    if has_sm:
        if "sm_translators" not in selectors:
            missing.append("no `sm_translators = ....translator_multiselect(...)`")
        for call in named("stanza_match_widgets") + named("stanza_match_form"):
            if keyword(call, "valid_translators") != "sm_translators.value":
                missing.append(f"line {call.lineno}: {name_of(call)} without valid_translators=sm_translators.value")
        for call in named("stanza_match_form"):
            if keyword(call, "translator_choice") != "True":
                missing.append(f"line {call.lineno}: stanza_match_form without translator_choice=True")
    if has_tp:
        if "tp_translators" not in selectors:
            missing.append("no `tp_translators = ....translator_multiselect(...)`")
        for call in named("translation_presence_form"):
            if keyword(call, "valid_translators") != "tp_translators.value":
                missing.append(f"line {call.lineno}: translation_presence_form without valid_translators=tp_translators.value")
        for call in named("balance_presence_items"):
            if not call.args or "tp_translators" not in ast.unparse(call.args[0]):
                missing.append(f"line {call.lineno}: balance_presence_items does not filter its items by tp_translators")
    return has_sm or has_tp, missing


def main() -> None:
    scopes = [pathlib.Path(arg) for arg in sys.argv[1:]] or [pathlib.Path(DEFAULT_SCOPE)]
    files = sorted({f for scope in scopes for f in notebooks(scope)})
    if not files:
        print(f"cannot run: no notebook below {', '.join(map(str, scopes))}", file=sys.stderr)
        sys.exit(2)
    checked = failed = 0
    for path in files:
        has_exercise, missing = check(path)
        if not has_exercise:
            continue
        checked += 1
        name = path.relative_to(REPO_ROOT).as_posix() if path.is_relative_to(REPO_ROOT) else str(path)
        if missing:
            failed += 1
            print(f"FAIL {name}: " + "; ".join(missing))
    if not checked:
        print("cannot run: no notebook calls stanza_match_form or translation_presence_form, so there is nothing to check", file=sys.stderr)
        sys.exit(2)
    print(f"{checked} notebook(s) with a translation exercise, {failed} lacking a part of the translator choice")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
