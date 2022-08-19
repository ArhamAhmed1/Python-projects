from operator import truediv
from pickle import TRUE
import random

random_number = random.randint(1,100)

moves = 0
print("THIS IS A GUESS GAME AND ONLY 5 MOVES ARE ALLOWED!")
print(" ")

while moves < 5:
    guess_number = int(input("Enter the random int: "))
    won = (guess_number == random_number)
    print(guess_number)
    if guess_number < random_number:
        print("The number guessed is smaller than the random number!")
        print("")
    elif guess_number > random_number:
        print("The guessed number is greater than random number!")
        print("")
    elif guess_number == random_number:
        print("You Won")
        won = True
        break

    moves += 1
if won == False:
    print("5 moves are complete : YOU LOOSE!")

