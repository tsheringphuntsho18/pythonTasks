#checking temperature
temperature = float(input('Enter temperature value: '))
if temperature >= 100:
    print('Boiling')
elif temperature >= 32:
    print('Liquid')
else:
    print('Freezing')