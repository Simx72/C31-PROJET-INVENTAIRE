import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller import Controller

class Login(tk.Frame):
    controller: Controller
    def __init__(self, parent: tk.Frame, controller: Controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="Bonjourr. C'est le Login")
        self.label.pack()
        # self.pack()

        # INSCIRPTION

        # titre
        self.label_titre = tk.Label(self, text="Connexion", font=("Arial", 16, "bold"))
        self.label_titre.pack(pady=(0, 15))

        # prenom
        self.label_prenom = tk.Label(self, text="Prenom")
        self.label_prenom.pack()
        self.champ_prenom = tk.Entry(self, width=25)
        self.champ_prenom.pack(pady=(0, 8))

        # nom
        self.label_nom = tk.Label(self, text="Nom")
        self.label_nom.pack()
        self.champ_nom = tk.Entry(self, width=25)
        self.champ_nom.pack(pady=(0, 8))

        # courriel (a terminer (nip ou courriel))
        self.label_courriel = tk.Label(self, text="Courriel")
        self.label_courriel.pack()
        self.champ_courriel = tk.Entry(self, width=25)
        self.champ_courriel.pack(pady=(0, 4))

        # matricule (a terminer (nip ou courriel))
        self.label_matricule = tk.Label(self, text="Matricule")
        self.label_matricule.pack()
        self.champ_matricule = tk.Entry(self, width=25)
        self.champ_matricule.pack(pady=(0, 8))

        # mot de passe1 (a terminer (if-else)(si les 2 sont correcte))
        self.label_mdp1 = tk.Label(self, text="Mot de passe")
        self.label_mdp1.pack()
        self.champ_mdp1 = tk.Entry(self, width=25, show="*")
        self.champ_mdp1.pack(pady=(0, 15))

        # mot de passe2 (a terminer (if-else)(si les 2 sont correcte))
        self.label_mdp2 = tk.Label(self, text="Retapez votre mot de passe")
        self.label_mdp2.pack()
        self.champ_mdp2 = tk.Entry(self, width=25, show="*")
        self.champ_mdp2.pack(pady=(0, 15))

        self.bouton_connexion = tk.Button(self, text="Connexion", command=self.connexion)
        self.bouton_connexion.pack(fill="x", ipady=4)

    def connexion(self):
        #https://www.w3schools.com/python/ref_string_strip.asp
        prenom = self.champ_prenom.get().strip()
        nom = self.champ_nom.get().strip()
        courriel = self.champ_courriel.get().strip()
        matricule = self.champ_matricule.get().strip()
        mot_de_passe1 = self.champ_mdp1.get().strip()
        mot_de_passe2 = self.champ_mdp2.get().strip()

        self.controller.handle_connection(prenom, nom, courriel, matricule, mot_de_passe1, mot_de_passe2)


# tests
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    page = Login(root)
    tk.mainloop()