#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import numpy as np

def simple_subscriber():
    rospy.init_node('simple_subscriber', anonymous=False)
    pub = rospy.Publisher("random_float_log", Float32, queue_size=10)

    def callback(data):
        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            pub.publish(np.log(data.data))
            rospy.loginfo(np.log(data.data))
            rate.sleep()
    
    rospy.Subscriber('my_random_float', Float32, callback)
    
    rospy.spin()

if __name__ == '__main__':
    simple_subscriber()
