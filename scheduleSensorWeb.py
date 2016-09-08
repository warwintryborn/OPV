import schedule
import time
import sqlite3
from sensorWeb import *

def insertDB():

    conn = sqlite3.connect('dbOPV.db')
    cursor = conn.cursor()

    #DADOS DA LOCALIZAÇÃO WEB
    sensorSP = sensorWeb('SaoPaulo,br')
    horario = sensorSP.getDate()
    temperatura = sensorSP.getTempValor()
    temperaturaMinima = sensorSP.getTempMin()
    temperaturaMaxima = sensorSP.getTempMax()
    humidade = sensorSP.getHumidade()    


    #INSERIR DADOS NA TABELA
    cursor.execute("""
    INSERT INTO sensorWeb (localizacao, horario, temperatura, temperaturaMinima, temperaturaMaxima, humidade)
    VALUES (?, ?, ?, ?, ?, ?)
    """, ('SaoPaulo,br', horario, temperatura, temperaturaMinima, temperaturaMaxima, humidade))

    conn.commit()

    print(temperatura)
    print(temperaturaMinima)
    print(temperaturaMaxima)
    print(humidade)
    print(horario)

    print('DADOS INSERIDOS COM SUCESSO')

    conn.close()


schedule.every(150).seconds.do(insertDB)

while True:
    schedule.run_pending()
    time.sleep(1)
