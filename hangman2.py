word = "apple"
guesses = ''
turns = 5

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1

    if failed == 0:
        print("\nYou won")
        break

    guess = input("  guess a character:").lower()

    guesses += guess

    if guess not in word:
        turns -= 1
        print("\nWrong! You have", + turns, 'more guesses')

        if turns == 0:
            print("\nYou Lose")
