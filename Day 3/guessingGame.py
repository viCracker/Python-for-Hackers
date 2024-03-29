num = 10
trial = 0
while trial < 3:
    guess = int(input("Guess: "))
    if guess != num:
        print("wrong")
        if trial == 3:
            print("You Lose, Game Over")
        trial += 1
    else:
        print("You win")
        break

        