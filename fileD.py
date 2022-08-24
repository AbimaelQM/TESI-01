import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as ms
from tkinter.scrolledtext import ScrolledText


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela CheckButton")
        self.janela.geometry("300x450")

        self.btn = tk.Button(self.janela, text="Mostrar arquivo", command=self.mostrar_arquivo)
        self.btn.pack()
        self.btn1 = tk.Button(self.janela, text="Carregar arquivo", command=self.carregar_arquivo)
        self.btn1.pack()
        self.sct = ScrolledText(self.janela, height=20)
        self.sct.pack()
        self.btn2 = tk.Button(self.janela, text="Salvar arquivo", command=self.salvar_arquivo)
        self.btn2.pack()

    def mostrar_arquivo(self):
        nome_arquivo = fd.askopenfilename()
        ms.showinfo('Aviso', f'{nome_arquivo}')

    def carregar_arquivo(self):
        tipos = ('Texto', '*.txt'), ('Python', '*.py')
        arquivo = fd.askopenfile(initialdir="/home/abimael.lima/telas", filetypes=tipos)
        with open(arquivo.name, 'r') as arq:
            for linha in arq:
                self.sct.insert(tk.END, linha)

            # print(arq.readlines())
            # for linha in arq:
            #     print(linha)

    def salvar_arquivo(self):
        arquivo = fd.asksaveasfile()
        with open(arquivo.name, 'w') as arq:
            arq.write(self.sct.get('1.0',tk.END))


app = tk.Tk()
Tela(app)
app.mainloop()