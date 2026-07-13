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
    from pathlib import Path as _Path
    _thumb_path = _Path(__file__).parent / "odysseus_bust.jpg"
    _badge = ""  # молаб-бейдж добавить после загрузки в molab
    _left = mo.vstack([
        mo.md("# Одиссея для отважных"),
        mo.md(_badge),
        mo.md("## День 3 · Odyss. IX.62–81"),
    ])
    _right = mo.image(src=_thumb_path.read_bytes(), width=280) if _thumb_path.exists() else mo.Html("")
    mo.hstack([_left, _right], align="start")
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    _txt = f"**Материалы занятия:** [Od_IX_62-81.pdf]({NB_REMOTE}/Od_IX_62-81.pdf) · [Od_IX_62-81_vocabula.docx]({NB_REMOTE}/Od_IX_62-81_vocabula.docx)"
    mo.md(_txt)
    return


@app.cell(hide_code=True)
def _(mo):
    from pathlib import Path as _Pp
    _prep = _Pp(__file__).parent / "prepositions.jpg"
    _pimg = mo.image(src=_prep.read_bytes(), width=440) if _prep.exists() else mo.Html("")
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
def _(mo):
    from pathlib import Path as _Pm
    _d = _Pm(__file__).parent
    _c, _m = _d / "malea_cliff.jpg", _d / "malea_map.jpg"
    _imgs = mo.hstack([
        mo.image(src=_c.read_bytes(), width=300) if _c.exists() else mo.Html(""),
        mo.image(src=_m.read_bytes(), width=300) if _m.exists() else mo.Html(""),
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
        'ἔνθεν δὲ προτέρω πλέομεν ἀκαχήμενοι ἦτορ,':
            "<b style='color:#980000'>ἔ</b>νθεν δ<b style='color:#980000'>ὲ</b> προτέρ<b style='color:#980000'>ω</b> πλέομ<b style='color:#980000'>εν</b> ἀκαχ<b style='color:#980000'>ή</b>μενοι <b style='color:#980000'>ἦ</b>τορ,",
        'ἄσμενοι ἐκ θανάτοιο, φίλους ὀλέσαντες ἑταίρους.':
            "<b style='color:#980000'>ἄ</b>σμενοι <b style='color:#980000'>ἐ</b>κ θανάτ<b style='color:#980000'>οι</b>ο, φίλ<b style='color:#980000'>ους</b> ὀλέσ<b style='color:#980000'>α</b>ντες ἑτ<b style='color:#980000'>αί</b>ρους.",
        "οὐδ' ἄρα μοι προτέρω νῆες κίον ἀμφιέλισσαι,":
            "<b style='color:#980000'>οὐ</b>δ' ἄρα μ<b style='color:#980000'>οι</b> προτέρ<b style='color:#980000'>ω</b> νῆ<b style='color:#980000'>ες</b> κίον ἀμφιέλ<b style='color:#980000'>ι</b>σσαι,",
        'πρίν τινα τῶν δειλῶν ἑτάρων τρὶς ἕκαστον ἀῦσαι,':
            "πρ<b style='color:#980000'>ί</b>ν τινα τ<b style='color:#980000'>ῶν</b> δειλ<b style='color:#980000'>ῶν</b> ἑτάρ<b style='color:#980000'>ων</b> τρὶς ἕκ<b style='color:#980000'>α</b>στον ἀ<b style='color:#980000'>ῦ</b>σαι,",
        'οἳ θάνον ἐν πεδίῳ Κικόνων ὕπο δῃωθέντες.':
            "<b style='color:#980000'>οἳ</b> θάνον <b style='color:#980000'>ἐ</b>ν πεδί<b style='color:#980000'>ῳ</b> Κικόν<b style='color:#980000'>ων</b> ὕπο δ<b style='color:#980000'>ῃ</b>ωθ<b style='color:#980000'>έ</b>ντες.",
        "νηυσὶ δ' ἐπῶρσ' ἄνεμον Βορέην νεφεληγερέτα Ζεὺς":
            "ν<b style='color:#980000'>ηυ</b>σὶ δ' ἐπ<b style='color:#980000'>ῶ</b>ρσ' ἄνεμ<b style='color:#980000'>ον</b> Βορέ<b style='color:#980000'>η</b>ν νεφελ<b style='color:#980000'>η</b>γερέτ<b style='color:#980000'>α</b> Ζεὺς",
        'λαίλαπι θεσπεσίῃ, σὺν δὲ νεφέεσσι κάλυψε':
            "λ<b style='color:#980000'>αί</b>λαπι θ<b style='color:#980000'>ε</b>σπεσί<b style='color:#980000'>ῃ</b>, σὺν δ<b style='color:#980000'>ὲ</b> νεφέ<b style='color:#980000'>ε</b>σσι κάλ<b style='color:#980000'>υ</b>ψε",
        "γαῖαν ὁμοῦ καὶ πόντον· ὀρώρει δ' οὐρανόθεν νύξ.":
            "γ<b style='color:#980000'>αῖ</b>αν ὁμ<b style='color:#980000'>οῦ</b> καὶ π<b style='color:#980000'>ό</b>ντον· ὀρ<b style='color:#980000'>ώ</b>ρει δ' <b style='color:#980000'>οὐ</b>ρανόθεν νύξ.",
        "αἱ μὲν ἔπειτ' ἐφέροντ' ἐπικάρσιαι, ἱστία δέ σφιν":
            "<b style='color:#980000'>αἱ</b> μὲν ἔπ<b style='color:#980000'>ει</b>τ' ἐφέρ<b style='color:#980000'>ο</b>ντ' ἐπικ<b style='color:#980000'>ά</b>ρσιαι, <b style='color:#980000'>ἱ</b>στία δ<b style='color:#980000'>έ</b> σφιν",
        'τριχθά τε καὶ τετραχθὰ διέσχισεν ἲς ἀνέμοιο.':
            "τρ<b style='color:#980000'>ι</b>χθά τε κ<b style='color:#980000'>αὶ</b> τετρ<b style='color:#980000'>α</b>χθὰ δι<b style='color:#980000'>έ</b>σχισεν <b style='color:#980000'>ἲ</b>ς ἀνέμ<b style='color:#980000'>οι</b>ο.",
        'καὶ τὰ μὲν ἐς νῆας κάθεμεν, δείσαντες ὄλεθρον,':
            "κ<b style='color:#980000'>αὶ</b> τὰ μὲν <b style='color:#980000'>ἐ</b>ς νῆ<b style='color:#980000'>α</b>ς κάθεμ<b style='color:#980000'>εν</b>, δείσ<b style='color:#980000'>α</b>ντες <b style='color:#980000'>ὄ</b>λεθρον,",
        "αὐτὰς δ' ἐσσυμένως προερέσσαμεν ἤπειρόνδε.":
            "<b style='color:#980000'>αὐ</b>τὰς δ' <b style='color:#980000'>ἐ</b>σσυμέν<b style='color:#980000'>ως</b> προερ<b style='color:#980000'>έ</b>σσαμεν <b style='color:#980000'>ἤ</b>πειρ<b style='color:#980000'>ό</b>νδε.",
        "ἔνθα δύω νύκτας δύο τ' ἤματα συνεχὲς αἰεὶ":
            "<b style='color:#980000'>ἔ</b>νθα δύ<b style='color:#980000'>ω</b> νύκτ<b style='color:#980000'>ας</b> δύο τ' <b style='color:#980000'>ἤ</b>ματα σ<b style='color:#980000'>υ</b>νεχὲς <b style='color:#980000'>αἰ</b>εὶ",
        "κείμεθ', ὁμοῦ καμάτῳ τε καὶ ἄλγεσι θυμὸν ἔδοντες.":
            "κ<b style='color:#980000'>εί</b>μεθ', ὁμ<b style='color:#980000'>οῦ</b> καμάτ<b style='color:#980000'>ῳ</b> τε καὶ <b style='color:#980000'>ἄ</b>λγεσι θ<b style='color:#980000'>υ</b>μὸν <b style='color:#980000'>ἔ</b>δοντες.",
        "ἀλλ' ὅτε δὴ τρίτον ἦμαρ ἐυπλόκαμος τέλεσ' Ἠώς,":
            "<b style='color:#980000'>ἀ</b>λλ' ὅτε δ<b style='color:#980000'>ὴ</b> τρίτον <b style='color:#980000'>ἦ</b>μαρ ἐ<b style='color:#980000'>υ</b>πλόκαμ<b style='color:#980000'>ο</b>ς τέλεσ' <b style='color:#980000'>Ἠ</b>ώς,",
        "ἱστοὺς στησάμενοι ἀνά θ' ἱστία λεύκ' ἐρύσαντες":
            "<b style='color:#980000'>ἱ</b>στοὺς στ<b style='color:#980000'>η</b>σάμεν<b style='color:#980000'>οι</b> ἀνά θ' <b style='color:#980000'>ἱ</b>στία λ<b style='color:#980000'>εύ</b>κ' ἐρύσ<b style='color:#980000'>α</b>ντες",
        "ἥμεθα, τὰς δ' ἄνεμός τε κυβερνῆταί τ' ἴθυνον.":
            "<b style='color:#980000'>ἥ</b>μεθα, τ<b style='color:#980000'>ὰς</b> δ' ἄνεμ<b style='color:#980000'>ό</b>ς τε κυβ<b style='color:#980000'>ε</b>ρνῆτ<b style='color:#980000'>αί</b> τ' <b style='color:#980000'>ἴ</b>θυνον.",
        'καί νύ κεν ἀσκηθὴς ἱκόμην ἐς πατρίδα γαῖαν·':
            "κ<b style='color:#980000'>αί</b> νύ κεν <b style='color:#980000'>ἀ</b>σκηθ<b style='color:#980000'>ὴ</b>ς ἱκόμ<b style='color:#980000'>η</b>ν ἐς π<b style='color:#980000'>α</b>τρίδα γ<b style='color:#980000'>αῖ</b>αν·",
        'ἀλλά με κῦμα ῥόος τε περιγνάμπτοντα Μάλειαν':
            "<b style='color:#980000'>ἀ</b>λλά με κ<b style='color:#980000'>ῦ</b>μα ῥό<b style='color:#980000'>ος</b> τε περ<b style='color:#980000'>ι</b>γνάμπτ<b style='color:#980000'>ο</b>ντα Μάλ<b style='color:#980000'>ει</b>αν",
        'καὶ Βορέης ἀπέωσε, παρέπλαγξεν δὲ Κυθήρων.':
            "κ<b style='color:#980000'>αὶ</b> Βορέ<b style='color:#980000'>η</b>ς ἀπέ<b style='color:#980000'>ω</b>σε, παρ<b style='color:#980000'>έ</b>πλαγξ<b style='color:#980000'>ε</b>ν δὲ Κυθ<b style='color:#980000'>ή</b>ρων.",
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
    build_lexicon_tabs,
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
        title='## Упражнение: словарная форма',
        meaning_key='_label',
        form_key='form',
        build_paradigm_table=build_lexicon_tabs,
        renew_btn=quiz_renew_btn,
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
def _(ag_backend, ag_byzantine, ag_homer, ag_lsj, ag_lxx, ag_morphgnt, eee, gu):
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
    filter_mode,
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
        QUIZ_WORDS_RAW, filter_mode.value,
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    ), n=SESSION_SIZE)

    eee.add_labels(QUIZ_WORDS)

    gu.reset_quiz_state(quiz_renew_btn, set_cv, set_remaining, set_score,
                         set_history, set_future, set_restore_entry)
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
