def make_hangman(secret_word):
    guesses = []

    attempts_left = len(secret_word) * 2

    def hangman_closure(letter):
        nonlocal attempts_left
        # Add the guessed letter to guesses array
        guesses.append(letter)

        # Create the display word with underscores for unguessed letters
        display_word = ''.join(
            letter if letter in guesses else '_' for letter in secret_word)
        print(display_word)

        # Decrease attempts if letter is not in word
        if letter not in secret_word:
            attempts_left -= 1
            print(f"Wrong guess! {attempts_left} attempts remaining")
            if attempts_left == 0:
                print(f"Game Over! The word was: {secret_word}")
                return None  # Special return value for game over
        # Check if all letters have been guessed
        return all(letter in guesses for letter in secret_word)

    return hangman_closure


def play_hangman():
    # Get the secret word
    secret_word = input("Enter the secret word: ").lower()
    print("\n")

    # Create the game instance
    game = make_hangman(secret_word)

    # Game loop
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter!")
            continue
        result = game(guess)
        if result is None:  # Game over due to running out of attempts
            break
        elif result:  # Won the game
            print("Congratulations! You've won!")
            break


if __name__ == "__main__":
    play_hangman()
