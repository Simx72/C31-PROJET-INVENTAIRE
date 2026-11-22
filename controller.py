#from model import Model
from model import model

import model.model as Model
from model.usager import Usager
from view.view import View
from view.pages.login import Login



class Controller:
    # Properties - hints
    model: Model
    view: View

    def __init__(self):
        # Properties definitions
        self.model = Model()
        self.view = View()

        self.usager = Usager(self, self.model)

        # Ouvrir Login
        self.login = Login()

if __name__ == "__main__":
    controller = Controller()