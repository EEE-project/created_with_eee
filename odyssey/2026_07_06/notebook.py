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
    _thumb_path = _Path(__file__).parent / "lotus_plant.jpg"
    _badge = ""  # молаб-бейдж добавить после загрузки в molab
    _left = mo.vstack([
        mo.md("# Одиссея для отважных"),
        mo.md(_badge),
        mo.md("## День 4 · Odyss. IX.82–104"),
    ])
    _right = mo.image(src=_thumb_path.read_bytes(), width=280) if _thumb_path.exists() else mo.Html("")
    mo.hstack([_left, _right], align="start")
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    _txt = f"**Материалы занятия:** [Od_IX_82-104.pdf]({NB_REMOTE}/Od_IX_82-104.pdf) · [Od_IX_82-104_vocabula.pdf]({NB_REMOTE}/Od_IX_82-104_vocabula.pdf)"
    mo.md(_txt)
    return


@app.cell(hide_code=True)
def _(mo):
    from pathlib import Path as _Pl
    _lot = _Pl(__file__).parent / "lotus_plant.jpg"
    _limg = mo.image(src=_lot.read_bytes(), width=300) if _lot.exists() else mo.Html("")
    _cap = mo.md(
        "<div style='font-size:.8em;color:#9ca3af;text-align:center'>"
        "<i>Ziziphus jujuba</i> — Adolphus Ypey, <i>Afbeeldingen der artseny-gewassen</i>, 1813</div>"
    )
    _txt = mo.md(r"""
    ---
    ## Что за «лотос»?

    Что за растение ели лотофаги у Гомера — точно неизвестно. Геродот описывает его дважды.

    **Hdt. II.92** (о египетском лотосе):

    > …φύεται ἐν τῷ ὕδατι κρίνεα πολλά, τὰ Αἰγύπτιοι καλέουσι **λωτόν**. […]
    > Ἔστι δὲ καὶ ἡ ῥίζα τοῦ λωτοῦ τούτου ἐδωδίμη […] ἐὸν στρογγύλον,
    > **μέγαθος κατὰ μῆλον**.

    «…в воде вырастает много лилий, которые египтяне называют лотосом… Корень
    этого растения также съедобен, круглый, величиной с яблоко».

    **Hdt. IV.177** (о ливийских лотофагах):

    > Ἀκτὴν δὲ προέχουσαν ἐς τὸν πόντον … νέμονται **Λωτοφάγοι**, οἳ τὸν καρπὸν
    > μοῦνον τοῦ λωτοῦ τρώγοντες ζώουσι. … γλυκύτητα δὲ τοῦ φοίνικος τῷ καρπῷ
    > προσείκελος. Ποιεῦνται δὲ ἐκ τοῦ καρποῦ τούτου οἱ Λωτοφάγοι καὶ **οἶνον**.

    «…обитают лотофаги. Они питаются исключительно плодами лотоса… по сладости
    плод похож на финик; из него лотофаги делают и вино».
    *(речь о Малом Сирте — побережье современного Туниса.)*

    **Полибий**
    (II в. до н.э., в пересказе Страбона) отождествил его с **зизифусом**
    (*Ziziphus lotus*, дикое унаби, родич ююбы): колючий кустарник с мелкими
    листьями, плод как круглая слива, при созревании пурпурный, из которого,
    как из фиников, делали вино. Раньше о растении писали Геродот и Феофраст,
    позже его популяризировал Плиний Старший.
    """)
    mo.vstack([_txt, mo.hstack([mo.vstack([_limg, _cap])], justify="center")])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Λωτός — слово-ловушка

    В современном греческом *λωτός* — это **хурма** (от *Diospyros
    lotus* — дикая хурма); финик же — *χουρμάς*, а финиковая пальма — *φοίνικας*. Тем же словом
    *λωτός* называют и водяной лотос — различают по контексту.
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
        "ἔνθεν δ' ἐννῆμαρ φερόμην ὀλοοῖσ' ἀνέμοισι":
            "<b style='color:#980000'>ἔ</b>νθεν δ' <b style='color:#980000'>ἐ</b>ννῆμ<b style='color:#980000'>α</b>ρ φερόμ<b style='color:#980000'>η</b>ν ὀλο<b style='color:#980000'>οῖ</b>σ' ἀνέμ<b style='color:#980000'>οι</b>σι",
        "πόντον ἐπ' ἰχθυόεντα· ἀτὰρ δεκάτῃ ἐπέβημεν":
            "<b style='color:#980000'>πό</b>ντον ἐπ' <b style='color:#980000'>ἰ</b>χθυόεντα· ἀτ<b style='color:#980000'>ὰ</b>ρ δεκάτ<b style='color:#980000'>ῃ</b> ἐπ<b style='color:#980000'>έ</b>βημεν",
        "γαίης Λωτοφάγων, οἵ τ' ἄνθινον εἶδαρ ἔδουσιν.":
            "γ<b style='color:#980000'>αί</b>ης Λ<b style='color:#980000'>ω</b>τοφάγ<b style='color:#980000'>ω</b>ν, οἵ τ' <b style='color:#980000'>ἄ</b>νθινον <b style='color:#980000'>εἶ</b>δαρ ἔδ<b style='color:#980000'>ου</b>σιν.",
        "ἔνθα δ' ἐπ' ἠπείρου βῆμεν καὶ ἀφυσσάμεθ' ὕδωρ,":
            "<b style='color:#980000'>ἔ</b>νθα δ' ἐπ' <b style='color:#980000'>ἠ</b>πείρ<b style='color:#980000'>ου</b> βῆμ<b style='color:#980000'>εν</b> καὶ ἀφ<b style='color:#980000'>υ</b>σσάμεθ' <b style='color:#980000'>ὕ</b>δωρ,",
        'αἶψα δὲ δεῖπνον ἕλοντο θοῇς παρὰ νηυσὶν ἑταῖροι.':
            "<b style='color:#980000'>αἶ</b>ψα δὲ δ<b style='color:#980000'>εῖ</b>πνον ἕλοντο θο<b style='color:#980000'>ῇ</b>ς παρὰ ν<b style='color:#980000'>η</b>υσὶν ἑτ<b style='color:#980000'>αῖ</b>ροι.",
        "αὐτὰρ ἐπεὶ σίτοιό τ' ἐπασσάμεθ' ἠδὲ ποτῆτος,":
            "<b style='color:#980000'>αὐ</b>τὰρ ἐπ<b style='color:#980000'>εὶ</b> σίτ<b style='color:#980000'>οι</b>ό τ' ἐπ<b style='color:#980000'>α</b>σσάμεθ' <b style='color:#980000'>ἠ</b>δὲ ποτ<b style='color:#980000'>ῆ</b>τος,",
        "δὴ τότ' ἐγὼν ἑτάρους προΐην πεύθεσθαι ἰόντας,":
            "δ<b style='color:#980000'>ὴ</b> τότ' ἐγ<b style='color:#980000'>ὼ</b>ν ἑτάρ<b style='color:#980000'>ου</b>ς προΐην π<b style='color:#980000'>εύ</b>θ<b style='color:#980000'>ε</b>σθαι ἰ<b style='color:#980000'>ό</b>ντας,",
        'οἵ τινες ἀνέρες εἶεν ἐπὶ χθονὶ σῖτον ἔδοντες,':
            "<b style='color:#980000'>οἵ</b> τινες <b style='color:#980000'>ἀ</b>νέρες <b style='color:#980000'>εἶ</b>εν ἐπ<b style='color:#980000'>ὶ</b> χθονὶ σ<b style='color:#980000'>ῖ</b>τ<b style='color:#980000'>ο</b>ν ἔδοντες,",
        "ἄνδρε δύω κρίνας, τρίτατον κήρυχ' ἅμ' ὀπάσσας.":
            "<b style='color:#980000'>ἄ</b>νδρε δύ<b style='color:#980000'>ω</b> κρίν<b style='color:#980000'>α</b>ς, τρίτατ<b style='color:#980000'>ο</b>ν κήρ<b style='color:#980000'>υ</b>χ' ἅμ' ὀπ<b style='color:#980000'>ά</b>σσας.",
        "οἱ δ' αἶψ' οἰχόμενοι μίγεν ἀνδράσι Λωτοφάγοισιν·":
            "<b style='color:#980000'>οἱ</b> δ' αἶψ' <b style='color:#980000'>οἰ</b>χόμεν<b style='color:#980000'>οι</b> μίγεν <b style='color:#980000'>ἀ</b>νδράσι Λ<b style='color:#980000'>ω</b>τοφάγ<b style='color:#980000'>οι</b>σιν·",
        "οὐδ' ἄρα Λωτοφάγοι μήδονθ' ἑτάροισιν ὄλεθρον":
            "<b style='color:#980000'>οὐ</b>δ' ἄρα Λ<b style='color:#980000'>ω</b>τοφάγ<b style='color:#980000'>οι</b> μήδ<b style='color:#980000'>ο</b>νθ' ἑτάρ<b style='color:#980000'>οι</b>σιν <b style='color:#980000'>ὄ</b>λεθρον",
        "ἡμετέροισ', ἀλλά σφι δόσαν λωτοῖο πάσασθαι.":
            "<b style='color:#980000'>ἡ</b>μετέρ<b style='color:#980000'>οι</b>σ', ἀλλ<b style='color:#980000'>ά</b> σφι δόσ<b style='color:#980000'>α</b>ν λωτ<b style='color:#980000'>οῖ</b>ο πάσασθαι.",
        "τῶν δ' ὅς τις λωτοῖο φάγοι μελιηδέα καρπόν,":
            "τ<b style='color:#980000'>ῶν</b> δ' ὅς τ<b style='color:#980000'>ι</b>ς λωτ<b style='color:#980000'>οῖ</b>ο φάγ<b style='color:#980000'>οι</b> μελι<b style='color:#980000'>η</b>δέα κ<b style='color:#980000'>α</b>ρπόν,",
        "οὐκέτ' ἀπαγγεῖλαι πάλιν ἤθελεν οὐδὲ νέεσθαι,":
            "<b style='color:#980000'>οὐ</b>κέτ' ἀπ<b style='color:#980000'>α</b>γγ<b style='color:#980000'>εῖ</b>λαι πάλιν <b style='color:#980000'>ἤ</b>θελεν <b style='color:#980000'>οὐ</b>δὲ ν<b style='color:#980000'>έ</b>εσθαι,",
        "ἀλλ' αὐτοῦ βούλοντο μετ' ἀνδράσι Λωτοφάγοισι":
            "<b style='color:#980000'>ἀ</b>λλ' αὐτ<b style='color:#980000'>οῦ</b> β<b style='color:#980000'>ο</b>ύλοντο μετ' <b style='color:#980000'>ἀ</b>νδράσι Λ<b style='color:#980000'>ω</b>τοφάγ<b style='color:#980000'>οι</b>σι",
        'λωτὸν ἐρεπτόμενοι μενέμεν νόστου τε λαθέσθαι.':
            "λ<b style='color:#980000'>ω</b>τὸν ἐρ<b style='color:#980000'>ε</b>πτόμεν<b style='color:#980000'>οι</b> μεν<b style='color:#980000'>έ</b>μεν νόστ<b style='color:#980000'>ου</b> τε λαθ<b style='color:#980000'>έ</b>σθαι.",
        'τοὺς μὲν ἐγὼν ἐπὶ νῆας ἄγον κλαίοντας ἀνάγκῃ,':
            "τ<b style='color:#980000'>οὺ</b>ς μὲν ἐγ<b style='color:#980000'>ὼ</b>ν ἐπ<b style='color:#980000'>ὶ</b> νῆας <b style='color:#980000'>ἄ</b>γον κλα<b style='color:#980000'>ί</b>οντας ἀν<b style='color:#980000'>ά</b>γκῃ,",
        "νηυσὶ δ' ἐνὶ γλαφυρῇσιν ὑπὸ ζυγὰ δῆσα ἐρύσσας·":
            "ν<b style='color:#980000'>ηυ</b>σὶ δ' ἐν<b style='color:#980000'>ὶ</b> γλαφυρ<b style='color:#980000'>ῇ</b>σιν ὑπ<b style='color:#980000'>ὸ</b> ζυγ<b style='color:#980000'>ὰ</b> δ<b style='color:#980000'>ῆ</b>σα ἐρύσσας·",
        'αὐτὰρ τοὺς ἄλλους κελόμην ἐρίηρας ἑταίρους':
            "<b style='color:#980000'>αὐ</b>τὰρ τ<b style='color:#980000'>οὺ</b>ς ἄλλ<b style='color:#980000'>ου</b>ς κελ<b style='color:#980000'>ό</b>μην ἐρ<b style='color:#980000'>ί</b>ηρας ἑτ<b style='color:#980000'>αί</b>ρους",
        'σπερχομένους νηῶν ἐπιβαινέμεν ὠκειάων,':
            "σπ<b style='color:#980000'>ε</b>ρχομέν<b style='color:#980000'>ου</b>ς νη<b style='color:#980000'>ῶ</b>ν ἐπιβ<b style='color:#980000'>αι</b>νέμεν <b style='color:#980000'>ὠ</b>κει<b style='color:#980000'>ά</b>ων,",
        'μή πώς τις λωτοῖο φαγὼν νόστοιο λάθηται.':
            "μ<b style='color:#980000'>ή</b> π<b style='color:#980000'>ώ</b>ς τις λωτ<b style='color:#980000'>οῖ</b>ο φαγ<b style='color:#980000'>ὼ</b>ν νόστ<b style='color:#980000'>οι</b>ο λ<b style='color:#980000'>ά</b>θηται.",
        "οἱ δ' αἶψ' εἴσβαινον καὶ ἐπὶ κληῖσι καθῖζον,":
            "<b style='color:#980000'>οἱ</b> δ' αἶψ' <b style='color:#980000'>εἴ</b>σβαινον κ<b style='color:#980000'>αὶ</b> ἐπ<b style='color:#980000'>ὶ</b> κλη<b style='color:#980000'>ῖ</b>σι καθ<b style='color:#980000'>ῖ</b>ζον,",
        "ἑξῆς δ' ἑζόμενοι πολιὴν ἅλα τύπτον ἐρετμοῖς.":
            "ἑξ<b style='color:#980000'>ῆ</b>ς δ' ἑζόμεν<b style='color:#980000'>οι</b> πολι<b style='color:#980000'>ὴ</b>ν <b style='color:#980000'>ἅ</b>λα τ<b style='color:#980000'>ύ</b>πτον ἐρετμ<b style='color:#980000'>οῖ</b>ς.",
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
    quiz_renew_btn = gu._mo.ui.button(label="↺ Новый набор", on_click=lambda v: (v or 0) + 1)
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
def _(ag_backend, ag_byzantine, ag_homer, ag_lsj, ag_lxx, ag_morphgnt, gu):
    import csv
    from pathlib import Path

    _vocab_path = Path(__file__).parent / "vocab_IX_82-104.tsv"
    with open(_vocab_path, encoding="utf-8") as _f:
        QUIZ_WORDS_RAW = gu.resolve_word_grammar(
            list(csv.DictReader(_f, delimiter="\t")), ag_backend, "ru"
        )

    _POS_MAP = {"adj": "adjective"}
    _QUIZZABLE = {"noun", "verb", "adj", "pronoun"}
    _LEXICONS = [("homer", ag_homer), ("lsj", ag_lsj), ("lxx", ag_lxx), ("morphgnt", ag_morphgnt), ("byzantine", ag_byzantine)]

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

    _ = quiz_renew_btn.value
    set_cv(None)
    set_remaining(None)
    set_score({"correct": 0, "total": 0})
    set_history([])
    set_future([])
    set_restore_entry(None)
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
    NB_REMOTE = f"{cfg.raw_base}/2026_07_06"
    for _f in (
        'Od_IX_82-104.pdf',
        'Od_IX_82-104_vocabula.pdf',
        'map_ortelius.jpg',
        'map_ortelius_full.jpg',
        'lotus_plant.jpg',
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
