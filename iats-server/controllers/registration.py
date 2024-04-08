""" This will handle incoming requests from the registration frontend component """
from flask import Blueprint, request
import secrets
import hashlib

def generate_salt(length=16) -> str:
    """
    Generate a random salt of the specified length.

    Parameters:
    - length (int): Length of the salt in bytes. Default is 16 bytes.

    Returns:
    - str: A random salt encoded as a hexadecimal string.
    """
    # Generate a random byte encode string
    return secrets.token_bytes(length)

def generate_hash(password : str, salt : str = generate_salt()) -> tuple:
    """
    Generate a SHA3-256 hash for the given password and salt...
    This function is to return a password digest, as well as the salt string used...
    NB : the salt and password must both be encoded as when concatenating for data consistency 
    """
    password_with_salt = password.encode() + salt
    password_hash = hashlib.sha3_256(password_with_salt).hexdigest()
    return password_hash, salt

reg = Blueprint('reg', __name__)

@reg.route("/submit-registration", methods=['POST'])
def registerUser():
    """Submit the user data to the application database"""
    data = request.json
    try:
        if data:
            """ generate a hash for secure password store """
            salt = generate_salt()
            ...
        return "200"
    except Exception as e:
        print(f'Error at reg.getData(): {e}') 
        ...
    finally:
        ...