#!/usr/bin/env python3
"""Check that every Odyssey lesson passes by_translator=True to balance_presence_items. Read-only, no network, takes a second.

A session of the exercise "is the word reflected in the translation" is split by answer ("yes" and "no") only, unless the call passes
by_translator=True (eee-project 1.26.0). Then a translator whose rendering omits many words supplies most of the session (one translator
supplied 7 of the 10 items). The Kavafis lessons have one translator and are not checked.

Usage:
    python3 tools/check-presence-balance.py                                # every notebook below ancient_greek/odyssey
    python3 tools/check-presence-balance.py ancient_greek/odyssey/2026_06_01/notebook.py

Exit status 0: every call has the flag; 1: a call lacks it; 2: nothing to check (a mistyped path never counts as a pass).
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


def calls_without_the_flag(path: pathlib.Path) -> "tuple[int, list[int]]":
    """(number of balance_presence_items calls, the line numbers of those that do not pass by_translator=True)."""
    found, missing = 0, []
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Call) and getattr(node.func, "attr", getattr(node.func, "id", None)) == "balance_presence_items":
            found += 1
            if not any(k.arg == "by_translator" and isinstance(k.value, ast.Constant) and k.value.value is True for k in node.keywords):
                missing.append(node.lineno)
    return found, missing


def main() -> None:
    scopes = [pathlib.Path(arg) for arg in sys.argv[1:]] or [pathlib.Path(DEFAULT_SCOPE)]
    files = sorted({f for scope in scopes for f in notebooks(scope)})
    if not files:
        print(f"cannot run: no notebook below {', '.join(map(str, scopes))}", file=sys.stderr)
        sys.exit(2)
    checked = failed = 0
    for path in files:
        found, missing = calls_without_the_flag(path)
        if not found:
            continue
        checked += 1
        name = path.relative_to(REPO_ROOT).as_posix() if path.is_relative_to(REPO_ROOT) else str(path)
        if missing:
            failed += 1
            print(f"FAIL {name}: balance_presence_items without by_translator=True at line {', '.join(map(str, missing))}")
    if not checked:
        print("cannot run: no notebook calls balance_presence_items, so there is nothing to check", file=sys.stderr)
        sys.exit(2)
    print(f"{checked} notebook(s) call balance_presence_items, {failed} without by_translator=True")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
