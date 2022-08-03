import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela")
        self.janela.geometry("300x300")
        self.fm1 = tk.LabelFrame(self.janela)
        self.fm1.pack()
        self.fm2 = tk.LabelFrame(self.janela)
        self.fm2.pack()


        self.btn1 = tk.Button(self.fm1, text="Adicionar")
        self.btn1.pack(side=tk.LEFT)
        self.btn2 = tk.Button(self.fm1, text="Editar")
        self.btn2.pack(side=tk.LEFT)
        self.btn3 = tk.Button(self.fm1, text="Remover")
        self.btn3.pack(side=tk.LEFT)


        self.btn4 = tk.Button(self.fm2, text="Salvar")
        self.btn4.pack(side=tk.BOTTOM)
        self.btn5 = tk.Button(self.fm2, text="Fechar")
        self.btn5.pack(side=tk.BOTTOM)
        self.btn6 = tk.Button(self.fm2, text="Listar")
        self.btn6.pack(side=tk.BOTTOM)

display = tk.Tk()
Tela(display)
display.mainloop()