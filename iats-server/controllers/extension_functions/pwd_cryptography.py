"""Functions to be used for hashing passwords i.e., upon user registration"""

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

def decode_bytes_to_hex(salt_bytes: bytes) -> str:
    return salt_bytes.hex()

def encode_hex_to_bytes(hex_salt: str) -> bytes:
    """
    Encode a decoded hexadecimal salt back to bytes.

    Parameters:
    - hex_salt (str): Decoded hexadecimal salt string.

    Returns:
    - bytes: Bytes representation of the hexadecimal salt.
    """
    # Convert hexadecimal string to bytes
    salt_bytes = bytes.fromhex(hex_salt)
    
    return salt_bytes

def generate_hash(password : str, salt : str) -> tuple:
    """
    Generate a SHA3-256 hash for the given password and salt...
    This function is to return a password digest, as well as the salt string used...
    NB : the salt and password must both be encoded as when concatenating for data consistency 
    """
    password_with_salt = password.encode() + salt
    password_hash = hashlib.sha3_256(password_with_salt).hexdigest()
    return password_hash