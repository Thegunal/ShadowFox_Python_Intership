import random

# Word list for the game
words = ["python", "developer", "internship", "shadowfox", "programming"]

# Choose a random word
word = random.choice(words).lower()
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("🎮 Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Used letters:", ", ".join(used_letters))
    
    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that letter!")
        continue

    used_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
        for idx, letter in enumerate(word):
            if letter == guess:
                guessed[idx] = guess
    else:
        print("❌ Wrong guess!")
        attempts -= 1

# Final Result
if "_" not in guessed:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game over! The word was:", word)