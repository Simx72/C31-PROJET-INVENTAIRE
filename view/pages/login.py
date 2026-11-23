import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller import Controller

class Login(tk.Frame):
    controller: Controller
    def __init__(self, parent: tk.Tk, controller: Controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # LOGIN

        # title
        self.label_titre = tk.Label(self, text="Connexion", font=("Arial", 16, "bold"))
        self.label_titre.pack(pady=(0, 15))

        # name
        self.label_name = tk.Label(self, text="Tapez votre nom")
        self.label_name.pack()
        self.field_name = tk.Entry(self, width=25)
        self.field_name.pack(pady=(0, 8))

        # password
        self.label_password = tk.Label(self, text="Tapez votre mot de passe")
        self.label_password.pack()
        self.field_password = tk.Entry(self, width=25, show="*")
        self.field_password.pack(pady=(0, 15))

        self.bouton_connexion = tk.Button(self, text="Connexion", command=self.connexion)
        self.bouton_connexion.pack(fill="x", ipady=4)

    def connexion(self):
        #https://www.w3schools.com/python/ref_string_strip.asp
        username = self.field_name.get().strip()
        password = self.field_password.get().strip()

        self.controller.handle_connection(username, password) # password2

# tests
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    # pyrefly: ignore[bad-argument-type]
    page = Login(root, None)
    tk.mainloop()