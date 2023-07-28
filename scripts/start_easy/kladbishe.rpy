label kladbishe:
    $ open_kladbishe = True
    scene town_wood_1
    $ main_energy -= 1
    "Я вышел из деревни и направился в лес"
    scene town_wood_kladbishe
    $ main_energy -= 2
    "Через некоторое время я увидел крест, значит, кладбище рядом."
    play music "music/nightcity1.ogg"
#    scene enter_kladbishe_1:
#        xalign 0.5 yalign 0.0
    i "Стою у входа на кладбище. {w} Справа небольшая заброшенная церковь."
    scene kladbishe_2:
        xalign 0.5 yalign 0.0
    i "Скелетов пока нет или отсюда их просто не видно. Слева склепы . Ещё один в конце кладбища."
    menu:
        "Пойду как я отсюда":
            i " Лучше уйду, пока монстры не набежали."
            return
        "Может проверить, что в церкви?":
            i "Я, стараясь не шуметь, подхожу к дверям. Закрыто."
            i " Лучше уйду отсюда, пока скелеты не появились."
            return
        "Посмотрю, что в ближнем склепе":
            call sklep1 from _call_sklep1
            return
        "Пойду в дальний склеп, там мобы сильнее":

            i "Потихоньку пробираюсь вдоль ограды и захожу в склеп."
            scene enter
            $ main_energy -= 1
#            i "Появляется сообщение."
            i "Выберите уровень сложности для прохождения этого подземелья?"
            menu: 
                "Обучение":
                    call battle_sklep(0) from _call_battle_sklep
                    return
#                    jump go_home

                "Легкий":
                    call battle_sklep(1) from _call_battle_sklep_1
                    return
#                    jump go_home

                "Нормальный":
                    call battle_sklep(2) from _call_battle_sklep_2
                    return
 #                   jump go_home

                "Сложный":
                    call battle_sklep(3) from _call_battle_sklep_3
                    return
                "Лучше уйду отсюда, не хочу сражаться.":
                    return
            return
        "Поохотиться на мобов, что-ли? Эй, где вы все попрятались?":
            i "Я вслух произнёс эту фразу"
            i "Из-за ближайшего могильного камня послышалось рычание и показался полуразложившийся зомби. Заметив меня, он по-киношному протянул ко мне руки и медленно побрел ко мне."
            i " Лучше уйду отсюда, пока он ещё далеко."
            $ main_energy -= 10
            return
   
    return

# Битва с мобами в склепе.
label battle_sklep(hard_lvl):
    play music "music/desertkingdom.ogg"
    $ main_energy -= 5
    scene   big_sklep_1:
        xalign 0.5 yalign 0.0
    i "Передо мной пояляется прямоходящий ящер."
    show screen info_monster_1
    scene   monster_yasher_1:
        xalign 0.5 yalign 0.0
    i "Он не особо сильный. Если нападу первым, сваншотю его."
    call atack_001(1) from _call_atack_001
    i "Иду дальше"
    $ main_energy -= 5
    scene   big_sklep_1:
        xalign 0.5 yalign 0.0
    i "Передо мной снова ящер."
    show screen info_monster_1
    scene   monster_yasher_1:
        xalign 0.5 yalign 0.0
    i "Сейчас по-быстрому завалю его."
    call atack_001(1) from _call_atack_001_1
    i "Изучаю склеп"

    $ main_energy -= 5
    scene   big_sklep_2:
        xalign 0.5 yalign 0.0
    hide screen info_monster_1
    i "Передо мной пояляется троль. Если бы он не был таким неповоротливым, он вполне мог бы доставить мне хлопот."
    scene   monster_troll_1:
        xalign 0.5 yalign 0.0
    show screen info_monster_2
    call atack_001(2) from _call_atack_001_2 # вызываем бой с монстром уровня 2
    hide screen info_monster_2
    i "Благодаря моим прокачанным умениям, я легко побеждаю его."
    i "Продолжаю изучать склеп"
    $ main_energy -= 10
    scene   big_sklep_3:
        xalign 0.5 yalign 0.0
    i "Мне навстречу выходит огр."
    scene   monster_vampire_ogr_1:
        xalign 0.5 yalign 0.0
    i "Судя по его клыкам, он вполне может быть вампиром"
    show screen info_monster_3
    call atack_001(3) from _call_atack_001_3 # вызываем бой с монстром уровня 3
    hide screen info_monster_3
    i "Благодаря моим прокачанным умениям, мне удаётся победить огра."    

#    $ main_level += 1
#    hide info_player
#    show info_player
    i "Опыт получил. Лут собрал"            
    $ main_energy -= 10
    i "Пора возвращаться. Уже вечер."
    return
# бой с монстром
label atack_001(monster_lvl):
#отображаем заклинание кинуть огненный шар и ждём нажатия на нём
    $ monster_lvl += 1
    $ monster_lvl += hard_lvl
    call screen spell_001
    "Вы наносите 5 урона: огонь. Монстр наносит вам [monster_lvl] урона."
    $ main_health -= monster_lvl 
    $ main_mana -= 5
    $ main_energy -= 10
    call screen spell_003
    "Вы наносите 5 урона: воздух. Монстр наносит вам [monster_lvl] урона."
    $ main_health -= monster_lvl 
    $ main_mana -= 5
    $ main_energy -= 10

    "Монстр погибает. Вы получаете: опыт [monster_lvl] XP. золото:1 "
    $ main_gold += 1
    call add_xp_main(monster_lvl) from _call_add_xp_main_4 # добавляем опыт главному персонажу
    $ main_energy += 5
    i "Надо подлечиться и восствовить потраченную ману."
    call screen spell_100
    $ main_health = main_health_max
#    "Вы выпили зелье лечения. Уровень здоровья восстановлен."
    $ main_energy += 5
#    i "Маловато маны!"
    call screen spell_101
    $ main_mana = main_mana_max
#   "Вы выпили зелье маны. Уровень маны восстановлен."
    return

# Бой в малом склепе
label atack_002(monster_lvl):
    $ monster_lvl += 1
    $ main_energy -= 10
    $ main_health -= monster_lvl
    $ main_health -= monster_lvl
    $ main_mana -= 6
    "Монстр погибает. Вы получаете: опыт [monster_lvl] XP. золото:1 "

    $ main_gold += 1
    call add_xp_main(monster_lvl) from _call_add_xp_main_5 # добавляем опыт главному персонажу

    $ main_energy += 5
#    i "Надо бы подлечиться и ману восстановить"
#    show screen spell_100
#    pause(1)
    $ main_health = main_health_max
#    "Вы выпили зелье лечения. Уровень здоровья восстановлен."
#    $ main_energy += 5
#    pause(1)
#   i "Маловато маны"
#   call screen spell_101
    $ main_mana = main_mana_max
#    pause(1)
#    "Вы выпили зелье маны. Уровень маны восстановлен."
    return


