#for loop to calculate factorial
user_number = int(input('Enter the number: '))
fac = 1
for i in range(1,user_number + 1):
    fac = fac * i
print(fac)