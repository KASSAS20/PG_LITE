import pygame as pg
pg.init()


def button(root, color, location_size, event, text=False, text_color = False, text_font = False, text_size = 10):
    action = event.type
    but = pg.draw.rect(root, color, location_size)

    if text != False:
        if text_color == False:
            text_color = (255-color[0], 255-color[1], 255-color[2])
        if text_font == False:
            text_font = 'notosansmonocjkjp'

        font = pg.font.SysFont(text_font, text_size)
        button_text = font.render(text, True, text_color)
        but_center = button_text.get_rect(center=but.center)
        root.blit(button_text, (but_center))

        

    if action == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            position = event.pos
            if position[0] > location_size[0]-1 and position[0] < location_size[0]+location_size[2]+1 and position[1] > location_size[1]-1 and position[1] < location_size[1] + location_size[3] + 1:
                return True
