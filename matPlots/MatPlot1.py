import numpy as np
import matplotlib.pyplot as plt

def getMatPlot1():
    x = np.linspace(0, 5, 11)
    y = x ** 2

    fig = plt.figure()
    #axes1 = fig.add_axes([0.0, 0.0, 1, 1])
    axes2 = fig.add_axes([0.11, 0.59, 0.4, 0.3])
    axes3 = fig.add_axes([0.45, 0.11, 0.4, 0.3])

    #axes1.plot(x,y)
    #axes1.set_xlabel('X Label1')
    #axes1.set_ylabel('Y Label1')
    #axes1.set_title('Plot 1')

    axes2.plot(y,x, 'r')
    axes2.set_xlabel('X Label2')
    axes2.set_ylabel('Y Label2')
    axes2.set_title('Plot 2')

    axes3.plot(y,x, 'r')
    axes3.set_xlabel('X Label3')
    axes3.set_ylabel('Y Label3')
    axes3.set_title('Plot 3')

    return fig