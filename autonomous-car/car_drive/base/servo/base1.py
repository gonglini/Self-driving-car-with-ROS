import time   
from adafruit_servokit import ServoKit   

MIN_IMP  =500
MAX_IMP  =2500
MIN_ANG  =0
MAX_ANG  =180

pca = ServoKit(channels=16)


def main():

    print("wait for initialize...")
    pca.servo[0].set_pulse_width_range(MIN_IMP , MAX_IMP)
    time.sleep(0.5)
    servomove();
    print("done")



def servomove():
    for i in range(0,3):
        print("working count",i+1)

        pca.servo[0].angle = 180
        time.sleep(0.6)

        pca.servo[0].angle = 0
        time.sleep(0.6)

main()
