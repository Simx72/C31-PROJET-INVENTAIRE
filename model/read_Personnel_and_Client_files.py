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



