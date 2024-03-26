"""@dataclass decorator is a shortcut for defining initialisation variables"""

from dataclasses import dataclass

@dataclass
class User:
    userid: int 
    username: str
    email: str
    password: str
    deleted: int = 0

    def userDataToSubmit(self):
        """For feeding data into the DB via POST..."""
        return tuple(self.username, self.email, self.password)