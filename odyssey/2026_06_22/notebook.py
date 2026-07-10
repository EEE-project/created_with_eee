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

__generated_with = "0.23.8"
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
    from pathlib import Path as _Path
    _thumb_path = _Path(__file__).parent / "map_ortelius.jpg"
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_PWHcMdBAUW2bygSvQbeTjE)"
    _left = mo.vstack([
        mo.md("# Одиссея для отважных"),
        mo.md(_badge),
        mo.md("## День 2 · Odyss. IX.39–61"),
    ])
    _right = mo.image(src=_thumb_path.read_bytes(), width=280) if _thumb_path.exists() else mo.Html("")
    mo.hstack([_left, _right], align="start")
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    _txt = f"**Материалы занятия:** [Od_IX_39-61.pdf]({NB_REMOTE}/Od_IX_39-61.pdf) · [Od_IX_39-61_vocabula.pdf]({NB_REMOTE}/Od_IX_39-61_vocabula.pdf)"
    mo.md(_txt)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Слова, слова…

    **μῆλον** (τό) — и *мелкий скот, овцы*, и *яблоко*.

    В нашем тексте (IX.45): *πολλὰ δὲ **μῆλα** ἔσφαζον* — «много скота они резали».
    Никаких яблок.

    ---

    **ἀγαθός** → **ἀρείων** → **ἄριστος** — суплетивное сравнение («хороший, доблестный»):

    | степень | ед. ч. | мн. ч. |
    |---------|--------|--------|
    | сравнительная | ἀρείων | ἀρείονες |
    | превосходная | ἄριστος | — |

    В тексте (IX.48): *πλέονες καὶ **ἀρείους*** — «более многочисленные и более доблестные».

    ср. англ. *good → better → best*.

    ---

    **μόρος** (ὁ) — *рок, судьба, гибель* (муж. род)
    **μόρον** (τό) — *тут, шелковица* (ср. род)

    В последней строке (IX.61): *φύγομεν **θάνατόν** τε **μόρον** τε* — «мы избежали смерти и рока».
    Но μόρον можно прочитать и как «тут»: избежали смерти и шелковицы.
    """)
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
        'Ἰλιόθεν με φέρων ἄνεμος Κικόνεσσι πέλασσεν,':
            "<b style='color:#980000'>Ἰ</b>λιόθεν με φέρ<b style='color:#980000'>ω</b>ν ἄνεμ<b style='color:#980000'>ο</b>ς Κικόν<b style='color:#980000'>ε</b>σσι πέλ<b style='color:#980000'>α</b>σσεν,",
        "Ἰσμάρῳ· ἔνθα δ' ἐγὼ πόλιν ἔπραθον, ὤλεσα δ' αὐτούς.":
            "<b style='color:#980000'>Ἰ</b>σμάρῳ· <b style='color:#980000'>ἔ</b>νθα δ' ἐγ<b style='color:#980000'>ὼ</b> πόλιν <b style='color:#980000'>ἔ</b>πραθον, <b style='color:#980000'>ὤ</b>λεσα δ' <b style='color:#980000'>αὐ</b>τούς.",
        "ἐκ πόλιος δ' ἀλόχους καὶ κτήματα πολλὰ λαβόντες":
            "<b style='color:#980000'>ἐ</b>κ πόλι<b style='color:#980000'>ο</b>ς δ' ἀλόχ<b style='color:#980000'>ου</b>ς καὶ κτ<b style='color:#980000'>ή</b>ματα π<b style='color:#980000'>ο</b>λλὰ λαβ<b style='color:#980000'>ό</b>ντες",
        "δασσάμεθ', ὡς μή τίς μοι ἀτεμβόμενος κίοι ἴσης.":
            "δ<b style='color:#980000'>α</b>σσάμεθ', <b style='color:#980000'>ὡ</b>ς μή τ<b style='color:#980000'>ί</b>ς μοι ἀτ<b style='color:#980000'>ε</b>μβόμεν<b style='color:#980000'>ο</b>ς κίοι <b style='color:#980000'>ἴ</b>σης.",
        "ἔνθ' ἦ τοι μὲν ἐγὼ διερῷ ποδὶ φευγέμεν ἡμέας":
            "<b style='color:#980000'>ἔ</b>νθ' ἦ τ<b style='color:#980000'>οι</b> μὲν ἐγ<b style='color:#980000'>ὼ</b> διερ<b style='color:#980000'>ῷ</b> ποδὶ φ<b style='color:#980000'>ευ</b>γέμεν <b style='color:#980000'>ἡ</b>μέας",
        'ἠνώγεα, τοὶ δὲ μέγα νήπιοι οὐκ ἐπίθοντο.':
            "<b style='color:#980000'>ἠ</b>νώγ<b style='color:#980000'>εα</b>, τοὶ δ<b style='color:#980000'>ὲ</b> μέγα ν<b style='color:#980000'>ή</b>πιοι <b style='color:#980000'>οὐ</b>κ ἐπίθ<b style='color:#980000'>ο</b>ντο.",
        'ἔνθα δὲ πολλὸν μὲν μέθυ πίνετο, πολλὰ δὲ μῆλα':
            "<b style='color:#980000'>ἔ</b>νθα δὲ π<b style='color:#980000'>ο</b>λλὸν μ<b style='color:#980000'>ὲ</b>ν μέθυ π<b style='color:#980000'>ί</b>νετο, π<b style='color:#980000'>ο</b>λλὰ δὲ μ<b style='color:#980000'>ῆ</b>λα",
        'ἔσφαζον παρὰ θῖνα καὶ εἰλίποδας ἕλικας βοῦς.':
            "<b style='color:#980000'>ἔ</b>σφαζ<b style='color:#980000'>ο</b>ν παρὰ θ<b style='color:#980000'>ῖ</b>να καὶ <b style='color:#980000'>εἰ</b>λίποδας ἕλικ<b style='color:#980000'>α</b>ς βοῦς.",
        "τόφρα δ' ἄρ' οἰχόμενοι Κίκονες Κικόνεσσι γεγώνευν,":
            "τ<b style='color:#980000'>ό</b>φρα δ' ἄρ' <b style='color:#980000'>οἰ</b>χόμεν<b style='color:#980000'>οι</b> Κίκον<b style='color:#980000'>ε</b>ς Κικόν<b style='color:#980000'>ε</b>σσι γεγ<b style='color:#980000'>ώ</b>νευν,",
        'οἵ σφιν γείτονες ἦσαν, ἅμα πλέονες καὶ ἀρείους,':
            "<b style='color:#980000'>οἵ</b> σφιν γ<b style='color:#980000'>εί</b>τονες <b style='color:#980000'>ἦ</b>σαν, ἅμ<b style='color:#980000'>α</b> πλέον<b style='color:#980000'>ε</b>ς καὶ ἀρ<b style='color:#980000'>εί</b>ους,",
        "ἤπειρον ναίοντες, ἐπιστάμενοι μὲν ἀφ' ἵππων":
            "<b style='color:#980000'>ἤ</b>πειρον ναί<b style='color:#980000'>ο</b>ντες, ἐπ<b style='color:#980000'>ι</b>στάμεν<b style='color:#980000'>οι</b> μὲν ἀφ' <b style='color:#980000'>ἵ</b>ππων",
        'ἀνδράσι μάρνασθαι καὶ ὅθι χρὴ πεζὸν ἐόντα.':
            "<b style='color:#980000'>ἀ</b>νδράσι μ<b style='color:#980000'>ά</b>ρνασθ<b style='color:#980000'>αι</b> καὶ ὅθ<b style='color:#980000'>ι</b> χρὴ π<b style='color:#980000'>ε</b>ζὸν ἐ<b style='color:#980000'>ό</b>ντα.",
        "ἦλθον ἔπειθ', ὅσα φύλλα καὶ ἄνθεα γίνεται ὥρῃ,":
            "<b style='color:#980000'>ἦ</b>λθον ἔπ<b style='color:#980000'>ει</b>θ', ὅσα φ<b style='color:#980000'>ύ</b>λλα καὶ <b style='color:#980000'>ἄ</b>νθεα γ<b style='color:#980000'>ί</b>νεται <b style='color:#980000'>ὥ</b>ρῃ,",
        'ἠέριοι· τότε δή ῥα κακὴ Διὸς αἶσα παρέστη':
            "<b style='color:#980000'>ἠ</b>έρι<b style='color:#980000'>οι</b>· τότε δ<b style='color:#980000'>ή</b> ῥα κακ<b style='color:#980000'>ὴ</b> Διὸς <b style='color:#980000'>αἶ</b>σα παρ<b style='color:#980000'>έ</b>στη",
        "ἡμῖν αἰνομόροισιν, ἵν' ἄλγεα πολλὰ πάθοιμεν.":
            "<b style='color:#980000'>ἡ</b>μῖν <b style='color:#980000'>αἰ</b>νομόρ<b style='color:#980000'>οι</b>σιν, ἵν' <b style='color:#980000'>ἄ</b>λγεα π<b style='color:#980000'>ο</b>λλὰ πάθ<b style='color:#980000'>οι</b>μεν.",
        "στησάμενοι δ' ἐμάχοντο μάχην παρὰ νηυσὶ θοῇσι,":
            "στ<b style='color:#980000'>η</b>σάμεν<b style='color:#980000'>οι</b> δ' ἐμάχ<b style='color:#980000'>ο</b>ντο μάχ<b style='color:#980000'>η</b>ν παρὰ ν<b style='color:#980000'>ηυ</b>σὶ θο<b style='color:#980000'>ῇ</b>σι,",
        "βάλλον δ' ἀλλήλους χαλκήρεσιν ἐγχείῃσιν.":
            "β<b style='color:#980000'>ά</b>λλον δ' <b style='color:#980000'>ἀ</b>λλήλ<b style='color:#980000'>ου</b>ς χαλκ<b style='color:#980000'>ή</b>ρεσιν <b style='color:#980000'>ἐ</b>γχεί<b style='color:#980000'>ῃ</b>σιν.",
        'ὄφρα μὲν ἠὼς ἦν καὶ ἀέξετο ἱερὸν ἦμαρ,':
            "<b style='color:#980000'>ὄ</b>φρα μὲν <b style='color:#980000'>ἠ</b>ὼς <b style='color:#980000'>ἦ</b>ν καὶ ἀ<b style='color:#980000'>έ</b>ξετο <b style='color:#980000'>ἱ</b>ερὸν <b style='color:#980000'>ἦ</b>μαρ,",
        "τόφρα δ' ἀλεξόμενοι μένομεν πλέονάς περ ἐόντας·":
            "τ<b style='color:#980000'>ό</b>φρα δ' ἀλ<b style='color:#980000'>ε</b>ξόμεν<b style='color:#980000'>οι</b> μένομ<b style='color:#980000'>ε</b>ν πλέον<b style='color:#980000'>ά</b>ς περ ἐ<b style='color:#980000'>ό</b>ντας·",
        "ἦμος δ' ἠέλιος μετενίσετο βουλυτόνδε,":
            "<b style='color:#980000'>ἦ</b>μος δ' <b style='color:#980000'>ἠ</b>έλι<b style='color:#980000'>ο</b>ς μετεν<b style='color:#980000'>ί</b>σετο β<b style='color:#980000'>ου</b>λυτ<b style='color:#980000'>ό</b>νδε,",
        'καὶ τότε δὴ Κίκονες κλῖναν δαμάσαντες Ἀχαιούς.':
            "κ<b style='color:#980000'>αὶ</b> τότε δ<b style='color:#980000'>ὴ</b> Κίκον<b style='color:#980000'>ε</b>ς κλῖν<b style='color:#980000'>α</b>ν δαμάσ<b style='color:#980000'>α</b>ντες Ἀχ<b style='color:#980000'>αι</b>ούς.",
        "ἓξ δ' ἀφ' ἑκάστης νηὸς ἐϋκνήμιδες ἑταῖροι":
            "<b style='color:#980000'>ἓ</b>ξ δ' ἀφ' ἑκ<b style='color:#980000'>ά</b>στης ν<b style='color:#980000'>η</b>ὸς ἐ<b style='color:#980000'>ϋ</b>κνήμ<b style='color:#980000'>ι</b>δες ἑτ<b style='color:#980000'>αῖ</b>ροι",
        "ὤλονθ'· οἱ δ' ἄλλοι φύγομεν θάνατόν τε μόρον τε.":
            "<b style='color:#980000'>ὤ</b>λονθ'· <b style='color:#980000'>οἱ</b> δ' ἄλλ<b style='color:#980000'>οι</b> φύγομ<b style='color:#980000'>ε</b>ν θάνατ<b style='color:#980000'>ό</b>ν τε μόρ<b style='color:#980000'>ο</b>ν τε.",
    }

    def _bare(html):
        text, in_tag = '', False
        for ch in html:
            if ch == '<': in_tag = True
            elif ch == '>': in_tag = False
            elif not in_tag: text += ch
        return text.strip("·,;.'·,!?·")


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
            f'<div style="{_GRK};padding-right:1.5em">' + _greek_html + "</div>"
        )
        _txt = _stanza["translations"].get(trans_selector.value, "—")
        _line_divs = "".join(
            f'<div>{l.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")}</div>'
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
        options={
            "Гомер": "homer",
            "выкл.": None,
            # "словоформы": "current",
            # "все слова": "none",
        },
        value="Гомер",
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
        options={
            # "словоформы": "current",
            "Гомер": "homer",
            "все слова": "none",
        },
        value="Гомер",
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
    build_lexicon_tabs,
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
        build_paradigm_table=build_lexicon_tabs,
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
    * [**ancient-greek-backend-eee**](https://codeberg.org/EEE-project/ancient-greek-backend-eee) — анализ на основе морфологических словарей; лексиконы по эпохам:
      * **Homer** — гомеровский эпос (Илиада, Одиссея); эпический/ионийский, ~VIII в. до н.э.
      * **Словарь классического аттического** — (pratt + ltrg + lsj); аттика V–IV вв. до н.э.
      * **LXX** — Септуагинта; эллинистический койне, IV–I вв. до н.э.
      * **MorphGNT** — греческий Новый Завет; римский койне, I–III вв. н.э.
    * [**modern-greek-backend-eee**](https://codeberg.org/EEE-project/modern-greek-backend-eee) — новогреческий (демотика); показывает, как древнее слово склоняется/спрягается сегодня — последняя «ступень» в таблице словоформ (если у слова есть живой новогреческий рефлекс)

    **Лексикон** (фильтр):

    <!-- - *словоформы* — слова, для которых движку удаётся построить парадигму,
      используя unimorph-backend-eee и ancient-greek-backend-eee с лексиконами Homer, LXX, MorphGNT -->
    - *Гомер* — слова из гомеровского лексикона ancient-greek-backend-eee
    - *все слова* — весь словарь занятия без фильтрации

    В таблице словоформ можно переключаться между лексиконами разных исторических периодов,
    если соответствующие данные для данного слова в системе есть.
    """)
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
def _(ag_lsj, ag_backend, ag_homer, ag_lxx, ag_morphgnt, gu):
    import csv
    from pathlib import Path

    _vocab_path = Path(__file__).parent / "vocab_IX_39-61.tsv"
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
        lexicons = ", ".join(f'\"{s}\"' for s in sources)
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
    filter_mode,
    grc_lexicons,
    set_cv,
    set_remaining,
):
    QUIZ_WORDS = eee.filter_grc_quiz_words(
        QUIZ_WORDS_RAW, filter_mode.value,
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    )

    eee.add_labels(QUIZ_WORDS)

    set_cv(None)
    set_remaining(None)
    return (QUIZ_WORDS,)


@app.cell(hide_code=True)
def _(QUIZ_WORDS_RAW, SHOW_COVERAGE, build_paradigm_table, eee, grc_lexicons):
    WORDS_COMBINED = eee.grc_coverage_words(
        QUIZ_WORDS_RAW, SHOW_COVERAGE.value,
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    )
    return (WORDS_COMBINED,)


@app.cell(hide_code=True)
def _(ag_backend, eee, grc_lexicons, mg, um_backend):
    build_paradigm_table = eee.build_grc_paradigm_table(ag_backend, um_backend)
    build_lexicon_tabs = eee.build_grc_lexicon_tabs(
        ag_backend, um_backend,
        lexicons=grc_lexicons,
        el_backend=mg,
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
    return ag_lsj, ag_backend, ag_homer, ag_lxx, ag_morphgnt, eee, grc_lexicons, gu, mg, mo, um_backend


@app.cell(hide_code=True)
def _(cfg, gu):
    from pathlib import Path as _P
    NB_DIR = _P(__file__).parent
    NB_REMOTE = f"{cfg.raw_base}/2026_06_22"
    for _f in (
        'Od_IX_39-61.pdf',
        'Od_IX_39-61_vocabula.pdf',
        'map_ortelius.jpg',
        'map_ortelius_full.jpg',
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
