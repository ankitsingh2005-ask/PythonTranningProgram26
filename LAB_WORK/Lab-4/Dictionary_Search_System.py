# function to search in a dict system
def search_dict(dictionary, search_key):
    """4: Dictionary Search System
Write a Python program that defines a function search_student(student_dict, roll_no).
The function should:
• Accept a dictionary where:
o Key = Roll Number
o Value = Student Name
• Search for the given roll number.
• Return the student name if found; otherwise return "Student Not Found".
The main program should:
• Create a dictionary of at least 5 students.
• Accept a roll number from the user.
• Display the search result. """

    return dictionary.get(search_key, "Student Not Found")

# main program to create a dictionary of students and search for a student by roll number
student_dict = {
    "101": "Ankit",
    "102": "Rohit",
    "103": "Priya",
    "104": "Sneha",
    "105": "Amit"
}

# accept a roll number from the user and display the search result
roll_no = input("Enter roll number to search for student: ")
result = search_dict(student_dict, roll_no)
print(result)

