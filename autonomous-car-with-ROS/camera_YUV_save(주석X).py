#설명
#기존의 camera_cv2_yuv에 인식되는 카메라 영상을 설정한 time값에 맞춰 지정된 경로에 사진을 저장함


from re import S
import cv2 
import time
import numpy as np


def main():
    camera=cv2.VideoCapture(-1)
    camera.set(4,1024)
    camera.set(3,768)

    i = 0

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

        cv2.imwrite("video/test_%05d.jpg"% i, save_image)
       
      #  cv2.imwrite("test.jpg", save_image)
        i += 1

        time.sleep(0.1)

        if cv2.waitKey(1) ==ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ =='__main__':
    main()
