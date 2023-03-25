import customtkinter as ctk

def getTxtAge(parent, row: int):
    # Age Label
    parent.ageLabel = ctk.CTkLabel(parent,
                                 text="Age")
    parent.ageLabel.grid(row=row, column=0,
                       padx=20, pady=20,
                       sticky="ew")

    # Age Entry Field
    vAge = (parent.register(validAge))
    parent.ageEntry = ctk.CTkEntry(parent,placeholder_text="18",)
    parent.ageEntry.bind('<FocusOut>', parent.generateResults)

    parent.ageEntry.grid(row=row, column=1,
                       columnspan=3, padx=20,
                       pady=20, sticky="ew")

def validAge(P):
    if str.isdigit(P) or P == "":
        print('callback True : {}'.format(P))
        return True
    else:
        print('callback False: {}'.format(P))
        return False