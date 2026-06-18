# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "marimo>=0.23.3",
#     "modern-greek-eee @ git+https://github.com/EEE-project/modern-greek-eee.git",
#     "modern-greek-inflexion-eee @ git+https://github.com/EEE-project/modern-greek-inflexion-eee.git",
#     "pandas",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# modern-greek-eee = { git = "https://github.com/EEE-project/modern-greek-eee" }
# modern-greek-inflexion-eee = { git = "https://github.com/EEE-project/modern-greek-inflexion-eee" }
# ///

import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(language_selector, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _cfg = ConfigStore.from_url(
        f"{_ROOT}/ellinika_b/lessons.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=_cfg.index_url(), lang=language_selector.value, titles={
        "ru": "Ελληνικά Β", "el": "Ελληνικά Β", "en": "Ελληνικά Β",
    }, ga_config=_cfg.ga_config())
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Title
    _lang = language_selector.value
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_LgoXtFZWGveFacZETuUiZx)"
    if _lang == "ru":
        _sub = "Глава 2 — Жильё · B1"
        _gl, _tl = "Грамматика", "Тесты"
        _tc = "Существительные · Глаголы · Прилагательные"
    elif _lang == "el":
        _sub = "Ενότητα 2 — Κατοικία · B1"
        _gl, _tl = "Γραμματική", "Τεστ"
        _tc = "Ουσιαστικά · Ρήματα · Επίθετα"
    else:
        _sub = "Unit 2 — Housing · B1"
        _gl, _tl = "Grammar", "Tests"
        _tc = "Nouns · Verbs · Adjectives"
    _gc = "Άρθρα · Έμμεσα Αντικείμενα · Γενική · Κτητικές Αντωνυμίες (δικός μου)"
    _out = mo.md(f"""# «Σπίτι μου σπιτάκι μου» 🏠
## {_sub} {_badge}

**{_gl}:** {_gc}
**{_tl}:** {_tc}
""")
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Articles
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ## Грамматика: Артикли (Άρθρα)

    **Определённый артикль** (ο, η, το) указывает на конкретный предмет.
    **Неопределённый артикль** (ένας, μία, ένα) указывает на неопределённый предмет.

    | Род | Опр. ед.ч. | Опр. мн.ч. | Неопр. |
    |--------|------------------|-----------------|------------|
    | Мужской (αρσ.) | **ο** φίλος | **οι** φίλοι | **ένας** φίλος |
    | Женский (θηλ.) | **η** κουζίνα | **οι** κουζίνες | **μία** κουζίνα |
    | Средний (ουδ.) | **το** σπίτι | **τα** σπίτια | **ένα** σπίτι |

    > *Έχω **ένα** διαμέρισμα. **Το** διαμέρισμα είναι ευρύχωρο.*
    > (У меня есть квартира. Квартира просторная.)
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ## Γραμματική: Άρθρα (Άρθρα)

    Το **οριστικό άρθρο** (ο, η, το) αναφέρεται σε κάτι συγκεκριμένο.
    Το **αόριστο άρθρο** (ένας, μία, ένα) αναφέρεται σε κάτι αόριστο.

    | Γένος | Οριστικό Ενικός | Οριστικό Πληθυντικός | Αόριστο |
    |--------|------------------|-----------------|------------|
    | Αρσενικό (αρσ.) | **ο** φίλος | **οι** φίλοι | **ένας** φίλος |
    | Θηλυκό (θηλ.) | **η** κουζίνα | **οι** κουζίνες | **μία** κουζίνα |
    | Ουδέτερο (ουδ.) | **το** σπίτι | **τα** σπίτια | **ένα** σπίτι |

    > *Έχω **ένα** διαμέρισμα. **Το** διαμέρισμα είναι ευρύχωρο.*
    """)
    else:
        _md = mo.md("""
    ## Grammar: Articles (Άρθρα)

    The **definite article** (ο, η, το) refers to something specific.
    The **indefinite article** (ένας, μία, ένα) refers to something non-specific.

    | Gender | Definite Singular | Definite Plural | Indefinite |
    |--------|------------------|-----------------|------------|
    | Masculine (αρσ.) | **ο** φίλος | **οι** φίλοι | **ένας** φίλος |
    | Feminine (θηλ.) | **η** κουζίνα | **οι** κουζίνες | **μία** κουζίνα |
    | Neuter (ουδ.) | **το** σπίτι | **τα** σπίτια | **ένα** σπίτι |

    > *Έχω **ένα** διαμέρισμα. **Το** διαμέρισμα είναι ευρύχωρο.*
    > (I have an apartment. The apartment is spacious.)
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Indirect Object Pronouns
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ## Грамматика: Местоимения косвенного объекта

    В греческом косвенное дополнение выражается через **родительный падеж** (аналог «мне», «тебе», «ему»).
    Есть две формы: **слабая (клитика)** и **сильная (эмфатическая)**.

    | Лицо | Слабая форма | Сильная форма | Пример |
    |--------|-----------|-------------|---------|
    | 1-е ед.ч. | **μου** | εμένα | **Μου** αρέσει το σπίτι. *(Мне нравится дом.)* |
    | 2-е ед.ч. | **σου** | εσένα | **Σου** έδωσα το κλειδί. *(Я дал тебе ключ.)* |
    | 3-е ед.ч. м.р. | **του** | αυτού | **Του** στέλνω το συμβόλαιο. *(Я отправляю ему контракт.)* |
    | 3-е ед.ч. ж.р. | **της** | αυτής | **Της** λέω την τιμή. *(Я говорю ей цену.)* |
    | 3-е ед.ч. ср.р. | **του** | αυτού | — |
    | 1-е мн.ч. | **μας** | εμάς | **Μας** φτιάχνεις καφέ; *(Ты сделаешь нам кофе?)* |
    | 2-е мн.ч. | **σας** | εσάς | **Σας** πάει πολύ. *(Вам очень идёт.)* |
    | 3-е мн.ч. | **τους** | αυτών | **Τους** είπε ψέματα. *(Он солгал им.)* |

    **Сильная форма** используется для выражения ударения или противопоставления:
    > ***Εμένα** μου αρέσει. Εσένα;* (Мне нравится. А тебе?)
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ## Γραμματική: Αντωνυμίες Έμμεσου Αντικειμένου

    Στα ελληνικά, το έμμεσο αντικείμενο εκφράζεται με τη **γενική πτώση**.
    Υπάρχουν δύο μορφές: **αδύνατος τύπος (εγκλιτικός)** και **δυνατός τύπος (εμφατικός)**.

    | Πρόσωπο | Αδύνατος τύπος | Δυνατός τύπος | Παράδειγμα |
    |--------|-----------|-------------|---------|
    | 1ο εν. | **μου** | εμένα | **Μου** αρέσει το σπίτι. |
    | 2ο εν. | **σου** | εσένα | **Σου** έδωσα το κλειδί. |
    | 3ο εν. αρσ. | **του** | αυτού | **Του** στέλνω το συμβόλαιο. |
    | 3ο εν. θηλ. | **της** | αυτής | **Της** λέω την τιμή. |
    | 3ο εν. ουδ. | **του** | αυτού | — |
    | 1ο πλ. | **μας** | εμάς | **Μας** φτιάχνεις καφέ; |
    | 2ο πλ. | **σας** | εσάς | **Σας** πάει πολύ. |
    | 3ο πλ. | **τους** | αυτών | **Τους** είπε ψέματα. |

    Ο **δυνατός τύπος** χρησιμοποιείται για έμφαση ή αντίθεση:
    > ***Εμένα** μου αρέσει. Εσένα;*
    """)
    else:
        _md = mo.md("""
    ## Grammar: Indirect Object Pronouns

    Greek uses the **genitive case** for indirect objects (equivalent to English "to me", "for you", etc.).
    There are two forms: **weak (clitic)** and **strong (emphatic)**.

    | Person | Weak Form | Strong Form | Example |
    |--------|-----------|-------------|---------|
    | 1st sg | **μου** | εμένα | **Μου** αρέσει το σπίτι. *(I like the house.)* |
    | 2nd sg | **σου** | εσένα | **Σου** έδωσα το κλειδί. *(I gave you the key.)* |
    | 3rd sg m | **του** | αυτού | **Του** στέλνω το συμβόλαιο. *(I'm sending him the contract.)* |
    | 3rd sg f | **της** | αυτής | **Της** λέω την τιμή. *(I tell her the price.)* |
    | 3rd sg n | **του** | αυτού | — |
    | 1st pl | **μας** | εμάς | **Μας** φτιάχνεις καφέ; *(Will you make us coffee?)* |
    | 2nd pl | **σας** | εσάς | **Σας** πάει πολύ. *(It suits you very much.)* |
    | 3rd pl | **τους** | αυτών | **Τους** είπε ψέματα. *(He told them lies.)* |

    **Strong form** is used for emphasis or contrast:
    > ***Εμένα** μου αρέσει. Εσένα;* (I like it. What about you?)
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Genitive for Possession
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ## Грамматика: Родительный падеж для выражения принадлежности

    **Родительный падеж** выражает принадлежность или отношение к кому-либо.

    | Пример | Перевод |
    |---------|-------------|
    | Το σπίτι **του Κώστα** | Дом Костаса |
    | Το κλειδί **της κυρίας** | Ключ госпожи |
    | Το δωμάτιο **του παιδιού** | Комната ребёнка |
    | **Ποιανού** είναι το σπίτι; | Чей это дом? |

    Вопросительное слово **ποιανού / τίνος** = «чей»
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ## Γραμματική: Γενική Πτώση για Κατοχή

    Η **γενική πτώση** εκφράζει κτήση ή ανήκειν σε κάποιον/κάτι.

    | Παράδειγμα | Σημασία |
    |---------|-------------|
    | Το σπίτι **του Κώστα** | Το σπίτι που ανήκει στον Κώστα |
    | Το κλειδί **της κυρίας** | Το κλειδί της κυρίας |
    | Το δωμάτιο **του παιδιού** | Το δωμάτιο του παιδιού |
    | **Ποιανού** είναι το σπίτι; | Σε ποιον ανήκει το σπίτι; |

    Η ερωτηματική αντωνυμία **ποιανού / τίνος** = «σε ποιον ανήκει»
    """)
    else:
        _md = mo.md("""
    ## Grammar: Genitive Case for Possession

    The **genitive case** expresses ownership or belonging.

    | Example | Translation |
    |---------|-------------|
    | Το σπίτι **του Κώστα** | Kostas's house |
    | Το κλειδί **της κυρίας** | The lady's key |
    | Το δωμάτιο **του παιδιού** | The child's room |
    | **Ποιανού** είναι το σπίτι; | Whose house is it? |

    The question word **ποιανού / τίνος** = "whose"
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Possessive Pronouns
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ## Грамматика: Притяжательные местоимения (δικός μου)

    Используются для **выделения** или чёткого указания на принадлежность.

    **Схема:** [Артикль] + **δικός / δική / δικό** + [Слабое местоимение]

    | Форма | Пример | Перевод |
    |------|---------|-------------|
    | δικός μου / δική μου / δικό μου | Το σπίτι είναι **δικό μου**. | Дом принадлежит мне. |
    | δικός σου / δική σου / δικό σου | Έχεις **δικό σου** σπίτι; | У тебя есть собственный дом? |
    | δικός του / δική του / δικό του | Αυτό είναι **δικό του**. | Это его. |
    | δικός μας / δική μας / δικό μας | Το σαλόνι είναι **δικό μας**. | Гостиная наша. |
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ## Γραμματική: Κτητικές Αντωνυμίες (δικός μου)

    Χρησιμοποιούνται για **έμφαση** ή για να διευκρινίσουμε την κτήση.

    **Σχήμα:** [Άρθρο] + **δικός / δική / δικό** + [Αδύνατη αντωνυμία]

    | Τύπος | Παράδειγμα | Σημασία |
    |------|---------|-------------|
    | δικός μου / δική μου / δικό μου | Το σπίτι είναι **δικό μου**. | Το σπίτι ανήκει σε μένα. |
    | δικός σου / δική σου / δικό σου | Έχεις **δικό σου** σπίτι; | Έχεις σπίτι στο όνομά σου; |
    | δικός του / δική του / δικό του | Αυτό είναι **δικό του**. | Αυτό ανήκει σε αυτόν. |
    | δικός μας / δική μας / δικό μας | Το σαλόνι είναι **δικό μας**. | Το σαλόνι ανήκει σε μας. |
    """)
    else:
        _md = mo.md("""
    ## Grammar: Possessive Pronouns (δικός μου)

    Used for **emphasis** or to distinguish ownership clearly.

    **Pattern:** [Article] + **δικός / δική / δικό** + [Weak Pronoun]

    | Form | Example | Translation |
    |------|---------|-------------|
    | δικός μου / δική μου / δικό μου | Το σπίτι είναι **δικό μου**. | The house is mine. |
    | δικός σου / δική σου / δικό σου | Έχεις **δικό σου** σπίτι; | Do you have your own house? |
    | δικός του / δική του / δικό του | Αυτό είναι **δικό του**. | That's his. |
    | δικός μας / δική μας / δικό μας | Το σαλόνι είναι **δικό μας**. | The living room is ours. |
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Useful phrases cell
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ## Полезные фразы (Πώς το λένε;)

    | Греческий | Русский | Контекст |
    |-------|---------|---------|
    | Το σπίτι βγάζει προβλήματα. | В доме возникают проблемы. | Сообщение о ремонте |
    | Εμένα μου αρέσει. Εσένα; | Мне нравится. А тебе? | Обсуждение предпочтений |
    | Ποιανού είναι το σπίτι; | Чей это дом? | Вопрос о собственности |
    | Το ενοίκιο είναι λογικό. | Арендная плата разумная. | Обсуждение цены |
    | Πού τη βάζω την κούτα; | Куда мне поставить коробку? | Во время переезда |
    | Η τιμή θα είναι πολύ πιο χαμηλή. | Цена будет намного ниже. | Комментарий о низких затратах |
    | Θέλω να συμφωνήσουμε πριν την επισκευή. | Хочу, чтобы мы договорились до ремонта. | Переговоры с арендодателем |
    | Έχω τις μαύρες μου. | У меня плохое настроение. | Выражение недовольства |
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ## Χρήσιμες Φράσεις (Πώς το λένε;)

    | Φράση | Σημασία (αγγλικά) | Πλαίσιο |
    |-------|---------|---------|
    | Το σπίτι βγάζει προβλήματα. | The house is having issues. | Αναφορά βλάβης |
    | Εμένα μου αρέσει. Εσένα; | I like it. What about you? | Συζήτηση προτιμήσεων |
    | Ποιανού είναι το σπίτι; | Whose house is it? | Ερώτηση για ιδιοκτησία |
    | Το ενοίκιο είναι λογικό. | The rent is reasonable. | Συζήτηση τιμής |
    | Πού τη βάζω την κούτα; | Where do I put the box? | Κατά τη μετακόμιση |
    | Η τιμή θα είναι πολύ πιο χαμηλή. | The price will be much lower. | Σχόλιο για χαμηλό κόστος |
    | Θέλω να συμφωνήσουμε πριν την επισκευή. | I want us to agree before the repair. | Διαπραγμάτευση με ιδιοκτήτη |
    | Έχω τις μαύρες μου. | I am in a bad mood. | Έκφραση δυσαρέσκειας |
    """)
    else:
        _md = mo.md("""
    ## Useful Phrases (Πώς το λένε;)

    | Greek | English | Context |
    |-------|---------|---------|
    | Το σπίτι βγάζει προβλήματα. | The house is having issues. | Reporting maintenance |
    | Εμένα μου αρέσει. Εσένα; | I like it. What about you? | Discussing preferences |
    | Ποιανού είναι το σπίτι; | Whose house is it? | Asking about ownership |
    | Το ενοίκιο είναι λογικό. | The rent is reasonable. | Discussing price |
    | Πού τη βάζω την κούτα; | Where do I put the box? | During a move |
    | Η τιμή θα είναι πολύ πιο χαμηλή. | The price will be much lower. | Commenting on low costs |
    | Θέλω να συμφωνήσουμε πριν την επισκευή. | I want us to agree before the repair. | Negotiating with landlord |
    | Έχω τις μαύρες μου. | I am in a bad mood. | Expressing dissatisfaction |
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 1 heading
    mo.md(t_ui("test1_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Noun state init
    tbl_sel_n, set_tbl_sel_n = mo.state(None)
    session_total_n, set_session_total_n = mo.state(0)
    return session_total_n, set_session_total_n, set_tbl_sel_n, tbl_sel_n


@app.cell(hide_code=True)
def _(mo):
    # Noun file upload
    file_upload_noun = mo.ui.file(label="Load nouns TSV")
    file_upload_noun
    return (file_upload_noun,)


@app.cell(hide_code=True)
def _(file_upload_noun, gu, language_selector, notebook_dir, os, pd):
    # Load noun data
    if file_upload_noun.value:
        df_noun = gu.load_data(file_upload_noun, [])
    else:
        _ru = os.path.join(notebook_dir, 'nouns_ru.tsv')
        _default = os.path.join(notebook_dir, 'nouns.tsv')
        _path = _ru if language_selector.value == 'ru' and os.path.exists(_ru) else _default
        try:
            df_noun = pd.read_csv(_path, sep='\t')
        except FileNotFoundError:
            df_noun = None
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, language_selector, mo, t_ui, tbl_sel_n):
    # Noun table
    table_noun = mo.ui.table(df_noun, selection="multi", initial_selection=tbl_sel_n()) if df_noun is not None else None
    _lang = language_selector.value
    _table_noun = table_noun if table_noun is not None else mo.md(t_ui("nouns_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_nouns", _lang)), _table_noun])
    return (table_noun,)


@app.cell(hide_code=True)
def _(gu, mo, random, session_total_n, set_session_total_n, table_noun):
    # Noun words + state
    words_noun = gu.get_words(table_noun)
    words4test_noun, set_words4test_noun = mo.state(words_noun.copy() if words_noun else [])
    if words_noun:
        if len(words_noun) > session_total_n():
            set_session_total_n(len(words_noun))
    else:
        set_session_total_n(0)
    noun_msg, set_noun_msg = mo.state("")
    current_noun, set_current_noun = mo.state(None)
    captured_simple, set_captured_simple = mo.state(None)
    captured_article, set_captured_article = mo.state(None)
    _clk = lambda v: (v or 0) + 1
    skip_button_n = mo.ui.button(label="Skip", on_click=_clk)
    clear_button_n = mo.ui.button(label="Clear", on_click=_clk)
    skip_count_n, set_skip_count_n = mo.state(0)
    clear_count_n, set_clear_count_n = mo.state(0)
    submit_count_n, set_submit_count_n = mo.state(0)
    if words_noun:
        if current_noun() is None:
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
    # Simple noun form
    clear_count_n()
    _nc = current_noun()
    noun_word, noun_trans, noun_form = gu.create_noun_test_ui([_nc] if _nc else [], mode='simple')
    return noun_form, noun_trans, noun_word


@app.cell(hide_code=True)
def _(clear_count_n, current_noun, gu):
    # Article noun form
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
    # Noun submit button
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
    submit_button_n = mo.ui.button(label="Submit", on_click=_clk, kind="warn" if _dirty else "neutral")
    set_submit_count_n(0)
    return (submit_button_n,)


@app.cell(hide_code=True)
def _(
    captured_simple,
    clear_button_n,
    gu,
    language_selector,
    mo,
    noun_form,
    noun_trans,
    noun_word,
    session_total_n,
    skip_button_n,
    submit_button_n,
    t_ui,
    words4test_noun,
):
    # Simple noun display
    _lang = language_selector.value
    _feedback = mo.md("")
    if words4test_noun() and noun_word:
        _cs = captured_simple()
        if _cs and getattr(_cs, 'test_word', None) == noun_word:
            with mo.capture_stdout() as _buf:
                gu.check_noun_test(noun_word, _cs, mode='simple')
            if _buf.getvalue():
                _feedback = mo.md(_buf.getvalue())
        _view = mo.vstack([
            mo.md(f"{t_ui('simple_noun_heading', _lang)} ({len(words4test_noun())}/{session_total_n()})"),
            mo.md(f"{t_ui('translation_label', _lang)} **{noun_trans}**"),
            noun_form,
            _feedback,
            mo.hstack([skip_button_n, clear_button_n, submit_button_n], justify="end"),
        ])
    else:
        _view = mo.md(t_ui("noun_empty", _lang))
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
    language_selector,
    mo,
    session_total_n,
    skip_button_n,
    submit_button_n,
    t_ui,
    words4test_noun,
):
    # Article noun display
    _lang = language_selector.value
    _feedback_a = mo.md("")
    if words4test_noun() and art_noun_word:
        _ca = captured_article()
        if _ca and getattr(_ca, 'test_word', None) == art_noun_word:
            with mo.capture_stdout() as _buf_a:
                gu.check_noun_test(art_noun_word, _ca, mode='article')
            if _buf_a.getvalue():
                _feedback_a = mo.md(_buf_a.getvalue())
        _view_art = mo.vstack([
            mo.md(f"{t_ui('article_noun_heading', _lang)} ({len(words4test_noun())}/{session_total_n()})"),
            mo.md(f"{t_ui('translation_label', _lang)} **{art_noun_trans}**"),
            art_noun_form,
            _feedback_a,
            mo.hstack([skip_button_n, clear_button_n, submit_button_n], justify="end"),
        ])
    else:
        _view_art = mo.md(t_ui("noun_empty", _lang))
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
    language_selector,
    random,
    session_total_n,
    set_captured_article,
    set_captured_simple,
    set_current_noun,
    set_noun_msg,
    set_tbl_sel_n,
    set_words4test_noun,
    t_ui,
    words4test_noun,
):
    # Noun check handler
    _lang = language_selector.value
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
            set_noun_msg(t_ui("noun_passed", _lang).format(word=_cn["Word"], remaining=len(_new), total=session_total_n()))
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
        if noun_word and noun_form is not None:
            set_captured_simple(gu.make_snapshot(noun_form))
        if art_noun_word and art_noun_form is not None:
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
def _(language_selector, mo, t_ui):
    # Test 2 heading
    mo.md(t_ui("test2_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Verb state init
    tbl_sel_v, set_tbl_sel_v = mo.state(None)
    session_total_v, set_session_total_v = mo.state(0)
    return session_total_v, set_session_total_v, set_tbl_sel_v, tbl_sel_v


@app.cell(hide_code=True)
def _(mo):
    # Verb file upload
    file_upload_verb = mo.ui.file(label="Load verbs TSV")
    file_upload_verb
    return (file_upload_verb,)


@app.cell(hide_code=True)
def _(file_upload_verb, gu, language_selector, notebook_dir, os, pd):
    # Load verb data
    if file_upload_verb.value:
        df_verb = gu.load_data(file_upload_verb, [])
    else:
        _ru = os.path.join(notebook_dir, 'verbs_ru.tsv')
        _default = os.path.join(notebook_dir, 'verbs.tsv')
        _path = _ru if language_selector.value == 'ru' and os.path.exists(_ru) else _default
        try:
            df_verb = pd.read_csv(_path, sep='\t')
        except FileNotFoundError:
            df_verb = None
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, language_selector, mo, t_ui, tbl_sel_v):
    # Verb table
    table_verb = mo.ui.table(df_verb, selection="multi", initial_selection=tbl_sel_v()) if df_verb is not None else None
    _lang = language_selector.value
    _table_verb = table_verb if table_verb is not None else mo.md(t_ui("verbs_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_verbs", _lang)), _table_verb])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu, language_selector, mo, t_ui):
    # Tense selector
    _lang = language_selector.value
    _b1_tenses = ['present', 'imperfect', 'aorist', 'future', 'future_continuous']
    if _lang == 'ru':
        _tense_names = {
            'present': 'Настоящее',
            'imperfect': 'Прошедшее незавершённое',
            'aorist': 'Прошедшее завершённое',
            'future': 'Будущее простое',
            'future_continuous': 'Будущее длительное',
        }
    elif _lang == 'el':
        _tense_names = {
            'present': 'Ενεστώτας',
            'imperfect': 'Παρατατικός',
            'aorist': 'Αόριστος',
            'future': 'Απλός Μέλλοντας',
            'future_continuous': 'Εξακολουθητικός Μέλλοντας',
        }
    else:
        _tense_names = {
            'present': 'Present',
            'imperfect': 'Imperfect (Past)',
            'aorist': 'Simple Past',
            'future': 'Simple Future',
            'future_continuous': 'Continuous Future',
        }
    _tense_options = {
        f"{gu.TENSE_LABELS[k]['greek']} ({_tense_names[k]})": k
        for k in _b1_tenses if k in gu.TENSE_LABELS
    }
    _first_key = next(iter(_tense_options))
    tense_selector = mo.ui.dropdown(
        options=_tense_options,
        value=_first_key,
        label=t_ui("tense_label", _lang),
    )
    tense_selector
    return (tense_selector,)


@app.cell(hide_code=True)
def _(gu, mo, session_total_v, set_session_total_v, table_verb):
    # Verb words + state
    words_verb = gu.get_words(table_verb)
    words4test_verb, set_words4test_verb = mo.state(words_verb.copy() if words_verb else [])
    if words_verb:
        if len(words_verb) > session_total_v():
            set_session_total_v(len(words_verb))
    else:
        set_session_total_v(0)
    verb_msg, set_verb_msg = mo.state("")
    captured_verb, set_captured_verb = mo.state(None)
    _clk = lambda v: (v or 0) + 1
    skip_button_v = mo.ui.button(label="Skip", on_click=_clk)
    clear_button_v = mo.ui.button(label="Clear", on_click=_clk)
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
    # Verb submit button
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
    submit_button_v = mo.ui.button(label="Submit", on_click=_clk, kind="warn" if _dirty else "neutral")
    set_submit_count_v(0)
    return (submit_button_v,)


@app.cell(hide_code=True)
def _(
    captured_verb,
    clear_button_v,
    cv_verb,
    gu,
    language_selector,
    mo,
    session_total_v,
    skip_button_v,
    submit_button_v,
    t_ui,
    tense_selector,
    verb_fields,
    verb_msg,
    words4test_verb,
):
    # Verb display
    _lang = language_selector.value
    _TENSE_LABELS = {k: gu.TENSE_LABELS[k]['greek'] for k in gu.TENSE_LABELS}
    if not words4test_verb():
        _view_verb = mo.md(t_ui("verb_empty", _lang))
    elif not tense_selector.value:
        _view_verb = mo.md(t_ui("verb_no_tense", _lang))
    else:
        _feedback_v = mo.md("")
        _c = captured_verb()
        if cv_verb and _c and getattr(_c, 'verb_word', None) == cv_verb['Word'] and getattr(_c, 'tense', None) == tense_selector.value:
            _, _msg = gu.check_verb_test(cv_verb['Word'], _c, tense_selector.value)
            _feedback_v = mo.md(_msg)
        _label = _TENSE_LABELS.get(tense_selector.value, tense_selector.value)
        _rem = len(words4test_verb())
        _items = [mo.md(f"{t_ui('verb_heading', _lang)} — {_label} ({_rem}/{session_total_v()})")]
        if verb_msg():
            _items.append(mo.md(verb_msg()))
        _items += [
            mo.md(f"{t_ui('translation_label', _lang)} **{cv_verb['Translation']}**") if cv_verb else mo.md(""),
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
    language_selector,
    session_total_v,
    set_captured_verb,
    set_tbl_sel_v,
    set_verb_msg,
    set_words4test_verb,
    t_ui,
    tense_selector,
    words4test_verb,
):
    # Verb check handler
    _lang = language_selector.value
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
            set_verb_msg(t_ui("verb_passed", _lang).format(word=cv_verb["Word"], trans=cv_verb["Translation"], remaining=len(_new), total=session_total_v()))
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
        if cv_verb and verb_fields is not None:
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
def _(language_selector, mo, t_ui):
    # Test 3 heading
    mo.md(t_ui("test3_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Adjective state init
    tbl_sel_a, set_tbl_sel_a = mo.state(None)
    session_total_a, set_session_total_a = mo.state(0)
    return session_total_a, set_session_total_a, set_tbl_sel_a, tbl_sel_a


@app.cell(hide_code=True)
def _(mo):
    # Adjective file upload
    file_upload_adj = mo.ui.file(label="Load adjectives TSV")
    file_upload_adj
    return (file_upload_adj,)


@app.cell(hide_code=True)
def _(file_upload_adj, gu, language_selector, notebook_dir, os, pd):
    # Load adjective data
    if file_upload_adj.value:
        df_adj = gu.load_data(file_upload_adj, [])
    else:
        _ru = os.path.join(notebook_dir, 'adjectives_ru.tsv')
        _default = os.path.join(notebook_dir, 'adjectives.tsv')
        _path = _ru if language_selector.value == 'ru' and os.path.exists(_ru) else _default
        try:
            df_adj = pd.read_csv(_path, sep='\t')
        except FileNotFoundError:
            df_adj = None
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, language_selector, mo, t_ui, tbl_sel_a):
    # Adjective table
    table_adj = mo.ui.table(df_adj, selection="multi", initial_selection=tbl_sel_a()) if df_adj is not None else None
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
def _(gu, mo, random, session_total_a, set_session_total_a, table_adj):
    # Adjective words + state
    words_adj = gu.get_words(table_adj)
    words4test_adj, set_words4test_adj = mo.state(words_adj.copy() if words_adj else [])
    if words_adj:
        if len(words_adj) > session_total_a():
            set_session_total_a(len(words_adj))
    else:
        set_session_total_a(0)
    adj_last_passed_mesg, set_adj_last_passed_mesg = mo.state("")
    adj_cv, set_adj_cv = mo.state(None)
    captured_adj, set_captured_adj = mo.state(None)
    _clk = lambda v: (v or 0) + 1
    skip_button_a = mo.ui.button(label="Skip", on_click=_clk)
    clear_button_a = mo.ui.button(label="Clear", on_click=_clk)
    skip_count_a, set_skip_count_a = mo.state(0)
    clear_count_a, set_clear_count_a = mo.state(0)
    submit_count_a, set_submit_count_a = mo.state(0)
    if words_adj:
        if adj_cv() is None:
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
    # Adjective form
    clear_count_a()
    _acv = adj_cv()
    _mode = mode_selector.value
    adj_form, _ = gu.create_adjective_test_ui([] if not _acv else [_acv], [], _acv, mode=_mode)
    return (adj_form,)


@app.cell(hide_code=True)
def _(adj_form, captured_adj, mo, set_submit_count_a):
    # Adjective submit button
    _values = adj_form.value if adj_form is not None else []
    _snap = captured_adj()
    _has_input = bool(_values and any(v.strip() for v in _values))
    _matches_snap = _snap is not None and [v.strip() for v in _values] == [v.strip() for v in (_snap.value or [])]
    _dirty = _has_input and not _matches_snap
    _clk = lambda v: (v or 0) + 1
    submit_button_a = mo.ui.button(label="Submit", on_click=_clk, kind="warn" if _dirty else "neutral")
    set_submit_count_a(0)
    return (submit_button_a,)


@app.cell(hide_code=True)
def _(
    adj_cv,
    adj_form,
    captured_adj,
    clear_button_a,
    gu,
    language_selector,
    mo,
    mode_selector,
    session_total_a,
    skip_button_a,
    submit_button_a,
    t_ui,
    words4test_adj,
):
    # Adjective display
    _lang = language_selector.value
    _adj = adj_cv()
    _mode = mode_selector.value
    if words4test_adj() and _adj:
        _feedback_a = mo.md("")
        _c = captured_adj()
        if _c and getattr(_c, 'adj_word', None) == _adj['Word']:
            _, _msg = gu.check_adjective_test(_adj['Word'], _c, mode=_mode)
            if _msg:
                _feedback_a = mo.md(_msg)
        _view_adj = mo.vstack([
            mo.md(f"{t_ui('adj_heading', _lang)} ({len(words4test_adj())}/{session_total_a()})"),
            mo.md(f"{t_ui('translation_label', _lang)} **{_adj['Translation']}**"),
            adj_form,
            _feedback_a,
            mo.hstack([skip_button_a, clear_button_a, submit_button_a], justify="end"),
        ])
    else:
        _view_adj = mo.md(t_ui("adj_empty", _lang))
    _view_adj
    return


@app.cell(hide_code=True)
def _(adj_last_passed_mesg, mo):
    # Adjective message
    mo.md(adj_last_passed_mesg())
    return


@app.cell(hide_code=True)
def _(
    adj_cv,
    captured_adj,
    df_adj,
    gu,
    language_selector,
    random,
    session_total_a,
    set_adj_cv,
    set_adj_last_passed_mesg,
    set_captured_adj,
    set_tbl_sel_a,
    set_words4test_adj,
    t_ui,
    words4test_adj,
):
    # Adjective check handler
    _lang = language_selector.value
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
            set_adj_last_passed_mesg(t_ui("adj_passed", _lang).format(word=_adj["Word"], trans=_adj["Translation"], remaining=len(_new), total=session_total_a()))
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
    # Adjective submit handler
    if (submit_button_a.value or 0) > submit_count_a():
        set_submit_count_a(submit_button_a.value)
        _acv = adj_cv()
        if _acv and adj_form is not None:
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
    # Adjective skip handler
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
    # Adjective clear handler
    if (clear_button_a.value or 0) > clear_count_a():
        set_clear_count_a(clear_button_a.value)
        set_captured_adj(None)
    return


@app.cell(hide_code=True)
def _():
    # UI strings
    UI_STRINGS = {
        "en": {
            "test1_heading": "---\n## Test 1: Nouns (Ουσιαστικά)",
            "test2_heading": "---\n## Test 2: Verbs (Ρήματα)",
            "test3_heading": "---\n## Test 3: Adjectives (Επίθετα)",
            "select_nouns": "### Select nouns to test",
            "select_verbs": "### Select verbs to test",
            "select_adjs": "### Select adjectives to test",
            "translation_label": "Translation:",
            "simple_noun_heading": "**Simple declension**",
            "article_noun_heading": "**Article declension**",
            "verb_heading": "**Verb test**",
            "adj_heading": "**Adjective test**",
            "noun_empty": "_Select words above to start the test._",
            "verb_empty": "_Select verbs above to start the test._",
            "verb_no_tense": "_Select a tense above._",
            "adj_empty": "_Select adjectives above to start the test._",
            "tense_label": "Tense:",
            "mode_label": "Test mode:",
            "nouns_not_found": "_nouns.tsv not found — upload a file to begin._",
            "verbs_not_found": "_verbs.tsv not found — upload a file to begin._",
            "adjs_not_found": "_adjectives.tsv not found — upload a file to begin._",
            "noun_passed": '<span style="color:green;">Test for <b>"{word}"</b> passed.\n\n{remaining} words remaining out of {total}.</span>',
            "verb_passed": '<span style="color:green;">Test for <b>"{word} — {trans}"</b> passed.\n\n{remaining} words remaining out of {total}.</span>',
            "adj_passed": '<span style="color:green;">Test for <b>"{word} — {trans}"</b> passed.\n\n{remaining} words remaining out of {total}.</span>',
        },
        "ru": {
            "test1_heading": "---\n## Тест 1: Существительные (Ουσιαστικά)",
            "test2_heading": "---\n## Тест 2: Глаголы (Ρήματα)",
            "test3_heading": "---\n## Тест 3: Прилагательные (Επίθετα)",
            "select_nouns": "### Выберите существительные для теста",
            "select_verbs": "### Выберите глаголы для теста",
            "select_adjs": "### Выберите прилагательные для теста",
            "translation_label": "Перевод:",
            "simple_noun_heading": "**Склонение**",
            "article_noun_heading": "**Артикли**",
            "verb_heading": "**Тест по глаголам**",
            "adj_heading": "**Тест по прилагательным**",
            "noun_empty": "_Выберите слова выше для начала теста._",
            "verb_empty": "_Выберите глаголы выше для начала теста._",
            "verb_no_tense": "_Выберите время выше._",
            "adj_empty": "_Выберите прилагательные выше для начала теста._",
            "tense_label": "Время:",
            "mode_label": "Режим теста:",
            "nouns_not_found": "_nouns.tsv не найден — загрузите файл._",
            "verbs_not_found": "_verbs.tsv не найден — загрузите файл._",
            "adjs_not_found": "_adjectives.tsv не найден — загрузите файл._",
            "noun_passed": '<span style="color:green;">Тест для <b>"{word}"</b> пройден.\n\n{remaining} слов осталось из {total}.</span>',
            "verb_passed": '<span style="color:green;">Тест для <b>"{word} — {trans}"</b> пройден.\n\n{remaining} слов осталось из {total}.</span>',
            "adj_passed": '<span style="color:green;">Тест для <b>"{word} — {trans}"</b> пройден.\n\n{remaining} слов осталось из {total}.</span>',
        },
        "el": {
            "test1_heading": "---\n## Τεστ 1: Ουσιαστικά",
            "test2_heading": "---\n## Τεστ 2: Ρήματα",
            "test3_heading": "---\n## Τεστ 3: Επίθετα",
            "select_nouns": "### Επιλέξτε ουσιαστικά για τεστ",
            "select_verbs": "### Επιλέξτε ρήματα για τεστ",
            "select_adjs": "### Επιλέξτε επίθετα για τεστ",
            "translation_label": "Μετάφραση:",
            "simple_noun_heading": "**Κλίση**",
            "article_noun_heading": "**Άρθρα**",
            "verb_heading": "**Τεστ ρημάτων**",
            "adj_heading": "**Τεστ επιθέτων**",
            "noun_empty": "_Επιλέξτε λέξεις παραπάνω για να ξεκινήσετε το τεστ._",
            "verb_empty": "_Επιλέξτε ρήματα παραπάνω για να ξεκινήσετε το τεστ._",
            "verb_no_tense": "_Επιλέξτε χρόνο παραπάνω._",
            "adj_empty": "_Επιλέξτε επίθετα παραπάνω για να ξεκινήσετε το τεστ._",
            "tense_label": "Χρόνος:",
            "mode_label": "Τρόπος τεστ:",
            "nouns_not_found": "_Το αρχείο nouns.tsv δεν βρέθηκε — φόρτωσε αρχείο._",
            "verbs_not_found": "_Το αρχείο verbs.tsv δεν βρέθηκε — φόρτωσε αρχείο._",
            "adjs_not_found": "_Το αρχείο adjectives.tsv δεν βρέθηκε — φόρτωσε αρχείο._",
            "noun_passed": '<span style="color:green;">Τεστ για <b>"{word}"</b> ολοκληρώθηκε.\n\n{remaining} λέξεις απομένουν από {total}.</span>',
            "verb_passed": '<span style="color:green;">Τεστ για <b>"{word} — {trans}"</b> ολοκληρώθηκε.\n\n{remaining} λέξεις απομένουν από {total}.</span>',
            "adj_passed": '<span style="color:green;">Τεστ για <b>"{word} — {trans}"</b> ολοκληρώθηκε.\n\n{remaining} λέξεις απομένουν από {total}.</span>',
        },
    }

    def t_ui(key, lang=None):
        _lang = lang if lang else "en"
        return UI_STRINGS.get(_lang, UI_STRINGS["en"]).get(key, UI_STRINGS["en"].get(key, key))

    return (t_ui,)


@app.cell(hide_code=True)
def _(mo):
    # Language selector
    language_selector = mo.ui.dropdown(
        options={"English": "en", "Русский": "ru", "Ελληνικά": "el"},
        value="English",
        label="🌐",
    )
    mo.Html(f"""
    <div style="position: fixed; top: 60px; right: 10px; z-index: 1000; background: white; padding: 8px 12px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
        {language_selector}
    </div>
    """)
    return (language_selector,)


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
