#1o Passo: Criar o Arquivo .ui no PyQT5
#2o Passo: Transformar para .py
## Para isso abra o prompt de comando, te vire como:
### vá para o diretório que salvou o arquivo .ui, dica: use cd "caminho do diretório"
#### use o comando: pyuic5 -x arquivodopyqt.ui -o arquivodopyqt.py
# Caso você não criou um Main Window deve-se alterar o arquivodopyqt.Ui_MainWindow para arquivodopyqt.xxx o que estiver dentro do arquivo .py abre ele que tá escrito lá o nome da Classe
#Qualquer dúvida me procura - > Giovanni aqui


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from OPV_sensorWeb import *
from OPV_equipamento import *
from datetime import datetime
import OPV_Designer, sys, threading, time, sqlite3
import numpy as np
import matplotlib.pyplot as plt

#VARIAVEIS

green_led = 'green_led.png'
red_led = 'red_led.png'
gray_led = 'gray_led.png'
BAG01 = Bomba('Bomba de Água Gelada 01')
Chiller01 = Chiller('Chiller 01')
VAG01 = Valvula('Valvula de Água Gelada 01')
BAG02 = Bomba('Bomba de Água Gelada 02')
Chiller02 = Chiller('Chiller 02')
VAG02 = Valvula('Valvula de Água Gelada 02')
BAGR = Bomba('Bomba de Água Gelada Reserva')


def clickable(widget):
    class Filter(QObject):        
        clicked = pyqtSignal()         
        def eventFilter(self, obj, event):           
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                         # The developer can opt for .emit(obj) to get the object within the slot.
                        return True             
            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

class OPV_Window(QWidget, OPV_Designer.Ui_Form):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.pushButton.clicked.connect(self.falhaBAG01)
        self.pushButton_2.clicked.connect(self.falhaBAG02)
        self.pushButton_3.clicked.connect(self.falhaChiller01)
        self.pushButton_4.clicked.connect(self.falhaChiller02)
        self.pushButton_5.clicked.connect(self.partidaCAG)
        self.pushButton_6.clicked.connect(self.releaseAll)
        self.pushButton_7.clicked.connect(self.comandoManual01)
        self.pushButton_8.clicked.connect(self.comandoManual02)
        self.pushButton_9.clicked.connect(self.makeGraph)
        manual01 = self.label_gray
        manual01.mouseReleaseEvent = self.manualBAG01
        
        self.ydata = []
        
        thread1 = threading.Thread(target=self.threadDados1)
        thread1.start()

        thread2 = threading.Thread(target=self.threadDados2)
        thread2.start()


    def manualBAG01(self, event):
        if (BAG01.getFalha() == 0):
            if (BAG01.getMA() == 'Manual'):
                if (BAG01.getEstado() == 0):
                    BAG01.setComando(1)
                    self.changeImage(self.label_gray,green_led)
                    time.sleep(5)
                    self.changeImage(self.label_gray_2,green_led)
                else:
                    BAG01.setComando(0)
                    self.changeImage(self.label_gray,gray_led)
                    self.changeImage(self.label_gray_2,gray_led)

        
    def comandoManual01(self):
        if (BAG01.getMA() == 'Automatico'):
            BAG01.setMA('Manual')
            self.text_LR.setText('Manual')
        elif (BAG01.getMA() == 'Manual'):
            BAG01.setMA('Automatico')
            self.text_LR.setText('Automatico')
            

        if (Chiller01.getMA() == 'Automatico'):
            Chiller01.setMA('Manual')
            self.text_MA.setText('Manual')
        elif (Chiller01.getMA() == 'Manual'):
            Chiller01.setMA('Automatico')
            self.text_MA.setText('Automatico')
            
        if (VAG01.getMA() == 'Automatico'):
            VAG01.setMA('Manual')
            self.text_MA_3.setText('Manual')
        elif (VAG01.getMA() == 'Manual'):
            VAG01.setMA('Automatico')
            self.text_MA_3.setText('Automatico')

    def comandoManual02(self):
        if (BAG02.getMA() == 'Automatico'):
            BAG02.setMA('Manual')
            self.text_LR_4.setText('Manual')
        elif (BAG02.getMA() == 'Manual'):
            BAG02.setMA('Automatico')
            self.text_LR_4.setText('Automatico')
            
        if (Chiller02.getMA() == 'Automatico'):
            Chiller02.setMA('Manual')
            self.text_MA_2.setText('Manual')
        elif (Chiller02.getMA() == 'Manual'):
            Chiller02.setMA('Automatico')
            self.text_MA_2.setText('Automatico')
            
        if (VAG02.getMA() == 'Automatico'):
            VAG02.setMA('Manual')
            self.text_MA_4.setText('Manual')
        elif (VAG02.getMA() == 'Manual'):
            VAG02.setMA('Automatico')
            self.text_MA_4.setText('Automatico')

    def threadDados1(self):
        while 1:
            now = datetime.now()
            self.label_18.setNum(now.hour)  #LABEL HORAS
            self.label_19.setNum(now.minute)  #LABEL MINUTOS
            self.label_21.setNum(now.second)  #LABEL SEGUNDOS

            time.sleep(1)
            
    def threadDados2(self):
        while 1:
            conn = sqlite3.connect('dbOPV.db')
            cursor = conn.cursor()

            now = datetime.now()
            today = now.replace(microsecond=0)
            
            sensorSP = sensorWeb('SaoPaulo,br')
            temperatura = sensorSP.getTempValor()
            status = sensorSP.getStatus()
            vento = sensorSP.getWind()
            umidade = sensorSP.getUmidade()

            self.label_5.setNum(temperatura)    #LABEL TEMPERATURA
            self.label_14.setText(status) #LABEL STATUS
            self.label_12.setText(vento) #LABEL VENTO
            self.label_11.setNum(umidade)   #LABEL UMIDADE
            self.label_2.setText('SaoPaulo,br')  #LABEL DE LOCALIZAÇÃO            
            self.label_22.setNum(now.day)  #LABEL DIA
            self.label_24.setNum(now.month)  #LABEL MES
            self.label_26.setNum(now.year)  #LABEL ANO

            #INSERIR DADOS NA TABELA
            cursor.execute("""
            INSERT INTO sensorWeb (horario, temperatura, status, vento, umidade)
            VALUES (?, ?, ?, ?, ?)
            """, (today, temperatura, status, vento, umidade))

            conn.commit()

##            print(temperatura)
##            print(status)
##            print(vento)
##            print(umidade)
##            print(today)
##
##            print('DADOS INSERIDOS COM SUCESSO')
##
            conn.close()

            #self.loopGraph(temperatura)
            time.sleep(60)
 
    def makeGraph(self):
        plt.ion()
        conn = sqlite3.connect('dbOPV.db')
        cursor = conn.cursor()
        d=cursor.execute("SELECT temperatura FROM sensorWeb").fetchall()
        for item in d:
            self.ydata.append(item[0])
        while len(self.ydata) < 150:
            self.ydata.insert(0,0.0)
        #print(self.ydata)            
            
        conn.close()
        self.ax1=plt.axes()
        self.line, = plt.plot(self.ydata)
        plt.ylim([10,45])
        self.loopGraph(self.ydata[149])

    def loopGraph(self,data=0):
        #Max and min values
        if self.ydata == []:
            self.makeGraph(0)
        #print(self.ydata)
        ymin = float(min(self.ydata))-10
        ymax = float(max(self.ydata))+10
        
        self.ydata.append(data)
        del self.ydata[0]
        self.line.set_xdata(np.arange(len(self.ydata)))

        self.line.set_ydata(self.ydata) # update the data
        #print('DRAW')
        plt.draw() # update the plot
        plt.pause(600)        

    def partidaCAG(self):
        
        sensorSP = sensorWeb('SaoPaulo,br')
        temperatura = sensorSP.getTempValor()
      
        if (temperatura <= 21):

            if (Chiller01.getFalha() == 0):
                #COMANDO DO CHILLER 01
                Chiller01.setComando(1)
                self.changeImage(self.label_gray_10,green_led)
                #COMANDO DA BOMBAS
                if (BAG01.getFalha() == 0):
                    BAG01.setComando(1)
                    self.changeImage(self.label_gray,green_led)
                elif (BAG01.getFalha() == 1):
                    BAGR.setComando(1)
                    self.changeImage(self.label_gray_8,green_led)
                #COMANDO VAG01
                VAG01.setComando(1)
                self.changeImage(self.label_gray_18,green_led)
            elif (Chiller01.getFalha() == 1):
                #COMANDO DO CHILLER 02
                Chiller02.setComando(1)
                self.changeImage(self.label_gray_14,green_led)
                #COMANDO DAS BOMBAS
                if (BAG02.getFalha() == 0):
                    BAG02.setComando(1)
                    self.changeImage(self.label_gray_5,green_led)
                elif (BAG02.getFalha() == 1):
                    BAGR.setComando(1)
                    self.changeImage(self.label_gray_8,green_led)
                VAG02.setComando(1)
                self.changeImage(self.label_gray_21,green_led)
                
        elif (temperatura >= 23):

            if (Chiller02.getFalha() == 0):
                #COMANDO DO CHILLER 02
                Chiller02.setComando(1)
                self.changeImage(self.label_gray_14,green_led)
                #COMANDO DA BOMBAS
                if (BAG02.getFalha() == 0):
                    BAG02.setComando(1)
                    self.changeImage(self.label_gray_5,green_led)
                elif (BAG02.getFalha() == 1):
                    BAGR.setComando(1)
                    self.changeImage(self.label_gray_8,green_led)
                #COMANDO VAG02
                VAG02.setComando(1)
                self.changeImage(self.label_gray_21,green_led)
            elif (Chiller02.getFalha() == 1):
                #COMANDO DO CHILLER 01
                Chiller01.setComando(1)
                self.changeImage(self.label_gray_10,green_led)
                #COMANDO DAS BOMBAS
                if (BAG01.getFalha() == 0):
                    BAG01.setComando(1)
                    self.changeImage(self.label_gray,green_led)
                elif (BAG01.getFalha() == 1):
                    BAGR.setComando(1)
                    self.changeImage(self.label_gray_8,green_led)
                VAG01.setComando(1)
                self.changeImage(self.label_gray_18,green_led)
    
        if (BAG01.getEstado() == 1):
            self.changeImage(self.label_gray_2,green_led)
        else:
            self.changeImage(self.label_gray_2,gray_led)

        if (BAG02.getEstado() == 1):
            self.changeImage(self.label_gray_6,green_led)
        else:
            self.changeImage(self.label_gray_6,gray_led)

        if (BAGR.getEstado() == 1):
            self.changeImage(self.label_gray_9,green_led)
        else:
            self.changeImage(self.label_gray_9,gray_led)

        if (Chiller01.getEstado() == 1):
            self.changeImage(self.label_gray_11,green_led)
        else:
            self.changeImage(self.label_gray_11,gray_led)

        if (Chiller02.getEstado() == 1):
            self.changeImage(self.label_gray_13,green_led)
        else:
            self.changeImage(self.label_gray_13,gray_led)

        if (VAG01.getEstado() == 1):
            self.changeImage(self.label_gray_16,green_led)
        else:
            self.changeImage(self.label_gray_16,gray_led)

        if (VAG02.getEstado() == 1):
            self.changeImage(self.label_gray_19,green_led)
        else:
            self.changeImage(self.label_gray_19,gray_led)

          
    def changeImage(self,label,image):
        label.setText('')
        picture = QPixmap(image)
        label.setPixmap(picture)
        
    def falhaBAG01(self):
        if (BAG01.getFalha() == 0):
            BAG01.setFalha(1)
            self.changeImage(self.label_gray_3,red_led)
        else:
            BAG01.setFalha(0)
            self.changeImage(self.label_gray_3,gray_led)
        
    def falhaBAG02(self):
        if (BAG02.getFalha() == 0):
            BAG02.setFalha(1)
            self.changeImage(self.label_gray_4,red_led)
        else:
            BAG02.setFalha(0)
            self.changeImage(self.label_gray_4,gray_led)
            
    def falhaChiller01(self):
        if (Chiller01.getFalha() == 0):
            Chiller01.setFalha(1)
            self.changeImage(self.label_gray_12,red_led)
        else:
            Chiller01.setFalha(0)
            self.changeImage(self.label_gray_12,gray_led)

    def falhaChiller02(self):
        if (Chiller02.getFalha() == 0):
            Chiller02.setFalha(1)
            self.changeImage(self.label_gray_15,red_led)
        else:
            Chiller02.setFalha(0)
            self.changeImage(self.label_gray_15,gray_led)

    def releaseAll(self):
        BAG01.setComando(0)
        BAG01.setFalha(0)
        BAG01.setMA('Automatico')
        BAG02.setComando(0)
        BAG02.setFalha(0)
        BAG02.setMA('Automatico')
        BAGR.setComando(0)
        BAGR.setFalha(0)
        BAGR.setMA('Automatico')
        Chiller01.setComando(0)
        Chiller01.setFalha(0)
        Chiller01.setMA('Automatico')
        Chiller02.setComando(0)
        Chiller02.setFalha(0)
        Chiller02.setMA('Automatico')
        VAG01.setComando(0)
        VAG01.setFalha(0)
        VAG01.setMA('Automatico')
        VAG02.setComando(0)
        VAG02.setFalha(0)
        VAG02.setMA('Automatico')
        self.changeImage(self.label_gray,gray_led)
        self.changeImage(self.label_gray_2,gray_led)
        self.changeImage(self.label_gray_3,gray_led)
        self.changeImage(self.label_gray_4,gray_led)
        self.changeImage(self.label_gray_5,gray_led)
        self.changeImage(self.label_gray_6,gray_led)
        self.changeImage(self.label_gray_7,gray_led)
        self.changeImage(self.label_gray_8,gray_led)
        self.changeImage(self.label_gray_9,gray_led)
        self.changeImage(self.label_gray_10,gray_led)
        self.changeImage(self.label_gray_11,gray_led)
        self.changeImage(self.label_gray_12,gray_led)
        self.changeImage(self.label_gray_13,gray_led)
        self.changeImage(self.label_gray_14,gray_led)
        self.changeImage(self.label_gray_15,gray_led)
        self.changeImage(self.label_gray_16,gray_led)
        self.changeImage(self.label_gray_17,gray_led)
        self.changeImage(self.label_gray_18,gray_led)
        self.changeImage(self.label_gray_19,gray_led)
        self.changeImage(self.label_gray_20,gray_led)
        self.changeImage(self.label_gray_21,gray_led)
        self.text_LR.setText('Automatico')
        self.text_LR_4.setText('Automatico')
        self.text_LR_5.setText('Automatico')
        self.text_MA.setText('Automatico')
        self.text_MA_2.setText('Automatico')
        self.text_MA_3.setText('Automatico')
        self.text_MA_4.setText('Automatico')
        
def main():
    app = QApplication(sys.argv)
    app.setStyle('cleanlooks') #dá para alterar
    form = OPV_Window() #Nome da Classe lá em cima  
    form.show()
    app.exec_()

  
if __name__ == '__main__': 
    main()

#self.label_CAG.hide()
