class Studentsss:
    def __init__(self, math=50, science=50, language=50, drama=50, music=50, biology=50):
        self.students = []  # List to store student information
        self.schools = []   # List to store assigned schools
        self.gpa_list = []  # List to store student names and their GPA

        # Initialize grades for each subject
        self.math = math
        self.science = science
        self.language = language
        self.drama = drama
        self.music = music
        self.biology = biology

    def calculateGPA(self, grades):
        # Define the fixed credit hours for each subject
        math_credit_hours = 4
        science_credit_hours = 5
        language_credit_hours = 4
        drama_credit_hours = 3
        music_credit_hours = 2
        biology_credit_hours = 4

        # Calculate the total credit hours
        total_credit_hours = (math_credit_hours + science_credit_hours + language_credit_hours +
                              drama_credit_hours + music_credit_hours + biology_credit_hours)

        # Calculate the total points
        total_points = (grades[0] * math_credit_hours +
                        grades[1] * science_credit_hours +
                        grades[2] * language_credit_hours +
                        grades[3] * drama_credit_hours +
                        grades[4] * music_credit_hours +
                        grades[5] * biology_credit_hours)

        # Calculate the GPA
        gpa = total_points / total_credit_hours
        return gpa

    def get_student_info(self, students):
        for name, grades in students.items():
            valid_grades = False
            while not valid_grades:
                valid_grades = True  # Assume all grades are initially valid
                for course, grade in grades.items():
                    if not (0 <= grade <= 100):
                        valid_grades = False
                        print(f"Invalid grade for {course}: {grade}. Grade must be between 0 and 100.")
                        break
                if not valid_grades:
                    # Re-enter all grades for the student
                    grades['Math'] = int(input("Enter Math grade: "))
                    grades['Science'] = int(input("Enter Science grade: "))
                    grades['Language'] = int(input("Enter Language grade: "))
                    grades['Drama'] = int(input("Enter Drama grade: "))
                    grades['Music'] = int(input("Enter Music grade: "))
                    grades['Biology'] = int(input("Enter Biology grade: "))

            # Append student info and calculate GPA
            self.students.append((name, list(grades.values())))  # Convert grades dictionary to list
            gpa = self.calculateGPA(list(grades.values()))  # Calculate GPA from grades list
            self.gpa_list.append((name, gpa))

    def assign_schools(self):
        for name, grades in self.students:
            gpa = self.calculateGPA(grades)
            if 90 <= gpa <= 100:
                self.schools.append("School of Engineering")
            elif 80 <= gpa < 90:
                self.schools.append("School of Business")
            elif 70 <= gpa < 80:
                self.schools.append("Law School")
            else:
                self.schools.append("Not accepted")

def validate_password(s): 
    u, p, d = 0, 0, 0 
    special_char = "!@#$%^&*()_+[]{}|;:,.<>?/" 
    if len(s) >= 10: 
        for i in s: 
            # counting uppercase alphabets 
            if i.isupper(): 
                u += 1            
            # counting digits 
            if i.isdigit(): 
                d += 1            
            # counting the mentioned special characters 
            if i in special_char: 
                p += 1           
    if u >= 1 and p >= 1 and d > 1 and d < 4: 
        return "Password is valid"
    else: 
        return "Invalid Password"    

def main():
    print("Welcome to Humber College")
    
    # Password input
    attempts = 0
    while attempts < 3:
        password = input("Please enter your password: ")
        if validate_password(password) == "Password is valid":
            break
        else:
            attempts += 1
            print("Invalid password. Please try again.")
    if attempts == 3:
        print("You have exceeded the maximum number of attempts. Exiting program.")
        return
    
    # Number of students input
    num_students = 0
    attempts = 0
    while attempts < 3:
        num_students_input = input("Please enter the number of students (1-50): ")
        if num_students_input.isdigit():
            num_students = int(num_students_input)
            if 1 <= num_students <= 50:
                break
            else:
                attempts += 1
                print("Invalid input. Please enter a number between 1 and 50.")
        else:
            attempts += 1
            print("Invalid input. Please enter a numerical value.")
    else:
        print("You have exceeded the maximum number of attempts. Exiting program.")
        return
    
    # Student data input
    students = {}
    choice = input("To input values manually, enter 1. To use the test set, enter 2: ")
    if choice == '2':
        students = students = {
        'John Doe': {'Math': 85, 'Science': 90, 'Language': 78, 'Drama': 88, 'Music': 92, 'Biology': 80},
        'Jane Smith': {'Math': 72, 'Science': 84, 'Language': 90, 'Drama': 76, 'Music': 85, 'Biology': 88},
        'Alice Johnson': {'Math': 95, 'Science': 92, 'Language': 82, 'Drama': 80, 'Music': 78, 'Biology': 85},
        'Bob Brown': {'Math': 60, 'Science': 70, 'Language': 68, 'Drama': 58, 'Music': 62, 'Biology': 65},
        'Charlie Davis': {'Math': 88, 'Science': 76, 'Language': 85, 'Drama': 89, 'Music': 90, 'Biology': 78},
        'David Wilson': {'Math': 90, 'Science': 85, 'Language': 92, 'Drama': 87, 'Music': 90, 'Biology': 86},
        'Eve Thompson': {'Math': 78, 'Science': 80, 'Language': 85, 'Drama': 83, 'Music': 88, 'Biology': 84},
        'Frank Harris': {'Math': 65, 'Science': 70, 'Language': 72, 'Drama': 66, 'Music': 70, 'Biology': 68},
        'Grace Lee': {'Math': 85, 'Science': 88, 'Language': 90, 'Drama': 80, 'Music': 75, 'Biology': 80},
        'Henry Clark': {'Math': 92, 'Science': 95, 'Language': 88, 'Drama': 90, 'Music': 85, 'Biology': 92},
        'Isabella Martinez': {'Math': 70, 'Science': 72, 'Language': 75, 'Drama': 68, 'Music': 70, 'Biology': 74},
        'Jack Robinson': {'Math': 80, 'Science': 85, 'Language': 88, 'Drama': 82, 'Music': 84, 'Biology': 86},
        'Kathy Lewis': {'Math': 88, 'Science': 92, 'Language': 90, 'Drama': 85, 'Music': 87, 'Biology': 89},
        'Liam Walker': {'Math': 74, 'Science': 78, 'Language': 80, 'Drama': 76, 'Music': 79, 'Biology': 77},
        'Mia Hall': {'Math': 90, 'Science': 94, 'Language': 85, 'Drama': 88, 'Music': 92, 'Biology': 91},
        'Nathan Young': {'Math': 68, 'Science': 70, 'Language': 65, 'Drama': 60, 'Music': 65, 'Biology': 70},
        'Olivia King': {'Math': 85, 'Science': 87, 'Language': 90, 'Drama': 80, 'Music': 82, 'Biology': 85},
        'Paul Green': {'Math': 90, 'Science': 88, 'Language': 85, 'Drama': 89, 'Music': 90, 'Biology': 88},
        'Quinn Adams': {'Math': 72, 'Science': 75, 'Language': 78, 'Drama': 70, 'Music': 74, 'Biology': 73},
        'Ryan Baker': {'Math': 88, 'Science': 90, 'Language': 92, 'Drama': 85, 'Music': 87, 'Biology': 89},
        'Sophia Gonzalez': {'Math': 80, 'Science': 82, 'Language': 84, 'Drama': 78, 'Music': 80, 'Biology': 83},
        'Tom Wright': {'Math': 75, 'Science': 78, 'Language': 80, 'Drama': 72, 'Music': 74, 'Biology': 76},
        'Uma Patel': {'Math': 85, 'Science': 87, 'Language': 90, 'Drama': 85, 'Music': 88, 'Biology': 90},
        'Victor Scott': {'Math': 90, 'Science': 92, 'Language': 88, 'Drama': 85, 'Music': 87, 'Biology': 89},
        'Wendy Mitchell': {'Math': 70, 'Science': 72, 'Language': 75, 'Drama': 68, 'Music': 70, 'Biology': 74},
        'Xavier Perez': {'Math': 80, 'Science': 85, 'Language': 88, 'Drama': 82, 'Music': 84, 'Biology': 86},
        'Yara Collins': {'Math': 88, 'Science': 92, 'Language': 90, 'Drama': 85, 'Music': 87, 'Biology': 89},
        'Zoe Turner': {'Math': 74, 'Science': 78, 'Language': 80, 'Drama': 76, 'Music': 79, 'Biology': 77},
        'Aaron Edwards': {'Math': 68, 'Science': 70, 'Language': 65, 'Drama': 60, 'Music': 65, 'Biology': 70},
        'Bella Roberts': {'Math': 90, 'Science': 94, 'Language': 85, 'Drama': 88, 'Music': 92, 'Biology': 91},}
    else:
        for _ in range(num_students):
            name = input("Enter student name: ")
            grades = {}
            grades['Math'] = int(input("Enter Math grade: "))
            grades['Science'] = int(input("Enter Science grade: "))
            grades['Language'] = int(input("Enter Language grade: "))
            grades['Drama'] = int(input("Enter Drama grade: "))
            grades['Music'] = int(input("Enter Music grade: "))
            grades['Biology'] = int(input("Enter Biology grade: "))
            students[name] = grades
            print(students)
    
    # Create student system
    student_system = Studentsss()

    # Process student data
    student_system.get_student_info(students)

    # Assign schools
    student_system.assign_schools()
    
    # Print reports
    print("\nReport 1: Student Name, School Name")
    for i in range(len(student_system.students)):
        student = student_system.students[i]
        school = student_system.schools[i]
        print(f"{student[0]}: {school}")

    # Additional reports
    accepted_students = [school for school in student_system.schools if school != "Not accepted"]
    not_accepted_students = len(student_system.students) - len(accepted_students)

    print("\nReport 2: Number of accepted students in Humber college showing students distribution per each school.")
    unique_schools = []
    for school in accepted_students:
        if school not in unique_schools:
            unique_schools.append(school)

    for school in unique_schools:
        print(f"{school}: {accepted_students.count(school)}")

    print("\nReport 3: Number of students that are not accepted.")
    print(f"Not accepted: {not_accepted_students}")

    print("\nReport 4: Additional report")
    # Initialize highest and lowest GPA values and corresponding students
    max_gpa_student = ("", 0)
    min_gpa_student = ("", 101)

    # Find the student with the highest and lowest GPA
    total_gpa = 0
    for student in student_system.gpa_list:
        total_gpa += student[1]
        if student[1] > max_gpa_student[1]:
            max_gpa_student = student
        if student[1] < min_gpa_student[1]:
            min_gpa_student = student

    num_students = len(student_system.gpa_list)
    average_gpa = total_gpa / num_students

    print(f"Average GPA: {average_gpa:.2f}")
    if max_gpa_student[0]:
        print(f"Student with the highest GPA: {max_gpa_student[0]} with a GPA of {max_gpa_student[1]:.2f}")
    if min_gpa_student[0]:
        print(f"Student with the lowest GPA: {min_gpa_student[0]} with a GPA of {min_gpa_student[1]:.2f}")

if __name__ == "__main__":
    main()
