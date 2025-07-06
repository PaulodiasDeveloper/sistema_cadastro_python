from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox

from tkinter import filedialog as fd


# Importando Pillow
from PIL import Image, ImageTk

# Importando Tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# importando view
from view import *


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

# Criando funções ------------------
global tree

# Função inserir


def inserir():
    global imagem, imagem_string, l_imagem

    nome = entrada_nome.get()
    local = entrada_local.get()
    descricao = entrada_descricao.get()
    modelo = entrada_modelo.get()
    data_compra = entrada_calendario.get()  # Obtendo a data do calendário
    valor_compra = entrada_valor_compra.get()
    serial = entrada_serial.get()   # Obtendo o número de série
    imagem = imagem_string  # Obtendo a imagem carregada

    lista_inserir = [nome, local, descricao, modelo,
                     data_compra, valor_compra, serial, imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos!')
            return
    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso', 'Item adicionado com sucesso!')

    entrada_nome.delete(0, END)
    entrada_local.delete(0, END)
    entrada_descricao.delete(0, END)
    entrada_modelo.delete(0, END)
    entrada_calendario.delete(0, END)
    entrada_valor_compra.delete(0, END)
    entrada_serial.delete(0, END)

    mostrar()  # Atualizando a tabela com os novos dados


# Função atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()  # Obtendo o item selecionado na tabela
        # Obtendo os dados do item selecionado
        treev_dicionario = tree.item(treev_dados)
        # Obtendo os valores do item selecionado
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]  # Obtendo o ID do item selecionado

        entrada_nome.delete(0, END)
        entrada_local.delete(0, END)
        entrada_descricao.delete(0, END)
        entrada_modelo.delete(0, END)
        entrada_calendario.delete(0, END)
        entrada_valor_compra.delete(0, END)
        entrada_serial.delete(0, END)

        id = int(treev_lista[0])  # Convertendo o ID para inteiro
        entrada_nome.insert(0, treev_lista[1])
        entrada_local.insert(0, treev_lista[2])
        entrada_descricao.insert(0, treev_lista[3])
        entrada_modelo.insert(0, treev_lista[4])
        entrada_calendario.insert(0, treev_lista[5])
        entrada_valor_compra.insert(0, treev_lista[6])
        entrada_serial.insert(0, treev_lista[7])
        imagem_string = treev_lista[8]  # Obtendo a imagem do item selecionado

        def update():
            global imagem, imagem_string, l_imagem

            nome = entrada_nome.get()
            local = entrada_local.get()
            descricao = entrada_descricao.get()
            modelo = entrada_modelo.get()
            data_compra = entrada_calendario.get()
            valor_compra = entrada_valor_compra.get()
            serial = entrada_serial.get()
            imagem = imagem_string

            if imagem == '':
                imagem = entrada_serial.insert(0, treev_lista[7])

            lista_atualizar = [nome, local, descricao, modelo,
                               data_compra, valor_compra, serial, imagem, id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos!')
                    return
            atualizar_(lista_atualizar)

            messagebox.showinfo('Sucesso', 'Item atualizado com sucesso!')

            entrada_nome.delete(0, END)
            entrada_local.delete(0, END)
            entrada_descricao.delete(0, END)
            entrada_modelo.delete(0, END)
            entrada_calendario.delete(0, END)
            entrada_valor_compra.delete(0, END)
            entrada_serial.delete(0, END)

            b_confirmar.destroy()  # Removendo o botão de confirmação

            mostrar()  # Atualizando a tabela com os novos dados

        b_confirmar = Button(frameMeio, command=update, width=13, text='  Confirmar'.upper(
        ), overrelief=RIDGE, font=('Ivy 8 bold'), bg=co2, fg=co1)
        b_confirmar.place(x=400, y=185)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item para atualizar!')


# Função deletar
def deletar():
    try:
        treev_dados = tree.focus()  # Obtendo o item selecionado na tabela
        # Obtendo os dados do item selecionado
        treev_dicionario = tree.item(treev_dados)
        # Obtendo os valores do item selecionado
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]  # Obtendo o ID do item selecionado

        deletar_form([valor])  # Convertendo o ID para inteiro

        messagebox.showinfo('Sucesso', 'Item deletado com sucesso!')

        mostrar()  # Atualizando a tabela com os novos dados

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item da tabela!')


# Função para escolher imagem
global imagem_string, l_imagem


def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    # Abrindo Imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((150, 150))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=735, y=10)


# Função para ver imgem
def ver_imagem():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()  # Obtendo o item selecionado na tabela
    # Obtendo os dados do item selecionado
    treev_dicionario = tree.item(treev_dados)
    # Obtendo os valores do item selecionado
    treev_lista = treev_dicionario['values']

    id_item = int(treev_lista[0])

    item = ver_item(id_item)

    if not item or not item[8]:
        messagebox.showwarning(
            'Aviso', 'Este item não possui imagem associada.')
        return

    imagem = item[8]
    # Abrindo Imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((150, 150))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=740, y=10)


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
nome = Label(frameMeio, text='Nome', height=1,
             anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
nome.place(x=10, y=10)

entrada_nome = Entry(frameMeio, width=30, justify='left',
                     relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_nome.place(x=140, y=10)


local = Label(frameMeio, text='Sala/Área', height=1,
              anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
local.place(x=10, y=45)

entrada_local = Entry(frameMeio, width=30, justify='left',
                      relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_local.place(x=140, y=45)


descricao = Label(frameMeio, text='Descrição', height=1,
                  anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
descricao.place(x=10, y=80)

entrada_descricao = Entry(frameMeio, width=30, justify='left',
                          relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_descricao.place(x=140, y=80)


modelo = Label(frameMeio, text='Modelo', height=1,
               anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
modelo.place(x=10, y=115)

entrada_modelo = Entry(frameMeio, width=30, justify='left',
                       relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_modelo.place(x=140, y=115)


# Criando Calendário
calendario = Label(frameMeio, text='Data da compra', height=1,
                   anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
calendario.place(x=10, y=145)

entrada_calendario = DateEntry(frameMeio, width=12, background='darkblue',
                               foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy',
                               year=date.today().year, month=date.today().month, day=date.today().day,
                               relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_calendario.place(x=140, y=145)


valor_compra = Label(frameMeio, text='Valor da compra', height=1,
                     anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
valor_compra.place(x=10, y=175)

entrada_valor_compra = Entry(frameMeio, width=30, justify='left',
                             relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_valor_compra.place(x=140, y=175)


serial = Label(frameMeio, text='Número de Série', height=1,
               anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
serial.place(x=10, y=210)

entrada_serial = Entry(frameMeio, width=30, justify='left',
                       relief="solid", font=('Verdana 10'), bg=co1, fg=co0)
entrada_serial.place(x=140, y=210)


# Criando botões-----------------------

# Botão carregar
carregar_imagem = Label(frameMeio, text='Imagem do Item', height=1,
                        anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
carregar_imagem.place(x=10, y=240)

carregar_imagem = Button(frameMeio, command=escolher_imagem, width=39, text='carregar'.upper(), compound=CENTER,
                         anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
carregar_imagem.place(x=140, y=240)


# Botão inserir
img_add = Image.open("./assets/img/plus.png")
img_add = img_add.resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(frameMeio, command=inserir, image=img_add, width=95, text='  ADICIONAR'.upper(), compound=LEFT,
                   anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=400, y=10)


# Botão atualizar
img_update = Image.open("./assets/img/sync.png")
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)

b_update = Button(frameMeio, command=atualizar, image=img_update, width=95, text='  ATUALIZAR'.upper(), compound=LEFT,
                  anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_update.place(x=400, y=50)


# Botão deletar
img_delete = Image.open("./assets/img/delete.png")
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)

b_delete = Button(frameMeio, command=deletar, image=img_delete, width=95, text='  DELETAR'.upper(), compound=LEFT,
                  anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_delete.place(x=400, y=90)


# Botão ver imagem
img_item = Image.open("./assets/img/item.png")
img_item = img_item.resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)

b_item = Button(frameMeio, command=ver_imagem, image=img_item, width=95, text='  Ver item'.upper(), compound=LEFT,
                anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_item.place(x=400, y=237)


# Label quantidade total e valores
l_total = Label(frameMeio, text='', width=22, height=4,
                anchor=CENTER, font=('Verdana 10 bold'), bg=co7, fg=co1)
l_total.place(x=520, y=10)

l_total_ = Label(frameMeio, text='Valor Total dos itens', height=1,
                 anchor=NW, font=('Verdana 10 bold'), bg=co7, fg=co1)
l_total_.place(x=545, y=10)


l_qtd = Label(frameMeio, text='', width=22, height=4, pady=3,
              anchor=CENTER, font=('Verdana 10 bold'), bg=co7, fg=co1)
l_qtd.place(x=520, y=90)

l_qtd_ = Label(frameMeio, text='Quantidade total de itens', height=1,
               anchor=NW, font=('Verdana 10 bold'), bg=co7, fg=co1)
l_qtd_.place(x=525, y=92)


# tabela -----------------------------------------------------------
def mostrar():
    global tree

    # creating a treeview with dual scrollbars
    tabela_head = ['#Item', 'Nome',  'Sala/Área', 'Descrição',
                   'Marca/Modelo', 'Data da compra', 'Valor da compra', 'Número de série']

    lista_itens = ver_form()

    tree = ttk.Treeview(frameBaixo, selectmode="extended",
                        columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd = ["center", "center", "center", "center",
          "center", "center", "center", 'center']
    h = [40, 150, 100, 160, 130, 100, 100, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    # Inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)

    valores = []
    for item in lista_itens:
        try:
            # A coluna 6 corresponde ao 'valor_da_compra'
            valor_str = str(item[6]).replace(',', '.')
            valores.append(float(valor_str))
        except (ValueError, TypeError):
            # Ignora valores que não podem ser convertidos para float
            continue

    Total_valor = sum(valores)
    Total_itens = len(lista_itens)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens


mostrar()


janela.mainloop()
