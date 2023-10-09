#for loop to count vowel in user name
user_name = input('Enter your name: ')
vowels = 'aeiouAEIOU'
count = 0
for i in user_name:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i ==  'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        count += 1
print('There are ' ,count ,'vowels')