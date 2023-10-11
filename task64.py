#find max
def find_max(num):
    max_num = num[0]
    for i in num:
        if i > max_num:
            max_num = i
    return max_num
user_inputs = [5,2,37,9,41,68]
Maximum = find_max(user_inputs)
print(Maximum)
