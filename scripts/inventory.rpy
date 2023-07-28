#Инвентарь от cosmo
#    define inventory = [] # 
label take_item(newitem):
    $ inventory.append(newitem)
    return
init python:
    def remove_item_by_name(item_name, number):
        for item in inventory:
            if item == item_name['name']:
#                inventory.remove(item)
                text = "Вы выбрали " + item['name'] # + number
                renpy.notify(text)
                break
    def drop_item(item, number):
        inventory.remove(item)
        text = "Вы выбросили " + item['name'] # +" "+ string(number)
        renpy.notify(text)
#        renpy.notify(number)

screen inventory_screen:
    modal True
    frame:
        xsize 1200
        ysize 680
        xalign 0.5
        yalign 0.5
        padding (20,20)
        vbox:
            hbox:
                xsize 1180
                text "{image=/images/pic/pic_suma.png} Рюкзак"
                imagebutton xalign 0.9:
                    idle ('images/pic/pic4.png')
                    hover ('images/pic/pic1.png')
                    action Hide('inventory_screen')
            hbox:
                xsize 1180
                ysize 660
                viewport id "vp":
                    draggable True
                    mousewheel True
                    xsize 1130
                    xalign 0.1
                    vbox:
                        for item in inventory:
                            hbox:
#                                text "{image=images/items/pic_scroll_1.png}"
                                null height 15
                                vbox:

                                    text "[item[count]]  шт {size=36} [item[name]] {/size}"
                                    text "{size=32} [item[desc]] {/size}"
                                    hbox:
                                        xsize 400
                                        textbutton "{size=27}Использовать{/size}" action Function(use_item, item) xalign 0.5
                                        textbutton "{size=27}Выложить{/size}" action Function(drop_item, item) xalign 0.5 
                vbar value YScrollValue("vp") 
