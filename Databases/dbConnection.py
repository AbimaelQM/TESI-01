import sqlite3 as sq
from sqlite3 import Error


def conexao():
    caminho = "../bancoA.db"

    try:
        con = None
        con = sq.connect(caminho)
        return con
    except Error as error:
        print(error)

sql_insert = "INSERT INTO cliente VALUES(4, 'Teste', '11111111111');"
sql_table = '''CREATE TABLE cçiente(
                id INTEGER PRIMARY KEY,
                nome VARCHAR(60) NOT NULL,
                cpf VARCHAR(11) NOT NULL);
'''

def insert(sql):
    con = conexao()
    cursor =  con.cursor()
    cursor.execute(sql)
    con.commit()
    print("Registro inserido com sucesso!")

def tabela(sql):
    con = conexao()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    print("Tabela criada!")
    con.close()

tabela(sql_table)
insert(sql_insert)