#function
user_inputs = int(input('Check, is your number even or odd by entering your number: '))
def is_even(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)
is_even(user_inputs)