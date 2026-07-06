'''Lab 1: Student Marks Management
Problem Statement:
Create a dictionary to store the marks of 5 students, where the key is the student's name and the
value is their marks.
Perform the following operations:
• Display all student names and marks.
• Add a new student with marks.
• Update the marks of an existing student.
• Delete a student by name.
• Display the student who scored the highest marks.'''

# Create a dictionary to store student marks

student_marks = {"Ankit": 85, "Rohit": 90, "Priya": 78, "Sneha": 92, "Amit": 88}

# display all student names and marks
print("Student name and marks is : ")

print(student_marks)

# add a new student with marks
new_student = student_marks["Amit"] = 95

print("After adding new student with marks : ")
print(student_marks)

# update the marks of an existing student
student_marks["Rohit"] = 95
student_marks["Ankit"] = 90
student_marks["Priya"] = 80
student_marks["Sneha"] = 95
print("After updating student marks : ")
print(student_marks)

# delete a student by name
del student_marks["Amit"]
print("After deleting student by name : ")
print(student_marks)

# display the student who scored the highest marks
highest_marks_student = max(student_marks, key=student_marks.get)
print("The student who scored the highest marks is: ", highest_marks_student, "with marks: ", student_marks[highest_marks_student])

