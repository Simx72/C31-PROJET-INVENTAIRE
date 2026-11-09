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

        
       

    
    def creer_usager(self, prenom, nom, email, password, personnel):
        # Modifer par des input (texte écrit)
        self.prenom = prenom
        self.nom = nom
        self.email = email
        self.password = password
        self.personnel = personnel




class Model():
    def __init__(self):
        self.Usager = Usager