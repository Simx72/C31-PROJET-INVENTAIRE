from model.model import Model
from view.view import View

class Controller:
    # Properties - hints
    model: Model
    view: View

    def __init__(self):
        # Properties definitions
        self.model = Model()
        self.view = View(controller=self)
        # Start app        
        self.view.mainloop()
    
    def handle_connection(self, prenom, nom, courriel, matricule, mot_de_passe1, mot_de_passe2):
        print("Handling connection...")

if __name__ == "__main__":
    print("Error: Don't run this file directly!\nInstead, run:    python main.py")