import pygame as pg
pg.init()


def message_error(num, message):
    print(f'\nEROOR {num} : {message}\n')
    pg.quit()
    exit()


def button(root, color, location_size, event, text=False, text_color = False, text_font = False, text_size = 10):
    if not isinstance(root, pg.surface.Surface):
        message_error('1', 'root is specified incorrectly')
    elif not isinstance(color, tuple):
        message_error(
            '2', 'the color of the button should be transmitted as a tuple')
    elif len(color) != 3:
        message_error('3', 'the color must be transmitted in RGB format')
    elif not isinstance(location_size, tuple):
        message_error(
            '4', 'the location_size of the button should be transmitted as a tuple')
    elif len(location_size) != 4:
        message_error(
            '5', 'location_size must be passed in the format (x, y, width, height)')
    elif not isinstance(event, pg.event.Event):
        message_error('6', 'event is specified incorrectly')
    
    


    action = event.type
    but = pg.draw.rect(root, color, location_size)

    if text != False:
        text = str(text)
        if text_color == False:
            text_color = (255-color[0], 255-color[1], 255-color[2])
        if text_font == False:
            text_font = 'notosansmonocjkjp'

        elif text_color not in pg.font.get_fonts():
            message_error('7', 'The font you entered was not found on your PC')
        elif not isinstance(text_color, tuple):
            message_error(
            '8', 'the text_color of the button should be transmitted as a tuple')
        elif len(color) != 3:
            message_error('9', 'the text_color must be transmitted in RGB format')

        font = pg.font.SysFont(text_font, text_size)
        button_text = font.render(text, True, text_color)
        but_center = button_text.get_rect(center=but.center)
        root.blit(button_text, (but_center))

        

    if action == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            position = event.pos
            if position[0] > location_size[0]-1 and position[0] < location_size[0]+location_size[2]+1 and position[1] > location_size[1]-1 and position[1] < location_size[1] + location_size[3] + 1:
                return True
