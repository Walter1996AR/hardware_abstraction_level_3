#!/usr/bin/env python

import time
import rospy
import actionlib
import hardware_abstraction_level_3.msg

current_angle = 90 # servo will start on middle position, 90 degrees. 

class ServoAction(object):

    feedback = hardware_abstraction_level_3.msg.ServoFeedback()
    result = hardware_abstraction_level_3.msg.ServoResult()

    
    def count_to_number_handler(self, goal):
        r = rospy.Rate(4) # action server has a 4hz rate
        success = True
        global current_angle 
        angle = goal.servoAngle

        rospy.loginfo("Request received to change angle to  %i degrees" %(angle))
        rospy.loginfo('Program will now start changing anle')
        delta_angle =  angle - current_angle
        

        

        # check if servo needs to add or substract valu
        if (current_angle <= angle):
            rospy.loginfo('requested angle is bigger, I need to add:%i.'%angle)
            rospy.loginfo('Servo needs to move:%i degrees.'%delta_angle)
            #adding value until desired angle has been reached
            for i in range(1, delta_angle+1):

                # Check that preempt has not been requested by the client
                # If yes, kill the action 
                if self.server.is_preempt_requested():
                    rospy.loginfo('Preempted')
                    self.server.set_preempted()
                    success = False
                    break

                time.sleep(0.1) #small delay to increase servo control 

                current_angle += 1 # the current angle is changed with 1 degree every loop
                self.feedback.percentage = round(float((current_angle/180.0)*100)) #percentage of the angle 
                self.server.publish_feedback(self.feedback)
                rospy.loginfo ('percentage of current servo angle = %i'%self.feedback.percentage)
                
                
                
        
        negative_angle = delta_angle * -1   #need to Invert this value because its negative

        if (current_angle >= angle):
            
            rospy.loginfo('requested angle is smaller, I need to substract %i.'%angle)
            rospy.loginfo('Servo needs to move:%i degrees.'%negative_angle)
        
            for i in range(1, negative_angle+1 ):

                # Check that preempt has not been requested by the client
                # If yes, kill the action 
                if self.server.is_preempt_requested():
                    rospy.loginfo('Preempted')
                    self.server.set_preempted()
                    success = False
                    break

                current_angle -= 1
                self.feedback.percentage = round(float((current_angle / 180.0)*100))
                rospy.loginfo('percentage of current servo angle = %i'%self.feedback.percentage)
                self.server.publish_feedback(self.feedback)
                time.sleep(0.1)

        if success:
            rospy.loginfo('State is now succeeded')
            self.server.set_succeeded(self.result)
            self.result.ActualServoAngle = (current_angle)
            rospy.loginfo('result is = %i', self.result.ActualServoAngle)

        rospy.loginfo('Angle reached: ready to change angle again.')
     
        r.sleep()
       

    
    
    def __init__(self):
        self.server = actionlib.SimpleActionServer('angle_to_servomotion', hardware_abstraction_level_3.msg.ServoAction, self.count_to_number_handler, False)
        self.server.start()
    
    

if __name__ == "__main__":

    rospy.init_node('Servo_action_server')
    server = ServoAction()
    print("Initialization done, ready to control angle")
    rospy.spin()