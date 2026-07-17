# B1 Greek Language and Culture — Agent Reference

Covers both sub-courses under this umbrella: `kapodistrias/` and `zorba/`.

## Directory layout

```
b1greeklanguageandculture/
  kapodistrias/
    lessons.tsv          # trilingual lesson index (url, icon, greek, label_{ru,el,en}, title_{ru,el,en}, desc_{ru,el,en}, index_url)
    notebook.py           # index/parent notebook
    26_05_01/ 26_05_08/ 26_05_15/ 26_05_22/   # one dir per lesson (YY_MM_DD)
  zorba/
    lessons.tsv          # same trilingual schema
    notebook.py           # index/parent notebook
    26_06_26/ 26_07_10/ 26_07_17/   # one dir per lesson (YY_MM_DD)
```

Each lesson directory:

```
notebook.<YY_MM_DD>.py     ← the real notebook (imported/served)
slide-N.jpg                ← one JPG per source-presentation slide, 1-indexed
verbs.tsv, nouns.tsv, adjectives.tsv   ← vocabulary (Word\tTranslation, 2-col)
```

**Both courses moved here from `created_with_eee/kapodistrias/` on 2026-07-15** — they share the same B1-level lecture series (`~/work/greek/lectures/B1greeklanguageandculture/`), so they're grouped under one umbrella instead of living as unrelated top-level course dirs. `zorba/` was built fresh under the new layout; nothing in the wider repo referenced the old `kapodistrias/` path, so the move only required updating each notebook's own `ConfigStore.from_url(...)` calls (6 in kapodistrias, mechanical `sed` substitution — verify with `grep -rn "b1greeklanguageandculture" **/*.py` after any further restructuring).

---

## Source discipline — CRITICAL

**Base every cell on the lecture's own materials in `~/work/greek/lectures/B1greeklanguageandculture/<Course>/<lesson>/`** — the presentation (`.pptx`), and for the vocabulary specifically, the master notes file described below. **Do not invent vocabulary, dates, or biographical facts** — everything in these notebooks should trace back to a slide, a quote, or a dated vocabulary entry.

### Extracting PPTX content

`.pptx` files aren't directly readable — convert first:
```bash
soffice --headless --convert-to pdf "<file>.pptx"      # → readable PDF (Read tool handles it)
pdftoppm -jpeg -r 100 "<file>.pdf" slide                # → slide-1.jpg, slide-2.jpg, ... for the notebook's own _img() cells
```

### The master vocabulary/notes file — has a landmine

`~/work/greek/lectures/B1greeklanguageandculture/Α2-Β1_ Ιστορία και Πολιτισμός της Ελλάδας .md` is a single running log of **every** class session across **every** topic unit in this lecture series (El Greco, Kapodistrias, Zorz Sari, Zorba, ...), organized under `# DD/MM/YYYY [topic name]` headers, most recent at the bottom. This is the authoritative source for per-lesson vocabulary — cross-reference the lesson's date against the header to find its list.

**It is a 3MB file with only ~500 lines** — a handful of lines (screenshots someone pasted into the notes) are each 100,000+ characters of embedded base64 image data. A plain `Read` on the whole file, or even an unfiltered `offset`/`limit` slice through one of those lines, blows the token budget instantly. Always filter first:
```bash
awk 'length($0) < 2000' "<file>.md"     # drops the embedded-image lines, keeps all real text
```
Identify which dated section(s) belong to the lesson you're building (a session's date may not exactly match the lesson directory's own date — e.g. Zorba's two lesson notebooks pull vocabulary from three dated sessions: 26/06 for Lesson 1, and 3/7 + 10/7 combined for the merged Lesson 2-3), then hand-curate the noun/verb/adjective TSVs from that section only — the file's own POS grouping (Ουσιαστικά/Ρήματα/Επίθετα) usually maps directly to the three TSVs. Skip multi-word phrases (e.g. "δεν τα παρατάω") from the verb TSV — the conjugation drill expects a single lemma; keep such phrases as inline vocabulary notes in the content cell instead.

---

## Notebook structure

Every lesson notebook is one large trilingual (ru/el/en) file combining:

1. **A content cell** — `_lang`-branched `mo.vstack([...])`, interspersing `mo.md(...)` prose (title, biography/discussion text, closing vocabulary summary) with `_img(n)` calls for each relevant slide. This is the only cell that's genuinely lesson-specific.
2. **Noun/verb/adjective drill machinery** — identical across every lesson in both courses (confirmed: two arbitrary lessons diff at ~320 of ~1130-1213 lines, i.e. ~75% shared). Reads `nouns.tsv`/`verbs.tsv`/`adjectives.tsv` from the lesson's own directory, builds a `mo.ui.table` selector, then a skip/clear/submit drill loop per part of speech via `gu.create_noun_test_ui` / `gu.create_verb_test_ui` / `gu.create_adjective_test_ui` and `gu.check_*_test`.
3. **A trilingual `UI_STRINGS` dict + `t_ui()` helper** — all drill labels, not just content, are translated.
4. **A fixed-position `language_selector` dropdown** and shared `eee_footer`.

**Never hand-write this machinery.** To add a new lesson: copy the closest existing `notebook.<date>.py` as a template (matches the pattern documented in Palaestra's own AGENTS.md), then replace only:
- the content cell (all three `if _lang == "ru" / elif "el" / else` blocks),
- the `_badge` placeholder (`""` with a `# молаб-бейдж добавить после загрузки в molab` comment until the lesson is uploaded to molab — never invent a molab ID),
- the three vocabulary TSVs,
- the `slide-N.jpg` files.

Leave the drill machinery, `UI_STRINGS`, language selector, and footer untouched.

## Index notebook + lessons.tsv

Each course's `notebook.py` reads its own `lessons.tsv` (trilingual schema — see Directory layout above) and renders one card per row via `ConfigStore.from_url(...)` + `eee_card_list(mo, cfg, lang_sel.value)` (shared across all index notebooks — don't hand-roll the card CSS/loop again). A row with an empty `url` renders as a disabled "coming soon"/"σύντομα"/"скоро" card — this is the correct state for a lesson that's built but not yet uploaded to molab. Once uploaded, add the real `url` (the full `https://molab.marimo.io/notebooks/nb_XXX/app` link) to both the lesson's own `_badge` line and its `lessons.tsv` row — these are two independent places, keep them in sync.

### Course-index hero + topbar: own name vs. grouping context

On a course's own index page (Kapodistrias, Zorba), `eee_hero`'s large title is **this course's own name** with no "Lesson series —"/"Σειρά μαθημάτων —" prefix (e.g. "Αλέξης Ζορμπάς", not "Σειρά μαθημάτων — Αλέξης Ζορμπάς") — the small subtitle carries the grouping context instead (e.g. "B1: Ελληνική Γλώσσα και Πολιτισμός"). This is the opposite of what you'd get by copying B1's own hero cell (where the large title *is* "B1: ...", correctly, since that page is describing itself).

`eee_topbar`'s `style="index"` call needs `parent_titles=` set to that same B1 name dict whenever `back_url` comes from `parent_back_url()` — without it, the up-link falls back to `titles` (this course's own name) and mislabels itself, e.g. showing "● Αλέξης Ζορμπάς" (or, post-fix, "◀ Αλέξης Ζορμπάς") as the clickable link to B1 instead of "◀ B1: Ελληνική Γλώσσα και Πολιτισμός". See both current index notebooks' topbar cell for the pattern.
