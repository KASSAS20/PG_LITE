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


def vertical_switch(root, color, color_circle, location_size, event, check):
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
    width = location_size[2]//2
    height = location_size[3]

    pg.draw.circle(
        root, color, (x+width//2, y + height // 2), width//2)
    pg.draw.rect(root, color, (x, y+height//2, width, height))
    pg.draw.circle(
        root, color, (x + width // 2, y + height*1.5), width//2)

    switch_coordinate_1 = coordinat_circle(
        width//2, x+width//2, y + height // 2)
    switch_coordinate_2 = coordinat_rect(x, y+height//2, width, height)
    switch_coordinate_3 = coordinat_circle(
        width//2, x + width // 2, y + height*1.5)
    switch_coordinate_full = list(
        set(switch_coordinate_1 + switch_coordinate_2 + switch_coordinate_3))

    action = event.type

    if action == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            position = event.pos
            if position in switch_coordinate_full:
                check = not check
    if check == False:
        pg.draw.circle(
            root, color_circle, (x+width//2, y + height // 2), width // 2.22)
    if check == True:
        pg.draw.circle(
            root, color_circle, (x + width // 2, y + height+height//2), width // 2.22)

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


def on_off(root, color_on, color_off, color_text_on, color_text_off, location_size, event, check, text_on='ON', text_off='OFF', text_font='notosansmonocjkjp', text_size=10):
    if not isinstance(root, pg.surface.Surface):
        message_error(1)
    elif not isinstance(location_size, tuple):
        message_error(4)
    elif len(location_size) != 4:
        message_error(5)
    elif not isinstance(event, pg.event.Event):
        message_error(6)
    elif not isinstance(check, bool):
        message_error(10)
    elif not isinstance(color_on, tuple):
        message_error(13)
    elif len(color_on) != 3:
        message_error(14)
    elif not isinstance(color_off, tuple):
        message_error(15)
    elif len(color_off) != 3:
        message_error(16)
    elif not isinstance(color_text_on, tuple) and not isinstance(color_text_on, bool):
        message_error(17)
    elif not isinstance(color_text_on, bool):
        if len(color_text_on) != 3:
            message_error(18)
    elif not isinstance(color_text_off, tuple) and not isinstance(color_text_on, bool):
        message_error(19)
    elif not isinstance(color_text_off, bool):
        if len(color_text_off) != 3:
            message_error(20)

    x_1 = location_size[0]
    y = location_size[1]
    width = location_size[2]//2
    height = location_size[3]
    x_2 = location_size[0] + width

    coordinat = coordinat_rect(x_1, y, x_1+width*2, y+height)

    action = event.type

    if action == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            position = event.pos
            if position in coordinat:
                check = not check

    if check == False:
        btn_1 = pg.draw.rect(root, color_on, (x_1, y, width, height))
        btn_2 = pg.draw.rect(root, color_off, (x_2, y, width, height))
    if check == True:
        btn_1 = pg.draw.rect(root, color_off, (x_1, y, width, height))
        btn_2 = pg.draw.rect(root, color_on, (x_2, y, width, height))

    if text_on != False or text_off != False:
        text_on = str(text_on)
        text_off = str(text_off)
        if color_text_on == False:
            if check == True:
                color_text_on = color_on
            else:
                color_text_on = color_off
        if color_text_off == False:
            if check == True:
                color_text_off = color_off
            else:
                color_text_off = color_on

        font = pg.font.SysFont(text_font, text_size)
        button_text = font.render(text_on, True, color_text_on)
        button_text_2 = font.render(text_off, True, color_text_off)
        but_center = button_text.get_rect(center=btn_1.center)
        but_2_center = button_text.get_rect(center=btn_2.center)
        root.blit(button_text, (but_center))
        root.blit(button_text_2, (but_2_center))

    return check
