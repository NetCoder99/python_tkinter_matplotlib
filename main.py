# Import customtkinter module
from tkinter import Menu

import customtkinter as ctk

from menus.MenuMain import MainMenu
from pages.PageSet01 import StartPage, Page1, Page2
from pages.Questionnaire import Questionnaire

# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
ctk.set_appearance_mode("System")

# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("green")

appWidth, appHeight = 900, 800

# Create App class
class App(ctk.CTk):
    # Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("GUI Application")
        self.geometry(f"{appWidth}x{appHeight}")

        # creating a container
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}
        for page in (StartPage, Page1, Page2, Questionnaire):
            frame = page(container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[page] = frame

        self.show_frame(StartPage)

        # initializing the main menu
        menubar = MainMenu(self, container)

    def show_page(self, page_name):
        if page_name == 'start':
            self.show_frame(StartPage)
        elif page_name == 'page1':
            self.show_frame(Page1)
        elif page_name == 'page2':
            self.show_frame(Page2)
        elif page_name == 'Questionnaire':
            self.show_frame(Questionnaire)

        #Questionnaire.py


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# ----------------------------------------------------
if __name__ == "__main__":
    app = App()
    # Runs the app
    app.mainloop()