# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.14",
#     "eee-project>=1.1.0",
#     "modern-greek-backend-eee>=1.0.0",
#     "pandas==3.0.2",
# ]
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App(
    width="medium",
    css_file="/usr/local/_marimo/custom.css",
    html_head_file="head.html",
    auto_download=["html"],
)


@app.cell(hide_code=True)
def _(language_selector, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _cfg = ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/modern_greek/b1greeklanguageandculture/zorba/index.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=_cfg.index_url(), lang=language_selector.value, titles={
        "ru": "Алексис Зорбас", "el": "Αλέξης Ζορμπάς", "en": "Alexis Zorbas",
    }, ga_config=_cfg.ga_config(), same_window=True)
    return


@app.cell(hide_code=True)
def _(RAW_BASE, gu, language_selector, mo, notebook_dir):
    _lang = language_selector.value
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_CHTRKm9qTf6hSeF455c8iV)"
    def _img(n):
        _p = gu.ensure_file(f'slide-{n}.jpg', nb_dir=notebook_dir, remote_base=RAW_BASE)
        return mo.image(src=open(_p, 'rb').read(), width=700) if _p else mo.md("")
    if _lang == "ru":
        _c = mo.vstack([
            mo.md(f"""
            # **Алексис Зорбас: кто он?** {_badge}
            По материалам презентации «ΑΛΕΞΗΣ ΖΟΡΜΠΑΣ» и записей занятия 26/6/2026:
            """),
            _img(1),
            mo.md(r"""
            ### **Кто такой Алексис Зорбас?**
            *   Что вы видите? Сколько ему лет? Кем он работает? Он богат или беден? Он счастлив?
            """),
            _img(2),
            _img(3),
            mo.md(r"""
            ### **Настоящий Зорбас**
            *   Алексис Зорбас был реальным человеком. Его настоящее имя — **Георгиос Зорбас**. Он родился в **1865 году** в Катафигио (Козани), а умер в **1941 году** в Скопье.
            *   В жизни он сменил много профессий: был **лесорубом, животноводом, кузнецом и шахтёром**. Любил путешествовать и знакомиться с новыми людьми.
            *   В **1914 году** он познакомился с писателем **Никосом Казандзакисом** на Афоне. Несколько лет спустя они вместе работали на руднике в Мани.
            *   Казандзакис был впечатлён характером Зорбаса и написал знаменитую книгу **«Βίος και Πολιτεία του Αλέξη Ζορμπά»** («Жизнь и деяния Алексиса Зорбаса»), изданную в **1946 году**.
            *   В книге Зорбас предстаёт человеком, который любит жизнь, природу, музыку и свободу. Он оптимистичен, непосредственен и не боится трудностей.
            *   Книга стала всемирно известной, а в **1964 году** по ней сняли фильм. Роль Зорбаса сыграл **Энтони Куин**. Музыка **Микиса Теодоракиса** и танец **сиртаки** прославились на весь мир и стали ассоциироваться с Грецией.
            """),
            _img(4),
            mo.md(r"""
            ### **Занимательный факт**
            Многие считают, что имя выбрано неслучайно: приставка «алекси-» в древнегреческом означает «защищать» и «сопротивляться». Так герой символизирует человека, который борется с трудностями и никогда не сдаётся (**δεν τα παρατάω**).
            """),
            _img(5),
            mo.md(r"""
            ### **А кто, по-вашему, Зорбас?**
            - https://youtu.be/BpsVm2N7HuO?si=253frk2Db9SkR0EY
            - https://youtu.be/zkk6mFg90bE?si=Zivm7AjHC1O8T1P0
            """),
            _img(6),
            mo.md(r"""
            ### **Существительные**
            *   ο ήρωας → герой
            *   ο συγγραφέας → писатель
            *   ο χαρακτήρας → характер
            *   η ελευθερία → свобода
            *   η φύση → природа
            *   το ορυχείο → шахта
            *   ο μεταλλωρύχος → шахтёр
            *   ο σιδεράς → кузнец
            *   ο κτηνοτρόφος → животновод
            *   ο υλοτόμος → лесоруб (αυτός που κόβει ξύλα, ύλη = δάσος, ξυλεία + -τόμος = αυτός που κόβει από το ρήμα τέμνω = κόβω; синоним: ξυλοκόπος)
            *   ο χορός → танец
            *   το συρτάκι → сиртаки
            *   η έμπνευση → вдохновение
            *   η δυσκολία → трудность

            ### **Глаголы**
            *   γεννιέμαι → родиться
            *   πεθαίνω → умереть
            *   εργάζομαι → работать
            *   γνωρίζω → познакомиться с
            *   ταξιδεύω → путешествовать
            *   αγαπώ → любить
            *   γράφω → писать
            *   εκδίδω (εκδόθηκε) → издавать (быть изданным)
            *   παρουσιάζομαι → быть представленным
            *   γίνομαι → становиться
            *   παίζω (ρόλο) → играть (роль)
            *   συμβολίζω → символизировать
            *   παλεύω → бороться
            *   φοβάμαι → бояться
            *   συνδέομαι → ассоциироваться
            *   εντυπωσιάζομαι → быть впечатленным
            *   δεν τα παρατάω → не сдаваться (δεν τα αφήνω)

            ### **Прилагательные**
            *   πραγματικός → настоящий
            *   αισιόδοξος → оптимистичный
            *   αυθόρμητος → непосредственный
            *   ελεύθερος → свободный
            *   γενναίος → смелый
            *   εργατικός → трудолюбивый
            *   δυνατός → сильный
            *   χαρούμενος → весёлый
            *   παγκόσμιος → всемирный (παν + κόσμος)
            *   διαφορετικός → разный

            ### **Полезные фразы**
            *   παρουσιάζεται ως… → представлен как…
            *   παλεύει με τις δυσκολίες → борется с трудностями
            *   συμβολίζει την ελευθερία → символизирует свободу
            *   δεν τα παρατάει ποτέ → никогда не сдаётся
            *   συνδέθηκε με την Ελλάδα → стал символом (ассоциируется) с Грецией
            """),
        ])
    elif _lang == "el":
        _c = mo.vstack([
            mo.md(f"""
            # **Αλέξης Ζορμπάς: ποιος είναι;** {_badge}
            Με βάση την παρουσίαση «ΑΛΕΞΗΣ ΖΟΡΜΠΑΣ» και τις σημειώσεις του μαθήματος 26/6/2026:
            """),
            _img(1),
            mo.md(r"""
            ### **Ποιος είναι πραγματικά ο Αλέξης Ζορμπάς;**
            *   Τι βλέπετε; Πόσο χρονών είναι; Τι δουλειά κάνει; Είναι πλούσιος ή φτωχός; Είναι χαρούμενος;
            """),
            _img(2),
            _img(3),
            mo.md(r"""
            ### **Ο αληθινός Ζορμπάς**
            *   Ο Αλέξης Ζορμπάς ήταν πραγματικός άνθρωπος. Το πραγματικό του όνομα ήταν **Γεώργιος Ζορμπάς**. Γεννήθηκε το **1865** στο Καταφύγιο Κοζάνης και πέθανε το **1941** στα Σκόπια.
            *   Στη ζωή του έκανε πολλές δουλειές: **υλοτόμος, κτηνοτρόφος, σιδεράς και μεταλλωρύχος**. Του άρεσε να ταξιδεύει και να γνωρίζει νέους ανθρώπους.
            *   Το **1914** γνώρισε τον συγγραφέα **Νίκο Καζαντζάκη** στο Άγιο Όρος. Λίγα χρόνια αργότερα εργάστηκαν μαζί σε ένα ορυχείο στη Μάνη.
            *   Ο Καζαντζάκης εντυπωσιάστηκε από τον χαρακτήρα του Ζορμπά και έγραψε το διάσημο βιβλίο **«Βίος και Πολιτεία του Αλέξη Ζορμπά»**, που εκδόθηκε το **1946**.
            *   Στο βιβλίο, ο Ζορμπάς παρουσιάζεται ως ένας άνθρωπος που αγαπάει τη ζωή, τη φύση, τη μουσική και την ελευθερία. Είναι αισιόδοξος, αυθόρμητος και δεν φοβάται τις δυσκολίες.
            *   Το βιβλίο έγινε παγκόσμια γνωστό και το **1964** μεταφέρθηκε στον κινηματογράφο. Τον Ζορμπά έπαιξε ο **Άντονι Κουίν**. Η μουσική του **Μίκη Θεοδωράκη** και το **συρτάκι** έγιναν γνωστά σε όλο τον κόσμο και συνδέθηκαν με την Ελλάδα.
            """),
            _img(4),
            mo.md(r"""
            ### **Fun fact**
            Πολλοί πιστεύουν ότι το όνομα διαλέχτηκε γιατί το «αλεξι-» στα αρχαία ελληνικά σημαίνει προστατεύω και αντιστέκομαι. Έτσι, ο ήρωας συμβολίζει έναν άνθρωπο που παλεύει με τις δυσκολίες και δεν τα παρατάει ποτέ.
            """),
            _img(5),
            mo.md(r"""
            ### **Ποιος νομίζετε ότι είναι ο Ζορμπάς;**
            - https://youtu.be/BpsVm2N7HuO?si=253frk2Db9SkR0EY
            - https://youtu.be/zkk6mFg90bE?si=Zivm7AjHC1O8T1P0
            """),
            _img(6),
            mo.md(r"""
            ### **Ουσιαστικά**
            *   ο ήρωας
            *   ο συγγραφέας
            *   ο χαρακτήρας
            *   η ελευθερία
            *   η φύση
            *   το ορυχείο
            *   ο μεταλλωρύχος
            *   ο σιδεράς
            *   ο κτηνοτρόφος
            *   ο υλοτόμος (αυτός που κόβει ξύλα, ύλη = δάσος, ξυλεία + -τόμος = αυτός που κόβει από το ρήμα τέμνω = κόβω· συνών.: ξυλοκόπος)
            *   ο χορός
            *   το συρτάκι
            *   η έμπνευση
            *   η δυσκολία

            ### **Ρήματα**
            *   γεννιέμαι
            *   πεθαίνω
            *   εργάζομαι
            *   γνωρίζω
            *   ταξιδεύω
            *   αγαπώ
            *   γράφω
            *   εκδίδω (εκδόθηκε)
            *   παρουσιάζομαι
            *   γίνομαι
            *   παίζω (ρόλο)
            *   συμβολίζω
            *   παλεύω
            *   φοβάμαι
            *   συνδέομαι
            *   εντυπωσιάζομαι
            *   δεν τα παρατάω (δεν τα αφήνω)

            ### **Επίθετα**
            *   πραγματικός
            *   αισιόδοξος
            *   αυθόρμητος
            *   ελεύθερος
            *   γενναίος
            *   εργατικός
            *   δυνατός
            *   χαρούμενος
            *   παγκόσμιος (παν + κόσμος)
            *   διαφορετικός

            ### **Χρήσιμες φράσεις**
            *   παρουσιάζεται ως…
            *   παλεύει με τις δυσκολίες
            *   συμβολίζει την ελευθερία
            *   δεν τα παρατάει ποτέ
            *   συνδέθηκε με την Ελλάδα
            """),
        ])
    else:
        _c = mo.vstack([
            mo.md(f"""
            # **Alexis Zorbas: Who Is He?** {_badge}
            Based on the presentation "ΑΛΕΞΗΣ ΖΟΡΜΠΑΣ" and notes from the lesson on 26/6/2026:
            """),
            _img(1),
            mo.md(r"""
            ### **Who Is Alexis Zorbas, Really?**
            *   What do you see? How old is he? What's his job? Is he rich or poor? Is he happy?
            """),
            _img(2),
            _img(3),
            mo.md(r"""
            ### **The Real Zorbas**
            *   Alexis Zorbas was a real person. His real name was **Georgios Zorbas**. He was born in **1865** in Katafygio, Kozani, and died in **1941** in Skopje.
            *   Over his life he held many jobs: **lumberjack, herder, blacksmith, and miner**. He loved to travel and meet new people.
            *   In **1914** he met the writer **Nikos Kazantzakis** on Mount Athos. A few years later they worked together at a mine in Mani.
            *   Kazantzakis was impressed by Zorbas's character and wrote the famous book **"Βίος και Πολιτεία του Αλέξη Ζορμπά"** ("Zorba the Greek"), published in **1946**.
            *   In the book, Zorbas is portrayed as a man who loves life, nature, music, and freedom. He's optimistic, spontaneous, and unafraid of hardship.
            *   The book became world-famous, and in **1964** it was made into a film. Zorbas was played by **Anthony Quinn**. The music of **Mikis Theodorakis** and the **sirtaki** dance became world-famous and came to be associated with Greece.
            """),
            _img(4),
            mo.md(r"""
            ### **Fun Fact**
            Many believe the name was chosen deliberately: the prefix "alexi-" in Ancient Greek means "to ward off" and "to resist." So the hero symbolizes someone who fights hardship and never gives up.
            """),
            _img(5),
            mo.md(r"""
            ### **Who Do You Think Zorbas Is?**
            - https://youtu.be/BpsVm2N7HuO?si=253frk2Db9SkR0EY
            - https://youtu.be/zkk6mFg90bE?si=Zivm7AjHC1O8T1P0
            """),
            _img(6),
            mo.md(r"""
            ### **Nouns**
            *   ο ήρωας — hero
            *   ο συγγραφέας — writer
            *   ο χαρακτήρας — character
            *   η ελευθερία — freedom
            *   η φύση — nature
            *   το ορυχείο — mine
            *   ο μεταλλωρύχος — miner
            *   ο σιδεράς — blacksmith
            *   ο κτηνοτρόφος — herder
            *   ο υλοτόμος — lumberjack (from τέμνω/κόβω, "to cut"; synonym: ξυλοκόπος)
            *   ο χορός — dance
            *   το συρτάκι — sirtaki
            *   η έμπνευση — inspiration
            *   η δυσκολία — difficulty

            ### **Verbs**
            *   γεννιέμαι — to be born
            *   πεθαίνω — to die
            *   εργάζομαι — to work
            *   γνωρίζω — to meet
            *   ταξιδεύω — to travel
            *   αγαπώ — to love
            *   γράφω — to write
            *   εκδίδω (εκδόθηκε) — to publish (to be published)
            *   παρουσιάζομαι — to be presented
            *   γίνομαι — to become
            *   παίζω (ρόλο) — to play (a role)
            *   συμβολίζω — to symbolize
            *   παλεύω — to struggle
            *   φοβάμαι — to fear
            *   συνδέομαι — to be associated
            *   εντυπωσιάζομαι — to be impressed
            *   δεν τα παρατάω — never give up

            ### **Adjectives**
            *   πραγματικός — real
            *   αισιόδοξος — optimistic
            *   αυθόρμητος — spontaneous
            *   ελεύθερος — free
            *   γενναίος — brave
            *   εργατικός — hardworking
            *   δυνατός — strong
            *   χαρούμενος — joyful
            *   παγκόσμιος — worldwide (παν "all" + κόσμος "world")
            *   διαφορετικός — different

            ### **Useful Phrases**
            *   παρουσιάζεται ως… — presented as…
            *   παλεύει με τις δυσκολίες — struggles with hardship
            *   συμβολίζει την ελευθερία — symbolizes freedom
            *   δεν τα παρατάει ποτέ — never gives up
            *   συνδέθηκε με την Ελλάδα — became associated with Greece
            """),
        ])
    _c
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    mo.md(t_ui("nouns_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    tbl_sel_n, set_tbl_sel_n = mo.state(None)
    session_total_n, set_session_total_n = mo.state(0)
    return session_total_n, set_session_total_n, set_tbl_sel_n, tbl_sel_n


@app.cell(hide_code=True)
def _(mo):
    file_upload_noun = mo.ui.file(label="Upload nouns TSV")
    file_upload_noun
    return (file_upload_noun,)


@app.cell(hide_code=True)
def _(RAW_BASE, file_upload_noun, gu, notebook_dir):
    df_noun = gu.load_vocab_table("nouns.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE, ru_variant=True, language='ru', file_upload=file_upload_noun)
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, gu, language_selector, mo, t_ui, tbl_sel_n):
    table_noun = gu.vocab_table(df_noun, select_state=tbl_sel_n)
    mo.vstack([mo.md(t_ui("select_nouns", language_selector.value)), table_noun])
    return (table_noun,)


@app.cell(hide_code=True)
def _(eee, gu, mo, random, session_total_n, set_session_total_n, table_noun):
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
    _clk = eee.increment_counter
    skip_button_n = mo.ui.button(label="Skip", on_click=_clk)
    clear_button_n = mo.ui.button(label="Clear", on_click=_clk)
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
    eee,
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
    _clk = eee.increment_counter
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
    _lang = language_selector.value
    _feedback = mo.md("")
    if words4test_noun() and noun_word:
        _cs = captured_simple()
        if _cs and getattr(_cs, 'test_word', None) == noun_word:
            _, _msg = gu.check_noun_test(noun_word, _cs, mode='simple')
            if _msg:
                _feedback = mo.md(_msg)
        _view = mo.vstack([
            mo.md(t_ui("simple_noun_test", _lang).format(count=len(words4test_noun()), total=session_total_n())),
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
    _lang = language_selector.value
    _feedback_a = mo.md("")
    if words4test_noun() and art_noun_word:
        _ca = captured_article()
        if _ca and getattr(_ca, 'test_word', None) == art_noun_word:
            _, _msg_a = gu.check_noun_test(art_noun_word, _ca, mode='article')
            if _msg_a:
                _feedback_a = mo.md(_msg_a)
        _view_art = mo.vstack([
            mo.md(t_ui("article_noun_test", _lang).format(count=len(words4test_noun()), total=session_total_n())),
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
    _lang = language_selector.value
    _cn = current_noun()
    _cs = captured_simple()
    _ca = captured_article()
    if words4test_noun() and _cn and (_cs or _ca):
        _passed = False
        if _cs and getattr(_cs, 'test_word', None) == _cn['Word']:
            _passed, _ = gu.check_noun_test(_cn['Word'], _cs, mode='simple')
        if not _passed and _ca and getattr(_ca, 'test_word', None) == _cn['Word']:
            _passed, _ = gu.check_noun_test(_cn['Word'], _ca, mode='article')
        if _passed:
            _new = [w for w in words4test_noun() if w['Word'] != _cn['Word']]
            set_words4test_noun(_new)
            if df_noun is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_n([i for i, w in enumerate(df_noun['Word']) if w in _rem])
            set_noun_msg(t_ui("noun_passed", _lang).format(word=_cn['Word'], remaining=len(_new), total=session_total_n()))
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
def _(language_selector, mo, t_ui):
    mo.md(t_ui("verbs_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    tbl_sel_v, set_tbl_sel_v = mo.state(None)
    session_total_v, set_session_total_v = mo.state(0)
    return session_total_v, set_session_total_v, set_tbl_sel_v, tbl_sel_v


@app.cell(hide_code=True)
def _(mo):
    file_upload_verb = mo.ui.file(label="Upload verbs TSV")
    file_upload_verb
    return (file_upload_verb,)


@app.cell(hide_code=True)
def _(RAW_BASE, file_upload_verb, gu, notebook_dir):
    df_verb = gu.load_vocab_table("verbs.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE, file_upload=file_upload_verb)
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, gu, language_selector, mo, t_ui, tbl_sel_v):
    table_verb = gu.vocab_table(df_verb, select_state=tbl_sel_v)
    mo.vstack([mo.md(t_ui("select_verbs", language_selector.value)), table_verb])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu, language_selector, mo, t_ui):
    _lang = language_selector.value
    _b1_tenses = ['present', 'past_continuous', 'aorist', 'future', 'future_continuous']
    _opts = {label: key for label, key in gu.tense_dropdown_options(_lang).items() if key in _b1_tenses}
    _default = next(label for label, key in gu.tense_dropdown_options(_lang).items() if key == 'present')
    tense_selector = mo.ui.dropdown(options=_opts, value=_default, label=t_ui("tense_label", _lang))
    tense_selector
    return (tense_selector,)


@app.cell(hide_code=True)
def _(eee, gu, mo, random, session_total_v, set_session_total_v, table_verb):
    words_verb = gu.get_words(table_verb)
    words4test_verb, set_words4test_verb = mo.state(words_verb.copy() if words_verb else [])
    if words_verb and len(words_verb) > session_total_v():
        set_session_total_v(len(words_verb))
    elif not words_verb:
        set_session_total_v(0)
    verb_msg, set_verb_msg = mo.state("")
    captured_verb, set_captured_verb = mo.state(None)
    cv_verb, set_cv_verb = mo.state(None)
    _clk = eee.increment_counter
    skip_button_v = mo.ui.button(label="Skip", on_click=_clk)
    clear_button_v = mo.ui.button(label="Clear", on_click=_clk)
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
    verb_fields, _ = gu.create_verb_test_ui(_ui_label, words_verb, words4test_verb(), _cv, _tense_key)
    return (verb_fields,)


@app.cell(hide_code=True)
def _(captured_verb, eee, mo, set_submit_count_v, tense_selector, verb_fields):
    _values = verb_fields.value if verb_fields is not None else []
    _snap = captured_verb()
    _has_input = bool(_values and any(v.strip() for v in _values))
    _matches_snap = (
        _snap is not None
        and getattr(_snap, 'tense', None) == tense_selector.value
        and [v.strip() for v in _values] == [v.strip() for v in (_snap.value or [])]
    )
    _dirty = _has_input and not _matches_snap
    _clk = eee.increment_counter
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
    _lang = language_selector.value
    _cv = cv_verb()
    if not words4test_verb():
        _view_verb = mo.md(t_ui("verb_empty", _lang))
    elif not tense_selector.value:
        _view_verb = mo.md(t_ui("verb_no_tense", _lang))
    else:
        _feedback_v = mo.md("")
        _c = captured_verb()
        if _cv and _c and getattr(_c, 'verb_word', None) == _cv['Word'] and getattr(_c, 'tense', None) == tense_selector.value:
            _, _msg = gu.check_verb_test(_cv['Word'], _c, tense_selector.value)
            _feedback_v = mo.md(_msg)
        _tense_key = tense_selector.value
        _label = gu.TENSE_LABELS.get(_tense_key, {}).get('label', {}).get(_lang, _tense_key)
        _items = [mo.md(t_ui("verb_test_heading", _lang).format(label=_label, count=len(words4test_verb()), total=session_total_v()))]
        if verb_msg():
            _items.append(mo.md(verb_msg()))
        _items += [
            mo.md(f"{t_ui('translation_label', _lang)} **{_cv['Translation']}**") if _cv else mo.md(""),
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
    random,
    session_total_v,
    set_captured_verb,
    set_cv_verb,
    set_tbl_sel_v,
    set_verb_msg,
    set_words4test_verb,
    t_ui,
    tense_selector,
    words4test_verb,
):
    _lang = language_selector.value
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
            set_verb_msg(t_ui("verb_passed", _lang).format(word=_cv['Word'], trans=_cv['Translation'], remaining=len(_new), total=session_total_v()))
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
        if _cv and verb_fields is not None:
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
def _(language_selector, mo, t_ui):
    mo.md(t_ui("adjectives_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    tbl_sel_a, set_tbl_sel_a = mo.state(None)
    session_total_a, set_session_total_a = mo.state(0)
    return session_total_a, set_session_total_a, set_tbl_sel_a, tbl_sel_a


@app.cell(hide_code=True)
def _(mo):
    file_upload_adj = mo.ui.file(label="Upload adjectives TSV")
    file_upload_adj
    return (file_upload_adj,)


@app.cell(hide_code=True)
def _(RAW_BASE, file_upload_adj, gu, notebook_dir):
    df_adj = gu.load_vocab_table("adjectives.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE, file_upload=file_upload_adj)
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, gu, language_selector, mo, t_ui, tbl_sel_a):
    table_adj = gu.vocab_table(df_adj, select_state=tbl_sel_a)
    mo.vstack([mo.md(t_ui("select_adjs", language_selector.value)), table_adj])
    return (table_adj,)


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    _lang = language_selector.value
    if _lang == "ru":
        _opts = {
            "Простой: 3 рода × 2 числа (6 полей)": "simple",
            "Полный: все роды, числа и падежи (18 полей)": "complex",
        }
        _default_mode = "Простой: 3 рода × 2 числа (6 полей)"
    elif _lang == "el":
        _opts = {
            "Απλό: 3 γένη × 2 αριθμοί (6 πεδία)": "simple",
            "Πλήρες: όλα τα γένη, αριθμοί και πτώσεις (18 πεδία)": "complex",
        }
        _default_mode = "Απλό: 3 γένη × 2 αριθμοί (6 πεδία)"
    else:
        _opts = {
            "Simple: 3 genders × 2 numbers (6 fields)": "simple",
            "Full: all genders, numbers and cases (18 fields)": "complex",
        }
        _default_mode = "Simple: 3 genders × 2 numbers (6 fields)"
    mode_selector = mo.ui.radio(options=_opts, value=_default_mode, label=t_ui("mode_label", _lang))
    mo.md(f"{mode_selector}")
    return (mode_selector,)


@app.cell(hide_code=True)
def _(eee, gu, mo, random, session_total_a, set_session_total_a, table_adj):
    adj_words = gu.get_words(table_adj)
    words4test_adj, set_words4test_adj = mo.state(adj_words.copy() if adj_words else [])
    if adj_words and len(adj_words) > session_total_a():
        set_session_total_a(len(adj_words))
    elif not adj_words:
        set_session_total_a(0)
    adj_last_passed_mesg, set_adj_last_passed_mesg = mo.state("")
    adj_cv, set_adj_cv = mo.state(None)
    captured_adj, set_captured_adj = mo.state(None)
    _clk = eee.increment_counter
    skip_button_a = mo.ui.button(label="Skip", on_click=_clk)
    clear_button_a = mo.ui.button(label="Clear", on_click=_clk)
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
def _(adj_form, captured_adj, eee, mo, set_submit_count_a):
    _values = adj_form.value if adj_form is not None else []
    _snap = captured_adj()
    _has_input = bool(_values and any(v.strip() for v in _values))
    _matches_snap = _snap is not None and [v.strip() for v in _values] == [v.strip() for v in (_snap.value or [])]
    _dirty = _has_input and not _matches_snap
    _clk = eee.increment_counter
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
    _lang = language_selector.value
    _adj = adj_cv()
    if words4test_adj() and _adj:
        _feedback_a = mo.md("")
        _c = captured_adj()
        if _c and getattr(_c, 'adj_word', None) == _adj['Word']:
            _, _msg = gu.check_adjective_test(_adj['Word'], _c, mode=mode_selector.value)
            if _msg:
                _feedback_a = mo.md(_msg)
        _view_adj = mo.vstack([
            mo.md(t_ui("adj_test_heading", _lang).format(count=len(words4test_adj()), total=session_total_a())),
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
            set_adj_last_passed_mesg(t_ui("adj_passed", _lang).format(word=_adj['Word'], trans=_adj['Translation'], remaining=len(_new), total=session_total_a()))
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
    UI_STRINGS = {
        "en": {
            "nouns_heading": "## NOUNS",
            "verbs_heading": "## VERBS",
            "adjectives_heading": "## ADJECTIVES",
            "select_nouns": "### Select nouns to practice",
            "select_verbs": "### Select verbs to practice",
            "select_adjs": "### Select adjectives to practice",
            "translation_label": "Translation:",
            "simple_noun_test": "**Simple noun test** ({count}/{total})",
            "article_noun_test": "**Noun test with articles** ({count}/{total})",
            "verb_test_heading": "**Verb test — {label}** ({count}/{total})",
            "adj_test_heading": "**Test: Adjective declension** ({count}/{total})",
            "noun_empty": "_Select nouns from the table above._",
            "verb_empty": "_Select verbs from the table above._",
            "verb_no_tense": "_Select a tense above._",
            "adj_empty": "_Select adjectives from the table above._",
            "tense_label": "Select tense:",
            "mode_label": "Test mode:",
            "noun_passed": '<span style="color:green;">Test for <b>"{word}"</b> passed.\n\n{remaining} words remaining out of {total}.</span>',
            "verb_passed": '<span style="color:green;">Test for <b>"{word} — {trans}"</b> passed.\n\n{remaining} words remaining out of {total}.</span>',
            "adj_passed":  '<span style="color:green;">Test for <b>"{word} — {trans}"</b> passed.\n\n{remaining} words remaining out of {total}.</span>',
        },
        "ru": {
            "nouns_heading": "## СУЩЕСТВИТЕЛЬНЫЕ",
            "verbs_heading": "## ГЛАГОЛЫ",
            "adjectives_heading": "## ПРИЛАГАТЕЛЬНЫЕ",
            "select_nouns": "### Выберите существительные для практики",
            "select_verbs": "### Выберите глаголы для практики",
            "select_adjs": "### Выберите прилагательные для практики",
            "translation_label": "Перевод:",
            "simple_noun_test": "**Простой тест: Существительные** ({count}/{total})",
            "article_noun_test": "**Тест с артиклями: Существительные** ({count}/{total})",
            "verb_test_heading": "**Тест глагола — {label}** ({count}/{total})",
            "adj_test_heading": "**Тест: Склонение прилагательного** ({count}/{total})",
            "noun_empty": "_Выберите существительные из таблицы выше._",
            "verb_empty": "_Выберите глаголы из таблицы выше._",
            "verb_no_tense": "_Выберите время выше._",
            "adj_empty": "_Выберите прилагательные из таблицы выше._",
            "tense_label": "Выбрать время:",
            "mode_label": "Режим теста:",
            "noun_passed": '<span style="color:green;">Тест для <b>"{word}"</b> пройден.\n\n{remaining} слов осталось из {total}.</span>',
            "verb_passed": '<span style="color:green;">Тест для <b>"{word} — {trans}"</b> пройден.\n\n{remaining} слов осталось из {total}.</span>',
            "adj_passed":  '<span style="color:green;">Тест для <b>"{word} — {trans}"</b> пройден.\n\n{remaining} слов осталось из {total}.</span>',
        },
        "el": {
            "nouns_heading": "## ΟΥΣΙΑΣΤΙΚΑ",
            "verbs_heading": "## ΡΗΜΑΤΑ",
            "adjectives_heading": "## ΕΠΙΘΕΤΑ",
            "select_nouns": "### Επιλέξτε ουσιαστικά για εξάσκηση",
            "select_verbs": "### Επιλέξτε ρήματα για εξάσκηση",
            "select_adjs": "### Επιλέξτε επίθετα για εξάσκηση",
            "translation_label": "Μετάφραση:",
            "simple_noun_test": "**Απλό τεστ: Ουσιαστικά** ({count}/{total})",
            "article_noun_test": "**Τεστ με άρθρο: Ουσιαστικά** ({count}/{total})",
            "verb_test_heading": "**Τεστ ρήματος — {label}** ({count}/{total})",
            "adj_test_heading": "**Τεστ: Κλίση επιθέτου** ({count}/{total})",
            "noun_empty": "_Επιλέξτε ουσιαστικά από τον πίνακα παραπάνω._",
            "verb_empty": "_Επιλέξτε ρήματα από τον πίνακα παραπάνω._",
            "verb_no_tense": "_Επιλέξτε χρόνο παραπάνω._",
            "adj_empty": "_Επιλέξτε επίθετα από τον πίνακα παραπάνω._",
            "tense_label": "Επιλέξτε χρόνο:",
            "mode_label": "Λειτουργία τεστ:",
            "noun_passed": '<span style="color:green;">Τεστ για <b>"{word}"</b> ολοκληρώθηκε.\n\n{remaining} λέξεις απομένουν από {total}.</span>',
            "verb_passed": '<span style="color:green;">Τεστ για <b>"{word} — {trans}"</b> ολοκληρώθηκε.\n\n{remaining} λέξεις απομένουν από {total}.</span>',
            "adj_passed":  '<span style="color:green;">Τεστ για <b>"{word} — {trans}"</b> ολοκληρώθηκε.\n\n{remaining} λέξεις απομένουν από {total}.</span>',
        },
    }

    def t_ui(key, lang=None):
        _l = lang if lang else "el"
        return UI_STRINGS.get(_l, UI_STRINGS["el"]).get(key, UI_STRINGS["el"].get(key, key))

    return (t_ui,)


@app.cell(hide_code=True)
def _(mo):
    from eee_project import language_bridge
    lang_bridge = language_bridge(mo)
    lang_bridge
    return (lang_bridge,)


@app.cell(hide_code=True)
def _(lang_bridge, mo):
    # Fixed-position language selector overlay
    from eee_project import language_selector as _language_selector
    language_selector = _language_selector(mo, lang_bridge, default="el")
    mo.Html(f"""
    <div style="position: fixed; top: 60px; right: 10px; z-index: 1000; background: white; padding: 8px 12px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
        {language_selector}
    </div>
    """)
    return (language_selector,)


@app.cell(hide_code=True)
def _(lang_bridge, language_selector):
    from eee_project import save_language_selection
    save_language_selection(lang_bridge, language_selector)
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    from eee_project import ConfigStore as _ConfigStore
    from eee_project.notebook_utils import eee_footer
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _cfg = _ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/modern_greek/b1greeklanguageandculture/zorba/index.tsv",
    )
    _prev_url, _next_url = _cfg.adjacent_urls("26_06_26/")
    eee_footer(mo, lang=language_selector.value, prev_url=_prev_url, next_url=_next_url, same_window=True)
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
    RAW_BASE = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/modern_greek/b1greeklanguageandculture/zorba/26_06_26"
    return RAW_BASE, eee, gu, mo, notebook_dir, random


if __name__ == "__main__":
    app.run()
