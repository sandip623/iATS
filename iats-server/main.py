from flask import Flask, jsonify, Blueprint, request
from flask_cors import CORS
from controllers import reg
from typing import Optional, Union, List

#app = Flask(__name__)
#CORS(app, origins='http://localhost:3000')

"""
@app.route("/")
def index():
    return jsonify("You are logged in...")

@app.route("/submit-registration", methods=['POST'])
def getData():
    data = request.json
    print(data)
    print(type(data))
    return ("Received registration data")
"""

"""CORS configuration parameters for the flask app"""
CORS_CONFIG = {
    "origins": ["http://localhost:3000"],
    "methods": ["GET", "POST"],
    "allow_headers": ["Content-Type"]
 }

"""list of Flask blueprints to be registered to the app instance"""
BLUEPRINTS = [reg]

def launch_application(app: Flask = None, cors_config: Optional[dict] = None, blueprints: List[Blueprint] = None) -> Flask:
    """Launches a Flask application with optional CORS configuration"""
    if app is None:
        app = Flask(__name__)
    if cors_config is not None:
        """Unpack dictionary contents to be passed as K/V-pairs"""
        CORS(app, **cors_config)
    if blueprints is not None:
        for blueprint in blueprints:
            app.register_blueprint(blueprint)
    return app 

if __name__ == "__main__":
    app = launch_application(cors_config=CORS_CONFIG, blueprints=BLUEPRINTS)
    app.run(debug=True)