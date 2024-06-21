from tkinter import * # Import tkinter
def grades(window):

    # Adding a label for the number of students selection
    no_mess = Label(window, text="Please enter grades of students")
    no_mess.grid(row=0, column=0, columnspan=5, pady=5)

    # Adding a slider to select the number of students
    Text(window, height = 5, width = 52).grid(row=1, column=0, columnspan=5, pady=5, padx=10)
