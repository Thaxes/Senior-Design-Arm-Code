from flask import Flask
import time
import socket
import json
app = Flask(__name__)

for x in range(0, 3): # try 3 times, then stop trying to connect
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
    payload = "me"
    talker(payload) # sending a message to the talker on the server we connected to above
    # converting the payload to a json format for the response
    res = json.dumps(payload)
    return res


@app.route('/up')
def shoulderUp():
    payload = "w"
    talker(payload)
    # converting the payload to a json format for the response
    res = json.dumps(payload)
    return res


@app.route('/down')
def shoulderDown():
    payload = "s"
    talker(payload)
    # converting the payload to a json format for the response
    res = json.dumps(payload)
    return res


@app.route('/stop')
def shoulderStop():
    payload = "x"
    talker(payload)
    # converting the payload to a json format for the response
    res = json.dumps(payload)
    return res


@app.route('/end')
def endShoulder():
    client_socket.close()
    payload = "Goodnight"
    res = json.dumps(payload)
    return res
