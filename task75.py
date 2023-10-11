#find longest word
def find_longest_word(string):
    word = string.split()
    longest_word = " "
    for i in word:
        if len(i) > len(longest_word):
            longest_word = i
    return longest_word
sentence = "My name is tshering "
result = find_longest_word(sentence)
print(result)