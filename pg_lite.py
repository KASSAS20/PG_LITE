import pygame as pg
pg.init()


def button(root, color, location_size, event):
    action = event.type
    but = pg.draw.rect(root, color, location_size)
    if action == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            position = event.pos
            if position[0] > location_size[0]-1 and position[0] < location_size[0]+location_size[2]+1 and position[1] > location_size[1]-1 and position[1] < location_size[1] + location_size[3] + 1:
                return True
