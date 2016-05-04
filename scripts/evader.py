#!/usr/bin/env python
#Code referenced from http://wiki.ros.org/mini_max/Tutorials/Moving%20the%20Base
import rospy
import random
import time
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan



class MoverClass:
	__globaldata = []
	__threshold = 1.0
	#angularflag = 1
	#angularsign = 1 #0 for negative 1 for positive

	def mover(self):
		rospy.init_node('mover', anonymous=True)
		rospy.Subscriber("base_scan",LaserScan,self.callback)
		pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
		
		rate = rospy.Rate(120)
		while not rospy.is_shutdown():
			bool = 0
			if len(self.__globaldata) > 0:
				for i in range(150,210):
					if self.__globaldata[i] < self.__threshold:
						bool = 1
						break

			#if len(self.__globaldata) > 0 and self.__globaldata[180] < 3.0:
			#	bool =1

			twist = Twist()
			if bool == 0:
				#rospy.loginfo("Length of globaldata is %s", len(self.get_globaldata()))
				angularflag = 0
				twist.linear.x = 2.0;
				twist.linear.y = 0.0;
				twist.linear.z = 0.0;
				twist.angular.x = 0.0;
				twist.angular.y = 0.0;
				twist.angular.z = 0.0;
			else:

				twist.linear.x = 0.0;
				twist.linear.y = 0.0;
				twist.linear.z = 0.0;
				twist.angular.x = 0.0;
				twist.angular.y = 0.0;
				#min_val = min(self.__globaldata)
				
				#if angularflag == 1:
				#	if angularsign == 1:
				#		twist.angular.z = random.uniform(0.00,3.14)
				#	else:
				#		twist.angular.z = random.uniform(-3.14,0.00)
				#else:
				#	twist.angular.z = random.uniform(-3.14,3.14)
				#	angularsign = twist.angular.z / abs(twist.angular.z)
				#	angularflag = 1

				twist.angular.z = random.uniform(0,3.14)
				#time.sleep(2)
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
		
