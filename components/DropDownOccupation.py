import customtkinter as ctk
# Gender Radio Buttons
def getDropDownOccupation(parent):
    # Occupation Label
    parent.occupationLabel = ctk.CTkLabel(parent,
                                        text="Occupation")
    parent.occupationLabel.grid(row=4, column=0,
                              padx=20, pady=20,
                              sticky="ew")

    # Occupation combo box
    parent.occupationOptionMenu = ctk.CTkOptionMenu(parent,
                                                  values=["Not Set",
                                                          "Student",
                                                          "Professional"])
    parent.occupationOptionMenu.grid(row=4, column=1,
                                   padx=20, pady=20,
                                   columnspan=2, sticky="ew")
