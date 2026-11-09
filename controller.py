from model.model import Model
from view.view import View



class Controller:
    # Properties - hints
    model: Model
    view: View

    def __init__(self):
        # Properties definitions
        self.model = Model()
        self.view = View(model=self.model, controleur=self)

        self.usager = self.model.Usager(self, self.model)

if __name__ == "__main__":
    controller = Controller()