#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def cb(message):
    rospy.loginfo(message.data)

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', String, cb)
    rospy.spin()
