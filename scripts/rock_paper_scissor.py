from random import randint


def getWinner(player, computer):
    if player == "rock":
        if computer == "scissor":
            return f"You Win!!, {player} Beats {computer}"
        elif computer == "paper":
            return f"You Lose, {computer} Beats {player}"
        else:
            return "Draw"
    elif player == "paper":
        if computer == "rock":
            return f"You Win!!, {player} Beats {computer}"
        elif computer == "scissor":
            return f"You Lose, {computer} Beats {player}"
        else:
            return "Draw"
    elif player == "scissor":
        if computer == "paper":
            return f"You Win!!, {player} Beats {computer}"
        elif computer == "rock":
            return f"You Lose, {computer} Beats {player}"
        else:
            return "Draw"
    else:
        return "Check your spelling"


objs = ["rock", "paper", "scissor"]

computer = objs[randint(0, 2)]

playing = True

while playing:
    player = input("Rock, Paper or Scissor ?    ")
    player = player.lower()
    computer = objs[randint(0, 2)]

    print(getWinner(player, computer))

    key = input("""
    1. To keep Playing Press Enter
    2. To Quit Press input Q
    """)
    if key == "q" or "Q":
        playing = False

print("Thank You For Playing!")
