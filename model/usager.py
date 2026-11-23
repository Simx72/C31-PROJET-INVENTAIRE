import math
import tkinter as tk
import view.pages.login as login

id_client = 0


def Creer_Usager():
    global id_client
    id_client += 1
    return str(id_client)


class Usager():
    # def __init__(self, prenom, nom, courriel, mot_de_passe, personnel)
    #     self.prenom = prenom
    #     self.nom = nom
    #     self.id_client = Creer_Usager()

    def __init__(self, prenom, nom, courriel, matricule, mot_de_passe1):
        self.prenom = prenom
        self.nom = nom
        self.courriel = courriel
        self.matricule = matricule
        self.mot_de_passe1 = mot_de_passe1

    # MÉTHODE GET
    def get_prenom(self):
        return self.prenom

    def get_nom(self):
        return self.nom

    def get_courriel(self):
        return self.courriel

    def get_matricule(self):
        return self.matricule

    def get_mot_de_passe1(self):
        return self.mot_de_passe1




#     def mot_de_passe_correcte(self, password1, password2):
#         if (password1 == password2):
#             self.password = password1
#             return True
#         else:
#             raise ValueError("Les mots de passe ne correspondent pas.")
#             return False



