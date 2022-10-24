from flask import Flask
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    payload = {
        "direction": "null",
        "amount": "null"
    }
    # converting the payload to a json format for the response
    res = json.dumps(payload)
    print(res)  # replace this line with ROS comms
    # will need to figure out subscriber publisher for communication with ROS
    return res


@app.route('/up')
def shoulderUp():
    payload = {
        "direction": "up",
        "amount": "1"
    }
    # converting the payload to a json format for the response
    res = json.dumps(payload)
    return res


@app.route('/down')
def shoulderDown():
    payload = {
        "direction": "down",
        "amount": "1"
    }
    # converting the payload to a json format for the response
    res = json.dumps(payload)
    return res


@app.route('/stop')
def shoulderStop():
    payload = {
        "direction": "null",
        "amount": "0"
    }
    # converting the payload to a json format for the response
    res = json.dumps(payload)
    return res
