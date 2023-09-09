import pygame as pg


def message_error(num):
    if num == 1:
        message = 'root is specified incorrectly'
    elif num == 2:
        message = 'the color of the button should be transmitted as a tuple'
    elif num == 3:
        message = 'the color must be transmitted in RGB format'
    elif num == 4:
        message = 'the location_size of the button should be transmitted as a tuple'
    elif num == 5:
        message = 'location_size must be passed in the format (x, y, width, height)'
    elif num == 6:
        message = 'event is specified incorrectly'
    elif num == 7:
        message = 'The font you entered was not found on your PC'
    elif num == 8:
        message = 'the text_color of the button should be transmitted as a tuple'
    elif num == 9:
        message = 'the text_color must be transmitted in RGB format'
    elif num == 10:
        message = 'A non-Boolean value was passed to the check parameter'
    elif num == 11:
        message = 'the color_box of the button should be transmitted as a tuple'
    elif num == 12:
        message = 'the box_color must be transmitted in RGB format'
    print(f'\nEROOR {num} : {message}\n')
    pg.quit()
    exit()
