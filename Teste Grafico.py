import numpy as np
import matplotlib.pyplot as plt
import random

##
##plt.ion()
##ydata = [0] * 50
##ax1=plt.axes()
##line, = plt.plot(ydata)
##plt.ylim([10,40])
##
##while True:
##    #Max and min values
##    PID=float(10*random.random()-5)
##    
##    ymin = float(min(ydata))-10
##    ymax = float(max(ydata))+10
##    plt.ylim([ymin,ymax])
##
##    ydata.append(PID)
##    del ydata[0]
##    line.set_xdata(np.arange(len(ydata)))
##
##    line.set_ydata(ydata) # update the data
##
##    plt.draw() # update the plot
##    print(ydata)
##    plt.pause(0.01)
##

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
