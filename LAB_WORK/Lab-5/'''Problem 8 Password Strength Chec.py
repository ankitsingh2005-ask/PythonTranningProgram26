'''Problem 8: Password Strength Checker
Accept a password and check whether it satisfies:
• Minimum 8 characters
• At least one uppercase letter
• At least one lowercase letter
• At least one digit
• At least one special character
Output:
Strong Password
or
Weak Password
Also display the missing conditions.
'''

#-------------------------------------------------------------
# Password Strength Checker

password = input("Enter Password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

# Check every character
for ch in password:

    if ch.isupper():
        has_upper = True

    elif ch.islower():
        has_lower = True

    elif ch.isdigit():
        has_digit = True

    elif ch in special_characters:
        has_special = True

print("\n------ Password Report ------")

strong = True

# Check all conditions

if len(password) < 8:
    print("Minimum 8 characters required.")
    strong = False

if not has_upper:
    print("Missing Uppercase Letter.")
    strong = False

if not has_lower:
    print("Missing Lowercase Letter.")
    strong = False

if not has_digit:
    print("Missing Digit.")
    strong = False

if not has_special:
    print("Missing Special Character.")
    strong = False

if strong:
    print("Strong Password")
else:
    print("Weak Password")