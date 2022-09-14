import tkinter as tk
from tkinter import messagebox

from Databases.dbConnection import insert
import Databases.dbConnection as db

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title("Cadastro de clientes")
        self.janela.geometry("400x400")

        self.frm = tk.Frame(self.janela)
        self.frm.pack()

        self.lbl_nome = tk.Label(self.frm, text="Nome:")
        self.lbl_nome.grid(column=0, row=0)
        self.ent_nome = tk.Entry(self.frm, width=40)
        self.ent_nome.grid(column=1, row=0, columnspan=2)

        self.lbl_cpf = tk.Label(self.frm, text="CPF:")
        self.lbl_cpf.grid(column=0, row=1)
        self.ent_cpf = tk.Entry(self.frm, width=40)
        self.ent_cpf.grid(column=1, row=1, columnspan=2)

        self.btn_inserir = tk.Button(self.frm, text="Inserir", command=self.inserir, width=20)
        self.btn_inserir.grid(column=2, row=2,sticky=tk.E)

    def inserir(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        sql_inserir = f'INSERT INTO cliente(nome, cpf) VALUES ("{nome}", "{cpf}");'
        insert(sql_inserir)
        messagebox.showinfo("Aviso", "Cliente inserido com sucesso!")


display = tk.Tk()
Tela(display)
display.mainloop()