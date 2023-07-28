# Вы можете расположить сценарий своей игры в этом файле.



# Игра начинается здесь:
label start:
    # Start by playing some music.
    play music "music/home.ogg"
#    $ renpy.movie_cutscene("videos/1.ogg")

    n '''2032 год. Компания Saturn Games, лидер в сфере компьютерных игр, запускает на рынок новую игру Space - место под солнцем. Игра очень быстро набирает популярность. Среди миллионов игроков, в игру приходит школьники Павел и Маша, а вслед за ними их одноклассник Степашин - любитель безумных экспериментов, выдумщик и фантазер. Благодаря своей запредельной удаче, настойчивости и любознательности, Степашин начинает своими поступками влиять на глобальную историю вселенной игры,'''
    nvl clear
    n ''' изменяя границы поселений,  устои и традиции государств и отношения между фрациями и империями. Разработчики игры и представить не могли, что кто-то будет ТАК играть в их игру.'''
 #   clean nlv
    nvl hide
    scene wallpaper
    $ main_yes = False #ещё не создан персонаж
label enter_game:
    scene home_stepashin:
        yalign  0.0
    e "Сити. Моя комната. {w}Я сел перед компьютером и запустил  игру. Вперед, к новым приключениям!"
    scene booting:
        yalign  0.0
    call begin_game from _call_begin_game # создаем, если ещё не создали персонажа
# Выполняем квесты с Евой
    $ eva_quest = 0
    $ night_up = 0
# Сколько изучено заклинаний разных школ магии

    $ spell_fire = 0
    $ spell_water = 0

    $ spell_air = 0
    $ spell_ground = 0

    $ spell_light = 0
    $ spell_dark = 0

    $ spell_life = 0
    $ spell_dead = 0
    $ spell_nekro = 0
    
    $ spell_chaos = 0
    $ spell_order = 0

    $ spell_mental = 0
    $ spell_psy = 0
    $ spell_astral = 0
    
    $ spell_bezdna = 0
    $ spell_pustota = 0
    $ spell_time = 0
    $ spell_space = 0 # магия пространства, включет телепортация и подпространственные карманы для складов, инвентаря и секретных комнат
    $ spell_elemental = 0 #магия элементалей
    $ spell_true = 0 #Истинная (изначальная) магия


    $ map_mark = 0 # карта не показана
    if  main_hard_lvl == 2:
        jump start_hard    
#Вошли в игру Space
label imagemap_example1:
    show screen info_player
label imagemap_example2:
#    scene   town_centre
    scene   town_centr

    play music "music/wood.ogg"
    i "Стою посреди улицы и думаю, куда бы пойти? {w} Открываю карту."
label imagemap_example:

#Выбираем на карте дом, куда отправиться
    call screen imagemap_example

#сюда уже не придем
#    show screen town_000

    return
#Карта поселка
screen imagemap_example():
    imagemap:
        idle "map_town"
        hover "imagemap hover"

        hotspot (165,510,135,100) action Jump("go_home_starosta") alt "Starosta"
        hotspot (355,170,128,93) action Jump("go_kuznets") alt "Kuznets"
        hotspot (500,255,64,64) action Jump("go_home_mag") alt "Mag 2"
        hotspot (505,455,64,64) action Jump ("go_home") alt "My Home"
        hotspot (400,280,93,93) action Jump("go_home_torgovets") alt "Torgovets"
        hotspot (370,385,93,64) action Jump ("go_home_lekar") alt "My Home"
        hotspot (300,250,48,48) action Jump ("go_home_eva") alt "Eva Home"
        hotspot (275,410,48,48) action Jump ("go_home_taverna") alt "Taverna"
        hotspot (575,120,48,48) action Jump("go_home_kladbishe") alt "Mag 2"
#Переход на кладбище
label go_home_kladbishe:
    call kladbishe from _call_kladbishe
    jump go_home
#Дом старосты
label go_home_starosta:
    i "Напрявляюсь в гости к старосте"
    scene home_starosta_in:
        xalign 0.5 yalign 0.0

    starosta "Это деревня Малые Топольки"

    starosta "Приветствую тебя, [main_name]."

#    starosta "Я не могу определить твою расу. Кто ты,[main_name]?"
#label name_present:
    i "Я ищу приключения! Где мне найти злобных чудовищ?"
    starosta "Иди в лес, держись правой стороны реки, когда пройдешь до тропы к болоту ,не сворачивай туда. Иди дальше. Там ты найдёшь вход в подземелье. Ты готов?"
    menu:
        "Да. Уже иду!":
            jump yes_quest
        "Эээ... Нет, мне нужно время для подготовки!":
            jump no_quest
label yes_quest:

    starosta "Вот возьми свитки телепортации в нашу деревню. Если заблудишься, используй." # А вот свитки с заклинаниями, они помогут тебе в подземелье."
    call take_item(items_db['scroll_teleport']) from _call_take_item
#    call take_item(items_db['scroll_light'])
    i "А вам не жалко отдавать такое сокровище? Они же стоят целое состоние!"
    starosta "У меня их целый ящик. Наш маг Томас приносит их мне. Его ученики делают свитки десятками и сотнями, чтобы повысить своё мастерство."
    i "Спасибо!" 
    starosta " Удачи, [main_name]!  "
    jump go_les

label no_quest:
    starosta " [main_name], если хочешь улучшить свои познания в магии, поговори с нашим магом Томом!"
    starosta "А для улучшения воинских умений, иди к кузнецу Вепрю."
    starosta "Также загляни к торговцу Златогорну. Он поможет тебе подобрать что-нибудь из оружия, брони и свитков с заклинаниями.{w} Увидимся позже"
    jump imagemap_example1


