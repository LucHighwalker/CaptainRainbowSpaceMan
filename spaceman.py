
import random
import os

secret_word = ''
blanks = list()
guessed = list()

attempts_left = 7

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
    
    blanks = list('-' * len(secret_word))

def initialize():
    global secret_word
    global blanks
    global guessed
    global attempts_left
    global game_won
    global game_lost
    global help_prompt

    secret_word = ''
    blanks = list()
    guessed = list()
    attempts_left = 7
    game_won = False
    game_lost = False
    help_prompt = False

    load_word()
    gen_blanks()

def draw_spaceman():
    global attempts_left

    if attempts_left == 7:
        return '\n\n'
    elif attempts_left == 6:
        return ' o \n\n'
    elif attempts_left == 5:
        return ' o \n | \n'
    elif attempts_left == 4:
        return ' o \n/| \n'
    elif attempts_left == 3:
        return ' o \n/|\\\n'
    elif attempts_left == 2:
        return ' o \n/|\\\n/  '
    elif attempts_left == 1:
        return ' o \n/|\\\n/ \\'
    

def render_screen():
    global blanks
    global guessed
    global attempts_left
    global help_prompt
    global game_won
    global game_lost


    os.system('cls' if os.name == 'nt' else 'clear')
    if game_won:
        print('CONGRATS!!! You survive another day! :D\n\n' + 'The word was: ' + secret_word + '\n')
    elif game_lost:
        print('RIP! You got shot into space. GG :\'(\n\n' + 'The word was: ' + secret_word + '\n')
    else:
        blank_lines = ''
        guesses = ''

        for i in blanks:
            blank_lines = blank_lines + i

        for i in guessed:
            guesses = guesses + i + ' '

        print(blank_lines)
        print('\n\nGuessed: ' + guesses + '\n')
        print(draw_spaceman())
        print('\n')
        if help_prompt:
            print('Enter a single letter or \'quit\' to exit the program.\n')
            help_prompt = False
        

def user_input(prompt):
    try: 
        user_input = input(prompt)
        return user_input

    except EOFError:
        return ''


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
    elif len(inp) == 1 and inp.isalpha():
        check_guess(inp.lower())
        render_screen()
    else:
        help_prompt = True
        render_screen()

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
        if i == '-':
            found_blank = True
            break
    
    if not found_blank:
        game_won = True
        return


initialize()
render_screen()
while running:
    if not game_won and not game_lost:
        inp = user_input('Enter guess: ')
        process_input(inp)
        check_win()
    else:
        render_screen()
        inp = user_input('Press enter to replay or enter \'quit\' to exit: ')
        if inp == 'quit' or inp == 'q':
            running = False
        elif not inp:
            initialize()
            render_screen()

    