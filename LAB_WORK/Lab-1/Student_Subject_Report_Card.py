'''Lab 5: Student Subject Report Card
Problem Statement:
Create a nested dictionary to store marks of students in three subjects.
Example:
{
'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
'Priya': {'Math': 78, 'Science': 95, 'English': 82},
'Ankit': {'Math': 91, 'Science': 89, 'English': 94}
}
Write a program to:
• Calculate the total marks of each student.
• Calculate the average marks of each student.
• Display the topper based on total marks.
• Display the subject-wise highest marks along with the student's name.'''

# Create a nested dictionary to store marks of students in three subjects
student_marks = {
    'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
    'Priya': {'Math': 78, 'Science': 95, 'English': 82},
    'Ankit': {'Math': 91, 'Science': 89, 'English   ': 94}
}

# Calculate the total marks of each student
for student, marks in student_marks.items():
    total_marks = sum(marks.values())
    student_marks[student]['Total'] = total_marks
    average_marks = total_marks / len(marks)
    student_marks[student]['Average'] = average_marks

# Display the total and average marks of each student
print("Student marks report card: ")
for student, marks in student_marks.items():
    print(f"Student: {student}, Total Marks: {marks['Total']}, Average Marks: {marks['Average']}")

# Display the topper based on total marks
topper = max(student_marks, key=lambda x: student_marks[x]['Total'])
print(f"The topper is: {topper} with total marks: {student_marks[topper]['Total']}")

# Display the subject-wise highest marks along with the student's name
subject_wise_highest = {}   
for student, marks in student_marks.items():
    for subject, mark in marks.items():
        if subject not in ['Total', 'Average']:
            if subject not in subject_wise_highest or mark > subject_wise_highest[subject][1]:
                subject_wise_highest[subject] = (student, mark)

# Display the subject-wise highest marks along with the student's name
print("\nSubject-wise highest marks: ")
for subject, (student, mark) in subject_wise_highest.items():
    print(f"{subject}: {student} - {mark}") 

