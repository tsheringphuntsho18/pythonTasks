#guessing with while loop
secret_number = 88
x = 1
while x > 0:
    guess = int(input('Guess a number between 1 to 100: '))
    if guess > 88 and guess <= 100:
        print('Your guess is too high')
        print('Guess again')
        print('')
        continue
    elif guess < 88 and guess > 0:
        print('Your guess is too low')
        print('Guess again')
        print('')
        continue
    elif guess == secret_number:
        print('Correct guess it is ' ,secret_number)
        break
    else:
        print('Invalid input')
        print('')
        continue

    