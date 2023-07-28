#ночная деревня
label town_night:
    scene town_night_1:
        xalign 0.5 yalign 0.0
    play music "music/two.ogg"
    i "Летняя ночь,тишина. Побродив некоторое время по деревне,пряталсф от стражников, чтобы ещё немного прокачать скрытность. Вернулся домой." 
    $ night_up = 1
    jump go_home
#     jump home_done

