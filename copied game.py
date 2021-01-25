import random

print("Here is a guessing game!")
print("Try to guess the number. It is a value from 1-10")

answer = random.randint(1,10)
guess = int(input('Enter your guess: '))
counter = 0

while (guess != answer):
    counter += 1
    if guess < answer:
        print('Your guess is too low!')
    elif guess > answer:
        print('Your guess is too high!')
    guess = int(input('Try again, your new guess: '))
print('Correct!')
