#!/usr/bin/env python  
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	rospy.init_node('turtle2_pose')
	pub=rospy.Publisher('/turtle2/pose',Twist,queue_size=0)
	t=Twist()
	t.linear.x=12.2
	t.linear.y=12.2
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		pub.publish(t)
		rate.sleep()
	rospy.spin()