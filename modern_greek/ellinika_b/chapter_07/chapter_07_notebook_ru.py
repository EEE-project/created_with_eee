# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.14",
#     "modern-greek-eee @ git+https://github.com/EEE-project/modern-greek-eee.git",
#     "modern-greek-inflexion-eee @ git+https://github.com/EEE-project/modern-greek-inflexion-eee.git",
#     "pandas",
# ]
# modern-greek-eee = { git = "https://github.com/EEE-project/modern-greek-eee" }
# modern-greek-inflexion-eee = { git = "https://github.com/EEE-project/modern-greek-inflexion-eee" }
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", html_head_file="head.html")


@app.cell(hide_code=True)
def _(mo):
    # Title
    mo.md("""
    # «Θυμάμαι ότι παίζαμε όλη μέρα...» 🏘️
    ## Глава 7 — Образы из прошлого · B1

    **Грамматика:** Παρατατικός (Α, Β1, Β2, Α/Β) · Временны́е союзы
    **Тесты:** Существительные · Глаголы · Прилагательные
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Vocabulary & Phrases
    mo.md("""
    ## Словарь и фразы (с. 106)

    ### Πώς το λένε; — Как сказать?

    - **Εδώ, τα λέγαμε…** — Вот, мы раньше говорили…
    - **Μα τι κατάσταση είναι αυτή;** — Ну что за дела!
    - **Αμάν πια!** — Ну сколько можно!
    - **Εμ, βέβαια!** — Ну конечно!
    - **Ακόμα και…** — Даже…
    - **Άκουσα ότι…** — Я слышал(а), что…
    - **Αλλά με όλα τα προβλήματά του…** — Но со всеми его/её проблемами…
    - **Όχι όπως τώρα που…** — Не то что сейчас, когда…
    - **Δεν είναι η μέρα σου σήμερα.** — Сегодня не твой день.
    - **Όλα μαύρα τα βλέπεις.** — Ты всё видишь в чёрном цвете.
    - **Μήπως σου φτιάξει το κέφι.** — Может, это поднимет тебе настроение.
    - **Τι να σας κεράσουμε;** — Чем вас угостить?

    ### Λέξεις, λέξεις — Слова, слова...

    | Греческий | Артикль | Русский |
    |:----------|:--------|:--------|
    | πεζοδρόμιο | το | тротуар |
    | πολυκατοικία | η | многоквартирный дом |
    | πράσινο | το | зелень / зелёные насаждения |
    | χωράφι | το | поле |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Grammar: Παρατατικός
    mo.md("""
    ## Грамматика: Παρατατικός (Прошедшее продолженное)

    Описывает **длительные или повторяющиеся** действия в прошлом.
    Маркеры времени: *κάθε μέρα* (каждый день), *συχνά* (часто), *πάντα* (всегда), *όταν ήμουν παιδί* (когда я был ребёнком).

    ### Тип А — окончания **-α, -ες, -ε, -αμε, -ατε, -αν(ε)**

    | Лицо | παίζω | πηγαίνω |
    |:-----|:------|:--------|
    | εγώ | **<span style="color:red">έ</span>παιζα** | **πήγαινα** |
    | εσύ | **<span style="color:red">έ</span>παιζες** | **πήγαινες** |
    | αυτός/ή/ό | **<span style="color:red">έ</span>παιζε** | **πήγαινε** |
    | εμείς | **παίζαμε** | **πηγαίναμε** |
    | εσείς | **παίζατε** | **πηγαίνατε** |
    | αυτοί/ές/ά | **<span style="color:red">έ</span>παιζαν / παίζανε** | **πήγαιναν / πηγαίνανε** |

    > Красное <span style="color:red">**έ-**</span> — приращение, добавляемое к кратким основам: γράφω→<span style="color:red">**έ**</span>γραφα, διαβάζω→**διά**βαζα.

    ### Тип Β1 (-άω) · два варианта · Тип Β2 (-ώ) · один вариант

    | Лицо | περνάω (Β1) | μπορώ (Β2) |
    |:-----|:------------|:-----------|
    | εγώ | **περνούσα** / **πέρναγα** | **μπορούσα** |
    | εσύ | **περνούσες** / **πέρναγες** | **μπορούσες** |
    | αυτός/ή/ό | **περνούσε** / **πέρναγε** | **μπορούσε** |
    | εμείς | **περνούσαμε** / **περνάγαμε** | **μπορούσαμε** |
    | εσείς | **περνούσατε** / **περνάγατε** | **μπορούσατε** |
    | αυτοί/ές/ά | **περνούσαν(ε)** / **πέρναγαν** | **μπορούσαν(ε)** |

    ### Тип Α/Β — вставка **-γ-** *(ακούω, καίω, λέω, κλαίω, τρώω, φταίω)*

    | Лицо | ακούω |
    |:-----|:------|
    | εγώ | **άκου<span style="color:red">γ</span>α** |
    | εσύ | **άκου<span style="color:red">γ</span>ες** |
    | αυτός/ή/ό | **άκου<span style="color:red">γ</span>ε** |
    | εμείς | **ακού<span style="color:red">γ</span>αμε** |
    | εσείς | **ακού<span style="color:red">γ</span>ατε** |
    | αυτοί/ές/ά | **άκου<span style="color:red">γ</span>αν / ακού<span style="color:red">γ</span>ανε** |

    > Красное <span style="color:red">**-γ-**</span> вставляется перед окончанием: λέω→<span style="color:red">**έ</span>λε**<span style="color:red">**γ**</span>α, τρώω→<span style="color:red">**έ**</span>τρω<span style="color:red">**γ**</span>α

    ### Глаголы-исключения

    | Глагол | Παρατατικός |
    |:-------|:------------|
    | θέλω | **ήθελα** |
    | ξέρω | **ήξερα** |
    | υπάρχω | **υπήρχα** |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Grammar: Time connectors
    mo.md("""
    ## Грамматика: Временны́е союзы с Παρατατικός

    ### Παρατατικός + Παρατατικός — два одновременных длительных действия

    Союзы: **Όταν** (когда), **Ενώ** (в то время как), **Όση ώρα** (пока).

    | Греческий | Русский |
    |:----------|:--------|
    | Όταν εσύ **πήγαινες**, εγώ **γύριζα**. | Когда ты шёл, я возвращался. |
    | Ενώ **διάβαζα**, **άκουγα** μουσική. | Пока я учился, я слушал музыку. |

    ### Παρατατικός + Αόριστος — длительное действие прерывается кратким событием

    Союзы: **Ενώ**, **Την ώρα που**, **Καθώς** (в то время как / пока).

    | Греческий | Русский |
    |:----------|:--------|
    | Την ώρα που **πήγαινα** στη στάση, **πέρασε** το λεωφορείο. | Пока я шёл на остановку, проехал автобус. |
    | Καθώς **έπαιζα**, **χτύπησε** το τηλέφωνο. | Пока я играл, зазвонил телефон. |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Phonology: Φωνή-Γραφή
    mo.md("""
    ## Φωνή-Γραφή — Звук и письмо (с. 111)

    ### Απαλοίφη φωνήεντος — Выпадение гласной (элизия)

    Краткие слова теряют конечную гласную перед гласным звуком:

    | | + гласная | → | Пример |
    |:-|:----------|:--|:-------|
    | με, σε | φωνήεν | μ', σ' | με άκουγε → μ' άκουγε |
    | το | ο, α | τ' | σε έβλεπε → σ' έβλεπε |
    | τα | α | τ' | |

    Слабые местоимения + звук [е-/и-]:

    | | → | Пример |
    |:-|:--|:-------|
    | μου + [е-/и-] | μου '- | μου έλεγε → μου 'λεγε |
    | σου + [е-/и-] | σου '- | σου έστελνε → σου 'στέλνε |
    | του + [е-/и-] | του '- | του έφερνε → του 'φερνε |
    | το + [е-/и-] | το '- | το ήξερε → το 'ξερε |
    | τα + [е-/и-] | τα '- | τα έδινε → τα 'δινε |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Test 1 heading
    mo.md("""
    ## Тест 1: Существительные
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Noun state
    tbl_sel_n, set_tbl_sel_n = mo.state(None)
    session_total_n, set_session_total_n = mo.state(0)
    return session_total_n, set_session_total_n, set_tbl_sel_n, tbl_sel_n


@app.cell(hide_code=True)
def _(gu, notebook_dir):
    # Load noun data
    df_noun = gu.load_vocab_table("nouns.tsv", nb_dir=notebook_dir)
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, gu, mo, tbl_sel_n):
    # Noun table
    table_noun = gu.vocab_table(df_noun, initial_selection=tbl_sel_n())
    mo.vstack([mo.md("### Выберите существительные для практики"), table_noun if table_noun is not None else mo.md("_Файл nouns.tsv не найден — загрузите файл, чтобы начать._")])
    return (table_noun,)


@app.cell(hide_code=True)
def _(gu, mo, random, session_total_n, set_session_total_n, table_noun):
    # Noun words
    words_noun = gu.get_words(table_noun)
    words4test_noun, set_words4test_noun = mo.state(words_noun.copy() if words_noun else [])
    if words_noun and len(words_noun) > session_total_n():
        set_session_total_n(len(words_noun))
    elif not words_noun:
        set_session_total_n(0)
    noun_msg, set_noun_msg = mo.state("")
    current_noun, set_current_noun = mo.state(None)
    captured_simple, set_captured_simple = mo.state(None)
    captured_article, set_captured_article = mo.state(None)
    _clk = lambda v: (v or 0) + 1
    skip_button_n = mo.ui.button(label="Пропустить", on_click=_clk)
    clear_button_n = mo.ui.button(label="Очистить", on_click=_clk)
    skip_count_n, set_skip_count_n = mo.state(0)
    clear_count_n, set_clear_count_n = mo.state(0)
    submit_count_n, set_submit_count_n = mo.state(0)
    if words_noun and current_noun() is None:
        set_current_noun(random.choice(words_noun))
    return (
        captured_article,
        captured_simple,
        clear_button_n,
        clear_count_n,
        current_noun,
        noun_msg,
        set_captured_article,
        set_captured_simple,
        set_clear_count_n,
        set_current_noun,
        set_noun_msg,
        set_skip_count_n,
        set_submit_count_n,
        set_words4test_noun,
        skip_button_n,
        skip_count_n,
        submit_count_n,
        words4test_noun,
    )


@app.cell(hide_code=True)
def _(clear_count_n, current_noun, gu):
    # Noun simple form
    clear_count_n()
    _nc = current_noun()
    noun_word, noun_trans, noun_form = gu.create_noun_test_ui([_nc] if _nc else [], mode='simple')
    return noun_form, noun_trans, noun_word


@app.cell(hide_code=True)
def _(clear_count_n, current_noun, gu):
    # Noun article form
    clear_count_n()
    _acn = current_noun()
    art_noun_word, art_noun_trans, art_noun_form = gu.create_noun_test_ui([_acn] if _acn else [], mode='article')
    return art_noun_form, art_noun_trans, art_noun_word


@app.cell(hide_code=True)
def _(
    art_noun_form,
    captured_article,
    captured_simple,
    mo,
    noun_form,
    set_submit_count_n,
):
    # Submit button N
    _vals_s = noun_form.value if noun_form is not None else []
    _vals_a = art_noun_form.value if art_noun_form is not None else []
    _snap_s = captured_simple()
    _snap_a = captured_article()
    _has_s = bool(_vals_s and any(v.strip() for v in _vals_s))
    _has_a = bool(_vals_a and any(v.strip() for v in _vals_a))
    _match_s = _snap_s is not None and [v.strip() for v in _vals_s] == [v.strip() for v in (_snap_s.value or [])]
    _match_a = _snap_a is not None and [v.strip() for v in _vals_a] == [v.strip() for v in (_snap_a.value or [])]
    _dirty = (_has_s and not _match_s) or (_has_a and not _match_a)
    _clk = lambda v: (v or 0) + 1
    submit_button_n = mo.ui.button(label="Проверить", on_click=_clk, kind="warn" if _dirty else "neutral")
    set_submit_count_n(0)
    return (submit_button_n,)


@app.cell(hide_code=True)
def _(
    captured_simple,
    clear_button_n,
    gu,
    mo,
    noun_form,
    noun_trans,
    noun_word,
    session_total_n,
    skip_button_n,
    submit_button_n,
    words4test_noun,
):
    # Noun simple display
    _feedback = mo.md("")
    if words4test_noun() and noun_word:
        _cs = captured_simple()
        if _cs and getattr(_cs, 'test_word', None) == noun_word:
            with mo.capture_stdout() as _buf:
                gu.check_noun_test(noun_word, _cs, mode='simple')
            if _buf.getvalue():
                _feedback = mo.md(_buf.getvalue())
        _view = mo.vstack([
            mo.md(f"**Простой тест по существительным** ({len(words4test_noun())}/{session_total_n()})"),
            mo.md(f"Перевод: **{noun_trans}**"),
            noun_form,
            _feedback,
            mo.hstack([skip_button_n, clear_button_n, submit_button_n], justify="end"),
        ])
    else:
        _view = mo.md("_Выберите существительные из таблицы выше, чтобы начать._")
    _view
    return


@app.cell(hide_code=True)
def _(
    art_noun_form,
    art_noun_trans,
    art_noun_word,
    captured_article,
    clear_button_n,
    gu,
    mo,
    session_total_n,
    skip_button_n,
    submit_button_n,
    words4test_noun,
):
    # Noun article display
    _feedback_a = mo.md("")
    if words4test_noun() and art_noun_word:
        _ca = captured_article()
        if _ca and getattr(_ca, 'test_word', None) == art_noun_word:
            with mo.capture_stdout() as _buf_a:
                gu.check_noun_test(art_noun_word, _ca, mode='article')
            if _buf_a.getvalue():
                _feedback_a = mo.md(_buf_a.getvalue())
        _view_art = mo.vstack([
            mo.md(f"**Тест по существительным с артиклями** ({len(words4test_noun())}/{session_total_n()})"),
            mo.md(f"Перевод: **{art_noun_trans}**"),
            art_noun_form,
            _feedback_a,
            mo.hstack([skip_button_n, clear_button_n, submit_button_n], justify="end"),
        ])
    else:
        _view_art = mo.md("_Выберите существительные из таблицы выше, чтобы начать._")
    _view_art
    return


@app.cell(hide_code=True)
def _(mo, noun_msg):
    # Noun message
    mo.md(noun_msg())
    return


@app.cell(hide_code=True)
def _(
    captured_article,
    captured_simple,
    current_noun,
    df_noun,
    gu,
    random,
    session_total_n,
    set_captured_article,
    set_captured_simple,
    set_current_noun,
    set_noun_msg,
    set_tbl_sel_n,
    set_words4test_noun,
    words4test_noun,
):
    # Noun pass handler
    _cn = current_noun()
    _cs = captured_simple()
    _ca = captured_article()
    if words4test_noun() and _cn and (_cs or _ca):
        _passed = False
        if _cs and getattr(_cs, 'test_word', None) == _cn['Word']:
            _passed = gu.check_noun_test(_cn['Word'], _cs, mode='simple')
        if not _passed and _ca and getattr(_ca, 'test_word', None) == _cn['Word']:
            _passed = gu.check_noun_test(_cn['Word'], _ca, mode='article')
        if _passed:
            _new = [w for w in words4test_noun() if w['Word'] != _cn['Word']]
            set_words4test_noun(_new)
            if df_noun is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_n([i for i, w in enumerate(df_noun['Word']) if w in _rem])
            set_noun_msg(f'<span style="color:green;">Тест для <b>"{_cn["Word"]}"</b> пройден.\n\n{len(_new)} слов осталось из {session_total_n()}.</span>')
            set_captured_simple(None)
            set_captured_article(None)
            set_current_noun(random.choice(_new) if _new else None)
    return


@app.cell(hide_code=True)
def _(
    art_noun_form,
    art_noun_word,
    gu,
    noun_form,
    noun_word,
    set_captured_article,
    set_captured_simple,
    set_submit_count_n,
    submit_button_n,
    submit_count_n,
):
    # Noun submit handler
    if (submit_button_n.value or 0) > submit_count_n():
        set_submit_count_n(submit_button_n.value)
        if noun_word and noun_form:
            set_captured_simple(gu.make_snapshot(noun_form))
        if art_noun_word and art_noun_form:
            set_captured_article(gu.make_snapshot(art_noun_form))
    return


@app.cell(hide_code=True)
def _(
    current_noun,
    df_noun,
    random,
    set_captured_article,
    set_captured_simple,
    set_current_noun,
    set_skip_count_n,
    set_tbl_sel_n,
    set_words4test_noun,
    skip_button_n,
    skip_count_n,
    words4test_noun,
):
    # Noun skip handler
    if (skip_button_n.value or 0) > skip_count_n():
        set_skip_count_n(skip_button_n.value)
        set_captured_simple(None)
        set_captured_article(None)
        _cn = current_noun()
        _new = [w for w in words4test_noun() if not _cn or w['Word'] != _cn['Word']]
        set_words4test_noun(_new)
        if df_noun is not None:
            _rem = {w['Word'] for w in _new}
            set_tbl_sel_n([i for i, w in enumerate(df_noun['Word']) if w in _rem])
        set_current_noun(random.choice(_new) if _new else None)
    return


@app.cell(hide_code=True)
def _(
    clear_button_n,
    clear_count_n,
    set_captured_article,
    set_captured_simple,
    set_clear_count_n,
):
    # Noun clear handler
    if (clear_button_n.value or 0) > clear_count_n():
        set_clear_count_n(clear_button_n.value)
        set_captured_simple(None)
        set_captured_article(None)
    return


@app.cell(hide_code=True)
def _(mo):
    # Test 2 heading
    mo.md("""
    ## Тест 2: Глаголы
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Verb state
    tbl_sel_v, set_tbl_sel_v = mo.state(None)
    session_total_v, set_session_total_v = mo.state(0)
    return session_total_v, set_session_total_v, set_tbl_sel_v, tbl_sel_v


@app.cell(hide_code=True)
def _(gu, notebook_dir):
    # Load verb data
    df_verb = gu.load_vocab_table("verbs.tsv", nb_dir=notebook_dir)
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, gu, mo, tbl_sel_v):
    # Verb table
    table_verb = gu.vocab_table(df_verb, initial_selection=tbl_sel_v())
    mo.vstack([mo.md("### Выберите глаголы для практики"), table_verb if table_verb is not None else mo.md("_Файл verbs.tsv не найден — загрузите файл, чтобы начать._")])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu, mo):
    # Tense selector
    tense_selector = mo.ui.dropdown(
        options={
            f"{gu.TENSE_LABELS['imperfect']['greek']} (Прошедшее продолженное)": "imperfect",
            f"{gu.TENSE_LABELS['present']['greek']} (Настоящее время)": "present",
        },
        value=f"{gu.TENSE_LABELS['imperfect']['greek']} (Прошедшее продолженное)",
        label="Выбрать время:",
    )
    tense_selector
    return (tense_selector,)


@app.cell(hide_code=True)
def _(gu, mo, session_total_v, set_session_total_v, table_verb):
    # Verb words
    words_verb = gu.get_words(table_verb)
    words4test_verb, set_words4test_verb = mo.state(words_verb.copy() if words_verb else [])
    if words_verb and len(words_verb) > session_total_v():
        set_session_total_v(len(words_verb))
    elif not words_verb:
        set_session_total_v(0)
    verb_msg, set_verb_msg = mo.state("")
    captured_verb, set_captured_verb = mo.state(None)
    _clk = lambda v: (v or 0) + 1
    skip_button_v = mo.ui.button(label="Пропустить", on_click=_clk)
    clear_button_v = mo.ui.button(label="Очистить", on_click=_clk)
    skip_count_v, set_skip_count_v = mo.state(0)
    clear_count_v, set_clear_count_v = mo.state(0)
    submit_count_v, set_submit_count_v = mo.state(0)
    return (
        captured_verb,
        clear_button_v,
        clear_count_v,
        set_captured_verb,
        set_clear_count_v,
        set_skip_count_v,
        set_submit_count_v,
        set_verb_msg,
        set_words4test_verb,
        skip_button_v,
        skip_count_v,
        submit_count_v,
        verb_msg,
        words4test_verb,
        words_verb,
    )


@app.cell(hide_code=True)
def _(clear_count_v, gu, random, tense_selector, words4test_verb, words_verb):
    # Verb form
    clear_count_v()
    cv_verb = random.choice(words4test_verb()) if words4test_verb() else None
    _tense_key = tense_selector.value
    _ui_label = gu.TENSE_LABELS[_tense_key]['greek'] if _tense_key else "—"
    verb_fields, _ = gu.create_verb_test_ui(_ui_label, words_verb, words4test_verb(), cv_verb)
    return cv_verb, verb_fields


@app.cell(hide_code=True)
def _(captured_verb, mo, set_submit_count_v, tense_selector, verb_fields):
    # Submit button V
    _values = verb_fields.value if verb_fields is not None else []
    _snap = captured_verb()
    _has_input = bool(_values and any(v.strip() for v in _values))
    _matches_snap = (
        _snap is not None
        and getattr(_snap, 'tense', None) == tense_selector.value
        and [v.strip() for v in _values] == [v.strip() for v in (_snap.value or [])]
    )
    _dirty = _has_input and not _matches_snap
    _clk = lambda v: (v or 0) + 1
    submit_button_v = mo.ui.button(label="Проверить", on_click=_clk, kind="warn" if _dirty else "neutral")
    set_submit_count_v(0)
    return (submit_button_v,)


@app.cell(hide_code=True)
def _(
    captured_verb,
    clear_button_v,
    cv_verb,
    gu,
    mo,
    session_total_v,
    skip_button_v,
    submit_button_v,
    tense_selector,
    verb_fields,
    verb_msg,
    words4test_verb,
):
    # Verb display
    _TENSE_LABELS = {k: gu.TENSE_LABELS[k]['greek'] for k in gu.TENSE_LABELS}
    if not words4test_verb():
        _view_verb = mo.md("_Выберите глаголы из таблицы выше, чтобы начать._")
    elif not tense_selector.value:
        _view_verb = mo.md("_Выберите время выше._")
    else:
        _feedback_v = mo.md("")
        _c = captured_verb()
        if cv_verb and _c and getattr(_c, 'verb_word', None) == cv_verb['Word'] and getattr(_c, 'tense', None) == tense_selector.value:
            _, _msg = gu.check_verb_test(cv_verb['Word'], _c, tense_selector.value)
            _feedback_v = mo.md(_msg)
        _label = _TENSE_LABELS.get(tense_selector.value, tense_selector.value)
        _rem = len(words4test_verb())
        _items = [mo.md(f"**Тест по глаголам** — {_label} ({_rem}/{session_total_v()})")]
        if verb_msg():
            _items.append(mo.md(verb_msg()))
        _items += [
            mo.md(f"Перевод: **{cv_verb['Translation']}**") if cv_verb else mo.md(""),
            verb_fields,
            mo.hstack([skip_button_v, clear_button_v, submit_button_v], justify="end"),
            _feedback_v,
        ]
        _view_verb = mo.vstack(_items)
    _view_verb
    return


@app.cell(hide_code=True)
def _(
    captured_verb,
    cv_verb,
    df_verb,
    gu,
    session_total_v,
    set_captured_verb,
    set_tbl_sel_v,
    set_verb_msg,
    set_words4test_verb,
    tense_selector,
    words4test_verb,
):
    # Verb pass handler
    _tense_key = tense_selector.value
    _c = captured_verb()
    if cv_verb and _tense_key and _c and getattr(_c, 'verb_word', None) == cv_verb['Word'] and getattr(_c, 'tense', None) == _tense_key:
        _ok, _ = gu.check_verb_test(cv_verb['Word'], _c, _tense_key)
        if _ok:
            _new = [w for w in words4test_verb() if w['Word'] != cv_verb['Word']]
            set_words4test_verb(_new)
            if df_verb is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_v([i for i, w in enumerate(df_verb['Word']) if w in _rem])
            set_verb_msg(f'<span style="color:green;">Тест для <b>"{cv_verb["Word"]} — {cv_verb["Translation"]}"</b> пройден.\n\n{len(_new)} слов осталось из {session_total_v()}.</span>')
            set_captured_verb(None)
    return


@app.cell(hide_code=True)
def _(
    cv_verb,
    gu,
    set_captured_verb,
    set_submit_count_v,
    submit_button_v,
    submit_count_v,
    tense_selector,
    verb_fields,
):
    # Verb submit handler
    if (submit_button_v.value or 0) > submit_count_v():
        set_submit_count_v(submit_button_v.value)
        if cv_verb and verb_fields:
            set_captured_verb(gu.make_snapshot(verb_fields, verb_word=cv_verb['Word'], tense=tense_selector.value))
    return


@app.cell(hide_code=True)
def _(
    cv_verb,
    df_verb,
    set_captured_verb,
    set_skip_count_v,
    set_tbl_sel_v,
    set_words4test_verb,
    skip_button_v,
    skip_count_v,
    words4test_verb,
):
    # Verb skip handler
    if (skip_button_v.value or 0) > skip_count_v():
        set_skip_count_v(skip_button_v.value)
        set_captured_verb(None)
        if words4test_verb():
            _new = [w for w in words4test_verb() if not cv_verb or w['Word'] != cv_verb['Word']]
            set_words4test_verb(_new)
            if df_verb is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_v([i for i, w in enumerate(df_verb['Word']) if w in _rem])
    return


@app.cell(hide_code=True)
def _(clear_button_v, clear_count_v, set_captured_verb, set_clear_count_v):
    # Verb clear handler
    if (clear_button_v.value or 0) > clear_count_v():
        set_clear_count_v(clear_button_v.value)
        set_captured_verb(None)
    return


@app.cell(hide_code=True)
def _(mo):
    # Test 3 heading
    mo.md("""
    ## Тест 3: Прилагательные
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Adj state
    tbl_sel_a, set_tbl_sel_a = mo.state(None)
    session_total_a, set_session_total_a = mo.state(0)
    return session_total_a, set_session_total_a, set_tbl_sel_a, tbl_sel_a


@app.cell(hide_code=True)
def _(gu, notebook_dir):
    # Load adj data
    df_adj = gu.load_vocab_table("adjectives.tsv", nb_dir=notebook_dir)
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, gu, mo, tbl_sel_a):
    # Adj table
    table_adj = gu.vocab_table(df_adj, initial_selection=tbl_sel_a())
    mo.vstack([mo.md("### Выберите прилагательные для практики"), table_adj if table_adj is not None else mo.md("_Файл adjectives.tsv не найден — загрузите файл, чтобы начать._")])
    return (table_adj,)


@app.cell(hide_code=True)
def _(mo):
    # Mode selector
    mode_selector = mo.ui.radio(
        options={
            "Простой: 3 рода × 2 числа (6 полей)": "simple",
            "Сложный: все роды, числа и падежи (18 полей)": "complex",
        },
        value="Простой: 3 рода × 2 числа (6 полей)",
        label="Режим теста:",
    )
    mo.md(f"{mode_selector}")
    return (mode_selector,)


@app.cell(hide_code=True)
def _(gu, mo, random, session_total_a, set_session_total_a, table_adj):
    # Adj words
    words_adj = gu.get_words(table_adj)
    words4test_adj, set_words4test_adj = mo.state(words_adj.copy() if words_adj else [])
    if words_adj and len(words_adj) > session_total_a():
        set_session_total_a(len(words_adj))
    elif not words_adj:
        set_session_total_a(0)
    adj_last_passed_mesg, set_adj_last_passed_mesg = mo.state("")
    adj_cv, set_adj_cv = mo.state(None)
    captured_adj, set_captured_adj = mo.state(None)
    _clk = lambda v: (v or 0) + 1
    skip_button_a = mo.ui.button(label="Пропустить", on_click=_clk)
    clear_button_a = mo.ui.button(label="Очистить", on_click=_clk)
    skip_count_a, set_skip_count_a = mo.state(0)
    clear_count_a, set_clear_count_a = mo.state(0)
    submit_count_a, set_submit_count_a = mo.state(0)
    if words_adj and adj_cv() is None:
        set_adj_cv(random.choice(words_adj))
    return (
        adj_cv,
        adj_last_passed_mesg,
        captured_adj,
        clear_button_a,
        clear_count_a,
        set_adj_cv,
        set_adj_last_passed_mesg,
        set_captured_adj,
        set_clear_count_a,
        set_skip_count_a,
        set_submit_count_a,
        set_words4test_adj,
        skip_button_a,
        skip_count_a,
        submit_count_a,
        words4test_adj,
    )


@app.cell(hide_code=True)
def _(adj_cv, clear_count_a, gu, mode_selector):
    # Adj form
    clear_count_a()
    _acv = adj_cv()
    adj_form, _ = gu.create_adjective_test_ui([] if not _acv else [_acv], [], _acv, mode=mode_selector.value)
    return (adj_form,)


@app.cell(hide_code=True)
def _(adj_form, captured_adj, mo, set_submit_count_a):
    # Submit button A
    _values = adj_form.value if adj_form else []
    _snap = captured_adj()
    _has_input = bool(_values and any(v.strip() for v in _values))
    _matches_snap = _snap is not None and [v.strip() for v in _values] == [v.strip() for v in (_snap.value or [])]
    _dirty = _has_input and not _matches_snap
    _clk = lambda v: (v or 0) + 1
    submit_button_a = mo.ui.button(label="Проверить", on_click=_clk, kind="warn" if _dirty else "neutral")
    set_submit_count_a(0)
    return (submit_button_a,)


@app.cell(hide_code=True)
def _(
    adj_cv,
    adj_form,
    captured_adj,
    clear_button_a,
    gu,
    mo,
    mode_selector,
    session_total_a,
    skip_button_a,
    submit_button_a,
    words4test_adj,
):
    # Adj display
    _adj = adj_cv()
    if words4test_adj() and _adj:
        _feedback_a = mo.md("")
        _c = captured_adj()
        if _c and getattr(_c, 'adj_word', None) == _adj['Word']:
            _, _msg = gu.check_adjective_test(_adj['Word'], _c, mode=mode_selector.value)
            if _msg:
                _feedback_a = mo.md(_msg)
        _view_adj = mo.vstack([
            mo.md(f"**Тест по прилагательным** ({len(words4test_adj())}/{session_total_a()})"),
            mo.md(f"Перевод: **{_adj['Translation']}**"),
            adj_form,
            _feedback_a,
            mo.hstack([skip_button_a, clear_button_a, submit_button_a], justify="end"),
        ])
    else:
        _view_adj = mo.md("_Выберите прилагательные из таблицы выше, чтобы начать._")
    _view_adj
    return


@app.cell(hide_code=True)
def _(adj_last_passed_mesg, mo):
    # Adj message
    mo.md(adj_last_passed_mesg())
    return


@app.cell(hide_code=True)
def _(
    adj_cv,
    captured_adj,
    df_adj,
    gu,
    random,
    session_total_a,
    set_adj_cv,
    set_adj_last_passed_mesg,
    set_captured_adj,
    set_tbl_sel_a,
    set_words4test_adj,
    words4test_adj,
):
    # Adj pass handler
    _adj = adj_cv()
    _c = captured_adj()
    if words4test_adj() and _adj and _c and getattr(_c, 'adj_word', None) == _adj['Word']:
        adj_ok, _ = gu.check_adjective_test(_adj['Word'], _c)
        if adj_ok:
            _new = [w for w in words4test_adj() if w['Word'] != _adj['Word']]
            set_words4test_adj(_new)
            if df_adj is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_a([i for i, w in enumerate(df_adj['Word']) if w in _rem])
            set_adj_last_passed_mesg(f'<span style="color:green;">Тест для <b>"{_adj["Word"]} — {_adj["Translation"]}"</b> пройден.\n\n{len(_new)} слов осталось из {session_total_a()}.</span>')
            set_adj_cv(random.choice(_new) if _new else None)
            set_captured_adj(None)
    return


@app.cell(hide_code=True)
def _(
    adj_cv,
    adj_form,
    gu,
    set_captured_adj,
    set_submit_count_a,
    submit_button_a,
    submit_count_a,
):
    # Adj submit handler
    if (submit_button_a.value or 0) > submit_count_a():
        set_submit_count_a(submit_button_a.value)
        _acv = adj_cv()
        if _acv and adj_form:
            set_captured_adj(gu.make_snapshot(adj_form))
    return


@app.cell(hide_code=True)
def _(
    adj_cv,
    df_adj,
    random,
    set_adj_cv,
    set_captured_adj,
    set_skip_count_a,
    set_tbl_sel_a,
    set_words4test_adj,
    skip_button_a,
    skip_count_a,
    words4test_adj,
):
    # Adj skip handler
    if (skip_button_a.value or 0) > skip_count_a():
        set_skip_count_a(skip_button_a.value)
        set_captured_adj(None)
        _acv = adj_cv()
        _new = [w for w in words4test_adj() if not _acv or w['Word'] != _acv['Word']]
        set_words4test_adj(_new)
        if df_adj is not None:
            _rem = {w['Word'] for w in _new}
            set_tbl_sel_a([i for i, w in enumerate(df_adj['Word']) if w in _rem])
        set_adj_cv(random.choice(_new) if _new else None)
    return


@app.cell(hide_code=True)
def _(clear_button_a, clear_count_a, set_captured_adj, set_clear_count_a):
    # Adj clear handler
    if (clear_button_a.value or 0) > clear_count_a():
        set_clear_count_a(clear_button_a.value)
        set_captured_adj(None)
    return


@app.cell(hide_code=True)
def _():
    # Imports
    import os
    import random
    import marimo as mo
    from modern_greek_eee import greek_utils as gu
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    return gu, mo, notebook_dir, random


if __name__ == "__main__":
    app.run()
