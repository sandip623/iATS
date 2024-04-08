""" This will handle incoming requests from the registration frontend component """
from flask import Blueprint, request
from models import User
# note the relative import here works at flask run-time
from .extension_functions import generate_salt, generate_hash

reg = Blueprint('reg', __name__)

@reg.route("/submit-registration", methods=['POST'])
def registerUser():
    """Submit the user data to the application database"""
    try:
        data = request.json
        if data:
            """ generate a hash for secure password store """
            salt = generate_salt()

            """ use regexp to strip username from email """
            user = User(username='abc', email='abc@email.com', pwd='abc', pwd_hash='abc_hash', pwd_salt='abc_salt')
            ...
        return "200"
    except Exception as e:
        print(f'Error at reg.getData(): {e}') 
        ...
    finally:
        ...