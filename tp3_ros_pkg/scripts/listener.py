#!/usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs.point_cloud2 import read_points

bluepoints = []
redpoints = []
greenpoints = []
bluecounter=0
redcounter=0
greencounter=0
flag = 0

def callback(pointcloud):
    
    if flag == 0 :
        k=0
        RGB=[]
        while k < len(pointcloud):
            RGB = pointcloud[k+16:k+19]
            point = pointcloud[k:k+13]
            if sum(RGB)-RGB[0]<100 and redcounter <= 100:
                redpoints += point
                redcounter += 1
            elif sum(RGB)-RGB[1]<100 and greencounter <= 100 :
                greenpoints += point
                greencounter +=  1
            elif sum(RGB)-RGB[2]<100 and bluecounter <= 100 :
                bluepoints += point
                bluecounter += 1

            k+=32
        flag += 1
        print(callback)


    else :
        pass
    
    


    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener_node', anonymous=True)

    rospy.Subscriber("camera/depth/points", PointCloud2, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
