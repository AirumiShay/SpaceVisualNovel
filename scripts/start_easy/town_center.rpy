screen map_button:
    zorder 12
    if map_mark == 0:
        textbutton "Открыть карту" action [SetVariable('map_mark',1), Show('map_scr')]
    else:
        textbutton "Закрыть карту" action [SetVariable('map_mark',0), Hide('map_scr')]
screen map_scr:
    zorder 11
    add '/images/karta_renpy.png' align .5, .5
