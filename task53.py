#calculating multiplication  with for loop
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
num1 = int(input("Enter any number: "))

for i in list:
    result = num1 * i
    print(num1 ,"*" ,i  ,"is" ,result)