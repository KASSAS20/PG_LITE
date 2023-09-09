import pygame as pg
from error import message_error
from coordinat_calculate import coordinat_circle, coordinat_rect

pg.init()


def button(root, color, location_size, event, text=False, text_color=False, text_font=False, text_size=10):
    if not isinstance(root, pg.surface.Surface):
        message_error(1)
    elif not isinstance(color, tuple):
        message_error(2)
    elif len(color) != 3:
        message_error(3)
    elif not isinstance(location_size, tuple):
        message_error(4)
    elif len(location_size) != 4:
        message_error(5)
    elif not isinstance(event, pg.event.Event):
        message_error(6)

    action = event.type
    but = pg.draw.rect(root, color, location_size)

    if text != False:
        text = str(text)
        if text_color == False:
            text_color = (255-color[0], 255-color[1], 255-color[2])
        if text_font == False:
            text_font = 'notosansmonocjkjp'

        elif text_color not in pg.font.get_fonts():
            message_error(7)
        elif not isinstance(text_color, tuple):
            message_error(8)
        elif len(color) != 3:
            message_error(9)

        font = pg.font.SysFont(text_font, text_size)
        button_text = font.render(text, True, text_color)
        but_center = button_text.get_rect(center=but.center)
        root.blit(button_text, (but_center))

    if action == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            position = event.pos
            if position[0] > location_size[0]-1 and position[0] < location_size[0]+location_size[2]+1 and position[1] > location_size[1]-1 and position[1] < location_size[1] + location_size[3] + 1:
                return True


def switch(root, color, color_circle, location_size, event, check):
    if not isinstance(root, pg.surface.Surface):
        message_error(1)
    elif not isinstance(color, tuple):
        message_error(2)
    elif len(color) != 3:
        message_error(3)
    elif not isinstance(location_size, tuple):
        message_error(4)
    elif len(location_size) != 4:
        message_error(5)
    elif not isinstance(event, pg.event.Event):
        message_error(6)
    elif not isinstance(check, bool):
        message_error(10)

    x = location_size[0]
    y = location_size[1]
    height = location_size[3]
    width = location_size[2]-height

    pg.draw.circle(
        root, color, (x + height // 2, y + height // 2), height // 2)
    pg.draw.rect(root, color, (x+height//2, y, width, height))
    pg.draw.circle(
        root, color, (x + height // 2 + width, y + height // 2), height//2)

    switch_coordinate_1 = coordinat_circle(
        height // 2, x + height // 2, y + height // 2)
    switch_coordinate_2 = coordinat_rect(x, y, x + width, y + height)
    switch_coordinate_3 = coordinat_circle(
        height//2, x + height // 2 + width, y + height // 2)
    switch_coordinate_full = list(
        set(switch_coordinate_1 + switch_coordinate_2 + switch_coordinate_3))

    action = event.type

    if action == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            position = event.pos
            if position in switch_coordinate_full:
                check = not check
    if check == False:
        switch_circle_1 = pg.draw.circle(
            root, color_circle, (x + height // 2, y + height // 2), height // 2.22)
    if check == True:
        switch_circle_2 = pg.draw.circle(
            root, color_circle, (x + height // 2 + width, y + height // 2), height // 2.22)
    return check


def check_box(root, color, color_box, location_size, event, check):

    if not isinstance(root, pg.surface.Surface):
        message_error(1)
    elif not isinstance(color, tuple):
        message_error(2)
    elif len(color) != 3:
        message_error(3)
    elif not isinstance(location_size, tuple):
        message_error(4)
    elif len(location_size) != 4:
        message_error(5)
    elif not isinstance(event, pg.event.Event):
        message_error(6)
    elif not isinstance(check, bool):
        message_error(10)
    elif not isinstance(color_box, tuple):
        message_error(11)
    elif len(color_box) != 3:
        message_error(12)

    x = location_size[0]
    y = location_size[1]
    width = location_size[2]
    height = location_size[3]

    pg.draw.rect(root, color, location_size)

    if check == True:
        modul_x = location_size[2]//20
        modul_y = location_size[3]//20
        pg.draw.rect(root, color_box, (location_size[0]+modul_x, location_size[1] +
                     modul_y, location_size[2]-modul_x*2, location_size[3]-modul_y*2))

    coordinat = coordinat_rect(x, y, x + width, y + height)

    action = event.type

    if action == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            position = event.pos
            if position in coordinat:
                check = not check

    return check
