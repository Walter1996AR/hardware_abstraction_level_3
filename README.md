# Hardware abstraction level 3 

## Installing package

Install this package with: 

` cd ~/<your catkin workspace>/src/ `

` git clone https://github.com/Walter1996AR/hardware_abstraction_level_3 ` 

Make files executable with: 

` cd ~/<your catkin workspace>/src/ `

` chmod +x *.py ` 

## Running the service server and client 

What this 'service' does is check if enough levels have been reached to have the required points(20 in total) to pass the minor adaptive robotics. 


Run the service server with: 

` rosrun hardware_abstraction_level_3 level_3_server.py ` 

You can directly do a service call with: 

` rosservice call /levels_to_points 2 2 2 2 2 ` 

The arguments "2 2 2 2 2 " are standing for the levels you have reached

Run the service client with: 

` rosservice call /levels_to_points 2 2 2 2 2 ` 

Where the "2 2 2 2 2" arguments are the levels again. 



## Running the action server and client

What the action client does is ask the user for the desired servo motor angle and sent that angle to the action server. This should be a  angle between 0 and 180 (simulating) the properties of a real servo motor). The action server will then start to adjust the current angle of the (simulated) servo motor and change this to the new desired angle. 

Make sure to run an instance of roscore and run the action server with: 

` rosrun hardware_abstraction_level_3 level_3_action_server.py ` 

Then start the action client with: 

` rosrun hardware_abstraction_level_3 level_3_action_client.py ` 

The program will ask the desired angle and after pressing the ENTER button will start adjusting the current angle. 
