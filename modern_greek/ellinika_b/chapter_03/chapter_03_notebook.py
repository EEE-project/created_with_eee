# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project>=1.1.0",
#     "marimo>=0.23.14",
#     "modern-greek-backend-eee>=1.0.0",
#     "pandas",
# ]
# ///

import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(language_selector, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _cfg = ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/modern_greek/ellinika_b/index.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=_cfg.index_url(), lang=language_selector.value, titles={
        "ru": "Ελληνικά Β", "el": "Ελληνικά Β", "en": "Ελληνικά Β",
    }, ga_config=_cfg.ga_config(), same_window=True)
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Title
    _lang = language_selector.value
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_znfXhVVXiTiyHNWfJg8dNi)"
    if _lang == "ru":
        _sub = "Глава 3 — Городская жизнь · B1"
        _gl, _tl = "Грамматика", "Тесты"
        _tc = "Существительные · Глаголы · Прилагательные"
    elif _lang == "el":
        _sub = "Ενότητα 3 — Ζωή στην πόλη · B1"
        _gl, _tl = "Γραμματική", "Τεστ"
        _tc = "Ουσιαστικά · Ρήματα · Επίθετα"
    else:
        _sub = "Unit 3 — City Life · B1"
        _gl, _tl = "Grammar", "Tests"
        _tc = "Nouns · Verbs · Adjectives"
    _gc = "Αόριστες Αντωνυμίες (κάποιος/κανένας/ίδιος) · Δεικτικές (τέτοιος/τόσος)"
    _out = mo.md(f"""# «Είχε τέτοια κίνηση!» 🚌
    ## {_sub} {_badge}

    **{_gl}:** {_gc}
    **{_tl}:** {_tc}
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Indefinite Pronouns
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ## Грамматика: Неопределённые местоимения I — ο ίδιος, άλλος, μόνος (стр. 45)

    Неопределённые местоимения указывают на **неконкретных** людей или вещи. В учебнике этой теме посвящены три отдельные врезки (стр. 45, 53, 54).

    **ο ίδιος / η ίδια / το ίδιο** («тот же самый» / «сам»):

    | | Муж. (Им.) | Жен. (Им.) | Ср. (Им.) |
    |-|------------|-----------|-----------|
    | ο ίδιος | ο ίδιος | η ίδια | το ίδιο |

    - – Τον κύριο Παναγιωτίδη, παρακαλώ. – **Ο ίδιος**. — _Он самый._
    - Δεν μπορεί να πάει κανένας άλλος. Πρέπει να πάω **η ίδια**. — _Никто другой не может пойти. Придётся идти мне самой._
    - Έχουμε **τους ίδιους** καθηγητές. — _У нас те же самые преподаватели._
    - – Τι νέα; – Τίποτα ιδιαίτερο. **Τα ίδια και τα ίδια**. — _Ничего особенного. Всё то же самое._

    **άλλος / άλλη / άλλο** («другой»):

    - Πρέπει να πάρεις **άλλο** εισιτήριο. Δεν μπορείς να συνεχίσεις με το ίδιο. — _Тебе нужен другой билет. С этим продолжать нельзя._
    - Η **άλλη** γειτονιά ήταν πιο ήσυχη από αυτή. — _Тот, другой район был тише этого._
    - Δεν είχε λεωφορεία. Έτσι, **άλλοι** πήραν ταξί και **άλλοι** γύρισαν με τα πόδια. — _Автобусов не было. Так что одни взяли такси, а другие пошли пешком._
    - Τον **άλλο** μήνα θα ψάξω για καινούριο σπίτι. — _В следующем месяце я поищу новую квартиру._
    - Δε θα έρθει μαζί μας **κανένας άλλος**; — _Больше никто с нами не пойдёт?_

    Порядок слов меняет смысл: **ένα άλλο** ποτήρι (= не это, *другой* стакан) — **άλλο ένα** ποτήρι (= *ещё один* стакан).

    **μόνος, μόνη, μόνο** («один» / «сам»):

    | Форма | + |
    |-------|---|
    | μόνος, μόνη, μόνο | μου |
    | μόνος, μόνη, μόνο | σου |
    | μόνος | του |
    | μόνη | της |
    | μόνο | του |
    | μόνοι, μόνες, μόνα | μας |
    | μόνοι, μόνες, μόνα | σας |
    | μόνοι, μόνες, μόνα | τους |

    - Η Μαρίνα μένει **μόνη της**. — _Марина живёт одна._
    - Σήμερα το παιδί πήγε στο σχολείο **μόνο του**. — _Сегодня ребёнок пошёл в школу один (сам)._
    - Δε χρειάζεται να έρθεις κι εσύ. Θα πάμε **μόνες μας**. — _Тебе не нужно идти тоже. Мы пойдём одни (сами)._
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ## Γραμματική: Αόριστες Αντωνυμίες Ι — ο ίδιος, άλλος, μόνος (σ. 45)

    Οι αόριστες αντωνυμίες αναφέρονται σε **αόριστα** πρόσωπα ή πράγματα. Το βιβλίο τις παρουσιάζει σε τρεις ξεχωριστές ενότητες (σ. 45, 53, 54).

    **ο ίδιος / η ίδια / το ίδιο**:

    | | Αρσ. (Ον.) | Θηλ. (Ον.) | Ουδ. (Ον.) |
    |-|------------|-----------|-----------|
    | ο ίδιος | ο ίδιος | η ίδια | το ίδιο |

    - – Τον κύριο Παναγιωτίδη, παρακαλώ. – **Ο ίδιος**. _("Speaking." — lit. "the same one")_
    - Δεν μπορεί να πάει κανένας άλλος. Πρέπει να πάω **η ίδια**. _(No one else can go. I have to go myself.)_
    - Έχουμε **τους ίδιους** καθηγητές. _(We have the same teachers.)_
    - – Τι νέα; – Τίποτα ιδιαίτερο. **Τα ίδια και τα ίδια**. _(Nothing special. Same old, same old.)_

    **άλλος / άλλη / άλλο**:

    - Πρέπει να πάρεις **άλλο** εισιτήριο. Δεν μπορείς να συνεχίσεις με το ίδιο. _(You need to get another ticket. You can't continue with the same one.)_
    - Η **άλλη** γειτονιά ήταν πιο ήσυχη από αυτή. _(The other neighborhood was quieter than this one.)_
    - Δεν είχε λεωφορεία. Έτσι, **άλλοι** πήραν ταξί και **άλλοι** γύρισαν με τα πόδια. _(There were no buses. So some took taxis and others walked back.)_
    - Τον **άλλο** μήνα θα ψάξω για καινούριο σπίτι. _(Next month I'll look for a new place.)_
    - Δε θα έρθει μαζί μας **κανένας άλλος**; _(Is no one else coming with us?)_

    Η σειρά των λέξεων αλλάζει το νόημα: **ένα άλλο** ποτήρι (= a *different* glass, not this one) — **άλλο ένα** ποτήρι (= one *more* glass).

    **μόνος, μόνη, μόνο**:

    | Τύπος | + |
    |-------|---|
    | μόνος, μόνη, μόνο | μου |
    | μόνος, μόνη, μόνο | σου |
    | μόνος | του |
    | μόνη | της |
    | μόνο | του |
    | μόνοι, μόνες, μόνα | μας |
    | μόνοι, μόνες, μόνα | σας |
    | μόνοι, μόνες, μόνα | τους |

    - Η Μαρίνα μένει **μόνη της**. _(Marina lives alone.)_
    - Σήμερα το παιδί πήγε στο σχολείο **μόνο του**. _(Today the child went to school by himself.)_
    - Δε χρειάζεται να έρθεις κι εσύ. Θα πάμε **μόνες μας**. _(You don't need to come too. We'll go by ourselves.)_
    """)
    else:
        _md = mo.md("""
    ## Grammar: Indefinite Pronouns I — ο ίδιος, άλλος, μόνος (p. 45)

    Indefinite pronouns refer to **non-specific** people or things. The textbook covers them across three separate boxes (pp. 45, 53, 54).

    **ο ίδιος / η ίδια / το ίδιο** ("the same" / "-self"):

    | | Masc. (Nom.) | Fem. (Nom.) | Neut. (Nom.) |
    |-|-------------|------------|--------------|
    | ο ίδιος | ο ίδιος | η ίδια | το ίδιο |

    - – Τον κύριο Παναγιωτίδη, παρακαλώ. – **Ο ίδιος**. — _Speaking._ (lit. "the same one")
    - Δεν μπορεί να πάει κανένας άλλος. Πρέπει να πάω **η ίδια**. — _No one else can go. I have to go myself._
    - Έχουμε **τους ίδιους** καθηγητές. — _We have the same teachers._
    - – Τι νέα; – Τίποτα ιδιαίτερο. **Τα ίδια και τα ίδια**. — _Nothing special. Same old, same old._

    **άλλος / άλλη / άλλο** ("other/another"):

    - Πρέπει να πάρεις **άλλο** εισιτήριο. Δεν μπορείς να συνεχίσεις με το ίδιο. — _You need to get another ticket. You can't continue with the same one._
    - Η **άλλη** γειτονιά ήταν πιο ήσυχη από αυτή. — _The other neighborhood was quieter than this one._
    - Δεν είχε λεωφορεία. Έτσι, **άλλοι** πήραν ταξί και **άλλοι** γύρισαν με τα πόδια. — _There were no buses. So some took taxis and others walked back._
    - Τον **άλλο** μήνα θα ψάξω για καινούριο σπίτι. — _Next month I'll look for a new place._
    - Δε θα έρθει μαζί μας **κανένας άλλος**; — _Is no one else coming with us?_

    Word order changes the meaning: **ένα άλλο** ποτήρι (= a *different* glass, not this one) vs. **άλλο ένα** ποτήρι (= one *more* glass).

    **μόνος, μόνη, μόνο** ("alone" / "by oneself"):

    | Form | + |
    |------|---|
    | μόνος, μόνη, μόνο | μου |
    | μόνος, μόνη, μόνο | σου |
    | μόνος | του |
    | μόνη | της |
    | μόνο | του |
    | μόνοι, μόνες, μόνα | μας |
    | μόνοι, μόνες, μόνα | σας |
    | μόνοι, μόνες, μόνα | τους |

    - Η Μαρίνα μένει **μόνη της**. — _Marina lives alone._
    - Σήμερα το παιδί πήγε στο σχολείο **μόνο του**. — _Today the child went to school by himself._
    - Δε χρειάζεται να έρθεις κι εσύ. Θα πάμε **μόνες μας**. — _You don't need to come too. We'll go by ourselves._
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Indefinite Pronouns II
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ## Грамматика: Неопределённые местоимения II — κανένας, τίποτα (стр. 53)

    **κανένας/κανείς, καμία/καμιά, κανένα** и **τίποτα** в утвердительных/вопросительных предложениях означают «кто-то/что-то», а в отрицательных — «никто/ничто».

    | Форма | Утвердит./вопросит. (= κάποιος/κάτι) | Отрицат. (= ούτε ένας/καμία) |
    |-------|----------------------------------------|-------------------------------|
    | κανένας/κανείς, κανενός, κανέναν | Είναι κανείς εδώ; Υπάρχει κανένας σταθμός του μετρό εδώ κοντά; Πρέπει να επικυρώσεις το εισιτήριό σου. Μπορεί να μπει κανένας ελεγκτής. Είναι κανενός αυτό το αυτοκίνητο; | **Κανένας** δεν ήταν στη στάση του λεωφορείου. |
    | καμία/καμιά, καμίας/καμιάς, καμία/καμιά | Υπάρχει καμία στάση εδώ κοντά; Πάρε καμιά ασπιρίνη. | Όχι, δε βλέπω **καμία**. Δε βλέπω **καμία** στάση εδώ κοντά. |
    | κανένα, κανενός, κανένα | Βλέπεις κανένα ταξί; Πρέπει να αγοράσω κανένα εισιτήριο. | Όχι, δε βλέπω **κανένα**. Δεν υπάρχει **κανένα** αυτοκίνητο στον δρόμο. |
    | τίποτα/τίποτε | Θέλεις τίποτα από το περίπτερο; Θέλετε τίποτα άλλο; | Δε θέλω **τίποτα**. Εγώ δεν άκουσα **τίποτα** τέτοιο. Δεν αγόρασα **τίποτα** καινούριο. |

    _Иногда мы едем с каким-нибудь другом куда-нибудь, чтобы съесть что-нибудь? — шуточный пример из учебника, где κανέναν/πουθενά/τίποτα все стоят в «утвердительном» (вопросительном) значении._
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ## Γραμματική: Αόριστες Αντωνυμίες ΙΙ — κανένας, τίποτα (σ. 53)

    | Τύπος | Καταφατικό/ερωτηματικό (= κάποιος/κάτι) | Αρνητικό (= ούτε ένας/καμία) |
    |-------|------------------------------------------|-------------------------------|
    | κανένας/κανείς, κανενός, κανέναν | Είναι κανείς εδώ; Υπάρχει κανένας σταθμός του μετρό εδώ κοντά; Πρέπει να επικυρώσεις το εισιτήριό σου. Μπορεί να μπει κανένας ελεγκτής. Είναι κανενός αυτό το αυτοκίνητο; | **Κανένας** δεν ήταν στη στάση του λεωφορείου. |
    | καμία/καμιά, καμίας/καμιάς, καμία/καμιά | Υπάρχει καμία στάση εδώ κοντά; Πάρε καμιά ασπιρίνη. | Όχι, δε βλέπω **καμία**. Δε βλέπω **καμία** στάση εδώ κοντά. |
    | κανένα, κανενός, κανένα | Βλέπεις κανένα ταξί; Πρέπει να αγοράσω κανένα εισιτήριο. | Όχι, δε βλέπω **κανένα**. Δεν υπάρχει **κανένα** αυτοκίνητο στον δρόμο. |
    | τίποτα/τίποτε | Θέλεις τίποτα από το περίπτερο; Θέλετε τίποτα άλλο; | Δε θέλω **τίποτα**. Εγώ δεν άκουσα **τίποτα** τέτοιο. Δεν αγόρασα **τίποτα** καινούριο. |

    _«Καμιά φορά πάμε με κανέναν φίλο σου πουθενά να φάμε τίποτα;» ("Do we ever go somewhere with some friend of yours to eat something?") — παράδειγμα του βιβλίου όπου κανέναν/πουθενά/τίποτα έχουν όλα καταφατική (ερωτηματική) σημασία._
    """)
    else:
        _md = mo.md("""
    ## Grammar: Indefinite Pronouns II — κανένας, τίποτα (p. 53)

    **κανένας/κανείς, καμία, κανένα** and **τίποτα** mean "someone/anything" in affirmative/questions, but "no one/nothing" in negative sentences.

    | Form | Affirmative/interrogative (= κάποιος/κάτι) | Negative (= not even one) |
    |------|---------------------------------------------|----------------------------|
    | κανένας/κανείς, κανενός, κανέναν | Είναι κανείς εδώ; Υπάρχει κανένας σταθμός του μετρό εδώ κοντά; Πρέπει να επικυρώσεις το εισιτήριό σου. Μπορεί να μπει κανένας ελεγκτής. Είναι κανενός αυτό το αυτοκίνητο; | **Κανένας** δεν ήταν στη στάση του λεωφορείου. |
    | καμία/καμιά, καμίας/καμιάς, καμία/καμιά | Υπάρχει καμία στάση εδώ κοντά; Πάρε καμιά ασπιρίνη. | Όχι, δε βλέπω **καμία**. Δε βλέπω **καμία** στάση εδώ κοντά. |
    | κανένα, κανενός, κανένα | Βλέπεις κανένα ταξί; Πρέπει να αγοράσω κανένα εισιτήριο. | Όχι, δε βλέπω **κανένα**. Δεν υπάρχει **κανένα** αυτοκίνητο στον δρόμο. |
    | τίποτα/τίποτε | Θέλεις τίποτα από το περίπτερο; Θέλετε τίποτα άλλο; | Δε θέλω **τίποτα**. Εγώ δεν άκουσα **τίποτα** τέτοιο. Δεν αγόρασα **τίποτα** καινούριο. |

    _"Καμιά φορά πάμε με κανέναν φίλο σου πουθενά να φάμε τίποτα;" — the book's own example, where κανέναν/πουθενά/τίποτα are all used in their affirmative (question) sense, not the negative one._
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Indefinite Pronouns III
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ## Грамматика: Неопределённые местоимения III — κάποιος, κάτι (стр. 54)

    **κάποιος / κάποια / κάποιο** («кто-то» / «какой-то, некий»):

    | κάποιος | κάποια | κάποιο |
    |---------|--------|--------|
    | κάποιος, κάποιου, κάποιον | κάποια, κάποιας, κάποια | κάποιο, κάποιου, κάποιο |
    | κάποιοι, κάποιων, κάποιους | κάποιες, κάποιων, κάποιες | κάποια, κάποιων, κάποια |

    - **Κάποιος** σε ζητάει. Περιμένετε **κάποιον**. Θα πάμε με το αυτοκίνητο **κάποιων** φίλων. Αύριο θα γνωρίσουμε **κάποιους** καινούριους συναδέλφους. — _Тебя кто-то спрашивает. Подождите кое-кого. Мы поедем на машине каких-то друзей. Завтра познакомимся с некоторыми новыми коллегами._
    - Θα έρθω **κάποια** στιγμή να σε δω. Είναι το παιδί **κάποιας** γειτόνισσας. **Κάποιες** ώρες η κίνηση στους δρόμους είναι μεγάλη. — _Я как-нибудь зайду к тебе. Это ребёнок какой-то соседки. В некоторые часы движение на дорогах сильное._
    - – Ποιος χτύπησε την πόρτα; – Μάλλον **κάποιο** παιδί από τη γειτονιά. Ξύπνησα από τη μηχανή **κάποιου** αυτοκινήτου. Έχει **κάποια** προβλήματα αυτόν τον καιρό. — _– Кто стучал в дверь? – Наверное, какой-то ребёнок из района. Меня разбудил звук чьей-то машины. У него сейчас кое-какие проблемы._

    **κάτι** («что-то»):

    - Ήθελα να σου πω **κάτι**, αλλά δε θυμάμαι τι. Ξέρεις **κάτι**; Θα έρθω μαζί σου τελικά. Θέλετε **κάτι** άλλο; Πρώτη φορά ακούω **κάτι** τέτοιο. Αγόρασα **κάτι** ωραίο. Αυτή η γειτονιά έχει **κάτι** δρόμους! – Τι ώρα είναι; – Πέντε και **κάτι**. — _Я хотел(а) сказать тебе кое-что, но не помню что. Знаешь что? Я всё-таки пойду с тобой. Хотите ещё что-нибудь? Первый раз слышу такое. Я купил(а) кое-что красивое. В этом районе такие улицы! – Который час? – Начало шестого._

    Ударение сдвигается во множественном числе: κάποιος → κάποι**οι**, как и τέτοιος → τέτοι**οι**.
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ## Γραμματική: Αόριστες Αντωνυμίες ΙΙΙ — κάποιος, κάτι (σ. 54)

    **κάποιος (= ένας) / κάποια (= μια) / κάποιο (= ένα)**:

    | κάποιος | κάποια | κάποιο |
    |---------|--------|--------|
    | κάποιος, κάποιου, κάποιον | κάποια, κάποιας, κάποια | κάποιο, κάποιου, κάποιο |
    | κάποιοι, κάποιων, κάποιους | κάποιες, κάποιων, κάποιες | κάποια, κάποιων, κάποια |

    - **Κάποιος** σε ζητάει. Περιμένετε **κάποιον**. Θα πάμε με το αυτοκίνητο **κάποιων** φίλων. Αύριο θα γνωρίσουμε **κάποιους** καινούριους συναδέλφους. _(Someone's asking for you. Wait for someone. We'll go in some friends' car. Tomorrow we'll meet some new colleagues.)_
    - Θα έρθω **κάποια** στιγμή να σε δω. Είναι το παιδί **κάποιας** γειτόνισσας. **Κάποιες** ώρες η κίνηση στους δρόμους είναι μεγάλη. _(I'll come see you at some point. It's some neighbor's child. At certain hours the traffic is heavy.)_
    - – Ποιος χτύπησε την πόρτα; – Μάλλον **κάποιο** παιδί από τη γειτονιά. Ξύπνησα από τη μηχανή **κάποιου** αυτοκινήτου. Έχει **κάποια** προβλήματα αυτόν τον καιρό. _(— Who knocked on the door? — Probably some kid from the neighborhood. I woke up to the engine of some car. He's having some problems these days.)_

    **κάτι**:

    - Ήθελα να σου πω **κάτι**, αλλά δε θυμάμαι τι. Ξέρεις **κάτι**; Θα έρθω μαζί σου τελικά. Θέλετε **κάτι** άλλο; Πρώτη φορά ακούω **κάτι** τέτοιο. Αγόρασα **κάτι** ωραίο. Αυτή η γειτονιά έχει **κάτι** δρόμους! – Τι ώρα είναι; – Πέντε και **κάτι**. _(I wanted to tell you something, but I don't remember what. You know what? I'll come with you after all. Would you like something else? First time I've heard anything like that. I bought something nice. This neighborhood has some streets! — What time is it? — A bit past five.)_

    Ο τόνος μετακινείται στον πληθυντικό: κάποιος → κάποι**οι**, όπως και τέτοιος → τέτοι**οι**.
    """)
    else:
        _md = mo.md("""
    ## Grammar: Indefinite Pronouns III — κάποιος, κάτι (p. 54)

    **κάποιος / κάποια / κάποιο** ("someone" / "a certain"):

    | κάποιος | κάποια | κάποιο |
    |---------|--------|--------|
    | κάποιος, κάποιου, κάποιον | κάποια, κάποιας, κάποια | κάποιο, κάποιου, κάποιο |
    | κάποιοι, κάποιων, κάποιους | κάποιες, κάποιων, κάποιες | κάποια, κάποιων, κάποια |

    - **Κάποιος** σε ζητάει. Περιμένετε **κάποιον**. Θα πάμε με το αυτοκίνητο **κάποιων** φίλων. Αύριο θα γνωρίσουμε **κάποιους** καινούριους συναδέλφους. — _Someone's asking for you. Wait for someone. We'll go in some friends' car. Tomorrow we'll meet some new colleagues._
    - Θα έρθω **κάποια** στιγμή να σε δω. Είναι το παιδί **κάποιας** γειτόνισσας. **Κάποιες** ώρες η κίνηση στους δρόμους είναι μεγάλη. — _I'll come see you at some point. It's some neighbor's child. At certain hours the traffic is heavy._
    - – Ποιος χτύπησε την πόρτα; – Μάλλον **κάποιο** παιδί από τη γειτονιά. Ξύπνησα από τη μηχανή **κάποιου** αυτοκινήτου. Έχει **κάποια** προβλήματα αυτόν τον καιρό. — _– Who knocked on the door? – Probably some kid from the neighborhood. I woke up to the engine of some car. He's having some problems these days._

    **κάτι** ("something"):

    - Ήθελα να σου πω **κάτι**, αλλά δε θυμάμαι τι. Ξέρεις **κάτι**; Θα έρθω μαζί σου τελικά. Θέλετε **κάτι** άλλο; Πρώτη φορά ακούω **κάτι** τέτοιο. Αγόρασα **κάτι** ωραίο. Αυτή η γειτονιά έχει **κάτι** δρόμους! – Τι ώρα είναι; – Πέντε και **κάτι**. — _I wanted to tell you something, but I don't remember what. You know what? I'll come with you after all. Would you like something else? First time I've heard anything like that. I bought something nice. This neighborhood has some streets! – What time is it? – A bit past five._

    The stress shifts in the plural: κάποιος → κάποι**οι**, same as τέτοιος → τέτοι**οι**.
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Demonstrative Pronouns
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ## Грамматика: Указательные местоимения (Δεικτικές Αντωνυμίες)

    Указательные местоимения указывают на **конкретные качества или количества** (стр. 52).

    | Местоимение | Значение | Муж. (Им.) | Жен. (Им.) | Ср. (Им.) |
    |-------------|----------|------------|-----------|-----------|
    | τέτοιος | такой | τέτοιος | τέτοια | τέτοιο |
    | τόσος | столько | τόσος | τόση | τόσο |

    **Формы винительного падежа:**

    | | Муж. | Жен. | Ср. |
    |-|------|------|-----|
    | τέτοιος | τέτοιον | τέτοια | τέτοιο |
    | τόσος | τόσον | τόση | τόσο |

    **Примеры:**
    - Πρώτη φορά γνωρίζω **τέτοιον** άνθρωπο. — _Впервые встречаю такого человека._
    - Είχε **τόσο** κόσμο, που φύγαμε. — _Было столько народу, что мы ушли._
    - Δεν περίμενα να κάνω **τόσες** ώρες. — _Я не ожидал(а), что это займёт столько часов._
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ## Γραμματική: Δεικτικές Αντωνυμίες

    Οι δεικτικές αντωνυμίες δείχνουν **συγκεκριμένες ιδιότητες ή ποσότητες** (σ. 52).

    | Αντωνυμία | Σημασία | Αρσ. (Ον.) | Θηλ. (Ον.) | Ουδ. (Ον.) |
    |-----------|---------|------------|-----------|-----------|
    | τέτοιος | αυτού του είδους | τέτοιος | τέτοια | τέτοιο |
    | τόσος | τόσο πολύ / πολλοί | τόσος | τόση | τόσο |

    **Αιτιατική:**

    | | Αρσ. | Θηλ. | Ουδ. |
    |-|------|------|------|
    | τέτοιος | τέτοιον | τέτοια | τέτοιο |
    | τόσος | τόσον | τόση | τόσο |

    **Παραδείγματα:**
    - Πρώτη φορά γνωρίζω **τέτοιον** άνθρωπο. — _First time I've met such a person._
    - Είχε **τόσο** κόσμο, που φύγαμε. — _There were so many people that we left._
    - Δεν περίμενα να κάνω **τόσες** ώρες. — _I didn't expect it to take so many hours._
    """)
    else:
        _md = mo.md("""
    ## Grammar: Demonstrative Pronouns (Δεικτικές Αντωνυμίες)

    Demonstrative pronouns point out **specific qualities or quantities** (p. 52).

    | Pronoun | Meaning | Masc. (Nom.) | Fem. (Nom.) | Neut. (Nom.) |
    |---------|---------|-------------|------------|--------------|
    | τέτοιος | such / like this | τέτοιος | τέτοια | τέτοιο |
    | τόσος | so much / so many | τόσος | τόση | τόσο |

    **Accusative forms:**

    | | Masc. | Fem. | Neut. |
    |-|-------|------|-------|
    | τέτοιος | τέτοιον | τέτοια | τέτοιο |
    | τόσος | τόσον | τόση | τόσο |

    **Examples:**
    - Πρώτη φορά γνωρίζω **τέτοιον** άνθρωπο. — _First time I've met such a person._
    - Είχε **τόσο** κόσμο, που φύγαμε. — _There were so many people that we left._
    - Δεν περίμενα να κάνω **τόσες** ώρες. — _I didn't expect it to take so many hours._
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: pairno vs pernao usage note
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ## Παίρνω или περνάω; (стр. 50)

    Эти два глагола легко перепутать в контексте передвижения по городу:

    - **παίρνω** = садиться на (транспорт) *или* заезжать за кем-то: παίρνω το λεωφορείο / ένα ταξί · παίρνω κάποιον από το αεροδρόμιο / την Ντιάνα από τη στάση / τα παιδιά από το σχολείο.
    - **περνάω / περνώ** = проходить / проезжать (мимо, через): περνάς απέναντι (переходишь на другую сторону) · Πόσο συχνά περνάει το λεωφορείο; (Как часто ходит автобус?)
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ## Παίρνω ή περνάω; (σ. 50)

    Αυτά τα δύο ρήματα μπερδεύονται εύκολα σε πλαίσιο μετακίνησης στην πόλη:

    - **παίρνω** = επιβιβάζομαι σε (μεταφορικό μέσο) *ή* πηγαίνω να πάρω κάποιον: παίρνω το λεωφορείο / ένα ταξί ("I take the bus / a taxi") · παίρνω κάποιον από το αεροδρόμιο / την Ντιάνα από τη στάση / τα παιδιά από το σχολείο ("I pick someone up from the airport / Diana from the stop / the kids from school").
    - **περνάω / περνώ** = διέρχομαι: περνάς απέναντι ("you cross over/pass to the other side") · Πόσο συχνά περνάει το λεωφορείο; ("How often does the bus come by?")
    """)
    else:
        _md = mo.md("""
    ## Παίρνω vs. περνάω (p. 50)

    Easy to confuse in transit contexts:

    - **παίρνω** = to take (a means of transport) *or* to pick someone up: παίρνω το λεωφορείο / ένα ταξί ("I take the bus / a taxi") · παίρνω κάποιον από το αεροδρόμιο / την Ντιάνα από τη στάση / τα παιδιά από το σχολείο ("I pick someone up from the airport / Diana from the stop / the kids from school").
    - **περνάω / περνώ** = to pass / go by: περνάς απέναντι ("you cross over/pass to the other side") · Πόσο συχνά περνάει το λεωφορείο; ("How often does the bus come by?")
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Useful phrases
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ## Полезные фразы (Πώς το λένε;)

    | Греческий | Русский | Контекст |
    |-----------|---------|----------|
    | Μπορώ να σας ρωτήσω κάτι; | Могу я вас кое-что спросить? | Обращение к незнакомцу |
    | Μήπως ξέρετε πού είναι η στάση ...; | Вы, случайно, не знаете, где остановка ...? | Общественный транспорт |
    | Πηγαίνετε ίσια. | Идите прямо. | Объяснить дорогу |
    | Στο δεύτερο στενό θα στρίψεις αριστερά. | На втором переулке повернёшь налево. | Объяснить дорогу |
    | Είναι κάθετη στην Παπάγου. | Она перпендикулярна улице Папагу. | Описать маршрут |
    | Έχασες τον δρόμο; | Ты заблудился/заблудилась? | Телефонный разговор |
    | Είχε τέτοια κίνηση! | Было такое движение! | Объяснить опоздание |
    | Πάντως, δεν άργησες και τόσο. | В любом случае, ты не так уж опоздал(а). | Успокоить |
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ## Χρήσιμες Εκφράσεις (Πώς το λένε;)

    | Φράση | Εξήγηση | Πλαίσιο |
    |-------|---------|---------|
    | Μπορώ να σας ρωτήσω κάτι; | Θέλω να σας κάνω μια ερώτηση. | Απευθύνομαι σε άγνωστο |
    | Μήπως ξέρετε πού είναι η στάση ...; | Γνωρίζετε τυχόν πού βρίσκεται η στάση ...; | Δημόσιες συγκοινωνίες |
    | Πηγαίνετε ίσια. | Πηγαίνετε ευθεία. | Οδηγίες πορείας |
    | Στο δεύτερο στενό θα στρίψεις αριστερά. | Στον δεύτερο στενό δρόμο θα πας αριστερά. | Οδηγίες πορείας |
    | Είναι κάθετη στην Παπάγου. | Σχηματίζει ορθή γωνία με την οδό Παπάγου. | Περιγραφή διαδρομής |
    | Έχασες τον δρόμο; | Δεν ξέρεις πού βρίσκεσαι; | Τηλεφωνική συνομιλία |
    | Είχε τέτοια κίνηση! | Υπήρχε πάρα πολλή κίνηση! | Εξήγηση καθυστέρησης |
    | Πάντως, δεν άργησες και τόσο. | Δεν καθυστέρησες τόσο πολύ, τελικά. | Καθησυχασμός |
    """)
    else:
        _md = mo.md("""
    ## Useful Phrases (Πώς το λένε;)

    | Greek | English | Context |
    |-------|---------|---------|
    | Μπορώ να σας ρωτήσω κάτι; | Can I ask you something? | Approaching a stranger |
    | Μήπως ξέρετε πού είναι η στάση ...; | Would you happen to know where the ... stop is? | Public transport |
    | Πηγαίνετε ίσια. | Go straight. | Giving directions |
    | Στο δεύτερο στενό θα στρίψεις αριστερά. | At the second alley you'll turn left. | Giving directions |
    | Είναι κάθετη στην Παπάγου. | It's perpendicular to Papagou street. | Describing a route |
    | Έχασες τον δρόμο; | Did you lose your way? | Phone call |
    | Είχε τέτοια κίνηση! | There was so much traffic! | Explaining a delay |
    | Πάντως, δεν άργησες και τόσο. | Anyway, you weren't that late. | Reassurance |
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Pronunciation cell
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ## Φωνή-γραφή (Правила произношения и написания, стр. 58-59)

    Дополнительный раздел учебника: как безударное **ι** перед другой гласной образует скользящий звук (глайд) — качество звука зависит от предшествующего согласного.

    | Пример | Правило | Звучит как |
    |--------|---------|------------|
    | εισιτήρια, αεροδρόμιο | /i/ + /a,e,o,u/ → [ia], [ie], [io], [iu] | — |
    | ποια, ποιες, ποιοι, ποιος, ποιους | после p/t/ts/f/θ/x/s + /i/ + гласная | χέρι, όχι |
    | καινούρια, καινούριες, καινούριοι | после b/d/dz/v/δ/γ/z/r + /i/ + гласная | Γερμανία, γεια |
    | μια, ζημιές | после **μ** + /i/ + гласная | — |
    | γειτονιά, γειτονιές, νιώθω | после **ν** + /i/ + гласная | — |
    | παλιά, παλιές, παλιοί | после **λ** + /i/ + гласная | — |

    Скороговорка из учебника: «Μια πάπια με ποια πάπια; Μια πάπια με παπιά.» (Какая утка с какой уткой? Утка с утятами.)

    Упражнения на слух (стр. 58-59): различение пар слов с глайдом и без (μπανάνα–μπανανιά, χρόνοι–χρόνια, δουλεία–δουλειά) и распределение слов по колонкам согласно типу звучания.
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ## Φωνή-γραφή (σ. 58-59)

    Πρόσθετη ενότητα του βιβλίου: πώς το άτονο **ι** πριν από άλλο φωνήεν σχηματίζει ημίφωνο — η ποιότητα του ήχου εξαρτάται από το προηγούμενο σύμφωνο.

    | Παράδειγμα | Κανόνας | Όπως: |
    |-----------|---------|-------|
    | εισιτήρια, αεροδρόμιο | /i/ + /a,e,o,u/ → [ia], [ie], [io], [iu] | — |
    | ποια, ποιες, ποιοι, ποιος, ποιους | μετά από p/t/ts/f/θ/x/s + /i/ + φωνήεν | χέρι, όχι |
    | καινούρια, καινούριες, καινούριοι | μετά από b/d/dz/v/δ/γ/z/r + /i/ + φωνήεν | Γερμανία, γεια |
    | μια, ζημιές | μετά από **μ** + /i/ + φωνήεν | — |
    | γειτονιά, γειτονιές, νιώθω | μετά από **ν** + /i/ + φωνήεν | — |
    | παλιά, παλιές, παλιοί | μετά από **λ** + /i/ + φωνήεν | — |

    Γλωσσοδέτης του βιβλίου: «Μια πάπια με ποια πάπια; Μια πάπια με παπιά.» ("Which duck with which duck? A duck with ducklings.")

    Ασκήσεις ακοής (σ. 58-59): διάκριση ζευγών λέξεων με/χωρίς ημίφωνο (μπανάνα–μπανανιά, χρόνοι–χρόνια, δουλεία–δουλειά) και κατάταξη λέξεων σε στήλες ανάλογα με τον ήχο.
    """)
    else:
        _md = mo.md("""
    ## Φωνή-γραφή (Pronunciation/Spelling, pp. 58-59)

    A supplementary segment: how an unstressed **ι** before another vowel forms a glide — the glide's quality depends on the preceding consonant.

    | Example | Rule | Sounds like |
    |---------|------|-------------|
    | εισιτήρια, αεροδρόμιο | /i/ + /a,e,o,u/ → [ia], [ie], [io], [iu] | — |
    | ποια, ποιες, ποιοι, ποιος, ποιους | after p/t/ts/f/θ/x/s + /i/ + vowel | χέρι, όχι |
    | καινούρια, καινούριες, καινούριοι | after b/d/dz/v/δ/γ/z/r + /i/ + vowel | Γερμανία, γεια |
    | μια, ζημιές | after **μ** + /i/ + vowel | — |
    | γειτονιά, γειτονιές, νιώθω | after **ν** + /i/ + vowel | — |
    | παλιά, παλιές, παλιοί | after **λ** + /i/ + vowel | — |

    Tongue-twister from the book: "Μια πάπια με ποια πάπια; Μια πάπια με παπιά." (Which duck with which duck? A duck with ducklings.)

    Listening exercises (pp. 58-59): telling apart word pairs with/without the glide (μπανάνα–μπανανιά, χρόνοι–χρόνια, δουλεία–δουλειά) and sorting words into columns by which sound they contain.
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 1 heading
    mo.md(t_ui("test1_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Noun file upload
    file_upload_noun = mo.ui.file(label="Load nouns TSV")
    file_upload_noun
    return (file_upload_noun,)


@app.cell(hide_code=True)
def _(RAW_BASE, file_upload_noun, gu2, language_selector, notebook_dir, pd):
    # Load noun data
    if file_upload_noun.value:
        df_noun = gu2.load_data(file_upload_noun)
    else:
        _noun_fname = 'nouns_ru.tsv' if language_selector.value == 'ru' else 'nouns.tsv'
        _noun_path = gu2.ensure_file(_noun_fname, nb_dir=notebook_dir, remote_base=RAW_BASE) or gu2.ensure_file("nouns.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
        df_noun = pd.read_csv(_noun_path, sep='\t') if _noun_path else None
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, language_selector, mo, t_ui):
    # Noun table
    table_noun = mo.ui.table(df_noun, selection="multi", initial_selection=None) if df_noun is not None else None
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
    # Noun indefinite-article toggle (creation only -- no dependency on
    # mode_selector_n, so switching modes doesn't reset it back to False)
    indefinite_toggle_n = mo.ui.switch(label=t_ui("indefinite_label", language_selector.value), value=False)
    return (indefinite_toggle_n,)


@app.cell(hide_code=True)
def _(indefinite_toggle_n, mo, mode_selector_n):
    # Noun indefinite-article toggle (conditional display: only meaningful
    # once the article itself is being tested)
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
    return (
        captured_noun,
        enter_count_n,
        entered_noun,
        hist_noun,
        next_count_n,
        noun_msg,
        prev_count_n,
        restart_count_n,
        set_captured_noun,
        set_enter_count_n,
        set_entered_noun,
        set_hist_noun,
        set_next_count_n,
        set_noun_msg,
        set_prev_count_n,
        set_restart_count_n,
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
def _(
    captured_noun,
    check_btn_n,
    cv_noun,
    enter_count_n,
    entered_noun,
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
    set_captured_noun,
    set_enter_count_n,
    set_entered_noun,
    set_hist_noun,
    set_next_count_n,
    set_noun_msg,
    set_prev_count_n,
    set_restart_count_n,
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
    ) if words_noun else mo.md(t_ui("noun_empty", _lang))
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 2 heading
    mo.md(t_ui("test2_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Verb file upload
    file_upload_verb = mo.ui.file(label="Load verbs TSV")
    file_upload_verb
    return (file_upload_verb,)


@app.cell(hide_code=True)
def _(RAW_BASE, file_upload_verb, gu2, language_selector, notebook_dir, pd):
    # Load verb data
    if file_upload_verb.value:
        df_verb = gu2.load_data(file_upload_verb)
    else:
        _verb_fname = 'verbs_ru.tsv' if language_selector.value == 'ru' else 'verbs.tsv'
        _verb_path = gu2.ensure_file(_verb_fname, nb_dir=notebook_dir, remote_base=RAW_BASE) or gu2.ensure_file("verbs.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
        df_verb = pd.read_csv(_verb_path, sep='\t') if _verb_path else None
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, language_selector, mo, t_ui):
    # Verb table
    table_verb = mo.ui.table(df_verb, selection="multi", initial_selection=None) if df_verb is not None else None
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
    return (
        captured_verb,
        enter_count_v,
        entered_verb,
        hist_verb,
        next_count_v,
        prev_count_v,
        restart_count_v,
        set_captured_verb,
        set_enter_count_v,
        set_entered_verb,
        set_hist_verb,
        set_next_count_v,
        set_prev_count_v,
        set_restart_count_v,
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
def _(
    captured_verb,
    check_btn_v,
    cv_verb,
    enter_count_v,
    entered_verb,
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
    set_captured_verb,
    set_enter_count_v,
    set_entered_verb,
    set_hist_verb,
    set_next_count_v,
    set_prev_count_v,
    set_restart_count_v,
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
        )
    elif not words_verb:
        _output = mo.md(t_ui("verb_empty", _lang))
    else:
        _output = mo.md(t_ui("verb_no_tense", _lang))
    _output
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 3 heading
    mo.md(t_ui("test3_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Adjective file upload
    file_upload_adj = mo.ui.file(label="Load adjectives TSV")
    file_upload_adj
    return (file_upload_adj,)


@app.cell(hide_code=True)
def _(RAW_BASE, file_upload_adj, gu2, language_selector, notebook_dir, pd):
    # Load adjective data
    if file_upload_adj.value:
        df_adj = gu2.load_data(file_upload_adj)
    else:
        _adj_fname = 'adjectives_ru.tsv' if language_selector.value == 'ru' else 'adjectives.tsv'
        _adj_path = gu2.ensure_file(_adj_fname, nb_dir=notebook_dir, remote_base=RAW_BASE) or gu2.ensure_file("adjectives.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
        df_adj = pd.read_csv(_adj_path, sep='\t') if _adj_path else None
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, language_selector, mo, t_ui):
    # Adjective table
    table_adj = mo.ui.table(df_adj, selection="multi", initial_selection=None) if df_adj is not None else None
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
    return (
        adj_msg,
        captured_adj,
        enter_count_a,
        entered_adj,
        hist_adj,
        next_count_a,
        prev_count_a,
        restart_count_a,
        set_adj_msg,
        set_captured_adj,
        set_enter_count_a,
        set_entered_adj,
        set_hist_adj,
        set_next_count_a,
        set_prev_count_a,
        set_restart_count_a,
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
    _entered_adj_form = entered_adj().get(cv_adj["Word"]) if cv_adj else None
    adj_form, prev_btn_a, next_btn_a, restart_btn_a = gu2.paradigm_drill_widgets(
        labels=gu2.adjective_slot_labels(_mode, lang=language_selector.value),
        values=_entered_adj_form,
        history_len=len(hist_adj()),
        remaining_len=len(words4test_adj()),
        lang=language_selector.value,
    )
    set_prev_count_a(0)
    set_next_count_a(0)
    set_enter_count_a(0)
    return adj_form, cv_adj, next_btn_a, prev_btn_a, restart_btn_a


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
def _(
    adj_form,
    adj_msg,
    captured_adj,
    check_btn_a,
    cv_adj,
    enter_count_a,
    entered_adj,
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
    set_adj_msg,
    set_captured_adj,
    set_enter_count_a,
    set_entered_adj,
    set_hist_adj,
    set_next_count_a,
    set_prev_count_a,
    set_restart_count_a,
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
        mode=_mode,
        word_key="Word",
        meaning_key="Translation",
        meaning_label=t_ui("translation_label", _lang).rstrip(":"),
        title=t_ui("adj_heading", _lang),
        done_message=t_ui("test3_done", _lang),
    ) if words_adj else mo.md(t_ui("adj_empty", _lang))
    return


@app.cell(hide_code=True)
def _(gu2):
    t_ui = gu2.ui_label
    return (t_ui,)


@app.cell(hide_code=True)
def _(mo):
    from eee_project import language_bridge
    lang_bridge = language_bridge(mo)
    lang_bridge
    return (lang_bridge,)


@app.cell(hide_code=True)
def _(lang_bridge, mo):
    # Language selector
    from eee_project import language_selector as _language_selector
    language_selector = _language_selector(mo, lang_bridge)
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
        f"{_ROOT}/modern_greek/ellinika_b/index.tsv",
    )
    _prev_url, _next_url = _cfg.adjacent_urls("chapter_03/")
    eee_footer(mo, lang=language_selector.value, prev_url=_prev_url, next_url=_next_url, same_window=True)
    return


@app.cell(hide_code=True)
def _():
    # Imports
    import os
    import random
    import pandas as pd
    import marimo as mo
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    RAW_BASE = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/modern_greek/ellinika_b/chapter_03"
    return RAW_BASE, mo, notebook_dir, pd, random


@app.cell(hide_code=True)
def _():
    # Modern Greek eee_project: imports
    import eee_project as eee
    from eee_project import GreekUtils, MODERN_GREEK
    from modern_greek_backend_eee import ModernGreekBackend

    return GreekUtils, MODERN_GREEK, ModernGreekBackend, eee


@app.cell(hide_code=True)
def _(GreekUtils, MODERN_GREEK, ModernGreekBackend, eee, mo, pd):
    # Modern Greek eee_project: backend setup
    _mg_backend = ModernGreekBackend()
    eee.register_backend("el", _mg_backend, backend="modern-greek")
    eee.set_chain("el", ["modern-greek"])
    gu2 = GreekUtils(_mg_backend, mo, pd, eee_module=eee, config=MODERN_GREEK)
    return (gu2,)


if __name__ == "__main__":
    app.run()
