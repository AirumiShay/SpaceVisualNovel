#В этом файле инициализация переменных в начале игры

# Определение персонажей игры.
define e = Character('Степашин', color="#c8ffc8")
define i = Character('Я', color="#c8ffc8")
define n = Character(None, kind = nvl, what_size=48)
define starosta = Character('Староста Мудрогор', color="#c8ffc8")
define tomas = Character('Томас', color="#c8ffc8")
define vepr = Character('Вепрь', color="#c8ffc8")
define eva = Character('Восхитительная', color="#c8ffc8")
define lekar = Character('Фелина', color="#c8ffc8")
define torgovets = Character('Златогор', color="#c8ffc8")
define neckromant = Character('Колдун', color="#c8ffc8")

label begin_game:
#    $ renpy.movie_cutscene('videos/logo.ogv')
    "Вход в  игру Space - Место под солнцем."
    define inventory = [] #
#    $ inventory.append(items_db['scroll_fire'])
    $ night_up = 0 
    if main_yes == False:
        "Выберите уровень сложности игры, от него зависит стартовая локация, репутация с НПС и набор вещей персонажа и его раса. В процессе игры можно будет изменять уровень сложности, но  вышеперечисленное не изменится."
#        "На легком уровне у вашего персонажа сразу будет хорошая начальная экипировка и  репутация с нпс. Персонаж появится в мирном поселении и все нпс будут помогать ему развиваться. Монстры не будут нападать первыми." 
#        "На сложном уровне  персонаж получит минимальную экипировку и нейтральную репутацию."
           
        menu:
            "Легкий":
                $ main_gold = 250     # денег у персонажа
                $ main_level = 5    # уровень персонажа 
                $ main_health = 35  # здоровье персонажа   в данный момент
                $ main_health_max = 35  # максимальное здоровье персонажа на этом уровне
                $ main_xp_add = 16 # нужно опыта для след. уровня
                $ main_town_repo = 200 # репутация с деревней
                $ main_hard_lvl = 0
                call take_item(items_db['scroll_fire']) from _call_take_item_1

                call take_item(items_db['scroll_light']) from _call_take_item_2


                jump  begin_game1
            "Средний":
                $ main_gold = 25     # денег у персонажа
                $ main_level = 2    # уровень персонажа 
                $ main_health = 20  # здоровье персонажа   в данный момент
                $ main_health_max = 20  # максимальное здоровье персонажа на этом уровне
                $ main_xp_add = 14 # нужно опыта для след. уровня
                $ main_town_repo = 50 # репутация с деревней
                $ main_hard_lvl = 1
                call take_item(items_db['scroll_fire']) from _call_take_item_3

                jump  begin_game1
            "Сложный":
                $ main_level = 0    # уровень персонажа
                $ main_gold = 2     # денег у персонажа
                $ main_health = 5  # здоровье персонажа   в данный момент
                $ main_health_max = 10  # максимальное здоровье персонажа на этом уровне
                $ main_xp_add = 10 # нужно опыта для след. уровня
                $ main_town_repo = 5 # репутация с деревней
                $ main_hard_lvl = 2
#                call take_item(items_db['scroll_fire'])

#                call take_item(items_db['scroll_light'])

 
                jump  begin_game1
            "Выбрать максимально сложный уровень":
                $ main_level = 0    # уровень персонажа
                $ main_gold = 0     # денег у персонажа
                $ main_health = 1  # здоровье персонажа   в данный момент
                $ main_health_max = 10  # максимальное здоровье персонажа на этом уровне
                $ main_xp_add = 10 # нужно опыта для след. уровня
                $ main_town_repo = 0 # репутация с деревней
                $ main_hard_lvl = 3
                jump  begin_game1

label begin_game1:
        $ main_yes = True    #создаём
 
        $ main_mana = 10    # значение маны персонажа  в данный момент
        $ main_mana_max = 10    # максимальная мана персонажа на этом уровне 
        $ main_energy = 100  #   бодрость персонажа в данный момент, тратиться на действия и может быть больше из-за бафов или меньше из-за дебафов   
        $ main_energy_max = 100  # максимальная бодрость персонажа может быть больше из-зи бафов или меньше из-за дебафов
  
        $ main_xp = 0      #  набрано опыта на текущем уровне

        e "Создание персонажа"
#        $ main_name = renpy.input("Введите имя для нового персонажа", length=20, default="Шмыг").strip()
        $ main_name = "Шмыг"
        return

