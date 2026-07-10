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
def _(mo):
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_32dyZq8gA6x14GL2Zwa6ZU)"
    _left = mo.vstack([
        mo.md("# Одиссея для отважных"),
        mo.md(_badge),
        mo.md("## Пилотное занятие · Odyss. I.1–21"),
    ])
    _img_url = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/odyssey/2026_06_01/Odysseus_Sirens_BM_E440_n2.jpg"
    _img = mo.Html(
        f'<a href="{_img_url}" target="_blank" rel="noopener">'
        f'<img src="{_img_url}" style="max-width:340px;width:100%;border-radius:4px;object-fit:cover;cursor:pointer"/>'
        f'</a>'
    )
    mo.hstack([_left, _img], align="start")
    return


@app.cell(hide_code=True)
def _(mo):
    _base = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/odyssey/2026_06_01"
    mo.md(
        f"**Материалы занятия:** "
        f"[Одиссея. Зачин.pdf]({_base}/Одиссея.%20Зачин.pdf) · "
        f"[Одиссея\_1-21\_словарь.pdf]({_base}/Одиссея_1-21_словарь.pdf) · "
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
def _(mo):
    SHOW_ICTUS = mo.ui.switch(value=True)
    mo.hstack(
        [SHOW_ICTUS, mo.md(
            "Икты (ударные слоги) каждой стопы выделены <b style='color:#980000'>красным</b>."
        )],
        justify="start", align="center", gap=1.5,
    )
    return (SHOW_ICTUS,)


@app.cell(hide_code=True)
def _(
    CLICKABLE_FORMS,
    SHOW_ICTUS,
    STANZAS,
    eee,
    mo,
    stanza_selector,
    trans_selector,
):
    _st_map = {s["ref"]: s for s in STANZAS}
    _stanza = _st_map[stanza_selector.value]

    _RHYTHM_HTML = {
        'Ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ':
            "<b style='color:#980000'>Ἄ</b>νδρα μοι <b style='color:#980000'>ἔ</b>ννεπε, μ<b style='color:#980000'>οῦ</b>σα, πολ<b style='color:#980000'>ύ</b>τροπον, <b style='color:#980000'>ὃ</b>ς μάλα π<b style='color:#980000'>ο</b>λλὰ",
        'πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν·':
            "πλ<b style='color:#980000'>ά</b>γχθη, ἐπ<b style='color:#980000'>εὶ</b> Τροί<b style='color:#980000'>η</b>ς ἱερ<b style='color:#980000'>ὸ</b>ν πτολί<b style='color:#980000'>ε</b>θρον ἔπ<b style='color:#980000'>ε</b>ρσεν·",
        "πολλῶν δ' ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,":
            "π<b style='color:#980000'>ο</b>λλῶν δ' <b style='color:#980000'>ἀ</b>νθρώπων ἴδεν <b style='color:#980000'>ἄ</b>στεα κ<b style='color:#980000'>αὶ</b> νόον <b style='color:#980000'>ἔ</b>γνω,",
        "πολλὰ δ' ὅ γ' ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,":
            "π<b style='color:#980000'>ο</b>λλὰ δ' ὅ γ' <b style='color:#980000'>ἐ</b>ν πόντ<b style='color:#980000'>ῳ</b> πάθεν <b style='color:#980000'>ἄ</b>λγεα <b style='color:#980000'>ὃ</b>ν κατὰ θ<b style='color:#980000'>υ</b>μόν,",
        'ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.':
            "<b style='color:#980000'>ἀ</b>ρνύμεν<b style='color:#980000'>ο</b>ς ἥν τ<b style='color:#980000'>ε</b> ψυχ<b style='color:#980000'>ὴ</b>ν καὶ ν<b style='color:#980000'>ό</b>στον ἑτ<b style='color:#980000'>αί</b>ρων.",
        "ἀλλ' οὐδ' ὣς ἑτάρους ἐρρύσατο, ἱέμενός περ·":
            "<b style='color:#980000'>ἀ</b>λλ' οὐδ' <b style='color:#980000'>ὣ</b>ς ἑτάρ<b style='color:#980000'>ου</b>ς ἐρρ<b style='color:#980000'>ύ</b>σατο, <b style='color:#980000'>ἱ</b>έμεν<b style='color:#980000'>ό</b>ς περ·",
        'αὐτῶν γὰρ σφετέρῃσιν ἀτασθαλίῃσιν ὄλοντο,':
            "<b style='color:#980000'>αὐ</b>τῶν γ<b style='color:#980000'>ὰ</b>ρ σφετέρ<b style='color:#980000'>ῃ</b>σιν ἀτ<b style='color:#980000'>α</b>σθαλίῃσιν ὄλ<b style='color:#980000'>ο</b>ντο,",
        'νήπιοι, οἳ κατὰ βοῦς Ὑπερίονος Ἠελίοιο':
            "ν<b style='color:#980000'>ή</b>πιοι, <b style='color:#980000'>οἳ</b> κατὰ β<b style='color:#980000'>οῦ</b>ς Ὑπερ<b style='color:#980000'>ί</b>ονος <b style='color:#980000'>Ἠ</b>ελί<b style='color:#980000'>οι</b>ο",
        'ἤσθιον· αὐτὰρ ὁ τοῖσιν ἀφείλετο νόστιμον ἦμαρ.':
            "<b style='color:#980000'>ἤ</b>σθιον· <b style='color:#980000'>αὐ</b>τὰρ ὁ τ<b style='color:#980000'>οῖ</b>σιν ἀφ<b style='color:#980000'>εί</b>λετο ν<b style='color:#980000'>ό</b>στιμον <b style='color:#980000'>ἦ</b>μαρ.",
        'τῶν ἁμόθεν γε, θεά, θύγατερ Διός, εἰπὲ καὶ ἡμῖν.':
            "τ<b style='color:#980000'>ῶ</b>ν ἁμόθ<b style='color:#980000'>ε</b>ν γε, θε<b style='color:#980000'>ά</b>, θύγατ<b style='color:#980000'>ε</b>ρ Διός, <b style='color:#980000'>εἰ</b>πὲ καὶ <b style='color:#980000'>ἡ</b>μῖν.",
        "Ἔνθ' ἄλλοι μὲν πάντες, ὅσοι φύγον αἰπὺν ὄλεθρον,":
            "<b style='color:#980000'>Ἔ</b>νθ' ἄλλ<b style='color:#980000'>οι</b> μὲν π<b style='color:#980000'>ά</b>ντες, ὅσ<b style='color:#980000'>οι</b> φύγον <b style='color:#980000'>αἰ</b>πὺν ὄλ<b style='color:#980000'>ε</b>θρον,",
        'οἴκοι ἔσαν, πόλεμόν τε πεφευγότες ἠδὲ θάλασσαν·':
            "<b style='color:#980000'>οἴ</b>κοι ἔσ<b style='color:#980000'>α</b>ν, πόλεμ<b style='color:#980000'>ό</b>ν τε πεφ<b style='color:#980000'>ευ</b>γότες <b style='color:#980000'>ἠ</b>δὲ θάλ<b style='color:#980000'>α</b>σσαν·",
        "τὸν δ' οἶον νόστου κεχρημένον ἠδὲ γυναικὸς":
            "τ<b style='color:#980000'>ὸ</b>ν δ' οἶ<b style='color:#980000'>ο</b>ν νόστ<b style='color:#980000'>ου</b> κεχρ<b style='color:#980000'>η</b>μένον <b style='color:#980000'>ἠ</b>δὲ γυν<b style='color:#980000'>αι</b>κὸς",
        "νύμφη πότνι' ἔρυκε Καλυψὼ δῖα θεάων":
            "ν<b style='color:#980000'>ύ</b>μφη π<b style='color:#980000'>ό</b>τνι' ἔρ<b style='color:#980000'>υ</b>κε Καλ<b style='color:#980000'>υ</b>ψὼ δ<b style='color:#980000'>ῖ</b>α θε<b style='color:#980000'>ά</b>ων",
        'ἐν σπέσσι γλαφυροῖσι, λιλαιομένη πόσιν εἶναι.':
            "<b style='color:#980000'>ἐ</b>ν σπέσσ<b style='color:#980000'>ι</b> γλαφυρ<b style='color:#980000'>οῖ</b>σι, λιλ<b style='color:#980000'>αι</b>ομέν<b style='color:#980000'>η</b> πόσιν <b style='color:#980000'>εἶ</b>ναι.",
        "ἀλλ' ὅτε δὴ ἔτος ἦλθε περιπλομένων ἐνιαυτῶν,":
            "<b style='color:#980000'>ἀ</b>λλ' ὅτε δ<b style='color:#980000'>ὴ</b> ἔτος <b style='color:#980000'>ἦ</b>λθε περ<b style='color:#980000'>ι</b>πλομέν<b style='color:#980000'>ω</b>ν ἐνι<b style='color:#980000'>αυ</b>τῶν,",
        'τῷ οἱ ἐπεκλώσαντο θεοὶ οἰκόνδε νέεσθαι':
            "τ<b style='color:#980000'>ῷ</b> οἱ ἐπ<b style='color:#980000'>ε</b>κλώσ<b style='color:#980000'>α</b>ντο θε<b style='color:#980000'>οὶ</b> οἶκ<b style='color:#980000'>ό</b>νδε νέ<b style='color:#980000'>ε</b>σθαι",
        "εἰς Ἰθάκην, οὐδ' ἔνθα πεφυγμένος ἦεν ἀέθλων":
            "<b style='color:#980000'>εἰ</b>ς Ἰθάκ<b style='color:#980000'>η</b>ν, οὐδ' <b style='color:#980000'>ἔ</b>νθα πεφ<b style='color:#980000'>υ</b>γμένος <b style='color:#980000'>ἦ</b>εν ἀ<b style='color:#980000'>έ</b>θλων",
        "καὶ μετὰ οἷσι φίλοισι. θεοὶ δ' ἐλέαιρον ἅπαντες":
            "κ<b style='color:#980000'>αὶ</b> μετὰ <b style='color:#980000'>οἷ</b>σι φίλ<b style='color:#980000'>οι</b>σι. θε<b style='color:#980000'>οὶ</b> δ' ἐλέ<b style='color:#980000'>αι</b>ρον ἅπ<b style='color:#980000'>α</b>ντες",
        "νόσφι Ποσειδάωνος· ὁ δ' ἀσπερχὲς μενέαινεν":
            "ν<b style='color:#980000'>ό</b>σφι Ποσ<b style='color:#980000'>ει</b>δά<b style='color:#980000'>ω</b>νος· ὁ δ' <b style='color:#980000'>ἀ</b>σπερχ<b style='color:#980000'>ὲ</b>ς μενέ<b style='color:#980000'>αι</b>νεν",
        'ἀντιθέῳ Ὀδυσῆι πάρος ἥν γαῖαν ἱκέσθαι.':
            "<b style='color:#980000'>ἀ</b>ντιθέ<b style='color:#980000'>ῳ</b> Ὀδυσ<b style='color:#980000'>ῆ</b>ι πάρ<b style='color:#980000'>ο</b>ς ἣν γ<b style='color:#980000'>αῖ</b>αν ἱκ<b style='color:#980000'>έ</b>σθαι.",
    }

    text_widget = eee.interactive_text(
        mo,
        lines=_stanza["lines"],
        clickable=CLICKABLE_FORMS,
        ictus_html=_RHYTHM_HTML,
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
def _(QUIZ_WORDS_RAW, build_lexicon_tabs, eee, mo, text_widget):
    _sel = text_widget.widget.selected_word
    _w = eee.resolve_clicked_word(QUIZ_WORDS_RAW, _sel)

    if _w is None:
        _panel = mo.md("*Выберите слово в тексте, чтобы увидеть перевод и формы слов из гомеровскго лексикона…*")
    else:
        _w2 = dict(_w)
        eee.add_labels([_w2])
        _gloss = f"**{_w2.get('form', _sel)}** — {_w2['_label']}"
        _grammar = _w2.get("grammar_label", "")
        if _grammar:
            _gloss += f"  \n_{_grammar}_"
        _tables = build_lexicon_tabs(_w2) or ""
        if _tables:
            _caption = mo.md(
                "*Формы слова по эпохам — только морфологическое соответствие, "
                "смысл может меняться*"
            )
            _panel = mo.vstack([mo.md(_gloss), _caption, mo.Html(_tables)])
        else:
            _panel = mo.md(_gloss)

    _panel
    return


@app.cell(hide_code=True)
def _(mo):
    _EEE_NOTE = """
    Используется [EEE](https://codeberg.org/EEE-project) — систему для построения интерактивных учебных материалов.
    В данном случае задействованы [модули морфологического анализа](https://codeberg.org/EEE-project/eee-project/src/branch/main/docs/backends.md):

    * [**unimorph-backend-eee**](https://codeberg.org/EEE-project/unimorph-backend-eee) — база данных UniMorph:
      для древнегреческого парадигмы существительных и прилагательных (глаголы отсутствуют);
      покрытие лучше для греческого НЗ, чем для гомеровского текста
    * [**ancient-greek-backend-eee**](https://codeberg.org/EEE-project/ancient-greek-backend-eee) — анализ на основе морфологических словарей; лексиконы по эпохам:
      * **Homer** — гомеровский эпос (Илиада, Одиссея); эпический/ионийский, ~VIII в. до н.э.
      * **Словарь классического аттического** — (pratt + ltrg + lsj); аттика V–IV вв. до н.э.
      * **LXX** — Септуагинта; эллинистический койне, IV–I вв. до н.э.
      * **MorphGNT** — греческий Новый Завет; римский койне, I–III вв. н.э.
    * [**modern-greek-backend-eee**](https://codeberg.org/EEE-project/modern-greek-backend-eee) — новогреческий (демотика); показывает, как древнее слово склоняется/спрягается сегодня — последняя «ступень» в таблице словоформ (если у слова есть живой новогреческий рефлекс)

    В таблице словоформ можно переключаться между лексиконами разных исторических периодов,
    если соответствующие данные для данного слова в системе есть.
    """
    mo.accordion({"О проверке форм (EEE)": _EEE_NOTE})
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
    pass
    return


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
    STANZAS,
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
        stanzas=STANZAS,
        direction=sm_direction.value,
        restore_entry=sm_restore_entry(),
        done=sm_cv() is None and sm_remaining() is not None and len(sm_remaining()) == 0,
        history_len=len(sm_history()),
    )
    return sm_choice_radio, sm_next_btn, sm_prev_btn


@app.cell(hide_code=True)
def _(
    STANZAS,
    gu,
    sm_choice_radio,
    sm_cv,
    sm_direction,
    sm_future,
    sm_history,
    sm_next_btn,
    sm_prev_btn,
    sm_remaining,
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
        stanzas=STANZAS,
        direction=sm_direction.value,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Упражнение: слово в переводе
    """)
    return


@app.cell(hide_code=True)
def _(QUIZ_WORDS_RAW, STANZAS, gu):
    from pathlib import Path as _P

    LITERARY_TRANSLATORS = ["Жуковский", "Вересаев"]
    _TP_CONTENT_POS = {"noun", "verb", "adj", "adv", "name"}
    _tp_vocab = [w for w in QUIZ_WORDS_RAW if w.get("pos") in _TP_CONTENT_POS]
    _tp_path = _P(__file__).parent / "translation_presence.tsv"
    gu.sync_translation_presence_tsv(_tp_vocab, LITERARY_TRANSLATORS, STANZAS, _tp_path)
    TP_ITEMS = gu.build_translation_presence_items(
        gu.read_translation_presence_tsv(_tp_path), QUIZ_WORDS_RAW, STANZAS
    )
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
    )
    return


@app.cell(hide_code=True)
def _(QUIZ_WORDS_RAW, build_paradigm_table, eee, grc_lexicons):
    CLICKABLE_FORMS = eee.grc_coverage_words(
        QUIZ_WORDS_RAW, "none",
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    )
    return (CLICKABLE_FORMS,)


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
    return STANZAS, TRANS_DESC


@app.cell(hide_code=True)
def _(ag_backend, ag_homer, ag_lsj, ag_lxx, ag_morphgnt, gu):
    import csv
    from pathlib import Path

    _vocab_path = Path(__file__).parent / "vocab_I_1-21.tsv"
    with open(_vocab_path, encoding="utf-8") as _f:
        QUIZ_WORDS_RAW = gu.resolve_word_grammar(
            list(csv.DictReader(_f, delimiter="\t")), ag_backend, "ru"
        )

    _POS_MAP = {"adj": "adjective"}
    _QUIZZABLE = {"noun", "verb", "adj"}
    _LEXICONS = [("homer", ag_homer), ("lsj", ag_lsj), ("lxx", ag_lxx), ("morphgnt", ag_morphgnt)]

    def _lexicon_tag(w):
        if w.get("pos") not in _QUIZZABLE:
            return ""
        pos = _POS_MAP.get(w["pos"], w["pos"])
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
            for name, backend in _LEXICONS:
                try:
                    if any(backend.paradigm(w["lemma"], pos).values()):
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
    build_paradigm_table,
    eee,
    grc_lexicons,
    set_cv,
    set_remaining,
):
    QUIZ_WORDS = eee.filter_grc_quiz_words(
        QUIZ_WORDS_RAW, "none",
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    )

    eee.add_labels(QUIZ_WORDS)

    set_cv(None)
    set_remaining(None)
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
    ag_backend = AncientGreekBackend(lexicons=["homer", "lxx", "morphgnt", "pratt", "ltrg", "lsj"])
    ag_homer = AncientGreekBackend(lexicons=["homer"])
    ag_lsj = AncientGreekBackend(lexicons=["pratt", "ltrg", "lsj"])
    ag_lxx = AncientGreekBackend(lexicons=["lxx"])
    ag_morphgnt = AncientGreekBackend(lexicons=["morphgnt"])
    grc_lexicons = {"homer": ag_homer, "lsj": ag_lsj, "lxx": ag_lxx, "morphgnt": ag_morphgnt}
    um_backend = UniMorphBackend(language="grc")
    mg = ModernGreekBackend()   # Modern-Greek rung of the diachronic dropdown
    eee.register_backend("grc", ag_backend, backend="ancient-greek")
    eee.register_backend("grc", ag_homer, backend="ag-homer")
    eee.register_backend("grc", um_backend, backend="unimorph")
    eee.set_chain("grc", ["ancient-greek", "unimorph"])
    gu = eee.GreekUtils(mo_module=mo)
    return (
        ag_backend,
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
