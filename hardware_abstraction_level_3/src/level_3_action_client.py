#!/usr/bin/env python

import sys
import time
import roslib
import rospy
import actionlib
import hardware_abstraction_level_3.msg


def change_servo(angle):
    try:
        rospy.init_node('action_client')
        change_servo = actionlib.SimpleActionClient('angle_to_servomotion', hardware_abstraction_level_3.msg.ServoAction)
        change_servo.wait_for_server()

        goal = hardware_abstraction_level_3.msg.ServoGoal()
        goal.servoAngle = angle
        
        change_servo.send_goal(goal)

        # Waits for the server to finish performing the action.
        change_servo.wait_for_result()

        # Prints out the result of executing the action
        return change_servo.get_result() 

    except rospy.ServiceException, e:
        rospy.loginfo("Action call failed: %s" %(e))

if __name__ == "__main__":

    while not rospy.is_shutdown():
      
        print('please type desired servo angle in range of 0 to 180 degrees.')
        angle = input('Angle:')

        #cap angle from 0 to 180
        if angle > 180:
            angle = 180
            rospy.loginfo('Entered numer is too high, changed to 180 instead.')
        if angle < 0:
            angle = 0
            rospy.loginfo('Entered numer is too small, changed to 0 instead.')
        

        print("Requesting the system to change servo angle to %i degrees" %(angle))
        raw_input("Press ENTER to start changing servo angle.")
        result = change_servo(angle)
        
        rospy.loginfo('Desired goal has been reached, ready to take new order.')

        
