import sqlite3 as sq
from sqlite3 import Error


def conexao():
    caminho = "../../bancoA.db"

    try:
        con = None
        con = sq.connect(caminho)
        return con
    except Error as error:
        print(error)


sql_queryAll = 'SELECT * FROM cliente'
sql_update = 'UPDATE cliente SET nome="Bill" WHERE id=5;'
sql_delete = 'DELETE FROM cliente WHERE id=4;'
sql_insert = "INSERT INTO cliente( nome, cpf) VALUES('Bill', '11111111111');"
sql_table = '''CREATE TABLE cliente(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(60) NOT NULL,
                cpf VARCHAR(11) NOT NULL);
'''


def query(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado
    except Error as error:
        print(error)


def insert(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Registro inserido com sucesso!")
    except Error as er:
        print(er)


def tabela(sql):
    con = conexao()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    print("Tabela criada!")
    con.close()


def delete(sql):
    con = conexao()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    print("Registro excluido com sucesso!")


def update(sql):
    con = conexao()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    print("Registro atualizado com sucesso!")


# tabela(sql_table)
# insert(sql_insert)
# update(sql_update)
# for i in consulta(sql_consultas):
#     print (i)
