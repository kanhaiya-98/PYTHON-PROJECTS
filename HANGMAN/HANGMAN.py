import random

# -------------------------------
# TODO 1: Define ASCII Art Stages
# -------------------------------

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

# -------------------------------
# TODO 2: Create a Word List
# -------------------------------

WORDS = "python hangman coding programming developer openai artificial intelligence innovation creativity learning".split()

# -------------------------------
# TODO 3: Pick a Random Word
# -------------------------------

def get_random_word(word_list):
    word = random.choice(word_list)
    return word.upper()

# -------------------------------
# TODO 4: Main Game Function
# -------------------------------

def play_hangman():
    word = get_random_word(WORDS)
    word_letters = set(word)
    guessed_letters = set()
    tries = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman! 🎉")
    print("_ " * len(word))

    # -------------------------------
    # TODO 5: Game Loop
    # -------------------------------

    while tries > 0 and len(word_letters) > 0:
        print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - tries])
        print("Guessed letters: ", ' '.join(sorted(guessed_letters)))
        
        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        if guess in word_letters:
            word_letters.remove(guess)
            print(f"Good job! {guess} is in the word.")
        else:
            tries -= 1
            print(f"Oops! {guess} is not in the word.")
        
        guessed_letters.add(guess)

        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print(' '.join(word_display))
        print()

    # -------------------------------
    # TODO 6: End Game Logic
    # -------------------------------

    if len(word_letters) == 0:
        print("Congratulations! You guessed the word:", word)
    else:
        print(HANGMAN_PICS[-1])
        print("Sorry, you ran out of tries. The word was:", word)

# -------------------------------
# TODO 7: Run the Game
# -------------------------------

if __name__ == "__main__":
    play_hangman()
