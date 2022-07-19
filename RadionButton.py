import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela RadionButton")
        self.janela.minsize(400,400)
        self.v = tk.StringVar(self.janela, "1")
        self.rbt_1 = tk.Radiobutton(self.janela, text="Opção 1", value="1", variable=self.v).pack()
        self.rbt_1 = tk.Radiobutton(self.janela, text="Opção 2", value="2", variable=self.v).pack()
        self.rbt_1 = tk.Radiobutton(self.janela, text="Opção 3", value="3", variable=self.v).pack()

display = tk.Tk()
Tela(display)
display.mainloop()