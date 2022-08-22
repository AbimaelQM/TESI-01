import tkinter as tk
from tkinter import ttk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela")
        self.janela.geometry("300x400")

        self.btn = tk.Button(self.janela, text="Esquerdo")
        self.btn.bind('<Button-3>', self.esquerdo)
        self.btn.bind('<Button-1>', self.direito, add='+')
        self.btn.bind('<Leave>', self.direito, add='+')
        self.btn.bind('<Any-KeyPress>', self.clicou, add='+')
        self.btn.pack(side=tk.LEFT)

        self.btn2 = tk.Button(self.janela, text="Direito")
        self.btn2.pack(side=tk.RIGHT)

    def clicou(self, event):
        self.lbl = tk.Label(self.janela, text=f"voce clicou na tecla {event.keysym}")
        self.lbl.pack()

    def esquerdo(self, event):
        self.btn2.config(bg="yellow")

    def direito(self, event):
        self.btn2.config(bg="pink")



janela_pricipal = tk.Tk()
Tela(janela_pricipal)
janela_pricipal.mainloop()
