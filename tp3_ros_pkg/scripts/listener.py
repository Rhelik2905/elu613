#!/usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs.point_cloud2 import read_points
import struct
import numpy as np

flag = 0

def callback(pointcloud):
    global flag
    if flag == 0:
        redpoints,greenpoints,bluepoints = retrievePointsList(pointcloud)
        redplane = leastSquares(redpoints)
        greenplane = leastSquares(greenpoints)
        blueplane = leastSquares(bluepoints)
        intersectionPoint = list(intersect(redplane,greenplane,blueplane))
        x,y,z=intersectionPoint
        rospy.loginfo("6DOF pose : "+str(x)+" "+str(y)+" "+str(z))
        flag += 1

    else :
        pass





def leastSquares(points):
    # z= a1*y+a2*x+a3*1
    z = np.array([points[i][2] for i in range(len(points))])
    y = np.array([points[i][1] for i in range(len(points))])
    x = np.array([points[i][0] for i in range(len(points))])
    H = np.array([[x[i],y[i],1] for i in range(len(points))])
    Hplus = np.dot(np.linalg.inv(np.dot(H.T,H)),H.T)
    X = np.dot(Hplus,z)
    return X

def intersect(r, g, b):
    A=np.array([[-r[1],-r[0],1],[-g[1],-g[0],1],[-b[1],-b[0],1]])
    B=np.array([r[2],g[2],b[2]])
    X=np.dot(np.linalg.inv(A),B)
    return X
    

def retrievePointsList(cloud,list_number=100):
    to_treat = list(read_points(cloud,None,True))
    red,green,blue = [],[],[]
    for point in to_treat : 
        color = decode_color(point)
        if (color == 0) and (len(red) < list_number) :
            red.append(point[:3])
        elif (color == 1) and (len(green) < list_number):
            green.append(point[:3])
        elif (color == 2) and (len(blue) < list_number) : 
            blue.append(point[:3])
    return (red,green,blue)



def decode_color(point):
    to_decode = struct.pack('f',point[3])
    first_decode = struct.unpack('I',to_decode)[0]
    blue = (first_decode % 256)
    second_decode = first_decode/256
    green = second_decode % 256
    red = second_decode /256
    if (red > green + 100) and (red > blue + 100):
        return (0) 
    elif (green > red + 100) and (green > blue + 100):
        return(1)
    elif (blue > red + 100) and (blue > green + 100):
        return(2)
    else : 
        return(3)



    
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
