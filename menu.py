import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela CheckButton")
        self.janela.minsize(300, 100)
        self.barra = tk.Menu(self.janela)
        self.menu1 = tk.Menu(self.barra)
        self.barra.add_cascade(label="Arquivo", menu=self.menu1)
        self.menu1.add_command(label='Abrir')
        self.menu1.add_command(label='Salvar')
        self.menu1.add_separator()
        self.menu1.add_command(label='Exportar')
        self.janela.config(menu=self.barra)




display = tk.Tk()
Tela(display)
display.mainloop()