import tkinter as tk
from tkinter import ttk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela")
        self.janela.geometry("300x300")
        self.tvw = ttk.Treeview(self.janela)
        self.tvw.pack()

        self.tvw.insert("", "end", text="Alunos")
        self.tvw.insert("", "end", text="Seres humanos")
        self.id_capivaras = self.tvw.insert("", "end", text="Capivaras")
        self.tvw.insert(self.id_capivaras, "end", text="Roger")
        self.tvw.insert(self.id_capivaras, "end", text="Jair")




janela_pricipal = tk.Tk()
Tela(janela_pricipal)
janela_pricipal.mainloop()
