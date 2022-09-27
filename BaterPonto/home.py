import tkinter as tk

class TelaHome:
    def __init__(self, master):
        self.tela_home = master
        self.tela_home.title("Home")
        self.tela_home.geometry("600x400")

        self.frm_botoes = tk.Frame(self.tela_home)
        self.frm_botoes.pack()

        self.btn_checkin = tk.Button(self.frm_botoes, text="Check In", height=4, width=16)
        self.btn_checkin.pack(side=tk.LEFT)
        self.btn_checkout = tk.Button(self.frm_botoes, text="Check Out", height=4, width=16)
        self.btn_checkout.pack(side=tk.LEFT)
        self.btn_relatorio = tk.Button(self.frm_botoes, text="Relatório", height=4, width=16)
        self.btn_relatorio.pack(side=tk.LEFT)

