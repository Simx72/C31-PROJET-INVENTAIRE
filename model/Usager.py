import math
import helper as hp
import tkinter as tk

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



        
       

    
    def __init__(self, prenom, nom, email, password, password2, personnel):
        # Modifer par des input (texte écrit)
        self.prenom = prenom
        self.nom = nom
        self.email = email
        if(password == password2):
            self.password = password
        else:
            raise ValueError("Les mots de passe ne correspondent pas.")
        
      
        self.is_personnel = personnel # si false == etudiant, si true == personnel  


