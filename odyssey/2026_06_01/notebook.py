# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.8",
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "ancient-greek-backend-eee @ git+https://codeberg.org/EEE-project/ancient-greek-backend-eee.git",
#     "unimorph-backend-eee @ git+https://codeberg.org/EEE-project/unimorph-backend-eee.git",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# ancient-greek-backend-eee = { git = "https://codeberg.org/EEE-project/ancient-greek-backend-eee.git" }
# unimorph-backend-eee = { git = "https://codeberg.org/EEE-project/unimorph-backend-eee.git" }
# ///

import marimo

__generated_with = "0.23.11"
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
def _(mo, trans_selector):
    _TRANS_DESC = {
        "подстрочник": "**подстрочник** · буквальный перевод слово-в-слово с сохранением порядка оригинала",
        "Жуковский":   "**Жуковский, 1849** · рус., белый стих (пятистопный ямб) · романтический возвышенный стиль · первый классический стихотворный перевод на русский",
        "Вересаев":    "**Вересаев, 1953** · рус., проза · ясный современный язык · ориентирован на смысловую точность · стандартный учебный перевод",
    }
    mo.md(_TRANS_DESC.get(trans_selector.value, ""))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Икты (ударные слоги) каждой стопы выделены <b style='color:#980000'>красным</b>.
    """)
    return


@app.cell(hide_code=True)
def _(
    SHOW_COVERAGE,
    STANZAS,
    WORDS_COMBINED,
    mo,
    stanza_selector,
    trans_selector,
):
    _st_map = {s["ref"]: s for s in STANZAS}
    _stanza = _st_map[stanza_selector.value]

    _GRK = (
        "font-family:'Gentium Plus','GFS Didot',serif;"
        "font-size:1.15em;line-height:2"
    )

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
        "νύμφη πόντι' ἔρυκε Καλυψὼ δῖα θεάων":
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

    def _bare(html):
        text, in_tag = '', False
        for ch in html:
            if ch == '<': in_tag = True
            elif ch == '>': in_tag = False
            elif not in_tag: text += ch
        return text.strip("·,;\.'·,!?·")


    def _norm(s):
        import unicodedata as _u
        nfd = _u.normalize("NFD", s)
        no_mn = "".join(c for c in nfd if _u.category(c) != "Mn")
        return _u.normalize("NFC", no_mn)

    def _split_html(s):
        tokens, buf, depth = [], [], 0
        for ch in s:
            if ch == '<': depth += 1; buf.append(ch)
            elif ch == '>': depth -= 1; buf.append(ch)
            elif ch == ' ' and depth == 0:
                tokens.append(''.join(buf)); buf = []
            else: buf.append(ch)
        if buf: tokens.append(''.join(buf))
        return tokens

    def _hl(line):
        colored = _RHYTHM_HTML.get(line, line)
        parts = []
        for w in _split_html(colored):
            if SHOW_COVERAGE.value is not None and _norm(_bare(w)) in WORDS_COMBINED:
                parts.append(
                    f"<span style='border-bottom:2px solid #b5451b;padding-bottom:0'>{w}</span>"
                )
            else:
                parts.append(w)
        return ' '.join(parts)

    if trans_selector.value == "подстрочник":
        _pairs = _stanza["interlinear"]
        _rows = "".join(
            f'<tr>'
            f'<td style="{_GRK};padding-right:1.5em;vertical-align:top">{_hl(gl) if gl else ""}</td>'
            f'<td style="font-size:1.0em;line-height:2.3;color:#333;vertical-align:top">{tl}</td>'
            f'</tr>'
            for gl, tl in _pairs
        )
        _content = mo.Html(
            '<table style="width:100%;border-collapse:collapse">' + _rows + "</table>"
        )
    else:
        _greek_html = "<br>".join(_hl(ln) for ln in _stanza["lines"])
        _left = mo.Html(
            f'<div style="{_GRK};padding-right:1.5em">'
            + _greek_html + "</div>"
        )
        _txt = _stanza["translations"].get(trans_selector.value, "—")
        _line_divs = "".join(
            f'<div>{l.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")}</div>'
            for l in _txt.split("\n")
        )
        _right = mo.Html(
            '<div style="font-size:1.0em;display:flex;flex-direction:column;'
            'justify-content:space-between;border-left:3px solid #ccc;padding-left:0.8em">'
            + _line_divs + "</div>"
        )
        _content = mo.hstack([_left, _right], justify="start", align="stretch")

    mo.vstack([
        mo.hstack([stanza_selector, trans_selector], justify="space-between"),
        _content,
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    SHOW_COVERAGE = mo.ui.radio(
        options={"выкл.": None, "словоформы": "current", "только Гомер": "homer", "все слова": "none"},
        value="выкл.",
        label="**Подсветка слов в тексте:**",
        inline=True,
    )
    SHOW_COVERAGE
    return (SHOW_COVERAGE,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Упражнение: словарная форма
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    filter_mode = mo.ui.radio(
        options={"словоформы": "current", "только Гомер": "homer", "все слова": "none"},
        value="словоформы",
        label="**Лексикон:**",
        inline=True,
    )
    filter_mode
    return (filter_mode,)


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
        title='## Упражнение: словарная форма',
        meaning_key='_label',
        form_key='form',
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ### О проверке форм (EEE)

    Упражнение использует [EEE](https://codeberg.org/EEE-project) — систему для построения интерактивных учебных материалов.
    В данном случае задействованы [модули морфологического анализа](https://codeberg.org/EEE-project/eee-project/src/branch/main/docs/backends.md):

    * [**unimorph-backend-eee**](https://codeberg.org/EEE-project/unimorph-backend-eee) — база данных UniMorph:
      для древнегреческого парадигмы существительных и прилагательных (глаголы отсутствуют);
      покрытие лучше для греческого НЗ, чем для гомеровского текста
    * [**ancient-greek-backend-eee**](https://codeberg.org/EEE-project/ancient-greek-backend-eee) — анализ на основе морфологических словарей с лексиконами:
      * **Homer** — лексикон гомеровского эпоса (Илиада, Одиссея); эпический/ионийский, ~VIII в. до н.э.
      * **LXX** — лексикон Септуагинты; эллинистический койне, ~III–I вв. до н.э.
      * **MorphGNT** — лексикон греческого Нового Завета; койне, I в. н.э.

    **Лексикон** (фильтр):

    - *словоформы* — слова, для которых движку удаётся построить парадигму,
      используя unimorph-backend-eee и ancient-greek-backend-eee с лексиконами Homer, LXX, MorphGNT
    - *только Гомер* — слова из гомеровского лексикона ancient-greek-backend-eee
    - *все слова* — весь словарь занятия без фильтрации

    В таблице словоформ можно переключаться между лексиконами разных исторических периодов,
    если соответствующие данные для данного слова в системе есть.
    """)
    return


@app.cell(hide_code=True)
def _(QUIZ_WORDS_RAW, SHOW_COVERAGE, ag_homer, build_paradigm_table, eee):
    import unicodedata as _u

    def _norm_f(s):
        nfd = _u.normalize("NFD", s)
        no_mn = "".join(c for c in nfd if _u.category(c) != "Mn")
        nfc = _u.normalize("NFC", no_mn)
        return nfc.strip("',.᾽᾿ʼ")

    def _words_for_coverage(mode):
        if mode is None:
            return set()
        if mode == "none":
            return {_norm_f(w["form"]) for w in QUIZ_WORDS_RAW}
        if mode == "homer":
            result = set()
            for w in QUIZ_WORDS_RAW:
                try:
                    pos = "adjective" if w["pos"] == "adj" else w["pos"]
                    slots = ag_homer.get_slot_templates("grc", pos, "ru") or []
                    if slots and eee.inflect_slot(w["lemma"], slots[0], pos, language="grc", backend="ag-homer"):
                        result.add(_norm_f(w["form"]))
                except Exception:
                    pass
            return result
        result = set()
        for w in QUIZ_WORDS_RAW:
            try:
                r = build_paradigm_table(w)
                if r and "#f97316" not in r:
                    result.add(_norm_f(w["form"]))
            except Exception:
                pass
        return result

    WORDS_COMBINED = _words_for_coverage(SHOW_COVERAGE.value)
    return (WORDS_COMBINED,)


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

    def _parse_iln(md):
        out, ref, grc, buf = {}, None, None, []
        for L in md.splitlines():
            if L.startswith("### Odyss. "):
                if ref: out[ref] = buf
                ref, grc, buf = L[11:].strip(), None, []
            elif L.startswith("**") and L.endswith("**"):
                grc = L[2:-2].strip()
            elif ref and L.strip() and grc is not None:
                buf.append((grc, L.strip()))
                grc = None
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
    _iln_ru = _parse_iln((_root / "interlenear_ru.md").read_text(encoding="utf-8"))
    _trans_ru, _desc_ru = _parse_trans((_root / "translations_ru.md").read_text(encoding="utf-8"))
    TRANS_DESC = _desc_ru
    STANZAS = [
        {
            "ref": ref,
            "lines": lines,
            "interlinear": _iln_ru.get(ref, []),
            "translations": {tr: d.get(ref, "—") for tr, d in _trans_ru.items()},
        }
        for ref, lines in _greek.items()
    ]
    return (STANZAS,)


@app.cell(hide_code=True)
def _(ag_backend, ag_homer, ag_lxx, ag_morphgnt, gu):
    import csv
    from pathlib import Path

    _vocab_path = Path(__file__).parent / "vocab_I_1-21.tsv"
    with open(_vocab_path, encoding="utf-8") as _f:
        QUIZ_WORDS_RAW = gu.resolve_word_grammar(
            list(csv.DictReader(_f, delimiter="\t")), ag_backend, "ru"
        )

    _POS_MAP = {"adj": "adjective"}
    _QUIZZABLE = {"noun", "verb", "adj"}
    _LEXICONS = [("homer", ag_homer), ("lxx", ag_lxx), ("morphgnt", ag_morphgnt)]

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
    ag_homer,
    build_paradigm_table,
    eee,
    filter_mode,
    set_cv,
    set_remaining,
):
    def _has_displayable_form(w):
        try:
            result = build_paradigm_table(w)
            if not result:
                return False
            return "#f97316" not in result
        except Exception:
            return False

    def _in_homer(w):
        try:
            pos = "adjective" if w["pos"] == "adj" else w["pos"]
            slots = ag_homer.get_slot_templates("grc", pos, "ru") or []
            if not slots:
                return False
            forms = eee.inflect_slot(w["lemma"], slots[0], pos, language="grc", backend="ag-homer")
            return bool(forms)
        except Exception:
            return False

    _mode = filter_mode.value
    if _mode == "none":
        QUIZ_WORDS = list(QUIZ_WORDS_RAW)
    elif _mode == "homer":
        QUIZ_WORDS = [w for w in QUIZ_WORDS_RAW if _in_homer(w)]
    else:
        _flags = [_has_displayable_form(w) for w in QUIZ_WORDS_RAW]
        QUIZ_WORDS = [w for w, ok in zip(QUIZ_WORDS_RAW, _flags) if ok]

    eee.add_labels(QUIZ_WORDS)

    set_cv(None)
    set_remaining(None)
    return (QUIZ_WORDS,)


@app.cell(hide_code=True)
def _(ag_backend, ag_homer, ag_lxx, ag_morphgnt, eee, um_backend):
    build_paradigm_table = eee.build_grc_paradigm_table(ag_backend, um_backend)
    build_lexicon_tabs = eee.build_grc_lexicon_tabs(
        ag_backend, um_backend,
        lexicons={"homer": ag_homer, "lxx": ag_lxx, "morphgnt": ag_morphgnt},
    )
    return (build_paradigm_table,)


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

    ag_backend = AncientGreekBackend(lexicons=["homer", "lxx", "morphgnt"])
    ag_homer = AncientGreekBackend(lexicons=["homer"])
    ag_lxx = AncientGreekBackend(lexicons=["lxx"])
    ag_morphgnt = AncientGreekBackend(lexicons=["morphgnt"])
    um_backend = UniMorphBackend(language="grc")
    eee.register_backend("grc", ag_backend, backend="ancient-greek")
    eee.register_backend("grc", ag_homer, backend="ag-homer")
    eee.register_backend("grc", um_backend, backend="unimorph")
    eee.set_chain("grc", ["ancient-greek", "unimorph"])
    gu = eee.GreekUtils(mo_module=mo)
    return ag_backend, ag_homer, ag_lxx, ag_morphgnt, eee, gu, mo, um_backend


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
