import tkinter as tk
from Inventaire.widgets.headers import Heading1, Heading2, Heading3, Heading4, SearchBar
from Inventaire.widgets.buttons import ConfirmationButton, CancelButton
from Inventaire.widgets.inputs import Input
from datetime import date

class View:
    def create_return_page(self, return_parent):
        self.return_parent = return_parent
        self.return_frame = tk.Frame(return_parent)
        self.return_frame.pack(fill="both", expand=True)

        #info 
        heading1 = Heading1(self.return_frame, "Gestion des équipements")
        heading1.pack()

        heading2 = Heading2(self.return_frame, "Retour d'équipement")
        heading2.pack()

        heading3 = Heading3(self.return_frame, "Information de l'emprunteur")
        heading3.pack()

        #select borrowing
        self.id_input = Input(self.return_frame, "No. d'identifiant : ")
        self.id_input.pack()
        
        self.no_equip_input = Input(self.return_frame, "No. d'équipement : ")
        self.no_equip_input.pack()

        heading4 = Heading4(self.return_frame, "Pret sélectionné ")
        heading4.pack()

        equip_input = Input(self.return_frame, "Équipement : ")
        equip_input.pack()
        
        self.borrower_input = Input(self.return_frame, "Emprunteur : ")
        self.borrower_input.pack()
        
        self.return_date_input = Input(self.return_frame, "Date de l'emprunt (jj/mm/aa) : ")
        self.return_date_input.pack()

        heading5 = Heading4(self.return_frame, "Date du retour")
        heading5.pack()

        confirm_btn = ConfirmationButton(self.return_frame, "Confirmer le retour", command=lambda: print("Confirmé"))
        confirm_btn.pack()
        
        cancel_btn = CancelButton(self.return_frame, "Annuler" ,command=lambda: print("Annulé"))
        cancel_btn.pack()



# Temporary test window
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")

    today = date.today()

    view = View()
    view.create_return_page(root)

    root.mainloop()




