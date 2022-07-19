import tkinter as tk
from tkinter import ttk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela CheckButton")
        self.janela.minsize(300, 100)
        self.v = tk.IntVar()
        self.lbl = tk.Label(self.janela, text="Qual dia do fim de semana?", font=("Arial", 12, "bold")).pack()
        self.cbx = ttk.Combobox(self.janela, textvariable=self.v, values=( "sexta", "sabado", "domingo")).pack()





display = tk.Tk()
Tela(display)
display.mainloop()