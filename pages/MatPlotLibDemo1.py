import customtkinter as ctk

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from matPlots.MatPlot1 import getMatPlot1
from matPlots.MatPlot2 import getMatPlot2
from matPlots.MatPlot3 import getMatPlot3

LARGEFONT = ("Verdana", 25)

class MatPlotPage1(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)
        self.pageLabel = ctk.CTkLabel(self, text="MatPlotLib Demo - 001", font=LARGEFONT)
        self.pageLabel.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.plotMenu  = ctk.CTkOptionMenu(self, values=self.getPlotNames(), command=self.selectPlot)
        self.plotMenu.grid(row=1, column=0, padx=10, pady=10)

        self.saveBtn = ctk.CTkButton(self, text="Save", command=lambda: self.savePlot("Test"))
        self.saveBtn.grid(row=1, column=1, padx=10, pady=10,)

        self.fig1 = getMatPlot1()
        self.fig2 = getMatPlot2()
        self.fig3 = getMatPlot3()

        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self)
        self.canvas1.get_tk_widget().grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.activePlot = "getMatPlot1"
        #self.canvas1.get_tk_widget().grid_remove()

        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self)
        self.canvas2.get_tk_widget().grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.canvas2.get_tk_widget().grid_remove()

        self.canvas3 = FigureCanvasTkAgg(self.fig3, master=self)
        self.canvas3.get_tk_widget().grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.canvas3.get_tk_widget().grid_remove()

        print('MatPlotPage1 - initialized')

    def getPlotNames(self):
        return ["getMatPlot1", "getMatPlot2", "getMatPlot3"]

    def selectPlot(self, plot_name: str):
        print(f'selectPlot:{plot_name}')
        self.canvas1.get_tk_widget().grid_remove()
        self.canvas2.get_tk_widget().grid_remove()
        self.canvas3.get_tk_widget().grid_remove()
        if plot_name == 'getMatPlot1':
            self.activePlot = "getMatPlot1"
            self.canvas1.get_tk_widget().grid()
        elif plot_name == 'getMatPlot2':
            self.activePlot = "getMatPlot2"
            self.canvas2.get_tk_widget().grid()
        else:
            self.activePlot = "getMatPlot3"
            self.canvas3.get_tk_widget().grid()

    def savePlot(self, plot_name: str):
        print(f'savePlot:{plot_name}')
        if self.activePlot == 'getMatPlot1':
            self.fig1.savefig('MatPlot1.png')
        if self.activePlot == 'getMatPlot2':
            self.fig2.savefig('MatPlot2.png')
        if self.activePlot == 'getMatPlot3':
            self.fig3.savefig('MatPlot3.png')
