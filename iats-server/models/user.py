"""@dataclass decorator is a shortcut for defining initialisation variables of a class"""
from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str
    pwd: str
    pwd_hash: str 
    pwd_salt: str