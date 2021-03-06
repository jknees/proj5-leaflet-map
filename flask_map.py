import flask
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify # For AJAX transactions

import json
import logging

import pre

app = flask.Flask(__name__)
import CONFIG

@app.route("/")
@app.route("/index")
def index():
	raw = open('poi.txt')
	flask.session['places'] = pre.process(raw)
	return flask.render_template('index.html')


if __name__ == "__main__":
    # Standalone. 
    app.secret_key = CONFIG.secret_key
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
else:
    # Running from cgi-bin or from gunicorn WSGI server, 
    # which makes the call to app.run.  Gunicorn may invoke more than
    # one instance for concurrent service.
    #FIXME:  Debug cgi interface 
    app.debug=False