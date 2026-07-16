# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "marimo>=0.23.14",
#     "modern-greek-eee @ git+https://github.com/EEE-project/modern-greek-eee.git",
#     "modern-greek-inflexion-eee @ git+https://github.com/EEE-project/modern-greek-inflexion-eee.git",
#     "pandas",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# modern-greek-eee = { git = "https://github.com/EEE-project/modern-greek-eee" }
# modern-greek-inflexion-eee = { git = "https://github.com/EEE-project/modern-greek-inflexion-eee" }
# ///

import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium", html_head_file="head.html")


@app.cell(hide_code=True)
def _(language_selector, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _cfg = ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/modern_greek/ellinika_b/lessons.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=_cfg.index_url(), lang=language_selector.value, titles={
        "ru": "Ελληνικά Β", "el": "Ελληνικά Β", "en": "Ελληνικά Β",
    }, ga_config=_cfg.ga_config())
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Title
    _lang = language_selector.value
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_cNVzwZExWFfbrcMMDWCynL)"
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

| Условие | Следствие |
|:--------|:-------|
| **Αν** *έρθετε* στην Ελλάδα τον Ιούνιο, | *θα βρείτε* κάτι καλό και οικονομικό. |
| **Αν** *έρθετε* στο νησί, | *να σας φιλοξενήσουμε*. |
| **Αν** δε *βρείτε* δωμάτιο στην πόλη, | *να ψάξετε* στα γύρω χωριά. |

Придаточное следствия: Простое будущее (θα) или Υποτακτική (να).
""")
    elif _lang == "el":
        _out = mo.md("""
## Υποθετικές προτάσεις (Τύπος Α)

Το **αν** εισάγει μια υπόθεση. Το ρήμα μετά το **αν** χρησιμοποιεί το θέμα του Απλού Μέλλοντα **χωρίς θα**.

| Υπόθεση | Αποτέλεσμα |
|:--------|:-------|
| **Αν** *έρθετε* στην Ελλάδα τον Ιούνιο, | *θα βρείτε* κάτι καλό και οικονομικό. |
| **Αν** *έρθετε* στο νησί, | *να σας φιλοξενήσουμε*. |
| **Αν** δε *βρείτε* δωμάτιο στην πόλη, | *να ψάξετε* στα γύρω χωριά. |

Η πρόταση αποτελέσματος: Απλός Μέλλοντας (θα) ή Υποτακτική (να).
""")
    else:
        _out = mo.md("""
## Conditional Sentences (Υποθετικές προτάσεις — Τύπος Α)

**Αν** introduces a condition. The verb after **αν** uses the Simple Future stem **without θα**.

| Condition | Result |
|:----------|:-------|
| **Αν** *έρθετε* στην Ελλάδα τον Ιούνιο, | *θα βρείτε* κάτι καλό και οικονομικό. |
| **Αν** *έρθετε* στο νησί, | *να σας φιλοξενήσουμε*. |
| **Αν** δε *βρείτε* δωμάτιο στην πόλη, | *να ψάξετε* στα γύρω χωριά. |

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

| Πρότaση |
|:------|
| **Αν και** η Σαντορίνη έχει πολύ κόσμο αυτή την εποχή, περνάμε υπέροχα. |
| **Αν και / Ενώ** δεν είχαν πολλά χρήματα μαζί τους, πέρασαν πολύ καλά στις διακοπές. |

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

| Φράση |
|:------|
| Ένα τέτοιο ταξίδι είναι το όνειρό μου! |
| Θέλουμε να χαλαρώσουμε, χωρίς να πληρώσουμε μια περιουσία. |
| Καιρό είχαμε να τα πούμε. |
| Αξίζει! |
| Παίρνω το πλοίο της γραμμής. |
| Θα σας έρθει πολύ πιο φτηνά. |
| Να αποφασίσετε όσο το δυνατόν πιο γρήγορα. |
| Μου λείπει η Αθήνα. |
| Τον Δεκαπενταύγουστο γίνεται χαμός. |
| Δε βρίσκεις χώρο ούτε να καθίσεις. |
| Δεν μπορέσαμε να κλείσουμε μάτι όλη τη νύχτα. |
| Εμείς θέλουμε την ησυχία μας. |
| Κατά τα άλλα... |
| Καλή διαμονή σάς εύχομαι. |
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
def _(language_selector, mo, t_ui):
    # Test 1 heading
    mo.md(t_ui("test1_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Noun state
    tbl_sel_n, set_tbl_sel_n = mo.state(None)
    session_total_n, set_session_total_n = mo.state(0)
    return session_total_n, set_session_total_n, set_tbl_sel_n, tbl_sel_n


@app.cell(hide_code=True)
def _(mo):
    # Noun file upload
    file_upload_noun = mo.ui.file(label="Load nouns TSV")
    file_upload_noun
    return (file_upload_noun,)


@app.cell(hide_code=True)
def _(file_upload_noun, gu, notebook_dir, os, pd):
    # Load noun data
    if file_upload_noun.value:
        df_noun = gu.load_data(file_upload_noun, [])
    else:
        try:
            df_noun = pd.read_csv(os.path.join(notebook_dir, 'nouns.tsv'), sep='\t')
        except FileNotFoundError:
            df_noun = None
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, language_selector, mo, t_ui, tbl_sel_n):
    # Noun table
    _lang = language_selector.value
    table_noun = mo.ui.table(df_noun, selection="multi", initial_selection=tbl_sel_n()) if df_noun is not None else None
    _display = table_noun if table_noun is not None else mo.md(
        "_nouns.tsv не найден — загрузите файл._" if _lang == "ru" else
        "_Το αρχείο nouns.tsv δεν βρέθηκε — φόρτωσε αρχείο._" if _lang == "el" else
        "_nouns.tsv not found — upload a file to begin._"
    )
    mo.vstack([mo.md(t_ui("select_nouns", _lang)), _display])
    return (table_noun,)


@app.cell(hide_code=True)
def _(gu, mo, random, session_total_n, set_session_total_n, table_noun):
    # Noun words
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
    # Noun simple form
    clear_count_n()
    _nc = current_noun()
    noun_word, noun_trans, noun_form = gu.create_noun_test_ui([_nc] if _nc else [], mode='simple')
    return noun_form, noun_trans, noun_word


@app.cell(hide_code=True)
def _(clear_count_n, current_noun, gu):
    # Noun article form
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
    # Submit button N
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
    # Noun simple display
    _lang = language_selector.value
    _feedback = mo.md("")
    if words4test_noun() and noun_word:
        _cs = captured_simple()
        if _cs and getattr(_cs, 'test_word', None) == noun_word:
            with mo.capture_stdout() as _buf:
                gu.check_noun_test(noun_word, _cs, mode='simple')
            if _buf.getvalue():
                _feedback = mo.md(_buf.getvalue())
        _view = mo.vstack([
            mo.md(f"{t_ui('simple_noun_heading', _lang)} ({len(words4test_noun())}/{session_total_n()})"),
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
    # Noun article display
    _lang = language_selector.value
    _feedback_a = mo.md("")
    if words4test_noun() and art_noun_word:
        _ca = captured_article()
        if _ca and getattr(_ca, 'test_word', None) == art_noun_word:
            with mo.capture_stdout() as _buf_a:
                gu.check_noun_test(art_noun_word, _ca, mode='article')
            if _buf_a.getvalue():
                _feedback_a = mo.md(_buf_a.getvalue())
        _view_art = mo.vstack([
            mo.md(f"{t_ui('article_noun_heading', _lang)} ({len(words4test_noun())}/{session_total_n()})"),
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
    # Noun message
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
    # Noun pass handler
    _cn = current_noun()
    _cs = captured_simple()
    _ca = captured_article()
    _lang = language_selector.value
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
            set_noun_msg(t_ui("noun_passed", _lang).format(word=_cn["Word"], remaining=len(_new), total=session_total_n()))
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
    # Noun submit handler
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
    # Noun skip handler
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
def _(clear_button_n, clear_count_n, set_captured_article, set_captured_simple, set_clear_count_n):
    # Noun clear handler
    if (clear_button_n.value or 0) > clear_count_n():
        set_clear_count_n(clear_button_n.value)
        set_captured_simple(None)
        set_captured_article(None)
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 2 heading
    mo.md(t_ui("test2_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Verb state
    tbl_sel_v, set_tbl_sel_v = mo.state(None)
    session_total_v, set_session_total_v = mo.state(0)
    return session_total_v, set_session_total_v, set_tbl_sel_v, tbl_sel_v


@app.cell(hide_code=True)
def _(mo):
    # Verb file upload
    file_upload_verb = mo.ui.file(label="Load verbs TSV")
    file_upload_verb
    return (file_upload_verb,)


@app.cell(hide_code=True)
def _(file_upload_verb, gu, notebook_dir, os, pd):
    # Load verb data
    if file_upload_verb.value:
        df_verb = gu.load_data(file_upload_verb, [])
    else:
        try:
            df_verb = pd.read_csv(os.path.join(notebook_dir, 'verbs.tsv'), sep='\t')
        except FileNotFoundError:
            df_verb = None
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, language_selector, mo, t_ui, tbl_sel_v):
    # Verb table
    _lang = language_selector.value
    table_verb = mo.ui.table(df_verb, selection="multi", initial_selection=tbl_sel_v()) if df_verb is not None else None
    _display = table_verb if table_verb is not None else mo.md(
        "_verbs.tsv не найден — загрузите файл._" if _lang == "ru" else
        "_Το αρχείο verbs.tsv δεν βρέθηκε — φόρτωσε αρχείο._" if _lang == "el" else
        "_verbs.tsv not found — upload a file to begin._"
    )
    mo.vstack([mo.md(t_ui("select_verbs", _lang)), _display])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu, language_selector, mo, t_ui):
    # Tense selector — language-dependent, defaults to future (Υποτακτική)
    _lang = language_selector.value
    if _lang == "ru":
        _opts = {
            f"{gu.TENSE_LABELS['future']['greek']} (Απλή Υποτακτική / Простое будущее)": "future",
            f"{gu.TENSE_LABELS['present']['greek']} (Настоящее)": "present",
            f"{gu.TENSE_LABELS['imperfect']['greek']} (Имперфект)": "imperfect",
            f"{gu.TENSE_LABELS['aorist']['greek']} (Аорист)": "aorist",
            f"{gu.TENSE_LABELS['future_continuous']['greek']} (Длительное будущее)": "future_continuous",
        }
        _default = f"{gu.TENSE_LABELS['future']['greek']} (Απλή Υποτακτική / Простое будущее)"
    elif _lang == "el":
        _opts = {
            f"{gu.TENSE_LABELS['future']['greek']} (Απλή Υποτακτική / Απλός Μέλλοντας)": "future",
            f"{gu.TENSE_LABELS['present']['greek']} (Ενεστώτας)": "present",
            f"{gu.TENSE_LABELS['imperfect']['greek']} (Παρατατικός)": "imperfect",
            f"{gu.TENSE_LABELS['aorist']['greek']} (Αόριστος)": "aorist",
            f"{gu.TENSE_LABELS['future_continuous']['greek']} (Συνεχής Μέλλοντας)": "future_continuous",
        }
        _default = f"{gu.TENSE_LABELS['future']['greek']} (Απλή Υποτακτική / Απλός Μέλλοντας)"
    else:
        _opts = {
            f"{gu.TENSE_LABELS['future']['greek']} (Subjunctive / Simple Future)": "future",
            f"{gu.TENSE_LABELS['present']['greek']} (Present)": "present",
            f"{gu.TENSE_LABELS['imperfect']['greek']} (Imperfect)": "imperfect",
            f"{gu.TENSE_LABELS['aorist']['greek']} (Simple Past)": "aorist",
            f"{gu.TENSE_LABELS['future_continuous']['greek']} (Continuous Future)": "future_continuous",
        }
        _default = f"{gu.TENSE_LABELS['future']['greek']} (Subjunctive / Simple Future)"
    tense_selector = mo.ui.dropdown(options=_opts, value=_default, label=t_ui("tense_label", _lang))
    tense_selector
    return (tense_selector,)


@app.cell(hide_code=True)
def _(gu, mo, random, session_total_v, set_session_total_v, table_verb):
    # Verb words
    words_verb = gu.get_words(table_verb)
    words4test_verb, set_words4test_verb = mo.state(words_verb.copy() if words_verb else [])
    if words_verb and len(words_verb) > session_total_v():
        set_session_total_v(len(words_verb))
    elif not words_verb:
        set_session_total_v(0)
    verb_msg, set_verb_msg = mo.state("")
    captured_verb, set_captured_verb = mo.state(None)
    _clk = lambda v: (v or 0) + 1
    skip_button_v = mo.ui.button(label="Skip", on_click=_clk)
    clear_button_v = mo.ui.button(label="Clear", on_click=_clk)
    skip_count_v, set_skip_count_v = mo.state(0)
    clear_count_v, set_clear_count_v = mo.state(0)
    submit_count_v, set_submit_count_v = mo.state(0)
    cv_verb, set_cv_verb = mo.state(None)
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
    # Verb form
    clear_count_v()
    _cv = cv_verb()
    _tense_key = tense_selector.value
    _ui_label = gu.TENSE_LABELS[_tense_key]['greek'] if _tense_key else "—"
    verb_fields, _ = gu.create_verb_test_ui(_ui_label, words_verb, words4test_verb(), _cv)
    return (verb_fields,)


@app.cell(hide_code=True)
def _(captured_verb, mo, set_submit_count_v, tense_selector, verb_fields):
    # Submit button V
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
    # Verb display
    _lang = language_selector.value
    _TENSE_LABELS = {k: gu.TENSE_LABELS[k]['greek'] for k in gu.TENSE_LABELS}
    if not words4test_verb():
        _view_verb = mo.md(t_ui("verb_empty", _lang))
    elif not tense_selector.value:
        _view_verb = mo.md(t_ui("verb_no_tense", _lang))
    else:
        _feedback_v = mo.md("")
        _cv = cv_verb()
        _c = captured_verb()
        if _cv and _c and getattr(_c, 'verb_word', None) == _cv['Word'] and getattr(_c, 'tense', None) == tense_selector.value:
            _, _msg = gu.check_verb_test(_cv['Word'], _c, tense_selector.value)
            _feedback_v = mo.md(_msg)
        _label = _TENSE_LABELS.get(tense_selector.value, tense_selector.value)
        _rem = len(words4test_verb())
        _items = [mo.md(f"{t_ui('verb_heading', _lang)} — {_label} ({_rem}/{session_total_v()})")]
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
    # Verb pass handler
    _tense_key = tense_selector.value
    _c = captured_verb()
    _cv = cv_verb()
    _lang = language_selector.value
    if _cv and _tense_key and _c and getattr(_c, 'verb_word', None) == _cv['Word'] and getattr(_c, 'tense', None) == _tense_key:
        _ok, _ = gu.check_verb_test(_cv['Word'], _c, _tense_key)
        if _ok:
            _new = [w for w in words4test_verb() if w['Word'] != _cv['Word']]
            set_words4test_verb(_new)
            if df_verb is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_v([i for i, w in enumerate(df_verb['Word']) if w in _rem])
            set_verb_msg(t_ui("verb_passed", _lang).format(word=_cv["Word"], trans=_cv["Translation"], remaining=len(_new), total=session_total_v()))
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
    # Verb submit handler
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
    # Verb skip handler
    if (skip_button_v.value or 0) > skip_count_v():
        set_skip_count_v(skip_button_v.value)
        set_captured_verb(None)
        _cv = cv_verb()
        if words4test_verb():
            _new = [w for w in words4test_verb() if not _cv or w['Word'] != _cv['Word']]
            set_words4test_verb(_new)
            if df_verb is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_v([i for i, w in enumerate(df_verb['Word']) if w in _rem])
            set_cv_verb(random.choice(_new) if _new else None)
    return


@app.cell(hide_code=True)
def _(clear_button_v, clear_count_v, set_captured_verb, set_clear_count_v):
    # Verb clear handler
    if (clear_button_v.value or 0) > clear_count_v():
        set_clear_count_v(clear_button_v.value)
        set_captured_verb(None)
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 3 heading
    mo.md(t_ui("test3_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Adj state
    tbl_sel_a, set_tbl_sel_a = mo.state(None)
    session_total_a, set_session_total_a = mo.state(0)
    return session_total_a, set_session_total_a, set_tbl_sel_a, tbl_sel_a


@app.cell(hide_code=True)
def _(mo):
    # Adj file upload
    file_upload_adj = mo.ui.file(label="Load adjectives TSV")
    file_upload_adj
    return (file_upload_adj,)


@app.cell(hide_code=True)
def _(file_upload_adj, gu, notebook_dir, os, pd):
    # Load adj data
    if file_upload_adj.value:
        df_adj = gu.load_data(file_upload_adj, [])
    else:
        try:
            df_adj = pd.read_csv(os.path.join(notebook_dir, 'adjectives.tsv'), sep='\t')
        except FileNotFoundError:
            df_adj = None
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, language_selector, mo, t_ui, tbl_sel_a):
    # Adj table
    _lang = language_selector.value
    table_adj = mo.ui.table(df_adj, selection="multi", initial_selection=tbl_sel_a()) if df_adj is not None else None
    _display = table_adj if table_adj is not None else mo.md(
        "_adjectives.tsv не найден — загрузите файл._" if _lang == "ru" else
        "_Το αρχείο adjectives.tsv δεν βρέθηκε — φόρτωσε αρχείο._" if _lang == "el" else
        "_adjectives.tsv not found — upload a file to begin._"
    )
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
def _(gu, mo, random, session_total_a, set_session_total_a, table_adj):
    # Adj words
    words_adj = gu.get_words(table_adj)
    words4test_adj, set_words4test_adj = mo.state(words_adj.copy() if words_adj else [])
    if words_adj and len(words_adj) > session_total_a():
        set_session_total_a(len(words_adj))
    elif not words_adj:
        set_session_total_a(0)
    adj_last_passed_mesg, set_adj_last_passed_mesg = mo.state("")
    adj_cv, set_adj_cv = mo.state(None)
    captured_adj, set_captured_adj = mo.state(None)
    _clk = lambda v: (v or 0) + 1
    skip_button_a = mo.ui.button(label="Skip", on_click=_clk)
    clear_button_a = mo.ui.button(label="Clear", on_click=_clk)
    skip_count_a, set_skip_count_a = mo.state(0)
    clear_count_a, set_clear_count_a = mo.state(0)
    submit_count_a, set_submit_count_a = mo.state(0)
    if words_adj and adj_cv() is None:
        set_adj_cv(random.choice(words_adj))
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
    # Adj form
    clear_count_a()
    _acv = adj_cv()
    adj_form, _ = gu.create_adjective_test_ui([] if not _acv else [_acv], [], _acv, mode=mode_selector.value)
    return (adj_form,)


@app.cell(hide_code=True)
def _(adj_form, captured_adj, mo, set_submit_count_a):
    # Submit button A
    _values = adj_form.value if adj_form else []
    _snap = captured_adj()
    _has_input = bool(_values and any(v.strip() for v in _values))
    _matches_snap = _snap is not None and [v.strip() for v in _values] == [v.strip() for v in (_snap.value or [])]
    _dirty = _has_input and not _matches_snap
    _clk = lambda v: (v or 0) + 1
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
    # Adj display
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
            mo.md(f"{t_ui('adj_heading', _lang)} ({len(words4test_adj())}/{session_total_a()})"),
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
    # Adj message
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
    # Adj pass handler
    _adj = adj_cv()
    _c = captured_adj()
    _lang = language_selector.value
    if words4test_adj() and _adj and _c and getattr(_c, 'adj_word', None) == _adj['Word']:
        adj_ok, _ = gu.check_adjective_test(_adj['Word'], _c)
        if adj_ok:
            _new = [w for w in words4test_adj() if w['Word'] != _adj['Word']]
            set_words4test_adj(_new)
            if df_adj is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_a([i for i, w in enumerate(df_adj['Word']) if w in _rem])
            set_adj_last_passed_mesg(t_ui("adj_passed", _lang).format(word=_adj["Word"], trans=_adj["Translation"], remaining=len(_new), total=session_total_a()))
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
    # Adj submit handler
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
    # Adj skip handler
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
    # Adj clear handler
    if (clear_button_a.value or 0) > clear_count_a():
        set_clear_count_a(clear_button_a.value)
        set_captured_adj(None)
    return


@app.cell(hide_code=True)
def _():
    # UI strings — static dict, no language_selector dependency to avoid cascading resets
    UI_STRINGS = {
        "en": {
            "test1_heading": "## Test 1: Nouns",
            "test2_heading": "## Test 2: Verbs",
            "test3_heading": "## Test 3: Adjectives",
            "select_nouns": "### Select nouns to practice",
            "select_verbs": "### Select verbs to practice",
            "select_adjs": "### Select adjectives to practice",
            "translation_label": "Translation:",
            "simple_noun_heading": "**Simple noun test**",
            "article_noun_heading": "**Noun test with articles**",
            "verb_heading": "**Verb test**",
            "adj_heading": "**Adjective test**",
            "noun_empty": "_Select nouns from the table above to begin._",
            "verb_empty": "_Select verbs from the table above to begin._",
            "verb_no_tense": "_Select a tense above._",
            "adj_empty": "_Select adjectives from the table above to begin._",
            "tense_label": "Select tense:",
            "mode_label": "Test mode:",
            "noun_passed": '<span style="color:green;">Test for <b>"{word}"</b> passed.\n\n{remaining} words remaining out of {total}.</span>',
            "verb_passed": '<span style="color:green;">Test for <b>"{word} — {trans}"</b> passed.\n\n{remaining} words remaining out of {total}.</span>',
            "adj_passed":  '<span style="color:green;">Test for <b>"{word} — {trans}"</b> passed.\n\n{remaining} words remaining out of {total}.</span>',
        },
        "ru": {
            "test1_heading": "## Тест 1: Существительные",
            "test2_heading": "## Тест 2: Глаголы",
            "test3_heading": "## Тест 3: Прилагательные",
            "select_nouns": "### Выберите существительные для практики",
            "select_verbs": "### Выберите глаголы для практики",
            "select_adjs": "### Выберите прилагательные для практики",
            "translation_label": "Перевод:",
            "simple_noun_heading": "**Простой тест по существительным**",
            "article_noun_heading": "**Тест по существительным с артиклями**",
            "verb_heading": "**Тест по глаголам**",
            "adj_heading": "**Тест по прилагательным**",
            "noun_empty": "_Выберите существительные из таблицы выше, чтобы начать._",
            "verb_empty": "_Выберите глаголы из таблицы выше, чтобы начать._",
            "verb_no_tense": "_Выберите время выше._",
            "adj_empty": "_Выберите прилагательные из таблицы выше, чтобы начать._",
            "tense_label": "Выбрать время:",
            "mode_label": "Режим теста:",
            "noun_passed": '<span style="color:green;">Тест для <b>"{word}"</b> пройден.\n\n{remaining} слов осталось из {total}.</span>',
            "verb_passed": '<span style="color:green;">Тест для <b>"{word} — {trans}"</b> пройден.\n\n{remaining} слов осталось из {total}.</span>',
            "adj_passed":  '<span style="color:green;">Тест для <b>"{word} — {trans}"</b> пройден.\n\n{remaining} слов осталось из {total}.</span>',
        },
        "el": {
            "test1_heading": "## Τεστ 1: Ουσιαστικά",
            "test2_heading": "## Τεστ 2: Ρήματα",
            "test3_heading": "## Τεστ 3: Επίθετα",
            "select_nouns": "### Επιλογή ουσιαστικών για εξάσκηση",
            "select_verbs": "### Επιλογή ρημάτων για εξάσκηση",
            "select_adjs": "### Επιλογή επιθέτων για εξάσκηση",
            "translation_label": "Μετάφραση:",
            "simple_noun_heading": "**Απλό τεστ ουσιαστικών**",
            "article_noun_heading": "**Τεστ ουσιαστικών με άρθρα**",
            "verb_heading": "**Τεστ ρημάτων**",
            "adj_heading": "**Τεστ επιθέτων**",
            "noun_empty": "_Επιλέξτε ουσιαστικά από τον παραπάνω πίνακα για να ξεκινήσετε._",
            "verb_empty": "_Επιλέξτε ρήματα από τον παραπάνω πίνακα για να ξεκινήσετε._",
            "verb_no_tense": "_Επιλέξτε χρόνο παραπάνω._",
            "adj_empty": "_Επιλέξτε επίθετα από τον παραπάνω πίνακα για να ξεκινήσετε._",
            "tense_label": "Επιλογή χρόνου:",
            "mode_label": "Επιλογή τρόπου:",
            "noun_passed": '<span style="color:green;">Τεστ για <b>"{word}"</b> ολοκληρώθηκε.\n\n{remaining} λέξεις απομένουν από {total}.</span>',
            "verb_passed": '<span style="color:green;">Τεστ για <b>"{word} — {trans}"</b> ολοκληρώθηκε.\n\n{remaining} λέξεις απομένουν από {total}.</span>',
            "adj_passed":  '<span style="color:green;">Τεστ για <b>"{word} — {trans}"</b> ολοκληρώθηκε.\n\n{remaining} λέξεις απομένουν από {total}.</span>',
        },
    }

    def t_ui(key, lang=None):
        _lang = lang if lang else "en"
        return UI_STRINGS.get(_lang, UI_STRINGS["en"]).get(key, UI_STRINGS["en"].get(key, key))

    return (t_ui,)


@app.cell(hide_code=True)
def _(mo):
    # Language selector — fixed-position overlay
    language_selector = mo.ui.dropdown(
        options={"English": "en", "Русский": "ru", "Ελληνικά": "el"},
        value="English",
        label="🌐",
    )
    mo.Html(f"""
    <div style="position: fixed; top: 60px; right: 10px; z-index: 1000; background: white; padding: 8px 12px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
        {language_selector}
    </div>
    """)
    return (language_selector,)


@app.cell(hide_code=True)
def _():
    # Imports
    import os
    import random
    import pandas as pd
    import marimo as mo
    from modern_greek_eee import greek_utils as gu
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    return gu, mo, notebook_dir, os, pd, random


if __name__ == "__main__":
    app.run()
