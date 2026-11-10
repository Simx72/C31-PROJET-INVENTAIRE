from database import Db

class Model():
    db: Db
    def __init__(self):
        self.db = Db()