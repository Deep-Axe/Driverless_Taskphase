#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from task2_dv_interfaces.msg import RT2String
from task2_dv_interfaces.msg import Node2To
from task2_dv_interfaces.msg import Node3To

class Task2_Node2(Node):
    def __init__(self):
        super().__init__('task2_node2')
        self.subscription = self.create_subscription(
            RT2String, "/tasktwo",self.node2_callback,10
        )
        self.publisher =self.create_publisher(Node2To,"/tasktwo2",10)
        self.subscription_node3_=self.create_subscription(Node3To,"taskthree2",10)
    
    def is_palindrome(self,word):
        word=word.replace(" ","").lower()
        set =0
        if word==word[::-1]:
            set=1
            return set
        else:
            set=0
            return set

    def node2_callback(self,msg):
        self.get_logger().info(f"Node2 received: {msg.node_1} from Node1")
        result=self.is_palindrome(msg.node_1)
        response_msg=Node2To()
        response_msg.check=result
        self.publisher.publish(response_msg)

    def response_callback(self,msg):
        self.get_logger().info(f"Node2 received: {msg.check2} from Node 3")

def main(args=None):
    rclpy.init(args=args)
    node = Task2_Node2()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
   main()
