from flask import Flask
import time
import socket
import json

app = Flask(__name__)

while True: # I want the attempts to appear like a log graph
    try:
        host = '10.42.0.1'  # as both code is running on same pc
        port = 5000  # socket server port number
        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server
        err = None
    except Exception as e:
        err = str(e)
        # [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
    if err:
        time.sleep(30) # sleep 30 seconds before attempting to reconnect
        print('Looking for listener again...')
    else: # otherwise, if we connected to the server, break this loop to allow for end point usage
        break 


def talker(res):
    message = res
    client_socket.send(message.encode())  # send message


@app.route('/')
def hello_world():
    payload = {"tester": "me"}
    response = json.dumps(payload)
    talker(response) # sending a message to the talker on the server we connected to above
    # converting the payload to a json format for the response
    return response


@app.route('/up')
def shoulderUp():
    payload = {"shoulder": "w"}
    response = json.dumps(payload)
    talker(response)
    return response


@app.route('/down')
def shoulderDown():
    payload = {"shoulder": "s"}
    response = json.dumps(payload)
    talker(response)
    return response


@app.route('/stop')
def shoulderStop():
    payload = {"shoulder": "x"}
    response = json.dumps(payload)
    talker(response)
    return response

@app.route('/stop/wheel') # example json response for the wheel
def wheelStop():
    payload = {"wheel": "x"}
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