'''Program to calculate the factorial of a number'''
#input of the number from the user
num = int(input("Enter a number: "))
#--------------------------------------
if (num < 0):
    # negative number 
    print("factorial is not possible")
elif (num == 0):
    # factorial of 0 is 1
    print("factorial is 1")
else:
    # positive number
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    print("factorial is", factorial)

