#This script should initialize the service and set up the endpoints 

#---------------------------------------------
#|           Author: Diego de Dios            |
# ---------------------------------------------


#------ Importing dependencies of Google API ------

import firebase_admin
from firebase_admin import credentials

#------ Importing local dependencies ---------
import os
import sys
from flask import Flask


def load_auth_key():
    "Returns credential authentication object for Firebase"
    cred = credentials.Certificate("./api_src/auth_key.json")
    return cred 

def create_app(test_config=None):

    #------ Firebase initialization -----
    app = Flask(__name__, instance_relative_config=True)
    auth = load_auth_key()
    firebase_admin.initialize_app(auth)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hw')
    def hello_world():
        return "Hello world"

    return app