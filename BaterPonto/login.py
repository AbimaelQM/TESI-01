import tkinter as tk
from home import TelaHome

class TelaLogin:
    def __init__(self, master):
        self.tela_login = master
        self.tela_login.title("Login")
        # self.tela_login.geometry("600x500")

        self.centro = tk.Frame(self.tela_login)
        self.centro.pack(padx=6,pady=6)

        self.lbl_usuario = tk.Label(self.centro, text="Usuário:", font=20)
        self.lbl_usuario.grid(row=0, column=0, sticky=tk.W)
        self.ent_usuario = tk.Entry(self.centro, width=40)
        self.ent_usuario.grid(row=1, column=0, padx=4)
        self.lbl_senha = tk.Label(self.centro, text="Senha:", font=20)
        self.lbl_senha.grid(row=2, column=0, sticky=tk.W)
        self.ent_senha = tk.Entry(self.centro, width=40)
        self.ent_senha.grid(row=3, column=0, padx=4)

        self.frm_login = tk.Frame(self.tela_login)
        self.frm_login.pack()
        self.btn_login = tk.Button(self.centro, text="Login", width=10, height=1, command=self.logar)
        # self.btn_login.pack()
        self.btn_login.grid(row=4, column=0,pady=5)


    def logar(self):
        topLogar = tk.Toplevel(self.tela_login)
        TelaHome(topLogar)
        self.tela_login.grab_set()
        self.tela_login.withdraw()



