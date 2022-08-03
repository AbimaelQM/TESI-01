import tkinter as tk

app = tk.Tk()
app.title("Exemplo LabelFrame")
app.geometry("300x300")

lfr = tk.LabelFrame(app,text="Alinhamento", labelanchor=tk.SW)
lfr.pack()


rbt1 = tk.Radiobutton(lfr, text="LEFT")
rbt1.pack(side=tk.LEFT)

rbt2 = tk.Radiobutton(lfr, text="CENTER")
rbt2.pack(side=tk.LEFT)

rb3 = tk.Radiobutton(lfr, text="RIGHT")
rb3.pack(side=tk.LEFT)

app.mainloop()