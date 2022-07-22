import textwrap
from collections import OrderedDict

x = input("Please, enter a sequence of characters:\n")         # getting a sequence of characters from user

while True:
    # noinspection PyBroadException
    try:
        y = int(input("Please, enter a single digit:\n"))      # getting a number from user and validating it
        break
    except:
        print("You have entered not a single digit...")

rules = [int(y) > 0,                     # conditions to check
         len(x) % int(y) == 0]

if all(rules):           # if all rules are met
    chunks = textwrap.wrap(x, y)         # getting the list of chunks
    length = len(chunks)
    for i in range(length):              # in each chunk print only unique chars
        print(''.join(OrderedDict.fromkeys(chunks[i]).keys()))

else:
    print("Not all conditions are met")
