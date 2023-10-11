# checking is the list is sorted or not 
def is_sorted(list):
    if list == sorted(list):
        return True
    else:
        return False
mark = [23,45,67,78,86]
result = is_sorted(mark)
print(result)