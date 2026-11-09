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
            # to see if email valid
            self.model.email = email.message.EmailMessage()
            self.model.mot_de_passe_correcte(password1, password2)