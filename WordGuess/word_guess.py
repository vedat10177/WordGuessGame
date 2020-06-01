"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    # create a list includes each letter as a char
    list = letter_list(secret_word)
    # create a list replace each char into line
    line = create_lines(list)
    # display the lines
    display_sign = " ".join(line)
    print("The word now looks like this: ", display_sign.upper())

    print("You have " + str(INITIAL_GUESSES) + " guesses left")
    # get guesses
    player_guess = input("Type a single letter here, then press enter: ")
    # count guesses
    current_guesses = 8
    # check the input for single letter
    pl_guess = approve_guess(player_guess)
    # check the guess for uppercase
    if pl_guess.upper() in secret_word or pl_guess.lower() in secret_word:
        print("That guess is correct.")
    else:
        print("There is no " + str(pl_guess) + " in the word")
        current_guesses -= 1
    # display list
    display_list(pl_guess,list,line)
    # print current position
    display_sign = " ".join(line)
    print("The word now looks like this: ", display_sign.upper())
    while current_guesses >= 1 and not line == list:
        print("You have " + str(current_guesses) + " guesses left")
        # get guesses
        player_guess = input("Type a single letter here, then press enter: ")
        # count guesses
        # check the input for single letter
        pl_guess = approve_guess(player_guess)
        # check the guess for uppercase
        if pl_guess.upper() in secret_word or pl_guess.lower() in secret_word:
            print("That guess is correct.")
        else:
            print("There is no " + str(pl_guess) + " in the word")
            current_guesses -= 1
            # display list
        display_list(pl_guess, list, line)
            # print current position
        display_sign = " ".join(line)
        print("The word now looks like this: ", display_sign.upper())

    check_result(line,list,secret_word)


def check_result(line,list,secret_word):
    if line == list:
        print("you won")
    else:
        print(" Sorry, you lost. The secret word was: ", secret_word)

def display_list(pl_guess,list,line):
    for i in range(len(line)):
        if pl_guess.upper() in list[i] or pl_guess.lower() in list[i]:
            del line[i]
            line.insert(i,pl_guess.upper())
    return line

def validate(pl_guess,secret_word,current_guesses):
    if pl_guess.upper() in secret_word or pl_guess.lower() in secret_word:
       print("That guess is correct.")
       return current_guesses
    else:
       print("There is no " + str(pl_guess) +" in the word")
       current_guesses -= 1
       return current_guesses

def approve_guess(player_guess):
     while True:
        if player_guess.isalpha() and  len(player_guess) == 1  :
            return player_guess
        else:
            print("Guess should only be a single character.")
            player_guess = input("Type a single letter here, then press enter: ")





def letter_list(secret_word):
    word = []
    for char in secret_word:
        word.append(char)
    return word

def create_lines(list):
    lines = []
    for char in list:
        lines.append('_')
    return lines


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    words = []
    for line in open(LEXICON_FILE):
        line = line.strip()
        words.append(line)

    index = random.randrange(0,len(words))
    return words[index]




def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()