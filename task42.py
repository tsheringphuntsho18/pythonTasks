#while loop
user_name = input('Enter your name: ')
vowels = 'aeiouAEIOU'
index = 0
while index < len(user_name):
    if user_name[index] in vowels:
        print(True)
        break
    index += 1
if index == len(user_name):
    print(False)