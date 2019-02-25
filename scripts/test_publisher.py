#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point
from std_msgs.msg import Int32

def pos_publisher():
    pub = rospy.Publisher('position', Point, queue_size=10)
    rospy.init_node('test_pub', anonymous=True)
    r = rospy.Rate(1)
    x_pos = 1.0
    y_pos = 1.0
    z_pos = 1.0
    msg = Point()
    while not rospy.is_shutdown():
        msg.x = x_pos
        msg.y = y_pos
        msg.z = z_pos

        rospy.loginfo("Position:%s,%s,%s" ,x_pos, y_pos, z_pos)
        pub.publish(msg)
        r.sleep()

def state_publisher():
    pub = rospy.Publisher('state', Int32, queue_size=10)
    rospy.init_node('test_pub', anonymous=True)
    r = rospy.Rate(1)
    state = 0
    msg = Int32()
    while not rospy.is_shutdown():
        msg.data = state

        rospy.loginfo("State:" + state)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        pos_publisher()
    except rospy.ROSInternalException: pass
    # try:
        # state_publisher()
    # except rospy.ROSInterruptException: pass
