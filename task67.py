#power
def power(base,exponent):
    square = base ** exponent
    return square
num1 = int(input("Enter base: "))
num2 = int(input("Enter exponent: "))
result = power(num1,num2)
print(num1 ,"raise to" ,num2 ,"is" ,result)
