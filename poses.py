#!/usr/bin/env python
import rospy
import moveit_commander
while True :
 from tf import transformations
 from geometry_msgs.msg import Pose
 rospy.init_node( 'move' )
 robot = moveit_commander.RobotCommander()
 ur_group = moveit_commander.MoveGroupCommander('manipulator')
 print "============ Reference frame: %s" % ur_group.get_planning_frame()
 print "============ End effector frame: %s" % ur_group.get_end_effector_link()
 print "============ Robot Groups: %s" % ", ".join(robot.get_group_names())
 print "============ Printing robot state"
 print robot.get_current_state()
 print "============ Current cartesian pose: %s" % ur_group.get_current_pose()
 print "============ Current joint values: %s" % ur_group.get_current_joint_values()
 raw_input('Pause')


