# function to display the grade based on marks

def calculate_grade(marks):
    """Problem Statement 1: Student Grade Calculator
Write a Python program that defines a function calculate_grade(marks).
The function should:
• Accept marks (0–100) as a parameter.
• Return the grade according to the following criteria:
o 90 and above → A+
o 75–89 → A
o 60–74 → B
o 40–59 → C
o Below 40 → Fail
The main program should:
• Accept marks of 5 students.
• Call the function for each student.
• Display the marks and corresponding grade. """

    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

# main program to accept marks of 5 students and display their grades

for i in range(5):
    marks = float(input(f"Enter marks for student {i + 1}  "))
    grade = calculate_grade(marks)
    print(f"Student {i + 1}: Marks = {marks}, Grade = {grade}")


