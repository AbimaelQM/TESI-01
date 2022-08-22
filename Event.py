import tkinter as tk
from tkinter import ttk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela")
        self.janela.geometry("300x300")

        self.btn = tk.Button(self.janela, text="Botao")
        self.btn.bind('<Button-3>', self.clicou)
        self.btn.bind('<Button-1>', self.clicou, add='+')
        self.btn.bind('<Return>', self.clicou, add='+')
        self.btn.pack()


    def clicou(self, event):
        self.lbl = tk.Label(self.janela, text="voce clicou no botao")
        self.lbl.pack()

janela_pricipal = tk.Tk()
Tela(janela_pricipal)
janela_pricipal.mainloop()
