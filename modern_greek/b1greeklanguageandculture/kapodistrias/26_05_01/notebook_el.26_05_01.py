# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.14",
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "modern-greek-backend-eee @ git+https://codeberg.org/EEE-project/modern-greek-backend-eee.git",
#     "pandas==3.0.2",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# modern-greek-backend-eee = { git = "https://codeberg.org/EEE-project/modern-greek-backend-eee.git" }
# ///

import marimo

__generated_with = "0.23.5"
app = marimo.App(
    width="medium",
    css_file="/usr/local/_marimo/custom.css",
    html_head_file="head.html",
    auto_download=["html"],
)


@app.cell(hide_code=True)
def _(mo, notebook_dir, os):
    def _img(n):
        _p = os.path.join(notebook_dir, f'slide-{n}.jpg')
        return mo.image(src=open(_p, 'rb').read(), width=700) if os.path.exists(_p) else mo.md("")
    mo.vstack([
        mo.md(r"""
        # **Ιωάννης Καποδίστριας: Ο Πρώτος Κυβερνήτης της Ελλάδας**
        Ακολουθεί μια σύνοψη των πληροφοριών για τον Ιωάννη Καποδίστρια από την [παρουσίαση](https://docs.google.com/presentation/d/1Za9Z9vyZDUYFn_Rv_QZBga_GxfO5fn9I/edit?usp=sharing&ouid=114390708685640574713&rtpof=true&sd=true) και την ταινία "Ιωάννης Καποδίστριας – Η Συγκλονιστική Ιστορία του Πρώτου Κυβερνήτη της Ελλάδας" ([υπότιτλοι](https://drive.google.com/file/d/1z-3NR6gyGQg4kugiOVovggtP4_UWoIKh/view?usp=drive_link)):
        """),
        _img(1),
        mo.Html('''<iframe
            width="560"
            height="315"
            src="https://www.youtube.com/embed/IeLVfRQ9Lsk"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
        </iframe>'''),
        _img(2),
        mo.md(r"""
        ## **1. Καταγωγή και Πρώτα Χρόνια**
        *   Ο Ιωάννης Καποδίστριας γεννήθηκε στην **Κέρκυρα το 1776**.
        *   Σπούδασε **ιατρική, φιλοσοφία και νομικά** στην Ιταλία.
        *   Το επώνυμό του έχει ιταλική προέλευση (**Capo d'Istria**) και σημαίνει "από την Ιστρία", μια περιοχή στη σημερινή Σλοβενία/Κροατία, ενώ το αρχικό του επώνυμο ήταν "Βιττόρι".
        """),
        _img(3),
        _img(4),
        mo.md(r"""
        ## **2. Διπλωματική Καριέρα στη Ρωσία**
        *   Το 1808 μετανάστευσε στη **Ρωσία**, όπου εργάστηκε ως διπλωμάτης.
        *   Αναδείχθηκε σε έναν από τους κορυφαίους διπλωμάτες της Ευρώπης, φτάνοντας στη θέση του **Υπουργού Εξωτερικών του Τσάρου Αλεξάνδρου Α΄**.
        *   Παρά την πλούσια και ασφαλή ζωή του στη Ρωσία, αποφάσισε να τα εγκαταλείψει όλα για να βοηθήσει την Ελλάδα μετά την επανάσταση.
        """),
        _img(5),
        mo.md(r"""
        ## **3. Η Διακυβέρνηση της Ελλάδας (1828-1831)**
        *   Έφτασε στην Ελλάδα το **1828** και βρήκε μια χώρα σε κατάσταση απόλυτου χάους, χωρίς στρατό, ταμείο, δρόμους ή σχολεία.
        *   **Σημαντικά Έργα:**
            *   Ίδρυσε το πρώτο **σχολικό σύστημα**.
            *   Οργάνωσε τον **τακτικό στρατό** και τη δημόσια διοίκηση.
            *   Έκοψε το πρώτο ελληνικό νόμισμα, τον **Φοίνικα**.
        *   **Προσωπική Στάση:** Αρνήθηκε να λαμβάνει μισθό και διέθεσε την προσωπική του περιουσία για τη στήριξη ορφανών και χηρών.
        """),
        _img(6),
        mo.md(r"""
        ## **4. Συγκρούσεις και Αντιπολίτευση**
        *   Η πολιτική του για ένα **ισχυρό κεντρικό κράτος** προκάλεσε την οργή των τοπικών αρχόντων και ισχυρών οικογενειών, όπως οι **Μαυρομιχαλαίοι**, που έχασαν τα προνόμιά τους.
        *   Οι ξένες δυνάμεις τον αντιμετώπιζαν με καχυποψία, καθώς ήθελαν μια Ελλάδα αδύναμη και ελεγχόμενη.

        ## **5. Η Δολοφονία και η Κληρονομιά του**
        *   Δολοφονήθηκε το πρωί της **27ης Σεπτεμβρίου 1831** στο Ναύπλιο, έξω από την εκκλησία του Αγίου Σπυρίδωνα.
        *   Δράστες ήταν ο Κωνσταντίνος και ο Γεώργιος Μαυρομιχάλης.
        *   Μετά τον θάνατό του, η χώρα βυθίστηκε ξανά στο χάος και στις εμφύλιες συγκρούσεις. Εμφύλιες συγκρούσεις, ξένες παρεμβάσεις και τελικά ένας βασιλιάς από το εξωτερικό.
        *   Η σημαντικότερη κληρονομιά του ήταν η ιδέα ότι η Ελλάδα μπορεί να λειτουργήσει ως ένα **σύγχρονο, οργανωμένο και έντιμο κράτος**.
        """),
    ])
    return


@app.cell(hide_code=True)
def _(mo, notebook_dir, os, pd):
    df_vocabulary = pd.read_csv(os.path.join(notebook_dir, 'vocabulary.tsv'), sep='\t')
    table_vocabulary = mo.ui.table(df_vocabulary, selection="multi") if df_vocabulary is not None else None
    mo.vstack([
        mo.md("## ΧΡΗΣΙΜΕΣ ΛΕΞΕΙΣ"),
        table_vocabulary,
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## ΟΥΣΙΑΣΤΙΚΑ
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    tbl_sel_n, set_tbl_sel_n = mo.state(None)
    session_total_n, set_session_total_n = mo.state(0)
    return session_total_n, set_session_total_n, set_tbl_sel_n, tbl_sel_n


@app.cell(hide_code=True)
def _(mo):
    file_upload_noun = mo.ui.file(label="Φόρτωση TSV ουσιαστικών")
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
def _(df_noun, mo, tbl_sel_n):
    table_noun = mo.ui.table(df_noun, selection="multi", initial_selection=(tbl_sel_n() if tbl_sel_n() is not None else list(range(len(df_noun))))) if df_noun is not None else None
    mo.vstack([
        mo.md("### Επιλέξτε ουσιαστικά για εξάσκηση"),
        table_noun,
    ])
    return (table_noun,)


@app.cell(hide_code=True)
def _(gu, mo, random, session_total_n, set_session_total_n, table_noun):
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
    skip_button_n = mo.ui.button(label="Παράλειψη", on_click=_clk)
    clear_button_n = mo.ui.button(label="Καθαρισμός", on_click=_clk)
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
    clear_count_n()
    _nc = current_noun()
    noun_word, noun_trans, noun_form = gu.create_noun_test_ui([_nc] if _nc else [], mode='simple')
    return noun_form, noun_trans, noun_word


@app.cell(hide_code=True)
def _(clear_count_n, current_noun, gu):
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
    submit_button_n = mo.ui.button(label="Υποβολή", on_click=_clk, kind="warn" if _dirty else "neutral")
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
    _feedback = mo.md("")
    if words4test_noun() and noun_word:
        _cs = captured_simple()
        if _cs and getattr(_cs, 'test_word', None) == noun_word:
            with mo.capture_stdout() as _buf:
                gu.check_noun_test(noun_word, _cs, mode='simple')
            if _buf.getvalue():
                _feedback = mo.md(_buf.getvalue())
        _view = mo.vstack([
            mo.md(f"**Απλό τεστ: Ουσιαστικά** ({len(words4test_noun())}/{session_total_n()})"),
            mo.md(f"Μετάφραση: **{noun_trans}**"),
            noun_form,
            _feedback,
            mo.hstack([skip_button_n, clear_button_n, submit_button_n], justify="end"),
        ])
    else:
        _view = mo.md("_Επιλέξτε ουσιαστικά από τον πίνακα παραπάνω._")
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
    _feedback_a = mo.md("")
    if words4test_noun() and art_noun_word:
        _ca = captured_article()
        if _ca and getattr(_ca, 'test_word', None) == art_noun_word:
            with mo.capture_stdout() as _buf_a:
                gu.check_noun_test(art_noun_word, _ca, mode='article')
            if _buf_a.getvalue():
                _feedback_a = mo.md(_buf_a.getvalue())
        _view_art = mo.vstack([
            mo.md(f"**Τεστ με άρθρο: Ουσιαστικά** ({len(words4test_noun())}/{session_total_n()})"),
            mo.md(f"Μετάφραση: **{art_noun_trans}**"),
            art_noun_form,
            _feedback_a,
            mo.hstack([skip_button_n, clear_button_n, submit_button_n], justify="end"),
        ])
    else:
        _view_art = mo.md("_Επιλέξτε ουσιαστικά από τον πίνακα παραπάνω._")
    _view_art
    return


@app.cell(hide_code=True)
def _(mo, noun_msg):
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
            set_noun_msg(f'<span style="color:green;">Τεστ για <b>"{_cn["Word"]}"</b> ολοκληρώθηκε.\n\n{len(_new)} λέξεις απομένουν από {session_total_n()}.</span>')
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
    if (clear_button_n.value or 0) > clear_count_n():
        set_clear_count_n(clear_button_n.value)
        set_captured_simple(None)
        set_captured_article(None)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## ΡΗΜΑΤΑ
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    tbl_sel_v, set_tbl_sel_v = mo.state(None)
    session_total_v, set_session_total_v = mo.state(0)
    return session_total_v, set_session_total_v, set_tbl_sel_v, tbl_sel_v


@app.cell(hide_code=True)
def _(mo):
    file_upload_verb = mo.ui.file(label="Φόρτωση TSV ρημάτων")
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
def _(df_verb, mo, tbl_sel_v):
    table_verb = mo.ui.table(df_verb, selection="multi", initial_selection=(tbl_sel_v() if tbl_sel_v() is not None else list(range(len(df_verb))))) if df_verb is not None else None
    mo.vstack([mo.md("### Επιλέξτε ρήματα για εξάσκηση"), table_verb])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu, mo):
    _b1_tenses = ['present', 'imperfect', 'aorist', 'future', 'future_continuous']
    _tense_options = {gu.TENSE_LABELS[k]['dropdown']: k for k in _b1_tenses if k in gu.TENSE_LABELS}
    tense_selector = mo.ui.dropdown(
        options=_tense_options,
        value=gu.TENSE_LABELS['present']['dropdown'],
        label="Επιλέξτε χρόνο:",
    )
    tense_selector
    return (tense_selector,)


@app.cell(hide_code=True)
def _(gu, mo, random, session_total_v, set_session_total_v, table_verb):
    words_verb = gu.get_words(table_verb)
    words4test_verb, set_words4test_verb = mo.state(words_verb.copy() if words_verb else [])
    if words_verb and len(words_verb) > session_total_v():
        set_session_total_v(len(words_verb))
    elif not words_verb:
        set_session_total_v(0)
    verb_msg, set_verb_msg = mo.state("")
    captured_verb, set_captured_verb = mo.state(None)
    cv_verb, set_cv_verb = mo.state(None)
    _clk = lambda v: (v or 0) + 1
    skip_button_v = mo.ui.button(label="Παράλειψη", on_click=_clk)
    clear_button_v = mo.ui.button(label="Καθαρισμός", on_click=_clk)
    skip_count_v, set_skip_count_v = mo.state(0)
    clear_count_v, set_clear_count_v = mo.state(0)
    submit_count_v, set_submit_count_v = mo.state(0)
    if words_verb and cv_verb() is None:
        set_cv_verb(random.choice(words_verb))
    return (
        captured_verb,
        clear_button_v,
        clear_count_v,
        cv_verb,
        set_captured_verb,
        set_clear_count_v,
        set_cv_verb,
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
def _(clear_count_v, cv_verb, gu, tense_selector, words4test_verb, words_verb):
    clear_count_v()
    _cv = cv_verb()
    _tense_key = tense_selector.value
    _ui_label = gu.TENSE_LABELS[_tense_key]['greek'] if _tense_key else "—"
    verb_fields, _ = gu.create_verb_test_ui(_ui_label, words_verb, words4test_verb(), _cv)
    return (verb_fields,)


@app.cell(hide_code=True)
def _(captured_verb, mo, set_submit_count_v, tense_selector, verb_fields):
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
    submit_button_v = mo.ui.button(label="Υποβολή", on_click=_clk, kind="warn" if _dirty else "neutral")
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
    _cv = cv_verb()
    if not words4test_verb():
        _view_verb = mo.md("_Επιλέξτε ρήματα από τον πίνακα παραπάνω._")
    elif not tense_selector.value:
        _view_verb = mo.md("_Επιλέξτε χρόνο παραπάνω._")
    else:
        _feedback_v = mo.md("")
        _c = captured_verb()
        if _cv and _c and getattr(_c, 'verb_word', None) == _cv['Word'] and getattr(_c, 'tense', None) == tense_selector.value:
            _, _msg = gu.check_verb_test(_cv['Word'], _c, tense_selector.value)
            _feedback_v = mo.md(_msg)
        _label = gu.TENSE_LABELS.get(tense_selector.value, {}).get('greek', tense_selector.value)
        _items = [mo.md(f"**Τεστ ρήματος — {_label}** ({len(words4test_verb())}/{session_total_v()})")]
        if verb_msg():
            _items.append(mo.md(verb_msg()))
        _items += [
            mo.md(f"Μετάφραση: **{_cv['Translation']}**") if _cv else mo.md(""),
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
    random,
    session_total_v,
    set_captured_verb,
    set_cv_verb,
    set_tbl_sel_v,
    set_verb_msg,
    set_words4test_verb,
    tense_selector,
    words4test_verb,
):
    _tense_key = tense_selector.value
    _c = captured_verb()
    _cv = cv_verb()
    if _cv and _tense_key and _c and getattr(_c, 'verb_word', None) == _cv['Word'] and getattr(_c, 'tense', None) == _tense_key:
        _ok, _ = gu.check_verb_test(_cv['Word'], _c, _tense_key)
        if _ok:
            _new = [w for w in words4test_verb() if w['Word'] != _cv['Word']]
            set_words4test_verb(_new)
            if df_verb is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_v([i for i, w in enumerate(df_verb['Word']) if w in _rem])
            set_verb_msg(f'<span style="color:green;">Τεστ για <b>"{_cv["Word"]} — {_cv["Translation"]}"</b> ολοκληρώθηκε.\n\n{len(_new)} λέξεις απομένουν από {session_total_v()}.</span>')
            set_captured_verb(None)
            set_cv_verb(random.choice(_new) if _new else None)
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
    if (submit_button_v.value or 0) > submit_count_v():
        set_submit_count_v(submit_button_v.value)
        _cv = cv_verb()
        if _cv and verb_fields:
            set_captured_verb(gu.make_snapshot(verb_fields, verb_word=_cv['Word'], tense=tense_selector.value))
    return


@app.cell(hide_code=True)
def _(
    cv_verb,
    df_verb,
    random,
    set_captured_verb,
    set_cv_verb,
    set_skip_count_v,
    set_tbl_sel_v,
    set_words4test_verb,
    skip_button_v,
    skip_count_v,
    words4test_verb,
):
    if (skip_button_v.value or 0) > skip_count_v():
        set_skip_count_v(skip_button_v.value)
        set_captured_verb(None)
        _cv = cv_verb()
        _new = [w for w in words4test_verb() if not _cv or w['Word'] != _cv['Word']]
        set_words4test_verb(_new)
        if df_verb is not None:
            _rem = {w['Word'] for w in _new}
            set_tbl_sel_v([i for i, w in enumerate(df_verb['Word']) if w in _rem])
        set_cv_verb(random.choice(_new) if _new else None)
    return


@app.cell(hide_code=True)
def _(clear_button_v, clear_count_v, set_captured_verb, set_clear_count_v):
    if (clear_button_v.value or 0) > clear_count_v():
        set_clear_count_v(clear_button_v.value)
        set_captured_verb(None)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## ΕΠΙΘΕΤΑ
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    tbl_sel_a, set_tbl_sel_a = mo.state(None)
    session_total_a, set_session_total_a = mo.state(0)
    return session_total_a, set_session_total_a, set_tbl_sel_a, tbl_sel_a


@app.cell(hide_code=True)
def _(mo):
    file_upload_adj = mo.ui.file(label="Φόρτωση TSV επιθέτων")
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
def _(df_adj, mo, tbl_sel_a):
    table_adj = mo.ui.table(df_adj, selection="multi", initial_selection=(tbl_sel_a() if tbl_sel_a() is not None else list(range(len(df_adj))))) if df_adj is not None else None
    mo.vstack([mo.md("### Επιλέξτε επίθετα για εξάσκηση"), table_adj])
    return (table_adj,)


@app.cell(hide_code=True)
def _(mo):
    mode_selector = mo.ui.radio(
        options={
            "Απλό: 3 γένη × 2 αριθμοί (6 πεδία)": "simple",
            "Πλήρες: όλα τα γένη, αριθμοί και πτώσεις (18 πεδία)": "complex",
        },
        value="Απλό: 3 γένη × 2 αριθμοί (6 πεδία)",
        label="Λειτουργία τεστ:",
    )
    mo.md(f"{mode_selector}")
    return (mode_selector,)


@app.cell(hide_code=True)
def _(gu, mo, random, session_total_a, set_session_total_a, table_adj):
    adj_words = gu.get_words(table_adj)
    words4test_adj, set_words4test_adj = mo.state(adj_words.copy() if adj_words else [])
    if adj_words and len(adj_words) > session_total_a():
        set_session_total_a(len(adj_words))
    elif not adj_words:
        set_session_total_a(0)
    adj_last_passed_mesg, set_adj_last_passed_mesg = mo.state("")
    adj_cv, set_adj_cv = mo.state(None)
    captured_adj, set_captured_adj = mo.state(None)
    _clk = lambda v: (v or 0) + 1
    skip_button_a = mo.ui.button(label="Παράλειψη", on_click=_clk)
    clear_button_a = mo.ui.button(label="Καθαρισμός", on_click=_clk)
    skip_count_a, set_skip_count_a = mo.state(0)
    clear_count_a, set_clear_count_a = mo.state(0)
    submit_count_a, set_submit_count_a = mo.state(0)
    if adj_words and adj_cv() is None:
        set_adj_cv(random.choice(adj_words))
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
    clear_count_a()
    _acv = adj_cv()
    adj_form, _ = gu.create_adjective_test_ui([] if not _acv else [_acv], [], _acv, mode=mode_selector.value)
    return (adj_form,)


@app.cell(hide_code=True)
def _(adj_form, captured_adj, mo, set_submit_count_a):
    _values = adj_form.value if adj_form else []
    _snap = captured_adj()
    _has_input = bool(_values and any(v.strip() for v in _values))
    _matches_snap = _snap is not None and [v.strip() for v in _values] == [v.strip() for v in (_snap.value or [])]
    _dirty = _has_input and not _matches_snap
    _clk = lambda v: (v or 0) + 1
    submit_button_a = mo.ui.button(label="Υποβολή", on_click=_clk, kind="warn" if _dirty else "neutral")
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
    _adj = adj_cv()
    if words4test_adj() and _adj:
        _feedback_a = mo.md("")
        _c = captured_adj()
        if _c and getattr(_c, 'adj_word', None) == _adj['Word']:
            _, _msg = gu.check_adjective_test(_adj['Word'], _c, mode=mode_selector.value)
            if _msg:
                _feedback_a = mo.md(_msg)
        _view_adj = mo.vstack([
            mo.md(f"**Τεστ: Κλίση επιθέτου** ({len(words4test_adj())}/{session_total_a()})"),
            mo.md(f"Μετάφραση: **{_adj['Translation']}**"),
            adj_form,
            _feedback_a,
            mo.hstack([skip_button_a, clear_button_a, submit_button_a], justify="end"),
        ])
    else:
        _view_adj = mo.md("_Επιλέξτε επίθετα από τον πίνακα παραπάνω._")
    _view_adj
    return


@app.cell(hide_code=True)
def _(adj_last_passed_mesg, mo):
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
            set_adj_last_passed_mesg(f'<span style="color:green;">Τεστ για <b>"{_adj["Word"]} — {_adj["Translation"]}"</b> ολοκληρώθηκε.\n\n{len(_new)} λέξεις απομένουν από {session_total_a()}.</span>')
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
    if (clear_button_a.value or 0) > clear_count_a():
        set_clear_count_a(clear_button_a.value)
        set_captured_adj(None)
    return


@app.cell(hide_code=True)
def _():
    import os, random, pandas as pd, marimo as mo
    import eee_project as eee
    from eee_project import GreekUtils
    from modern_greek_backend_eee import ModernGreekBackend
    mg = ModernGreekBackend()
    eee.register_backend("el", mg)
    gu = GreekUtils(mg, mo, pd, eee_module=eee)
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    return gu, mo, notebook_dir, os, pd, random


if __name__ == "__main__":
    app.run()
