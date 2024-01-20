
import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
import numpy
from rclpy.qos import QoSProfile
from nav_msgs.msg import Odometry

class Turtlebot3PositionControl(Node):

    def __init__(self):

        super().__init__('turtlebot3_position_control')

        self.odom = Odometry()
        self.last_pose_x1 = 0.0
        self.last_pose_y1 = 0.0
        qos = QoSProfile(depth=10)

        #Initialise publisher
        self.odom_sub1 = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback1,
            qos)
        
        self.cmd_pub1 = self.create_publisher(
            Twist,
            '/cmd_vel',
            qos)
        

        self.timer4 = self.create_timer(0.1, self.same_orien1)  

    
    def odom_callback1(self, msg):
        self.last_pose_x1 = msg.pose.pose.position.x
        self.last_pose_y1 = msg.pose.pose.position.y
        _, _, self.last_pose_theta1 = self.euler_from_quaternion(msg.pose.pose.orientation)


    
        
    
    def same_orien1(self):
        
        twist = Twist()
        
        if(self.last_pose_x1 <= 1):
           twist.linear.x = 0.1
           self.cmd_pub1.publish(twist)
        else:
            twist.linear.x = 0.0
            self.cmd_pub1.publish(twist)

           

    def euler_from_quaternion(self, quat):
        """
        Convert quaternion (w in last place) to euler roll, pitch, yaw.

        quat = [x, y, z, w]
        """
        z = quat.z
        w = quat.w

        roll = 0
        pitch = 0

        siny_cosp = 2 * w * z
        cosy_cosp = 1 - 2 * z * z
        yaw = numpy.arctan2(siny_cosp, cosy_cosp)

        return roll, pitch, yaw


def main(args=None):
    
    rclpy.init(args=args)
    turtlebot3_position_control = Turtlebot3PositionControl()
    rclpy.spin(turtlebot3_position_control)
    turtlebot3_position_control.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()