# Program for atm pin verification
pin = 4589
# user enter the pin input from user 
user_pin = int(input("Enter your PIN: "))

if user_pin == pin:
    print("Access granted")
else:
    
    print("Incorrect PIN")


