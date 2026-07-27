# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.14",
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "ancient-greek-backend-eee @ git+https://codeberg.org/EEE-project/ancient-greek-backend-eee.git",
#     "unimorph-backend-eee @ git+https://codeberg.org/EEE-project/unimorph-backend-eee.git",
#     "modern-greek-backend-eee @ git+https://codeberg.org/EEE-project/modern-greek-backend-eee.git",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# ancient-greek-backend-eee = { git = "https://codeberg.org/EEE-project/ancient-greek-backend-eee.git" }
# unimorph-backend-eee = { git = "https://codeberg.org/EEE-project/unimorph-backend-eee.git" }
# modern-greek-backend-eee = { git = "https://codeberg.org/EEE-project/modern-greek-backend-eee.git" }
# ///

import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    cfg = ConfigStore.from_file_or_url(__file__, f"{_ROOT}/ancient_greek/odyssey/index.tsv", ga=f"{_ROOT}/ga.json")
    eee_topbar(mo, back_url=cfg.index_url(), lang="ru", titles={
        "ru": "Одиссея для отважных",
    }, ga_config=cfg.ga_config())
    return (cfg,)


@app.cell(hide_code=True)
def _(eee, mo):
    from pathlib import Path as _Ph
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_32dyZq8gA6x14GL2Zwa6ZU)"
    _left = mo.vstack([
        mo.md("# Одиссея для отважных"),
        mo.md(_badge),
        mo.md("## Пилотное занятие · Odyss. I.1–21"),
    ])
    _img = eee.magnify_image(
        mo, _Ph(__file__).parent / "Odysseus_Sirens_BM_E440_n2.jpg",
        raw_base="https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/ancient_greek/odyssey/2026_06_01",
        width=340,
    )
    mo.hstack([_left, _img], align="start")
    return


@app.cell(hide_code=True)
def _(mo):
    _base = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/ancient_greek/odyssey/2026_06_01"
    mo.md(
        f"**Материалы занятия:** "
        f"[Одиссея. Зачин.pdf]({_base}/Одиссея.%20Зачин.pdf) · "
        rf"[Одиссея\_1-21\_словарь.pdf]({_base}/Одиссея_1-21_словарь.pdf) · "
        f"[Греческий алфавит.pdf]({_base}/Греческий%20алфавит.pdf)"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Текст поэмы с параллельными переводами.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    _MURRAY = "<b>Homer.</b> <a href='https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0135'><i>The Odyssey</i></a> with an English Translation by A.T. Murray, PH.D. in two volumes. Cambridge, MA., Harvard University Press; London, William Heinemann, Ltd. 1919."
    mo.md(_MURRAY)
    return


@app.cell(hide_code=True)
def _(TRANS_DESC, mo, trans_selector):
    _PODSTROCHNIK_DESC = "**подстрочник** · буквальный перевод слово-в-слово с сохранением порядка оригинала"
    _desc_map = {"подстрочник": _PODSTROCHNIK_DESC, **TRANS_DESC}
    mo.md(_desc_map.get(trans_selector.value, ""))
    return


@app.cell(hide_code=True)
def _(cfg, gu, mo):
    from pathlib import Path as _P
    SHOW_ICTUS = mo.ui.switch(value=True)
    SHOW_HOMER = mo.ui.switch(value=True)

    # Shared across all 6 lessons. Fetched via ensure_file, not a bare local
    # read: molab only bundles files that live in the notebook's own directory,
    # so a parent-directory file like this one is missing there unless we
    # download it ourselves (matches the pattern already used for materials PDFs).
    _eee_note_path = gu.ensure_file(
        "eee_note.md", nb_dir=_P(__file__).parent.parent, remote_base=cfg.raw_base,
    )
    EEE_NOTE = _eee_note_path.read_text(encoding="utf-8") if _eee_note_path else (
        "*(не удалось загрузить описание движка EEE)*"
    )

    gu.ictus_toggle_panel(SHOW_ICTUS, SHOW_HOMER, EEE_NOTE,
                           ictus_color="#980000", ictus_color_name="красным")
    return EEE_NOTE, SHOW_HOMER, SHOW_ICTUS


@app.cell(hide_code=True)
def _(
    CLICKABLE_FORMS,
    HOMER_WORDS,
    RHYTHM_HTML,
    SHOW_HOMER,
    SHOW_ICTUS,
    STANZAS,
    eee,
    mo,
    stanza_selector,
    trans_selector,
):
    _st_map = {s["ref"]: s for s in STANZAS}
    _stanza = _st_map[stanza_selector.value]

    text_widget = eee.interactive_text(
        mo,
        lines=_stanza["lines"],
        clickable=CLICKABLE_FORMS,
        homer_words=HOMER_WORDS if SHOW_HOMER.value else set(),
        ictus_html=RHYTHM_HTML,
        show_ictus=SHOW_ICTUS.value,
    )

    _txt_lines = _stanza["translations"].get(trans_selector.value, "—").split("\n")

    _line_divs = "".join(
        f'<div>{line.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")}</div>'
        for line in _txt_lines
    )
    _right = mo.Html(
        '<div style="font-size:1.0em;display:flex;flex-direction:column;'
        'justify-content:space-between;border-left:3px solid #ccc;padding-left:0.8em">'
        + _line_divs + "</div>"
    )

    mo.vstack([
        mo.hstack([stanza_selector, trans_selector], justify="space-between"),
        mo.hstack([text_widget, _right], justify="start", align="stretch", gap=1.5),
    ])
    return (text_widget,)


@app.cell(hide_code=True)
def _(QUIZ_WORDS_RAW, build_lexicon_tabs, gu, text_widget):
    gu.render_gloss_panel(QUIZ_WORDS_RAW, text_widget.widget.selected_word, build_lexicon_tabs)
    return


@app.cell(hide_code=True)
def _(EEE_NOTE, mo):
    mo.accordion({"О проверке форм (EEE)": EEE_NOTE})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Упражнения
    """)
    return


@app.cell(hide_code=True)
def _():
    # Shared per-lesson default: how many items each exercise below draws per
    # session. Change this one value to affect every exercise at once, or
    # override a single exercise by editing its own n=SESSION_SIZE argument.
    SESSION_SIZE = 10
    return (SESSION_SIZE,)


@app.cell(hide_code=True)
def _(gu):
    quiz_renew_btn = gu.make_renew_button()
    return (quiz_renew_btn,)


@app.cell(hide_code=True)
def _(QUIZ_WORDS, cv, gu, history, remaining, restore_entry):
    _ = cv()
    answer_radio, next_btn, prev_btn = gu.word_quiz_widgets(
        cv=cv(),
        remaining=remaining(),
        vocab=QUIZ_WORDS,
        restore_entry=restore_entry(),
        history_len=len(history()),
    )
    return answer_radio, next_btn, prev_btn


@app.cell(hide_code=True)
def _(
    QUIZ_WORDS,
    answer_radio,
    cv,
    future,
    gu,
    history,
    next_btn,
    prev_btn,
    quiz_renew_btn,
    remaining,
    restore_entry,
    score,
    set_cv,
    set_future,
    set_history,
    set_remaining,
    set_restore_entry,
    set_score,
):
    gu.word_quiz_form(
        cv, set_cv, remaining, set_remaining,
        score, set_score, restore_entry, set_restore_entry,
        history, set_history, future, set_future,
        answer_radio, next_btn, prev_btn,
        vocab=QUIZ_WORDS,
        title='### Упражнение: найди слово',
        meaning_key='_label',
        form_key='form',
        renew_btn=quiz_renew_btn,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Упражнение: сопоставь строфу и перевод
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    sm_direction = mo.ui.radio(
        options={
            "Строфа → перевод": "grc_to_tr",
            "Перевод → строфа": "tr_to_grc",
        },
        value="Строфа → перевод",
        label="**Направление:**",
        inline=True,
    )
    sm_direction
    return (sm_direction,)


@app.cell(hide_code=True)
def _(mo):
    sm_cv, sm_set_cv = mo.state(None)
    sm_score, sm_set_score = mo.state({"correct": 0, "total": 0})
    sm_remaining, sm_set_remaining = mo.state(None)
    sm_history, sm_set_history = mo.state([])
    sm_future, sm_set_future = mo.state([])
    sm_restore_entry, sm_set_restore_entry = mo.state(None)
    return (
        sm_cv,
        sm_future,
        sm_history,
        sm_remaining,
        sm_restore_entry,
        sm_score,
        sm_set_cv,
        sm_set_future,
        sm_set_history,
        sm_set_remaining,
        sm_set_restore_entry,
        sm_set_score,
    )


@app.cell(hide_code=True)
def _(sm_direction, sm_set_cv, sm_set_remaining):
    _ = sm_direction.value
    sm_set_cv(None)
    sm_set_remaining(None)
    return


@app.cell(hide_code=True)
def _(
    SESSION_SIZE,
    STANZAS,
    gu,
    sm_renew_btn,
    sm_set_cv,
    sm_set_future,
    sm_set_history,
    sm_set_remaining,
    sm_set_restore_entry,
    sm_set_score,
):
    SM_STANZAS = gu.sample_session_items(STANZAS, n=SESSION_SIZE)
    gu.reset_quiz_state(sm_renew_btn, sm_set_cv, sm_set_remaining, sm_set_score,
                         sm_set_history, sm_set_future, sm_set_restore_entry)
    return (SM_STANZAS,)


@app.cell(hide_code=True)
def _(gu):
    sm_renew_btn = gu.make_renew_button()
    return (sm_renew_btn,)


@app.cell(hide_code=True)
def _(
    SM_STANZAS,
    gu,
    sm_cv,
    sm_direction,
    sm_history,
    sm_remaining,
    sm_restore_entry,
):
    _ = sm_cv()
    sm_choice_radio, sm_next_btn, sm_prev_btn = gu.stanza_match_widgets(
        cv=sm_cv(),
        remaining=sm_remaining(),
        stanzas=SM_STANZAS,
        direction=sm_direction.value,
        restore_entry=sm_restore_entry(),
        history_len=len(sm_history()),
    )
    return sm_choice_radio, sm_next_btn, sm_prev_btn


@app.cell(hide_code=True)
def _(
    SM_STANZAS,
    gu,
    sm_choice_radio,
    sm_cv,
    sm_direction,
    sm_future,
    sm_history,
    sm_next_btn,
    sm_prev_btn,
    sm_remaining,
    sm_renew_btn,
    sm_restore_entry,
    sm_score,
    sm_set_cv,
    sm_set_future,
    sm_set_history,
    sm_set_remaining,
    sm_set_restore_entry,
    sm_set_score,
):
    gu.stanza_match_form(
        sm_cv, sm_set_cv, sm_remaining, sm_set_remaining,
        sm_score, sm_set_score, sm_restore_entry, sm_set_restore_entry,
        sm_history, sm_set_history, sm_future, sm_set_future,
        sm_choice_radio, sm_next_btn, sm_prev_btn,
        stanzas=SM_STANZAS,
        direction=sm_direction.value,
        renew_btn=sm_renew_btn,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Упражнение: слово в переводе
    """)
    return


@app.cell(hide_code=True)
def _(
    QUIZ_WORDS_RAW,
    SESSION_SIZE,
    STANZAS,
    eee,
    gu,
    tp_renew_btn,
    tp_set_cv,
    tp_set_future,
    tp_set_history,
    tp_set_remaining,
    tp_set_restore_entry,
    tp_set_score,
):
    from pathlib import Path as _P

    LITERARY_TRANSLATORS = ["Жуковский", "Вересаев"]
    _tp_vocab = [w for w in QUIZ_WORDS_RAW if w.get("pos") in eee.TRANSLATION_PRESENCE_CONTENT_POS]
    _tp_path = _P(__file__).parent / "translation_presence.tsv"
    gu.sync_translation_presence_tsv(_tp_vocab, LITERARY_TRANSLATORS, STANZAS, _tp_path)
    TP_ITEMS = gu.balance_presence_items(gu.build_translation_presence_items(
        gu.read_translation_presence_tsv(_tp_path), QUIZ_WORDS_RAW, STANZAS
    ), n=SESSION_SIZE)
    gu.reset_quiz_state(tp_renew_btn, tp_set_cv, tp_set_remaining, tp_set_score,
                         tp_set_history, tp_set_future, tp_set_restore_entry)
    return (TP_ITEMS,)


@app.cell(hide_code=True)
def _(mo):
    tp_cv, tp_set_cv = mo.state(None)
    tp_score, tp_set_score = mo.state({"correct": 0, "total": 0})
    tp_remaining, tp_set_remaining = mo.state(None)
    tp_history, tp_set_history = mo.state([])
    tp_future, tp_set_future = mo.state([])
    tp_restore_entry, tp_set_restore_entry = mo.state(None)
    return (
        tp_cv,
        tp_future,
        tp_history,
        tp_remaining,
        tp_restore_entry,
        tp_score,
        tp_set_cv,
        tp_set_future,
        tp_set_history,
        tp_set_remaining,
        tp_set_restore_entry,
        tp_set_score,
    )


@app.cell(hide_code=True)
def _(gu):
    tp_renew_btn = gu.make_renew_button()
    return (tp_renew_btn,)


@app.cell(hide_code=True)
def _(TP_ITEMS, gu, tp_cv, tp_history, tp_remaining, tp_restore_entry):
    _ = tp_cv()
    tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch = gu.translation_presence_widgets(
        cv=tp_cv(),
        remaining=tp_remaining(),
        items=TP_ITEMS,
        restore_entry=tp_restore_entry(),
        history_len=len(tp_history()),
    )
    return tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch


@app.cell(hide_code=True)
def _(
    TP_ITEMS,
    gu,
    tp_choice_radio,
    tp_cv,
    tp_future,
    tp_history,
    tp_next_btn,
    tp_prev_btn,
    tp_remaining,
    tp_renew_btn,
    tp_restore_entry,
    tp_score,
    tp_set_cv,
    tp_set_future,
    tp_set_history,
    tp_set_remaining,
    tp_set_restore_entry,
    tp_set_score,
    tp_source_switch,
):
    gu.translation_presence_form(
        tp_cv, tp_set_cv, tp_remaining, tp_set_remaining,
        tp_score, tp_set_score, tp_restore_entry, tp_set_restore_entry,
        tp_history, tp_set_history, tp_future, tp_set_future,
        tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch,
        items=TP_ITEMS,
        renew_btn=tp_renew_btn,
    )
    return


@app.cell(hide_code=True)
def _(QUIZ_WORDS_RAW, build_paradigm_table, eee, grc_lexicons):
    CLICKABLE_FORMS = eee.grc_coverage_words(
        QUIZ_WORDS_RAW, "none",
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    )
    # words whose exact attested surface form is confirmed by the Homeric
    # corpus lexicon specifically -- highlighted (background) in the clickable
    # text so a reader can tell "Homer himself confirms this form" apart from
    # "some later-period lexicon in the combined engine reaches it".
    HOMER_WORDS = eee.grc_coverage_words(
        QUIZ_WORDS_RAW, "homer",
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    )
    return CLICKABLE_FORMS, HOMER_WORDS


@app.cell(hide_code=True)
def _(mo):
    cv, set_cv = mo.state(None)
    score, set_score = mo.state({"correct": 0, "total": 0})
    remaining, set_remaining = mo.state(None)
    history, set_history = mo.state([])
    future, set_future = mo.state([])
    restore_entry, set_restore_entry = mo.state(None)
    return (
        cv,
        future,
        history,
        remaining,
        restore_entry,
        score,
        set_cv,
        set_future,
        set_history,
        set_remaining,
        set_restore_entry,
        set_score,
    )


@app.cell(hide_code=True)
def _(STANZAS, mo):
    stanza_selector = mo.ui.dropdown(
        options=[st["ref"] for st in STANZAS],
        value=STANZAS[0]["ref"],
        label="Строфа",
    )
    return (stanza_selector,)


@app.cell(hide_code=True)
def _(mo):
    trans_selector = mo.ui.dropdown(
        options={
            "подстрочник":             "подстрочник",
            "Жуковский (1849) · рус.": "Жуковский",
            "Вересаев (1953) · рус.":  "Вересаев",
        },
        value="подстрочник",
        label="Перевод",
    )
    return (trans_selector,)


@app.cell(hide_code=True)
def _(eee):
    from pathlib import Path as _P

    _root = _P(__file__).parent
    _greek = eee.parse_stanza_text((_root / "greek.md").read_text(encoding="utf-8"), ref_prefix="### Odyss. ")
    _trans_ru, _desc_ru = eee.parse_stanza_translations((_root / "translations_ru.md").read_text(encoding="utf-8"), ref_prefix="### Odyss. ")
    TRANS_DESC = _desc_ru
    STANZAS = [
        {
            "ref": ref,
            "lines": lines,
            "translations": {tr: d.get(ref, "—") for tr, d in _trans_ru.items()},
        }
        for ref, lines in _greek.items()
    ]

    # ictus (rhythm) markup: one marked-up line per plain line, in the same
    # reading order as greek.md -- zipped by position, not re-keyed, so a plain
    # line's own accents/punctuation never need to match the markup exactly.
    _ictus_lines = (_root / "ictus.html").read_text(encoding="utf-8").splitlines()
    _all_plain_lines = [line for lines in _greek.values() for line in lines]
    RHYTHM_HTML = dict(zip(_all_plain_lines, _ictus_lines))
    return RHYTHM_HTML, STANZAS, TRANS_DESC


@app.cell(hide_code=True)
def _(
    ag_backend,
    eee,
    grc_lexicons,
    gu,
):
    from pathlib import Path

    QUIZ_WORDS_RAW = gu.resolve_word_grammar(
        gu.load_inflected_vocab_tsv("vocab_I_1-21.tsv", nb_dir=Path(__file__).parent),
        ag_backend, "ru"
    )

    def _lexicon_tag(w):
        sources = eee.grc_lexicon_sources(w, lexicons=grc_lexicons)
        if not sources:
            return ""
        lexicons = ", ".join(f'"{s}"' for s in sources)
        return f"ancient-greek[{lexicons}]"

    for _w in QUIZ_WORDS_RAW:
        _tag = _lexicon_tag(_w)
        if _tag:
            _w["lexicon_tag"] = _tag
    return (QUIZ_WORDS_RAW,)


@app.cell(hide_code=True)
def _(
    QUIZ_WORDS_RAW,
    SESSION_SIZE,
    build_paradigm_table,
    eee,
    grc_lexicons,
    gu,
    quiz_renew_btn,
    set_cv,
    set_future,
    set_history,
    set_remaining,
    set_restore_entry,
    set_score,
):
    QUIZ_WORDS = gu.sample_session_items(eee.filter_grc_quiz_words(
        QUIZ_WORDS_RAW, "none",
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    ), n=SESSION_SIZE)

    eee.add_labels(QUIZ_WORDS)

    gu.reset_quiz_state(quiz_renew_btn, set_cv, set_remaining, set_score,
                         set_history, set_future, set_restore_entry)
    return (QUIZ_WORDS,)


@app.cell(hide_code=True)
def _(ag_backend, eee, grc_lexicons, mg, um_backend):
    build_paradigm_table = eee.build_grc_paradigm_table(ag_backend, um_backend)
    build_lexicon_tabs = eee.build_grc_lexicon_tabs(
        ag_backend, um_backend,
        lexicons=grc_lexicons,
        el_backend=mg,
        require_lexicon="homer",
    )
    return build_lexicon_tabs, build_paradigm_table


@app.cell(hide_code=True)
def _():
    import sys as _sys
    import pathlib as _pl
    for _pth in _pl.Path(_sys.prefix).glob("lib/python*/site-packages/_editable_impl_*.pth"):
        _src = _pth.read_text().strip()
        if _src not in _sys.path:
            _sys.path.insert(0, _src)

    import marimo as mo
    import eee_project as eee
    from ancient_greek_backend_eee import AncientGreekBackend
    from unimorph_backend_eee import UniMorphBackend
    from modern_greek_backend_eee import ModernGreekBackend

    # union recognizer for coverage + quiz — all diachronic rungs, incl. Classical Attic (pratt + ltrg + lsj)
    ag_backend = AncientGreekBackend.for_period("epic", "attic", "hellenistic_koine", "roman_koine", extra_lexicons=["odyssey_morpheus"])
    # odyssey_morpheus is Epic-register, Odyssey-course-vocabulary-specific --
    # merged alongside homer (same register), not lsj/byzantine (Attic/Koine).
    ag_homer = AncientGreekBackend.for_period("epic", extra_lexicons=["odyssey_morpheus"])
    ag_lsj = AncientGreekBackend.for_period("attic")
    ag_lxx = AncientGreekBackend.for_period("hellenistic_koine")
    ag_morphgnt = AncientGreekBackend.for_period("roman_koine")
    # byzantine is a sparse exceptions layer, not a standalone engine -- merge
    # onto the same Koine/Attic base the other rungs use so it inherits their
    # lemma coverage and only overrides the specific cells it documents.
    ag_byzantine = AncientGreekBackend.for_period("byzantine")
    grc_lexicons = {"homer": ag_homer, "lsj": ag_lsj, "lxx": ag_lxx, "morphgnt": ag_morphgnt, "byzantine": ag_byzantine}
    um_backend = UniMorphBackend(language="grc")
    mg = ModernGreekBackend()   # Modern-Greek rung of the diachronic dropdown
    eee.register_backend("grc", ag_backend, backend="ancient-greek")
    eee.register_backend("grc", ag_homer, backend="ag-homer")
    eee.register_backend("grc", um_backend, backend="unimorph")
    eee.set_chain("grc", ["ancient-greek", "unimorph"])
    gu = eee.GreekUtils(mo_module=mo)
    return (
        ag_backend,
        ag_byzantine,
        ag_homer,
        ag_lsj,
        ag_lxx,
        ag_morphgnt,
        eee,
        grc_lexicons,
        gu,
        mg,
        mo,
        um_backend,
    )


@app.cell(hide_code=True)
def _(mo):
    from eee_project.notebook_utils import eee_footer
    eee_footer(mo, lang="ru")
    return


@app.cell(hide_code=True)
def _(cfg, gu):
    from pathlib import Path as _P
    NB_DIR = _P(__file__).parent
    NB_REMOTE = f"{cfg.raw_base}/2026_06_01"
    for _pdf in (
        'Одиссея. Зачин.pdf',
        'Одиссея_1-21_словарь.pdf',
        'Греческий алфавит.pdf',
    ):
        gu.ensure_file(_pdf, nb_dir=NB_DIR, remote_base=NB_REMOTE)

    # Set True to underline words known to eee in the poem text (coverage view)
    return


if __name__ == "__main__":
    app.run()
