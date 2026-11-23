import tkinter as tk
# import Controller as controller
class Login(tk.Frame):
  def __init__(self, parent):
    tk.Frame.__init__(self, parent)

    #self.label = tk.Label(self, text="Bonjourr. C'est le Login")
    #self.label.pack()
    #self.pack()

    # Connexion (Pas inscriptio (si nouveau client => harcoder dans Client.txt ou Personnel.txt))

    # titre
    self.label_titre = tk.Label(parent, text="Connexion", font=("Arial", 16, "bold"))
    self.label_titre.pack(pady=(0, 15))

    # prenom
    self.label_prenom = tk.Label(parent, text="Prenom")
    self.label_prenom.pack()
    self.champ_prenom = tk.Entry(parent, width=25)
    self.champ_prenom.pack(pady=(0, 8))

    # nom
    self.label_nom = tk.Label(parent, text="Nom")
    self.label_nom.pack()
    self.champ_nom = tk.Entry(parent, width=25)
    self.champ_nom.pack(pady=(0, 8))

    # courriel (a terminer (nip ou courriel))
    self.label_courriel = tk.Label(parent, text="Courriel")
    self.label_courriel.pack()
    self.champ_courriel = tk.Entry(parent, width=25)
    self.champ_courriel.pack(pady=(0, 4))

    # matricule (a terminer (nip ou courriel))
    self.label_matricule = tk.Label(parent, text="Matricule")
    self.label_matricule.pack()
    self.champ_matricule = tk.Entry(parent, width=25)
    self.champ_matricule.pack(pady=(0, 8))

    # mot de passe1 (a terminer (if-else)(si les 2 sont correcte))
    self.label_mdp1 = tk.Label(parent, text="Mot de passe")
    self.label_mdp1.pack()
    self.champ_mdp1 = tk.Entry(parent, width=25, show="*")
    self.champ_mdp1.pack(pady=(0, 15))

    # # mot de passe2 (a terminer (if-else)(si les 2 sont correcte))
    # self.label_mdp2 = tk.Label(parent, text="Retapez votre mot de passe")
    # self.label_mdp2.pack()
    # self.champ_mdp2 = tk.Entry(parent, width=25, show="*")
    # self.champ_mdp2.pack(pady=(0, 15))

    self.bouton_connexion = tk.Button(parent, text="Connexion", command=self.connexion)
    self.bouton_connexion.pack(fill="x", ipady=4)

  def connexion(self):
    #https://www.w3schools.com/python/ref_string_strip.asp
    prenom = self.champ_prenom.get().strip()
    nom = self.champ_nom.get().strip()
    courriel = self.champ_courriel.get().strip()
    matricule = self.champ_matricule.get().strip()
    mot_de_passe1 = self.champ_mdp1.get().strip()
    # mot_de_passe2 = self.champ_mdp2.get().strip()
                                                                                    # mot_de_passe2
    # traiter_connexion(prenom, nom, courriel, matricule, mot_de_passe1)
    self.traiter_connexion(self, prenom, nom, courriel, matricule, mot_de_passe1)

  def traiter_connexion(self, self1, prenom, nom, courriel, matricule, mot_de_passe1):
    pass


# # tests
# if __name__ == "__main__":
#   root = tk.Tk()
#   root.geometry("800x700")
#   page = Login(root)
#
#   tk.mainloop()