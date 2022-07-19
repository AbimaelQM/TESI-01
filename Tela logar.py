import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela")
        self.janela.minsize(400,100)
        self.lbl_nome = tk.Label(self.janela, text="Nome:", font=("calibre", 12, "bold"))
        self.lbl_nome.pack()
        self.ent_nome = tk.Entry(self.janela, width=20).pack()
        self.lbl_senha = tk.Label(self.janela, text="Senha:", font=("Calibre", 12, "bold")).pack()
        self.ent_senha = tk.Entry(self.janela, width=15, show="10").pack()
        self.btn_logar = tk.Button(self.janela, text="Logar", command=self.janela.destroy).pack()

display = tk.Tk()
Tela(display)
display.mainloop()