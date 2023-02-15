#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import numpy as np

def callback(data):
    rospy.loginfo(np.log(data), loger_name="random_float_log")

def simple_subscriber():
    rospy.init_node('simple_subscriber', anonymous=False)
    rospy.Subscriber('my_random_float', Float32, callback)
    rospy.spin()

if __name__ == '__main__':
        simple_subscriber()