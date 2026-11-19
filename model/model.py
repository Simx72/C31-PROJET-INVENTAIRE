from model.usager import Usager
from model.database import Db

class Model():
    db: Db
    def __init__(self):
        self.db = Db()
