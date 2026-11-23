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
    
    def handle_connection(self, username: str, password: str) -> None:
        # valid credentials
        valid = self.model.validate_credentials(username, password)
        print("login was valid ? ", valid)
        # change page
        if valid:
            self.view.show_frame("MenuPrincipal")

    def get_client_list(self):
        return  self.model.get_client_list()

if __name__ == "__main__":
    print("Error: Don't run this file directly!\nInstead, run:    python main.py")