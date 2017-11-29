#!/usr/bin/env python  
import rospy

import tf
import geometry_msgs.msg
import nav_msgs.msg
global map_pose

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    global map_pose
    try :
        br.sendTransform((msg.linear.x+map_pose.position.x, msg.linear.y+map_pose.position.y, msg.linear.z+map_pose.position.z),
                     (map_pose.orientation.x,map_pose.orientation.y,map_pose.orientation.z,map_pose.orientation.w),
                     rospy.Time.now(),
                     turtlename,
                     "map")
    except:
        pass

def map_data_listener():
    rospy.Subscriber("/map_metadata",nav_msgs.msg.MapMetaData,map_data_callback)

def map_data_callback(MapMetaData):
    global map_pose
    map_pose=MapMetaData.origin
    



if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')
    turtlename = rospy.get_param('~turtle')
    map_data_listener()
    rospy.Subscriber('/%s/pose' % turtlename,
                     geometry_msgs.msg.Twist,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()

