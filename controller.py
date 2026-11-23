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
    
    def handle_connection(self, name, email, matricule, mot_de_passe1):
        self.model.usager(name, email, matricule, mot_de_passe1,)
        print("Handling connection...")

    def get_client_list(self):
        return  self.model.get_client_list()

if __name__ == "__main__":
    print("Error: Don't run this file directly!\nInstead, run:    python main.py")