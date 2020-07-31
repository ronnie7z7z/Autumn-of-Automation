#!/usr/bin/env python


import rospy
from math import *
from beginner_tutorials.msg import eangles
from beginner_tutorials.msg import quarternion

qn = quarternion()
ang = eangles()

def callback(data):
    rospy.loginfo(data)
    global qn
    qn = data

def perform():
    rospy.init_node('my_converter')
    rospy.Subscriber("topic1", quarternion, callback)
    pub = rospy.Publisher('topic2', eangles, queue_size=10)
    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():

        sinr_cosp = 2*(qn.q*qn.x + qn.y*qn.z)
        cosr_cosp = 1-2*(qn.x*qn.x + qn.y*qn.y)
        ang.r = atan2(sinr_cosp, cosr_cosp)

        sinp = 2*(qn.q*qn.y - qn.z*qn.x)
        if abs(sinp) >= 1:
            ang.p = copysign(3.1423/2, sinp) # use 90 degrees if out of range
        else:
            ang.p = asin(sinp)

        siny_cosp = 2*(qn.q*qn.z + qn.x*qn.y)
        cosy_cosp = 1 - 2*(qn.y*qn.y + qn.z*qn.z)
        ang.y = atan2(sinr_cosp, cosr_cosp)

        rospy.loginfo(ang)
        pub.publish(ang)
        rate.sleep()

if __name__ == '__main__':
    try:
        perform()
    except rospy.ROSInterruptException:
        pass