# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.22.4",
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
    ## Κοινωνικές επαφές & Επικοινωνία

    **Επίπεδο:** B1 | **Θέμα:** Κοινωνικές επαφές & Επικοινωνία

    Αυτό το notebook περιλαμβάνει:
    - 📖 Γραμματική εξήγηση
    - 💬 Χρήσιμες φράσεις
    - 🧪 Tests: Ουσιαστικά · Ρήματα · Επίθετα
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Γραμματική

    ### Α. Αδύνατοι τύποι προσωπικών αντωνυμιών (Αιτιατική)

    Χρησιμοποιούνται ως άμεσα αντικείμενα — τοποθετούνται **πριν** από το ρήμα.

    | Πρόσωπο | Ενικός | Πληθυντικός |
    |---------|--------|-------------|
    | 1ο | **με** (me) | **μας** (us) |
    | 2ο | **σε** (you) | **σας** (you) |
    | 3ο αρσ. | **τον** (him) | **τους** (them) |
    | 3ο θηλ. | **την** (her) | **τις / τες** (them) |
    | 3ο ουδ. | **το** (it) | **τα** (them) |

    _Παράδειγμα:_ **Σε** ακούω. _(I hear you.)_
    _Παράδειγμα:_ Ποιος **τη** ζητάει; _(Who is asking for her?)_

    ---

    ### Β. Πτώσεις ουσιαστικών: Ονομαστική, Αιτιατική, Κλητική

    | Πτώση | Αρσενικό | Θηλυκό | Ουδέτερο |
    |-------|----------|--------|----------|
    | **Ονομ.** | ο Γιώργος | η Μαρίνα | το πάρτι |
    | **Αιτ.** | τον Γιώργο | τη(ν) Μαρίνα | το πάρτι |
    | **Κλητ.** | Γιώργο! | Μαρίνα! | πάρτι |

    **Θηλυκά ουσιαστικά σε -ος** ακολουθούν κλίση αρσενικών:

    | Ονομαστική | Γενική | Αιτιατική |
    |-----------|--------|-----------|
    | η **οδός** | της **οδού** | την **οδό** |
    | η **είσοδος** | της **εισόδου** | την **είσοδο** |
    | η **λεωφόρος** | της **λεωφόρου** | την **λεωφόρο** |

    ---

    ### Γ. Απαλοιφή φωνήεντος (Elision)

    Όταν μια λέξη που τελειώνει σε φωνήεν ακολουθείται από λέξη που αρχίζει με φωνήεν,
    το πρώτο φωνήεν αποβάλλεται και αντικαθίσταται με απόστροφο:

    | Κανονικός τύπος | Συντομευμένος τύπος | Μετάφραση |
    |-----------------|---------------------|-----------|
    | μου **είπε** | μου **'πε** | he told me |
    | σου **είπα** | σου **'πα** | I told you |
    | να **είναι** | να **'ναι** | to be |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Χρήσιμες Φράσεις — Τηλεφωνική Επικοινωνία

    | Ελληνική Φράση | Αγγλική Μετάφραση | Περίσταση |
    |----------------|-------------------|-----------|
    | Παρακαλώ. / Λέγετε; / Εμπρός. | Hello? / Yes? | Τυπικός χαιρετισμός στο τηλέφωνο |
    | Λάθος πήρατε. | You have the wrong number. | Λανθασμένος αριθμός |
    | Αφήστε το μήνυμά σας. | Leave your message. | Τηλεφωνητής / αυτόματος τηλεφωνητής |
    | Ποιος τη/τον ζητάει; | Who is asking for her/him? | Ρωτάμε τον καλούντα |
    | Μισό λεπτό (να την φωνάξω). | One moment, I'll call her. | Βάζουμε σε αναμονή |
    | Καλώς ήλθατε! / Καλώς ορίσατε! | Welcome! | Χαιρετισμός επισκέπτη |
    | Να σας συστήσω τον φίλο μου... | May I introduce my friend... | Κοινωνική παρουσίαση |
    | Χαίρω πολύ. / Χάρηκα πολύ. | Pleased to meet you. | Απάντηση σε παρουσίαση |
    | Συγχαρητήρια! | Congratulations! | Ευχές για πτυχίο / επιτυχία |
    | Δεν πειράζει. / Δεν υπάρχει πρόβλημα. | No problem. | Κατευνασμός |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Τεστ: Ουσιαστικά
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    file_upload_noun = mo.ui.file(label="Φόρτωση αρχείου ουσιαστικών (nouns.tsv) — προαιρετικό", filetypes=[".tsv"])
    file_upload_noun
    return (file_upload_noun,)


@app.cell(hide_code=True)
def _(file_upload_noun, notebook_dir, os, pd):
    if file_upload_noun.value:
        from modern_greek_eee import greek_utils as _gu
        df_noun = _gu.load_data(file_upload_noun, [])
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
        mo.md("### Επιλέξτε ουσιαστικά για εξάσκηση"),
        table_noun if table_noun is not None else mo.md("_Το αρχείο nouns.tsv δεν βρέθηκε — φόρτωσε αρχείο._")
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
            mo.md(f"#### Κλίση ({_total - _remaining + 1}/{_total})"),
            mo.md(f"**Μετάφραση:** {noun_trans}"),
            noun_form,
        ])
    else:
        _view = mo.md("Επιλέξτε λέξεις για να ξεκινήσετε το τεστ.")
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
            mo.md(f"#### Άρθρα ({_total - _remaining + 1}/{_total})"),
            mo.md(f"**Μετάφραση:** {art_noun_trans}"),
            art_noun_form,
        ])
    else:
        _view = mo.md("Επιλέξτε λέξεις για να ξεκινήσετε το τεστ.")
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
    ## Τεστ: Ρήματα
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    file_upload_verb = mo.ui.file(label="Φόρτωση αρχείου ρημάτων (verbs.tsv) — προαιρετικό", filetypes=[".tsv"])
    file_upload_verb
    return (file_upload_verb,)


@app.cell(hide_code=True)
def _(file_upload_verb, notebook_dir, os, pd):
    if file_upload_verb.value:
        from modern_greek_eee import greek_utils as _gu
        df_verb = _gu.load_data(file_upload_verb, [])
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
        mo.md("### Επιλέξτε ρήματα για εξάσκηση"),
        table_verb if table_verb is not None else mo.md("_Το αρχείο verbs.tsv δεν βρέθηκε — φόρτωσε αρχείο._")
    ])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu, table_verb):
    words_verb = gu.get_words(table_verb)
    return (words_verb,)


@app.cell(hide_code=True)
def _(gu, mo):
    _b1_tenses = ['present', 'imperfect', 'aorist', 'future', 'future_continuous']
    _plain_en = {
        'present': 'Present',
        'imperfect': 'Imperfect (Past)',
        'aorist': 'Simple Past',
        'future': 'Simple Future',
        'future_continuous': 'Continuous Future',
    }
    _tense_options = {
        f"{gu.TENSE_LABELS[k]['greek']} ({_plain_en[k]})": k
        for k in _b1_tenses if k in gu.TENSE_LABELS
    }
    _first_key = next(iter(_tense_options))
    tense_selector = mo.ui.dropdown(
        options=_tense_options,
        value=_first_key,
        label="Επιλέξτε χρόνο:"
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
            mo.md(f"#### Τεστ ρήματος ({_total - _remaining + 1}/{_total})"),
            _verb_md,
        ])
    else:
        verb_form = None
        _view = mo.md("Επιλέξτε λέξεις για να ξεκινήσετε το τεστ.")
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
            _msg = f'Τεστ για <b>"{cv_verb["Word"]} — {cv_verb["Translation"]}"</b> ολοκληρώθηκε.\n\nΑπομένουν {_remaining} από {_total}.'
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
    ## Τεστ: Επίθετα
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    file_upload_adj = mo.ui.file(label="Φόρτωση αρχείου επιθέτων (adjectives.tsv) — προαιρετικό", filetypes=[".tsv"])
    file_upload_adj
    return (file_upload_adj,)


@app.cell(hide_code=True)
def _(file_upload_adj, notebook_dir, os, pd):
    if file_upload_adj.value:
        from modern_greek_eee import greek_utils as _gu
        df_adj = _gu.load_data(file_upload_adj, [])
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
        mo.md("### Επιλέξτε επίθετα για εξάσκηση"),
        table_adj if table_adj is not None else mo.md("_Το αρχείο adjectives.tsv δεν βρέθηκε — φόρτωσε αρχείο._")
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
            "Πλήρες: όλα τα γένη, αριθμοί και πτώσεις (18 πεδία)": "complex"
        },
        value="Απλό: 3 γένη × 2 αριθμοί (6 πεδία)",
        label="Λειτουργία test:"
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
        _view = mo.md("Επιλέξτε λέξεις για να ξεκινήσετε το τεστ.")
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
