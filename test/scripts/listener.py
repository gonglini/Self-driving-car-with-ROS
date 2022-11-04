#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

sub= rospy.Subscriber('my_topic', Int32,queue_size=1)

def callback(msg):

	print("Recieved angle => ",format(msg.data))
	
	if msg.data > 40:
	    print(" hi!!!")
3

rospy.init_node('listen', anonymous=False)

sub= rospy.Subscriber('my_topic', Int32,callback,queue_size=1)

rospy.spin()
