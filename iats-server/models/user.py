"""@dataclass decorator is a shortcut for defining initialisation variables of a class"""
from dataclasses import dataclass

@dataclass
class User:
    userid: int 
    username: str
    email: str
    password: str
    deleted: int = 0

    def userDataToSubmit(self) -> tuple:
        """For feeding data into the DB via POST..."""
        return tuple(self.username, self.email, self.password)