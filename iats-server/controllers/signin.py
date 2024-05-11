""" This will handle incoming requests from the signin frontend component """
from flask import Blueprint, request, jsonify
from models import User
from .extension_functions import generate_salt, generate_hash, extract_email_prefix, decode_bytes_to_hex
from dbutils import UserRepository, DBCONFIG
import http

signin = Blueprint('signin', __name__)

@signin.route("/submit-signin", methods=['POST'])
def signinUser():
    """ Check if user exists """
    ...
    """ If exists, proceed with sign in validation """
    ...
    """ If not exists, throw user not found error """
    ...