import numpy as np
import matplotlib.pyplot as plt
import random


plt.ion()
ydata = [0] * 50
ax1=plt.axes()
line, = plt.plot(ydata)
plt.ylim([10,40])

while True:
    #Max and min values
    PID=float(10*random.random()-5)
    
    ymin = float(min(ydata))-10
    ymax = float(max(ydata))+10
    plt.ylim([ymin,ymax])

    ydata.append(PID)
    del ydata[0]
    line.set_xdata(np.arange(len(ydata)))

    line.set_ydata(ydata) # update the data

    plt.draw() # update the plot
    print(ydata)
    plt.pause(0.01)
