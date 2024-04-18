""" This will handle incoming requests from the registration frontend component """
from flask import Blueprint, request, jsonify
# note the relative import(s) here works at flask run-time
from models import User
from .extension_functions import generate_salt, generate_hash, extract_email_prefix
from dbutils import UserRepository, DBCONFIG
import http

reg = Blueprint('reg', __name__)

@reg.route("/submit-registration", methods=['POST'])
def registerUser():
    """Submit the user data to the application database"""
    try:
        data = request.json
        if data:
            """ generate a hash for secure password store """
            salt_bytes = generate_salt()
            salt_hex = ...
            # nb: we retrieve from index 0 as this part of the tuple contains the hash
            hash = generate_hash(data['password'], salt_bytes)
            """ data pre-process; using regexp helper functions to extract additional data """
            username = extract_email_prefix(data['email'])
            userdata = User(username=username, email=data['email'], pwd=data['password'], pwd_salt=salt_bytes, pwd_hash=hash)
            """ check if email/user exists in db, otherwise create the user and return the respective response status """
            dbinstance = UserRepository(DBCONFIG['host'], DBCONFIG['username'], DBCONFIG['password'], DBCONFIG['database'])
            dbresponse = dbinstance.countUser(userdata.email)
            if dbresponse == 0: # only create user if not already exist
                dbinstance.createUser(userdata)
                return jsonify({"message":f"User {userdata.username} created"}), http.HTTPStatus.OK
            return jsonify(http.HTTPStatus.NOT_ACCEPTABLE)
        return jsonify(http.HTTPStatus.NO_CONTENT)
    except Exception as e:
        print(f'Error at reg.getData(): {e}') 
        ...
    finally:
        ...

print(generate_hash('random', generate_salt()))