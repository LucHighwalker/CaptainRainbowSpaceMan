
import random
import os

secret_word = ''
blanks = []
guessed = []

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
    load_word()
    gen_blanks()

def render_screen():
    global blanks
    global guessed

    blank_lines = ''
    guesses = ''

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in blanks:
        blank_lines = blank_lines + i

    for i in guessed:
        guesses = guesses + i + ' '

    print(blank_lines)
    print(guesses)
        

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def check_guess(guess):
    global secret_word
    global blanks
    global guessed 

    if len(guess) == 1:
        guessed.append(guess)
        letter_index = 0
        for i in secret_word:
            if i == guess:
                blanks[letter_index] = guess
            letter_index += 1


initialize()
running = True
while running:
    render_screen()
    guess = user_input('Enter guess: ')
    check_guess(guess)


    