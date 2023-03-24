from tkinter import END

import customtkinter as ctk

from components.BtnGenderRadio import getBtnGenderRadio
from components.ChkBoxChoice import getChkBoxChoice
from components.DropDownOccupation import getDropDownOccupation
from components.TxtAge import getTxtAge
from components.TxtName import getTxtName

pageWidth, pageHeight = 600, 700

class Questionnaire(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        #self.CTktitle("GUI Questionnaire")
        #parent.geometry(f"{pageWidth}x{pageHeight}")

        #vcmd = (self.register(self.callback))

        getTxtName(self, 0)
        getTxtAge(self, 1)
        getBtnGenderRadio(self, 2)
        getChkBoxChoice(self)
        getDropDownOccupation(self)

        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                                   text="Generate Results",
                                                   command=self.generateResults)
        self.generateResultsButton.grid(row=5, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")

        # Text Box
        self.displayBox = ctk.CTkTextbox(self, width=300,
                                         height=100)
        self.displayBox.grid(row=6, column=0, columnspan=4,
                             padx=20, pady=20, sticky="nsew")


    # This function is used to insert the
    # details entered by users into the textbox
    def generateResults(self):
        Font_tuple_bold_12 = ("Courier", 12, "bold")
        Font_tuple_bold_14 = ("Courier", 14, "bold")

        self.displayBox.delete("0.0", END)
        self.displayBox.configure(font=Font_tuple_bold_12)
        text = self.createText()
        self.displayBox.insert("0.0", text)

    # This function is used to get the selected
    # options and text from the available entry
    # fields and boxes and then generates
    # a prompt using them
    def createText(self):
        # Constructing the text variable
        text   =  "Name:       {}\n".format(self.getName())
        text   += "Age:        {}\n".format(self.getAge())
        text   += "Gender:     {}\n".format(self.getGender())
        text   += "Choice:     {}\n".format(self.getChoice())
        text   += "Occupation: {}\n".format(self.getOccupation())
        return text

    def getName(self):
        return 'No name' if len(self.nameEntry.get()) < 1 else self.nameEntry.get()

    def getAge(self):
        return 'Age not set' if len(self.ageEntry.get()) < 1 else self.ageEntry.get()

    def getGender(self):
        return 'Gender not set' if len(self.genderVar.get()) < 1 else self.genderVar.get()

    def getChoice(self):
        if not self.choice1.check_state and not self.choice2.check_state:
            return 'No choice selected'
        if self.choice1.check_state and not self.choice2.check_state:
            return 'Choice 1 selected'
        if not self.choice1.check_state and self.choice2.check_state:
            return 'Choice 2 selected'
        if self.choice1.check_state and self.choice2.check_state:
            return 'Choice 1 & 2 selected'
        return "Unknown choice state"

    def getOccupation(self):
        return self.occupationOptionMenu.get()


    # def callback(self, P):
    #     if str.isdigit(P) or P == "":
    #         print('callback True : {}'.format(P))
    #         return True
    #     else:
    #         print('callback False: {}'.format(P))
    #         return False
