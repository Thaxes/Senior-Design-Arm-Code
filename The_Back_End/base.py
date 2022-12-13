from flask import Flask
import time
import socket
import json

app = Flask(__name__)

print("Hello world!")


connected = False  # if the backend is connected and talking to the ROS publisher
host = '10.42.0.1'  # the socket server address, could be the reason it only works on emulator, todo look at network IPs and their uses
port = 5000  # socket server port number
client_socket = socket.socket()  # instantiate


def talker(res):
    global connected  # declaring the connected variable so that this function can change it
    message = res
    if (connected):
        try:
           # send the message if the backend thinks it is still connected to the ROS
            client_socket.send(message.encode())
        except Exception as e:
            print(e)
            print("Connection failed. Reset this and ROS.")
            connected = False
    else:  # if not connected to the ros
        print("Attempting connection")
        try:
            client_socket.connect((host, port))  # connect to the server
            connected = True
            client_socket.send(message.encode())
        except Exception as e:
            print(e)
            print("Couldn't connect to ROS")
            # [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
        print(message)


@app.route('/')
def hello_world():  # this function can be called manually but doesn't need to be
    # the password key to stop random programs from attempting a connection to any open port
    # could change password to an actual password, but it seems unlikely that the ROS is going 
    # to be left open enough for a password cracker to realistically crack the key
    payload = {"tester": "MyP@s5w0rd"}
    # converting the payload to a json format for the response
    response = json.dumps(payload)
    # sending a message to the talker on the server we connected to above
    talker(response)
    return response  # returning the payload to the frontend


@app.route('/shoulder/up')
def shoulderUp():
    # this payload is not intended to be changed
    payload = {"shoulder": "w"}
    response = json.dumps(payload)
    talker(response)
    return response


@app.route('/wheel/stop')  # example json response for the wheel
def wheelStop():
    payload = {"wheel": "x"}
    response = json.dumps(payload)
    talker(response)
    return response


@app.route('/shoulder/down')
def shoulderDown():
    payload = {"shoulder": "s"}
    response = json.dumps(payload)
    talker(response)
    return response


@app.route('/shoulder/stop')
def shoulderStop():
    payload = {"shoulder": "x"}
    response = json.dumps(payload)
    talker(response)
    return response


@app.route('/end')
def endShoulder():
    # lets the ros know to close the connection
    payload = {"tester": "goodnight"}
    response = json.dumps(payload)
    talker(response)
    return response


hello_world()
# automatically send the hello message/password to the ROS
