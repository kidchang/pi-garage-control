import os
import docker
import simplejson as json

from flask import Flask
from flask import request
import utils

import subprocess

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def trigger_listen():
    queue_id = json.loads(request.data)['requestBody']['queueId']
    # return trigger_listener(queue_id)
    return utils.make_json_response(200, queue_id)

def trigger_listener(queue_id):
    subprocess.Popen(
        ['./garage_listener.py', queue_id],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return utils.make_json_response(
        200, "Daemon Started."
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
