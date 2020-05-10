# generate a random number unknown to user
# user inputs a guess
# program informs user if guess is too high or too low

import random

def inputNumber(message):  # totes got this off the web since I had no clue how to do this on my own :(
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print('That is not a number!')
            continue
        else:
            return userInput
        break

def guessnumber():
    answer = random.randint(0, 100)
    guess = inputNumber('Guess a number: ')
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
