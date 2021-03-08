# def countLetters(word):
#     counter = {}
#     for letter in word:
#         if letter in counter:
#             counter[letter] += 1
#         else:
#             counter[letter] = 1

#     return counter


# print(countLetters("hello world"))

from collections import Counter

# print(Counter("hello world"))
# print(Counter("hello world").most_common())
print(Counter("hello world").most_common(2))