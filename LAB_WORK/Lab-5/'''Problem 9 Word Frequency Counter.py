'''Problem 9: Word Frequency Counter
Topics: Function, Dictionary, String, List
Accept a sentence from the user.
Create a function:
word_frequency(sentence)
The function should:
• Remove punctuation.
• Ignore case sensitivity.
• Count frequency of every word.
• Display words in alphabetical order.
• Print the most repeated word.
Example:
Input:
Python is easy. Python is powerful.
Output
easy :1
is :2
powerful :1
python :2
Most Repeated:
python
'''
#----------------------------------------------------------------

# Word Frequency Counter

def word_frequency(sentence):

    # Convert to lowercase
    sentence = sentence.lower()

    # Remove punctuation
    punctuation = ".,!?;:-'\"()[]{}"

    for ch in punctuation:
        sentence = sentence.replace(ch, "")

    # Split sentence into words
    words = sentence.split()

    # Create dictionary
    frequency = {}

    # Count frequency
    for word in words:

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Display words alphabetically
    print("\nWord Frequencies\n")

    for word in sorted(frequency):
        print(word, ":", frequency[word])

    # Find most repeated word
    max_word = ""
    max_count = 0

    for word in frequency:

        if frequency[word] > max_count:
            max_count = frequency[word]
            max_word = word

    print("\nMost Repeated Word :", max_word)


# Main Program
sentence = input("Enter a sentence: ")

word_frequency(sentence)