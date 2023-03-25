import customtkinter as ctk
# Gender Radio Buttons
def getBtnGenderRadio(parent, row: int):

    # Gender Label
    parent.genderLabel = ctk.CTkLabel(parent,
                                    text="Gender")
    parent.genderLabel.grid(row=row, column=0,
                          padx=20, pady=20,
                          sticky="ew")

    parent.genderVar = ctk.StringVar(value="Prefer not to say")

    parent.maleRadioButton = ctk.CTkRadioButton(parent,
                                                text="Male",
                                                variable=parent.genderVar,
                                                value="Male",
                                                command=parent.generateResults)
    parent.maleRadioButton.grid(row=row, column=1, padx=20,
                              pady=20, sticky="ew")

    parent.femaleRadioButton = ctk.CTkRadioButton(parent,
                                                  text="Female",
                                                  variable=parent.genderVar,
                                                  value="Female",
                                                  command=parent.generateResults)
    parent.femaleRadioButton.grid(row=row, column=2,
                                padx=20,
                                pady=20, sticky="ew")

    parent.noneRadioButton = ctk.CTkRadioButton(parent,
                                                text="Prefer not to say",
                                                variable=parent.genderVar,
                                                value="Prefer not to say",
                                                command=parent.generateResults)
    parent.noneRadioButton.grid(row=row, column=3,
                              padx=20, pady=20,
                              sticky="ew")

