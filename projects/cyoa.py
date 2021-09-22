"""Project 1: Choose your Own Adventure."""

__author__ = "730401304"

player: str = ""
points: int = 0


def main() -> None:
    """The programs entrypoint."""
    greet()
    global points
    points = points
    print(f"Well welcome to the crew {player}!!!")
    print("Where would you like to go next sailor? You have 3 options. Option 1, you can be captain on the Black Pearl and choose how to deal with trouble over the horizon while gaining Adventure Points. Option 2, you can wager your Adventure Points for double or nothing on a coin toss against Davy Jones. And option 3, you can end the experience right now and walk away with your adventure points. ")
    x: int = int(input("Pick an option by typing either 1, 2 or 3. "))
    if x == 3:
        print(f"Goodbye {player}, you have earned {points} Adventure Points! Safe Travels.")
    if x == 1:
        option_1()
    if x == 2:
        option_2(points)


def greet() -> None:
    """General greeting for player."""
    print("Ahoy matey, you have stumbled across the Pirates of the Carribean adventure story!!! In this experience you will sail the 7 seas and experience a variety of pit stops, where your actions will either make you a legendary pirate or leave you in Davy Jones' Locker. As the story progresses, you will gain adventure points depending on your choices. The more action points you have, the closer you become to being a legendary pirate like Jack Sparrow! All hands to deck!!!")
    global player
    player = input("Now before we begin, what might ye name be sailor? ")


def option_1() -> None:
    """Option used to gain points through story."""
    print(f"Youve been promoted to captain aboard the Black Pearl, {player}!")


def option_2(points: int) -> int:
    print(f"so you chose to gamble your points eh {player}? Best of luck to ye. ")

if __name__ == '__main__':
    main()
