# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.14",
#     "modern-greek-eee @ git+https://github.com/EEE-project/modern-greek-eee.git",
#     "modern-greek-inflexion-eee @ git+https://github.com/EEE-project/modern-greek-inflexion-eee.git",
#     "pandas",
# ]
#
# [tool.uv.sources]
# modern-greek-eee = { git = "https://github.com/EEE-project/modern-greek-eee" }
# modern-greek-inflexion-eee = { git = "https://github.com/EEE-project/modern-greek-inflexion-eee" }
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Αφήστε το μήνυμά σας 📞
    ## Оставьте ваше сообщение

    **Уровень:** B1 | **Тема:** Социальные контакты и общение

    В этом блокноте:
    - 📖 Объяснение грамматики
    - 💬 Полезные фразы
    - 🧪 Тесты: Существительные · Глаголы · Прилагательные
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Грамматика

    ### А. Слабые формы личных местоимений (Винительный падеж)

    Используются как прямые дополнения — ставятся **перед** глаголом.

    | Лицо | Единственное число | Множественное число |
    |------|--------------------|---------------------|
    | 1-е | **με** (меня) | **μας** (нас) |
    | 2-е | **σε** (тебя/вас) | **σας** (вас) |
    | 3-е муж. | **τον** (его) | **τους** (их) |
    | 3-е жен. | **την** (её) | **τις / τες** (их) |
    | 3-е ср. | **το** (его/это) | **τα** (их) |

    _Пример:_ **Σε** ακούω. _(Я тебя слышу.)_
    _Пример:_ Ποιος **τη** ζητάει; _(Кто её спрашивает?)_

    ---

    ### Б. Падежи существительных: Именительный, Винительный, Звательный

    | Падеж | Мужской | Женский | Средний |
    |-------|---------|---------|---------|
    | **Имен.** | ο Γιώργος | η Μαρίνα | το πάρτι |
    | **Вин.** | τον Γιώργο | τη(ν) Μαρίνα | το πάρτι |
    | **Зват.** | Γιώργο! | Μαρίνα! | πάρτι |

    **Существительные женского рода на -ος** склоняются как мужские:

    | Именительный | Родительный | Винительный |
    |-------------|-------------|-------------|
    | η **οδός** | της **οδού** | την **οδό** |
    | η **είσοδος** | της **εισόδου** | την **είσοδο** |
    | η **λεωφόρος** | της **λεωφόρου** | την **λεωφόρο** |

    ---

    ### В. Элизия (Απαλοιφή φωνήεντος)

    Когда слово, оканчивающееся на гласную, предшествует слову, начинающемуся с гласной,
    первая гласная опускается и заменяется апострофом:

    | Полная форма | Сокращённая форма | Значение |
    |-------------|------------------|----------|
    | μου **είπε** | μου **'πε** | он мне сказал |
    | σου **είπα** | σου **'πα** | я тебе сказал |
    | να **είναι** | να **'ναι** | быть |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Полезные фразы — Телефонное общение

    | Греческая фраза | Перевод | Ситуация |
    |-----------------|---------|----------|
    | Παρακαλώ. / Λέγετε; / Εμπρός. | Алло? / Слушаю? | Стандартный ответ на звонок |
    | Λάθος πήρατε. | Вы ошиблись номером. | Неверный номер |
    | Αφήστε το μήνυμά σας. | Оставьте ваше сообщение. | Автоответчик |
    | Ποιος τη/τον ζητάει; | Кто её/его спрашивает? | Уточняем звонящего |
    | Μισό λεπτό (να την φωνάξω). | Одну минуту (позову её). | Ставим на ожидание |
    | Καλώς ήλθατε! / Καλώς ορίσατε! | Добро пожаловать! | Приветствие гостя |
    | Να σας συστήσω τον φίλο μου... | Позвольте представить моего друга... | Знакомство |
    | Χαίρω πολύ. / Χάρηκα πολύ. | Очень приятно. | Ответ на знакомство |
    | Συγχαρητήρια! | Поздравляю! | Поздравление с дипломом / успехом |
    | Δεν πειράζει. / Δεν υπάρχει πρόβλημα. | Ничего страшного. | Успокоение |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Тест: Существительные (Ουσιαστικά)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    file_upload_noun = mo.ui.file(label="Загрузить файл существительных (nouns_ru.tsv) — необязательно", filetypes=[".tsv"])
    file_upload_noun
    return (file_upload_noun,)


@app.cell(hide_code=True)
def _(file_upload_noun, notebook_dir, os, pd):
    if file_upload_noun.value:
        from modern_greek_eee import greek_utils as _gu
        df_noun = _gu.load_data(file_upload_noun, [])
    else:
        _nouns_ru = os.path.join(notebook_dir, 'nouns_ru.tsv')
        _nouns_base = os.path.join(notebook_dir, 'nouns.tsv')
        try:
            df_noun = pd.read_csv(_nouns_ru, sep='\t')
        except FileNotFoundError:
            try:
                df_noun = pd.read_csv(_nouns_base, sep='\t')
            except FileNotFoundError:
                df_noun = None
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, mo):
    table_noun = mo.ui.table(df_noun, selection="multi") if df_noun is not None else None
    mo.vstack([
        mo.md("### Выберите существительные для тренировки"),
        table_noun if table_noun is not None else mo.md("_nouns.tsv не найден — загрузите файл._")
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
def _(mo, noun_form, noun_trans, noun_word, words4test_noun, words_noun):
    _remaining = len(words4test_noun())
    _total = len(words_noun)
    if words4test_noun() and noun_word:
        _view = mo.vstack([
            mo.md(f"#### Склонение ({_total - _remaining + 1}/{_total})"),
            mo.md(f"**Перевод:** {noun_trans}"),
            noun_form,
        ])
    else:
        _view = mo.md("Выберите слова для начала теста.")
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
    gu.process_noun_test(
        noun_word, noun_form, words_noun, words4test_noun,
        set_words4test_noun, set_noun_msg, set_noun_current, mode='simple'
    )
    return


@app.cell(hide_code=True)
def _(gu, noun_current):
    _acn = noun_current()
    art_noun_word, art_noun_trans, art_noun_form = gu.create_noun_test_ui([_acn] if _acn else [], mode='article')
    return art_noun_form, art_noun_trans, art_noun_word


@app.cell(hide_code=True)
def _(art_noun_form, art_noun_trans, art_noun_word, mo, words4test_noun, words_noun):
    _remaining = len(words4test_noun())
    _total = len(words_noun)
    if words4test_noun() and art_noun_word:
        _view = mo.vstack([
            mo.md(f"#### Артикли ({_total - _remaining + 1}/{_total})"),
            mo.md(f"**Перевод:** {art_noun_trans}"),
            art_noun_form,
        ])
    else:
        _view = mo.md("Выберите слова для начала теста.")
    _view
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
    gu.process_noun_test(
        art_noun_word, art_noun_form, words_noun, words4test_noun,
        set_words4test_noun, set_noun_msg, set_noun_current, mode='article'
    )
    return


@app.cell(hide_code=True)
def _(mo, noun_msg):
    mo.md(noun_msg()) if noun_msg() else None
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Тест: Глаголы (Ρήματα)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    file_upload_verb = mo.ui.file(label="Загрузить файл глаголов (verbs_ru.tsv) — необязательно", filetypes=[".tsv"])
    file_upload_verb
    return (file_upload_verb,)


@app.cell(hide_code=True)
def _(file_upload_verb, notebook_dir, os, pd):
    if file_upload_verb.value:
        from modern_greek_eee import greek_utils as _gu
        df_verb = _gu.load_data(file_upload_verb, [])
    else:
        _verbs_ru = os.path.join(notebook_dir, 'verbs_ru.tsv')
        _verbs_base = os.path.join(notebook_dir, 'verbs.tsv')
        try:
            df_verb = pd.read_csv(_verbs_ru, sep='\t')
        except FileNotFoundError:
            try:
                df_verb = pd.read_csv(_verbs_base, sep='\t')
            except FileNotFoundError:
                df_verb = None
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, mo):
    table_verb = mo.ui.table(df_verb, selection="multi") if df_verb is not None else None
    mo.vstack([
        mo.md("### Выберите глаголы для тренировки"),
        table_verb if table_verb is not None else mo.md("_verbs.tsv не найден — загрузите файл._")
    ])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu, table_verb):
    words_verb = gu.get_words(table_verb)
    return (words_verb,)


@app.cell(hide_code=True)
def _(gu, mo):
    _b1_tenses = ['present', 'imperfect', 'aorist', 'future', 'future_continuous']
    _plain_ru = {
        'present': 'Настоящее',
        'imperfect': 'Прошедшее незавершённое',
        'aorist': 'Прошедшее завершённое',
        'future': 'Будущее простое',
        'future_continuous': 'Будущее длительное',
    }
    _tense_options = {
        f"{gu.TENSE_LABELS[k]['greek']} ({_plain_ru[k]})": k
        for k in _b1_tenses if k in gu.TENSE_LABELS
    }
    _first_key = next(iter(_tense_options))
    tense_selector = mo.ui.dropdown(
        options=_tense_options,
        value=_first_key,
        label="Выберите время:"
    )
    tense_selector
    return (tense_selector,)


@app.cell(hide_code=True)
def _(mo, random, words_verb):
    _shuffled_verb = random.sample(words_verb, len(words_verb)) if words_verb else []
    words4test_verb, set_words4test_verb = mo.state(_shuffled_verb)
    verb_msg, set_verb_msg = mo.state("")
    return set_verb_msg, set_words4test_verb, verb_msg, words4test_verb


@app.cell(hide_code=True)
def _(gu, mo, tense_selector, words4test_verb, words_verb):
    cv_verb = words4test_verb()[0] if words4test_verb() else None
    _tense_key = tense_selector.value
    if cv_verb and _tense_key:
        _TENSE_UI_LABELS = {k: f"{gu.TENSE_LABELS[k]['english']} ({gu.TENSE_LABELS[k]['greek']})" for k in gu.TENSE_LABELS}
        _ui_label = _TENSE_UI_LABELS.get(_tense_key, _tense_key)
        verb_form, _verb_md = gu.create_verb_test_ui(_ui_label, words_verb, words4test_verb(), cv_verb)
        _remaining = len(words4test_verb())
        _total = len(words_verb)
        _view = mo.vstack([
            mo.md(f"#### Тест глагола ({_total - _remaining + 1}/{_total})"),
            _verb_md,
        ])
    else:
        verb_form = None
        _view = mo.md("Выберите слова для начала теста.")
    _view
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
    if cv_verb and tense_selector.value and verb_form is not None:
        _ok, _errors = gu.check_verb_test(cv_verb['Word'], verb_form, tense_selector.value)
        if _ok:
            _new_words4test = [w for w in words4test_verb() if w["Word"] != cv_verb["Word"]]
            set_words4test_verb(_new_words4test)
            _remaining = len(_new_words4test)
            _total = len(words_verb)
            _msg = f'Тест для <b>"{cv_verb["Word"]} — {cv_verb["Translation"]}"</b> пройден.\n\nОсталось {_remaining} из {_total}.'
            set_verb_msg(_msg)
        _view = mo.md(_errors) if (not _ok and _errors) else mo.md("")
    else:
        _view = mo.md("")
    _view
    return


@app.cell(hide_code=True)
def _(mo, verb_msg):
    mo.md(verb_msg()) if verb_msg() else None
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Тест: Прилагательные (Επίθετα)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    file_upload_adj = mo.ui.file(label="Загрузить файл прилагательных (adjectives_ru.tsv) — необязательно", filetypes=[".tsv"])
    file_upload_adj
    return (file_upload_adj,)


@app.cell(hide_code=True)
def _(file_upload_adj, notebook_dir, os, pd):
    if file_upload_adj.value:
        from modern_greek_eee import greek_utils as _gu
        df_adj = _gu.load_data(file_upload_adj, [])
    else:
        _adj_ru = os.path.join(notebook_dir, 'adjectives_ru.tsv')
        _adj_base = os.path.join(notebook_dir, 'adjectives.tsv')
        try:
            df_adj = pd.read_csv(_adj_ru, sep='\t')
        except FileNotFoundError:
            try:
                df_adj = pd.read_csv(_adj_base, sep='\t')
            except FileNotFoundError:
                df_adj = None
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, mo):
    table_adj = mo.ui.table(df_adj, selection="multi") if df_adj is not None else None
    mo.vstack([
        mo.md("### Выберите прилагательные для тренировки"),
        table_adj if table_adj is not None else mo.md("_adjectives.tsv не найден — загрузите файл._")
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
            "Полный: все роды, числа и падежи (18 полей)": "complex"
        },
        value="Простой: 3 рода × 2 числа (6 полей)",
        label="Режим теста:"
    )
    mode_selector
    return (mode_selector,)


@app.cell(hide_code=True)
def _(adj_words, mo, random):
    _shuffled_adj = random.sample(adj_words, len(adj_words)) if adj_words else []
    adj_words4test, set_adj_words4test = mo.state(_shuffled_adj)
    adj_cv, set_adj_cv = mo.state(_shuffled_adj[0] if _shuffled_adj else None)
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
def _(adj_cv, adj_words4test, gu, mode_selector):
    _mode = mode_selector.value
    adj_form, _ = gu.create_adjective_test_ui(
        [] if not adj_cv() else [adj_cv()],
        adj_words4test(),
        adj_cv(),
        mode=_mode
    )
    return (adj_form,)


@app.cell(hide_code=True)
def _(adj_cv, adj_form, adj_words, adj_words4test, mo):
    _remaining = len(adj_words4test())
    _total = len(adj_words)
    _current = adj_cv()
    if adj_words4test() and _current:
        _view = mo.vstack([
            mo.md(f"#### **{_current['Translation']}** ({_total - _remaining + 1}/{_total})"),
            adj_form,
        ])
    else:
        _view = mo.md("Выберите слова для начала теста.")
    _view
    return


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
    mo.md(adj_last_passed_mesg()) if adj_last_passed_mesg() else None
    return


@app.cell(hide_code=True)
def _():
    import os
    import random
    import pandas as pd
    import marimo as mo

    try:
        from modern_greek_eee import greek_utils as gu
    except ImportError:
        import greek_utils as gu

    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    return gu, mo, notebook_dir, os, pd, random


if __name__ == "__main__":
    app.run()
