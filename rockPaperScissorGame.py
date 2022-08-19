import random

print(" ")
print("A ROCK PAPER SCISSOR GAME")
print(" ")

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
            print("you win.")
        elif player == "scissors":
            print("you loose.")
    elif computer == "paper":
        if player == "rock":
            print("you loose.")
        elif player == "scissors":
            print("you win.")
    elif computer == "scissors":
        if player == "rock":
            print("you win.")
        elif player == "paper":
            print("you loose.")
            
    play_again = input("play again (y,n): ").lower()
    if play_again != "y":
        break
    
print("THANKS FOR PLAYING, BYE!")
