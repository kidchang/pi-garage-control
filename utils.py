import simplejson as json
from flask import make_response

def make_json_response(status_code, data):
    result = json.dumps(data)
    resp = make_response(result, status_code)
    resp.headers['Content-type'] = 'application/json'

    return resp
