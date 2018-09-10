
import random
import os

secret_word = ''
blanks = []
guessed = []

attempts_left = 5

game_won = False
game_lost = False

help_prompt = False
running = True

def load_word():
    global secret_word
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)

def gen_blanks():
    global secret_word
    global blanks
    for i in secret_word:
        blanks.append('_')

def initialize():
    global secret_word
    global blanks
    global guessed
    global attempts_left
    global game_won
    global game_lost
    global help_prompt

    secret_word = ''
    blanks = []
    guessed = []
    attempts_left = 5
    game_won = False
    game_lost = False
    help_prompt = False

    load_word()
    gen_blanks()

def render_screen():
    global blanks
    global guessed
    global attempts_left
    global help_prompt
    global game_won
    global game_lost


    os.system('cls' if os.name == 'nt' else 'clear')
    if game_won:
        print('CONGRATS!!! You are a spaceman!')
        print()
        print('The word was: ' + secret_word)
        print()
    elif game_lost:
        print('BOO!! You got sucked up by a black hole! :\'(')
        print()
        print('The word was: ' + secret_word)
        print()
    else:
        blank_lines = ''
        guesses = ''

        for i in blanks:
            blank_lines = blank_lines + i

        for i in guessed:
            guesses = guesses + i + ' '

        print(blank_lines)
        print()
        print('Guessed: ' + guesses)
        print()
        print('Attempts left: ' + str(attempts_left))
        print()
        if help_prompt:
            print('Enter a single letter or \'quit\' to exit the program')
            print()
            help_prompt = False
        

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def check_guess(guess):
    global secret_word
    global blanks
    global guessed 
    global attempts_left

    correct_letter = False
    letter_index = 0
    for i in secret_word:
        if i == guess:
            blanks[letter_index] = guess
            correct_letter = True
        letter_index += 1

    if not correct_letter:
        for i in guessed:
            if i == guess:
                return
        attempts_left -= 1
        guessed.append(guess)

def process_input(inp):
    global help_prompt
    global running

    if inp == 'quit':
        running = False
    elif len(inp) == 1:
        check_guess(inp)
    else:
        help_prompt = True

def check_win():
    global blanks
    global attempts_left
    global game_won
    global game_lost

    if attempts_left <= 0:
        game_lost = True
        return

    found_blank = False
    for i in blanks:
        if i == '_':
            found_blank = True
            break
    
    if not found_blank:
        game_won = True
        return



initialize()
while running:
    render_screen()
    if not game_won and not game_lost:
        inp = user_input('Enter guess: ')
        process_input(inp)
        check_win()
    else:
        inp = user_input('Press enter to replay or enter \'quit\' to exit: ')
        if inp == 'quit' or inp == 'q':
            running = False
        elif not inp:
            initialize()

    