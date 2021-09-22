"""Project 1: Choose your Own Adventure."""

__author__ = "730401304"

player: str = ""


def main() -> None:
    """The programs entrypoint."""
    global points
    points = 0
    greet()
    print(player)


def greet() -> None:
    """General greeting for player."""
    print("Ahoy matey, you have stumbled across the Pirates of the Carribean character quiz!!! You will answer Pirates of the Carribean      related questions which will guage what character you are most similar to!!!")
    global player
    player = input("Now before we begin, what might ye name be sailor? ")


if __name__ == '__main__':
    main()
print(points)