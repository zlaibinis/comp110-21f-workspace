"""An exercise in remainders and boolean logic."""

__author__ = "730401304"


# Begin your solution here...
number: int = int(input("Enter an int: "))

if number % 2 == 0 and number % 7 == 0:
    print("TAR HEELS")
else:
    if number % 2 == 0:
        print("TAR")
    if number % 7 == 0:
        print("HEELS")
    else:
        print("CAROLINA")
