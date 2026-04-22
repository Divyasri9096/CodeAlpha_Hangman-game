import random

# List of words
words = ["apple", "tiger", "house", "plant", "chair"]

# Choose a random word
word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(word)

# Number of guesses
guesses = 6

print("Welcome to Hangman Game!")

# Game loop
while guesses > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guesses left:", guesses)

    guess = input("Enter a letter: ").lower()

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong!")
        guesses -= 1

# Result
if "_" not in guessed_word:
    print("\nYou Won! The word was:", word)
else:
    print("\nYou Lost! The word was:", word)
