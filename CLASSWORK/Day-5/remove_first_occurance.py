''' program to remove first occurance'''
#-----------------------------------
#------coding-----------------
#creating a blank list :
numbers = []
#input from user :
print("Enter the 5 number: ")
for x in range (5):
    num = int(input())
    numbers.append(num)
print("the list is :",numbers)

#input the number to remove from list
print("Enter number to remove from list :")
num1 = int(input())

#Removing the occurance of the number:
while num1 in numbers:
    numbers.remove(num1)
    print("Updated list : ",numbers)
else:
    print("number not found in list")

