# control + c stop de code 
from sense_hat import SenseHat
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from time import sleep
import sys
import random
sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
    
    # sense.show_message("press up")

    while True: # programma loopt zolang niet afgebroken
        randomColor = random.randint(0,255),random.randint(0,255),random.randint(0,255)

        x = 0
        y = 0
        amountOfTime = 0.1
        
        def pixelColor():
            for y in range(8):
                print(y)
                sleep(amountOfTime)
                sense.set_pixel(x,y,randomColor)
            
                for p in range(8):
                    print(p)
                    sleep(amountOfTime)
                    sense.set_pixel(p,y,randomColor)
            refresh()
            pixelColor()
        
        # start
        def pushed_up(event):
            if event.action == ACTION_PRESSED:
                pixelColor()

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
    
