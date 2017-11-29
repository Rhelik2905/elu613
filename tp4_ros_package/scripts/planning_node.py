#!/usr/bin/env python
import rospy
from nav_msgs.msg import OccupancyGrid
from tf2_msgs.msg import TFMessage
import nav_msgs.msg


global map_2d
global pos
global width
global height
global r2dmap
global res

def map_data_listener():
    rospy.Subscriber("/map_metadata",nav_msgs.msg.MapMetaData,map_data_callback)

def map_data_callback(MapMetaData):
    global width
    global height
    global res
    width=MapMetaData.width
    height=MapMetaData.height
    res=MapMetaData.resolution

def map_listener():
	rospy.Subscriber("/map",OccupancyGrid,map_callback)

def tf_listener():
	rospy.Subscriber("/tf",TFMessage, tf_callback)

def map_callback(OccupancyGrid):
	global map_2d
	global r2dmap
	map_2d=OccupancyGrid.data
	r2dmap=OccupancyGrid

def tf_callback(tf):
	global pos
	pos=(tf.transforms[0].transform.translation.x,tf.transforms[0].transform.translation.y)
	

def convert(x,y):
	global res
	global width
	global height
	i=(x/res)+(width/2)
	j=(y/res)+(height/2)
	return int((i-1)*544+j)


def BFS_path(map, start, goal):
	count = 0
	global width
	global height
	global res
	if not map[start] or not map [goal]:
		visited, queue = [], [start]
		ancestor_dict = {}
		while (goal not in queue) and queue:
		    point_to_study = queue.pop(0)
		    if point_to_study not in visited :
		        visited.append(point_to_study)
		        if point_to_study >= width :
		            up = point_to_study - width
		            if not map[up] and up not in visited:
		                queue.append(up)		 
		                ancestor_dict[up] = point_to_study
		        if point_to_study % width > 0 :
		            left = point_to_study - 1
		            if not map[left] and left not in visited :
		                queue.append(left)		                
		                ancestor_dict[left] = point_to_study
		        if point_to_study % width != width-1 :
		            right = point_to_study + 1
		            if not map[right] and right not in visited:
		                queue.append(right)
		                ancestor_dict[right] = point_to_study
		        if point_to_study < (height-1)*width :
		            down = point_to_study + width
		            if not map[down] and down not in visited:
		                queue.append(down)
		                ancestor_dict[down] = point_to_study
		if goal not in queue :
		    return "No path found between start and goal."
		else :
		    path = []
		    ancestor = goal
		    while ancestor != start and count < 100000:
		        path.append(ancestor)
		        ancestor = ancestor_dict[ancestor]
		        count +=1
		    print("goal is : "+str(goal))
		    print("start is : "+str(start))
		    path.reverse()
		    return path
	else :
		return "Start and/or goal unknown or unaccessible."


if __name__ == '__main__':
	rospy.init_node('planning_node',anonymous=True)
	map_listener()
	tf_listener()
	map_data_listener()
	global map_2d
	global pos
	global r2dmap
	rate=rospy.Rate(0.1)
	rate.sleep()
	target=(rospy.get_param('~x_coord'),rospy.get_param('~y_coord'))
	pos_point=convert(pos[0],pos[1])
	target_point=convert(target[0],target[1])
	if (map_2d[pos_point],map_2d[target_point])==(0,0):
		rospy.loginfo("source :" + str(pos) +"   target : "+str(target))
		path=BFS_path(map_2d,pos_point,target_point)
		list_map_2d=list(map_2d)
		for point in path:
			list_map_2d[point]=100
		r2dmap.data=tuple(list_map_2d)
		pub=rospy.Publisher('/rmap',OccupancyGrid,queue_size=1)

	else :
		rospy.loginfo("wrong source or target")	
	print("You can now retrieve the map on /rmap topic")
	while not rospy.is_shutdown():
		pub.publish(r2dmap)
			
		rate.sleep()
	rospy.spin()
	

