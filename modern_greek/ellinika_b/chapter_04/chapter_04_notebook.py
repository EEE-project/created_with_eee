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
    }, ga_config=_cfg.ga_config())
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Title
    _lang = language_selector.value
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_BoDy4MqY588btgJnGdVhkH)"
    if _lang == "ru":
        _sub = "Глава 4 — Покупки и цены · B1"
        _gl, _tl = "Грамматика", "Тесты"
        _tc = "Существительные · Глаголы · Прилагательные"
    elif _lang == "el":
        _sub = "Ενότητα 4 — Αγορές & Τιμές · B1"
        _gl, _tl = "Γραμματική", "Τεστ"
        _tc = "Ουσιαστικά · Ρήματα · Επίθετα"
    else:
        _sub = "Unit 4 — Shopping & Prices · B1"
        _gl, _tl = "Grammar", "Tests"
        _tc = "Nouns · Verbs · Adjectives"
    _gc = "Επίθετα -ύς/-ιά/-ύ · Επίθετα -ής/-ιά/-ί · Συνίζηση"
    _out = mo.md(f"""# «Είναι πανάκριβα!» 🛍️
    ## {_sub} {_badge}

    **{_gl}:** {_gc}
    **{_tl}:** {_tc}
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Adjectives -ύς/-ιά/-ύ and -ής/-ιά/-ί
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ### Грамматика: Прилагательные на -ύς, -ιά, -ύ (стр. 66)

    Эти прилагательные описывают размеры и свойства. Пример: **ο φαρδύς** (широкий)

    | Падеж | Мужской | Женский | Средний |
    |-------|---------|---------|---------|
    | Им. ед. | ο φαρδύς | η φαρδιά | το φαρδύ |
    | Род. ед. | του φαρδιού / (του φαρδύ) | της φαρδιάς | του φαρδιού / (του φαρδύ) |
    | Вин. ед. | τον φαρδύ | τη φαρδιά | το φαρδύ |
    | Им. мн. | οι φαρδιοί | οι φαρδιές | τα φαρδιά |
    | Род. мн. | των φαρδιών | των φαρδιών | των φαρδιών |
    | Вин. мн. | τους φαρδιούς | τις φαρδιές | τα φαρδιά |

    Слова того же типа: **ελαφρύς** (лёгкий), **μακρύς** (длинный), **παχύς** (толстый), **βαρύς** (тяжёлый), **βαθύς** (глубокий), **πλατύς** (широкий).

    Примеры:
    - Ο γάτος σας, κυρία μου, είναι πολύ **παχύς**. Πρέπει να αρχίσει δίαιτα αμέσως! — _Ваш кот, мадам, очень толстый. Ему срочно нужна диета!_
    - Η μπλούζα είναι τέλεια, αλλά η φούστα είναι **φαρδιά**. Μήπως έχετε ένα νούμερο πιο μικρό; — _Блузка идеальна, а юбка широковата. У вас нет размера поменьше?_
    - Στο σημείο αυτό το ποτάμι γίνεται πολύ **βαθύ**. Προσέξτε! — _В этом месте река становится очень глубокой. Осторожно!_
    - Μην ανησυχείς. Οι δρόμοι της περιοχής είναι αρκετά **φαρδιοί** και μπορείς να παρκάρεις εύκολα. — _Не волнуйся. Улицы в этом районе довольно широкие, припарковаться легко._
    - Το πιστεύεις; Όταν ήταν νέος, ο Άγγελος είχε **μακριά** σγουρά μαλλιά! — _Представляешь? В молодости у Ангелоса были длинные вьющиеся волосы!_

    Шутка-скороговорка (про толстого священника, который ел жирную чечевицу):
    > Ο παπάς ο παχύς έφαγε παχιά φακή.
    > Γιατί, παπά παχύ, έφαγες παχιά φακή;
    > Θεέ μου, να πάθει γλωσσοδέτη.

    (Игра слов: γλωσσοδέτης значит «скороговорка» — дети желают священнику «языкозаплетение».)

    ---

    ### Грамматика: Прилагательные на -ής, -ιά, -ί — цвета (стр. 67)

    Пример: **ο καφετής** (коричневый)

    | Падеж | Мужской | Женский | Средний |
    |-------|---------|---------|---------|
    | Им. ед. | ο καφετής | η καφετιά | το καφετί |
    | Род. ед. | του καφετή / του καφετιού | της καφετιάς | του καφετιού |
    | Вин. ед. | τον καφετή | την καφετιά | το καφετί |
    | Им. мн. | οι καφετιοί | οι καφετιές | τα καφετιά |
    | Род. мн. | των καφετιών | των καφετιών | των καφετιών |
    | Вин. мн. | τους καφετιούς | τις καφετιές | τα καφετιά |

    Другие цвета этого типа: **βυσσινής** (вишнёвый), **θαλασσής** (морской), **κανελής** (коричный), **πορτοκαλής** (оранжевый), **σοκολατής** (шоколадный), **σταχτής** (пепельный), **χρυσαφής** (золотистый).

    Примеры:
    - Τίνος είναι αυτός ο **καφετής** σκύλος έξω από την πόρτα μας; — _Чья это коричневая собака у нашей двери?_
    - Η Χριστίνα αγόρασε για το μωρό μια ωραία, **θαλασσιά** φόρμα. — _Христина купила малышу красивый комбинезон морского цвета._
    - Εκείνο το **πορτοκαλί** κασκόλ μού αρέσει πολύ. Θα το αγοράσω. — _Мне очень нравится тот оранжевый шарф. Я его куплю._

    **καφετής – καφετιά – καφετί = καφετί**: в разговорной речи форма среднего рода часто используется неизменной вместо согласующейся формы:
    - Γιατί δε φοράς εκείνη την **καφετιά/καφετί** μπλούζα που σου αγόρασα πέρσι; — _Почему ты не носишь ту коричневую блузку, которую я купил(а) тебе в прошлом году?_
    - Μου αρέσουν τα ρούχα σε **καφετιούς/καφετί** τόνους. — _Мне нравится одежда коричневых тонов._
    - Πού είναι τα **καφετιά/καφετί** μου παπούτσια; — _Где мои коричневые туфли?_
    - Μου δανείζεις τις **πορτοκαλιές/πορτοκαλί** σου πιτζάμες; — _Одолжишь мне свою оранжевую пижаму?_
    - Ο **βυσσινής/βυσσινί** σκούφος μου είναι στο συρτάρι. Μου τον φέρνεις, σε παρακαλώ; — _Моя вишнёвая шапка в ящике. Принесёшь мне её, пожалуйста?_
    - Σου πάνε πολύ αυτές οι **θαλασσιές/θαλασσί** κάλτσες. — _Тебе очень идут эти носки цвета морской волны._
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ### Γραμματική: Επίθετα σε -ύς, -ιά, -ύ (σ. 66)

    Αυτά τα επίθετα περιγράφουν διαστάσεις και ιδιότητες. Παράδειγμα: **ο φαρδύς** (wide)

    | Πτώση | Αρσενικό | Θηλυκό | Ουδέτερο |
    |-------|----------|--------|----------|
    | Ονομ. Εν. | ο φαρδύς | η φαρδιά | το φαρδύ |
    | Γεν. Εν. | του φαρδιού / (του φαρδύ) | της φαρδιάς | του φαρδιού / (του φαρδύ) |
    | Αιτ. Εν. | τον φαρδύ | τη φαρδιά | το φαρδύ |
    | Ονομ. Πλ. | οι φαρδιοί | οι φαρδιές | τα φαρδιά |
    | Γεν. Πλ. | των φαρδιών | των φαρδιών | των φαρδιών |
    | Αιτ. Πλ. | τους φαρδιούς | τις φαρδιές | τα φαρδιά |

    Άλλες λέξεις του ίδιου τύπου: **ελαφρύς** (light), **μακρύς** (long), **παχύς** (fat), **βαρύς** (heavy), **βαθύς** (deep), **πλατύς** (broad).

    Παραδείγματα:
    - Ο γάτος σας, κυρία μου, είναι πολύ **παχύς**. Πρέπει να αρχίσει δίαιτα αμέσως! ("Your cat, madam, is very fat. He needs to start a diet right away!")
    - Η μπλούζα είναι τέλεια, αλλά η φούστα είναι **φαρδιά**. Μήπως έχετε ένα νούμερο πιο μικρό; ("The blouse is perfect, but the skirt is loose. Would you happen to have a smaller size?")
    - Στο σημείο αυτό το ποτάμι γίνεται πολύ **βαθύ**. Προσέξτε! ("At this point the river gets very deep. Be careful!")
    - Μην ανησυχείς. Οι δρόμοι της περιοχής είναι αρκετά **φαρδιοί** και μπορείς να παρκάρεις εύκολα. ("Don't worry. The streets around here are quite wide, and you can park easily.")
    - Το πιστεύεις; Όταν ήταν νέος, ο Άγγελος είχε **μακριά** σγουρά μαλλιά! ("Can you believe it? When he was young, Angelos had long curly hair!")

    Γλωσσοδέτης-αστείο (για έναν παχύ παπά που έφαγε παχιά φακή) — ("Tongue-twister joke, about a fat priest who ate fat lentils"):
    > Ο παπάς ο παχύς έφαγε παχιά φακή.
    > Γιατί, παπά παχύ, έφαγες παχιά φακή;
    > Θεέ μου, να πάθει γλωσσοδέτη.

    (The punchline is a pun: γλωσσοδέτης means "tongue-twister," so the children wish the priest a "tongue-tying.")

    ---

    ### Γραμματική: Επίθετα σε -ής, -ιά, -ί — χρώματα (σ. 67)

    Παράδειγμα: **ο καφετής** (brown)

    | Πτώση | Αρσενικό | Θηλυκό | Ουδέτερο |
    |-------|----------|--------|----------|
    | Ονομ. Εν. | ο καφετής | η καφετιά | το καφετί |
    | Γεν. Εν. | του καφετή / του καφετιού | της καφετιάς | του καφετιού |
    | Αιτ. Εν. | τον καφετή | την καφετιά | το καφετί |
    | Ονομ. Πλ. | οι καφετιοί | οι καφετιές | τα καφετιά |
    | Γεν. Πλ. | των καφετιών | των καφετιών | των καφετιών |
    | Αιτ. Πλ. | τους καφετιούς | τις καφετιές | τα καφετιά |

    Άλλα χρώματα του ίδιου τύπου: **βυσσινής** (maroon), **θαλασσής** (sea-blue), **κανελής** (cinnamon), **πορτοκαλής** (orange), **σοκολατής** (chocolate), **σταχτής** (ash-grey), **χρυσαφής** (golden).

    Παραδείγματα:
    - Τίνος είναι αυτός ο **καφετής** σκύλος έξω από την πόρτα μας; ("Whose brown dog is this outside our door?")
    - Η Χριστίνα αγόρασε για το μωρό μια ωραία, **θαλασσιά** φόρμα. ("Christina bought the baby a nice sea-blue onesie.")
    - Εκείνο το **πορτοκαλί** κασκόλ μού αρέσει πολύ. Θα το αγοράσω. ("I really like that orange scarf. I'll buy it.")

    **καφετής – καφετιά – καφετί = καφετί**: στην καθομιλουμένη, ο ουδέτερος τύπος χρησιμοποιείται συχνά αμετάβλητος αντί για τον κανονικό τύπο:
    - Γιατί δε φοράς εκείνη την **καφετιά/καφετί** μπλούζα που σου αγόρασα πέρσι; ("Why don't you wear that brown blouse I bought you last year?")
    - Μου αρέσουν τα ρούχα σε **καφετιούς/καφετί** τόνους. ("I like clothes in brown tones.")
    - Πού είναι τα **καφετιά/καφετί** μου παπούτσια; ("Where are my brown shoes?")
    - Μου δανείζεις τις **πορτοκαλιές/πορτοκαλί** σου πιτζάμες; ("Will you lend me your orange pajamas?")
    - Ο **βυσσινής/βυσσινί** σκούφος μου είναι στο συρτάρι. Μου τον φέρνεις, σε παρακαλώ; ("My maroon hat is in the drawer. Will you bring it to me, please?")
    - Σου πάνε πολύ αυτές οι **θαλασσιές/θαλασσί** κάλτσες. ("Those sea-blue socks really suit you.")
    """)
    else:
        _md = mo.md("""
    ### Grammar: Adjectives ending in -ύς, -ιά, -ύ (p. 66)

    These adjectives describe dimensions and properties. Example: **ο φαρδύς** (wide)

    | Case | Masculine | Feminine | Neuter |
    |------|-----------|----------|--------|
    | Nom. Sg. | ο φαρδύς | η φαρδιά | το φαρδύ |
    | Gen. Sg. | του φαρδιού / (του φαρδύ) | της φαρδιάς | του φαρδιού / (του φαρδύ) |
    | Acc. Sg. | τον φαρδύ | τη φαρδιά | το φαρδύ |
    | Nom. Pl. | οι φαρδιοί | οι φαρδιές | τα φαρδιά |
    | Gen. Pl. | των φαρδιών | των φαρδιών | των φαρδιών |
    | Acc. Pl. | τους φαρδιούς | τις φαρδιές | τα φαρδιά |

    Other words of the same type: **ελαφρύς** (light), **μακρύς** (long), **παχύς** (fat/thick), **βαρύς** (heavy), **βαθύς** (deep), **πλατύς** (broad).

    Examples:
    - Ο γάτος σας, κυρία μου, είναι πολύ **παχύς**. Πρέπει να αρχίσει δίαιτα αμέσως! — _Your cat, madam, is very fat. He needs to start a diet right away!_
    - Η μπλούζα είναι τέλεια, αλλά η φούστα είναι **φαρδιά**. Μήπως έχετε ένα νούμερο πιο μικρό; — _The blouse is perfect, but the skirt is loose. Would you happen to have a smaller size?_
    - Στο σημείο αυτό το ποτάμι γίνεται πολύ **βαθύ**. Προσέξτε! — _At this point the river gets very deep. Be careful!_
    - Μην ανησυχείς. Οι δρόμοι της περιοχής είναι αρκετά **φαρδιοί** και μπορείς να παρκάρεις εύκολα. — _Don't worry. The streets around here are quite wide, and you can park easily._
    - Το πιστεύεις; Όταν ήταν νέος, ο Άγγελος είχε **μακριά** σγουρά μαλλιά! — _Can you believe it? When he was young, Angelos had long curly hair!_

    Tongue-twister joke (about a fat priest who ate fat lentils):
    > Ο παπάς ο παχύς έφαγε παχιά φακή.
    > Γιατί, παπά παχύ, έφαγες παχιά φακή;
    > Θεέ μου, να πάθει γλωσσοδέτη.

    (The punchline is a pun: γλωσσοδέτης means "tongue-twister," so the children wish the priest a "tongue-tying.")

    ---

    ### Grammar: Adjectives ending in -ής, -ιά, -ί — colors (p. 67)

    Example: **ο καφετής** (brown)

    | Case | Masculine | Feminine | Neuter |
    |------|-----------|----------|--------|
    | Nom. Sg. | ο καφετής | η καφετιά | το καφετί |
    | Gen. Sg. | του καφετή / του καφετιού | της καφετιάς | του καφετιού |
    | Acc. Sg. | τον καφετή | την καφετιά | το καφετί |
    | Nom. Pl. | οι καφετιοί | οι καφετιές | τα καφετιά |
    | Gen. Pl. | των καφετιών | των καφετιών | των καφετιών |
    | Acc. Pl. | τους καφετιούς | τις καφετιές | τα καφετιά |

    Other colors of the same type: **βυσσινής** (maroon), **θαλασσής** (sea-blue), **κανελής** (cinnamon), **πορτοκαλής** (orange), **σοκολατής** (chocolate-brown), **σταχτής** (ash-grey), **χρυσαφής** (golden).

    Examples:
    - Τίνος είναι αυτός ο **καφετής** σκύλος έξω από την πόρτα μας; — _Whose brown dog is this outside our door?_
    - Η Χριστίνα αγόρασε για το μωρό μια ωραία, **θαλασσιά** φόρμα. — _Christina bought the baby a nice sea-blue onesie._
    - Εκείνο το **πορτοκαλί** κασκόλ μού αρέσει πολύ. Θα το αγοράσω. — _I really like that orange scarf. I'll buy it._

    **καφετής – καφετιά – καφετί = καφετί**: in everyday speech the neuter form is often used unchanged instead of the properly agreeing form:
    - Γιατί δε φοράς εκείνη την **καφετιά/καφετί** μπλούζα που σου αγόρασα πέρσι; — _Why don't you wear that brown blouse I bought you last year?_
    - Μου αρέσουν τα ρούχα σε **καφετιούς/καφετί** τόνους. — _I like clothes in brown tones._
    - Πού είναι τα **καφετιά/καφετί** μου παπούτσια; — _Where are my brown shoes?_
    - Μου δανείζεις τις **πορτοκαλιές/πορτοκαλί** σου πιτζάμες; — _Will you lend me your orange pajamas?_
    - Ο **βυσσινής/βυσσινί** σκούφος μου είναι στο συρτάρι. Μου τον φέρνεις, σε παρακαλώ; — _My maroon hat is in the drawer. Will you bring it to me, please?_
    - Σου πάνε πολύ αυτές οι **θαλασσιές/θαλασσί** κάλτσες. — _Those sea-blue socks really suit you._
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Phrases
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ### Полезные фразы (Πώς το λένε;)

    **Стр. 63 — в обувном магазине (диалог A17):**

    | Греческий | Русский |
    |-----------|---------|
    | Να βοηθήσω; | Помочь вам? |
    | Κάνατε πολύ καλή επιλογή. | Вы сделали очень хороший выбор. |
    | Εξαρτάται. | Смотря как. |
    | Πώς σας φαίνεται; | Как вам кажется? |
    | Δε με τρελαίνει. | Не в восторге. |
    | Μα τι λέτε; | Да что вы такое говорите?! |
    | Ευχαρίστως. | С удовольствием. |
    | Για εσάς θα κάνουμε καλύτερη τιμή. | Для вас сделаем цену получше. |
    | Πανάκριβα είναι! | Это слишком дорого! |
    | Εδώ που φτάσαμε... | Раз уж так вышло... |
    | Α πα πα πα! | Ой-ой-ой! |
    | Ούτε να ακούω δε θέλω... | Даже слышать не хочу... |
    | Μετρητά και πάλι μετρητά. | Наличными, и только наличными. |
    | Κρατήστε εκατό ευρώ. | Возьмите сто евро. |
    | Θα μείνετε ικανοποιημένη. | Вы останетесь довольны. |
    | Με γεια σας. | Носите на здоровье! |

    **Стр. 64-65 — цена и мнение об одежде** (это не отдельные фразы, а вопросы с вариантами ответов):

    | Вопрос | Возможные ответы |
    |--------|-------------------|
    | **Πόσο κάνει/κοστίζει;** _(Сколько это стоит?)_ | Κάνει/κοστίζει 32,50. _(Стоит 32,50.)_ Είναι πάμφθηνο! Είναι πανάκριβο! _(Это очень дёшево! Это слишком дорого!)_ Είναι σε πολύ λογική τιμή. _(По очень разумной цене.)_ Είναι σχεδόν τσάμπα. / Είναι δωρεάν. _(Почти бесплатно. / Бесплатно.)_ |
    | **Πόσο κάνουν/κοστίζουν;** _(Сколько они стоят?)_ | Κάνουν/Κοστίζουν 29 ευρώ. _(29 евро.)_ Είναι φτηνά! Θα τα αγοράσω. _(Дёшево! Куплю.)_ Είναι πολύ ακριβά! Θα περιμένω τις εκπτώσεις. _(Очень дорого! Подожду скидок.)_ |
    | **Θα μου κάνετε καλύτερη τιμή;** _(Сделаете мне скидку получше?)_ | Βεβαίως. Θα σας κάνουμε έκπτωση 10 ευρώ. _(Конечно. Сделаем скидку 10 евро.)_ Θα σας το/τα αφήσουμε 40 ευρώ από 45. _(Отдадим за 40 вместо 45.)_ |
    | **Θέλετε κάτι; Να (σας) βοηθήσω;** _(Вам что-нибудь нужно? Помочь?)_ | Ναι, θα ήθελα ένα πουκάμισο. _(Да, хотел(а) бы рубашку.)_ |
    | **Θέλετε βοήθεια;** _(Нужна помощь?)_ | Όχι, ευχαριστώ! Τα καταφέρνω και μόνος/μόνη μου. _(Нет, спасибо! Я сам(а) справлюсь.)_ |
    | **Πώς μπορώ να σας εξυπηρετήσω;** _(Чем могу вам помочь?)_ | Έχετε αυτή την μπλούζα σε πράσινο χρώμα; _(У вас есть эта блузка зелёного цвета?)_ |
    | **Τι θέλει η κοπέλα / ο νεαρός;** _(Что нужно девушке/парню?)_ | Θέλω / Θα ήθελα δύο ζευγάρια κάλτσες. _(Хочу / хотел(а) бы две пары носков.)_ |
    | **Εσύ τι λες; / Πώς σου φαίνεται; / Εσείς τι λέτε; / Πώς το βλέπετε; / Πώς σας φαίνεται;** _(Что скажешь? Как тебе/вам кажется?)_ | Είναι πολύ ωραίο πάνω σου/σας. _(Очень хорошо на тебе/вас смотрится.)_ Σου/Σας πάει πολύ. _(Тебе/вам очень идёт.)_ Σου/Σας ταιριάζει. _(Подходит.)_ Είναι τέλειο. _(Идеально.)_ Είναι φανταστικό. _(Потрясающе.)_ Είναι καλύτερο από το προηγούμενο. _(Лучше, чем предыдущее.)_ Αυτό μου αρέσει πιο πολύ. _(Это мне нравится больше.)_ Δε σου/σας πάει πολύ. _(Не очень тебе/вам идёт.)_ Δε μου αρέσει καθόλου. Είναι χάλια! _(Совсем не нравится. Ужас!)_ |

    **Стр. 70 — «Φωτιά και λαύρα, Παναγιώτη μου!» (диалог A18):**

    | Греческий | Русский |
    |-----------|---------|
    | Σε χάσαμε. | Тебя совсем не видно. |
    | Πες μου τώρα ότι έχεις και παράπονο! | Только не говори, что ты ещё и жалуешься! |
    | Καλά, μια κουβέντα είπα. Για να σε πειράξω. | Ладно, это я так, пошутить. |
    | Άσε τι έπαθα σήμερα. | Не спрашивай, что со мной сегодня случилось. |
    | Τι κάνει αυτή η ψυχή; | Как там наша душенька? |
    | Περνάει ζωή και κότα, ε; | Живёт как у Христа за пазухой, да? |
    | Και μη χειρότερα! | Могло быть и хуже! |
    | Άσ' τα, μην τα συζητάς καλύτερα. | Даже не говори, лучше не спрашивай. |
    | Μου έφυγαν τριάντα ευρώ. | Улетело тридцать евро. |
    | Σε χαιρετώ. | Ну, пока. |
    | Τρέχω να προλάβω. | Бегу, а то не успею. |
    | Καλές δουλειές. | Удачи с делами. |
    | Μπάι! | Пока! |

    **Стр. 72 — «Μπορώ να το αλλάξω;» (диалог A20, возврат неисправного телефона):**

    | Греческий | Русский |
    |-----------|---------|
    | Για να το δω λίγο. | Дайте-ка я посмотрю. |
    | Ακολουθήστε πιστά τις οδηγίες; | Вы точно следовали инструкции? |
    | Εννοείται! | Конечно! |
    | Ασφαλώς. | Разумеется. |
    | Αλίμονο! | Да что вы, не за что! |
    | Τη δουλειά μου κάνω. | Просто делаю свою работу. |
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ### Χρήσιμες φράσεις (Πώς το λένε;)

    **Σ. 63 — στο κατάστημα παπουτσιών (διάλογος A17):**

    | Ελληνικά | Αγγλικά |
    |----------|---------|
    | Να βοηθήσω; | Can I help (you)? |
    | Κάνατε πολύ καλή επιλογή. | You made a very good choice. |
    | Εξαρτάται. | It depends. |
    | Πώς σας φαίνεται; | How does it seem to you? |
    | Δε με τρελαίνει. | I'm not crazy about it. |
    | Μα τι λέτε; | But what are you saying?! |
    | Ευχαρίστως. | Gladly. |
    | Για εσάς θα κάνουμε καλύτερη τιμή. | For you we'll make a better price. |
    | Πανάκριβα είναι! | They're way too expensive! |
    | Εδώ που φτάσαμε... | Given where things stand now... |
    | Α πα πα πα! | Oh no no no! |
    | Ούτε να ακούω δε θέλω... | I don't even want to hear about it... |
    | Μετρητά και πάλι μετρητά. | Cash, and only cash. |
    | Κρατήστε εκατό ευρώ. | Take a hundred euros. |
    | Θα μείνετε ικανοποιημένη. | You'll be satisfied. |
    | Με γεια σας. | Wear it in good health! |

    **Σ. 64-65 — τιμή και γνώμη για ρούχα** (δεν είναι μεμονωμένες φράσεις, αλλά ερωτήσεις με πιθανές απαντήσεις):

    | Ερώτηση | Πιθανές απαντήσεις |
    |---------|---------------------|
    | **Πόσο κάνει/κοστίζει;** _(How much is it?)_ | Κάνει/κοστίζει 32,50. _(It costs 32.50.)_ Είναι πάμφθηνο! Είναι πανάκριβο! _(It's dirt cheap! It's way too expensive!)_ Είναι σε πολύ λογική τιμή. _(It's a very reasonable price.)_ Είναι σχεδόν τσάμπα. / Είναι δωρεάν. _(It's almost free. / It's free.)_ |
    | **Πόσο κάνουν/κοστίζουν;** _(How much are they?)_ | Κάνουν/Κοστίζουν 29 ευρώ. _(They're 29 euros.)_ Είναι φτηνά! Θα τα αγοράσω. _(They're cheap! I'll buy them.)_ Είναι πολύ ακριβά! Θα περιμένω τις εκπτώσεις. _(They're very expensive! I'll wait for the sales.)_ |
    | **Θα μου κάνετε καλύτερη τιμή;** _(Will you give me a better price?)_ | Βεβαίως. Θα σας κάνουμε έκπτωση 10 ευρώ. _(Of course. We'll give you a 10-euro discount.)_ Θα σας το/τα αφήσουμε 40 ευρώ από 45. _(We'll let you have it for 40 instead of 45.)_ |
    | **Θέλετε κάτι; Να (σας) βοηθήσω;** _(Do you need anything? Can I help you?)_ | Ναι, θα ήθελα ένα πουκάμισο. _(Yes, I'd like a shirt.)_ |
    | **Θέλετε βοήθεια;** _(Do you need help?)_ | Όχι, ευχαριστώ! Τα καταφέρνω και μόνος/μόνη μου. _(No, thanks! I can manage on my own.)_ |
    | **Πώς μπορώ να σας εξυπηρετήσω;** _(How can I help you?)_ | Έχετε αυτή την μπλούζα σε πράσινο χρώμα; _(Do you have this blouse in green?)_ |
    | **Τι θέλει η κοπέλα / ο νεαρός;** _(What would the young lady/man like?)_ | Θέλω / Θα ήθελα δύο ζευγάρια κάλτσες. _(I want / I'd like two pairs of socks.)_ |
    | **Εσύ τι λες; / Πώς σου φαίνεται; / Εσείς τι λέτε; / Πώς το βλέπετε; / Πώς σας φαίνεται;** _(What do you say? How does it look to you?)_ | Είναι πολύ ωραίο πάνω σου/σας. _(It looks great on you.)_ Σου/Σας πάει πολύ. _(It really suits you.)_ Σου/Σας ταιριάζει. _(It fits you.)_ Είναι τέλειο. _(It's perfect.)_ Είναι φανταστικό. _(It's fantastic.)_ Είναι καλύτερο από το προηγούμενο. _(It's better than the previous one.)_ Αυτό μου αρέσει πιο πολύ. _(I like this one more.)_ Δε σου/σας πάει πολύ. _(It doesn't suit you well.)_ Δε μου αρέσει καθόλου. Είναι χάλια! _(I don't like it at all. It's terrible!)_ |

    **Σ. 70 — «Φωτιά και λαύρα, Παναγιώτη μου!» (διάλογος A18):**

    | Ελληνικά | Αγγλικά |
    |----------|---------|
    | Σε χάσαμε. | We haven't seen you around. |
    | Πες μου τώρα ότι έχεις και παράπονο! | Now don't tell me you're complaining too! |
    | Καλά, μια κουβέντα είπα. Για να σε πειράξω. | Fine, it was just a comment. To tease you. |
    | Άσε τι έπαθα σήμερα. | Don't even ask what happened to me today. |
    | Τι κάνει αυτή η ψυχή; | How's the dear thing doing? |
    | Περνάει ζωή και κότα, ε; | Living the good life, huh? |
    | Και μη χειρότερα! | Could've been worse! |
    | Άσ' τα, μην τα συζητάς καλύτερα. | Never mind, better not talk about it. |
    | Μου έφυγαν τριάντα ευρώ. | I'm thirty euros lighter. |
    | Σε χαιρετώ. | I'll say bye then. |
    | Τρέχω να προλάβω. | I'm rushing off to make it in time. |
    | Καλές δουλειές. | Good luck with your errands. |
    | Μπάι! | Bye! |

    **Σ. 72 — «Μπορώ να το αλλάξω;» (διάλογος A20):**

    | Ελληνικά | Αγγλικά |
    |----------|---------|
    | Για να το δω λίγο. | Let me have a look at it. |
    | Ακολουθήστε πιστά τις οδηγίες; | Did you follow the instructions exactly? |
    | Εννοείται! | Of course! |
    | Ασφαλώς. | Certainly. |
    | Αλίμονο! | Not at all! |
    | Τη δουλειά μου κάνω. | I'm just doing my job. |
    """)
    else:
        _md = mo.md("""
    ### Useful Phrases (Πώς το λένε;)

    **p. 63 — at the shoe store (dialogue A17):**

    | Greek | English |
    |-------|---------|
    | Να βοηθήσω; | Can I help (you)? |
    | Κάνατε πολύ καλή επιλογή. | You made a very good choice. |
    | Εξαρτάται. | It depends. |
    | Πώς σας φαίνεται; | How does it seem to you? |
    | Δε με τρελαίνει. | I'm not crazy about it. |
    | Μα τι λέτε; | But what are you saying?! |
    | Ευχαρίστως. | Gladly. |
    | Για εσάς θα κάνουμε καλύτερη τιμή. | For you we'll make a better price. |
    | Πανάκριβα είναι! | They're way too expensive! |
    | Εδώ που φτάσαμε... | Given where things stand now... |
    | Α πα πα πα! | Oh no no no! |
    | Ούτε να ακούω δε θέλω... | I don't even want to hear about it... |
    | Μετρητά και πάλι μετρητά. | Cash, and only cash. |
    | Κρατήστε εκατό ευρώ. | Take a hundred euros. |
    | Θα μείνετε ικανοποιημένη. | You'll be satisfied. |
    | Με γεια σας. | Wear it in good health! |

    **p. 64-65 — price and opinion on clothes** (this isn't a list of separate phrases — it's a set of questions with their possible answers):

    | Question | Possible answers |
    |----------|-------------------|
    | **Πόσο κάνει/κοστίζει;** _(How much is it?)_ | Κάνει/κοστίζει 32,50. _(It costs 32.50.)_ Είναι πάμφθηνο! Είναι πανάκριβο! _(It's dirt cheap! It's way too expensive!)_ Είναι σε πολύ λογική τιμή. _(It's a very reasonable price.)_ Είναι σχεδόν τσάμπα. / Είναι δωρεάν. _(It's almost free. / It's free.)_ |
    | **Πόσο κάνουν/κοστίζουν;** _(How much are they?)_ | Κάνουν/Κοστίζουν 29 ευρώ. _(They're 29 euros.)_ Είναι φτηνά! Θα τα αγοράσω. _(They're cheap! I'll buy them.)_ Είναι πολύ ακριβά! Θα περιμένω τις εκπτώσεις. _(They're very expensive! I'll wait for the sales.)_ |
    | **Θα μου κάνετε καλύτερη τιμή;** _(Will you give me a better price?)_ | Βεβαίως. Θα σας κάνουμε έκπτωση 10 ευρώ. _(Of course. We'll give you a 10-euro discount.)_ Θα σας το/τα αφήσουμε 40 ευρώ από 45. _(We'll let you have it for 40 instead of 45.)_ |
    | **Θέλετε κάτι; Να (σας) βοηθήσω;** _(Do you need anything? Can I help you?)_ | Ναι, θα ήθελα ένα πουκάμισο. _(Yes, I'd like a shirt.)_ |
    | **Θέλετε βοήθεια;** _(Do you need help?)_ | Όχι, ευχαριστώ! Τα καταφέρνω και μόνος/μόνη μου. _(No, thanks! I can manage on my own.)_ |
    | **Πώς μπορώ να σας εξυπηρετήσω;** _(How can I help you?)_ | Έχετε αυτή την μπλούζα σε πράσινο χρώμα; _(Do you have this blouse in green?)_ |
    | **Τι θέλει η κοπέλα / ο νεαρός;** _(What would the young lady/man like?)_ | Θέλω / Θα ήθελα δύο ζευγάρια κάλτσες. _(I want / I'd like two pairs of socks.)_ |
    | **Εσύ τι λες; / Πώς σου φαίνεται; / Εσείς τι λέτε; / Πώς το βλέπετε; / Πώς σας φαίνεται;** _(What do you say? How does it look to you?)_ | Είναι πολύ ωραίο πάνω σου/σας. _(It looks great on you.)_ Σου/Σας πάει πολύ. _(It really suits you.)_ Σου/Σας ταιριάζει. _(It fits you.)_ Είναι τέλειο. _(It's perfect.)_ Είναι φανταστικό. _(It's fantastic.)_ Είναι καλύτερο από το προηγούμενο. _(It's better than the previous one.)_ Αυτό μου αρέσει πιο πολύ. _(I like this one more.)_ Δε σου/σας πάει πολύ. _(It doesn't suit you well.)_ Δε μου αρέσει καθόλου. Είναι χάλια! _(I don't like it at all. It's terrible!)_ |

    **p. 70 — "Φωτιά και λαύρα, Παναγιώτη μου!" (dialogue A18):**

    | Greek | English |
    |-------|---------|
    | Σε χάσαμε. | We haven't seen you around. |
    | Πες μου τώρα ότι έχεις και παράπονο! | Now don't tell me you're complaining too! |
    | Καλά, μια κουβέντα είπα. Για να σε πειράξω. | Fine, it was just a comment. To tease you. |
    | Άσε τι έπαθα σήμερα. | Don't even ask what happened to me today. |
    | Τι κάνει αυτή η ψυχή; | How's the dear thing doing? |
    | Περνάει ζωή και κότα, ε; | Living the good life, huh? |
    | Και μη χειρότερα! | Could've been worse! |
    | Άσ' τα, μην τα συζητάς καλύτερα. | Never mind, better not talk about it. |
    | Μου έφυγαν τριάντα ευρώ. | I'm thirty euros lighter. |
    | Σε χαιρετώ. | I'll say bye then. |
    | Τρέχω να προλάβω. | I'm rushing off to make it in time. |
    | Καλές δουλειές. | Good luck with your errands. |
    | Μπάι! | Bye! |

    **p. 72 — "Μπορώ να το αλλάξω;" (dialogue A20):**

    | Greek | English |
    |-------|---------|
    | Για να το δω λίγο. | Let me have a look at it. |
    | Ακολουθήστε πιστά τις οδηγίες; | Did you follow the instructions exactly? |
    | Εννοείται! | Of course! |
    | Ασφαλώς. | Certainly. |
    | Αλίμονο! | Not at all! |
    | Τη δουλειά μου κάνω. | I'm just doing my job. |
    """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Pronunciation cell
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
    ### Произношение: Φωνή-γραφή (стр. 76)

    Не новое правило, а повторение синизиса (слияния гласных) из Главы 3 на новом материале, плюс отдельное упражнение на слух для различения окончаний -ύς/-ιά, которые вы только что выучили в этой главе.

    **2.0 (A21) — «Обведи слова, которые слышишь»**: упражнение на различение ударного окончания женского рода -ιά/-ιές (**φαρδιά**) от мужского/среднего -ύ/-ού/-ούς (φαρδύ, φαρδιού) — окончаний прилагательных на -ύς/-ιά/-ύ. Список слов: φαρδού, (φαρδιά), βυσσινιές, βυσσινιά, πορτοκαλιά, πορτοκαλιές, μακρύς, μακριές, παχιά, παχύ, πλατιές, πλατιούς, βαριά, βαριές.

    **2.1 (A22) — «Послушай и распредели по столбцам»**: то же явление синизиса, что и в Главе 3 (безударное /i/ + гласный сливаются в один слог, а качество этого слияния зависит от предыдущего согласного) — здесь на новых словах этой главы. Пример: **μάτια** (глаза). Список слов: μάτια, διαβάζω, μολύβια, εισιτήρια, ποτήρια, βαθιά, καμιά, πόδια, εστιατόρια, σπίτια, βαριά, βυσσινιά, κανελιά, παιδιά, πιάνω, κομπιούτερ, τραπέζια, πορτοκαλιές, γυμναστήριο.
    """)
    elif _lang == 'el':
        _md = mo.md("""
    ### Φωνή-γραφή (σ. 76)

    Δεν είναι νέος κανόνας, αλλά επανάληψη της συνίζησης από το Κεφάλαιο 3 με νέο υλικό, συν μια ξεχωριστή ακουστική άσκηση για τη διάκριση των καταλήξεων -ύς/-ιά που μόλις μάθατε σε αυτό το κεφάλαιο.

    **2.0 (A21) — «Βάζω σε κύκλο τις λέξεις που ακούω»**: άσκηση διάκρισης της τονισμένης θηλυκής κατάληξης -ιά/-ιές (**φαρδιά**) από την αρσενική/ουδέτερη -ύ/-ού/-ούς (φαρδύ, φαρδιού) των επιθέτων σε -ύς/-ιά/-ύ. Λέξεις: φαρδού, (φαρδιά), βυσσινιές, βυσσινιά, πορτοκαλιά, πορτοκαλιές, μακρύς, μακριές, παχιά, παχύ, πλατιές, πλατιούς, βαριά, βαριές.

    **2.1 (A22) — «Ακούω τις λέξεις και τις βάζω στη σωστή στήλη»**: το ίδιο φαινόμενο συνίζησης του Κεφαλαίου 3 (το άτονο /i/ + φωνήεν συγχωνεύονται σε μία συλλαβή, με την ποιότητα να εξαρτάται από το προηγούμενο σύμφωνο), εδώ με το λεξιλόγιο αυτού του κεφαλαίου. Παράδειγμα: **μάτια** (eyes). Λέξεις: μάτια, διαβάζω, μολύβια, εισιτήρια, ποτήρια, βαθιά, καμιά, πόδια, εστιατόρια, σπίτια, βαριά, βυσσινιά, κανελιά, παιδιά, πιάνω, κομπιούτερ, τραπέζια, πορτοκαλιές, γυμναστήριο.
    """)
    else:
        _md = mo.md("""
    ### Pronunciation: Φωνή-γραφή (p. 76)

    Not a new rule — a redrill of Chapter 3's synizesis (vowel-merging) with fresh vocabulary, plus a dedicated listening exercise for the -ύς/-ιά endings just introduced in this chapter's own grammar.

    **2.0 (A21) — "Circle the words you hear"**: an exercise in distinguishing the stressed feminine -ιά/-ιές ending (**φαρδιά**) from the masculine/neuter -ύ/-ού/-ούς endings (φαρδύ, φαρδιού) of -ύς/-ιά/-ύ adjectives. Word list: φαρδού, (φαρδιά), βυσσινιές, βυσσινιά, πορτοκαλιά, πορτοκαλιές, μακρύς, μακριές, παχιά, παχύ, πλατιές, πλατιούς, βαριά, βαριές.

    **2.1 (A22) — "Listen and sort into the correct column"**: the same synizesis phenomenon documented in Chapter 3 (unstressed /i/ + vowel merges into one syllable, with the exact glide quality depending on the preceding consonant) — redrilled here with this chapter's own vocabulary. Worked example: **μάτια** (eyes). Word list: μάτια, διαβάζω, μολύβια, εισιτήρια, ποτήρια, βαθιά, καμιά, πόδια, εστιατόρια, σπίτια, βαριά, βυσσινιά, κανελιά, παιδιά, πιάνω, κομπιούτερ, τραπέζια, πορτοκαλιές, γυμναστήριο.
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
    # Chapter 4's own grammar focus is adjective morphology, not a new verb tense --
    # default to "present" (the neutral/basic tense), but keep the full tense set
    # selectable so students can still drill/review any tense from the dropdown.
    _default_tense = "present"
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
    _ = tense_selector.value  # rebuild the form (clear stale input) when the tense changes
    _entered_verb_form = entered_verb().get(cv_verb["Word"]) if cv_verb else None
    verb_form, prev_btn_v, next_btn_v, restart_btn_v = gu2.paradigm_drill_widgets(
        labels=gu2.verb_slot_labels(),
        values=_entered_verb_form,
        history_len=len(hist_verb()),
        remaining_len=len(words4test_verb()),
        lang=language_selector.value,
    )
    set_prev_count_v(0)
    set_next_count_v(0)
    set_enter_count_v(0)
    return cv_verb, next_btn_v, prev_btn_v, restart_btn_v, verb_form


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
    # Language selector
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
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    RAW_BASE = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/modern_greek/ellinika_b/chapter_04"
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
