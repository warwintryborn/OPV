import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from mainWindow import Ui_MainWindow

import matplotlib.pyplot as plt
import numpy as np

#!/usr/bin/python
"""
*************************************************
* @Project: Self Balance
* @Platform: Ubuntu
* @Description: Exemplo Matplotlib + QT
* @Owner: Guilherme Chinellato
* @Email: guilhermechinellato@gmail.com
*************************************************
"""

import time
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtGui, QtCore, QtWidgets

#Clase para plotar o matplotlib, criando em uma thread em paralelo para nao travar a aplicacao do QT
class Plot(QtCore.QThread):
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.parent = parent
        self.stop = False

    def run(self):
        plt.ion()
        ydata1 = [0] * 50
        ax1=plt.axes()
        line1, = plt.plot(ydata1)
        plt.ylim([10,40])

        #define o tempo de atualizacao do grafico
        LP = 0.1

        while not self.stop:
            #Le o valor no momento para ser plotado, aqui vc tem que chamar a funcao getTemp, por exemplo: self.parent.getTemp()
            data = self.parent.value

            #Max e min valores para o eixo Y
            #Eixo Y dinamico
            ymin = float(min(ydata1))-10
            ymax = float(max(ydata1))+10
            #Eixo Y fixo
            #ymin = -100.0
            #ymax = 100.0

            plt.ylim([ymin,ymax])
            ydata1.append(data)
            del ydata1[0]
            line1.set_xdata(np.arange(len(ydata1)))
            line1.set_ydata(ydata1)

            #Atualiza o grafico
            plt.draw()
            plt.pause(LP)

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Metodos de acao dos botoes
        self.ui.pushButton_plot.clicked.connect(self.pushButton_plot_onClicked)
        self.ui.pushButton_set.clicked.connect(self.pushButton_set_onClicked)

        #Variavel da classe (apenas para teste)
        self.value = 0.0

    def pushButton_plot_onClicked(self):
        #Instancia o objeto Plot que cria uma nova thread (para rodar em "paralelo")
        self.plot = Plot(self)
        #Inicia a thread nova do matplotlib
        self.plot.start()

    def pushButton_set_onClicked(self):
        #atualiza a variavel da classe com o valor do campo
        self.value = float(self.ui.lineEdit.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = mainWindow()
    myapp.show()
    sys.exit(app.exec_())
