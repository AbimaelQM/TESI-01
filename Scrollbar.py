import tkinter as tk
from tkinter import ttk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela CheckButton")
        self.janela.minsize(300, 100)
        self.scrollbar = tk.Scrollbar(self.janela)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.txt = tk.Text(self.janela, height=5, yscrollcommand=self.scrollbar.set)
        self.txt.pack(side=tk.LEFT,fill=tk.BOTH)
        self.scrollbar.config(command=self.txt.yview)




display = tk.Tk()
Tela(display)
display.mainloop()