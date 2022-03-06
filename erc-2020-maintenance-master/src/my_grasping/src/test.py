#! /usr/bin/env python

import sys
import rospy
import moveit_commander
import geometry_msgs.msg
from geometry_msgs.msg import Point
import copy
import tf

from interactive_markers.interactive_marker_server import *
from interactive_markers.menu_handler import *
from visualization_msgs.msg import *
from visualization_msgs.msg import InteractiveMarkerFeedback
from geometry_msgs.msg import Pose
from tf.broadcaster import TransformBroadcaster

from random import random
from math import sin

def callback(msg):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", visualization_msgs.msg.x
    #p = data
    #p = msg.pose
    
    arm_group.set_pose_target(msg.pose)
    plan = arm_group.go()

    rospy.sleep(3)
    moveit_commander.roscpp_shutdown()

    sub.unregister()
    #print "u"

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('our_node_grasping', anonymous=True)
robot = moveit_commander.RobotCommander()
arm_group = moveit_commander.MoveGroupCommander("arm")
#Pose = geometry_msgs.msg.Pose()
global sub
sub = rospy.Subscriber('/basic_controls/feedback', InteractiveMarkerFeedback ,callback) 

#p = Pose()
#print p
#rospy.wait_for_message()
#p = Pose()
#/basic_controls/feedback
#/basic_controls/update
#/basic_controls/update_full

rospy.spin()