import random

def load_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text.split() # Basic word extraction

def select_random_word(words):
    return random.choice(words)


def init_game_status(word):
    return {'player_life':6, 'word to guess':word, 'letter_guessed':[], 'word guessed':False}

def check_all_letters_guessed(game_status):
    for letter in game_status['word to guess']:
        if letter not in game_status['letter_guessed']:
            return False
    return True

def print_game_status(game_status):
    print(f"Player life: {game_status['player_life']}\n\n")
    print("Word: ")
    word_hided = ""
    for i in range(len(game_status['word to guess'])):
        if len(game_status['letter_guessed']) == 0:
            word_hided += "_"
        elif  game_status['letter_guessed'].count(game_status['word to guess'][i]):
            word_hided = word_hided + game_status['word to guess'][i]
        else:
            word_hided += "_"
    print(word_hided)

    if game_status['player_life'] == 0:
        print("No life left! You lost :(\n")
        print(f"The word was: {game_status['word to guess']}\n")
        return

    if check_all_letters_guessed(game_status):
        print("You guessed the word! You win!")
        game_status['word guessed'] = True

def ask_letter():
    while (True):
        letter_to_guess = input("Please enter a letter to guess: ")
        if len(letter_to_guess) > 1:
            print("Too many letters! Please enter just 1 letter.\n")
        else:
            return letter_to_guess

def guess_letter(game_status):

    letter_to_guess = ask_letter()

    #if the letter is in the word
    if game_status['word to guess'].count(letter_to_guess) != 0:

        #If the letter is already guessed we won't add it
        if game_status['letter_guessed'].count(letter_to_guess) != 0:
            print("You already guessed that letter. Try again.")
        else:
            print("Well played! you guessed a new letter!")
            game_status['letter_guessed'].append(letter_to_guess)
    else:
        game_status['player_life'] -= 1
        print("This letter is not in the word.")

# Game init
print("Choosing a random word...\n")
words = load_words("data/random_words.txt")
word_to_guess = select_random_word(words)
game_status = init_game_status(word_to_guess)
print_game_status(game_status)

# Game loop
while game_status['player_life'] != 0 and game_status['word guessed'] == False:
    guess_letter(game_status)
    print_game_status(game_status)

