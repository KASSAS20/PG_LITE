import pygame as pg
from pg_lite import switch, button, check_box, vertical_switch, on_off, switch_box


root = pg.display.set_mode((500, 500))


while True:
    for event in pg.event.get():
        action = event.type
        root.fill((0, 0, 0))
        if 'but' not in locals():
            but = False
            but_2 = False
            but_2 = False
            but_3 = False
            but_4 = False
            but_5 = False
            but_6 = False
        but = switch(root=root,
                     event=event,
                     location_size=(0,0, 40, 20),
                     color=(255,0,0),
                     check=but)
        but_2 = vertical_switch(root=root,
                                event=event,
                                location_size=(0, 400, 30, 60),
                                check=but_2)
        
        but_3 = button(root=root,
                       event = event,
                       location_size=(100,0,30,30),
                       color=(255,0,0),
                       text = 'SAS')
        but_4 = check_box(root=root,
                          event=event,
                          location_size=(400, 300, 50,50), 
                          check=but_4)
        but_5 = on_off(root=root,
                       event=event,
                       location_size=(70, 200, 60, 30),
                       check = but_5)
        but_6 = switch_box(root=root,
                           event=event,
                           location_size=(300, 200, 50,50),
                           check= but_6)
        if action == pg.QUIT:
            pg.quit()
            exit()
        if but:
            print('press 1')
        if but_2:
            print('press 2')
        if but_3:
            print('press 3')
        if but_4:
            print('press 4')
        if but_5:
            print('press on/off')
        if but_6:
            print('press switch_box')
    pg.display.flip()
