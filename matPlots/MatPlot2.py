import numpy as np
import matplotlib.pyplot as plt

def getMatPlot2():
    x = np.linspace(0, 5, 11)
    y = x ** 2
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(7,5), dpi=100)
    axes[0].plot(x,y)
    axes[1].plot(y,x)
    return fig