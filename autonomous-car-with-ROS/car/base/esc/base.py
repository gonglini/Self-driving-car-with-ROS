import time   
import keyboard
import os
from adafruit_servokit import ServoKit   

MIN_IMP  =500
MAX_IMP  =2500
MIN_ANG  =0
MAX_ANG  =180

pca = ServoKit(channels=16)


def main():
    os.system('clear')
    pca.servo[1].set_pulse_width_range(MIN_IMP , MAX_IMP)
    pca.servo[1].angle = 90


    time.sleep(0.5)
    servomove();
    print("done")



def servomove():
    while 1:



        if keyboard.is_pressed('w'):

            if pca.servo[1].angle <= 131:
                print("servo angle: %d" %pca.servo[1].angle)
                pca.servo[1].angle +=1
                time.sleep(0.15)

            else:
                print("can't move servo anymoore")
                time.sleep(0.15)

        if keyboard.is_pressed('e'):

            if pca.servo[1].angle >= 0:

                print("servo angle: %d" %pca.servo[1].angle)
                pca.servo[1].angle -=3
                time.sleep(0.15)
 
            else:
                print("can't move servo anymoore")
                time.sleep(0.15)

        if keyboard.is_pressed('q'):
            os.system('clear')
            return False

main()

