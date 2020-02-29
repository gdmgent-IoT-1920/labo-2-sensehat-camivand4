import time
import random
from sense_hat import SenseHat
# initialiseer
sense = SenseHat()
# rotate 180 degrees
sense.set_rotation(180)
# toon een bericht

# message, snelheid, letterkleur, achtergrondkleur

nmd = ['N', 'M', 'D']

while True:
    randomColor = random.randint(0,255),random.randint(0,255),random.randint(0,255)

    for i in nmd:
        sense.show_letter(str(i), randomColor)
        time.sleep(1)
    time.sleep(3)
    
try:
    main()
except (keyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen v/d matrix')
    sense.clear()
    sys.exit(0)
    