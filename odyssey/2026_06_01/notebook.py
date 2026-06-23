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

__generated_with = "0.23.10"
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
def _():
    import base64 as _b64
    from pathlib import Path as _Path

    _img_path = _Path(__file__).parent / "Odysseus_Sirens_BM_E440_n2.jpg"
    img_b64 = _b64.b64encode(_img_path.read_bytes()).decode()
    return (img_b64,)


@app.cell(hide_code=True)
def _(img_b64, mo):
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_32dyZq8gA6x14GL2Zwa6ZU)"
    _left = mo.vstack([
        mo.md("# Древнегреческий с Гомером"),
        mo.md(_badge),
        mo.md("## Пилотное занятие · Odyss. I.1–21"),
    ])
    _img = mo.Html(
        f'<a href="data:image/jpeg;base64,{img_b64}" target="_blank">'
        f'<img src="data:image/jpeg;base64,{img_b64}" '
        f'style="max-width:340px;width:100%;border-radius:4px;object-fit:cover;cursor:pointer"/>'
        f'</a>'
    )
    mo.hstack([_left, _img], align="start")
    return


@app.cell(hide_code=True)
def _(mo):
    _MURRAY = "<b>Homer.</b> <a href='https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3atext%3a1999.01.0135'><i>The Odyssey</i></a> with an English Translation by A.T. Murray, PH.D. in two volumes. Cambridge, MA., Harvard University Press; London, William Heinemann, Ltd. 1919."
    mo.md(
        "Текст поэмы с параллельными переводами. "
        "Икты (ударные слоги) каждой стопы выделены "
        "<b style='color:#980000'>красным</b>. "
        "Слова, известные движку eee, <u>подчёркнуты</u>.\n\n"
        + _MURRAY
    )
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(
        "**Материалы занятия:** "
        f"[Одиссея. Зачин.pdf]({NB_REMOTE}/Одиссея.%20Зачин.pdf) · "
        f"[Одиссея\_1-21\_словарь.pdf]({NB_REMOTE}/Одиссея_1-21_словарь.pdf) · "
        f"[Греческий алфавит.pdf]({NB_REMOTE}/Греческий%20алфавит.pdf)"
    )
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
def _(QUIZ_WORDS, STANZAS, mo, stanza_selector, trans_selector):
    _st_map = {s["ref"]: s for s in STANZAS}
    _stanza = _st_map[stanza_selector.value]

    _HIGHLIGHT = {q["form"] for q in QUIZ_WORDS}
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
            if _bare(w) in _HIGHLIGHT:
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
    mo.md("""
    ---
    ## Упражнение: словарная форма
    """)
    return


@app.cell(hide_code=True)
def _(QUIZ_WORDS, cv, mo, next_btn, score):
    _s = score()
    _n = _s['total'] + (1 if cv() is not None else 0)
    mo.hstack(
        [mo.md(f"Тесты: **{_n}** / {len(QUIZ_WORDS)}"),
         mo.Html('<div style="width:2rem"></div>'),
         next_btn],
        justify="start",
        align="center",
    )
    return


@app.cell(hide_code=True)
def _(QUIZ_WORDS, cv, gu, random):
    answer_radio, w = gu.word_quiz_question(cv(), QUIZ_WORDS, "ru", random)
    return answer_radio, w


@app.cell(hide_code=True)
def _(answer_radio, build_paradigm_table, gu, mo, score, w):
    mo.vstack([answer_radio,
               gu.word_quiz_feedback(w, answer_radio.value, score(), "ru",
                                     build_paradigm_table=build_paradigm_table)])
    return


@app.cell(hide_code=True)
def _(mo):
    cv, set_cv = mo.state(None)
    score, set_score = mo.state({"correct": 0, "total": 0})
    remaining, set_remaining = mo.state(None)
    return cv, remaining, score, set_cv, set_remaining, set_score


@app.cell(hide_code=True)
def _(QUIZ_WORDS, random, remaining, set_cv, set_remaining):
    if remaining() is None and QUIZ_WORDS:
        _shuffled = random.sample(QUIZ_WORDS, len(QUIZ_WORDS))
        set_cv(_shuffled[0])
        set_remaining(_shuffled[1:])
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
def _(cv, mo, remaining):
    _r = remaining()
    _done = cv() is None and _r is not None and len(_r) == 0
    next_btn = mo.ui.button(
        label="Начать сначала" if _done else "→ Следующее",
        on_click=lambda v: (v or 0) + 1,
    )
    return (next_btn,)


@app.cell(hide_code=True)
def _(
    QUIZ_WORDS,
    answer_radio,
    cv,
    next_btn,
    random,
    remaining,
    score,
    set_cv,
    set_remaining,
    set_score,
):
    def _record_answer():
        if answer_radio.value is not None and cv() is not None:
            s = score()
            set_score({
                "correct": s["correct"] + (1 if answer_radio.value == cv()["form"] else 0),
                "total": s["total"] + 1,
            })

    if next_btn.value:
        r = remaining()
        if r is None:
            pass
        elif r:
            _record_answer()
            set_cv(r[0])
            set_remaining(r[1:])
        else:
            if cv() is None:
                _shuffled = random.sample(QUIZ_WORDS, len(QUIZ_WORDS))
                set_cv(_shuffled[0])
                set_remaining(_shuffled[1:])
                set_score({"correct": 0, "total": 0})
            else:
                _record_answer()
                set_cv(None)
    return


@app.cell(hide_code=True)
def _():
    STANZAS = [
        {
            "ref": "I.1–5",
            "lines": [
                "Ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ",
                "πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν·",
                "πολλῶν δ' ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,",
                "πολλὰ δ' ὅ γ' ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,",
                "ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.",
            ],
            "interlinear": [
                ("Ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ",
                 "О муже мне расскажи, муза, о многостранном, который весьма много"),
                ("πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν·",
                 "скитался, когда Трои святую твердыню разрушил."),
                ("πολλῶν δ' ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,",
                 "Многих людей он видел города и ум узнал,"),
                ("πολλὰ δ' ὅ γ' ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,",
                 "много также он и на море претерпел страданий в своем духе,"),
                ("ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.",
                 "борясь и за свою душу, и за возвращение товарищей."),
            ],
            "translations": {
                "Жуковский": (
                    "Муза, скажи мне о том многоопытном муже, который,\n"
                    "Странствуя долго со дня, как святой Илион им разрушен,\n"
                    "Многих людей города посетил и обычаи видел,\n"
                    "Много и сердцем скорбел на морях, о спасенье заботясь\n"
                    "Жизни своей и возврате в отчизну сопутников; тщетны…"
                ),
                "Вересаев": (
                    "Муза, скажи мне о том многоопытном муже, который\n"
                    "Долго скитался с тех пор, как разрушил священную Трою,\n"
                    "Многих людей города посетил и обычаи видел,\n"
                    "Много духом страдал на морях, о спасеньи заботясь\n"
                    "Жизни своей и возврате в отчизну товарищей верных."
                ),
            },
        },
        {
            "ref": "I.6–10",
            "lines": [
                "ἀλλ' οὐδ' ὣς ἑτάρους ἐρρύσατο, ἱέμενός περ·",
                "αὐτῶν γὰρ σφετέρῃσιν ἀτασθαλίῃσιν ὄλοντο,",
                "νήπιοι, οἳ κατὰ βοῦς Ὑπερίονος Ἠελίοιο",
                "ἤσθιον· αὐτὰρ ὁ τοῖσιν ἀφείλετο νόστιμον ἦμαρ.",
                "τῶν ἁμόθεν γε, θεά, θύγατερ Διός, εἰπὲ καὶ ἡμῖν.",
            ],
            "interlinear": [
                ("ἀλλ' οὐδ' ὣς ἑτάρους ἐρρύσατο, ἱέμενός περ·",
                 "но и своих товарищей он не спас, хотя и стремился,"),
                ("αὐτῶν γὰρ σφετέρῃσιν ἀτασθαλίῃσιν ὄλοντο,",
                 "от их ведь собственных нечестий они погибли,"),
                ("νήπιοι, οἳ κατὰ βοῦς Ὑπερίονος Ἠελίοιο",
                 "неразумные, которые быков Гипериона Гелиоса"),
                ("ἤσθιον· αὐτὰρ ὁ τοῖσιν ἀφείλετο νόστιμον ἦμαρ.",
                 "пожрали, и был у них отнят возвратный день."),
                ("τῶν ἁμόθεν γε, θεά, θύγατερ Διός, εἰπὲ καὶ ἡμῖν.",
                 "Вот об этом откуда-нибудь, богиня, дочь Зевса, расскажи и нам."),
            ],
            "translations": {
                "Жуковский": (
                    "Были, однако, заботы, не спас он сопутников: сами\n"
                    "Гибель они на себя навлекли святотатством, безумцы,\n"
                    "Съевши быков Гелиоса, над нами ходящего бога, —\n"
                    "День возврата у них он похитил. Скажи же об этом\n"
                    "Что-нибудь нам, о Зевесова дочь, благосклонная Муза."
                ),
                "Вересаев": (
                    "Все же при этом не спас он товарищей, как ни старался.\n"
                    "Собственным сами себя святотатством они погубили:\n"
                    "Съели, безумцы, коров Гелиоса Гиперионида.\n"
                    "Дня возвращенья домой навсегда их за это лишил он.\n"
                    "Муза! Об этом и нам расскажи, начав с чего хочешь."
                ),
            },
        },
        {
            "ref": "I.11–15",
            "lines": [
                "Ἔνθ' ἄλλοι μὲν πάντες, ὅσοι φύγον αἰπὺν ὄλεθρον,",
                "οἴκοι ἔσαν, πόλεμόν τε πεφευγότες ἠδὲ θάλασσαν·",
                "τὸν δ' οἶον νόστου κεχρημένον ἠδὲ γυναικὸς",
                "νύμφη πόντι' ἔρυκε Καλυψὼ δῖα θεάων",
                "ἐν σπέσσι γλαφυροῖσι, λιλαιομένη πόσιν εἶναι.",
            ],
            "interlinear": [
                ("Ἔνθ' ἄλλοι μὲν πάντες, ὅσοι φύγον αἰπὺν ὄλεθρον,",
                 "Когда другие все, которые избежали стремительной гибели,"),
                ("οἴκοι ἔσαν, πόλεμόν τε πεφευγότες ἠδὲ θάλασσαν·",
                 "дома были, войны избежав и моря,"),
                ("τὸν δ' οἶον νόστου κεχρημένον ἠδὲ γυναικὸς",
                 "его одного, возвращения лишенного и жены,"),
                ("νύμφη πόντι' ἔρυκε Καλυψὼ δῖα θεάων",
                 "нимфа владычица держала Калипсо, славная среди богинь,"),
                ("ἐν σπέσσι γλαφυροῖσι, λιλαιομένη πόσιν εἶναι.",
                 "в пещерах глубоких, страстно желая, чтобы мужем он был."),
            ],
            "translations": {
                "Жуковский": (
                    "Все уж другие, погибели верной избегшие, были\n"
                    "Дома, избегнув и брани и моря; его лишь, разлукой\n"
                    "С милой женой и отчизной крушимого, в гроте глубоком\n"
                    "Светлая нимфа Калипсо, богиня богинь, произвольной\n"
                    "Силой держала, напрасно желая, чтоб был ей супругом."
                ),
                "Вересаев": (
                    "Все остальные в то время, избегнув погибели близкой,\n"
                    "Были уж дома, равно и войны избежавши и моря.\n"
                    "Только его, по жене и отчизне болевшего сердцем,\n"
                    "Нимфа-царица Калипсо, богиня в богинях, держала\n"
                    "В гроте глубоком, желая, чтоб сделался ей он супругом."
                ),
            },
        },
        {
            "ref": "I.16–21",
            "lines": [
                "ἀλλ' ὅτε δὴ ἔτος ἦλθε περιπλομένων ἐνιαυτῶν,",
                "τῷ οἱ ἐπεκλώσαντο θεοὶ οἰκόνδε νέεσθαι",
                "εἰς Ἰθάκην, οὐδ' ἔνθα πεφυγμένος ἦεν ἀέθλων",
                "καὶ μετὰ οἷσι φίλοισι. θεοὶ δ' ἐλέαιρον ἅπαντες",
                "νόσφι Ποσειδάωνος· ὁ δ' ἀσπερχὲς μενέαινεν",
                "ἀντιθέῳ Ὀδυσῆι πάρος ἥν γαῖαν ἱκέσθαι.",
            ],
            "interlinear": [
                ("ἀλλ' ὅτε δὴ ἔτος ἦλθε περιπλομένων ἐνιαυτῶν,",
                 "но когда уже год пришел, по обращении времен,"),
                ("τῷ οἱ ἐπεκλώσαντο θεοὶ οἰκόνδε νέεσθαι",
                 "в который ему назначили боги домой вернуться"),
                ("εἰς Ἰθάκην, οὐδ' ἔνθα πεφυγμένος ἦεν ἀέθλων",
                 "на Итаку, и даже там он не избег испытаний,"),
                ("καὶ μετὰ οἷσι φίλοισι. θεοὶ δ' ἐλέαιρον ἅπαντες",
                 "и со своими друзьями. А боги все смилостивились,"),
                ("νόσφι Ποσειδάωνος· ὁ δ' ἀσπερχὲς μενέαινεν",
                 "кроме Посейдона: он беспрерывно гневался"),
                ("ἀντιθέῳ Ὀδυσῆι πάρος ἥν γαῖαν ἱκέσθαι.",
                 "на богоравного Одиссея, пока он не прибыл на свою землю."),
            ],
            "translations": {
                "Жуковский": (
                    "Но когда наконец обращеньем времен приведен был\n"
                    "Год, в который ему возвратиться назначили боги\n"
                    "В дом свой, в Итаку (но где и в объятиях верных друзей он\n"
                    "Всё не избег от тревог), преисполнились жалостью боги\n"
                    "Все; Посейдон лишь единый упорствовал гнать Одиссея,\n"
                    "Богоподобного мужа, пока не достиг он отчизны."
                ),
                "Вересаев": (
                    "Но протекали года, и уж год наступил, когда было\n"
                    "Сыну Лаэрта богами назначено в дом свой вернуться.\n"
                    "Также, однако, и там, на Итаке, не мог избежать он\n"
                    "Многих трудов, хоть и был меж друзей. Сострадания полны\n"
                    "Были все боги к нему. Лишь один Посейдон непрерывно\n"
                    "Гнал Одиссея, покамест своей он земли не достигнул."
                ),
            },
        },
    ]
    return (STANZAS,)


@app.cell(hide_code=True)
def _():
    import csv
    from pathlib import Path

    _vocab_path = Path(__file__).parent / "vocab_I_1-21.tsv"
    with open(_vocab_path, encoding="utf-8") as _f:
        QUIZ_WORDS_RAW = list(csv.DictReader(_f, delimiter="\t"))
    return (QUIZ_WORDS_RAW,)


@app.cell(hide_code=True)
def _(QUIZ_WORDS_RAW, build_paradigm_table):
    def _has_displayable_form(w):
        try:
            result = build_paradigm_table(w)
            if not result:
                return False
            return "#f97316" not in result
        except Exception:
            return False

    _flags            = [_has_displayable_form(w) for w in QUIZ_WORDS_RAW]
    QUIZ_WORDS        = [w for w, ok in zip(QUIZ_WORDS_RAW, _flags) if ok]
    words_no_paradigm = [w for w, ok in zip(QUIZ_WORDS_RAW, _flags) if not ok]
    return (QUIZ_WORDS,)


@app.cell(hide_code=True)
def _(ag_backend, eee, um_backend):
    import unicodedata
    import functools

    def _norm_grc(s):
        _STRIP = {
            "̀","́","̂","̈",
            "̓","̔","̓","͂",
            "̄","̆",
        }
        s = unicodedata.normalize("NFD", s).lower()
        return unicodedata.normalize("NFC", "".join(c for c in s if c not in _STRIP))

    @functools.lru_cache(maxsize=None)
    def _ag_slots(pos):
        t = ag_backend.get_slot_templates("grc", pos, "ru")
        return {} if t is None else {s.tag: s for s in t}

    @functools.lru_cache(maxsize=None)
    def _um_noun_slots():
        t = um_backend.get_slot_templates("grc", "noun", "ru")
        return {} if t is None else {s.tag: s for s in t}

    _CL   = {"Nom": "Им.", "Gen": "Род.", "Dat": "Дат.", "Acc": "Вин.", "Voc": "Зват."}
    _NL   = ("Ед.", "Мн.")
    _TCOL = {"PAI": "Наст.", "IAI": "Имп.", "AAI": "Аор.", "AMI": "Аор. М.", "API": "Аор. П."}
    _PROW = {"1S": "1 ед.", "2S": "2 ед.", "3S": "3 ед.", "1P": "1 мн.", "2P": "2 мн.", "3P": "3 мн."}
    _INF_LBL = "Инф."
    _IMP_LBL = {"2S": "Пов. 2ед.", "2P": "Пов. 2мн."}

    def build_paradigm_table(w, lang="ru"):
        lemma, pos, tested = w["lemma"], w["pos"], w["form"]
        tn  = _norm_grc(tested)
        HL  = "background:#fef3c7;font-weight:bold;color:#92400e;padding:3px 10px;text-align:center;font-family:serif;"
        TD  = "padding:3px 10px;text-align:center;font-family:serif;"
        TH  = "padding:3px 8px;font-weight:600;border-bottom:1px solid #e5e7eb;color:#6b7280;font-size:.82em;text-align:center;"
        ROW = "padding:3px 8px;color:#9ca3af;font-size:.82em;text-align:right;"
        CAP = "font-size:.75em;color:#9ca3af;text-align:right;padding:2px 4px;"
        found = [False]

        def td(forms):
            hl = any(_norm_grc(f.replace("(ν)", "ν")) == tn for f in forms)
            if hl:
                found[0] = True
            return f'<td style="{HL if hl else TD}">{"/ ".join(sorted(forms)) if forms else chr(8212)}</td>'

        if pos == "noun":
            ag_nmap = _ag_slots("noun")
            sg_lbl, pl_lbl = _NL

            ag_rows = {}
            for c in ["N", "G", "D", "A", "V"]:
                for n in ("S", "P"):
                    forms = set()
                    for g in "MFN":
                        slot = ag_nmap.get(f".{c}{n}{g}")
                        if slot:
                            forms |= eee.inflect_slot(lemma, slot, "noun", language="grc", backend="ancient-greek")
                    ag_rows[(c, n)] = forms

            _ag_has = any(ag_rows.values())
            be_lbl = "ancient-greek" if _ag_has else "unimorph"
            tbl = f'<table style="border-collapse:collapse;font-size:.95em;margin-top:8px"><caption style="{CAP}">{be_lbl}</caption><tr><th style="{TH}"></th><th style="{TH}">{sg_lbl}</th><th style="{TH}">{pl_lbl}</th></tr>'

            if _ag_has:
                for c in ["N", "G", "D", "A", "V"]:
                    case_key = {"N": "Nom", "G": "Gen", "D": "Dat", "A": "Acc", "V": "Voc"}[c]
                    tbl += f'<tr><td style="{ROW}">{_CL.get(case_key, c)}</td>'
                    for n in ("S", "P"):
                        tbl += td(ag_rows[(c, n)])
                    tbl += "</tr>"
            else:
                um_nmap = _um_noun_slots()
                _UM_CASES = [("NOM", "Nom"), ("GEN", "Gen"), ("DAT", "Dat"), ("ACC", "Acc"), ("VOC", "Voc")]
                for c, case_key in _UM_CASES:
                    tbl += f'<tr><td style="{ROW}">{_CL.get(case_key, c)}</td>'
                    for ns in ("SG", "PL"):
                        slot = um_nmap.get(f"N;{c};{ns}")
                        forms = eee.inflect_slot(lemma, slot, "noun", language="grc", backend="unimorph") if slot else set()
                        tbl += td(forms)
                    tbl += "</tr>"

            tbl += "</table>"

        elif pos == "verb":
            slot_map = _ag_slots("verb")
            PS_TAGS = ["1S", "2S", "3S", "1P", "2P", "3P"]

            _vcache = {}
            def _vf(tag):
                if tag not in _vcache:
                    slot = slot_map.get(tag)
                    _vcache[tag] = (
                        eee.inflect_slot(lemma, slot, "verb", language="grc", backend="ancient-greek")
                        if slot else set()
                    )
                return _vcache[tag]

            TENSES = [(t, _TCOL.get(t, t)) for t in ["PAI", "IAI", "AAI", "AMI", "API"]
                      if any(_vf(f"{t}.{ps}") for ps in PS_TAGS)]
            if not TENSES:
                return None

            tbl = f'<table style="border-collapse:collapse;font-size:.95em;margin-top:8px"><caption style="{CAP}">ancient-greek</caption><tr><th style="{TH}"></th>'
            tbl += "".join(f'<th style="{TH}">{lbl}</th>' for _, lbl in TENSES) + "</tr>"
            for ps in PS_TAGS:
                tbl += f'<tr><td style="{ROW}">{_PROW.get(ps, ps)}</td>'
                for t, _ in TENSES:
                    tbl += td(_vf(f"{t}.{ps}"))
                tbl += "</tr>"

            INF_MAP = {"PAI": "PAN", "IAI": "IAN", "AAI": "AAN", "AMI": "AMN", "API": "APN"}
            if any(_vf(INF_MAP.get(t, "")) for t, _ in TENSES):
                tbl += f'<tr><td style="{ROW}">{_INF_LBL}</td>'
                for t, _ in TENSES:
                    tbl += td(_vf(INF_MAP.get(t, "")))
                tbl += "</tr>"

            IMP_MAP = {"PAI": "PAD", "AAI": "AAD", "AMI": "AMD"}
            for imp_ps, imp_sfx in [("2S", ".2S"), ("2P", ".2P")]:
                if any(_vf(f"{IMP_MAP[t]}{imp_sfx}") for t, _ in TENSES if t in IMP_MAP):
                    tbl += f'<tr><td style="{ROW}">{_IMP_LBL.get(imp_ps, imp_ps)}</td>'
                    for t, _ in TENSES:
                        imp_t = IMP_MAP.get(t)
                        tbl += td(_vf(f"{imp_t}{imp_sfx}")) if imp_t else f'<td style="{TD}">—</td>'
                    tbl += "</tr>"

            tbl += "</table>"
        else:
            return None

        if not found[0]:
            NOTE = "background:#fff7ed;border-left:3px solid #f97316;padding:7px 12px;margin-top:8px;font-size:.9em;color:#7c2d12;"
            note = f'<div style="{NOTE}"><b>{tested}</b> — нерегулярная форма, отсутствует в парадигме {lemma}</div>'
            return note + tbl
        return tbl

    return (build_paradigm_table,)


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import random
    import eee_project as eee
    from ancient_greek_backend_eee import AncientGreekBackend
    from unimorph_backend_eee import UniMorphBackend

    ag_backend = AncientGreekBackend(lexicons=["homer", "lxx", "morphgnt"])
    um_backend = UniMorphBackend(language="grc")
    eee.register_backend("grc", ag_backend, backend="ancient-greek")
    eee.register_backend("grc", um_backend, backend="unimorph")
    eee.set_chain("grc", ["ancient-greek", "unimorph"])
    gu = eee.GreekUtils(mo_module=mo)
    return ag_backend, eee, gu, mo, random, um_backend


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
    return (NB_REMOTE,)


if __name__ == "__main__":
    app.run()
