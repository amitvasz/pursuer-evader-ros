#!/usr/bin/env python 
#Code referenced from http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20broadcaster%20%28Python%29 
import rospy
import tf
from nav_msgs.msg import Odometry

def handle_odometry(msg):
    #rospy.loginfo("Read it %s" , msg)
    #rospy.loginfo(rospy.get_namespace()[1:-1])
    br = tf.TransformBroadcaster()
    try:
        br.sendTransform((msg.pose.pose.position.x,msg.pose.pose.position.y,msg.pose.pose.position.z),
                     (msg.pose.pose.orientation.x,msg.pose.pose.orientation.y,msg.pose.pose.orientation.z,msg.pose.pose.orientation.w),
                     rospy.Time.now() - rospy.Duration(1.0),
                     rospy.get_namespace()[1:-1],
                    "world")
    except (TypeError):
        br.sendTransform((msg.pose.pose.position.x,msg.pose.pose.position.y,msg.pose.pose.position.z),
                     (msg.pose.pose.orientation.x,msg.pose.pose.orientation.y,msg.pose.pose.orientation.z,msg.pose.pose.orientation.w),
                     rospy.Time.now(),
                     rospy.get_namespace()[1:-1],
                    "world")

if __name__ == '__main__':
    rospy.init_node('tf_broadcaster')
    rospy.Subscriber('odom',
                     Odometry,
                     handle_odometry)
    rospy.spin()