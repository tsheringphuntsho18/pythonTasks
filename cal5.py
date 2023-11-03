#calculator program
#add
def add_num(x, y):
    sum = x + y
    return sum

#subtract
def subtract_num(x, y):
    subtract = x - y
    return subtract
 
#multiply
def multiply_num(x, y):
    multiply = x * y
    return multiply

#divide
def divide_num(x, y):
    if y == 0:
        print("Cannot divide by 0")
    else:
        divide = x / y
        return divide 
 
#main function
def main_func():
    x = 1
    while x > 0:
        #get user input
        user_input = input("Enter 'e' to exit and 'c' to calculate: ")
        if user_input == 'e' or user_input == 'E':
            print("Thank you")
            break
        elif user_input == "c" or user_input == 'C':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("enter operation + - / *: ")
            if operation == "+":
                result = add_num(num1, num2)
                print("Sum is " ,result)
                print("")               
            elif operation == "-":
                result = subtract_num(num1, num2)
                print("Difference is" ,result)
                print("")
            elif operation == "*":
                result = multiply_num(num1, num2)
                print("Product is" ,result)
                print("")
            elif operation == "/":
                result = divide_num(num1, num2)
                print("Quotient is" ,result)
                print("")
            else:
                print("invalid operation")
        else:
            print('press either e or c')
        x += 1   
main_func()
