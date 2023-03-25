import customtkinter as ctk

from pages.PageEnums import PagesEnum

LARGEFONT = ("Verdana", 35)

class CanvasPage(ctk.CTkFrame):
    def __init__(self, parent ):
        ctk.CTkFrame.__init__(self, parent, border_color="green", border_width=1)

        label = ctk.CTkLabel(self, text="Canvas Page", font=LARGEFONT)
        label.grid(row=0, column=0, padx=30, pady=30, columnspan=2)

        button1 = ctk.CTkButton(self, text="Show Plot 1",
                             command=lambda: self.showPlot("plot1"))
        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Show Plot 2",
                             command=lambda: self.showPlot("plot2"))
        button2.grid(row=1, column=1, ipadx=10, pady=10)

        canvas1 = self.getCanvas('canvas1', 'orange')
        self.canvas1 = canvas1

        canvas2 = self.getCanvas('canvas2', 'pink')
        self.canvas2 = canvas2

        canvas1.grid()

    def showPlot(self, plot_name: str):
        if plot_name == 'plot1':
            self.canvas2.grid_remove()
            self.canvas1.grid()
        else:
            self.canvas1.grid_remove()
            self.canvas2.grid()

    def getCanvas(self, name: str, fill_color: str):
        canvas = ctk.CTkCanvas(self, bg='#eee', name=name)
        canvas.grid(row=2, column=0,  padx=10, pady=10, columnspan=2, sticky=ctk.NSEW)
        canvas.update()
        canvas.create_oval(self.getCenter(canvas, 90), width=3, fill=fill_color)
        canvas.grid_remove()
        return canvas

    def getCenter(self, canvas, size):
        width  = canvas.winfo_width()
        height = canvas.winfo_height()
        x0 = width  / 2 - (size / 2)
        y0 = height / 2 - (size / 2)
        x1 = width  / 2 + (size / 2)
        y1 = height / 2 + (size / 2)
        return x0, y0, x1, y1