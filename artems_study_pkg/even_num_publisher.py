#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Talker(Node):
    def __init__(self):
        super().__init__('even_publisher')
        
        self.number = 0
        
        # Основной publisher
        self.publisher = self.create_publisher(Int32, '/even_numbers', 10)
        
        # Publisher для оверфлоу (создаем сразу)
        self.overflow_publisher = self.create_publisher(Int32, '/even_overflow', 10)
        
        # Таймер на 10 секунд
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = self.number
        self.number += 2
        
        # Проверка на переполнение
        if self.number > 100:
            self.number = 0
            overflow_msg = Int32()
            overflow_msg.data = 100
            self.overflow_publisher.publish(overflow_msg)
            self.get_logger().warn(f"OVERFLOW! Reset to 0, published 100 to /even_overflow")
        
        # Публикуем четное число
        self.publisher.publish(msg)
        self.get_logger().info(f"Even number: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()