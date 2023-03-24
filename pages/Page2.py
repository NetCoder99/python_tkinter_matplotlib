# import customtkinter as ctk
#
# from pages.Page1 import Page1
# from pages.StartPage import StartPage
#
# LARGEFONT = ("Verdana", 35)
#
# # third window frame page2
# class Page2(ctk.CTkFrame):
#     def __init__(self, parent, controller):
#         ctk.CTkFrame.__init__(self, parent)
#
#         label = ctk.CTkLabel(self, text="Page 2", font=LARGEFONT)
#         label.grid(row=0, column=4, padx=10, pady=10)
#
#         button1 = ctk.CTkButton(self, text="Page 1",
#                              command=lambda: controller.show_frame(Page1))
#         button1.grid(row=1, column=1, padx=10, pady=10)
#
#         button2 = ctk.CTkButton(self, text="Startpage",
#                              command=lambda: controller.show_frame(StartPage))
#         button2.grid(row=2, column=1, padx=10, pady=10)