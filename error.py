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
    elif num == 13:
        message = 'the color_on of the button should be transmitted as a tuple'
    elif num == 14:
        message = 'the color_on must be transmitted in RGB format'
    elif num == 15:
        message = 'the color_off of the button should be transmitted as a tuple'
    elif num == 16:
        message = 'the color_off must be transmitted in RGB format'
    elif num == 17:
        message = 'the color_text_on of the button should be transmitted as a tuple'
    elif num == 18:
        message = 'the color_text_on must be transmitted in RGB format'
    elif num == 19:
        message = 'the color_text_off of the button should be transmitted as a tuple'
    elif num == 20:
        message = 'the color_text_off must be transmitted in RGB format'
    elif num == 21:
        message = 'the color_circle of the button should be transmitted as a tuple'
    elif num == 22:
        message = 'the color_ciecle must be transmitted in RGB format'
    elif num == 23:
        message = 'the color_box of the button should be transmitted as a tuple'
    elif num == 24:
        message = 'the color_box must be transmitted in RGB format'
        
    print(f'\nEROOR {num} : {message}\n')
    pg.quit()
    exit()
