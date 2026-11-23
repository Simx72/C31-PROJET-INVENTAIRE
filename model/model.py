from model.usager import Usager
from model.database import Db
from model.usager import Usager

class Model():
    db: Db
    def __init__(self):
        self.db = Db()
        # Add admin user if no users
        if len(self.db.users) == 0:
            self.db.users.insert_row({ "username": "admin", "password": "0000" })

    def get_client_list(self):
        return self.db.clients

    def validate_credentials(self, username: str, password: str) -> bool:
        for user in self.db.users:
            if user["username"] == username and user["password"] == password:
                return True
        return False
