import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tm
from pass_val_v2 import validate_password
from Student_info import GridManagerDemo
from grades_info import grades
from Reports_v2 import reports

"""def outer_func(parameter):
    def inner_func():
        validate_password(parameter.get())
    return inner_func"""

def clear_widgets():
    for widget in window.winfo_children():
        widget.destroy()
    
#Enter Student grades
def rep():
    clear_widgets()
    reports(window)
    
#Enter Student Reports
def student_grades():
    clear_widgets()
    grades(window)
    done = tk.Button(window, text="Done",bg ="red", command= rep) #outer_func(pass_txt))
    done.grid(row=5, column=0, columnspan=5, pady=10)
    
#Enter Student names
def student_names():
        clear_widgets()
        GridManagerDemo(window)
        done = tk.Button(window, text="Done",bg ="red", command= student_grades) #outer_func(pass_txt))
        done.grid(row=5, column=0, columnspan=5, pady=10)
        #tk.Label(window, text='Hello Admin !!', bg='brown', fg='white').grid(row=0, column=1, padx=20, pady=20)


def valid():
    x = pass_txt.get()
    y= validate_password(x)
    if y == "Password is valid":
        tm.showinfo("Login Info", "Login Successfully")
        student_names()
        return out_str.set(y)
    else:
        return out_str.set(y)
    

# Create the main window
window = tk.Tk()
window.title("Humber Student Evaluator")
window.geometry('800x600')


#create humber logo image
photo = PhotoImage(file = "GUI_final\data\Logo.gif")
# frame1 to contain label and canvas
frame1 = ttk.Frame(master =window)
hum_logo = ttk.Label(master = frame1, image = photo)
hum_logo.pack(side = 'left', padx=20)
frame1.pack()

#Create a title
heading = Label(window, text = "Welcome to Humber College!", font=("Arial", 26, "bold"))
heading.pack()

# Create and place the password label and entry
password_label = tk.Label(window, text="Password:")
password_label.pack()

#Entery
pass_txt = tk.StringVar(value='Enter a Password')
password_entry = ttk.Entry(window, textvariable= pass_txt, width = 50)
password_entry.pack()
# Create and place the login button
login_button = tk.Button(window, text="Login", command= valid) #outer_func(pass_txt))
login_button.pack()

#Output
out_str = tk.StringVar()
out_val = ttk.Label(master = window, textvariable = out_str )
out_val.pack()




# Start the Tkinter event loop
window.mainloop()