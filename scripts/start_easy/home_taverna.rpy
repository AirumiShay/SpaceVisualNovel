#Дом Таверна
label go_home_taverna:
    scene town_taverna:
        xalign 0.5 yalign 0.0 
    i "Зайду в таверну."
    
    scene town_taverna_2:
        xalign 0.5 yalign 0.0 
    "Вы заглянули в таверну. За столами  сидят несколько местных жителей."
    scene town_taverna_zakaz:
        xalign 0.5 yalign 0.0 

    "Подошла хозяйка и я сделал заказ. {w}  Пока я кушал, невольно слышал разговоры. Узнав новости, получил пару очков опыта и отправился домой."
    $ main_gold -= 1
#    $ monster_lvl = 2
    call add_xp_main(2) from _call_add_xp_main_3 
    jump go_home

