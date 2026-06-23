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
def _(lang_sel, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _cfg = ConfigStore.from_url(f"{_ROOT}/odyssey/lessons.tsv", ga=f"{_ROOT}/ga.json")
    eee_topbar(mo, back_url=_cfg.index_url(), lang=lang_sel.value, titles={
        "ru": "Древнегреческий с Гомером",
        "en": "Ancient Greek with Homer",
        "el": "Αρχαία Ελληνικά με τον Όμηρο",
    }, ga_config=_cfg.ga_config())
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    import base64 as _b64
    from pathlib import Path as _Path
    _img_path = _Path(__file__).parent.parent / "2026_06_01" / "Odysseus_Sirens_BM_E440_n2.jpg"
    _img_tag = (
        f'<img src="data:image/jpeg;base64,{_b64.b64encode(_img_path.read_bytes()).decode()}" '
        f'style="max-width:280px;width:100%;border-radius:4px;object-fit:cover"/>'
        if _img_path.exists() else ""
    )
    _lang = lang_sel.value
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io)"
    _TITLE = {
        "ru": "Одиссея для отважных",
        "en": "Odyssey for the Brave",
        "el": "Οδύσσεια για τους Τολμηρούς",
    }
    _LESSON = {
        "ru": "День 1 · Odyss. IX.19–38",
        "en": "Day 1 · Odyss. IX.19–38",
        "el": "Ημέρα 1 · Οδ. Θ.19–38",
    }
    _left = mo.vstack([
        mo.md(f"# {_TITLE.get(_lang, _TITLE['en'])}"),
        mo.md(_badge),
        mo.md(f"## {_LESSON.get(_lang, _LESSON['en'])}"),
    ])
    _right = mo.Html(_img_tag) if _img_tag else mo.Html("")
    mo.hstack([_left, _right], align="start")
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _lang = lang_sel.value
    _DESC = {
        "ru": (
            "Текст поэмы с параллельными переводами. "
            "Икты (ударные слоги) каждой стопы выделены "
            "<b style='color:#980000'>красным</b>. "
            "Слова из словаря занятия подчёркнуты "
            "<span style='border-bottom:2px solid #b5451b'>оранжевым</span>."
        ),
        "en": (
            "Poem text with parallel translations. "
            "Metrical ictus of each foot in <b style='color:#980000'>red</b>. "
            "Lesson vocabulary words underlined in "
            "<span style='border-bottom:2px solid #b5451b'>orange</span>."
        ),
        "el": (
            "Κείμενο με παράλληλες μεταφράσεις. "
            "Μετρικός ίκτος κάθε ποδός <b style='color:#980000'>κόκκινος</b>. "
            "Λέξεις λεξιλογίου υπογραμμισμένες "
            "<span style='border-bottom:2px solid #b5451b'>πορτοκαλί</span>."
        ),
    }
    mo.md(_DESC.get(_lang, _DESC["en"]))

    return


@app.cell(hide_code=True)
def _(STANZAS, WORDS_COMBINED, lang_sel, mo, stanza_selector, trans_selector):
    _lang = lang_sel.value
    _st_map = {s["ref"]: s for s in STANZAS}
    _stanza = _st_map[stanza_selector.value]
    _GRK = (
        "font-family:'Gentium Plus','GFS Didot',serif;"
        "font-size:1.15em;line-height:2"
    )

    _R = "<b style='color:#980000'>"
    _E = "</b>"

    _RHYTHM_HTML = {
        # IX 19–24
        "εἶμ' Ὀδυσεὺς Λαερτιάδης, ὃς πᾶσι δόλοισιν":
            f"{_R}εἶ{_E}μ' Ὀδυσ{_R}εὺ{_E}ς Λα{_R}ε{_E}ρτιάδ{_R}η{_E}ς, ὃς π{_R}ᾶ{_E}σι δόλ{_R}οι{_E}σιν",
        "ἀνθρώποισι μέλω, καί μευ κλέος οὐρανὸν ἵκει.":
            f"{_R}ἀ{_E}νθρώπ{_R}οι{_E}σι μέλ{_R}ω{_E}, καί μ{_R}ευ{_E} κλέος {_R}οὐ{_E}ρανὸν {_R}ἵ{_E}κει.",
        "ναιετάω δ' Ἰθάκην εὐδείελον· ἐν δ' ὄρος αὐτῇ":
            f"ν{_R}αι{_E}ετά{_R}ω{_E} δ' Ἰθάκ{_R}η{_E}ν εὐδ{_R}εί{_E}ελον· {_R}ἐ{_E}ν δ' ὄρος {_R}αὐ{_E}τῇ",
        "Νήριτον εἰνοσίφυλλον, ἀριπρεπές· ἀμφὶ δὲ νῆσοι":
            f"Ν{_R}ή{_E}ριτον {_R}εἰ{_E}νοσίφ{_R}υ{_E}λλον, ἀρ{_R}ι{_E}πρεπές· {_R}ἀ{_E}μφὶ δὲ ν{_R}ῆ{_E}σοι",
        "πολλαὶ ναιετάουσι μάλα σχεδὸν ἀλλήλῃσι,":
            f"π{_R}ο{_E}λλαὶ ν{_R}αι{_E}ετά{_R}ου{_E}σι μάλ{_R}α{_E} σχεδὸν {_R}ἀ{_E}λλήλ{_R}ῃ{_E}σι,",
        "Δουλίχιόν τε Σάμη τε καὶ ὑλήεσσα Ζάκυνθος.":
            f"Δ{_R}ου{_E}λίχι{_R}ό{_E}ν τε Σάμ{_R}η{_E} τε καὶ {_R}ὑ{_E}λή{_R}ε{_E}σσα Ζάκ{_R}υ{_E}νθος.",
        # IX 25–28
        "αὐτὴ δὲ χθαμαλὴ πανυπερτάτη εἰν ἁλὶ κεῖται":
            f"{_R}αὐ{_E}τὴ δ{_R}ὲ{_E} χθαμαλ{_R}ὴ{_E} πανυπ{_R}ε{_E}ρτάτη {_R}εἰ{_E}ν ἁλὶ κ{_R}εῖ{_E}ται",
        "πρὸς ζόφον, αἱ δέ τ' ἄνευθε πρὸς ἠῶ τ' ἠέλιόν τε,":
            f"πρ{_R}ὸ{_E}ς ζόφον, {_R}αἱ{_E} δέ τ' {_R}ἄ{_E}νευθε πρ{_R}ὸ{_E}ς {_R}ἠ{_E}ῶ τ' {_R}ἠ{_E}έλι{_R}ό{_E}ν τε,",
        "τρηχεῖ', ἀλλ' ἀγαθὴ κουροτρόφος· οὔ τοι ἐγώ γε":
            f"τρ{_R}η{_E}χεῖ', {_R}ἀ{_E}λλ' ἀγαθ{_R}ὴ{_E} κουρ{_R}ο{_E}τρόφος· {_R}οὔ{_E} τοι ἐγ{_R}ώ{_E} γε",
        "ἧς γαίης δύναμαι γλυκερώτερον ἄλλο ἰδέσθαι.":
            f"{_R}ἧ{_E}ς γαί{_R}η{_E}ς δύναμ{_R}αι{_E} γλυκερ{_R}ώ{_E}τερον {_R}ἄ{_E}λλο ἰδ{_R}έ{_E}σθαι.",
        # IX 29–33
        "ἦ μέν μ' αὐτόθ' ἔρυκε Καλυψώ, δῖα θεάων,":
            f"{_R}ἦ{_E} μέν μ' {_R}αὐ{_E}τόθ' ἔρ{_R}υ{_E}κε Καλ{_R}υ{_E}ψώ, δ{_R}ῖ{_E}α θε{_R}ά{_E}ων,",
        "ἐν σπέσσι γλαφυροῖσι, λιλαιομένη πόσιν εἶναι·":
            f"{_R}ἐ{_E}ν σπέσσ{_R}ι{_E} γλαφυρ{_R}οῖ{_E}σι, λιλ{_R}αι{_E}ομέν{_R}η{_E} πόσιν {_R}εἶ{_E}ναι·",
        "ὣς δ' αὔτως Κίρκη κατερήτυεν ἐν μεγάροισιν":
            f"{_R}ὣ{_E}ς δ' αὔτ{_R}ω{_E}ς Κίρκ{_R}η{_E} κατερ{_R}ή{_E}τυεν {_R}ἐ{_E}ν μεγάρ{_R}οι{_E}σιν",
        "Αἰαίη δολόεσσα, λιλαιομένη πόσιν εἶναι·":
            f"{_R}Αἰ{_E}αί{_R}η{_E} δολό{_R}ε{_E}σσα, λιλ{_R}αι{_E}ομέν{_R}η{_E} πόσιν {_R}εἶ{_E}ναι·",
        "ἀλλ' ἐμὸν οὔ ποτε θυμὸν ἐνὶ στήθεσσιν ἔπειθον.":
            f"{_R}ἀ{_E}λλ' ἐμὸν {_R}οὔ{_E} ποτε θ{_R}υ{_E}μὸν ἐν{_R}ὶ{_E} στήθ{_R}ε{_E}σσιν ἔπ{_R}ει{_E}θον.",
        # IX 34–38
        "ὣς οὐδὲν γλύκιον ἧς πατρίδος οὐδὲ τοκήων":
            f"{_R}ὣ{_E}ς οὐδ{_R}ὲ{_E}ν γλύκι{_R}ο{_E}ν ἧς π{_R}α{_E}τρίδος {_R}οὐ{_E}δὲ τοκ{_R}ή{_E}ων",
        "γίγνεται, εἴ περ καί τις ἀπόπροθι πίονα οἶκον":
            f"γ{_R}ί{_E}γνεται, {_R}εἴ{_E} περ κ{_R}αί{_E} τις ἀπ{_R}ό{_E}προθι π{_R}ί{_E}ονα {_R}οἶ{_E}κον",
        "γαίῃ ἐν ἀλλοδαπῇ ναίει ἀπάνευθε τοκήων.":
            f"γ{_R}αί{_E}ῃ ἐν {_R}ἀ{_E}λλοδαπ{_R}ῇ{_E} ναί{_R}ει{_E} ἀπάν{_R}ευ{_E}θε τοκ{_R}ή{_E}ων.",
        "εἰ δ' ἄγε τοι καὶ νόστον ἐμὸν πολυκηδέ' ἐνίσπω,":
            f"{_R}εἰ{_E} δ' ἄγε τ{_R}οι{_E} καὶ ν{_R}ό{_E}στον ἐμ{_R}ὸ{_E}ν πολυκ{_R}η{_E}δέ' ἐν{_R}ί{_E}σπω,",
        "ὅν μοι Ζεὺς ἐφέηκεν ἀπὸ Τροίηθεν ἰόντι.":
            f"{_R}ὅ{_E}ν μοι Ζ{_R}εὺ{_E}ς ἐφέ{_R}η{_E}κεν ἀπ{_R}ὸ{_E} Τροί{_R}η{_E}θεν ἰ{_R}ό{_E}ντι.",
    }

    def _bare(html):
        text, in_tag = '', False
        for ch in html:
            if ch == '<':
                in_tag = True
            elif ch == '>':
                in_tag = False
            elif not in_tag:
                text += ch
        return text.strip("·,;.'·,!?·")

    def _hl(line):
        colored = _RHYTHM_HTML.get(line, line)
        parts = []
        for w in colored.split(' '):
            if _bare(w) in WORDS_COMBINED:
                parts.append(
                    f"<span style='border-bottom:2px solid #b5451b;padding-bottom:0'>{w}</span>"
                )
            else:
                parts.append(w)
        return ' '.join(parts)

    if trans_selector.value == "подстрочник":
        _iln = _stanza["interlinear"]
        _pairs = _iln.get(_lang, _iln.get("ru", []))
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
def _(lang_sel, mo):
    _lang = lang_sel.value
    _ETYM = {
        "ru": r"""---
    ## Имя героя

    **Ὀδυσσεύς** ← **ὀδύσσομαι** — гневаться, ненавидеть; причинять страдание

    > *πολλοῖσιν γὰρ ἐγώ γε ὀδυσσάμενος* (Od. XIX.407)
    > «ибо многим я причинил страдание»

    Имя означает «тот, кто причиняет / претерпевает страдания». Гомер использует его как этимологический символ судьбы героя.
    """,
        "en": r"""---
    ## The hero's name

    **Ὀδυσσεύς** ← **ὀδύσσομαι** — to be angry at, to hate; to cause suffering

    > *πολλοῖσιν γὰρ ἐγώ γε ὀδυσσάμενος* (Od. XIX.407)
    > "for I have caused suffering to many"

    The name encodes the hero's fate: one who suffers and causes suffering.
    """,
        "el": r"""---
    ## Το όνομα του ήρωα

    **Ὀδυσσεύς** ← **ὀδύσσομαι** — οργίζομαι, μισώ· προκαλώ πόνο

    > *πολλοῖσιν γὰρ ἐγώ γε ὀδυσσάμενος* (Od. XIX.407)

    Το όνομα συμβολίζει τη μοίρα του ήρωα: αυτός που υποφέρει και προκαλεί πόνο.
    """,
    }
    mo.md(_ETYM.get(_lang, _ETYM["en"]))
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
    return


@app.cell(hide_code=True)
def _(mo):
    lang_sel = mo.ui.dropdown(
        options={"Русский": "ru", "English": "en", "Ελληνικά": "el"},
        value="Русский",
        label="🌐",
    )
    mo.Html(f"""
    <div style="position: fixed; top: 60px; right: 10px; z-index: 1000;
         background: white; padding: 8px 12px; border-radius: 8px;
         box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
        {lang_sel}
    </div>
    """)
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
        options=[s["ref"] for s in STANZAS],
        value=STANZAS[0]["ref"],
        label="Строфа",
    )
    return (stanza_selector,)


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _lang = lang_sel.value
    _ILN  = {"ru": "подстрочник", "en": "interlinear", "el": "λέξη-λέξη"}
    _ALL = {
        _ILN.get(_lang, "подстрочник"):                       "подстрочник",
        "Жуковский (1849) · рус., классический":               "Жуковский",
        "Вересаев (1953) · рус., точный":                     "Вересаев",
        "Murray (1919) · eng., prose":                         "Murray",
        "Lattimore (1951) · eng., verse":                      "Lattimore",
        "Πολυλάς (1875) · ν.ε., κλασική":                    "Πολυλάς",
        "Καζαντζάκης–Κακριδής (1965) · ν.ε., σύγχρονη":      "Καζαντζάκης–Κακριδής",
    }
    _LANG_VALS = {
        "ru": {"подстрочник", "Жуковский", "Вересаев"},
        "en": {"подстрочник", "Murray", "Lattimore"},
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
    _iln_en = _parse_iln((_root / "interlenear_en.md").read_text(encoding="utf-8"))
    _iln_el = _parse_iln((_root / "interlenear_el.md").read_text(encoding="utf-8"))
    _trans_ru, _desc_ru = _parse_trans((_root / "translations_ru.md").read_text(encoding="utf-8"))
    _trans_en, _desc_en = _parse_trans((_root / "translations_en.md").read_text(encoding="utf-8"))
    _trans_el, _desc_el = _parse_trans((_root / "translations_el.md").read_text(encoding="utf-8"))
    TRANS_DESC = {**_desc_ru, **_desc_en, **_desc_el}
    STANZAS = [
        {
            "ref": ref,
            "lines": lines,
            "interlinear": {
                "ru": _iln_ru.get(ref, []),
                "en": _iln_en.get(ref, []),
                "el": _iln_el.get(ref, []),
            },
            "translations": {
                **{tr: d.get(ref, "—") for tr, d in _trans_ru.items()},
                **{tr: d.get(ref, "—") for tr, d in _trans_en.items()},
                **{tr: d.get(ref, "—") for tr, d in _trans_el.items()},
            },
        }
        for ref, lines in _greek.items()
    ]
    return (STANZAS,)


@app.cell(hide_code=True)
def _():
    import csv
    from pathlib import Path

    _vocab_path = Path(__file__).parent / "vocab_IX_19-38.tsv"
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

    _flags     = [_has_displayable_form(w) for w in QUIZ_WORDS_RAW]
    QUIZ_WORDS = [w for w, ok in zip(QUIZ_WORDS_RAW, _flags) if ok]
    return (QUIZ_WORDS,)


@app.cell(hide_code=True)
def _(QUIZ_WORDS_RAW):
    WORDS_COMBINED = {w["form"] for w in QUIZ_WORDS_RAW}
    return (WORDS_COMBINED,)


@app.cell(hide_code=True)
def _(ag_backend, eee, um_backend):
    import unicodedata
    import functools

    def _norm_grc(s):
        _STRIP = {
            "̀", "́", "̂", "̈",
            "̓", "̔", "̓", "͂",
            "̄", "̆",
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
            tbl = (
                f'<table style="border-collapse:collapse;font-size:.95em;margin-top:8px">'
                f'<caption style="{CAP}">{be_lbl}</caption>'
                f'<tr><th style="{TH}"></th><th style="{TH}">{sg_lbl}</th><th style="{TH}">{pl_lbl}</th></tr>'
            )

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

            tbl = (
                f'<table style="border-collapse:collapse;font-size:.95em;margin-top:8px">'
                f'<caption style="{CAP}">ancient-greek</caption>'
                f'<tr><th style="{TH}"></th>'
            )
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

        elif pos == "adj":
            ag_nmap = _ag_slots("adjective", lang)
            cl = _CL.get(lang, _CL["en"])
            sg_lbl, pl_lbl = _NL.get(lang, _NL["en"])

            ag_rows = {}
            for c in ["N", "G", "D", "A"]:
                for n in ("S", "P"):
                    forms = set()
                    for g in "MFN":
                        slot = ag_nmap.get(f".{c}{n}{g}")
                        if slot:
                            forms |= eee.inflect_slot(lemma, slot, "adjective", language="grc", backend="ancient-greek")
                    ag_rows[(c, n)] = forms

            if not any(ag_rows.values()):
                return None

            tbl = (
                f'<table style="border-collapse:collapse;font-size:.95em;margin-top:8px">'
                f'<caption style="{CAP}">ancient-greek</caption>'
                f'<tr><th style="{TH}"></th><th style="{TH}">{sg_lbl}</th><th style="{TH}">{pl_lbl}</th></tr>'
            )
            for c in ["N", "G", "D", "A"]:
                case_key = {"N": "Nom", "G": "Gen", "D": "Dat", "A": "Acc"}[c]
                tbl += f'<tr><td style="{ROW}">{cl.get(case_key, c)}</td>'
                for n in ("S", "P"):
                    tbl += td(ag_rows[(c, n)])
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
    from eee_project.notebook_utils import eee_footer
    eee_footer(mo, lang=lang_sel.value)
    return


if __name__ == "__main__":
    app.run()
