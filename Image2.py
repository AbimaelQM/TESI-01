import tkinter as tk
from PIL import Image, ImageTk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Janela")
        self.janela.geometry("326x480")
        self.img = Image.open("image.jpg")
        self.minha_imagem = ImageTk.PhotoImage(self.img)
        self.lbl = tk.Label(self.janela, image=self.minha_imagem)
        self.lbl.image = self.minha_imagem
        self.lbl.pack()


janela_pricipal = tk.Tk()
Tela(janela_pricipal)
janela_pricipal.mainloop()
