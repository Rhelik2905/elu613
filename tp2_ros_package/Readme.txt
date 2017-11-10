Instructions of use :

1. Keyboard mode :
The keyboard_node.py node is meant to allow you to control turtlebot using your keyboard. 


a. Prerequisite.

To use this node you need to install python module getch. To do so, please run :

sudo pip install https://pypi.python.org/packages/56/f7/cde35f44d267df7122005c40f1a15cf5e3c60ffc83a2ab00d11d99e9d8c4/getch-1.0-python2.tar.gz#md5=586ea0f1f16aa094ff6a30736ba03c50

in your terminal.

This will install getch module for python 2.7.
If you don't have pip please install it running :

sudo apt install python-pip

in you terminal.


b. How to use

To run the node, type :

rosrun tp2_ros_package keyboard_node.py

The commands to move the turtlebot are : 
- 'T' to go forward
- 'G' to go backward
- 'H' to rotate clockwise
- 'F' to rotate counter-clockwise
- '1' to '9' buttons are to set linear turtlebot speed from 0.1 m/s to 0.9 m/s.
