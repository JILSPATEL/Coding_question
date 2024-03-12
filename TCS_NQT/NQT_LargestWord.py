'''

find a longest word present in given stetement

Example:

input:
This is Python Programming

output:
Longest word is Programming having 11 length


'''

str = input("Enter the sentence: ")

words = str.split()

max_length = 0
maxlen_word = ""

for word in words:
    word_length = len(word)

    if word_length > max_length:
        max_length = word_length
        maxlen_word = word

print(f"Longest word is {maxlen_word} having {max_length} length")


# L = str.split()
# m = 0
# for i in L:
#     m = max(m, len(i))
# print(m)
