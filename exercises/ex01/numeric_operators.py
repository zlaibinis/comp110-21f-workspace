"""Practive with numeric operators, type conversions, and string concatenation."""

__author__ = "730401304"

left_hand_side: str = input("Left-hand side: ")
right_hand_side: str = input("Right-hand side: ")

print(left_hand_side + " ** " + right_hand_side + " is " + str(int(left_hand_side) ** int(right_hand_side)))
print(left_hand_side + " / " + right_hand_side + " is " + str(int(left_hand_side) / int(right_hand_side)))
print(left_hand_side + " // " + right_hand_side + " is " + str(int(left_hand_side) // int(right_hand_side)))
print(left_hand_side + " % " + right_hand_side + " is " + str(int(left_hand_side) % int(right_hand_side)))