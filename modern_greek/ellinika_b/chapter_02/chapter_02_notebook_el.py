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

__generated_with = "0.23.16"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Σπίτι μου σπιτάκι μου 🏠
    ## Το σπίτι μου είναι το κάστρο μου

    **Εγχειρίδιο:** Ελληνικά Β' | **Ενότητα:** 2 | **Επίπεδο:** B1 | **Γλώσσα:** Ελληνικά

    **Θέμα:** Κατοικία, διαμονή

    **Τεστ σε αυτή την τετράδα:** Ουσιαστικά · Ρήματα · Επίθετα
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    ## Τεστ: Ουσιαστικά (Ουσιαστικά)
    """)
    return


@app.cell(hide_code=True)
def _(gu, notebook_dir):
    df_noun = gu.load_vocab_table("nouns.tsv", nb_dir=notebook_dir)
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, gu, mo):
    table_noun = gu.vocab_table(df_noun)
    mo.vstack([
        mo.md("### Επιλέξτε ουσιαστικά για τεστ"),
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
            mo.md(f"#### Κλίση ({_total - _remaining + 1}/{_total})"),
            mo.md(f"Μετάφραση: **{noun_trans}**"),
            noun_form,
        ])
    else:
        _view = mo.md("_Επιλέξτε ουσιαστικά παραπάνω για να ξεκινήσετε το τεστ._")
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
            mo.md(f"#### Άρθρα ({_total - _remaining + 1}/{_total})"),
            mo.md(f"Μετάφραση: **{art_noun_trans}**"),
            art_noun_form,
        ])
    else:
        _view = mo.md("_Επιλέξτε ουσιαστικά παραπάνω για να ξεκινήσετε το τεστ._")
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
    ## Τεστ: Ρήματα (Ρήματα)
    """)
    return


@app.cell(hide_code=True)
def _(gu, notebook_dir):
    df_verb = gu.load_vocab_table("verbs.tsv", nb_dir=notebook_dir)
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, gu, mo):
    table_verb = gu.vocab_table(df_verb)
    mo.vstack([
        mo.md("### Επιλέξτε ρήματα για τεστ"),
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
    _plain_el = {
        'present': 'Ενεστώτας',
        'imperfect': 'Παρατατικός',
        'aorist': 'Αόριστος',
        'future': 'Απλός Μέλλοντας',
        'future_continuous': 'Εξακολουθητικός Μέλλοντας',
    }
    _tense_opts = {
        f"{gu.TENSE_LABELS[k]['greek']} ({_plain_el[k]})": k
        for k in _chapter_tenses if k in gu.TENSE_LABELS
    }
    tense_selector = mo.ui.dropdown(
        options=_tense_opts,
        value=next(iter(_tense_opts)),
        label="Χρόνος:",
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
    _ui_label = _TENSE_UI_LABELS.get(_tense_key, _tense_key) if _tense_key else "Επιλέξτε χρόνο"
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
            _msg = f'<span style="color: green;">Τεστ για <b>"{cv_verb["Word"]} — {cv_verb["Translation"]}"</b> ολοκληρώθηκε.\n\nΑπομένουν {_remaining} από {_total}.</span>'
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
    ## Τεστ: Επίθετα (Επίθετα)
    """)
    return


@app.cell(hide_code=True)
def _(gu, notebook_dir):
    df_adj = gu.load_vocab_table("adjectives.tsv", nb_dir=notebook_dir)
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, gu, mo):
    table_adj = gu.vocab_table(df_adj)
    mo.vstack([
        mo.md("### Επιλέξτε επίθετα για τεστ"),
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
            "Απλό: 3 γένη × 2 αριθμοί (6 πεδία)": "simple",
            "Πλήρες: όλα τα γένη, αριθμοί και πτώσεις (18 πεδία)": "complex",
        },
        value="Απλό: 3 γένη × 2 αριθμοί (6 πεδία)",
        label="Τύπος τεστ:",
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
