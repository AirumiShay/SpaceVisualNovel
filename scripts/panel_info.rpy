#В этом файле панели с информацией о характеристиках персонажей и монстров
#маленькие панели с умениями и заклинаниями.
#Так же здесь будет панель инвентарь и основное окно персонажа в конце файла
#Панель информации о монстре
screen info_monster():
    frame:
        padding (10,10)
        xalign 0.95
        yalign 0.05
        xsize 200
        ysize 200

        vbox:
            xsize 200
            text "Зомби-Босс"
            text "Уровень: 20"
            null height 15
            textbutton "Убрать" action Hide("info_monster")
#    show screen monster_000
#Панель информации о монстре
screen info_monster_1():
    frame:
        padding (10,10)
        xalign 0.95
        yalign 0.05
        xsize 200
        ysize 200

        vbox:
            xsize 200
            text "Ящер"
            text "Уровень: 1"
            null height 15
            textbutton "Убрать" action Hide("info_monster")
#Панель информации о монстре
screen info_monster_2():
    frame:
        padding (10,10)
        xalign 0.95
        yalign 0.05
        xsize 200
        ysize 200

        vbox:
            xsize 200
            text "Тролль"
            text "Уровень: 2"
            null height 15
            textbutton "Убрать" action Hide("info_monster")
#Панель информации о монстре
screen info_monster_3():
    frame:
        padding (10,10)
        xalign 0.95
        yalign 0.05
        xsize 200
        ysize 200

        vbox:
            xsize 200
            text "Огр"
            text "Уровень: 3"
            null height 15
            textbutton "Убрать" action Hide("info_monster")


#Ниже панельки заклинаний

#Заклинание лечение
screen spell_000():
    frame:
        xalign 0.0 ypos 200
        vbox:
            text "Малое лечение"
            textbutton "Излечиться (+5)":
                action Return(True)
#Заклинание огненный шар
screen spell_001():
    frame:
        xalign 0.0 ypos 200
        vbox:
            text "Огненный шар (-5)"
            textbutton "Кинуть (-5)":
                action  Return(True)
#заклинание ледяная игла или стрела
screen spell_002():
    frame:
        xalign 0.0 ypos 650
        vbox:
            text "Ледяная игла (-2)"
            textbutton "Стрелять (-2)":
                action  Return(True)
#Заклинание воздушный кулак
screen spell_003():
    frame:
        xalign 0.0 ypos 200
        vbox:
            text "воздушный кулак (-5)"
            textbutton "Ударить (-5)":
                action  Return(True)
#заклинание каменный осколок
screen spell_004():
    frame:
        xalign 0.0 ypos 650
        vbox:
            text "каменный осколок"
            textbutton "Бросить (-2)":
                action  Return(True)
#Заклинание Удар Тьмы
screen spell_005():
    frame:
        xalign 0.0 ypos 450
        vbox:
            text "Удар Тьмы"
            textbutton "Ударить (-3)":
                action  Return(True)
#заклинание Прах
screen spell_006():
    frame:
        xalign 0.0 ypos 350
        vbox:
            text "Прах (-5)"
            textbutton "применить (-5)":
                action  Return(True)
#Заклинание контроль нежити
screen spell_007():
    frame:
        xalign 0.0 ypos 350
        vbox:
            text "контроль нежити (-4)"
            textbutton "применить (1сек)":
                action  Return(True)
#выпить зелье здоровья
screen spell_100():
    frame:
        xalign 0.0 ypos 450
        vbox:
            text "Зелье здоровья"
            textbutton "Выпить (+10)":
                action  Return(True)
#выпить зелье маны
screen spell_101():
    frame:
        xalign 0.0 ypos 550
        vbox:
            text "Зелье маны"
            textbutton "Выпить (+10)":
                action  Return(True)
#выпить зелье бодрости
screen spell_102():
    frame:
        xalign 0.0 ypos 650
        vbox:
            text "Зелье бодрости"
            textbutton "Выпить (+35)":
                action  Return(True)



 
#Панель информации об игроке
screen info_player():
    frame:
        padding (20,20)
        xalign 0
        yalign 0
        xsize 200
        ysize 270

        vbox:
            xsize 200
            text "[main_name]"
            text "Lvl: [main_level]"
            text "HP: [main_health] из [main_health_max]"
            text "MP:  из  из "
            text "E: [main_energy]"
#            text "Gold: [main_gold]"
            text "XP: [main_xp] из [main_xp_add]"
#            null height 5
            textbutton "Карта" action Show("map_button") alt "map_button"
            textbutton "Инвентарь" action Show("info_bag") alt "View"
#    call screen inventory_screen
#label view_bag:
#    call screen info_bag 
#    return True
#    jump go_home
#Панель инвентаря
screen info_bag():
    modal True
    frame:
        padding (5,5)
        xalign 0
        yalign 0
        xsize 1270
        ysize 710

        vbox:
            hbox:
                xsize 1180
                null height 10
                textbutton "Закрыть" action Hide("info_bag")
                text "  Вещи в инвентаре. Coin's: [main_gold] Максимум вес,кг: 10"

            hbox:
                xsize 1180
                ysize 680
 
                viewport id "vp":
                    draggable True
                    mousewheel True
                    xsize 1180
                    xalign 0.1
                    vbox:
#                        text "              "
                        $ number_item = -1
                        for item in inventory:
                            hbox:
                                null height 5
                                vbox:
                                    text "   [item[count]]  шт {size=36} [item[name]] {/size}"
                                    text "{size=32} [item[desc]] {/size}"
                                    hbox:
                                        xsize 400
                                        textbutton "{size=27}Использовать{/size}" action  Hide("info_bag") xalign 0.5
                                        $ number_item += 1
                                        textbutton "{size=27}Выложить{/size}" action  Function(drop_item, item, number_item) xalign 0.5 
 
                vbar value YScrollValue("vp")

 
