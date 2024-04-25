import rospy
from std_msgs.msg import Float64

def velpub():
        pub=rospy.Publisher('cmdvel',Float64)
        rospy.initnode ('vello', anonymous=True)
        rate = rospy.Rate(1) 
        while not rospy.is_shutdown():
                rospy.loginfo (0000)
                h=pub.publish(1)
                if (h !=1 ):
                      rospy.is_shutdown()
                rate.sleep()
if __name__== '__main__':
        try:
                velpub()
        except rospy.ROSInterruptException:
                pass