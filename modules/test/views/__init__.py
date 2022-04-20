# -*- coding: utf-8 -*-

from flask import Blueprint

demo_bp = Blueprint('demo', __name__)

from . import hello
