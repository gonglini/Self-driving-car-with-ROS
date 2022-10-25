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
    pca.servo[0].set_pulse_width_range(MIN_IMP , MAX_IMP)

    print("""
Servo Control Module for move Servo.
Enter one of the following options:
-----------------------------
    q     w     e

     a     s     d

q: Quit current command mode
a: move servo angle: 180
s: move servo angle: 90
d: move servo angle: 0
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
        key = keyboard.read_key() 
        if key == "a":
            print("move servo angle: 180")
            pca.servo[0].angle = 180
            time.sleep(0.2) 
        if key == "s":
            print("move servo angle: 90")
            pca.servo[0].angle = 90
            time.sleep(0.2)      

        if key == "d":
            print("move servo angle: 0")
            pca.servo[0].angle = 0
            time.sleep(0.2)

        if key == "w":
            pca.servo[0].angle +=5
            print("servo angle: %d" %pca.servo[0].angle)

        if key == "e":
            pca.servo[0].angle -=5
            print("servo angle: %d" %pca.servo[0].angle)

        if key == "q":
            os.system('clear')
            return False

main()

