# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.13",
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

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    cfg = ConfigStore.from_url(f"{_ROOT}/odyssey/lessons.tsv", ga=f"{_ROOT}/ga.json")
    eee_topbar(mo, back_url=cfg.index_url(), lang="ru", titles={
        "ru": "Одиссея для отважных",
    }, ga_config=cfg.ga_config())
    return (cfg,)


@app.cell(hide_code=True)
def _(eee, mo):
    from pathlib import Path as _Path
    _thumb_path = _Path(__file__).parent / "odysseus_bust.jpg"
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_d77Y36J87ufwqrDNgVzvZQ)"
    _left = mo.vstack([
        mo.md("# Одиссея для отважных"),
        mo.md(_badge),
        mo.md("## День 3 · Odyss. IX.62–81"),
    ])
    _right = eee.magnify_image(mo, _thumb_path, raw_base="https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/odyssey/2026_06_29", width=280)
    mo.hstack([_left, _right], align="start")
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    _txt = f"**Материалы занятия:** [Od_IX_62-81.pdf]({NB_REMOTE}/Od_IX_62-81.pdf) · [Od_IX_62-81_vocabula.docx]({NB_REMOTE}/Od_IX_62-81_vocabula.docx)"
    mo.md(_txt)
    return


@app.cell(hide_code=True)
def _(eee, mo):
    from pathlib import Path as _Pp
    _prep = _Pp(__file__).parent / "prepositions.jpg"
    _pimg = eee.magnify_image(mo, _prep, raw_base="https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/odyssey/2026_06_29", width=440)
    mo.vstack([
        mo.md(r"""
    ---
    ## Грамматическая памятка для начинающих моряков

    - Обычно показатель прошедшего времени — приставка **ἐ-** перед корнем глагола
      (*аугмент*). Но **у Гомера** аугмента вполне может и не быть: тогда прошедшее
      опознаётся по окончаниям и иногда по изменившейся основе.
      *πλέομεν* — и «мы поплыли», и «мы плывём»: формы настоящего и имперфекта совпали.
    - В древнегреческом есть **артикль** — всегда определённый; ставится перед словом
      и повторяет его падеж. В большинстве падежей начинается на **τ-**: *τῶν δειλῶν*.
    - У древнегреческого глагола три **залога**: *активный* (я делаю), *медиальный*
      (я делаю сам, для себя, в своих интересах) и *пассивный* (со мной делают).

    Предлоги движения — **куда**, **откуда**, **где** — вокруг «сосуда» ἐν:
    """),
        _pimg,
    ])
    return


@app.cell(hide_code=True)
def _(eee, mo):
    from pathlib import Path as _Pm
    _d = _Pm(__file__).parent
    _c, _m = _d / "malea_cliff.jpg", _d / "malea_map.jpg"
    _imgs = mo.hstack([
        eee.magnify_image(mo, _c, raw_base="https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/odyssey/2026_06_29", width=300),
        eee.magnify_image(mo, _m, raw_base="https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/odyssey/2026_06_29", width=300),
    ], justify="start", align="center")
    mo.vstack([
        mo.md(r"""
    ---
    ### Μάλεια — мыс Малея

    Юго-восточная оконечность Пелопоннеса. Обогнув её, Одиссей был бы уже почти дома —
    но волна, течение и Борей отбросили его от Киферы (*Κύθηρα*) в открытое море, к лотофагам.
    Плавание вокруг Малеи славилось опасностью: встречные ветры и течения у мыса
    нередко сносили корабли в открытое море — как и Одиссея. Отсюда морская
    поговорка, которую приводит **Страбон** (*География* 8.6.20):

    > **Μαλέας δὲ κάμψας ἐπιλάθου τῶν οἴκαδε** — «обогнув Малею, забудь о доме».

    (*κάμψας* «обогнув» — аор. причастие от *κάμπτω*; *ἐπιλάθου* «забудь» — аор.
    императив от *ἐπιλανθάνομαι*.) По смыслу — как наше «пуститься в рискованное
    плавание»: за Малеей о возвращении можно уже и не думать.
    """),
        _imgs,
    ])
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
    _MURRAY = (
        "<b>Homer.</b> <a href='https://www.perseus.tufts.edu/hopper/text?"
        "doc=Perseus%3atext%3a1999.01.0136%3abook%3d9'><i>The Odyssey</i></a>"
        " with an English Translation by A.T. Murray, PH.D. in two volumes."
        " Cambridge, MA., Harvard University Press; London, William Heinemann, Ltd. 1919."
    )
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
        f'<div>{l.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")}</div>'
        for l in _txt_lines
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
        vocab=QUIZ_WORDS,
        restore_entry=restore_entry(),
        done=cv() is None and remaining() is not None and len(remaining()) == 0,
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
        stanzas=SM_STANZAS,
        direction=sm_direction.value,
        restore_entry=sm_restore_entry(),
        done=sm_cv() is None and sm_remaining() is not None and len(sm_remaining()) == 0,
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
        items=TP_ITEMS,
        restore_entry=tp_restore_entry(),
        done=tp_cv() is None and tp_remaining() is not None and len(tp_remaining()) == 0,
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
def _():
    pass
    return


@app.cell(hide_code=True)
def _(STANZAS, mo):
    stanza_selector = mo.ui.dropdown(
        options=[s["ref"] for s in STANZAS],
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
def _():
    pass
    return


@app.cell(hide_code=True)
def _():
    pass
    return


@app.cell(hide_code=True)
def _():
    from pathlib import Path as _P

    def _parse_greek(md):
        out, ref, buf = {}, None, []
        for L in md.splitlines():
            if L.startswith("### Odyss. "):
                if ref: out[ref] = buf
                ref, buf = L[11:].strip(), []
            elif ref and L.strip() and not L.startswith("<!--"):
                buf.append(L.strip())
        if ref: out[ref] = buf
        return out

    def _parse_trans(md):
        out, desc, tr, ref, buf = {}, {}, None, None, []
        for L in md.splitlines():
            if L.startswith("## "):
                if tr and ref and buf: out.setdefault(tr, {})[ref] = "\n".join(buf)
                tr, ref, buf = L[3:].strip(), None, []
            elif tr and ref is None and L.startswith("<!-- **") and L.endswith("-->"):
                desc[tr] = L[4:-3].strip()
            elif L.startswith("### Odyss. "):
                if tr and ref and buf: out.setdefault(tr, {})[ref] = "\n".join(buf)
                ref, buf = L[11:].strip(), []
            elif ref and L.strip() and L.strip() != "---":
                buf.append(L)
        if tr and ref and buf: out.setdefault(tr, {})[ref] = "\n".join(buf)
        return out, desc

    _root = _P(__file__).parent
    _greek = _parse_greek((_root / "greek.md").read_text(encoding="utf-8"))
    _trans_ru, _desc_ru = _parse_trans((_root / "translations_ru.md").read_text(encoding="utf-8"))
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
    ag_byzantine,
    ag_homer,
    ag_lsj,
    ag_lxx,
    ag_morphgnt,
    eee,
    gu,
):
    import csv
    from pathlib import Path

    _vocab_path = Path(__file__).parent / "vocab_IX_62-81.tsv"
    with open(_vocab_path, encoding="utf-8") as _f:
        QUIZ_WORDS_RAW = gu.resolve_word_grammar(
            list(csv.DictReader(_f, delimiter="\t")), ag_backend, "ru"
        )

    _LEXICONS = [("homer", ag_homer), ("lsj", ag_lsj), ("lxx", ag_lxx), ("morphgnt", ag_morphgnt), ("byzantine", ag_byzantine)]

    def _lexicon_tag(w):
        if w.get("pos") not in eee.LEXICON_TAG_POS:
            return ""
        pos = eee.LEXICON_TAG_POS_ALIASES.get(w["pos"], w["pos"])
        form = w.get("form", "")
        sources = []
        for name, backend in _LEXICONS:
            try:
                para = backend.paradigm(w["lemma"], pos)
                if any(form in forms for forms in para.values()):
                    sources.append(name)
            except Exception:
                pass
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
    import sys as _sys, pathlib as _pl
    for _pth in _pl.Path(_sys.prefix).glob("lib/python*/site-packages/_editable_impl_*.pth"):
        _src = _pth.read_text().strip()
        if _src not in _sys.path:
            _sys.path.insert(0, _src)

    import marimo as mo
    import random
    import eee_project as eee
    from ancient_greek_backend_eee import AncientGreekBackend
    from unimorph_backend_eee import UniMorphBackend
    from modern_greek_backend_eee import ModernGreekBackend

    # union recognizer for coverage + quiz — all diachronic rungs, incl. Classical Attic (pratt + ltrg + lsj)
    ag_backend = AncientGreekBackend(lexicons=["homer", "odyssey_morpheus", "lxx", "morphgnt", "pratt", "ltrg", "lsj"])
    # odyssey_morpheus is Epic-register, Odyssey-course-vocabulary-specific --
    # merged alongside homer (same register), not lsj/byzantine (Attic/Koine).
    ag_homer = AncientGreekBackend(lexicons=["homer", "odyssey_morpheus"])
    ag_lsj = AncientGreekBackend(lexicons=["pratt", "ltrg", "lsj"])
    ag_lxx = AncientGreekBackend(lexicons=["lxx"])
    ag_morphgnt = AncientGreekBackend(lexicons=["morphgnt"])
    # byzantine is a sparse exceptions layer, not a standalone engine -- merge
    # onto the same Koine/Attic base the other rungs use so it inherits their
    # lemma coverage and only overrides the specific cells it documents.
    ag_byzantine = AncientGreekBackend(lexicons=["lxx", "morphgnt", "pratt", "ltrg", "lsj", "byzantine"])
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
def _(cfg, gu):
    from pathlib import Path as _P
    NB_DIR = _P(__file__).parent
    NB_REMOTE = f"{cfg.raw_base}/2026_06_29"
    for _f in (
        'map_ortelius.jpg',
        'map_ortelius_full.jpg',
        'odysseus_bust.jpg',
        'prepositions.jpg',
        'malea_cliff.jpg',
        'malea_map.jpg',
        'Od_IX_62-81.pdf',
        'Od_IX_62-81_vocabula.docx',
    ):
        gu.ensure_file(_f, nb_dir=NB_DIR, remote_base=NB_REMOTE)

    # Set True to underline words known to eee in the poem text (coverage view)
    return (NB_REMOTE,)


@app.cell(hide_code=True)
def _(mo):
    from eee_project.notebook_utils import eee_footer
    eee_footer(mo, lang="ru")
    return


if __name__ == "__main__":
    app.run()
