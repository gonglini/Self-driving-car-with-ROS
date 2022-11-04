#!/usr/bin/env python3 

import rospy
from std_msgs.msg import Int32

rospy.init_node('talk',anonymous=False)
pub=rospy.Publisher('my_topic', Int32, queue_size=10)
rate=rospy.Rate(2)

count = 1

while(pub.get_num_connections()==0):#퍼블리셔 객체와 연결된 커넥션의 개수를 반환
	pass
while not rospy.is_shutdown() and count<=10:
	pub.publish(count)
	print("Sent:{0:>3}".format(count))#0에 오는 format값을 오른 정렬로 3자리로 표현한다라는 뜻
	count+=1
	rate.sleep()
		
