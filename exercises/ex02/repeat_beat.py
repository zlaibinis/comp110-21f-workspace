"""Repeating a beat in a loop."""

__author__ = "730401304"


# Begin your solution here...
beat_name: str = input("What beat do you want to repeat? ")
beat_count: int = int(input("How many times do you want to repeat it? "))
i: str = ""


if beat_count <= 0:
    print("No beat...")
else:
    while beat_count > 0:
        if beat_count == 1:
            i = i + beat_name
        else:
            i = i + beat_name + " " 
        beat_count = beat_count - 1
    print(i)
