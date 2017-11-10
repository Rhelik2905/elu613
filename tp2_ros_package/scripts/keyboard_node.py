#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from getch import *

def talker():
    pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=1)
    rospy.init_node('keyboard_inputs_node', anonymous=True)
    linspeed=0.1
    msg=Twist()
    while not rospy.is_shutdown():
    	char = getch()
    	if char in [str(x) for x in range(1,10)]:
    		linspeed = float(char)/10
    	elif char == 't' or char == 'T':
    		msg.linear.x=linspeed
    		msg.angular.z=0.0
    		rospy.loginfo(msg)
    		pub.publish(msg)
    	elif char == 'g' or char == 'G' :
    		msg.linear.x=-linspeed
    		msg.angular.z=0.0
    		rospy.loginfo(msg)
    		pub.publish(msg)
    	elif char == 'h' or char == 'H':
    		msg.linear.x=0.0
    		msg.angular.z=-1.0
    		rospy.loginfo(msg)
    		pub.publish(msg)
    	elif char == 'f' or char == 'F':
    		msg.linear.x=0.0
    		msg.angular.z=1.0
    		rospy.loginfo(msg)
    		pub.publish(msg)



   

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
