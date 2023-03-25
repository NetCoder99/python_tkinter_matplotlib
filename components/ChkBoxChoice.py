import customtkinter as ctk
# Gender Radio Buttons
def getChkBoxChoice(parent, row:int):
    # Choice Label
    parent.choiceLabel = ctk.CTkLabel(parent,
                                    text="Choice")
    parent.choiceLabel.grid(row=row, column=0,
                          padx=20, pady=20,
                          sticky="ew")

    # Choice Check boxes
    parent.checkboxVar = ctk.StringVar(value="Choice 1")

    parent.choice1 = ctk.CTkCheckBox(parent, text="choice 1",
                                   variable=parent.checkboxVar,
                                   onvalue="choice1",
                                   offvalue="c1")
    parent.choice1.grid(row=row, column=1, padx=20,
                      pady=20, sticky="ew")

    parent.choice2 = ctk.CTkCheckBox(parent, text="choice 2",
                                   variable=parent.checkboxVar,
                                   onvalue="choice2",
                                   offvalue="c2")
    parent.choice2.grid(row=row, column=2, padx=20, pady=20,
                      sticky="ew")
