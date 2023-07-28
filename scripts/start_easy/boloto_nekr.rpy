label boloto:
    scene home_nekromant
    e "Очень осторожно иду по болоту, и через некоторое время замечаю огромные стволы деревьев. На одном из них виднеется жилье из бревен. {w} Как только я направился к дереву с домиком, перед ним появилась темная фигурас посохом." 
    e "Лицо скрыто капюшоном. Похоже это и есть тот самый колдун, о котором говорил маг Том"
    scene nekro:
        xalign 0.5 yalign -0.3
        size (1280,720)
    menu:
        "Не стоит с ним связываться, темная магия не для меня":
            i "Не начиная разговора, я отошел подальше"
            jump go_town1
        "Вот он шанс стать Некромантом" if spell_nekro == 0:
            i "Я был доволен. Колдун охотно посвятил меня в основы некромантии. По его словам, я первый за несколько десятилетий, пожелал стать его учеником"
            $ spell_nekro = 1  
            jump go_town1
        "Надо изучить еще  заклинания. Пойду к некроманту" if spell_nekro != 0:
            i "Я был доволен. Старый колдун увлеченно рассказывал мне особенности своей професии и помог улучшить мои навыки"    
            jump go_town1
label go_town1:
    i " Использую один из свитков телепорта, который мне дал староста и возвращаюсь в деревню"
    jump imagemap_example

