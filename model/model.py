#from database import Db
from model.database import Db
from model.usager import Usager
import controller as c

class Model():
    db: Db
    DataPersonnel: DataPersonnel
    def __init__(self):
        self.db = Db()
        self.usager = Usager(self, self.c.usager)