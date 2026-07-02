'''An electricity department wants to analyze the electricity consumption of N houses. Accept the monthly units consumed by each houses
Calculate and display
. total unit consumed
. Average:'''

#Program to analyze electricity bill based on units consumed
# take input from the user
n = int(input("Enter the number of houses: "))

unit = []
# take input for each house
for i in range(n):
    units = int(input("Enter the units consumed by house {}: ".format(i + 1)))
    unit.append(units)




