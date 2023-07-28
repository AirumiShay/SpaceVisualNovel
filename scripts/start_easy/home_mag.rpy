#Дом мага
label go_home_mag:
    e "Вы решили пойти в гости к магу Тому"
    hide screen info_player
    show mage:
        xalign 0.5 yalign 0.3

    show air-magic:
        xalign 0.15 yalign 0.0  
    show fire-magic:
        xalign 0.8 yalign 0.0 
    show water-magic:
        xalign 0.15 yalign 0.6 
    show necromanc:
        xalign 0.8 yalign 0.6  

# уменьшаем количество свитков Света в инвентаре
#    $ item_name = 'scroll_light'
#    call remove_item_by_name('scroll_light') 
 #   $ for item in inventory:
#        if item == item_name['name']:
 #           "В инвентаре найден свиток [item]"
#            #$ inventory.remove(item)
#                break
#        if item == item_name['name']:
#            "В инвентаре найден свиток [item]"


    tomas "Выберите тип магии, которую вы хотите изучить: {w} Магия воздуха, огня, воды, некромантия"
    menu:
        "Хочу изучить магию воздуха":
            i "Том приносит мне старую книгу, после изучения я получаю базовый навык - Магия Воздуха и пару начальных заклинаний."
            $ spell_air += 1



            jump end_select_mag
        "Я буду огненным магом!":
            i "Том предлагает мне  книгу в кожаном переплёте, изучив которую я получил базовый навык - Магия Огня и пару начальных заклинаний."
            $ spell_fire += 1

            jump end_select_mag
        "Магия воды? - очень интересно":
            i "Том передал мне старую книгу, изучив которую я получил базовый навык - Магия Воды и пару начальных заклинаний."
            $ spell_water += 1

            jump end_select_mag
        "Некромантия - самая сильная магия. Я выбираю её!":
            tomas "Я не могу научить тебя. В лесу на болотах когда-то жил некромант. Попробуй найти его.  Возможно, он захочет обучать тебя."
            jump end_select_mag
label end_select_mag:
    show screen info_player 
    jump go_home

