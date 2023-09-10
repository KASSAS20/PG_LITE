import pygame as pg
from pg_lite import switch, button, check_box, vertical_switch, on_off


root = pg.display.set_mode((500, 500))


while True:
    for event in pg.event.get():
        action = event.type
        root.fill((0, 0, 0))
        if 'but' not in locals():
            but = False
            but_2 = False
            but_2 = False
            but_4 = False
            but_5 = False
        but = switch(root, (255, 0, 0), (0, 0, 0),
                     (0, 0, 70, 40), event, check=but)
        but_2 = vertical_switch(root, (255, 0, 0), (0, 0, 0),
                                (5, 50, 70, 40), event, check=but_2)
        but_3 = button(root, (255, 0, 0), (80, 5, 70, 40), event, text='3')
        but_4 = check_box(root, (255, 0, 0), (0, 0, 0),
                          (80, 50, 70, 40), event, check=but_4)
        but_5 = on_off(root, (255, 0, 0), (50, 0, 0), False,
                       False, (0, 200, 70, 40), event, but_5)

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
    pg.display.flip()
