import re

text = input("Enter your text: ")                   # text input
positive = input("Enter positive characters: ")     # positive chars input
negative = input("Enter negative characters: ")     # negative chars input


# Scan through string looking for a match to the pattern, returning a Match object
def char_calc(n, a, b):
    c = 0                   # counter
    for i in n:
        if re.search(i, a):  # searching for positive charters
            c = c + 1        # if got match – increase counter by 1 
        if re.search(i, b):  # searching for negative charters
            c = c - 1       # if got match – reduce counter by 1
    return c

print(char_calc(text, positive, negative))  # checking function