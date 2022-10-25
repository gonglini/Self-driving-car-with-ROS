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
    pca.servo[0].set_pulse_width_range(MIN_IMP , MAX_IMP)
    pca.servo[0].angle = 100

    print("""
Servo Control Module for move Servo.
Enter one of the following options:
-----------------------------
    q     w     e

     a     s     d

q: Quit current command mode
a: move servo angle: 130
s: move servo angle:100
d: move servo angle: 70
w: move servo angle: +5
e: move servo angle: -5
 

anything else : Prompt again for command

CTRL-C to quit
""")

    time.sleep(0.5)
    servomove();
    print("done")



def servomove():
    while 1:
        if keyboard.is_pressed('w'):
            print("move servo angle: 105")
            pca.servo[1].angle = 105
            time.sleep(0.1) 
        if keyboard.is_pressed('d'):
            print("move servo angle:95")
            pca.servo[1].angle = 95
            time.sleep(0.1)      

        if keyboard.is_pressed('s'):
            print("move servo angle: 84")
            pca.servo[1].angle = 84
            time.sleep(0.1) 

        if keyboard.is_pressed('e'):

            if pca.servo[1].angle <= 110:
                print("servo angle: %d" %pca.servo[1].angle)
                pca.servo[1].angle +=1
                time.sleep(0.1)

            else:
                print("can't move servo anymoore")
                time.sleep(0.1)

        if keyboard.is_pressed('r'):

            if pca.servo[1].angle >= 70:

                print("servo angle: %d" %pca.servo[1].angle)
                pca.servo[1].angle -=1
                time.sleep(0.1)
            else:
                print("can't move servo anymoore")
                time.sleep(0.1)


        if keyboard.is_pressed('j'):
            print("move servo angle: 130")
            pca.servo[0].angle = 130
            time.sleep(0.15) 

        if keyboard.is_pressed('k'):
            print("move servo angle:100")
            pca.servo[0].angle = 100
            time.sleep(0.15)      

        if keyboard.is_pressed('l'):
            print("move servo angle: 72")
            pca.servo[0].angle = 72
            time.sleep(0.15)
 
        if keyboard.is_pressed('q'):
            os.system('clear')
            return False


main()

