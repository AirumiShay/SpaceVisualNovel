#Дом персонажа
label go_home:

    scene home_main:
        xalign 0.5 yalign 0.0 
#    play music "music/wood.ogg"
    play music "music/town1.ogg"
    i "Дом, милый дом."
#    $ night_up = 0
    i "Наверно,гулять уже поздно? Или ... [night_up]"

    menu:
        "Пройтись по деревне":
            jump imagemap_example1
        "Отдыхать до наступления темноты, потом выйти гулять" if night_up != 1:
            jump  town_night
        "Отдыхать до утра":

            jump home_done

        "Прочитать игровую вики":
            "Space - это игра в жанре RPG. Пока всё"
            jump imagemap_example1
        "Выйти из игры Space?":   
            jump image_map_done
label home_done:
    $ night_up = 0
    "На следующее утро..."


    $ main_energy = main_energy_max 
    $ main_energy += 50
    $ main_mana = main_mana_max
    $ main_health = main_health_max
    i "Я хорошо отдохнул. Уровень здоровья и  маны восстановлен. Уровень бодрости повышен на 50. Выхожу на улицу."
#    $ item = inventory[0]
#    "Вещь {image=images/items/pic_scroll_1.png} [item]  шт {size=36} [item] {/size} {size=32} [item[desc]] {/size}"
    jump imagemap_example1 

label image_map_done:
    scene home_stepashin:
        yalign  0.0

    play music "music/home.ogg"
    e "Я выключил компьютер и потянулся. Пора отдохнуть. Завтра ещё поиграю."
    jump  imagemap_example2 # enter_game


