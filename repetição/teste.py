import random

start = int(input('Enter the start of the range: '))
end = int(input('Enter the end of the range: '))


if end < start:
    raise ValueError('Please enter a valid number.')

random_number = random.randint(int(start), int(end))
attempts = 0

while True:
    guess = input('Guess a number: ')
    attempts += 1

    try:
        guess = int(guess)

    except ValueError:
        print('Please enter a valid number.')

    if guess == random_number and attempts == 1:
        print(f'You guessed the number in {attempts} attempt')

    if guess == random_number and attempts > 1:
        print(f'You guessed the number in {attempts} attempts')
