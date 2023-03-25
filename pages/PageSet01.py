import customtkinter as ctk

from pages.PageEnums import PagesEnum

LARGEFONT = ("Verdana", 35)
class StartPage(ctk.CTkFrame):
    def __init__(self, parent ):
        ctk.CTkFrame.__init__(self, parent, border_color="red", border_width=1)

        label = ctk.CTkLabel(self, text="Startpage", font=LARGEFONT)
        label.grid(row=0, column=0, padx=30, pady=30)

        button1 = ctk.CTkButton(self, text="Page 1",
                             command=lambda: parent.show_frame(PagesEnum.Page1))
        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Page 2",
                             command=lambda: parent.show_frame(PagesEnum.Page2))
        button2.grid(row=2, column=0, ipadx=10, pady=10)

class Page1(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent, border_color="blue", border_width=1)
        label = ctk.CTkLabel(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=0, padx=30, pady=30)

        button1 = ctk.CTkButton(self, text="StartPage",
                             command=lambda: parent.show_frame(PagesEnum.StartPage))
        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Page 2",
                             command=lambda: parent.show_frame(PagesEnum.Page2))
        button2.grid(row=2, column=0, padx=10, pady=10)

class Page2(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)

        label = ctk.CTkLabel(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=0, ipadx=30, ipady=30)

        button1 = ctk.CTkButton(self, text="Page 1",
                             command=lambda: parent.show_frame(PagesEnum.Page1))
        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="parent",
                             command=lambda: parent.show_frame(PagesEnum.StartPage))
        button2.grid(row=2, column=0, padx=10, pady=10)