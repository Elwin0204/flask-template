# -*- coding: utf-8 -*-
from flask import make_response


class Http(object):
    @classmethod
    def response(cls, data):
        resp = make_response(data)
        resp.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
        resp.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        return resp
