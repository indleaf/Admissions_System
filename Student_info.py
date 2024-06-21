from tkinter import * # Import tkinter
def GridManagerDemo(window):

    # Adding a label for the number of students selection
    no_mess = Label(window, text="Please select the number of students from the slider")
    no_mess.grid(row=0, column=0, columnspan=5, pady=5)

    # Adding a slider to select the number of students
    Scale(window, from_= 1, to=50, orient=HORIZONTAL, length= 300).grid(row=1, column=0, columnspan=5, pady=5, padx=10)

    # Adding a label for the names entry
    name_mess = Label(window, text="Please insert student names and press Get Names")
    name_mess.grid(row=2, column=0, columnspan=5, pady=5)

    # Adding a label and entry for student names
    Label(window, text="Enter a list of students with names:").grid(row=3, column=0, padx=10, pady=5, sticky=W)
    Entry(window).grid(row=3, column=1, columnspan=4, padx=10, pady=5, sticky=EW)

    # Adding a button to get the names
    Button(window, text="Get Name", bg="green").grid(row=4, column=0, columnspan=5, pady=10)
