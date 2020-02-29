from time import sleep
from random import randint
from math import floor
from sense_hat import SenseHat
# initialiseer
sense = SenseHat()
# rotate 180 degrees
sense.set_rotation(180)
# toon een bericht

def pick_random_colour():
    random_red = randint(0, 255)
    random_green = randint(0,255)
    random_blue = randint(0, 255)
    return (random_red, random_green, random_blue)

def pick_random_colour2():
    random_red = floor(randint(0, 255)*0.1)
    random_green = floor(randint(0,255)*0.1)
    random_blue = floor(randint(0, 255)*0.1)
    return [random_red, random_green, random_blue]

while True:
    sense.show_message("Hello! We are New Media Development:", text_colour=pick_random_colour(), back_colour=pick_random_colour2())
    
try:
    main()
except (keyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen v/d matrix')
    sense.clear()
    sys.exit(0)
    