''' program to find the factors of a number '''

#input of the number from the user
num = int(input("Enter a number: "))

#--------------------------------------
if (num == 0):
    print("infinite factors")
elif (num < 0):
    print("Factors are: ")
    for x in range(1, num + 1):

        # to check divisibility of the number
        if (num % x == 0):
            print(x, end=",")

else:
    #negative number has infinite factors
    
    print("Factors are: ")
    for x in range(1, num + 1):

        # to check divisibility of the number
        if (num % x == 0):
            print(x, end=",")


