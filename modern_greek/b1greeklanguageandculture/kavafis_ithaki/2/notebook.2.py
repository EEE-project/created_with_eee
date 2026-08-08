# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project>=1.1.0",
#     "marimo>=0.23.14",
#     "modern-greek-backend-eee>=1.0.0",
#     "pandas",
# ]
# ///

import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(language_selector, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://raw.githubusercontent.com/EEE-project/created_with_eee/main"
    cfg = ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/modern_greek/b1greeklanguageandculture/kavafis_ithaki/index.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=cfg.index_url(), lang=language_selector.value, titles={
        "ru": "Καβάφης — Ιθάκη", "el": "Καβάφης — Ιθάκη", "en": "Kavafis — Ithaki",
    }, ga_config=cfg.ga_config(), same_window=True)
    return


@app.cell(hide_code=True)
def _(img, language_selector, mo):
    # Title + badge + painting
    _lang = language_selector.value
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_HSFHB31SYFX7i6ibHwsh4a)"
    _heading = mo.md(f"# C. P. Cavafy — «Ithaki» {_badge}") if _lang == "en" else mo.md(f"# Κ. Π. Καβάφης — «Ιθάκη» {_badge}")
    if _lang == "ru":
        _subtitle = mo.md("Второй урок из цикла о стихотворении Константиноса Кавафиса «Итака» (1911): Лестригоны, Циклопы и Посейдон.")
    elif _lang == "el":
        _subtitle = mo.md("Δεύτερο μάθημα από τον κύκλο μαθημάτων για το ποίημα του Κ. Π. Καβάφη «Ιθάκη» (1911): οι Λαιστρυγόνες, οι Κύκλωπες και ο Ποσειδώνας.")
    else:
        _subtitle = mo.md("Second lesson in the series on Constantine P. Cavafy's poem «Ithaka» (1911): the Laestrygonians, the Cyclopes, and Poseidon.")
    _title = mo.vstack([_heading, _subtitle])
    _painting = img("painting.jpg", width=360)
    mo.hstack([_title, _painting], justify="space-between", align="start", gap=2)
    return


@app.cell(hide_code=True)
def _(img, language_selector, mo):
    # Recap of lesson 1
    _lang = language_selector.value
    _text = {
        "ru": r"""
            ## Повторение

            На прошлом уроке мы разобрали первые строки «Итаки»: кто такой Кавафис,
            что символизирует Итака, кто такой Одиссей и почему поэт желает, чтобы
            «путь был долгим».
            """,
        "el": r"""
            ## Επανάληψη

            Στο προηγούμενο μάθημα αναλύσαμε τους πρώτους στίχους της «Ιθάκης»:
            ποιος ήταν ο Καβάφης, τι συμβολίζει η Ιθάκη, ποιος ήταν ο Οδυσσέας και
            γιατί ο ποιητής εύχεται «να είναι μακρύς ο δρόμος».
            """,
    }.get(_lang, r"""
        ## Review

        In the previous lesson we looked at the opening lines of «Ithaka»: who
        Cavafy was, what Ithaka symbolizes, who Odysseus was, and why the poet
        wishes that «the road be long».
        """)
    mo.vstack([mo.md(_text), img("slide-1.jpg")])
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Poem section heading
    mo.md(t_ui("poem_section_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    _CITATION = (
        '<b>Κ. Π. Καβάφης, «Ιθάκη»</b> (1911). Δεύτερη στροφή, στίχοι 4–12. '
        '<a href="https://www.greek-language.gr/digitalResources/literature/tools/concordance/browse.html?cnd_id=9&text_id=658" target="_blank" rel="noopener">greek-language.gr — Πύλη για την ελληνική γλώσσα</a>'
    )
    mo.md(_CITATION)
    return


@app.cell(hide_code=True)
def _(TRANS_DESC, mo, trans_selector):
    _PODSTROCHNIK_DESC = "**подстрочник** · буквальный перевод слово-в-слово с сохранением порядка оригинала"
    _desc_map = {"подстрочник": _PODSTROCHNIK_DESC, **TRANS_DESC}
    mo.md(_desc_map.get(trans_selector.value, ""))
    return


@app.cell(hide_code=True)
def _(STANZAS, mo, trans_selector):
    # Plain (non-clickable) poem text alongside the selected parallel translation
    import html as _html
    _stanza = STANZAS[0]

    def _lines_html(lines, *, border=None):
        _divs = "".join(f'<div>{_html.escape(line)}</div>' for line in lines)
        _style = "font-size:1.0em;display:flex;flex-direction:column;justify-content:space-between;"
        if border:
            _style += f"border-left:3px solid {border};padding-left:0.8em"
        else:
            _style += "padding-right:0.8em"
        return mo.Html(f'<div style="{_style}">{_divs}</div>')

    _left = _lines_html(_stanza["lines"])
    _right = _lines_html(_stanza["translations"].get(trans_selector.value, "—").split("\n"), border="#ccc")

    mo.vstack([
        trans_selector,
        mo.hstack([_left, _right], justify="start", align="stretch", gap=1.5),
    ])
    return


@app.cell(hide_code=True)
def _(img, language_selector, mo):
    # Who were they + metaphorical meaning + verse analysis + discussion + closing
    _lang = language_selector.value
    _texts = {
        "ru": (
            r"""
            ## Кто они такие

            **Лестригоны** — людоеды-великаны, разрушавшие корабли чужеземцев и
            убивавшие их людей; символ больших опасностей и разрушений.

            **Циклопы** — великаны с одним глазом на лбу, обладавшие огромной силой
            и жившие в одиночестве; символ насилия, грубой силы и отсутствия
            культуры.

            **Посейдон** — бог моря, враг Одиссея (тот ослепил его сына Полифема);
            символ сил, которые мы не можем контролировать — природы, судьбы,
            обстоятельств.

            У Кавафиса эти образы — не просто мифологические персонажи, они имеют
            более глубокий, символический смысл.
            """,
            r"""
            ## Переносный смысл

            Эти образы могут символизировать: наши страхи, тревогу, неуверенность,
            трудности, проблемы, людей, которые нас разочаровывают, препятствия,
            которые мы создаём сами.
            """,
            r"""
            ## Анализ стихов

            Особое внимание — строкам «если не носишь их в своей душе, если твоя
            душа не ставит их перед тобой». Что значит «носить с собой страх»?
            Может ли человек сам создавать себе проблемы? Боялись ли вы когда-нибудь
            того, что в итоге не случилось?

            **Вопросы для обсуждения:**
            - Находятся ли наши самые большие страхи внутри нас или вовне?
            - Согласны ли вы, что мы часто сами создаём себе проблемы?
            - Если бы Одиссей жил в 2026 году, с какими трудностями он бы
              столкнулся?
            """,
            r"""
            ## Заключение

            Наши главные враги не всегда — внешние трудности. Часто это страхи,
            сомнения и негативные мысли, которые мы носим внутри себя. Когда
            меняется наше отношение к жизни, меняется и само путешествие.

            *Подумайте до следующего урока: кто ваши собственные «Лестригоны»,
            «Циклопы» и «Посейдон»? Это внешние препятствия, или, может быть,
            некоторые из них находятся внутри нас?*
            """,
        ),
        "el": (
            r"""
            ## Ποιοι ήταν

            **Οι Λαιστρυγόνες** — ανθρωποφάγοι γίγαντες, κατέστρεφαν τα πλοία των
            ξένων και έτρωγαν τους ανθρώπους τους· σύμβολο των μεγάλων κινδύνων και
            των καταστροφών.

            **Οι Κύκλωπες** — γίγαντες με ένα μόνο μάτι στο μέτωπο, με τεράστια
            δύναμη και απομονωμένη ζωή· σύμβολο της βίας, της ωμής δύναμης και της
            έλλειψης πολιτισμού.

            **Ο Ποσειδώνας** — θεός της θάλασσας, εχθρός του Οδυσσέα (αφού ο
            Οδυσσέας τύφλωσε τον γιο του, τον Πολύφημο)· σύμβολο των δυνάμεων που
            δεν μπορούμε να ελέγξουμε — η φύση, η μοίρα, οι συγκυρίες.

            Στον Καβάφη οι μορφές αυτές δεν είναι μόνο μυθολογικά πρόσωπα· έχουν
            και βαθύτερο, συμβολικό νόημα.
            """,
            r"""
            ## Μεταφορικό νόημα

            Μπορεί να συμβολίζουν: τους φόβους μας, το άγχος, την ανασφάλεια, τις
            δυσκολίες, τα προβλήματα, τους ανθρώπους που μας απογοητεύουν, τα
            εμπόδια που δημιουργούμε μόνοι μας.
            """,
            r"""
            ## Ανάλυση των στίχων

            Ιδιαίτερη προσοχή στους στίχους «αν δεν τους κουβανείς μες στην ψυχή
            σου, αν η ψυχή σου δεν τους στήνει εμπρός σου». Τι σημαίνει «κουβαλώ
            έναν φόβο»; Μπορεί ο άνθρωπος να δημιουργεί μόνος του τα προβλήματά
            του; Έχετε φοβηθεί ποτέ κάτι που τελικά δεν συνέβη;

            **Ερωτήσεις για συζήτηση:**
            - Πιστεύετε ότι οι μεγαλύτεροι φόβοι μας βρίσκονται μέσα μας ή έξω από
              εμάς;
            - Συμφωνείτε ότι πολλές φορές δημιουργούμε μόνοι μας τα προβλήματά
              μας;
            - Αν ο Οδυσσέας ζούσε το 2026, ποιες δυσκολίες θα αντιμετώπιζε;
            """,
            r"""
            ## Κλείσιμο

            Οι μεγαλύτεροι εχθροί μας δεν είναι πάντα οι εξωτερικές δυσκολίες.
            Συχνά είναι οι φόβοι, οι αμφιβολίες και οι αρνητικές σκέψεις που
            κουβαλάμε μέσα μας. Όταν αλλάζει η στάση μας απέναντι στη ζωή, αλλάζει
            και το ίδιο το ταξίδι.

            *Σκεφτείτε μέχρι το επόμενο μάθημα: ποιοι είναι οι δικοί σας
            «Λαιστρυγόνες», οι «Κύκλωπες» και ο «Ποσειδώνας»; Είναι εξωτερικά
            εμπόδια ή μήπως κάποιοι από αυτούς βρίσκονται μέσα μας;*
            """,
        ),
    }.get(_lang, (
        r"""
        ## Who they were

        **The Laestrygonians** — man-eating giants who destroyed the ships of
        strangers and killed their crews; a symbol of great dangers and
        destruction.

        **The Cyclopes** — giants with a single eye on the forehead, possessing
        enormous strength and living in isolation; a symbol of violence, brute
        force, and the absence of civilization.

        **Poseidon** — the god of the sea, Odysseus's enemy (since Odysseus
        blinded his son Polyphemus); a symbol of the forces we cannot control —
        nature, fate, circumstance.

        For Cavafy, these figures are not just mythological characters — they
        carry a deeper, symbolic meaning.
        """,
        r"""
        ## Metaphorical meaning

        These figures can symbolize: our fears, anxiety, insecurity,
        difficulties, problems, people who disappoint us, obstacles we create
        for ourselves.
        """,
        r"""
        ## Analysis of the verses

        Particular attention to the lines «if you don't carry them within your
        soul, if your soul doesn't set them up before you». What does it mean to
        «carry a fear»? Can a person create their own problems? Have you ever
        feared something that, in the end, never happened?

        **Discussion questions:**
        - Are our greatest fears inside us or outside us?
        - Do you agree that we often create our own problems?
        - If Odysseus lived in 2026, what difficulties would he face?
        """,
        r"""
        ## Closing

        Our greatest enemies are not always external difficulties. Often they
        are the fears, doubts, and negative thoughts we carry within ourselves.
        When our attitude toward life changes, the journey itself changes too.

        *Think about this before the next lesson: who are your own
        "Laestrygonians," "Cyclopes," and "Poseidon"? Are they external
        obstacles, or might some of them be within us?*
        """,
    ))
    mo.vstack([
        mo.md(_texts[0]),
        img("slide-3.jpg"),
        mo.md(_texts[1]),
        img("slide-4.jpg"),
        mo.md(_texts[2]),
        img("slide-5.jpg"),
        img("slide-6.jpg"),
        mo.md(_texts[3]),
        img("slide-7.jpg"),
    ])
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 1 heading -- presence exercise leads (poem-specific, right after the poem)
    _lang = language_selector.value
    mo.md(f"## {t_ui('test_label', _lang)} 1: {t_ui('presence_test_topic', _lang)}")
    return


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
def _(gu2):
    tp_renew_btn = gu2.make_renew_button()
    return (tp_renew_btn,)


@app.cell(hide_code=True)
def _(
    POEM_WORDS_RAW,
    RAW_BASE,
    STANZAS,
    eee,
    gu2,
    notebook_dir,
    tp_renew_btn,
    tp_set_cv,
    tp_set_future,
    tp_set_history,
    tp_set_remaining,
    tp_set_restore_entry,
    tp_set_score,
):
    LITERARY_TRANSLATORS = ["Шмаков/Бродский", "Ильинская", "Левитов"]
    _tp_vocab = [w for w in POEM_WORDS_RAW if w.get("pos") in eee.TRANSLATION_PRESENCE_CONTENT_POS]
    _tp_path = gu2.ensure_file("translation_presence.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
    # An empty TP_ITEMS list on its own is indistinguishable downstream from
    # "quiz genuinely completed" (both leave translation_presence_widgets
    # with no current item, i.e. the same done-screen) -- TP_UNAVAILABLE
    # lets the rendering cell show an honest not-found message instead,
    # matching how the noun/verb/adjective sections already handle a
    # missing TSV.
    TP_UNAVAILABLE = _tp_path is None
    if _tp_path:
        gu2.sync_translation_presence_tsv(_tp_vocab, LITERARY_TRANSLATORS, STANZAS, _tp_path)
        TP_ITEMS = gu2.balance_presence_items(gu2.build_translation_presence_items(
            gu2.read_translation_presence_tsv(_tp_path), POEM_WORDS_RAW, STANZAS
        ), n=None)
    else:
        TP_ITEMS = []
    gu2.reset_quiz_state(tp_renew_btn, tp_set_cv, tp_set_remaining, tp_set_score,
                          tp_set_history, tp_set_future, tp_set_restore_entry)
    return TP_ITEMS, TP_UNAVAILABLE


@app.cell(hide_code=True)
def _(
    TP_ITEMS,
    gu2,
    language_selector,
    tp_cv,
    tp_history,
    tp_remaining,
    tp_restore_entry,
):
    _ = tp_cv()
    tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch = gu2.translation_presence_widgets(
        cv=tp_cv(),
        remaining=tp_remaining(),
        items=TP_ITEMS,
        restore_entry=tp_restore_entry(),
        history_len=len(tp_history()),
        lang=language_selector.value,
    )
    return tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch


@app.cell(hide_code=True)
def _(
    TP_ITEMS,
    TP_UNAVAILABLE,
    gu2,
    language_selector,
    mo,
    t_ui,
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
    if TP_UNAVAILABLE:
        _output = mo.md(t_ui("translation_presence_not_found", language_selector.value))
    else:
        _output = gu2.translation_presence_form(
            tp_cv, tp_set_cv, tp_remaining, tp_set_remaining,
            tp_score, tp_set_score, tp_restore_entry, tp_set_restore_entry,
            tp_history, tp_set_history, tp_future, tp_set_future,
            tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch,
            items=TP_ITEMS,
            lang=language_selector.value,
            renew_btn=tp_renew_btn,
        )
    _output
    return


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, notebook_dir, pd):
    # Vocabulary data (useful expressions + literary terms)
    _vocab_path = gu2.ensure_file("vocabulary.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
    df_vocab = pd.read_csv(_vocab_path, sep='\t') if _vocab_path else None
    return (df_vocab,)


@app.cell(hide_code=True)
def _(df_vocab, language_selector, mo, t_ui):
    # Vocabulary table
    _lang = language_selector.value
    _tbl_vocab = mo.ui.table(df_vocab, selection="multi") if df_vocab is not None else None
    mo.vstack([
        mo.md(t_ui("vocabulary_heading", _lang)),
        _tbl_vocab,
    ])
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 2 heading
    _lang = language_selector.value
    mo.md(f"## {t_ui('test_label', _lang)} 2: {t_ui('noun_test_topic', _lang)}")
    return


@app.cell(hide_code=True)
def _(mo):
    # Noun file upload
    file_upload_noun = mo.ui.file(label="Load nouns TSV")
    file_upload_noun
    return (file_upload_noun,)


@app.cell(hide_code=True)
def _(RAW_BASE, file_upload_noun, gu2, notebook_dir, pd):
    # Load noun data
    if file_upload_noun.value:
        df_noun = gu2.load_data(file_upload_noun, [])
    else:
        _noun_path = gu2.ensure_file("nouns.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
        df_noun = pd.read_csv(_noun_path, sep='\t') if _noun_path else None
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, language_selector, mo, t_ui):
    # Noun table
    table_noun = mo.ui.table(df_noun, selection="multi", initial_selection=None) if df_noun is not None else None
    _lang = language_selector.value
    _table_noun = table_noun if table_noun is not None else mo.md(t_ui("nouns_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_nouns", _lang)), _table_noun])
    return (table_noun,)


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Noun mode selector
    _lang = language_selector.value
    if _lang == 'ru':
        _opts_n = {"без артикля": "simple", "с артиклем": "article"}
        _default_mode_n = "без артикля"
    elif _lang == 'el':
        _opts_n = {"χωρίς άρθρο": "simple", "με άρθρο": "article"}
        _default_mode_n = "χωρίς άρθρο"
    else:
        _opts_n = {"no article": "simple", "with article": "article"}
        _default_mode_n = "no article"
    mode_selector_n = mo.ui.radio(options=_opts_n, value=_default_mode_n, label=t_ui("mode_label", _lang))
    mo.md(f"{mode_selector_n}")
    return (mode_selector_n,)


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Noun indefinite-article toggle (creation only)
    indefinite_toggle_n = mo.ui.switch(label=t_ui("indefinite_label", language_selector.value), value=False)
    return (indefinite_toggle_n,)


@app.cell(hide_code=True)
def _(indefinite_toggle_n, mo, mode_selector_n):
    indefinite_toggle_n if mode_selector_n.value == "article" else mo.md("")
    return


@app.cell(hide_code=True)
def _(gu2, random, table_noun):
    # Noun words + state
    words_noun = gu2.get_words(table_noun)
    (words4test_noun, set_words4test_noun, hist_noun, set_hist_noun, noun_msg, set_noun_msg,
     captured_noun, set_captured_noun, entered_noun, set_entered_noun,
     submit_count_n, set_submit_count_n, prev_count_n, set_prev_count_n,
     next_count_n, set_next_count_n, enter_count_n, set_enter_count_n,
     restart_count_n, set_restart_count_n) = gu2.make_paradigm_drill_state(
        random.sample(words_noun, len(words_noun)) if words_noun else []
    )
    return (
        captured_noun,
        enter_count_n,
        entered_noun,
        hist_noun,
        next_count_n,
        noun_msg,
        prev_count_n,
        restart_count_n,
        set_captured_noun,
        set_enter_count_n,
        set_entered_noun,
        set_hist_noun,
        set_next_count_n,
        set_noun_msg,
        set_prev_count_n,
        set_restart_count_n,
        set_submit_count_n,
        set_words4test_noun,
        submit_count_n,
        words4test_noun,
        words_noun,
    )


@app.cell(hide_code=True)
def _(
    entered_noun,
    gu2,
    hist_noun,
    indefinite_toggle_n,
    language_selector,
    mode_selector_n,
    set_enter_count_n,
    set_next_count_n,
    set_prev_count_n,
    t_ui,
    words4test_noun,
):
    # Noun form
    cv_noun = words4test_noun()[0] if words4test_noun() else None
    noun_meta = gu2.noun_drill_meta(cv_noun["Word"]) if cv_noun else None
    _ac_noun = getattr(noun_meta, "active_cases", [])
    _entered_noun_form = entered_noun().get(cv_noun["Word"]) if cv_noun else None
    _lang_n = language_selector.value
    _article_n = mode_selector_n.value == "article"
    _indef_n = indefinite_toggle_n.value and _article_n
    _labels_noun = gu2.noun_slot_labels(_ac_noun, lang=_lang_n)
    if _article_n:
        _def_prefix = t_ui("def_prefix", _lang_n)
        _labels_noun = [f"{_def_prefix} {_l}" for _l in _labels_noun]
    if _indef_n:
        _indef_prefix = t_ui("indef_prefix", _lang_n)
        _labels_noun = _labels_noun + [f"{_indef_prefix} {_l}" for _l in gu2.noun_slot_labels(gu2.noun_indef_cells(_ac_noun), lang=_lang_n)]
    noun_form, prev_btn_n, next_btn_n, restart_btn_n = gu2.paradigm_drill_widgets(
        labels=_labels_noun,
        values=_entered_noun_form,
        history_len=len(hist_noun()),
        remaining_len=len(words4test_noun()),
        lang=_lang_n,
    )
    set_prev_count_n(0)
    set_next_count_n(0)
    set_enter_count_n(0)
    return cv_noun, next_btn_n, noun_form, noun_meta, prev_btn_n, restart_btn_n


@app.cell(hide_code=True)
def _(
    captured_noun,
    cv_noun,
    gu2,
    language_selector,
    noun_form,
    set_submit_count_n,
    t_ui,
):
    # Noun check button
    check_btn_n = gu2.dirty_check_button(
        noun_form, captured_noun, cv_noun, "test_word", word_key="Word",
        label=t_ui("check_label", language_selector.value),
    )
    set_submit_count_n(0)
    return (check_btn_n,)


@app.cell(hide_code=True)
def _(
    captured_noun,
    check_btn_n,
    cv_noun,
    enter_count_n,
    entered_noun,
    gu2,
    hist_noun,
    indefinite_toggle_n,
    language_selector,
    mo,
    mode_selector_n,
    next_btn_n,
    next_count_n,
    noun_form,
    noun_meta,
    noun_msg,
    prev_btn_n,
    prev_count_n,
    restart_btn_n,
    restart_count_n,
    set_captured_noun,
    set_enter_count_n,
    set_entered_noun,
    set_hist_noun,
    set_next_count_n,
    set_noun_msg,
    set_prev_count_n,
    set_restart_count_n,
    set_submit_count_n,
    set_words4test_noun,
    submit_count_n,
    t_ui,
    words4test_noun,
    words_noun,
):
    # Noun drill
    _lang = language_selector.value
    _article = mode_selector_n.value == "article"
    _indef_n = indefinite_toggle_n.value and _article
    _title = t_ui("article_noun_heading", _lang) if _article else t_ui("simple_noun_heading", _lang)
    gu2.noun_paradigm_drill_form(
        words4test_noun, set_words4test_noun, hist_noun, set_hist_noun, noun_msg, set_noun_msg,
        captured_noun, set_captured_noun, entered_noun, set_entered_noun,
        submit_count_n, set_submit_count_n, prev_count_n, set_prev_count_n,
        next_count_n, set_next_count_n, enter_count_n, set_enter_count_n,
        restart_count_n, set_restart_count_n,
        cv_noun, noun_form, check_btn_n, prev_btn_n, next_btn_n, restart_btn_n,
        vocab=words_noun,
        noun_meta=noun_meta,
        article=_article,
        indefinite=_indef_n,
        word_key="Word",
        meaning_key="Translation",
        meaning_label=t_ui("translation_label", _lang).rstrip(":"),
        title=_title,
        done_message=t_ui("test1_done", _lang),
    ) if words_noun else mo.md(t_ui("noun_empty", _lang))
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 3 heading
    _lang = language_selector.value
    mo.md(f"## {t_ui('test_label', _lang)} 3: {t_ui('verb_test_topic', _lang)}")
    return


@app.cell(hide_code=True)
def _(mo):
    # Verb file upload
    file_upload_verb = mo.ui.file(label="Load verbs TSV")
    file_upload_verb
    return (file_upload_verb,)


@app.cell(hide_code=True)
def _(RAW_BASE, file_upload_verb, gu2, notebook_dir, pd):
    # Load verb data
    if file_upload_verb.value:
        df_verb = gu2.load_data(file_upload_verb, [])
    else:
        _verb_path = gu2.ensure_file("verbs.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
        df_verb = pd.read_csv(_verb_path, sep='\t') if _verb_path else None
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, language_selector, mo, t_ui):
    # Verb table
    table_verb = mo.ui.table(df_verb, selection="multi", initial_selection=None) if df_verb is not None else None
    _lang = language_selector.value
    _table_verb = table_verb if table_verb is not None else mo.md(t_ui("verbs_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_verbs", _lang)), _table_verb])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu2, language_selector, mo, t_ui):
    # Tense selector
    _lang = language_selector.value
    _tense_options = gu2.tense_dropdown_options(lang=_lang)
    _first_key = next(iter(_tense_options))
    tense_selector = mo.ui.dropdown(
        options=_tense_options,
        value=_first_key,
        label=t_ui("tense_label", _lang),
    )
    tense_selector
    return (tense_selector,)


@app.cell(hide_code=True)
def _(gu2, random, table_verb):
    # Verb words + state
    words_verb = gu2.get_words(table_verb)
    (words4test_verb, set_words4test_verb, hist_verb, set_hist_verb, verb_msg, set_verb_msg,
     captured_verb, set_captured_verb, entered_verb, set_entered_verb,
     submit_count_v, set_submit_count_v, prev_count_v, set_prev_count_v,
     next_count_v, set_next_count_v, enter_count_v, set_enter_count_v,
     restart_count_v, set_restart_count_v) = gu2.make_paradigm_drill_state(
        random.sample(words_verb, len(words_verb)) if words_verb else []
    )
    return (
        captured_verb,
        enter_count_v,
        entered_verb,
        hist_verb,
        next_count_v,
        prev_count_v,
        restart_count_v,
        set_captured_verb,
        set_enter_count_v,
        set_entered_verb,
        set_hist_verb,
        set_next_count_v,
        set_prev_count_v,
        set_restart_count_v,
        set_submit_count_v,
        set_verb_msg,
        set_words4test_verb,
        submit_count_v,
        verb_msg,
        words4test_verb,
        words_verb,
    )


@app.cell(hide_code=True)
def _(
    entered_verb,
    gu2,
    hist_verb,
    language_selector,
    set_enter_count_v,
    set_next_count_v,
    set_prev_count_v,
    tense_selector,
    words4test_verb,
):
    # Verb form
    cv_verb = words4test_verb()[0] if words4test_verb() else None
    _ = tense_selector.value  # rebuild the form (clear stale input) when the tense changes
    _entered_verb_form = entered_verb().get(cv_verb["Word"]) if cv_verb else None
    verb_form, prev_btn_v, next_btn_v, restart_btn_v = gu2.paradigm_drill_widgets(
        labels=gu2.verb_slot_labels(),
        values=_entered_verb_form,
        history_len=len(hist_verb()),
        remaining_len=len(words4test_verb()),
        lang=language_selector.value,
    )
    set_prev_count_v(0)
    set_next_count_v(0)
    set_enter_count_v(0)
    return cv_verb, next_btn_v, prev_btn_v, restart_btn_v, verb_form


@app.cell(hide_code=True)
def _(
    captured_verb,
    cv_verb,
    gu2,
    language_selector,
    set_submit_count_v,
    t_ui,
    verb_form,
):
    # Verb check button
    check_btn_v = gu2.dirty_check_button(
        verb_form, captured_verb, cv_verb, "verb_word", word_key="Word",
        label=t_ui("check_label", language_selector.value),
    )
    set_submit_count_v(0)
    return (check_btn_v,)


@app.cell(hide_code=True)
def _(
    captured_verb,
    check_btn_v,
    cv_verb,
    enter_count_v,
    entered_verb,
    gu2,
    hist_verb,
    language_selector,
    mo,
    next_btn_v,
    next_count_v,
    prev_btn_v,
    prev_count_v,
    restart_btn_v,
    restart_count_v,
    set_captured_verb,
    set_enter_count_v,
    set_entered_verb,
    set_hist_verb,
    set_next_count_v,
    set_prev_count_v,
    set_restart_count_v,
    set_submit_count_v,
    set_verb_msg,
    set_words4test_verb,
    submit_count_v,
    t_ui,
    tense_selector,
    verb_form,
    verb_msg,
    words4test_verb,
    words_verb,
):
    # Verb drill
    _lang = language_selector.value
    _tense_key = tense_selector.value
    if words_verb and _tense_key:
        _tlabel = gu2.TENSE_LABELS[_tense_key]["greek"]
        _output = gu2.verb_paradigm_drill_form(
            words4test_verb, set_words4test_verb, hist_verb, set_hist_verb, verb_msg, set_verb_msg,
            captured_verb, set_captured_verb, entered_verb, set_entered_verb,
            submit_count_v, set_submit_count_v, prev_count_v, set_prev_count_v,
            next_count_v, set_next_count_v, enter_count_v, set_enter_count_v,
            restart_count_v, set_restart_count_v,
            cv_verb, verb_form, check_btn_v, prev_btn_v, next_btn_v, restart_btn_v,
            vocab=words_verb,
            tense=_tense_key,
            word_key="Word",
            meaning_key="Translation",
            meaning_label=t_ui("translation_label", _lang).rstrip(":"),
            title=f"{t_ui('verb_heading', _lang)} — {_tlabel}",
            done_message=t_ui("test2_done", _lang),
        )
    elif not words_verb:
        _output = mo.md(t_ui("verb_empty", _lang))
    else:
        _output = mo.md(t_ui("verb_no_tense", _lang))
    _output
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 4 heading
    _lang = language_selector.value
    mo.md(f"## {t_ui('test_label', _lang)} 4: {t_ui('adj_test_topic', _lang)}")
    return


@app.cell(hide_code=True)
def _(mo):
    # Adjective file upload
    file_upload_adj = mo.ui.file(label="Load adjectives TSV")
    file_upload_adj
    return (file_upload_adj,)


@app.cell(hide_code=True)
def _(RAW_BASE, file_upload_adj, gu2, notebook_dir, pd):
    # Load adjective data
    if file_upload_adj.value:
        df_adj = gu2.load_data(file_upload_adj, [])
    else:
        _adj_path = gu2.ensure_file("adjectives.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
        df_adj = pd.read_csv(_adj_path, sep='\t') if _adj_path else None
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, language_selector, mo, t_ui):
    # Adjective table
    table_adj = mo.ui.table(df_adj, selection="multi", initial_selection=None) if df_adj is not None else None
    _lang = language_selector.value
    _table_adj = table_adj if table_adj is not None else mo.md(t_ui("adjs_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_adjs", _lang)), _table_adj])
    return (table_adj,)


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Mode selector
    _lang = language_selector.value
    if _lang == 'ru':
        _opts = {"Простой: 3 рода × 2 числа (6 полей)": "simple", "Полный: все роды, числа и падежи (18 полей)": "complex"}
        _default_mode = "Простой: 3 рода × 2 числа (6 полей)"
    elif _lang == 'el':
        _opts = {"Απλό: 3 γένη × 2 αριθμοί (6 πεδία)": "simple", "Πλήρες: όλα τα γένη, αριθμοί και πτώσεις (18 πεδία)": "complex"}
        _default_mode = "Απλό: 3 γένη × 2 αριθμοί (6 πεδία)"
    else:
        _opts = {"Simple: 3 genders × 2 numbers (6 fields)": "simple", "Full: all genders, numbers, and cases (18 fields)": "complex"}
        _default_mode = "Simple: 3 genders × 2 numbers (6 fields)"
    mode_selector = mo.ui.radio(options=_opts, value=_default_mode, label=t_ui("mode_label", _lang))
    mo.md(f"{mode_selector}")
    return (mode_selector,)


@app.cell(hide_code=True)
def _(gu2, random, table_adj):
    # Adjective words + state
    words_adj = gu2.get_words(table_adj)
    (words4test_adj, set_words4test_adj, hist_adj, set_hist_adj, adj_msg, set_adj_msg,
     captured_adj, set_captured_adj, entered_adj, set_entered_adj,
     submit_count_a, set_submit_count_a, prev_count_a, set_prev_count_a,
     next_count_a, set_next_count_a, enter_count_a, set_enter_count_a,
     restart_count_a, set_restart_count_a) = gu2.make_paradigm_drill_state(
        random.sample(words_adj, len(words_adj)) if words_adj else []
    )
    return (
        adj_msg,
        captured_adj,
        enter_count_a,
        entered_adj,
        hist_adj,
        next_count_a,
        prev_count_a,
        restart_count_a,
        set_adj_msg,
        set_captured_adj,
        set_enter_count_a,
        set_entered_adj,
        set_hist_adj,
        set_next_count_a,
        set_prev_count_a,
        set_restart_count_a,
        set_submit_count_a,
        set_words4test_adj,
        submit_count_a,
        words4test_adj,
        words_adj,
    )


@app.cell(hide_code=True)
def _(
    entered_adj,
    gu2,
    hist_adj,
    language_selector,
    mode_selector,
    set_enter_count_a,
    set_next_count_a,
    set_prev_count_a,
    words4test_adj,
):
    # Adjective form
    cv_adj = words4test_adj()[0] if words4test_adj() else None
    _mode = mode_selector.value
    _entered_adj_form = entered_adj().get(cv_adj["Word"]) if cv_adj else None
    adj_form, prev_btn_a, next_btn_a, restart_btn_a = gu2.paradigm_drill_widgets(
        labels=gu2.adjective_slot_labels(_mode, lang=language_selector.value),
        values=_entered_adj_form,
        history_len=len(hist_adj()),
        remaining_len=len(words4test_adj()),
        lang=language_selector.value,
    )
    set_prev_count_a(0)
    set_next_count_a(0)
    set_enter_count_a(0)
    return adj_form, cv_adj, next_btn_a, prev_btn_a, restart_btn_a


@app.cell(hide_code=True)
def _(
    adj_form,
    captured_adj,
    cv_adj,
    gu2,
    language_selector,
    set_submit_count_a,
    t_ui,
):
    # Adjective check button
    check_btn_a = gu2.dirty_check_button(
        adj_form, captured_adj, cv_adj, "adj_word", word_key="Word",
        label=t_ui("check_label", language_selector.value),
    )
    set_submit_count_a(0)
    return (check_btn_a,)


@app.cell(hide_code=True)
def _(
    adj_form,
    adj_msg,
    captured_adj,
    check_btn_a,
    cv_adj,
    enter_count_a,
    entered_adj,
    gu2,
    hist_adj,
    language_selector,
    mo,
    mode_selector,
    next_btn_a,
    next_count_a,
    prev_btn_a,
    prev_count_a,
    restart_btn_a,
    restart_count_a,
    set_adj_msg,
    set_captured_adj,
    set_enter_count_a,
    set_entered_adj,
    set_hist_adj,
    set_next_count_a,
    set_prev_count_a,
    set_restart_count_a,
    set_submit_count_a,
    set_words4test_adj,
    submit_count_a,
    t_ui,
    words4test_adj,
    words_adj,
):
    # Adjective drill
    _lang = language_selector.value
    _mode = mode_selector.value
    gu2.adjective_paradigm_drill_form(
        words4test_adj, set_words4test_adj, hist_adj, set_hist_adj, adj_msg, set_adj_msg,
        captured_adj, set_captured_adj, entered_adj, set_entered_adj,
        submit_count_a, set_submit_count_a, prev_count_a, set_prev_count_a,
        next_count_a, set_next_count_a, enter_count_a, set_enter_count_a,
        restart_count_a, set_restart_count_a,
        cv_adj, adj_form, check_btn_a, prev_btn_a, next_btn_a, restart_btn_a,
        vocab=words_adj,
        mode=_mode,
        word_key="Word",
        meaning_key="Translation",
        meaning_label=t_ui("translation_label", _lang).rstrip(":"),
        title=t_ui("adj_heading", _lang),
        done_message=t_ui("test3_done", _lang),
    ) if words_adj else mo.md(t_ui("adj_empty", _lang))
    return


@app.cell(hide_code=True)
def _(mo):
    # Fixed-position language selector overlay
    language_selector = mo.ui.dropdown(
        options={"Русский": "ru", "Ελληνικά": "el"},
        value="Ελληνικά",
        label="🌐",
    )
    mo.Html(f"""
    <div style="position: fixed; top: 60px; right: 10px; z-index: 1000; background: white; padding: 8px 12px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
        {language_selector}
    </div>
    """)
    return (language_selector,)


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    trans_selector = mo.ui.dropdown(
        options={
            "подстрочник": "подстрочник",
            "Шмаков / Бродский · рус.": "Шмаков/Бродский",
            "Ильинская (1984) · рус.": "Ильинская",
            "Левитов · рус.": "Левитов",
        },
        value="подстрочник",
        label=t_ui("translation_label", language_selector.value).rstrip(":"),
    )
    return (trans_selector,)


@app.cell(hide_code=True)
def _(gu2):
    t_ui = gu2.ui_label
    return (t_ui,)


@app.cell(hide_code=True)
def _(eee, mo, notebook_dir):
    from pathlib import Path as _Path
    RAW_BASE = "https://raw.githubusercontent.com/EEE-project/created_with_eee/main/modern_greek/b1greeklanguageandculture/kavafis_ithaki/2"
    def img(name, width=700):
        return eee.magnify_image(mo, _Path(notebook_dir) / name, raw_base=RAW_BASE, width=width, prefer_local=True)

    return RAW_BASE, img


@app.cell(hide_code=True)
def _(RAW_BASE, eee, gu2, notebook_dir):
    # molab only bundles files that live alongside the notebook when it's
    # imported from a published repo URL -- a raw single-file upload (the
    # only option before this course is committed/pushed) leaves siblings
    # like greek.md/translations.md behind, so route them through
    # ensure_file() rather than a bare local read (see created_with_eee's
    # root CLAUDE.md, "Notebook Content Gotchas"). The two files are
    # unrelated, so fetch them concurrently rather than paying for two
    # sequential round-trips on a cold cache.
    from concurrent.futures import ThreadPoolExecutor as _Pool
    with _Pool(max_workers=2) as _pool:
        _greek_path, _trans_path = _pool.map(
            lambda _fn: gu2.ensure_file(_fn, nb_dir=notebook_dir, remote_base=RAW_BASE),
            ("greek.md", "translations.md"),
        )
    if not _greek_path or not _trans_path:
        raise FileNotFoundError("greek.md/translations.md: could not be found locally or fetched from remote_base")
    _greek = eee.parse_stanza_text(_greek_path.read_text(encoding="utf-8"))
    _trans, _desc = eee.parse_stanza_translations(_trans_path.read_text(encoding="utf-8"))
    TRANS_DESC = _desc
    STANZAS = [
        {
            "ref": ref,
            "lines": lines,
            "translations": {tr: d.get(ref, "—") for tr, d in _trans.items()},
        }
        for ref, lines in _greek.items()
    ]
    return STANZAS, TRANS_DESC


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, notebook_dir):
    POEM_WORDS_RAW = gu2.load_inflected_vocab_tsv("poem_vocab.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
    return (POEM_WORDS_RAW,)


@app.cell(hide_code=True)
def _(language_selector, mo):
    from eee_project.notebook_utils import eee_footer
    eee_footer(mo, lang=language_selector.value)
    return


@app.cell(hide_code=True)
def _():
    import os, random, pandas as pd, marimo as mo
    import eee_project as eee
    from eee_project import GreekUtils, MODERN_GREEK
    from modern_greek_backend_eee import ModernGreekBackend
    _mg_backend = ModernGreekBackend()
    eee.register_backend("el", _mg_backend, backend="modern-greek")
    eee.set_chain("el", ["modern-greek"])
    gu2 = GreekUtils(_mg_backend, mo, pd, eee_module=eee, config=MODERN_GREEK)
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    return eee, gu2, mo, notebook_dir, pd, random


if __name__ == "__main__":
    app.run()
