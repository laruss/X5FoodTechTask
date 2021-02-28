import json
import os
from flask import Flask
from settings import *


def create_app():
    app = Flask(__name__)

    def _get_path(file):
        return os.path.dirname(os.path.abspath(__file__)) + '/' + file

    def _get_json():
        with open(_get_path('data.json'), 'r') as file:
            data = json.load(file)
        return data

    def _response(data, status_code=200):
        """ Prepare response """
        return json.dumps(data), status_code, {'Content-Type': 'application/json'}

    @app.route(PATH, methods=['GET'])
    def get_test_path():
        data = _get_json()
        return _response(data)

    return app
