import time   
import keyboard
import os
from adafruit_servokit import ServoKit   

MIN_IMP  =500
MAX_IMP  =2500
MIN_ANG  =70
MAX_ANG  =110

pca = ServoKit(channels=16)


def main():
    os.system('clear')
    pca.servo[1].set_pulse_width_range(MIN_IMP , MAX_IMP)
    pca.servo[1].angle = 95


    time.sleep(0.5)
    servomove();
    print("done")



def servomove():
    while 1:
        if keyboard.is_pressed('a'):
            print("move servo angle: 105")
            pca.servo[1].angle = 105
            time.sleep(0.1) 
        if keyboard.is_pressed('s'):
            print("move servo angle:95")
            pca.servo[1].angle = 95
            time.sleep(0.1)      

        if keyboard.is_pressed('d'):
            print("move servo angle: 84")
            pca.servo[1].angle = 84
            time.sleep(0.1) 

        if keyboard.is_pressed('w'):

            if pca.servo[1].angle <= 110:
                print("servo angle: %d" %pca.servo[1].angle)
                pca.servo[1].angle +=1
                time.sleep(0.1)

            else:
                print("can't move servo anymoore")
                time.sleep(0.1)

        if keyboard.is_pressed('e'):

            if pca.servo[1].angle >= 70:

                print("servo angle: %d" %pca.servo[1].angle)
                pca.servo[1].angle -=1
                time.sleep(0.1)
 
            else:
                print("can't move servo anymoore")
                time.sleep(0.1)

        if keyboard.is_pressed('q'):
            os.system('clear')
            return False


main()

