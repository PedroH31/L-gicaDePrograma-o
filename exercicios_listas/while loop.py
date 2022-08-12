import random

number = 28
guesses = 0

while guesses < 10:
    attempt = int(input('Advinhe o numero(entre 1 e 100): '))

    if attempt != number:
        print('Wrong number.')
        guesses += 1
        if attempt >= 40:
            print('Too high.')

        elif attempt <= 18:
            print('Too low.')

    elif attempt == number:
        print('Congratulations! You guessed correctly!')
        break
if guesses == 10:
    print('You ran out of guesses. Better luck next time!')






