#find common element
def find_common_elements(list1,list2):
    new_list = []
    x = 0
    for i in list1:
        for j in list2:
            if i == j:
                new_list.append(i)
                
    return new_list
num1 = [1,2,3,4,5]
num2 = [3,4,5,6,7]
result = find_common_elements(num1,num2)
print(result)       