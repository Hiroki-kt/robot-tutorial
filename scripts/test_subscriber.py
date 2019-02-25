#!/usr/bin/env python
import rospy
# from spring_seminar.msg import Pos
# from spring_seminar.msg import State
from std_msgs.msg import UInt8
from geometry_msgs.msg import Point

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "%s,%s,%s",data.x_pos, data.y_pos,data.z_pos)

def pos_subscriber():
    rospy.init_node('test_sub', anonymous=True)
    rospy.Subscriber("sample_position", Pos, callback)
    #rospy.Subscriber("position", Pos, callback)
    
    rospy.spin()

def state_subscriber():
    rospy.init_node('test_sub', anonymous=True)
    rospy.Subscriber("state", State, callback)
    
    rospy.spin()

if __name__ == "__main__":
    pos_subscriber()
    #state_subscriber()