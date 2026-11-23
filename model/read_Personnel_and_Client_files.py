# #personnel: str
# class Personne:
#     def __init__(self, nom: str, prenom: str, courriel: str, matricule: str, ) -> None:
#         self.nom = nom
#         self.prenom = prenom
#         self.courriel = courriel
#         self.matricule = matricule
#         # self.is_personnel = personnel # si false == etudiant, si true == personnel
#
#     # @property
#     # def nom_complet(self) -> str:
#     #     return f"{self.nom.upper()}, {self.prenom}"
#
#
# class Modele:
#     def __init__(self, dossier: Path | None = None) -> None:
#         self.dossier = dossier if dossier is not None else Path(".")
#         self.personnes: list[Personne] = []
#         self.charger_donnees()
#
#     def _resoudre_chemin(self, noms_possibles: list[str]) -> Path | None:
#         for nom in noms_possibles:
#             chemin = self.dossier / nom
#             if chemin.exists():
#                 return chemin
#         return None
#
#
# def _lire_fichier(self, noms_possibles: list[str], col_nom: str, col_prenom: str) -> list[Personne]:
#     chemin = self._resoudre_chemin(noms_possibles)
#     resultat: list[Personne] = []
#
#     if chemin is None:
#         return resultat
#
#     with open(chemin, mode="r", encoding="utf-8", newline="") as fichier:
#         lecteur = csv.DictReader(fichier)
#         for ligne in lecteur:
#             nom = (ligne.get(col_nom) or "").strip()
#             prenom = (ligne.get(col_prenom) or "").strip()
#             courriel = (ligne.get("email") or "").strip()
#             matricule = (ligne.get("nip") or "").strip()
#             if nom or prenom or courriel:
#                 resultat.append(Personne(nom, prenom, courriel, matricule))
#
#     return resultat


# GEMINI
# import csv
# from pathlib import Path
#
# from usager import Usager
#
#
# class Modele:
#     def __init__(self, dossier: Path | None = None) -> None:
#         self.dossier = dossier if dossier is not None else Path(".")
#         # Chaque élément contient : {"usager": Usager, "nip": str}
#         self.comptes_personnel: list[dict] = []
#         self.comptes_clients: list[dict] = []
#         self.charger_donnees()
#
#     def _resoudre_chemin(self, noms_possibles: list[str]) -> Path | None:
#         for nom in noms_possibles:
#             chemin = self.dossier / nom
#             if chemin.exists():
#                 return chemin
#         return None
#
#     def _lire_fichier(
#         self,
#         noms_possibles: list[str],
#         col_nom: str,
#         col_prenom: str,
#         est_personnel: bool,
#     ) -> list[dict]:
#         chemin = self._resoudre_chemin(noms_possibles)
#         resultat: list[dict] = []
#
#         if chemin is None:
#             return resultat
#
#         with open(chemin, mode="r", encoding="utf-8", newline="") as fichier:
#             lecteur = csv.DictReader(fichier)
#             for ligne in lecteur:
#                 nom = (ligne.get(col_nom) or "").strip()
#                 prenom = (ligne.get(col_prenom) or "").strip()
#                 courriel = (ligne.get("email") or "").strip()
#                 nip = (ligne.get("nip") or "").strip()
#                 mot_de_passe = (ligne.get("password") or "").strip()
#
#                 if nom or prenom or courriel or nip:
#                     usager = Usager(prenom, nom, courriel, mot_de_passe, est_personnel)
#                     resultat.append({"usager": usager, "nip": nip})
#
#         return resultat
#
#     def charger_donnees(self) -> None:
#         self.comptes_personnel = self._lire_fichier(
#             ["Personnel.txt"],
#             "nom_personnel",
#             "prenom_personnel",
#             est_personnel=True,
#         )
#         self.comptes_clients = self._lire_fichier(
#             ["Client.txt", "Clients.txt"],
#             "nom_client",
#             "prenom_client",
#             est_personnel=False,
#         )
#
#     def verifier_connexion_personnel(
#         self,
#         prenom: str,
#         nom: str,
#         courriel: str,
#         matricule: str,
#         mot_de_passe: str,
#     ) -> Usager | None:
#         """Vérifie si les informations correspondent à un membre du personnel."""
#         if not mot_de_passe:
#             return None
#
#         for compte in self.comptes_personnel:
#             usager: Usager = compte["usager"]
#             nip: str = compte["nip"]
#
#             if not usager.is_personnel:
#                 continue
#
#             if usager.password != mot_de_passe:
#                 continue
#
#             courriel_ok = bool(courriel) and usager.email.strip().lower() == courriel.strip().lower()
#             matricule_ok = bool(matricule) and nip == matricule.strip()
#
#             if not (courriel_ok or matricule_ok):
#                 continue
#
#             if prenom and usager.prenom.strip().lower() != prenom.strip().lower():
#                 continue
#
#             if nom and usager.nom.strip().lower() != nom.strip().lower():
#                 continue
#
#             return usager
#
#         return None
#
#     def obtenir_tous_les_comptes(self) -> list[dict]:
#         return self.comptes_clients + self.comptes_personnel
#
#     def trier_comptes(self, critere: str) -> list[dict]:
#         comptes = self.obtenir_tous_les_comptes()
#         if critere == "Matricule (0-9)":
#             return sorted(
#                 comptes,
#                 key=lambda c: (
#                     int(c["nip"]) if c["nip"].isdigit() else 0,
#                     c["usager"].nom.lower(),
#                     c["usager"].prenom.lower(),
#                 ),
#             )
#         return sorted(
#             comptes,
#             key=lambda c: (
#                 c["usager"].nom.lower(),
#                 c["usager"].prenom.lower(),
#                 int(c["nip"]) if c["nip"].isdigit() else 0,
#             ),
#         )



# from usager import Usager
import model.usager as usager
import view.pages.login as login
# import controller as controller

class Personnel:
    def __init__(self):
        self.personel = usager.Usager(login.Login.get_prenom(),
                                      login.Login.get_nom(),
                                      login.Login.get_courriel(),
                                      login.Login.get_matricule(),
                                      login.Login.get_mot_de_passe1())


    def lire_Personnel_et_Client(self):
        self.liste_personnel = []
        self.liste_client = []


        #https: // www.docstring.fr / formations / faq / fichiers / comment - lire - et - ecrire - dans - un - fichier - en - python /
        # Personnel.txt
        with open('Personnel.txt', 'r') as fPersonnel:
            self.lignesP = fPersonnel.readlines()  # Retourne une liste

        for ligne in self.lignesP:
            print(ligne)

        # Clients.txt
        with open('Client.txt', 'r') as fClients:
            self.lignesC = fClients.readlines()  # Retourne une liste

        for ligne in self.lignesC:
            print(ligne)

        for i in range(0, 5):  # 0 = premon, 4 = mot_de_passe1
            self.liste_personnel.append(usager.Creer_Usager(self.lignesP[i].strip().split(",")))


        for i in range(0, 5):  # 0 = premon, 4 = mot_de_passe1
            self.liste_client.append(usager.Creer_Usager(self.lignesC[i].strip().split(",")))


    def compare_inputs_to_lists(self):
        for employers in self.liste_personnel:
            #prend ligne par ligne de la liste des employer
            #compare usager avec la ligne
            #si vrai = connexion valide
            #si pas employer/personnel = ne fait rien (pas de connexion)

            for i in range(0, len(self.liste_personnel)):
                if(employers.prenom == self.liste_personnel[i].prenom and
                employers.nom == self.liste_personnel[i].nom and
                employers.courriel == self.liste_personnel[i].courriel and
                employers.matricule == self.liste_personnel[i].matricule and
                employers.mot_de_passe1 == self.liste_personnel[i].mot_de_passe1):
                    print("yes :)")
                else:
                    print("no :(")







# if __name__ == '__main__':
#     personnel = Personnel()