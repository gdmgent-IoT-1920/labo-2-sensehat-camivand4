from sense_hat import SenseHat
import sys
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from time import sleep
sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():

    def marioStart():
        sense.set_pixel(2,0,255,0,0) #rood hoed
        sense.set_pixel(3,0,255,0,0) #rood hoed
        sense.set_pixel(4,0,255,255,255) # wit hoed
        
        sense.set_pixel(1,1,255,0,0) #rood hoed
        sense.set_pixel(2,1,255,0,0) #rood hoed
        sense.set_pixel(3,1,255,0,0) #rood hoed
        sense.set_pixel(4,1,255,0,0) #rood hoed
        sense.set_pixel(5,1,255,0,0) #rood hoed

        sense.set_pixel(1,2,153,76,0) #bruin haar
        sense.set_pixel(2,2,255,190,139) #lichaamskleur
        sense.set_pixel(3,2,0,0,0) #zwart
        sense.set_pixel(4,2,255,190,139) #lichaamskleur
        
        sense.set_pixel(1,3,153,76,0) #bruin haar
        sense.set_pixel(2,3,255,190,139) #lichaamskleur
        sense.set_pixel(3,3,153,76,0) #bruin haar
        sense.set_pixel(4,3,153,76,0) #bruin haar
        sense.set_pixel(5,3,255,190,139) #lichaamskleur
        
        sense.set_pixel(2,4,153,76,0) #bruin haar
        sense.set_pixel(3,4,255,190,139) #lichaamskleur
        sense.set_pixel(4,4,255,190,139) #lichaamskleur
        
        sense.set_pixel(1,5,255,0,0) #rood kledij
        sense.set_pixel(2,5,250,250,35) #geel knoop
        sense.set_pixel(3,5,35,157,250) #blauw kledij
        sense.set_pixel(4,5,250,250,35) #geel knoop
        sense.set_pixel(5,5,255,0,0) #rood kledij
        
        sense.set_pixel(1,6,255,190,139) #lichaamskleur
        sense.set_pixel(2,6,35,157,250) #blauw kledij
        sense.set_pixel(3,6,35,157,250) #blauw kledij
        sense.set_pixel(4,6,35,157,250) #blauw kledij
        sense.set_pixel(5,6,255,190,139) #lichaamskleur
        
        sense.set_pixel(2,7,153,76,0) #bruin schoenen
        sense.set_pixel(4,7,153,76,0) #bruin schoenen
    
    marioStart()
    
    while True: # programma loopt zolang niet afgebroken
        # x y kleur
        
        def refresh():
            sense.clear()
            
        def jump():
            sense.set_pixel(1,0,255,0,0) #rood hoed
            sense.set_pixel(2,0,255,0,0) #rood hoed
            sense.set_pixel(3,0,255,0,0) #rood hoed
            sense.set_pixel(4,0,255,0,0) #rood hoed
            sense.set_pixel(5,0,255,0,0) #rood hoed

            sense.set_pixel(1,1,153,76,0) #bruin haar
            sense.set_pixel(2,1,255,190,139) #lichaamskleur
            sense.set_pixel(3,1,0,0,0) #zwart
            sense.set_pixel(4,1,255,190,139) #lichaamskleur
        
            sense.set_pixel(1,2,153,76,0) #bruin haar
            sense.set_pixel(2,2,255,190,139) #lichaamskleur
            sense.set_pixel(3,2,153,76,0) #bruin haar
            sense.set_pixel(4,2,153,76,0) #bruin haar
            sense.set_pixel(5,2,255,190,139) #lichaamskleur
        
            sense.set_pixel(2,3,153,76,0) #bruin haar
            sense.set_pixel(3,3,255,190,139) #lichaamskleur
            sense.set_pixel(4,3,255,190,139) #lichaamskleur
        
            sense.set_pixel(1,4,255,0,0) #rood kledij
            sense.set_pixel(2,4,250,250,35) #geel knoop
            sense.set_pixel(3,4,35,157,250) #blauw kledij
            sense.set_pixel(4,4,250,250,35) #geel knoop
            sense.set_pixel(5,4,255,0,0) #rood kledij
        
            sense.set_pixel(1,5,255,190,139) #lichaamskleur
            sense.set_pixel(2,5,35,157,250) #blauw kledij
            sense.set_pixel(3,5,35,157,250) #blauw kledij
            sense.set_pixel(4,5,35,157,250) #blauw kledij
            sense.set_pixel(5,5,255,190,139) #lichaamskleur

            sense.set_pixel(2,6,153,76,0) #bruin schoenen
            sense.set_pixel(4,6,153,76,0) #bruin schoenen
            
        def mario():
            refresh()
            sense.set_pixel(2,0,255,0,0) #rood hoed
            sense.set_pixel(3,0,255,0,0) #rood hoed
            sense.set_pixel(4,0,255,255,255) # wit hoed
        
            sense.set_pixel(1,1,255,0,0) #rood hoed
            sense.set_pixel(2,1,255,0,0) #rood hoed
            sense.set_pixel(3,1,255,0,0) #rood hoed
            sense.set_pixel(4,1,255,0,0) #rood hoed
            sense.set_pixel(5,1,255,0,0) #rood hoed

            sense.set_pixel(1,2,153,76,0) #bruin haar
            sense.set_pixel(2,2,255,190,139) #lichaamskleur
            sense.set_pixel(3,2,0,0,0) #zwart
            sense.set_pixel(4,2,255,190,139) #lichaamskleur
        
            sense.set_pixel(1,3,153,76,0) #bruin haar
            sense.set_pixel(2,3,255,190,139) #lichaamskleur
            sense.set_pixel(3,3,153,76,0) #bruin haar
            sense.set_pixel(4,3,153,76,0) #bruin haar
            sense.set_pixel(5,3,255,190,139) #lichaamskleur
        
            sense.set_pixel(2,4,153,76,0) #bruin haar
            sense.set_pixel(3,4,255,190,139) #lichaamskleur
            sense.set_pixel(4,4,255,190,139) #lichaamskleur
        
            sense.set_pixel(1,5,255,0,0) #rood kledij
            sense.set_pixel(2,5,250,250,35) #geel knoop
            sense.set_pixel(3,5,35,157,250) #blauw kledij
            sense.set_pixel(4,5,250,250,35) #geel knoop
            sense.set_pixel(5,5,255,0,0) #rood kledij
        
            sense.set_pixel(1,6,255,190,139) #lichaamskleur
            sense.set_pixel(2,6,35,157,250) #blauw kledij
            sense.set_pixel(3,6,35,157,250) #blauw kledij
            sense.set_pixel(4,6,35,157,250) #blauw kledij
            sense.set_pixel(5,6,255,190,139) #lichaamskleur
        
            sense.set_pixel(2,7,153,76,0) #bruin schoenen
            sense.set_pixel(4,7,153,76,0) #bruin schoenen
                

        def pushed_up(event):
            if event.action == ACTION_PRESSED:
                refresh()
                jump()
                sleep(1)
                refresh()
                mario()


                
        sense.stick.direction_up = pushed_up
        
                
try:
    main()
except (keyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen v/d matrix')
    sense.clear()
    sys.exit(0)
    