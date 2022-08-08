import tkinter as tk
from tkinter import messagebox

def info():
    messagebox.showinfo("Exemplo info", "Aqui jas um prescritor")

def aviso():
    messagebox.showwarning("Aviso", "Deu erro aqui po")

def pergunta():
    teste = messagebox.askquestion("Pergunta", "Quer escolher?")
    print(teste)


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("MessageBox")
        self.janela.geometry("300x300")
        self.btn1 = tk.Button(self.janela, text="Informação", command=info)
        self.btn1.pack()
        self.btn2 = tk.Button(self.janela, text="Aviso", command=aviso)
        self.btn2.pack()
        self.btn3 = tk.Button(self.janela, text="Pergunta", command=pergunta)
        self.btn3.pack()


janela_pricipal = tk.Tk()
Tela(janela_pricipal)
janela_pricipal.mainloop()
