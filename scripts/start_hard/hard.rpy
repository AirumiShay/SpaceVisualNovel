label start_hard:
    scene black
    nvl clear
    window hide
    n '''Вот уже две недели я иду на север, моя цель - покинуть земли Темной Империи и выйти в Ничейные земли. После этого добраться до столицы Империи людей и найти своих родителей.
Пробираясь по густому лесу, я встретил отряд существ, закутанных в темные одежды. Они вели за собой пленников. И я решил проследить за ними и постараться помочь. Я понадеялся на Амулет Духа, подаренный старым шаманом в день моего совершеннолетия. Он позволял переходить в состояние невидимости.'''
    nvl clear
    n ''' Никто меня не замечал, пока мы не зашли в эту пещеру.Здесь было много темных эльфов, двуногие ящерицы и даже  несколько троллей. В дальнем углу вокруг высокого эльфа с посохом суетились гоблины. В ярком свете факелов можно было хорошо  рассмотреть каждое существо.
 Я в невидимости стоял у входа в пещеру и пытался придумать план спасения. Нужно было уже тогда понять, что я ничего не смогу сделать и бежать оттуда, пока меня не заметили. '''
    nvl clear
    n ''' Пленников  разложили по лучам пентаграммы, даже не развязав их. Это были светлые эльфы и люди. Некоторые выделялись своим видом. На шеях у них я разглядел ошейники с начерченными рунами. Похожие друг на друга, с очень бледными лицами.Длинные черные волосы.  Молодая девушка, двое парней и девчонка-подросток. Словно что-то почувстовав, один из парней повернул голову и посмотрел прямо на меня своими ярко-красными глазами.'''
    nvl clear
    n ''' Он меня видел!!! Но как? Мне вспомнились уроки шамана. Он рассказывал про вампиров и других  магических существ, которые могли видеть сквозь астрал и активно взаимодействовать с ним. Только я успокоился, как в моей голове раздался  голос. Он то затихал, что становился громче:
 - Помоги... Отвлеки колдуна, и тогда я смогу убить его. Если я не выживу... Моя сестра Рюни...  
Парень глазами показал на девчонку. 
 - Защити её... Отведи в наш клан... Клан  МаКии... Наши земли на востоке в неделе пути отсюда... '''
    nvl clear
    n ''' Он не закончил фразу. Колдун начал читать заклинание призыва. Камень в навершии посоха ярко засиял и в центре пентаграммы возник красный сгусток света. Несколько мгновений я колебался. Рюни повернулась и я увидел её полный ужаса взгляд. Её губы приоткрылись, она пыталась что-то сказать. Надо решаться, пока ритуал не завершен. Вокруг зашумело,и в голове раздался тонкий девичий голос: - Я боюсь. Помоги...
Голос становился всё тише, растворяясь в шуме потоков энергии: -  Не хочу умирать...'''
    nvl hide
    scene black
    menu:
        "Атаковать колдуна":
            jump warlock_atack
        "Ударить в красный сгусток":
            jump core_atack
        "Подождать":
            jump wait_more
        "Убежать":
            jump go_out1
label warlock_atack:
    jump go_action1
    return
label core_atack:
    jump go_action1
    return
label wait_more:
    jump go_action1
    return
label go_out1:
    "Я быстро направился вглубь туннеля, подальше о пещеры. {w} В голове голос парня просил меня вернуться и прервать ритуал. Решительно развернулся и на полной скорости побежал обратно."
label go_action1:
    "Я старался удерживать мысленный контакт с Рюни."
    nvl clear
    window hide
    play music "music/hard/wolf.mp3"
    n '''В центре пещеры висел огромный багровый шар. Бушующие вокруг него потоки энергии завивались в некий узор, оплетая тела жертв. Фигура колдуна тряслась от проходящей сквозь него энергии. От сияющего навершия посоха к шару змеилась красная молния.
    С трудом сосредоточившись я перешёл в Астрал, и , как учил меня  шаман, первым делом активировал Астральный якорь, создающий островок стабильного астрала вокруг меня и способный защитить от воздействия разрушительной энергии.'''
    nvl clear
    n ''' Формирую заклинание Астрального разрыва. Вкладываю в него почти всю доступную мне энергию. От меня распрастроняется яркая зеленая волна, разрывая связь колдуна с ядром ритуала. Тело колдуна отбрасывает к стене и тут же возле Рюни вспухает голубое облако. Шар меняет цвет на кроваво-красный, увеличиваясь в размерах. И словно расплескивается по пещере, заставляя темные фигуры вокруг кричать и корчиться от боли. Красное свечение заполняет всё вокруг. '''
    nvl clear
    n ''' Я ощущаю, как связь с Рюни становиться всё слабее. Пробую удерживать её, но растворяюсь в ослепительной вспышке, когда энергия взрыва захлестывает меня.'''
    n ''' Сознание возвращалось ко мне постепенно. Зрение  прояснилось, но окружающее виделось мне в бледных тонах. Что же произошло? Я в пещере. Вокруг разбросаны тела. Повсюду следы крови, на полу светится рисунок пентаграммы. Взглянул на него и сразу всё вспомнил.
Ритуал, Рюни, взрыв... Якорь выдержал удар.  Моё астральное тело '''
    nvl clear
    n '''  в порядке. Старый шаман мог бы гордиться своим учеником. Сколько же времени прошло? Несколько суток не меньше. Хотя вокруг якоря ещё виднеются отголоски энергии ритуала, но они достаточно слабые. Остался ли кто в живых, кроме меня. Сосредотачиваюсь, мир воркруг расцветает яркими красками. Пробую почувствовать связь с Рюни, но не получаю словесного отклика. Только ощущение её присутствия где-то совсем рядом. Рюни жива! Внимательно осматриваюсь. Почти всё мертвы, но в некоторых телах я замечаю остатки'''
    nvl clear
    n '''энергии.  Когда я оборвал контроль колдуна над ядром ритуала, его энергия расплескалась вокруг и вызвала астральный шторм. Он был такой мощный, что разрушил энергетическую структуру тел почти всех, кто был в пещере.  Но вампиры очень живучи, и даже взрыв такой мощи не смог их убить.Один из троллей тоже жив. Их ещё можно будет попробовать вернуть к жизни. Приближаюсь к телу колдуна.'''
    nvl clear
    n ''' Он окончательно мертв, а вокруг на несколько метров светится оранжевая пленка магического щита.
 Мощный артефакт не помог хозяину пережить откат заклинания. А нескольким темным эльфам и гоблинам рядом с ним повезло больше и жизнь всё ещё теплится в них. Пробую выйти из Астрала и с ужасом понимаю, что не могу этого сделать! Что-то мешает и втягивает меня обратно.'''
    nvl clear
    n '''  В панике я  начинаю метаться и когда приближаюсь к телу Рюни, ощущение её присутсвия возрастает. Её тело покрыто голубой дымкой, внешних повреждений не видно. Похоже, что голубое облако, которое я заметил перед взрывом было магическим щитом. Пробую мысленно потянутся ней и на этот раз слышу её голос.''' 
    nvl clear
    n ''' - Мне холодно, так холодно...мне нужна энергия...помоги... так холодно...'''
    n ''' - Ты жива, это главное. Я могу попробовать направить тебе часть моей энергию. '''
    nvl hide
    menu:
        "Поделиться своей энергией с Рюни":
            $ spell_astral_link = 0
            jump Ryuni_energy
        "Спросить, как выйти из Астрала":
            $ spell_astral_link = 1 
            " - Пожалуйста, помоги мне, если я пробуду здесь ещё немного, то сойду с ума,  - просит она слабым голосом"
            "- Подожди ещё минутку. Ты знаешь, почему я не могу выйти из Астрала?. Раньше у меня это легко получалось. Что мне теперь делать?"
    nvl clear
    n '''Я точно не знаю. Возможно, это из-за твоего вмешательства в ритуал. Освобождённая энергия взрыва ядра наполнила твоё астральное тело. И теперь ты не можешь вернуться в физическое, потому что оно не может вместить в себя всю эту мощь. Припоминаю, брат рассказывал о подобном. Используй заклинание Астральной Привязки.'''
    n '''- Я не знаю такого. Мой учитель никогда не упоминал о нём. А что оно делает?. 
    - Привязывает твою душу к физическому телу, если оно ещё не умерло окончательно.''' 
    nvl clear
    n ''' Тут есть подходящие тела, ты может вселиться в них. Я могу научить тебя, но перед этим мне надо отключить этот щит. А для этого у меня не хватает энергии.
    - Я дам тебе часть своей энергии, у меня есть такое заклинание'''
 
    "Я использую заклинание перекачки энергии и немного подпитываю её астральное тело.Голубая оболочка вокруг её тела исчезает."
label  Ryuni_energy: 
    " - Спасибо тебе, что спас меня и остальных."
    if spell_astral_link == 1: 
        "Приготовься принять заклинание Астральной Привязки. В мою сторону направляется серебристый поток, но я не защищаюсь, а наоборот, открываюсь навстречу ему."
        "- Тебе надо определить, в кого ты будешь вселяться."
    "Я должна помочь брату  - Рюни медленно встала и направилась к другим телам."
    if spell_astral_link == 1:
        n ''' - Я смогу вселиться в любое тело?
- Надо хорошенько подумать... - она помолчала, в её эмоциях я уловил смущение. - Я ещё слишком слаба, чтобы возвращаться в родной замок. Я могла бы разрешить тебе вселиться в моё тело, но только на то время, пока  ты отведешь меня домой. У тебя теперь должно быть много ''' 
        nvl clear
        n '''энергии. Ты чувствуешь, что стал сильнее? Когда вернёмся домой, я уверена, тобой заинтересуются наши Астральные маги и может даже научать тебя чему-то ноовому.
- Эмм... И я до конца жизни останусть вампиршей и буду пить кровь?  Может я вселюсь в кого-то из этих людей? - она быстро отвернулась и наклонилась над братом, но я успел заметить , как изменилось её лицо.'''
        nvl clear
        n ''' - Вампиры бессмертны!!! Сами они не умирают никогда. Только если им кто-то поможет, - она показала на остальных. - Наши маги проведут ритуал и я снова займу своё тело. Но если ты не хочешь, - она снова замолчала. Тогда мне придется остаться здесь до окончательного выздоровления. Ты будешь приводить мне свежие тела с кровью.. И тогда я быстро верну свою прежнюю форму.
 - А эти тела тебе не подойдут?'''
        nvl clear
        n ''' - В них почти нет крови, а там где осталась, она уже испортилась.Сколько времени прошло после ритуала? Где-то четыре-пять дней. Её можно использовать только в самом крайнем случае, для исцеления очень тяжелых ранений. А ты сам видишь - моё тело в порядке, - она покружилась, подпрыгнула и сделала сальто в воздухе. 
 - Ты же говорила, что ослабела?'''
        nvl clear
        n ''' - Для длительного недельного перехода по чужим землям да, у меня слишком мало энергии, а это - очень легко. Ты раньше не встречался с вампирами? Смотри, как  я могу, - и она заметалась по пещере с огромной скоростью, словно ребёнок, который показывает родителям своих успехи. Подпрыгивала, цеплялась за потолок, совершала скачки на несколько метров. 
 - Что-то я сомневаюсь, вселюсь я в тебя, с что будет с твоим братом и остальными вампирами? А что ещё ты можешь предложить?'''
        nvl clear
        n ''' -Нуу... - она резко остановилась, -  Если хочешь, ты можешь меня всю дорогу нести на руках . Выбирай тело вот этого тролля. Его силы как раз хватит до замка. Путешествие займет несколько месяцев. А там мы подберем тебе новое тело, получше. - я не видел её лица, но через мысленную связь вдруг понял, что она покраснела.'''
        nvl clear
        n '''- Так долго? Твой брат говорил неделю, - я уже привык к мысленному общению с Рюни и попробовал передать её своё удивление. - Ну ты сравнил! Ты знаешь, как быстро передвигаются вампиры? Особенно ночью.  А тролли такие медленные, совсем не приспособлены к перемещениям по лесу. И потом, там полно диких зверей, с которыми нужно сражаться. Да и патрули темных эльфов тоже не станут спокойно смотреть на гуляющего по их землям тролля с моим телом на плече, - Она что-то достала из поясной сумки'''
        nvl clear
        n '''и снова наклонилась над братом.
- Лучше выбери одного из этих вампиров, эти наши родственники Муни и Мейни. Если мы вернёся без них, родители будут нас ругать и даже могут наказать. Сейчас я верну брата к жизни, он подлечит меня и мы сможем отправитья в путь. ''' 
        n '''Все остальные расы слишком медленные. Светлых эльфов вообще не учитывай - здесь, в дали от родного леса, они очень ослаблены и ты станешь легкой добычей темных.'''
        nvl clear
        n '''  Человеческое тело ты не сможешь использовать, так же, как и своё ты ведь до ритуала был человеком?'''
    menu:
        "Да, я человек, и хочу им остаться.":
            $ hard_race = 0 # расса человек
            jump hard_no_race
        "Нет, я человек только наполовину":
            $ hard_race = 1 # расса полу-человек        
label hard_no_race:
    nvl clear
    n ''' Очень сомневаюсь, что эти люди изучали магию Астрала и смогут вместить в себя такую мощную сущность, как ты. - Рюни усмехнулась. - Так что тебе нужно будет в будущем найти человека, владеющего высшей магией Астрала, а пока придётся выбирать другую рассу. Гоблины - это низшие существа, не знаю, сможешь ли ты вселиться в них. Никогда о таком не слышала. Да и вообще, кто захочет быть гоблином? Они такие слабые и беспомощьные. В теле гоблина ты не сможешь меня защитить. И кто тогда понесёт моих'''
    nvl clear
    n '''родственничков? - она отошла от брата и направилась к другим вампирам. Потом продолжила. - Остаюстя тёмные эльфы - они с рождения изучают магию. Брат обратит тебя в вампира, у тебя хватит сил нести Муни или Мейни, а он понесёт второе тело. Но даже так, это замедлит нас. Трансформация в вампира может занять полдня или целые сутки. Мы уже столько времени потеряли в этой пещере.  Странно, что сюда ещё никто не заявился. Скорее всего нас уже ищут. Надо поспешить, пока наши поисковые отряды не встретились с темными. Нельзя допустить резню.'''
    menu:
        "С чего это на твои поиски выделят столько вампиров? Ты что,  принцесса ?":
            jump vampire_prince 
        "Почему поисковые отряды начнут убивать темных эльфов?":
            "На границе всегда случаются стычки, уже лет десять точно. Ты где жил всё это время?"
            menu:
                "Рассказать о себе":
                    "В горах в пещере с шаманом. Он нашел меня в лесу ещё ребенком. И всё эти годы обучал магии Астрала. Про вашу вражду с темными ничего не рассказывал."
                "Спросить о выходе из Астрала":
                    $ spell_astral_link = 1 
                    "Я не могу выйти из Астрала в своё тело."
                    "Как твой брат? Я вижу энергию в его теле, но не ощущаю присутствия. Он мог бы помочь мне." 

    return           


    

    

    return
label vampire_prince:
            "По мыслесвязи я очутил эмоции Рюни и понял, что угадал. Ну надо же, Принцесса Рюни. А брат получается принц. Надо перевести разговор на другую тему."
            menu:
                "А как ваши маги будут оживлять твоего брата и остальных?":
                    "Я вижу энергию в их телах, но не ощущаю присутствия?"
                    "Маги отыщут их души в глубинах Астрала и вернут в тела."
                    menu:
                        "Разве у вампиров есть души? Я всегда считал их одним из видов нежити?":
                            jump vampire_dusha
                        "Разве вампирам доступна магия Астрала? Насколько я знаю, они владеют магие Крови и Смерти.":
                            jump vampire_astral
label vampire_dusha:
    "Рюни скривилась,по мыслесвязи я ощутил её возмущение,  но всё же она ответила. - Это у низших вампиров. А мы - Высшие. Конечно же, у нас есть душа. Мы чувствуем, страдаем и любим. Ты же читаешь мои эмоции,"
    "улавливаешь мои чувства. Я что, похожа на бездушного упыря?"
    "Внезапно через мыслесвязь ко мне от неё повеяло нежностью и обожанием, и я почувствовал себя неловко за свои слова."
    "- Рюни, извини.Ты живая! Я всё понял, мне не следовало это говорить."
    return
label vampire_astral:
    "Так то обычные вампиры. А мы - Высшие! Мы может изучать все виды магии, если захотим!, - в её словах я почувствовал гордость за свою расу." 
    return