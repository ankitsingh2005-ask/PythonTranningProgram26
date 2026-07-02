# program to generate multiplication table of a number
# take input from the user
num = int(input("Enter a number: "))

# generate multiplication table
for i in range(1, 21):
    print(num, "x", i, "=", num * i)
    
