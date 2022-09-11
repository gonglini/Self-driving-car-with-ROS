from re import S
import cv2 
import time
import numpy as np

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

if __name__ =='__main__':
    main()
