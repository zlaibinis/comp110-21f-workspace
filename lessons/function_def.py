"""An example function definition."""

def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a > b:
        return a
    else:
        return b

print(my_max(10 + 1, 10))
print(my_max(-50, 100))

result: int = my_max(-60,150)
print(result)

# x: int = 6
# y: int = 5 + 2
# z: int = my_max(x, y)
#x, y is an expression
# print(z)