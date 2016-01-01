#!/usr/bin/env python
# coding: utf-8

from flask import Flask
app = Flask(__name__, instance_relative_config=True)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#加载配置文件
import todo.config
import todo.db

#加载todo模块
from todo import controllers
from todo.controllers import todos