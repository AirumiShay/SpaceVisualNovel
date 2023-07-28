#добавляем персонажу опыт,и если хватило, то и уровень.
label add_xp_main(addxp):
#    $ main_xp += monster_lvl 
    $ main_xp += addxp 

    if main_xp >= main_xp_add :
        $ main_xp -= main_xp_add #  сохраняем превышение уровня
        $ main_level += 1           # повышаем уровень и здоровье
        $ main_health_max += 4 # заменить для других классов
        $ main_energy_max += 5
        $ main_health = main_health_max
        $ main_mana = main_mana_max
        $ main_energy = main_energy_max
        "Получен новый уровень: [main_level], поздравляем. Здоровье вашего персонажа повышено на 4, уровень бодрости на 5."
        $ main_xp_add = main_xp_add + main_hard_lvl + 1
        return
 
