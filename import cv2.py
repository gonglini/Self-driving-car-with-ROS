
import cv2 
import numpy as np





def main():
    camera=cv2.VideoCapture(0)
    camera.set(3,520)
    camera.set(4,360)

    while True:
        ret,frame=camera.read() #read는 무조건 2개의 값을 반환한다, ret은 reterval의 약자로 값을 입력받아 True,False로 반환한다.
        # frame은 읽어온 카메라 영상을 담는 변수로 선언
        
        slicing=frame[220:520, 0:360] 
        #문자열 슬라이싱과 같이 frame을 픽셀 단위로 자를 수 있다/
        #세로 데이터를 220~520까지 데이터를 쓰고  가로 데이터는 0~360까지 데이터를 씀(다 쓴단 의미져) 
                
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(gray,(5,5),0)
        ret,thresh=cv2.threshold(blur,130,255,cv2.THRESH_BINARY_INV) #threshold:이미지 BGR에 이진화 처리를해 흑 백을 바꾼다. 
        #영상or이미지,임계점,최대점,cv2.THRESH_BINARY_INV
        #1=white(),0=black
        q
        #노이즈 제거 모폴리지기법
        mask=cv2.erode(thresh,None,iterations=2)
        #erode(이미지변수,필터가 적용되어 저장될 이미지 변수, 반복할 횟수,)
        # object의 영역을 침식시켜 줄여버림(압축) 
        # 원리는 필터를 적용하려는 중심 픽셀에 커널을 가중하여 가장 작은 값을 찾고 그 중 가장 작은 값을
        # 필터의 중심 픽셀에 적용, 이진화되어서 픽셀엔 0,255밖에 없으니 0주위의 값은 커널 크기만큼 0으로 바뀌어 output됨


        #팽창연산
        mask=cv2.dilate(mask,None,iterations=2)
        #eride와 정반대로 255주위 픽셀을 가중치된 커널의 크기만큼 255로 바꾸어 팽창연산해버림
        
        #윤곽선 검출,contour(등고선)을 출력,contour:동일한 픽셀값을 가지는 영역의 경계선 정보
        contours=cv2.findContours(mask.copy(),1,cv2.CHAIN_APPROX_NONE)
        #findContours(입력영상변수.non-zero픽셀을 객체로 간주(white만 객체로 간주) 
        #             (1: 외곽선 개수, CHAIN_APPROX_NONE:모든 컨투어 포인트를 반환)   
        
        
    
        
        cv2.imshow('mask',mask)










        if cv2.waitKey(1) ==ord('q'):
            break


    cv2.destroyAllWindows()
 
        


if __name__ =='__main__':
    main()
            
            








 













































            

