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
app = marimo.App(width="medium", html_head_file="head.html", app_title="Ελληνικά Β1 — Chapter 12: An Accident on the Road")


@app.cell(hide_code=True)
def _(language_selector, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://raw.githubusercontent.com/EEE-project/created_with_eee/main"
    _cfg = ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/modern_greek/ellinika_b/index.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=_cfg.index_url(), lang=language_selector.value, titles={
        "ru": "Ελληνικά Β1", "el": "Ελληνικά Β1", "en": "Ελληνικά Β1",
    }, ga_config=_cfg.ga_config(), same_window=True)
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Title
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md(f"""
    # «Ένα ατύχημα στους δρόμους» 🚑
    ## Глава 12 — Авария на дороге · B1

    **Грамматика:** Ενδοιαστικές · Сослагательное (Простое и Длительное) · Λέει να vs Λέει ότι
    **Тесты:** Существительные · Глаголы · Прилагательные
    """)
    elif _lang == "el":
        _out = mo.md(f"""
    # «Ένα ατύχημα στους δρόμους» 🚑
    ## Ενότητα 12 — Ένα ατύχημα στους δρόμους · B1

    **Γραμματική:** Ενδοιαστικές · Υποτακτική (Απλή & Συνεχής) · Λέει να vs Λέει ότι
    **Τεστ:** Ουσιαστικά · Ρήματα · Επίθετα
    """)
    else:
        _out = mo.md(f"""
    # «Ένα ατύχημα στους δρόμους» 🚑
    ## Unit 12 — An Accident on the Road · B1

    **Grammar:** Subjunctive (Simple & Continuous) · Ενδοιαστικές · Λέει να vs Λέει ότι
    **Tests:** Nouns · Verbs · Adjectives
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Vocabulary
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Словарь (Λέξεις, λέξεις)

    ### На месте аварии (с.187)

    | Греческий | Русский |
    |:----------|:--------|
    | το ασθενοφόρο | скорая помощь |
    | το ατύχημα | авария, несчастный случай |
    | η διασταύρωση | перекрёсток |
    | το κράνος | шлем |
    | το στενό | переулок |
    | η τροχαία | дорожная полиция |

    ### В приёмном покое (с.191)

    | Греческий | Русский |
    |:----------|:--------|
    | η ακτινογραφία | рентген |
    | η αναρρωτική άδεια | больничный лист |
    | η ζαλάδα | головокружение |
    | ζαλίζομαι | чувствовать головокружение |
    | το κάταγμα | перелом |
    | το παυσίπονο | обезболивающее |
    | βγάζω ακτινογραφία | сделать рентген |
    | έχω κάταγμα | иметь перелом |
    | παίρνω παυσίπονα | принимать обезболивающее |
    | βάζω πάγο | прикладывать лёд |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Λεξιλόγιο

    ### Στον τόπο του ατυχήματος (σ.187)

    | Ελληνικά | Αγγλικά |
    |:---------|:--------|
    | το ασθενοφόρο | ambulance |
    | το ατύχημα | accident |
    | η διασταύρωση | intersection |
    | το κράνος | helmet |
    | το στενό | alley |
    | η τροχαία | traffic police |

    ### Στα επείγοντα (σ.191)

    | Ελληνικά | Αγγλικά |
    |:---------|:--------|
    | η ακτινογραφία | X-ray |
    | η αναρρωτική άδεια | sick leave |
    | η ζαλάδα | dizziness |
    | ζαλίζομαι | to feel dizzy |
    | το κάταγμα | fracture |
    | το παυσίπονο | painkiller |
    | βγάζω ακτινογραφία | to get an X-ray |
    | έχω κάταγμα | to have a fracture |
    | παίρνω παυσίπονα | to take painkillers |
    | βάζω πάγο | to apply ice |
    """)
    else:
        _out = mo.md("""
    ## Vocabulary

    ### At the accident scene (p.187)

    | Greek | English |
    |:------|:--------|
    | το ασθενοφόρο | ambulance |
    | το ατύχημα | accident |
    | η διασταύρωση | intersection |
    | το κράνος | helmet |
    | το στενό | alley |
    | η τροχαία | traffic police |

    ### At the emergency room (p.191)

    | Greek | English |
    |:------|:--------|
    | η ακτινογραφία | X-ray |
    | η αναρρωτική άδεια | sick leave |
    | η ζαλάδα | dizziness |
    | ζαλίζομαι | to feel dizzy |
    | το κάταγμα | fracture |
    | το παυσίπονο | painkiller |
    | βγάζω ακτινογραφία | to get an X-ray |
    | έχω κάταγμα | to have a fracture |
    | παίρνω παυσίπονα | to take painkillers |
    | βάζω πάγο | to apply ice |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar 1: Ενδοιαστικές
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика 1: Выражение опасений (Ενδοιαστικές Προτάσεις, с.188)

    **Ανησυχώ / Έχω αγωνία / Φοβάμαι** + **μη(ν) / μήπως** + Простое будущее (без **θα**) или Аорист

    > После μη(ν) / μήπως θα не ставится: глагол употребляется непосредственно, без частицы θα.

    | | | | |
    |:--|:--|:--|:--|
    | Ανησυχώ | **μήπως** | δεν έρθει. | *Волнуюсь, что он может не прийти.* |
    | Φοβάμαι | **μην** | καταλάβουν το λάθος μου. | *Боюсь, что они могут заметить мою ошибку.* |
    | Φοβάμαι | **μήπως** | έπαθε κάτι. | *Боюсь, что с ним что-то могло случиться.* |
    | Έχω αγωνία | **μήπως** | είχαν κανένα ατύχημα. | *Тревожусь, что они могли попасть в аварию.* |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Γραμματική 1: Ενδοιαστικές Προτάσεις (σ.188)

    **Ανησυχώ / Έχω αγωνία / Φοβάμαι** + **μη(ν) / μήπως** + Απλός Μέλλοντας (χωρίς **θα**) ή Αόριστος

    > Το ρήμα μετά το μη(ν)/μήπως **δεν** παίρνει **θα** — χρησιμοποιείται απευθείας το θέμα του απλού μέλλοντα.

    | | | | |
    |:--|:--|:--|:--|
    | Ανησυχώ | **μήπως** | δεν έρθει. | *I'm worried he might not come.* |
    | Φοβάμαι | **μην** | καταλάβουν το λάθος μου. | *I'm afraid they'll notice my mistake.* |
    | Φοβάμαι | **μήπως** | έπαθε κάτι. | *I'm afraid something happened to him.* |
    | Έχω αγωνία | **μήπως** | είχαν κανένα ατύχημα. | *I'm anxious they may have had an accident.* |
    """)
    else:
        _out = mo.md("""
    ## Grammar 1: Ενδοιαστικές Προτάσεις (p.188)

    **Ανησυχώ / Έχω αγωνία / Φοβάμαι** + **μη(ν) / μήπως** + Simple Future (without **θα**) or Aorist

    > The verb after μη(ν)/μήπως does **not** take **θα** — it uses the simple future stem directly.

    | | | | |
    |:--|:--|:--|:--|
    | Ανησυχώ | **μήπως** | δεν έρθει. | *I'm worried he might not come.* |
    | Φοβάμαι | **μην** | καταλάβουν το λάθος μου. | *I'm afraid they'll notice my mistake.* |
    | Φοβάμαι | **μήπως** | έπαθε κάτι. | *I'm afraid something happened to him.* |
    | Έχω αγωνία | **μήπως** | είχαν κανένα ατύχημα. | *I'm anxious they may have had an accident.* |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar 2: Φοβάμαι
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика 2: Φοβάμαι — три конструкции (с.189)

    | Конструкция | Значение | Пример |
    |:------------|:---------|:-------|
    | Φοβάμαι **ότι / πως** + Изъявительное | Уверенность в плохом исходе | Φοβάμαι **ότι** θα χάσουμε το τρένο. *(Боюсь, что опоздаем на поезд.)* |
    | Φοβάμαι **μήπως / μη(ν)** + Сослагательное | Беспокойство о возможном событии | Φοβάμαι **μήπως** χάσουμε το τρένο. *(Боюсь, как бы не опоздать на поезд.)* |
    | Φοβάμαι **να** + Сослагательное | Страх делать что-то самому | Φοβάμαι **να** ανεβώ στη μηχανή του. *(Боюсь садиться на его мотоцикл.)* |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Γραμματική 2: Φοβάμαι — τρεις κατασκευές (σ.189)

    | Κατασκευή | Σημασία | Παράδειγμα |
    |:----------|:--------|:-----------|
    | Φοβάμαι **ότι / πως** + Οριστική | Βεβαιότητα για αρνητική έκβαση | Φοβάμαι **ότι** θα χάσουμε το τρένο. *(I'm pretty sure we'll miss the train.)* |
    | Φοβάμαι **μήπως / μη(ν)** + Υποτακτική | Ανησυχία ότι μπορεί να συμβεί κάτι | Φοβάμαι **μήπως** χάσουμε το τρένο. *(I'm worried we might miss the train.)* |
    | Φοβάμαι **να** + Υποτακτική | Φόβος να κάνει κάτι ο ίδιος | Φοβάμαι **να** ανεβώ στη μηχανή του. *(I'm afraid to get on his motorcycle.)* |
    """)
    else:
        _out = mo.md("""
    ## Grammar 2: Φοβάμαι — three constructions (p.189)

    | Construction | Meaning | Example |
    |:-------------|:--------|:--------|
    | Φοβάμαι **ότι / πως** + Indicative | Certainty about a negative outcome | Φοβάμαι **ότι** θα χάσουμε το τρένο. *(I'm pretty sure we'll miss the train.)* |
    | Φοβάμαι **μήπως / μη(ν)** + Subjunctive | Worry that something might happen | Φοβάμαι **μήπως** χάσουμε το τρένο. *(I'm worried we might miss the train.)* |
    | Φοβάμαι **να** + Subjunctive | Fear of doing something oneself | Φοβάμαι **να** ανεβώ στη μηχανή του. *(I'm afraid to get on his motorcycle.)* |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar 3: Λέει να vs Λέει ότι
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика 3: Λέει να vs Λέει ότι (с.190)

    | | |
    |:--|:--|
    | **Λέει να** πάει με τα πόδια. Δεν είναι πολύ μακριά. | *Думает пойти пешком.* (намерение, не уверен) |
    | **Λέει ότι** θα πάει με τα πόδια, γιατί δεν είναι πολύ μακριά. | *Говорит, что пойдёт пешком.* (сообщает факт) |

    - **Λέω να** + Сослагательное → намерение / размышление о действии
    - **Λέω ότι / πως** + Изъявительное → сообщение факта
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Γραμματική 3: Λέει να vs Λέει ότι (σ.190)

    | | |
    |:--|:--|
    | **Λέει να** πάει με τα πόδια. Δεν είναι πολύ μακριά. | *He's thinking of going on foot.* (considering, not certain) |
    | **Λέει ότι** θα πάει με τα πόδια, γιατί δεν είναι πολύ μακριά. | *He says he will go on foot.* (stating a fact) |

    - **Λέω να** + Υποτακτική → πρόθεση / σκέψη για πράξη
    - **Λέω ότι / πως** + Οριστική → δήλωση γεγονότος
    """)
    else:
        _out = mo.md("""
    ## Grammar 3: Λέει να vs Λέει ότι (p.190)

    | | |
    |:--|:--|
    | **Λέει να** πάει με τα πόδια. Δεν είναι πολύ μακριά. | *He's thinking of going on foot.* (considering, not certain) |
    | **Λέει ότι** θα πάει με τα πόδια, γιατί δεν είναι πολύ μακριά. | *He says he will go on foot.* (stating a fact) |

    - **Λέω να** + Subjunctive → intention / considering something
    - **Λέω ότι / πως** + Indicative → stating a fact
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar 4: Simple vs Continuous Subjunctive
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика 4: Простое vs Длительное сослагательное (с.192)

    | Один раз — **Απλή Υποτακτική** | Длительно, часто — **Συνεχής Υποτακτική** |
    |:-------------------------------------------------|:--------------------------------------------------|
    | Μπορείς **να φας** ό,τι θέλεις σήμερα. ("Ты можешь съесть, что хочешь, сегодня.") | Μπορείς **να τρως** ό,τι θέλεις από αύριο. ("Ты можешь есть, что хочешь, с завтрашнего дня.") |
    | Πρέπει **να πας** στο νοσοκομείο. ("Тебе нужно пойти в больницу.") | Πρέπει **να πηγαίνεις** τακτικά στον οδοντίατρο. ("Тебе нужно регулярно ходить к стоматологу.") |
    | Θέλω **να περπατήσω** λίγο. ("Я хочу немного погулять.") | Θέλω **να περπατάω** μία ώρα κάθε μέρα. ("Я хочу гулять по часу каждый день.") |
    | Προσπαθώ **να διαβάσω** για το τεστ. ("Я стараюсь позаниматься к тесту.") | Προσπαθώ **να διαβάζω** κάθε απόγευμα. ("Я стараюсь заниматься каждый день после обеда.") |
    | Ελπίζω **να φτάσουμε** νωρίς. ("Надеюсь, мы приедем рано.") | Ελπίζω **να οδηγείς** προσεκτικά. ("Надеюсь, ты водишь осторожно.") |

    > **Απλή** = совершенный вид основы (та же основа, что у Простого будущего: θα φάω → να **φάω**)
    > **Συνεχής** = несовершенный вид основы / основа Настоящего (τρώω → να **τρώω**)

    ### Модальные выражения (с.192)

    | | Απλή (одно действие) | Συνεχής (привычка/длящееся) |
    |:--|:--|:--|
    | **Απαγορεύεται να** | Απόψε **απαγορεύεται να** οδηγήσεις. ("Сегодня вечером тебе нельзя водить.") | **Απαγορεύεται να** οδηγείτε όταν πίνετε. ("Нельзя водить, когда вы выпили.") |
    | **Επιτρέπεται να** | **Επιτρέπεται να** καπνίσω; ("Можно мне закурить?") | **Δεν επιτρέπεται να** καπνίζετε. ("Курить не разрешается.") |
    | **Είναι αδύνατον να** | **Είναι αδύνατον να** σας δει τώρα. ("Он никак не может вас сейчас принять.") | **Είναι αδύνατον να** μιλάει κινέζικα καλά. ("Не может быть, что он хорошо говорит по-китайски.") |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Γραμματική 4: Απλή vs Συνεχής Υποτακτική (σ.192)

    | Μία φορά — **Απλή Υποτακτική** | Συνέχεια, συχνά — **Συνεχής Υποτακτική** |
    |:------------------------------------------------|:-----------------------------------------------------|
    | Μπορείς **να φας** ό,τι θέλεις σήμερα. ("You can eat whatever you want today.") | Μπορείς **να τρως** ό,τι θέλεις από αύριο. ("You can eat whatever you want starting tomorrow.") |
    | Πρέπει **να πας** στο νοσοκομείο. ("You need to go to the hospital.") | Πρέπει **να πηγαίνεις** τακτικά στον οδοντίατρο. ("You need to go to the dentist regularly.") |
    | Θέλω **να περπατήσω** λίγο. ("I want to walk a bit.") | Θέλω **να περπατάω** μία ώρα κάθε μέρα. ("I want to walk an hour every day.") |
    | Προσπαθώ **να διαβάσω** για το τεστ. ("I'm trying to study for the test.") | Προσπαθώ **να διαβάζω** κάθε απόγευμα. ("I'm trying to study every afternoon.") |
    | Ελπίζω **να φτάσουμε** νωρίς. ("I hope we arrive early.") | Ελπίζω **να οδηγείς** προσεκτικά. ("I hope you drive carefully.") |

    > **Απλή** = συνοπτικό θέμα (το ίδιο θέμα με τον Απλό Μέλλοντα: θα φάω → να **φάω**)
    > **Συνεχής** = εξακολουθητικό θέμα / θέμα Ενεστώτα (τρώω → να **τρώω**)

    ### Τροπικές εκφράσεις (σ.192)

    | | Απλή (μία πράξη) | Συνεχής (συνήθεια/διαρκές) |
    |:--|:--|:--|
    | **Απαγορεύεται να** | Απόψε **απαγορεύεται να** οδηγήσεις. ("Tonight you're not allowed to drive.") | **Απαγορεύεται να** οδηγείτε όταν πίνετε. ("You're not allowed to drive when you've been drinking.") |
    | **Επιτρέπεται να** | **Επιτρέπεται να** καπνίσω; ("Am I allowed to smoke?") | **Δεν επιτρέπεται να** καπνίζετε. ("You're not allowed to smoke.") |
    | **Είναι αδύνατον να** | **Είναι αδύνατον να** σας δει τώρα. ("It's impossible for him to see you now.") | **Είναι αδύνατον να** μιλάει κινέζικα καλά. ("It's impossible that he speaks Chinese well.") |
    """)
    else:
        _out = mo.md("""
    ## Grammar 4: Απλή vs Συνεχής Υποτακτική (p.192)

    | Once — **Απλή Υποτακτική** | Continuous, often — **Συνεχής Υποτακτική** |
    |:-----------------------------------------|:---------------------------------------------|
    | Μπορείς **να φας** ό,τι θέλεις σήμερα. ("You can eat whatever you want today.") | Μπορείς **να τρως** ό,τι θέλεις από αύριο. ("You can eat whatever you want starting tomorrow.") |
    | Πρέπει **να πας** στο νοσοκομείο. ("You need to go to the hospital.") | Πρέπει **να πηγαίνεις** τακτικά στον οδοντίατρο. ("You need to go to the dentist regularly.") |
    | Θέλω **να περπατήσω** λίγο. ("I want to walk a bit.") | Θέλω **να περπατάω** μία ώρα κάθε μέρα. ("I want to walk an hour every day.") |
    | Προσπαθώ **να διαβάσω** για το τεστ. ("I'm trying to study for the test.") | Προσπαθώ **να διαβάζω** κάθε απόγευμα. ("I'm trying to study every afternoon.") |
    | Ελπίζω **να φτάσουμε** νωρίς. ("I hope we arrive early.") | Ελπίζω **να οδηγείς** προσεκτικά. ("I hope you drive carefully.") |

    > **Απλή** = perfective stem (the same stem used in the Simple Future: θα φάω → να **φάω**)
    > **Συνεχής** = imperfective/present stem (τρώω → να **τρώω**)

    ### Modal expressions (p.192)

    | | Απλή (single action) | Συνεχής (habit/ongoing) |
    |:--|:--|:--|
    | **Απαγορεύεται να** | Απόψε **απαγορεύεται να** οδηγήσεις. ("Tonight you're not allowed to drive.") | **Απαγορεύεται να** οδηγείτε όταν πίνετε. ("You're not allowed to drive when you've been drinking.") |
    | **Επιτρέπεται να** | **Επιτρέπεται να** καπνίσω; ("Am I allowed to smoke?") | **Δεν επιτρέπεται να** καπνίζετε. ("You're not allowed to smoke.") |
    | **Είναι αδύνατον να** | **Είναι αδύνατον να** σας δει τώρα. ("It's impossible for him to see you now.") | **Είναι αδύνατον να** μιλάει κινέζικα καλά. ("It's impossible that he speaks Chinese well.") |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar 5: Verbs with Simple or Continuous Subjunctive
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика 5: Глаголы с Простым или Длительным сослагательным (с.194)

    ### Ρήματα και εκφράσεις με Απλή Υποτακτική (σχεδόν πάντα) — Глаголы с Простым сослагательным

    | Глагол | Пример | |
    |:-------|:-------|:-|
    | **Έχω να** | Έχω **να** δουλέψω. | Мне нужно поработать. |
    | **Πάω να** | Πάω **να** αγοράσω ψωμί. | Иду купить хлеб. |
    | **Ξέχασα να** | Ξέχασα **να** αγοράσω εφημερίδα. | Забыл купить газету. |
    | **Είμαι έτοιμος να** | Είμαι έτοιμος **να** φύγω. | Я готов уйти. |
    | **Ψάχνω να** | Ψάχνω **να** βρω τα κλειδιά μου. | Ищу свои ключи. |
    | **Αργείς να** | Αργείς **να** πας στη δουλειά σου; | Ты опаздываешь на работу? |
    | **Κοντεύω να** | Κοντεύω **να** τελειώσω το διάβασμα. | Почти закончил учиться. |
    | **Περιμένω να** | Περιμένω **να** γυρίσει ο διευθυντής. | Жду, когда вернётся директор. |
    | **Δεν πρόλαβα να** | Δεν πρόλαβα **να** διαβάσω. | Не успел прочитать. |
    | **είναι πιθανό να** | Είναι **πιθανό να** πάθεις ατύχημα. | Возможно, ты попадёшь в аварию. |
    | **είναι απίθανο να** | Είναι **απίθανο να** τρακάρεις. | Маловероятно, что ты врежешься. |

    **Вопросительные предложения с να:**

    | | |
    |:-|:-|
    | **Τι να** κάνουμε απόψε; | Что нам делать сегодня вечером? |
    | **Πού να** πάμε; | Куда нам пойти? |
    | **Πώς να** ταξιδέψουμε; | Как нам путешествовать? |
    | **Πότε να** φύγουμε; | Когда нам уехать? |
    | **Γιατί να** το κάνω; | Зачем мне это делать? |
    | **Ποιος να** αγοράσει τα εισιτήρια; | Кто должен купить билеты? |

    ### Ρήματα και εκφράσεις με Συνεχή Υποτακτική (σχεδόν πάντα) — Глаголы с Длительным сослагательным

    | Глагол | Пример | |
    |:-------|:-------|:-|
    | **Αρχίζω** | Άρχισα **να καπνίζω** όταν ήμουν 18 χρονών. | Начал курить в 18 лет. |
    | **Συνεχίζω** | Συνέχισα **να καπνίζω** μέχρι τα 35 μου. | Продолжал курить до 35. |
    | **Σταματάω** | Σταμάτησα **να καπνίζω** εδώ και λίγο καιρό. | Бросил курить некоторое время назад. |
    | **Παύω** | Πάψε **να μιλάς** όλη την ώρα. | Перестань говорить всё время. |
    | **Συνηθίζω** | Δε συνηθίζω **να οδηγώ** χωρίς ζώνη. | Я не привык ездить без ремня. |
    | **Μαθαίνω** | Έμαθα **να κολυμπάω** όταν ήμουν 6 χρονών. | Научился плавать в 6 лет. |
    | **Ξέρω** | Δυστυχώς δεν ξέρω **να παίζω** μουσική. | К сожалению, не умею играть на инструменте. |
    | **Μου αρέσει** | Μου αρέσει **να ταξιδεύω**. | Люблю путешествовать. |
    | **Τρελαίνομαι** | Τρελαίνομαι **να ακούω** μουσική. | Обожаю слушать музыку. |
    | **Βλέπω** | Τον είδα **να μπαίνει** στο δωμάτιο. | Видел, как он входил в комнату. |
    | **Ακούω** | Τον άκουσα **να κλαίει**. | Слышал, как он плакал. |
    | **Αισθάνομαι** | Αισθάνομαι την καρδιά μου **να χτυπάει** δυνατά. | Чувствую, как сердце бьётся сильно. |
    | **Νιώθω** | Νιώθω **να με ενοχλεί** κάτι. | Чувствую, что что-то меня беспокоит. |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Γραμματική 5: Ρήματα με Απλή ή Συνεχή Υποτακτική (σ.194)

    ### Ρήματα και εκφράσεις με Απλή Υποτακτική (σχεδόν πάντα)

    | Ρήμα | Παράδειγμα | |
    |:-----|:-----------|:-|
    | **Έχω να** | Έχω **να** δουλέψω. | I have work to do. |
    | **Πάω να** | Πάω **να** αγοράσω ψωμί. | I'm going to buy bread. |
    | **Ξέχασα να** | Ξέχασα **να** αγοράσω εφημερίδα. | I forgot to buy a newspaper. |
    | **Είμαι έτοιμος να** | Είμαι έτοιμος **να** φύγω. | I'm ready to leave. |
    | **Ψάχνω να** | Ψάχνω **να** βρω τα κλειδιά μου. | I'm trying to find my keys. |
    | **Αργείς να** | Αργείς **να** πας στη δουλειά σου; | Are you late for work? |
    | **Κοντεύω να** | Κοντεύω **να** τελειώσω το διάβασμα. | I'm almost done studying. |
    | **Περιμένω να** | Περιμένω **να** γυρίσει ο διευθυντής. | I'm waiting for the director to return. |
    | **Δεν πρόλαβα να** | Δεν πρόλαβα **να** διαβάσω. | I didn't have time to read. |
    | **είναι πιθανό να** | Είναι **πιθανό να** πάθεις ατύχημα. | It's possible you'll have an accident. |
    | **είναι απίθανο να** | Είναι **απίθανο να** τρακάρεις. | It's unlikely you'll crash. |

    **Ερωτηματικές προτάσεις με να:**

    | | |
    |:-|:-|
    | **Τι να** κάνουμε απόψε; | What should we do tonight? |
    | **Πού να** πάμε; | Where should we go? |
    | **Πώς να** ταξιδέψουμε; | How should we travel? |
    | **Πότε να** φύγουμε; | When should we leave? |
    | **Γιατί να** το κάνω; | Why should I do it? |
    | **Ποιος να** αγοράσει τα εισιτήρια; | Who should buy the tickets? |

    ### Ρήματα και εκφράσεις με Συνεχή Υποτακτική (σχεδόν πάντα)

    | Ρήμα | Παράδειγμα | |
    |:-----|:-----------|:-|
    | **Αρχίζω** | Άρχισα **να καπνίζω** όταν ήμουν 18 χρονών. | I started smoking when I was 18. |
    | **Συνεχίζω** | Συνέχισα **να καπνίζω** μέχρι τα 35 μου. | I kept smoking until I was 35. |
    | **Σταματάω** | Σταμάτησα **να καπνίζω** εδώ και λίγο καιρό. | I stopped smoking a while ago. |
    | **Παύω** | Πάψε **να μιλάς** όλη την ώρα. | Stop talking all the time. |
    | **Συνηθίζω** | Δε συνηθίζω **να οδηγώ** χωρίς ζώνη. | I don't usually drive without a seatbelt. |
    | **Μαθαίνω** | Έμαθα **να κολυμπάω** όταν ήμουν 6 χρονών. | I learned to swim when I was 6. |
    | **Ξέρω** | Δυστυχώς δεν ξέρω **να παίζω** μουσική. | Unfortunately I don't know how to play music. |
    | **Μου αρέσει** | Μου αρέσει **να ταξιδεύω**. | I love to travel. |
    | **Τρελαίνομαι** | Τρελαίνομαι **να ακούω** μουσική. | I'm crazy about listening to music. |
    | **Βλέπω** | Τον είδα **να μπαίνει** στο δωμάτιο. | I saw him enter the room. |
    | **Ακούω** | Τον άκουσα **να κλαίει**. | I heard him crying. |
    | **Αισθάνομαι** | Αισθάνομαι την καρδιά μου **να χτυπάει** δυνατά. | I feel my heart beating fast. |
    | **Νιώθω** | Νιώθω **να με ενοχλεί** κάτι. | I feel something bothering me. |
    """)
    else:
        _out = mo.md("""
    ## Grammar 5: Verbs with Simple or Continuous Subjunctive (p.194)

    ### Ρήματα και εκφράσεις με Απλή Υποτακτική (σχεδόν πάντα) — Verbs with Simple Subjunctive

    | Verb | Example | |
    |:-----|:--------|:-|
    | **Έχω να** | Έχω **να** δουλέψω. | I have work to do. |
    | **Πάω να** | Πάω **να** αγοράσω ψωμί. | I'm going to buy bread. |
    | **Ξέχασα να** | Ξέχασα **να** αγοράσω εφημερίδα. | I forgot to buy a newspaper. |
    | **Είμαι έτοιμος να** | Είμαι έτοιμος **να** φύγω. | I'm ready to leave. |
    | **Ψάχνω να** | Ψάχνω **να** βρω τα κλειδιά μου. | I'm trying to find my keys. |
    | **Αργείς να** | Αργείς **να** πας στη δουλειά σου; | Are you late for work? |
    | **Κοντεύω να** | Κοντεύω **να** τελειώσω το διάβασμα. | I'm almost done studying. |
    | **Περιμένω να** | Περιμένω **να** γυρίσει ο διευθυντής. | I'm waiting for the director to return. |
    | **Δεν πρόλαβα να** | Δεν πρόλαβα **να** διαβάσω. | I didn't have time to read. |
    | **είναι πιθανό να** | Είναι **πιθανό να** πάθεις ατύχημα. | It's possible you'll have an accident. |
    | **είναι απίθανο να** | Είναι **απίθανο να** τρακάρεις. | It's unlikely you'll crash. |

    **Interrogative clauses with να:**

    | | |
    |:-|:-|
    | **Τι να** κάνουμε απόψε; | What should we do tonight? |
    | **Πού να** πάμε; | Where should we go? |
    | **Πώς να** ταξιδέψουμε; | How should we travel? |
    | **Πότε να** φύγουμε; | When should we leave? |
    | **Γιατί να** το κάνω; | Why should I do it? |
    | **Ποιος να** αγοράσει τα εισιτήρια; | Who should buy the tickets? |

    ### Ρήματα και εκφράσεις με Συνεχή Υποτακτική (σχεδόν πάντα) — Verbs with Continuous Subjunctive

    | Verb | Example | |
    |:-----|:--------|:-|
    | **Αρχίζω** | Άρχισα **να καπνίζω** όταν ήμουν 18 χρονών. | I started smoking when I was 18. |
    | **Συνεχίζω** | Συνέχισα **να καπνίζω** μέχρι τα 35 μου. | I kept smoking until I was 35. |
    | **Σταματάω** | Σταμάτησα **να καπνίζω** εδώ και λίγο καιρό. | I stopped smoking a while ago. |
    | **Παύω** | Πάψε **να μιλάς** όλη την ώρα. | Stop talking all the time. |
    | **Συνηθίζω** | Δε συνηθίζω **να οδηγώ** χωρίς ζώνη. | I don't usually drive without a seatbelt. |
    | **Μαθαίνω** | Έμαθα **να κολυμπάω** όταν ήμουν 6 χρονών. | I learned to swim when I was 6. |
    | **Ξέρω** | Δυστυχώς δεν ξέρω **να παίζω** μουσική. | Unfortunately I don't know how to play music. |
    | **Μου αρέσει** | Μου αρέσει **να ταξιδεύω**. | I love to travel. |
    | **Τρελαίνομαι** | Τρελαίνομαι **να ακούω** μουσική. | I'm crazy about listening to music. |
    | **Βλέπω** | Τον είδα **να μπαίνει** στο δωμάτιο. | I saw him enter the room. |
    | **Ακούω** | Τον άκουσα **να κλαίει**. | I heard him crying. |
    | **Αισθάνομαι** | Αισθάνομαι την καρδιά μου **να χτυπάει** δυνατά. | I feel my heart beating fast. |
    | **Νιώθω** | Νιώθω **να με ενοχλεί** κάτι. | I feel something bothering me. |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Key phrases
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Разговорные фразы (Πώς το λένε;)

    | Греческий | Русский |
    |:----------|:--------|
    | **Ω, Θεέ μου!** | Боже мой! |
    | **Ρε άνθρωπέ μου, στραβός είσαι;** | Ты что, слепой? |
    | **Ολόκληρο ΣΤΟΠ δεν το είδες;** | Ты не увидел знак СТОП? |
    | **Φοβάμαι ότι το έσπασα.** | Боюсь, что сломал. |
    | **Ευτυχώς που φορούσε κράνος.** | Хорошо, что он был в шлеме. |
    | **Εμ, βέβαια! Αν μιλάς στο κινητό, πώς να προσέξεις τη μηχανή;** | Ну конечно! Если говоришь по телефону, как следить за мотоциклом? |
    | **Θα μπλέξετε άσχημα.** | Попадёте в большие неприятности. |
    | **Μπορεί να το πληρώσετε ακριβά.** | Это может вам дорого обойтись. |
    | **Πώς αισθάνεσαι;** | Как ты себя чувствуешь? |
    | **Αυτό είναι μάλλον λογικό.** | Это вполне понятно. |
    | **Κάπως λιγότερο, νομίζω.** | Немного меньше, думаю. |
    | **Εν πάση περιπτώσει...** | В любом случае... |
    | **Βγάζω ακτινογραφία** | Делаю рентген |
    | **Έχω κάταγμα** | У меня перелом |
    | **Ζαλίζομαι = Νιώθω ζαλάδα** | Испытываю головокружение |
    | **Παίρνω παυσίπονα** | Принимаю обезболивающее |
    | **Βάζω πάγο** | Прикладываю лёд |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Πώς το λένε;

    | Ελληνικά | Αγγλικά |
    |:---------|:--------|
    | **Ω, Θεέ μου!** | Oh, my God! |
    | **Ρε άνθρωπέ μου, στραβός είσαι;** | Are you blind, man? |
    | **Ολόκληρο ΣΤΟΠ δεν το είδες;** | You didn't see the whole STOP sign? |
    | **Φοβάμαι ότι το έσπασα.** | I'm afraid I broke it. |
    | **Ευτυχώς που φορούσε κράνος.** | Fortunately he was wearing a helmet. |
    | **Εμ, βέβαια! Αν μιλάς στο κινητό, πώς να προσέξεις τη μηχανή;** | Well, of course! If you're on the phone, how can you pay attention? |
    | **Θα μπλέξετε άσχημα.** | You'll get into serious trouble. |
    | **Μπορεί να το πληρώσετε ακριβά.** | You might pay dearly for it. |
    | **Πώς αισθάνεσαι;** | How are you feeling? |
    | **Αυτό είναι μάλλον λογικό.** | That's quite understandable. |
    | **Κάπως λιγότερο, νομίζω.** | Somewhat less, I think. |
    | **Εν πάση περιπτώσει...** | In any case... |
    | **Βγάζω ακτινογραφία** | I get an X-ray |
    | **Έχω κάταγμα** | I have a fracture |
    | **Ζαλίζομαι = Νιώθω ζαλάδα** | I feel dizzy |
    | **Παίρνω παυσίπονα** | I take painkillers |
    | **Βάζω πάγο** | I apply ice |
    """)
    else:
        _out = mo.md("""
    ## Useful Phrases (Πώς το λένε;)

    | Greek | English |
    |:------|:--------|
    | **Ω, Θεέ μου!** | Oh, my God! |
    | **Ρε άνθρωπέ μου, στραβός είσαι;** | Are you blind, man? |
    | **Ολόκληρο ΣΤΟΠ δεν το είδες;** | You didn't see the whole STOP sign? |
    | **Φοβάμαι ότι το έσπασα.** | I'm afraid I broke it. |
    | **Ευτυχώς που φορούσε κράνος.** | Fortunately he was wearing a helmet. |
    | **Εμ, βέβαια! Αν μιλάς στο κινητό, πώς να προσέξεις τη μηχανή;** | Well, of course! If you're on the phone, how can you pay attention? |
    | **Θα μπλέξετε άσχημα.** | You'll get into serious trouble. |
    | **Μπορεί να το πληρώσετε ακριβά.** | You might pay dearly for it. |
    | **Πώς αισθάνεσαι;** | How are you feeling? |
    | **Αυτό είναι μάλλον λογικό.** | That's quite understandable. |
    | **Κάπως λιγότερο, νομίζω.** | Somewhat less, I think. |
    | **Εν πάση περιπτώσει...** | In any case... |
    | **Βγάζω ακτινογραφία** | I get an X-ray |
    | **Έχω κάταγμα** | I have a fracture |
    | **Ζαλίζομαι = Νιώθω ζαλάδα** | I feel dizzy |
    | **Παίρνω παυσίπονα** | I take painkillers |
    | **Βάζω πάγο** | I apply ice |
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
    _ROOT = "https://raw.githubusercontent.com/EEE-project/created_with_eee/main"
    _cfg = _ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/modern_greek/ellinika_b/index.tsv",
    )
    _prev_url, _next_url = _cfg.adjacent_urls("chapter_12/")
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
    RAW_BASE = "https://raw.githubusercontent.com/EEE-project/created_with_eee/main/modern_greek/ellinika_b/chapter_12"
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
