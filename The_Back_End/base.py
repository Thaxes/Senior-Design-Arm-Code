from flask import Flask
import time
import socket
import json

app = Flask(__name__)

print("Hello world!")
connected = False


def talker(res):
    global connected  # declaring the connected variable so that this function can change it
    message = res
    if (connected):
        try:
            client_socket.send(message.encode())
        except Exception as e:
            print(e)
            connected = False
    else:  # if not connected to the ros
        print("Attempting connection")
        try:
            host = '10.42.0.1'  # the socket server address
            port = 5000  # socket server port number
            client_socket = socket.socket()  # instantiate
            client_socket.connect((host, port))  # connect to the server
            connected = True
            client_socket.send(message.encode())
        except Exception as e:
            print(e)
            # [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
        print(message)


@app.route('/')
def hello_world():
    # plan to change me to a generated key for security purposes
    payload = {"tester": "me"}
    # converting the payload to a json format for the response
    response = json.dumps(payload)
    # sending a message to the talker on the server we connected to above
    talker(response)
    return response


@app.route('/shoulder/up')
def shoulderUp():
    # this payload is not intended to be changed
    payload = {"shoulder": "w"}
    response = json.dumps(payload)
    talker(response)
    return response


@app.route('/stop/wheel')  # example json response for the wheel
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
    payload = {"tester": "goodnight"}
    response = json.dumps(payload)
    talker(response)
    client_socket.close()
    return response
