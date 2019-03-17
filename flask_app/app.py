import os
import docker
import simplejson as json

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/trigger', methods=['POST'])
def trigger_listen():
    queue_id = json.loads(request.data)['queueId']
    _run_control_container(queue_id)
    return "Container Running."

def _run_control_container(queue_id):
    client = docker.from_env()
    client.containers.run(
        'compassindocker/pi-garage-opener',
        detach=True,
        environment={
            "QUEUE": queue_id,
            "RABBIT_HOST": os.environ['RABBIT_HOST']
        })
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333)
