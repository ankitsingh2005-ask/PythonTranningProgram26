'''Problem 2: Character Frequency Analyzer
Accept a string from the user and perform the following:
• Count uppercase letters
• Count lowercase letters
• Count digits
• Count special characters
• Print the most frequently occurring character
Example:
Input:
Python@2026
Output:
Uppercase : 1
Lowercase : 5
Digits : 4
Special Characters : 1
Most Frequent Character : 2
'''

#----------------------------------------------------------

# Character Frequency Analyzer

text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
special = 0

frequency = {}

# Traverse every character
for ch in text:

    if ch.isupper():
        uppercase += 1

    elif ch.islower():
        lowercase += 1

    elif ch.isdigit():
        digits += 1

    else:
        special += 1

    # Count frequency
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# Find most frequent character
max_char = ""
max_count = 0

for key in frequency:
    if frequency[key] > max_count:
        max_count = frequency[key]
        max_char = key

# Display Output
print("\n------ Character Analysis ------")
print("Uppercase Letters :", uppercase)
print("Lowercase Letters :", lowercase)
print("Digits :", digits)
print("Special Characters :", special)
print("Most Frequent Character :", max_char)