#IDLE source  
import random

# List of words to choose from
word_list = ['python', 'hangman', 'developer', 'challenge', 'openai', 'keyboard']

# Select a random word
word = random.choice(word_list)
word_letters = set(word)  # Unique letters in the word
guessed_letters = set()   # Letters the user has guessed
attempts = 6              # Maximum incorrect guesses allowed

print("Welcome to Hangman!")
print("_ " * len(word))

while attempts > 0 and word_letters:
    # Show current progress
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print("\nCurrent word:", ' '.join(display_word))
    print(f"Remaining attempts: {attempts}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        print("Good guess!")
        word_letters.remove(guess)
    else:
        print("Incorrect guess.")
        attempts -= 1

# Game end
if not word_letters:
    print(f"\n🎉 Congratulations! You guessed the word: {word}")
else:
    print(f"\n💀 Game over! The word was: {word}")
