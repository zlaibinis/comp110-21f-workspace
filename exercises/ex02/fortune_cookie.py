"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730401304"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")

fortune_1: str = "You will take a pleasent journey to a place far away."
fortune_2: str = "A faithful friend is a strong defense."
fortune_3: str = "A lifetime of happiness lies ahead of you."
fortune_4: str = "Each day, compel yourself to do something you would rather not do."

i: int = randint(1, 4)

if i == 2:
    print(fortune_2)
else:
    if i < 2:
        print(fortune_1)
if i == 3:
    print(fortune_3)
else:
    if i > 3:
        print(fortune_4)

print("Now, go spread positive vibes!")