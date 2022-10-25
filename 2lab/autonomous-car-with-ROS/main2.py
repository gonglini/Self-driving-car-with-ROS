import os
import cv2 
import time
import keyboard
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model


def img_preprocess(frame):
    height , _, _=frame.shape
    save_image = frame[int(height/2):,:,:]  
    save_image = cv2.cvtColor(save_image, cv2.COLOR_BGR2YUV) 
    save_image =cv2.GaussianBlur(save_image ,(3,3),0)
    save_image = cv2.resize(save_image, (200, 66))
    save_image = save_image/255
    
    return save_image


def cam():
#    camera=cv2.VideoCapture(2)
  #  camera.set(4,1024)
  #  camera.set(3,768)

    model_path = '/home/gonglini/2lab/data/lane_navigation_final.h5'
    model = load_model(model_path)


    while (True):

        keyValue = cv2.waitKey(1)
        
        if cv2.waitKey(1) ==ord('q'):
           break
        
    #    ret,frame=camera.read() 
        frame = cv2.imread('/home/gonglini/2lab/data/car.png',cv2.IMREAD_UNCHANGED)
        cv2.imshow('original',frame)
        
        preprocessed = img_preprocess(frame)

        cv2.imshow('pre',preprocessed)

        X = np.asarray([preprocessed])
        steering_angle= int(model.predict(X)[0])
        print("predict angle: ", steering_angle)
        time.sleep(0.2)



    cv2.destroyAllWindows()

def main():
    os.system('clear')

    cam()


    ''' 
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
            return False    '''


if __name__ =='__main__':
    main()

 
