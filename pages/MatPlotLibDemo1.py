import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matPlots.MatPlot1 import getMatPlot1

LARGEFONT = ("Verdana", 25)

class MatPlotPage1(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="MatPlotLib Demo - 001", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="Show Plot",
                             command=lambda: self.showPlot("show"))
        button1.grid(row=1, column=0, padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="Hide Plot",
                             command=lambda: self.showPlot("hide"))
        button1.grid(row=1, column=2, padx=10, pady=10)

        fig1 = getMatPlot1()
        canvas = FigureCanvasTkAgg(fig1, master=self)

        canvas.get_tk_widget().grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        #canvas.get_tk_widget().grid_remove()

        self.canvas = canvas
        print('MatPlotPage1 - initialized')

    def showPlot(self, plot_name: str):
        print(f'showPlot:{plot_name}')
        if plot_name == 'hide':
            self.canvas.get_tk_widget().grid_remove()
        else:
            self.canvas.get_tk_widget().grid()
