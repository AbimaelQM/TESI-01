import datetime
import tkinter as tk

class TelaCheckin:
    def __init__(self, master):
        self.tela_checkin = master
        self.tela_checkin.title("Check In")
        self.tela_checkin.geometry("300x200")

        self.frm = tk.Frame(self.tela_checkin)
        self.frm.pack(pady=(10, 50), padx=(0, 70))

        self.lbl_nome = tk.Label(self.frm, text="Nome:", font=("Roboto", 10,"bold"))
        self.lbl_nome.pack(anchor=tk.W)
        self.lbl_usuario = tk.Label(self.frm, text="Abimael de Queiroz Lima", font=("Roboto", 10))
        self.lbl_usuario.pack(anchor=tk.W, padx=(10, 0))

        self.hora_atual = datetime.datetime.now()
        self.hora_atual_str = self.hora_atual.strftime("%H:%M:%S %d/%m/%Y")

        self.lbl_hora_ent = tk.Label(self.frm, text="Horário de entrada:", font=("Roboto", 10, "bold"))
        self.lbl_hora_ent.pack(anchor=tk.W)
        self.lbl_hora = tk.Label(self.frm, text=self.hora_atual_str, font=("Roboto", 10))
        self.lbl_hora.pack(anchor=tk.W, padx=(10, 0))


