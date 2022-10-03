import os
import cv2 
import time
import keyboard
import numpy as np
import tensorflow as tf
from adafruit_servokit import ServoKit   
from tensorflow.keras.models import load_model

MIN_IMP  =500
MAX_IMP  =2500
MIN_ANG  =0
MAX_ANG  =180

pca = ServoKit(channels=16)

def img_preprocess(frame):
    height , _, _=frame.shape
    save_image = frame[int(height/2):,:,:]  
    save_image = cv2.cvtColor(save_image, cv2.COLOR_BGR2YUV) 
    save_image =cv2.GaussianBlur(save_image ,(3,3),0)
    save_image = cv2.resize(save_image, (200, 66))
    save_image = save_image/255
    
    return save_image


def cam():
    camera=cv2.VideoCapture(-1)
    camera.set(4,1024)
    camera.set(3,768)

    model_path = '/home/gonglini/2lab/data/lane_navigation_final.h5'
    model = load_model(model_path)


    while (camera.isOpened()):

        keyValue = cv2.waitKey(1)
        
        if cv2.waitKey(1) ==ord('q'):
            break
        
        ret,frame=camera.read() 
        frame = cv2.flip(frame,1)
        cv2.imshow('original',frame)
        
        preprocessed = img_preprocess(frame)

        cv2.imshow('pre',preprocessed)

        X = np.asarray([preprocessed])
        steering_angle= int(model.predoct(X)[0])
        print("predict angle: ", steering_angle)

        ''' if steering_angle >= 85 and steering_angle <= 95:
            print('go')
        elif steering_angle > 96:
            print('right')
        elif steering_angle < 84:
            print('left')'''

    cv2.destroyAllWindows()

def main():
    os.system('clear')
    pca.servo[1].set_pulse_width_range(MIN_IMP , MAX_IMP)
    pca.servo[1].angle = 98
    pca.servo[0].set_pulse_width_range(MIN_IMP , MAX_IMP)
    pca.servo[0].angle = 100

    time.sleep(0.2)
    cam()


    '''  if keyboard.is_pressed('j'):
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
            return False    '''


if __name__ =='__main__':
    main()

    if keyboard.is_pressed('w'):

        if pca.servo[1].angle <= 110:
            print("car speed %d" %pca.servo[1].angle)
            pca.servo[1].angle +=1
            time.sleep(0.1)

        else:
            print("can't move faster anymore")
            time.sleep(0.1)

    if keyboard.is_pressed('s'):

        if pca.servo[1].angle >= 70:

            print("car speed %d" %pca.servo[1].angle)
            pca.servo[1].angle -=1
            time.sleep(0.1)
        else:
            print("can't move slower anymore")
            time.sleep(0.1)
