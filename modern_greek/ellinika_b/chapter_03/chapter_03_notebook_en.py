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
    ## Chapter 3 — Είχε τέτοια κίνηση!

    **Textbook:** Ελληνικά Β' &nbsp;|&nbsp; **Level:** B1 &nbsp;|&nbsp; **Tests:** Nouns · Verbs · Adjectives

    ---

    **Theme:** City life, public transport, giving and asking for directions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Grammar: Indefinite Pronouns (Αόριστες Αντωνυμίες)

    Indefinite pronouns refer to **non-specific** people or things.

    | Pronoun | Meaning | Masc. (Nom.) | Fem. (Nom.) | Neut. (Nom.) |
    |---------|---------|-------------|------------|--------------|
    | κάποιος | someone | κάποιος | κάποια | κάποιο |
    | κανένας | no one / anyone | κανένας | καμία | κανένα |
    | ο καθένας | each one | ο καθένας | η καθεμία | το καθένα |

    **Accusative forms:**

    | | Masc. | Fem. | Neut. |
    |-|-------|------|-------|
    | κάποιος | κάποιον | κάποια | κάποιο |
    | κανένας | κανέναν | καμία | κανένα |
    | ο καθένας | τον καθέναν | την καθεμία | το καθένα |

    **Examples:**
    - **Κάποιος** σε ζητάει στο τηλέφωνο. — _Someone is asking for you on the phone._
    - **Κανένας** δεν ήρθε. — _No one came._
    - **Ο καθένας** έχει τη γνώμη του. — _Each one has their own opinion._
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Grammar: Demonstrative Pronouns (Δεικτικές Αντωνυμίες)

    Demonstrative pronouns point out **specific qualities or quantities**.

    | Pronoun | Meaning | Masc. (Nom.) | Fem. (Nom.) | Neut. (Nom.) |
    |---------|---------|-------------|------------|--------------|
    | ίδιος | the same | ο ίδιος | η ίδια | το ίδιο |
    | τέτοιος | such / like this | τέτοιος | τέτοια | τέτοιο |
    | τόσος | so much / so many | τόσος | τόση | τόσο |

    **Accusative forms:**

    | | Masc. | Fem. | Neut. |
    |-|-------|------|-------|
    | ίδιος | τον ίδιο | την ίδια | το ίδιο |
    | τέτοιος | τέτοιον | τέτοια | τέτοιο |
    | τόσος | τόσον | τόση | τόσο |

    **Examples:**
    - Έχουμε **το ίδιο** πρόβλημα. — _We have the same problem._
    - **Τέτοια** κίνηση δεν έχω ξαναδεί! — _I've never seen such traffic!_
    - **Τόση** κίνηση! — _So much traffic!_
    - Μην βάζεις **τόση** ζάχαρη! — _Don't put in so much sugar!_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Useful Phrases (Πώς το λένε;)

    | Greek | English | Context |
    |-------|---------|---------|
    | Πώς θα πάω στο ...; | How will I get to ...? | Asking for directions |
    | Πού είναι η πλησιέστερη στάση; | Where is the nearest stop? | Public transport |
    | Πού κατεβαίνω για το ...; | Where do I get off for ...? | Bus / Metro |
    | Στρίψτε δεξιά / αριστερά. | Turn right / left. | Giving directions |
    | Προχωρήστε ίσια / ευθεία. | Go straight ahead. | Giving directions |
    | Στο τρίτο στενό. | At the third alley. | Identifying a turn-off |
    | Είχε τόση κίνηση! | There was so much traffic! | Explaining a delay |
    | Πάνω στην ώρα! | Right on time! | Arriving perfectly on time |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## 🧪 Test 1: Nouns
    """)
    return


@app.cell(hide_code=True)
def _(gu, notebook_dir):
    df_noun = gu.load_vocab_table("nouns.tsv", nb_dir=notebook_dir)
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, gu, mo):
    table_noun = gu.vocab_table(df_noun)
    mo.vstack([mo.md("### Select nouns to test"), table_noun if table_noun is not None else mo.md("_nouns.tsv not found — upload a file to begin._")])
    return (table_noun,)


@app.cell(hide_code=True)
def _(gu, table_noun):
    words_noun = gu.get_words(table_noun)
    return (words_noun,)


@app.cell(hide_code=True)
def _(mo, random, words_noun):
    _shuffled_noun = random.sample(words_noun, len(words_noun)) if words_noun else []
    words4test_noun, set_words4test_noun = mo.state(_shuffled_noun)
    noun_current, set_noun_current = mo.state(_shuffled_noun[0] if _shuffled_noun else None)
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
def _(
    mo,
    noun_form,
    noun_msg,
    noun_trans,
    noun_word,
    words4test_noun,
    words_noun,
):
    if noun_word:
        _remaining = len(words4test_noun())
        _total = len(words_noun)
        _items = [
            mo.md(f"#### Noun test — simple ({_remaining}/{_total})"),
            mo.md(f"Translation: **{noun_trans}**"),
        ]
        if noun_msg():
            _items.append(mo.md(noun_msg()))
        _items.append(noun_form)
        _view = mo.vstack(_items)
    else:
        _view = mo.md("_Select nouns above to start the test._")
    _view
    return


@app.cell(hide_code=True)
def _(gu, mo, noun_form, noun_word):
    if noun_word and noun_form is not None and noun_form.value:
        with mo.capture_stdout() as _buf:
            gu.check_noun_test(noun_word, noun_form, mode='simple')
        _noun_fb = mo.md(_buf.getvalue()) if _buf.getvalue() else mo.md("")
    else:
        _noun_fb = mo.md("")
    _noun_fb
    return


@app.cell(hide_code=True)
def _(
    art_noun_form,
    art_noun_trans,
    art_noun_word,
    mo,
    noun_msg,
    words4test_noun,
    words_noun,
):
    if art_noun_word:
        _remaining = len(words4test_noun())
        _total = len(words_noun)
        _items = [
            mo.md(f"#### Noun test — article ({_remaining}/{_total})"),
            mo.md(f"Translation: **{art_noun_trans}**"),
        ]
        if noun_msg():
            _items.append(mo.md(noun_msg()))
        _items.append(art_noun_form)
        _view = mo.vstack(_items)
    else:
        _view = mo.md("")
    _view
    return


@app.cell(hide_code=True)
def _(art_noun_form, art_noun_word, gu, mo):
    if art_noun_word and art_noun_form is not None and art_noun_form.value:
        with mo.capture_stdout() as _buf2:
            gu.check_noun_test(art_noun_word, art_noun_form, mode='article')
        _art_fb = mo.md(_buf2.getvalue()) if _buf2.getvalue() else mo.md("")
    else:
        _art_fb = mo.md("")
    _art_fb
    return


@app.cell(hide_code=True)
def _(
    gu,
    mo,
    noun_form,
    noun_word,
    set_noun_current,
    set_noun_msg,
    set_words4test_noun,
    words4test_noun,
    words_noun,
):
    if noun_word and noun_form is not None and noun_form.value:
        with mo.capture_stdout() as _buf3:
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
    mo,
    set_noun_current,
    set_noun_msg,
    set_words4test_noun,
    words4test_noun,
    words_noun,
):
    if art_noun_word and art_noun_form is not None and art_noun_form.value:
        with mo.capture_stdout() as _buf4:
            gu.process_noun_test(
                art_noun_word, art_noun_form, words_noun, words4test_noun,
                set_words4test_noun, set_noun_msg, set_noun_current, mode='article'
            )
    return


@app.cell(hide_code=True)
def _(mo, noun_msg):
    _msg = noun_msg()
    mo.md(_msg) if _msg else None
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## 🧪 Test 2: Verbs
    """)
    return


@app.cell(hide_code=True)
def _(gu, notebook_dir):
    df_verb = gu.load_vocab_table("verbs.tsv", nb_dir=notebook_dir)
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, gu, mo):
    table_verb = gu.vocab_table(df_verb)
    mo.vstack([mo.md("### Select verbs to test"), table_verb if table_verb is not None else mo.md("_verbs.tsv not found — upload a file to begin._")])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu, table_verb):
    words_verb = gu.get_words(table_verb)
    return (words_verb,)


@app.cell(hide_code=True)
def _(gu, mo):
    _tense_options = {
        f"{gu.TENSE_LABELS[k]['greek']} ({_en})": k
        for k, _en in [
            ('present', 'Present'),
            ('imperfect', 'Imperfect / Past'),
            ('aorist', 'Simple Past'),
            ('future', 'Simple Future'),
            ('future_continuous', 'Continuous Future'),
        ]
        if k in gu.TENSE_LABELS
    }
    tense_selector = mo.ui.dropdown(
        options=_tense_options,
        value=list(_tense_options.keys())[0],
        label="Select tense:",
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
def _(gu, tense_selector, words4test_verb, words_verb):
    cv_verb = words4test_verb()[0] if words4test_verb() else None
    _tense_key = tense_selector.value
    if cv_verb and _tense_key:
        _ui_label = f"{gu.TENSE_LABELS[_tense_key]['english']} ({gu.TENSE_LABELS[_tense_key]['greek']})"
        verb_form, _ = gu.create_verb_test_ui(_ui_label, words_verb, words4test_verb(), cv_verb)
    else:
        verb_form = None
    return cv_verb, verb_form


@app.cell(hide_code=True)
def _(cv_verb, gu, mo, tense_selector, verb_form, words4test_verb, words_verb):
    _tense_key = tense_selector.value
    if verb_form is not None and cv_verb and _tense_key:
        _, _msg = gu.check_verb_test(cv_verb['Word'], verb_form, _tense_key)
        _remaining = len(words4test_verb())
        _total = len(words_verb)
        _view2 = mo.vstack([
            mo.md(f"#### Verb test ({_remaining}/{_total})"),
            mo.md(f"Translation: **{cv_verb['Translation']}**"),
            verb_form,
            mo.md(_msg) if _msg else mo.md(""),
        ])
    else:
        _view2 = mo.md("_Select verbs above to start the test._")
    _view2
    return


@app.cell(hide_code=True)
def _(
    cv_verb,
    gu,
    set_verb_msg,
    set_words4test_verb,
    tense_selector,
    verb_form,
    words4test_verb,
    words_verb,
):
    if cv_verb and tense_selector.value and verb_form is not None and verb_form.value:
        _ok, _ = gu.check_verb_test(cv_verb['Word'], verb_form, tense_selector.value)
        if _ok:
            _new = [w for w in words4test_verb() if w["Word"] != cv_verb["Word"]]
            set_words4test_verb(_new)
            _rem, _tot = len(_new), len(words_verb)
            set_verb_msg(f'<span style="color:green;">Test for <b>"{cv_verb["Word"]} — {cv_verb["Translation"]}"</b> passed. {_rem}/{_tot} remaining.</span>')
    return


@app.cell(hide_code=True)
def _(mo, verb_msg):
    _vm = mo.md(verb_msg()) if verb_msg() else mo.md("")
    _vm
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## 🧪 Test 3: Adjectives
    """)
    return


@app.cell(hide_code=True)
def _(gu, notebook_dir):
    df_adj = gu.load_vocab_table("adjectives.tsv", nb_dir=notebook_dir)
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, gu, mo):
    table_adj = gu.vocab_table(df_adj)
    mo.vstack([mo.md("### Select adjectives to test"), table_adj if table_adj is not None else mo.md("_adjectives.tsv not found — upload a file to begin._")])
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
            "Full: All genders, numbers, and cases (18 fields)": "complex",
        },
        value="Simple: 3 genders × 2 numbers (6 fields)",
        label="Test Mode:",
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
def _(adj_cv, adj_words, adj_words4test, gu, mode_selector):
    _mode = mode_selector.value
    adj_form, _ = gu.create_adjective_test_ui(adj_words, adj_words4test(), adj_cv(), mode=_mode)
    return (adj_form,)


@app.cell(hide_code=True)
def _(adj_cv, adj_form, adj_words, adj_words4test, gu, mo, mode_selector):
    _adj = adj_cv()
    if adj_form is not None and _adj:
        _, _msg = gu.check_adjective_test(_adj['Word'], adj_form, mode=mode_selector.value)
        _remaining = len(adj_words4test())
        _total = len(adj_words)
        _view3 = mo.vstack([
            mo.md(f"#### Adjective test ({_remaining}/{_total})"),
            mo.md(f"Translation: **{_adj['Translation']}**"),
            adj_form,
            mo.md(_msg) if _msg else mo.md(""),
        ])
    else:
        _view3 = mo.md("_Select adjectives above to start the test._")
    _view3
    return


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
    if adj_form is not None and _adj and adj_form.value:
        _ok, _ = gu.check_adjective_test(_adj['Word'], adj_form, mode=mode_selector.value)
        gu.process_adjective_completion(
            _adj, _ok, adj_words, adj_words4test(),
            set_adj_words4test, set_adj_last_passed_mesg, set_adj_cv,
        )
    return


@app.cell(hide_code=True)
def _(adj_last_passed_mesg, mo):
    _alm = mo.md(adj_last_passed_mesg()) if adj_last_passed_mesg() else mo.md("")
    _alm
    return


@app.cell(hide_code=True)
def _():
    import os
    import random
    import marimo as mo

    from modern_greek_eee import greek_utils as gu

    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    return gu, mo, notebook_dir, random


if __name__ == "__main__":
    app.run()
