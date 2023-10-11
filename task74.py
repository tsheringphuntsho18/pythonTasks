#reverse word
def reverse_word(str):
    separate = words.split()
    reverse = [word[::-1] for word in separate]
    reversed_word = " ".join(reverse)
    return reversed_word
words = "Hello world"
result = reverse_word(words)
print(result)