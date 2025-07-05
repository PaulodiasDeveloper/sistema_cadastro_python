from tkinter import *
from tkinter import Tk, StringVar, ttk

# Importando Pillow
from PIL import Image, ImageTk

# Importando Tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

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

# Trabalhando no frame cima--------------------------

# Abrindo Imagem
app_img = Image.open("./assets/img/inventory2.png")
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)


app_logo = Label(frameCima, image=app_img, text=' Inventário Doméstico', width=900,
                 compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co7, fg=co1)
app_logo.place(x=0, y=0)


# Trabalhando no frame do meio-----------------------

# Criando entradas
primeiro_nome = Label(frameMeio, text='Nome', height=1,
                      anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
primeiro_nome.place(x=10, y=10)

entrada_nome = Entry(frameMeio, width=30, justify='left',
                     relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_nome.place(x=140, y=11)


local = Label(frameMeio, text='Sala/Área', height=1,
              anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
local.place(x=10, y=50)

entrada_local = Entry(frameMeio, width=30, justify='left',
                      relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_local.place(x=140, y=50)


descricao = Label(frameMeio, text='Descrição', height=1,
                  anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
descricao.place(x=10, y=90)

entrada_descricao = Entry(frameMeio, width=30, justify='left',
                          relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_descricao.place(x=140, y=90)


modelo = Label(frameMeio, text='Modelo', height=1,
               anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
modelo.place(x=10, y=130)

entrada_modelo = Entry(frameMeio, width=30, justify='left',
                       relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_modelo.place(x=140, y=130)


# Criando Calendário
calendario = Label(frameMeio, text='Data da compra', height=1,
                   anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
calendario.place(x=10, y=170)

entrada_calendario = DateEntry(frameMeio, width=12, background='darkblue',
                               foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy',
                               year=date.today().year, month=date.today().month, day=date.today().day,
                               relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_calendario.place(x=140, y=170)


valor_compra = Label(frameMeio, text='Valor da compra', height=1,
                     anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
valor_compra.place(x=10, y=210)

entrada_valor_compra = Entry(frameMeio, width=30, justify='left',
                             relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_valor_compra.place(x=140, y=210)


serial = Label(frameMeio, text='Número de Série', height=1,
               anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
serial.place(x=10, y=250)

entrada_serial = Entry(frameMeio, width=30, justify='left',
                       relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_serial.place(x=140, y=250)


janela.mainloop()
