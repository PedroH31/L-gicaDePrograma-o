import random

while True:
    start = input('Enter the start of the range: ')
    try:
        start = int(start)
        break
    except ValueError:
        print('Please enter a valid number.')

while True:
    end = input('Enter the end of the range: ')
    try:
        end = int(end)
        if end < start:
            raise ValueError('Please enter a valid number.')
        break
    except ValueError:
        print('Please enter a valid number.')


random_number = random.randint(int(start), int(end))
attempts = 0

while True:
    guess = input('Guess a number: ')
    attempts += 1

    try:
        guess = int(guess)

    except ValueError:
        print('Please enter a valid number.')
        attempts -= 1

    if guess == random_number and attempts == 1:
        print(f'You guessed the number in {attempts} attempt')
        break

    if guess == random_number and attempts > 1:
        print(f'You guessed the number in {attempts} attempts')
        break
