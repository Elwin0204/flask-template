# -*- coding: utf-8 -*-

from flask import Flask, make_response
from modules.test.views import demo_bp
from flask_cors import CORS


class App(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(demo_bp)
        CORS(self.app, supports_credentials=True)

        # 请求钩子，在所有的请求发生后执行，加入headers。
        @self.app.after_request
        def after_request(resp):
            resp = make_response(resp)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
            resp.headers['Access-Control-Allow-Credentials'] = 'true'
            resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
            return resp

        # 请求拦截：可以在请求进入app.route之前做一些操作
        @self.app.before_request
        def before_request(resp):
            pass

    def start(self):
        self.app.run(host='0.0.0.0', port=8080)
