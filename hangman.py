# hangman.py
# Simple text-based Hangman game
# Uses: random, lists, strings, while, if-else

import random
import string

# ---------- Configuration ----------
WORD_LIST = ["python", "flask", "database", "hangman", "developer"]  # 5 predefined words
MAX_INCORRECT = 6  # allowed incorrect guesses

# ---------- Helper functions ----------
def choose_word(word_list):
    """Randomly choose a word from the word_list."""
    return random.choice(word_list).lower()

def masked_word(word, guessed_letters):
    """Return the word display with underscores for unguessed letters."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def is_word_guessed(word, guessed_letters):
    """Return True if all letters in word have been guessed."""
    return all(letter in guessed_letters for letter in word)

def valid_guess(input_str, previous_guesses):
    """Validate that the input is a single alphabetical letter and not guessed before."""
    if len(input_str) != 1:
        return False, "Please enter a single letter."
    if input_str not in string.ascii_letters:
        return False, "Please enter an alphabetical letter (a-z)."
    letter = input_str.lower()
    if letter in previous_guesses:
        return False, f"You already guessed '{letter}'. Try another letter."
    return True, letter

# ---------- Main game ----------
def play_hangman():
    print("Welcome to Hangman!")
    print(f"You have {MAX_INCORRECT} incorrect guesses allowed.\n")

    word = choose_word(WORD_LIST)
    guessed_letters = set()
    incorrect_guesses = 0

    # keep playing until win or lose
    while True:
        # Display progress
        print("Word:", masked_word(word, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "(none)")
        print(f"Incorrect guesses left: {MAX_INCORRECT - incorrect_guesses}")

        # Check win
        if is_word_guessed(word, guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            break

        # Check lose
        if incorrect_guesses >= MAX_INCORRECT:
            print("\nSorry — you've run out of guesses.")
            print(f"The correct word was: {word}")
            break

        # Get guess from user
        user_input = input("Enter a letter: ").strip()
        valid, result = valid_guess(user_input, guessed_letters)
        if not valid:
            print(">>", result, "\n")
            continue

        letter = result  # single lowercase letter
        guessed_letters.add(letter)

        if letter in word:
            print(f"Good guess! '{letter}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{letter}' is NOT in the word.\n")

    # End of game summary
    print("\nGame Over. Thanks for playing!")

if __name__ == "__main__":
    play_hangman()