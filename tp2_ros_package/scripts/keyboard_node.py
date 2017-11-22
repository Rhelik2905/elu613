#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from getch import *

def talker():
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=1)
    rospy.init_node('keyboard_inputs_node', anonymous=True)
    linspeed=rospy.get_param("linspeed",default=0.1)
    msg=Twist()
    while not rospy.is_shutdown():
    	char = getch() #retrieves the value of the pressed key.
        linspeed=rospy.get_param("linspeed",default=0.1)
        # We ask the robot to do different movements accordingly to the pressed key.
    	if char in [str(x) for x in range(1,10)]: # If the key is 1-9 we set up the linear speed accordingly.
            new_linspeed=float(char)/10
            rospy.set_param("linspeed",new_linspeed)
            rospy.set_param("fwd_linear_speed_x", new_linspeed) 
            rospy.set_param("bckwd_linear_speed_x", -new_linspeed)
    	elif char == 't' or char == 'T': # If the key is 'T' (or 't') we ask the robot to go straight forward at the set up linear speed.
    		msg.linear.x=rospy.get_param("fwd_linear_speed_x",default=0.0)
    		msg.angular.z=rospy.get_param("fwd_angular_speed_z",default=0.0)
    		rospy.loginfo(msg)
    		pub.publish(msg) 
    	elif char == 'g' or char == 'G' : # If the key is 'G' (or 't') we ask the robot to go backward at the set up linear speed.
            msg.linear.x=rospy.get_param("bckwd_linear_speed_x",default=0.0)
            msg.angular.z=rospy.get_param("bckwd_angular_speed_z",default=0.0)
            rospy.loginfo(msg)
            pub.publish(msg)
    	elif char == 'h' or char == 'H': # If the key is 'H' (or 'h') we ask the robot to do a clockwise rotation at 0.5 m/s of angular speed.
            msg.linear.x=rospy.get_param("clw_linear_speed_x",default=0.0)
            msg.angular.z=rospy.get_param("clw_angular_speed_z",default=0.0)
            rospy.loginfo(msg)
            pub.publish(msg)
    	elif char == 'f' or char == 'F': # If the key is 'F' (or 'f') we ask the robot to do a counter-clockwise rotation at 0.5 m/s of angular speed.
            msg.linear.x=rospy.get_param("counclw_linear_speed_x",default=0.0)
            msg.angular.z=rospy.get_param("counclw_angular_speed_z",default=0.0)
            rospy.loginfo(msg)
            pub.publish(msg)



   

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
