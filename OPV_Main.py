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
        self.ydata = []
        thread1 = threading.Thread(target=self.threadDados1)
        thread1.start()
        self.makeGraph()
        thread2 = threading.Thread(target=self.threadDados2)
        thread2.start()

    def threadDados1(self):
        i=1
        while 1:
            sensorSP = sensorWeb('SaoPaulo,br')
            horario = sensorSP.getDate()
            temperatura = sensorSP.getTempValor()
            temperaturaMinima = sensorSP.getTempMin()
            temperaturaMaxima = sensorSP.getTempMax()
            humidade = sensorSP.getUmidade()
            localizacao = sensorSP.getLocalizacao()
            dia = sensorSP.getDia()
            mes = sensorSP.getMes()
            ano = sensorSP.getAno()
            horas = sensorSP.getHora()
            minutos = sensorSP.getMinuto()
            segundos = sensorSP.getSegundo()

            self.label_5.setNum(temperatura)    #LABEL TEMPERATURA
            self.label_14.setNum(temperaturaMaxima) #LABEL TEMPERATURA MAXIMA
            self.label_12.setNum(temperaturaMinima) #LABEL TEMPERATURA MINIMA
            self.label_11.setNum(humidade)   #LABEL HUMIDADE
            self.label_2.setText(localizacao)  #LABEL DE LOCALIZAÇÃO
            self.label_22.setText(dia)  #LABEL DIA
            self.label_24.setText(mes)  #LABEL MES
            self.label_26.setText(ano)  #LABEL ANO
            self.label_18.setText(horas)  #LABEL HORAS
            self.label_19.setText(minutos)  #LABEL MINUTOS
            self.label_21.setText(segundos)  #LABEL SEGUNDOS


            time.sleep(1)
            i=i+1

    def makeGraph(self):
        plt.ion()
        conn = sqlite3.connect('dbOPV.db')
        cursor = conn.cursor()
        d=cursor.execute("SELECT temperatura FROM sensorWeb").fetchall()
        for item in d:
            self.ydata.append(item[0])
        while len(self.ydata) < 500:
            self.ydata.insert(0,0.0)
        #print(self.ydata)
            
            
        conn.close()
##        self.ax1=plt.axes()
##        self.line, = plt.plot(self.ydata)
##        plt.ylim([10,60])
##        self.loopGraph(self.ydata[49])

##    def loopGraph(self,data=0):
##                #Max and min values
##        if self.ydata == []:
##            self.makeGraph(0)
##        print(self.ydata)
##        ymin = float(min(self.ydata))-10
##        ymax = float(max(self.ydata))+10
##
##
##        self.ydata.append(data)
##        del self.ydata[0]
##        self.line.set_xdata(np.arange(len(self.ydata)))
##
##        self.line.set_ydata(self.ydata) # update the data
##        print('DRAW')
##        plt.draw() # update the plot
##        plt.pause(0.05)
##        

            
    def threadDados2(self):
        while 1:
            conn = sqlite3.connect('dbOPV.db')
            cursor = conn.cursor()

            #DADOS DA LOCALIZAÇÃO WEB
            sensorSP = sensorWeb('SaoPaulo,br')
            horario = sensorSP.getDate()
            temperatura = sensorSP.getTempValor()
            temperaturaMinima = sensorSP.getTempMin()
            temperaturaMaxima = sensorSP.getTempMax()
            humidade = sensorSP.getUmidade()    


            #INSERIR DADOS NA TABELA
            cursor.execute("""
            INSERT INTO sensorWeb (localizacao, horario, temperatura, temperaturaMinima, temperaturaMaxima, humidade)
            VALUES (?, ?, ?, ?, ?, ?)
            """, ('SaoPaulo,br', horario, temperatura, temperaturaMinima, temperaturaMaxima, humidade))

            conn.commit()

##            print(temperatura)
##            print(temperaturaMinima)
##            print(temperaturaMaxima)
##            print(humidade)
##            print(horario)
##
##            print('DADOS INSERIDOS COM SUCESSO')

            conn.close()

            #self.loopGraph(temperatura)
            time.sleep(60)

 
            
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
            elif (Chiller01.getFalha == 1):
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
        BAG02.setComando(0)
        BAG02.setFalha(0)
        BAGR.setComando(0)
        BAGR.setFalha(0)
        Chiller01.setComando(0)
        Chiller01.setFalha(0)
        Chiller02.setComando(0)
        Chiller02.setFalha(0)
        VAG01.setComando(0)
        VAG01.setFalha(0)
        VAG02.setComando(0)
        VAG02.setFalha(0)
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
        
def main():
    app = QApplication(sys.argv)
    app.setStyle('cleanlooks') #dá para alterar
    form = OPV_Window() #Nome da Classe lá em cima  
    form.show()
    app.exec_()

  
if __name__ == '__main__': 
    main()

#self.label_CAG.hide()
