#!/usr/bin/env python
#Code referenced from http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20listener%20%28Python%29
import rospy
import random
import math
import sys
import tf
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan



class MoverClass:
	__globaldata = []
	__threshold = 1.0

	def mover(self):
		
		rospy.init_node('tf_listener', anonymous=True)
		rospy.Subscriber("base_scan",LaserScan,self.callback)
		pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
		listener = tf.TransformListener()
		
		rate = rospy.Rate(20)
		while not rospy.is_shutdown():
			bool = 0
			if len(self.__globaldata) > 0:
				for i in range(100,260):
					if self.__globaldata[i] < self.__threshold:
						bool = 1
						break

			#if len(self.__globaldata) > 0 and self.__globaldata[180] < 3.0:
			#	bool =1

			twist = Twist()
			if bool == 0:
				#rospy.loginfo("Length of globaldata is %s", len(self.get_globaldata()))
				#rospy.loginfo("bool is 0")
				try:
					(trans,rot) = listener.lookupTransform('/robot_1','/robot_0',rospy.Time(0))
					angular = 4 * math.atan2(trans[1], trans[0])
					linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
					twist.linear.x = linear
					twist.angular.z = angular
				except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
					rospy.loginfo(sys.exc_info())
					continue
					
			else:
				#rospy.loginfo("bool is 1")
				twist.linear.x = 0.0;
				twist.linear.y = 0.0;
				twist.linear.z = 0.0;
				twist.angular.x = 0.0;
				twist.angular.y = 0.0;
				min_val = min(self.__globaldata)
				#x
				#if min_val > self.__threshold:
				#	x = self.__globaldata.index(min_val)
				#else:
				#	x = 90	
				twist.angular.z = random.uniform(0.00,3.14)
			pub.publish(twist)
			rate.sleep()	

	def callback(self,data):
		#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
		self.set_globaldata(data.ranges)
		#rospy.loginfo("Globaldata: %s , Range Data: %s", len(self.get_globaldata()), len(data.ranges))
		return

	def set_globaldata(self,data):
		self.__globaldata = data
		return

	def get_globaldata(self):
		return self.__globaldata

def main():
	mover = MoverClass()
	mover.mover()

if __name__=="__main__":
	main()
		
