
"""
simple python flask application
"""

##########################################################################
## Imports
##########################################################################

import os
import controleur as ctrl
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify
from tensorflow import keras


##########################################################################
## Application Setup
##########################################################################

app = Flask(__name__)

##########################################################################
## Routes
##########################################################################

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/classify")
def prediction():
    """
    Return the model prediction for given image
    """
    return jsonify({"prediction":ctrl.get_class(request.args["img"]) }) 

##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()