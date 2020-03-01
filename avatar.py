from sense_hat import SenseHat
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from time import sleep
import sys
import random
sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
    
    #sense.show_message("press up")

    while True: # programma loopt zolang niet afgebroken
        x = 0
        y = 0
        
        randomValue = random.randint(0,1)

        
        
        def avatar():
            randomColor = random.randint(0,255),random.randint(0,255),random.randint(0,255)
                

            for y in range(8):         
                for p in range(4):
                    if randomValue == 1:
                        sense.set_pixel(p,y,randomColor)
                        sense.set_pixel(p+4,y,randomColor)
                    elif randomValue == 0:
                        sense.set_pixel(p,y,0,0,0)
                        sense.set_pixel(p+4,y,0,0,0)
            sleep(5)
            avatar()

        
        # start
        def pushed_up(event):
            if event.action == ACTION_PRESSED:
                avatar()

        sense.stick.direction_up = pushed_up

        
        # clear everything
        def refresh():
            sense.clear()
        
        def pushed_down(event):
            if event.action == ACTION_PRESSED:
                refresh()

        sense.stick.direction_down = pushed_down
    
try:
    main()
except (keyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen v/d matrix')
    sense.clear()
    sys.exit(0)
    

