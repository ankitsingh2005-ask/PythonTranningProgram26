'''Lab 2: Word Frequency Counter
Problem Statement:
Accept a sentence from the user and create a dictionary that stores the frequency of each word.
Example:
Input:
python is easy and python is powerful
Output:
{
'python': 2,
'is': 2,
'easy': 1,
'and': 1,
'powerful': 1
}
Additionally:
• Display the most frequently occurring word.
• Display all words in alphabetical order. '''

# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Create a dictionary to store the frequency of each word
word_frequency = {}

# Loop through each word in the list of words
for word in words:
    # If the word is already in the dictionary, increment its count
    if word in word_frequency:
        word_frequency[word] += 1
    # If the word is not in the dictionary, add it with a count of 1
    else:
        word_frequency[word] = 1

# Display the word frequency dictionary
print("Word frequency dictionary: ")
print(word_frequency)

# Display the most frequently occurring word
most_frequent_word = max(word_frequency, key=word_frequency.get)
print("The most frequently occurring word is: ", most_frequent_word, "with frequency: ", word_frequency[most_frequent_word])

# Display all words in alphabetical order
sorted_words = sorted(word_frequency.keys())
print("All words in alphabetical order: ")
for word in sorted_words:
    print(word, ":", word_frequency[word])

