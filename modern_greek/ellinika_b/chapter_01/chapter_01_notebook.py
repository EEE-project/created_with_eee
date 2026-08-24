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
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_Jet2XzZu3epyb6M7N9K3JA)"
    if _lang == "ru":
        _sub = "Глава 1 — Социальные контакты · B1"
        _gl, _tl = "Грамматика", "Тесты"
        _tc = "Существительные · Глаголы · Прилагательные"
    elif _lang == "el":
        _sub = "Ενότητα 1 — Κοινωνικές Επαφές · B1"
        _gl, _tl = "Γραμματική", "Τεστ"
        _tc = "Ουσιαστικά · Ρήματα · Επίθετα"
    else:
        _sub = "Unit 1 — Social Contacts · B1"
        _gl, _tl = "Grammar", "Tests"
        _tc = "Nouns · Verbs · Adjectives"
    _gc = "Αντωνυμίες (αδύν. τύποι αιτ.) · Ουσιαστικά (ον./αιτ./κλητ.) · Απαλοιφή"
    _out = mo.md(f"""# «Αφήστε το μήνυμά σας» 📞
    ## {_sub} {_badge}

    **{_gl}:** {_gc}
    **{_tl}:** {_tc}
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar cell
    _lang = language_selector.value
    _XI = '<span style="color:#c00">έξ</span>'  # book colors this letter red in λέξη -- spelling callout, not the case-ending
    if _lang == 'ru':
        _md = mo.md(f"""
        ## Грамматика

        ### А. Личные местоимения, Винительный падеж — слабые и сильные формы

        Книга печатает это как две параллельные таблицы — слабых и сильных форм, — чьи примеры
        буквально повторяют друг друга: сильная форма повторяет предложение слабой формы и
        добавляет уточнение в скобках, какой референт имеется в виду.

        **Слабая форма (αδύνατος τύπος):**

        | Местоимение | Слабая форма | Пример | Перевод |
        |---|---|---|---|
        | εγώ | **Με** | Με ζήτησες; | Ты меня искал(а)? |
        | εσύ | **Σε** | Σε ζήτησα. | Я тебя искал(а). |
        | αυτός | **Τον** | Τον ζήτησαν στο τηλέφωνο. | Его звали к телефону. |
        | αυτή | **Τη(ν)** | Τη(ν) ζήτησαν στο τηλέφωνο. | Её звали к телефону. |
        | αυτό | **Το** | Το ζήτησε η Αρλέτα. | Арлета его попросила. |
        | εμείς | **Μας** | Μας ζήτησαν; | Нас искали? |
        | εσείς | **Σας** | Σας ζήτησαν. | Вас искали. |
        | αυτοί | **Τους** | Τους ζήτησε ο Αντώνης. | Андонис их искал (м.р.). |
        | αυτές | **Τις** | Τις ζήτησε ο Αντώνης. | Андонис их искал (ж.р.). |
        | αυτά | **Τα** | Τα ζήτησε ο Αντώνης. | Андонис их искал (ср.р.). |

        **Сильная форма (δυνατός τύπος)** — те же предложения, с уточнением в скобках:

        | Местоимение | Сильная форма | Пример | Перевод | Уточнение |
        |---|---|---|---|---|
        | εγώ | **Εμένα** | Εμένα ζήτησες; | МЕНЯ ты искал(а)? | (или Никоса?) |
        | εσύ | **Εσένα** | Εσένα ζήτησα. | ТЕБЯ я искал(а). | (не Никоса) |
        | αυτός | **Αυτόν** | Αυτόν ζήτησαν στο τηλέφωνο. | ЕГО звали к телефону. | (Никоса, не Эрвина) |
        | αυτή | **Αυτή(ν)** | Αυτή(ν) ζήτησαν στο τηλέφωνο. | ЕЁ звали к телефону. | (Марину, не Мелек) |
        | αυτό | **Αυτό** | Αυτό ζήτησε η Αρλέτα. | ИМЕННО ЭТО попросила Арлета. | (не другое) |
        | εμείς | **Εμάς** | Εμάς ζήτησαν; | НАС искали? | (или вас?) |
        | εσείς | **Εσάς** | Εσάς ζήτησαν. | ВАС искали. | (не нас) |
        | αυτοί | **Αυτούς** | Αυτούς ζήτησε ο Αντώνης. | ИМЕННО ИХ (м.р.) искал Андонис. | (не других) |
        | αυτές | **Αυτές** | Αυτές ζήτησε ο Αντώνης. | ИМЕННО ИХ (ж.р.) искал Андонис. | (не других) |
        | αυτά | **Αυτά** | Αυτά ζήτησε ο Αντώνης. | ИМЕННО ИХ (ср.р.) искал Андонис. | (не других) |

        Слабая форма — обычная, ставится **перед** глаголом. Сильная используется для акцента,
        как однословный ответ, или после предлога — слабая форма никогда не ставится после предлога.

        _Ещё примеры:_
        - Χαίρομαι που **σε** γνωρίζω. _(Рад с тобой познакомиться.)_
        - Ποιος **τη** ζητάει; _(Кто её спрашивает?)_
        - – Ποιον περιμένεις; – **Εσένα**. _(никогда просто «Σε» как однословный ответ)_
        - Αυτό το δώρο είναι **από εμένα για εσένα**. _(никогда «από με για σε» — слабая форма не
          может стоять после предлога)_
        - **Εμένα** με φοβούνται όλοι. _(сильная форма вынесена вперёд для акцента)_

        ---

        ### Б. Склонение существительных: Именительный и Винительный

        | Тип | Именительный | Винительный |
        |-----|---------------|-------------|
        | Муж. -ος | ο φίλ**ος** / οι φίλ**οι** | τον φίλ**ο** / τους φίλ**ους** |
        | Муж. -ας | ο άντρ**ας** / οι άντρ**ες** | τον άντρ**α** / τους άντρ**ες** |
        | Муж. -ης | ο μαθητ**ής** / οι μαθητ**ές** | τον μαθητ**ή** / τους μαθητ**ές** |
        | Жен. -α | η γυναίκ**α** / οι γυναίκ**ες** | τη γυναίκ**α** / τις γυναίκ**ες** |
        | Жен. -η | η φίλ**η** / οι φίλ**ες** | τη φίλ**η** / τις φίλ**ες** |
        | Жен. -η (-ξη) | η λ{_XI}**η** / οι λ{_XI}**εις** | τη λ{_XI}**η** / τις λ{_XI}**εις** |
        | Ср. -ο | το βιβλί**ο** / τα βιβλί**α** | (как Им.) |
        | Ср. -ι | το παιδ**ί** / τα παιδι**ά** | (как Им.) |
        | Ср. -μα | το μάθημ**α** / τα μαθήματ**α** | (как Им.) |

        _Примеры (со стр. 17 учебника):_
        - Η **Αρλέτα** δουλεύει σε ένα γυμναστήριο. _(Арлета работает в спортзале.)_
        - Ξέρεις **τον Παναγιώτη**; _(Ты знаешь Панайотиса?)_
        - Γνώρισα τη Μαρίνα **τον Ιανουάριο**. _(Я познакомился(-ась) с Мариной в январе.)_

        ---

        ### В. Существительные женского рода на -ος

        Существительные женского рода на **-ος** склоняются как мужские на -ος:
        η οδ**ός** / της οδ**ού** / την οδ**ό**. Та же модель: η είσοδος (вход), η έξοδος (выход),
        η λεωφόρος (проспект); названия профессий с любым артиклем: ο/η γιατρός, ο/η δικηγόρος,
        ο/η μηχανικός, ο/η οδηγός, ο/η πρόεδρος.

        _Примеры:_
        - Ο Στέφανος μένει **στην οδό** Ιπποκράτους, κοντά **στη λεωφόρο** Αλεξάνδρας. _(Стефанос живёт на улице Ипократус, рядом с проспектом Александрас.)_
        - Έχεις το τηλέφωνο αυτής **της δικηγόρου**; _(У тебя есть телефон этой адвокатессы?)_

        ---

        ### Г. Соответствие окончаний существительного/прилагательного и глагола

        Некоторые окончания существительных/прилагательных соответствуют определённому классу
        спряжения глагола:
        - ο/-ος, το/-ο → глаголы на **-ω**: ο φίλος, το τηλέφωνο → τηλεφωνώ
        - τον/-ης, η/την/-η → глаголы на **-εις/-ει**: ο φοιτητής, τον φοιτητή, η/τη φίλη →
          σπουδάζεις, σπουδάζει
        """)
    elif _lang == 'el':
        _md = mo.md(f"""
        ## Γραμματική

        ### Α. Προσωπικές αντωνυμίες, Αιτιατική — Αδύνατοι & Δυνατοί τύποι

        Το βιβλίο τυπώνει αυτό ως δύο παράλληλους πίνακες — αδύνατων και δυνατών τύπων —, των
        οποίων τα παραδείγματα κυριολεκτικά επαναλαμβάνουν το ένα το άλλο: η πρόταση του δυνατού
        τύπου επαναλαμβάνει την πρόταση του αδύνατου και προσθέτει διευκρίνιση σε παρένθεση.

        **Αδύνατος τύπος:**

        | Αντωνυμία | Αδύνατος τύπος | Παράδειγμα | Μετάφραση |
        |---|---|---|---|
        | εγώ | **Με** | Με ζήτησες; | Did you ask for me? |
        | εσύ | **Σε** | Σε ζήτησα. | I asked for you. |
        | αυτός | **Τον** | Τον ζήτησαν στο τηλέφωνο. | They asked for him on the phone. |
        | αυτή | **Τη(ν)** | Τη(ν) ζήτησαν στο τηλέφωνο. | They asked for her on the phone. |
        | αυτό | **Το** | Το ζήτησε η Αρλέτα. | Arleta asked for it. |
        | εμείς | **Μας** | Μας ζήτησαν; | Did they ask for us? |
        | εσείς | **Σας** | Σας ζήτησαν. | They asked for you (pl./formal). |
        | αυτοί | **Τους** | Τους ζήτησε ο Αντώνης. | Antonis asked for them (masc.). |
        | αυτές | **Τις** | Τις ζήτησε ο Αντώνης. | Antonis asked for them (fem.). |
        | αυτά | **Τα** | Τα ζήτησε ο Αντώνης. | Antonis asked for them (neut.). |

        **Δυνατός τύπος** — οι ίδιες προτάσεις, με διευκρίνιση σε παρένθεση:

        | Αντωνυμία | Δυνατός τύπος | Παράδειγμα | Μετάφραση | Διευκρίνιση |
        |---|---|---|---|---|
        | εγώ | **Εμένα** | Εμένα ζήτησες; | Was it ME you asked for? | (or Nikos?) |
        | εσύ | **Εσένα** | Εσένα ζήτησα. | It was YOU I asked for. | (not Nikos) |
        | αυτός | **Αυτόν** | Αυτόν ζήτησαν στο τηλέφωνο. | It was HIM they asked for on the phone. | (Nikos, not Ervin) |
        | αυτή | **Αυτή(ν)** | Αυτή(ν) ζήτησαν στο τηλέφωνο. | It was HER they asked for on the phone. | (Marina, not Melek) |
        | αυτό | **Αυτό** | Αυτό ζήτησε η Αρλέτα. | It was THAT one Arleta asked for. | (not the other one) |
        | εμείς | **Εμάς** | Εμάς ζήτησαν; | Was it US they asked for? | (or you?) |
        | εσείς | **Εσάς** | Εσάς ζήτησαν. | It was YOU they asked for. | (not us) |
        | αυτοί | **Αυτούς** | Αυτούς ζήτησε ο Αντώνης. | It was THEM (masc.) Antonis asked for. | (not the others) |
        | αυτές | **Αυτές** | Αυτές ζήτησε ο Αντώνης. | It was THEM (fem.) Antonis asked for. | (not the others) |
        | αυτά | **Αυτά** | Αυτά ζήτησε ο Αντώνης. | It was THOSE (neut.) Antonis asked for. | (not the others) |

        Ο αδύνατος τύπος είναι ο συνηθισμένος, μπαίνει **πριν** από το ρήμα. Ο δυνατός
        χρησιμοποιείται για έμφαση, ως μονολεκτική απάντηση, ή μετά από πρόθεση — ο αδύνατος
        δεν μπαίνει ποτέ μετά από πρόθεση.

        _Κι άλλα παραδείγματα:_
        - Χαίρομαι που **σε** γνωρίζω. _(I'm glad to meet you.)_
        - Ποιος **τη** ζητάει; _(Who's asking for her?)_
        - – Ποιον περιμένεις; – **Εσένα**. _(never a bare "Σε" as a one-word answer)_
        - Αυτό το δώρο είναι **από εμένα για εσένα**. _(never "από με για σε")_
        - **Εμένα** με φοβούνται όλοι. _(strong form fronted for emphasis)_

        ---

        ### Β. Κλίση ουσιαστικών: Ονομαστική & Αιτιατική

        | Τύπος | Ονομαστική | Αιτιατική |
        |-------|-----------|-----------|
        | Αρσ. -ος | ο φίλ**ος** / οι φίλ**οι** | τον φίλ**ο** / τους φίλ**ους** |
        | Αρσ. -ας | ο άντρ**ας** / οι άντρ**ες** | τον άντρ**α** / τους άντρ**ες** |
        | Αρσ. -ης | ο μαθητ**ής** / οι μαθητ**ές** | τον μαθητ**ή** / τους μαθητ**ές** |
        | Θηλ. -α | η γυναίκ**α** / οι γυναίκ**ες** | τη γυναίκ**α** / τις γυναίκ**ες** |
        | Θηλ. -η | η φίλ**η** / οι φίλ**ες** | τη φίλ**η** / τις φίλ**ες** |
        | Θηλ. -η (-ξη) | η λ{_XI}**η** / οι λ{_XI}**εις** | τη λ{_XI}**η** / τις λ{_XI}**εις** |
        | Ουδ. -ο | το βιβλί**ο** / τα βιβλί**α** | (ίδιο) |
        | Ουδ. -ι | το παιδ**ί** / τα παιδι**ά** | (ίδιο) |
        | Ουδ. -μα | το μάθημ**α** / τα μαθήματ**α** | (ίδιο) |

        _Παραδείγματα (σελ. 17):_
        - Η **Αρλέτα** δουλεύει σε ένα γυμναστήριο. _(Arleta works at a gym.)_
        - Ξέρεις **τον Παναγιώτη**; _(Do you know Panagiotis?)_
        - Γνώρισα τη Μαρίνα **τον Ιανουάριο**. _(I met Marina in January.)_

        ---

        ### Γ. Θηλυκά ουσιαστικά σε -ος

        Τα θηλυκά ουσιαστικά σε **-ος** κλίνονται όπως τα αρσενικά σε -ος: η οδ**ός** / της οδ**ού** /
        την οδ**ό**. Ίδιο μοτίβο: η είσοδος, η έξοδος, η λεωφόρος· ουσιαστικά επαγγελμάτων με είτε
        άρθρο: ο/η γιατρός, ο/η δικηγόρος, ο/η μηχανικός, ο/η οδηγός, ο/η πρόεδρος.

        _Παραδείγματα:_
        - Ο Στέφανος μένει **στην οδό** Ιπποκράτους, κοντά **στη λεωφόρο** Αλεξάνδρας. _(Stefanos lives on Ippokratous street, near Alexandras avenue.)_
        - Έχεις το τηλέφωνο αυτής **της δικηγόρου**; _(Do you have this [female] lawyer's phone number?)_

        ---

        ### Δ. Καταλήξεις ουσιαστικού/επιθέτου ↔ ρήματος

        Ορισμένες καταλήξεις ουσιαστικών/επιθέτων αντιστοιχούν σε συγκεκριμένη κλίση ρήματος:
        - ο/-ος, το/-ο → ρήματα σε **-ω**: ο φίλος, το τηλέφωνο → τηλεφωνώ
        - τον/-ης, η/την/-η → ρήματα σε **-εις/-ει**: ο φοιτητής, τον φοιτητή, η/τη φίλη →
          σπουδάζεις, σπουδάζει
        """)
    else:
        _md = mo.md(f"""
        ## Grammar

        ### A. Personal Pronouns, Accusative Case — Weak & Strong Forms

        The book prints this as two parallel tables — weak and strong forms — whose examples
        literally repeat each other: the strong-form sentence repeats the weak-form sentence and
        adds a parenthetical clarifying which referent is meant.

        **Weak (αδύνατος τύπος):**

        | Pronoun | Weak form | Example | Translation |
        |---|---|---|---|
        | εγώ | **Με** | Με ζήτησες; | Did you ask for me? |
        | εσύ | **Σε** | Σε ζήτησα. | I asked for you. |
        | αυτός | **Τον** | Τον ζήτησαν στο τηλέφωνο. | They asked for him on the phone. |
        | αυτή | **Τη(ν)** | Τη(ν) ζήτησαν στο τηλέφωνο. | They asked for her on the phone. |
        | αυτό | **Το** | Το ζήτησε η Αρλέτα. | Arleta asked for it. |
        | εμείς | **Μας** | Μας ζήτησαν; | Did they ask for us? |
        | εσείς | **Σας** | Σας ζήτησαν. | They asked for you (pl./formal). |
        | αυτοί | **Τους** | Τους ζήτησε ο Αντώνης. | Antonis asked for them (masc.). |
        | αυτές | **Τις** | Τις ζήτησε ο Αντώνης. | Antonis asked for them (fem.). |
        | αυτά | **Τα** | Τα ζήτησε ο Αντώνης. | Antonis asked for them (neut.). |

        **Strong (δυνατός τύπος)** — same sentences, with a parenthetical clarifying the contrast:

        | Pronoun | Strong form | Example | Translation | Clarifies |
        |---|---|---|---|---|
        | εγώ | **Εμένα** | Εμένα ζήτησες; | Was it ME you asked for? | (or Nikos?) |
        | εσύ | **Εσένα** | Εσένα ζήτησα. | It was YOU I asked for. | (not Nikos) |
        | αυτός | **Αυτόν** | Αυτόν ζήτησαν στο τηλέφωνο. | It was HIM they asked for on the phone. | (Nikos, not Ervin) |
        | αυτή | **Αυτή(ν)** | Αυτή(ν) ζήτησαν στο τηλέφωνο. | It was HER they asked for on the phone. | (Marina, not Melek) |
        | αυτό | **Αυτό** | Αυτό ζήτησε η Αρλέτα. | It was THAT one Arleta asked for. | (not the other one) |
        | εμείς | **Εμάς** | Εμάς ζήτησαν; | Was it US they asked for? | (or you?) |
        | εσείς | **Εσάς** | Εσάς ζήτησαν. | It was YOU they asked for. | (not us) |
        | αυτοί | **Αυτούς** | Αυτούς ζήτησε ο Αντώνης. | It was THEM (masc.) Antonis asked for. | (not the others) |
        | αυτές | **Αυτές** | Αυτές ζήτησε ο Αντώνης. | It was THEM (fem.) Antonis asked for. | (not the others) |
        | αυτά | **Αυτά** | Αυτά ζήτησε ο Αντώνης. | It was THOSE (neut.) Antonis asked for. | (not the others) |

        The weak form is the default, placed **directly before** the verb. The strong form is
        used for emphasis, as a standalone answer, or after a preposition — a weak form can
        never follow a preposition.

        _More examples:_
        - Χαίρομαι που **σε** γνωρίζω. _(I'm glad to meet you.)_
        - Ποιος **τη** ζητάει; _(Who's asking for her?)_
        - – Ποιον περιμένεις; – **Εσένα**. _(never a bare "Σε" as a one-word answer)_
        - Αυτό το δώρο είναι **από εμένα για εσένα**. _(never "από με για σε" — weak forms can't
          follow a preposition)_
        - **Εμένα** με φοβούνται όλοι. _(strong form fronted for emphasis — weak form still
          required before the verb)_

        ---

        ### B. Noun Declension: Nominative & Accusative

        | Pattern | Nominative | Accusative |
        |---------|-----------|------------|
        | Masc. -ος | ο φίλ**ος** / οι φίλ**οι** | τον φίλ**ο** / τους φίλ**ους** |
        | Masc. -ας | ο άντρ**ας** / οι άντρ**ες** | τον άντρ**α** / τους άντρ**ες** |
        | Masc. -ης | ο μαθητ**ής** / οι μαθητ**ές** | τον μαθητ**ή** / τους μαθητ**ές** |
        | Fem. -α | η γυναίκ**α** / οι γυναίκ**ες** | τη γυναίκ**α** / τις γυναίκ**ες** |
        | Fem. -η | η φίλ**η** / οι φίλ**ες** | τη φίλ**η** / τις φίλ**ες** |
        | Fem. -η (-ξη) | η λ{_XI}**η** / οι λ{_XI}**εις** | τη λ{_XI}**η** / τις λ{_XI}**εις** |
        | Neut. -ο | το βιβλί**ο** / τα βιβλί**α** | (same) |
        | Neut. -ι | το παιδ**ί** / τα παιδι**ά** | (same) |
        | Neut. -μα | το μάθημ**α** / τα μαθήματ**α** | (same) |

        _Examples (p. 17):_
        - Η **Αρλέτα** δουλεύει σε ένα γυμναστήριο. _(Arleta works at a gym.)_
        - Ξέρεις **τον Παναγιώτη**; _(Do you know Panagiotis?)_
        - Γνώρισα τη Μαρίνα **τον Ιανουάριο**. _(I met Marina in January.)_

        ---

        ### C. Feminine nouns in -ος

        Feminine nouns ending in **-ος** decline like masculine -ος nouns: η οδ**ός** / της οδ**ού** /
        την οδ**ό**. Same pattern: η είσοδος (entrance), η έξοδος (exit), η λεωφόρος (avenue);
        profession nouns that take either article: ο/η γιατρός, ο/η δικηγόρος, ο/η μηχανικός,
        ο/η οδηγός, ο/η πρόεδρος.

        _Examples:_
        - Ο Στέφανος μένει **στην οδό** Ιπποκράτους, κοντά **στη λεωφόρο** Αλεξάνδρας. _(Stefanos lives on Ippokratous street, near Alexandras avenue.)_
        - Έχεις το τηλέφωνο αυτής **της δικηγόρου**; _(Do you have this [female] lawyer's phone number?)_

        ---

        ### D. Noun/Adjective ↔ Verb ending patterns

        Certain noun/adjective endings correlate with a verb's conjugation class:
        - ο/-ος, το/-ο → **-ω** verbs: ο φίλος, το τηλέφωνο → τηλεφωνώ
        - τον/-ης, η/την/-η → **-εις/-ει** verbs: ο φοιτητής, τον φοιτητή, η/τη φίλη →
          σπουδάζεις, σπουδάζει
        """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Useful phrases cell
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
        ## Полезные фразы — Телефонное общение

        Дословно из учебника, по разделам («Πώς το λένε;» / «Για δες»).

        ### стр. 9

        | Греческий | Русский |
        |-----------|---------|
        | Παρακαλώ. | Алло? (отвечая на звонок) |
        | Λέγετε; | Слушаю? |
        | Έλα, Αρλέτα. | Привет, Арлета. |
        | Μπορώ να μιλήσω με την κυρία...; | Могу я поговорить с госпожой...? |
        | Ποιος τη ζητάει; | Кто её спрашивает? |
        | Μισό λεπτό να τη φωνάξω. | Минуту, я её позову. |
        | Συγνώμη που σε ενοχλώ... | Извини, что беспокою... |
        | Δεν υπάρχει πρόβλημα. | Нет проблем. |
        | Το γιορτάζουμε. | Мы это празднуем. |
        | Ευχαριστώ για την πρόσκληση. | Спасибо за приглашение. |
        | Πες μου. | Расскажи. |
        | Κοίτα. | Слушай... |

        ### стр. 10

        | Греческий | Русский |
        |-----------|---------|
        | Εμπρός; | Алло? |
        | Τη Σοφία θα ήθελα, παρακαλώ. | Софию, пожалуйста. |
        | Λάθος πήρατε. | Вы ошиблись номером. |
        | Έλα. Πού βρίσκεσαι; | Привет. Ты где? |
        | Τι κανονίζεις; | Что планируешь? |
        | Μια χαρά! | Отлично! |
        | Τα λέμε πάλι. | До связи. |

        ### стр. 11

        | Греческий | Русский |
        |-----------|---------|
        | Καλέσατε το 210 7282537. Αφήστε το μήνυμά σας. | Вы позвонили на номер 210 7282537. Оставьте своё сообщение. |
        | Θα επικοινωνήσω μαζί σας το συντομότερο δυνατόν. | Я свяжусь с вами как можно скорее. |
        | Θα σε ξαναπάρω το βράδυ. | Я перезвоню тебе вечером. |
        | Τα έμαθες; Θα γίνει χαμός! | Ты слышал новость? Будет жара! |
        | Α, και πού 'σαι... | Ах, и где ты... |

        ### стр. 12 — Στο τηλέφωνο

        | Греческий | Русский |
        |-----------|---------|
        | Παρακαλώ; | Алло? |
        | Εμπρός; | Алло? |
        | Λέγετε; | Слушаю? |
        | Ορίστε; | Да? Слушаю вас? |
        | Αφήστε μήνυμα και θα επικοινωνήσω μαζί σας. | Оставьте сообщение, и я с вами свяжусь. |
        | Θα ήθελα να μιλήσω στον κύριο Οικονόμου, παρακαλώ. | Я хотел бы поговорить с господином Икономму, пожалуйста. |
        | Μπορώ να μιλήσω στον κύριο Οικονόμου; | Могу я поговорить с господином Икономму? |
        | Μου δίνετε τον Φοίβο, σας παρακαλώ; | Не могли бы вы позвать Фивоса? |
        | Μήπως είναι εκεί ο Φοίβος; | Фивос случайно не там? |
        | Περιμένετε ένα λεπτό, παρακαλώ. | Подождите минуту, пожалуйста. |
        | Μισό λεπτό να σας συνδέσω. | Минуту, я вас соединю. |
        | Μια στιγμή, παρακαλώ. | Секундочку, пожалуйста. |
        | Ποιος τον/τη ζητά; | Кто его/её спрашивает? |
        | Μισό λεπτό να δω αν είναι εδώ. | Минуту, посмотрю, здесь ли он. |
        | Ένα λεπτό να τον/τη φωνάξω. | Минуту, я его/её позову. |
        | Δεν είναι εδώ αυτή τη στιγμή. | Его сейчас здесь нет. |
        | Θέλετε ν' αφήσετε ένα μήνυμα; | Хотите оставить сообщение? |
        | Θέλετε να του πω κάτι; | Хотите, чтобы я ему что-то передал? |
        | Λάθος πήρατε. Δεν υπάρχει κύριος Οικονόμου εδώ. | Вы ошиблись номером. Здесь нет господина Икономму. |
        | Μάλλον κάνατε λάθος. | Вы, наверное, ошиблись. |
        | Ο κύριος Οικονόμου; / Η κυρία Αντωνοπούλου; → Ο ίδιος. / Η ίδια. | Господин Икономму? / Госпожа Антонопулу? → Это я. |
        | Ναι; / Έλα. Πού βρίσκεσαι; → Έλα, Φοίβο. Η Σοφία είμαι. | Да? / Привет, ты где? → Привет, Фивос. Это София. |
        | Ναι; Με ακούτε; / Ναι; Μ' ακούς; | Вы/ты меня слышите/слышишь? (форм. / неформ.) |
        | Δε σας ακούω καλά. / Έλα, Κώστα. Εσύ είσαι; | Я вас плохо слышу. / Привет, Костас. Это ты? |

        ### стр. 15

        | Греческий | Русский |
        |-----------|---------|
        | Αυτός είναι ο Παναγιώτης. Από 'δώ η Σοφία. | Это Панайотис. А это София. |
        | Καλώς τα παιδιά. Περάστε. | Добро пожаловать, ребята. Проходите. |
        | Συγχαρητήρια. Καλή σταδιοδρομία. | Поздравляю. Успешной карьеры. |
        | – Αυτό είναι για σένα. – Ευχαριστώ. Δεν ήταν ανάγκη. | – Это тебе. – Спасибо, не стоило. |
        | – Να σου συστήσω τη Μελέκ. – Χαίρομαι που σε γνωρίζω. | – Познакомься, это Мелек. – Рада знакомству. |
        | – Θυμάσαι τον Φου και τη Λι; | – Помнишь Фу и Ли? |
        | Ό,τι επιθυμείς. | Как пожелаешь. |
        """)
    elif _lang == 'el':
        _md = mo.md("""
        ## Χρήσιμες Φράσεις — Τηλεφωνική Επικοινωνία

        Ακριβώς όπως στο βιβλίο, ανά ενότητα («Πώς το λένε;» / «Για δες»).

        ### σελ. 9

        | Ελληνικά | Αγγλικά |
        |----------|---------|
        | Παρακαλώ. | Hello? (answering) |
        | Λέγετε; | Yes? / Go ahead? |
        | Έλα, Αρλέτα. | Hi, Arleta. |
        | Μπορώ να μιλήσω με την κυρία...; | Can I speak with Mrs. ...? |
        | Ποιος τη ζητάει; | Who's asking for her? |
        | Μισό λεπτό να τη φωνάξω. | One moment, I'll get her. |
        | Συγνώμη που σε ενοχλώ... | Sorry to bother you... |
        | Δεν υπάρχει πρόβλημα. | No problem. |
        | Το γιορτάζουμε. | We're celebrating it. |
        | Ευχαριστώ για την πρόσκληση. | Thanks for the invitation. |
        | Πες μου. | Tell me. |
        | Κοίτα. | Look... |

        ### σελ. 10

        | Ελληνικά | Αγγλικά |
        |----------|---------|
        | Εμπρός; | Hello? (answering) |
        | Τη Σοφία θα ήθελα, παρακαλώ. | I'd like [to speak to] Sofia, please. |
        | Λάθος πήρατε. | You have the wrong number. |
        | Έλα. Πού βρίσκεσαι; | Hey. Where are you? |
        | Τι κανονίζεις; | What are you arranging? |
        | Μια χαρά! | Great! / Just fine! |
        | Τα λέμε πάλι. | Talk to you again. |

        ### σελ. 11

        | Ελληνικά | Αγγλικά |
        |----------|---------|
        | Καλέσατε το 210 7282537. Αφήστε το μήνυμά σας. | You've reached 210 7282537. Leave your message. |
        | Θα επικοινωνήσω μαζί σας το συντομότερο δυνατόν. | I will contact you as soon as possible. |
        | Θα σε ξαναπάρω το βράδυ. | I'll call you back tonight. |
        | Τα έμαθες; Θα γίνει χαμός! | Did you hear the news? It's going to be wild! |
        | Α, και πού 'σαι... | Oh, and where are you... |

        ### σελ. 12 — Στο τηλέφωνο

        | Ελληνικά | Αγγλικά |
        |----------|---------|
        | Παρακαλώ; | Hello? |
        | Εμπρός; | Hello? |
        | Λέγετε; | Yes? / Go ahead? |
        | Ορίστε; | Yes? / How can I help? |
        | Αφήστε μήνυμα και θα επικοινωνήσω μαζί σας. | Leave a message and I'll get back to you. |
        | Θα ήθελα να μιλήσω στον κύριο Οικονόμου, παρακαλώ. | I would like to speak to Mr. Oikonomou, please. |
        | Μπορώ να μιλήσω στον κύριο Οικονόμου; | Can I speak to Mr. Oikonomou? |
        | Μου δίνετε τον Φοίβο, σας παρακαλώ; | Could you put me through to Phoivos, please? |
        | Μήπως είναι εκεί ο Φοίβος; | Is Phoivos there by any chance? |
        | Περιμένετε ένα λεπτό, παρακαλώ. | Wait a moment, please. |
        | Μισό λεπτό να σας συνδέσω. | One moment, let me connect you. |
        | Μια στιγμή, παρακαλώ. | One moment, please. |
        | Ποιος τον/τη ζητά; | Who's asking for him/her? |
        | Μισό λεπτό να δω αν είναι εδώ. | One moment, let me see if he/she is here. |
        | Ένα λεπτό να τον/τη φωνάξω. | One moment, I'll get him/her. |
        | Δεν είναι εδώ αυτή τη στιγμή. | He/she isn't here right now. |
        | Θέλετε ν' αφήσετε ένα μήνυμα; | Would you like to leave a message? |
        | Θέλετε να του πω κάτι; | Would you like me to tell him something? |
        | Λάθος πήρατε. Δεν υπάρχει κύριος Οικονόμου εδώ. | Wrong number. There's no Mr. Oikonomou here. |
        | Μάλλον κάνατε λάθος. | You must have the wrong number. |
        | Ο κύριος Οικονόμου; / Η κυρία Αντωνοπούλου; → Ο ίδιος. / Η ίδια. | Mr. Oikonomou? / Mrs. Antonopoulou? → Speaking. |
        | Ναι; / Έλα. Πού βρίσκεσαι; → Έλα, Φοίβο. Η Σοφία είμαι. | Yes? / Hey, where are you? → Hi, Phoivos. It's Sofia. |
        | Ναι; Με ακούτε; / Ναι; Μ' ακούς; | Yes? Can you hear me? (formal / informal) |
        | Δε σας ακούω καλά. / Έλα, Κώστα. Εσύ είσαι; | I can't hear you well. / Hey, Kosta. Is that you? |

        ### σελ. 15

        | Ελληνικά | Αγγλικά |
        |----------|---------|
        | Αυτός είναι ο Παναγιώτης. Από 'δώ η Σοφία. | This is Panagiotis. This is Sofia. |
        | Καλώς τα παιδιά. Περάστε. | Welcome, everyone. Come in. |
        | Συγχαρητήρια. Καλή σταδιοδρομία. | Congratulations. Good luck with your career. |
        | – Αυτό είναι για σένα. – Ευχαριστώ. Δεν ήταν ανάγκη. | – This is for you. – Thanks. You shouldn't have. |
        | – Να σου συστήσω τη Μελέκ. – Χαίρομαι που σε γνωρίζω. | – Let me introduce Melek. – Glad to meet you. |
        | – Θυμάσαι τον Φου και τη Λι; | – Do you remember Fou and Li? |
        | Ό,τι επιθυμείς. | Whatever you wish. |
        """)
    else:
        _md = mo.md("""
        ## Useful Phrases — Telephone Communication

        Transcribed exactly as printed, box by box («Πώς το λένε;» / «Για δες»).

        ### p. 9

        | Greek | English |
        |-------|---------|
        | Παρακαλώ. | Hello? (answering) |
        | Λέγετε; | Yes? / Go ahead? |
        | Έλα, Αρλέτα. | Hi, Arleta. |
        | Μπορώ να μιλήσω με την κυρία...; | Can I speak with Mrs. ...? |
        | Ποιος τη ζητάει; | Who's asking for her? |
        | Μισό λεπτό να τη φωνάξω. | One moment, I'll get her. |
        | Συγνώμη που σε ενοχλώ... | Sorry to bother you... |
        | Δεν υπάρχει πρόβλημα. | No problem. |
        | Το γιορτάζουμε. | We're celebrating it. |
        | Ευχαριστώ για την πρόσκληση. | Thanks for the invitation. |
        | Πες μου. | Tell me. |
        | Κοίτα. | Look... |

        ### p. 10

        | Greek | English |
        |-------|---------|
        | Εμπρός; | Hello? (answering) |
        | Τη Σοφία θα ήθελα, παρακαλώ. | I'd like [to speak to] Sofia, please. |
        | Λάθος πήρατε. | You have the wrong number. |
        | Έλα. Πού βρίσκεσαι; | Hey. Where are you? |
        | Τι κανονίζεις; | What are you arranging? |
        | Μια χαρά! | Great! / Just fine! |
        | Τα λέμε πάλι. | Talk to you again. |

        ### p. 11

        | Greek | English |
        |-------|---------|
        | Καλέσατε το 210 7282537. Αφήστε το μήνυμά σας. | You've reached 210 7282537. Leave your message. |
        | Θα επικοινωνήσω μαζί σας το συντομότερο δυνατόν. | I will contact you as soon as possible. |
        | Θα σε ξαναπάρω το βράδυ. | I'll call you back tonight. |
        | Τα έμαθες; Θα γίνει χαμός! | Did you hear the news? It's going to be wild! |
        | Α, και πού 'σαι... | Oh, and where are you... |

        ### p. 12 — Στο τηλέφωνο

        | Greek | English |
        |-------|---------|
        | Παρακαλώ; | Hello? |
        | Εμπρός; | Hello? |
        | Λέγετε; | Yes? / Go ahead? |
        | Ορίστε; | Yes? / How can I help? |
        | Αφήστε μήνυμα και θα επικοινωνήσω μαζί σας. | Leave a message and I'll get back to you. |
        | Θα ήθελα να μιλήσω στον κύριο Οικονόμου, παρακαλώ. | I would like to speak to Mr. Oikonomou, please. |
        | Μπορώ να μιλήσω στον κύριο Οικονόμου; | Can I speak to Mr. Oikonomou? |
        | Μου δίνετε τον Φοίβο, σας παρακαλώ; | Could you put me through to Phoivos, please? |
        | Μήπως είναι εκεί ο Φοίβος; | Is Phoivos there by any chance? |
        | Περιμένετε ένα λεπτό, παρακαλώ. | Wait a moment, please. |
        | Μισό λεπτό να σας συνδέσω. | One moment, let me connect you. |
        | Μια στιγμή, παρακαλώ. | One moment, please. |
        | Ποιος τον/τη ζητά; | Who's asking for him/her? |
        | Μισό λεπτό να δω αν είναι εδώ. | One moment, let me see if he/she is here. |
        | Ένα λεπτό να τον/τη φωνάξω. | One moment, I'll get him/her. |
        | Δεν είναι εδώ αυτή τη στιγμή. | He/she isn't here right now. |
        | Θέλετε ν' αφήσετε ένα μήνυμα; | Would you like to leave a message? |
        | Θέλετε να του πω κάτι; | Would you like me to tell him something? |
        | Λάθος πήρατε. Δεν υπάρχει κύριος Οικονόμου εδώ. | Wrong number. There's no Mr. Oikonomou here. |
        | Μάλλον κάνατε λάθος. | You must have the wrong number. |
        | Ο κύριος Οικονόμου; / Η κυρία Αντωνοπούλου; → Ο ίδιος. / Η ίδια. | Mr. Oikonomou? / Mrs. Antonopoulou? → Speaking. |
        | Ναι; / Έλα. Πού βρίσκεσαι; → Έλα, Φοίβο. Η Σοφία είμαι. | Yes? / Hey, where are you? → Hi, Phoivos. It's Sofia. |
        | Ναι; Με ακούτε; / Ναι; Μ' ακούς; | Yes? Can you hear me? (formal / informal) |
        | Δε σας ακούω καλά. / Έλα, Κώστα. Εσύ είσαι; | I can't hear you well. / Hey, Kosta. Is that you? |

        ### p. 15

        | Greek | English |
        |-------|---------|
        | Αυτός είναι ο Παναγιώτης. Από 'δώ η Σοφία. | This is Panagiotis. This is Sofia. |
        | Καλώς τα παιδιά. Περάστε. | Welcome, everyone. Come in. |
        | Συγχαρητήρια. Καλή σταδιοδρομία. | Congratulations. Good luck with your career. |
        | – Αυτό είναι για σένα. – Ευχαριστώ. Δεν ήταν ανάγκη. | – This is for you. – Thanks. You shouldn't have. |
        | – Να σου συστήσω τη Μελέκ. – Χαίρομαι που σε γνωρίζω. | – Let me introduce Melek. – Glad to meet you. |
        | – Θυμάσαι τον Φου και τη Λι; | – Do you remember Fou and Li? |
        | Ό,τι επιθυμείς. | Whatever you wish. |
        """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Pronunciation cell
    _lang = language_selector.value
    if _lang == 'ru':
        _md = mo.md("""
        ## Φωνή-γραφή (Правила произношения и написания)

        Дополнительный раздел учебника, не входящий в три стандартных типа — здесь фонетика.

        ### А. Элизия: артикль/частица + гласная → апостроф

        | Правило | Пример |
        |---------|--------|
        | το + ο, α → τ' | το όνομα = τ' όνομα · το αγόρι = τ' αγόρι |
        | τα + α → τ' | τα αγόρια = τ' αγόρια |
        | του + ου → τ' | του ουρανού = τ' ουρανού |
        | με, σε + гласная → μ', σ' | Με ακούς; = Μ' ακούς; · Σε ακούω. = Σ' ακούω. |

        Также встречается в диалоге этой главы: Α, και πού 'σαι... _(= πού είσαι)_

        ---

        ### Б. Ассимиляция носового + смычного согласного

        Когда слово, оканчивающееся на **-ν**, сразу сопровождается словом, начинающимся с π, τ или κ,
        сочетание произносится звонко:

        | Правило | Примеры |
        |---------|---------|
        | -ν + π → [mb] | τον Πέτρο → [to(m)bétro] · δεν παίζω → [de(m)bézo] |
        | -ν + τ → [nd] | τον Τάσο → [to(n)dáso] · δεν το ξέρω → [dé(n)dokséro] |
        | -ν + κ → [ng] | την Κατερίνα → [ti(n)gaterína] · δεν καταλαβαίνω → [dé(n)gatalavéno] |
        """)
    elif _lang == 'el':
        _md = mo.md("""
        ## Φωνή-γραφή

        Πρόσθετη ενότητα του βιβλίου, πέρα από τις τρεις βασικές — εδώ φωνητική.

        ### Α. Έκθλιψη: άρθρο/μόριο + φωνήεν → απόστροφος

        | Κανόνας | Παράδειγμα |
        |---------|-----------|
        | το + ο, α → τ' | το όνομα = τ' όνομα · το αγόρι = τ' αγόρι |
        | τα + α → τ' | τα αγόρια = τ' αγόρια |
        | του + ου → τ' | του ουρανού = τ' ουρανού |
        | με, σε + φωνήεν → μ', σ' | Με ακούς; = Μ' ακούς; · Σε ακούω. = Σ' ακούω. |

        Επίσης στον διάλογο του κεφαλαίου: Α, και πού 'σαι... _(= πού είσαι)_

        ---

        ### Β. Αφομοίωση ένρινου + κλειστού συμφώνου

        Όταν μια λέξη που τελειώνει σε **-ν** ακολουθείται από λέξη που αρχίζει με π, τ ή κ,
        το σύμπλεγμα προφέρεται ηχηρά:

        | Κανόνας | Παραδείγματα |
        |---------|--------------|
        | -ν + π → [mb] | τον Πέτρο → [to(m)bétro] · δεν παίζω → [de(m)bézo] |
        | -ν + τ → [nd] | τον Τάσο → [to(n)dáso] · δεν το ξέρω → [dé(n)dokséro] |
        | -ν + κ → [ng] | την Κατερίνα → [ti(n)gaterína] · δεν καταλαβαίνω → [dé(n)gatalavéno] |
        """)
    else:
        _md = mo.md("""
        ## Pronunciation / Spelling Rules (Φωνή-γραφή)

        A chapter-specific supplementary segment, beyond the three standard segment types —
        pronunciation rules.

        ### A. Vowel elision: article/particle + vowel → apostrophe

        | Rule | Example |
        |------|---------|
        | το + ο, α → τ' | το όνομα = τ' όνομα · το αγόρι = τ' αγόρι |
        | τα + α → τ' | τα αγόρια = τ' αγόρια |
        | του + ου → τ' | του ουρανού = τ' ουρανού |
        | με, σε + vowel → μ', σ' | Με ακούς; = Μ' ακούς; · Σε ακούω. = Σ' ακούω. |

        Also seen in this chapter's own dialogue: Α, και πού 'σαι... _(= πού είσαι)_

        ---

        ### B. Nasal + stop consonant assimilation

        When a word ending in **-ν** is directly followed by a word starting with π, τ, or κ,
        the cluster is pronounced as a voiced stop:

        | Rule | Examples |
        |------|----------|
        | -ν + π → [mb] | τον Πέτρο → [to(m)bétro] · δεν παίζω → [de(m)bézo] |
        | -ν + τ → [nd] | τον Τάσο → [to(n)dáso] · δεν το ξέρω → [dé(n)dokséro] |
        | -ν + κ → [ng] | την Κατερίνα → [ti(n)gaterína] · δεν καταλαβαίνω → [dé(n)gatalavéno] |
        """)
    _md
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 1 heading
    mo.md(t_ui("test1_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, notebook_dir):
    # Load noun data
    df_noun = gu2.load_vocab_table("nouns.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
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
def _(RAW_BASE, gu2, notebook_dir):
    # Load verb data
    df_verb = gu2.load_vocab_table("verbs.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
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
def _(language_selector, mo, t_ui):
    # Test 3 heading
    mo.md(t_ui("test3_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(RAW_BASE, gu2, notebook_dir):
    # Load adjective data
    df_adj = gu2.load_vocab_table("adjectives.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
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
    _prev_url, _next_url = _cfg.adjacent_urls("chapter_01/")
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
    RAW_BASE = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/modern_greek/ellinika_b/chapter_01"
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
