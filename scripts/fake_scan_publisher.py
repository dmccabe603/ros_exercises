#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import random
import numpy as np

def fake_scan_publisher():
    pub = rospy.Publisher('fake_scan', LaserScan, queue_size=10)
    rospy.init_node('fake_scan_publisher', anonymous=False)
    rate = rospy.Rate(20)
    scan = LaserScan()
    scan.header.stamp = rospy.Time.now()
    scan.header.frame_id = 'base_link'
    scan.angle_min = -2*np.pi/3
    scan.angle_max = 2*np.pi/3
    scan.angle_increment = np.pi/300
    scan.range_min = 1.0
    scan.range_max = 10.0
    scan.scan_time = 0.05
    num_points = int((4*np.pi/3)/(np.pi/300)) #calculates the number of fake data points
    while not rospy.is_shutdown():
        data_points = []
        for i in range(num_points):
            rand_num = random.uniform(1.0, 10.0)
            data_points.append(rand_num)
        scan.ranges = data_points
        rospy.loginfo(scan)
        pub.publish(scan)
        rate.sleep()
 
if __name__ == '__main__':
    fake_scan_publisher()