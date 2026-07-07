# function to count the number of vowel in a string

def count_vowels(string):

    
    """5: Vowel Counter using Function
Write a Python program that defines a function count_vowels(text).
The function should:
• Accept a string.
• Count the total number of vowels (a, e, i, o, u) irrespective of case.
• Return the total vowel count.
The main program should:
• Accept a sentence from the user.
• Call the function.
• Display the total number of vowels."""

      # Store all vowels in a string
    vowels = "aeiouAEIOU"

    # Variable to store the vowel count
    count = 0

    # Traverse each character in the text
    for ch in string:
        # Check if the character is a vowel
        if ch in vowels:
            count += 1

    # Return the total vowel count
    return count

# -------------------main progarm-------------------

# Eccept the string by user
str = input("Enter a sentence: ")

# function calling  
total = count_vowels(str)

# display the output 
print(" The total number of vowel is: ",total)


    
    



    










