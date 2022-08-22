import tkinter as tk
from tkinter import ttk, messagebox


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela CheckButton")
        self.janela.minsize(300, 100)
        self.v = tk.IntVar()
        self.lbl = tk.Label(self.janela, text="Qual dia do fim de semana?", font=("Arial", 12, "bold")).pack()
        self.cbx = ttk.Combobox(self.janela, textvariable=self.v, values=( "sexta", "sabado", "domingo"))
        self.cbx.bind('<<ComboboxSelected>>', self.selecionado)
        self.cbx.pack()


    def selecionado(self, event):
        messagebox.showinfo('Info', f'Voce clicou {self.cbx.get()}')




display = tk.Tk()
Tela(display)
display.mainloop()