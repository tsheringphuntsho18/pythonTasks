#count char
def count_chars(string):
    count = 0
    for i in string:
        count += 1
    return count
word = "tshering phuntsho"
result = count_chars(word)
print(result)