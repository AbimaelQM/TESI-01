import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import dbConnection as db


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Cadastro de clientes")
        self.janela.geometry("400x400")

        self.frm = tk.Frame(self.janela)
        self.frm.pack()
        self.frm_btn = tk.Frame(self.janela)
        self.frm_btn.pack()

        self.lbl_nome = tk.Label(self.frm, text="Nome:")
        self.lbl_nome.grid(column=0, row=0)
        self.ent_nome = tk.Entry(self.frm, width=40)
        self.ent_nome.grid(column=1, row=0, columnspan=2)

        self.lbl_cpf = tk.Label(self.frm, text="CPF:")
        self.lbl_cpf.grid(column=0, row=1)
        self.ent_cpf = tk.Entry(self.frm, width=40)
        self.ent_cpf.grid(column=1, row=1, columnspan=2)

        self.btn_inserir = tk.Button(self.frm, text="Inserir", command=self.inserir, width=20)
        self.btn_inserir.grid(column=2, row=2, sticky=tk.E)

        colunas = ['id', 'nome', 'cpf']
        self.tvw = ttk.Treeview(self.frm, show='headings', columns=colunas)
        self.tvw.grid(column=0, row=3, columnspan=3)

        # cabeçalho
        self.tvw.heading('id', text="ID")
        self.tvw.heading('nome', text="Nome")
        self.tvw.heading('cpf', text="CPF")

        self.tvw.column('id', minwidth=0, width=100)
        self.tvw.column('nome', minwidth=0, width=150)
        self.tvw.column('cpf', minwidth=0, width=150)

        self.atualizar_tvw()
        self.btn_remover = tk.Button(self.frm_btn, text="Remover", command=self.remover)
        self.btn_remover.pack(side=tk.LEFT)
        self.btn_atualizar = tk.Button(self.frm_btn, text="Atualizar", command=self.atualizar_item)
        self.btn_atualizar.pack(side=tk.LEFT)
        self.btn_confirmar = tk.Button(self.frm_btn, text="Confirmar", command=self.confirmar)
        self.btn_confirmar['state'] = tk.DISABLED
        self.btn_confirmar.pack(side=tk.LEFT)
        self.btn_cancelar = tk.Button(self.frm_btn, text="Cancelar", command=self.cancelar)
        self.btn_cancelar['state'] = tk.DISABLED
        self.btn_cancelar.pack(side=tk.LEFT)

    def atualizar_tvw(self):
        for i in self.tvw.get_children():
            self.tvw.delete(i)
        query = 'SELECT * FROM cliente;'
        dados = db.query(query)
        for linha in dados:
            self.tvw.insert('', 'end', values=linha)

    def inserir(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        sql_inserir = f'INSERT INTO cliente(nome, cpf) VALUES ("{nome}", "{cpf}");'
        db.insert(sql_inserir)
        messagebox.showinfo("Aviso", "Cliente inserido com sucesso!")
        self.limpar_campos()
        self.atualizar_tvw()

    def atualizar_item(self):
        selecionado = self.tvw.selection()
        nome = self.tvw.item(selecionado, 'values')[1]
        cpf = self.tvw.item(selecionado, 'values')[2]
        self.ent_nome.insert(0, nome)
        self.ent_cpf.insert(0, cpf)
        self.btn_confirmar['state'] = tk.NORMAL
        self.btn_cancelar['state'] = tk.NORMAL
        self.btn_atualizar['state'] = tk.DISABLED
        self.btn_remover['state'] = tk.DISABLED
        self.btn_inserir['state'] = tk.DISABLED

    def confirmar(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        selecionado = self.tvw.selection()
        id = self.tvw.item(selecionado, 'values')[0]
        update = f'UPDATE cliente SET nome="{nome}",cpf="{cpf}" WHERE id={id};'
        db.update(update)
        messagebox.showinfo("Aviso", "Cliente atualizado com sucesso!")
        self.btn_atualizar['state'] = tk.NORMAL
        self.btn_inserir['state'] = tk.NORMAL
        self.btn_remover['state'] = tk.NORMAL
        self.btn_cancelar['state'] = tk.DISABLED
        self.btn_confirmar['state'] = tk.DISABLED
        self.limpar_campos()
        self.atualizar_tvw()

    def cancelar(self):
        self.limpar_campos()
        self.btn_atualizar['state'] = tk.NORMAL
        self.btn_inserir['state'] = tk.NORMAL
        self.btn_remover['state'] = tk.NORMAL
        self.btn_confirmar['state'] = tk.DISABLED
        self.btn_cancelar['state'] = tk.DISABLED

    def remover(self):
        selecionado = self.tvw.selection()
        item = self.tvw.item(selecionado, 'values')
        id = item[0]
        delete = f'DELETE FROM cliente WHERE id={id}'
        db.delete(delete)
        messagebox.showinfo("Aviso", "Cliente excluido com sucesso!")
        self.atualizar_tvw()

    def limpar_campos(self):
        self.ent_nome.delete(0, "end")
        self.ent_cpf.delete(0, "end")


display = tk.Tk()
Tela(display)
display.mainloop()
