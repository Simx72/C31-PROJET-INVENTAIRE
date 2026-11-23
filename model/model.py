from model.usager import Usager
from model.database import Db
from model.usager import Usager

class Model():
    db: Db
    def __init__(self):
        self.db = Db()
        self.usager = Usager("", "", "")

    def get_client_list(self):
        return self.db.clients

