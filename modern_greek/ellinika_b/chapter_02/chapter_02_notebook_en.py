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
    # Σπίτι μου σπιτάκι μου 🏠
    ## Home Sweet Home

    **Textbook:** Ελληνικά Β' | **Chapter:** 2 (Ενότητα 2) | **Level:** B1 | **Language:** English

    **Theme:** Housing and residence (Κατοικία, διαμονή)

    **Tests in this notebook:** Nouns · Verbs · Adjectives
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Useful Phrases (Πώς το λένε;)

    | Greek | English | Context |
    |-------|---------|---------|
    | Το σπίτι βγάζει προβλήματα. | The house is having issues. | Reporting maintenance |
    | Εμένα μου αρέσει. Εσένα; | I like it. What about you? | Discussing preferences |
    | Ποιανού είναι το σπίτι; | Whose house is it? | Asking about ownership |
    | Το ενοίκιο είναι λογικό. | The rent is reasonable. | Discussing price |
    | Πού τη βάζω την κούτα; | Where do I put the box? | During a move |
    | Η τιμή θα είναι πολύ πιο χαμηλή.| Τhe price will be much lower. | Commenting on low costs |
    | Θέλω να συμφωνήσουμε πριν την επισκευή. | I want us to agree before the repair. | Negotiating with landlord |
    | Έχω τις μαύρες μου. | I am in a bad mood. | Expressing dissatisfaction |
    """)
    return


@app.cell(hide_code=True)
def _():
    import os
    import random
    import pandas as pd
    import marimo as mo

    from modern_greek_eee import greek_utils as gu

    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    return gu, mo, random, notebook_dir, os, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Test: Nouns (Ουσιαστικά)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    file_upload_noun = mo.ui.file(filetypes=[".tsv"], label="Upload nouns.tsv (optional — uses bundled file by default)")
    file_upload_noun
    return (file_upload_noun,)


@app.cell(hide_code=True)
def _(file_upload_noun, gu, notebook_dir, os, pd):
    if file_upload_noun.value:
        df_noun = gu.load_data(file_upload_noun, [])
    else:
        try:
            df_noun = pd.read_csv(os.path.join(notebook_dir, 'nouns.tsv'), sep='\t')
        except FileNotFoundError:
            df_noun = None
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, mo):
    table_noun = mo.ui.table(df_noun, selection="multi") if df_noun is not None else None
    mo.vstack([
        mo.md("### Select nouns to test"),
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
            mo.md(f"#### Simple declension ({_total - _remaining + 1}/{_total})"),
            mo.md(f"Translation: **{noun_trans}**"),
            noun_form,
        ])
    else:
        _view = mo.md("_Select nouns above to start the test._")
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
            mo.md(f"#### Article declension ({_total - _remaining + 1}/{_total})"),
            mo.md(f"Translation: **{art_noun_trans}**"),
            art_noun_form,
        ])
    else:
        _view = mo.md("_Select nouns above to start the test._")
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
    ## Test: Verbs (Ρήματα)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    file_upload_verb = mo.ui.file(filetypes=[".tsv"], label="Upload verbs.tsv (optional — uses bundled file by default)")
    file_upload_verb
    return (file_upload_verb,)


@app.cell(hide_code=True)
def _(file_upload_verb, gu, notebook_dir, os, pd):
    if file_upload_verb.value:
        df_verb = gu.load_data(file_upload_verb, [])
    else:
        try:
            df_verb = pd.read_csv(os.path.join(notebook_dir, 'verbs.tsv'), sep='\t')
        except FileNotFoundError:
            df_verb = None
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, mo):
    table_verb = mo.ui.table(df_verb, selection="multi") if df_verb is not None else None
    mo.vstack([
        mo.md("### Select verbs to test"),
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
    _plain_en = {
        'present': 'Present',
        'imperfect': 'Imperfect',
        'aorist': 'Simple Past',
        'future': 'Simple Future',
        'future_continuous': 'Continuous Future',
    }
    _tense_opts = {
        f"{gu.TENSE_LABELS[k]['greek']} ({_plain_en[k]})": k
        for k in _chapter_tenses if k in gu.TENSE_LABELS
    }
    tense_selector = mo.ui.dropdown(
        options=_tense_opts,
        value=next(iter(_tense_opts)),
        label="Tense:",
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
    _ui_label = _TENSE_UI_LABELS.get(_tense_key, _tense_key) if _tense_key else "Select a tense"
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
            _msg = f'<span style="color: green;">Test for <b>"{cv_verb["Word"]} — {cv_verb["Translation"]}"</b> passed.\n\n{_remaining} words remaining out of {_total}.</span>'
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
    ## Test: Adjectives (Επίθετα)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    file_upload_adj = mo.ui.file(filetypes=[".tsv"], label="Upload adjectives.tsv (optional — uses bundled file by default)")
    file_upload_adj
    return (file_upload_adj,)


@app.cell(hide_code=True)
def _(file_upload_adj, gu, notebook_dir, os, pd):
    if file_upload_adj.value:
        df_adj = gu.load_data(file_upload_adj, [])
    else:
        try:
            df_adj = pd.read_csv(os.path.join(notebook_dir, 'adjectives.tsv'), sep='\t')
        except FileNotFoundError:
            df_adj = None
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, mo):
    table_adj = mo.ui.table(df_adj, selection="multi") if df_adj is not None else None
    mo.vstack([
        mo.md("### Select adjectives to test"),
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
            "Simple: 3 genders × 2 numbers (6 fields)": "simple",
            "Full: all genders, numbers, and cases (18 fields)": "complex",
        },
        value="Simple: 3 genders × 2 numbers (6 fields)",
        label="Test mode:",
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
