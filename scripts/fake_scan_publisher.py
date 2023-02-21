#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import random
import numpy as np

def fake_scan_publisher():
    Pub_topic = rospy.get_param("Pub_topic", "fake_scan")
    pub = rospy.Publisher(Pub_topic, LaserScan, queue_size=10)
    rospy.init_node('fake_scan_publisher', anonymous=False)
    Pub_rate = rospy.get_param("Pub_rate", 20)
    rate = rospy.Rate(Pub_rate)
    scan = LaserScan()
    scan.header.stamp = rospy.Time.now()
    scan.header.frame_id = 'base_link'
    Angle_min = rospy.get_param("Angle_min", -2*np.pi/3)
    scan.angle_min = Angle_min
    Angle_max = rospy.get_param("Angle_max", 2*np.pi/3)
    scan.angle_max = Angle_max
    Angle_increment = rospy.get_param("Angle_increment", np.pi/300)
    scan.angle_increment = Angle_increment
    Range_min = rospy.get_param("Range_min", 1.0)
    scan.range_min = Range_min
    Range_max = rospy.get_param("Range_max", 10.0)
    scan.range_max = Range_max
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