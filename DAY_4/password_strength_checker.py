# Program to check the strength of a password
#take input from the user
password = input("Enter your password: ")
#-----------------------------------
if len(password) < 8:
    print("Weak password:Password is too short.")
else:
    print("Password Accepted.")
