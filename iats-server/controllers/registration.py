""" This will handle incoming requests from the registration frontend component """
from flask import Blueprint, request
from models import User

reg = Blueprint('reg', __name__)

@reg.route("/submit-registration", methods=['POST'])
def getData():
    data = request.json
    print(data)
    try:
        pass
    except Exception as e:
        pass 
    finally:
        pass 
    return ("Received registration data")