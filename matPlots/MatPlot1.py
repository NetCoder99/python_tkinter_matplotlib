import numpy as np
import matplotlib.pyplot as plt

def getMatPlot1():
    x = np.linspace(0, 5, 11)
    y = x ** 2

    fig = plt.figure(figsize=(7,5), dpi=100)
    axes1 = fig.add_axes([0.11, 0.11, 0.3, 0.3])
    axes2 = fig.add_axes([0.59, 0.59, 0.3, 0.3])
    axes3 = fig.add_axes([0.59, 0.11, 0.3, 0.3])
    axes4 = fig.add_axes([0.11, 0.59, 0.3, 0.3])

    axes1.plot(x,y)
    axes1.set_xlabel('X Label1')
    axes1.set_ylabel('Y Label1')
    axes1.set_title('Plot 1')

    axes2.plot(y,x, 'r')
    axes2.set_xlabel('X Label2')
    axes2.set_ylabel('Y Label2')
    axes2.set_title('Plot 2')

    axes3.plot(y,x, 'b')
    axes3.set_xlabel('X Label3')
    axes3.set_ylabel('Y Label3')
    axes3.set_title('Plot 3')

    axes4.plot(x, y, 'g')
    axes4.set_xlabel('X Label3')
    axes4.set_ylabel('Y Label3')
    axes4.set_title('Plot 4')

    return fig