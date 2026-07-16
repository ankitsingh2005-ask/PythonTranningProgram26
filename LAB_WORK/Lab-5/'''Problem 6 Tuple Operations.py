'''Problem 6: Tuple Operations
Create a tuple containing names of 15 students.
Perform the following:
• Count total students
• Display first five students
• Display last five students
• Search a student name
• Count occurrences of a given name
• Convert tuple into list and sort alphabetically '''

#---------------------------------------------------------------

#create empty tuple that contain 15 student 

# Tuple Operations

students = (
    "Ankit", "Rahul", "Priya", "Aman", "Neha",
    "Riya", "Karan", "Rohit", "Simran", "Aditi",
    "Aryan", "Pooja", "Vikas", "Sneha", "Mohit"
)

# Total Students
print("Total Students :", len(students))

# First Five Students
print("\nFirst Five Students:")
print(students[:5])

# Last Five Students
print("\nLast Five Students:")
print(students[-5:])

# Search Student
name = input("\nEnter student name to search: ")

if name in students:
    print(name, "is present in the tuple.")
else:
    print(name, "is not present.")

# Count Occurrences
search_name = input("\nEnter name to count occurrences: ")
count = students.count(search_name)
print(search_name, "appears", count, "time(s).")

# Convert Tuple to List
student_list = list(students)

# Sort Alphabetically
student_list.sort()

print("\nStudents in Alphabetical Order:")
print(student_list)

    
