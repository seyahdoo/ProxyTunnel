#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/proxy/")

from FlaskApp import app as application
application.secret_key = 'your secret here'