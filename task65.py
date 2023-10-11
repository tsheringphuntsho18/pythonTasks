#reverse string
def reverse_string(str):
    stack = []
    for i in str:
        stack.append(i)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string
string = "Tshering Phuntsho"
result = reverse_string(string)
print(result)