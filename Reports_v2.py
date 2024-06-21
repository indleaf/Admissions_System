from tkinter import * # Import tkinter

def reports(window):
    no_mess1 = Label(window, text="Below find reports of the students")
    no_mess1.grid(row=0, column=0, columnspan=5, pady=5)

    report_text="""Report 1: Student Name, School Name
John Doe: School of Business
Jane Smith: School of Business
Alice Johnson: School of Business
Bob Brown: Not accepted
Charlie Davis: School of Business
David Wilson: School of Business
Eve Thompson: School of Business
Frank Harris: Not accepted
Grace Lee: School of Business
Henry Clark: School of Engineering
Isabella Martinez: Law School
Jack Robinson: School of Business
Kathy Lewis: School of Business
Liam Walker: Law School
Mia Hall: School of Engineering
Nathan Young: Not accepted
Olivia King: School of Business
Paul Green: School of Business
Quinn Adams: Law School
Ryan Baker: School of Business
Sophia Gonzalez: School of Business
Tom Wright: Law School
Uma Patel: School of Business
Victor Scott: School of Business
Wendy Mitchell: Law School
Xavier Perez: School of Business
Yara Collins: School of Business
Zoe Turner: Law School
Aaron Edwards: Not accepted
Bella Roberts: School of Engineering

Report 2: Number of accepted students in Humber college showing students distribution per each school.
School of Business: 17
School of Engineering: 3
Law School: 6

Report 3: Number of students that are not accepted.
Not accepted: 4

Report 4: Additional report
Average GPA: 81.51
Student with the highest GPA: Henry Clark with a GPA of 91.05
Student with the lowest GPA: Bob Brown with a GPA of 64.55
Rejection Rate 13.0
Acceptance Rate 87.0"""

    # Adding a Text widget to display the reports
    report_text_widget = Text(window, wrap=WORD, height=30, width=100)
    report_text_widget.insert(END, report_text)
    report_text_widget.grid(row=1, column=1, columnspan=5, pady=5)

    # Adding a Scrollbar to the Text widget
    scrollbar = Scrollbar(window, command=report_text_widget.yview)
    scrollbar.grid(row=1, column=6, sticky='ns')
    report_text_widget.config(yscrollcommand=scrollbar.set)