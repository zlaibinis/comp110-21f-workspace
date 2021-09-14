"""Drawing forests in a loop."""

__author__ = "730401304"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
i: int = 0
j: int = i + 1

if depth <= 0:
    print("No tree")
else:
    while depth < i:
        print(TREE + "")
        j = j - 1
    i = i + 1