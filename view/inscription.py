import email.message
import tkinter as tk

class View():
    def __init__(self, controleur, model):
        self.controleur = controleur
        self.model = model
        # self.taille = "4000x3000"
        # self.root = tk.Tk()
        # self.cadre_principal = tk.Frame(self.root)
        # self.cadre_principal.pack()

        # self.panneau = tk.Frame(self.cadre_principal)
        # self.panneau.pack(side="right", padx=(100,300))

    #    # affichage menu de connexion
    #     self.model.prenom = tk.Label(self.panneau, text="Prenom")
    #     self.model.prenom.pack()

    #     self.model.nom = tk.Label(self.panneau, text="Nom")
    #     self.model.nom.pack()

        def inscription():
            #INSCRIPTION
            first = tk.Tk()
        
            prenom.grid(row=10, column=10)
            tk.Label(first, text="Prenom:").grid(row=10)
            prenom = tk.Entry(first)

            nom.grid(row=11, column=10)
            tk.Label(first, text="Nom").grid(row=11)
            nom = tk.Entry(first)

            # email.grid(row=12, column=10)
            # tk.Label(first, text="Email").grid(row=12)
            # email = tk.Entry(first)   


            # mot de passe ne faut pas qu'il soit visible
            password1.grid(row=13, column=10)
            password1 = tk.Entry(first, show="*")

            password2.grid(row=14, column=10)
            password2 = tk.Entry(first, show="*")
            first.mainloop()

            self.model.prenom = prenom
            self.model.nom = nom
            self.model.email = email.message.EmailMessage()
            self.model.mot_de_passe_correcte(password1, password2)
            self.model.envoyer_nip(self.model.email)

        def envoyer_nip(self):
            self.label_nip = tk.Label(self.panneau, text="Votre NIP est : {self.model.nip}")
            self.label_nip.pack()
            # Envoyer l'email

        def connexion(self):
            first = tk.Tk()
        
            prenom.grid(row=10, column=10)
            tk.Label(first, text="Prenom:").grid(row=10)
            prenom = tk.Entry(first)

            nom.grid(row=11, column=10)
            tk.Label(first, text="Nom").grid(row=11)
            nom = tk.Entry(first)

            # email.grid(row=12, column=10)
            # tk.Label(first, text="Email").grid(row=12)
            # email = tk.Entry(first)   

            # email ou nip
            nip.grid(row=12, column=10)
            tk.Label(first, text="NIP").grid(row=12)
            nip = tk.Entry(first)

            # mot de passe ne faut pas qu'il soit visible
            password.grid(row=13, column=10)
            password = tk.Entry(first, show="*")
            first.mainloop()

            self.model.prenom = prenom
            self.model.nom = nom
            self.model.email = email.message.EmailMessage()
            self.model.nip = nip
            self.model.password = password


            # si employer selon Personnel.txt
            f = open("Personnel.txt", "r")
            for line in f:
                if line.strip() == f"{nom} {prenom} ({email} || {nip}) {password}":
                    self.model.is_personnel = True # employer
                    break
                else:
                    self.model.is_personnel = False # client/etudiant
