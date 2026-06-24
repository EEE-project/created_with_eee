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
def _(mo):
    _MURRAY = (
        "<b>Homer.</b> <a href='https://www.perseus.tufts.edu/hopper/text?"
        "doc=Perseus%3atext%3a1999.01.0136%3abook%3d9'><i>The Odyssey</i></a>"
        " with an English Translation by A.T. Murray, PH.D. in two volumes."
        " Cambridge, MA., Harvard University Press; London, William Heinemann, Ltd. 1919."
    )
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
    _txt = f"**Материалы занятия:** [Od_IX_39-61.pdf]({NB_REMOTE}/Od_IX_39-61.pdf) · [Od_IX_39-61_vocabula.pdf]({NB_REMOTE}/Od_IX_39-61_vocabula.pdf)"
    mo.md(_txt)
    return


@app.cell(hide_code=True)
def _(STANZAS, WORDS_COMBINED, mo, stanza_selector, trans_selector):
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
            if _bare(w) in WORDS_COMBINED:
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
    mo.md("""
    ---
    ## Упражнение: словарная форма
    """)
    return


@app.cell(hide_code=True)
def _(QUIZ_WORDS, mo, next_btn, remaining):
    _r = remaining()
    _n = (len(QUIZ_WORDS) - len(_r)) if _r is not None else 0
    mo.hstack(
        [mo.md(f"Тесты: **{_n}** / {len(QUIZ_WORDS)}"),
         mo.Html('<div style="width:2rem"></div>'),
         next_btn],
        justify="start",
        align="center",
    )
    return


@app.cell(hide_code=True)
def _(QUIZ_WORDS, cv, gu, mo, random):
    if cv() is None:
        answer_radio = mo.ui.radio(options={"—": "—"})
        w = None
    else:
        answer_radio, w = gu.word_quiz_question(cv(), QUIZ_WORDS, "ru", random)
    return answer_radio, w


@app.cell(hide_code=True)
def _(answer_radio, build_paradigm_table, cv, gu, mo, score, w):
    mo.stop(cv() is None)
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
def _():
    import csv
    from pathlib import Path

    _vocab_path = Path(__file__).parent / "vocab_IX_39-61.tsv"
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

    _flags     = [_has_displayable_form(w) for w in QUIZ_WORDS_RAW]
    QUIZ_WORDS = [w for w, ok in zip(QUIZ_WORDS_RAW, _flags) if ok]
    return (QUIZ_WORDS,)


@app.cell(hide_code=True)
def _(QUIZ_WORDS):
    WORDS_COMBINED = {w["form"] for w in QUIZ_WORDS}
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
            tbl = (
                f'<table style="border-collapse:collapse;font-size:.95em;margin-top:8px">'
                f'<caption style="{CAP}">{be_lbl}</caption>'
                f'<tr><th style="{TH}"></th><th style="{TH}">{sg_lbl}</th><th style="{TH}">{pl_lbl}</th></tr>'
            )

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

            tbl = (
                f'<table style="border-collapse:collapse;font-size:.95em;margin-top:8px">'
                f'<caption style="{CAP}">ancient-greek</caption>'
                f'<tr><th style="{TH}"></th>'
            )
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

        elif pos == "adj":
            ag_nmap = _ag_slots("adjective")
            sg_lbl, pl_lbl = _NL

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
                tbl += f'<tr><td style="{ROW}">{_CL.get(case_key, c)}</td>'
                for n in ("S", "P"):
                    tbl += td(ag_rows[(c, n)])
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
    NB_REMOTE = f"{cfg.raw_base}/2026_06_22"
    for _f in (
        'Od_IX_39-61.pdf',
        'Od_IX_39-61_vocabula.pdf',
        'map_ortelius.jpg',
        'map_ortelius_full.jpg',
    ):
        gu.ensure_file(_f, nb_dir=NB_DIR, remote_base=NB_REMOTE)
    return (NB_REMOTE,)


if __name__ == "__main__":
    app.run()
