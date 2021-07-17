import random

def guess(x):
    random_no = random.randint(1, x)
    guess = 0
    while random_no != guess:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_no:
            print('Sorry, guess again. Too low.')
        elif random_no < guess:
            print('Sorry, guess again. Too high.')
    print(f"Congrats! You guessed it right. It's {guess}.")

def guess_computer(x):
    low = 1
    high = x
    feedback = ''
    print(f"Guess a number between {1} and {x}.")
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Computer guessed: {guess}. Is it (L)ow, (H)igh or (C)orrect? ").lower()
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess -1

    print("Yes! Computer guessed it correct.")

guess_computer(100)
