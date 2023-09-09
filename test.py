import pygame as pg
from pg_lite import button


root = pg.display.set_mode((500, 500))


while True:
    for event in pg.event.get():
        action = event.type
        but = button(root, (255, 0, 0), (10, 10, 30, 30), event)
        if action == pg.QUIT:
            pg.quit()
            exit()
        if but:
            print('press')
    pg.display.flip()
