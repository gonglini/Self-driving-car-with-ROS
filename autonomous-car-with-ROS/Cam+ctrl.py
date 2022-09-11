

#해당 코드는 자동차 위에서만 작동됩니다 하드웨어설계가 되어있지않으면 i2c인식 오류로 인해 작동하지 않음


from adafruit_servokit import ServoKit   
import numpy as np  
from re import S
import keyboard
import time
import cv2 
import os

MIN_IMP  =500
MAX_IMP  =2500
MIN_ANG  =0
MAX_ANG  =180

pca = ServoKit(channels=16)

def main():
    camera=cv2.VideoCapture(0)
    camera.set(4,1024)
    camera.set(3,768)

    while (camera.isOpened()):
        ret,frame=camera.read() 
        frame = cv2.flip(frame,1)
        cv2.imshow('frame',frame)
        
        height , _, _=frame.shape
        save_image = frame[int(height/2):,:,:]  
        save_image = cv2.cvtColor(save_image, cv2.COLOR_BGR2YUV)  
        cv2.imshow('mask1',save_image)
        save_image =cv2.GaussianBlur(save_image ,(5,5),0)
        save_image =cv2.dilate(save_image ,None,iterations=2)
        save_image = cv2.resize(save_image, (200, 66))
        cv2.imshow('mask3',save_image )

        if cv2.waitKey(1) ==ord('q'):
            break
    cv2.destroyAllWindows()


def control():
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
    servomove()
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

if __name__ =='__main__':
    main()
    control()
