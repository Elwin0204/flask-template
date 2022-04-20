# -*- coding: utf-8 -*-

from . import demo_bp
from flask import request, json
from utils.http import Http


@demo_bp.route('/demo', methods=['POST'])
def demo():
    demo_id = request.json.get('id', '')
    print('id: ', demo_id)
    res = {
        'code': 200,
        'msg': 'msg',
        'result': [
            {
                'id': 'id1',
                'name': 'name1'
            }
        ]
    }
    res_json = json.dumps(res, ensure_ascii=False)
    return Http.response(res_json), 200
