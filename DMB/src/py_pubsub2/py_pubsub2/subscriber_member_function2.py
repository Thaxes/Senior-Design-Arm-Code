import rclpy
from rclpy.node import Node
import serial
from std_msgs.msg import String
import time

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(   # defines the object as receiving String variables on the "shoulder" and the def to be repeated
            String,
            'Shoulder',
            self.listener_callback,
            10)

        self.subscription2 = self.create_subscription(   # defines the object as receiving String variables on the "wheel" and the def to be repeated
            String,
            'Wheel',
            self.listener_callback,
            10)

        #I'm assuming the latest message will be the one sent.

        #self.serial_send = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)    # defines the port the arduino is on and the bitrate.

        self.subscription  # prevent unused variable warning
        self.subscription2  # prevent unused variable warning

    def listener_callback(self, msg):   # passes objects self and msg to the def
        self.get_logger().info('I heard: "%s"' % msg.data) # outputs a strange amount of information currently
       # self.serial_send.write(bytes(msg.data,'utf-8')) # sends the msg.data information to the arduino
        time.sleep(1)   # wait one second before ending. Due to being an ros node, it is called again immediately

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()