"""Project 1: Choose your Own Adventure."""

__author__ = "730401304"


player: str = ""
points: int = 0


def main() -> None:
    """The programs entrypoint."""
    greet()
    global points
    points = points + 1
    print(f"Well welcome to the crew {player}!!!")
    x: int = 0
    while x != 3:
        print("Where would you like to go next sailor? You have 3 options. Option 1, you can be captain on the Black Pearl and choose how to deal with trouble over the horizon while gaining Adventure Points. Option 2, you can wager your Adventure Points for double or nothing on a coin toss against Davy Jones. And option 3, you can end the experience right now and walk away with your adventure points. ")
        x: int = int(input("Pick an option by typing either 1, 2 or 3. "))
        if x == 3:
            print(f"Goodbye {player}, you have earned {points} Adventure Points! Safe Travels.")
            return
        else:
            if x == 1:
                option_1()
            else:
                if x == 2:
                    option_2(x)


def greet() -> None:
    """General greeting for player."""
    print("Ahoy matey, you have stumbled across the Pirates of the Carribean adventure story!!! In this experience you will sail the 7 seas and experience a variety of pit stops, where your actions will either make you a legendary pirate or leave you in Davy Jones' Locker. As the story progresses, you will gain adventure points depending on your choices. The more action points you have, the closer you become to being a legendary pirate like Jack Sparrow! All hands to deck!!!")
    global player
    player = input("Now before we begin, what might ye name be sailor? ")


def option_1() -> None:
    """Option used to gain points through story."""
    print(f"Youve been promoted to captain aboard the Black Pearl, {player}!")


def option_2(x: int) -> int:
    print(f"so you chose to gamble your points for double or nothing against Davy Jones eh {player}? Best of luck to ye. ")
    from random import randint
    global points
    print("You will pick a side of the golden Aztec coin.")
    side: int = int(input("Enter 1 for Heads or 2 for Tails. "))
    coin: int = randint(1, 2)
    if side == coin:
        points *= 2
        print(f"Congrats, you doubled your points captain. {player}, you now have {points} Adventure Points! Davy Jones wants to double down again, this time he is sure you will be walking away with nothing.")
        z: int = int(input("Do you want to bet again? Enter 1 for Yes or 2 for No. "))
        if z == 1:
            side_2: int = int(input("Feeling lucky are ye? Well enter 1 for Heads or 2 for Tails. "))
            if side_2 == coin:
                points *= 2
                print("Well you are one of the luckiest pirates on the seven seas, good job captain!")
            else:
                None
        else:
            None      
    else:
        points = 0
    print(points)
    return points
    

if __name__ == '__main__':
    main()
