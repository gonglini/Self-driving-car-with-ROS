

import rospy
from std_msgs.msg import String
import os
import cv2 
import time
import keyboard
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model
 
sub= rospy.Subscriber('detect_inform', String,queue_size=1)


def callback(msg):

        print("Recieved object => ",format(msg.data))
        if msg.data == 'car':
            print("Car is detected" , end = "")
        return msg
	#[int(height):,:,:]     
def img_preprocess(frame):
    height , _, _=frame.shape
    save_image = frame 
    save_image = cv2.cvtColor(save_image, cv2.COLOR_BGR2YUV) 
    save_image =cv2.GaussianBlur(save_image ,(3,3),0)
  #  _,save_image=cv2.threshold(save_image,170,255,cv2.THRESH_BINARY_INV)
  #  save_image =cv2.dilate(save_image ,None,iterations=2)
    #cv2.imshow('original',save_image)
    save_image = cv2.resize(save_image, (200, 66))
    save_image = save_image/255
    
    return save_image


def cam():
    camera = cv2.VideoCapture('/home/yongs/Downloads/IMG_0094.MOV')
    camera.set(4,1024)
    camera.set(3,768)

    model_path = '/home/yongs/2lab/data/lane_navigation_final.h5'
    model = load_model(model_path)


    while (camera.isOpened()):

        keyValue = cv2.waitKey(1)
        
     
        ret,frame=camera.read() 
        frame = cv2.flip(frame,1)

        
        preprocessed = img_preprocess(frame)

        cv2.imshow('pre',preprocessed)

        X = np.asarray([preprocessed])
        steering_angle= int(model.predict(X)[0]) -24
           
        print("Detected angle => ", steering_angle )

        rospy.init_node('listen', anonymous=False)

        sub= rospy.Subscriber('detect_inform', String,callback,queue_size=1)
        time.sleep(0.0395)

        if cv2.waitKey(1) ==ord('q'):
 
            break



    cv2.destroyAllWindows()

if __name__ =='__main__':
    os.system('clear')

    cam()





		
