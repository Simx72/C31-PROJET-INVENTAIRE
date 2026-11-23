# from model.model import Model
# from view.view import View
import model.model as Model
from model.usager import Usager
from view.view import View
from view.pages.login import Login

import tkinter as tk


class Controller:
    # Properties - hints
    model: Model
    view: View

    def __init__(self):
        # Properties definitions
        self.model = Model
        # self.view = View()

        self.usager = self.model.Usager(self, self.model, "", "", "")

        self.root = tk.Tk()
        self.root.geometry("600x320")
        self.page = Login(self.root)

        # tk.mainloop()

        # self.login = Login(self.root)
        self.page.mainloop()

        # traiter information pour la connexion
    # def traiter_connexion(self):




if __name__ == "__main__":
    controller = Controller()