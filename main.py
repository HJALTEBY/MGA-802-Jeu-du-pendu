import random
import sys


def load_words():
    # Choosing if player use a custom file or not
    if input("Do you want to use a custom file? (y/n): ") == "y":

        #try catch block to handle IO exception
        try:
            filename = input("enter your file name:")
            with open(filename, 'r') as file:
                text = file.read()
                return text.split()

        #if an error occurred when trying to open the file...
        except IOError as e:
            print ("{1}".format(e.errno, e.strerror))
            print ("We will use the default file.")

    # We use the default file
    filename = "random_words.txt"

    try:
        with open(filename, 'r') as file:
            text = file.read()
            return text.split()

    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        print("The default file as probably been deleted or moved to another directory.")
        sys.exit()

def select_random_word(word_list):
    return random.choice(word_list)


def init_game_status(word):
    return {'player_life':6, 'word to guess':word, 'letter_guessed':[], 'word guessed':False}

def check_all_letters_guessed(game_state):
    for letter in game_state['word to guess']:
        if letter not in game_state['letter_guessed']:
            return False
    return True

def print_game_status(game_state):
    print(f"Player life: {game_state['player_life']}\n\n")
    print("Word: ")
    word_hided = ""
    for i in range(len(game_state['word to guess'])):
        if len(game_state['letter_guessed']) == 0:
            word_hided += "_"
        elif  game_state['letter_guessed'].count(game_state['word to guess'][i]):
            word_hided = word_hided + game_state['word to guess'][i]
        else:
            word_hided += "_"
    print(word_hided)

    if game_state['player_life'] == 0:
        print("No life left! You lost :(\n")
        print(f"The word was: {game_state['word to guess']}\n")
        return

    if check_all_letters_guessed(game_state):
        print("You guessed the word! You win!")
        game_state['word guessed'] = True

def ask_letter():
    while True:
        letter_to_guess = input("Please enter a letter to guess: ")
        if len(letter_to_guess) > 1:
            print("Too many letters! Please enter just 1 letter.\n")
        else:
            return letter_to_guess

def guess_letter(game_state):

    letter_to_guess = ask_letter()

    #if the letter is in the word
    if game_state['word to guess'].count(letter_to_guess) != 0:

        #If the letter is already guessed we won't add it
        if game_state['letter_guessed'].count(letter_to_guess) != 0:
            print("You already guessed that letter. Try again.")
        else:
            print("Well played! you guessed a new letter!")
            game_state['letter_guessed'].append(letter_to_guess)
    else:
        game_state['player_life'] -= 1
        print("This letter is not in the word.")

# Word file init

# Game init
words = load_words()
word_to_guess = select_random_word(words)
game_status = init_game_status(word_to_guess)
print_game_status(game_status)

# Game loop
while game_status['player_life'] != 0 and game_status['word guessed'] == False:
    guess_letter(game_status)
    print_game_status(game_status)

