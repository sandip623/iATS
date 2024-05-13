""" This will handle incoming requests from the signin frontend component """
from flask import Blueprint, request, jsonify
from models import User
from .extension_functions import generate_salt, generate_hash, extract_email_prefix, decode_bytes_to_hex
from dbutils import UserRepository, DBCONFIG
import http

signin = Blueprint('signin', __name__)

@signin.route("/submit-signin", methods=['POST'])
def signinUser():
    try:
        """ Get the http request content if applicable """
        data = request.json
        if data is not None:
            """ Check if user exists """
            dbinstance = UserRepository(DBCONFIG['host'], DBCONFIG['username'], DBCONFIG['password'], DBCONFIG['database'])
            dbresponse = dbinstance.countUser(data['email'])
            """ If exists (i.e., user count is 1), proceed with sign in validation """
            if dbresponse:
                username = extract_email_prefix(data['email'])
            """ If not exists, throw user not found error """
            ...
        return jsonify(200)        
    except Exception as e:
        return jsonify(400)
