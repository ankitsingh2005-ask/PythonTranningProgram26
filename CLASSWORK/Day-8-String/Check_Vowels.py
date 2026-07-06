# input the sentence

sentence = input("Enter a sentence: ")

# initialize a variable to count the number of vowels
vowel_count = 0

# loop through each character in the sentence
for char in sentence:
    # check if the character is a vowel
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or
        char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        vowel_count += 1

# display the number of vowels in the sentence
print("The number of vowels in the sentence is: ", vowel_count)