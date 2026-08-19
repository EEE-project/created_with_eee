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
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Οι δρόμοι της πόλης
    ## Дороги города

    **Учебник:** Ελληνικά Β' | **Глава:** 3 (Ενότητα 3) | **Уровень:** B1 | **Язык:** Русский

    **Тема:** Городская жизнь, общественный транспорт, ориентирование (Είχε τέτοια κίνηση!)

    **Тесты в этой тетради:** Существительные · Глаголы · Прилагательные
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Грамматика: Неопределённые местоимения (Αόριστες Αντωνυμίες)

    Неопределённые местоимения указывают на **неконкретных** людей или вещи.

    | Местоимение | Значение | Муж. (Им.) | Жен. (Им.) | Ср. (Им.) |
    |-------------|----------|------------|-----------|-----------|
    | κάποιος | кто-то | κάποιος | κάποια | κάποιο |
    | κανένας | никто / кто-либо | κανένας | καμία | κανένα |
    | ο καθένας | каждый | ο καθένας | η καθεμία | το καθένα |

    **Формы винительного падежа:**

    | | Муж. | Жен. | Ср. |
    |-|------|------|-----|
    | κάποιος | κάποιον | κάποια | κάποιο |
    | κανένας | κανέναν | καμία | κανένα |
    | ο καθένας | τον καθέναν | την καθεμία | το καθένα |

    **Примеры:**
    - **Κάποιος** σε ζητάει στο τηλέφωνο. — _Тебя кто-то спрашивает по телефону._
    - **Κανένας** δεν ήρθε. — _Никто не пришёл._
    - **Ο καθένας** έχει τη γνώμη του. — _У каждого своё мнение._
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Грамматика: Указательные местоимения (Δεικτικές Αντωνυμίες)

    Указательные местоимения указывают на **конкретные качества или количества**.

    | Местоимение | Значение | Муж. (Им.) | Жен. (Им.) | Ср. (Им.) |
    |-------------|----------|------------|-----------|-----------|
    | ίδιος | тот же самый | ο ίδιος | η ίδια | το ίδιο |
    | τέτοιος | такой | τέτοιος | τέτοια | τέτοιο |
    | τόσος | столько | τόσος | τόση | τόσο |

    **Формы винительного падежа:**

    | | Муж. | Жен. | Ср. |
    |-|------|------|-----|
    | ίδιος | τον ίδιο | την ίδια | το ίδιο |
    | τέτοιος | τέτοιον | τέτοια | τέτοιο |
    | τόσος | τόσον | τόση | τόσο |

    **Примеры:**
    - Έχουμε **το ίδιο** πρόβλημα. — _У нас та же проблема._
    - **Τέτοια** κίνηση δεν έχω ξαναδεί! — _Я никогда не видел такого движения!_
    - **Τόση** κίνηση! — _Столько машин!_
    - Μην βάζεις **τόση** ζάχαρη! — _Не клади столько сахара!_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Полезные фразы (Πώς το λένε;)

    | Греческий | Русский | Контекст |
    |-----------|---------|----------|
    | Πώς θα πάω στο ...; | Как мне добраться до ...? | Спросить дорогу |
    | Πού είναι η πλησιέστερη στάση; | Где ближайшая остановка? | Общественный транспорт |
    | Πού κατεβαίνω για το ...; | Где выходить на ...? | Автобус / Метро |
    | Στρίψτε δεξιά / αριστερά. | Поверните направо / налево. | Объяснить дорогу |
    | Προχωρήστε ίσια / ευθεία. | Идите прямо. | Объяснить дорогу |
    | Στο τρίτο στενό. | На третьем переулке. | Указать поворот |
    | Είχε τόση κίνηση! | Было столько пробок! | Объяснить опоздание |
    | Πάνω στην ώρα! | Точно вовремя! | Прийти вовремя |
    """)
    return


@app.cell(hide_code=True)
def _():
    import os
    import random
    import marimo as mo

    from modern_greek_eee import greek_utils as gu

    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    return gu, mo, notebook_dir, random


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Тест: Существительные (Ουσιαστικά)
    """)
    return


@app.cell(hide_code=True)
def _(gu, notebook_dir):
    df_noun = gu.load_vocab_table("nouns_ru.tsv", nb_dir=notebook_dir)
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, gu, mo):
    table_noun = gu.vocab_table(df_noun)
    mo.vstack([
        mo.md("### Выберите существительные для теста"),
        table_noun,
    ])
    return (table_noun,)


@app.cell(hide_code=True)
def _(gu, table_noun):
    words_noun = gu.get_words(table_noun)
    return (words_noun,)


@app.cell(hide_code=True)
def _(mo, random, words_noun):
    _shuffled = random.sample(words_noun, len(words_noun)) if words_noun else []
    words4test_noun, set_words4test_noun = mo.state(_shuffled)
    noun_current, set_noun_current = mo.state(_shuffled[0] if _shuffled else None)
    noun_msg, set_noun_msg = mo.state("")
    return (
        noun_current,
        noun_msg,
        set_noun_current,
        set_noun_msg,
        set_words4test_noun,
        words4test_noun,
    )


@app.cell(hide_code=True)
def _(gu, noun_current):
    _nc = noun_current()
    noun_word, noun_trans, noun_form = gu.create_noun_test_ui([_nc] if _nc else [], mode='simple')
    return noun_form, noun_trans, noun_word


@app.cell(hide_code=True)
def _(gu, noun_current):
    _acn = noun_current()
    art_noun_word, art_noun_trans, art_noun_form = gu.create_noun_test_ui([_acn] if _acn else [], mode='article')
    return art_noun_form, art_noun_trans, art_noun_word


@app.cell(hide_code=True)
def _(mo, noun_form, noun_trans, noun_word, words4test_noun, words_noun):
    if words4test_noun() and noun_word:
        _remaining = len(words4test_noun())
        _total = len(words_noun)
        _view = mo.vstack([
            mo.md(f"#### Склонение ({_remaining}/{_total})"),
            mo.md(f"Перевод: **{noun_trans}**"),
            noun_form,
        ])
    else:
        _view = mo.md("_Выберите существительные выше для начала теста._")
    _view
    return


@app.cell(hide_code=True)
def _(
    gu,
    noun_form,
    noun_word,
    set_noun_current,
    set_noun_msg,
    set_words4test_noun,
    words4test_noun,
    words_noun,
):
    _result = gu.process_noun_test(
        noun_word, noun_form, words_noun, words4test_noun,
        set_words4test_noun, set_noun_msg, set_noun_current, mode='simple'
    )
    _result
    return


@app.cell(hide_code=True)
def _(
    art_noun_form,
    art_noun_trans,
    art_noun_word,
    mo,
    words4test_noun,
    words_noun,
):
    if words4test_noun() and art_noun_word:
        _remaining = len(words4test_noun())
        _total = len(words_noun)
        _view = mo.vstack([
            mo.md(f"#### Артикли ({_remaining}/{_total})"),
            mo.md(f"Перевод: **{art_noun_trans}**"),
            art_noun_form,
        ])
    else:
        _view = mo.md("_Выберите существительные выше для начала теста._")
    _view
    return


@app.cell(hide_code=True)
def _(mo, noun_msg):
    mo.md(noun_msg())
    return


@app.cell(hide_code=True)
def _(
    art_noun_form,
    art_noun_word,
    gu,
    set_noun_current,
    set_noun_msg,
    set_words4test_noun,
    words4test_noun,
    words_noun,
):
    _result = gu.process_noun_test(
        art_noun_word, art_noun_form, words_noun, words4test_noun,
        set_words4test_noun, set_noun_msg, set_noun_current, mode='article'
    )
    _result
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Тест: Глаголы (Ρήματα)
    """)
    return


@app.cell(hide_code=True)
def _(gu, notebook_dir):
    df_verb = gu.load_vocab_table("verbs_ru.tsv", nb_dir=notebook_dir)
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, gu, mo):
    table_verb = gu.vocab_table(df_verb)
    mo.vstack([
        mo.md("### Выберите глаголы для теста"),
        table_verb,
    ])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu, table_verb):
    words_verb = gu.get_words(table_verb)
    return (words_verb,)


@app.cell(hide_code=True)
def _(gu, mo):
    _chapter_tenses = ['present', 'imperfect', 'aorist', 'future', 'future_continuous']
    _plain_ru = {
        'present': 'Настоящее',
        'imperfect': 'Прошедшее (незав.)',
        'aorist': 'Прошедшее простое',
        'future': 'Будущее простое',
        'future_continuous': 'Будущее продолжительное',
    }
    _tense_opts = {
        f"{gu.TENSE_LABELS[k]['greek']} ({_plain_ru[k]})": k
        for k in _chapter_tenses if k in gu.TENSE_LABELS
    }
    tense_selector = mo.ui.dropdown(
        options=_tense_opts,
        value=next(iter(_tense_opts)),
        label="Время:",
    )
    tense_selector
    return (tense_selector,)


@app.cell(hide_code=True)
def _(mo, random, words_verb):
    words4test_verb, set_words4test_verb = mo.state(random.sample(words_verb, len(words_verb)) if words_verb else [])
    verb_msg, set_verb_msg = mo.state("")
    return set_verb_msg, set_words4test_verb, verb_msg, words4test_verb


@app.cell(hide_code=True)
def _(gu, tense_selector, words4test_verb, words_verb):
    cv_verb = words4test_verb()[0] if words4test_verb() else None
    _tense_key = tense_selector.value
    _TENSE_UI_LABELS = {
        k: f"{gu.TENSE_LABELS[k]['greek']} ({gu.TENSE_LABELS[k]['english']})"
        for k in ['present', 'imperfect', 'aorist', 'future', 'future_continuous']
        if k in gu.TENSE_LABELS
    }
    _ui_label = _TENSE_UI_LABELS.get(_tense_key, _tense_key) if _tense_key else "Выберите время"
    verb_form, _verb_md = gu.create_verb_test_ui(_ui_label, words_verb, words4test_verb(), cv_verb)
    _verb_md
    return cv_verb, verb_form


@app.cell(hide_code=True)
def _(
    cv_verb,
    gu,
    mo,
    set_verb_msg,
    set_words4test_verb,
    tense_selector,
    verb_form,
    words4test_verb,
    words_verb,
):
    if cv_verb and verb_form is not None and verb_form.value:
        _ok, _errors = gu.check_verb_test(cv_verb['Word'], verb_form, tense_selector.value)
        if _ok:
            _new = [w for w in words4test_verb() if w["Word"] != cv_verb["Word"]]
            set_words4test_verb(_new)
            _remaining = len(_new)
            _total = len(words_verb)
            _msg = f'<span style="color: green;">Тест для <b>"{cv_verb["Word"]} — {cv_verb["Translation"]}"</b> пройден.\n\nОсталось {_remaining} из {_total}.</span>'
            set_verb_msg(_msg)
            _view = mo.md(_msg)
        else:
            _view = mo.md(_errors) if _errors else mo.md("")
    else:
        _view = mo.md("")
    _view
    return


@app.cell(hide_code=True)
def _(mo, verb_msg):
    mo.md(verb_msg())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Тест: Прилагательные (Επίθετα)
    """)
    return


@app.cell(hide_code=True)
def _(gu, notebook_dir):
    df_adj = gu.load_vocab_table("adjectives_ru.tsv", nb_dir=notebook_dir)
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, gu, mo):
    table_adj = gu.vocab_table(df_adj)
    mo.vstack([
        mo.md("### Выберите прилагательные для теста"),
        table_adj,
    ])
    return (table_adj,)


@app.cell(hide_code=True)
def _(gu, table_adj):
    adj_words = gu.get_words(table_adj)
    return (adj_words,)


@app.cell(hide_code=True)
def _(mo):
    mode_selector = mo.ui.radio(
        options={
            "Простой: 3 рода × 2 числа (6 полей)": "simple",
            "Полный: все роды, числа и падежи (18 полей)": "complex",
        },
        value="Простой: 3 рода × 2 числа (6 полей)",
        label="Режим теста:",
    )
    mode_selector
    return (mode_selector,)


@app.cell(hide_code=True)
def _(adj_words, mo, random):
    _shuffled = random.sample(adj_words, len(adj_words)) if adj_words else []
    adj_words4test, set_adj_words4test = mo.state(_shuffled)
    adj_cv, set_adj_cv = mo.state(_shuffled[0] if _shuffled else None)
    adj_last_passed_mesg, set_adj_last_passed_mesg = mo.state("")
    return (
        adj_cv,
        adj_last_passed_mesg,
        adj_words4test,
        set_adj_cv,
        set_adj_last_passed_mesg,
        set_adj_words4test,
    )


@app.cell(hide_code=True)
def _(adj_cv, adj_words, adj_words4test, gu, mode_selector):
    _current = adj_cv()
    _mode = mode_selector.value
    adj_form, _adj_md = gu.create_adjective_test_ui(
        adj_words,
        adj_words4test(),
        _current,
        mode=_mode,
    )
    _adj_md
    return (adj_form,)


@app.cell(hide_code=True)
def _(
    adj_cv,
    adj_form,
    adj_words,
    adj_words4test,
    gu,
    mo,
    mode_selector,
    set_adj_cv,
    set_adj_last_passed_mesg,
    set_adj_words4test,
):
    _current = adj_cv()
    if _current and adj_form is not None and adj_form.value:
        _ok, _errors = gu.check_adjective_test(_current['Word'], adj_form, mode=mode_selector.value)
        gu.process_adjective_completion(
            _current, _ok, adj_words, adj_words4test(),
            set_adj_words4test, set_adj_last_passed_mesg, set_adj_cv,
        )
        _view = mo.md(_errors) if (not _ok and _errors) else mo.md("")
    else:
        _view = mo.md("")
    _view
    return


@app.cell(hide_code=True)
def _(adj_last_passed_mesg, mo):
    mo.md(adj_last_passed_mesg())
    return


if __name__ == "__main__":
    app.run()
