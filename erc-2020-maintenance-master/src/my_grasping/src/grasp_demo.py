#! /usr/bin/env python

import sys
import rospy
import moveit_commander
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('our_node_grasping', anonymous=True)
robot = moveit_commander.RobotCommander()
arm_group = moveit_commander.MoveGroupCommander("arm")

#eef_link = arm_group.get_end_effector_link()

#arm_group.set_named_target('down')
#plan = arm_group.go()

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x = 0
pose_goal.orientation.y = 0
pose_goal.orientation.z = 0
pose_goal.orientation.w = 0
pose_goal.position.x = 1.19209289551e-07
pose_goal.position.y = -0.318157076836
pose_goal.position.z = 0.473009347916
arm_group.set_pose_target(pose_goal)
plan = arm_group.go()

rospy.sleep(3)
moveit_commander.roscpp_shutdown()


pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x = p.orientation.x
pose_goal.orientation.y = p.orientation.y
pose_goal.orientation.z = p.orientation.z
pose_goal.orientation.w = p.orientation.w
pose_goal.position.x = p.position.x
pose_goal.position.y = p.position.y
pose_goal.position.z = p.position.z
arm_group.set_pose_target(pose_goal)
plan = arm_group.go()

rospy.sleep(3)
moveit_commander.roscpp_shutdown()
