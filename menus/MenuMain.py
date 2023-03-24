from tkinter import Menu
from pages.PageSet01 import Page1, Page2, StartPage


class MainMenu(Menu):
    def __init__(self, parent, controller):
        menubar = Menu(parent)
        parent.config(menu=menubar)

        pages_menu = Menu(menubar, tearoff=False)
        pages_menu.add_command(
            label='Start Page',
            command=lambda: parent.show_page("start")
        )
        pages_menu.add_command(
            label='Page 1',
            command=lambda: parent.show_page("page1")
        )
        pages_menu.add_command(
            label='Page 2',
            command=lambda: parent.show_page("page2")
        )

        pages_menu.add_command(
            label='Questionnaire',
            command=lambda: parent.show_page("Questionnaire")
        )

        file_menu = Menu(menubar, tearoff=False)
        file_menu.add_command(
            label='Exit',
            command=parent.destroy,
        )
        menubar.add_cascade(
            label="File",
            menu=file_menu,
            underline=0
        )
        menubar.add_cascade(
            label="Pages",
            menu=pages_menu,
            underline=0
        )

    @staticmethod
    def sayHello():
        print("Hello")