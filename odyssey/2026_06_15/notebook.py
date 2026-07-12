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
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_LtJRZFGZ4wFNFPk4edTAbL)"
    _left = mo.vstack([
        mo.md("# Одиссея для отважных"),
        mo.md(_badge),
        mo.md("## День 1 · Odyss. IX.19–38"),
    ])
    _img_url = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/odyssey/2026_06_15/map_ithaca.jpg"
    _img = mo.Html(
        f'<a href="{_img_url}" target="_blank" rel="noopener">'
        f'<img src="{_img_url}" style="max-width:280px;width:100%;border-radius:4px;object-fit:cover;cursor:pointer"/>'
        f'</a>'
    )
    mo.hstack([_left, _img], align="start")
    return


@app.cell(hide_code=True)
def _(mo):
    _base = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/odyssey/2026_06_15"
    mo.md(
        f"**Материалы занятия:** "
        f"[Одиссея 1.pdf]({_base}/Одиссея%201.pdf) · "
        f"[слова день 1.pdf]({_base}/слова%20день%201.pdf) · "
        "[odysseus-unbound.org ↗](https://www.odysseus-unbound.org/mystery/)"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Имя героя

    **Ὀδυσσεύς** ← **ὀδύσσομαι** — гневаться, ненавидеть; причинять страдание

    > *πολλοῖσιν γὰρ ἐγώ γε ὀδυσσάμενος* (Od. XIX.407)
    > «ибо многим я причинил страдание»

    Имя означает «тот, кто причиняет / претерпевает страдания». Гомер использует его как этимологический символ судьбы героя.
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
def _(ag_backend, ag_byzantine, ag_homer, ag_lsj, ag_lxx, ag_morphgnt, gu):
    import csv
    from pathlib import Path

    _vocab_path = Path(__file__).parent / "vocab_IX_19-38.tsv"
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
def _(mo):
    from eee_project.notebook_utils import eee_footer
    eee_footer(mo, lang="ru")
    return


@app.cell(hide_code=True)
def _(cfg, gu):
    from pathlib import Path as _P
    NB_DIR = _P(__file__).parent
    NB_REMOTE = f"{cfg.raw_base}/2026_06_15"
    for _f in (
        'Одиссея 1.pdf',
        'слова день 1.pdf',
        'map_ithaca.jpg',
        'map_ithaca_full.jpg',
    ):
        gu.ensure_file(_f, nb_dir=NB_DIR, remote_base=NB_REMOTE)
    return


if __name__ == "__main__":
    app.run()
