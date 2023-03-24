# import customtkinter as ctk
#
# from pages.Page2 import Page2
# from pages.StartPage import StartPage
#
# LARGEFONT = ("Verdana", 35)
#
# class Page1(ctk.CTkFrame):
#
#     def __init__(self, parent, controller):
#         ctk.CTkFrame.__init__(self, parent)
#         label = ctk.CTkLabel(self, text="Page 1", font=LARGEFONT)
#         label.grid(row=0, column=4, padx=10, pady=10)
#
#         button1 = ctk.CTkButton(self, text="StartPage",
#                              command=lambda: controller.show_frame(StartPage))
#         button1.grid(row=1, column=1, padx=10, pady=10)
#
#         button2 = ctk.CTkButton(self, text="Page 2",
#                              command=lambda: controller.show_frame(Page2))
#         button2.grid(row=2, column=1, padx=10, pady=10)