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

        fig1 = getMatPlot1()
        canvas = FigureCanvasTkAgg(fig1, master=parent)
        canvas.draw()

        tmp = canvas.get_tk_widget().grid(row=1, column=0, padx=20, ipady=20)
        #canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        print('MatPlotPage1 - initialized')
        #canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=10, columnspan=4)