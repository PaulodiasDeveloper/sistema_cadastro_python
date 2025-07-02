from tkinter import *
from tkinter import Tk, StringVar, ttk

from PIL import Image, ImageTk


# Paleta de Cores Definida:**

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # Azul
co7 = "#3fbfb9"  # Verde - Padrão
co8 = "#263238"  # Verde - Escuro/Adição
co9 = "#e9edf5"  # Verde - Claro/Adição

# Criando janela principal
janela = Tk()
janela.title("")
janela.geometry("900x600")
janela.configure(bg=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frames

frameCima = Frame(janela, bg=co7, width=1043, height=50, relief="flat")
frameCima.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)

frameMeio = Frame(janela, bg=co1, width=1043,
                  height=303, pady=20, relief="flat")
frameMeio.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

frameBaixo = Frame(janela, bg=co1, width=1043,
                   height=300, relief="flat")
frameBaixo.grid(row=2, column=0, padx=1, pady=0, sticky=NSEW)


# Abrindo Imagem
app_img = Image.open("./assets/img/inventory2.png")
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)


app_logo = Label(frameCima, image=app_img, text=' Inventário Doméstico', width=900,
                 compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co7, fg=co1)
app_logo.place(x=0, y=0)


janela.mainloop()
