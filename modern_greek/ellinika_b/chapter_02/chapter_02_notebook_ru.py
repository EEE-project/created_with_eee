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
    # Σπίτι μου σπιτάκι μου 🏠
    ## Дом, милый дом

    **Учебник:** Ελληνικά Β' | **Глава:** 2 (Ενότητα 2) | **Уровень:** B1 | **Язык:** Русский

    **Тема:** Жильё и проживание (Κατοικία, διαμονή)

    **Тесты в этой тетради:** Существительные · Глаголы · Прилагательные
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
            mo.md(f"#### Склонение ({_total - _remaining + 1}/{_total})"),
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
            mo.md(f"#### Артикли ({_total - _remaining + 1}/{_total})"),
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
        for k in gu.TENSE_LABELS
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
