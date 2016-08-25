import schedule
import time
from sensorWeb import *

def insertDB():
    sensorSP = sensorWeb('SaoPaulo,br')
    print("Temperatura: {0} °C".format(sensorSP.getTempValor()))

schedule.every(1).seconds.do(insertDB)


while True:
    schedule.run_pending()
    time.sleep(1)
