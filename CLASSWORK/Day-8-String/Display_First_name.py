# take a input of full name from user 

full_name = input("Enter your full name: ")

# split the full name into first name and last name without using library functions

first_name = ""
last_name = ""

# loop through each character in the full name
for char in full_name:
    # check if the char is a space, if it is then break the loop
    if char == " ":
        break
    # if the char is not a space, then add it to the first name
    first_name += char

# loop through each character in the full name again to get the last name
for char in full_name:
    # check if the char is a space, if it is then continue to the next character
    if char == " ":
        continue
    # if the char is not a space, then add it to the last name
    last_name += char

# display the first name and last name
print("First name: ", first_name)

