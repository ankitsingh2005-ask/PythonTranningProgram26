'''Lab 3: Employee Information System
Problem Statement:
Create a dictionary where:
• Employee ID is the key.
• Value is another dictionary containing:
o Name
o Department
o Salary
Perform the following operations:
• Display all employee details.
• Search for an employee using Employee ID.
• Increase the salary of all employees by 10%.
• Display employees belonging to a specific department entered by the user. clear'''

# Create a dictionary to store employee information
employee_info = {
    101: {"Name": "Ankit", "Department": "HR", "Salary": 50000},
    102: {"Name": "Shagar", "Department": "Finance", "Salary": 60000},
    103: {"Name": "Sanjay", "Department": "IT", "Salary": 70000},
    104: {"Name": "Alok", "Department": "Marketing", "Salary": 55000},
    105: {"Name": "Priya", "Department": "IT", "Salary": 65000}
}   

# Display all employee details
print("Employee details: ")
for emp_id, details in employee_info.items():
    print(f"Employee ID: {emp_id}, Name: {details['Name']}, Department: {details['Department']}, Salary: {details['Salary']}")

# Search for an employee using Employee ID
search_id = int(input("Enter Employee ID to search: "))
if search_id in employee_info:
    details = employee_info[search_id]
    print(f"Employee ID: {search_id}, Name: {details['Name']}, Department: {details['Department']}, Salary: {details['Salary']}")

    # Increase the salary of all employees by 10%
    for emp_id in employee_info:
        employee_info[emp_id]["Salary"] *= 1.10

    print("After increasing salary by 10%: ")
    for emp_id, details in employee_info.items():
        print(f"Employee ID: {emp_id}, Name: {details['Name']}, Department: {details['Department']}, Salary: {details['Salary']}")

# Display employees belonging to a specific department entered by the user
department = input("Enter department to display employees: ")
print(f"Employees in {department} department: ")
for emp_id, details in employee_info.items():   
    if details["Department"].lower() == department.lower():
        print(f"Employee ID: {emp_id}, Name: {details['Name']}, Salary: {details['Salary']}")


