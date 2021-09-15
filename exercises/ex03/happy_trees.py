"""Drawing forests in a loop."""

__author__ = "730401304"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
i: int = 0
if depth <= 0:
    None
else:
    while depth > i: 
        tree: str = (TREE + "")
        j = i
        while j > 0:
            tree = tree + (TREE + "")
            j = j - 1
        i = i + 1
        print(tree)