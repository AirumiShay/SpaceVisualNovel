#подземелье в лесу
label dungeon:
    scene cavern_2:
        xalign 0.5 yalign 0.0
    i "Вот уже целый час я блуждаю в подземелье. Осторожно обхожу огромные сталктиты и сталагмиты."
    scene cavern_dungeon_1:
        xalign 0.5 yalign 0.0
    i "Что-же ждёт меня там, в глубине?"

    scene cavern_dungeon_2:
        xalign 0.5 yalign 0.0
    i "Зажигаю факел и подхожу ко входу туннеля."

    show boss_zombi:
        xalign 0.5 yalign 0.3
    i "Впереди  в темноте я с трудом различаю зомби. Судя по уровню -  босса этого подземелья. "
    show screen info_monster
    i "Огромный он, что-то я сомневаюсь в своей победе."
    i "Может лучше отступить, пока он меня не заметил?"
    menu:

        "Иду назад":
            jump choice1_yes

        "Буду сражаться!":
            jump choice1_no

label choice1_yes:

    $ menu_flag = True

 #       e "While creating a multi-path visual novel can be a bit more work, it can yield a unique experience."
    i "Решаю не рисковать напрасно. Вернусь позже, когда стану сильнее"
#    jump choice1_done
    hide screen info_monster
label go_town:
    i " Использую один из свитков телепорта, который мне дал староста и возвращаюсь в деревню"
    jump imagemap_example

label choice1_no:

    $ menu_flag = False


    i "Я достаю свиток  с заклинанием Света и активирую его на зомби."
    i " У него слабость к этой магии, он сгорает в ярком свечении. Невероятно, чтотак просто мне удаётся победить его!"
    hide screen info_monster


#    $ item[count] -= 1
    i "Забираю лут - 100 золотых"
#    i "Забираю лут - Легендарное оружие. 100 золотых, волшебное кольцо на интеллект и редкие перчатки."

    $ main_gold += 100
    $ monster_lvl = 24
    call add_xp_main(monster_lvl) from _call_add_xp_main # добавляем опыт главному персонажу  
    jump go_town

