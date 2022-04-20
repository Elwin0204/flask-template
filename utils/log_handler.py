#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import logging
import time
from logging.handlers import RotatingFileHandler


class LogHandler(object):
    @staticmethod
    def _make_dir(make_dir_path):
        path = make_dir_path.strip()
        if not os.path.exists(path):
            os.makedirs(path)
    @classmethod
    def make_log_handler(cls):
        log_dir_name = "logs"
        log_file_name = "logger-" + time.strftime("%Y-%m-%d", time.localtime(time.time())) + ".log"
        log_file_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + os.sep + log_dir_name
        cls._make_dir(log_file_folder)
        log_file_str = log_file_folder + os.sep + log_file_name
        print('log', log_file_str)
        # set log level
        logging.basicConfig(level=logging.INFO)
        # logging.basicConfig(level=logging.WARNING)
        # set log handler
        file_log_handler = RotatingFileHandler(log_file_str, maxBytes=1024 * 1024, backupCount=10, encoding="UTF-8")
        # set log fomatter
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - [%(filename)s]: %(lineno)d - %(message)s")
        file_log_handler.setFormatter(formatter)

        return file_log_handler
