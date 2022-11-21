
@app.route('/end')
def endShoulder():
    payload = {"tester": "goodnight"}
    response = json.dumps(payload)
    talker(response)
    client_socket.close()
    return response