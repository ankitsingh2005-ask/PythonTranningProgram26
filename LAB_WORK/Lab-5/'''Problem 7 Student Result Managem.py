'''Problem 7: Student Result Management
Create a dictionary where
Roll No → Marks
Store details of 10 students.
Perform:
• Find topper
• Find average marks
• Display students scoring above average
• Count failed students (Marks < 35)
• Display grade using:
Marks Grade
90+ A
75-89 B
60-74 C
35-59 D
Below 35 Fail'''

#-------------------------------------------------------------------------

# creating a dictionary of the student 
# Student Result Management

students = {}

# Input details of 10 students
print("Enter marks of 10 students")

for i in range(10):
    roll = input("Enter Roll Number: ")
    marks = float(input("Enter Marks: "))
    students[roll] = marks

# Find Topper
topper_roll = ""
highest_marks = -1

for roll, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        topper_roll = roll

# Calculate Average Marks
total = 0

for marks in students.values():
    total += marks

average = total / len(students)

# Count Failed Students
failed = 0

for marks in students.values():
    if marks < 35:
        failed += 1

# Display Results
print("\n------ Student Result ------")

print("Topper Roll Number :", topper_roll)
print("Highest Marks :", highest_marks)

print("Average Marks :", average)

print("\nStudents Scoring Above Average:")

for roll, marks in students.items():
    if marks > average:
        print("Roll:", roll, "Marks:", marks)

print("\nFailed Students :", failed)

print("\nGrades")

for roll, marks in students.items():

    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 60:
        grade = "C"

    elif marks >= 35:
        grade = "D"

    else:
        grade = "Fail"

    print("Roll:", roll, "Marks:", marks, "Grade:", grade)

