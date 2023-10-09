#Seasons
month = input('What is current month: ')
Month = month.capitalize()
if Month == 'January' or Month == 'February' or Month == 'March' or Month =='April' or Month == 'May':
    print('Spring')
elif Month == 'June' or Month == 'July' or Month == 'August':
    print('Summer')
elif Month == 'September' or Month == 'October' or Month == 'November':
    print('Fall')
elif Month == 'December':
    print('Winter')
else:
    print('Invalid input')
