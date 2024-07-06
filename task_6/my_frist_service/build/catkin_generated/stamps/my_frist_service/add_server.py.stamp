from my_frist_service.srv import AddTwoIntsSrv          
from my_frist_service.srv import AddTwoIntsSrvRequest   
from my_frist_service.srv import AddTwoIntsSrvResponse    
import time 
import rospy

def handel_add_two_ints(req):
    print("Returning [%s +%s =%s]"%(req.a,req.b,(req.a + req.b)))
    time.sleep(5) # 5 SECONDS DELAY
    sum_response = AddTwoIntsSrvResponse(req.a + req.b)
    return sum_response

def add_two_ints_server():
     rospy.init_node('add_two_ints_server')
     s= rospy.Service('add_two_ints',AddTwoIntsSrv,handel_add_two_ints)
     print("READY TO ADD TWO INTS.")
     rospy.spin()

if __name__ =="__main__":
    add_two_ints_server()