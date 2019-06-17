#!/usr/bin/env python

import sys
import rospy
from hardware_abstraction_level_3.srv import *

# Service call handler (arguments are the levels for the different subjects)
def add_two_ints_client(Vision, PrinciplesOfRobotics, HardwareAbstraction, Safety, Ros):
    # Wait for service to become available
    rospy.wait_for_service('levels_to_points')
    
    try:
        # The service proxy handles the service call, like a temporary node!
        # levels_to_points is the service name
        # PointsReached is the service type/file
        check_for_levels_req = rospy.ServiceProxy('levels_to_points', PointsReached)
        response = check_for_levels_req(Vision, PrinciplesOfRobotics, HardwareAbstraction, Safety, Ros)
        return response.Answer

    except rospy.ServiceException, e:
        print("Service call failed: %s")


if __name__ == "__main__":
    
    # If the service call was properly formatted, proceed.
    if len(sys.argv) == 6:

        Vision = int(sys.argv[1])
        PrinciplesOfRobotics = int(sys.argv[2])
        HardwareAbstraction = int(sys.argv[3])
        Safety = int(sys.argv[4])
        Ros = int(sys.argv[5])

        
    # Else, remind the user of the proper usage.
    else:
        print "Usage incorrent, please type the levels reached for the five subjects." 
        sys.exit(1) # Terminate the script. 

    print("Request with args: Vision %s and PrinciplesOfRobotics %s and HardwareAbstraction %s and Safety %s and Ros %s "%(Vision, PrinciplesOfRobotics, HardwareAbstraction, Safety, Ros))
    print (add_two_ints_client(Vision, PrinciplesOfRobotics, HardwareAbstraction, Safety, Ros))