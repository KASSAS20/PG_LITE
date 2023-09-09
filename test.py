import pygame as pg
from pg_lite import switch, button


root = pg.display.set_mode((500, 500))


while True:
    for event in pg.event.get():
        action = event.type
        root.fill((0,0,0))
        if 'but' not in locals():
            but = False
            but_2 = False
        but = switch(root, (255, 0, 0), (0,0,0), (0, 0, 70, 40),event, check=but)
        but_2 = switch(root, (255, 0, 0), (0,0,0), (0, 50, 70, 40),event, check=but_2)
        but_3 = button(root, (255, 0, 0), (80, 0, 70, 40), event, text = '3')
        but_4 = button(root, (255, 0, 0), (80, 50, 70, 40), event, text = '3')

        
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
    pg.display.flip()
