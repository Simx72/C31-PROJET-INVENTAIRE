import tkinter as tk
class Login(tk.Frame):
  def __init__(self, parent):
    tk.Frame.__init__(self, parent)
    self.label = tk.Label(self, text="Bonjourr. C'est le Login")
    self.label.pack()
    self.pack()

# tests
if __name__ == "__main__":
  root = tk.Tk()
  root.geometry("600x400")
  page = Login(root)

  tk.mainloop()