# generate a random number unknown to user
# user inputs a guess
# program informs user if guess is too high or too low

import random

def guessnumber():
    answer = random.randint(0, 100)
    guess = int(input('Guess a number: '))
    guessagain = 'y'
    while guessagain == 'y':
        if guess == answer:
            print('You guessed correctly!')
            guessagain = 'n'
        elif guess > answer:
            print('You guessed too high!')
            guessagain = input('Guess again (Y/N)? ').lower()
            if guessagain == 'y':
                guess = int(input('Guess a number: '))
            else:
                guessagain = 'n'
        else:
            print('You guessed too low!')
            guessagain = input('Guess again (Y/N)? ').lower()
            if guessagain == 'y':
                guess = int(input('Guess a number: '))
            else:
                guessagain = 'n'

guessnumber()
