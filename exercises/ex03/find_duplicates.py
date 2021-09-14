"""Finding duplicate letters in a word."""

__author__ = "730401304"

word: str = input("Enter a word: ")
dup: bool = False

i: int = 0
while i < len(word):
    char = word[i]
    # print(char)
    j: int = i + 1
    while j < len(word):
        # print(word[j])
        if char == word[j]:
            dup = True
        j += 1
    i += 1

print("Found duplicate: " + str(dup))
