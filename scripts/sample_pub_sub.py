#! /usr/bin/env python
import rospy
from spring_seminar.msg import Pos
from spring_seminar.msg import State

def sample_pos_pub(x,y,z):
    pub = rospy.Publisher('sample_position', Pos, queue_size=10)
    rospy.init_node('sample', anonymous=True)
    r = rospy.Rate(1)
    msg = Pos()
    while not rospy.is_shutdown():
        msg.x_pos = x
        msg.y_pos = y
        msg.z_pos = z

        rospy.loginfo("Position:x:%s,y:%s,z:%s",x,y,z)
        pub.publish(msg)
        r.sleep()

def sample_state_pub(s):
    pub = rospy.Publisher('state', State, queue_size=10)
    rospy.init_node('sample', anonymous=True)
    r = rospy.Rate(1)
    msg = State()
    while not rospy.is_shutdown():
        msg.State = s

        rospy.loginfo("State:%s",s)
        pub.publish(msg)
        r.sleep()
         
def callback_pos(data):
    # rospy.loginfo(rospy.get_caller_id() + "%s,%s,%s",data.x_pos, data.y_pos,data.z_pos)
    # samthing code?
    sample_pos_pub(data.x_pos +2 ,data.y_pos + 1 ,data.z_pos + 3)

def callback_state(data):
    rospy.loginfo(rospy.get_caller_id() + "%s", data.data)
    sample_state_pub(data.data)

def sample_pos_sub():
    rospy.init_node('sample', anonymous=True)
    rospy.Subscriber("position", Pos, callback_pos)
    
    rospy.spin()

def sample_state_sub():
    rospy.init_node('sample', anonymous=True)
    rospy.Subscriber("state", State ,callback_state)
    
    rospy.spin()

if __name__ == "__main__":
    sample_pos_sub()
    # sample_state_sub()