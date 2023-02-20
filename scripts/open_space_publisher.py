#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from ros_exercises.msg import OpenSpace
import numpy as np

def open_space_publisher():
    rospy.init_node('open_space_publisher', anonymous=False)

    pub = rospy.Publisher("open_space", OpenSpace, queue_size=10)
    space = OpenSpace()

    def callback(scan):
        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            max_val = max(scan.ranges)
            space.distance = max_val
            angle = scan.angle_min + scan.angle_increment*np.array(scan.ranges).argmax()
            space.angle = angle
            pub.publish(space)
            rospy.loginfo(max_val)
            rospy.loginfo(angle)
            rate.sleep()
    
    rospy.Subscriber('fake_scan', LaserScan, callback)
    
    rospy.spin()

if __name__ == '__main__':
    open_space_publisher()
