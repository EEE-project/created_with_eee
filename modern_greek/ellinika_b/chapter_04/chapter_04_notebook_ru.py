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

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # «Είναι πανάκριβα!»
    ## Глава 4 — Покупки и цены

    **Учебник:** Ελληνικά Β' &nbsp;|&nbsp; **Уровень:** B1 &nbsp;|&nbsp; **Тесты:** Существительные · Глаголы · Прилагательные

    ---

    ### Грамматика: Прилагательные на -ύς, -ιά, -ύ

    Эти прилагательные описывают размеры и свойства. Пример: **ο φαρδύς** (широкий)

    | Падеж | Мужской | Женский | Средний |
    |-------|---------|---------|---------|
    | Им. ед. | ο φαρδύς | η φαρδιά | το φαρδύ |
    | Род. ед. | του φαρδιού | της φαρδιάς | του φαρδιού |
    | Вин. ед. | τον φαρδύ | τη φαρδιά | το φαρδύ |
    | Им. мн. | οι φαρδιοί | οι φαρδιές | τα φαρδιά |
    | Род. мн. | των φαρδιών | των φαρδιών | των φαρδιών |
    | Вин. мн. | τους φαρδιούς | τις φαρδιές | τα φαρδιά |

    Другие прилагательные этого типа: **βαθύς** (глубокий), **μακρύς** (длинный)

    ---

    ### Грамматика: Прилагательные на -ής, -ιά, -ί (цвета)

    Эти прилагательные в основном обозначают цвета. Пример: **ο καφετής** (коричневый)

    | Падеж | Мужской | Женский | Средний |
    |-------|---------|---------|---------|
    | Им. ед. | ο καφετής | η καφετιά | το καφετί |
    | Им. мн. | οι καφετιοί | οι καφετιές | τα καφετιά |

    Цвета: **πορτοκαλής** (оранжевый), **βυσσινής** (бордовый), **θαλασσής** (морской), **χρυσαφής** (золотистый)

    ---

    ### Фонетика: Синизис (Συνίζηση)

    Два соседних гласных сливаются в один слог: /i/ + /a, e, o, u/ → один слог.

    Примеры: **παιδιά** (дети), **ποια** (которая), **γεια** (привет), **εισιτήρια** (билеты)

    ---

    ### Полезные фразы (Πώς το λένε;)

    | Греческий | Русский |
    |-----------|---------|
    | Πώς σας φαίνεται; | Как вам кажется? |
    | Τι νούμερο φοράτε; | Какой размер вы носите? |
    | Μπορώ να το αλλάξω; | Могу я это обменять? |
    | Φωτιά και λαύρα! | Очень дорого! |
    | Με μετρητά ή με κάρτα; | Наличными или картой? |
    | Πού πληρώνω; | Где я плачу? |
    """)
    return


@app.cell(hide_code=True)
def _(df_noun, mo):
    table_noun = mo.ui.table(df_noun, selection="multi") if df_noun is not None else None
    mo.vstack([
        mo.md("## Тест 1: Существительные\n\n### Выберите существительные для практики"),
        table_noun,
    ])
    return (table_noun,)


@app.cell(hide_code=True)
def _(mo):
    file_upload_noun = mo.ui.file(label="Загрузить TSV существительных")
    file_upload_noun
    return (file_upload_noun,)


@app.cell(hide_code=True)
def _(gu, mo, noun_form, noun_trans, noun_word, words4test_noun, words_noun):
    _feedback = ""
    if words4test_noun() and noun_word:
        with mo.capture_stdout() as _buf:
            gu.check_noun_test(noun_word, noun_form, mode='simple')
        _feedback = _buf.getvalue()
        _view_simple = mo.vstack([
            mo.md(f"**Простой тест: Существительные** ({len(words4test_noun())}/{len(words_noun)})"),
            mo.md(f"Перевод: **{noun_trans}**"),
            noun_form,
            mo.md(_feedback),
        ])
    else:
        _view_simple = mo.md("**Список слов пуст.** Выберите слова в таблице выше.")
    _view_simple
    return


@app.cell(hide_code=True)
def _(
    art_noun_form,
    art_noun_trans,
    art_noun_word,
    gu,
    mo,
    words4test_noun,
    words_noun,
):
    _feedback_art = ""
    if words4test_noun() and art_noun_word:
        with mo.capture_stdout() as _buf_art:
            gu.check_noun_test(art_noun_word, art_noun_form, mode='article')
        _feedback_art = _buf_art.getvalue()
        _view_art = mo.vstack([
            mo.md(f"**Тест с артиклем: Существительные** ({len(words4test_noun())}/{len(words_noun)})"),
            mo.md(f"Перевод: **{art_noun_trans}**"),
            art_noun_form,
            mo.md(_feedback_art),
        ])
    else:
        _view_art = mo.md("**Список слов пуст.** Выберите слова в таблице выше.")
    _view_art
    return


@app.cell(hide_code=True)
def _(mo, noun_msg):
    mo.md(noun_msg())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Тест 2: Глаголы
    """)
    return


@app.cell(hide_code=True)
def _(df_verb, mo):
    table_verb = mo.ui.table(df_verb, selection="multi") if df_verb is not None else None
    table_verb
    return (table_verb,)


@app.cell(hide_code=True)
def _(mo):
    file_upload_verb = mo.ui.file(label="Загрузить TSV глаголов")
    file_upload_verb
    return (file_upload_verb,)


@app.cell(hide_code=True)
def _(gu, mo):
    _b1_tenses = ['present', 'imperfect', 'aorist', 'future', 'future_continuous']
    _tense_options = {gu.TENSE_LABELS[k]['dropdown']: k for k in _b1_tenses if k in gu.TENSE_LABELS}
    tense_selector = mo.ui.dropdown(
        options=_tense_options,
        value=gu.TENSE_LABELS['present']['dropdown'],
        label="Выберите время:",
    )
    mo.md(f"""
    ### Практика: Спряжение глаголов

    {tense_selector}
    """)
    return (tense_selector,)


@app.cell(hide_code=True)
def _(cv_verb, gu, mo, tense_selector, verb_form, words4test_verb, words_verb):
    _tense_key = tense_selector.value
    _TENSE_LABELS = {k: gu.TENSE_LABELS[k]['greek'] for k in gu.TENSE_LABELS}
    if not words4test_verb():
        _view_verb = mo.md("**Список слов пуст.** Выберите слова в таблице выше.")
    elif not _tense_key:
        _view_verb = mo.md("Выберите время выше.")
    else:
        _feedback = ""
        if cv_verb:
            _, _msg = gu.check_verb_test(cv_verb['Word'], verb_form, _tense_key)
            _feedback = mo.md(_msg.replace("\n\n", "  \n")) if _msg else ""
        _label = _TENSE_LABELS.get(_tense_key, _tense_key)
        _view_verb = mo.vstack([
            mo.md(f"**Тест по глаголам — {_label}** ({len(words4test_verb())}/{len(words_verb)})"),
            mo.md(f"Перевод: **{cv_verb['Translation']}**") if cv_verb else mo.md(""),
            verb_form,
            _feedback,
        ])
    _view_verb
    return


@app.cell(hide_code=True)
def _(file_upload_noun, gu, notebook_dir, os, pd):
    if file_upload_noun.value:
        df_noun = gu.load_data(file_upload_noun, [])
    else:
        _path = os.path.join(notebook_dir, 'nouns_ru.tsv')
        try:
            df_noun = pd.read_csv(_path if os.path.exists(_path) else os.path.join(notebook_dir, 'nouns.tsv'), sep='\t')
        except FileNotFoundError:
            df_noun = None
    return (df_noun,)


@app.cell(hide_code=True)
def _(gu, mo, random, table_noun):
    words_noun = gu.get_words(table_noun)
    _shuffled = random.sample(words_noun, len(words_noun)) if words_noun else []
    words4test_noun, set_words4test_noun = mo.state(_shuffled)
    noun_msg, set_noun_msg = mo.state("")
    noun_current, set_noun_current = mo.state(_shuffled[0] if _shuffled else None)
    return (
        noun_current,
        noun_msg,
        set_noun_current,
        set_noun_msg,
        set_words4test_noun,
        words4test_noun,
        words_noun,
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
    if words4test_noun() and noun_word:
        gu.process_noun_test(
            noun_word, noun_form, words_noun, words4test_noun,
            set_words4test_noun, set_noun_msg, set_noun_current, mode='simple'
        )
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
    if words4test_noun() and art_noun_word:
        gu.process_noun_test(
            art_noun_word, art_noun_form, words_noun, words4test_noun,
            set_words4test_noun, set_noun_msg, set_noun_current, mode='article'
        )
    return


@app.cell(hide_code=True)
def _(file_upload_verb, gu, notebook_dir, os, pd):
    if file_upload_verb.value:
        df_verb = gu.load_data(file_upload_verb, [])
    else:
        _path = os.path.join(notebook_dir, 'verbs_ru.tsv')
        try:
            df_verb = pd.read_csv(_path if os.path.exists(_path) else os.path.join(notebook_dir, 'verbs.tsv'), sep='\t')
        except FileNotFoundError:
            df_verb = None
    return (df_verb,)


@app.cell(hide_code=True)
def _(gu, mo, random, table_verb):
    words_verb = gu.get_words(table_verb)
    _shuffled_verb = random.sample(words_verb, len(words_verb)) if words_verb else []
    words4test_verb, set_words4test_verb = mo.state(_shuffled_verb)
    verb_msg, set_verb_msg = mo.state("")
    return (
        set_verb_msg,
        set_words4test_verb,
        verb_msg,
        words4test_verb,
        words_verb,
    )


@app.cell(hide_code=True)
def _(gu, tense_selector, words4test_verb, words_verb):
    cv_verb = words4test_verb()[0] if words4test_verb() else None
    _tense_key = tense_selector.value
    _ui_label = f"{gu.TENSE_LABELS[_tense_key]['english']} ({gu.TENSE_LABELS[_tense_key]['greek']})" if _tense_key else "Выберите время"
    verb_form, _verb_md = gu.create_verb_test_ui(_ui_label, words_verb, words4test_verb(), cv_verb)
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
    verb_msg,
    words4test_verb,
    words_verb,
):
    _tense_key = tense_selector.value
    if cv_verb and _tense_key:
        _ok, _ = gu.check_verb_test(cv_verb['Word'], verb_form, _tense_key)
        if _ok:
            _new = [w for w in words4test_verb() if w["Word"] != cv_verb["Word"]]
            set_words4test_verb(_new)
            _rem, _tot = len(_new), len(words_verb)
            set_verb_msg(f'<span style="color:green;">Тест для <b>"{cv_verb["Word"]} — {cv_verb["Translation"]}"</b> пройден.\n\n{_rem} слов(а) осталось из {_tot}.</span>')
    _res = mo.md(verb_msg())
    _res
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Тест 3: Прилагательные
    """)
    return


@app.cell(hide_code=True)
def _(df_adj, mo):
    table_adj = mo.ui.table(df_adj, selection="multi") if df_adj is not None else None
    table_adj
    return (table_adj,)


@app.cell(hide_code=True)
def _(mo):
    file_upload_adj = mo.ui.file(label="Загрузить TSV прилагательных")
    file_upload_adj
    return (file_upload_adj,)


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
    mo.md(f"""
    {mode_selector}
    """)
    return (mode_selector,)


@app.cell(hide_code=True)
def _(adj_cv, adj_form, adj_words, adj_words4test, gu, mo):
    _adj = adj_cv()
    if adj_words4test() and _adj:
        _, _msg = gu.check_adjective_test(_adj['Word'], adj_form)
        _view_adj = mo.vstack([
            mo.md(f"**Тест: Склонение прилагательного** ({len(adj_words4test())}/{len(adj_words)})"),
            mo.md(f"Перевод: **{_adj['Translation']}**"),
            adj_form,
            mo.md(_msg.replace("\n\n", "  \n")) if _msg else mo.md(""),
        ])
    else:
        _view_adj = mo.md("**Список слов пуст.** Выберите слова в таблице выше.")
    _view_adj
    return


@app.cell(hide_code=True)
def _(adj_last_passed_mesg, mo):
    _res_adj = mo.md(adj_last_passed_mesg())
    _res_adj
    return


@app.cell(hide_code=True)
def _(file_upload_adj, gu, notebook_dir, os, pd):
    if file_upload_adj.value:
        df_adj = gu.load_data(file_upload_adj, [])
    else:
        _path = os.path.join(notebook_dir, 'adjectives_ru.tsv')
        try:
            df_adj = pd.read_csv(_path if os.path.exists(_path) else os.path.join(notebook_dir, 'adjectives.tsv'), sep='\t')
        except FileNotFoundError:
            df_adj = None
    return (df_adj,)


@app.cell(hide_code=True)
def _(gu, mo, random, table_adj):
    adj_words = gu.get_words(table_adj)
    _shuffled_adj = random.sample(adj_words, len(adj_words)) if adj_words else []
    adj_words4test, set_adj_words4test = mo.state(_shuffled_adj)
    adj_last_passed_mesg, set_adj_last_passed_mesg = mo.state("")
    adj_cv, set_adj_cv = mo.state(_shuffled_adj[0] if _shuffled_adj else None)
    return (
        adj_cv,
        adj_last_passed_mesg,
        adj_words,
        adj_words4test,
        set_adj_cv,
        set_adj_last_passed_mesg,
        set_adj_words4test,
    )


@app.cell(hide_code=True)
def _(adj_cv, gu, mode_selector):
    _acv = adj_cv()
    _mode = mode_selector.value
    adj_form, _ = gu.create_adjective_test_ui([] if not _acv else [_acv], [], _acv, mode=_mode)
    return (adj_form,)


@app.cell(hide_code=True)
def _(
    adj_cv,
    adj_form,
    adj_words,
    adj_words4test,
    gu,
    mode_selector,
    set_adj_cv,
    set_adj_last_passed_mesg,
    set_adj_words4test,
):
    _adj = adj_cv()
    _mode = mode_selector.value
    if adj_words4test() and _adj:
        adj_ok, _ = gu.check_adjective_test(_adj['Word'], adj_form, mode=_mode)
        gu.process_adjective_completion(
            _adj, adj_ok, adj_words, adj_words4test(),
            set_adj_words4test, set_adj_last_passed_mesg, set_adj_cv,
        )
    return


@app.cell(hide_code=True)
def _():
    import os
    import random
    import pandas as pd
    import marimo as mo
    from modern_greek_eee import greek_utils as gu
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    return gu, mo, notebook_dir, os, pd, random


if __name__ == "__main__":
    app.run()
