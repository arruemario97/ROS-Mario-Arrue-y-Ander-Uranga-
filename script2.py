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

# Variables

varx = 0
vary = 0

#preguntas
n_filas = int(input("Numero de filas?"))
n_columnas = int(input("Numero de columnas?"))
d_filas = float(input("Distancia entre filas?"))
d_columnas = float(input("Distancia entre columnas?"))

#confirmacion
print ("la configuracion que has elegido es la siguiente:")
print ("Numero de filas: " + str(n_filas))
print ("Numero de columnas: " + str(n_columnas))
print ("Distancia entre filas: " + str(d_filas))
print ("Distancia entre columnas: " + str(d_columnas))


#rutina de desbarbado
def desbarbado(varx, vary, n_filas, n_columnas, d_filas, d_columnas):
	i=1
	j=1
	#definicion pose coger
	pose1 = [-0.245591664773, 0.109488148961, 0.792095107353, 0.683296024445, 0.219512012839, -0.67359863067, 0.176595311252]#coger
	pose2 = [-0.245591664773, 0.109488148961, 0.992095107353, 0.683296024445, 0.219512012839, -0.67359863067, 0.176595311252]#precoger
	while i <= n_columnas:
		while  j <= n_filas:
			
			# acercamiento coger
			print "Moving to precoger"
			rospy.loginfo( 'Planning movement' )
			ur_group.set_pose_target( pose2 )
			plan = ur_group.plan()
			rospy.loginfo( 'Executing plan' )
			ur_group.execute( plan )
			raw_input('Pause')
			
			# coger
			print "Moving to coger"
			rospy.loginfo( 'Planning movement' )
			ur_group.set_pose_target( pose1 )
			plan = ur_group.plan()
			rospy.loginfo( 'Executing plan' )
			ur_group.execute( plan )
			raw_input('Pause')
			
			# salida coger
			print "Moving to precoger"
			rospy.loginfo( 'Planning movement' )
			ur_group.set_pose_target( pose2 )
			plan = ur_group.plan()
			rospy.loginfo( 'Executing plan' )
			ur_group.execute( plan )
			raw_input('Pause')
			
			#definicion poses dejar nuevas

			pose3 = [0.782046698843-varx, 0.407287698647+vary, 0.788043506315, -0.499871782382, 0.480776527156, 0.505013381385, 0.513754432327]#dejar
			pose4 = [0.782046698843-varx, 0.407287698647+vary, 0.888043506315, -0.499871782382, 0.480776527156, 0.505013381385, 0.513754432327]#predejar	
			
			#acercamiento dejar
			print "Moving to predejar"
			rospy.loginfo( 'Planning movement' )
			ur_group.set_pose_target( pose4 )
			plan = ur_group.plan()
			rospy.loginfo( 'Executing plan' )
			ur_group.execute( plan )
			raw_input('Pause')
			
			#dejar
			print "Moving to dejar"
			rospy.loginfo( 'Planning movement' )
			ur_group.set_pose_target( pose3 )
			plan = ur_group.plan()
			rospy.loginfo( 'Executing plan' )
			ur_group.execute( plan )
			raw_input('Pause')
			
			#salida dejar
			print "Moving to predejar"
			rospy.loginfo( 'Planning movement' )
			ur_group.set_pose_target( pose4 )
			plan = ur_group.plan()
			rospy.loginfo( 'Executing plan' )
			ur_group.execute( plan )
			
			#info y actualizacion variables
			raw_input('Pause')
			print("Dejar en fila "+str(j)+" columna "+str(i)+" finalizado")
			varx=varx+d_filas
			j=j+1
		
		#actualizacion variables columna nueva	
		varx=0
		j=1
		vary=vary+d_columnas
		i=i+1


#program
print "Iniciando programa pick and place rejilla"

#defining poses
safe_joint_positions = [0.18849519922135194, -1.3194694311514095, -1.0681412396999566, -2.3247786719632417, 1.3823008250875066, -3.1415900998779183]#safepose

# Mover a safe
print "Moving to safe pose"
ur_group.set_joint_value_target(safe_joint_positions)
rospy.loginfo( 'Planning movement' )
plan = ur_group.plan()
rospy.loginfo( 'Executing plan' )
ur_group.execute( plan )
raw_input('Pause')

#iniciar rutina pick and place
desbarbado (varx, vary, n_filas, n_columnas, d_filas, d_columnas)

# Mover a safe
print "Moving to safe pose"
ur_group.set_joint_value_target(safe_joint_positions)
rospy.loginfo( 'Planning movement' )
plan = ur_group.plan()
rospy.loginfo( 'Executing plan' )
ur_group.execute( plan )
raw_input('Pause')

#Fin
print("Programa finalizado")	
