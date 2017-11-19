#!/usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs.point_cloud2 import read_points


flag = 0

def callback(pointcloud):
    global flag
   
    if flag == 0 :
       redpoints, greenpoints, bluepoints=retrieveBinaryPoints(pointcloud)
       redplane=leastSquares(redpoints)
       greenplane=leastSquares(greenpoints)
       blueplane=leastSquares(bluepoints)
       intersectpoint=intersect(redplane,greenplane,blueplane)
       flag += 1   

    else :
        pass


def retrieveBinaryPoints(pointcloud):
    #TODO : function that given a point cloud, returns 3 list of point in the format : [ [x,y,z], [x,y,z], ... ]
    #one for the red points, one for the green points, one for the blue points.

def leastSquares(points):
    #TODO : function that given a list of points in the format [ [x,y,z], [x,y,z], ... ] returns
    #the parameters of equation of the corresponding plane

def intersect(redplane, greenplane, blueplane):
    #TODO : function that given three planes return the intersection of them.


    
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
