#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point
from std_msgs.msg import Int32

if __name__ == '__main__':
    rospy.init_node("Test_Pub", anonymous=True)

    posData = Point()
    stateData = Int32()

    posPub = rospy.Publisher('position', Point, queue_size=10)
    statePub = rospy.Publisher('state', Int32, queue_size=10)

    r = rospy.Rate(0.5)

    count = 2

    while not rospy.is_shutdown():
        posData.x = count + 1
        posData.y = count + 2
        posData.z = count + 3

        stateData.data = count

        rospy.loginfo("Position:(%s,%s,%s), State:%s",posData.x, posData.y, posData.z, stateData.data)

        posPub.publish(posData)
        statePub.publish(stateData)

        # count += 1

        r.sleep()
