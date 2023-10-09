#while loop to count vowel in user name
user_name = input('Enter your name: ')
vowels = 'aeiouAEIOU'
x = 0
count = 0
while x < len(user_name):
    if user_name[x] in vowels:
        count += 1
    x += 1
print('There are ' ,count ,'vowels')
