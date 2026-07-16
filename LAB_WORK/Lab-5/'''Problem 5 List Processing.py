'''Problem 5: List Processing
Accept 20 integers from the user into a list.
Perform the following:
a) Print largest number
b) Print second largest number
c) Print smallest number
d) Remove duplicate elements
e) Print only even numbers
f) Print numbers divisible by both 3 and 5
g) Reverse the list without using reverse()'''

#----------------------------------------------------------------e

# create a empty list that except 20 integer

# List Processing

numbers = []

print("Enter 20 integers:")

for i in range(20):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Largest Number
largest = max(numbers)

# Smallest Number
smallest = min(numbers)

# Second Largest Number
unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    second_largest = unique_numbers[-2]
else:
    second_largest = "Not Available"

# Remove Duplicates
duplicate_removed = list(set(numbers))

# Even Numbers
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# Divisible by both 3 and 5
divisible = []

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        divisible.append(num)

# Reverse without reverse()
reverse_list = numbers[::-1]

print("\n------ Result ------")
print("Original List :", numbers)
print("Largest Number :", largest)
print("Second Largest :", second_largest)
print("Smallest Number :", smallest)
print("Without Duplicates :", duplicate_removed)
print("Even Numbers :", even_numbers)
print("Divisible by 3 and 5 :", divisible)
print("Reversed List :", reverse_list)

