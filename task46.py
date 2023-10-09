#while loop to calculate factorial
user_number = int(input('Enter any number: '))
fac = 1
while user_number >= 1:
    fac = fac * user_number
    user_number -= 1
print(fac)