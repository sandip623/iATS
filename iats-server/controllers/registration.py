""" This will handle incoming requests from the registration frontend component """
from flask import Blueprint, request
from models import User

reg = Blueprint('reg', __name__)

@reg.route("/submit-registration", methods=['POST'])
def getData():
    data = request.json
    try:
        if data:
            print(data)
        return "200"
    except Exception as e:
        print(f'Error at reg.getData(): {e}') 
        return "500"
    finally:
        return "304"