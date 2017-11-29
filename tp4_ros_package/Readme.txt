How to use the planning node :
just run in your terminal :

roslaunch tp4_ros_package planning.launch x:=<x_coordinate> y:=<y_coordinate>

Where <x_coordinate> and <y_coordinate> must be the coordinates of the point you want to reach (i.e the target).
Please make sure those coordinate are on the white area of the map. As an example, I suggest you try with x=1.0 and y=2.0.

This will compute the path from the position of the robot (which is on (0.0) on the map) to the target, using the map.yaml file as the map.
It will then replace each point on the map the robot is supposed to take to reach the target by a black point, and then publish the new map on the /rmap topic.

Once you read the message "You can now retrieve the map on /rmap topic" in the terminal (takes a few seconds), you can then run :

rosrun map_server map_saver -f <mapname> map:=rmap

on a new terminal. <mapname> is the name you wish to give to the new file. It will save the map pusblished on /rmap as an .pgm image and a .yaml file.
So now you can observe the computed path.



Reactive process :

After launching turtlebot run the script by the following command :

rosrun tp4_ros_package reactive_process.py
