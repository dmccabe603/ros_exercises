#!/usr/bin/env python2
import rospy
import tf2_ros
import numpy as np
import geometry_msgs.msg

def dynamic_tf_cam_publisher():
    # Initialize the node
    rospy.init_node("dynamic_tf_cam_publisher")
    # Create a broadcaster
    br = tf2_ros.TransformBroadcaster()
    # Publish messages at 10 hz
    r = rospy.Rate(10)

    T_LCam = np.array([[1, 0, 0, 0.05],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

    T_RCam = np.array([[1, 0, 0, 0.10],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    while not rospy.is_shutdown():
        # Initialize a transform object
        t_w_LCam = geometry_msgs.msg.TransformStamped()
        # Add a timestamp
        t_w_LCam.header.stamp = rospy.Time.now()
        # Add the source and target frame
        t_world_bl = tfBuffer.lookup_transform("base_link_gt", "world", rospy.Time())
        
        t_w_LCam.transformations.concatenate_matrices(t_world_bl, T_LCam)
        
        trans_l = tf2_ros.tansformations.translation_from_matrix(t_w_LCam)
        rot_l = tf2_ros.transformation.quaternion_from_matrix(t_w_LCam)

        tf_bl_LCam = geometry_msgs.msg.TransformStamped()
        tf_bl_LCam.header.stamp = rospy.Time.now()
        tf_bl_LCam.header.frame_id = "world"
        tf_bl_LCam.child_frame_id = "left_cam"
        tf_bl_LCam.transform.translation.x = trans_l[0]
        tf_bl_LCam.transform.translation.y = trans_l[1]
        tf_bl_LCam.transform.translation.z = trans_l[2]
        tf_bl_LCam.transform.rotation.x = rot_l[0]
        tf_bl_LCam.transform.rotation.y = rot_l[1]
        tf_bl_LCam.transform.rotation.z = rot_l[2]
        tf_bl_LCam.transform.rotation.w = 1
        
        tf_LCam_RCam = geometry_msgs.msg.TransformStamped()
        tf_LCam_RCam.header.stamp = rospy.Time.now()
        tf_LCam_RCam.header.frame_id = "left_cam"
        tf_LCam_RCam.child_frame_id = "right_cam"
        tf_LCam_RCam.transform.translation.y = 0
        tf_LCam_RCam.transform.translation.z = 0
        tf_LCam_RCam.transform.translation.x = 0.10 #I just put these directly in from the matrix made above
        tf_LCam_RCam.transform.rotation.x = 0
        tf_LCam_RCam.transform.rotation.y = 0
        tf_LCam_RCam.transform.rotation.z = 0
        tf_LCam_RCam.transform.rotation.w = 1

        # Send the transform
        br.sendTransform(tf_bl_LCam)
        br.sendTransform(tf_LCam_RCam)
        # Wait for the next event
        r.sleep()

if __name__ == '__main__':
    try:
        dynamic_tf_cam_publisher()
    except rospy.ROSInteruptException:
        pass