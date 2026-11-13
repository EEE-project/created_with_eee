#!/usr/bin/env python3
"""Check, in a real browser, that a lesson's text/translation block and word sheet fit a phone and a wide page. Read-only.

The Odyssey lessons draw the stanza with `eee.interactive_text(..., wrap=True, translation=..., notes=...)` and the word
panel with `gu.render_gloss_sheet(...)` (eee-project 1.26.0). What that looks like is CSS (a container query, a fixed
bottom sheet), and neither pytest nor `marimo check` can see it. This tool runs each lesson with `marimo run`, opens it in
Chromium at each width and in each interface language, taps the words, and checks:

1. The block fits: the Greek, the translation card and the selector row stay inside the page (no sideways scroll caused
   by them), and the Greek lines wrap with a hanging indent.
2. The card stands beside the Greek where the box that holds the widget is at least 600 px wide (a container query),
   and under it where narrower; at 390 px it is under, at 830 px beside.
3. A tap on a Greek word opens the word sheet; it is fixed to the bottom of the screen below 750 px (at most 55% of the
   screen high) and a block in the page from 750 px on. A closed sheet opens again for the next word.
4. Every translation of the dropdown draws a card that fits (on the narrowest page in every stanza of the lesson, otherwise in
   the stanza on show); a translation with margin notes has tappable words (links, no star), a tap shows the note in the sheet and
   clears the Greek word (and the reverse); the blank entry removes the card.
5. The page raises no uncaught JavaScript error, and the server prints no exception while the tool works (a cell that raises,
   for instance a NameError left behind by a merge, fails the run with the line of the exception).
6. The page does not scroll sideways: `div#App`, the box marimo gives a lesson (`overflow-x: auto`), holds nothing wider than the page,
   and no element that is not fixed ends past the right edge of the page. The stanza on show and every translator are measured, so the
   translation source line is seen too. The archive links (`https://web.archive.org/...`) in that line are KB text and too long for a
   phone; they stay as they are (decision of 2026-11-09), so the `ok` line counts them and they do not fail the run. The tool reads the
   box of each element, not what the eye sees: a box that ends past the right edge is reported also when a parent with `overflow`
   hides or scrolls it, and text that a parent clips inside the page is not seen.

A lesson starts in its default interface language and is drawn again once the language kept in the browser has reached the kernel;
the tool waits until that has happened (a tap on the first draw is lost), the page has stopped changing and the rules of the widget are applied, and after each choice in a dropdown until the kernel has drawn the widget again, before it checks anything.

marimo (issue 10494) sometimes deletes the module of the stanza widget before the page has fetched it: the server prints `Virtual file not found`, and if the lost module is the one of
the widget that stays, the page shows no text for good. When no text shows 30 s after the first traceback and the server printed that message, the tool loads the page again, up to
`MAX_RELOADS` times, and the `ok` line says how often. Any other error of the lesson at the start fails the run.

The tool cannot see anything that happens in Pyodide (the published pages): the layout shows there only after eee-project 1.26.0 is released
and installed in the exporting Python (an older marimo pinned the page to the installed version; see AGENTS.md, "The stanza layout of the Odyssey lessons"), and
`.claude/skills/verify-pages` is the check of a published lesson. Each run loads the whole lesson once per
language and width, which takes 10 to 40 seconds.

A lesson run writes into its own folder (translation_presence.tsv, for one). The tool copies the folder's files first
and puts them back afterwards, also when it fails.

Usage:
    python3 tools/check-lesson-layout.py                                              # every lesson that calls render_gloss_sheet
    python3 tools/check-lesson-layout.py ancient_greek/odyssey/2026_06_01/notebook.py  # one notebook (or a folder: all below it)
    python3 tools/check-lesson-layout.py --widths 390 --langs el ancient_greek/odyssey  # fewer runs (comma-separated lists)
    python3 tools/check-lesson-layout.py --list                                       # only name the notebooks it would check

Needs, in the Python that runs it (`make check-lesson-layout` uses EEE_PYTHON): marimo, eee-project 1.26 or newer, and
Playwright with a Chromium (EEE_CHROMIUM, `chromium` on the PATH, one under /opt/pw-browsers, or Playwright's own).
Exit status 0: every check passed (or --list); 1: a check failed; 2: it could not run: something is missing, or the scope matches
no lesson (the message says which), so a mistyped path never counts as a pass.
"""
import argparse
import contextlib
import glob
import importlib.metadata
import os
import pathlib
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EXPORTED_NOTEBOOK = re.compile(r"(^|/)(notebook(\.[0-9_]+)?|.*_notebook)\.py$")      # a lesson notebook, never the _el/_en/_ru variants
USES_LAYOUT = "render_gloss_sheet("
STANZA, CARD, GREEK, SHEET, NOTE = ".eee-stanza-wrap", ".eee-tr", ".eee-itext", ".eee-sheet", ".gk-note"
BLANK = "--"                                  # the value of the blank entry of a marimo dropdown made with allow_select_none=True
LANGUAGE_NAME = {"el": "Ελληνικά", "ru": "Русский", "en": "English"}      # what the language dropdown of a lesson shows for each code
TWO_COLUMNS_FROM = 600                        # interactive_text(two_columns_from_px=...), the container width
SHEET_BELOW = 750                             # render_gloss_sheet(sheet_below_px=...), the viewport width
SHEET_MAX_SHARE = 0.55                        # the share of the screen height a fixed sheet may take
MAX_SNAPSHOT_FILE = 5_000_000                 # a bigger file in a lesson folder is not copied (none is written by a run)
LOAD_TIMEOUT_MS = 240_000                     # a lesson loads its backends first
ACTION_TIMEOUT_MS = 8_000                     # a tap or a choice that takes longer than this has not worked
ARCHIVE_LINK = "https://web.archive.org/"     # the archive links of the translation source lines (KB text) are cut on a phone; left as they are since 2026-11-09: counted, not failed
LOST_MODULE = "Virtual file not found"        # the server's line when marimo deleted the module of a widget before the page fetched it (marimo issue 10494)
MAX_RELOADS = 4                               # a page that lost the module is loaded again this often before the run fails


class Cannot(Exception):
    """The tool cannot run here: exit status 2."""


# ---------------------------------------------------------------------------------------------------- what to check

def lesson_notebooks(scope: pathlib.Path) -> "list[pathlib.Path]":
    """The tracked lesson notebooks below scope (or scope itself, a notebook) that call render_gloss_sheet."""
    scope = (REPO_ROOT / scope).resolve()      # an absolute scope stays as it is
    if not scope.exists():
        raise Cannot(f"no such file or folder: {scope.relative_to(REPO_ROOT) if scope.is_relative_to(REPO_ROOT) else scope} "
                     "(a list of languages or widths is comma-separated: --langs el,ru)")
    if scope.is_file():
        return [scope]
    tracked = subprocess.run(["git", "-C", str(REPO_ROOT), "ls-files", "-z", "*.py"], capture_output=True, text=True, check=True).stdout.split("\0")
    found = []
    for name in tracked:
        path = REPO_ROOT / name
        if EXPORTED_NOTEBOOK.search(name) and path.is_file() and path.is_relative_to(scope) and USES_LAYOUT in path.read_text(encoding="utf-8"):
            found.append(path)
    return sorted(found)


def check_prerequisites() -> None:
    """Raise Cannot with the thing that is missing."""
    try:
        import playwright.sync_api  # noqa: F401
    except ImportError:
        raise Cannot(f"Playwright is not installed in {sys.executable} (pip install playwright; a Chromium is needed too)") from None
    if subprocess.run([sys.executable, "-m", "marimo", "--version"], capture_output=True, check=False).returncode != 0:
        raise Cannot(f"marimo is not installed in {sys.executable}")
    try:
        import eee_project
    except ImportError:
        raise Cannot(f"eee-project is not installed in {sys.executable}") from None
    version = tuple(int(part) for part in re.findall(r"\d+", eee_project.__version__)[:3])
    if version < (1, 26, 0):
        raise Cannot(f"the lessons need eee-project 1.26.0 or newer (wrap=, translation=, render_gloss_sheet); {sys.executable} has {eee_project.__version__}")
    installed = importlib.metadata.version("eee-project")
    if installed != eee_project.__version__:
        print(f"note: eee_project.__version__ is {eee_project.__version__} but the installed metadata says {installed} (an editable install made before a version bump?); "
              "an export from this Python with an older marimo pins the metadata version", file=sys.stderr)


def launch_chromium(playwright):
    """A launched Chromium: EEE_CHROMIUM, a Chromium on the PATH or under /opt/pw-browsers, then Playwright's own."""
    candidates = [os.environ.get("EEE_CHROMIUM"), shutil.which("chromium"), shutil.which("chromium-browser"),
                  *sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome")), None]
    last = None
    for executable in candidates:
        if executable is not None and not pathlib.Path(executable).exists():
            continue
        try:
            return playwright.chromium.launch(**({"executable_path": executable} if executable else {}), args=["--no-sandbox"])
        except Exception as exc:  # noqa: BLE001 - whatever Playwright raises, try the next candidate
            last = exc
    raise Cannot(f"no Chromium could be started (set EEE_CHROMIUM to a binary): {str(last).strip().splitlines()[0] if last else 'none found'}")


# -------------------------------------------------------------------------------------------- a lesson, run for real

@contextlib.contextmanager
def restored_folder(folder: pathlib.Path):
    """Copy the files of the lesson folder, and put them back at exit: written files restored, new files removed."""
    saved = {p: p.read_bytes() for p in folder.rglob("*") if p.is_file() and ".git" not in p.parts and p.stat().st_size <= MAX_SNAPSHOT_FILE}
    try:
        yield
    finally:
        for p in folder.rglob("*"):
            if p.is_file() and ".git" not in p.parts and p not in saved and p.stat().st_size <= MAX_SNAPSHOT_FILE:
                p.unlink()
        for p, data in saved.items():
            if not p.is_file() or p.read_bytes() != data:
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(data)


@contextlib.contextmanager
def marimo_run(notebook: pathlib.Path):
    """`marimo run` on the notebook; yields (its URL, a function that returns what the server printed so far)."""
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    with tempfile.TemporaryFile() as log:
        process = subprocess.Popen([sys.executable, "-m", "marimo", "run", str(notebook), "--headless", "--host", "127.0.0.1", "--port", str(port)],
                                   stdout=log, stderr=subprocess.STDOUT, cwd=notebook.parent)

        def printed() -> str:
            log.seek(0)
            return log.read().decode("utf-8", "replace")

        url = f"http://127.0.0.1:{port}/"
        try:
            for _ in range(240):
                if process.poll() is not None:
                    raise Cannot(f"marimo run {notebook.name} stopped at once: {printed().strip().splitlines()[-1:] or 'no output'}")
                try:
                    if urllib.request.urlopen(url, timeout=1).status == 200:
                        break
                except OSError:
                    time.sleep(0.5)
            else:
                raise Cannot(f"marimo run {notebook.name} did not answer within two minutes")
            yield url, printed
        finally:
            process.terminate()
            try:
                process.wait(timeout=20)
            except subprocess.TimeoutExpired:
                process.kill()


# ------------------------------------------------------------------------------------------------- the browser checks

def box(page, selector: str):
    """The bounding box of the first match; a widget drawn again by the kernel has none for a moment, so it is asked again."""
    for _ in range(15):
        try:
            found = page.locator(selector).first.bounding_box(timeout=1000) if page.locator(selector).count() else None
        except Exception:  # noqa: BLE001 - the element went away while it was asked for; ask again
            found = None
        if found is not None:
            return found
        page.wait_for_timeout(200)
    return None


def wait_until(page, condition, seconds: float = 20.0) -> bool:
    """Poll condition() until it holds; page.wait_for_timeout keeps Playwright's events (a page error) flowing."""
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        try:
            if condition():
                return True
        except Exception:  # noqa: BLE001 - an element that the kernel just replaced is not there yet; ask again
            pass
        page.wait_for_timeout(200)
    return False


def styled(page) -> bool:
    """The rules of the widget are applied: the wrapped Greek lines have their hanging indent."""
    return page.locator(f"{GREEK}.wrap .eee-line").first.evaluate("el => parseFloat(getComputedStyle(el).textIndent) < 0")


def language_shown(page, lang: str) -> bool:
    """The lesson is drawn in the interface language asked for: its language dropdown shows the name of that language (a lesson starts in its default one)."""
    selects = page.locator("select")
    return any(selects.nth(i).evaluate("s => s.value") == LANGUAGE_NAME[lang] for i in range(selects.count())) if lang in LANGUAGE_NAME else True


def close_sheet(page) -> None:
    """A fixed sheet covers the lower part of a phone screen: close it before the next tap."""
    close = page.locator(".eee-sheet-close")
    if close.count() and close.first.is_visible():      # a wide page hides the button: its sheet is part of the page
        close.first.click()
        wait_until(page, lambda: not sheet_state(page)["open"], 5)


def sheet_state(page) -> dict:
    """The sheet as it is now. `open` means: in the page, not hidden by the close button, and holding a word."""
    return page.locator(SHEET).first.evaluate(
        """el => { const r = el.getBoundingClientRect(), cs = getComputedStyle(el);
                   return {cls: el.className, position: cs.position, display: cs.display, bottom: r.bottom, height: r.height,
                           screen: window.innerHeight, text: el.innerText.trim(),
                           open: el.isConnected && cs.display !== 'none' && r.height > 0 && /(^| )on( |$)/.test(el.className)}; }""")


def fits(page, width: int) -> "list[str]":
    """The block stays inside the page, and the Greek and the card inside the block."""
    problems = []
    wrap, greek, card = box(page, STANZA), box(page, GREEK), box(page, CARD)
    if wrap is None or greek is None:
        return ["the text block has no size"]
    if wrap["x"] + wrap["width"] > width + 0.5:
        problems.append(f"the text block reaches x={wrap['x'] + wrap['width']:.0f}, past the {width} px page")
    if greek["x"] + greek["width"] > wrap["x"] + wrap["width"] + 0.5:
        problems.append("the Greek text is wider than the block")
    if card is not None and card["x"] + card["width"] > wrap["x"] + wrap["width"] + 0.5:
        problems.append("the translation card is wider than the block")
    return problems


# Every element that ends past the page and is neither fixed nor inside a fixed box (the table of contents of marimo is one), shadow roots included. `reach` is the right edge of the
# text block that holds the element: text right after a link, such as ").", counts too. Not `scrollWidth > clientWidth` of each element: that flags the parents of an overflowing link too.
RIGHT_EDGE_JS = """width => {
    const app = document.getElementById('App'), found = [];
    const pinned = el => { for (let n = el; n; n = n.parentElement || n.getRootNode().host) if (getComputedStyle(n).position === 'fixed') return true; return false; };
    const blockOf = el => { let b = el.parentElement; while (b && getComputedStyle(b).display.startsWith('inline')) b = b.parentElement; return b || el; };
    const walk = root => { for (const el of root.querySelectorAll('*')) {
        const r = el.getBoundingClientRect();
        if (r.width > 0 && r.right > width + 1 && !pinned(el)) {
            const text = document.createRange(); text.selectNodeContents(blockOf(el));
            found.push({tag: el.tagName.toLowerCase(), href: typeof el.href === 'string' ? el.href : '', right: Math.round(r.right), reach: Math.round(text.getBoundingClientRect().right),
                        text: (el.innerText || '').trim().replace(/\\s+/g, ' ').slice(0, 40)}); }
        if (el.shadowRoot) walk(el.shadowRoot); } };
    walk(document);
    return {app: app && [app.scrollWidth, app.clientWidth], found}; }"""


def sideways(page, width: int) -> "tuple[list[str], set[str]]":
    """(problems, accepted): `div#App` holds more than the page is wide, or an element ends past the right edge. The cut archive links of the
    translation source line are not problems: their addresses come back as `accepted`. (The scroll width of the page itself says nothing: `div#App` scrolls inside it.)"""
    got = page.evaluate(RIGHT_EDGE_JS, width)
    if got["app"] is None:
        return ["div#App is not in the page, so a sideways scroll cannot be measured"], set()
    cut, others = [], []
    for found in got["found"]:
        (cut if found["href"].startswith(ARCHIVE_LINK) else others).append(found)
    scroll, client = got["app"]
    problems = []
    if scroll > max([client, *(e["reach"] for e in cut)]) + 1:      # what the accepted links cause (with the text after them) is not counted
        problems.append(f"the page scrolls sideways inside div#App: {scroll} px of content in a {client} px page")
    if others:
        problems.append("past the right edge: " + "; ".join(f"{e['tag']} {e['text']!r} ends at x={e['right']}" for e in others[:3])
                        + (f" (and {len(others) - 3} more)" if len(others) > 3 else ""))
    return problems, {e["href"] for e in cut}


def placement(page) -> "tuple[str, list[str]]":
    """('beside' | 'under', problems): where the card stands, against the rule of the container query."""
    wrap, greek, card = box(page, STANZA), box(page, GREEK), box(page, CARD)
    if wrap is None or greek is None or card is None:
        return "?", ["the text block or the card has no size"]
    beside = card["x"] >= greek["x"] + greek["width"] - 1 and abs(card["y"] - greek["y"]) < 6
    under = card["y"] >= greek["y"] + greek["height"] - 1
    where = "beside" if beside else "under" if under else "?"
    expected = "beside" if wrap["width"] >= TWO_COLUMNS_FROM else "under"
    problems = [] if where == expected else [f"the card stands {where!r} the Greek in a {wrap['width']:.0f} px block, expected {expected!r}"]
    return where, problems


def pickers(page):
    """(stanza dropdown, translation dropdown): the one with the blank entry and the one before it; (None, None) when the page has no such pair."""
    selects = page.locator("select")
    for i in range(selects.count()):
        if BLANK in option_values(selects.nth(i)):
            return (selects.nth(i - 1) if i else None), selects.nth(i)
    return None, None


def option_values(select) -> "list[str]":
    return select.evaluate("s => [...s.options].map(o => o.value)")


def check_sheet_after_tap(page, width: int, label: str) -> "list[str]":
    """The sheet is open after a tap and sits where its width says."""
    if not wait_until(page, lambda: sheet_state(page)["open"]):
        return [f"{label}: the sheet did not open"]
    page.wait_for_timeout(300)      # the kernel may still be swapping the element of the sheet
    state, problems = sheet_state(page), []
    if not state["text"]:
        problems.append(f"{label}: the sheet is empty")
    expected = "fixed" if width < SHEET_BELOW else "static"
    if state["position"] != expected:
        problems.append(f"{label}: the sheet is {state['position']!r} on a {width} px page, expected {expected!r}")
    if expected == "fixed":
        if abs(state["bottom"] - state["screen"]) > 2:
            problems.append(f"{label}: the fixed sheet ends at y={state['bottom']:.0f}, not at the bottom of the screen ({state['screen']})")
        if state["height"] > SHEET_MAX_SHARE * state["screen"] + 2:
            problems.append(f"{label}: the sheet takes {state['height'] / state['screen']:.0%} of the screen, at most {SHEET_MAX_SHARE:.0%}")
    return problems


def settle(page, quiet: float = 1.5, limit: float = 15.0) -> None:
    """Wait until the text of the page has stopped changing (a lesson is drawn again once the language kept in localStorage reaches the kernel), or the limit."""
    def snapshot() -> str:
        return page.evaluate("() => document.body.innerText") + page.locator(GREEK).first.inner_text()

    last, changed, deadline = snapshot(), time.monotonic(), time.monotonic() + limit
    while time.monotonic() < deadline:
        page.wait_for_timeout(250)
        now = snapshot()
        if now != last:
            last, changed = now, time.monotonic()
        elif time.monotonic() - changed >= quiet:
            return


def kernel_errors(printed, since: int) -> "list[str]":
    """The exception lines (a NameError in a cell...) that the server printed after offset `since` of its output."""
    found = re.findall(r"(?m)^[\w.]*(?:Error|Exception)\b.*$", printed()[since:])
    return sorted({line.strip()[:200] for line in found})


def model_id(page) -> str:
    """The id of the model of the stanza widget: a widget that the kernel draws again has a new one, a moment after the choice that caused it.
    While the kernel draws it again the text has no host, so there is no id yet: the function waits up to 2 s for the new one, then raises."""
    for _ in range(20):
        found = page.locator(GREEK).first.evaluate("el => { const host = el.getRootNode().host; return host ? host.getAttribute('data-model-id') : null; }")
        if found:
            return found
        page.wait_for_timeout(100)
    raise RuntimeError("the stanza widget has no model id for 2 s")


def choose(page, select, value: str) -> bool:
    """Choose a value of a dropdown and, when that changes it, wait until the kernel has drawn the stanza widget again (the old one stays for a moment)."""
    before, current = model_id(page), select.evaluate("s => s.value")
    select.select_option(value)
    return current == value or wait_until(page, lambda: model_id(page) != before, 20)


def show(page, stanza, stanza_value: "str | None", translation, translator: str) -> bool:
    """Choose a stanza (None: keep) and a translator, and wait for the card of that pair. False when it does not come."""
    try:
        if (stanza_value is not None and not choose(page, stanza, stanza_value)) or not choose(page, translation, translator):
            return False
    except Exception:  # noqa: BLE001 - the dropdown is gone: the cell that draws it raised an error
        return False
    return wait_until(page, lambda: page.locator(CARD).count() == 1 and page.locator(f"{STANZA} .gk-word").count() > 0 and styled(page), 40)


def check_translations(page, width: int, all_stanzas: bool) -> "tuple[list[str], list[str], tuple | None]":
    """Every translator (with all_stanzas: in every stanza) draws a card that fits. Returns (problems, notes, the first (stanza, translator) with margin notes)."""
    stanza, translation = pickers(page)
    translators = [o for o in option_values(translation) if o != BLANK]
    stanzas = option_values(stanza) if stanza is not None and all_stanzas else [None]
    problems, with_notes, shown, accepted = [], None, 0, set()
    for stanza_value in stanzas:
        for translator in translators:
            where = f"translation {translator!r}" + (f" in stanza {stanza_value!r}" if stanza_value else "")
            if not show(page, stanza, stanza_value, translation, translator):
                problems.append(f"{where}: no card")
                if pickers(page)[1] is None:
                    problems.append("the dropdowns are gone after this choice (the cell that draws them raised an error)")
                    return problems, [], with_notes
                continue
            shown += 1
            problems += [f"{where}: {p}" for p in fits(page, width)]
            bad, cut = sideways(page, width)
            problems += [f"{where}: {p}" for p in bad]
            accepted |= cut
            if with_notes is None and page.locator(f"{STANZA} {NOTE}").count():
                with_notes = (stanza_value, translator)
    notes = [f"{len(translators)} translations" + (f" in {len(stanzas)} stanzas" if stanza is not None and all_stanzas else ""),
             "margin notes at " + (f"{with_notes[1]!r}" + (f" in {with_notes[0]!r}" if with_notes[0] else "") if with_notes else "none")]
    if accepted:
        notes.append(f"{len(accepted)} archive link(s) past the edge (accepted)")
    return problems, notes, with_notes


def check_note(page, width: int) -> "list[str]":
    """With a margin-note card on show: a tap on a noted word shows its note and clears the Greek word; a tap on a Greek word clears the note."""
    problems = []
    close_sheet(page)
    page.locator(f"{STANZA} {NOTE}").first.click()
    if not wait_until(page, lambda: page.locator(f"{STANZA} {NOTE}.active").count() == 1):
        return ["a tap on a noted word selects no note"]
    problems += check_sheet_after_tap(page, width, "a noted word")
    if page.locator(f"{STANZA} .gk-word.active").count():
        problems.append("a Greek word stays selected beside a note")
    if not page.locator(f"{SHEET} .eee-note-word").count():
        problems.append("the sheet does not show the note of a noted word")
    close_sheet(page)
    page.locator(f"{STANZA} .gk-word").first.click()
    if not wait_until(page, lambda: page.locator(f"{STANZA} {NOTE}.active").count() == 0):
        problems.append("a note stays selected after a tap on a Greek word")
    return problems


def check_page(page, width: int, all_stanzas: bool) -> "tuple[list[str], list[str]]":
    """(problems, notes) for one loaded lesson at one width."""
    problems: list[str] = []
    notes: list[str] = []
    if not page.locator(f"{STANZA} .gk-word").count():
        problems.append("no text block with a translation card by default")
    else:
        problems += fits(page, width)
        problems += sideways(page, width)[0]      # the accepted links are counted by check_translations
        lines = page.locator(f"{GREEK}.wrap .eee-line")
        if not lines.count():
            problems.append("the Greek lines are not drawn with wrap=True")
        elif lines.first.evaluate("el => parseFloat(getComputedStyle(el).textIndent)") >= 0:
            problems.append("the wrapped Greek lines have no hanging indent")
        where, bad = placement(page)
        problems += bad
        notes.append(f"card {where}")

        # a tap on a Greek word; on a phone: close the sheet, and the next word opens it again
        words = page.locator(f"{STANZA} .gk-word")
        words.first.click()
        problems += check_sheet_after_tap(page, width, "a Greek word")
        close = page.locator(".eee-sheet-close")
        if width < SHEET_BELOW and words.count() > 1 and close.count() and close.first.is_visible():     # hidden: the sheet did not open, reported above
            close.first.click()
            if not wait_until(page, lambda: not sheet_state(page)["open"], 5):
                problems.append("the close button does not hide the sheet")
            words.nth(1).click()
            problems += check_sheet_after_tap(page, width, "the next word after closing")
        close_sheet(page)

        # every translator (in every stanza, on the narrowest page): a card that fits; the notes; the blank entry
        stanza, translation = pickers(page)
        if translation is None:
            problems.append("no translation dropdown with a blank entry")
        else:
            bad, more, with_notes = check_translations(page, width, all_stanzas)
            problems += bad
            notes += more
            if with_notes:
                stanza_value, translator = with_notes
                if show(page, stanza, stanza_value, translation, translator):
                    problems += check_note(page, width)
                else:
                    problems.append("the card with margin notes does not come back")
            if pickers(page)[1] is not None:
                translation.select_option(BLANK)
                if not wait_until(page, lambda: page.locator(CARD).count() == 0):
                    problems.append("the blank entry does not remove the translation card")
                elif not page.locator(f"{GREEK}.wrap .eee-line").count():
                    problems.append("the blank entry removes the Greek text with the card")
    return problems, notes


def describe(exc: Exception) -> str:
    """One line for a failed browser call: the exception's name and the first lines of Playwright's message."""
    return f"{type(exc).__name__}: " + " | ".join(line.strip() for line in str(exc).strip().splitlines()[:3])[:300]


def wait_for_greek(page, printed, old: int) -> int:
    """Wait for the Greek text and return how often the page was loaded again; give up early, with what the server printed, when the lesson raised an error and the text stays away.
    `old` is the length of the server output before this load began: what the server printed earlier is not an error of this page.
    marimo (issue 10494) sometimes deletes the module of the stanza widget before the page fetched it: the server prints `Virtual file not found`, and if the lost module is the one of the
    widget that stays, the page shows no text for good. A new load of the page fixes that, so only this error is answered with up to MAX_RELOADS new loads; any other error still ends the wait."""
    failed_at, reloads = None, 0
    deadline = time.monotonic() + LOAD_TIMEOUT_MS / 1000
    while time.monotonic() < deadline:
        if page.locator(f"{GREEK} .gk-word").count():
            return reloads
        if failed_at is None and "Traceback (most recent call last)" in printed()[old:]:
            failed_at = time.monotonic()
        if failed_at is not None and time.monotonic() - failed_at > 30:
            if LOST_MODULE in printed()[old:] and reloads < MAX_RELOADS:
                old = len(printed())      # taken before the load starts: what the server prints while the page loads counts
                page.reload(wait_until="load", timeout=LOAD_TIMEOUT_MS)
                failed_at, reloads = None, reloads + 1
                deadline = time.monotonic() + LOAD_TIMEOUT_MS / 1000      # the limit counts from the newest load
            else:
                tail = [line for line in printed().splitlines() if line.strip()][-4:]
                again = f" (page loaded again {reloads}x)" if reloads else ""
                raise RuntimeError(f"the lesson raised an error and shows no text{again}: " + " | ".join(line.strip()[:200] for line in tail))
        page.wait_for_timeout(1000)
    raise RuntimeError(f"no clickable Greek text within {LOAD_TIMEOUT_MS // 1000} s")


def check_notebook(browser, url: str, printed, widths: "list[int]", langs: "list[str]"):
    """Yield (lang, width, problems, notes) for each run of a running lesson. The narrowest width also goes through every stanza."""
    for lang in langs:
        for width in widths:
            context = browser.new_context(viewport={"width": width, "height": 844})
            context.add_init_script(f"try {{ localStorage.setItem('eee_lang', '{lang}'); }} catch (e) {{}}")
            page = context.new_page()
            page.set_default_timeout(ACTION_TIMEOUT_MS)
            errors: list[str] = []
            page.on("pageerror", lambda exc, errors=errors: errors.append(str(exc).splitlines()[0][:160]))
            problems: list[str] = []
            notes: list[str] = []
            try:
                opened = len(printed())
                page.goto(url, wait_until="load", timeout=LOAD_TIMEOUT_MS)
                reloads = wait_for_greek(page, printed, opened)
                first = model_id(page)
                wait_until(page, lambda: model_id(page) != first and language_shown(page, lang), 60)     # drawn again when the stored language reaches the kernel; a tap before is lost
                settle(page)
                wait_until(page, lambda: styled(page), 120)      # a stylesheet that never comes is reported by the checks below
                since = len(printed())
                try:
                    problems, notes = check_page(page, width, all_stanzas=width == min(widths))
                except Exception as exc:  # noqa: BLE001 - a timeout or a closed page is a finding, not a crash of the tool
                    problems = [describe(exc)]
                if reloads:
                    notes.append(f"page loaded again {reloads}x (marimo issue 10494)")
                problems += [f"the lesson raised an error: {line}" for line in kernel_errors(printed, since)]
            except Exception as exc:  # noqa: BLE001 - the lesson did not even start
                problems = [describe(exc)]
            problems += [f"uncaught JavaScript error: {e}" for e in sorted(set(errors))]
            context.close()
            yield lang, width, problems, notes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("scope", nargs="*", type=pathlib.Path, help="Notebooks, or folders with lesson notebooks, relative to the repo root (default: the whole repo)")
    parser.add_argument("--widths", default="390,830", help="Page widths in px, comma-separated (default: 390,830)")
    parser.add_argument("--langs", default="el,ru,en", help="Interface languages, comma-separated (default: el,ru,en)")
    parser.add_argument("--list", action="store_true", help="Only name the notebooks that would be checked")
    args = parser.parse_args()
    widths, langs = [int(w) for w in args.widths.split(",")], args.langs.split(",")

    try:
        notebooks = sorted({n for scope in (args.scope or [pathlib.Path(".")]) for n in lesson_notebooks(scope)})
        if args.list:
            for notebook in notebooks:
                print(notebook.relative_to(REPO_ROOT).as_posix())
            print(f"{len(notebooks)} notebook(s) call {USES_LAYOUT[:-1]}")
            sys.exit(0)
        if not notebooks:
            raise Cannot(f"no notebook {'below ' + ', '.join(map(str, args.scope)) if args.scope else 'of this repository'} calls {USES_LAYOUT[:-1]}, so there is nothing to check")
        check_prerequisites()
        from playwright.sync_api import sync_playwright

        failures = 0
        with sync_playwright() as playwright:
            browser = launch_chromium(playwright)
            for notebook in notebooks:
                name = notebook.relative_to(REPO_ROOT).as_posix()
                started, runs, bad = time.monotonic(), 0, 0
                print(name, flush=True)
                with restored_folder(notebook.parent), marimo_run(notebook) as (url, printed):
                    for lang, width, problems, notes in check_notebook(browser, url, printed, widths, langs):
                        runs, bad = runs + 1, bad + bool(problems)
                        detail = f" ({'; '.join(notes)})" if notes else ""
                        for problem in problems:
                            print(f"    FAIL {lang} {width}px: {problem}", flush=True)
                        if not problems:
                            print(f"    ok   {lang} {width}px{detail}", flush=True)
                failures += bad
                print(f"  {runs} run(s), {bad} failed ({time.monotonic() - started:.0f} s)", flush=True)
            browser.close()
    except Cannot as exc:
        print(f"cannot run: {exc}", file=sys.stderr)
        sys.exit(2)
    print(f"{len(notebooks)} notebook(s) checked, {failures} run(s) failed")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
