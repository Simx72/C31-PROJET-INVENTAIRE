from model.model import Model
from view.view import View

class Controller:
    # Properties - hints
    model: Model
    view: View

    def __init__(self):
        # Properties definitions
        self.model = Model()
        self.view = View()
        # Start app        
        self.view.mainloop()

if __name__ == "__main__":
    print("Error: Don't run this file directly!\nInstead, run:    python main.py")