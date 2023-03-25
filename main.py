import customtkinter as ctk

from menus.MenuMain import MainMenu
from pages.CanvasDemo import CanvasPage
from pages.MatPlotLibDemo1 import MatPlotPage1
from pages.PageEnums import PagesEnum
from pages.PageSet01 import StartPage, Page1, Page2
from pages.Questionnaire import Questionnaire

# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
ctk.set_appearance_mode("System")

# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("green")

appWidth, appHeight = 900, 800
class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = ctk.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

# Create App class
class App(ctk.CTk):
    # Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("GUI Application")
        self.geometry(f"{appWidth}x{appHeight}")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        menubar = MainMenu(self)
        frame_dict = {'row':0, 'column':0, 'padx':20, 'pady':20, 'sticky':"nsew"}

        self.StartPage = StartPage(parent=self)
        self.StartPage.grid(**frame_dict)
        self.StartPage.grid_remove()

        self.Page1 = Page1(parent=self)
        self.Page1.grid(**frame_dict)
        self.Page1.grid_remove()

        self.Page2 = Page2(parent=self)
        self.Page2.grid(**frame_dict)
        self.Page2.grid_remove()

        self.Questionnaire = Questionnaire(parent=self)
        self.Questionnaire.grid(**frame_dict)
        self.Questionnaire.grid_remove()

        self.MatPlotPage1 = MatPlotPage1(parent=self)
        self.MatPlotPage1.grid(**frame_dict)
        self.MatPlotPage1.grid_remove()

        self.CanvasPage = CanvasPage(parent=self)
        self.CanvasPage.grid(**frame_dict)
        self.CanvasPage.grid_remove()

        self.MatPlotPage1.grid()
        self.active_page = self.MatPlotPage1


    def show_frame(self, page_name:str):
        print('Showing frame: {}'.format(page_name.name))
        for obj in self.children:
            print('obj:{}'.format(obj))
            if obj.replace('!', '').casefold() == (page_name.name.casefold()):
                print('found: {} : {}'.format(page_name.name, obj))
                tmp = self.children[obj]
                tmp.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
                self.active_page.grid_remove()
                self.active_page = tmp


    def shutdown_app(self):
        print('Shutting down 1')
        app.quit()

# ----------------------------------------------------
if __name__ == "__main__":
    app = App()
    # trap the close event to kill the matplotlib agent
    app.protocol('WM_DELETE_WINDOW', app.shutdown_app)
    app.mainloop()
