#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

twist = Twist()
twist.linear.x = 1
twist.linear.z = 0
# Define a function called 'callback' that receives a parameter


def turn_right():
    twist.linear.x = 0
    twist.angular.z = -1


def straight():
    twist.linear.x = 1
    twist.angular.z = 0


def callback(msg):
    pub.publish(twist)
    if(msg.ranges[360] < 1):
        turn_right()
    if(msg.ranges[719] < 1 and msg.ranges[400] == float('inf')):
        straight()


# Initiate a Node called 'topic_subscriber'
rospy.init_node('laser_sub')

# Create a Subscriber object that will listen to the /counter
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=3)
# topic and will cal the 'callback' function each time it reads
# something from the topic
rospy.spin()
