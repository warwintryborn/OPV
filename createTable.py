import sqlite3

#CONEXÃO COM O BANCO DE DADOS
conn = sqlite3.connect('dbOPV.db')

#DEFININDO UM CURSOR
cursor = conn.cursor()

#CRIANDO A TABELA
cursor.execute("""
CREATE TABLE sensorWeb (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    localizacao VARCHAR(50),
    horario DATETIME,
    temperatura FLOAT,
    temperaturaMinima FLOAT,
    temperaturaMaxima FLOAT,
    humidade INT
);
""")

print('TABELA CRIADA COM SUCESSO')

conn.close()
