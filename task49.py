#Guessing game using for loop
secret_number = 55
print('You will get 5 try')
for i in range(5):
    guess = int(input('Guess a number between 1 to 100: '))
    if  guess == secret_number:
        print('You found a number. It is ' ,secret_number)
        break
    elif guess > 55 and guess <= 100:
        print('Your guess is too high')
        print('Guess again')
        print('')
        continue
    elif guess < 55 and guess > 0:
        print('Your guess is too low')
        print('Guess again')
        print('')
        continue
    else:
        print('Invalid input')
        print('')
        continue

