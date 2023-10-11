#multifly list
def multiply_lists(list1,list2):
    new_list = []
    x = 0
    for i in list1:
        index = list2[x]
        multiply = i * index
        new_list.append(multiply)
        x += 1
    return new_list
num1 = [1,2,3]
num2 = [4,5,6]
result = multiply_lists(num1,num2)
print(result)       