import tkinter as tk
from tkinter import ttk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela")
        self.janela.geometry("450x300")

        self.colunas = ["nome", "cpf", "email"]
        self.tvw = ttk.Treeview(self.janela, show="headings",columns=self.colunas)
        self.tvw.pack(side=tk.LEFT)

        #cabeçalho

        self.tvw.heading("nome",text="Nome")
        self.tvw.heading("cpf",text="CPF")
        self.tvw.heading("email",text="Email")

        self.tvw.column("nome", minwidth=50, width=150)
        self.tvw.column("cpf", minwidth=50, width=150)
        self.tvw.column("email", minwidth=50, width=150)

        self.tvw.insert("", "end", values=("Abimael", "00000000000", "abimael@gmail.com"))
        self.tvw.insert("", "end", values=("Bruno", "00000000000", "bruno@gmail.com"))
        self.tvw.insert("", "end", values=("Debora", "00000000000", "debora@gmail.com"))

        self.scr = ttk.Scrollbar(self.janela,command=self.tvw.yview)
        self.scr.pack(side=tk.RIGHT, fill=tk.Y, expand=True)
        self.tvw.config(yscroll=self.scr.set)



janela_pricipal = tk.Tk()
Tela(janela_pricipal)
janela_pricipal.mainloop()
