# function to analyze a list of numbers and return the sum, average, maximum, and minimum values
def analyze_list(numbers):
    """2: List Analysis using Functions
Write a Python program that defines the following functions:
• find_max(numbers)
• find_min(numbers)
• find_average(numbers)
The program should:
• Accept a list of 10 integers from the user.
• Call all three functions.
• Display the maximum value, minimum value, and average of the list. """ 

    if not numbers:
        return None, None, None, None

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total_sum, average, maximum, minimum

# main program to accept a list of 10 integers from the user and display the analysis
numbers = []

for i in range(10):
    num = int(input(f"Enter integer {i + 1}: "))
    numbers.append(num)

total_sum, average, maximum, minimum = analyze_list(numbers)

print(f"Sum: {total_sum}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")


