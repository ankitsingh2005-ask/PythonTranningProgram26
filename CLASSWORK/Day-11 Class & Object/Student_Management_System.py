# create a class with name student 

class Student:

    # Method to accept student details from the user
    def acceptData(self):
        self.student_id = int(input("Enter id of the Student: "))
        self.name = input("Enter the name of studnt: ")
        self.course = input("Enter the course name: ")
        self.marks = int(input("Enter the marks of student: "))

    # Method to display Student details
    def displayDetail(self):
        print("\n--------Student Detail----------")
        print("student ID: ", self.student_id)
        print("Name      : ", self.name)
        print("Course    : ", self.course)
        print("Marks     : ", self.marks)

    # Method to check the student marks 
    def checkResult(self):
        if self.marks >= 35:
            print("Result   : Pass")

        else:
            print("Result   : Fail")



# creating object 

student = Student()

#Calling Method 

student.acceptData()
student.displayDetail()
student.checkResult()

    