import model.usager as usager
import view.pages.login as login
import controller as controller

class Personnel:
    def __init__(self):



        # self.personel = usager.Usager(login.Login.get_prenom(),
        #                               login.Login.get_nom(),
        #                               login.Login.get_courriel(),
        #                               login.Login.get_matricule(),
        #                               login.Login.get_mot_de_passe1())

        self.personel = usager.Usager("Amande",
                                      "Cachou",
                                      "noix@peanut.com",
                                      "2",
                                      "Arachide1234")
        # liste des employers

        self.liste_personnel = [
            usager.Creer_Usager("Pomme", "Depin", "depinp@gmail.com", "1", "Arbre2000"),
            usager.Creer_Usager("Amande", "Cachou", "noix@peanut.com", "2", "Arachide1234"),
            usager.Creer_Usager("Venus", "Mercure", "terre@mars.jupiter", "3", "UranusNeptunePluton"),
            usager.Creer_Usager("Dormir", "Respirer", "manger.action@gmail.com", "4", "MotDePasse101"),
        ]

        self.liste_client = [
            usager.Creer_Usager("Jeu", "Video", "gaming@gmail.com", "12", "yes12345"),
            usager.Creer_Usager("Mario", "Sonic", "gmail@olympique.com", "21", "ABCD1234"),
            usager.Creer_Usager("Un", "Deux", "gmail@olympique.com", "33", "Somethinghere101"),
            usager.Creer_Usager("Lmnop", "Xyz", "lettre.alphabet@gmail.com", "46", "Password101")
        ]


    def verifier_si_exployer(self):

        connexion_valide = False

        for i in range(0, len(self.liste_personnel)):
            if(self.liste_personnel[i]. == self.personel):
                connexion_valide = True

        if(connexion_valide):
            print("yes :)")
        else:
            print("no :(")