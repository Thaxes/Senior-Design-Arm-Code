from flask import Flask
import socket
import json
app = Flask(__name__)

host = '10.42.0.1'  # as both code is running on same pc
port = 5000  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server


def talker(res):
    message = res
    client_socket.send(message.encode())  # send message


@app.route('/')
def hello_world():
    payload = "me"
    talker(payload)
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
