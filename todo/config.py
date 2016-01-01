#!/usr/bin/env python
# coding: utf-8

import os
from todo import app

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'todo.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='root',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# configuration
SITE_NAME = "任务跟踪"


app.config.from_object(__name__)

 


        
