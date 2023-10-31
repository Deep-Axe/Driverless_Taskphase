#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from task_dv_interfaces.msg import TaskOne

class task1_pub(Node):

    def __init__(self):
        super().__init__("taskone_publisher")
        self.publisher = self.create_publisher(TaskOne, "/taskone", 10)
        self.get_logger().info("Publisher node has started")
        self.publish_task1()
    
    def publish_task1(self):
        angvel=float(input("Enter the angular velocity: "))
        radius=float(input("Enter the radius: "))
        msg_publish = TaskOne()
        msg_publish.angvel = angvel
        msg_publish.radius = radius
        self.publisher.publish(msg_publish)
        self.get_logger().info(f"Angular velocity = {angvel} and radius = {radius} published")

def main(args=None):
    rclpy.init(args=args)
    node = task1_pub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()