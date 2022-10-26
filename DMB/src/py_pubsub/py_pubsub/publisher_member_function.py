import rclpy
from rclpy.node import Node
import time
from std_msgs.msg import String
import socket


class MinimalPublisher(Node):   # class provided by ros2

    def __init__(self):
        super().__init__('minimal_publisher')   # name of class
        self.publisher_ = self.create_publisher(String, 'Shoulder', 10) #Defines publishing variable type, topic to publish to, and ?
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback) #creates a timer using the timer_period as the time before triggering,
                                                                        # and calls the timer_callback function once that time has elapsed.

    host = socket.gethostname() #Gets the name of the computer. When DNS is not available, manually input the host's ipv4 address in ticks '10.42.0.1'
    port = 5000  # use any number above 1024. Some ports are "assigned" services, 
                    #keep in mind for security purposes that a bot may connect to any available port 22, etc.

    server_socket = socket.socket()  # creates the socket used for networking
    server_socket.bind((host, port))  # bind host address and port together

    server_socket.listen(2)     # Two connections are allowed for testing purposes; later it will be reduced to one.
    conn, address = server_socket.accept()  # accept new connection


    def timer_callback(self):   # This def is executed every .5 seconds, the timer_period

        print("Connection from: " + str(self.address))  # Shows the ip address that connects.
        while True: # This vague line actually means "while connection is active"
            data = self.conn.recv(2).decode() # receives data stream. Can only receive two bytes per packet.
            if not data:  
                # if data is not received break. This is necessary becase it must continue checking for new data
                break
            msg = String()  # define msg as a string0
            msg.data = str(data)    # pass the data to msg.data because otherwise it would redefine itself as an int.
            self.publisher_.publish(msg)    # publishes the msg variable on the Shoulder topic.
            self.get_logger().info('Publishing: "%s"' % msg.data)   # Outputs the value of the data being published.
            #conn.send(data.encode())  # send data to the client

        self.conn.close()  # close the connection. Currently this causes the object to crash


def main(args=None):
    rclpy.init(args=args)   # ros2 magic; must be called before creating a node

    minimal_publisher = MinimalPublisher()  # create object of the above class

    rclpy.spin(minimal_publisher)   # spinning the object calls its defs

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()    # Destroys the object
    rclpy.shutdown()    # ends the ros2 global executor


if __name__ == '__main__':
    main()
