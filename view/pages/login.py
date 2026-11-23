import tkinter as tk


class Login(tk.Frame):
  def __init__(self, parent, input=None): #aucun input de fait au depart
    tk.Frame.__init__(self, parent)

    self.input = input
    # self.on_login_submit = None
    # self.pack(padx=20, pady=20)

    self.prenom = None
    self.nom = None
    self.courriel = None
    self.matricule = None
    self.mot_de_passe1 = None

    # titre
    self.label_titre = tk.Label(self, text="Connexion", font=("Arial", 16, "bold"))
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

    # mot de passe1 (a terminer (if-else)(si les 2 sont correcte) (a voir si besoin d'inscirption ou de harcoder le mot_de_pase))
    self.label_mdp1 = tk.Label(parent, text="Mot de passe")
    self.label_mdp1.pack()
    self.champ_mdp1 = tk.Entry(parent, width=25, show="*")
    self.champ_mdp1.pack(pady=(0, 15))

    self.bouton_connexion = tk.Button(parent, text="Connexion", command=self.connexion)
    self.bouton_connexion.pack(fill="x", ipady=4)

  def connexion(self):
    self.prenom = self.champ_prenom.get().strip()
    self.nom = self.champ_nom.get().strip()
    self.courriel = self.champ_courriel.get().strip()
    self.matricule = self.champ_matricule.get().strip()
    self.mot_de_passe1 = self.champ_mdp1.get().strip()

    # s'il s'inscit, met les inputs dans usager (sinon sont en air)
    if (self.input != None):
      self.input(self.prenom, self.nom, self.courriel, self.matricule, self.mot_de_passe1)

  # MÉTHODE GET
  def get_prenom(self):
    return self.prenom

  def get_nom(self):
    return self.champ_nom.get().strip()

  def get_courriel(self):
    return self.champ_courriel.get().strip()

  def get_matricule(self):
    return self.champ_matricule.get().strip()

  def get_mot_de_passe1(self):
    return self.champ_mdp1.get().strip()
