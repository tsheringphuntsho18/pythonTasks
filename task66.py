#calculate_average
def calculate_average(list):
    sum = 0
    count = 0
    for i in list:
        sum += i
        count += 1
    avg = sum / count
    return avg
num = [100,100,100,55,60]
result = calculate_average(num)
print(result)
