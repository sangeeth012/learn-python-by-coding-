import random

print("Welcome to the Hangman program!")

# Word list
name_list = ["sangeeth", "gowtham", "sumathi", "kuppusamy", "tiger"]
random_computer_choice = random.choice(name_list)
word = ["_"] * len(random_computer_choice)
print(" ".join(word))

# Set lives
lives = 5
wrong_guesses = []

while "_" in word and lives > 0:
    user_guess = input("Guess a letter: ").lower()

    if user_guess in random_computer_choice:
        # Correct guess → fill in the blanks
        for i in range(len(random_computer_choice)):
            if random_computer_choice[i] == user_guess:
                word[i] = user_guess
        print("✅ Good guess!")
    else:
        # Wrong guess → lose a life
        if user_guess not in wrong_guesses:  # avoid double penalty
            wrong_guesses.append(user_guess)
            lives -= 1
            print(f"❌ Wrong guess! Lives left: {lives}")
        else:
            print("⚠️ You already tried that letter!")

    print(" ".join(word))
    print("Wrong guesses so far:", wrong_guesses)

# End of game
if "_" not in word:
    print(f"\n🎉 Congratulations! You guessed the word: {random_computer_choice}")
else:
    print(f"\n💀 Game Over! The word was: {random_computer_choice}")
