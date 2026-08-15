import random

words = ["python", "computer", "program", "coding", "developer"]

word = random.choice(words)
guessed_letters = []
guesses_left = 6

print("Welcome to Hangman Game!")

while guesses_left > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guesses left:", guesses_left)

    if "_" not in display_word:
        print("Congratulations! You guessed the word!")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        guesses_left -= 1

else:
    print("\nGame Over!")
    print("The word was:", word)