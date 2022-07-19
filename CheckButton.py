import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela CheckButton")
        self.janela.minsize(400,400)
        self.v1 = tk.IntVar()
        self.v2 = tk.IntVar()
        self.ckb1 = tk.Checkbutton(self.janela,text="Opção 1", variable=self.v1).pack()
        self.ckb2 = tk.Checkbutton(self.janela,text="Opção 2", variable=self.v2).pack()

display = tk.Tk()
Tela(display)
display.mainloop()