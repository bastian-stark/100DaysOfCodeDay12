# Number Guessing Game App

import random

def generate_number():
    """Randomly chooses a number between 1 and 100"""
    return random.randint(1, 100)

def choose_difficulty():
    """Asks user for difficulty setting and outputs the response as number of lives (Easy: 15; Normal: 10; Hard: 5)"""
    response = input('Choose a difficulty. Type "easy", "normal", or "hard": ').lower()
    if response == "easy":
        return difficulties[1]
    elif response == "normal":
        return difficulties[2]
    elif response == "hard":
        return difficulties[3]
    else:
        print('Invalid response. Please try again.')
        return choose_difficulty()

def check_guess(guess, number):
    """Checks if the guessed number is higher, lower, or equal to correct answer"""
    if guess == number:
        print('Correct! You win!')
        return True
    elif guess > number:
        print('Too high!')
        return False
    elif guess < number:
        print('Too low!')
        return False
    else:
        print('Error')

def makeGuess(number, lives):
    """Executes guessing loop"""
    print(f'You have {lives} attempts remaining to guess the number. ')
    guess = int(input('Make a guess: '))
    checkGuess = check_guess(guess, number)
    if checkGuess == False:
        lives -= 1
        if lives > 0:
            makeGuess(number, lives)
        else:
            print('You lose...')

def continue_game():
    """Asks whether player wants to continue game"""
    return input('Would you like to play again? ("y"/"n")').lower()

def play_game():
    """Executes complete game loop"""
    number = generate_number()
    lives = choose_difficulty()
    makeGuess(number, lives)
    cont = continue_game()
    if cont == "n":
        print('Game over...')
    else:
        play_game()

difficulties = {1: 15, 2: 10, 3: 5}

# Intro
print('Welcome to the Number Guessing Game! ')
play_game()