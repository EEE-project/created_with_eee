# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project>=1.10.0",
#     "marimo>=0.23.14",
#     "modern-greek-backend-eee>=1.0.0",
#     "pandas",
# ]
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", html_head_file="head.html")


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
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_EDUnXkowen3RAuckrYhYUb)"
    if _lang == "ru":
        _out = mo.md(f"""
    # «Πάμε διακοπές;» ✈️
    ## Глава 11 — Поедем в отпуск? · B1 {_badge}

    **Грамматика:** Простое сослагательное (Απλή Υποτακτική) · Условные и уступительные предложения
    **Тесты:** Существительные · Глаголы · Прилагательные
    """)
    elif _lang == "el":
        _out = mo.md(f"""
    # «Πάμε διακοπές;» ✈️
    ## Ενότητα 11 — Πάμε διακοπές; · B1 {_badge}

    **Γραμματική:** Απλή Υποτακτική · Υποθετικές και Εναντιωματικές προτάσεις
    **Τεστ:** Ουσιαστικά · Ρήματα · Επίθετα
    """)
    else:
        _out = mo.md(f"""
    # «Πάμε διακοπές;» ✈️
    ## Unit 11 — Shall We Go on Holiday? · B1 {_badge}

    **Grammar:** Simple Subjunctive (Απλή Υποτακτική) · Conditional & Concessive Clauses
    **Tests:** Nouns · Verbs · Adjectives
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Vocabulary: Λέξεις, λέξεις
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Словарь (Λέξεις, λέξεις)

    | Греческий | Русский |
    |:----------|:--------|
    | η άδεια | отпуск |
    | η άνεση | удобство, комфорт |
    | το αξιοθέατο | достопримечательность |
    | το δεκαήμερο | десятидневный период |
    | το δεκαπενθήμερο | двухнедельный период |
    | ο Δεκαπενταύγουστος | Успение Богородицы (15 августа) |
    | η διαμονή | проживание |
    | η διασκέδαση | развлечение |
    | το δρομολόγιο | расписание, маршрут |
    | η προσφορά | предложение, скидка |
    | η κρουαζιέρα | круиз |
    | η βαλίτσα | чемодан |
    | η πτήση | рейс |
    | η αναχώρηση | отправление |
    | η άφιξη | прибытие |
    | η καθυστέρηση | задержка |
    | το εισιτήριο | билет |
    | η φασαρία | шум, суета |
    | η ησυχία | тишина, покой |
    | το κάμπινγκ | кемпинг |
    | η σκηνή | палатка |
    | το καταφύγιο | убежище, приют |
    | η πανσιόν | пансион |
    | το ξενοδοχείο | отель |
    | η κράτηση | бронирование |
    | χαλαρώνω | отдыхать, расслабляться |
    | οργανώνω | организовывать |
    | ταξιδεύω | путешествовать |
    | κάνω κράτηση δωματίου | бронировать номер |
    | κλείνω εισιτήρια | бронировать билеты |
    | οι τιμές ανεβαίνουν ≠ πέφτουν | цены растут ≠ падают |
    | δεν κλείνω μάτι | не сомкнуть глаз |
    | εντυπωσιακός, -ή, -ό | впечатляющий |
    | ερημικός, -ή, -ό | безлюдный, отдалённый |
    | οικονομικός, -ή, -ό | экономичный, доступный |
    | πανέμορφος, -η, -ο | прекрасный |
    | υπέροχος, -η, -ο | великолепный |
    | ικανοποιημένος, -η, -ο | довольный |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Λεξιλόγιο

    | Ελληνικά | Αγγλικά |
    |:---------|:--------|
    | η άδεια | vacation, leave |
    | η άνεση | comfort, ease |
    | το αξιοθέατο | attraction, sight |
    | το δεκαήμερο | ten-day period |
    | το δεκαπενθήμερο | two-week period |
    | ο Δεκαπενταύγουστος | Feast of the Dormition (August 15th) |
    | η διαμονή | accommodation, stay |
    | η διασκέδαση | entertainment, fun |
    | το δρομολόγιο | schedule, timetable |
    | η προσφορά | offer, deal, discount |
    | η κρουαζιέρα | cruise |
    | η βαλίτσα | suitcase |
    | η πτήση | flight |
    | η αναχώρηση | departure |
    | η άφιξη | arrival |
    | η καθυστέρηση | delay |
    | το εισιτήριο | ticket |
    | η φασαρία | noise, fuss, trouble |
    | η ησυχία | quiet, peace, silence |
    | το κάμπινγκ | camping |
    | η σκηνή | tent |
    | το καταφύγιο | shelter, refuge |
    | η πανσιόν | pension, guesthouse |
    | το ξενοδοχείο | hotel |
    | η κράτηση | reservation, booking |
    | χαλαρώνω | to relax |
    | οργανώνω | to organize |
    | ταξιδεύω | to travel |
    | κάνω κράτηση δωματίου | to make a room reservation |
    | κλείνω εισιτήρια | to book tickets |
    | οι τιμές ανεβαίνουν ≠ πέφτουν | prices go up ≠ fall |
    | δεν κλείνω μάτι | I don't sleep a wink |
    | εντυπωσιακός, -ή, -ό | impressive |
    | ερημικός, -ή, -ό | deserted, remote |
    | οικονομικός, -ή, -ό | economical, affordable |
    | πανέμορφος, -η, -ο | beautiful, gorgeous |
    | υπέροχος, -η, -ο | wonderful, excellent |
    | ικανοποιημένος, -η, -ο | satisfied, pleased |
    """)
    else:
        _out = mo.md("""
    ## Vocabulary

    | Greek | English |
    |:------|:--------|
    | η άδεια | vacation, leave |
    | η άνεση | comfort, ease |
    | το αξιοθέατο | attraction, sight |
    | το δεκαήμερο | ten-day period |
    | το δεκαπενθήμερο | two-week period |
    | ο Δεκαπενταύγουστος | Feast of the Dormition (August 15th) |
    | η διαμονή | accommodation, stay |
    | η διασκέδαση | entertainment, fun |
    | το δρομολόγιο | schedule, timetable |
    | η προσφορά | offer, deal, discount |
    | η κρουαζιέρα | cruise |
    | η βαλίτσα | suitcase |
    | η πτήση | flight |
    | η αναχώρηση | departure |
    | η άφιξη | arrival |
    | η καθυστέρηση | delay |
    | το εισιτήριο | ticket |
    | η φασαρία | noise, fuss, trouble |
    | η ησυχία | quiet, peace, silence |
    | το κάμπινγκ | camping |
    | η σκηνή | tent |
    | το καταφύγιο | shelter, refuge |
    | η πανσιόν | pension, guesthouse |
    | το ξενοδοχείο | hotel |
    | η κράτηση | reservation, booking |
    | χαλαρώνω | to relax |
    | οργανώνω | to organize |
    | ταξιδεύω | to travel |
    | κάνω κράτηση δωματίου | to make a room reservation |
    | κλείνω εισιτήρια | to book tickets |
    | οι τιμές ανεβαίνουν ≠ πέφτουν | prices go up ≠ fall |
    | δεν κλείνω μάτι | I don't sleep a wink |
    | εντυπωσιακός, -ή, -ό | impressive |
    | ερημικός, -ή, -ό | deserted, remote |
    | οικονομικός, -ή, -ό | economical, affordable |
    | πανέμορφος, -η, -ο | beautiful, gorgeous |
    | υπέροχος, -η, -ο | wonderful, excellent |
    | ικανοποιημένος, -η, -ο | satisfied, pleased |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Simple Subjunctive — when to use
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика: Простое сослагательное наклонение (Απλή Υποτακτική)

    Απλή Υποτακτική использует **ту же основу, что и Простое будущее**, но с **να** или **ας** вместо **θα**.

    > θα αγοράσω (Простое будущее) → **να αγοράσω** (Υποτακτική)

    ### Когда используется

    | Греческий | Русский | Пример |
    |:------|:--------|:--------|
    | **Θέλω / θα ήθελα** | хочу | Θέλω **να κάνω** ένα ταξίδι. |
    | **Πρέπει** | нужно / должен | Πρέπει **να ψάξουμε** για δωμάτιο. |
    | **Πρόκειται** | собираюсь | Πρόκειται **να πάω** στην Ιαπωνία. |
    | **Μπορεί** | может быть | Μπορεί **να μη βρούμε** εισιτήρια. |
    | **Μπορώ** | могу | Δεν μπορώ **να έρθω** μαζί σας. |
    | **Ελπίζω** | надеюсь | Ελπίζω **να έρθετε** μαζί μας. |
    | **Λέω** | думаю / собираюсь | Λέω **να πάω** διακοπές στη Νάξο. |
    | **Προτιμώ** | предпочитаю | Προτιμώ **να μη φάω** τώρα. |
    | **Προτείνω** | предлагаю | Προτείνω **να πάμε** στο Μαρόκο. |
    | **Σκοπεύω** | намереваюсь | Σκοπεύω **να μείνω** αρκετό καιρό. |
    | **Είναι ανάγκη** | необходимо | Είναι ανάγκη **να σε δω** σήμερα. |
    | **Είναι ώρα** | пора | Είναι ώρα **να φύγω**. |
    | **χωρίς να** | без того чтобы | Γιατί έκλεισες εισιτήρια **χωρίς να** με ρωτήσεις; |
    | **ας** | пусть / давайте | **Ας πάμε** όλοι μαζί! / **Ας φύγει**. |

    **Отрицание:** Λέω **να μη** βγούμε. / Σκέφτομαι **να μην** πάω πουθενά.
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Γραμματική: Απλή Υποτακτική

    Η Απλή Υποτακτική χρησιμοποιεί **το ίδιο θέμα με τον Απλό Μέλλοντα**, αλλά με **να** ή **ας** αντί για **θα**.

    > θα αγοράσω (Απλός Μέλλοντας) → **να αγοράσω** (Υποτακτική)

    ### Πότε χρησιμοποιείται

    | Ελληνικά | Αγγλικά | Παράδειγμα |
    |:------|:--------|:--------|
    | **Θέλω / θα ήθελα** | I want | Θέλω **να κάνω** ένα ταξίδι. |
    | **Πρέπει** | I/you must | Πρέπει **να ψάξουμε** για δωμάτιο. |
    | **Πρόκειται** | I'm going to | Πρόκειται **να πάω** στην Ιαπωνία. |
    | **Μπορεί** | maybe / it's possible | Μπορεί **να μη βρούμε** εισιτήρια. |
    | **Μπορώ** | I can | Δεν μπορώ **να έρθω** μαζί σας. |
    | **Ελπίζω** | I hope | Ελπίζω **να έρθετε** μαζί μας. |
    | **Λέω** | I'm thinking of | Λέω **να πάω** διακοπές στη Νάξο. |
    | **Προτιμώ** | I prefer | Προτιμώ **να μη φάω** τώρα. |
    | **Προτείνω** | I suggest | Προτείνω **να πάμε** στο Μαρόκο. |
    | **Σκοπεύω** | I intend | Σκοπεύω **να μείνω** αρκετό καιρό. |
    | **Είναι ανάγκη** | it's necessary | Είναι ανάγκη **να σε δω** σήμερα. |
    | **Είναι ώρα** | it's time | Είναι ώρα **να φύγω**. |
    | **χωρίς να** | without | Γιατί έκλεισες εισιτήρια **χωρίς να** με ρωτήσεις; |
    | **ας** | let's / let him | **Ας πάμε** όλοι μαζί! / **Ας φύγει**. |

    **Άρνηση:** Λέω **να μη** βγούμε. / Σκέφτομαι **να μην** πάω πουθενά.
    """)
    else:
        _out = mo.md("""
    ## Grammar: Simple Subjunctive (Απλή Υποτακτική)

    The Simple Subjunctive uses **the same stem as the Simple Future**, but with **να** or **ας** instead of **θα**.

    > θα αγοράσω (Simple Future) → **να αγοράσω** (Simple Subjunctive)

    ### When to use

    | Greek | English | Example |
    |:------|:--------|:--------|
    | **Θέλω / θα ήθελα** | I want | Θέλω **να κάνω** ένα ταξίδι. |
    | **Πρέπει** | I/you must | Πρέπει **να ψάξουμε** για δωμάτιο. |
    | **Πρόκειται** | I'm going to | Πρόκειται **να πάω** στην Ιαπωνία. |
    | **Μπορεί** | maybe / it's possible | Μπορεί **να μη βρούμε** εισιτήρια. |
    | **Μπορώ** | I can | Δεν μπορώ **να έρθω** μαζί σας. |
    | **Ελπίζω** | I hope | Ελπίζω **να έρθετε** μαζί μας. |
    | **Λέω** | I'm thinking of | Λέω **να πάω** διακοπές στη Νάξο. |
    | **Προτιμώ** | I prefer | Προτιμώ **να μη φάω** τώρα. |
    | **Προτείνω** | I suggest | Προτείνω **να πάμε** στο Μαρόκο. |
    | **Σκοπεύω** | I intend | Σκοπεύω **να μείνω** αρκετό καιρό. |
    | **Είναι ανάγκη** | it's necessary | Είναι ανάγκη **να σε δω** σήμερα. |
    | **Είναι ώρα** | it's time | Είναι ώρα **να φύγω**. |
    | **χωρίς να** | without | Γιατί έκλεισες εισιτήρια **χωρίς να** με ρωτήσεις; |
    | **ας** | let's / let him | **Ας πάμε** όλοι μαζί! / **Ας φύγει**. |

    **Negation:** Λέω **να μη** βγούμε. / Σκέφτομαι **να μην** πάω πουθενά.
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Formation
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Образование Υποτακτικής

    | Тип А | | Тип Б1 / Б2 | |
    |:-------|:-|:-------------|:-|
    | **-νω → -σω** | πληρώνω → **να πληρώσω**, αγοράζω → **να αγοράσω** | **-ήσω** | μιλάω → **να μιλήσω**, τηλεφωνώ → **να τηλεφωνήσω** |
    | **-ζω/-γω/-χω/-χνω/-κω/-σκω → -ξω** | κοιτάζω → **να κοιτάξω**, ανοίγω → **να ανοίξω** | **-άσω** | γελάω → **να γελάσω**, ξεχνάω → **να ξεχάσω** |
    | **-εύω/-πω/-φω/-βω → -ψω** | δουλεύω → **να δουλέψω**, γράφω → **να γράψω** | **-έσω** | φοράω → **να φορέσω**, μπορώ → **να μπορέσω** |
    | | | **-ήξω / -άξω** | τραβάω → **να τραβήξω**, πετάω → **να πετάξω** |

    ### Спряжение: να αγοράσω

    | | | | |
    |:--|:--|:--|:--|
    | εγώ | **να αγοράσω** | εμείς | **να αγοράσουμε** |
    | εσύ | **να αγοράσεις** | εσείς | **να αγοράσετε** |
    | αυτός/ή/ό | **να αγοράσει** | αυτοί/ές/ά | **να αγοράσουν(ε)** |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Σχηματισμός της Απλής Υποτακτικής

    | Τύπος Α | | Τύπος Β1 / Β2 | |
    |:-------|:-|:-------------|:-|
    | **-νω → -σω** | πληρώνω → **να πληρώσω**, αγοράζω → **να αγοράσω** | **-ήσω** | μιλάω → **να μιλήσω**, τηλεφωνώ → **να τηλεφωνήσω** |
    | **-ζω/-γω/-χω/-χνω/-κω/-σκω → -ξω** | κοιτάζω → **να κοιτάξω**, ανοίγω → **να ανοίξω** | **-άσω** | γελάω → **να γελάσω**, ξεχνάω → **να ξεχάσω** |
    | **-εύω/-πω/-φω/-βω → -ψω** | δουλεύω → **να δουλέψω**, γράφω → **να γράψω** | **-έσω** | φοράω → **να φορέσω**, μπορώ → **να μπορέσω** |
    | | | **-ήξω / -άξω** | τραβάω → **να τραβήξω**, πετάω → **να πετάξω** |

    ### Κλίση: να αγοράσω

    | | | | |
    |:--|:--|:--|:--|
    | εγώ | **να αγοράσω** | εμείς | **να αγοράσουμε** |
    | εσύ | **να αγοράσεις** | εσείς | **να αγοράσετε** |
    | αυτός/ή/ό | **να αγοράσει** | αυτοί/ές/ά | **να αγοράσουν(ε)** |
    """)
    else:
        _out = mo.md("""
    ## Formation of the Simple Subjunctive

    | Type A | | Type B1 / B2 | |
    |:-------|:-|:-------------|:-|
    | **-νω → -σω** | πληρώνω → **να πληρώσω**, αγοράζω → **να αγοράσω** | **-ήσω** | μιλάω → **να μιλήσω**, τηλεφωνώ → **να τηλεφωνήσω** |
    | **-ζω/-γω/-χω/-χνω/-κω/-σκω → -ξω** | κοιτάζω → **να κοιτάξω**, ανοίγω → **να ανοίξω** | **-άσω** | γελάω → **να γελάσω**, ξεχνάω → **να ξεχάσω** |
    | **-εύω/-πω/-φω/-βω → -ψω** | δουλεύω → **να δουλέψω**, γράφω → **να γράψω** | **-έσω** | φοράω → **να φορέσω**, μπορώ → **να μπορέσω** |
    | | | **-ήξω / -άξω** | τραβάω → **να τραβήξω**, πετάω → **να πετάξω** |

    ### Conjugation: να αγοράσω

    | | | | |
    |:--|:--|:--|:--|
    | εγώ | **να αγοράσω** | εμείς | **να αγοράσουμε** |
    | εσύ | **να αγοράσεις** | εσείς | **να αγοράσετε** |
    | αυτός/ή/ό | **να αγοράσει** | αυτοί/ές/ά | **να αγοράσουν(ε)** |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Irregular verbs
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Неправильные формы (Ανώμαλα ρήματα)

    | Словарная форма | Υποτακτική | | Словарная форма | Υποτακτική |
    |:----------------|:------------|:|:----------------|:------------|
    | ανεβαίνω | **να ανέβω** | | λέω | **να πω** |
    | βγαίνω | **να βγω** | | μαθαίνω | **να μάθω** |
    | βλέπω | **να δω** | | μένω | **να μείνω** |
    | βρίσκω | **να βρω** | | μπαίνω | **να μπω** |
    | βάζω | **να βάλω** | | παίρνω | **να πάρω** |
    | βγάζω | **να βγάλω** | | πηγαίνω | **να πάω** |
    | δίνω | **να δώσω** | | πίνω | **να πιω** |
    | είμαι | **να είμαι** | | στέλνω | **να στείλω** |
    | έχω | **να έχω** | | τρώω | **να φάω** |
    | κάνω | **να κάνω** | | φέρνω | **να φέρω** |
    | κατεβαίνω | **να κατέβω** | | φεύγω | **να φύγω** |
    | κλαίω | **να κλάψω** | | έρχομαι | **να έρθω** |
    | ξέρω | **να ξέρω** | | γίνομαι | **να γίνω** |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Ανώμαλα ρήματα

    | Λεξικός τύπος | Υποτακτική | | Λεξικός τύπος | Υποτακτική |
    |:----------------|:------------|:|:----------------|:------------|
    | ανεβαίνω | **να ανέβω** | | λέω | **να πω** |
    | βγαίνω | **να βγω** | | μαθαίνω | **να μάθω** |
    | βλέπω | **να δω** | | μένω | **να μείνω** |
    | βρίσκω | **να βρω** | | μπαίνω | **να μπω** |
    | βάζω | **να βάλω** | | παίρνω | **να πάρω** |
    | βγάζω | **να βγάλω** | | πηγαίνω | **να πάω** |
    | δίνω | **να δώσω** | | πίνω | **να πιω** |
    | είμαι | **να είμαι** | | στέλνω | **να στείλω** |
    | έχω | **να έχω** | | τρώω | **να φάω** |
    | κάνω | **να κάνω** | | φέρνω | **να φέρω** |
    | κατεβαίνω | **να κατέβω** | | φεύγω | **να φύγω** |
    | κλαίω | **να κλάψω** | | έρχομαι | **να έρθω** |
    | ξέρω | **να ξέρω** | | γίνομαι | **να γίνω** |
    """)
    else:
        _out = mo.md("""
    ## Key Irregular Forms (Ανώμαλα ρήματα)

    | Dictionary form | Subjunctive | | Dictionary form | Subjunctive |
    |:----------------|:------------|:|:----------------|:------------|
    | ανεβαίνω | **να ανέβω** | | λέω | **να πω** |
    | βγαίνω | **να βγω** | | μαθαίνω | **να μάθω** |
    | βλέπω | **να δω** | | μένω | **να μείνω** |
    | βρίσκω | **να βρω** | | μπαίνω | **να μπω** |
    | βάζω | **να βάλω** | | παίρνω | **να πάρω** |
    | βγάζω | **να βγάλω** | | πηγαίνω | **να πάω** |
    | δίνω | **να δώσω** | | πίνω | **να πιω** |
    | είμαι | **να είμαι** | | στέλνω | **να στείλω** |
    | έχω | **να έχω** | | τρώω | **να φάω** |
    | κάνω | **να κάνω** | | φέρνω | **να φέρω** |
    | κατεβαίνω | **να κατέβω** | | φεύγω | **να φύγω** |
    | κλαίω | **να κλάψω** | | έρχομαι | **να έρθω** |
    | ξέρω | **να ξέρω** | | γίνομαι | **να γίνω** |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Conditional sentences
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Условные предложения (Υποθετικές προτάσεις — Τύπος Α)

    **Αν** вводит условие. Глагол после **αν** использует основу Простого будущего **без θα**.

    | Условие | Следствие | Перевод |
    |:--------|:-------|:--------|
    | **Αν** *έρθετε* στην Ελλάδα τον Ιούνιο, | *θα βρείτε* κάτι καλό και οικονομικό. | Если вы приедете в Грецию в июне, вы найдёте что-то хорошее и недорогое. |
    | **Αν** *έρθετε* στο νησί, | *να σας φιλοξενήσουμε*. | Если вы приедете на остров, дайте нам вас принять. |
    | **Αν** δε *βρείτε* δωμάτιο στην πόλη, | *να ψάξετε* στα γύρω χωριά. | Если вы не найдёте комнату в городе, поищите в окрестных деревнях. |

    Придаточное следствия: Простое будущее (θα) или Υποτακτική (να).
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Υποθετικές προτάσεις (Τύπος Α)

    Το **αν** εισάγει μια υπόθεση. Το ρήμα μετά το **αν** χρησιμοποιεί το θέμα του Απλού Μέλλοντα **χωρίς θα**.

    | Υπόθεση | Αποτέλεσμα | Μετάφραση |
    |:--------|:-------|:--------|
    | **Αν** *έρθετε* στην Ελλάδα τον Ιούνιο, | *θα βρείτε* κάτι καλό και οικονομικό. | If you come to Greece in June, you'll find something good and affordable. |
    | **Αν** *έρθετε* στο νησί, | *να σας φιλοξενήσουμε*. | If you come to the island, let us host you. |
    | **Αν** δε *βρείτε* δωμάτιο στην πόλη, | *να ψάξετε* στα γύρω χωριά. | If you don't find a room in the town, look in the surrounding villages. |

    Η πρόταση αποτελέσματος: Απλός Μέλλοντας (θα) ή Υποτακτική (να).
    """)
    else:
        _out = mo.md("""
    ## Conditional Sentences (Υποθετικές προτάσεις — Τύπος Α)

    **Αν** introduces a condition. The verb after **αν** uses the Simple Future stem **without θα**.

    | Condition | Result | Translation |
    |:----------|:-------|:-------------|
    | **Αν** *έρθετε* στην Ελλάδα τον Ιούνιο, | *θα βρείτε* κάτι καλό και οικονομικό. | If you come to Greece in June, you'll find something good and affordable. |
    | **Αν** *έρθετε* στο νησί, | *να σας φιλοξενήσουμε*. | If you come to the island, let us host you. |
    | **Αν** δε *βρείτε* δωμάτιο στην πόλη, | *να ψάξετε* στα γύρω χωριά. | If you don't find a room in the town, look in the surrounding villages. |

    Result clause: Simple Future (θα) or Subjunctive (να).
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Concessive clauses
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Уступительные предложения (Εναντιωματικές προτάσεις)

    **Αν και** и **ενώ** = «хотя / несмотря на то что»:

    | Греческий | Русский |
    |:------|:--------|
    | **Αν και** η Σαντορίνη έχει πολύ κόσμο αυτή την εποχή, περνάμε υπέροχα. | Хотя на Санторини в это время много народу, нам очень хорошо. |
    | **Αν και / Ενώ** δεν είχαν πολλά χρήματα μαζί τους, πέρασαν πολύ καλά στις διακοπές. | Хотя у них с собой было мало денег, они отлично провели отпуск. |

    > **Αν και** = хотя (уступительное) — не путать с **Αν** (если — условное)
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Εναντιωματικές προτάσεις

    **Αν και** και **ενώ** = «αν και / παρόλο που»:

    | Ελληνικά | Μετάφραση |
    |:------|:--------|
    | **Αν και** η Σαντορίνη έχει πολύ κόσμο αυτή την εποχή, περνάμε υπέροχα. | Although Santorini is very crowded at this time, we're having a great time. |
    | **Αν και / Ενώ** δεν είχαν πολλά χρήματα μαζί τους, πέρασαν πολύ καλά στις διακοπές. | Although they didn't have much money with them, they had a great holiday. |

    > **Αν και** = εναντιωματικό — μη συγχέεις με **Αν** = υποθετικό
    """)
    else:
        _out = mo.md("""
    ## Concessive Clauses (Εναντιωματικές προτάσεις)

    **Αν και** and **ενώ** mean "although / even though":

    | Greek | English |
    |:------|:--------|
    | **Αν και** η Σαντορίνη έχει πολύ κόσμο αυτή την εποχή, περνάμε υπέροχα. | Although Santorini is very crowded at this time, we're having a great time. |
    | **Αν και / Ενώ** δεν είχαν πολλά χρήματα μαζί τους, πέρασαν πολύ καλά στις διακοπές. | Although they didn't have much money with them, they had a great holiday. |

    > **Αν και** = although (concessive) — do not confuse with **Αν** (if — conditional)
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Key phrases: Πώς το λένε;
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Разговорные фразы (Πώς το λένε;)

    | Греческий | Русский |
    |:----------|:--------|
    | Ένα τέτοιο ταξίδι είναι το όνειρό μου! | Такое путешествие — моя мечта! |
    | Θέλουμε να χαλαρώσουμε, χωρίς να πληρώσουμε μια περιουσία. | Хотим отдохнуть, не потратив целое состояние. |
    | Καιρό είχαμε να τα πούμε. | Давно не разговаривали. |
    | Αξίζει! | Стоит того! |
    | Παίρνω το πλοίο της γραμμής. | Еду на рейсовом пароме. |
    | Θα σας έρθει πολύ πιο φτηνά. | Вам это обойдётся намного дешевле. |
    | Να αποφασίσετε όσο το δυνατόν πιο γρήγορα. | Решайте как можно быстрее. |
    | Μου λείπει η Αθήνα. | Я скучаю по Афинам. |
    | Τον Δεκαπενταύγουστο γίνεται χαμός. | На 15 августа творится настоящий хаос. |
    | Δε βρίσκεις χώρο ούτε να καθίσεις. | Нет места даже сесть. |
    | Δεν μπορέσαμε να κλείσουμε μάτι όλη τη νύχτα. | Мы не сомкнули глаз всю ночь. |
    | Εμείς θέλουμε την ησυχία μας. | Нам нужна тишина и покой. |
    | Κατά τα άλλα... | В остальном... |
    | Καλή διαμονή σάς εύχομαι. | Желаю вам приятного пребывания. |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Πώς το λένε;

    | Ελληνικά | Αγγλικά |
    |:---------|:--------|
    | Ένα τέτοιο ταξίδι είναι το όνειρό μου! | A trip like that is my dream! |
    | Θέλουμε να χαλαρώσουμε, χωρίς να πληρώσουμε μια περιουσία. | We want to relax without spending a fortune. |
    | Καιρό είχαμε να τα πούμε. | It's been a while since we talked. |
    | Αξίζει! | It's worth it! |
    | Παίρνω το πλοίο της γραμμής. | I'm taking the regular ferry. |
    | Θα σας έρθει πολύ πιο φτηνά. | It will cost you much less. |
    | Να αποφασίσετε όσο το δυνατόν πιο γρήγορα. | Decide as quickly as possible. |
    | Μου λείπει η Αθήνα. | I miss Athens. |
    | Τον Δεκαπενταύγουστο γίνεται χαμός. | On August 15th it gets crazy busy. |
    | Δε βρίσκεις χώρο ούτε να καθίσεις. | You can't find a place even to sit. |
    | Δεν μπορέσαμε να κλείσουμε μάτι όλη τη νύχτα. | We couldn't sleep a wink all night. |
    | Εμείς θέλουμε την ησυχία μας. | We want our peace and quiet. |
    | Κατά τα άλλα... | Apart from that... / Otherwise... |
    | Καλή διαμονή σάς εύχομαι. | I wish you a pleasant stay. |
    """)
    else:
        _out = mo.md("""
    ## Useful Phrases (Πώς το λένε;)

    | Greek | English |
    |:------|:--------|
    | Ένα τέτοιο ταξίδι είναι το όνειρό μου! | A trip like that is my dream! |
    | Θέλουμε να χαλαρώσουμε, χωρίς να πληρώσουμε μια περιουσία. | We want to relax without spending a fortune. |
    | Καιρό είχαμε να τα πούμε. | It's been a while since we talked. |
    | Αξίζει! | It's worth it! |
    | Παίρνω το πλοίο της γραμμής. | I'm taking the regular ferry. |
    | Θα σας έρθει πολύ πιο φτηνά. | It will cost you much less. |
    | Να αποφασίσετε όσο το δυνατόν πιο γρήγορα. | Decide as quickly as possible. |
    | Μου λείπει η Αθήνα. | I miss Athens. |
    | Τον Δεκαπενταύγουστο γίνεται χαμός. | On August 15th it gets crazy busy. |
    | Δε βρίσκεις χώρο ούτε να καθίσεις. | You can't find a place even to sit. |
    | Δεν μπορέσαμε να κλείσουμε μάτι όλη τη νύχτα. | We couldn't sleep a wink all night. |
    | Εμείς θέλουμε την ησυχία μας. | We want our peace and quiet. |
    | Κατά τα άλλα... | Apart from that... / Otherwise... |
    | Καλή διαμονή σάς εύχομαι. | I wish you a pleasant stay. |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Pronunciation cell
    _lang = language_selector.value
    if _lang == 'ru':
        _out = mo.md("""
    ### Произношение: Φωνή-γραφή (стр. 184)

    **Упражнение B15, «Что я слышу? Выбираю правильное»**: упражнение на различение похожих форм Υποτακτικής РАЗНЫХ глаголов на слух (по структуре аналогично минимальным парам аориста из Главы 6, стр. 102). Пары как в книге:

    1. Σκεφτόμαστε **να 'ρθούμε**. / Σκεφτόμαστε **να δούμε**. ("Мы думаем прийти." / "Мы думаем посмотреть.")
    2. Προτείνω **να πάμε** με τρένο. / Προτιμώ **να πάμε** με τρένο. ("Я предлагаю поехать на поезде." / "Я предпочитаю поехать на поезде.")
    3. Λέω **να βρω**. / Λέω **να βγω**. ("Думаю найти." / "Думаю выйти.")
    4. **Να το συζητήσουμε**. / **Να το ζητήσουμε**. ("Давайте это обсудим." / "Давайте это попросим.")
    5. **Τι να πω**; / **Τι να πιω**; ("Что мне сказать?" / "Что мне выпить?")
    6. Λέω **να μην πάω**. / Λέω **να μην μπω**. ("Думаю не пойти." / "Думаю не войти.")
    """)
    elif _lang == 'el':
        _out = mo.md("""
    ### Φωνή-γραφή (σ. 184)

    **Άσκηση B15, «Τι ακούω; Διαλέγω το σωστό»**: άσκηση διάκρισης παρόμοιων τύπων της Υποτακτικής ΔΙΑΦΟΡΕΤΙΚΩΝ ρημάτων με το αυτί (ίδια λογική με τα ζευγάρια αορίστου του Κεφαλαίου 6, σ. 102). Ζευγάρια όπως στο βιβλίο:

    1. Σκεφτόμαστε **να 'ρθούμε**. / Σκεφτόμαστε **να δούμε**. ("We're thinking of coming." / "We're thinking of seeing [it].")
    2. Προτείνω **να πάμε** με τρένο. / Προτιμώ **να πάμε** με τρένο. ("I suggest we go by train." / "I prefer we go by train.")
    3. Λέω **να βρω**. / Λέω **να βγω**. ("I'm thinking of finding [it]." / "I'm thinking of going out.")
    4. **Να το συζητήσουμε**. / **Να το ζητήσουμε**. ("Let's discuss it." / "Let's ask for it.")
    5. **Τι να πω**; / **Τι να πιω**; ("What should I say?" / "What should I drink?")
    6. Λέω **να μην πάω**. / Λέω **να μην μπω**. ("I'm thinking of not going." / "I'm thinking of not entering.")
    """)
    else:
        _out = mo.md("""
    ### Pronunciation: Φωνή-γραφή (p. 184)

    **Exercise B15, "What do I hear? Choose the correct one"**: a listening-discrimination exercise between similar-sounding subjunctive forms of DIFFERENT verbs (structurally the same idea as Chapter 6's aorist minimal pairs, p. 102). Pairs as printed:

    1. Σκεφτόμαστε **να 'ρθούμε**. / Σκεφτόμαστε **να δούμε**. ("We're thinking of coming." / "We're thinking of seeing [it].")
    2. Προτείνω **να πάμε** με τρένο. / Προτιμώ **να πάμε** με τρένο. ("I suggest we go by train." / "I prefer we go by train.")
    3. Λέω **να βρω**. / Λέω **να βγω**. ("I'm thinking of finding [it]." / "I'm thinking of going out.")
    4. **Να το συζητήσουμε**. / **Να το ζητήσουμε**. ("Let's discuss it." / "Let's ask for it.")
    5. **Τι να πω**; / **Τι να πιω**; ("What should I say?" / "What should I drink?")
    6. Λέω **να μην πάω**. / Λέω **να μην μπω**. ("I'm thinking of not going." / "I'm thinking of not entering.")
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 1 heading
    mo.md(t_ui("test1_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, language_selector, notebook_dir):
    # Load noun data
    df_noun = gu2.load_vocab_table("nouns.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE, ru_variant=True, language=language_selector.value)
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, gu2, language_selector, mo, t_ui):
    # Noun table
    _lang = language_selector.value
    table_noun = gu2.vocab_table(df_noun)
    _display = table_noun if table_noun is not None else mo.md(t_ui("nouns_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_nouns", _lang)), _display])
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
def _(language_selector, mo, t_ui):
    # Test 2 heading
    mo.md(t_ui("test2_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, language_selector, notebook_dir):
    # Load verb data
    df_verb = gu2.load_vocab_table("verbs.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE, ru_variant=True, language=language_selector.value)
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, gu2, language_selector, mo, t_ui):
    # Verb table
    _lang = language_selector.value
    table_verb = gu2.vocab_table(df_verb)
    _display = table_verb if table_verb is not None else mo.md(t_ui("verbs_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_verbs", _lang)), _display])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu2, language_selector, mo, t_ui):
    # Tense selector
    _lang = language_selector.value
    _tense_options = gu2.tense_dropdown_options(lang=_lang)
    _default_tense = "future"
    _default_key = next((k for k, v in _tense_options.items() if v == _default_tense), next(iter(_tense_options)))
    tense_selector = mo.ui.dropdown(
        options=_tense_options,
        value=_default_key,
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
def _(language_selector, mo, t_ui):
    # Test 3 heading
    mo.md(t_ui("test3_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, language_selector, notebook_dir):
    # Load adj data
    df_adj = gu2.load_vocab_table("adjectives.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE, ru_variant=True, language=language_selector.value)
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, gu2, language_selector, mo, t_ui):
    # Adj table
    _lang = language_selector.value
    table_adj = gu2.vocab_table(df_adj)
    _display = table_adj if table_adj is not None else mo.md(t_ui("adjs_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_adjs", _lang)), _display])
    return (table_adj,)


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Mode selector — language-dependent
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
            "Complex: all genders, numbers, and cases (18 fields)": "complex",
        }
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
def _(language_selector, mo, t_ui):
    mo.md(t_ui("phrases_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, language_selector, notebook_dir):
    df_phrases = gu2.load_vocab_table("phrases.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE, ru_variant=True, language=language_selector.value)
    return (df_phrases,)


@app.cell(hide_code=True)
def _(df_phrases, gu2, language_selector, mo, t_ui):
    _lang = language_selector.value
    table_phrases = gu2.vocab_table(df_phrases)
    _display = table_phrases if table_phrases is not None else mo.md(t_ui("phrases_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_phrases", _lang)), _display])
    return (table_phrases,)


@app.cell(hide_code=True)
def _(mo):
    confirmed_phrases, set_confirmed_phrases = mo.state([])
    return confirmed_phrases, set_confirmed_phrases


@app.cell(hide_code=True)
def _(
    confirmed_phrases,
    set_checked_phrase_d,
    set_confirmed_phrases,
    set_cv_phrase,
    set_remaining_phrase,
    table_phrases,
):
    if table_phrases.value is not None and not table_phrases.value.empty:
        _new_vocab = []
        for _, r in table_phrases.value.iterrows():
            _word = str(r.get("Word", "")).strip()
            if not _word:
                continue
            _new_vocab.append({"form": _word, "meaning": str(r.get("Translation", "")).strip()})
    else:
        _new_vocab = []

    if _new_vocab != confirmed_phrases():
        set_confirmed_phrases(_new_vocab)
        # Selection or language changed -- restart the quiz fresh instead of
        # keeping a frozen question/meaning from before the change (word_quiz_form/
        # word_drill_form only ever consult vocab on their own first init, per
        # their `if remaining is None:` init gate -- a later vocab change is
        # otherwise silently ignored until the quiz reaches "done").
        set_remaining_phrase(None)
        set_cv_phrase(None)
        set_checked_phrase_d(None)
    return


@app.cell(hide_code=True)
def _(mo):
    cv_phrase, set_cv_phrase = mo.state(None)
    remaining_phrase, set_remaining_phrase = mo.state(None)
    score_phrase, set_score_phrase = mo.state({"correct": 0, "total": 0})
    restore_phrase, set_restore_phrase = mo.state(None)
    history_phrase, set_history_phrase = mo.state([])
    future_phrase, set_future_phrase = mo.state([])
    checked_phrase_d, set_checked_phrase_d = mo.state(None)
    return (
        checked_phrase_d,
        cv_phrase,
        future_phrase,
        history_phrase,
        remaining_phrase,
        restore_phrase,
        score_phrase,
        set_checked_phrase_d,
        set_cv_phrase,
        set_future_phrase,
        set_history_phrase,
        set_remaining_phrase,
        set_restore_phrase,
        set_score_phrase,
    )


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    _lang = language_selector.value
    phrase_mode = mo.ui.radio(
        options={t_ui("quiz_mode_choice", _lang): "choice", t_ui("quiz_mode_type", _lang): "type"},
        value=t_ui("quiz_mode_choice", _lang),
        label=t_ui("phrase_mode_label", _lang),
    )
    phrase_mode
    return (phrase_mode,)


@app.cell(hide_code=True)
def _(
    confirmed_phrases,
    cv_phrase,
    gu2,
    history_phrase,
    language_selector,
    phrase_mode,
    remaining_phrase,
    restore_phrase,
):
    _lang = language_selector.value
    if phrase_mode.value == "type":
        write_input_phrase, dia_phrase, _plain_check_btn_phrase, prev_btn_phrase, next_btn_phrase = gu2.word_drill_widgets(
            cv=cv_phrase(), remaining=remaining_phrase(),
            restore_entry=restore_phrase(), history_len=len(history_phrase()),
            lang=_lang,
        )
        answer_radio_phrase = None
    else:
        answer_radio_phrase, next_btn_phrase, prev_btn_phrase = gu2.word_quiz_widgets(
            cv=cv_phrase(), remaining=remaining_phrase(), vocab=confirmed_phrases(),
            restore_entry=restore_phrase(),
            history_len=len(history_phrase()),
            lang=_lang,
        )
        write_input_phrase = dia_phrase = None
    return (
        answer_radio_phrase,
        dia_phrase,
        next_btn_phrase,
        prev_btn_phrase,
        write_input_phrase,
    )


@app.cell(hide_code=True)
def _(checked_phrase_d, dia_phrase, gu2, language_selector, phrase_mode, t_ui):
    # Built in its own cell (mirrors dirty_check_button's own paradigm-drill
    # pattern) so it re-renders -- and recolors -- on every keystroke via
    # dia_phrase, without rebuilding write_input_phrase itself.
    if phrase_mode.value == "type":
        check_btn_phrase_d = gu2.word_drill_check_button(
            dia_phrase, checked_phrase_d(),
            label=t_ui("check_label", language_selector.value),
        )
    else:
        check_btn_phrase_d = None
    return (check_btn_phrase_d,)


@app.cell(hide_code=True)
def _(
    answer_radio_phrase,
    check_btn_phrase_d,
    checked_phrase_d,
    confirmed_phrases,
    cv_phrase,
    dia_phrase,
    future_phrase,
    gu2,
    history_phrase,
    language_selector,
    mo,
    next_btn_phrase,
    phrase_mode,
    prev_btn_phrase,
    remaining_phrase,
    restore_phrase,
    score_phrase,
    set_checked_phrase_d,
    set_cv_phrase,
    set_future_phrase,
    set_history_phrase,
    set_remaining_phrase,
    set_restore_phrase,
    set_score_phrase,
    t_ui,
    write_input_phrase,
):
    _lang = language_selector.value
    if not confirmed_phrases():
        _out = mo.md(t_ui("phrases_empty", _lang))
    elif phrase_mode.value == "choice" and len(confirmed_phrases()) < 4:
        _out = mo.md(t_ui("phrases_too_few", _lang))
    elif phrase_mode.value == "type":
        _out = gu2.word_drill_form(
            cv_phrase, set_cv_phrase, remaining_phrase, set_remaining_phrase,
            score_phrase, set_score_phrase, restore_phrase, set_restore_phrase,
            history_phrase, set_history_phrase, future_phrase, set_future_phrase,
            write_input_phrase, dia_phrase, check_btn_phrase_d, prev_btn_phrase, next_btn_phrase,
            vocab=confirmed_phrases(),
            title=t_ui("phrase_heading", _lang),
            lang=_lang,
            get_checked=checked_phrase_d, set_checked=set_checked_phrase_d,
        )
    else:
        _out = gu2.word_quiz_form(
            cv_phrase, set_cv_phrase, remaining_phrase, set_remaining_phrase,
            score_phrase, set_score_phrase, restore_phrase, set_restore_phrase,
            history_phrase, set_history_phrase, future_phrase, set_future_phrase,
            answer_radio_phrase, next_btn_phrase, prev_btn_phrase,
            vocab=confirmed_phrases(),
            title=t_ui("phrase_heading", _lang),
            lang=_lang,
        )
    _out
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
    # Language selector — fixed-position overlay
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
    _prev_url, _next_url = _cfg.adjacent_urls("chapter_11/")
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
    RAW_BASE = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/modern_greek/ellinika_b/chapter_11"
    return RAW_BASE, mo, notebook_dir, pd, random


@app.cell(hide_code=True)
def _():
    # Modern Greek eee_project: imports
    import dataclasses
    import eee_project as eee
    from eee_project import GreekUtils, MODERN_GREEK
    from modern_greek_backend_eee import ModernGreekBackend


    return GreekUtils, MODERN_GREEK, ModernGreekBackend, dataclasses, eee


@app.cell(hide_code=True)
def _(GreekUtils, MODERN_GREEK, ModernGreekBackend, dataclasses, eee, mo, pd):
    # Modern Greek eee_project: backend setup
    _mg_backend = ModernGreekBackend()
    eee.register_backend("el", _mg_backend, backend="modern-greek")
    eee.set_chain("el", ["modern-greek"])
    # nav_icons/show_prev_when_done (eee-project 1.10.0+): this course wants
    # the ◀/▶/↺ nav-icon treatment and reviewable done screen everywhere, so
    # it's set once here via the course's own config instead of repeating
    # both kwargs at every quiz/drill call site.
    _config = dataclasses.replace(MODERN_GREEK, nav_icons=True, show_prev_when_done=True)
    gu2 = GreekUtils(_mg_backend, mo, pd, eee_module=eee, config=_config)
    return (gu2,)


if __name__ == "__main__":
    app.run()
