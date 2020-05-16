#!/usr/bin/env python
import rospy
import moveit_commander
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
#defining poses
safe_joint_positions = [0.18849519922135194, -1.3194694311514095, -1.0681412396999566, -2.3247786719632417, 1.3823008250875066, -3.1415900998779183]#safepose
pose1 = [-0.245591664773, 0.109488148961, 0.792095107353, 0.683296024445, 0.219512012839, -0.67359863067, 0.176595311252]#coger
pose2 = [-0.245591664773, 0.109488148961, 0.892095107353, 0.683296024445, 0.219512012839, -0.67359863067, 0.176595311252]#precoger
pose3 = [0.609735345035, 0.566103320109, 0.784735181801, -0.50323928217, 0.483160131028, 0.501490594343, 0.511677336269]#dejar
pose4 = [0.609735345035, 0.566103320109, 0.884735181801, -0.50323928217, 0.483160131028, 0.501490594343, 0.511677336269]#predejar


#program
print "Moving to safe pose"
ur_group.set_joint_value_target(safe_joint_positions)
rospy.loginfo( 'Planning movement' )
plan = ur_group.plan()
rospy.loginfo( 'Executing plan' )
ur_group.execute( plan )
raw_input('Pause')
k=0
n=2 # numero de repeticiones
while k<n :
	print "Moving to precoger"
	rospy.loginfo( 'Planning movement' )
	ur_group.set_pose_target( pose2 )
	plan = ur_group.plan()
	rospy.loginfo( 'Executing plan' )
	ur_group.execute( plan )
	raw_input('Pause')
	print "Moving to coger"
	rospy.loginfo( 'Planning movement' )
	ur_group.set_pose_target( pose1 )
	plan = ur_group.plan()
	rospy.loginfo( 'Executing plan' )
	ur_group.execute( plan )
	raw_input('Pause')
	print "Moving to precoger"
	rospy.loginfo( 'Planning movement' )
	ur_group.set_pose_target( pose2 )
	plan = ur_group.plan()
	rospy.loginfo( 'Executing plan' )
	ur_group.execute( plan )
	raw_input('Pause')
	print "Moving to predejar"
	rospy.loginfo( 'Planning movement' )
	ur_group.set_pose_target( pose4 )
	plan = ur_group.plan()
	rospy.loginfo( 'Executing plan' )
	ur_group.execute( plan )
	raw_input('Pause')
	print "Moving to dejar"
	rospy.loginfo( 'Planning movement' )
	ur_group.set_pose_target( pose3 )
	plan = ur_group.plan()
	rospy.loginfo( 'Executing plan' )
	ur_group.execute( plan )
	raw_input('Pause')
	print "Moving to predejar"
	rospy.loginfo( 'Planning movement' )
	ur_group.set_pose_target( pose4 )
	plan = ur_group.plan()
	rospy.loginfo( 'Executing plan' )
	ur_group.execute( plan )
	k = k+1
print "Moving to safe pose"
ur_group.set_joint_value_target(safe_joint_positions)
rospy.loginfo( 'Planning movement' )
plan = ur_group.plan()
rospy.loginfo( 'Executing plan' )
ur_group.execute( plan )
raw_input('Pause')	
