#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from task_dv_interfaces.msg import TaskOne

class Task1_Sub(Node):
  def __init__(self):
     super().__init__("taskone_sub")
     self.subscriber_ = self.create_subscription(
       TaskOne, "/taskone", self.listen_callback, 10)
     self.get_logger().info("Subscriber node has started")

  def listen_callback(self,msg):
       self.get_logger().info(f"Longitudnal Speed is { (msg.radius)*(msg.angvel)}")

def main(args=None):
    rclpy.init(args=args)
    node = Task1_Sub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
   main()
