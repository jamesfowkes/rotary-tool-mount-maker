import logging

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CsrfProtect

import os

from rtmmapp.blueprints import add_blueprints

app = Flask(__name__)
app.secret_key = os.getenv("RTMM_APP_SECRET_KEY")

import rtmmapp.views.index

CsrfProtect(app)

Bootstrap(app)

add_blueprints(app)

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	app.run(debug=True)