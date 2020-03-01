from sense_hat import SenseHat
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from time import sleep
import sys
import random
sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
    
    sense.show_message("press up")

    while True: # programma loopt zolang niet afgebroken
        
        color = 255,0,0
        timeout = 0.5
        
        
        def square1():
            sense.set_pixel(3,3,color)
            sense.set_pixel(4,4,color)
            sense.set_pixel(3,4,color)
            sense.set_pixel(4,3,color)
            sleep(timeout)
            refresh()
            square2()
            
        def square2():
            a = 5
            b = 2
            
            for c in range(2,6):
                sense.set_pixel(a,c,color)
                sense.set_pixel(b,c,color)
                sense.set_pixel(c,a,color)
                sense.set_pixel(c,b,color)
            sleep(timeout)
            refresh()
            square3()
            
        def square3():
            a = 6
            b = 1
            
            for c in range(1,7):
                sense.set_pixel(a,c,color)
                sense.set_pixel(b,c,color)
                sense.set_pixel(c,a,color)
                sense.set_pixel(c,b,color)
            sleep(timeout)
            refresh()
            square4()

        def square4():
            a = 7
            b = 0
            
            for c in range(0,8):
                sense.set_pixel(a,c,color)
                sense.set_pixel(b,c,color)
                sense.set_pixel(c,a,color)
                sense.set_pixel(c,b,color)
            sleep(timeout)
            refresh()
            square1()
            
            
        
        # start
        def pushed_up(event):
            if event.action == ACTION_PRESSED:
                square1()

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
    

