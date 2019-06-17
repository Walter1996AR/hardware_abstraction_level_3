#!/usr/bin/env python

from hardware_abstraction_level_3.srv import *
import rospy

# Here's your service callback function
def handle_check_levels(req):
    print 'request received to check if enough levels are reached'
    if req.Ros + req.Vision + req.PrinciplesOfRobotics + req.Safety + req.HardwareAbstraction >= 10:
        message = "Levels have been reached, Congrats!"
    else:
        message = "levels are not reached yet, please hurry!!"
    return PointsReachedResponse(message)


def handle_to_level_server():
    rospy.init_node('check_levels_server')
    
    # Here's the  service hook 
    service = rospy.Service('levels_to_points', PointsReached, handle_check_levels)
    print("Ready to check if enough levels have been reached.")
    rospy.spin()

if __name__ == "__main__":
    handle_to_level_server()