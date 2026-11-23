import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller import Controller

class Login(tk.Frame):
    controller: Controller
    def __init__(self, parent: tk.Frame, controller: Controller, sizeX = 400, sizeY = 300):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.geometry = ("{sizeX}x{sizeY}")
        # self.label = tk.Label(self, text="Bonjourr. C'est le Login")
#        self.label.pack()
        # self.pack()

        # INSCIRPTION

        # titre
        self.label_titre = tk.Label(self, text="Connexion", font=("Arial", 16, "bold"))
        self.label_titre.pack(pady=(0, 15))

        # prenom
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
        name = self.field_name.get().strip()
        # nom = self.champ_nom.get().strip()
        # courriel = self.champ_courriel.get().strip()
        # matricule = self.champ_matricule.get().strip()
        # mot_de_passe1 = self.champ_mdp1.get().strip()
        password = self.field_password.get().strip()

        self.controller.handle_connection(name, "", "", "", password, "")
        print(name, password)

    # méthode get
    def get_geometry(self):
        return self.geometry

# tests
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    page = Login(root)
    tk.mainloop()