import random

play = {
    "Spock": "🖖",
    "Rock": "👊",
    "Paper": "✋",
    "Scissor": "✌️",
    "Lizard": "🦎"
}
player = str(
    input("Please select: Spock, Rock, Paper, Scissor, Lizard. \nYou play: ")
).title()

if player in play:
    pcPlay = str(random.choice(list(play.keys())))

    print("And the Computer plays: " + pcPlay + "\n" + play[player] + " vs " +
          play[pcPlay])

    if player == "Spock" and (pcPlay == "Scissor" or pcPlay == "Rock"):
        print("You win! xD")
    elif player == "Rock" and (pcPlay == "Lizard" or pcPlay == "Scissor"):
        print("You win! xD  ")
    elif player == "Paper" and (pcPlay == "Rock" or pcPlay == "Spock"):
        print("You win! xD  ")
    elif player == "Scissor" and (pcPlay == "Lizard" or pcPlay == "Paper"):
        print("You win! xD  ")
    elif player == "Lizard" and (pcPlay == "Paper" or pcPlay == "Spock"):
        print("You win! xD  ")
    elif player == pcPlay:
        print("It's a draw =T ")
    else:
        print("You lose =/ ")
else:
    print("You typed an invalid comand, you lose!")
