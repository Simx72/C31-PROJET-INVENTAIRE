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
import csv
from pathlib import Path

from usager import Usager


class Modele:
    def __init__(self, dossier: Path | None = None) -> None:
        self.dossier = dossier if dossier is not None else Path(".")
        # Chaque élément contient : {"usager": Usager, "nip": str}
        self.comptes_personnel: list[dict] = []
        self.comptes_clients: list[dict] = []
        self.charger_donnees()

    def _resoudre_chemin(self, noms_possibles: list[str]) -> Path | None:
        for nom in noms_possibles:
            chemin = self.dossier / nom
            if chemin.exists():
                return chemin
        return None

    def _lire_fichier(
        self,
        noms_possibles: list[str],
        col_nom: str,
        col_prenom: str,
        est_personnel: bool,
    ) -> list[dict]:
        chemin = self._resoudre_chemin(noms_possibles)
        resultat: list[dict] = []

        if chemin is None:
            return resultat

        with open(chemin, mode="r", encoding="utf-8", newline="") as fichier:
            lecteur = csv.DictReader(fichier)
            for ligne in lecteur:
                nom = (ligne.get(col_nom) or "").strip()
                prenom = (ligne.get(col_prenom) or "").strip()
                courriel = (ligne.get("email") or "").strip()
                nip = (ligne.get("nip") or "").strip()
                mot_de_passe = (ligne.get("password") or "").strip()

                if nom or prenom or courriel or nip:
                    usager = Usager(prenom, nom, courriel, mot_de_passe, est_personnel)
                    resultat.append({"usager": usager, "nip": nip})

        return resultat

    def charger_donnees(self) -> None:
        self.comptes_personnel = self._lire_fichier(
            ["Personnel.txt"],
            "nom_personnel",
            "prenom_personnel",
            est_personnel=True,
        )
        self.comptes_clients = self._lire_fichier(
            ["Client.txt", "Clients.txt"],
            "nom_client",
            "prenom_client",
            est_personnel=False,
        )

    def verifier_connexion_personnel(
        self,
        prenom: str,
        nom: str,
        courriel: str,
        matricule: str,
        mot_de_passe: str,
    ) -> Usager | None:
        """Vérifie si les informations correspondent à un membre du personnel."""
        if not mot_de_passe:
            return None

        for compte in self.comptes_personnel:
            usager: Usager = compte["usager"]
            nip: str = compte["nip"]

            if not usager.is_personnel:
                continue

            if usager.password != mot_de_passe:
                continue

            courriel_ok = bool(courriel) and usager.email.strip().lower() == courriel.strip().lower()
            matricule_ok = bool(matricule) and nip == matricule.strip()

            if not (courriel_ok or matricule_ok):
                continue

            if prenom and usager.prenom.strip().lower() != prenom.strip().lower():
                continue

            if nom and usager.nom.strip().lower() != nom.strip().lower():
                continue

            return usager

        return None

    def obtenir_tous_les_comptes(self) -> list[dict]:
        return self.comptes_clients + self.comptes_personnel

    def trier_comptes(self, critere: str) -> list[dict]:
        comptes = self.obtenir_tous_les_comptes()
        if critere == "Matricule (0-9)":
            return sorted(
                comptes,
                key=lambda c: (
                    int(c["nip"]) if c["nip"].isdigit() else 0,
                    c["usager"].nom.lower(),
                    c["usager"].prenom.lower(),
                ),
            )
        return sorted(
            comptes,
            key=lambda c: (
                c["usager"].nom.lower(),
                c["usager"].prenom.lower(),
                int(c["nip"]) if c["nip"].isdigit() else 0,
            ),
        )