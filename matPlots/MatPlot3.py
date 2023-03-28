import numpy as np
import matplotlib.pyplot as plt

def getMatPlot3():
    x = np.linspace(0, 5, 11)
    y = x ** 2
    fig = plt.figure(figsize=(7,5), dpi=100)
    axes = fig.add_axes([0,0,1,1])
    axes.plot(x,x**2, label="X Squared")
    axes.plot(x,x**3, label="X Cubed")
    axes.legend(loc='best')
    return fig