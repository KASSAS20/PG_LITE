import pygame as pg
from error import message_error
from coordinat_calculate import coordinat_circle, coordinat_rect

pg.init()


def button(root=False, event=False, location_size=(0, 0, 10, 10), color=(0, 0, 0), text=False, text_color=(255, 255, 255), text_font='notosansmonocjkjp', text_size=10):
    # Обработка возможных ошибок аргументов
    if not isinstance(root, pg.surface.Surface) or root == False:
        message_error(1)
    elif not isinstance(color, tuple):
        message_error(2)
    elif len(color) != 3:
        message_error(3)
    elif not isinstance(location_size, tuple):
        message_error(4)
    elif len(location_size) != 4:
        message_error(5)
    elif not isinstance(event, pg.event.Event) or root == False:
        message_error(6)
    elif text_font not in pg.font.get_fonts():
        message_error(7)
    elif not isinstance(text_color, tuple):
        message_error(8)
    elif len(color) != 3:
        message_error(9)
    for i in color:
        if not isinstance(i, int):
            message_error(25)
        if i < 0 or i > 255:
            message_error(25)
    but = pg.draw.rect(root, color, location_size)

    if text != False:  # добавление текста на кнопку
        text = str(text)
        font = pg.font.SysFont(text_font, text_size)
        button_text = font.render(text, True, text_color)
        but_center = button_text.get_rect(center=but.center)
        root.blit(button_text, (but_center))

    action = event.type
    if action == pg.MOUSEBUTTONDOWN:  # Проверка на нажатие по кнопке
        if event.button == 1:
            position = event.pos
            x_1 = location_size[0]
            y_1 = location_size[1]
            x_2 = location_size[0]+location_size[2]
            y_2 = location_size[1]+location_size[3]
            coordinat = coordinat_rect(x_1, y_1, x_2, y_2)
            if position in coordinat:
                return True


def switch(root=False, event=False, location_size=(0, 0, 30, 10), color=(255, 0, 0), color_circle=(0, 0, 0), check=False):
    # обработка возможных ошибок при передаче аргументов
    if not isinstance(root, pg.surface.Surface):
        message_error(1)
    elif not isinstance(color, tuple):
        message_error(2)
    elif len(color) != 3:
        print(color, len(color))
        message_error(3)
    elif not isinstance(location_size, tuple):
        message_error(4)
    elif len(location_size) != 4:
        message_error(5)
    elif not isinstance(event, pg.event.Event):
        message_error(6)
    elif not isinstance(check, bool):
        message_error(10)
    elif not isinstance(color_circle, tuple):
        message_error(21)
    elif len(color_circle) != 3:
        message_error(22)
    for i in color:
        if not isinstance(i, int):
            message_error(25)
        if i < 0 or i > 255:
            message_error(25)
    for i in color_circle:
        if not isinstance(i, int):
            message_error(26)
        if i < 0 or i > 255:
            message_error(26)

    x = location_size[0]
    y = location_size[1]
    height = location_size[3]
    width = location_size[2]-height

    # отрисовка
    pg.draw.circle(
        root, color, (x + height // 2, y + height // 2), height // 2)
    pg.draw.rect(root, color, (x+height//2, y, x+width, y+height))
    pg.draw.circle(
        root, color, (x + height // 2 + width, y + height // 2), height//2)

    # просчёт координат кнопки
    switch_coordinate_1 = coordinat_circle(
        height // 2, x + height // 2, y + height // 2)
    switch_coordinate_2 = coordinat_rect(x+width//2, y, x+width//2 + width, y + height)
    switch_coordinate_3 = coordinat_circle(
        height//2, x + height // 2 + width, y + height // 2)
    switch_coordinate_full = list(
        set(switch_coordinate_1 + switch_coordinate_2 + switch_coordinate_3))

    action = event.type
    if action == pg.MOUSEBUTTONDOWN:  # Проверка на нажатие кнопки
        if event.button == 1:
            position = event.pos
            if position in switch_coordinate_full:
                check = not check
    if check == False:
        pg.draw.circle(
            root, color_circle, (x + height // 2, y + height // 2), height // 2.22)
    if check == True:
        pg.draw.circle(
            root, color_circle, (x + height // 2 + width, y + height // 2), height // 2.22)
    return check

def vertical_switch(root=False, event=False, color=(255, 0, 0), color_circle=(0, 0, 0), location_size=(0, 0, 20, 40), check=False):
    if not isinstance(root, pg.surface.Surface):  # обработка ошибок ввода
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
    for i in color:
        if not isinstance(i, int):
            message_error(25)
        if i < 0 or i > 255:
            message_error(25)
    for i in color_circle:
        if not isinstance(i, int):
            message_error(26)
        if i < 0 or i > 255:
            message_error(26)

    x = location_size[0]
    y = location_size[1]
    width = location_size[2]//2
    height = location_size[3]

    # отрисовка
    pg.draw.circle(
        root, color, (x+width//2, y + height // 2), width//2)
    pg.draw.rect(root, color, (x, y+height//2, width, height))
    pg.draw.circle(
        root, color, (x + width // 2, y + height*1.5), width//2)

    # Просчёт координат
    switch_coordinate_1 = coordinat_circle(
        width//2, x+width//2, y + height // 2)
    switch_coordinate_2 = coordinat_rect(x, y+height//2, x+width, y+height//2+height)
    switch_coordinate_3 = coordinat_circle(
        width//2, x + width // 2, y + height*1.5)
    switch_coordinate_full = list(
        set(switch_coordinate_1 + switch_coordinate_2 + switch_coordinate_3))

    action = event.type
    if action == pg.MOUSEBUTTONDOWN:  # Проверка на нажатие
        if event.button == 1:
            position = event.pos
            if position in switch_coordinate_full:
                check = not check
    if check == False:  # отрисовка "анимации"
        pg.draw.circle(
            root, color_circle, (x+width//2, y + height // 2), width // 2.22)
    if check == True:
        pg.draw.circle(
            root, color_circle, (x + width // 2, y + height+height//2), width // 2.22)

    return check


def switch_box(root=False, event=False, color=(255, 0, 0), color_box=(0, 0, 0), location_size=(0, 0, 0), check=False):
    if not isinstance(root, pg.surface.Surface):  # обработка возможных исключений
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
        message_error(23)
    elif len(color_box) != 3:
        message_error(24)
    for i in color:
        if not isinstance(i, int):
            message_error(25)
        if i < 0 or i > 255:
            message_error(25)
    for i in color_box:
        if not isinstance(i, int):
            message_error(26)
        if i < 0 or i > 255:
            message_error(27)

    x = location_size[0]
    y = location_size[1]
    width = location_size[2]
    height = location_size[3]

    pg.draw.rect(root, color, location_size)  # отрисовка

    action = event.type
    if action == pg.MOUSEBUTTONDOWN:  # проверка на нажатие
        if event.button == 1:
            coordinat = coordinat_rect(x, y, x + width, y + height)
            position = event.pos
            if position in coordinat:
                check = not check
    if check == False:  # отрисовка
        pg.draw.rect(root, color_box, (x+height//20, y+height //
                     20, width//2.1, height-height//10))
    elif check == True:
        pg.draw.rect(root, color_box, (x+width//2, y+height //
                     20, width//2.1, height-height//10))
    return check



def check_box(root=False, event=False, color=(255, 0, 0), color_box=(0, 0, 0), location_size=(0, 0, 50, 50), check=False):
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


def on_off(root = False, event = False, color_on = (255,0,0), color_off=(150,0,0), color_text_on = False, color_text_off = False, location_size = (0,0,60,30), text_on='ON', text_off='OFF', text_font='notosansmonocjkjp', text_size=10, check = False):
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
