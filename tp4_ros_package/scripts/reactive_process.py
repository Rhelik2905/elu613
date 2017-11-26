#!/usr/bin/env python 

import rospy
from kobuki_msgs.msg import BumperEvent 
from kobuki_msgs.msg import WheelDropEvent
from kobuki_msgs.msg import MotorPower


def BumperCallback(data):
            
	global bump
        if (data.state == BumperEvent.PRESSED):
	        bump = True
        else:
                bump = False

def WheelDropCallback(data):
	global wheel

	if (data.state == WheelDropEvent.DROPPED):
		wheel = True
	else:
		wheel = False
	
	

def BumperListener():
	rospy.Subscriber("mobile_base/events/bumper",BumperEvent,BumperCallback)
	rospy.spin()

def WheelDropListener():
	rospy.Subscriber("mobile_base/events/wheel_drop",WheelDropEvent,WheelDropCallback)
	rospy.spin()

def MotorTalker(): 
	
	pub = rospy.Publisher('mobile_base/commands/motor_power',MotorPower,queue_size=10)
	rospy.init_node('MotorTalker', anonymous=True)
	BumperListener()
	WheelDropListener()
	while not rospy.is_shutdown():

		if bump or wheel:
			rospy.loginfo("motor off")
			pub.publish(MotorPower.OFF)
		else:
			rospy.loginfo("motor on")
			pub.publish(MotorPower.ON)
	
		BumperListener()
		WheelDropListener()
	
if __name__ == '__main__' :
	try:
		MotorTalker()
	except rospy.ROSInterruptException:
		pass
