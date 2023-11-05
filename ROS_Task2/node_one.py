#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from task2_dv_interfaces.msg import RT2String

class node_1(Node):

    def __init__(self):
        super().__init__("tasktwo_publisher")
        self.publisher = self.create_publisher(RT2String, "/tasktwo", 10)
        self.get_logger().info("Publisher node has started")
        
        msg_publish = RT2String()
        msg_publish.node_1 = "AABAA"
        self.publisher.publish(msg_publish)

def main(args=None):
    rclpy.init(args=args)
    node = node_1()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
