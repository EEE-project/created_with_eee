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

__generated_with = "0.23.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _TITLE = {
        "ru": "Древнегреческий с Гомером",
        "en": "Ancient Greek with Homer",
        "el": "Αρχαία Ελληνικά με τον Όμηρο",
    }
    _t = _TITLE.get(lang_sel.value, _TITLE["en"])
    _b = f"◀ {_t}"
    mo.Html(f'''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;700;800&display=swap');
    #eee-topbar {{
      position: sticky; top: 0; z-index: 100;
      height: 48px; background: #f5f5f5;
      border-bottom: 2px solid #003d82;
      display: flex; align-items: center;
      padding: 0 12px; gap: 10px;
      margin: -16px -16px 16px -16px;
      font-family: Syne, sans-serif;
    }}
    #eee-topbar .tb-back {{
      font-size: 15px; font-weight: 700; letter-spacing: 0.02em;
      color: #003d82; text-decoration: none;
      padding: 4px 6px; flex: 1;
      white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }}
    #eee-topbar .tb-badge {{
      font-family: "DM Mono", monospace; font-size: 12px; font-weight: 700;
      color: #003d82; background: rgba(0,61,130,0.08);
      border: 1px solid rgba(0,61,130,0.3); border-radius: 4px;
      padding: 4px 8px; letter-spacing: 0.1em; text-decoration: none; flex-shrink: 0;
    }}
    </style>
    <div id="eee-topbar">
      <a class="tb-back" href="https://eee-project.codeberg.page/created_with_eee/odyssey/">{_b}</a>
      <a class="tb-badge" href="https://t.me/+VuocC5la3ZwyNDky" target="_blank">EEE Community</a>
    </div>
    ''')
    return


@app.cell(hide_code=True)
def _():
    import base64 as _b64
    from pathlib import Path as _Path

    _img_path = _Path(__file__).parent / "Odysseus_Sirens_BM_E440_n2.jpg"
    img_b64 = _b64.b64encode(_img_path.read_bytes()).decode()
    return (img_b64,)


@app.cell(hide_code=True)
def _(img_b64, lang_sel, mo):
    _lang = lang_sel.value
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_32dyZq8gA6x14GL2Zwa6ZU)"
    _TITLE = {
        "ru": "Древнегреческий с Гомером",
        "en": "Ancient Greek with Homer",
        "el": "Αρχαία Ελληνικά με τον Όμηρο",
    }
    _LESSON = {
        "ru": "Пилотное занятие · Odyss. I.1–21",
        "en": "Pilot Lesson · Odyss. I.1–21",
        "el": "Δοκιμαστικό μάθημα · Οδ. Α.1–21",
    }
    _left = mo.vstack([
        mo.md(f"# {_TITLE.get(_lang, _TITLE['en'])}"),
        mo.md(_badge),
        mo.md(f"## {_LESSON.get(_lang, _LESSON['en'])}"),
    ])
    _img = mo.Html(
        f'<img src="data:image/jpeg;base64,{img_b64}" '
        f'style="max-width:340px;width:100%;border-radius:4px;object-fit:cover"/>'
    )
    mo.hstack([_left, _img], align="start")
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _lang = lang_sel.value
    _DESC = {
        "ru": "Текст поэмы с параллельными переводами. Слова, известные движку **eee** (базы `ancient-greek` и `unimorph grc`), выделены <span style='color:#b5451b;font-weight:bold'>цветом</span>.",
        "en": "Poem text with parallel translations. Words known to the **eee** engine (backends `ancient-greek` and `unimorph grc`) are highlighted <span style='color:#b5451b;font-weight:bold'>in color</span>.",
        "el": "Κείμενο με παράλληλες μεταφράσεις. Λέξεις γνωστές στη μηχανή **eee** (βάσεις `ancient-greek` και `unimorph grc`) επισημαίνονται <span style='color:#b5451b;font-weight:bold'>με χρώμα</span>.",
    }
    mo.md(_DESC.get(_lang, _DESC["en"]))
    return


@app.cell(hide_code=True)
def _(lang_sel, mo, trans_selector):
    _lang = lang_sel.value
    _ILN_DESC = {
        "ru": "**подстрочник** · буквальный перевод слово-в-слово с сохранением порядка оригинала",
        "en": "**interlinear** · word-for-word literal translation preserving original word order",
        "el": "**λέξη-λέξη** · κατά λέξη μετάφραση με διατήρηση της σειράς του πρωτοτύπου",
    }
    _TRANS_DESC = {
        "подстрочник":          _ILN_DESC.get(_lang, _ILN_DESC["ru"]),
        "Жуковский":            "**Жуковский, 1849** · рус., белый стих (пятистопный ямб) · романтический возвышенный стиль · первый классический стихотворный перевод на русский",
        "Вересаев":             "**Вересаев, 1953** · рус., проза · ясный современный язык · ориентирован на смысловую точность · стандартный учебный перевод",
        "Pope":                 "**Pope, 1725–26** · eng., heroic couplets · elegant 18th-c. rhetorical style · poetic adaptation; long considered the standard English version",
        "Lattimore":            "**Lattimore, 1951** · eng., blank verse · restrained academic style · closest to literal among English translations; standard for philological study",
        "Πολυλάς":              "**Πολυλάς, 1875** · ν.ε., Καθαρεύουσα · κανονική νεοελληνική μετάφραση του 19ου αι. · κλασικό λογοτεχνικό ύφος",
        "Καζαντζάκης–Κακριδής": "**Καζαντζάκης–Κακριδής, 1965** · ν.ε., Δημοτική · καλλιτεχνική (Καζαντζάκης) + επιστημονική (Κακριδής) · σύγχρονη γλώσσα",
    }
    mo.md(_TRANS_DESC.get(trans_selector.value, ""))
    return


@app.cell(hide_code=True)
def _(
    QUIZ_WORDS,
    STANZAS,
    interlinear_el,
    interlinear_en,
    lang_sel,
    mo,
    stanza_selector,
    trans_selector,
):
    # ── Parallel text display ────────────────────────────────────────────────────
    from itertools import zip_longest as _zip_longest
    _lang = lang_sel.value
    _st_map = {s["ref"]: s for s in STANZAS}
    _stanza = _st_map[stanza_selector.value]

    _HIGHLIGHT = {q["form"] for q in QUIZ_WORDS}
    _GRK = (
        "font-family:'Gentium Plus','GFS Didot',serif;"
        "font-size:1.15em;line-height:2"
    )

    def _hl(line):
        return " ".join(
            f'<span style="color:#b5451b;font-weight:600">{w}</span>'
            if w.strip("·,;.'") in _HIGHLIGHT else w
            for w in line.split()
        )

    if trans_selector.value == "подстрочник":
        if _lang == "el":
            _el_lines = interlinear_el.get(_stanza["ref"], [])
            _pairs = list(_zip_longest(_stanza["lines"], _el_lines, fillvalue=""))
        elif _lang == "en":
            _pairs = interlinear_en.get(_stanza["ref"], [])
        else:
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
def _(lang_sel, mo):
    _lang = lang_sel.value
    _HEAD = {
        "ru": "## Упражнение: словарная форма",
        "en": "## Exercise: dictionary form",
        "el": "## Άσκηση: λεξικός τύπος",
    }
    mo.md(f"""
    ---
    {_HEAD.get(_lang, _HEAD["en"])}
    """)
    return


@app.cell(hide_code=True)
def _(QUIZ_WORDS, cv, lang_sel, mo, next_btn, score):
    _s = score()
    _n = _s['total'] + (1 if cv() is not None else 0)
    _lang = lang_sel.value
    _LBL = {"ru": "Тесты:", "en": "Cards:", "el": "Κάρτες:"}
    mo.hstack(
        [mo.md(f"{_LBL.get(_lang, 'Tests:')} **{_n}** / {len(QUIZ_WORDS)}"),
         mo.Html('<div style="width:2rem"></div>'),
         next_btn],
        justify="start",
        align="center",
    )
    return


@app.cell(hide_code=True)
def _(QUIZ_WORDS, cv, gu, lang_sel, random):
    answer_radio, w = gu.word_quiz_question(cv(), QUIZ_WORDS, lang_sel.value, random)
    return answer_radio, w


@app.cell(hide_code=True)
def _(answer_radio, build_paradigm_table, gu, lang_sel, mo, score, w):
    mo.vstack([answer_radio,
               gu.word_quiz_feedback(w, answer_radio.value, score(), lang_sel.value,
                                     build_paradigm_table=build_paradigm_table)])


@app.cell(hide_code=True)
def _():
    class _Sel:
        value = "el"
    lang_sel = _Sel()
    return (lang_sel,)


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
def _(lang_sel, mo):
    _lang = lang_sel.value
    _ILN  = {"ru": "подстрочник", "en": "interlinear", "el": "λέξη-λέξη"}
    _ALL = {
        _ILN.get(_lang, "подстрочник"):                   "подстрочник",
        "Жуковский (1849) · рус., классический":           "Жуковский",
        "Вересаев (1953) · рус., точный":                 "Вересаев",
        "Pope (1725) · eng., classical":                  "Pope",
        "Lattimore (1951) · eng., literal":               "Lattimore",
        "Πολυλάς (1875) · ν.ε., κλασική":                "Πολυλάς",
        "Καζαντζάκης–Κακριδής (1965) · ν.ε., σύγχρονη":  "Καζαντζάκης–Κακριδής",
    }
    _LANG_VALS = {
        "ru": {"подстрочник", "Жуковский", "Вересаев"},
        "en": {"подстрочник", "Pope", "Lattimore"},
        "el": {"подстрочник", "Πολυλάς", "Καζαντζάκης–Κακριδής"},
    }
    _LANG_DEF  = {"ru": "подстрочник", "en": "подстрочник", "el": "подстрочник"}
    _TRANS_LBL = {"ru": "Перевод", "en": "Translation", "el": "Μετάφραση"}
    _valid  = _LANG_VALS.get(_lang, _LANG_VALS["ru"])
    _opts   = {k: v for k, v in _ALL.items() if v in _valid}
    _def_v  = _LANG_DEF.get(_lang, "подстрочник")
    _def_k  = next((k for k, v in _opts.items() if v == _def_v), list(_opts.keys())[0])
    trans_selector = mo.ui.dropdown(
        options=_opts,
        value=_def_k,
        label=_TRANS_LBL.get(_lang, "Translation"),
    )
    return (trans_selector,)


@app.cell(hide_code=True)
def _(cv, lang_sel, mo, remaining):
    _r = remaining()
    _done = cv() is None and _r is not None and len(_r) == 0
    _lang = lang_sel.value
    _NEXT = {"ru": "→ Следующее", "en": "→ Next", "el": "→ Επόμενο"}
    _REST = {"ru": "Начать сначала", "en": "Start over", "el": "Αρχή"}
    next_btn = mo.ui.button(
        label=_REST.get(_lang, "→") if _done else _NEXT.get(_lang, "→"),
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
            pass  # not yet initialized
        elif r:
            _record_answer()
            set_cv(r[0])
            set_remaining(r[1:])
        else:
            if cv() is None:
                # done state → restart
                _shuffled = random.sample(QUIZ_WORDS, len(QUIZ_WORDS))
                set_cv(_shuffled[0])
                set_remaining(_shuffled[1:])
                set_score({"correct": 0, "total": 0})
            else:
                # last word → score and transition to done
                _record_answer()
                set_cv(None)
    return


@app.cell(hide_code=True)
def _():
    # ── Text data ──────────────────────────────────────────────────────────────
    # interlinear: list of (greek_line, russian_line) pairs
    # translations: literary translations keyed by name

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
                "Lattimore": (
                    "Tell me, Muse, of the man of many ways, who was driven\n"
                    "far journeys, after he had sacked Troy's sacred citadel.\n"
                    "Many were they whose cities he saw, whose minds he learned of,\n"
                    "many the pains he suffered in his spirit on the wide sea,\n"
                    "struggling for his own life and the homecoming of his companions."
                ),
                "Pope": (
                    "The man, for wisdom's various arts renown'd,\n"
                    "Long exercis'd in woes, O Muse! resound;\n"
                    "Who, when his arms had wrought the destin'd fall\n"
                    "Of sacred Troy, and raz'd her heav'n-built wall,\n"
                    "Wand'ring from clime to clime, observant stray'd,\n"
                    "Their manners noted, and their states survey'd,\n"
                    "On stormy seas unnumber'd toils he bore,\n"
                    "Safe with his friends to gain his natal shore."
                ),
                "Πολυλάς": (
                    "Πες μου, θεά, τ' ἀνδρὸς τὸν πολύτροπον, ὅπου πλανήθη τόσο\n"
                    "ἀφότου τῆς Τροίας τὸ ἱερὸ κάστρο χάλασε·\n"
                    "πολλῶν ἀνθρώπων τὰ ἄστη εἶδε κι ἔγνωσε τὸν νοῦ τους,\n"
                    "πολλὰ κι ἔπαθε στὴ θάλασσα ἀλγέα μέσα στὴν ψυχή του,\n"
                    "παλεύοντας γιὰ τὴ ζωή του καὶ γιὰ τὸ νόστο τῶν ἑταίρων."
                ),
                "Καζαντζάκης–Κακριδής": (
                    "Πές μου, Μούσα, γιὰ τὸν ἄντρα τὸν πολύτροπο, ποὺ πλανήθηκε πολύ,\n"
                    "ἀφότου τῆς Τροίας τὴν ἱερὴ πολιτεία χάλασε·\n"
                    "πολλῶν ἀνθρώπων τὰ ἄστη εἶδε καὶ ἔμαθε τὴ σκέψη τους,\n"
                    "πολλὰ ἔπαθε στὴ θάλασσα ἀλγέα στὰ βάθη τῆς ψυχῆς του,\n"
                    "παλεύοντας γιὰ τὴ ζωή του καὶ γιὰ τὸν γυρισμὸ τῶν συντρόφων."
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
                    "тщетны\n"
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
                "Lattimore": (
                    "Even so he could not save his companions, hard though\n"
                    "he strove to; they were destroyed by their own wild recklessness,\n"
                    "fools, who devoured the oxen of Helios, the Sun God,\n"
                    "and he took away the day of their homecoming.\n"
                    "From some point here, goddess, daughter of Zeus, speak, and begin our story."
                ),
                "Pope": (
                    "Vain toils! their impious folly dar'd to prey\n"
                    "On herds devoted to the god of day;\n"
                    "The god vindictive doom'd them then to die,\n"
                    "For sacrilegious crimes — nor could his care\n"
                    "Preserve from death a race of men so bold.\n"
                    "Begin from hence, and all the truth unfold."
                ),
                "Πολυλάς": (
                    "Μὰ μήτε ὡς τόσο τοὺς ἑταίρους του ἔσωσε, ποὺ τόσο φιλοτιμήθη·\n"
                    "γιατὶ χάθηκαν ἀπὸ τὴ δική τους τὴν ἀτασθαλία,\n"
                    "νήπιοι, ποὺ τοῦ Ἡλίου Ὑπερίωνα τοὺς βόες ἔφαγαν·\n"
                    "κι αὐτὸς τοὺς ἀφαίρεσε τὴν ἡμέρα τοῦ γυρισμοῦ.\n"
                    "Ἀπ' ὁπουδήποτε, θεά, κόρη τοῦ Δία, πές μας κι ἐμᾶς."
                ),
                "Καζαντζάκης–Κακριδής": (
                    "Μὰ μήτε ἔτσι τοὺς συντρόφους του τοὺς ἔσωσε, κι ἄς ποθοῦσε·\n"
                    "γιατὶ χάθηκαν ἀπ' τὴν τρέλα τους,\n"
                    "ἀνόητοι, ποὺ τοῦ Ἡλίου τοῦ Ὑπερίωνα τὰ βόδια ἔφαγαν·\n"
                    "κι ἐκεῖνος τοὺς ἀφαίρεσε τὴ μέρα τοῦ γυρισμοῦ.\n"
                    "Ἀπ' ὁπουδήποτε, θεά, κόρη τοῦ Δία, πές μας κι ἐμᾶς."
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
                "Lattimore": (
                    "So now all the others, as many as fled sheer destruction,\n"
                    "were at home, having escaped both the sea and the fighting;\n"
                    "but he alone, longing for his wife and his homecoming,\n"
                    "was detained by the queenly nymph Calypso, a goddess,\n"
                    "in her hollow caverns, desiring that he be her husband."
                ),
                "Pope": (
                    "Now all the rest who 'scap'd the cruel fate\n"
                    "In safety reach'd their long-desir'd retreat.\n"
                    "Him, yet alone from Ithaca detain'd,\n"
                    "Calypso long in her soft arms contain'd;\n"
                    "Who, in her grottoes, fond of him remain'd,\n"
                    "Desiring, fain would make the hero stay."
                ),
                "Πολυλάς": (
                    "Ἐκεῖ οἱ ἄλλοι ὅλοι, ὅσοι γλύτωσαν τὸν αἰπὺν ὄλεθρο,\n"
                    "ἦταν στὸ σπίτι, τὸν πόλεμο καὶ τὴ θάλασσα γλυτώσαντες·\n"
                    "αὐτὸν μόνον, ποὺ λαχταροῦσε νόστο καὶ γυναίκα,\n"
                    "νύμφη ἡ πότνια τὸν κρατοῦσε, ἡ Καλυψώ, θεία στὶς θεές,\n"
                    "στὶς κοίλες σπηλιές, ποθώντας νὰ τὴν πάρει γιὰ ἄντρα της."
                ),
                "Καζαντζάκης–Κακριδής": (
                    "Τότ' ἄλλοι μὲν ὅλοι, ὅσοι γλύτωσαν τὸν ἀπόκρημνο χαμό,\n"
                    "ἦταν στὰ σπίτια τους, καὶ πόλεμο καὶ θάλασσα γλυτωμένοι·\n"
                    "αὐτὸν μόνο, ποὺ ποθοῦσε νόστο καὶ γυναίκα,\n"
                    "ἡ νύμφη ἡ πότνια τὸν κρατοῦσε, ἡ Καλυψώ, ἡ θεϊκὴ θεά,\n"
                    "σὲ κοῖλες σπηλιές, λαχταρώντας νὰ τὴν κάνει ἄντρα της."
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
                "Lattimore": (
                    "But when in the circling of the years that very year came\n"
                    "in which the gods had spun for him his time of homecoming\n"
                    "to Ithaca, not even then was he free of his trials,\n"
                    "not even among his own people. All the gods pitied him\n"
                    "except Poseidon; he remained relentlessly angry\n"
                    "with godlike Odysseus, until he reached his own country."
                ),
                "Pope": (
                    "But when the years, by great Jove's sister's will,\n"
                    "Had fill'd their number on the rolling year,\n"
                    "When Ithaca at last was destin'd nigh,\n"
                    "New toils await him, and new dangers nigh.\n"
                    "The gods relent, and all except the god\n"
                    "Of ocean, who relentless still pursu'd\n"
                    "With hatred fierce divine Ulysses' way,\n"
                    "Till safe he landed on his native shore."
                ),
                "Πολυλάς": (
                    "Μὰ ὅταν πέρασαν τὰ χρόνια κι ἦρθε ἐκεῖνο τὸ ἔτος,\n"
                    "ποὺ οἱ θεοὶ τοῦ ἔκλωσαν νὰ γυρίσει στὸ σπίτι του,\n"
                    "στὴν Ἰθάκη, μήτε ἐκεῖ γλύτωσε τοὺς ἄθλους\n"
                    "μέσα στοὺς δικούς του. Οἱ θεοὶ τὸν λυπήθηκαν ὅλοι,\n"
                    "ἐκτὸς ἀπὸ τὸν Ποσειδῶνα· αὐτὸς ἀδιάκοπα ὀργιζόταν\n"
                    "στὸν ἰσόθεο Ὀδυσσέα, ὣς νὰ φτάσει στὴ γῆ του."
                ),
                "Καζαντζάκης–Κακριδής": (
                    "Μὰ ὅταν κύλησαν τὰ χρόνια κι ἦρθε τὸ χρόνο ἐκεῖνο,\n"
                    "ποὺ οἱ θεοὶ τοῦ ἔγνεσαν νὰ πάει σπίτι του,\n"
                    "στὴν Ἰθάκη, μήτ' ἐκεῖ ξέφυγε τοὺς πόνους\n"
                    "κι ἀνάμεσα στοὺς δικούς του. Τὸν λυπήθηκαν ὅλοι οἱ θεοί,\n"
                    "μόνο ὄχι ὁ Ποσειδῶνας· αὐτὸς ἀδιάλειπτα μανιόταν\n"
                    "ἐναντίον τοῦ ἰσόθεου Ὀδυσσέα, ὣς νὰ φτάσει στὸ χῶμα του."
                ),
            },
        },
    ]
    return (STANZAS,)


@app.cell(hide_code=True)
def _():
    # ── Quiz data ──────────────────────────────────────────────────────────────
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
            result = build_paradigm_table(w, lang="en")
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
def _():
    from pathlib import Path as _Path

    _md = (_Path(__file__).parent / "interlenear_en.md").read_text(encoding="utf-8")

    # Parse pairs: **greek** then english translation
    interlinear_en = {}
    _ref = None
    _grc = None
    _pairs = []
    for _line in _md.splitlines():
        if _line.startswith("### Odyss. "):
            if _ref and _pairs:
                interlinear_en[_ref] = _pairs
            _ref = _line.replace("### Odyss. ", "").strip()
            _pairs = []
            _grc = None
        elif _line.startswith("**") and _line.endswith("**"):
            _grc = _line[2:-2].strip()
        elif _line.strip() and _grc is not None:
            _pairs.append((_grc, _line.strip()))
            _grc = None

    if _ref and _pairs:
        interlinear_en[_ref] = _pairs
    return (interlinear_en,)


@app.cell(hide_code=True)
def _():
    from pathlib import Path as _Path
    from itertools import zip_longest as _zip_longest

    _md = (_Path(__file__).parent / "interlenear_el.md").read_text(encoding="utf-8")

    # Split into stanza blocks by "---" and "### Οδύσσεια" headers
    interlinear_el = {}
    _ref = None
    _buf = []
    _paras = []

    for _line in _md.splitlines():
        if _line.startswith("### Οδύσσεια"):
            # save any open paragraph
            if _buf:
                _paras.append(" ".join(_buf))
                _buf = []
            # save current stanza
            if _ref and _paras:
                interlinear_el[_ref] = _paras
            # start new stanza
            _raw = _line.replace("### Οδύσσεια Α΄ ", "").strip()
            _ref = "I." + _raw
            _paras = []
        elif _line.startswith("---") or _line.startswith("### ") or _line.startswith("|"):
            # divider or notes section — close current stanza
            if _buf:
                _paras.append(" ".join(_buf))
                _buf = []
            if _ref and _paras:
                interlinear_el[_ref] = _paras
            _ref = None
            _paras = []
            _buf = []
        elif _ref and _line.strip():
            _buf.append(_line.strip())
        elif not _line.strip() and _buf:
            _paras.append(" ".join(_buf))
            _buf = []

    if _ref:
        if _buf:
            _paras.append(" ".join(_buf))
        if _paras:
            interlinear_el[_ref] = _paras
    return (interlinear_el,)


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
    def _ag_slots(pos, lang):
        t = ag_backend.get_slot_templates("grc", pos, lang)
        return {} if t is None else {s.tag: s for s in t}

    @functools.lru_cache(maxsize=None)
    def _um_noun_slots(lang):
        t = um_backend.get_slot_templates("grc", "noun", lang)
        return {} if t is None else {s.tag: s for s in t}

    _CL = {
        "ru": {"Nom": "Им.", "Gen": "Род.", "Dat": "Дат.", "Acc": "Вин.", "Voc": "Зват."},
        "en": {"Nom": "Nom.", "Gen": "Gen.", "Dat": "Dat.", "Acc": "Acc.", "Voc": "Voc."},
        "el": {"Nom": "Ον.", "Gen": "Γεν.", "Dat": "Δοτ.", "Acc": "Αιτ.", "Voc": "Κλ."},
    }
    _NL = {
        "ru": ("Ед.", "Мн."),
        "en": ("Sg.", "Pl."),
        "el": ("Εν.", "Πλ."),
    }
    _TCOL = {
        "ru": {"PAI": "Наст.", "IAI": "Имп.", "AAI": "Аор.", "AMI": "Аор. М.", "API": "Аор. П."},
        "en": {"PAI": "Pres.", "IAI": "Impf.", "AAI": "Aor.", "AMI": "Aor. M.", "API": "Aor. P."},
        "el": {"PAI": "Ενεστ.", "IAI": "Παρατ.", "AAI": "Αορ.", "AMI": "Αορ. Μ.", "API": "Αορ. Π."},
    }
    _PROW = {
        "ru": {"1S": "1 ед.", "2S": "2 ед.", "3S": "3 ед.", "1P": "1 мн.", "2P": "2 мн.", "3P": "3 мн."},
        "en": {"1S": "1 sg.", "2S": "2 sg.", "3S": "3 sg.", "1P": "1 pl.", "2P": "2 pl.", "3P": "3 pl."},
        "el": {"1S": "1 εν.", "2S": "2 εν.", "3S": "3 εν.", "1P": "1 πλ.", "2P": "2 πλ.", "3P": "3 πλ."},
    }
    _INF_LBL = {"ru": "Инф.", "en": "Inf.", "el": "Απρφ."}
    _IMP_LBL = {
        "ru": {"2S": "Пов. 2ед.", "2P": "Пов. 2мн."},
        "en": {"2S": "Imp. 2sg.", "2P": "Imp. 2pl."},
        "el": {"2S": "Προστ. 2εν.", "2P": "Προστ. 2πλ."},
    }

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

        _SUPPL = {
            "ru": f"нерегулярная форма, отсутствует в парадигме {lemma}",
            "en": f"irregular form, not in the standard paradigm of {lemma}",
            "el": f"ανώμαλος τύπος, λείπει από το παράδειγμα του {lemma}",
        }

        if pos == "noun":
            ag_nmap = _ag_slots("noun", lang)
            cl = _CL.get(lang, _CL["en"])
            sg_lbl, pl_lbl = _NL.get(lang, _NL["en"])

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
                    tbl += f'<tr><td style="{ROW}">{cl.get(case_key, c)}</td>'
                    for n in ("S", "P"):
                        tbl += td(ag_rows[(c, n)])
                    tbl += "</tr>"
            else:
                um_nmap = _um_noun_slots(lang)
                _UM_CASES = [("NOM", "Nom"), ("GEN", "Gen"), ("DAT", "Dat"), ("ACC", "Acc"), ("VOC", "Voc")]
                for c, case_key in _UM_CASES:
                    tbl += f'<tr><td style="{ROW}">{cl.get(case_key, c)}</td>'
                    for ns in ("SG", "PL"):
                        slot = um_nmap.get(f"N;{c};{ns}")
                        forms = eee.inflect_slot(lemma, slot, "noun", language="grc", backend="unimorph") if slot else set()
                        tbl += td(forms)
                    tbl += "</tr>"

            tbl += "</table>"

        elif pos == "verb":
            slot_map = _ag_slots("verb", lang)
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

            tcol = _TCOL.get(lang, _TCOL["en"])
            prow = _PROW.get(lang, _PROW["en"])

            TENSES = [(t, tcol.get(t, t)) for t in ["PAI", "IAI", "AAI", "AMI", "API"]
                      if any(_vf(f"{t}.{ps}") for ps in PS_TAGS)]
            if not TENSES:
                return None

            tbl = f'<table style="border-collapse:collapse;font-size:.95em;margin-top:8px"><caption style="{CAP}">ancient-greek</caption><tr><th style="{TH}"></th>'
            tbl += "".join(f'<th style="{TH}">{lbl}</th>' for _, lbl in TENSES) + "</tr>"
            for ps in PS_TAGS:
                tbl += f'<tr><td style="{ROW}">{prow.get(ps, ps)}</td>'
                for t, _ in TENSES:
                    tbl += td(_vf(f"{t}.{ps}"))
                tbl += "</tr>"

            INF_MAP = {"PAI": "PAN", "IAI": "IAN", "AAI": "AAN", "AMI": "AMN", "API": "APN"}
            if any(_vf(INF_MAP.get(t, "")) for t, _ in TENSES):
                tbl += f'<tr><td style="{ROW}">{_INF_LBL.get(lang, "Inf.")}</td>'
                for t, _ in TENSES:
                    tbl += td(_vf(INF_MAP.get(t, "")))
                tbl += "</tr>"

            IMP_MAP = {"PAI": "PAD", "AAI": "AAD", "AMI": "AMD"}
            for imp_ps, imp_sfx in [("2S", ".2S"), ("2P", ".2P")]:
                if any(_vf(f"{IMP_MAP[t]}{imp_sfx}") for t, _ in TENSES if t in IMP_MAP):
                    tbl += f'<tr><td style="{ROW}">{_IMP_LBL.get(lang, _IMP_LBL["en"]).get(imp_ps, imp_ps)}</td>'
                    for t, _ in TENSES:
                        imp_t = IMP_MAP.get(t)
                        tbl += td(_vf(f"{imp_t}{imp_sfx}")) if imp_t else f'<td style="{TD}">—</td>'
                    tbl += "</tr>"

            tbl += "</table>"
        else:
            return None

        if not found[0]:
            NOTE = "background:#fff7ed;border-left:3px solid #f97316;padding:7px 12px;margin-top:8px;font-size:.9em;color:#7c2d12;"
            note = f'<div style="{NOTE}"><b>{tested}</b> — {_SUPPL.get(lang, _SUPPL["en"])}</div>'
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
def _(lang_sel, mo):
    _SRC = {"ru": "Исходный код:", "en": "Source:", "el": "Πηγαίος κώδικας:"}
    _lbl = _SRC.get(lang_sel.value, _SRC["en"])
    mo.Html(f'''
    <style>
    #eee-footer {{
      height: 40px; background: #f5f5f5; border-top: 1px solid #e0e0e0;
      display: flex; align-items: center; justify-content: center; gap: 6px;
      margin: 16px -16px -16px -16px;
      font-family: "DM Mono", monospace;
    }}
    #eee-footer .footer-label {{ font-size: 10px; color: #1a1a1a; }}
    #eee-footer a {{ font-size: 11px; color: #003d82; text-decoration: none; }}
    </style>
    <div id="eee-footer">
      <span class="footer-label">{_lbl}</span>
      <a href="https://codeberg.org/EEE-project" target="_blank">codeberg.org/EEE-project</a>
    </div>
    ''')
    return


if __name__ == "__main__":
    app.run()
