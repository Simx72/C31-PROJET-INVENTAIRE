import math

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

    def __init__(self, controleur, modele):
        self.controleur = controleur
        self.modele = modele
        self.id_client = Creer_Usager()

        
       

    
    def creer_usager(self, prenom, nom, email, password1, password2, personnel):
        # Modifer par des input (texte écrit)
        self.prenom = prenom
        self.nom = nom
        self.email = email
        self.password = self.mot_de_passe_correcte(password1, password2)
        self.is_personnel = personnel # si false == etudiant, si true == personnel  




class Model():
    def __init__(self):
        self.Usager = Usager