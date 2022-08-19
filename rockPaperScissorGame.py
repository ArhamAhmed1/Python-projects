import random

while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissors: ")

    print("")

    print("player: %s"%player)
    print("computer: %s"%computer)

    print("")

    if computer == player:
        print("its a tie.")
    elif computer == "rock":
        if player == "paper":
            print("player win.")
        elif player == "scissors":
            print("computer wins.")
    elif computer == "paper":
        if player == "rock":
            print("computer wins.")
        elif player == "scissors":
            print("player wins.")
    elif computer == "scissors":
        if player == "rock":
            print("player wins.")
        elif player == "paper":
            print("computer wins.")
            
    play_again = input("play again (y,n): ").lower()
    if play_again != "yes":
        break
print("bye")
