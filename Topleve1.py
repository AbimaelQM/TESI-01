import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela")
        self.janela.geometry("300x300")
        self.btn = tk.Button(self.janela, text="abrir janela", command=self.abrir_toplevel)
        self.btn.pack()


    def abrir_toplevel(self):
        self.janela_secundaria = tk.Toplevel()
        self.janela_secundaria.title("TOP")
        self.janela_secundaria.geometry("300x300")


janela_pricipal = tk.Tk()
Tela(janela_pricipal)
janela_pricipal.mainloop()

