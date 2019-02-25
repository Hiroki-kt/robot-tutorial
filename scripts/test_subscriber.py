#!/usr/bin/env python
import rospy
<<<<<<< HEAD
from geometry_msgs.msg import Point
from std_msgs.msg import Int32
=======
# from spring_seminar.msg import Pos
# from spring_seminar.msg import State
from std_msgs.msg import UInt8
from geometry_msgs.msg import Point
>>>>>>> 6ce1c030b5d5bd04e26c2e70f3445dbc49b191cc

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "%s,%s,%s",data.x, data.y,data.z)

def pos_subscriber():
    rospy.init_node('test_sub', anonymous=True)
    rospy.Subscriber("sample_position", Point, callback)
    #rospy.Subscriber("position", Pos, callback)

    rospy.spin()

def state_subscriber():
    rospy.init_node('test_sub', anonymous=True)
    rospy.Subscriber("state", Int32, callback)

    rospy.spin()

if __name__ == "__main__":
    pos_subscriber()
    #state_subscriber()
