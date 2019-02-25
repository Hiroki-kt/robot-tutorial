#! /usr/bin/env python
import rospy
#from spring_seminar.msg import Pos
#from spring_seminar.msg import State
from std_msgs.msg import Int32
from geometry_msgs.msg import Point

def sample_pos_pub(x,y,z):
    pub = rospy.Publisher('sample_position', Point, queue_size=10)
    rospy.init_node('sample', anonymous=True)
    r = rospy.Rate(1)
    msg = Point()
    while not rospy.is_shutdown():
        msg.x = x
        msg.y = y
        msg.z = z

        rospy.loginfo("Position:x:%s,y:%s,z:%s",x,y,z)
        pub.publish(msg)
        r.sleep()

def sample_state_pub(s):
    pub = rospy.Publisher('state', Int32, queue_size=10)
    rospy.init_node('sample', anonymous=True)
    r = rospy.Rate(1)
    msg = Int32()
    while not rospy.is_shutdown():
        msg.data = s

        rospy.loginfo("State:%s",s)
        pub.publish(msg)
        r.sleep()

def callback_pos(data):
    # rospy.loginfo(rospy.get_caller_id() + "%s,%s,%s",data.x_pos, data.y_pos,data.z_pos)
    # samthing code?
    sample_pos_pub(data.x +2 ,data.y + 1 ,data.z + 3)

def callback_state(data):
    rospy.loginfo(rospy.get_caller_id() + "%s", data.data)
    sample_state_pub(data.data)

def sample_pos_sub():
    rospy.init_node('sample', anonymous=True)
    rospy.Subscriber("position", Point, callback_pos)

    rospy.spin()

def sample_state_sub():
    rospy.init_node('sample', anonymous=True)
    rospy.Subscriber("state", Int32 ,callback_state)

    rospy.spin()

if __name__ == "__main__":
    sample_pos_sub()
    # sample_state_sub()
