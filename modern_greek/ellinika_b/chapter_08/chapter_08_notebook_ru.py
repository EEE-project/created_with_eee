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

__generated_with = "0.23.5"
app = marimo.App(width="medium", html_head_file="head.html")


@app.cell(hide_code=True)
def _(mo):
    # Title
    mo.md("""
    # «Έχει ο καιρός γυρίσματα» 🌤️
    ## Глава 8 — Погода переменчива · B1

    **Грамматика:** Απλός Μέλλοντας · Условные предложения (Αν…) · Прилагательные на -ης/-α/-ικο
    **Тесты:** Существительные · Глаголы · Прилагательные
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Vocabulary: Λέξεις, λέξεις
    mo.md("""
    ## Словарь

    | Греческий | Русский |
    |:---------|:--------|
    | δελτίο καιρού (το) | прогноз погоды |
    | η θερμοκρασία πέφτει / ανεβαίνει | температура падает / поднимается |
    | κακοκαιρία (η) | плохая погода |
    | οργανώνω | организовывать |
    | πεζοπορία (η) | пеший туризм / поход |
    | περπάτημα (το) | ходьба / прогулка |
    | φύση (η) | природа |
    | λιακάδα (η) | солнечная погода / просветление |
    | ο καιρός χειροτερεύει | погода ухудшается |
    | παραπονιάρης, -α, -ικο | нытик, склонный к жалобам |
    | πεισματάρης, -α, -ικο | упрямый |
    | τεμπέλης, -α, -ικο | ленивый |
    | υπομονή (η) | терпение |
    | υψηλή (για την εποχή) θερμοκρασία | высокая (для сезона) температура |
    | ψιχαλίζει — ψιχάλα (η) | моросит — морось |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Phrases: Πώς το λένε;
    mo.md("""
    ## Полезные фразы

    | Греческий | Русский |
    |:---------|:--------|
    | Έχεις κανένα σχέδιο; | У тебя есть какие-то планы? |
    | Πώς σου ΄ρθε; | Как тебе пришло в голову? |
    | Θα είμαστε καλή παρέα. | Мы будем хорошей компанией. |
    | Έλα τώρα... | Ну ладно... |
    | Καλό θα μας κάνει το πρωινό περπάτημα στη φύση. | Утренняя прогулка на природе пойдёт нам на пользу. |
    | Δεν είναι κακή ιδέα. | Неплохая идея. |
    | Νιώθω χάλια. | Я чувствую себя ужасно. |
    | Άντε, ρε! | Ну давай! / Да ладно! |
    | Η θερμοκρασία θα πέσει πολύ. | Температура упадёт сильно. |
    | Ελπίζω ο καιρός να μας κάνει τη χάρη. | Надеюсь, погода нас не подведёт. |
    | Πώς κάνεις έτσι; | Как ты можешь так делать? |
    | Τι παραπονιάρης που είσαι... | Ну и нытик же ты... |
    | Ελάτε, παιδιά! | Давайте, ребята! |
    | Μη μαλώνετε! | Не ругайтесь! |
    | Επιτέλους! | Наконец-то! |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Weather forecast: fixed phrase patterns for describing conditions
    mo.md("""
    ## Прогноз погоды

    | Конструкция | Варианты |
    |:------------|:---------|
    | **Ο καιρός αύριο θα είναι** … | ήπιος (мягкий) · αίθριος (ясный) · άστατος (переменный) |
    | **Θα έχει** … | υψηλές/χαμηλές θερμοκρασίες · ηλιοφάνεια · ήλιο με αραιή συννεφιά · νεφώσεις (облачно) · βροχές και καταιγίδες · δυνατούς ανέμους |
    | **Θα έχουμε** … | άνοδο / πτώση της θερμοκρασίας |

    **Направления ветра:** βοριάς (С) · νοτιάς (Ю) · ανατολικός (В) · δυτικός (З)
    **Бофорт:** ανέμους 5 μποφόρ · ισχυρούς βόρειους ανέμους έντασης 9 μποφόρ
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Grammar: Απλός Μέλλοντας
    mo.md("""
    ## Грамматика: Απλός Μέλλοντας (Простое будущее)

    Используется для **однократного, завершённого** действия в будущем.
    Образуется с частицей **θα** + основа аориста.

    | Тип | Настоящее | Простое будущее | Изменение основы |
    |:----|:----------|:----------------|:-----------------|
    | A | γράφω | **θα γράψω** | γραφ → γραψ |
    | A | αγοράζω | **θα αγοράσω** | αγοραζ → αγορας |
    | A | πετάω | **θα πετάξω** | πετα → πεταξ |
    | A/B | λέω | **θα πω** | неправильный |
    | A/B | τρώω | **θα φάω** | неправильный |
    | B1 | μιλάω | **θα μιλήσω** | μιλα → μιλης |
    | — | πηγαίνω | **θα πάω** | неправильный |

    ### Спряжение: αγοράζω → θα αγοράσω

    | Лицо | Форма |
    |:-----|:------|
    | εγώ | **θα αγοράσω** |
    | εσύ | **θα αγοράσεις** |
    | αυτός/ή/ό | **θα αγοράσει** |
    | εμείς | **θα αγοράσουμε** |
    | εσείς | **θα αγοράσετε** |
    | αυτοί/ές/ά | **θα αγοράσουν** |

    > **Ср. Συνεχής Μέλλοντας** (θα + настоящее): *θα αγοράζω* = буду покупать (многократно).
    > **Απλός** = один раз; **Συνεχής** = повторно / продолжительно.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Stem formation by ending class; Type A = consonant stems, B1/B2 = vowel stems (-άω/-ώ)
    mo.md("""
    ## Образование основы — Простое будущее

    | Окончание | Примеры |
    |:----------|:--------|
    | **— Α —** |   |
    | -νω, -ζω, -θω → **-σω** | πληρώ**νω** · θα πληρώ**σω**, αγορά**ζω** · θα αγορά**σω**, νιώ**θω** · θα νιώ**σω** |
    | -ζω, -γω, -χω, -χνω, -κω, -σκω → **-ξω** | κοιτά**ζω** · θα κοιτά**ξω**, ανοί**γω** · θα ανοί**ξω**, τρέ**χω** · θα τρέ**ξω**, φτιά**χνω** · θα φτιά**ξω**, μπλέ**κω** · θα μπλέ**ξω**, διδά**σκω** · θα διδά**ξω** |
    | -εύω, -πω, -φω, -βω, -πτω → **-ψω** | δουλε**ύω** · θα δουλέ**ψω**, λεί**πω** · θα λεί**ψω**, γρά**φω** · θα γρά**ψω**, ανά**βω** · θα ανά**ψω**, βλά**πτω** · θα βλά**ψω** |
    | **— Β1 / Β2 —** |   |
    | **-ήσω** | μιλάω – θα μιλ**ήσω** · τηλεφωνώ – θα τηλεφων**ήσω** · ζω – θα ζ**ήσω** |
    | **-άσω** | γελάω – θα γελ**άσω** · διψάω – θα διψ**άσω** · ξεχνάω – θα ξεχ**άσω** |
    | **-έσω** | φοράω – θα φορ**έσω** · καλώ – θα καλ**έσω** · μπορώ – θα μπορ**έσω** |
    | **-ήξω** | πηδάω – θα πηδ**ήξω** · τραβάω – θα τραβ**ήξω** · φυσάω – θα φυσ**ήξω** · βουτάω – θα βουτ**ήξω** |
    | **-άξω** | κοιτάω – θα κοιτ**άξω** · πετάω – θα πετ**άξω** · φυλάω – θα φυλ**άξω** |

    ### Нерегулярные глаголы

    | Настоящее | Простое будущее |
    |:----------|:----------------|
    | ανεβαίνω | θα ανέβω / θα ανεβώ |
    | αρρωσταίνω | θα αρρωστήσω |
    | βάζω | θα βάλω |
    | βγάζω | θα βγάλω |
    | βγαίνω | θα βγω |
    | βλέπω | θα δω |
    | βρίσκω | θα βρω |
    | δίνω | θα δώσω |
    | είμαι | θα είμαι |
    | έχω | θα έχω |
    | θέλω | θα θελήσω |
    | καίω | θα κάψω |
    | κάνω | θα κάνω |
    | καταλαβαίνω | θα καταλάβω |
    | κατεβαίνω | θα κατέβω / θα κατεβώ |
    | κλαίω | θα κλάψω |
    | λέω | θα πω |
    | μαθαίνω | θα μάθω |
    | μένω | θα μείνω |
    | μεθάω | θα μεθύσω |
    | ξέρω | θα ξέρω |
    | μπαίνω | θα μπω |
    | παθαίνω | θα πάθω |
    | παίρνω | θα πάρω |
    | πεθαίνω | θα πεθάνω |
    | περιμένω | θα περιμένω |
    | πέφτω | θα πέσω |
    | πηγαίνω (πάω) | θα πάω |
    | πίνω | θα πιω |
    | πλένω | θα πλύνω |
    | στέλνω | θα στείλω |
    | τρώω | θα φάω |
    | φέρνω | θα φέρω |
    | φεύγω | θα φύγω |
    | γίνομαι | θα γίνω |
    | έρχομαι | θα έρθω |
    | κάθομαι | θα καθίσω / θα κάτσω |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Grammar: Conditional sentences
    mo.md("""
    ## Грамматика: Условные предложения — Тип 1 (Υποθετικές — Τύπος Α)

    **Структура:** **Αν** + форма сослагательного (без *να*) → **θα** + Простое будущее

    Используется для **реальных, возможных** условий в будущем.

    | Греческий | Русский |
    |:---------|:--------|
    | Αν **βρέξει** αύριο, δε θα **πάμε** εκδρομή. | Если завтра будет дождь, мы не поедем на экскурсию. |
    | Αν **έχει** ωραίο καιρό, θα **πάμε** για πεζοπορία. | Если погода будет хорошей, мы пойдём в поход. |
    | Αν **φτάσεις** νωρίς, θα **φάμε** μαζί. | Если ты придёшь рано, мы поедим вместе. |

    > Придаточное с **Αν** использует ту же основу, что и Простое будущее (основа аориста), но без θα.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Grammar: Adjectives -ης/-α/-ικο
    mo.md("""
    ## Грамматика: Прилагательные на **-ης, -α, -ικο**

    Описывают **черты характера** (часто разговорные, с эмоциональной окраской).

    | Мужской (-ης) | Женский (-α) | Средний (-ικο) | Значение |
    |:--------------|:-------------|:---------------|:---------|
    | τεμπέλης | τεμπέλα | τεμπέλικο | ленивый |
    | γκρινιάρης | γκρινιάρα | γκρινιάρικο | брюзгливый |
    | ζηλιάρης | ζηλιάρα | ζηλιάρικο | ревнивый |
    | πεισματάρης | πεισματάρα | πεισματάρικο | упрямый |
    | ξεχασιάρης | ξεχασιάρα | ξεχασιάρικο | забывчивый |
    | παραπονιάρης | παραπονιάρα | παραπονιάρικο | нытик |

    **Склонение τεμπέλης:**

    | Падеж | М. р. (ед./мн.) | Ж. р. (ед./мн.) | Ср. р. (ед./мн.) |
    |:------|:----------------|:----------------|:-----------------|
    | Им. | τεμπέλης / τεμπέληδες | τεμπέλα / τεμπέλες | τεμπέλικο / τεμπέλικα |
    | Рд. | τεμπέλη / τεμπέληδων | τεμπέλας / τεμπέλων | τεμπέλικου / τεμπέλικων |
    | Вн. | τεμπέλη / τεμπέληδες | τεμπέλα / τεμπέλες | τεμπέλικο / τεμπέλικα |

    **Склонение γκρινιάρης** (пример из учебника):

    | Падеж | М. р. | Ж. р. | Ср. р. |
    |:------|:------|:------|:------|
    | Им. ед. | ο γκρινιάρης | η γκρινιάρα | το γκρινιάρικο |
    | Рд. ед. | του γκρινιάρη | της γκρινιάρας | του γκρινιάρικου |
    | Вн. ед. | τον γκρινιάρη | την γκρινιάρα | το γκρινιάρικο |
    | Им. мн. | οι γκρινιάρηδες | οι γκρινιάρες | τα γκρινιάρικα |
    | Рд. мн. | των γκρινιάρηδων | — | των γκρινιάρικων |
    | Вн. мн. | τους γκρινιάρηδες | τις γκρινιάρες | τα γκρινιάρικα |

    **Другие прилагательные этого типа:**
    πενηντάρης · κοκκινομάλλης · γαλανομάτης · μικρούλης · γκρινιάρης · ζηλιάρης · ναζιάρης · ξεχασιάρης · κουτσομπόλης
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
def _(mo):
    # Noun file upload
    file_upload_noun = mo.ui.file(label="Загрузить TSV с существительными")
    file_upload_noun
    return (file_upload_noun,)


@app.cell(hide_code=True)
def _(file_upload_noun, gu, notebook_dir, os, pd):
    # Load noun data
    if file_upload_noun.value:
        df_noun = gu.load_data(file_upload_noun, [])
    else:
        try:
            df_noun = pd.read_csv(os.path.join(notebook_dir, 'nouns.tsv'), sep='\t')
        except FileNotFoundError:
            df_noun = None
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, mo, tbl_sel_n):
    # Noun table
    table_noun = mo.ui.table(df_noun, selection="multi", initial_selection=tbl_sel_n()) if df_noun is not None else None
    _display = table_noun if table_noun is not None else mo.md("_nouns.tsv не найден — загрузите файл._")
    mo.vstack([mo.md("### Выберите существительные для практики"), table_noun])
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
def _(mo):
    # Verb file upload
    file_upload_verb = mo.ui.file(label="Загрузить TSV с глаголами")
    file_upload_verb
    return (file_upload_verb,)


@app.cell(hide_code=True)
def _(file_upload_verb, gu, notebook_dir, os, pd):
    # Load verb data
    if file_upload_verb.value:
        df_verb = gu.load_data(file_upload_verb, [])
    else:
        try:
            df_verb = pd.read_csv(os.path.join(notebook_dir, 'verbs.tsv'), sep='\t')
        except FileNotFoundError:
            df_verb = None
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, mo, tbl_sel_v):
    # Verb table
    table_verb = mo.ui.table(df_verb, selection="multi", initial_selection=tbl_sel_v()) if df_verb is not None else None
    _display = table_verb if table_verb is not None else mo.md("_verbs.tsv не найден — загрузите файл._")
    mo.vstack([mo.md("### Выберите глаголы для практики"), table_verb])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu, mo):
    # Tense selector
    tense_selector = mo.ui.dropdown(
        options={
            f"{gu.TENSE_LABELS['future']['greek']} (Simple Future)": "future",
            f"{gu.TENSE_LABELS['present']['greek']} (Present)": "present",
        },
        value=f"{gu.TENSE_LABELS['future']['greek']} (Simple Future)",
        label="Выберите время:",
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
def _(mo):
    # Adj file upload
    file_upload_adj = mo.ui.file(label="Загрузить TSV с прилагательными")
    file_upload_adj
    return (file_upload_adj,)


@app.cell(hide_code=True)
def _(file_upload_adj, gu, notebook_dir, os, pd):
    # Load adj data
    if file_upload_adj.value:
        df_adj = gu.load_data(file_upload_adj, [])
    else:
        try:
            df_adj = pd.read_csv(os.path.join(notebook_dir, 'adjectives.tsv'), sep='\t')
        except FileNotFoundError:
            df_adj = None
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, mo, tbl_sel_a):
    # Adj table
    table_adj = mo.ui.table(df_adj, selection="multi", initial_selection=tbl_sel_a()) if df_adj is not None else None
    _display = table_adj if table_adj is not None else mo.md("_adjectives.tsv не найден — загрузите файл._")
    mo.vstack([mo.md("### Выберите прилагательные для практики"), table_adj])
    return (table_adj,)


@app.cell(hide_code=True)
def _(mo):
    # Mode selector — MUST be before state init (Marimo dependency order)
    mode_selector = mo.ui.radio(
        options={
            "Простой: 3 рода × 2 числа (6 полей)": "simple",
            "Полный: все роды, числа и падежи (18 полей)": "complex",
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
    import pandas as pd
    import marimo as mo
    from modern_greek_eee import greek_utils as gu
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    return gu, mo, notebook_dir, os, pd, random


if __name__ == "__main__":
    app.run()
