#Allocating day
day = input('What is today\'s day: ')
Day = day.capitalize()
if Day == 'Monday' or Day == 'Tuesday' or Day == 'Wednesday' or Day =='Thursday':
    print('Weekday')
elif Day == 'Friday':
    print('TGIF')
elif Day == 'Saturday' or Day =='Sunday':
    print('Weekend')
else:
    print('Invalid input')
