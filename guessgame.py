import random
correct_number = random.randint(0,100)

moves = 0
while moves < 10:
    guessed_number = int(input("guess ypour number: "))
    print(guessed_number)

    if guessed_number < correct_number:
        print("your guessed number is smaller than the correct value. try guessing a bigger number")
    elif guessed_number > correct_number:
        print("your guessed number is bigger than the correct value. try guessing a smaller number ")
    else:
        print("won")
        won = True
        break

    moves += 1
if won == False:
    print("you loose")
