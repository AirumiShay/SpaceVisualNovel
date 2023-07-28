#Дом игрока  Eva
label go_home_eva:
    $ open_eva = True
    e "Вы пришли в гости к игроку Восхитительная."
    show ohotnitsa:
        xalign 0.5 yalign 0.2
    i "Привет, пойдём вместе качаться?"
    if eva_quest == 0:
        eva "Конечно, только в другой раз. Сегодня я изучаю зельеварение. Пообщайся с Травинкой, - сказала она и ушла в другую комнату."
        hide ohotnitsa
        $ eva_quest = 1
        scene travinka:
            xalign 0.5 yalign 0.0
        i "С Травинкой время летит незаметно. Она рассказывала про расы, населяющие этот мир, про империи, религии, богов и ещё много интересного. Потом накормила меня домашней выпечкой, завернула несколько пирожков с собой и пополнила запас моих зелий."
        i "Тепло попрощавшись с Травинкой, я вышел на улицу."
    else:
        $ eva_quest = 0
        eva "Идем, будем делать социальные квесты."
        i "Мы ходили по деревне, помогали местным жителям."
        scene town_23:
            zoom 1.3
        i "Носили воду из колодца, очищали огороды от бурьяна и рубили дрова."
        scene town_drova
        i "Выполнив квесты, мы получили немного опыта и прибавку к силе, ловкости и выносливости. Репутация с деревней тоже повысилась. Я попрощался с подругой, и она ушла."
#    $ main_xp += 5
    $ monster_lvl = 5
    call add_xp_main(monster_lvl) from _call_add_xp_main_2 # добавляем опыт главному персонажу  

    $ main_gold += 5
#   $ main_town_repo += 25
    $ main_energy -= 50
    $ night_up = 1
    jump town_night
