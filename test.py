import pygame as pg
from pg_lite import button


root = pg.display.set_mode((500, 500))


while True:
    for event in pg.event.get():
        action = event.type
        root.fill((0,0,0))
        but = button(root, (255, 0, 0), (10, 10, 50, 50), event, text = 1)
        but_2 = button(root, (255, 0, 0), (50, 50, 50, 30), event, text = '2')
        but_3 = button(root, (255, 0, 0), (90, 90, 30, 50), event, text = '3')

        
        if action == pg.QUIT:
            pg.quit()
            exit()
        if but:
            print('press 1')
        elif but_2:
            print('press 2')
        elif but_3:
            print('press 3')
    pg.display.flip()
