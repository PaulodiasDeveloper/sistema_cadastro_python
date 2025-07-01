# importando sqlite
import sqlite3 as lite

# criando a conexao com o banco de dados
con = lite.connect('dados.db')

# criando a tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_da_compra DATE, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")
