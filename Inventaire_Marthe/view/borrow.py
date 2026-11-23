import tkinter as tk
from Inventaire.widgets.headers import Heading1, Heading2, Heading3, Heading4, SearchBar
from Inventaire.widgets.buttons import ConfirmationButton, CancelButton
from Inventaire.widgets.inputs import Input

class View:
    def create_borrow_page(self, borrow_parent):
        self.borrow_parent = borrow_parent
        self.borrow_frame = tk.Frame(borrow_parent)
        self.borrow_frame.pack(fill="both", expand=True)

        #headings
        heading1 = Heading1(self.borrow_frame, "Gestion des équipements")
        heading1.pack()

        heading2 = Heading2(self.borrow_frame, "Emprunt d'équipement")
        heading2.pack()

        heading3 = Heading3(self.borrow_frame, "Information de l'emprunteur")
        heading3.pack()

        #borrow info
        self.nom_input = Input(self.borrow_frame, "Nom : ")
        self.nom_input.pack()

        self.prenom_input = Input(self.borrow_frame, "Prénom : ")
        self.prenom_input.pack()

        self.id_input = Input(self.borrow_frame, "No. d'identifiant : ")
        self.id_input.pack()

        self.status_input = Input(self.borrow_frame, "Status : ")
        self.status_input.pack()

        self.search_bar = SearchBar(self.borrow_frame)
        self.search_bar.pack()

        self.date_input = Input(self.borrow_frame,"Date de l'emprunt (JJ-MM-AAAA) :")
        self.date_input.pack()

        confirm_btn = ConfirmationButton(self.borrow_frame,"Confirmer l'emprunt", command=lambda: print("Confirmé"))
        confirm_btn.pack()
        cancel_btn = CancelButton(self.borrow_frame, "Annuler", command=lambda: print("Annulé"))
        cancel_btn.pack()




# Temporary test window
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")

    view = View()
    view.create_borrow_page(root)

    root.mainloop()