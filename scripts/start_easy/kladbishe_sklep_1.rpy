#поход в ближний склеп.
label sklep1:
    i "Потихоньку пробираюсь вдоль ограды и подхожу к склепу."
    i " Изнутри тянет холодом. Пока я рассматривал склеп, из открытой гробницы поблизосьти  послышалось рычание и показался  зомби. Заметив меня, он  медленно начал вылазить, но я успел зайти в склеп."
    scene sklep_1:
        xalign 0.5 yalign 0.0
    $ main_energy -= 10
    i "Мрачновато тут. Похоже на усыпальницу. Пройду немного вглубь."
    scene sklep_1_1:
        xalign 0.5 yalign 0.0
    $ monster_lvl = main_level + 1
#            scene monster_goblin_1
    $ main_energy -= 10
    i "Я медленно иду по коридору. Впереди коридор сворачивает влево."
    $ renpy.movie_cutscene("videos/1.ogg")

    i "Вдруг из-за угла появляются несколько крыс и бегут ко мне. Одна пробегает мимо, вторая тоже.Странно, почему они не нападают. Похоже они от кого-то убегают."
#    $ renpy.movie_cutscene("videos/1.ogg")
    scene sklep_rats_1:
        xalign 0.5 yalign 0.0

    menu:
        "Лучше уйду отсюда, пока не появился монстр, напугавший крыс.":
            i "Вышел из склепа и отправился в деревню."
            $ main_energy -= 10
            return
        "Нападу на последнюю крысу,и на монстра,кем-бы он ни был. Опыт лишним не бывает":  
#            call atack_002(0)
            $ main_energy -= 10
#            scene monster_zombi_1
#            pause(1)
#           image launch = Movie(play="videos/zombi_knife.mkv", pos=(10, 10), anchor=(0, 0))
#            show launch # behind e
#
#            i "Побродил ещё полчаса."
#            hide launch
 
            $ renpy.movie_cutscene("videos/rat_fire.ogg")
            scene sklep_rat_1:
                xalign 0.5 yalign 0.0
            call atack_002(0) from _call_atack_002
            i "Я легко расправился с крысой, кинув в неё огненный шар. Выпил зелье восстановления. {w} Только подошел к повороту, тут же появился зомби. Вот значит, от кого бежали крысы.{w}. Попробую ударить его кинжалом."
            $ renpy.movie_cutscene("videos/zombi_knife_fail.ogg")
            scene sklep_zombi_1:
                xalign 0.5 yalign 0.0
            i "Похоже кинжалом его не победить.У зомби не было одной руки,но не смотря на это он напирал на меня и нанес несколько ударов. Я едва успевал отходить назад.{w} Попробую бросить в него огонь."
            $ renpy.movie_cutscene("videos/zombi_fire.ogg")
            scene sklep_zombi_3:
                xalign 0.5 yalign 0.0
            call atack_002(0) from _call_atack_002_1
            i "Надо запомнить - у зомби уязвимость к огню."
            i "Я побродил ещё полчаса."
            $ renpy.movie_cutscene('videos/2.ogg')
            scene sklep_zombi_2:
                xalign 0.5 yalign 0.0
            i "Упокоил ещё одного зомби, тоже однорукого. Возможно, на них ставили опыты."
            $ main_energy -= 30
#           $ main_xp += 8
            $ monster_lvl += 8
            call add_xp_main(monster_lvl) from _call_add_xp_main_1 # добавляем опыт главному персонажу
#pause(1)
            i "Все встреченные здесь мобы были 0-го  и 1-го уровня, я легко их побеждал. Надеюсь, в других склепах у мобов будут уровни побольше."
            $ main_energy -= 10
#           i "успешно упокоил несколько монстров с  уровнями  не выше 2-го, получил опыт и простенький лут." 
#            pause(1)
#label skip_battle_1:
            i "Пора возвращаться."
            $ main_energy -= 10
            return
