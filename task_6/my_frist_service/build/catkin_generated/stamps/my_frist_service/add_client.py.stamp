import sys 
import rospy 
from my_frist_service.srv import AddTwoIntsSrv
from my_frist_service.srv import AddTwoIntsSrvRequest
from my_frist_service.srv import AddTwoIntsSrvResponse
 
def add_two_ints_client(x,y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints',AddTwoIntsSrv)
        resp1 =add_two_ints(x,y)
        return resp1.Hello_ROS 
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        

if __name__ == "__main__":
    if len(sys.argv)==3 :
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        sys.exit(1)
    print("Requesting %s+%s"%(x,y))
    print("%s+%s=%s"%(x,y,add_two_ints_client(x,y)))
                    
