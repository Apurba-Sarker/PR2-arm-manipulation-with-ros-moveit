This project demonstrates how to implement moving a robotic arm to a certain location using ROS and gazebo simulation. Thw simulation has a kinect
camera and a robotic arm without gripper. The moveit package is configured with the kincet camera for octomap and gazebo simulaton. 

To launch the simulation run : roslaunch arm_gazebo empty_world.launch 
this will simultaneously launch gazebo , rviz , moveit and the ros controller

To move the arm in a certain point using rviz marker do the following 
1/ launch the simulation with the previous command (roslaunch arm_moveit demo.launch can also be used in this case)

2/ run the command: rosrun my_grasping 6DOF_marker.py
then go to the rviz window and add an InteractiveMarkers. Select the topic /basic_controls/update for InteractiveMarkers. This will show an interactive marker. We need to place the marker to the desired positoon where we want to move the arm to

3/ run the command: rosrun my_grasping test.py
The terminal will show the line "Ready to take commands for planning group arm." Then we need to move the marker a little to start the message to be sent. The arm will be moved to the initial position of the marker because the program takes the first message sent from the topic as the target position.