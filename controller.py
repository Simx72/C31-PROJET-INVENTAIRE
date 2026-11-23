# from model.model import Model
# from view.view import View
import model.model as Model
from model.usager import Usager
from view.view import View
# from view.pages.login import Login
import view.pages.login as login
import model.read_Personnel_and_Client_files as employer
import tkinter as tk


class Controller:
    # Properties - hints
    model: Model
    view: View

    # def __init__(self):
    #     # Properties definitions
    #     self.model = Model
    #     # self.view = View()
    #
    #
    #
    #     self.root = tk.Tk()
    #     self.root.geometry("600x320")
    #     self.page = login.Login(self.root)
    #
    #     # tk.mainloop()
    #
    #     # self.login = Login(self.root)
    #     self.page.mainloop()
    #
    #     # self.usager = self.model.Usager(login.Login.get_prenom(),
    #     #                                 login.Login.get_nom(),
    #     #                                 login.Login.get_courriel(),
    #     #                                 login.Login.get_matricule(),
    #     #                                 login.Login.get_mot_de_passe())
    #     self.usager = None
    #
    #
    #
    #     # employer.Personnel.lire_Personnel_et_Client(self.usager)
    #     # traiter information pour la connexion
    # # def traiter_connexion

    def __init__(self):
        #Properties definitions
        self.model = Model
        self.view = View


        self.usager = None                      # (JS ex: form on_sumbit=traiter_connexion()) prend les informations que tas recu, met les dans traiter_connexion
        self.root = tk.Tk()                     # |
        self.root.geometry("400x300")           # v
        self.vue_login = login.Login(self.root, input=self.traiter_connexion)
        # self.root = tk.Tk()
        self.root.mainloop()

    def traiter_connexion(self, prenom, nom, courriel, matricule, mot_de_passe1):
        self.usager = Usager(prenom, nom, courriel, matricule, mot_de_passe1) # créer un usager
        print(self.usager.get_mot_de_passe1()) # JAVA (avec let methode get)




if __name__ == "__main__":
    controller = Controller()
    # print(Usager.get_prenom(controller.usager))
    # print(Usager.get_nom(controller.usager))
