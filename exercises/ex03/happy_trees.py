"""Drawing forests in a loop."""

__author__ = "730401304"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
i: int = 0
line: int = i + 1
and_one: int = 0
if depth <= 0:
    print("No tree")
else:
    while depth > i:
        oput: str = (TREE + "")
        and_one = i
        while and_one > 0:
            oput = oput + (TREE + "")
            and_one = and_one - 1
        i = i + 1
        print(oput)