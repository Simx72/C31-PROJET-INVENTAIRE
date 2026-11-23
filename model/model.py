from model.usager import Usager
from model.database import Db
from model.usager import Usager

class Model():
    db: Db
    def __init__(self):
        self.db = Db()

    def get_client_list(self):
        return self.db.clients

