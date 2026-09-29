# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.14",
#     "eee-project>=1.19.0",
#     "ancient-greek-backend-eee>=2.0.0",
#     "unimorph-backend-eee>=1.0.3",
#     "modern-greek-backend-eee>=1.0.0",
# ]
# ///

import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium", app_title="Одиссея с Гомером — День 4: Одиссея IX.82–104")


@app.cell(hide_code=True)
def _(lang_sel, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://raw.githubusercontent.com/EEE-project/created_with_eee/main"
    cfg = ConfigStore.from_file_or_url(__file__, f"{_ROOT}/ancient_greek/odyssey/index.tsv", ga=f"{_ROOT}/ga.json")
    eee_topbar(mo, back_url=cfg.index_url(), lang=lang_sel.value, titles={
        "ru": "Одиссея с Гомером",
        "en": "Odyssey with Homer",
        "el": "Οδύσσεια με τον Όμηρο",
    }, ga_config=cfg.ga_config(), same_window=True)
    return (cfg,)


@app.cell(hide_code=True)
def _(cfg):
    import pathlib as _pl
    # Course-local lexicon files (moved from greek-inflexion-eee 2026-07-31,
    # see this course's own AGENTS.md) -- Epic-register, Odyssey-course-
    # vocabulary-specific data merged into ag_backend/ag_homer below,
    # alongside homer (same register), not lsj/byzantine (Attic/Koine).
    _odyssey_yamls = [_pl.Path(__file__).parent.parent / f"odyssey_morpheus_{_p}_lexicon.yaml" for _p in ("adjs", "nouns", "verbs")]
    from eee_project import GreekUtils as _GU
    for _y in _odyssey_yamls:
        _GU.ensure_file(_y.name, nb_dir=_y.parent, remote_base=cfg.raw_base)
    ODYSSEY_EXTRA_LEXICONS = [str(_y.resolve()) for _y in _odyssey_yamls]
    return (ODYSSEY_EXTRA_LEXICONS,)


@app.cell(hide_code=True)
def _(eee, lang_sel, mo):
    from pathlib import Path as _Path
    _TITLES = {
        "ru": ("# Одиссея с Гомером", "## День 4 · Odyss. IX.82–104"),
        "en": ("# Odyssey with Homer", "## Day 4 · Odyss. IX.82–104"),
        "el": ("# Οδύσσεια με τον Όμηρο", "## Ημέρα 4 · Odyss. IX.82–104"),
    }
    _h1, _h2 = _TITLES.get(lang_sel.value, _TITLES["ru"])
    _thumb_path = _Path(__file__).parent / "lotus_plant.jpg"
    _left = mo.vstack([
        mo.md(_h1),
        mo.md(_h2),
    ])
    _img = eee.magnify_image(mo, _thumb_path, raw_base="https://raw.githubusercontent.com/EEE-project/created_with_eee/main/ancient_greek/odyssey/2026_07_06", width=280)
    _cap = mo.md(
            "<div style='font-size:.8em;color:#9ca3af;text-align:center'>"
            "<i>Ziziphus jujuba</i> — Adolphus Ypey, <i>Afbeeldingen der artseny-gewassen</i>, 1813</div>"
        )

    _right = mo.vstack([_img, _cap], align="center")
    mo.hstack([_left, _right], align="start")
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, gu, lang_sel, mo):
    _txt = (
        f"{gu.ui_label('lesson_materials_label', lang_sel.value)} "
        f"[Od_IX_82-104.pdf]({NB_REMOTE}/Od_IX_82-104.pdf) · "
        f"[Od_IX_82-104_vocabula.pdf]({NB_REMOTE}/Od_IX_82-104_vocabula.pdf)"
    )
    mo.md(_txt)
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _TXT = {
        "ru": r"""
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
    """,
        "en": r"""
    ---
    ## What plant was the "lotus"?

    Exactly which plant the Lotus-eaters ate in Homer is not known for certain. Herodotus describes it twice.

    **Hdt. II.92** (on the Egyptian lotus):

    > …φύεται ἐν τῷ ὕδατι κρίνεα πολλά, τὰ Αἰγύπτιοι καλέουσι **λωτόν**. […]
    > Ἔστι δὲ καὶ ἡ ῥίζα τοῦ λωτοῦ τούτου ἐδωδίμη […] ἐὸν στρογγύλον,
    > **μέγαθος κατὰ μῆλον**.

    "…many lilies grow in the water, which the Egyptians call the lotus…
    The root of this plant is also edible, round, the size of an apple."

    **Hdt. IV.177** (on the Libyan Lotus-eaters):

    > Ἀκτὴν δὲ προέχουσαν ἐς τὸν πόντον … νέμονται **Λωτοφάγοι**, οἳ τὸν καρπὸν
    > μοῦνον τοῦ λωτοῦ τρώγοντες ζώουσι. … γλυκύτητα δὲ τοῦ φοίνικος τῷ καρπῷ
    > προσείκελος. Ποιεῦνται δὲ ἐκ τοῦ καρποῦ τούτου οἱ Λωτοφάγοι καὶ **οἶνον**.

    "…the Lotus-eaters dwell there. They live solely on the fruit of the
    lotus… in sweetness the fruit is like a date; from it the Lotus-eaters
    also make wine."
    *(this refers to the Lesser Syrtis — the coast of present-day Tunisia.)*

    **Polybius**
    (2nd century BC, as retold by Strabo) identified it with the
    **ziziphus** (*Ziziphus lotus*, wild jujube, a relative of the common
    jujube): a thorny shrub with small leaves, its fruit like a round plum,
    turning purple when ripe, from which wine was made, as from dates.
    Herodotus and Theophrastus had written about the plant earlier; later
    it was popularized by Pliny the Elder.
    """,
        "el": r"""
    ---
    ## Τι φυτό ήταν ο «λωτός»;

    Ποιο ακριβώς φυτό έτρωγαν οι λωτοφάγοι στον Όμηρο δεν είναι γνωστό με
    βεβαιότητα. Ο Ηρόδοτος το περιγράφει δύο φορές.

    **Hdt. II.92** (για τον αιγυπτιακό λωτό):

    > …φύεται ἐν τῷ ὕδατι κρίνεα πολλά, τὰ Αἰγύπτιοι καλέουσι **λωτόν**. […]
    > Ἔστι δὲ καὶ ἡ ῥίζα τοῦ λωτοῦ τούτου ἐδωδίμη […] ἐὸν στρογγύλον,
    > **μέγαθος κατὰ μῆλον**.

    «…μέσα στο νερό φυτρώνουν πολλά κρίνα, που οι Αιγύπτιοι ονομάζουν
    λωτό… Η ρίζα αυτού του φυτού είναι επίσης βρώσιμη, στρογγυλή, στο
    μέγεθος μήλου».

    **Hdt. IV.177** (για τους λίβυους λωτοφάγους):

    > Ἀκτὴν δὲ προέχουσαν ἐς τὸν πόντον … νέμονται **Λωτοφάγοι**, οἳ τὸν καρπὸν
    > μοῦνον τοῦ λωτοῦ τρώγοντες ζώουσι. … γλυκύτητα δὲ τοῦ φοίνικος τῷ καρπῷ
    > προσείκελος. Ποιεῦνται δὲ ἐκ τοῦ καρποῦ τούτου οἱ Λωτοφάγοι καὶ **οἶνον**.

    «…εκεί κατοικούν οι λωτοφάγοι. Ζουν αποκλειστικά από τον καρπό του
    λωτού… στη γλυκύτητα ο καρπός μοιάζει με χουρμά· από αυτόν οι
    λωτοφάγοι φτιάχνουν και κρασί».
    *(ο λόγος είναι για τη Μικρή Σύρτη — τις ακτές της σημερινής Τυνησίας.)*

    **Πολύβιος**
    (2ος αι. π.Χ., όπως τον αναφέρει ο Στράβων) το ταύτισε με το
    **τζιτζιφιά** (*Ziziphus lotus*, άγρια τζίτζιφα, συγγενής της κοινής
    τζίτζιφας): αγκαθωτός θάμνος με μικρά φύλλα, καρπός σαν στρογγυλό
    δαμάσκηνο, που ωριμάζοντας γίνεται πορφυρός, από τον οποίο, όπως από
    τους χουρμάδες, έφτιαχναν κρασί. Παλαιότερα για το φυτό είχαν γράψει
    ο Ηρόδοτος και ο Θεόφραστος, αργότερα το έκανε δημοφιλές ο Πλίνιος
    ο Πρεσβύτερος.
    """,
    }
    mo.md(_TXT.get(lang_sel.value, _TXT["ru"]))
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _TXT = {
        "ru": r"""
    ## Λωτός — слово-ловушка

    В современном греческом одним и тем же словом *[λωτός](https://el.wiktionary.org/wiki/%CE%BB%CF%89%CF%84%CF%8C%CF%82)* называют и **водяной лотос**, и **хурму** (от *Diospyros lotus* — дикая хурма) — различают по контексту.

    Финик же — *[χουρμάς](https://el.wiktionary.org/wiki/%CF%87%CE%BF%CF%85%CF%81%CE%BC%CE%AC%CF%82)*, а финиковая пальма — *[φοίνικας](https://el.wiktionary.org/wiki/%CF%86%CE%BF%CE%AF%CE%BD%CE%B9%CE%BA%CE%B1%CF%82)*.

    В русский язык слово «хурма» попало из фарси, где в оригинале звучит как خرمالو khormâlu — то есть «финиковая слива». Само слово خرما khormâ означает финик, слово آلو âlu — слива. Название khormâlu первоначально относилось к хурме кавказской. Вяленая хурма по вкусу очень напоминает финики, отсюда и произошло название хурмы кавказской на фарси. Затем это название распространилось на другие виды хурмы, в том числе и на восточную (японскую). [Wikipedia](https://ru.wikipedia.org/wiki/%D0%A5%D1%83%D1%80%D0%BC%D0%B0#%D0%9D%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)
    """,
        "en": r"""
    ## Λωτός — a word-trap

    In Modern Greek, the same word *[λωτός](https://el.wiktionary.org/wiki/%CE%BB%CF%89%CF%84%CF%8C%CF%82)* is used for both the **water lotus** and **persimmon** (from *Diospyros lotus* — the wild "date-plum" persimmon) — the two are told apart from context.

    The date, meanwhile, is *[χουρμάς](https://el.wiktionary.org/wiki/%CF%87%CE%BF%CF%85%CF%81%CE%BC%CE%AC%CF%82)*, and the date palm is *[φοίνικας](https://el.wiktionary.org/wiki/%CF%86%CE%BF%CE%AF%CE%BD%CE%B9%CE%BA%CE%B1%CF%82)*.

    The Russian word for persimmon, *khurma*, entered Russian from Persian, where the original word is خرمالو khormâlu — literally "date-plum." The word خرما khormâ itself means "date," and آلو âlu means "plum." The name khormâlu originally referred to the Caucasian persimmon; dried Caucasian persimmon tastes very much like dates, which is where the Persian name comes from. The name later spread to other kinds of persimmon, including the Oriental (Japanese) persimmon. [Wikipedia](https://ru.wikipedia.org/wiki/%D0%A5%D1%83%D1%80%D0%BC%D0%B0#%D0%9D%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)
    """,
        "el": r"""
    ## Λωτός — παγίδα λέξης

    Στα νέα ελληνικά, η ίδια λέξη *[λωτός](https://el.wiktionary.org/wiki/%CE%BB%CF%89%CF%84%CF%8C%CF%82)* χρησιμοποιείται και για τον **υδρόβιο λωτό**, και για το **κάκι** (από το *Diospyros lotus* — το άγριο κάκι) — ξεχωρίζουν από τα συμφραζόμενα.

    Ο χουρμάς πάλι είναι *[χουρμάς](https://el.wiktionary.org/wiki/%CF%87%CE%BF%CF%85%CF%81%CE%BC%CE%AC%CF%82)*, και ο φοίνικας (το δέντρο) είναι *[φοίνικας](https://el.wiktionary.org/wiki/%CF%86%CE%BF%CE%AF%CE%BD%CE%B9%CE%BA%CE%B1%CF%82)*.

    Η ρωσική λέξη για το κάκι, *khurma*, μπήκε στα ρωσικά από τα περσικά, όπου η αρχική λέξη είναι خرمالو khormâlu — κυριολεκτικά «δαμάσκηνο-χουρμάς». Η ίδια η λέξη خرما khormâ σημαίνει «χουρμάς», και η λέξη آلو âlu σημαίνει «δαμάσκηνο». Το όνομα khormâlu αναφερόταν αρχικά στο καυκάσιο κάκι· το αποξηραμένο καυκάσιο κάκι θυμίζει πολύ στη γεύση χουρμάδες, από εκεί προήλθε το περσικό όνομα. Αργότερα το όνομα επεκτάθηκε και σε άλλα είδη κακιού, μεταξύ αυτών και στο ανατολικό (ιαπωνικό) κάκι. [Wikipedia](https://ru.wikipedia.org/wiki/%D0%A5%D1%83%D1%80%D0%BC%D0%B0#%D0%9D%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)
    """,
    }
    mo.md(_TXT.get(lang_sel.value, _TXT["ru"]))
    return


@app.cell(hide_code=True)
def _(gu, lang_sel, mo):
    mo.md(gu.ui_label('poem_section_heading', lang_sel.value))
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
def _(TRANS_DESC, eee, gu, lang_sel, mo, trans_selector):
    _desc_map = {eee.interlinear_translator_key(lang_sel.value): gu.ui_label('interlinear_description', lang_sel.value), **TRANS_DESC}
    mo.md(_desc_map.get(trans_selector.value, ""))
    return


@app.cell(hide_code=True)
def _(cfg, gu, lang_sel, mo):
    from pathlib import Path as _P
    SHOW_ICTUS = mo.ui.switch(value=True)
    SHOW_HOMER = mo.ui.switch(value=True)

    # Shared across all lessons. Fetched via ensure_file, not a bare local
    # read: molab only bundles files that live in the notebook's own directory,
    # so a parent-directory file like this one is missing there unless we
    # download it ourselves (matches the pattern already used for materials PDFs).
    _eee_note_filename = (
        "eee_note.md" if lang_sel.value == "ru" else f"eee_note_{lang_sel.value}.md"
    )
    _eee_note_path = gu.ensure_file(
        _eee_note_filename, nb_dir=_P(__file__).parent.parent, remote_base=cfg.raw_base,
    )
    EEE_NOTE = _eee_note_path.read_text(encoding="utf-8") if _eee_note_path else (
        gu.ui_label('eee_note_load_error', lang_sel.value)
    )

    _ICTUS_COLOR_NAME = {"ru": "красным", "en": "red", "el": "κόκκινο"}
    gu.ictus_toggle_panel(SHOW_ICTUS, SHOW_HOMER, EEE_NOTE,
                           ictus_color="#980000",
                           ictus_color_name=_ICTUS_COLOR_NAME.get(lang_sel.value, "красным"),
                           lang=lang_sel.value)
    return EEE_NOTE, SHOW_HOMER, SHOW_ICTUS


@app.cell(hide_code=True)
def _(
    CLICKABLE_FORMS,
    HOMER_WORDS,
    RHYTHM_HTML,
    SHOW_HOMER,
    SHOW_ICTUS,
    STANZAS,
    eee,
    mo,
    stanza_selector,
    trans_selector,
):
    _st_map = {s["ref"]: s for s in STANZAS}
    _stanza = _st_map[stanza_selector.value]

    text_widget = eee.interactive_text(
        mo,
        lines=_stanza["lines"],
        clickable=CLICKABLE_FORMS,
        homer_words=HOMER_WORDS if SHOW_HOMER.value else set(),
        ictus_html=RHYTHM_HTML,
        show_ictus=SHOW_ICTUS.value,
    )

    _txt_lines = _stanza["translations"].get(trans_selector.value, "—").split("\n")

    _line_divs = "".join(
        f'<div>{line.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")}</div>'
        for line in _txt_lines
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
def _(QUIZ_WORDS_RAW, build_period_tables, gu, lang_sel, text_widget):
    period_tables, period_selector, gloss_panel = gu.render_gloss_selector(
        QUIZ_WORDS_RAW, text_widget.widget.selected_word, build_period_tables, lang=lang_sel.value,
    )
    gloss_panel
    return period_selector, period_tables


@app.cell(hide_code=True)
def _(gu, period_selector, period_tables):
    gu.render_gloss_table(period_tables, period_selector)
    return


@app.cell(hide_code=True)
def _(EEE_NOTE, gu, lang_sel, mo):
    mo.accordion({gu.ui_label('form_check_accordion_label', lang_sel.value): EEE_NOTE})
    return


@app.cell(hide_code=True)
def _(gu, lang_sel, mo):
    mo.md(f"""
    ---
    {gu.ui_label('exercises_section_heading', lang_sel.value)}
    """)
    return


@app.cell(hide_code=True)
def _():
    # Shared per-lesson default: how many items each exercise below draws per
    # session. Change this one value to affect every exercise at once, or
    # override a single exercise by editing its own n=SESSION_SIZE argument.
    SESSION_SIZE = 10
    return (SESSION_SIZE,)


@app.cell(hide_code=True)
def _(gu, lang_sel):
    quiz_renew_btn = gu.make_renew_button(lang=lang_sel.value)
    return (quiz_renew_btn,)


@app.cell(hide_code=True)
def _(QUIZ_WORDS, cv, gu, history, lang_sel, remaining, restore_entry):
    _ = cv()
    answer_radio, next_btn, prev_btn = gu.word_quiz_widgets(
        cv=cv(),
        remaining=remaining(),
        vocab=QUIZ_WORDS,
        restore_entry=restore_entry(),
        history_len=len(history()),
        lang=lang_sel.value,
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
    lang_sel,
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
        title=gu.ui_label('word_find_exercise_heading', lang_sel.value),
        meaning_key='_label',
        form_key='form',
        lang=lang_sel.value,
        renew_btn=quiz_renew_btn,
    )
    return


@app.cell(hide_code=True)
def _(gu, lang_sel, mo):
    mo.md(gu.ui_label('stanza_match_section_heading', lang_sel.value))
    return


@app.cell(hide_code=True)
def _(gu, lang_sel, mo):
    _DIRECTION_OPTS = {
        gu.ui_label('stanza_match_toggle_grc_to_tr', lang_sel.value): "grc_to_tr",
        gu.ui_label('stanza_match_toggle_tr_to_grc', lang_sel.value): "tr_to_grc",
    }
    sm_direction = mo.ui.radio(
        options=_DIRECTION_OPTS,
        value=list(_DIRECTION_OPTS.keys())[0],
        label=gu.ui_label('stanza_match_direction_label', lang_sel.value),
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
    SESSION_SIZE,
    STANZAS,
    gu,
    sm_renew_btn,
    sm_set_cv,
    sm_set_future,
    sm_set_history,
    sm_set_remaining,
    sm_set_restore_entry,
    sm_set_score,
):
    SM_STANZAS = gu.sample_session_items(STANZAS, n=SESSION_SIZE)
    gu.reset_quiz_state(sm_renew_btn, sm_set_cv, sm_set_remaining, sm_set_score,
                         sm_set_history, sm_set_future, sm_set_restore_entry)
    return (SM_STANZAS,)


@app.cell(hide_code=True)
def _(gu, lang_sel):
    sm_renew_btn = gu.make_renew_button(lang=lang_sel.value)
    return (sm_renew_btn,)


@app.cell(hide_code=True)
def _(
    SM_STANZAS,
    TRANS_BY_LANG,
    gu,
    lang_sel,
    sm_cv,
    sm_direction,
    sm_history,
    sm_remaining,
    sm_restore_entry,
):
    _ = sm_cv()
    sm_choice_radio, sm_next_btn, sm_prev_btn = gu.stanza_match_widgets(
        cv=sm_cv(),
        remaining=sm_remaining(),
        stanzas=SM_STANZAS,
        direction=sm_direction.value,
        restore_entry=sm_restore_entry(),
        history_len=len(sm_history()),
        lang=lang_sel.value,
        valid_translators=TRANS_BY_LANG.get(lang_sel.value, TRANS_BY_LANG["ru"]),
    )
    return sm_choice_radio, sm_next_btn, sm_prev_btn


@app.cell(hide_code=True)
def _(
    SM_STANZAS,
    TRANS_BY_LANG,
    gu,
    lang_sel,
    sm_choice_radio,
    sm_cv,
    sm_direction,
    sm_future,
    sm_history,
    sm_next_btn,
    sm_prev_btn,
    sm_remaining,
    sm_renew_btn,
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
        stanzas=SM_STANZAS,
        direction=sm_direction.value,
        lang=lang_sel.value,
        renew_btn=sm_renew_btn,
        valid_translators=TRANS_BY_LANG.get(lang_sel.value, TRANS_BY_LANG["ru"]),
    )
    return


@app.cell(hide_code=True)
def _(gu, lang_sel, mo):
    mo.md(gu.ui_label('presence_exercise_heading', lang_sel.value))
    return


@app.cell(hide_code=True)
def _(
    QUIZ_WORDS_RAW,
    SESSION_SIZE,
    STANZAS,
    TRANS_BY_LANG,
    cfg,
    eee,
    gu,
    lang_sel,
    tp_renew_btn,
    tp_set_cv,
    tp_set_future,
    tp_set_history,
    tp_set_remaining,
    tp_set_restore_entry,
    tp_set_score,
):
    from pathlib import Path as _P

    _interlinear_keys = {eee.interlinear_translator_key(_l) for _l in ("ru", "en", "el")}
    LITERARY_TRANSLATORS = [
        t for t in TRANS_BY_LANG.get(lang_sel.value, TRANS_BY_LANG["ru"])
        if t not in _interlinear_keys
    ]
    _tp_vocab = [w for w in QUIZ_WORDS_RAW if w.get("pos") in eee.TRANSLATION_PRESENCE_CONTENT_POS]
    # Same-directory file, but the WASM export doesn't bundle it -- needs ensure_file like the vocab TSV above.
    _tp_path = gu.ensure_file(
        "translation_presence.tsv", nb_dir=_P(__file__).parent, remote_base=cfg.nb_remote("2026_07_06"),
    )
    gu.sync_translation_presence_tsv(_tp_vocab, LITERARY_TRANSLATORS, STANZAS, _tp_path)
    TP_ITEMS = gu.balance_presence_items(gu.build_translation_presence_items(
        gu.read_translation_presence_tsv(_tp_path), QUIZ_WORDS_RAW, STANZAS,
        valid_translators=LITERARY_TRANSLATORS,
    ), n=SESSION_SIZE)
    gu.reset_quiz_state(tp_renew_btn, tp_set_cv, tp_set_remaining, tp_set_score,
                         tp_set_history, tp_set_future, tp_set_restore_entry)
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
def _(gu, lang_sel):
    tp_renew_btn = gu.make_renew_button(lang=lang_sel.value)
    return (tp_renew_btn,)


@app.cell(hide_code=True)
def _(TP_ITEMS, gu, lang_sel, tp_cv, tp_history, tp_remaining, tp_restore_entry):
    _ = tp_cv()
    tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch = gu.translation_presence_widgets(
        cv=tp_cv(),
        remaining=tp_remaining(),
        items=TP_ITEMS,
        restore_entry=tp_restore_entry(),
        history_len=len(tp_history()),
        lang=lang_sel.value,
    )
    return tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch


@app.cell(hide_code=True)
def _(
    TP_ITEMS,
    gu,
    lang_sel,
    tp_choice_radio,
    tp_cv,
    tp_future,
    tp_history,
    tp_next_btn,
    tp_prev_btn,
    tp_remaining,
    tp_renew_btn,
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
        lang=lang_sel.value,
        renew_btn=tp_renew_btn,
    )
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
def _(STANZAS, gu, lang_sel, mo):
    stanza_selector = mo.ui.dropdown(
        options=[s["ref"] for s in STANZAS],
        value=STANZAS[0]["ref"],
        label=gu.ui_label('stanza_label', lang_sel.value),
    )
    return (stanza_selector,)


@app.cell(hide_code=True)
def _(eee, gu, lang_sel, mo):
    TRANS_BY_LANG = {
        # Each language's own interlinear crib is a "## interlinear_{lang}"
        # section inside that language's translations_{lang}.md (KB naming
        # convention -- confirmed against greek-knowledge-eee's actual file
        # headers, not the old pre-port local translations_ru.md, which used
        # "подстрочник" instead). eee.interlinear_translator_key derives the
        # per-language key from this same convention -- see the
        # STANZAS-building cell.
        "ru": [eee.interlinear_translator_key("ru"), "Жуковский", "Вересаев"],
        "en": ["Pope", "Murray", eee.interlinear_translator_key("en")],
        "el": ["Πολυλάς", eee.interlinear_translator_key("el")],
    }
    _DEFAULT_BY_LANG = {"ru": "Жуковский", "en": "Pope", "el": "Πολυλάς"}
    # Only one interlinear variant is ever relevant for the current language,
    # so it's looked up dynamically rather than listed as three static
    # entries -- all three would render the same gu.ui_label(...) text for
    # a given lang_sel.value and silently collide as dict keys otherwise.
    _ALL_OPTIONS = {
        gu.ui_label('interlinear_label', lang_sel.value): eee.interlinear_translator_key(lang_sel.value),
        "Жуковский (1849)":    "Жуковский",
        "Вересаев (1953)":     "Вересаев",
        "Pope (1725)":          "Pope",
        "Murray (1919)":        "Murray",
        "Πολυλάς (1875/1877)":  "Πολυλάς",
    }
    _valid = TRANS_BY_LANG.get(lang_sel.value, TRANS_BY_LANG["ru"])
    _opts = {k: v for k, v in _ALL_OPTIONS.items() if v in _valid}
    _default_v = _DEFAULT_BY_LANG.get(lang_sel.value, "Жуковский")
    _default_k = next((k for k, v in _opts.items() if v == _default_v), list(_opts.keys())[0])
    trans_selector = mo.ui.dropdown(
        options=_opts,
        value=_default_k,
        label=gu.ui_label('trans_selector_label', lang_sel.value),
    )
    return TRANS_BY_LANG, trans_selector


@app.cell(hide_code=True)
async def _(cfg, eee):
    from pathlib import Path as _P
    from eee_project import GreekUtils as _GU

    _root = _P(__file__).parent
    _session_remote = cfg.nb_remote("2026_07_06")
    _fetched = await _GU.ensure_files(
        "greek.md", "ictus.html",
        nb_dir=_root, remote_base=_session_remote,
    )
    _greek_md = _fetched["greek.md"]
    _ictus_html = _fetched["ictus.html"]

    _gke_remote = "https://codeberg.org/EEE-project/greek-knowledge-eee/raw/branch/main/texts/odyssey"
    _trans_fetched = await _GU.ensure_files(
        "translations_ru.md", "translations_en.md", "translations_el.md",
        nb_dir=_root, remote_base=_gke_remote,
    )
    if _greek_md is None or _ictus_html is None or any(v is None for v in _trans_fetched.values()):
        raise FileNotFoundError(
            "greek.md/ictus.html/translations_{ru,en,el}.md: one or more "
            "required session files could not be fetched (see ensure_file "
            "diagnostics above)"
        )
    _greek = eee.parse_stanza_text(_greek_md.read_text(encoding="utf-8"), ref_prefix="### Odyss. ")

    _translations: dict = {}
    TRANS_DESC: dict = {}
    for _fname in ("translations_ru.md", "translations_en.md", "translations_el.md"):
        _tr, _desc = eee.parse_stanza_translations(
            _trans_fetched[_fname].read_text(encoding="utf-8"), ref_prefix="### Odyss. "
        )
        _translations.update(_tr)
        TRANS_DESC.update(_desc)

    # Strip any <!-- ... --> annotation (e.g. an interlinear translator's
    # own echoed Greek source line) from every translator's stanza text --
    # a no-op for translators without one.
    _translations = {
        tr: {ref: eee.strip_comment_lines(txt) for ref, txt in d.items()}
        for tr, d in _translations.items()
    }

    STANZAS = [
        {
            "ref": ref,
            "lines": lines,
            # find_stanza_translation, not a bare d.get(ref, "—"): Pope and
            # Murray are transcribed against coarser "equivalent passage"
            # spans than this course's own per-lesson stanza split from
            # IX.39 onward (Πολυλάς stays fine-grained). interlinear_{en,el}
            # were ALSO coarser here until greek-knowledge-eee's KB was
            # re-split to match every lesson (like interlinear_ru already
            # did) -- allow_coarse_fallback=False is kept for interlinear
            # keys as a safety net: a coarse match there would mean extra
            # lines from a neighboring stanza, not a genuine equivalent
            # passage -- see eee-project's own find_stanza_translation
            # docstring.
            "translations": {
                tr: eee.find_stanza_translation(ref, d, allow_coarse_fallback=not tr.startswith("interlinear_"))
                for tr, d in _translations.items()
            },
        }
        for ref, lines in _greek.items()
    ]

    # ictus (rhythm) markup: one marked-up line per plain line, in the same
    # reading order as greek.md -- zipped by position, not re-keyed, so a plain
    # line's own accents/punctuation never need to match the markup exactly.
    _ictus_lines = _ictus_html.read_text(encoding="utf-8").splitlines()
    _all_plain_lines = [line for lines in _greek.values() for line in lines]
    RHYTHM_HTML = dict(zip(_all_plain_lines, _ictus_lines))
    return RHYTHM_HTML, STANZAS, TRANS_DESC


@app.cell(hide_code=True)
def _(
    ag_backend,
    cfg,
    eee,
    grc_lexicons,
    gu,
    lang_sel,
):
    from pathlib import Path

    _vocab_filename = (
        "vocab_IX_82-104.tsv" if lang_sel.value == "ru" else f"vocab_IX_82-104_{lang_sel.value}.tsv"
    )
    QUIZ_WORDS_RAW = gu.resolve_word_grammar(
        gu.load_inflected_vocab_tsv(_vocab_filename, nb_dir=Path(__file__).parent, remote_base=cfg.nb_remote("2026_07_06")),
        ag_backend, lang_sel.value
    )

    def _lexicon_tag(w):
        sources = eee.grc_lexicon_sources(w, lexicons=grc_lexicons)
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
        QUIZ_WORDS_RAW, "none",
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    ), n=SESSION_SIZE)

    eee.add_labels(QUIZ_WORDS)

    gu.reset_quiz_state(quiz_renew_btn, set_cv, set_remaining, set_score,
                         set_history, set_future, set_restore_entry)
    return (QUIZ_WORDS,)


@app.cell(hide_code=True)
def _(QUIZ_WORDS_RAW, build_paradigm_table, eee, grc_lexicons):
    CLICKABLE_FORMS = eee.grc_coverage_words(
        QUIZ_WORDS_RAW, "none",
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    )
    # words whose exact attested surface form is confirmed by the Homeric
    # corpus lexicon specifically -- highlighted (background) in the clickable
    # text so a reader can tell "Homer himself confirms this form" apart from
    # "some later-period lexicon in the combined engine reaches it".
    HOMER_WORDS = eee.grc_coverage_words(
        QUIZ_WORDS_RAW, "homer",
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    )
    return CLICKABLE_FORMS, HOMER_WORDS


@app.cell(hide_code=True)
def _(ag_backend, eee, grc_lexicons, lang_sel, mg, um_backend):
    build_paradigm_table = eee.build_grc_paradigm_table(ag_backend, um_backend, lang=lang_sel.value)
    build_period_tables = eee.build_grc_period_tables(
        ag_backend, um_backend,
        lexicons=grc_lexicons,
        el_backend=mg,
        require_lexicon="homer",
        lang=lang_sel.value,
    )
    return build_period_tables, build_paradigm_table


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(ODYSSEY_EXTRA_LEXICONS, mo):
    import sys as _sys
    import pathlib as _pl
    for _pth in _pl.Path(_sys.prefix).glob("lib/python*/site-packages/_editable_impl_*.pth"):
        _src = _pth.read_text().strip()
        if _src not in _sys.path:
            _sys.path.insert(0, _src)

    import eee_project as eee
    from ancient_greek_backend_eee import AncientGreekBackend
    from unimorph_backend_eee import UniMorphBackend
    from modern_greek_backend_eee import ModernGreekBackend

    # union recognizer for coverage + quiz — all diachronic rungs, incl. Classical Attic (pratt + ltrg + lsj)
    ag_backend = AncientGreekBackend.for_period("epic", "attic", "hellenistic_koine", "roman_koine", extra_lexicons=ODYSSEY_EXTRA_LEXICONS)
    # odyssey_morpheus is Epic-register, Odyssey-course-vocabulary-specific --
    # merged alongside homer (same register), not lsj/byzantine (Attic/Koine).
    ag_homer = AncientGreekBackend.for_period("epic", extra_lexicons=ODYSSEY_EXTRA_LEXICONS)
    ag_lsj = AncientGreekBackend.for_period("attic")
    ag_lxx = AncientGreekBackend.for_period("hellenistic_koine")
    ag_morphgnt = AncientGreekBackend.for_period("roman_koine")
    # byzantine is a sparse exceptions layer, not a standalone engine -- merge
    # onto the same Koine/Attic base the other rungs use so it inherits their
    # lemma coverage and only overrides the specific cells it documents.
    ag_byzantine = AncientGreekBackend.for_period("byzantine")
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
        um_backend,
    )


@app.cell(hide_code=True)
def _(cfg, gu):
    from pathlib import Path as _P
    NB_DIR = _P(__file__).parent
    NB_REMOTE = cfg.nb_remote("2026_07_06")
    for _f in (
        'Od_IX_82-104.pdf',
        'Od_IX_82-104_vocabula.pdf',
        'lotus_plant.jpg',
    ):
        gu.ensure_file(_f, nb_dir=NB_DIR, remote_base=NB_REMOTE)

    # Set True to underline words known to eee in the poem text (coverage view)
    return (NB_REMOTE,)


@app.cell(hide_code=True)
def _(cfg, lang_sel, mo):
    from eee_project.notebook_utils import eee_footer
    _prev_url, _next_url = cfg.adjacent_urls("2026_07_06/")
    eee_footer(mo, lang=lang_sel.value, prev_url=_prev_url, next_url=_next_url, same_window=True)
    return


@app.cell(hide_code=True)
def _(mo):
    from eee_project import language_bridge
    # own cell, undisplayed: a cell that also displays/uses this would
    # rerun (and reset the bridge) on every dependent re-render
    bridge = language_bridge(mo)
    return (bridge,)


@app.cell(hide_code=True)
def _(bridge, mo):
    from eee_project import language_selector
    # takes `bridge` as a parameter (not just via closure) so marimo
    # reruns this cell -- rebuilding the dropdown with the persisted
    # language -- the moment the browser's async localStorage read lands
    lang_sel = language_selector(mo, bridge)
    return (lang_sel,)


@app.cell(hide_code=True)
def _(bridge, lang_sel, mo):
    from eee_project import save_language_selection
    save_language_selection(bridge, lang_sel)
    mo.Html(f"""
    <div style="position:fixed;top:56px;right:12px;z-index:1000;
                background:white;padding:6px 10px;border-radius:8px;
                box-shadow:0 2px 8px rgba(0,0,0,.12);">
      {lang_sel}{bridge}
    </div>
    """)
    return


if __name__ == "__main__":
    app.run()
