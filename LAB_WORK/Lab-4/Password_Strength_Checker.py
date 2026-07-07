# function to check the strength of a password 

def check_password_strength(password):
    """3: Password Strength Checker
Write a function check_password(password) that checks whether a password is strong.
A password is considered Strong if:
• It contains at least 8 characters.
• It contains at least one uppercase letter.
• It contains at least one lowercase letter.
• It contains at least one digit.
The function should return:
• "Strong Password" or
• "Weak Password"
The main program should accept a password from the user and display the result."""

    # check the length of the password
    if len(password) < 8:
        return "Weak Password: Password must be at least 8 characters long."
    
    # check for at least one uppercase letter, one lowercase letter, and one digit
    elif not any(char.isupper() for char in password):
        return "Weak Password: Password must contain at least one uppercase letter."
    
    # check for at least one lowercase letter
    elif not any(char.islower() for char in password):
        return "Weak Password: Password must contain at least one lowercase letter."
    
    # check for at least one digit
    elif not any(char.isdigit() for char in password):
        return "Weak Password: Password must contain at least one digit."
    
    # if all conditions are met, the password is strong
    else:
        return "Strong Password"
    
# main program to accept a password from the user and display the result
password = input("Enter a password to check its strength: ")        

strength = check_password_strength(password)

print(strength)
