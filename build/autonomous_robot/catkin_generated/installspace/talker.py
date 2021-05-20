import rospy
#from std_msgs.msg import String
from std_msgs.msg import Int64MultiArray
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

# def encoderCallback(msg):
#     global encoder1_ticks 
#     global encoder2_ticks 
#     global encoder3_ticks 
#     global encoder4_ticks 
#     encoder1_ticks = msg.data[1]
#     encoder2_ticks = msg.data[0]
#     encoder3_ticks = msg.data[2]
#     encoder4_ticks = msg.data[3]

# def ticks_to_odometry():
#         #Parameters
#     l=34 #
#     phi2=234 #
#     R=235 #

#     encoder1_ticks = 0
#     encoder2_ticks = 0
#     encoder3_ticks = 0
#     encoder4_ticks = 0
#     last_encoder1_ticks = 0
#     last_encoder2_ticks = 0
#     last_encoder3_ticks = 0
#     last_encoder4_ticks = 0

#     x = 0.0
#     y = 0.0
#     th = 0.0

#     vx =  0.0
#     vy =  0.0
#     vth =  0.0
#     odom_pub = rospy.Publisher('odometry_info', Odometry, queue_size=10)
#     rospy.init_node('Odometry_info', anonymous=True)
#     encoders_sub =rospy.Subscriber("/pulses", Int64MultiArray, encoderCallback)
#     odom_broadcaster = tf.TransformBroadcaster()
#     current_time = rospy.Time.now()
#     last_time = rospy.Time.now()
#     r = rospy.Rate(10) #10 Hz

#     while not rospy.is_shutdown():
#         current_time = rospy.Time.now()
#         delta_encoder1 = encoder1_ticks - last_encoder1_ticks
#         delta_encoder2 = encoder2_ticks - last_encoder2_ticks
#         delta_encoder3 = encoder3_ticks - last_encoder3_ticks
#         delta_encoder4 = encoder4_ticks - last_encoder4_ticks
#         dt = (current_time - last_time).to_sec()

#         #Calculation of encoder velocities
#         velocity_encoder1 = delta_encoder1/dt
#         velocity_encoder2 = delta_encoder2/dt
#         velocity_encoder3 = delta_encoder3/dt
#         velocity_encoder4 = delta_encoder4/dt

#         vx = (R/4)* (velocity_encoder1+velocity_encoder2+velocity_encoder3+velocity_encoder4)
#         vy =  (R/4)* (-velocity_encoder1+velocity_encoder2+velocity_encode-velocity_encoder4)
#         vth = (R/(4*2*l)* (-velocity_encoder1+velocity_encoder2-velocity_encode+velocity_encoder4)

#         dx= vx*dt
#         dy= vy*dt
#         dth= vth*dt

#         x += dx  
#         y += dy 
#         th += dth

#         odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)
# #-----------------------------------------------------------------------------
#         odom = Odometry()
#         odom.header.stamp = current_time
#         odom.header.frame_id = "odom"
#         odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

#         odom.child_frame_id = "base_link"
#         odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))
#         odom_pub.publish(odom)
#         last_encoder1_ticks = encoder1_ticks
#         last_encoder2_ticks = encoder2_ticks
#         last_encoder3_ticks = encoder3_ticks
#         last_encoder4_ticks = encoder4_ticks
#         last_time = current_time
#         r.sleep()


# if __name__ == '__main__':
#     try:
#         ticks_to_odometry()
#     except rospy.ROSInterruptException:
#         pass
