import flask
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify # For AJAX transactions

import json
import logging


app = app.Flask(__name__)
import CONFIG

@app.route("/")
@app.route("/index")
def index():
	raw = open('places.txt')
	flask.session['Places'] = pre.process(raw)
	return flask.rendertemplate('index.html')


if __name__ == "__main__":
    # Standalone. 
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