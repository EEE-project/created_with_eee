# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project>=1.22.0",
#     "marimo>=0.25.1",
#     "modern-greek-backend-eee>=1.0.0",
#     "pandas",
# ]
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Καβάφης — Ιθάκη — Μάθημα 4: Η Ιθάκη σ' έδωσε τ' ωραίο ταξίδι")


@app.cell(hide_code=True)
def _(language_selector, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    cfg = ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/modern_greek/b1greeklanguageandculture/kavafis_ithaki/index.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=cfg.index_url(), lang=language_selector.value, titles={
        "ru": "Καβάφης — Ιθάκη", "el": "Καβάφης — Ιθάκη", "en": "Kavafis — Ithaki",
    }, ga_config=cfg.ga_config(), same_window=True)
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Title + subtitle (no dedicated painting: this lesson has no source lecture)
    _lang = language_selector.value
    _heading = mo.md("# C. P. Cavafy — «Ithaki»") if _lang == "en" else mo.md("# Κ. Π. Καβάφης — «Ιθάκη»")
    if _lang == "ru":
        _subtitle = mo.md("Четвёртый урок из цикла о стихотворении Константиноса Кавафиса «Итака» (1911): заключительные строфы — Итака как цель и как путь — и общий разбор поэтического языка стихотворения.")
    elif _lang == "el":
        _subtitle = mo.md("Τέταρτο μάθημα από τον κύκλο μαθημάτων για το ποίημα του Κ. Π. Καβάφη «Ιθάκη» (1911): οι τελευταίες στροφές — η Ιθάκη ως προορισμός και ως ταξίδι — και μια γενική ανάλυση της ποιητικής γλώσσας του ποιήματος.")
    else:
        _subtitle = mo.md("Fourth lesson in the series on Constantine P. Cavafy's poem «Ithaka» (1911): the closing stanzas — Ithaka as destination and as journey — and a general analysis of the poem's poetic language.")
    mo.vstack([_heading, _subtitle])
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Recap of lesson 3
    _lang = language_selector.value
    _text = {
        "ru": r"""
            ## Повторение

            На прошлом уроке мы собирали сокровища для пути: финикийские товары —
            перламутр, кораллы, янтарь, чёрное дерево, благовония — и мудрость
            египетских городов: учиться и учиться.
            """,
        "el": r"""
            ## Επανάληψη

            Στο προηγούμενο μάθημα μαζέψαμε θησαυρούς για το ταξίδι: τα φοινικικά
            εμπορεύματα — σεντέφια, κοράλλια, κεχριμπάρια, έβενο, μυρωδικά — και τη
            σοφία των αιγυπτιακών πόλεων: να μάθεις και να μάθεις.
            """,
    }.get(_lang, r"""
        ## Review

        In the previous lesson we gathered treasures for the journey: Phoenician
        goods — mother-of-pearl, coral, amber, ebony, perfumes — and the wisdom
        of the Egyptian cities: to learn and to learn.
        """)
    mo.md(_text)
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Discussion warm-up: the destination or the journey?
    _lang = language_selector.value
    _text = {
        "ru": r"""
            ## Что важнее: цель или путь?

            Подумайте и обсудите:

            - Какую «Итаку» вы держите в уме?
            - Что дала вам дорога такого, чего не дала бы сама цель?
            - Как вы понимаете слова «Итака тебя не обманула»?
            """,
        "el": r"""
            ## Τι μετράει περισσότερο: ο προορισμός ή το ταξίδι;

            Σκεφτείτε και συζητήστε:

            - Ποια «Ιθάκη» έχετε στον νου σας;
            - Τι σας έδωσε ο δρόμος που δεν θα σας έδινε ο ίδιος ο προορισμός;
            - Πώς καταλαβαίνετε τα λόγια «δεν σε γέλασε»;
            """,
    }.get(_lang, r"""
        ## What matters more: the destination or the journey?

        Think and discuss:

        - Which «Ithaka» do you keep in mind?
        - What did the road give you that the destination itself could not?
        - What do you make of the words «Ithaka did not deceive you»?
        """)
    mo.md(_text)
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Poem section heading
    mo.md(t_ui("poem_section_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    _CITATION = (
        '<b>Κ. Π. Καβάφης, «Ιθάκη»</b> (1911). Τρίτη, τέταρτη και πέμπτη στροφή, στίχοι 24–36. '
        '<a href="https://www.greek-language.gr/digitalResources/literature/tools/concordance/browse.html?cnd_id=9&text_id=658" target="_blank" rel="noopener">greek-language.gr — Πύλη για την ελληνική γλώσσα</a>'
    )
    mo.md(_CITATION)
    return


@app.cell(hide_code=True)
def _(TRANS_DESC, language_selector, mo, trans_selector):
    _PODSTROCHNIK_DESC = "**подстрочник** · буквальный перевод слово-в-слово с сохранением порядка оригинала"
    _desc_map = {"подстрочник": _PODSTROCHNIK_DESC, **TRANS_DESC}
    # English: add the pointer to the in-copyright Keeley/Sherrard version (a description-only section).
    _note = TRANS_DESC.get("Keeley/Sherrard", "") if language_selector.value == "en" else ""
    mo.md("\n\n".join(_d for _d in (_desc_map.get(trans_selector.value, ""), _note) if _d))
    return


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, notebook_dir):
    MIX_ROWS = gu2.load_language_notes(nb_dir=notebook_dir, remote_base=RAW_BASE)
    return (MIX_ROWS,)


@app.cell(hide_code=True)
def _(MIX_ROWS, STANZAS, eee, gu2, language_selector, mo, trans_selector):
    _lang = language_selector.value
    mo.vstack([trans_selector, eee.mixed_language_notes(
        mo, stanzas=STANZAS, translator=trans_selector.value, notes=MIX_ROWS, lang=_lang,
        heading=gu2.ui_label("mixed_language_heading", _lang), hint=gu2.ui_label("mixed_language_hint", _lang),
    )])
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Analysis: what the last stanzas say, the poem read aloud
    _lang = language_selector.value
    _texts = {
        "ru": (
            r"""
            ## Что говорят последние строфы

            **Строфа 3 (στ. 24–30).** Держи Итаку в уме — она твоя цель. Но не торопи
            путешествие: пусть оно длится много лет, чтобы ты пристал к острову стариком,
            богатым тем, что приобрёл в пути, и не ждал богатств от самой Итаки.

            **Строфа 4 (στ. 31–33).** Итака уже дала тебе прекрасное путешествие:
            без неё ты не вышел бы в путь. Больше ей дать нечего.

            **Строфа 5 (στ. 34–36).** Даже найдя Итаку бедной, ты не обманут: ты стал
            мудрым, у тебя столько опыта, что ты уже понял, что значат «Итаки».

            ### Почему «Итаки» во множественном числе?

            Стихотворение начинается с одной Итаки — острова из «Одиссеи». В конце слово
            стоит во множественном числе: «Итаки» — это уже не один остров, а любые цели,
            к которым мы идём. Одно из прочтений: важно не только прийти, но и то, что мы
            приобретаем в пути.

            ### Как построено стихотворение

            Страх → путешествие → опыт → мудрость → общий смысл:

            - урок 1 (στ. 1–3): отправление и пожелание долгого пути;
            - урок 2 (στ. 4–12): страхи — Лестригоны, Циклопы, Посейдон;
            - урок 3 (στ. 13–23): само путешествие и знания;
            - урок 4 (στ. 24–36): цель, результат и вывод.
            """,
            r"""
            ## «Итака» вслух и в музыке

            Стихотворение читают актёры и поэты, а на его текст есть ещё и музыкальная пьеса.
            Послушайте и сравните с текстом (ссылки на YouTube; записи здесь не копируются):

            **На греческом**
            
            - <a href="https://www.youtube.com/watch?v=r5lPCeT8Ex0" target="_blank" rel="noopener">ΙΘΑΚΗ - Κ.Π. ΚΑΒΑΦΗΣ- ΓΡΗΓΟΡΗΣ ΒΑΛΤΙΝΟΣ</a> — 1969anre, 2012
            - <a href="https://www.youtube.com/watch?v=IgbQAGAGQc0" target="_blank" rel="noopener">Κωνσταντίνος Καβάφης - Ιθάκη 1911 - Official Audio Release</a> — Ελληνική Ποίηση &amp; Θέατρο, 2019
            
            **На английском**
            
            - <a href="https://www.youtube.com/watch?v=i8is5ZE4_CU" target="_blank" rel="noopener">Sean Connery reads ITHAKA | Powerful Life Poem by C.P.Cavafy</a> — Upgrade Your Mindset, 2021
            - <a href="https://www.youtube.com/watch?v=U4D06vLQf5o" target="_blank" rel="noopener">"Ithaka" by C P Cavafy (read by Tom O'Bedlam)</a> — SpokenVerse, 2011
            
            **На русском**
            
            - <a href="https://www.youtube.com/watch?v=RN_SJgOu0EI" target="_blank" rel="noopener">ИТАКА. Константинос Кавафис.  Читает Ирина Ковалевская. Аудио-версия.</a> — Irina Kovalevskaja, 2023
            - <a href="https://www.youtube.com/watch?v=SrOxrgpEDLM" target="_blank" rel="noopener">Павел Курочкин читает Константиноса Кавафиса</a> — Eugenia Kritsevskagia, 2018
            - <a href="https://www.youtube.com/watch?v=3xUIztEwrqQ" target="_blank" rel="noopener">8 серия.  Итака.  Константинос Кавафис</a> — Херсонес Таврический в Севастополе, 2021
            
            **Музыка**
            
            - <a href="https://www.youtube.com/watch?v=4nHqjy65n6I" target="_blank" rel="noopener">Deep Pressed ft. 'Ελλη Λαμπέτη - Ιθάκη (Κ.Π.Καβάφης)</a> — Deep Pressed, 2018
            """,
        ),
        "el": (
            r"""
            ## Τι λένε οι τελευταίες στροφές

            **Τρίτη στροφή (στ. 24–30).** Να έχεις πάντα την Ιθάκη στον νου σου — είναι ο
            προορισμός σου. Μη βιάζεσαι όμως: καλύτερα το ταξίδι να κρατήσει πολλά χρόνια,
            για να αράξεις στο νησί ως γέρος, πλούσιος με όσα κέρδισες στον δρόμο, χωρίς να
            περιμένεις πλούτη από την Ιθάκη.

            **Τέταρτη στροφή (στ. 31–33).** Η Ιθάκη σου έδωσε ήδη το όμορφο ταξίδι —
            χωρίς αυτήν δεν θα είχες βγει στον δρόμο. Άλλο δεν έχει να σου δώσει πια.

            **Πέμπτη στροφή (στ. 34–36).** Ακόμη κι αν τη βρεις φτωχική, η Ιθάκη δεν σε
            γέλασε: έγινες σοφός, με τόση πείρα, και κατάλαβες ήδη τι σημαίνουν οι Ιθάκες.

            ### Γιατί «οι Ιθάκες» στον πληθυντικό;

            Το ποίημα ξεκινά με μία Ιθάκη — το νησί της «Οδύσσειας». Στο τέλος η λέξη
            βρίσκεται στον πληθυντικό: οι Ιθάκες δεν είναι πια ένα νησί, αλλά όλοι οι στόχοι
            προς τους οποίους ταξιδεύουμε. Μία από τις αναγνώσεις: δεν μετράει μόνο η
            άφιξη, αλλά και όσα αποκτούμε στον δρόμο.

            ### Πώς είναι χτισμένο το ποίημα

            Φόβος → ταξίδι → πείρα → σοφία → γενικό νόημα:

            - μάθημα 1 (στ. 1–3): η αναχώρηση και η ευχή για μακρύ δρόμο·
            - μάθημα 2 (στ. 4–12): οι φόβοι — Λαιστρυγόνες, Κύκλωπες, Ποσειδώνας·
            - μάθημα 3 (στ. 13–23): το ίδιο το ταξίδι και η γνώση·
            - μάθημα 4 (στ. 24–36): ο προορισμός, το αποτέλεσμα και το συμπέρασμα.
            """,
            r"""
            ## Η «Ιθάκη» φωναχτά και με μουσική

            Το ποίημα το έχουν διαβάσει ηθοποιοί και ποιητές· υπάρχει και ένα μουσικό κομμάτι
            πάνω στο κείμενό του. Ακούστε και συγκρίνετε με το κείμενο (σύνδεσμοι προς το
            YouTube· οι ηχογραφήσεις δεν αντιγράφονται):

            **Στα ελληνικά**
            
            - <a href="https://www.youtube.com/watch?v=r5lPCeT8Ex0" target="_blank" rel="noopener">ΙΘΑΚΗ - Κ.Π. ΚΑΒΑΦΗΣ- ΓΡΗΓΟΡΗΣ ΒΑΛΤΙΝΟΣ</a> — 1969anre, 2012
            - <a href="https://www.youtube.com/watch?v=IgbQAGAGQc0" target="_blank" rel="noopener">Κωνσταντίνος Καβάφης - Ιθάκη 1911 - Official Audio Release</a> — Ελληνική Ποίηση &amp; Θέατρο, 2019
            
            **Στα αγγλικά**
            
            - <a href="https://www.youtube.com/watch?v=i8is5ZE4_CU" target="_blank" rel="noopener">Sean Connery reads ITHAKA | Powerful Life Poem by C.P.Cavafy</a> — Upgrade Your Mindset, 2021
            - <a href="https://www.youtube.com/watch?v=U4D06vLQf5o" target="_blank" rel="noopener">"Ithaka" by C P Cavafy (read by Tom O'Bedlam)</a> — SpokenVerse, 2011
            
            **Στα ρωσικά**
            
            - <a href="https://www.youtube.com/watch?v=RN_SJgOu0EI" target="_blank" rel="noopener">Irina Kovalevskaya — audio reading</a> — Irina Kovalevskaja, 2023
            - <a href="https://www.youtube.com/watch?v=SrOxrgpEDLM" target="_blank" rel="noopener">Pavel Kurochkin — reading</a> — Eugenia Kritsevskagia, 2018
            - <a href="https://www.youtube.com/watch?v=3xUIztEwrqQ" target="_blank" rel="noopener">«My Chersonesos» poetry series, episode 8</a> — Chersonesos Taurica, Sevastopol, 2021
            
            **Μουσική**
            
            - <a href="https://www.youtube.com/watch?v=4nHqjy65n6I" target="_blank" rel="noopener">Deep Pressed ft. 'Ελλη Λαμπέτη - Ιθάκη (Κ.Π.Καβάφης)</a> — Deep Pressed, 2018
            """,
        ),
    }.get(_lang, (
        r"""
        ## What the last stanzas say

        **Stanza 3 (στ. 24–30).** Always keep Ithaka in mind — it is your destination.
        But do not hurry the journey: better that it lasts many years, so that you moor at
        the island as an old man, rich with all you gained on the way, not expecting
        Ithaka to give you riches.

        **Stanza 4 (στ. 31–33).** Ithaka has already given you the beautiful journey:
        without her you would not have set out. She has nothing more to give.

        **Stanza 5 (στ. 34–36).** Even if you find her poor, Ithaka has not deceived you:
        you have become wise, with so much experience, that you will already have
        understood what the Ithakas mean.

        ### Why «Ithakas» in the plural?

        The poem begins with one Ithaka — the island of the «Odyssey». At the end the word
        is plural: «Ithakas» are no longer one island but all the goals we travel towards.
        One reading: it is not only the arrival that counts, but also what we gain on the
        way.

        ### How the poem is built

        Fear → journey → experience → wisdom → general meaning:

        - lesson 1 (στ. 1–3): setting out, and the wish for a long road;
        - lesson 2 (στ. 4–12): the fears — Laestrygonians, Cyclopes, Poseidon;
        - lesson 3 (στ. 13–23): the journey itself and learning;
        - lesson 4 (στ. 24–36): the destination, the result and the conclusion.
        """,
        r"""
        ## «Ithaka» read aloud and in music

        Actors and poets have recorded the poem, and there is also a piece of music on its
        text. Listen and compare with the text (links to YouTube; the recordings are not
        copied here):

        **In Greek**
        
        - <a href="https://www.youtube.com/watch?v=r5lPCeT8Ex0" target="_blank" rel="noopener">ΙΘΑΚΗ - Κ.Π. ΚΑΒΑΦΗΣ- ΓΡΗΓΟΡΗΣ ΒΑΛΤΙΝΟΣ</a> — 1969anre, 2012
        - <a href="https://www.youtube.com/watch?v=IgbQAGAGQc0" target="_blank" rel="noopener">Κωνσταντίνος Καβάφης - Ιθάκη 1911 - Official Audio Release</a> — Ελληνική Ποίηση &amp; Θέατρο, 2019
        
        **In English**
        
        - <a href="https://www.youtube.com/watch?v=i8is5ZE4_CU" target="_blank" rel="noopener">Sean Connery reads ITHAKA | Powerful Life Poem by C.P.Cavafy</a> — Upgrade Your Mindset, 2021
        - <a href="https://www.youtube.com/watch?v=U4D06vLQf5o" target="_blank" rel="noopener">"Ithaka" by C P Cavafy (read by Tom O'Bedlam)</a> — SpokenVerse, 2011
        
        **In Russian**
        
        - <a href="https://www.youtube.com/watch?v=RN_SJgOu0EI" target="_blank" rel="noopener">Irina Kovalevskaya — audio reading</a> — Irina Kovalevskaja, 2023
        - <a href="https://www.youtube.com/watch?v=SrOxrgpEDLM" target="_blank" rel="noopener">Pavel Kurochkin — reading</a> — Eugenia Kritsevskagia, 2018
        - <a href="https://www.youtube.com/watch?v=3xUIztEwrqQ" target="_blank" rel="noopener">«My Chersonesos» poetry series, episode 8</a> — Chersonesos Taurica, Sevastopol, 2021
        
        **In music**
        
        - <a href="https://www.youtube.com/watch?v=4nHqjy65n6I" target="_blank" rel="noopener">Deep Pressed ft. 'Ελλη Λαμπέτη - Ιθάκη (Κ.Π.Καβάφης)</a> — Deep Pressed, 2018
        """,
    ))
    mo.vstack([mo.md(_t) for _t in _texts])
    return


@app.cell(hide_code=True)
def _(PRESENCE_SHOWN, language_selector, mo, t_ui):
    # Test 1 heading -- presence exercise leads (poem-specific, right after the poem)
    mo.stop(not PRESENCE_SHOWN)
    _lang = language_selector.value
    mo.md(f"## {t_ui('test_label', _lang)} 1: {t_ui('presence_test_topic', _lang)}")
    return


@app.cell(hide_code=True)
def _(mo):
    tp_cv, tp_set_cv = mo.state(None)
    tp_score, tp_set_score = mo.state({"correct": 0, "total": 0})
    tp_remaining, tp_set_remaining = mo.state(None)
    tp_history, tp_set_history = mo.state([])
    tp_future, tp_set_future = mo.state([])
    tp_restore_entry, tp_set_restore_entry = mo.state(None)
    return (
        tp_cv,
        tp_future,
        tp_history,
        tp_remaining,
        tp_restore_entry,
        tp_score,
        tp_set_cv,
        tp_set_future,
        tp_set_history,
        tp_set_remaining,
        tp_set_restore_entry,
        tp_set_score,
    )


@app.cell(hide_code=True)
def _(gu2, language_selector):
    tp_renew_btn = gu2.make_renew_button(lang=language_selector.value)
    return (tp_renew_btn,)


@app.cell(hide_code=True)
def _():
    # Shared per-lesson default (the same cell as in the Odyssey lessons): how many items the exercise below draws per
    # session -- here the word-in-translation test: half "yes", half "no" where the answer key has enough "no" rows.
    # Change this one value to change the session, or override the exercise by editing its own n=SESSION_SIZE argument.
    SESSION_SIZE = 10
    return (SESSION_SIZE,)


@app.cell(hide_code=True)
def _(
    POEM_WORDS_RAW,
    RAW_BASE,
    SESSION_SIZE,
    STANZAS,
    eee,
    gu2,
    language_selector,
    notebook_dir,
    tp_renew_btn,
    tp_set_cv,
    tp_set_future,
    tp_set_history,
    tp_set_remaining,
    tp_set_restore_entry,
    tp_set_score,
):
    # English: Valassopoulo is the only published English translation reproduced (the literal rendering is the crib, like подстрочник)
    LITERARY_TRANSLATORS = ["Valassopoulo"] if language_selector.value == "en" else ["Шмаков/Бродский", "Ильинская", "Левитов"]
    _tp_vocab = [w for w in POEM_WORDS_RAW if w.get("pos") in eee.TRANSLATION_PRESENCE_CONTENT_POS]
    _tp_path = gu2.ensure_file("translation_presence.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
    # An empty TP_ITEMS list on its own is indistinguishable downstream from
    # "quiz genuinely completed" (both leave translation_presence_widgets
    # with no current item, i.e. the same done-screen) -- TP_UNAVAILABLE
    # lets the rendering cell show an honest not-found message instead,
    # matching how the noun/verb/adjective sections already handle a
    # missing TSV.
    TP_UNAVAILABLE = _tp_path is None
    if _tp_path:
        gu2.sync_translation_presence_tsv(_tp_vocab, LITERARY_TRANSLATORS, STANZAS, _tp_path)
        TP_ITEMS = gu2.balance_presence_items(gu2.build_translation_presence_items(
            gu2.read_translation_presence_tsv(_tp_path), POEM_WORDS_RAW, STANZAS, valid_translators=LITERARY_TRANSLATORS
        ), n=SESSION_SIZE)
    else:
        TP_ITEMS = []
    gu2.reset_quiz_state(tp_renew_btn, tp_set_cv, tp_set_remaining, tp_set_score,
                          tp_set_history, tp_set_future, tp_set_restore_entry)
    return TP_ITEMS, TP_UNAVAILABLE


@app.cell(hide_code=True)
def _(
    TP_ITEMS,
    gu2,
    language_selector,
    tp_cv,
    tp_history,
    tp_remaining,
    tp_restore_entry,
):
    _ = tp_cv()
    tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch = gu2.translation_presence_widgets(
        cv=tp_cv(),
        remaining=tp_remaining(),
        items=TP_ITEMS,
        restore_entry=tp_restore_entry(),
        history_len=len(tp_history()),
        lang=language_selector.value,
    )
    return tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch


@app.cell(hide_code=True)
def _(
    PRESENCE_SHOWN,
    TP_ITEMS,
    TP_UNAVAILABLE,
    gu2,
    language_selector,
    mo,
    t_ui,
    tp_choice_radio,
    tp_cv,
    tp_future,
    tp_history,
    tp_next_btn,
    tp_prev_btn,
    tp_remaining,
    tp_renew_btn,
    tp_restore_entry,
    tp_score,
    tp_set_cv,
    tp_set_future,
    tp_set_history,
    tp_set_remaining,
    tp_set_restore_entry,
    tp_set_score,
    tp_source_switch,
):
    mo.stop(not PRESENCE_SHOWN)
    if TP_UNAVAILABLE:
        _output = mo.md(t_ui("translation_presence_not_found", language_selector.value))
    else:
        _output = gu2.translation_presence_form(
            tp_cv, tp_set_cv, tp_remaining, tp_set_remaining,
            tp_score, tp_set_score, tp_restore_entry, tp_set_restore_entry,
            tp_history, tp_set_history, tp_future, tp_set_future,
            tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch,
            items=TP_ITEMS,
            lang=language_selector.value,
            renew_btn=tp_renew_btn,
        )
    _output
    return


@app.cell(hide_code=True)
def _(TEST_NUM, language_selector, mo, t_ui):
    # Test 2 heading
    _lang = language_selector.value
    mo.md(f"## {t_ui('test_label', _lang)} {TEST_NUM['noun']}: {t_ui('noun_test_topic', _lang)}")
    return


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, notebook_dir, vocab_name):
    # Load noun data
    df_noun = gu2.load_vocab_table(vocab_name("nouns"), nb_dir=notebook_dir, remote_base=RAW_BASE)
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, gu2, language_selector, mo, t_ui):
    # Noun table
    table_noun = gu2.vocab_table(df_noun)
    _lang = language_selector.value
    _table_noun = table_noun if table_noun is not None else mo.md(t_ui("nouns_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_nouns", _lang)), _table_noun])
    return (table_noun,)


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Noun mode selector
    _lang = language_selector.value
    if _lang == 'ru':
        _opts_n = {"без артикля": "simple", "с артиклем": "article"}
        _default_mode_n = "без артикля"
    elif _lang == 'el':
        _opts_n = {"χωρίς άρθρο": "simple", "με άρθρο": "article"}
        _default_mode_n = "χωρίς άρθρο"
    else:
        _opts_n = {"no article": "simple", "with article": "article"}
        _default_mode_n = "no article"
    mode_selector_n = mo.ui.radio(options=_opts_n, value=_default_mode_n, label=t_ui("mode_label", _lang))
    mo.md(f"{mode_selector_n}")
    return (mode_selector_n,)


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Noun indefinite-article toggle (creation only)
    indefinite_toggle_n = mo.ui.switch(label=t_ui("indefinite_label", language_selector.value), value=False)
    return (indefinite_toggle_n,)


@app.cell(hide_code=True)
def _(indefinite_toggle_n, mo, mode_selector_n):
    indefinite_toggle_n if mode_selector_n.value == "article" else mo.md("")
    return


@app.cell(hide_code=True)
def _(gu2, random, table_noun):
    # Noun words + state
    words_noun = gu2.get_words(table_noun)
    (words4test_noun, set_words4test_noun, hist_noun, set_hist_noun, noun_msg, set_noun_msg,
     captured_noun, set_captured_noun, entered_noun, set_entered_noun,
     submit_count_n, set_submit_count_n, prev_count_n, set_prev_count_n,
     next_count_n, set_next_count_n, enter_count_n, set_enter_count_n,
     restart_count_n, set_restart_count_n) = gu2.make_paradigm_drill_state(
        random.sample(words_noun, len(words_noun)) if words_noun else []
    )
    errors_noun, set_errors_noun, retry_count_n, set_retry_count_n = gu2.make_error_tracking_state()
    return (
        captured_noun,
        enter_count_n,
        entered_noun,
        errors_noun,
        hist_noun,
        next_count_n,
        noun_msg,
        prev_count_n,
        restart_count_n,
        retry_count_n,
        set_captured_noun,
        set_enter_count_n,
        set_entered_noun,
        set_errors_noun,
        set_hist_noun,
        set_next_count_n,
        set_noun_msg,
        set_prev_count_n,
        set_restart_count_n,
        set_retry_count_n,
        set_submit_count_n,
        set_words4test_noun,
        submit_count_n,
        words4test_noun,
        words_noun,
    )


@app.cell(hide_code=True)
def _(
    entered_noun,
    gu2,
    hist_noun,
    indefinite_toggle_n,
    language_selector,
    mode_selector_n,
    set_enter_count_n,
    set_next_count_n,
    set_prev_count_n,
    t_ui,
    words4test_noun,
):
    # Noun form
    cv_noun = words4test_noun()[0] if words4test_noun() else None
    noun_meta = gu2.noun_drill_meta(cv_noun["Word"]) if cv_noun else None
    _ac_noun = getattr(noun_meta, "active_cases", [])
    _entered_noun_form = entered_noun().get(cv_noun["Word"]) if cv_noun else None
    _lang_n = language_selector.value
    _article_n = mode_selector_n.value == "article"
    _indef_n = indefinite_toggle_n.value and _article_n
    _labels_noun = gu2.noun_slot_labels(_ac_noun, lang=_lang_n)
    if _article_n:
        _def_prefix = t_ui("def_prefix", _lang_n)
        _labels_noun = [f"{_def_prefix} {_l}" for _l in _labels_noun]
    if _indef_n:
        _indef_prefix = t_ui("indef_prefix", _lang_n)
        _labels_noun = _labels_noun + [f"{_indef_prefix} {_l}" for _l in gu2.noun_slot_labels(gu2.noun_indef_cells(_ac_noun), lang=_lang_n)]
    noun_form, prev_btn_n, next_btn_n, restart_btn_n = gu2.paradigm_drill_widgets(
        labels=_labels_noun,
        values=_entered_noun_form,
        history_len=len(hist_noun()),
        remaining_len=len(words4test_noun()),
        lang=_lang_n,
    )
    set_prev_count_n(0)
    set_next_count_n(0)
    set_enter_count_n(0)
    return cv_noun, next_btn_n, noun_form, noun_meta, prev_btn_n, restart_btn_n


@app.cell(hide_code=True)
def _(
    captured_noun,
    cv_noun,
    gu2,
    language_selector,
    noun_form,
    set_submit_count_n,
    t_ui,
):
    # Noun check button
    check_btn_n = gu2.dirty_check_button(
        noun_form, captured_noun, cv_noun, "test_word", word_key="Word",
        label=t_ui("check_label", language_selector.value),
    )
    set_submit_count_n(0)
    return (check_btn_n,)


@app.cell(hide_code=True)
def _(errors_noun, gu2, language_selector):
    # Noun retry-mistakes button
    retry_btn_n = gu2.retry_mistakes_button(errors_noun(), lang=language_selector.value)
    return (retry_btn_n,)


@app.cell(hide_code=True)
def _(
    captured_noun,
    check_btn_n,
    cv_noun,
    enter_count_n,
    entered_noun,
    errors_noun,
    gu2,
    hist_noun,
    indefinite_toggle_n,
    language_selector,
    mo,
    mode_selector_n,
    next_btn_n,
    next_count_n,
    noun_form,
    noun_meta,
    noun_msg,
    prev_btn_n,
    prev_count_n,
    restart_btn_n,
    restart_count_n,
    retry_btn_n,
    retry_count_n,
    set_captured_noun,
    set_enter_count_n,
    set_entered_noun,
    set_errors_noun,
    set_hist_noun,
    set_next_count_n,
    set_noun_msg,
    set_prev_count_n,
    set_restart_count_n,
    set_retry_count_n,
    set_submit_count_n,
    set_words4test_noun,
    submit_count_n,
    t_ui,
    words4test_noun,
    words_noun,
):
    # Noun drill
    _lang = language_selector.value
    _article = mode_selector_n.value == "article"
    _indef_n = indefinite_toggle_n.value and _article
    _title = t_ui("article_noun_heading", _lang) if _article else t_ui("simple_noun_heading", _lang)
    gu2.noun_paradigm_drill_form(
        words4test_noun, set_words4test_noun, hist_noun, set_hist_noun, noun_msg, set_noun_msg,
        captured_noun, set_captured_noun, entered_noun, set_entered_noun,
        submit_count_n, set_submit_count_n, prev_count_n, set_prev_count_n,
        next_count_n, set_next_count_n, enter_count_n, set_enter_count_n,
        restart_count_n, set_restart_count_n,
        cv_noun, noun_form, check_btn_n, prev_btn_n, next_btn_n, restart_btn_n,
        vocab=words_noun,
        noun_meta=noun_meta,
        article=_article,
        indefinite=_indef_n,
        word_key="Word",
        meaning_key="Translation",
        meaning_label=t_ui("translation_label", _lang).rstrip(":"),
        title=_title,
        done_message=t_ui("test1_done", _lang),
        get_errors=errors_noun, set_errors=set_errors_noun,
        get_retry_cnt=retry_count_n, set_retry_cnt=set_retry_count_n,
        retry_btn=retry_btn_n,
    ) if words_noun else mo.md(t_ui("noun_empty", _lang))
    return


@app.cell(hide_code=True)
def _(TEST_NUM, language_selector, mo, t_ui):
    # Test 3 heading
    _lang = language_selector.value
    mo.md(f"## {t_ui('test_label', _lang)} {TEST_NUM['verb']}: {t_ui('verb_test_topic', _lang)}")
    return


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, notebook_dir, vocab_name):
    # Load verb data
    df_verb = gu2.load_vocab_table(vocab_name("verbs"), nb_dir=notebook_dir, remote_base=RAW_BASE)
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, gu2, language_selector, mo, t_ui):
    # Verb table
    table_verb = gu2.vocab_table(df_verb)
    _lang = language_selector.value
    _table_verb = table_verb if table_verb is not None else mo.md(t_ui("verbs_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_verbs", _lang)), _table_verb])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu2, language_selector, mo, t_ui):
    # Tense selector
    _lang = language_selector.value
    _tense_options = gu2.tense_dropdown_options(lang=_lang)
    _first_key = next(iter(_tense_options))
    tense_selector = mo.ui.dropdown(
        options=_tense_options,
        value=_first_key,
        label=t_ui("tense_label", _lang),
    )
    tense_selector
    return (tense_selector,)


@app.cell(hide_code=True)
def _(gu2, random, table_verb):
    # Verb words + state
    words_verb = gu2.get_words(table_verb)
    (words4test_verb, set_words4test_verb, hist_verb, set_hist_verb, verb_msg, set_verb_msg,
     captured_verb, set_captured_verb, entered_verb, set_entered_verb,
     submit_count_v, set_submit_count_v, prev_count_v, set_prev_count_v,
     next_count_v, set_next_count_v, enter_count_v, set_enter_count_v,
     restart_count_v, set_restart_count_v) = gu2.make_paradigm_drill_state(
        random.sample(words_verb, len(words_verb)) if words_verb else []
    )
    errors_verb, set_errors_verb, retry_count_v, set_retry_count_v = gu2.make_error_tracking_state()
    return (
        captured_verb,
        enter_count_v,
        entered_verb,
        errors_verb,
        hist_verb,
        next_count_v,
        prev_count_v,
        restart_count_v,
        retry_count_v,
        set_captured_verb,
        set_enter_count_v,
        set_entered_verb,
        set_errors_verb,
        set_hist_verb,
        set_next_count_v,
        set_prev_count_v,
        set_restart_count_v,
        set_retry_count_v,
        set_submit_count_v,
        set_verb_msg,
        set_words4test_verb,
        submit_count_v,
        verb_msg,
        words4test_verb,
        words_verb,
    )


@app.cell(hide_code=True)
def _(
    entered_verb,
    gu2,
    hist_verb,
    language_selector,
    set_enter_count_v,
    set_next_count_v,
    set_prev_count_v,
    tense_selector,
    words4test_verb,
):
    # Verb form
    cv_verb = words4test_verb()[0] if words4test_verb() else None
    _entered_verb_form = entered_verb().get(cv_verb["Word"]) if cv_verb else None
    verb_meta = gu2.verb_drill_meta(cv_verb["Word"], tense_selector.value) if cv_verb and tense_selector.value else None
    verb_form, prev_btn_v, next_btn_v, restart_btn_v = gu2.paradigm_drill_widgets(
        labels=gu2.verb_slot_labels(verb_meta.active_slots if verb_meta else None),
        values=_entered_verb_form,
        history_len=len(hist_verb()),
        remaining_len=len(words4test_verb()),
        lang=language_selector.value,
    )
    set_prev_count_v(0)
    set_next_count_v(0)
    set_enter_count_v(0)
    return cv_verb, next_btn_v, prev_btn_v, restart_btn_v, verb_form, verb_meta


@app.cell(hide_code=True)
def _(
    captured_verb,
    cv_verb,
    gu2,
    language_selector,
    set_submit_count_v,
    t_ui,
    verb_form,
):
    # Verb check button
    check_btn_v = gu2.dirty_check_button(
        verb_form, captured_verb, cv_verb, "verb_word", word_key="Word",
        label=t_ui("check_label", language_selector.value),
    )
    set_submit_count_v(0)
    return (check_btn_v,)


@app.cell(hide_code=True)
def _(errors_verb, gu2, language_selector):
    # Verb retry-mistakes button
    retry_btn_v = gu2.retry_mistakes_button(errors_verb(), lang=language_selector.value)
    return (retry_btn_v,)


@app.cell(hide_code=True)
def _(
    captured_verb,
    check_btn_v,
    cv_verb,
    enter_count_v,
    entered_verb,
    errors_verb,
    gu2,
    hist_verb,
    language_selector,
    mo,
    next_btn_v,
    next_count_v,
    prev_btn_v,
    prev_count_v,
    restart_btn_v,
    restart_count_v,
    retry_btn_v,
    retry_count_v,
    set_captured_verb,
    set_enter_count_v,
    set_entered_verb,
    set_errors_verb,
    set_hist_verb,
    set_next_count_v,
    set_prev_count_v,
    set_restart_count_v,
    set_retry_count_v,
    set_submit_count_v,
    set_verb_msg,
    set_words4test_verb,
    submit_count_v,
    t_ui,
    tense_selector,
    verb_form,
    verb_meta,
    verb_msg,
    words4test_verb,
    words_verb,
):
    # Verb drill
    _lang = language_selector.value
    _tense_key = tense_selector.value
    if words_verb and _tense_key:
        _tlabel = gu2.TENSE_LABELS[_tense_key]["greek"]
        _output = gu2.verb_paradigm_drill_form(
            words4test_verb, set_words4test_verb, hist_verb, set_hist_verb, verb_msg, set_verb_msg,
            captured_verb, set_captured_verb, entered_verb, set_entered_verb,
            submit_count_v, set_submit_count_v, prev_count_v, set_prev_count_v,
            next_count_v, set_next_count_v, enter_count_v, set_enter_count_v,
            restart_count_v, set_restart_count_v,
            cv_verb, verb_form, check_btn_v, prev_btn_v, next_btn_v, restart_btn_v,
            vocab=words_verb,
            verb_meta=verb_meta,
            tense=_tense_key,
            word_key="Word",
            meaning_key="Translation",
            meaning_label=t_ui("translation_label", _lang).rstrip(":"),
            title=f"{t_ui('verb_heading', _lang)} — {_tlabel}",
            done_message=t_ui("test2_done", _lang),
            get_errors=errors_verb, set_errors=set_errors_verb,
            get_retry_cnt=retry_count_v, set_retry_cnt=set_retry_count_v,
            retry_btn=retry_btn_v,
        )
    elif not words_verb:
        _output = mo.md(t_ui("verb_empty", _lang))
    else:
        _output = mo.md(t_ui("verb_no_tense", _lang))
    _output
    return


@app.cell(hide_code=True)
def _(TEST_NUM, language_selector, mo, t_ui):
    # Test 4 heading
    _lang = language_selector.value
    mo.md(f"## {t_ui('test_label', _lang)} {TEST_NUM['adj']}: {t_ui('adj_test_topic', _lang)}")
    return


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, notebook_dir, vocab_name):
    # Load adjective data
    df_adj = gu2.load_vocab_table(vocab_name("adjectives"), nb_dir=notebook_dir, remote_base=RAW_BASE)
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, gu2, language_selector, mo, t_ui):
    # Adjective table
    table_adj = gu2.vocab_table(df_adj)
    _lang = language_selector.value
    _table_adj = table_adj if table_adj is not None else mo.md(t_ui("adjs_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_adjs", _lang)), _table_adj])
    return (table_adj,)


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Mode selector
    _lang = language_selector.value
    if _lang == 'ru':
        _opts = {"Простой: 3 рода × 2 числа (6 полей)": "simple", "Полный: все роды, числа и падежи (18 полей)": "complex"}
        _default_mode = "Простой: 3 рода × 2 числа (6 полей)"
    elif _lang == 'el':
        _opts = {"Απλό: 3 γένη × 2 αριθμοί (6 πεδία)": "simple", "Πλήρες: όλα τα γένη, αριθμοί και πτώσεις (18 πεδία)": "complex"}
        _default_mode = "Απλό: 3 γένη × 2 αριθμοί (6 πεδία)"
    else:
        _opts = {"Simple: 3 genders × 2 numbers (6 fields)": "simple", "Full: all genders, numbers, and cases (18 fields)": "complex"}
        _default_mode = "Simple: 3 genders × 2 numbers (6 fields)"
    mode_selector = mo.ui.radio(options=_opts, value=_default_mode, label=t_ui("mode_label", _lang))
    mo.md(f"{mode_selector}")
    return (mode_selector,)


@app.cell(hide_code=True)
def _(gu2, random, table_adj):
    # Adjective words + state
    words_adj = gu2.get_words(table_adj)
    (words4test_adj, set_words4test_adj, hist_adj, set_hist_adj, adj_msg, set_adj_msg,
     captured_adj, set_captured_adj, entered_adj, set_entered_adj,
     submit_count_a, set_submit_count_a, prev_count_a, set_prev_count_a,
     next_count_a, set_next_count_a, enter_count_a, set_enter_count_a,
     restart_count_a, set_restart_count_a) = gu2.make_paradigm_drill_state(
        random.sample(words_adj, len(words_adj)) if words_adj else []
    )
    errors_adj, set_errors_adj, retry_count_a, set_retry_count_a = gu2.make_error_tracking_state()
    return (
        adj_msg,
        captured_adj,
        enter_count_a,
        entered_adj,
        errors_adj,
        hist_adj,
        next_count_a,
        prev_count_a,
        restart_count_a,
        retry_count_a,
        set_adj_msg,
        set_captured_adj,
        set_enter_count_a,
        set_entered_adj,
        set_errors_adj,
        set_hist_adj,
        set_next_count_a,
        set_prev_count_a,
        set_restart_count_a,
        set_retry_count_a,
        set_submit_count_a,
        set_words4test_adj,
        submit_count_a,
        words4test_adj,
        words_adj,
    )


@app.cell(hide_code=True)
def _(
    entered_adj,
    gu2,
    hist_adj,
    language_selector,
    mode_selector,
    set_enter_count_a,
    set_next_count_a,
    set_prev_count_a,
    words4test_adj,
):
    # Adjective form
    cv_adj = words4test_adj()[0] if words4test_adj() else None
    _mode = mode_selector.value
    adj_meta = gu2.adjective_drill_meta(cv_adj["Word"], _mode) if cv_adj else None
    _entered_adj_form = entered_adj().get(cv_adj["Word"]) if cv_adj else None
    adj_form, prev_btn_a, next_btn_a, restart_btn_a = gu2.paradigm_drill_widgets(
        labels=gu2.adjective_slot_labels(_mode, lang=language_selector.value, active_slots=adj_meta.active_slots if adj_meta else None),
        values=_entered_adj_form,
        history_len=len(hist_adj()),
        remaining_len=len(words4test_adj()),
        lang=language_selector.value,
    )
    set_prev_count_a(0)
    set_next_count_a(0)
    set_enter_count_a(0)
    return adj_form, adj_meta, cv_adj, next_btn_a, prev_btn_a, restart_btn_a


@app.cell(hide_code=True)
def _(
    adj_form,
    captured_adj,
    cv_adj,
    gu2,
    language_selector,
    set_submit_count_a,
    t_ui,
):
    # Adjective check button
    check_btn_a = gu2.dirty_check_button(
        adj_form, captured_adj, cv_adj, "adj_word", word_key="Word",
        label=t_ui("check_label", language_selector.value),
    )
    set_submit_count_a(0)
    return (check_btn_a,)


@app.cell(hide_code=True)
def _(errors_adj, gu2, language_selector):
    # Adjective retry-mistakes button
    retry_btn_a = gu2.retry_mistakes_button(errors_adj(), lang=language_selector.value)
    return (retry_btn_a,)


@app.cell(hide_code=True)
def _(
    adj_form,
    adj_meta,
    adj_msg,
    captured_adj,
    check_btn_a,
    cv_adj,
    enter_count_a,
    entered_adj,
    errors_adj,
    gu2,
    hist_adj,
    language_selector,
    mo,
    mode_selector,
    next_btn_a,
    next_count_a,
    prev_btn_a,
    prev_count_a,
    restart_btn_a,
    restart_count_a,
    retry_btn_a,
    retry_count_a,
    set_adj_msg,
    set_captured_adj,
    set_enter_count_a,
    set_entered_adj,
    set_errors_adj,
    set_hist_adj,
    set_next_count_a,
    set_prev_count_a,
    set_restart_count_a,
    set_retry_count_a,
    set_submit_count_a,
    set_words4test_adj,
    submit_count_a,
    t_ui,
    words4test_adj,
    words_adj,
):
    # Adjective drill
    _lang = language_selector.value
    _mode = mode_selector.value
    gu2.adjective_paradigm_drill_form(
        words4test_adj, set_words4test_adj, hist_adj, set_hist_adj, adj_msg, set_adj_msg,
        captured_adj, set_captured_adj, entered_adj, set_entered_adj,
        submit_count_a, set_submit_count_a, prev_count_a, set_prev_count_a,
        next_count_a, set_next_count_a, enter_count_a, set_enter_count_a,
        restart_count_a, set_restart_count_a,
        cv_adj, adj_form, check_btn_a, prev_btn_a, next_btn_a, restart_btn_a,
        vocab=words_adj,
        adj_meta=adj_meta,
        mode=_mode,
        word_key="Word",
        meaning_key="Translation",
        meaning_label=t_ui("translation_label", _lang).rstrip(":"),
        title=t_ui("adj_heading", _lang),
        done_message=t_ui("test3_done", _lang),
        get_errors=errors_adj, set_errors=set_errors_adj,
        get_retry_cnt=retry_count_a, set_retry_cnt=set_retry_count_a,
        retry_btn=retry_btn_a,
    ) if words_adj else mo.md(t_ui("adj_empty", _lang))
    return


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
    language_selector = _language_selector(
        mo, lang_bridge, options={"English": "en", "Русский": "ru", "Ελληνικά": "el"}, default="el"
    )
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
def _(language_selector, mo, t_ui):
    _en = language_selector.value == "en"
    trans_selector = mo.ui.dropdown(
        options={"literal": "literal", "Valassopoulo (1924)": "Valassopoulo"} if _en else {
            "подстрочник": "подстрочник",
            "Шмаков / Бродский · рус.": "Шмаков/Бродский",
            "Ильинская (1984) · рус.": "Ильинская",
            "Левитов · рус.": "Левитов",
        },
        value="literal" if _en else "подстрочник",
        label=t_ui("translation_label", language_selector.value).rstrip(":"),
    )
    return (trans_selector,)


@app.cell(hide_code=True)
def _(gu2):
    t_ui = gu2.ui_label
    return (t_ui,)


@app.cell(hide_code=True)
def _(language_selector):
    # One vocabulary file per UI language: English has *_en.tsv, ru/el share the Russian files.
    def vocab_name(stem):
        return f"{stem}_en.tsv" if language_selector.value == "en" else f"{stem}.tsv"
    return (vocab_name,)


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, language_selector, notebook_dir):
    # Russian/Greek: the word-in-translation exercise is always shown. English: only when the answer key has a reviewed "no" row for Valassopoulo --
    # a faithful translation reflects almost every word, and an exercise whose answer is always "yes" is not worth showing.
    PRESENCE_SHOWN = True
    if language_selector.value == "en":
        _tp_path = gu2.ensure_file("translation_presence.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
        PRESENCE_SHOWN = bool(_tp_path) and any(
            _r["translator"] == "Valassopoulo" and _r["reflected"] == "no" for _r in gu2.read_translation_presence_tsv(_tp_path)
        )
    TEST_NUM = {"noun": 2, "verb": 3, "adj": 4} if PRESENCE_SHOWN else {"noun": 1, "verb": 2, "adj": 3}
    return PRESENCE_SHOWN, TEST_NUM


@app.cell(hide_code=True)
def _():
    RAW_BASE = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/modern_greek/b1greeklanguageandculture/kavafis_ithaki/4"
    return (RAW_BASE,)


@app.cell(hide_code=True)
def _(RAW_BASE, eee, gu2, notebook_dir):
    # molab only bundles files that live alongside the notebook when it's
    # imported from a published repo URL -- a raw single-file upload (the
    # only option before this course is committed/pushed) leaves siblings
    # like greek.md/translations.md behind, so route them through
    # ensure_file() rather than a bare local read (see created_with_eee's
    # root CLAUDE.md, "Notebook Content Gotchas"). The three files are
    # unrelated, so fetch them concurrently rather than paying for three
    # sequential round-trips on a cold cache.
    from concurrent.futures import ThreadPoolExecutor as _Pool
    with _Pool(max_workers=3) as _pool:
        _greek_path, _trans_path, _trans_en_path = _pool.map(
            lambda _fn: gu2.ensure_file(_fn, nb_dir=notebook_dir, remote_base=RAW_BASE),
            ("greek.md", "translations.md", "translations_en.md"),
        )
    if not _greek_path or not _trans_path or not _trans_en_path:
        raise FileNotFoundError("greek.md/translations.md/translations_en.md: could not be found locally or fetched from remote_base")
    _greek = eee.parse_stanza_text(_greek_path.read_text(encoding="utf-8"))
    _trans, TRANS_DESC = eee.parse_stanza_translations(_trans_path.read_text(encoding="utf-8"))
    _trans_en, _desc_en = eee.parse_stanza_translations(_trans_en_path.read_text(encoding="utf-8"))
    _trans.update(_trans_en)
    TRANS_DESC.update(_desc_en)
    STANZAS = [
        {
            "ref": ref,
            "lines": lines,
            "translations": {tr: d.get(ref, "—") for tr, d in _trans.items()},
        }
        for ref, lines in _greek.items()
    ]
    return STANZAS, TRANS_DESC


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, notebook_dir, vocab_name):
    POEM_WORDS_RAW = gu2.load_inflected_vocab_tsv(vocab_name("poem_vocab"), nb_dir=notebook_dir, remote_base=RAW_BASE)
    return (POEM_WORDS_RAW,)


@app.cell(hide_code=True)
def _(language_selector, mo):
    from eee_project import ConfigStore as _ConfigStore
    from eee_project.notebook_utils import eee_footer
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _cfg = _ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/modern_greek/b1greeklanguageandculture/kavafis_ithaki/index.tsv",
    )
    _prev_url, _next_url = _cfg.adjacent_urls("4/")
    eee_footer(mo, lang=language_selector.value, prev_url=_prev_url, next_url=_next_url, same_window=True)
    return


@app.cell(hide_code=True)
def _():
    import os
    import random

    import marimo as mo
    import pandas as pd
    import eee_project as eee
    from eee_project import GreekUtils, MODERN_GREEK
    from modern_greek_backend_eee import ModernGreekBackend
    _mg_backend = ModernGreekBackend()
    eee.register_backend("el", _mg_backend, backend="modern-greek")
    eee.set_chain("el", ["modern-greek"])
    gu2 = GreekUtils(_mg_backend, mo, pd, eee_module=eee, config=MODERN_GREEK)
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    return eee, gu2, mo, notebook_dir, random


if __name__ == "__main__":
    app.run()
