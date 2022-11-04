#!/usr/bin/env python3 

import rospy
from std_msgs.msg import Int32
import os
import cv2 
import time
import keyboard
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model
 
rospy.init_node('talk',anonymous=False)
pub=rospy.Publisher('my_topic', Int32, queue_size=10)
rate=rospy.Rate(2)

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
        
     
        ret,frame=camera.read() 
        frame = cv2.flip(frame,1)
        cv2.imshow('original',frame)
        
        preprocessed = img_preprocess(frame)

        cv2.imshow('pre',preprocessed)

        X = np.asarray([preprocessed])
        steering_angle= int(model.predict(X)[0])


        if(pub.get_num_connections()==0):#퍼블리셔 객체와 연결된 커넥션의 개수를 반환
            pass
            
        pub.publish(steering_angle)
        print("Sent angle => ", steering_angle)

        time.sleep(0.1)

        if cv2.waitKey(1) ==ord('q'):
 
           break

    cv2.destroyAllWindows()

if __name__ =='__main__':
    os.system('clear')

    cam()






		
