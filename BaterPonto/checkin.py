import datetime
import tkinter as tk

class TelaCheckin:
    def __init__(self, master):
        self.tela_checkin = master
        self.tela_checkin.title("Check In")
        self.tela_checkin.geometry("300x200")
        self.tela_checkin.configure(background='white')

        self.frm = tk.Frame(self.tela_checkin)
        self.frm.configure(background='white')
        self.frm.pack(pady=(10, 50), padx=(0, 70))

        self.frm_btn_in = tk.Frame(self.tela_checkin)
        # self.frm_btn_out.configure(background='white')
        self.frm_btn_in.pack(pady=(10, 10), padx=(70, 70))

        self.lbl_nome = tk.Label(self.frm, text="Nome:", font=("Roboto", 10,"bold"), bg="white")
        self.lbl_nome.pack(anchor=tk.W)
        self.lbl_usuario = tk.Label(self.frm, text="Abimael de Queiroz Lima", font=("Roboto", 10), bg="#fffffd", borderwidth=2, relief="sunken")
        self.lbl_usuario.pack(anchor=tk.W, padx=(10, 0))

        self.hora_atual = datetime.datetime.now()
        self.hora_atual_str = self.hora_atual.strftime("%H:%M:%S %d/%m/%Y")

        self.lbl_hora_in = tk.Label(self.frm, text="Horário de entrada:", font=("Roboto", 10, "bold"), bg="white")
        self.lbl_hora_in.pack(anchor=tk.W)
        self.lbl_hora = tk.Label(self.frm, text=self.hora_atual_str, font=("Roboto", 10), bg="#fffffd", borderwidth=2, relief="sunken")
        self.lbl_hora.pack(anchor=tk.W, padx=(10, 0))

        self.btn_in = tk.Button(self.frm_btn_in, text="Check In", width=10, height=10, font=("Roboto" , 10, "bold"))
        self.btn_in.pack()

