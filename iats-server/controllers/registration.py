""" This will handle incoming requests from the registration frontend component """
from flask import Blueprint, request
# note the relative import(s) here works at flask run-time
from models import User
from .extension_functions import generate_salt, generate_hash, extract_email_prefix

reg = Blueprint('reg', __name__)

@reg.route("/submit-registration", methods=['POST'])
def registerUser():
    """Submit the user data to the application database"""
    try:
        data = request.json
        if data:
            """ generate a hash for secure password store """
            # salt = generate_salt()
            """ data pre-process; using regexp helper functions to extract additional data """
            username = extract_email_prefix(data['email'])
            print(username)
            """ check if email/user exists in db, otherwise create the user and return the respective response status """
            
            ...
        return "200 your data was received..."
    except Exception as e:
        print(f'Error at reg.getData(): {e}') 
        ...
    finally:
        ...

print(generate_hash('random', generate_salt()))