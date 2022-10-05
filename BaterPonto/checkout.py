import datetime
import tkinter as tk


class TelaCheckout:
    def __init__(self, master):
        self.tela_checkout = master
        self.tela_checkout.title("Check Out")
        self.tela_checkout.geometry("300x200")
        self.tela_checkout.configure(background='white')

        self.frm = tk.Frame(self.tela_checkout)
        self.frm.configure(background='white')
        self.frm.pack(pady=(10, 50), padx=(0, 70))

        self.frm_btn_out = tk.Frame(self.tela_checkout)
        # self.frm_btn_out.configure(background='white')
        self.frm_btn_out.pack(pady=(10, 10), padx=(70, 70))

        self.lbl_nome = tk.Label(self.frm, text="Nome:", font=("Roboto", 10, "bold"), bg="white")
        self.lbl_nome.pack(anchor=tk.W)
        self.lbl_usuario = tk.Label(self.frm, text="Abimael de Queiroz Lima", font=("Roboto", 10), bg="#fffffd", borderwidth=2, relief="sunken")
        self.lbl_usuario.pack(anchor=tk.W, padx=(10, 0))

        self.hora_atual = datetime.datetime.now()
        self.hora_atual_str = self.hora_atual.strftime("%H:%M:%S %d/%m/%Y")

        self.lbl_hora_out = tk.Label(self.frm, text="Horário de saída:", font=("Roboto", 10, "bold"), bg="white")
        self.lbl_hora_out.pack(anchor=tk.W)
        self.lbl_hora = tk.Label(self.frm, text=self.hora_atual_str, font=("Roboto", 10), bg="#fffffa", borderwidth=2, relief="sunken")
        self.lbl_hora.pack(anchor=tk.W, padx=(10, 0))

        self.btn_out = tk.Button(self.frm_btn_out, text="Check Out", width=10, height=10, font=("Roboto" , 10, "bold"))
        self.btn_out.pack()
