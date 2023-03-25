import customtkinter as ctk
# Gender Radio Buttons
def getTxtName(parent, row: int):
    # Name Label
    parent.nameLabel = ctk.CTkLabel(parent, text="Name")
    parent.nameLabel.grid(row=row, column=0,
                        padx=20, pady=20,
                        sticky="ew")

    # Name Entry Field
    parent.nameEntry = ctk.CTkEntry(parent,
                                    placeholder_text="Teja",
                                    )
    parent.nameEntry.bind('<FocusOut>', parent.generateResults)
    parent.nameEntry.grid(row=row, column=1,
                        columnspan=3, padx=20,
                        pady=20, sticky="ew")
