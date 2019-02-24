#!/usr/bin/env python

import rospy
from spring_seminar.msg import Pos
from spring_seminar.msg import State

def pos_publisher():
    pub = rospy.Publisher('position', Pos, queue_size=10)
    rospy.init_node('test_pub', anonymous=True)
    r = rospy.Rate(1)
    x_pos = 1.0
    y_pos = 1.0
    z_pos = 1.0
    msg = Pos()
    while not rospy.is_shutdown():
        msg.x_pos = x_pos
        msg.y_pos = y_pos
        msg.z_pos = z_pos

        rospy.loginfo("Position:%s,%s,%s" ,x_pos, y_pos, z_pos)
        pub.publish(msg)
        r.sleep()

def state_publisher():
    pub = rospy.Publisher('state', State, queue_size=10)
    rospy.init_node('test_pub', anonymous=True)
    r = rospy.Rate(1)
    state = 0
    msg = State()
    while not rospy.is_shutdown():
        msg.State = state

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
