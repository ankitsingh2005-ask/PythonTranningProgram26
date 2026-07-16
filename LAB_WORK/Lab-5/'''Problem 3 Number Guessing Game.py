'''Problem 3: Number Guessing Game
Create a number guessing game.
Rules:
• Secret number = 57
• User gets only 7 attempts.
• If the user enters a negative number, ignore it using continue.
• If the user guesses correctly, terminate using break.
• Display the number of attempts used. '''

#-----------------------------------------------------------

# Number Guessing Game

secret_number = 57
attempts = 0
max_attempts = 7

print("Guess the Secret Number!")
print("You have", max_attempts, "attempts.")

while attempts < max_attempts:

    guess = int(input("Enter your guess: "))

    # Ignore negative numbers
    if guess < 0:
        print("Negative numbers are ignored.")
        continue

    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        print("Attempts Used :", attempts)
        break

    elif guess > secret_number:
        print("Too High!")

    else:
        print("Too Low!")

else:
    print("\nGame Over!")
    print("The Secret Number was", secret_number)
    print("Attempts Used :", attempts)