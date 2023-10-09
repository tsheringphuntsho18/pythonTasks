#score
score = input('Enter game score: ')
if score.isdigit():#score should be only integer
    if score >= '90':
        print('A')
    elif score >= '80':
        print('B')
    elif score >= '70':
        print('C')
    elif score >= '60':
        print('D')
    else:
        print('F')
else:
    print('invalid input')#if user give alphabet input than this line will run

    