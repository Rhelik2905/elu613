#!/usr/bin/env python 

import rospy
from kobuki_msgs.msg import BumperEvent 
from kobuki_msgs.msg import WheelDropEvent
from kobuki_msgs.msg import MotorPower


def BumperCallback(data):  
	# the global variable bump indicate if a bumper is pressed or not
	global bump
        if (data.state == BumperEvent.PRESSED):
	        bump = True
        else:
                bump = False

def WheelDropCallback(data):
	#the global variable wheel will indicate if a wheel is dropped or not
	global wheel
	if (data.state == WheelDropEvent.DROPPED):
		wheel = True
	else:
		wheel = False
	
	

def BumperListener():
	
	rospy.Subscriber("mobile_base/events/bumper",BumperEvent,BumperCallback)
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

def WheelDropListener():
	
	rospy.Subscriber("mobile_base/events/wheel_drop",WheelDropEvent,WheelDropCallback)
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

def MotorTalker(): 
	
	MotorON = MotorPower()
	MotorON.state = Motor.ON
	MotorOFF = MotorPower()
	Motor.state = Motor.OFF
	
	pub = rospy.Publisher('mobile_base/commands/motor_power',MotorPower,queue_size=10)
	rospy.init_node('MotorTalker', anonymous=True)
	
	BumperListener()
	WheelDropListener()
	
	while not rospy.is_shutdown():
		MotorON = MotorPower()
		MotorON.state = Motor.ON
		MotorOFF = MotorPower()
		Motor.state = Motor.OFF
		if bump or wheel:
			rospy.loginfo("motor off")
			pub.publish(MotorOFF)
		else:
			rospy.loginfo("motor on")
			pub.publish(MotorON)
	
		BumperListener()
		WheelDropListener()
	
if __name__ == '__main__' :
	try:
		MotorTalker()
	except rospy.ROSInterruptException:
		pass
