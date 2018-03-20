from time import sleep
import itertools
import random

colours = 'Red Green Amber'.split()
rotation = itertools.cycle(colours)

def rg_timer():
    return random.randint(3, 7)

def light_rotation(rotation):
    for colour in rotation:
        if colour == 'Amber':
            print('Caution! The light is %s' % colour)
            sleep(3)
        elif colour == 'Red':
            print('STOP! The light is %s' % colour)
            sleep(rg_timer())
        else:
            print('Go! The light is %s' % colour)
            sleep(rg_timer())

if __name__ == '__main__':
    light_rotation(rotation)
