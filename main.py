import random

# List of words
words = ["apple", "python", "computer", "student", "mobile"]

# Randomly select a word
word = random.choice(words)

guessed_letters = []
tries = 6

print("=== Welcome to Hangman Game ===")

while tries > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        guessed_letters.append(guess)
        tries -= 1
        print("Wrong! Remaining chances:", tries)

if tries == 0:
    print("\nGame Over!")
    print("The correct word was:", word)