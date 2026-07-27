# B1 Greek Language and Culture — Agent Reference

Covers all sub-courses under this umbrella: `kapodistrias/`, `zorba/`, and `kavafis_ithaki/`.
**`kavafis_ithaki/` uses a different notebook architecture than the other two** — see
"Kavafis Ithaki: a second notebook architecture" below before touching it.

## Directory layout

```
b1greeklanguageandculture/
  kapodistrias/
    index.tsv          # trilingual lesson index (url, icon, greek, label_{ru,el,en}, title_{ru,el,en}, desc_{ru,el,en}, index_url)
    notebook.py           # index/parent notebook
    26_05_01/ 26_05_08/ 26_05_15/ 26_05_22/   # one dir per lesson (YY_MM_DD)
  zorba/
    index.tsv          # same trilingual schema
    notebook.py           # index/parent notebook
    26_06_26/ 26_07_10/ 26_07_17/   # one dir per lesson (YY_MM_DD)
  kavafis_ithaki/
    index.tsv          # same trilingual schema
    notebook.py           # index/parent notebook
    1/                     # one dir per lesson, numbered (not dated) -- matches the source material's own numbering
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

## Index notebook + index.tsv

Each course's `notebook.py` reads its own `index.tsv` (trilingual schema — see Directory layout above) and renders one card per row via `ConfigStore.from_url(...)` + `eee_card_list(mo, cfg, lang_sel.value)` (shared across all index notebooks — don't hand-roll the card CSS/loop again). A row with an empty `url` renders as a disabled "coming soon"/"σύντομα"/"скоро" card — this is the correct state for a lesson that's built but not yet uploaded to molab. Once uploaded, add the real `url` (the full `https://molab.marimo.io/notebooks/nb_XXX/app` link) to both the lesson's own `_badge` line and its `index.tsv` row — these are two independent places, keep them in sync.

### Course-index hero + topbar: own name vs. grouping context

On a course's own index page (Kapodistrias, Zorba), `eee_hero`'s large title is **this course's own name** with no "Lesson series —"/"Σειρά μαθημάτων —" prefix (e.g. "Αλέξης Ζορμπάς", not "Σειρά μαθημάτων — Αλέξης Ζορμπάς") — the small subtitle carries the grouping context instead (e.g. "B1: Ελληνική Γλώσσα και Πολιτισμός"). This is the opposite of what you'd get by copying B1's own hero cell (where the large title *is* "B1: ...", correctly, since that page is describing itself).

`eee_topbar`'s `style="index"` call needs `parent_titles=` set to that same B1 name dict whenever `back_url` comes from `parent_back_url()` — without it, the up-link falls back to `titles` (this course's own name) and mislabels itself, e.g. showing "● Αλέξης Ζορμπάς" (or, post-fix, "◀ Αλέξης Ζορμπάς") as the clickable link to B1 instead of "◀ B1: Ελληνική Γλώσσα και Πολιτισμός". See both current index notebooks' topbar cell for the pattern.

---

## Kavafis Ithaki: a second notebook architecture

`kavafis_ithaki/` deliberately does **not** follow "Never hand-write this machinery" /
`gu.create_noun_test_ui` above — that convention is kapodistrias/zorba-specific, not a
whole-umbrella rule. `kavafis_ithaki/1/notebook.1.py` was built to match `ellinika_b`
chapter 1's newer architecture instead (user-confirmed decision, 2026-07-25):

- **One `gu2 = GreekUtils(mg_backend, mo, pd, eee_module=eee, config=MODERN_GREEK)`
  instance for everything** — noun/verb/adjective drills use the newer
  `gu2.make_paradigm_drill_state` / `gu2.paradigm_drill_widgets` /
  `gu2.noun_paradigm_drill_form` / `gu2.verb_paradigm_drill_form` /
  `gu2.adjective_paradigm_drill_form` family (copied verbatim from
  `ellinika_b/chapter_01/chapter_01_notebook.py`), not kapodistrias's older
  `gu.create_noun_test_ui`/`check_noun_test`. `gu2.get_words`/`gu2.load_data` cover table
  loading too — **no `modern_greek_eee`/`modern_greek_inflexion_eee` dependency at all**
  (ellinika_b still imports those for an old `gu` it uses only for `get_words`/`load_data`;
  those are already methods on `eee_project.GreekUtils` itself, so this notebook's header
  only needs `eee-project` + `modern-greek-backend-eee` + `marimo` + `pandas`).
- **All UI chrome text goes through `t_ui = gu2.ui_label`** (TSV-backed,
  `eee_project/data/labels/ui-{lang}.tsv`) — never a hand-rolled `UI_STRINGS` dict like
  kapodistrias/zorba use. Added new keys for this lesson (`poem_section_heading`,
  `vocabulary_heading`, plus the `test_label`/`*_test_topic` set described below) to
  the 3 `ui-{lang}.tsv` files in `eee-project` itself; if a future lesson needs another
  chrome string, add it the same way rather than starting a local dict.
- **The poem stanza is plain text, deliberately** — an earlier draft used
  `eee.interactive_text(...)` (clickable words + a click-to-gloss paradigm-table panel,
  ported from Odyssey) but the user asked for it to be removed (2026-07-25): "in stanza
  we don't need any links or highlighting on words -- it's just a common text." The poem
  cell just renders `_stanza["lines"]` as plain `<div>` rows next to the selected
  translation's lines — no `anywidget`, no `CLICKABLE_FORMS`, no
  `build_modern_paradigm_table`/gloss-panel machinery at all. Don't re-add clickable
  poem text here without checking with the user first — it was tried and explicitly
  rejected. `POEM_WORDS_RAW` (from `poem_vocab.tsv`) still exists, but purely as the
  translation-presence exercise's word pool, not for any click target.
- **Parallel translations**: a `trans_selector` dropdown (подстрочник + literary
  translations) reading `greek.md` + `translations.md` via the same shared
  `eee.parse_stanza_text`/`eee.parse_stanza_translations` functions Odyssey uses
  (see `ancient_greek/odyssey/AGENTS.md`) — this lesson just passes the default
  `ref_prefix="### "` instead of Odyssey's `"### Odyss. "`, since the stanza-ref
  heading text differs per course. These used to be per-notebook local
  `_parse_greek`/`_parse_trans` functions (an 8th near-identical copy across Odyssey's
  7 lessons + this one); extracted into `eee_project/notebook_utils.py` and all 8
  call sites migrated, 2026-07-25. **Both the
  dropdown's option order and `translations.md`'s section order must match the order
  the translations are listed in the lecture's own `notes.md`** (Шмаков/Бродский →
  Ильинская → Левитов, подстрочник always first since it's this notebook's own
  addition, not from `notes.md`; Keeley/Sherrard last since English wasn't in that
  list at all) — don't alphabetize or reorder for any other reason.
- **New exercise type — translation-presence ("слово в переводе")** — added to the
  common-words tests as **Test 1** (not the last test — user-requested reordering,
  2026-07-25: it's poem-specific, so it comes right after the poem section, before the
  general nouns/verbs/adjectives drills, which shift to Tests 2/3/4), using the *same*
  `gu2.sync_translation_presence_tsv` / `gu2.build_translation_presence_items` /
  `gu2.balance_presence_items` / `gu2.translation_presence_widgets` /
  `gu2.translation_presence_form` machinery Odyssey uses, fed by `poem_vocab.tsv`
  (Odyssey's `form\tlemma\tpos\tcontext\tmeaning` schema — a *different* vocab file
  from `nouns.tsv`/`verbs.tsv`/`adjectives.tsv`, holding only the ~9 words that actually
  occur inflected in the 3 poem lines) and a hand-judged `translation_presence.tsv`
  (4 literary translators × the words each stanza actually contains; подстрочник
  excluded, matching Odyssey's own convention that подстрочник is definitionally 100%
  faithful). `translation_presence_widgets`/`_form` already take a `lang=` kwarg backed
  by `_YES_NO`/`_PRESENCE_EMPTY` (ru/en/el all present) — no extra chrome work needed
  there. Fixed one real (not just cosmetic) bug found while wiring this: the exercise's
  source/translation toggle switch caption hardcoded "(Ancient Greek)"/"(др.-греч.)"/
  "(αρχ. ελλ.)" — wrong for a Modern Greek poem; genericized to just "the original" in
  `eee_project`'s `_PRESENCE_SWITCH_LBL`, a pure wording fix with no signature change,
  safe for Odyssey's existing 7 lessons too (the passage's own attribution, shown via the
  already-generic `_PRESENCE_SOURCE_LBL`, was correct already).
- **Numbered test headings don't reuse ellinika_b's `test1_heading`/`test2_heading`/
  `test3_heading` keys** — those bake a fixed topic into a fixed number ("## Тест 1:
  Существительные") and ellinika_b's own lessons already depend on that exact
  noun=1/verb=2/adj=3 mapping. Since this lesson's own order is
  presence=1/noun=2/verb=3/adj=4, the heading cells compose two smaller, reusable
  `ui_label` keys instead: `test_label` (bare "Тест"/"Test"/"Τεστ") + a topic key
  (`presence_test_topic`/`noun_test_topic`/`verb_test_topic`/`adj_test_topic`), e.g.
  `f"## {t_ui('test_label', lang)} 1: {t_ui('presence_test_topic', lang)}"` — the
  number itself is a plain digit, not translated. Reuse this composable pair for any
  future lesson that needs its own test ordering, rather than adding another
  `testN_heading`-style monolithic key.
- **Two vocab TSVs coexist, don't confuse them**: `nouns.tsv`/`verbs.tsv`/`adjectives.tsv`
  (lemma-based, `Word\tTranslation`, the full 26/15/10-word curated class vocabulary from
  the dated master-notes section — feeds the common-words paradigm-drill tests) vs.
  `poem_vocab.tsv` (form-based, only the poem's own inflected words — feeds the
  translation-presence pool only, see above). `vocabulary.tsv` (3-col,
  `Word\tTranslation\tType`) is a third, non-drilled reference table for multi-word
  phrases/literary terms that don't fit a single-lemma drill — same pattern
  kapodistrias's own `vocabulary.tsv` already uses.
- Tested end-to-end via marimo-pair after the initial build, the plain-text/reorder
  revision, an `/simplify` cleanup pass, and the `_parse_greek`/`_parse_trans` extraction
  (0 errors across 52 cells throughout; verified real rendered content, not just
  "no error": noun drill with a real word, translation-presence items, all 4 heading
  numbers, the dropdown's translation order, and the plain-text poem markup). The
  parser extraction was also verified against `ancient_greek/odyssey/2026_07_20`
  (temporarily pointed at the local `eee-project` checkout) — identical `STANZAS`/
  `RHYTHM_HTML`/`QUIZ_WORDS_RAW`/`CLICKABLE_FORMS` shape before and after.
