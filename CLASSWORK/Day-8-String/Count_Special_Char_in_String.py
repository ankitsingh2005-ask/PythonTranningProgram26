# input a sentence
sentence = input("Enter a sentence: ")

# initialize a variable to count the number of special characters
special_char_count = 0

# loop through each character in the sentence
for char in sentence:
    # check if the char is a special character without using library functions
    if not (char >= 'A' and char <= 'Z') and not (char >= 'a' and char <= 'z') and not (char >= '0' and char <= '9'):
        special_char_count += 1

# display the number of special characters in the sentence
print("The number of special characters in the sentence is: ", special_char_count)