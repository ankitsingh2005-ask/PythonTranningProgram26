# input a Sentence 
sentence = input("Enter a sentence: ")

# initialize a variable to count the number of uppercase and lowercase characters
uppercase_count = 0
lowercase_count = 0

for char in sentence:
    # check if the char is uppercase without using library functions
    if char >= 'A' and char <= 'Z':
        uppercase_count += 1
    # check if the char is lowercase without using library functions
    elif char >= 'a' and char <= 'z':
        lowercase_count += 1

# display the number of uppercase and lowercase characters in the sentence
print("The number of uppercase characters in the sentence is: ", uppercase_count)
print("The number of lowercase characters in the sentence is: ", lowercase_count)