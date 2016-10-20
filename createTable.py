import sqlite3

#CONEXÃO COM O BANCO DE DADOS
conn = sqlite3.connect('dbOPV.db')

#DEFININDO UM CURSOR
cursor = conn.cursor()

#CRIANDO A TABELA
cursor.execute("""
CREATE TABLE sensorWeb (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    horario DATETIME,
    temperatura FLOAT,
    status TEXT,
    vento FLOAT,
    umidade INT
);
""")

print('TABELA CRIADA COM SUCESSO')

conn.close()
