#!/usr/bin/env python


import rospy
from beginner_tutorials.msg import quarternion

def qnsend():
    pub = rospy.Publisher('topic1', quarternion, queue_size=10)
    rospy.init_node('Qsender')
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        qn=quarternion()
        qn.q = 0.707
        qn.x = 0.25
        qn.y = -0.25
        qn.z = 0.25
        rospy.loginfo(qn)
        pub.publish(qn)
        rate.sleep()

if __name__ == '__main__':
    try:
        qnsend()
    except rospy.ROSInterruptException:
        pass