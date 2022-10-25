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
    pca.servo[1].angle = 95
    pca.servo[0].set_pulse_width_range(MIN_IMP , MAX_IMP)
    pca.servo[0].angle = 100

    print("""


Servo Control Module for move Servo.
Enter one of the following options:
-------------------------------------------
    q     w     e    r

           s     d         j      k      k

q: Quit current command mode
w: move foward
s: move backward
e: move faster
r: move slower
d: stop
l: move servo right
k: move servo straight
j: move servo left
 

anything else : Prompt again for command

CTRL-C to quit
""")

    time.sleep(0.2)
    servomove();
    print("done")



def servomove():
    while 1:
        if keyboard.is_pressed('w'):
            print("move foward")
            pca.servo[1].angle = 105
            time.sleep(0.1) 
        if keyboard.is_pressed('d'):
            print("stop")
            pca.servo[1].angle = 95
            time.sleep(0.1)      

        if keyboard.is_pressed('s'):
            print("move backward")
            pca.servo[1].angle = 84
            time.sleep(0.1) 

        if keyboard.is_pressed('e'):

            if pca.servo[1].angle <= 110:
                print("car speed %d" %pca.servo[1].angle)
                pca.servo[1].angle +=1
                time.sleep(0.1)

            else:
                print("can't move faster anymore")
                time.sleep(0.1)

        if keyboard.is_pressed('r'):

            if pca.servo[1].angle >= 70:

                print("car speed %d" %pca.servo[1].angle)
                pca.servo[1].angle -=1
                time.sleep(0.1)
            else:
                print("can't move slower anymore")
                time.sleep(0.1)


        if keyboard.is_pressed('j'):
            print("move servo right")
            pca.servo[0].angle = 130
            time.sleep(0.15) 

        if keyboard.is_pressed('k'):
            print("move servo straight")
            pca.servo[0].angle = 100
            time.sleep(0.15)      

        if keyboard.is_pressed('l'):
            print("move servo left")
            pca.servo[0].angle = 72
            time.sleep(0.15)
 
        if keyboard.is_pressed('q'):
            os.system('clear')
            return False


main()

