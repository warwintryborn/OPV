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
from sensorWeb import *
from equipamento import *
import OPV_Designer,sys
import threading
import time


#VARIAVEIS

green_led = 'green_led.png'
red_led = 'red_led.png'
grayled = 'gray_led.png'
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
        self.pushButton_5.clicked.connect(self.partidaCAG)
        
        thread1 = threading.Thread(target=self.threadDados)
        thread1.start()

    def threadDados(self):
        i=1
        while 1:
            #print('Opa fion')
            sensorSP = sensorWeb('SaoPaulo,br')
            horario = sensorSP.getDate()
            temperatura = sensorSP.getTempValor()
            temperaturaMinima = sensorSP.getTempMin()
            temperaturaMaxima = sensorSP.getTempMax()
            humidade = sensorSP.getHumidade()
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
            
    def partidaCAG(self):

        sensorSP = sensorWeb('SaoPaulo,br')
        temperatura = sensorSP.getTempValor()
      
        if (temperatura <= 21):
            #COMANDO BAG01
            if (BAG01.getFalha() == 0):
                BAG01.setComando(1)
                self.changeImage(self.label_gray,green_led)
            elif (BAG02.getFalha() == 0 and BAG01.getFalha() == 1):
                BAG02.setComando(1)
                self.changeImage(self.label_gray_5,green_led) 
            elif (BAG01.getFalha() == 1 and BAG02.getFalha() == 1):
                BAGR.setComando(1)
                self.changeImage(self.label_gray_8,green_led)                
            #COMANDO CHILLER01
            self.changeImage(self.label_gray_10,green_led)
            Chiller01.setComando(1)
            #COMANDO VAG01
            self.changeImage(self.label_gray_18,green_led)
            VAG01.setComando(1)
        elif (temperatura >= 22):
            #COMANDO BAG02
            if (BAG02.getFalha() == 0):
                BAG02.setComando(1)
                self.changeImage(self.label_gray_5,green_led)
            elif (BAG01.getFalha() == 0 and BAG02.getFalha() == 1):
                BAG01.setComando(1)
                self.changeImage(self.label_gray,green_led) 
            elif (BAG01.getFalha() == 1 and BAG02.getFalha() == 1):
                BAGR.setComando(1)
                self.changeImage(self.label_gray_8,green_led)     
            #COMANDO CHILLER02
            self.changeImage(self.label_gray_14,green_led)
            Chiller02.setComando(1)
            #COMANDO VAG02
            self.changeImage(self.label_gray_21,green_led)
            VAG02.setComando(1)

##        if (BAG01.getEstado() == 1):
##            self.changeImage(self.label_gray_2,green_led)
##        elif (BAG02.getEstado() == 1):
##            self.changeImage(self.label_gray_6,green_led)
##        elif (BAG
##            else:
##            self.changeImage(self.label_gray_8,green_led)
##            self.changeImage(self.label_gray_9,green_led)
##                BAGR.setComando(1)

    def changeImage(self,label,image):
        label.setText('')
        picture = QPixmap(image)
        label.setPixmap(picture)
        
    def falhaBAG01(self):
        self.changeImage(self.label_gray_3,red_led)
        BAG01.setFalha(1)

    def falhaBAG02(self):
        self.changeImage(self.label_gray_4,red_led)
        BAG02.setFalha(1)
        
def main():
    app = QApplication(sys.argv)
    app.setStyle('cleanlooks') #dá para alterar
    form = OPV_Window() #Nome da Classe lá em cima  
    form.show()
    app.exec_()

  
if __name__ == '__main__': 
    main()


#self.changeImage(self.label_gray_2,red_led)
#self.label_CAG.hide()
