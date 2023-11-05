#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from task2_dv_interfaces.msg import Node2To
from task2_dv_interfaces.msg import Node3To

class Node3(Node):
    def __init__(self):
        super().__init__('node3')
        self.subscriptions = self.create_subscription(
            Node2To, "/tasktwo2",self.node3_callback,10
        )
        self.publisher=self.create_publisher(Node3To,"taskthree2",10)

    def node3_callback(self,msg):
        response_msg=Node3To()
        if msg.check ==1:
            response_msg.check2="Yes"
        else:
            response_msg.check2="No"
        self.publisher.publish(response_msg)
         

def main(args=None):
    rclpy.init(args=args)
    node = Node3()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
   main()
