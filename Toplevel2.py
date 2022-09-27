import tkinter as tk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela")
        self.janela.geometry("300x300")
        self.btn = tk.Button(self.janela, text="Abrir janela", command=self.abrir_toplevel)
        self.btn.pack()

    def abrir_toplevel(self):

        # self.janela.iconify()
        self.janela.grab_set()
        self.janela.withdraw()
        self.janela_secundaria = tk.Toplevel()
        self.janela_secundaria.title("TOP")
        self.janela_secundaria.geometry("300x300")
        self.btn1 = tk.Button(self.janela_secundaria, text="Voltar", command=self.fechar_top)
        self.btn1.pack()

    def fechar_top(self):
        self.janela_secundaria.destroy()
        self.janela.deiconify()


janela_pricipal = tk.Tk()
Tela(janela_pricipal)
janela_pricipal.mainloop()
