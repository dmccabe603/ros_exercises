#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import random

def simple_publisher():
    pub = rospy.Publisher('my_random_float', Float32, queue_size=10)
    rospy.init_node('simple_publisher', anonymous=False)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        rand_num = 10*random.random() % rospy.get_time()
        rospy.loginfo(rand_num)
        pub.publish(rand_num)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        simple_publisher()
    except rospy.ROSInteruptException:
        pass