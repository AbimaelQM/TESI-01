import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as ms


class Display:
    def __int__(self, master):
        self.janela = master
        self.janela.title("Janela CheckButton")
        self.janela.geometry("300x150")

        self.btn = tk.Button(self.janela, text="Mostrar arquivo", command=self.mostrar_arquivo)
        self.btn.pack()
        self.btn1 = tk.Button(self.janela, text="Mostrar arquivo", command=self.carregar_arquivo)
        self.btn1.pack()

    def mostrar_arquivo(self):
        nome_arquivo = fd.askopenfilename()
        ms.showinfo('Aviso', f'{nome_arquivo}')

    def carregar_arquivo(self):
        tipos = ('Texto', '*.txt'), ('Python','*.py')
        arquivo = fd.askopenfile(initialdir="/home/abimael.lima/telas", filetypes=tipos)
        with open(arquivo, 'r') as arq:
            print(arq.readline())



display = tk.Tk()
Display(display)
display.mainloop()