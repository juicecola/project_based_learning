import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words['data'])
    while '-' in word or ' ' in word:
        word = random.choice(words['data'])
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # Show the current state of the word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter not in word. You lost a life.")
        elif user_letter in used_letters:
            print('You have already used that character. Please try again')
        else:
            print('Invalid character. Please try again')

    if lives == 0:
        print(f"Sorry, you lost. The word was {word}.")
    else:
        print(f"Congratulations, the word is {word}")

hangman()

