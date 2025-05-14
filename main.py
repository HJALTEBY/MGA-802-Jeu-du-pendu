import random

def load_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()  # Basic word extraction
    return words

def select_random_word(words):
    return random.choice(words)

def init_game_status(word):
    return {'player_life':6, 'word to guess':word}

# Game init

print("Choosing a random word...\n")
words = load_words("data/random_words.txt")
word_to_guess = select_random_word(words)
game_status = init_game_status(word_to_guess)



print(word_to_guess)
