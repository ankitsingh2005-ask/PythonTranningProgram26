# create a empty list 

nums = []

# take input from user
print("Enter the elements of the list ")

# take input from user
for i in range(5):
    n = int(input("Enter an element: "))
    nums.append(n)

#typecasting the list into tuple
nums_tup = tuple(nums)

print("The tuple is: ", nums_tup)

# check for odd numbers in the tuple

for element in nums_tup:
    if element % 2 != 0:
        print(element)