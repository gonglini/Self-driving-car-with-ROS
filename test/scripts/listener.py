#!/usr/bin/env python


import rospy
from std_msgs.msg import Int32

global prv_num
global missing_num

prv_num=0
missing_num=[]

sub= rospy.Subscriber('my_topic', Int32,queue_size=1)

def callback(msg):
	global prv_num
	global missing_num
   
	if msg.data != prv_num+1:
        	missing_num.extend(list(range(prv_num + 1, msg.data)))
        	print("		Missed:{0}".format(missing_num))
	prv_num=msg.data
	print("		Received:{0:>3}".format(msg.data))
	
	for i in range(0,msg.data):#2곱하기 0~2곱하기 9 stack 출력
		s=i*2
		print("2*{0}={1}".format(i,s))
		
	
	
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
rospy.init_node('listen', anonymous=False)

sub= rospy.Subscriber('my_topic', Int32,callback,queue_size=1)

    # spin() simply keeps python from exiting until this node is stopped
rospy.spin()
